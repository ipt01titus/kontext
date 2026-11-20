# Betrieb auf mehreren Geräten und Datenaustausch

Status: **Geräte, Offlinearbeit und automatischer Abgleich bestätigt; technische Architektur zur Diskussion.** Stand: 20. November 2026.

## Bestätigte Betriebsanforderungen

MacBook, iPad und iPhone sind verbindliche Zielgeräte. Auf allen drei Geräten soll auch offline gearbeitet werden können. Änderungen werden dauerhaft lokal erhalten und automatisch im Hintergrund synchronisiert, sobald Verbindung und Ausführung es ermöglichen. Offlinezustand und ausstehende Synchronisation bleiben sichtbar. Siehe [Entscheidung 0003](../entscheidungen/0003-apple-offline-synchronisation.md) und KTX-020 bis KTX-024.

## Drei getrennte Entscheidungen

1. **Oberfläche:** Auf welchen Geräten soll Kontext bedient werden?
2. **Betrieb und Datenort:** Wo laufen Anwendungslogik und gemeinsamer Datenbestand?
3. **Verbindungsverlust:** Wie werden die bestätigte Offlinearbeit, spätere Zusammenführung und die sichtbaren Statusangaben umgesetzt?

Eine installierbare Oberfläche entscheidet noch nicht, wo die Daten liegen oder wie sie synchronisiert werden. Die heutige Browserpersistenz ist geräte- und browsergebunden. Ein zweiter Browser, ein anderes Gerät oder eine separat installierte Web-App kann einen eigenen lokalen Bestand besitzen.

## Empfehlung als Ausgangspunkt

Ein lokaler Datenbestand auf jedem Gerät mit gemeinsamer Abgleichschnittstelle ist der Ausgangspunkt des weiteren Entwurfs. Ein zentraler Dienst als Vermittler bleibt ein Vorschlag; Eigenbetrieb oder gemanagter Betrieb und der konkrete Datenort sind noch offen. Eine rein auf Onlinezugriff ausgelegte Anwendung erfüllt die bestätigte Anforderung nicht.

Die bisherige Web-App-Empfehlung muss wegen des Hintergrundverhaltens auf iOS/iPadOS gegen native Apple-Clients beziehungsweise native Ergänzungen geprüft werden. Auch eine Weboberfläche kann lokale Offlinearbeit unterstützen; daraus folgt noch keine zuverlässige Ausführung bei inaktiver oder beendeter App. Die Entscheidung wird durch einen technischen Versuch auf den Zielgeräten vorbereitet.

Die gemeinsame API bedient Oberfläche, spätere Integrationen und autorisierte Assistenten. Serverseitig gelten dieselben fachlichen Regeln, unabhängig vom Client. Die Auswahl von Programmiersprache, Framework, Datenbankprodukt und Hosting folgt nach den Betriebsanforderungen.

### Geräte und Oberflächen

| Gerät | Möglicher Einstieg | Später bei nachgewiesenem Bedarf |
|---|---|---|
| MacBook | Lokaler Datenbestand und Offlinebedienung erforderlich; Web-App oder native Anwendung zu bewerten | Hintergrundbetrieb und Systemfunktionen nachweisen |
| iPhone und iPad | Lokaler Datenbestand und Offlinebedienung erforderlich; Web-App und native Varianten vergleichen | Verhalten bei inaktiver/gesperrter/beendeter App auf echten Geräten prüfen |
| Assistent / Hintergrundprozess | Authentifizierte API nach Umsetzung | MCP-Zugang für unterstützte Assistenten |

PWA-Installation und verfügbare Gerätefunktionen unterscheiden sich nach Betriebssystem und Browser. Installation ist noch kein Nachweis für die benötigte Hintergrundausführung. Windows, Linux und Android gehören aktuell nicht zur bestätigten Zielmatrix. Eine automatische Anruferkennung oder vollständige lokale Adressbuchintegration folgt aus der Wahl einer Oberfläche nicht.

## Betriebsvarianten

| Variante | Datenabgleich | Nutzen | Aufwand / Grenze |
|---|---|---|---|
| Zentraler Dienst, ausschließlich online | Alle Geräte greifen auf denselben Serverbestand zu | Einfacher Gerätewechsel und gemeinsamer Datenstand | Erfüllt die bestätigte Offlineanforderung nicht |
| Zentraler Dienst mit Offlinefunktion | Lokaler Bestand und ausstehende Änderungen werden mit dem Server abgeglichen | Auf jedem Zielgerät offline weiterarbeiten | Dauerhafte Warteschlange, Konfliktbehandlung, Migrationen und sichere Wiederaufnahme nötig |
| Vollständig lokale beziehungsweise verteilte Installation | Eigener Abgleich zwischen getrennten Beständen oder eigener zentraler Instanz | Stärkere lokale Kontrolle, je Modell ohne externen Dienst | Erreichbarkeit, Zusammenführung, Sicherung und Gerätewechsel sind zusätzliche Aufgaben |

