# Tätigkeitsstruktur – Anwendungsfälle und fachliche Ableitungen

Version: V0R1  
Stand: 18. November 2026  
Status: Konzeptentwurf zur gemeinsamen Weiterentwicklung

## 1. Zweck und festgehaltener Kern

Das Programm verbindet Objekte, Personen, Aktivitäten, Ziele und Ereignisse. Jede Entität bleibt eigenständig; ihre Beziehungen erschließen den jeweiligen Arbeitszusammenhang.

| Bestandteil | Bedeutung |
|---|---|
| Objekt | Etwas, das zu managen ist: etwa Server, darauf laufende Software, Gartenhaus, Fenster oder Elektrik. |
| Person | Ein Mensch mit Kontaktdaten und weiteren Eigenschaften, etwa Unternehmen und Funktion. |
| Aktivität | Eine Tätigkeit beziehungsweise Aufgabe, die einen Zustand eines Objekts oder einer Person beeinflussen soll. |
| Ziel | Ein angestrebter Zustand, gegebenenfalls mit mehreren beitragenden Aktivitäten. |
| Ereignis | Ein geplanter oder dokumentierter Kalendereintrag, etwa Besprechung, Arbeitstermin oder Telefonat. |
| Projekt | Gemeinsamer Kontext und Filter über die fünf Entitäten. |
| Themengebiet | Untergliederung eines Projekts. |

Projekte und Themengebiete sind fachliche Ordnungsmerkmale. Für ihre technische Verwaltung können später eigene Datensätze nötig sein; dadurch werden sie keine zusätzliche Art von Arbeitsgegenstand.

Objekte können Bestandteile haben und weitere Beziehungen eingehen: Elektrik ist Teil des Gartenhauses; Software läuft auf einem Server. Eine Person kann in mehreren Projekten beteiligt sein und bleibt ein gemeinsamer Kontakt.

Die nachfolgenden Abläufe geben die vier von Urs beschriebenen Situationen wieder. Ergänzende Regeln sind als Vorschläge formuliert und noch keine abschließend beschlossenen Anforderungen.

### Gemeinsame Sichten

| Entität | Grundsicht |
|---|---|
| Objekte | Objektliste beziehungsweise Objektstruktur |
| Personen | Kontaktliste und Personenansicht |
| Aktivitäten | Aufgabenliste und Kanban-Board |
| Ziele | Gemeinsame Zielansicht einschließlich aller Spezialisierungen |
| Ereignisse | Kalender |

Die Zielansicht zeigt auch Opportunities als Spezialisierung von Zielen. Ein Filter nach Zieltyp und passende Felder oder Darstellungen ermöglichen die Vertriebsplanung innerhalb dieser gemeinsamen Sicht. Die Tagessicht führt Ereignisse und Aufgaben zusammen; die Projektansicht erschließt die fünf Entitäten unter einem gemeinsamen Projektfilter.

## 2. Situation A: Eine Person ruft an

### Gewünschtes Ergebnis

Urs kann die aktuellen Zusammenhänge mit der Person unmittelbar überblicken und im Gespräch handeln: Termine, ausstehende Rückmeldungen, gemeinsame Ziele und betroffene Gegenstände.

### Ablauf

1. Person über die Suche oder Kontaktliste aufrufen.
2. Die Übersicht zeigt beispielsweise den gemeinsamen Termin am folgenden Tag, fünf offene Aufgaben mit ausstehender Rückmeldung dieser Person und das gemeinsame Ziel, die Holzschneiderei vertrieblich erfolgreich zu machen.
3. Die Einträge tragen ihre jeweiligen Projekt- und Themenzuordnungen. Von jedem Eintrag kann die betreffende Aufgabe, das Ziel, Objekt oder Ereignis geöffnet werden.
4. Während oder nach dem Gespräch in zwei bestehenden Aufgaben Kommentare ergänzen.
5. Falls sinnvoll, das Telefonat nachträglich als Ereignis dokumentieren und mit Person und besprochenen Aufgaben verknüpfen.
6. Aus neuen Vereinbarungen gegebenenfalls eine Aufgabe oder eine Wiedervorlage anlegen.

### Fachliche Ableitungen

