# Entscheidung 0002 – Hierarchien und erkennbare Einträge

Status: Anforderungen bestätigt; konkrete Ausgestaltung im Prototyp erprobt. Zusammengeführt am 20. November 2026.

## Kontext

Objekte brauchen eine auffindbare Struktur. Auch Projekte sollen hierarchisch organisiert werden können. Der persönliche Bereich aus Microsoft To Do ist ein Referenzbeispiel. Einträge sollen zusätzlich über eine Nummer identifizierbar sein.

## Bestätigte Anforderungen

- Während der Aktivitätsanlage soll ein neues Objekt angelegt und direkt verknüpft werden können.
- Objekte und Projekte benötigen hierarchische Strukturen.
- Jeder Eintrag soll eine erkennbare, bei Umbenennung erhaltene Nummer bekommen.
- Der Assistent soll das Programm bedienen können.

## Erprobte Ausgestaltung

Der Prototyp verwendet aufklappbare Bäume, Suche mit Strukturpfaden und den Kontext „Mein Leben“ mit zwölf persönlichen Bereichen. Die im Referenzbild angezeigten Aufgabenbestände wurden nicht importiert.

Projektfilter umfassen Unterprojekte, ohne Mitgliedschaften zu kopieren. Projekte haben im Prototyp bis zu ein Elternprojekt. Kreisbeziehungen werden verhindert. Die konkrete Gleichsetzung oder Abgrenzung von Themengebieten und Unterprojekten ist offen.

Ein gemeinsamer Nummernkreis wird pro Browserdatenbestand über alle Eintragsarten einschließlich Projektkontexten geführt. Die globale Suche akzeptiert `#42` und `42`. Interne IDs bleiben zusätzlich bestehen. Eine produktive zentrale Vergabe, die Gültigkeit je Arbeitsraum und die Nummernvergabe bei Offlineanlage sind noch zu entscheiden.

## Folgen

Bestehende Daten und Verbindungen werden bei der Erweiterung erhalten. Nummern dürfen bei normaler Bearbeitung nicht neu vergeben werden. Die künftige Übernahme mehrerer unabhängiger Prototypbestände muss mögliche Nummernkollisionen ausdrücklich behandeln.

Die Browserbedienung durch einen Assistenten wurde erprobt. Eigenständige Arbeit ohne geöffneten Browser erfordert einen weiteren authentifizierten Zugangsweg; die konkrete API beziehungsweise MCP-Anbindung ist noch nicht implementiert.
