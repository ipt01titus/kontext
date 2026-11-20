# Entscheidung 0004 – Synchronisationskonflikte

Status: **Fachliche Regel am 20. November 2026 bestätigt. Technische Umsetzung noch offen.**

## Kontext

MacBook, iPad und iPhone ermöglichen Offlinearbeit. Dabei können auf mehreren Geräten Ergänzungen oder Änderungen am selben Eintrag entstehen. Urs hat den Vorschlag bestätigt, Ergänzungen wie Kommentare automatisch zusammenzuführen und widersprüchliche Änderungen desselben Feldes zur Auswahl anzubieten.

## Entscheidung

1. Unabhängige neue Ergänzungen wie Kommentare werden automatisch zusammengeführt. Keine dieser Ergänzungen geht beim Abgleich verloren.
2. Bei widersprüchlichen Änderungen desselben Feldes bleiben beide Varianten erhalten. Die Anwendung bietet eine verständliche Auswahl zur Auflösung an.
3. Eine Variante wird nicht stillschweigend durch eine andere überschrieben. Die Geräteuhr entscheidet diesen fachlichen Konflikt nicht allein.

Anforderungen: KTX-025 und KTX-026. Die Regel ergänzt [Entscheidung 0003](0003-apple-offline-synchronisation.md).

## Abnahmebeispiele

| Situation | Erwartetes Ergebnis |
|---|---|
| Auf MacBook und iPhone jeweils einen neuen Kommentar zu derselben Aktivität ergänzen | Beide Kommentare erscheinen nach dem Abgleich an derselben Aktivität |
| Dieselbe Ergänzung nach einem Übertragungsabbruch erneut senden | Sie erscheint einmal; ihr Erhalt wird nicht mit einer zweiten Ergänzung verwechselt |
| Fälligkeit derselben Aktivität auf zwei Geräten offline auf unterschiedliche Tage ändern | Beide Varianten bleiben erhalten, der Konflikt ist sichtbar und eine verständliche Auswahl wird angeboten |
| Konflikt noch nicht entschieden | Keine Variante wird stillschweigend verworfen oder als endgültige Lösung ausgegeben |
| Konflikt bewusst auflösen und Geräte abgleichen | Die gewählte Auflösung wird auf den Geräten konsistent dargestellt |

## Noch auszuarbeiten

Die konkrete Versionierung, Erkennung gleichzeitiger Änderungen und Darstellung der Auswahl werden im Synchronisationskonzept festgelegt. Die automatische Zusammenführung unterschiedlicher Felder ist damit nicht pauschal beschlossen. Auch Löschung gegen Bearbeitung, widersprüchliche Beziehungen, Hierarchiekreise und die gleichzeitige Auflösung desselben Konflikts benötigen eigene Regeln.

Die Umsetzung muss Zusammenführung und wiederholte Übertragungen anhand stabiler Identitäten unterscheiden können. Dies ist eine technische Konsequenz der bestätigten Regel, keine Festlegung auf eine bestimmte Datenbank oder einen bestimmten Synchronisationsalgorithmus.

Die Entscheidung dokumentiert das gewünschte Verhalten. Im bestehenden Prototyp ist die geräteübergreifende Synchronisation weiterhin nicht implementiert.
