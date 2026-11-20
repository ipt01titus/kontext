# Anforderungskatalog

Stand: 20. November 2026. B = bestätigt/angefordert, V = Vorschlag, O = offen. Eine Umsetzung im Prototyp ist eine Erprobung und ersetzt keine fachliche Bestätigung. Die Anforderungen an Apple-Geräte, Offlinearbeit und automatischen Abgleich sind inzwischen bestätigt; ihre technische Umsetzung ist offen.

## Bestätigter fachlicher Kern

| Kennung | Status | Anforderung | Beobachtbares Ergebnis |
|---|---|---|---|
| KTX-001 | B | Fünf eigenständige, miteinander verknüpfbare Geschäftsentitäten | Derselbe Eintrag ist in unterschiedlichen Sichten erreichbar; sein Entitätstyp bleibt eindeutig |
| KTX-002 | B | Projekte sind Kontexte und Filter; Einträge können mehreren Projekten angehören | Eine Person wird beim zweiten Projekt nicht dupliziert |
| KTX-003 | B | Projektübergreifende Personenansicht mit gezieltem Projektfilter | Fall A zeigt Termin, fünf erwartete Rückmeldungen und gemeinsame Ziele über die jeweiligen Projekte |
| KTX-004 | B | Aktivitäten betreffen fachlich mindestens ein Objekt, eine Person oder bereiten ein Ereignis vor | Eine reine Terminvorbereitung ist zulässig; verantwortliche Person oder Arbeitsblock allein ersetzen den Bezug nicht |
| KTX-005 | B | Fehlender fachlicher Aktivitätsbezug wird ausschließlich als „Noch zuzuordnen“ kenntlich gemacht | Name, Schritte und Fälligkeit können vorher erfasst werden; erster fachlicher Bezug entfernt den Hinweis |
| KTX-006 | B | Objekte besitzen Name und Beschreibung sowie Verbindungen und eine Bestandteilsstruktur | Gartenhaus, Fenster und Elektrik sind getrennte Objekte; ein Bestandteil hat höchstens ein Elternobjekt |
| KTX-007 | B | Kontaktaufbau entsprechend iPhone-Kontakten, ergänzt um Vertrauenslevel 0 bis 100 | Mehrfachfelder und Beschriftungen bleiben bei späteren Importen erhalten; der Prototyp bildet erst einen Ausschnitt ab |
| KTX-008 | B | Aktivitätskern: Name, Schritte, Fälligkeitsdatum, Vorgänger/Vorbedingungen und inverse Nachfolger | Eine Vorgängerverbindung erscheint auf der Gegenseite ohne doppelte Pflege |
| KTX-009 | B | Höchstens eine verantwortliche Person je Aktivität | Mehrere Beteiligte oder Rückmeldungsgeber sind davon getrennt möglich |
| KTX-010 | B | Ziele mit Kriterien und Opportunities als Spezialisierung in einer gemeinsamen Zielansicht | Eine Opportunity besitzt zusätzliche Vertriebsangaben und bleibt ein Ziel |
| KTX-011 | B | Ereignisse sind mit den übrigen Entitäten verknüpfbar und können extern entstehen | Ein importierter Termin kann anschließend Personen und Aktivitäten zugeordnet werden |
| KTX-012 | B | Aufgabenkommentare und optionale Dokumentation eines Telefonats | Ein Telefonat kann zwei Aufgaben betreffen; Kommentare sind auch ohne Ereignisdokumentation möglich |
| KTX-013 | B | Gemeinsame Tagessicht für Termine und relevante Aufgaben | Fall B und die Vertriebswiedervorlage aus Fall D sind gemeinsam auffindbar |
| KTX-014 | B | Planung über Vorgänger/Nachfolger sowie Bedarf an Prioritäten und Wiedervorlagen | Abhängigkeit, Wichtigkeit und erneute Aufmerksamkeit bleiben fachlich unterscheidbar; konkrete Aktivitätsfelder siehe offene Fragen |
| KTX-015 | B | Kalender, Kontakte und Kommunikation in den Kontext einbinden | E-Mail, WhatsApp, Telefon und Teams berücksichtigen; Telegram und Signal optional |
| KTX-016 | B | Objektanlage während der Aktivitätsanlage | Die bisherigen Aktivitätseingaben bleiben erhalten; das neue Objekt wird direkt als Bezug ausgewählt |
| KTX-017 | B | Auffindbare Objektbäume und hierarchische Projekte | Unterobjekte/Unterprojekte lassen sich gliedern; „Mein Leben“ kann die persönlichen Bereiche aufnehmen |
| KTX-018 | B | Jeder Eintrag besitzt eine dauerhaft erkennbare Nummer | Ein Eintrag ist über seine Nummer suchbar und nach Umbenennung identifizierbar |
| KTX-019 | B | Assistenten sollen Kontext bedienen können | Die Oberfläche ist bedienbar; eine unabhängige Programmschnittstelle ist als weiterer Bedarf zu konkretisieren |
| KTX-027 | B | Projekt beziehungsweise Kontext während der Personenanlage anlegen | Kontaktdaten und bestehende Projektzuordnungen bleiben erhalten; das neue Projekt ist anschließend zusätzlich ausgewählt. Ein Abbruch der Projektanlage erzeugt keinen Eintrag. |

## Bestätigte Anforderungen an Geräte und Synchronisation