Die Empfehlung bleibt ein gemeinsamer Abgleichdienst mit von Anfang an offlinefähigen Clients. Offlinearbeit und automatischer Sync sind fester Bestandteil des ersten belastbaren Produktstands. Konkrete Speichertechnik, Dienst und Clientplattform sind noch zu entscheiden.

## Wie zwei Geräte denselben Datenbestand nutzen

Eine Änderung wird zuerst auf dem jeweiligen Gerät dauerhaft gespeichert und zur Übertragung vorgemerkt. Bei Verbindung wird automatisch abgeglichen: eigene Änderungen senden und bestätigte Änderungen anderer Geräte übernehmen. Der Abgleich läuft ohne Blockierung der Bedienung. Auch beim Öffnen oder erneuten Aktivieren wird automatisch ein Abgleich versucht. Die genaue Aktualisierungstechnik ist noch offen.

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

## Offlinearbeit und Wiederaufnahme

Die Oberfläche hält den bereitgestellten fachlichen Datenbestand und ausstehende Änderungen dauerhaft vor. Auch ein Schließen und erneutes Öffnen darf ungesendete Arbeit nicht verlieren. Beim Wiederverbinden werden Änderungen wiederholbar übertragen; Beziehungen zu offline erzeugten Einträgen bleiben über deren interne IDs erhalten. Die erste Bereitstellung auf einem neuen Gerät und der Umfang großer Anlagen sind gesondert zu regeln.

Für neue Offlineeinträge gibt es zwei offene Nummernmodelle: zunächst eine vorläufige lokale Kennung und einmalige endgültige Vergabe nach dem Abgleich oder ein komplexeres Verfahren zur vorab koordinierten Nummernvergabe. Wenn eine endgültige menschenlesbare Nummer sofort ohne Verbindung erforderlich ist, muss dies ausdrücklich gefordert werden.

Offline im Browser erfordert eine dafür ausgelegte Datenablage und Anwendungsbereitstellung, beispielsweise IndexedDB und Service Worker. Das ist im aktuellen Prototyp nicht umgesetzt. Eine Installation auf dem Home-Bildschirm stellt allein keine Offlinefunktion oder Synchronisation bereit.

### Hintergrundausführung bei inaktiver Anwendung

Automatischer Abgleich während der Bedienung und Ausführung bei inaktiver Anwendung sind getrennt zu prüfen. WebKit unterstützt den Web-Background-Sync-Mechanismus derzeit nicht; die Implementierungsanfrage ist offen und die dokumentierte Position ablehnend. Eine ausschließlich auf diese Web-API gestützte Lösung genügt deshalb für die Apple-Zielgeräte nicht.

Native Apple-Anwendungen können Hintergrundlaufzeit beantragen. Der Start und die verfügbare Laufzeit werden jedoch vom Betriebssystem bestimmt. Ein sofortiger Sync allein wegen wiederhergestellter Netzverbindung ist auch damit nicht garantiert. Der gewünschte Hintergrundbetrieb bleibt als Bedarf bestehen; ein App-/Plattformvergleich muss das nachweisbare Verhalten und verbleibende Verzögerungen offenlegen.

Im technischen Versuch sind aktive, inaktive, vom Betriebssystem angehaltene und ausdrücklich beendete Anwendungen sowie gesperrte Geräte zu unterscheiden. Die akzeptable Verzögerung bei inaktiver Anwendung wird noch vereinbart.

### Sichtbarer Verbindungs- und Abgleichstand

Folgende Darstellung ist ein Bedienvorschlag; die Pflicht zur Anzeige ist bestätigt:

| Situation | Beispielanzeige |
|---|---|
| Offline, keine lokalen Änderungen offen | Offline · letzter Abgleich 10:32 |
| Offline, lokale Änderungen offen | Offline · 3 Änderungen ausstehend |
| Dienst erreichbar, Änderungen vorgemerkt | Abgleich ausstehend |
| Übertragung läuft | Wird synchronisiert … |
| Senden und Empfangen erfolgreich abgeschlossen | Synchronisiert · letzter Abgleich 10:35 |
| Abgleich gescheitert | Synchronisation fehlgeschlagen · Änderungen lokal gespeichert |
| Inhaltlicher Konflikt offen | Konflikt zu klären |

