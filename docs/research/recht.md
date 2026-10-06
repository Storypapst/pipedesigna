# Recht: Anhaltspunkte für pipedesigna (DE/EU)

Stand: 2026-10-05. Keine Rechtsberatung; belegte Anhaltspunkte zur Prüfung durch einen Anwalt.

Grenze: Die meisten Rechtsportale waren gesperrt. Gesetzestexte und Urteile habe ich überwiegend über Suchauszüge geprüft; direkt abgerufen wurden nur die Anthropic-Seiten [1][3][4][6][12]. Wortlaut, Absatzzählung und Aktenzeichen vor Verwendung am Original prüfen. "Sekundär" = Kanzlei- oder Fachseite. "Folgerung" = eigene Schlussfolgerung, nicht belegt.

| # | Frage | Risiko | Anwalt prüfen |
|---|-------|--------|---------------|
| 1 | DSGVO: Chat-Speicherung, US-LLM, "datenschutzsicher" | mittel (Verarbeitung), hoch (Werbeclaim) | ja |
| 2 | Verbraucherstatus und Widerruf | mittel | ja |
| 3 | Streichpreise, Rabatte, Countdown | hoch (B2C), mittel (B2B) | ja |
| 4 | Empfehlungsmodell 15.000 auf 6.000 EUR | hoch | ja, vor Start |
| 5 | Tracking-Einwilligung (Meta, Google Ads) | mittel, hoch ohne Consent-Banner | ja (kurz) |

## 1. DSGVO und US-LLM

- **Vertrag:** Pipedesigna ist Verantwortlicher, Anthropic Auftragsverarbeiter. Das DPA wird Teil der Commercial Terms, SCC Modul 2/3 sind per Verweis eingebunden (abgerufene Fassung ab 24.2.2025) [1]; Art. 28 Abs. 3 DSGVO verlangt diesen Vertrag [2]. Die Terms gelten nur für Unternehmen und verbieten Training auf Customer Content [3]. AV-Vertrag mit Hetzner: nicht recherchiert.
- **Drittland:** Die direkte Claude API kennt nur `inference_geo` "global" (Standard) oder "us", Workspace-Geo nur "us"; eine reine EU-Verarbeitung ist nicht vorgesehen [4]. Jeder Chat geht also in die USA. Grundlage sind SCC (Art. 46 Abs. 2 lit. c) [1][5]. Die Privacy Policy nennt Angemessenheitsbeschlüsse und SCC, kein DPF [6]; DPF-Zertifizierung von Anthropic: nicht belegt. Das EuG wies die DPF-Klage Latombe am 3.9.2025 ab [7], die Berufung C-703/25 P ist anhängig (aktuellen Stand nicht geprüft) [8]. Bei SCC bleibt eine Transfer-Folgenabschätzung nötig [9]. EU-Regionen gibt es laut Sekundärquelle nur über Bedrock/Vertex/Foundry [10].
- **Aufbewahrung:** Laut Sekundärquelle 7 Tage seit 14.9.2025 [11]; bei Flagging bis zu 2 Jahre (offiziell) [12]. Eigene Chat-Logs: Löschfrist festlegen.
- **Rechtsgrundlage (Einschätzung):** Chat zur Spezifikation: Art. 6 Abs. 1 lit. b (vorvertragliche Maßnahme auf Anfrage); Missbrauchsschutz: lit. f; Einwilligung nur für Folgezwecke wie Marketing oder Wiederverwendung der Chats [13][14].
- **Informationen:** Art. 13: Zwecke, Rechtsgrundlage, Empfänger, Drittland mit Garantien, Speicherdauer [15]. Dazu Hinweis auf KI-Chat (Art. 50 KI-VO, laut Sekundärquelle seit 2.8.2026, Übergangsfristen unklar) [16]. Mitbewerber können DSGVO-Verstöße über das UWG verfolgen (EuGH C-21/23) [17].
- **"Datenschutzsicher":** Keine gesetzliche Definition. Maßstab ist § 5 UWG (Gesamteindruck) [18]; Zertifikatswerbung muss Prüfstelle und Gegenstand nennen [19]; Hervorheben von Selbstverständlichem kann irreführen (BGH I ZR 121/07) [20]. Ein Urteil speziell zu "datenschutzsicher" fand ich nicht (nicht belegt). Folgerung: Absolutclaims sind bei US-Verarbeitung nicht belegbar; belegbar sind Tatsachen (Hosting-Ort, Übermittlung an Anthropic in den USA, SCC, Löschfristen).

## 2. Verbraucherstatus und Widerruf

