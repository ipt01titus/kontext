# Entscheidung 0001 – Fachlicher Kern

Status: Bestätigte Ergebnisse aus dem Konzeptionsgespräch, zusammengeführt am 20. November 2026.

## Kontext

Kalender, Aufgaben, CRM und Ziele sollen aus unterschiedlichen Blickrichtungen denselben Arbeitszusammenhang erschließen. Unklare Vermischungen der Arbeitsgegenstände sollen vermieden werden.

## Festgehaltene Entscheidungen

1. Die fünf Geschäftsentitäten sind Objekt, Person, Aktivität, Ziel und Ereignis.
2. Projekte dienen als Kontexte und Filter; Themengebiete bilden deren Unterstruktur. Die technische Verwaltung eines Kontexts macht ihn nicht zu einer sechsten Geschäftsentität.
3. Eine Person bleibt über mehrere Projekte hinweg derselbe Kontakt. Unternehmen und Funktion gehören zunächst zu den Kontaktdaten.
4. Opportunities sind eine Spezialisierung von Zielen und werden in der gemeinsamen Zielansicht geführt.
5. Der fachliche Aktivitätsbezug besteht zu Objekt, betroffener Person oder vorzubereitendem Ereignis. Bei fehlender konkreter Zuordnung wird „Noch zuzuordnen“ angezeigt.
6. Ein Arbeitsblock und die Vorbereitung eines Ereignisses sind unterschiedliche Beziehungen.
7. Objekte haben Name und Beschreibung; Bestandteile besitzen höchstens ein direktes Elternobjekt. Je Aktivität gibt es höchstens eine verantwortliche Person.
8. Kommentare und optionale Gesprächsdokumentation ergänzen den Arbeitszusammenhang.

## Folgen

Beziehungen brauchen eine fachliche Bedeutung. Gemeinsame Projektmitgliedschaft allein begründet weder Verantwortlichkeit noch eine erwartete Rückmeldung. Die Ansichten greifen auf dieselben Identitäten zu.

Weitere Kardinalitäten, Rollenwerte und Lebenszyklusregeln sind nur insoweit beschlossen, wie der [Anforderungskatalog](../produkt/anforderungen.md) und das [Datenmodell](../produkt/datenmodell.md) dies kennzeichnen. Diese Entscheidung legt keinen technischen Framework- oder Datenbankentwurf fest.
