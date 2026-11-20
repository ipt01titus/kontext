# Betrieb auf mehreren Geräten und Datenaustausch

Status: **Vorschlag zur Diskussion, keine beschlossene Architektur.** Stand: 20. November 2026.

## Drei getrennte Entscheidungen

1. **Oberfläche:** Auf welchen Geräten soll Kontext bedient werden?
2. **Betrieb und Datenort:** Wo laufen Anwendungslogik und gemeinsamer Datenbestand?
3. **Verbindungsverlust:** Welche Vorgänge sollen ohne Verbindung weiter funktionieren?

Eine installierbare Oberfläche entscheidet noch nicht, wo die Daten liegen oder wie sie synchronisiert werden. Die heutige Browserpersistenz ist geräte- und browsergebunden. Ein zweiter Browser, ein anderes Gerät oder eine separat installierte Web-App kann einen eigenen lokalen Bestand besitzen.

## Empfehlung als Ausgangspunkt

Eine responsive Webanwendung mit zentraler Datenbank und gemeinsamer API bietet einen überschaubaren Anfang. Sie kann zunächst im Browser laufen und später als Progressive Web App (PWA) installierbar werden. Eigenbetrieb oder ein gemanagter Betrieb sind beide möglich; ein Anbieter ist noch nicht ausgewählt.

Die gemeinsame API bedient Oberfläche, spätere Integrationen und autorisierte Assistenten. Serverseitig gelten dieselben fachlichen Regeln, unabhängig vom Client. Die Auswahl von Programmiersprache, Framework, Datenbankprodukt und Hosting folgt nach den Betriebsanforderungen.

### Geräte und Oberflächen

| Gerät | Möglicher Einstieg | Später bei nachgewiesenem Bedarf |
|---|---|---|
| Mac, Windows-PC, Linux-PC | Browser mit responsiver Oberfläche | Installierte Web-App oder Desktopanwendung mit zusätzlichen Systemfunktionen |
| iPhone und iPad | Browser; Nutzung über Home-Bildschirm möglich | Native Ergänzung für erforderliche Systemintegrationen |
| Android-Telefon/-Tablet | Browser; Installation als Web-App je Browser möglich | Native Ergänzung für erforderliche Systemintegrationen |
| Assistent / Hintergrundprozess | Authentifizierte API nach Umsetzung | MCP-Zugang für unterstützte Assistenten |

PWA-Installation und verfügbare Gerätefunktionen unterscheiden sich nach Betriebssystem und Browser. Apple beschreibt Home-Bildschirm-Web-Apps auf dem iPhone sowie Safari-Web-Apps auf dem Mac; Chromium-basierte Desktopbrowser unterstützen installierbare Web-Apps ebenfalls. Die konkrete Zielmatrix muss praktisch geprüft werden. Eine automatische Anruferkennung oder vollständige lokale Adressbuchintegration folgt daraus nicht.

## Betriebsvarianten

| Variante | Datenabgleich | Nutzen | Aufwand / Grenze |
|---|---|---|---|
| Zentraler Dienst, zunächst online | Alle Geräte greifen auf denselben Serverbestand zu | Einfacher Gerätewechsel, gemeinsamer Datenstand, Integrationen und Agentenzugang | Verbindung zum Dienst nötig; Betrieb und Sicherung werden benötigt |
| Zentraler Dienst mit Offlinefunktion | Lokale Kopie und ausstehende Änderungen werden mit dem Server abgeglichen | Unterwegs lesen und gegebenenfalls weiterarbeiten | Lokale Warteschlange, Konfliktbehandlung, Migrationen und sichere Wiederaufnahme nötig |
| Vollständig lokale beziehungsweise verteilte Installation | Eigener Abgleich zwischen getrennten Beständen oder eigener zentraler Instanz | Stärkere lokale Kontrolle, je Modell ohne externen Dienst | Erreichbarkeit, Zusammenführung, Sicherung und Gerätewechsel sind zusätzliche Aufgaben |