- **Begriffe:** Verbraucher = natürliche Person, Zweck überwiegend weder gewerblich noch selbständig beruflich (§ 13 BGB); Unternehmer handelt in Ausübung einer solchen Tätigkeit (§ 14) [21]. Im B2B kein gesetzliches Widerrufsrecht [22][23].
- **Gründer:** Geschäfte im Zuge der Aufnahme einer selbständigen Tätigkeit, auch zur Vorbereitung, sind nach BGH unternehmerisch (BGHZ 162, 253; III ZR 295/06) [24]. Aber BGH VIII ZR 7/09: Zweifel gehen zugunsten der Verbrauchereigenschaft; der Anbieter muss Umstände beweisen, die eindeutig auf unternehmerischen Zweck deuten [25]. Folgerung: Unternehmerstatus abfragen und dokumentieren (Firma, USt-IdNr., Zweck); Privatpersonen, Hobby-Seiten, unklare Gründungsideen bleiben Verbraucherfälle.
- **Widerruf (Verbraucher):** 14 Tage. Bei Dienstleistungen erlischt das Recht vorzeitig nur bei vollständiger Leistung, wenn der Verbraucher vorher ausdrücklich zugestimmt und seine Kenntnis vom Verlust bestätigt hat (§ 356 Abs. 4; Bestätigung nach § 312f) [26]. Beweislast beim Unternehmer; bei Widerruf vor Abschluss der Leistung anteiliger Wertersatz [27]. Ohne wirksame Belehrung verlängert sich die Frist (bis 12 Monate + 14 Tage; Wortlaut nicht abgerufen) [29].
- **Spezifikation als Individualleistung:** Die Ausnahme § 312g Abs. 2 Nr. 1 betrifft nach Wortlaut Waren nach Kundenspezifikation [22]; für Dienstleistungen gilt sie nicht pauschal (Folgerung). Bei digitalen Inhalten ohne Datenträger erlischt das Recht schon mit Beginn der Ausführung, ebenfalls nur mit Zustimmung und Kenntnisbestätigung (§ 356 Abs. 5) [26]. Ob die Spezifikation Dienstleistung, Werk oder digitaler Inhalt ist: nicht belegt.
- **Neu:** Seit 19.6.2026 elektronische Widerrufsfunktion (§ 356a BGB) bei B2C-Fernabsatz über Online-Oberflächen [28][29].

## 3. Preiswerbung

- **Anwendungsbereich:** PAngV gilt B2C [30]. § 11 PAngV (niedrigster Preis der letzten 30 Tage) nennt Preisermäßigungen "für eine Ware" [31]; individuelle Preisermäßigungen sind laut Sekundärquelle ausgenommen [32]. Für Spezifikation und Bauangebot zählt daher vor allem § 5 UWG, auch im B2B (Folgerung). EuGH C-330/23 (Aldi Süd) zeigt die strenge Auslegung bei Waren [33].
- **"Eigentlich 15.000 EUR":** Der frühere Preis muss ernsthaft und über angemessene Zeit tatsächlich gefordert worden sein, sonst Mondpreis [34]. § 5 UWG vermutet Irreführung bei nur unangemessen kurzer Forderung; bei Streit trägt der Werbende die Beweislast (Fundstelle nennt Abs. 5, Zählung prüfen) [18]. Belegbar sein müssen reale Angebote und Verkäufe zu 15.000 EUR mit Zeitraum, Anzahl, Rechnungen. Wird der Preis praktisch nie gezahlt, ist das Risiko hoch.
- **Befristung und Countdown:** Anhang Nr. 7 zu § 3 Abs. 3 UWG verbietet gegenüber Verbrauchern die unwahre Angabe zeitlich begrenzter Verfügbarkeit [35]. Irreführend: LG Frankfurt 2-03 O 359/24, Countdown ohne echtes Ablaufdatum (Datum der Quellen uneinheitlich: 23.10.2025 bzw. 27.3.2026) [36]; LG Hanau 6 O 27/25, zweimal verlängert (Berufung OLG Frankfurt 6 U 313/25) [37]; OLG Köln 6 U 62/21, per Cookie-Löschen erneuerbarer Rabatt [38]; OLG Hamburg 3 U 99/20, Wiederholung im 2-3-Tage-Abstand [39]. Dagegen: BGH I ZR 181/10, Verlängerung nicht zwingend irreführend [40]; LG Deggendorf, Timer nicht per se irreführend (Sekundär) [41]. Folgerung: Timer nur mit echtem, serverseitig durchgesetztem Ablauf.
- **"Rabatt bei Zögern" bis 16 EUR:** Ein vom Verhalten abhängiger Preis ist personalisierte Preisgestaltung; bei automatisierter Entscheidung besteht gegenüber Verbrauchern eine Hinweispflicht (Art. 246a § 1 Abs. 1 S. 1 Nr. 6 EGBGB) [42]. Zahlen praktisch alle den Tiefpreis, ist auch der 100-EUR-Referenzpreis angreifbar (Folgerung). B2C-Preise brauchen den Gesamtpreis inkl. USt [30].

