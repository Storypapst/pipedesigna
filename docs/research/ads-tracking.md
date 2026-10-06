# Ads-Rückmeldung, Lernschwellen, Consent und Kosten pro Käufer

Abruf aller Quellen: 05.10.2026. Zugriffsart: **D** = Seite/Datei direkt gelesen (GitHub). **S** = Seite ist im Netzwerk gesperrt (facebook.com, developers.facebook.com, support.google.com, developers.google.com); Inhalt nur aus Suchergebnis-Auszügen. S-Zahlen vor dem Bauen gegen die Live-Seite prüfen.

## Fazit

Beide Plattformen nehmen serverseitig gemeldete Ereignisse an: Meta über die Conversions API (`fbc` aus `fbclid`, `fbp`, `event_id`; Ereignis höchstens 7 Tage alt), Google Ads über Click-Conversion-Upload bzw. Data Manager API (`gclid`/`wbraid`/`gbraid`, bis 90 Tage nach dem Klick) und Enhanced Conversions (gehashte E-Mail); die Click-ID muss daher beim Landing gespeichert und bis zum Kauf mitgeführt werden. Zum Lernen nennt Meta rund 50 Optimierungsereignisse je Anzeigengruppe in 7 Tagen, Google kein hartes Minimum, aber 30 bis 50 Conversions in 30 Tagen für belastbare Bewertung; bei zu wenig Käufen empfehlen beide ein häufigeres Ereignis als Ziel. Ohne Einwilligung fehlen Click-ID-Cookies und Nutzerdaten: Google modelliert erst ab 700 Klicks in 7 Tagen je Land und Domain, für Meta ist in der EU kein Ersatz dokumentiert, daher ist „Kosten pro Käufer“ nur für den zuordenbaren Anteil exakt und der nicht zuordenbare Anteil muss mit ausgewiesen werden. YouTube nutzt dieselben Kennungen, aber viele Conversions entstehen ohne Klick und sind nur in Google Ads sichtbar.

## 1. Serverseitige Rückmeldung

| Weg | Voraussetzung | Kennung bis zum Kauf | Grenzen / Verzögerung |
|---|---|---|---|
| **Meta Conversions API** | Pflicht: `event_name`, `event_time`, `user_data`, `action_source`; Web zusätzlich `event_source_url`, `client_user_agent` [M1, M2]. Läuft auch ein Pixel, gleiche `event_id` + `event_name` zur Deduplizierung [M4, M7]. Dataset-ID/Token: nicht gesondert belegt. | `fbclid` aus der Landing-URL → `fbc` = `fb.<Index>.<Zeit ms>.<fbclid>` [M3]; `fbp`; beide ungehasht, ebenso `client_ip_address` [M2]. Optional gehashte E-Mail/Telefon [M2]. | `event_time` höchstens 7 Tage alt, sonst wird die ganze Anfrage abgelehnt [M1]. Empfehlung: in Echtzeit, ideal binnen 1 h [M5]. Server-Event wird nicht verworfen, wenn in 48 h kein Browser-Event kam [M4]. Standard-Zuordnung 7 Tage Klick / 1 Tag View [M11]. |
| **Google Click-Conversion-Upload** (Ads API) | Auto-Tagging an; Conversion-Aktion „Import aus Klicks“ [G8]. Felder u. a. `conversion_action`, `conversion_date_time` (nach Klickzeit, mit Zeitzone), `order_id` (einmalig je Conversion-Aktion), Wert, Währung, `consent` [G5]. | `gclid`; bei iOS `wbraid`/`gbraid` [G5]. Ohne Click-ID: `session_attributes` (aus `gad_source`, `gad_campaignid`) [G7]. | Upload höchstens 90 Tage nach Klick [G1]. `consent` „dringend empfohlen“, sonst ggf. nicht zuordenbar [G2]. |
| **Google Data Manager API** (`events.ingest`) | Bis 2000 Events je Anfrage [G6]. Web-Events: Conversion-Aktion Typ WEBPAGE, `transactionId`, Zeitpunkt, mind. eine Zuordnung (Click-ID oder gehashte Nutzerdaten) [G4]. Consent auf Anfrage- und Eventebene [G6]. | `gclid`/`gbraid`/`wbraid` in `ad_identifiers`, optional Session-Attribute [G6, G7]. | Als Ergänzung zu Tag-Events binnen 24 h [G4]. |
| **Google Enhanced Conversions für Web** | Google-Tag auf der Kaufseite plus Order-ID; E-Mail u. Ä. SHA-256-gehasht [G3]. Per API: Tag meldet `gclid` + Order-ID, Server schickt Nutzerdaten später als `ENHANCEMENT` mit gleicher `order_id` [G3]. `ad_user_data`-Einwilligung nötig (EEA) [G10a]. | `gclid` im First-Party-Cookie `_gcl_*` (Conversion Linker) [G16]; zusätzlich Abgleich gehashter Daten mit Google-Konten [G17]. | API-Nachlieferung höchstens 24 h nach der Conversion [G3]. |
| **Google Enhanced Conversions für Leads** | Gehashte E-Mail/Telefon + Zeitpunkt, ohne Tag-Conversion [G1]. | Click-ID optional, aber mitsenden, wenn kein Tag Nutzerdaten sammelt [G4]. | Upload höchstens 63 Tage nach Klick [G1]. |

