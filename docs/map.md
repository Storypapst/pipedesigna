# Wayfinder-Karte: pipedesigna

Stand: 2026-10-05, nach Grill-Runde 1. Dieser Schnappschuss liegt im Repo; die Karte wandert als Issue-Baum in den GitHub-Tracker, sobald `/setup-matt-pocock-skills` in einer Session mit den Projekt-Skills gelaufen ist. Der Skill `wayfinder` war in der Session nicht installiert; dies ist die manuelle Anwendung der Methode (SKILL.md aus mattpocock/skills). Details zu geschlossenen Tickets stehen in `decisions/` bzw. direkt hier, solange es keinen Tracker gibt.

## Destination

Spec, Businessplan-Gerüst, Präsentation und ein belegter Prototyp-Lauf, so dass der Bau über `to-spec` → `to-tickets` → `implement` ohne offene Grundsatzfragen starten kann. Der Bau selbst ist out of scope.

## Notes

- Produktkern: Werbeanzeige (Meta, YouTube, Google Ads) → Chat-Funnel (Grilling-Sitzung) → bezahlte Spec → Bauangebot. Die Ads-Pipeline und die „Conversion Intelligence" (Kosten pro Käufer, gespeist in den Preis) gehören fest zum Produkt und sind wichtiger als die Zielgruppen-Feinabstimmung.
- Zielgruppe: kleine und mittlere Unternehmen, die eine Website brauchen. Segmentierung ist nicht Teil dieses Laufs.
- Skills pro Sitzung: `grilling`, `domain-modeling`; für Ticket-Typen `research`, `prototype`.
- Sprache Deutsch. Keine Superlative in Kundentexten; Versprechen müssen belegbar sein.

## Decisions so far

- **Destination und Umfang:** Spec, Businessplan-Gerüst, Präsentation, belegter Prototyp-Lauf; Bau out of scope.
- **Zielgruppe:** SMBs, die eine Website brauchen; Segmentierung nicht Teil dieses Laufs.
- **Schwerpunkt:** Ads-Pipeline (Meta, YouTube, Google Ads) samt Conversion Intelligence steht fest als Produktteil.
- **Preisuntergrenze:** Break-even-Kennzahl = (Tokenkosten pro Sitzung + Ad-Spend) / Zahl der Spec-Käufer. 15,99 € ist der Platzhalter für die erste Kampagne und wird danach gemessen.
- **Name und Heimat:** Projektname und Repo `pipedesigna` unter `Storypapst` (privat), angelegt am 2026-10-06. Tracker: GitHub Issues und das Projekt https://github.com/users/Storypapst/projects/1. Die Namenssuche ist damit geschlossen.
- **Agentur-Partnerschaften:** nicht Teil des Konzepts, vorerst gestrichen.
- **Chat-Basis, Research ([chat-basis.md](research/chat-basis.md)):** Weder LibreChat noch Open WebUI bringen anonyme Gast-Sitzungen aus einem Werbeklick oder eine Bezahlschranke mit. Tendenz des Researchers: Eigenbau auf der Messages API (Sicherheit mittel). Die Wahl ist noch nicht getroffen; sie hängt an den beiden Runde-3-Fragen oben und am Umfang des Prototyp-Laufs.
- **Ads-Tracking-Stack, Research ([ads-tracking.md](research/ads-tracking.md)):** Meta (Conversions API) und Google Ads (Click-Conversion-Upload, Enhanced Conversions) nehmen serverseitig gemeldete Ereignisse an; die Click-ID (`fbclid`/`gclid`) muss beim Landing gespeichert und bis zum Kauf mitgeführt werden. Zum Lernen nennt Meta ca. 50 Optimierungsereignisse je Anzeigengruppe in 7 Tagen, Google 30–50 Conversions in 30 Tagen; bei zu wenigen Käufen empfehlen beide ein häufigeres Zielereignis. Ohne Einwilligung ist „Kosten pro Käufer“ nur für den zuordenbaren Anteil exakt. **Einschränkung:** Plattformseiten waren gesperrt, viele Zahlen stammen aus Suchauszügen und sind vor dem Bauen gegen die Live-Doku zu prüfen. Das Conversion-Ereignis selbst ist noch offen (Runde 3).
- **Rechtliche Leitplanken, Research ([recht.md](research/recht.md); keine Rechtsberatung):** (1) Empfehlungsmodell „15.000 auf 6.000 €": Risiko hoch, Anwalt vor Start; gegenüber Verbrauchern kommt progressive Kundenwerbung in Betracht (§ 16 Abs. 2 UWG, strafbewehrt), ob ein Preisnachlass anders bewertet wird als eine Geldprämie, ist nicht belegt. (2) Streichpreis: der „eigentliche" Preis muss real belegbar sein, Countdown-Timer ohne echten Ablauf gelten in mehreren Urteilen als irreführend. (3) Anthropic API: keine reine EU-Verarbeitung, jeder Chat geht in die USA (Grundlage: SCC); „datenschutzsicher" ist als Absolutclaim nicht belegbar, belegbar sind nur konkrete Tatsachen. (4) Gründer gelten meist als Unternehmer, im Zweifel zählt Verbraucherrecht; der Status muss im Funnel erfasst werden. **Einschränkung:** Rechtsportale waren gesperrt, Gesetzestexte und Urteile überwiegend über Suchauszüge; Wortlaut und Aktenzeichen am Original prüfen.

