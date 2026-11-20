# Implementierungsstand

Stand: 20. November 2026 · Version 0.2.0. `app/` enthält den vorgezogenen lokalen Mac-Pilot mit SQLite-Speicherung und Sicherungen. Der historische Entwurf unter `prototype/dist/` bleibt erhalten; nur dieser speichert ausschließlich im Browser und verwendet den festen Demotag 18. November.

## Lokaler Mac-Pilot

- Doppelklick-Starter und Beenden über die beiden `.command`-Dateien; lokaler Python-Dienst auf `127.0.0.1:8773`.
- Eigene Daten und Beispieldaten getrennt, aktuelle lokale Tagesanzeige.
- Dauerhafte SQLite-Snapshots; bestätigte Speicherung, Revisionsschutz gegen Überschreiben und wiederholbare Speicheraufträge nach verlorener Antwort.
- Automatische konsistente Sicherung vor Änderungen; manuelle Sicherung, JSON-Export/Import und Wiederherstellung mit vorheriger Sicherheitssicherung.
- Laufzeitdaten außerhalb der Produktdateien und von Git ausgeschlossen. Kein Geräteabgleich oder externer Dienst erforderlich.

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
- Lokale Ressourcen werden vollständig vom Mac ausgeliefert; die HTTP-Prüfungen benötigen keine externen Dienste. Die Netzwerkverbindung des Mac wurde für den Test nicht abgeschaltet; ein kompletter macOS-Neustart wurde nicht ausgeführt.

## Ausgangsstand und Veröffentlichung

Der Prototyp wurde aus dem am 20. November veröffentlichten Site-Quellstand `a5ef54023aca9063642e9bb614e0f2d416428f80` übernommen. Die übernommenen Produktdateien werden bei dieser Repositoryanlage nicht funktional geändert. Der [bisherige Entwurf](https://kontext-urs-20261118.urs-mueller588623.chatgpt.site/) bleibt separat veröffentlicht und zugriffsbeschränkt.

Die frühere Unterbrechung betraf den Zugriff auf die lokale Entwicklungsumgebung. Der damalige unfertige Änderungsversuch war nicht gespeichert. Nach Wiederherstellung des Zugriffs wurden die Änderungen fertiggestellt, geprüft, gesichert und veröffentlicht. Die genaue Ursache der hängenden Chatnachrichten wurde nicht festgestellt.

GitHub dient nun als nachvollziehbarer Ausgangspunkt für weitere Anforderungen und Änderungen. Eine cloudbasierte Entwicklungsumgebung oder ein dauerhafter Worker kann später die Abhängigkeit vom erreichbaren Mac reduzieren; dies ist keine bereits eingerichtete Infrastruktur.