Zwischenereignisse: bei beiden Plattformen eigene Ereignisse bzw. Conversion-Aktionen. Meta: Custom Events lassen sich bei Website-Ereignissen zur Optimierung nutzen [M14]. Google: je Aktion „primär“ (Gebotsziel) oder „sekundär“ (nur Beobachtung) [G18].

## 2. Lernschwellen und früheres Ereignis als Ziel

**Meta:** Eine Anzeigengruppe verlässt die Lernphase nach rund 50 Optimierungsereignissen innerhalb von 7 Tagen nach der letzten signifikanten Änderung; sonst „Learning limited“ [M8, M8b]. Meta empfiehlt dann: Anzeigengruppen zusammenlegen, Zielgruppe erweitern, Budget oder Gebot erhöhen oder ein Optimierungsereignis wählen, das häufiger auftritt [M8b]. Eine weitere Hilfeseite nennt ca. 50 Conversions pro Woche und Landing-Page-View-Optimierung als Alternative [M8c].

**Google:** Kein hartes Minimum zum Start; Target CPA geht ohne Historie, zur Bewertung mindestens 30 Conversions in 30 Tagen [G9a], bei Target ROAS 50 [G9b]. Demand Gen: mind. 50 Conversions in den ersten 30 Tagen je Anzeigengruppe, Gruppen unter ca. 30 zusammenlegen [G9c]; Target ROAS dort ab 50 Conversions in 35 Tagen (10 davon in den letzten 7) oder 100 über alle Demand-Gen-Kampagnen des Kontos [G9d]. Lernphase 7 bis 14 Tage; unter 5 Conversions/Tag 14 Tage, über 100/Tag 1 bis 3 Tage [G9b, G9e]. Bei erwartet unter 10 Conversions/Tag: auf ein häufigeres Ereignis optimieren (sekundäre Conversion-Aktion + Kampagnenziel) [G9b]; alternativ tiefes Ziel behalten und flache Ziele als nicht gebotsrelevant mitmessen, damit der Anlauf schneller geht [G9f].

**Eigene Rechnung (keine Quelle):** 50 Käufer pro Woche und Anzeigengruppe erfordern ein Wochenbudget von etwa 50 × Kosten pro Käufer je Gruppe. Ob die Optimierung auf „Fragen abgeschlossen“ statt Kauf die Käuferqualität senkt, dokumentieren die Plattformen nicht; das ist zu testen.

## 3. Consent in der EU

