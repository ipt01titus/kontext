# Implementierungsstand

Stand: 20. November 2026 · Version 0.2.0. `app/` enthält den vorgezogenen lokalen Mac-Pilot mit SQLite-Speicherung und Sicherungen. Der historische Entwurf unter `prototype/dist/` bleibt erhalten; nur dieser speichert ausschließlich im Browser und verwendet den festen Demotag 18. November.

## Lokaler Mac-Pilot

- Doppelklick-Starter und Beenden über die beiden `.command`-Dateien; lokaler Python-Dienst auf `127.0.0.1:8773`.
- Eigene Daten und Beispieldaten getrennt, aktuelle lokale Tagesanzeige.
- Dauerhafte SQLite-Snapshots; bestätigte Speicherung, Revisionsschutz gegen Überschreiben und wiederholbare Speicheraufträge nach verlorener Antwort.
- Automatische konsistente Sicherung vor Änderungen; manuelle Sicherung, JSON-Export/Import und Wiederherstellung mit vorheriger Sicherheitssicherung.
- Laufzeitdaten außerhalb der Produktdateien und von Git ausgeschlossen. Kein Geräteabgleich oder externer Dienst erforderlich.
- Im Personendialog ein neues Projekt beziehungsweise einen Kontext direkt anlegen und zusätzlich auswählen. Bereits eingegebene Kontaktdaten und gewählte Projekte bleiben beim Anlegen oder Abbrechen erhalten; der neue Kontext wird unabhängig von der Person gespeichert. Umsetzung zu [Issue #13](https://github.com/ipt01titus/kontext/issues/13).
- Nicht mehr relevante Aktivitäten als „Abgebrochen“ führen und wieder öffnen. Sie zählen nicht zur offenen Arbeit, bleiben über Filter, Gesamtübersicht und Suche auffindbar und erhalten Nummer, Kommentare, Schritte und Beziehungen. Eine abgebrochene Vorbedingung bleibt unerfüllt. Umsetzung zu [Issue #15](https://github.com/ipt01titus/kontext/issues/15); nach diesem Update den lokalen Dienst einmal beenden und neu starten, damit die neue Statusvalidierung geladen wird.
- Für die tatsächlich noch verwendete Testansicht auf Port 8775 gibt es `Kontext-Testbetrieb-neustarten.command`. Sie sichert und erhält denselben Bestand und startet den richtigen Dienst neu; die normalen Dateien steuern nur Port 8773. Fehlgeschlagene Aktionen werden im geöffneten Dialog sichtbar erklärt.
- Mehrtägige Ereignisse mit Startdatum und optionalem Enddatum; Wochenansicht Montag bis Sonntag mit eigener Zeile für über mehrere Tage laufende Termine. Tagesansicht, Heute und Personenansicht berücksichtigen laufende Zeiträume. Ganztägige Zeiträume schließen den Endtag ein; ein zeitliches Ende um 00:00 belegt den Endtag nicht. Bestehende Ereignisse ohne Enddatum bleiben eintägig. Umsetzung zu [Issue #18](https://github.com/ipt01titus/kontext/issues/18).
- Erfolgskriterien und verbundene Personen direkt in der Zielseitenleiste ergänzen, bearbeiten und entfernen, jeweils mit Speichern und Abbrechen. Beim Speichern bleiben ungespeicherte Eingaben im anderen Abschnitt erhalten. Umsetzung zu [Issue #20](https://github.com/ipt01titus/kontext/issues/20); einmaliges Neuladen der Seite lädt die neue Oberfläche.

Details: [Betriebsanleitung](betrieb/mac-probebetrieb.md), [Entscheidung 0005](entscheidungen/0005-lokaler-mac-pilot.md) und [Issue #11](https://github.com/ipt01titus/kontext/issues/11). Die folgende Tabelle dokumentiert überwiegend den übernommenen fachlichen Oberflächenumfang; sie ist keine Zusage, dass alle Produktfelder bereits vollständig umgesetzt sind.

| Bereich | Im Prototyp erprobt | Für das Produkt noch erforderlich |
|---|---|---|
| Tagessicht | Termine, relevante Aktivitäten und Wiedervorlagen; Pilot mit aktuellem lokalen Datum | Vollständige Zeit-/Zeitzonenregeln und Geräteabgleich |
| Personen | Projektübergreifender Zusammenhang, erwartete Rückmeldungen, Ziele, Kontaktfelder und Vertrauenslevel | Vollständige iPhone-Kontaktstruktur, Import, Dubletten und differenzierte Rollen |
| Aktivitäten | Liste/Kanban, Schritte, Kommentare, Bezüge und Vorgänger/Nachfolger | Verbindlicher Feldumfang und vollständige Bearbeitung aller Beziehungen |
| Objekte | Anlage, Bearbeitung, Baum, Suche mit Pfad, Anlage aus Aktivitätsdialog | Produktiver Datenvertrag und vollständige Pflege zusätzlicher Beziehungen |
| Projekte | Hierarchische Struktur, Anlage/Bearbeitung und Elternfilter mit Nachkommen | Entscheidung zur Themenstruktur, Archivierung und künftiger Mehrbenutzerumfang |
| Ziele | Gemeinsame Ansicht mit Opportunityfilter, Kriterien und Vertriebsangaben | Vollständige Messgrößen, Prioritäten, Ergebnisbewertung und Beziehungsrollen |
| Ereignisse | Kalender, Terminvorbereitung, Gesprächsdokumentation und Verbindungen | Externe Kalender, Wiederholungen, getrennte Plan-/Istzeiten und Konfliktregeln |
| Eintragsnummern | Einmalige lokale Vergabe, Erhalt bei Bearbeitung und globale Suche | Zentraler Nummernkreis und kollisionssichere Migration aus mehreren Beständen |
| Assistenten | Bedienung der Oberfläche praktisch geprüft | Authentifizierte API und gegebenenfalls MCP |
| Datenaustausch | Pilot: SQLite, Sicherung, Export, Import und Wiederherstellung | Geräteabgleich, Teamzugriff und endgültiger Datenvertrag |
| Integrationen | Erklärende Platzhalter | Echte Kontakte, Kalender, E-Mail und weitere Kanäle |

Bestätigte Produktanforderung: Nutzung auf MacBook, iPad und iPhone mit Offlinearbeit, automatischem Geräteabgleich und sichtbarem Offline-/Abgleichstatus. Diese Funktionen sind mit der neuen Festlegung noch nicht implementiert. Siehe [Entscheidung 0003](entscheidungen/0003-apple-offline-synchronisation.md).

## Ausgeführte Prüfungen am übernommenen Stand

- JavaScript-Syntax geprüft.
- Vier automatisierte Modellprüfungen bestanden: Erhalt eigener Daten und Kommentare bei Migration, idempotente Migration, hierarchische Filter, stabile eindeutige Nummern und bewusste Wurzelzuordnung.
- Browserabläufe geprüft: Objektanlage und Abbruch aus Aktivität, Erhalt von Name/Schritten/Fälligkeit, gespeicherte Verknüpfung nach erneutem Laden, Objektbaum mit drei Ebenen, Projektanlage sowie Verschiebung und Umbenennung bei unveränderter Nummer, Nummernsuche und Elternkontextfilter.
- Mobile Darstellung bei 390 Pixeln geprüft. Dies ist kein vollständiger Test auf allen Zielgeräten.

## Prüfungen des Mac-Piloten

- Elf automatisierte Prüfungen für Speicherung und lokalen HTTP-Zugriff: Wiederöffnung, unveränderte IDs/Nummern/Beziehungen/Kommentare, idempotente Wiederholung, konkurrierende Änderungen, Sicherungsfehler, Wiederherstellung und Nummernzähler, getrennte Arbeitsbereiche, ungültige Graphen und Zugriffsschutz.
- Im Browser: eigener Projektkontext, Aktivität mit Name/Schritten/Fälligkeit, neues Objekt direkt aus der Aktivitätsanlage, gespeicherter Bezug und Kommentar; nach Beenden und Neustart des lokalen Dienstes unverändert erhalten.
- Manuelle Sicherung und Wiederherstellung im Browser: späteren Kommentar zurückgesetzt, ursprünglichen Kommentar, Schritte, Nummer und Objektbezug erhalten. Schreibversuch bei beendetem Dienst: Eingaben bleiben sichtbar; nach Neustart und erneutem Versuch genau einmal gespeichert und nach Neuladen erhalten.
- JSON-Export und anschließenden Dateiimport im Browser abgeschlossen: Aktivität #4 mit Objektbezug #3, Fälligkeit, zwei Schritten und beiden Kommentaren erhalten. Wechsel zu den getrennten Beispieldaten und zurück erhält den eigenen Testbestand. Alle diese Prüfungen verwenden einen eigenen Datenordner auf Port 8775; der Alltagstest beginnt separat auf Port 8773.
- Kontextanlage aus dem Personendialog im getrennten Beispielbestand auf Port 8775 geprüft: Abbruch ohne neuen Projekteintrag; Anlegen eines Unterprojekts mit automatischer Auswahl neben zwei vorhandenen Zuordnungen; Vorname, Nachname, Firma, Position, Telefon, E-Mail, Vertrauenslevel und Notizen unverändert erhalten. Person und Zuordnungen bleiben nach Neuladen erhalten; Aktion auch beim Bearbeiten vorhanden. Desktopdarstellung geprüft, kein zusätzlicher Mobilgerätetest für diese Ergänzung.
- Aktivitätsabbruch: zusätzliche Modellprüfungen für offene Arbeit, unerfüllte Vorbedingungen und Erhalt vorhandener Daten; Speicherprüfungen für Abbruch, Wiederöffnung und Wiederherstellung sowie ein HTTP-Prüffall für Speicherung, Export und Wiederöffnung. Im Browser wurden die Aktion und der Filter auf Port 8775 geprüft. Der komplette Speicherablauf im Browser steht nach Dienstneustart noch aus, weil der vorhandene Prozess die frühere Statusvalidierung verwendet und in dieser Sitzung nicht neu gestartet werden kann.
- Gemeldeten Abbruchfehler auf Port 8775 reproduziert: Der ursprüngliche Prozess lehnt „Abgebrochen“ noch ab. Die bislang außerhalb des geöffneten Detaildialogs verdeckte Fehlermeldung wird jetzt direkt im Dialog als fokussierte Meldung angezeigt und erklärt den nötigen Neustart. Der passende Neustartstarter wurde auf zsh-Syntax geprüft; seine Ausführung und der erfolgreiche Abbruch im neu gestarteten Dienst stehen noch aus.
- Mehrtägige Ereignisse im getrennten Beispielbestand auf Port 8775 geprüft: Anlage vom 19. bis 23. November, Darstellung an Donnerstag bis Sonntag und am Montag der Folgewoche, Tagesansicht, Heute, laufender Termin bei Jonas, Neuladen und Bearbeiten bei unveränderter Nummer #57. Anschließend bis 24. November verlängert und ganztägig gespeichert; leere Uhrzeiten, Personenbezug und Notiz bleiben beim erneuten Bearbeiten erhalten. Ein Enddatum vor dem Start wird bei erhaltenen Formulareingaben abgewiesen. Desktopdarstellung geprüft; kein zusätzlicher Mobilgerätetest.
- Zusätzliche Modell- und Speicherprüfungen decken Wochenende, Jahreswechsel, Mitternachtsende, laufende Zeiträume, Validierungsfehler, Export/Import und Wiederherstellung ab. Die aktualisierte serverseitige Datums-/Zeitprüfung benötigt einen Dienstneustart. Der bestehende Testdienst kann die getesteten Zeiträume bereits speichern; die Ausnahme für eine frühere Enduhrzeit am Folgetag wurde dort noch nicht im Browser ausgeführt und wird über HTTP automatisiert geprüft.
- Zielseitenleiste im getrennten Beispielbestand auf Port 8775 geprüft: Kriterien ergänzen, trimmen, vollständig entfernen und erneut ergänzen; Personen hinzufügen und entfernen; beide Bearbeitungen abbrechen; Neuladen erhält gespeicherte Änderungen. Beide Abschnitte gleichzeitig geöffnet und jeweils den anderen gespeichert: ungespeicherter Text beziehungsweise die Auswahl bleiben erhalten. Vergleich des gespeicherten Opportunity-Ziels #46 mit dem Ausgangsstand bestätigt unveränderte ID, Nummer, Status, Termine, Vertriebsangaben, Kommentare und übrige Beziehungen. Desktopdarstellung geprüft; kein zusätzlicher Mobilgerätetest für diese Ergänzung.
- Lokale Ressourcen werden vollständig vom Mac ausgeliefert; die HTTP-Prüfungen benötigen keine externen Dienste. Die Netzwerkverbindung des Mac wurde für den Test nicht abgeschaltet; ein kompletter macOS-Neustart wurde nicht ausgeführt.

## Ausgangsstand und Veröffentlichung

Der Prototyp wurde aus dem am 20. November veröffentlichten Site-Quellstand `a5ef54023aca9063642e9bb614e0f2d416428f80` übernommen. Die übernommenen Produktdateien werden bei dieser Repositoryanlage nicht funktional geändert. Der [bisherige Entwurf](https://kontext-urs-20261118.urs-mueller588623.chatgpt.site/) bleibt separat veröffentlicht und zugriffsbeschränkt.

Die frühere Unterbrechung betraf den Zugriff auf die lokale Entwicklungsumgebung. Der damalige unfertige Änderungsversuch war nicht gespeichert. Nach Wiederherstellung des Zugriffs wurden die Änderungen fertiggestellt, geprüft, gesichert und veröffentlicht. Die genaue Ursache der hängenden Chatnachrichten wurde nicht festgestellt.

GitHub dient nun als nachvollziehbarer Ausgangspunkt für weitere Anforderungen und Änderungen. Eine cloudbasierte Entwicklungsumgebung oder ein dauerhafter Worker kann später die Abhängigkeit vom erreichbaren Mac reduzieren; dies ist keine bereits eingerichtete Infrastruktur.