- „Mit dieser Person verbunden“ muss nach Rolle unterscheidbar sein: zuständig, ausführend, beteiligt oder Person, von der eine Rückmeldung erwartet wird.
- Eine ausstehende Rückmeldung braucht eine konkrete Bezugsperson. Die Person kann eine andere sein als die Person, die die Aufgabe insgesamt verantwortet.
- Kommentare gehören zu den jeweiligen Aufgaben und erhalten Autor und Zeitpunkt. Kommentare sind ergänzende Informationen zu den fünf Entitäten.
- Die Dokumentation eines Telefonats ist optional. Aufgaben können unabhängig davon kommentiert werden.
- Ein vergangenes Telefonat kann als Ereignis erfasst werden. Geplante und stattgefundene Ereignisse sind unterscheidbar.
- Ein Kommentar oder ein vergangener Termin erledigt eine Aufgabe nicht automatisch.
- Vorschlag: Eine über die globale Suche geöffnete Person startet mit allen Projekten. Ein bewusst eingeschalteter Projektfilter bleibt deutlich sichtbar und kann schnell aufgehoben werden.

### Prüffälle für den späteren Entwurf

- Bei einer Person mit Verbindungen zu zwei Projekten erscheinen die relevanten offenen Punkte beider Projekte.
- Der Termin am folgenden Tag ist sofort erkennbar.
- Die fünf ausstehenden Rückmeldungen sind von Aufgaben unterscheidbar, die lediglich dieselbe Person erwähnen.
- Zwei Kommentare landen in den beiden ausgewählten Aufgaben und sind dort später wieder auffindbar.
- Das Gespräch kann ohne Ereignisdokumentation beendet werden; eine optionale Dokumentation erzeugt genau ein verknüpftes Ereignis.

## 3. Situation B: Morgens den Tag überblicken

### Gewünschtes Ergebnis

Eine Tagessicht führt die zeitlichen Verpflichtungen und die für den Tag relevanten Aufgaben zusammen.

### Vorgeschlagener Aufbau

| Bereich | Inhalt |
|---|---|
| Zeitplan | Ereignisse mit Uhrzeit, etwa Termine und eingeplante Arbeitsblöcke |
| Heute bearbeiten | Aufgaben, für die heute als Bearbeitungstag festgelegt wurde |
| Heute fällig | Aufgaben mit verbindlichem Fälligkeitsdatum heute |
| Wiedervorlagen | Aufgaben, die heute wieder Aufmerksamkeit brauchen |
| Überfällig | Weiterhin offene Aufgaben mit überschrittener Fälligkeit |

Diese Bereiche sind zunächst ein Vorschlag für eine gemeinsame Tagesansicht. Eine Aufgabe kann mehrere Relevanzgründe besitzen; sie soll als derselbe Eintrag mit entsprechenden Hinweisen erkennbar bleiben.

### Unterscheidung der Zeitangaben

| Zeitangabe | Aussage | Beispiel |
|---|---|---|
| Fälligkeit | Bis wann muss das Ergebnis vorliegen? | Angebot bis Freitag versenden |
| Bearbeitungstag | An welchem Tag möchte ich daran arbeiten? | Angebot am Mittwoch vorbereiten |
| Wiedervorlage | Wann soll die Aufgabe erneut Aufmerksamkeit bekommen? | Mittwoch nach einer Rückmeldung sehen |
| Ereignis / Arbeitsblock | Wann findet etwas statt oder ist Arbeitszeit reserviert? | Mittwoch 10 bis 11 Uhr Angebot bearbeiten |

### Fachliche Ableitungen

- Aufgaben ohne konkrete Uhrzeit können in der Tagessicht erscheinen, ohne als Kalendertermin angelegt werden zu müssen.
- Eine Aktivität kann mehrere Arbeitsblöcke haben; diese Ereignisse verweisen auf dieselbe Aktivität.
- Ein Arbeitsblock und die dazugehörige Aufgabe sollen als zusammengehörig erkennbar sein.
- Ein Wiedervorlagedatum ist unabhängig vom Bearbeitungsstatus. Es kann sowohl einer wartenden als auch einer noch nicht begonnenen Aufgabe gehören.
- Blockierte Aufgaben bleiben sichtbar, wenn sie heute relevant sind; der Grund ist erkennbar.
- Projekt- und Themenfilter gelten auch für die Tagessicht. Für den Tagesbeginn ist die projektübergreifende Ansicht der Ausgangspunkt.
- Noch offen: Umgang mit unerledigten Aufgaben des Vortags. Vorschlag: sichtbar lassen und bewusst neu planen; die ursprüngliche Fälligkeit erhalten.

### Prüffälle für den späteren Entwurf