Die Empfehlung ist ein zentraler Dienst als erster belastbarer Produktstand. Der erforderliche Offlineumfang sollte schon vor dem Daten- und API-Entwurf geklärt werden. Vollständige Offlinebearbeitung ist eine bewusste Produkteigenschaft mit eigenem Aufwand.

## Wie zwei Geräte denselben Datenbestand nutzen

Im Onlinefall meldet sich ein Benutzer auf beiden Geräten an. Eine Änderung wird über die API gespeichert und danach auf dem anderen Gerät abgerufen. Die genaue Aktualisierungstechnik, etwa erneutes Laden, regelmäßiger Abgleich oder Echtzeitbenachrichtigung, ist noch offen. Realtime ist für die gemeinsame Datenhaltung nicht zwingend.

Beispiel: Auf dem Mac wird ein Kommentar zu einer Aktivität ergänzt. Das iPhone lädt beim nächsten Abgleich denselben Kommentar derselben Aktivität. Eine zweite Aufgabenliste entsteht dabei nicht.

| Bestandteil | Vorschlag |
|---|---|
| Identität | Dauerhafte interne ID, bei Offlineanlage kollisionsarm schon im Client erzeugbar |
| Sichtbare Nummer | Einmalige zentrale Vergabe je festgelegtem Nummernkreis; bei Umbenennung unverändert |
| Änderungsstand | Version/Revision je geändertem Datensatz, mit serverseitiger Prüfung |
| Wiederholte Anfrage | Eindeutige Operationskennung verhindert doppelte Anlage nach Verbindungsabbruch |
| Kommentare | Eigenständige Ergänzungen können getrennt übernommen werden |
| Beziehungen | Über stabile IDs übertragen; Rollen und Richtung erhalten |
| Löschungen | Für den Abgleich nachvollziehbar halten, damit alte Clients entfernte Daten nicht wiederherstellen |
| Geschäftliche Regeln | Beispielsweise Objekt-/Projekthierarchien und Abhängigkeiten auf dem Server prüfen |

### Gleichzeitige Änderungen

Ändern Mac und iPhone denselben Fälligkeitstermin auf Grundlage desselben alten Stands, soll keine Änderung stillschweigend verloren gehen. Der Server prüft den mitgesendeten Änderungsstand. Eine veraltete Änderung wird als Konflikt zurückgemeldet und zur bewussten Auswahl angeboten. Für HTTP kann dies beispielsweise über starke ETags und `If-Match` nach RFC 9110 umgesetzt werden.

Für unterschiedliche Felder kann später eine kontrollierte Zusammenführung sinnvoll sein. Hierarchien und gerichtete Beziehungen brauchen zusätzlich eine gemeinsame Konsistenzprüfung: Zwei einzeln erlaubte Verschiebungen dürfen zusammen keinen Kreis erzeugen. Eine Konfliktstrategie allein anhand der Geräteuhr ist keine ausreichende fachliche Lösung.

## Falls Offlinebearbeitung benötigt wird

Die Oberfläche hält einen passenden lokalen Datenbestand und ausstehende Änderungen vor. Sie zeigt sichtbar an, ob ein Stand synchronisiert ist oder Änderungen noch ausstehen. Beim Wiederverbinden werden Änderungen wiederholbar übertragen; Beziehungen zu offline erzeugten Einträgen bleiben über deren interne IDs erhalten.

Für neue Offlineeinträge gibt es zwei offene Nummernmodelle: zunächst eine vorläufige lokale Kennung und einmalige endgültige Vergabe nach dem Abgleich oder ein komplexeres Verfahren zur vorab koordinierten Nummernvergabe. Wenn eine endgültige menschenlesbare Nummer sofort ohne Verbindung erforderlich ist, muss dies ausdrücklich gefordert werden.

Offline im Browser erfordert eine dafür ausgelegte Datenablage und Anwendungsbereitstellung, beispielsweise IndexedDB und Service Worker. Das ist im aktuellen Prototyp nicht umgesetzt. Eine Installation auf dem Home-Bildschirm stellt allein keine Offlinefunktion oder Synchronisation bereit.