**Google:** Consent Mode v2 kennt `ad_user_data` und `ad_personalization`; für EEA-Nutzer wird `ad_user_data` für tag-basiertes Conversion-Tracking und Enhanced Conversions erwartet [G10a]. Basic: bei Ablehnung feuern die Tags nicht, nichts geht an Google, es gilt ein allgemeines Modell. Advanced: Tags senden cookielose Pings, es gibt ein händlerspezifisches Modell [G10b]. Bei `ad_storage` denied werden keine Ads-Cookies gesetzt; die Seiten-URL inkl. `gclid` kann in Pings stehen und dient nur der ungefähren Verkehrsmessung, `ads_data_redaction` schwärzt sie; `url_passthrough` reicht Click-IDs per URL weiter [G10b]. Modellierte Conversions erscheinen in der Spalte „Conversions“ [G10c]; Voraussetzung sind 700 Anzeigenklicks in 7 Tagen je Land × Domain [G10c]. Bei Uploads gilt das `consent`-Feld (siehe Tabelle) [G2, G6].

**Meta:** Die Business Tools Terms verlangen in Rechtsräumen mit Einwilligungspflicht (u. a. EU) nachweisbare Einwilligung, bevor Meta-Cookies oder Geräteinformationen genutzt werden [M9]. `data_processing_options` (LDU) betrifft nur US-Bundesstaaten [M12]; ein EU-Pendant zum Consent Mode ist nicht belegt. Üblich ist, bei fehlender Einwilligung weder Pixel noch CAPI-Event zu senden (Sekundärquelle [X1]; Pixel-Schalter `fbq('consent', ...)` nur über CMP-Hersteller belegt [X2]). Meta kann bei fehlenden Daten einzelne Conversions statistisch modellieren [M10]; Anwendung auf EU-Nichteinwilliger nicht belegt.

**Wirkung auf Kosten pro Käufer (eigene Folgerung):** Ad-Spend (Plattform-API) und Gesamtzahl Käufer (eigene Zahlung) sind unabhängig vom Consent messbar. Kanal und Kampagne eines Käufers sind nur bekannt, wenn UTM/Click-ID erfasst wurden. Plattform-eigene Conversion-Zahlen weichen ab (Google inkl. modellierter Anteile, Meta ohne Nichteinwilliger). Daher zwei Kennzahlen führen: Kosten pro attribuiertem Käufer und Anteil nicht zuordenbarer Käufer. Consent-Status je Sitzung speichern.

## 4. Kosten pro Käufer und Datenmodell

Formel: (Ad-Spend + Tokenkosten **aller** Sitzungen des Kanals, auch ohne Kauf) ÷ Zahl der Käufer (verschiedene, nicht stornierte `order_id`).

| Objekt | Felder (minimal) | Zweck |
|---|---|---|
| **Sitzung** (beim Landing) | `session_id`, `first_seen_at`, Kanal (meta/google/youtube/sonst), `utm_*`, Kampagnen-/Anzeigengruppen-/Anzeigen-ID aus URL (falls befüllt), `gclid`, `wbraid`, `gbraid`, `fbclid`, `fbc`, `fbp`, `gad_source`, `gad_campaignid`, `landing_url`, `user_agent`, IP (nur kurz, für CAPI ungehasht nötig [M2]), `consent_ad_user_data`, `consent_ad_personalization`, `consent_ts` | Zuordnung Kanal/Kampagne; Material für Uploads |
| **Ereignis** | `event_id` (zugleich Meta-`event_id`), `session_id`, Typ (chat_gestartet / fragen_abgeschlossen / kauf), `event_ts`, Wert, Währung | Zwischenereignisse und Kauf |
| **Kauf** | `order_id` (zugleich Google-`order_id`/`transactionId`), `session_id`, Betrag brutto/netto, Währung, `paid_at`, Erstattung (Zeit, Betrag), gehashte E-Mail (SHA-256) | Käuferzahl, Enhanced Conversions |
| **LLM-Nutzung** (je Aufruf) | `call_id`, `session_id`, Zeit, Modell, `input_tokens`, `output_tokens`, Cache-Schreib-/Lese-Tokens, Preisversion → `kosten_eur` | Tokenkosten je Sitzung; Zähler stehen in der Anbieterantwort (Anthropic: `usage`, Cache-Tokens getrennt bepreist) [X4] |
| **Preistabelle** | Modell, gültig_ab, EUR je Million Token (Eingabe/Ausgabe/Cache) | Kosten nachrechenbar |
| **Ad-Spend täglich** | Datum, Kanal, Konto, Kampagne, ggf. Gruppe/Format, Spend, Währung, Impressionen, Klicks, `abgerufen_am` | Zähler der Formel; Meta Insights `spend` [M13], Google `metrics.cost_micros` [G19]; nachträgliche Korrekturen überschreiben |
| **Upload-Protokoll** | `event_id`, Ziel (Meta CAPI / Google API / Data Manager), Status, Sendezeit, Antwort, Versuche | Einhaltung 7 Tage / 24 h / 63–90 Tage; Fehlersuche |
| **Plattform-Report** (optional) | Tag, Kampagne, gemeldete Conversions (inkl. modellierter) | Abgleich eigene Zahl gegen Plattformzahl |