- Ein Termin um 10 Uhr, eine heute fällige Aufgabe ohne Uhrzeit und ein heute wiedervorgelegtes Telefonat sind gemeinsam auffindbar.
- Dieselbe Aufgabe erscheint nicht als mehrere unabhängige Aufgaben, wenn sie heute fällig und wiedervorgelegt ist.
- Ein verstrichener Arbeitsblock markiert seine Aufgabe nicht automatisch als erledigt.
- Für eine überfällige Aufgabe bleibt die ursprüngliche Fälligkeit erkennbar.

## 4. Situation C: Am Gartenhaus weiterplanen

### Gewünschtes Ergebnis

Urs betrachtet das Projekt Gartenhaus, sieht die zugehörigen Objekte und plant die nächsten Schritte mit Abhängigkeiten und Prioritäten.

### Ablauf

1. Projekt „Gartenhaus“ öffnen.
2. Objektübersicht betrachten, beispielsweise Gartenhaus mit den Bestandteilen Fenster und Elektrik.
3. Ein Objekt öffnen und vorhandene Eigenschaften, Zustandsinformationen und offene Aktivitäten sehen.
4. Weitere Aktivitäten anlegen und mit den betroffenen Objekten verbinden.
5. Vorgänger-Nachfolger-Beziehungen setzen.
6. Bei Bedarf Prioritäten vergeben.
7. Zwischen Objektübersicht, Aufgabenliste und Kanban wechseln; der Projektfilter bleibt erhalten.

### Beispiel für eine Abhängigkeit

„Leitungsführung abstimmen“ muss abgeschlossen sein, bevor „Leitungen verlegen“ beginnen kann. „Leitungen verlegen“ muss abgeschlossen sein, bevor „Innenverkleidung schließen“ beginnen kann.

Diese Aufgaben und ihre Beziehungen sind illustrative Beispieldaten, keine tatsächliche Bauplanung.

### Fachliche Ableitungen

- „Gartenhaus“ kann der Name des Projektkontexts und des konkreten Objekts sein. Der Projektkontext umfasst alle zugeordneten Einträge; das Objekt besitzt Eigenschaften, Bestandteile und Zustandsinformationen.
- Eine Aktivität kann mehrere betroffene Objekte und mehrere beteiligte Personen haben.
- Vorgänger-Nachfolger-Beziehungen verbinden Aktivitäten. Sie können auch projektübergreifend sinnvoll sein.
- Vorschlag für den Anfang: Eine Nachfolgeraufgabe wird ausführbar, wenn alle zwingenden Vorgänger erledigt sind. Komplexere Abhängigkeitstypen bleiben einer späteren Entscheidung vorbehalten.
- Priorität und Abhängigkeit bleiben eigenständige Informationen. Eine hohe Priorität hebt eine Blockierung nicht auf.
- Vorschlag: Direkte oder indirekte Abhängigkeitskreise werden beim Anlegen verhindert und verständlich erklärt.
- Objektunterstrukturen haben keine Kreise. Die genaue Zahl erlaubter Elternobjekte bleibt im Fachkonzept zu entscheiden.
- Die Übersicht eines übergeordneten Objekts kann Aufgaben seiner Bestandteile einbeziehen. Die Herkunft ist dabei erkennbar.
- Vorschlag: Ein erledigter Vorgänger macht den Nachfolger verfügbar; er startet und terminiert ihn nicht automatisch.
- Objektzustände werden bei Bedarf aktualisiert. Ein einzelnes erledigtes Teilstück setzt nicht ungeprüft das gesamte Gartenhaus auf einen fertigen Zustand.

### Prüffälle für den späteren Entwurf

- Auf Projektebene sind die Aufgaben an Fenstern und Elektrik auffindbar.
- Eine Aufgabe mit offenem zwingendem Vorgänger zeigt die Blockierung samt Ursache.
- Ein Versuch, einen Abhängigkeitskreis zu erzeugen, wird verhindert.
- Nach Erledigung aller zwingenden Vorgänger ist die Nachfolgeraufgabe als ausführbar erkennbar.
- Eine priorisierte, blockierte Aufgabe bleibt von einer ausführbaren Aufgabe unterscheidbar.

## 5. Situation D: Vertrieb für die WATA Academy planen

### Gewünschtes Ergebnis

Urs sieht die konkreten Vertriebsziele beziehungsweise Opportunities, die verbundenen Personen und die nächsten Schritte einschließlich Wiedervorlagen.

### Ablauf

