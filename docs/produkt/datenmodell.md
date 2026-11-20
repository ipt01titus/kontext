# Aktuelles fachliches Datenmodell

Stand: 20. November 2026. Grundlage ist das vollständige [Geschäftsentitätenmodell V0R4](../referenz/Geschaeftsentitaetenmodell_V0R4.md) mit den danach besprochenen Ergänzungen. Dieses Dokument dient der Orientierung; die Attributtabellen und qualifizierten Beziehungen der Referenz bleiben erhalten. Bestätigte Regeln und Vorschläge werden nicht gleichgesetzt.

## Entitäten und Attribute

| Entität | Bestätigter Kern | Noch zu konkretisieren / Grenze des Prototyps |
|---|---|---|
| Objekt | Name, Beschreibung; bis zu ein direktes Elternobjekt; weitere Beziehungen | Keine zusätzlichen Objektfelder wie Typ oder aktueller Zustand vereinbart |
| Person | Kontaktstruktur der iPhone-Kontakte; Vertrauenslevel 0–100 | Vollständige Mehrfachfelder, Bilder und Import fehlen im Prototyp; optionale Ganzzahl und leerer Wert sind Vorschläge |
| Aktivität | Name, Schritte, Fälligkeitsdatum, Vorgänger/Vorbedingungen, inverse Nachfolger | Zusätzliche Angaben zu Status, Priorität, Wiedervorlage, Bearbeitungstag und Ergebnis noch abzustimmen |
| Ziel | Zielformulierung, Zieltyp, Erfolgskriterien, Status, Zieltermin, Priorität, Messgrößen, Ergebnisbewertung und Abschlusszeitpunkt | Die Oberfläche bildet nicht alle bestätigten Zielattribute vollständig ab |
| Ereignis | Zeitlich eingeordnetes geplantes oder dokumentiertes Geschehen mit Bezügen zu anderen Einträgen | Getrennte Plan-/Istzeiten, Zeitzonen und Wiederholungen sind im Produkt sauber auszuarbeiten |

Bestätigte Zielstatus: offen, in Verfolgung, pausiert, erreicht, beendet ohne Erreichung. Eine Opportunity ergänzt angebotene Leistung, Vertriebsphase, erwarteten Auftragswert mit Währung und erwartete Entscheidung. Sie erhält keine zweite Identität und keine getrennte gleichrangige CRM-Entität.

## Beziehungen

| ID | Verbindung | Regel / Einordnung |
|---|---|---|
| R01 | Objekt ist Teil von Objekt | Höchstens ein Elternobjekt bestätigt; kreisfreie Baumdarstellung im Entwurf |
| R02 | Objekt läuft auf / benötigt Objekt | Sachbeziehung getrennt von der Bestandteilsstruktur |
| R03 | Aktivität betrifft Objekt | Einer der möglichen fachlichen Aktivitätsbezüge |
| R04 | Aktivität betrifft Person | Betroffenheit ist von Mitwirkung zu unterscheiden |
| R05 | Person wirkt an Aktivität mit | Rollen wie verantwortlich, ausführend, beteiligt; höchstens eine verantwortliche Person |
| R06 | Rückmeldung einer Person zu Aktivität erwartet | Qualifizierte Verbindung mit Inhalt, Status und Zeitangaben vorgeschlagen |
| R07 | Person verantwortet / betreut Objekt | Rolle an der Verbindung |
| R08 | Aktivität ist Vorgänger von Aktivität | Vorgänger und Nachfolger sind inverse Sichten einer Beziehung; keine Kreise |
| R09 | Ziel beschreibt Zustand eines Objekts | Optionaler Objektbezug |
| R10 | Person steht mit Ziel in Verbindung | Beispielsweise mitverfolgend, Ansprechpartner oder Entscheider |
| R11 | Aktivität trägt zu Ziel bei | Abschluss einer Aktivität bestätigt nicht automatisch Zielerreichung |
| R12 | Person nimmt an Ereignis teil | Organisator-/Teilnehmerrolle und Teilnahmeantwort vorgeschlagen |
| R13 | Ereignis dient Durchführung/Besprechung einer Aktivität | Beschreibt beispielsweise einen Arbeitsblock |
| R14 | Ereignis betrifft Objekt | Direkter Gegenstandsbezug |
| R15 | Ereignis trägt zu Ziel bei / realisiert / prüft es | Direkter Zielbezug bestätigt; konkrete Ergebnisrollen vorgeschlagen |
| R16 | Ziel unterstützt übergeordnetes Ziel | Optionale spätere Ergänzung, keine bereits zugesagte Zielhierarchie |
| R17 | Aktivität bereitet Ereignis vor | Fachlicher Aktivitätsbezug; von R13 zu unterscheiden |

