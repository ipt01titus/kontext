# Gemeinsam an Kontext arbeiten

## Anforderungen weiterentwickeln

Jede Anforderung erhält eine Kennung im [Anforderungskatalog](docs/produkt/anforderungen.md). Ein Issue beschreibt die konkrete Frage oder Änderung, ihren Nutzen und beobachtbare Abnahmekriterien. Eine GitHub-Issue-Nummer ersetzt diese fachliche Kennung nicht.

Entscheidungen mit längerfristiger Wirkung werden unter `docs/entscheidungen/` festgehalten: Kontext, Entscheidung, Status und Folgen. Neue Vorschläge werden erst nach inhaltlicher Bestätigung als beschlossen gekennzeichnet. Historische Unterlagen werden nicht stillschweigend umgeschrieben.

## Änderungen umsetzen

Nach der erstmaligen Übernahme erfolgen abgegrenzte Änderungen auf einem Branch mit Pull Request. Die Beschreibung erläutert das resultierende Verhalten, die zugehörige Anforderung und die tatsächlich ausgeführte Prüfung. Umfangreiche Änderungen werden in prüfbare Teile gegliedert.

Der aktuelle Entwurf benötigt keine Installation von npm-Paketen. `npm run check` prüft JavaScript-Syntax; `npm test` prüft Migration, Hierarchiefilter und stabile Nummern. Die Automatisierung ersetzt keine Prüfung der Benutzerabläufe. Bei Änderungen an den Oberflächen die betroffenen Abläufe und passende Bildschirmgrößen gezielt prüfen.

## Betriebsdaten und Veröffentlichung

Das Repository enthält Quellcode, Dokumentation und Beispieldaten. Kontakte, persönliche Notizen, Kontozugänge und echte Kalenderdaten gehören in die spätere Datenhaltung. Die lokale Browserspeicherung des Prototyps wird nicht mit Git synchronisiert.

GitHub ist ab dieser Übernahme die gemeinsame Grundlage der Weiterentwicklung. Der bestehende veröffentlichte Site-Entwurf besitzt noch einen eigenen Veröffentlichungsweg. Ein automatischer Produktdeploy aus diesem Repository ist noch nicht eingerichtet. Betriebsmodell und Veröffentlichung werden im Architekturarbeitspaket entschieden.

Eine Quellcodelizenz wird vom Projektverantwortlichen festgelegt; die öffentliche Sichtbarkeit des Repositorys beantwortet diese Frage nicht.