## Sicherung, Import und externe Systeme

Synchronisation verteilt Änderungen; Sicherung ermöglicht die Wiederherstellung eines früheren Stands. Export, Sicherung und Wiederherstellung werden deshalb gesondert spezifiziert. Ein Gerätewechsel muss ohne Verlust der Beziehungen und Nummern prüfbar sein.

Der spätere Import bestehender Prototypdaten benötigt Quellkennung, Zuordnung und Konfliktprüfung. Mehrere bisher unabhängige Browserbestände können dieselben Nummern für verschiedene Einträge enthalten. Die Übernahme muss dies sichtbar auflösen und gegebenenfalls alte Nummern quellenbezogen als Referenz erhalten.

Kalender-/Kontaktintegration ist ein weiterer Abgleich: Externe Kennungen, Wiederholungsinstanzen und die jeweilige Feldhoheit werden getrennt von der internen Gerätesynchronisation geführt. Eine Kalenderlöschung darf keine zugehörige Aktivität löschen. Welche Konten gelesen oder beschrieben werden, ist noch festzulegen.

## Zugang für Assistenten

Im bestehenden Entwurf kann ein Assistent bei verfügbarem Browserzugriff die Oberfläche bedienen. Für eigenständige Arbeit unabhängig vom Benutzergerät wird eine authentifizierte API vorgeschlagen. Sie soll Einträge suchen, lesen, anlegen, bearbeiten und fachlich verknüpfen können. Rechte und Änderungsurheber werden mitgeführt; dieselben Geschäftsregeln gelten für Mensch und Assistent. MCP kann darauf aufsetzen, ist aber noch keine implementierte Schnittstelle.

## Zu entscheidende Fragen

| Frage | Beispielsweise mögliche Antworten |
|---|---|
| Welche Geräte zuerst? | Mac und iPhone; zusätzlich Windows, iPad oder Android |
| Was muss ohne Verbindung möglich sein? | Kein Bedarf; Lesen; Erfassen neuer Aktivitäten; vollständige Bearbeitung |
| Wer arbeitet mit denselben Daten? | Nur Urs; kleines Team mit gemeinsamer Sicht; getrennte Arbeitsräume |
| Wo soll der Dienst betrieben werden? | Eigener Server; gemanagter Dienst; ausschließlich lokal |
| Was soll der Assistent selbstständig tun? | Suchen und Auskunft; strukturieren; Änderungen; Hintergrundarbeit |

## Abnahmeszenarien des künftigen Mehrgerätebetriebs

- Auf Gerät A angelegte Einträge erscheinen mit denselben Identitäten, Nummern und Beziehungen auf Gerät B.
- Ein erneuter Sendeversuch nach verlorener Antwort erzeugt keinen zweiten Eintrag.
- Gleichzeitige widersprüchliche Änderungen werden sichtbar behandelt.
- Ein Gerätewechsel erhält Kommentare, Hierarchien, Abhängigkeiten und externe Zuordnungen.
- Soweit Offlinebearbeitung gewählt wird, überstehen ungesendete Änderungen einen Neustart und werden nach Wiederverbindung korrekt übernommen.
- Assistentenaktionen laufen unter einer nachvollziehbaren Identität und beachten die festgelegten Rechte.

## Technische Quellen

Am 20. November 2026 geprüft. Die Quellen belegen Plattformfähigkeiten und Protokollmechanismen, nicht die oben vorgeschlagene Produktentscheidung.

- [web.dev: PWA-Installation](https://web.dev/learn/pwa/installation)
- [Apple: Safari-Web-Apps auf dem Mac](https://support.apple.com/en-ie/104996)
- [Apple: Website als App auf dem iPhone](https://support.apple.com/en-az/guide/iphone/iphea86e5236/26/ios/26)
- [RFC 9110, Abschnitt 13.1.1: If-Match](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1)
