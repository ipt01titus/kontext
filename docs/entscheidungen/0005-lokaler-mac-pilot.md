# Entscheidung 0005 – Lokaler Mac-Pilot

Status: **Für den vorgezogenen Probebetrieb umgesetzt, 20. November 2026.** Die Mehrgerätearchitektur bleibt offen.

Urs möchte Kontext zunächst auf dem MacBook im Alltag testen und dort weiterentwickeln, bevor iPad und iPhone angeschlossen werden. Dafür wird der vorhandene Oberflächenentwurf unter `app/public/` zu einem lokalen Pilotbetrieb erweitert. `prototype/` bleibt als historischer Referenzstand erhalten.

## Umsetzung

- Ein lokaler Python-Dienst liefert Oberfläche und Datenzugriff ausschließlich an `127.0.0.1`. Python 3.9 oder neuer genügt; zusätzliche Pakete sind nicht erforderlich.
- SQLite speichert pro Arbeitsbereich einen versionierten Gesamtbestand im bisherigen JSON-Format. Dies ist ein überschaubarer Migrationsschritt, kein normalisierter endgültiger Produktdatenvertrag.
- „Eigene Daten“ beginnt mit der eigenen Kontaktkarte; „Beispieldaten“ bleibt ein getrennter Bestand. Der Nummernkreis gilt je Arbeitsbereich.
- Erfolgreiche Schreibantworten folgen erst auf einen Datenbank-Commit. Eine Revisionsprüfung verhindert das stille Überschreiben durch ein zweites Fenster. Eine wiederholte Speicheroperation mit derselben Kennung wird nicht doppelt ausgeführt.
- Vor jeder Änderung eines vorhandenen Bestands entsteht eine konsistente SQLite-Sicherung. Ein Sicherungsfehler verhindert die Änderung. Export und bewusster Import sowie Wiederherstellung sind verfügbar.
- Daten liegen im ignorierten Ordner `local-data/`. Die beiden `.command`-Dateien starten beziehungsweise beenden den Dienst. Updates am Quellcode ersetzen den Bestand nicht.

## Bewusste Grenzen

Ein Fenster pro Arbeitsbereich ist der vorgesehene Pilotbetrieb. Bei konkurrierenden Fassungen wird noch kein automatisches Zusammenführen angeboten; die ungespeicherte Fassung kann separat gesichert werden. Die bestätigten späteren Regeln aus [Entscheidung 0004](0004-synchronisationskonflikte.md) bleiben bestehen.

Es gibt keinen Geräteabgleich, keine Anmeldung, keine externe Kontoanbindung und keinen Autostart nach der Mac-Anmeldung. Andere Geräte können diesen Dienst nicht erreichen. Der lokale Dienst läuft ohne Internet weiter; ein beendeter Dienst muss erneut gestartet werden.

Für eine spätere Synchronisation müssen Datensätze und Ergänzungen eigene Änderungsinformationen erhalten. Der Snapshot-Speicher ersetzt dieses Konzept nicht. Der Pilot bewahrt vorhandene Identitäten, Nummern und Beziehungen und bietet einen vollständigen Export als Grundlage weiterer Migrationen.

Die [Betriebsanleitung](../betrieb/mac-probebetrieb.md) beschreibt Start, Sicherung und Einschränkungen. Umsetzung zu [Issue #11](https://github.com/ipt01titus/kontext/issues/11).
