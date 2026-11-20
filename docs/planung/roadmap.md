# Roadmap

Status: Vorgeschlagene Fortsetzung nach der strukturierten Übernahme am 20. November 2026. Die angelegten GitHub Issues konkretisieren diese Arbeitspakete. Neue Produktfunktionen werden aus den bestätigten Anforderungen abgeleitet.

| Schritt | Inhalt | Ergebnis | Voraussetzung |
|---|---|---|---|
| 1 | Bestätigte Apple-Geräte und Offlinearbeit konkretisieren; Betriebsmodell und Nutzerkreis klären | Mindestversionen, Hintergrundverhalten und vollständige Betriebsanforderungen | Geräte und Offlinebedarf sind bereits festgelegt |
| 2 | Aktivitätsumfang und Abgrenzung Unterprojekte/Themengebiete klären | Aktualisierter fachlicher Katalog | Vorhandenes Modell und Prototyp |
| 3 | Datenhaltung, API, Identitäten und Nummernkreis entwerfen | Entscheidbarer technischer Bauplan mit Migrationsweg | Schritte 1 und 2 |
| 4 | Geräteabgleich, Konflikte, Sicherung und Wiederherstellung spezifizieren | Prüffähige Synchronisations- und Betriebsszenarien | Betriebsanforderungen und Datenvertrag |
| 5 | Ersten durchgängigen Produktpfad implementieren | Verknüpfte Daten auf MacBook, iPad und iPhone, offline bearbeitbar und automatisch abgeglichen | Bauplan und Abgleichregeln |
| 6 | Authentifizierten Assistentenzugang ergänzen | Nachvollziehbare Aktionen über dieselben Geschäftsregeln | Produkt-API und festgelegte Rechte |
| 7 | Kontakte und Kalender, danach weitere Kommunikation anbinden | Echte Informationen in Personen- und Tagessicht | Gewählte Quellen, Identitäten und Feldhoheit |

Schritte 1 und 2 können im Gespräch parallel geklärt werden. Die Integrationsanforderungen werden früh gesammelt; ihre Umsetzung folgt auf die belastbare Datenbasis. Offlinearbeit auf allen drei Apple-Geräten, automatischer Abgleich und sichtbare Statusangaben sind bestätigte Anforderungen und werden von Beginn an im Bauplan berücksichtigt.

## Zugehörige Arbeitspakete

| Issue | Thema | Benötigte Vorentscheidungen |
|---|---|---|
| [#1](https://github.com/ipt01titus/kontext/issues/1) | Bestätigte Geräte/Offlinearbeit konkretisieren; Hintergrundverhalten, Nutzerkreis und Datenort klären | Geräte und Offlinebedarf geklärt |
| [#2](https://github.com/ipt01titus/kontext/issues/2) | Aktivitäten: Zusatzfelder, Status und Zeitangaben verbindlich klären | Keine |
| [#3](https://github.com/ipt01titus/kontext/issues/3) | Kontexte: Unterprojekte und Themengebiete fachlich abgrenzen | Keine |
| [#4](https://github.com/ipt01titus/kontext/issues/4) | Technischen Bauplan für zentrale Datenhaltung, API und Eintragsnummern erstellen | 1, 2 und 3 |
| [#5](https://github.com/ipt01titus/kontext/issues/5) | Geräteabgleich, Konflikte und Wiederherstellung spezifizieren | 1 und 4 |
| [#6](https://github.com/ipt01titus/kontext/issues/6) | Ersten Produktpfad mit Offlinearbeit und Abgleich auf den drei Apple-Geräten umsetzen | 4 und 5 |
| [#7](https://github.com/ipt01titus/kontext/issues/7) | Authentifizierten Assistentenzugang über die Produkt-API planen | 1 und 4 |
| [#8](https://github.com/ipt01titus/kontext/issues/8) | Integrationsumfang für Kontakte, Kalender und Kommunikationskanäle festlegen | Quellenklärung sofort möglich; Umsetzung nach 1, 4 und 5 |

## Vorgehen

Ein Issue hält jeweils eine abgegrenzte Frage oder Änderung fest. Dokumente erklären das zusammenhängende Produkt; Issues enthalten konkrete Aufgaben und Abnahmekriterien. Es gibt zunächst keine automatische Bearbeitung, keinen eingerichteten Agentenworker und keinen automatischen Produktdeploy.

Neue inhaltliche Entscheidungen werden im Katalog und gegebenenfalls als Entscheidungsdokument ergänzt. Pull Requests verbinden Umsetzung, Anforderungen und ausgeführte Prüfung. Die vorhandene CI prüft den Prototyp, nicht die noch zu entwickelnde Serveranwendung.
