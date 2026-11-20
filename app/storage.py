"""Transactional local snapshots with revision checks and consistent SQLite backups."""
import hashlib
import json
import os
import re
import sqlite3
import threading
import uuid
from datetime import datetime, date, timezone
from pathlib import Path

COLLECTIONS = ('projects', 'people', 'objects', 'tasks', 'goals', 'events')
TARGETS = dict(zip(('project', 'person', 'object', 'task', 'goal', 'event'), COLLECTIONS))
IDENTIFIER = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{0,159}$')

class Invalid(ValueError):
    pass

class Conflict(Exception):
    pass

def timestamp():
    return datetime.now(timezone.utc).isoformat()

def validate(state):
    if not isinstance(state, dict) or state.get('schema') != 1:
        raise Invalid('Unbekanntes Datenformat. Erwartet wird ein Kontext-Datenbestand der Version 1.')
    known, numbers = {}, set()
    for key in COLLECTIONS:
        rows = state.get(key)
        if not isinstance(rows, list) or len(rows) > 20000:
            raise Invalid('Ungültige Eintragsliste: ' + key)
        known[key] = {}
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get('id'), str) or not IDENTIFIER.fullmatch(row['id']):
                raise Invalid('Ungültige interne Eintragskennung.')
            if row['id'] in known[key]:
                raise Invalid('Doppelte interne Eintragskennung.')
            if not isinstance(row.get('name'), str) or not row['name'].strip():
                raise Invalid('Ein Eintrag benötigt einen Namen.')
            number = row.get('number')
            if type(number) is not int or number < 1 or number in numbers:
                raise Invalid('Eintragsnummern müssen positiv und eindeutig sein.')
            numbers.add(number)
            known[key][row['id']] = row
    if 'urs' not in known['people']:
        raise Invalid('Die eigene Kontaktkarte fehlt.')
    if type(state.get('nextNumber')) is not int or state['nextNumber'] <= max(numbers, default=0):
        raise Invalid('Der Nummernzähler liegt unter bereits vergebenen Nummern.')

    def refs(row, field, collection):
        values = row.get(field, [])
        if not isinstance(values, list) or any(not isinstance(v, str) or v not in known[collection] for v in values):
            raise Invalid('Ungültige Verbindung: ' + field)
        return values

    def dates(row, fields):
        for field in fields:
            value = row.get(field, '')
            if value:
                try:
                    if not isinstance(value, str) or date.fromisoformat(value).isoformat() != value:
                        raise ValueError()
                except (ValueError, TypeError):
                    raise Invalid('Ungültiges Datum: ' + field)

    for key in COLLECTIONS:
        for row in state[key]:
            refs(row, 'projects', 'projects')
            if not isinstance(row.get('comments', []), list):
                raise Invalid('Ungültige Kommentare.')
            for comment in row.get('comments', []):
                if not isinstance(comment, dict) or not isinstance(comment.get('text'), str) or comment.get('author') not in known['people']:
                    raise Invalid('Ungültiger Kommentar oder Urheber.')
                try:
                    datetime.fromisoformat(comment['at'].replace('Z', '+00:00'))
                except (ValueError, TypeError, KeyError, AttributeError):
                    raise Invalid('Ungültiger Kommentarzeitpunkt.')
            if key in ('projects', 'objects'):
                parent = row.get('parent')
                if parent is not None and parent not in known[key]:
                    raise Invalid('Übergeordneter Eintrag fehlt.')
            if key == 'projects' and not re.fullmatch(r'#[0-9a-fA-F]{6}', row.get('color', '')):
                raise Invalid('Ungültige Projektfarbe.')
            if key == 'people':
                if row.get('trust') is not None and (type(row['trust']) not in (int, float) or not 0 <= row['trust'] <= 100):
                    raise Invalid('Vertrauenslevel muss zwischen 0 und 100 liegen.')
                for field in ('emails', 'phones'):
                    if not isinstance(row.get(field, []), list) or any(not isinstance(v, dict) or not isinstance(v.get('value'), str) for v in row.get(field, [])):
                        raise Invalid('Ungültige Kontaktdaten.')
                if not isinstance(row.get('extra', {}), dict):
                    raise Invalid('Ungültige Kontaktzusatzfelder.')
            if key == 'tasks':
                if row.get('status') not in ('open', 'progress', 'done', 'cancelled'):
                    raise Invalid('Unbekannter Aktivitätsstatus.')
                if row.get('owner') not in known['people']:
                    raise Invalid('Verantwortliche Person fehlt.')
                for field, target in (('goals','goals'), ('waiting','people'), ('predecessors','tasks')):
                    refs(row, field, target)
                targets = row.get('targets', [])
                if not isinstance(targets, list) or any(not isinstance(v, dict) or v.get('type') not in ('object','person','event') or v.get('id') not in known[TARGETS[v['type']]] for v in targets):
                    raise Invalid('Ungültiger fachlicher Aktivitätsbezug.')
                if not isinstance(row.get('steps', []), list) or any(not isinstance(v, dict) or not isinstance(v.get('text'), str) or type(v.get('done')) is not bool for v in row.get('steps', [])):
                    raise Invalid('Ungültige Aktivitätsschritte.')
                dates(row, ('due', 'followUp', 'workOn'))
            if key in ('goals', 'events', 'objects'):
                refs(row, 'people', 'people')
            if key in ('goals', 'events'):
                refs(row, 'objects', 'objects')
            if key == 'goals':
                if not isinstance(row.get('criteria', []), list) or any(not isinstance(v, str) for v in row.get('criteria', [])):
                    raise Invalid('Ungültige Erfolgskriterien.')
                dates(row, ('targetDate', 'decisionDate'))
            if key == 'events':
                refs(row, 'goals', 'goals'); refs(row, 'tasks', 'tasks')
                dates(row, ('date', 'endDate'))
                if not row.get('date'):
                    raise Invalid('Ein Ereignis benötigt ein Datum.')
                end_date = row.get('endDate') or row['date']
                if end_date < row['date']:
                    raise Invalid('Das Enddatum liegt vor dem Startdatum.')
                for field in ('start', 'end'):
                    if row.get(field) and not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d', row[field]):
                        raise Invalid('Ungültige Uhrzeit.')
                if end_date == row['date'] and row.get('start') and row.get('end') and row['end'] < row['start']:
                    raise Invalid('Das Ende liegt vor dem Beginn.')
            if key == 'objects':
                if not isinstance(row.get('links', []), list):
                    raise Invalid('Ungültige Objektverbindungen.')
                for link in row.get('links', []):
                    if not isinstance(link, dict) or link.get('id') not in known['objects'] or not isinstance(link.get('type'), str):
                        raise Invalid('Ungültige Objektverbindung.')

    def acyclic(key, edges):
        finished, visiting = set(), set()
        def visit(identifier):
            if identifier in visiting:
                raise Invalid('Diese Verbindung würde einen Kreis erzeugen.')
            if identifier in finished:
                return
            visiting.add(identifier)
            for target in edges(known[key][identifier]):
                visit(target)
            visiting.remove(identifier); finished.add(identifier)
        for identifier in known[key]:
            visit(identifier)
    for key in ('projects', 'objects'):
        acyclic(key, lambda row: [row['parent']] if row.get('parent') else [])
    acyclic('tasks', lambda row: row.get('predecessors', []))
    return state

