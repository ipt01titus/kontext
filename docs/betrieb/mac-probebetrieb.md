# Kontext auf dem Mac ausprobieren

Version **0.2.0**, 20. November 2026. Der erste Probebetrieb läuft als Browseranwendung mit lokalem Datenbankdienst auf dem Mac. Für die tägliche Arbeit ist keine Internetverbindung erforderlich.

## Start und Ende

Im Projektordner `Kontext-starten.command` doppelklicken. Der Starter öffnet den Standardbrowser unter **http://127.0.0.1:8773/**. Einen schon laufenden Kontext-Dienst verwendet er erneut. Eine andere Anwendung an derselben Adresse wird nicht beendet.

Zum Beenden `Kontext-beenden.command` doppelklicken. Gespeicherte Einträge bleiben erhalten. Das Browserfenster kann geschlossen werden, ohne den Dienst zu beenden. Nach einem Neustart des Mac den Starter wieder öffnen; ein automatischer Start wurde nicht eingerichtet.

Voraussetzung: Python **3.9 oder neuer** mit Standardbibliothek einschließlich SQLite. Auf dem Entwicklungs-Mac geprüft mit Python 3.9.6 und SQLite 3.43.2. Es sind weder npm-Pakete noch zusätzliche Python-Pakete nötig. Node.js 24 wird nur für Entwicklungsprüfungen benötigt. Der Starter prüft, ob `python3` vorhanden ist; auf einem anderen Mac muss die Laufzeit gegebenenfalls zuerst eingerichtet werden.

## Eigene Daten und Beispiele

„Eigene Daten“ ist ein eigener Bestand mit zunächst nur der Kontaktkarte Urs Müller. Projekte, Objekte, Personen, Aktivitäten, Ziele und Ereignisse können über die vorhandenen Dialoge angelegt und verknüpft werden. Die beispielhaft erprobten Feldumfänge sind noch nicht der vollständige spätere Produktumfang.

„Beispieldaten“ zeigt den bisherigen Entwurf in einem getrennten Arbeitsbereich. Dort können die Beispiele über die Informationsansicht zurückgesetzt werden. Eigene Daten werden dabei nicht verändert. Beide Bereiche haben einen eigenen Nummernkreis; eine Nummer bezeichnet innerhalb des gewählten Bereichs einen Eintrag.

Die Tagessicht verwendet das lokale Datum des Mac. Die ursprünglichen Beispieldaten behalten ihre Beispieltermine; sie werden nicht täglich verschoben.

## Speicherung und Fehler

Die Datenbank liegt in `local-data/kontext.sqlite3`, Sicherungen in `local-data/backups/`. Der Ordner ist von Git ausgeschlossen. Ein Wechsel des Browsers löscht die Datenbank nicht. Ein zweiter Projektordner hat standardmäßig einen anderen Datenordner; den bisherigen Projektordner beim Aktualisieren beibehalten.

„Lokal gespeichert“ wird erst angezeigt, wenn der Datenbankdienst die Speicherung bestätigt hat. Das bedeutet Speicherung auf diesem Mac. Eine Synchronisation mit anderen Geräten gibt es in dieser Version noch nicht.

Ist der lokale Dienst beendet oder das Schreiben nicht möglich, hält ein Dialog die Eingaben im Fenster und bietet einen erneuten Versuch an. Den Starter erneut öffnen und „Erneut versuchen“ wählen. Der Speicherauftrag besitzt eine Kennung, damit eine verlorene Antwort beim Wiederholen keinen doppelten Auftrag erzeugt.

Zusätzlich hält der Browser einen noch nicht bestätigten Auftrag vorübergehend in seinem lokalen Speicher. Dies ist eine Wiederanlaufhilfe, kein Ersatz für die Datenbank. Bei ausgeschaltetem beziehungsweise vollem Browserspeicher kann diese Hilfe ausfallen. Ungespeicherte Eingaben dann vor dem Schließen über den angebotenen Download sichern.

Bitte zunächst **ein Fenster pro Arbeitsbereich** verwenden. Änderungen aus einem veralteten zweiten Fenster werden zurückgewiesen. Die Fassung lässt sich herunterladen; „Gespeicherten Stand laden“ legt sie zusätzlich als gerettete Eingabe im selben Browser ab. Eine automatische Zusammenführung ist noch nicht implementiert.

