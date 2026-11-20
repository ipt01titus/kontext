# Kontext

Kontext verbindet **Objekte, Personen, Aktivitäten, Ziele und Ereignisse**, ohne ihre fachlichen Unterschiede aufzulösen. Projekte und Themengebiete bilden den gemeinsamen Kontext. Eine Person, eine Aufgabe oder ein Objekt bleibt auch bei mehreren Projektzuordnungen ein gemeinsamer Eintrag.

**Stand: 20. November 2026 · Version 0.2.0.** Kontext kann jetzt als lokaler Probebetrieb auf dem Mac starten: Browseroberfläche, dauerhafte SQLite-Speicherung, getrennte eigene und Beispieldaten sowie Sicherungen und Wiederherstellung. Eine produktive Mehrgeräteanwendung ist noch zu entwickeln.

Für das Produkt bestätigt: **MacBook, iPad und iPhone, Offlinearbeit auf allen drei Geräten, automatischer späterer Abgleich und sichtbarer Offline-/Syncstatus.** Der lokale Mac-Pilot ist der vorgezogene erste Schritt; Geräteabgleich und externe Konten sind noch nicht angebunden.

## Auf dem Mac starten

1. Im Projektordner [Kontext-starten.command](Kontext-starten.command) doppelklicken. Python 3.9 oder neuer muss vorhanden sein; zusätzliche Python-Pakete werden nicht benötigt.
2. Kontext öffnet sich unter **http://127.0.0.1:8773/**. Unter „Eigene Daten“ mit eigenen Einträgen beginnen; „Beispieldaten“ ist ein getrennter Bereich.
3. „Lokal gespeichert“ bestätigt die Speicherung auf diesem Mac. Unter „Daten & Sicherungen“ exportieren, sichern oder einen gesicherten Stand wiederherstellen.
4. Zum Beenden [Kontext-beenden.command](Kontext-beenden.command) doppelklicken. Das Schließen des Browserfensters allein beendet den lokalen Dienst nicht.

Der Start funktioniert auch ohne Internet. Der Datenordner `local-data/` bleibt von Quellcodeänderungen getrennt und wird nicht nach GitHub übertragen. Die ausführliche [Anleitung zum Mac-Probebetrieb](docs/betrieb/mac-probebetrieb.md) erklärt Sicherung, Import, Updates und bekannte Grenzen.

## Einstieg

| Frage | Einstieg |
|---|---|
| Was soll das Produkt leisten? | [Vision und Begriffe](docs/produkt/vision-und-begriffe.md) |
| Was ist vereinbart, was noch offen? | [Anforderungskatalog](docs/produkt/anforderungen.md) |
| Wie sind Entitäten und Beziehungen definiert? | [Aktuelles Datenmodell](docs/produkt/datenmodell.md) |
| Was wurde bereits erprobt? | [Implementierungsstand](docs/status.md) |
| Wie starte und sichere ich Kontext auf dem Mac? | [Mac-Probebetrieb](docs/betrieb/mac-probebetrieb.md) |
| Wo kann Kontext laufen und wie teilen Geräte Daten? | [Betrieb und Synchronisation – Diskussionsgrundlage](docs/architektur/betrieb-und-synchronisation.md) |
| Wie geht es weiter? | [Roadmap](docs/planung/roadmap.md) und [GitHub Issues](https://github.com/ipt01titus/kontext/issues) |
| Wo sind die vollständigen bisherigen Unterlagen? | [Referenzunterlagen](docs/referenz/README.md) |

Der bisher veröffentlichte, zugriffsbeschränkte [Oberflächenentwurf](https://kontext-urs-20261118.urs-mueller588623.chatgpt.site/) bleibt als Anschauungsstand bestehen. Eine Änderung in GitHub veröffentlicht diesen Entwurf derzeit nicht automatisch.

## Entwickeln und prüfen

Voraussetzung für die Prüfungen: Node.js 24 und Python 3.9 oder neuer. Es gibt keine npm-Abhängigkeiten und keinen Buildschritt. Der tägliche Pilotbetrieb benötigt Node.js nicht.

```sh
npm run check
npm test
```

Den historischen Entwurf unter `prototype/dist/` bei Bedarf an einer anderen Adresse bereitstellen:

```sh
python3 -m http.server 8774 --bind 127.0.0.1 --directory prototype/dist
```

Anschließend `http://127.0.0.1:8774/` öffnen. Das direkte Öffnen als Datei ist kein verlässlicher Test für Browserpersistenz. Nur dieser historische Entwurf verwendet den festen Demotag 18. November 2026. Die Beispielkontakte sind fiktiv; die Profilanzeige verwendet den Namen des Auftraggebers. Daten des veröffentlichten Entwurfs werden nicht automatisch übernommen.

## Projektstruktur

| Pfad | Inhalt |
|---|---|
| `docs/produkt/` | Fachlicher Kern, Anforderungen und aktuelles Modell |
| `docs/entscheidungen/` | Nachvollziehbare fachliche Entscheidungen |
| `docs/architektur/` | Technische Optionen und noch zu bestätigende Vorschläge |
| `docs/planung/` | Reihenfolge und Abhängigkeiten der nächsten Arbeiten |
| `docs/referenz/` | Vollständige Konzeptstände vom 18. November und Herkunft des Prototyps |
| `prototype/` | Übernommener, getesteter Oberflächenprototyp |
| `app/` | Lokaler Mac-Pilot: Oberfläche, SQLite-Dienst und Starter |
| `tests/` | Prüfungen für Speicherung, Sicherungen und lokale HTTP-Schnittstelle |
| `local-data/` | Eigene Laufzeitdaten und Sicherungen; ignoriert von Git |
| `.github/` | Automatische Prüfungen sowie Vorlagen für Anforderungen, Fehler und Pull Requests |

## Arbeitsweise

Gespräche und Prototypen helfen, Anforderungen zu klären. Bestätigte Ergebnisse werden in den Dokumenten festgehalten; konkrete Arbeitspakete stehen in Issues. Änderungen an der Umsetzung werden mit den betroffenen Anforderungen und geeigneter Prüfung verbunden. Siehe [Mitwirken](CONTRIBUTING.md) und [Hinweise für Entwicklungsassistenten](AGENTS.md).

Die Eintragsnummern innerhalb von Kontext und die GitHub-Issue-Nummern sind getrennte Nummernkreise. GitHub verwaltet die Produktentwicklung; es ist kein Datenspeicher für die späteren Kontakte, Aufgaben oder Termine.

Eine Veröffentlichungslizenz für den Quellcode ist noch nicht festgelegt.
