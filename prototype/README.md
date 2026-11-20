# Kontext – Oberflächenentwurf

Interaktiver Browser-Prototyp mit Beispieldaten für die verknüpfte Organisation von Objekten, Personen, Aktivitäten, Zielen und Ereignissen.

Die Beispielwoche beginnt am 16. November 2026. Startpunkt ist Mittwoch, der 18. November 2026.

## Ausprobieren

- Tagessicht mit Terminen, Aktivitäten und Wiedervorlagen
- Personenansicht mit gemeinsamen Zielen und ausstehenden Rückmeldungen
- Aktivitäten als Liste und Kanban; Schritte, Kommentare und Abhängigkeiten
- Projekt- und Objektübersicht, insbesondere das Gartenhaus mit Bestandteilen
- Gemeinsame Zielansicht einschließlich Opportunities
- Kalender mit Terminbezügen und Vorbereitungsaktivitäten
- Suche über alle fünf Entitäten; Tastenkürzel Strg/Cmd+K
- Anlage und Bearbeitung von Einträgen; lokale Speicherung im Browser
- Objektanlage direkt im Aktivitätsdialog, ohne den Aktivitätsentwurf zu verlieren
- Aufklappbare Objekt- und Projektbäume mit Suche und Strukturpfaden
- Projektfilter schließen Unterprojekte ein; Zuordnungen bleiben am gewählten Projekt
- „Mein Leben“ mit den zwölf persönlichen Bereichen aus dem Referenzbild
- Ein gemeinsamer Nummernkreis über alle Einträge einschließlich Projekten; Suche mit `#42` oder `42`

Die Personen und Kontaktdaten der Beispieldaten sind fiktiv. Der Prototyp enthält keine externen Konten oder aktiven Kommunikationsanbindungen. Statusdarstellung, Wiedervorlagen und die Ausgestaltung der Schritte sind Interaktionsvorschläge für die gemeinsame Abstimmung. Kontaktfelder zeigen den Grundaufbau; der vollständige Kontaktimport ist noch nicht implementiert.

Statische Dateien liegen in `dist/`. Es ist kein Build erforderlich.

## Daten und Bedienung

Der Speicher bleibt `kontext-entwurf-v1`. Vorhandene Einträge, IDs, Beziehungen und Kommentare werden beim Upgrade erhalten. Der Strukturaufbau wird einmalig ergänzt. Nummern werden einmal vergeben und bei Bearbeitung oder Projektwechsel nicht geändert. Der Nummernkreis gilt für den jeweiligen Browserdatenbestand; eine gemeinsame Vergabe über mehrere Geräte benötigt die spätere zentrale Datenhaltung. Projekthierarchien und Objektstruktur haben jeweils höchstens einen übergeordneten Eintrag; Kreisbeziehungen werden verhindert.

Die Oberfläche ist mit beschrifteten Formularen, semantischen Schaltflächen und Tastatursuche über Browsersteuerung bedienbar. Agenten können sie bei verfügbarem Browserzugriff bedienen. Es gibt noch keine serverseitige Datenbank, keine authentifizierte Programmschnittstelle und keine Ausführung bei geschlossenem Browser.

## Entwicklungsstand und Wiederaufnahme

Stand 20. November 2026: Die zuvor unterbrochene Änderung war nicht gespeichert. Die Fortsetzung ergänzt Hierarchien, Inline-Objektanlage und Nummerierung. Entwicklung und Veröffentlichung erfolgen weiter im bestehenden Site-Projekt aus `.openai/hosting.json`; die Freigabe bleibt auf den Eigentümer beschränkt.

Prüfung: `node --check dist/app.js` und `node --test tests/model.test.cjs`. Die Modelltests sichern Datenmigration, Erhalt eigener Daten, wiederholbare Migration, hierarchische Filter und stabile Nummern. Zusätzlich wurden Objektanlage samt Abbruch, Erhalt des Aktivitätsentwurfs, dreistufige Bäume, Projektverschiebung und Umbenennung sowie Nummernsuche im Browser geprüft, einschließlich Mobilansicht bei 390 Pixeln.

Bei einer erneuten Unterbrechung zuerst Arbeitsumgebung und Git-Status prüfen, dann den veröffentlichten Versionsstand abgleichen. Änderungen sind erst nach erfolgreicher Quellsicherung, Prüfungen und Veröffentlichung abgeschlossen. Die lokale Mac-Arbeitsumgebung muss für diese Entwicklungsform verbunden und erreichbar sein.

Nächster fachlicher Ausbau: zentrale Datenhaltung und authentifizierte Schnittstelle für gemeinsame Nutzung und eigenständige Agentenarbeit; danach echte Kalender-, Kontakt- und Kommunikationsanbindungen. Der aktuelle Stand bleibt ein interaktiver Entwurf.
