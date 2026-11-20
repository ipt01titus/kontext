"""Loopback-only local application server; no third-party packages or network services."""
import argparse
import hashlib
import json
import os
import signal
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, parse_qs
from app.storage import Store, Invalid, Conflict

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / 'app' / 'public'
VERSION = '0.2.0'
ASSETS = {'index.html':'text/html', 'app.js':'text/javascript', 'model.js':'text/javascript',
          'storage.js':'text/javascript', 'styles.css':'text/css', 'hierarchy.css':'text/css', 'pilot.css':'text/css'}

def identity(directory):
    return hashlib.sha256((str(ROOT) + '\0' + str(Path(directory).resolve())).encode()).hexdigest()[:24]

def make_server(directory, port=8773):
    store = Store(directory)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            # Request bodies, data and query values are deliberately not logged.
            pass

        def respond(self, status, value, mime='application/json', attachment=None):
            body = json.dumps(value, ensure_ascii=False).encode() if mime == 'application/json' else value
            self.send_response(status)
            self.send_header('Content-Type', mime + '; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
            if attachment:
                self.send_header('Content-Disposition', 'attachment; filename="' + attachment + '"')
            self.end_headers()
            self.wfile.write(body)

        def host_ok(self):
            return self.headers.get('Host') == '127.0.0.1:' + str(self.server.server_port)

        def do_GET(self):
            try:
                if not self.host_ok():
                    return self.respond(403, dict(error='Unzulässige lokale Adresse.'))
                url = urlsplit(self.path)
                query = parse_qs(url.query)
                workspace = query.get('workspace', ['own'])[0]
                if url.path == '/api/health':
                    return self.respond(200, dict(app='kontext-local', version=VERSION, instance=identity(directory)))
                if url.path == '/api/state':
                    return self.respond(200, store.load(workspace))
                if url.path == '/api/backups':
                    return self.respond(200, dict(backups=store.list_backups()))
                if url.path == '/api/export':
                    from app.storage import timestamp
                    return self.respond(200, dict(format='kontext-export-v1', version=VERSION, workspace=workspace, exportedAt=timestamp(), data=store.load(workspace)['state']), attachment='kontext-' + workspace + '.json')
                name = 'index.html' if url.path == '/' else url.path.lstrip('/')
                if name in ASSETS:
                    return self.respond(200, (PUBLIC / name).read_bytes(), ASSETS[name])
                self.respond(404, dict(error='Nicht gefunden.'))
            except (Invalid, ValueError) as error:
                self.respond(400, dict(error=str(error)))
            except Exception:
                self.respond(500, dict(error='Der lokale Datenbestand konnte nicht gelesen werden. Bitte den Starter erneut öffnen.'))

        def do_POST(self):
            try:
                origin = 'http://127.0.0.1:' + str(self.server.server_port)
                if not self.host_ok() or self.headers.get('Origin') != origin or self.headers.get('X-Kontext-Client') != '1':
                    return self.respond(403, dict(error='Dieser Auftrag muss aus Kontext selbst kommen.'))
                if self.headers.get_content_type() != 'application/json':
                    return self.respond(415, dict(error='JSON erforderlich.'))
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 10 * 1024 * 1024:
                    return self.respond(413, dict(error='Ungültige oder zu große Datei (maximal 10 MB).'))
                request = json.loads(self.rfile.read(length))
                if not isinstance(request, dict):
                    raise Invalid('Ungültiger Auftrag.')
                path = urlsplit(self.path).path
                name = request.get('workspace', 'own')
                if path in ('/api/state', '/api/import'):
                    result = store.save(name, request.get('state'), request.get('revision'), request.get('operationId'), replace=path == '/api/import')
                    return self.respond(200, result)
                if path == '/api/backup':
                    return self.respond(200, dict(name=store.backup()))
                if path == '/api/restore':
                    return self.respond(200, store.restore(name, request.get('name'), request.get('revision'), request.get('operationId')))
                if path == '/api/shutdown':
                    self.respond(200, dict(stopped=True))
                    threading.Thread(target=self.server.shutdown, daemon=True).start()
                    return
                self.respond(404, dict(error='Nicht gefunden.'))
            except Conflict as error:
                self.respond(409, dict(error=str(error)))
            except (Invalid, ValueError, TypeError, RecursionError) as error:
                self.respond(400, dict(error=str(error) or 'Ungültiger Auftrag.'))
            except Exception:
                self.respond(500, dict(error='Speichern fehlgeschlagen. Deine Eingaben bleiben für einen erneuten Versuch erhalten. Prüfe den lokalen Dienst und freien Speicher.'))
    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    server.daemon_threads = False
    server.store = store
    return server

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', default=str(ROOT / 'local-data'))
    parser.add_argument('--port', type=int, default=8773)
    args = parser.parse_args()
    os.umask(0o077)
    # A single process owns a data directory, including when the port changes.
    import fcntl
    directory = Path(args.data_dir).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    lock = (directory / 'service.lock').open('a')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        raise SystemExit('Kontext läuft für diesen Datenordner bereits.')
    server = make_server(directory, args.port)
    (directory / 'service.json').write_text(json.dumps(dict(pid=os.getpid(), port=server.server_port, instance=identity(directory))))
    def stop(*_):
        threading.Thread(target=server.shutdown, daemon=True).start()
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    print('Kontext ' + VERSION + ' · http://127.0.0.1:' + str(server.server_port), flush=True)
    try:
        server.serve_forever(poll_interval=0.2)
    finally:
        server.server_close()
        lock.close()

if __name__ == '__main__':
    main()
