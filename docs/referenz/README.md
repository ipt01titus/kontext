# Herkunft und Referenzstände

Diese Unterlagen wurden vollständig aus den gemeinsam erarbeiteten Konzeptständen übernommen:

| Dokument | Stand | Bedeutung |
|---|---|---|
| [Anwendungsfälle V0R1](Taetigkeitsstruktur_Anwendungsfaelle_V0R1.md) | 18. November 2026 | Vier Alltagssituationen und erste Ableitungen |
| [Geschäftsentitätenmodell V0R4](Geschaeftsentitaetenmodell_V0R4.md) | 18. November 2026 | Vollständige Attribute, Beziehungen, Kardinalitäten und F/V-Kennzeichnung |

Die Referenzen bleiben als historische Ergebnisse erhalten. Spätere bestätigte Ergänzungen stehen im [aktuellen Katalog](../produkt/anforderungen.md), [aktuellen Datenmodell](../produkt/datenmodell.md) und den Entscheidungen. Frühere Revisionsstände V0R1 bis V0R3 des Modells wurden durch V0R4 zusammengeführt und werden nicht als konkurrierende aktuelle Grundlagen geführt.

## Bekannte spätere Präzisierungen

- Die Anwendungsfälle nennen stellenweise noch zusätzliche Objektzustände. Später wurde das Objekt auf Name und Beschreibung beschränkt.
- Die dort noch offene Elternanzahl eines Objekts wurde später auf höchstens eins festgelegt.
- Eine Aktivität kann auch ausschließlich ein Ereignis vorbereiten; die frühere Kurzdefinition ist entsprechend erweitert.
- Zielattribute wurden in der weiteren Abstimmung bestätigt; zusätzliche Aktivitätsfelder sind weiterhin im Umfang offen.
- Objektanlage aus Aktivitäten, Projekthierarchie, erkennbare Nummern und Bedienbarkeit durch Assistenten wurden nach dem Modellstand ergänzt.

## Prototyp

`prototype/` enthält den am 20. November 2026 veröffentlichten Entwurf aus Site-Commit `a5ef54023aca9063642e9bb614e0f2d416428f80`, einschließlich der bestehenden Tests und README. Site-Projekt: `appgprj_6afe120002f08191844b050519a5015d`.

Die Site-Veröffentlichung hatte einen eigenen Quell- und Bereitstellungsweg. Dieses Repository übernimmt den geprüften Dateistand mit Herkunftsverweis, keine Zugangsdaten oder Browserlaufzeitdaten. Ein automatischer Deploymentpfad aus GitHub ist noch nicht eingerichtet.
