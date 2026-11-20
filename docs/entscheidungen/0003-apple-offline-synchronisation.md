# Entscheidung 0003 – Apple-Geräte, Offlinearbeit und automatischer Abgleich

Status: **Produktanforderungen bestätigt am 20. November 2026. Technische Architektur noch offen.**

## Grundlage

Urs möchte Kontext auf MacBook, iPad und iPhone nutzen. Alle Geräte sollen nach dem Abgleich denselben Stand haben. Auf jedem Gerät soll offline gearbeitet werden können. Die Synchronisation findet im Hintergrund statt, sobald die Verbindung es erlaubt. Offlinezustand und noch ausstehender Abgleich werden angezeigt.

## Festlegung

1. MacBook, iPad und iPhone gehören zum verbindlichen Produktumfang.
2. Die fachliche Arbeit an den fünf Entitäten, ihren Beziehungen und Kommentaren muss offline möglich sein. Einträge werden lokal gelesen, angelegt und bearbeitet.
3. Änderungen werden dauerhaft auf dem Gerät gespeichert und ohne manuell ausgelösten Sync abgeglichen, sobald Verbindung und Ausführung möglich sind.
4. Der Abgleich überträgt lokale Änderungen und übernimmt Änderungen anderer Geräte. Nach erfolgreichem Abgleich konvergieren die Bestände.
5. Der Status zeigt sowohl fehlende Verbindung als auch noch nicht übertragene Änderungen. Eine erfolgreiche lokale Speicherung wird von einer bestätigten Übertragung unterschieden.

Referenzen: KTX-020 bis KTX-024. KTX-O01 und KTX-O02 sind damit inhaltlich geklärt; konkrete technische Details bleiben offen.

## Konsequenzen für den technischen Entwurf

Es wird ein für Offlinearbeit ausgelegter lokaler Datenbestand mit dauerhafter Änderungswarteschlange benötigt. Automatischer Abgleich ist eine Kernfunktion. Clientidentitäten müssen offline erzeugbar sein; Beziehungen dürfen beim späteren Abgleich nicht verloren gehen. Wiederholungen, Konflikte, Hierarchieregeln und endgültige Eintragsnummern werden im Synchronisationskonzept berücksichtigt.

Der letzte bestätigte Abgleich und ausstehende lokale Änderungen sind unterscheidbar. Ein Gerät ohne Verbindung kann den aktuellen Stand anderer Geräte nicht kennen. Ein Synchronisationsfehler darf keine bereits lokal gespeicherte Arbeit verwerfen.

Die erste Anmeldung und Bereitstellung des Datenbestands auf einem neuen Gerät benötigen eine gesonderte Regelung. Externe Quellen können offline nur mit dem zuvor übernommenen Inhalt dargestellt werden; echte Netzwerkaktionen benötigen weiterhin eine Verbindung.

## Hintergrundbetrieb auf Apple-Geräten

Der Nutzerbedarf umfasst automatischen Hintergrundabgleich. Bei einer aktiven Anwendung soll die Wiederverbindung unmittelbar einen nicht blockierenden Abgleich auslösen. Nach erneutem Öffnen oder Aktivieren wird ebenfalls automatisch abgeglichen.

Für eine inaktive, vom Betriebssystem angehaltene oder ausdrücklich beendete Anwendung muss das Verhalten gesondert geprüft werden. iOS/iPadOS steuern die Zuteilung von Hintergrundlaufzeit. Auch native Hintergrundaufgaben liefern keine Garantie eines sofortigen Starts bei Netzrückkehr. Der Stand der WebKit-Background-Sync-Unterstützung ist ein wesentliches Risiko einer ausschließlich webbasierten Umsetzung. Diese Einschränkungen ändern nicht stillschweigend die Anforderung.

Die bisherige Empfehlung einer Web-App wird deshalb erneut gegen eine native Apple-Anwendung beziehungsweise native Ergänzungen abgewogen. Es ist noch kein Framework, Syncdienst oder Hostinganbieter gewählt. Ein gezielter technischer Versuch auf den Zielgeräten soll die Entscheidung stützen.

## Noch zu konkretisieren

- Mindestversionen von macOS, iPadOS und iOS.
- Erwartetes Abgleichverhalten bei aktiver, inaktiver, gesperrter und ausdrücklich beendeter Anwendung; akzeptable Verzögerung im Hintergrund.
- Technische Konflikterkennung und Behandlung globaler Hierarchieregeln. Die fachliche Grundregel für Ergänzungen und widersprüchliche Feldänderungen ist inzwischen in [Entscheidung 0004](0004-synchronisationskonflikte.md) bestätigt.
- Endgültige Nummernvergabe bei Offlineanlage.
- Nutzerkreis, Datenort, Hosting und Wiederherstellung.

## Abnahmefälle

| Fall | Erwartetes Ergebnis |
|---|---|
| Auf jedem Gerät ohne Verbindung arbeiten | Einträge und Beziehungen lesen, anlegen, bearbeiten; Kommentare ergänzen |
| Anwendung vor dem Sync schließen und wieder öffnen | Lokale Änderungen und Übertragungswarteschlange bleiben vorhanden |
| Verbindung zum Dienst kehrt zurück | Automatischer Abgleich im Hintergrund der Bedienung; kein manueller Start erforderlich |
| Mehrfach abbrechende Übertragung | Keine Duplikate, keine verlorenen Verbindungen, bestätigter Zwischenstand bleibt korrekt |
| Drei Geräte erfolgreich abgeglichen | Gleiche Identitäten, endgültige Nummern und fachliche Inhalte |
| Offline, ohne lokale Änderungen | Offlinehinweis und letzter bekannter Abgleich sichtbar; kein behaupteter aktueller globaler Stand |
| Offline, mit lokalen Änderungen | Offlinehinweis und ausstehende Änderungen sichtbar |
| Online, mit Syncfehler oder Konflikt | Arbeit bleibt lokal gespeichert; Handlungsbedarf sichtbar |
| Gerät gesperrt / Anwendung inaktiv / beendet | Tatsächliches Plattformverhalten dokumentiert und am vereinbarten Zielverhalten geprüft |

## Quellen zur technischen Grenze

Am 20. November 2026 geprüft:

- [Apple: Choosing Background Strategies for Your App](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app)
- [WebKit: Position zu Web Background Synchronization](https://github.com/WebKit/standards-positions/issues/14)
- [WebKit: Implementierungsanfrage SyncManager](https://bugs.webkit.org/show_bug.cgi?id=182565)