1. Projekt „WATA Academy“ wählen und die Zielansicht öffnen.
2. Opportunities mit zugehörigen Personen und offenen Aktivitäten überblicken.
3. Eine Opportunity öffnen und angestrebtes Ergebnis, aktuellen Stand und nächsten Schritt sehen.
4. Für ein geplantes Telefonat die Aktivität bearbeiten oder eine solche anlegen.
5. Eine Wiedervorlage setzen.
6. Am betreffenden Tag erscheint das Telefonat in der Tagessicht.
7. Gesprächsergebnis als Kommentar festhalten, nächste Schritte ergänzen und den Opportunity-Stand bei Bedarf aktualisieren.

### Festgelegte Modellierung

Eine Opportunity ist eine Spezialisierung eines Ziels und wird innerhalb der Entität Ziele geführt. Die Vertriebsplanung findet in der gemeinsamen Zielansicht statt. Dort kann nach Opportunities gefiltert werden; die Spezialisierung kann passende Eigenschaften und Vertriebsphasen erhalten. Damit bleibt das Grundmodell bei fünf Entitäten.

Beispiel: „Person X bucht einen Academy-Workshop“ ist ein gewünschter Zielzustand. „Person X anrufen“ ist eine beitragende Aktivität. Wird dafür eine feste Uhrzeit vereinbart, kommt ein verknüpftes Ereignis hinzu.

### Mögliche Eigenschaften einer Opportunity

- Angestrebtes Ergebnis beziehungsweise angebotenes Leistungsangebot
- Verbundene Personen mit Rollen, etwa Ansprechpartner oder Entscheider
- Vertriebsphase
- Optional erwarteter Auftragswert und erwarteter Entscheidungszeitpunkt
- Offene Aktivitäten einschließlich Wiedervorlagen
- Ergebnis, etwa gewonnen, verloren oder zurückgestellt

Die konkreten Felder und Phasen sind noch festzulegen. Ziele können ergänzende Eigenschaften je nach Typ erhalten.

### Prüffälle für den späteren Entwurf

- Allgemeine Ziele und Opportunities sind in derselben Zielansicht zugänglich; ein Zieltypfilter grenzt die angezeigten Ziele ein.
- Zu einer Opportunity sind die verbundenen Personen und offenen nächsten Schritte auffindbar.
- Dieselbe Person kann mit mehreren Opportunities verknüpft sein, ohne mehrfach als Kontakt angelegt zu werden.
- Ein Telefonat auf Wiedervorlage braucht keine vorgetäuschte Uhrzeit im Kalender.
- Ein fest vereinbartes Telefonat ist als Ereignis mit derselben Aktivität und Opportunity verbunden.
- Der Abschluss einer einzelnen Vertriebsaktivität aktualisiert den Zielerfolg nicht ungeprüft.

## 6. Kalender, E-Mail und Kommunikationskanäle

Die Integration gehört zu den Anforderungen. Die relevanten Kommunikationskanäle sind festgelegt; konkrete Konten, gewünschter Funktionsumfang und technische Möglichkeiten sind noch zu klären.

### Festgelegte Kommunikationskanäle

| Kanal | Einordnung |
|---|---|
| E-Mail | Relevanter Kommunikationskanal |
| WhatsApp | Relevanter Kommunikationskanal |
| Telefon | Relevanter Kommunikationskanal; Gesprächsdokumentation nach Bedarf |
| Microsoft Teams | Relevanter Kommunikationskanal |
| Telegram | Optional zu berücksichtigen |
| Signal | Optional zu berücksichtigen |

Die fachliche Berücksichtigung der Kanäle ist festgelegt. Ob und in welchem Umfang pro Kanal Nachrichten angezeigt, verknüpft, übernommen oder gesendet werden sollen und können, ist im Integrationskonzept zu bestimmen.

| Bereich | Gewünschter Nutzen | Noch festzulegen |
|---|---|---|
| Kontakte | Vorhandene Personen mit Kontaktdaten verwenden | Quellen, Erkennung gleicher Personen, Änderungsrichtung |
| Kalender | Vorhandene Ereignisse in Tages- und Personenansicht einbeziehen | Konten, Kalenderauswahl, Lese- und Schreibumfang |
| E-Mail | Gesprächszusammenhang zugänglich machen und Aufgaben aus Nachrichten ableiten | Postfächer, manuelle oder automatische Zuordnung, Kopie oder Verweis |
| WhatsApp, Telefon und Microsoft Teams; optional Telegram und Signal | Relevante Nachrichten und Gesprächsergebnisse in den Kontext einordnen | Konten, gewünschter Umfang und jeweils mögliche Integration |

### Vorgeschlagene Grundregeln