## 4. Empfehlungsprämien

- **Grundsatz:** Kunden-werben-Kunden ist nicht per se unlauter; es braucht besondere Umstände (BGH I ZR 145/03) [43]. Ob ein Preisnachlass anders bewertet wird als eine Geldprämie: nicht belegt. § 16 Abs. 2 UWG spricht von "besonderen Vorteilen", nicht nur Geld [44]; Folgerung: Rabatt wird wohl wie Prämie behandelt.
- **Hauptrisiko progressive Kundenwerbung:** § 16 Abs. 2 UWG (Freiheitsstrafe bis 2 Jahre) erfasst, wer Verbraucher durch Vorteilsversprechen zum Kauf veranlasst, wenn sie andere zu gleichartigen Geschäften bewegen, die ihrerseits Vorteile für Weiterwerbung erlangen sollen [44]. Anhang Nr. 14 UWG (Schneeball-/Pyramidensystem, Vergütung "allein oder hauptsächlich" durch weitere Teilnehmer) ist im Anwendungsbereich deckungsgleich; jeder finanzielle Beitrag genügt [45]. Das Muster "5 Empfohlene mit je mindestens 1.000 EUR, dann 6.000 statt 15.000 EUR" ist rekursiv, wenn Empfohlene dieselbe Staffel nutzen können, und der Vorteil (9.000 EUR) ist groß. Abgrenzung nach Gesamtbetrachtung, ob der Vertrieb vor allem dem Absatz echter Leistungen dient [46]. Ob ein Preisnachlass als "Vergütung" zählt, ist nicht belegt; ein Urteil zu diesem Modell fand ich nicht. § 16 Abs. 2 nennt nur Verbraucher; die Zielgruppe ist gemischt.
- **Kennzeichnung:** Wer für eine Empfehlung einen Vorteil erhält, handelt kommerziell; Nichtkenntlichmachen ist unlauter, Gegenleistung wird vermutet (§ 5a Abs. 4 UWG) [47]; gekaufte Empfehlungen sind irreführend, wenn die Bezahlung verschwiegen wird (Sekundär) [48]. Gefälschte Verbraucherempfehlungen sind per se verboten (Anhang Nr. 23c) [35]; Prämie daher nicht an positive Bewertungen koppeln (Folgerung).
- **Belästigung:** E-Mail-Werbung ohne vorherige ausdrückliche Einwilligung ist unzumutbar (§ 7 Abs. 2 Nr. 2 UWG) [49]. Nach BGH I ZR 208/12 (Tell-a-friend) ist eine Empfehlungsfunktion, die im Namen des Unternehmens Mails verschickt, Werbung des Unternehmens [50]. Folgerung: Empfehlende teilen den Link selbst.
- **Steuern (angerissen):** Prämien an Private sind laut Sekundärquelle sonstige Einkünfte (§ 22 Nr. 3 EStG), Freigrenze 256 EUR [51]. Umsatzsteuer bei Rabatt gegenüber Geldprämie: nicht belegt, Steuerberater.

## 5. Werbe-Tracking

- **Einwilligung:** § 25 Abs. 1 TDDDG erlaubt Speichern und Auslesen auf dem Endgerät nur mit Einwilligung nach klarer und umfassender Information; Ausnahme nur für unbedingt erforderliche Zugriffe (Abs. 2 Nr. 2) [52]. Werbe- und Conversion-Tracking braucht nach DSK Opt-in [53]; vorangekreuzte Kästchen genügen nicht (BGH I ZR 7/16) [54].
- **Meta und Google:** Die Weitergabe personenbezogener Daten braucht zusätzlich eine DSGVO-Grundlage, praktisch Einwilligung. LG Leipzig (05 O 2351/23) und LG Lübeck (15 O 15/24) behandelten Meta Business Tools (u.a. Pixel, Conversions API) ohne wirksame Einwilligung als rechtswidrig und sprachen je 5.000 EUR gegen Meta zu [55]. Website-Betreiber können gemeinsam Verantwortliche sein (EuGH Fashion ID, C-40/17) [56]. Google verlangt für EWR-Traffic Consent Mode v2 (Sekundär) [57]; dass dies die rechtliche Einwilligung ersetzt, ist nicht belegt.
- **Kernaussage:** Pixel und Tags erst nach aktiver Einwilligung laden. Technik: anderes Ticket.

