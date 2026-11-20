"""Start/stop the local service without installing packages."""
import argparse
import json
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from app.server import identity

def health(url):
    try:
        with urllib.request.urlopen(url + '/api/health', timeout=0.8) as response:
            return json.load(response)
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start','stop','status'])
    parser.add_argument('--data-dir', default=str(ROOT / 'local-data'))
    parser.add_argument('--port', type=int, default=8773)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    directory = Path(args.data_dir).resolve()
    url = 'http://127.0.0.1:' + str(args.port)
    expected = identity(directory)
    current = health(url)
    if current and (current.get('app') != 'kontext-local' or current.get('instance') != expected):
        raise SystemExit('An dieser lokalen Adresse läuft eine andere Anwendung. Sie wurde nicht verändert.')
    if args.action == 'status':
        print('Kontext läuft: ' + url if current else 'Kontext ist beendet.')
        return
    if args.action == 'stop':
        if current:
            request = urllib.request.Request(url + '/api/shutdown', data=b'{}', headers={'Origin':url,'X-Kontext-Client':'1','Content-Type':'application/json'}, method='POST')
            with urllib.request.urlopen(request, timeout=3):
                pass
            for _ in range(30):
                if not health(url):
                    break
                time.sleep(0.1)
            else:
                raise SystemExit('Kontext beendet sich noch. Bitte den Status vor einem erneuten Start prüfen.')
        print('Kontext wurde beendet. Gespeicherte Daten bleiben erhalten.')
        return
    if not current:
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        with (directory / 'service.log').open('ab') as log:
            child = subprocess.Popen([sys.executable, '-m', 'app.server', '--data-dir', str(directory), '--port', str(args.port)], cwd=ROOT, stdout=log, stderr=log, start_new_session=True)
        for _ in range(80):
            current = health(url)
            if current and current.get('instance') == expected:
                break
            if child.poll() is not None:
                raise SystemExit('Kontext konnte nicht starten. Hinweise stehen in local-data/service.log; möglicherweise ist die Adresse bereits belegt.')
            time.sleep(0.1)
        else:
            raise SystemExit('Der Start dauert länger als erwartet. Bitte den Starter erneut öffnen.')
    print('Kontext läuft lokal auf diesem Mac: ' + url)
    print('Eigene Daten und Sicherungen: ' + str(directory))
    if not args.no_browser:
        webbrowser.open(url)

if __name__ == '__main__':
    main()