- Eine E-Mail oder Nachricht kann als Quelle beziehungsweise ergänzender Inhalt an vorhandene Entitäten angehängt oder mit ihnen verlinkt werden. Das fachliche Modell bleibt bei den fünf Entitäten.
- Aus einer Nachricht kann gezielt eine Aktivität entstehen; die ursprüngliche Nachricht bleibt als Quelle erreichbar, soweit die jeweilige Anbindung das erlaubt.
- Vorschläge für Zuordnungen können sich aus Absender, Empfängern und bestehenden Verbindungen ergeben. Eine sichere Projektzuordnung allein aus der Person ist bei mehreren gemeinsamen Kontexten nicht immer möglich.
- Bei importierten Terminen sollen Personen, Aktivitäten, Objekte und Ziele nachträglich verknüpft werden können, ohne einen zweiten Termin anzulegen.
- Die Anbindung braucht eine stabile Zuordnung zu den Originaleinträgen, damit wiederholtes Einlesen keine Duplikate erzeugt.
- Änderungen und Löschungen aus anderen Systemen benötigen festgelegte Regeln. Insbesondere darf eine Terminlöschung keine zugehörige Aufgabe löschen.
- Das Dokumentieren eines Telefonats bleibt eine bewusste, optionale Handlung.
- Vor einer automatischen Anruferkennung oder einer kanalübergreifenden Nachrichtenübernahme ist die konkrete technische Machbarkeit zu prüfen.

### Vorschlag für die Reihenfolge

1. Quellen und gewünschten Umfang bestimmen.
2. Kontakte und Kalender für die vier Anwendungsfälle anbinden.
3. E-Mails gezielt zuordnen und daraus Aktivitäten erstellen.
4. Weitere Kommunikationskanäle nach tatsächlichem Nutzen und technischer Machbarkeit ergänzen.

## 7. Übergreifende Anforderungen aus den vier Situationen

| Kennung | Anforderung | Herkunft |
|---|---|---|
| Q-01 | Person über alle gemeinsamen Projekte hinweg betrachten und gezielt filtern | A |
| Q-02 | Direkte Verbindungen und indirekt gefundene Zusammenhänge erkennbar machen | A, C, D |
| Q-03 | Erwartete Rückmeldung mit einer konkreten Person verbinden | A |
| Q-04 | Aufgaben kommentieren und optional vergangene Ereignisse dokumentieren | A |
| Q-05 | Tagessicht mit Terminen und zeitlich relevanten Aufgaben anbieten | B, D |
| Q-06 | Fälligkeit, Bearbeitungstag, Wiedervorlage und Arbeitsblock trennen | B, D |
| Q-07 | Objekte gliedern und ihre Aktivitäten im Projektkontext betrachten | C |
| Q-08 | Aufgaben mit Vorgängern, Nachfolgern und unabhängiger Priorität planen | C |
| Q-09 | Ziele einschließlich Opportunities in einer gemeinsamen Zielansicht mit Personen und nächsten Aktivitäten verbinden | D |
| Q-10 | Externe Kontakte, Termine und Kommunikation aus E-Mail, WhatsApp, Telefon und Microsoft Teams; optional Telegram und Signal zuordnen können | A–D |

## 8. Nächster Konzeptionsschritt

Aus diesem Arbeitsstand entsteht ein kompaktes Fachkonzept mit einem gemeinsamen Beispieldatensatz für die vier Situationen. Er enthält mindestens eine Person in zwei Projekten, fünf ausstehende Rückmeldungen, einen gemeinsamen Termin, ein gemeinsames Ziel, das Gartenhaus mit zwei Bestandteilen und eine Opportunity mit Wiedervorlage.

An diesem Datensatz werden anschließend die Personenansicht, die Tagessicht, der Projektüberblick und die gemeinsame Zielansicht einschließlich Opportunities als zusammenhängender bedienbarer Entwurf geprüft.

Offene Entscheidungen mit größerer Auswirkung:

1. Welche Konten und Kalender sollen angebunden werden, und welcher Funktionsumfang wird je festgelegtem Kommunikationskanal benötigt?
2. In welcher Reihenfolge sollen die Anbindungen umgesetzt werden?
3. Welche Zielkriterien, Prioritätsstufen und Vertriebsphasen braucht der Anfang?
4. Wie sollen Zustandsinformationen an Objekten erfasst werden: zunächst als Beschreibung oder bereits als frei definierbare Felder?

Diese Entscheidungen können überwiegend beim Fachkonzept und am Entwurf getroffen werden; sie blockieren die Ausarbeitung der vier Anwendungsfälle nicht.