## Quellen

[1] Anthropic DPA: https://www.anthropic.com/legal/data-processing-addendum
[2] Art. 28 DSGVO: https://datenschutz-grundverordnung.eu/dsgvo/art-28-dsgvo/
[3] Anthropic Commercial Terms: https://www.anthropic.com/legal/commercial-terms
[4] Anthropic, Data residency: https://platform.claude.com/docs/en/manage-claude/data-residency
[5] SCC-Beschluss (EU) 2021/914: https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A32021D0914
[6] Anthropic Privacy Policy: https://www.anthropic.com/legal/privacy
[7] Heuking zu EuG 3.9.2025: https://www.heuking.de/de/news-events/newsletter-fachbeitraege/artikel/eug-bestaetigt-wirksamkeit-des-eu-us-data-privacy-framework.html
[8] Berufung C-703/25 P: https://digitalpolicyalert.org/event/35459-latombe-filed-appeal-against-general-court-dismissal-of-challenge-to-european-unionunited-states-data-protection-framework-adequacy-decision-in-latombe-v-commission
[9] Taylor Wessing zu Schrems II: https://www.taylorwessing.com/de/insights-and-events/insights/2020/08/empfohlene-massnahmen-nach-dem-schrems-ii-urteil-des-eugh
[10] EU-Residency (Sekundär): https://sonomos.ai/blog/claude-eu-data-residency-2026/
[11] Aufbewahrung 7 Tage (Sekundär): https://www.theregister.com/a/5293789
[12] Anthropic, API and data retention: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
[13] Art. 6 DSGVO: https://dsgvo-gesetz.de/art-6-dsgvo/
[14] DSK, Orientierungshilfe KI: https://www.datenschutz-bayern.de/dsbk-ent/DSK_OH_KI_und_Datenschutz.pdf
[15] Art. 13 DSGVO: https://dsgvo-gesetz.de/art-13-dsgvo/
[16] KI-VO Art. 50 (Sekundär): https://secureprivacy.ai/de/blog/eu-ki-verordnung-artikel-50-transparenzpflichten-fr-chatbots-und-deepfakes-2026
[17] EuGH C-21/23 (Sekundär): https://www.taylorwessing.com/zh-hant/insights-and-events/insights/2024/10/ecj-lindenapotheke
[18] § 5 UWG: https://www.gesetze-im-internet.de/uwg_2004/__5.html
[19] Wettbewerbszentrale, Zertifizierung: https://www.wettbewerbszentrale.de/wp-content/uploads/2023/03/2022-05_Die-Werbung-mit-einer-Zertifzierung.pdf
[20] BGH I ZR 121/07: https://www.anwalt24.de/urteile/bgh/2008-10-23/i-zr-121_07
[21] §§ 13, 14 BGB: https://www.gesetze-im-internet.de/bgb/__13.html , https://www.gesetze-im-internet.de/bgb/__14.html
[22] § 312g BGB: https://www.gesetze-im-internet.de/bgb/__312g.html
[23] Kein Widerruf im B2B (Sekundär): https://www.it-recht-kanzlei.de/widerrufsrecht-unternehmer-ausschluss.html
[24] BGH zu Existenzgründern (Sekundär): https://www.uni-trier.de/fileadmin/fb5/prof/LEHR/ProfHSchmidt/R%C3%9C_zu_1.5.1.pdf , https://www.deubner-steuern.de/produkte/bwl-beratung/doc/abgrenzung-von-unternehmer--und-verbraucherhandeln-bei-vorbereitung-einer-existenzgruendung-616289
[25] BGH VIII ZR 7/09: https://lorenz.userweb.mwn.de/urteile/viiizr7_09.htm
[26] §§ 356, 312f BGB: https://www.gesetze-im-internet.de/bgb/__356.html , https://www.gesetze-im-internet.de/bgb/__312f.html
[27] Widerruf bei Dienstleistungen (Sekundär): https://www.it-recht-kanzlei.de/dienstleistung-widerrufsrecht-verbraucher.html
[28] Noerr zum Widerrufsbutton (BGBl. 2026 I Nr. 28): https://www.noerr.com/de/insights/umsetzungsgesetz-zum-widerrufsbutton-veroeffentlicht
[29] Bitkom zum Widerrufsbutton: https://www.bitkom.org/Bitkom/Publikationen/Umsetzung-des-Widerrufsbuttons
[30] PAngV § 1, § 3: https://www.gesetze-im-internet.de/pangv_2022/__1.html
[31] PAngV § 11: https://www.gesetze-im-internet.de/pangv_2022/__11.html
[32] Individuelle Preisermäßigungen (Sekundär): https://lexmea.de/en/gesetz/pangv/11
[33] EuGH C-330/23 (Sekundär): https://www.it-recht-kanzlei.de/streichpreise-aldi-eugh.html
[34] IHK Frankfurt, Mondpreise: https://www.frankfurt-main.ihk.de/recht/uebersicht-alle-rechtsthemen/wettbewerbsrecht/unlauterer-wettbewerb/irrefuehrende-werbung/mondpreise-5196206
[35] UWG-Anhang: https://www.gesetze-im-internet.de/uwg_2004/anhang.html
[36] LG Frankfurt (LTO): https://www.lto.de/recht/nachrichten/n/2-03-o-359/24-lg-frankfurt-zu-fitness-first-irrefuehrende-werbung
[37] LG Hanau (vzbv): https://www.vzbv.de/urteile/mobilfunk-countdown-fuer-angeblich-befristetes-sonderangebot-war-irrefuehrend
[38] OLG Köln (Sekundär): https://www.wbs.legal/wettbewerbsrecht/e-commerce/olg-koeln-zu-werbeaktion-fuer-erstbesucher-cookie-gesteuerter-rabatt-ist-wettbewerbswidrig-59993/
[39] OLG Hamburg/Köln (Sekundär): https://www.taylorwessing.com/de/insights-and-events/insights/2022/05/olg-hamburg-und-olg-koeln-online-rabattwerbung
[40] BGH I ZR 181/10 (Sekundär): https://www.otto-schmidt.de/news/wirtschaftsrecht/die-verlangerung-eines-zeitlich-befristeten-fruhbucherrabatts-ist-nicht-in-jedem-fall-irrefuhrend-2012-01-04.html
[41] LG Deggendorf (Sekundär): https://www.it-recht-kanzlei.de/countdown-uhr-online-shop-irrefuehrend-kundenbewertungen.html
[42] Personalisierte Preise: https://cms.law/de/deu/legal-updates/kuenftig-hinweispflicht-bei-personalized-pricing , https://www.gesetze-im-internet.de/bgbeg/art_246a__1.html
[43] BGH I ZR 145/03: https://rewis.io/urteile/urteil/yav-05-07-2006-i-zr-14503/
[44] § 16 UWG: https://www.gesetze-im-internet.de/uwg_2004/__16.html
[45] Schneeballsysteme (Sekundär): https://www.it-recht-kanzlei.de/schneballsysteme-sind-wettbewerbswidrig.html
[46] Strukturvertrieb (Sekundär): https://www.ferner-alsdorf.de/wettbewerbsrecht-abgrenzung-von-schneeballsystem-zu-zulaessigem-strukturvertrieb/
[47] § 5a UWG: https://www.gesetze-im-internet.de/uwg_2004/__5a.html
[48] Empfehlungen (Sekundär): https://www.omsels.info/die-verbote-oder-was-darf-ich-nicht/5-uwg-irrefuehrende-werbung/13-einzelfaelle/empfehlungen
[49] § 7 UWG: https://www.gesetze-im-internet.de/uwg_2004/__7.html
[50] Tell-a-friend (Sekundär): https://www.it-recht-kanzlei.de/tell-a-friend-bgh.html
[51] Prämien und Steuer (Sekundär, schwach): https://www.monsterdealz.de/magazin/kunden-werben-kunden
[52] § 25 TDDDG: https://www.gesetze-im-internet.de/ttdsg/__25.html
[53] DSK, OH Digitale Dienste (nur Listing): https://www.lda.brandenburg.de/lda/de/service/informationsmaterial/orientierungshilfen-und-anwendungshinweise/
[54] BGH Cookie-Einwilligung II (Sekundär): https://www.haendlerbund.de/de/news/aktuelles/rechtliches/3398-bundesgerichtshof-urteil-cookie-einwilligung
[55] LG Leipzig/Lübeck (Sekundär): https://www.ra-plutte.de/meta-business-tools/
[56] Fashion ID (Sekundär): https://www.dataprotectionreport.com/tag/data-controller/
[57] Google Consent Mode (Sekundär): https://ecommercefastlane.com/google-consent-mode-eu-ad-performance/