| Kennung | Status | Anforderung | Beobachtbares Ergebnis |
|---|---|---|---|
| KTX-020 | B | Kontext auf MacBook, iPad und iPhone nutzen | Alle drei Geräte gehören zur verbindlichen Ziel- und Testmatrix; konkrete Mindestversionen sind noch festzulegen |
| KTX-021 | B | Fachliche Arbeit auf jedem Gerät auch offline ermöglichen | Vorliegende Einträge und ihre Beziehungen lesen, anlegen und bearbeiten; die Bedienung wartet auf keinen Serverabgleich |
| KTX-022 | B | Änderungen automatisch im Hintergrund abgleichen, sobald die Verbindung es zulässt | Ohne manuellen Start senden und empfangen; nach erfolgreichem Abgleich haben alle erreichbaren Geräte denselben fachlichen Stand |
| KTX-023 | B | Offlinezustand und ausstehende Synchronisation sichtbar anzeigen | Verbindung und Abgleichstand getrennt erkennbar, einschließlich lokal noch nicht übertragener Änderungen |
| KTX-024 | B | Offlineänderungen dauerhaft lokal erhalten | Noch nicht übertragene Änderungen überstehen das Schließen und erneute Öffnen der Anwendung und werden später abgeglichen |
| KTX-025 | B | Unabhängige neue Ergänzungen wie Kommentare automatisch zusammenführen | Zwei offline ergänzte Kommentare bleiben nach dem Abgleich beide am selben Eintrag erhalten |
| KTX-026 | B | Widersprüchliche Änderungen desselben Feldes zur Auswahl anbieten | Beide Varianten bleiben erhalten; eine verständliche Auswahl ermöglicht die Auflösung ohne stillschweigendes Überschreiben |

Der Geräte- und Offlinebedarf ist in [Entscheidung 0003](../entscheidungen/0003-apple-offline-synchronisation.md), die bestätigte Konfliktregel in [Entscheidung 0004](../entscheidungen/0004-synchronisationskonflikte.md) festgehalten. Ein Offlinegerät kann Änderungen anderer Geräte erst nach erneutem Abgleich kennen. Der gewünschte Hintergrundbetrieb bei inaktiver Anwendung bleibt ein maßgebliches Auswahlkriterium; die Einschränkungen von iOS/iPadOS werden nicht als bereits erfüllte Funktion dargestellt. Mindestversionen, genaue Abgleichfristen bei inaktiver/geschlossener App, technische Konflikterkennung und lokale Bereitstellung großer Datenbestände sind noch auszuarbeiten.

### Geklärte bisherige Fragen

| Bisherige Kennung | Festlegung |
|---|---|
| KTX-O01 | Zielgeräte MacBook, iPad und iPhone; siehe KTX-020 |
| KTX-O02 | Offlinearbeit einschließlich Erfassen und Bearbeiten; automatischer späterer Abgleich und sichtbarer Status; siehe KTX-021 bis KTX-024 |

## Bereits erprobte Ausgestaltungen

| Kennung | Status | Ausgestaltung |
|---|---|---|
| KTX-V01 | V | Ein Projektfilter berücksichtigt alle Unterprojekte; Zugehörigkeiten werden nicht auf Elternprojekte kopiert |
| KTX-V02 | V | Projekthierarchie mit höchstens einem direkten Elternprojekt, ohne Kreise |
| KTX-V03 | V | Ein gemeinsamer Nummernkreis über Geschäftseinträge und Projektkontexte; im Prototyp je Browserdatenbestand |
| KTX-V04 | V | Aktivitätsstatus offen, in Arbeit, erledigt; Wartehinweise und blockierte Vorgänger zusätzlich |
| KTX-V05 | V | Schritte als geordnete Checkliste ohne eigene Fälligkeiten und Abhängigkeiten |
| KTX-V06 | V | Vertrauenslevel optional als ganze Zahl; „nicht bewertet“ ist von 0 verschieden |
| KTX-V07 | V | Fälligkeit, Bearbeitungstag, Wiedervorlage und reservierter Arbeitsblock als getrennte Zeitinformationen |
| KTX-V08 | V | Direkte Verbindungen und abgeleitete Zusammenhänge in Sichten unterscheiden |

## Offene Entscheidungen

| Kennung | Frage | Auswirkung |
|---|---|---|
| KTX-O03 | Einzelperson oder gemeinsamer Betrieb mit Team; welche Sichtbarkeit? | Konten, Arbeitsräume, Rechte und Nummernkreis |
| KTX-O04 | Eigenbetrieb, gemanagter Dienst oder vollständig lokaler Betrieb? | Verfügbarkeit, Verantwortlichkeit, Datenort, Sicherung und laufender Betrieb |
| KTX-O05 | Welche Aktivitätsfelder zusätzlich zum bestätigten Kern, mit welchen Werten? | Kanban, Priorität, Wiedervorlage, Bearbeitungstag, Ergebnis und Aufwand |
| KTX-O06 | Wie unterscheiden sich Unterprojekte und Themengebiete? | Kontextmodell und verständliche Navigation |
| KTX-O07 | Welche konkreten Konten und welche Leser-/Schreiberichtungen je Integration? | Kontakte, Kalender, E-Mail und weitere Kanäle |
| KTX-O08 | Wie werden Ziel- und Ereignisergebnisse bewertet? | Beitrag, Realisierung, Prüfung und automatische Statusänderungen |
| KTX-O09 | Welche Agentenaktionen, Rechte und Nachvollziehbarkeit werden benötigt? | Authentifizierte API und späterer MCP-Zugang |
| KTX-O10 | Welchen Umfang haben Export, Sicherung und Wiederherstellung? | Datenportabilität und verlässlicher Gerätewechsel |
| KTX-O11 | Welche Lizenz soll für das öffentliche Repository gelten? | Nutzungs- und Beitragsrahmen des Quellcodes |

Die [Roadmap](../planung/roadmap.md) ordnet diese Fragen und die daraus folgenden Umsetzungsschritte. Der [Implementierungsstand](../status.md) weist die Grenzen des bestehenden Entwurfs aus.