## 5. YouTube

- Gleiche Konten, Kennungen und Wege wie Google Ads allgemein (`gclid`, iOS `wbraid`/`gbraid`) [G5]. Video-Action-Kampagnen sind ab April 2025 nicht mehr neu anlegbar und werden bis April 2026 zu Demand Gen umgestellt; Berichte nach Format (In-Feed, Skippable In-Stream, Shorts) [G14]. Für YouTube gelten damit die Demand-Gen-Schwellen aus Frage 2.
- Ohne Klick zählt Google Engaged-View-Conversions (Skippable In-Stream ≥ 10 s oder ganze Anzeige, falls kürzer; In-Feed und Shorts ≥ 5 s; Fenster standardmäßig 3 Tage) [G11] und View-through-Conversions (Standardfenster 1 Tag) [G12, G13]. Diese haben in unserem Funnel keine Click-ID und erscheinen in eigenen Daten als direkt oder organisch; nur Google Ads sieht sie. Import-Uploads zählen für Engaged-View nur, wenn sie höchstens 14 Tage nach der Conversion erfolgen [G11].
- Gehashte Nutzerdaten (Enhanced Conversions) ermöglichen Zuordnung über Google-Konten ohne Klick [G17]. Klickfenster 1 bis 90 Tage, Standard 30 [G13].
- iOS: Bei iOS-14+-Verkehr aus einigen Google-Apps wird `gclid` ohne Zustimmung nicht angehängt [G15]. Welche Apps (ob YouTube) betroffen sind: nicht belegt.

## Quellen (Abruf 05.10.2026)

