# Hinweise für Entwicklungsassistenten

## Orientierung

Vor fachlichen Änderungen `docs/produkt/anforderungen.md`, `docs/produkt/datenmodell.md` und `docs/status.md` lesen. Zugehörige Entscheidungen unter `docs/entscheidungen/` beachten. Die Unterlagen unter `docs/referenz/` sind historische Quellen; spätere bestätigte Entscheidungen im aktuellen Katalog haben Vorrang.

## Fachlicher Kern

- Fünf Geschäftsentitäten getrennt führen: Objekt, Person, Aktivität, Ziel, Ereignis.
- Projekte bleiben Kontexte und Filter. Opportunities bleiben Ziele.
- Eine verantwortliche Person allein erfüllt den fachlichen Bezug einer Aktivität nicht. Ein Objekt, eine betroffene Person oder ein vorzubereitendes Ereignis erfüllt ihn. Fehlt jeder solche Bezug, gilt „Noch zuzuordnen“.
- Stabile Identitäten und Eintragsnummern bei Umbenennung oder Verschiebung erhalten.
- Hierarchien und Aufgabenabhängigkeiten kreisfrei halten; vorhandene Daten bei Migrationen erhalten.
- Vorschläge, Beispielverhalten und bestätigte Anforderungen unterscheidbar halten.

## Umsetzung

Den Umfang des jeweiligen Auftrags umsetzen. Keine neue Framework-, Hosting- oder Synchronisationsentscheidung als bereits beschlossen voraussetzen. `prototype/` ist ein übernommener Entwurf, keine Festlegung der Produktarchitektur. Änderungen an Geschäftsdaten, Integrationen und Geräteabgleich benötigen passende Prüfungen ihrer tatsächlichen Auswirkungen.

`npm run check` und `npm test` prüfen den aktuellen Prototyp. Bei einer Änderung der Bedienung zusätzlich den betroffenen Ablauf im verfügbaren Browser prüfen und die Grenzen der Prüfung benennen. Keine externe Kommunikation durch den Prototyp behaupten; die Kanäle sind noch nicht angebunden.

## Verlässliche Fortsetzung

Zu Beginn Arbeitsumgebung, Git-Status und den konkreten Issue-Stand prüfen. Fremde oder uncommittete Änderungen erhalten. Ergebnisse und verbleibende Blocker am passenden Issue beziehungsweise Dokument festhalten. Eine lokale Änderung ist erst dann in GitHub verfügbar, wenn sie dort erfolgreich gespeichert wurde. GitHub-Veröffentlichung und Produktdeployment getrennt behandeln.

Die Zusammenarbeit erfolgt auf Deutsch, Quellcode darf etablierte englische Namen verwenden. Keine produktiven Datensätze oder Zugangsdaten ins Repository übernehmen.
