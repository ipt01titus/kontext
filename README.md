# Kontext

Kontext verbindet **Objekte, Personen, Aktivitäten, Ziele und Ereignisse**, ohne ihre fachlichen Unterschiede aufzulösen. Projekte und Themengebiete bilden den gemeinsamen Kontext. Eine Person, eine Aufgabe oder ein Objekt bleibt auch bei mehreren Projektzuordnungen ein gemeinsamer Eintrag.

**Stand: 20. November 2026.** Dieses Repository führt das Fachkonzept, die Entscheidungen, den bestehenden Oberflächenprototyp und die nächsten Arbeitspakete zusammen. Der Prototyp ist ein Interaktionsentwurf mit lokaler Browserspeicherung. Eine produktive Mehrgeräteanwendung ist noch zu entwickeln.

## Einstieg

| Frage | Einstieg |
|---|---|
| Was soll das Produkt leisten? | [Vision und Begriffe](docs/produkt/vision-und-begriffe.md) |
| Was ist vereinbart, was noch offen? | [Anforderungskatalog](docs/produkt/anforderungen.md) |
| Wie sind Entitäten und Beziehungen definiert? | [Aktuelles Datenmodell](docs/produkt/datenmodell.md) |
| Was wurde bereits erprobt? | [Implementierungsstand](docs/status.md) |
| Wo kann Kontext laufen und wie teilen Geräte Daten? | [Betrieb und Synchronisation – Diskussionsgrundlage](docs/architektur/betrieb-und-synchronisation.md) |
| Wie geht es weiter? | [Roadmap](docs/planung/roadmap.md) und [GitHub Issues](https://github.com/ipt01titus/kontext/issues) |
| Wo sind die vollständigen bisherigen Unterlagen? | [Referenzunterlagen](docs/referenz/README.md) |

Der bisher veröffentlichte, zugriffsbeschränkte [Oberflächenentwurf](https://kontext-urs-20261118.urs-mueller588623.chatgpt.site/) bleibt als Anschauungsstand bestehen. Eine Änderung in GitHub veröffentlicht diesen Entwurf derzeit nicht automatisch.

## Prototyp lokal ausprobieren

Voraussetzung für die Prüfungen: Node.js 24. Es gibt keine npm-Abhängigkeiten und keinen Buildschritt.

```sh
npm run check
npm test
```

Die Dateien unter `prototype/dist/` mit einem lokalen HTTP-Server bereitstellen, beispielsweise mit installiertem Python 3:

```sh
python3 -m http.server 8773 --bind 127.0.0.1 --directory prototype/dist
```

Anschließend `http://127.0.0.1:8773/` öffnen. Das direkte Öffnen als Datei ist kein verlässlicher Test für Browserpersistenz. Die Beispielwoche startet am 16. November 2026; der Demotag ist der 18. November. Die Beispielkontakte sind fiktiv; die Profilanzeige verwendet den Namen des Auftraggebers. Die Daten eines anderen Browsers oder des veröffentlichten Entwurfs werden nicht automatisch übernommen.

## Projektstruktur

| Pfad | Inhalt |
|---|---|
| `docs/produkt/` | Fachlicher Kern, Anforderungen und aktuelles Modell |
| `docs/entscheidungen/` | Nachvollziehbare fachliche Entscheidungen |
| `docs/architektur/` | Technische Optionen und noch zu bestätigende Vorschläge |
| `docs/planung/` | Reihenfolge und Abhängigkeiten der nächsten Arbeiten |
| `docs/referenz/` | Vollständige Konzeptstände vom 18. November und Herkunft des Prototyps |
| `prototype/` | Übernommener, getesteter Oberflächenprototyp |
| `.github/` | Automatische Prüfungen sowie Vorlagen für Anforderungen, Fehler und Pull Requests |

## Arbeitsweise

Gespräche und Prototypen helfen, Anforderungen zu klären. Bestätigte Ergebnisse werden in den Dokumenten festgehalten; konkrete Arbeitspakete stehen in Issues. Änderungen an der Umsetzung werden mit den betroffenen Anforderungen und geeigneter Prüfung verbunden. Siehe [Mitwirken](CONTRIBUTING.md) und [Hinweise für Entwicklungsassistenten](AGENTS.md).

Die Eintragsnummern innerhalb von Kontext und die GitHub-Issue-Nummern sind getrennte Nummernkreise. GitHub verwaltet die Produktentwicklung; es ist kein Datenspeicher für die späteren Kontakte, Aufgaben oder Termine.

Eine Veröffentlichungslizenz für den Quellcode ist noch nicht festgelegt.