| ID | URL | Art |
|---|---|---|
| G1 | https://support.google.com/google-ads/answer/15081888 | S |
| G2 | https://developers.google.com/google-ads/api/docs/conversions/upload-offline | S |
| G3 | https://support.google.com/google-ads/answer/13261987 | S |
| G4 | https://developers.google.com/data-manager/api/devguides/events/google-ads/online/send-events | S |
| G5 | https://raw.githubusercontent.com/googleapis/googleapis/master/google/ads/googleads/v25/services/conversion_upload_service.proto | D |
| G6 | https://github.com/googleapis/googleapis/tree/master/google/ads/datamanager/v1 (gelesen: `ingestion_service.proto`, `event.proto`, `consent.proto` über raw.githubusercontent.com) | D |
| G7 | https://support.google.com/google-ads/answer/16194756 | S |
| G8 | https://support.google.com/google-ads/answer/7012522 | S |
| G9a–f | https://support.google.com/google-ads/answer/6268632 (a), /12262960 (b), /16797388 (c), /15209611 (d), /13020501 (e), /10970825 (f) | S |
| G10a | https://support.google.com/google-ads/answer/13695607 | S |
| G10b | https://developers.google.com/tag-platform/security/guides/consent und https://developers.google.com/tag-platform/security/concepts/consent-mode | S |
| G10c | https://support.google.com/google-ads/answer/10548233 | S |
| G11 | https://support.google.com/google-ads/answer/10048752 | S |
| G12 | https://support.google.com/google-ads/answer/16542520 | S |
| G13 | https://support.google.com/google-ads/answer/3123169 | S |
| G14 | https://support.google.com/google-ads/answer/15110871 | S |
| G15 | https://support.google.com/google-ads/answer/10417364 | S |
| G16 | https://support.google.com/tagmanager/answer/7549390 | S |
| G17 | https://support.google.com/google-ads/answer/15712870 | S |
| G18 | https://support.google.com/google-ads/answer/11461796 | S |
| G19 | https://developers.google.com/google-ads/api/docs/query/cookbook | S |
| M1 | https://developers.facebook.com/documentation/ads-commerce/conversions-api/using-the-api | S |
| M2 | https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/customer-information-parameters | S |
| M3 | https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/fbp-and-fbc | S |
| M4 | https://developers.facebook.com/documentation/ads-commerce/conversions-api/deduplicate-pixel-and-server-events | S |
| M5 | https://developers.facebook.com/documentation/ads-commerce/conversions-api/best-practices | S |
| M6 | https://raw.githubusercontent.com/facebook/capi-param-builder/main/nodejs/capi-param-builder/src/model/Constants.js | D |
| M7 | https://raw.githubusercontent.com/facebook/facebook-python-business-sdk/main/facebook_business/adobjects/serverside/event.py | D |
| M8 | https://www.facebook.com/business/help/112167992830700/ | S |
| M8b | https://en-gb.facebook.com/business/help/269269737396981 | S |
| M8c | https://en-gb.facebook.com/business/help/203012060587398 | S |
| M9 | https://www.facebook.com/legal/technology_terms | S |
| M10 | https://www.facebook.com/business/help/181058782494426 | S |
| M11 | https://en-gb.facebook.com/business/help/460276478298895 | S |
| M12 | https://developers.facebook.com/docs/marketing-apis/data-processing-options | S |
| M13 | https://developers.facebook.com/docs/marketing-api/insights/ | S |
| M14 | https://www.facebook.com/business/help/964258670337005 | S |
| X1 | https://consentstack.io/blog/meta-conversions-api-consent (Sekundärquelle) | S |
| X2 | https://support.cookiehub.com/article/551-meta-pixel-consent-mode (Sekundärquelle) | S |
| X4 | https://getlago.com/docs/guide/ai-agents/agent-sdk/anthropic (Sekundärquelle) | S |

## Offene Punkte

1. **Alle Plattformzahlen stammen aus Suchauszügen** (7 Tage, 48 h, 90/63 Tage, 24 h, 14 Tage, 700 Klicks, 30/50 Conversions). Zuordnung einer Zahl zur genauen Seite kann im Auszug ungenau sein. Vor der Umsetzung gegen die Live-Doku prüfen.
2. **Recht, nicht recherchiert:** Darf eine Click-ID/UTM vor Einwilligung in Cookie, Local Storage oder serverseitiger Sitzung gespeichert werden? Darf CAPI ohne Einwilligung senden? Juristisch klären; X1 ist keine Rechtsquelle.
3. **Nicht belegt:** Meta-URL-Parameter-Makros für Kampagnen-/Anzeigen-IDs; Cookie-Laufzeit von `_fbc` im Pixel selbst (belegt ist nur der Standard von 90 Tagen in der Meta-Parameter-Bibliothek, `DEFAULT_1PC_AGE` [M6]); Laufzeit von `_gcl_aw`; Berichtsverzögerung nach Google-Import; ob CAPI ohne Pixel für die Auslieferung gleichwertig ist; Meta-Modellierung für EU-Nichteinwilliger.
4. **Meta-Attributionsfenster 2026:** Sekundärquellen (https://www.jonloomer.com/meta-ads-attribution-2026/) berichten Änderungen (7-Tage-View, 28-Tage-View entfernt); Meta-Primärquelle nicht gefunden, M11 nennt den Stand vor dieser Änderung.
5. **Volumenfrage offen:** Ob unser Budget die 700-Klick-Schwelle (Google) bzw. 50 Ereignisse/Woche (Meta) erreicht, hängt vom Budget und der Käuferquote ab, beides unbekannt.
6. **Optimierung auf Zwischenereignis:** Auswirkung auf Käuferqualität nicht belegt, A/B-Test nötig.
7. **LLM-Anbieter nicht festgelegt;** das Feld-Schema der Tokenzähler ist je Anbieter zu prüfen.
8. **iOS/YouTube:** welche Google-Apps `gclid` unterdrücken, ist nicht belegt.