Viele Beziehungen erlauben mehrere Gegenstellen. Die detaillierten Kardinalitäten in V0R4 sind Vorschläge, soweit sie dort nicht ausdrücklich als festgelegt markiert sind.

## Wesentliche Konsistenzregeln

- Jede Aktivität betrifft fachlich mindestens ein Objekt, eine Person oder ein vorzubereitendes Ereignis. Fehlen diese konkreten Verbindungen im gespeicherten Eintrag, lautet der Hinweis „Noch zuzuordnen“.
- Eine verantwortliche Person, Projektzugehörigkeit, ein Zielbezug oder ein Arbeitsblock allein beseitigt diesen Hinweis nicht.
- Die Aktivität „Agenda vorbereiten“ kann einen Termin vorbereiten und zugleich am Vortag in einem anderen Ereignis als Arbeitsblock geplant werden.
- Dasselbe Telefonat kann mehrere Aktivitäten besprechen. Dokumentation des Telefonats, Aufgabenkommentar, beantwortete Rückmeldung und erledigte Aktivität sind unabhängige Aussagen.
- Gemeinsame Projektzugehörigkeit erzeugt keine direkte fachliche Beziehung und kopiert keine Projektmitgliedschaften.
- Zielerreichung folgt aus dem Ergebnis und den Kriterien. Ein stattgefundenes Ereignis oder viele erledigte Aufgaben beweisen sie nicht allein.

## Gemeinsamer Kern und Kontextstruktur

Alle fünf Entitäten brauchen eine stabile Identität. Kommentare, Quellen und Herkunftsinformationen ergänzen sie. Änderungsmetadaten und Archivierung sind in V0R4 vorgeschlagen und im Produkt auszuarbeiten. Ein Kontakt benötigt kein Benutzerkonto; ein späterer Benutzer kann zugleich als Person geführt werden.

Seit dem 20. November ist die sichtbare Eintragsnummer zusätzlich angefordert. Der Prototyp vergibt sie einmal und erhält sie bei Umbenennung oder Verschiebung. Die produktive Identität sollte unabhängig von einer menschenlesbaren Nummer funktionieren; Nummernkreis und Vergabe bei Offlineanlage sind Architekturentscheidungen.

Projekte gliedern Kontexte hierarchisch. Ein Projektfilter schließt im Prototyp seine Nachkommen ein. Personen, Objekte, Aktivitäten, Ziele und Ereignisse können mehreren Projekten angehören. Die bisherige Themengebietsstruktur wird dadurch nicht stillschweigend ersetzt; ihre Abgrenzung ist offen.

## Externe Identitäten

Ein importierter Kontakt oder Termin benötigt Herkunft, Konto und externe Kennung, gegebenenfalls zusätzlich eine Wiederholungsinstanz. Die externe Kennung ist von interner Identität und sichtbarer Eintragsnummer verschieden. Wiederholter Import soll aktualisieren statt duplizieren. Ein eindeutiger E-Mail-Treffer kann eine Person zuordnen; Mehrdeutigkeiten bleiben zur Klärung sichtbar. Eine externe Terminlöschung darf keine verknüpfte Aktivität löschen.

Der technische Datenbankentwurf ist noch nicht beschlossen. Das flache JSON-Modell des Prototyps dient der Interaktionserprobung.