class Store:
    def __init__(self, directory):
        self.directory = Path(directory).resolve()
        self.directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.backups = self.directory / 'backups'
        self.backups.mkdir(exist_ok=True, mode=0o700)
        self.path = self.directory / 'kontext.sqlite3'
        self.lock = threading.RLock()
        with self.connect() as db:
            db.executescript('''CREATE TABLE IF NOT EXISTS workspaces (
                name TEXT PRIMARY KEY, revision INTEGER NOT NULL, state TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS operations (
                workspace TEXT NOT NULL, operation_id TEXT NOT NULL, digest TEXT NOT NULL,
                PRIMARY KEY (workspace, operation_id));''')
        os.chmod(self.path, 0o600)

    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.execute('PRAGMA synchronous=FULL')
        return db

    @staticmethod
    def workspace(name):
        if name not in ('own', 'demo'):
            raise Invalid('Unbekannter Arbeitsbereich.')

    def load(self, name):
        self.workspace(name)
        with self.lock, self.connect() as db:
            row = db.execute('SELECT revision,state,updated_at FROM workspaces WHERE name=?', (name,)).fetchone()
            return dict(revision=row[0], state=json.loads(row[1]), updatedAt=row[2]) if row else dict(revision=0, state=None, updatedAt=None)

    def _backup(self):
        filename = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '-' + uuid.uuid4().hex[:6] + '.sqlite3'
        target = self.backups / filename
        try:
            with self.connect() as source, sqlite3.connect(target) as dest:
                source.backup(dest)
            os.chmod(target, 0o600)
        except Exception:
            target.unlink(missing_ok=True)
            raise
        return filename

    def backup(self):
        with self.lock:
            return self._backup()

    def list_backups(self):
        with self.lock:
            return [dict(name=p.name, size=p.stat().st_size, at=datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).isoformat()) for p in sorted(self.backups.glob('*.sqlite3'), reverse=True)]

    def save(self, name, state, revision, operation_id, replace=False):
        self.workspace(name); validate(state)
        if type(revision) is not int or revision < 0 or not isinstance(operation_id, str) or not IDENTIFIER.fullmatch(operation_id):
            raise Invalid('Ungültiger Speicherauftrag.')
        encoded = json.dumps(state, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)
        digest = hashlib.sha256(encoded.encode()).hexdigest()
        with self.lock, self.connect() as db:
            old = db.execute('SELECT digest FROM operations WHERE workspace=? AND operation_id=?', (name, operation_id)).fetchone()
            if old:
                if old[0] != digest:
                    raise Invalid('Ein Speicherauftrag wurde mit anderem Inhalt wiederverwendet.')
                return self.load(name)
            current = self.load(name)
            if current['revision'] != revision:
                raise Conflict('Der Datenbestand wurde in einem anderen Fenster geändert. Deine Fassung bleibt zur Sicherung erhalten.')
            if current['state'] and state['nextNumber'] < current['state']['nextNumber']:
                raise Invalid('Der Nummernzähler darf beim Bearbeiten nicht zurückgesetzt werden.')
            if current['state'] and not replace:
                for key in COLLECTIONS:
                    existing = {x['id']: x['number'] for x in current['state'][key]}
                    if any(x['id'] in existing and existing[x['id']] != x['number'] for x in state[key]):
                        raise Invalid('Bereits vergebene Eintragsnummern dürfen nicht geändert werden.')
            if current['state']:
                self._backup()
            with db:
                db.execute('BEGIN IMMEDIATE')
                fresh = db.execute('SELECT revision FROM workspaces WHERE name=?', (name,)).fetchone()
                if (fresh[0] if fresh else 0) != revision:
                    raise Conflict('Der Datenbestand wurde inzwischen geändert.')
                db.execute('INSERT OR REPLACE INTO workspaces VALUES(?,?,?,?)', (name, revision + 1, encoded, timestamp()))
                db.execute('INSERT INTO operations VALUES(?,?,?)', (name, operation_id, digest))
            return self.load(name)

    def restore(self, name, filename, revision, operation_id):
        self.workspace(name)
        if not isinstance(filename, str) or not re.fullmatch(r'\d{8}T\d{12}Z-[a-f0-9]{6}\.sqlite3', filename):
            raise Invalid('Ungültiger Sicherungsname.')
        path = self.backups / filename
        if not path.is_file():
            raise Invalid('Sicherung nicht gefunden.')
        with self.lock, sqlite3.connect('file:' + str(path) + '?mode=ro', uri=True) as db:
            row = db.execute('SELECT state FROM workspaces WHERE name=?', (name,)).fetchone()
            if not row:
                raise Invalid('Dieser Arbeitsbereich ist in der Sicherung nicht enthalten.')
            state = json.loads(row[0]); current = self.load(name)
            if current['state']:
                state['nextNumber'] = max(state['nextNumber'], current['state']['nextNumber'])
            return self.save(name, state, revision, operation_id, replace=True)
