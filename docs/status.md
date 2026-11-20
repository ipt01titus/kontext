# Implementierungsstand

Stand: 20. November 2026. Der übernommene Quellstand ist ein interaktiver Entwurf. `prototype/dist/` enthält HTML, CSS und JavaScript ohne Build oder externe Abhängigkeiten. Speicherung erfolgt unter `kontext-entwurf-v1` im jeweiligen Browser. Der feste Demotag ist der 18. November 2026.

| Bereich | Im Prototyp erprobt | Für das Produkt noch erforderlich |
|---|---|---|
| Tagessicht | Termine, relevante Aktivitäten und Wiedervorlagen | Echte Tageslogik, vollständige Zeit-/Zeitzonenregeln und zentraler Bestand |
| Personen | Projektübergreifender Zusammenhang, erwartete Rückmeldungen, Ziele, Kontaktfelder und Vertrauenslevel | Vollständige iPhone-Kontaktstruktur, Import, Dubletten und differenzierte Rollen |
| Aktivitäten | Liste/Kanban, Schritte, Kommentare, Bezüge und Vorgänger/Nachfolger | Verbindlicher Feldumfang und vollständige Bearbeitung aller Beziehungen |
| Objekte | Anlage, Bearbeitung, Baum, Suche mit Pfad, Anlage aus Aktivitätsdialog | Produktiver Datenvertrag und vollständige Pflege zusätzlicher Beziehungen |
| Projekte | Hierarchische Struktur, Anlage/Bearbeitung und Elternfilter mit Nachkommen | Entscheidung zur Themenstruktur, Archivierung und künftiger Mehrbenutzerumfang |
| Ziele | Gemeinsame Ansicht mit Opportunityfilter, Kriterien und Vertriebsangaben | Vollständige Messgrößen, Prioritäten, Ergebnisbewertung und Beziehungsrollen |
| Ereignisse | Kalender, Terminvorbereitung, Gesprächsdokumentation und Verbindungen | Externe Kalender, Wiederholungen, getrennte Plan-/Istzeiten und Konfliktregeln |
| Eintragsnummern | Einmalige lokale Vergabe, Erhalt bei Bearbeitung und globale Suche | Zentraler Nummernkreis und kollisionssichere Migration aus mehreren Beständen |
| Assistenten | Bedienung der Oberfläche praktisch geprüft | Authentifizierte API und gegebenenfalls MCP |
| Datenaustausch | Persistenz im selben Browser | Geräteabgleich, Teamzugriff, Sicherung, Export und Wiederherstellung |
| Integrationen | Erklärende Platzhalter | Echte Kontakte, Kalender, E-Mail und weitere Kanäle |

Bestätigte Produktanforderung: Nutzung auf MacBook, iPad und iPhone mit Offlinearbeit, automatischem Geräteabgleich und sichtbarem Offline-/Abgleichstatus. Diese Funktionen sind mit der neuen Festlegung noch nicht implementiert. Siehe [Entscheidung 0003](entscheidungen/0003-apple-offline-synchronisation.md).

## Ausgeführte Prüfungen am übernommenen Stand

- JavaScript-Syntax geprüft.
- Vier automatisierte Modellprüfungen bestanden: Erhalt eigener Daten und Kommentare bei Migration, idempotente Migration, hierarchische Filter, stabile eindeutige Nummern und bewusste Wurzelzuordnung.
- Browserabläufe geprüft: Objektanlage und Abbruch aus Aktivität, Erhalt von Name/Schritten/Fälligkeit, gespeicherte Verknüpfung nach erneutem Laden, Objektbaum mit drei Ebenen, Projektanlage sowie Verschiebung und Umbenennung bei unveränderter Nummer, Nummernsuche und Elternkontextfilter.
- Mobile Darstellung bei 390 Pixeln geprüft. Dies ist kein vollständiger Test auf allen Zielgeräten.

## Ausgangsstand und Veröffentlichung

Der Prototyp wurde aus dem am 20. November veröffentlichten Site-Quellstand `a5ef54023aca9063642e9bb614e0f2d416428f80` übernommen. Die übernommenen Produktdateien werden bei dieser Repositoryanlage nicht funktional geändert. Der [bisherige Entwurf](https://kontext-urs-20261118.urs-mueller588623.chatgpt.site/) bleibt separat veröffentlicht und zugriffsbeschränkt.

Die frühere Unterbrechung betraf den Zugriff auf die lokale Entwicklungsumgebung. Der damalige unfertige Änderungsversuch war nicht gespeichert. Nach Wiederherstellung des Zugriffs wurden die Änderungen fertiggestellt, geprüft, gesichert und veröffentlicht. Die genaue Ursache der hängenden Chatnachrichten wurde nicht festgestellt.

GitHub dient nun als nachvollziehbarer Ausgangspunkt für weitere Anforderungen und Änderungen. Eine cloudbasierte Entwicklungsumgebung oder ein dauerhafter Worker kann später die Abhängigkeit vom erreichbaren Mac reduzieren; dies ist keine bereits eingerichtete Infrastruktur.