Verbindung und Datenstand sind getrennte Merkmale. Eine vorhandene Netzverbindung beweist noch keine Erreichbarkeit des Abgleichdienstes. „Synchronisiert“ darf nicht allein aus dem Onlinezustand oder einem begonnenen Sendeversuch abgeleitet werden. Ein Offlinegerät kennt nur den letzten bestätigten gemeinsamen Stand und seine eigenen Änderungen.

## Sicherung, Import und externe Systeme

Synchronisation verteilt Änderungen; Sicherung ermöglicht die Wiederherstellung eines früheren Stands. Export, Sicherung und Wiederherstellung werden deshalb gesondert spezifiziert. Ein Gerätewechsel muss ohne Verlust der Beziehungen und Nummern prüfbar sein.

Der spätere Import bestehender Prototypdaten benötigt Quellkennung, Zuordnung und Konfliktprüfung. Mehrere bisher unabhängige Browserbestände können dieselben Nummern für verschiedene Einträge enthalten. Die Übernahme muss dies sichtbar auflösen und gegebenenfalls alte Nummern quellenbezogen als Referenz erhalten.

Kalender-/Kontaktintegration ist ein weiterer Abgleich: Externe Kennungen, Wiederholungsinstanzen und die jeweilige Feldhoheit werden getrennt von der internen Gerätesynchronisation geführt. Eine Kalenderlöschung darf keine zugehörige Aktivität löschen. Welche Konten gelesen oder beschrieben werden, ist noch festzulegen.

## Zugang für Assistenten

Im bestehenden Entwurf kann ein Assistent bei verfügbarem Browserzugriff die Oberfläche bedienen. Für eigenständige Arbeit unabhängig vom Benutzergerät wird eine authentifizierte API vorgeschlagen. Sie soll Einträge suchen, lesen, anlegen, bearbeiten und fachlich verknüpfen können. Rechte und Änderungsurheber werden mitgeführt; dieselben Geschäftsregeln gelten für Mensch und Assistent. MCP kann darauf aufsetzen, ist aber noch keine implementierte Schnittstelle.

## Zu entscheidende Fragen

| Frage | Beispielsweise mögliche Antworten |
|---|---|
| Welche Mindestversionen der drei Apple-Systeme? | macOS, iPadOS und iOS gezielt festlegen |
| Welche Verzögerung bei inaktiver Anwendung ist akzeptabel? | Gewünschtes Verhalten mit den nachgewiesenen Plattformmöglichkeiten abgleichen |
| Wer arbeitet mit denselben Daten? | Nur Urs; kleines Team mit gemeinsamer Sicht; getrennte Arbeitsräume |
| Wo soll der Dienst betrieben werden? | Eigener Server; gemanagter Dienst; ausschließlich lokal |
| Was soll der Assistent selbstständig tun? | Suchen und Auskunft; strukturieren; Änderungen; Hintergrundarbeit |

## Abnahmeszenarien des künftigen Mehrgerätebetriebs

- Auf Gerät A angelegte Einträge erscheinen mit denselben Identitäten, Nummern und Beziehungen auf Gerät B.
- Ein erneuter Sendeversuch nach verlorener Antwort erzeugt keinen zweiten Eintrag.
- Gleichzeitige widersprüchliche Änderungen werden sichtbar behandelt.
- Ein Gerätewechsel erhält Kommentare, Hierarchien, Abhängigkeiten und externe Zuordnungen.
- Auf MacBook, iPad und iPhone überstehen ungesendete Änderungen einen Neustart und werden nach Wiederverbindung automatisch korrekt übernommen.
- Offlinezustand, ausstehende Änderungen, letzter bestätigter Abgleich, Fehler und Konflikte sind unterscheidbar.
- Hintergrundverhalten bei aktiver, inaktiver, gesperrter und beendeter Anwendung wird auf den gewählten Systemversionen nachgewiesen.
- Assistentenaktionen laufen unter einer nachvollziehbaren Identität und beachten die festgelegten Rechte.

## Technische Quellen

Am 20. November 2026 geprüft. Die Quellen belegen Plattformfähigkeiten und Protokollmechanismen, nicht die oben vorgeschlagene Produktentscheidung.

- [web.dev: PWA-Installation](https://web.dev/learn/pwa/installation)
- [Apple: Safari-Web-Apps auf dem Mac](https://support.apple.com/en-ie/104996)
- [Apple: Website als App auf dem iPhone](https://support.apple.com/en-az/guide/iphone/iphea86e5236/26/ios/26)
- [RFC 9110, Abschnitt 13.1.1: If-Match](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1)
- [Apple: Choosing Background Strategies for Your App](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app)
- [WebKit: Background-Sync-Position](https://github.com/WebKit/standards-positions/issues/14)
- [WebKit: SyncManager-Implementierungsanfrage](https://bugs.webkit.org/show_bug.cgi?id=182565)