## Frontier (offen, nicht blockiert)

| Ticket | Typ | Stand |
| --- | --- | --- |
| Chat-Basis: Skills `grilling`/`domain-modeling` unverändert (Agent SDK, ein Prozess je Sitzung) oder als Prompt und Tool nachgebaut (Messages API) | grilling (HITL) | Runde 3, aus `research/chat-basis.md` |
| Kostenobergrenze je Sitzung vor der Zahlung: wie hart, darf eine Sitzung abgebrochen werden | grilling (HITL) | Runde 3, aus `research/chat-basis.md` |
| Ads-Pipeline: für wen, welches Conversion-Ereignis | grilling (HITL) | Runde 2, Frage 1 |
| Umfang des Prototyp-Laufs: echter Ad-Traffic oder simuliert | grilling (HITL) | Runde 2, Frage 2 |
| Rolle „Mitarbeiter" | grilling (HITL) | Runde 2, Frage 3 |

## Blockiert

| Ticket | Typ | Wartet auf |
| --- | --- | --- |
| Preisstufen und Zeitrabatt-Auslöser (ohne Fake-Countdown, Streichpreis nur mit realem Referenzpreis) | grilling | Conversion-Ereignis |
| Prototyp-Lauf auf dem Mac Mini (herdr) | prototype | Chat-Basis, Umfang des Laufs |
| Beleg-Kriterium für den Prototyp-Lauf | grilling | Umfang des Laufs, Ereignismodell |

## Not yet specified

- Businessplan-Gerüst (Zahlenmodell auf Basis der Kennzahlen oben).
- Content-Marketing mit gebauten Seiten.
- Referral-Mechanik und Preishebel (hängt an der Rechtsrecherche).
- Hetzner-Hosting als Teil des Angebots (Betrieb, Support, Haftung).
- Kunden-Repo je Username: Rechtemodell, Übertragung später.
- Credits für `teach`.
- Ads-Pipeline als Angebot an Kunden für deren eigene Website (nur falls Runde 2, Frage 1 das so entscheidet).
- Präsentation.

## Out of scope

- Der Bau der Pipeline (Chat-UI, Funnel, Repo-Automatik): läuft nach der Karte über `to-spec`, `to-tickets`, `implement`.
- Partnerschaften mit Agenturen für High-Ticket-Kunden: aus dem Konzept gestrichen. Kehrt nur zurück, wenn die Destination neu gezogen wird.
- Segmentierung der SMB-Zielgruppe.