## Sichern und wiederherstellen

1. „Daten & Sicherungen“ öffnen. „Jetzt sichern“ erstellt eine zusätzliche Sicherung der ganzen Datenbank.
2. „Daten exportieren“ lädt den ausgewählten Arbeitsbereich als lesbare JSON-Datei einschließlich IDs, Nummern, Kommentaren und Beziehungen herunter.
3. Für eine Rückkehr einen Sicherungszeitpunkt wählen, „Wiederherstellen“ und anschließend „Bestätigen“ anklicken. Nur der ausgewählte Arbeitsbereich wird wiederhergestellt; vorher wird der aktuelle Stand erneut gesichert.

Vor **jeder Änderung eines vorhandenen Arbeitsbereichs** erstellt Kontext automatisch eine konsistente Sicherung der gesamten Datenbank über die SQLite-Backup-Funktion. Bei einem Sicherungsfehler findet keine Änderung statt. Die Sicherungen bleiben vorerst vollständig erhalten und können deshalb mit der Nutzung wachsen; eine Aufbewahrungsregel ist noch nicht eingerichtet.

Beim Wiederherstellen bleibt der Nummernzähler mindestens auf seinem höchsten bisherigen Wert. Später angelegte und anschließend zurückgesetzte Einträge führen dadurch nicht zur Wiedervergabe ihrer Nummern. Die wiederhergestellten Einträge behalten ihre vorhandenen Nummern.

Sicherungen im selben Mac-Ordner schützen vor Bearbeitungsfehlern, nicht vor Verlust des Mac. Den Datenordner in die eigene Mac-Sicherung aufnehmen oder regelmäßig JSON-Exporte außerhalb dieses Ordners aufbewahren. Exporte enthalten die fachlichen Daten; entsprechend behandeln.

## Daten übernehmen

Unter „Daten & Sicherungen“ eine Kontext-JSON-Datei auswählen und die Ersetzung des gewählten Bereichs bestätigen. Es entsteht vorher eine Sicherung. Struktur, Referenzen, Nummern und kreisfreie Hierarchien werden geprüft; bei einem Fehler wird nichts ersetzt. Ein gültiger bisheriger Entwurfsbestand im Schema 1 wird migriert, ohne vorhandene gültige IDs und Nummern neu zu vergeben. Fehlende Nummern werden ergänzt.

Wenn unter genau derselben Browseradresse noch `kontext-entwurf-v1` vorliegt, erscheint zusätzlich „Entwurf aus diesem Browser übernehmen“. Der Bestand der veröffentlichten `chatgpt.site`-Adresse ist wegen der Browsertrennung nicht automatisch lesbar. Er wurde nicht automatisch übertragen. Vor einer Übernahme daraus benötigen wir einen Export dieses Bestands.

## Aktualisieren

Den Dienst über `Kontext-beenden.command` beenden, den Quellcode im **bestehenden Projektordner** aktualisieren und den Starter erneut öffnen. Browser neu laden. `local-data/` weder ersetzen noch löschen. Vor einer späteren Datenformatmigration muss eine passende Migration mit Erhalt der Daten implementiert und geprüft werden.

Eine GitHub-Änderung aktualisiert weder den laufenden lokalen Prozess noch den separat veröffentlichten Oberflächenentwurf automatisch. Die derzeitige Version zeigt „Kontext 0.2.0“ im Sicherungsdialog.

## Bekannte Grenzen

- Mac-Pilot für eine Person; keine Benutzerverwaltung oder Freigaben.
- Kein Abgleich mit iPad/iPhone und keine Anzeige eines erfundenen Sync-Erfolgs.
- Kontakte, Kalender und Kommunikationskanäle sind noch nicht angebunden.
- Kontaktfelder, Zielattribute und Beziehungsrollen sind noch nicht vollständig; allgemeine Archivierung und Löschung fehlen.
- Keine installierte native App und kein automatischer Hintergrundstart nach der Anmeldung.
- Vollständige Bestände werden als JSON-Snapshots gespeichert; große Datenmengen und Anhänge sind nicht ausgelegt.

Die [Roadmap](../planung/roadmap.md) ordnet die weiteren Arbeiten ein.
