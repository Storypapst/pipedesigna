# Chat-Basis: Open-Source-Oberfläche oder Eigenbau

Stand 2026-10-05. Ticket der Wayfinder-Karte `pipedesigna`. Eckige Klammern verweisen auf die Quellen unten.

## Fazit

1. LibreChat und Open WebUI bringen weder anonyme Gast-Sitzungen aus einem Werbeklick noch eine Bezahlschranke mit; beides müsste man um die Oberfläche herumbauen (Sicherheit: mittel, gelesen wurden README, Docs-Repos und Quellcode, nicht jede Einstellung).
2. Die Kostenmessung ist bei LibreChat je Konto und Gespräch eingebaut und bei Open WebUI nur eine Token-Statistik, doch beim Eigenbau auf der Messages API fällt sie ohnehin pro Antwort an und lässt sich direkt mit Klick-ID und Zahlung verknüpfen.
3. Meine Tendenz (Sicherheit: mittel) ist ein Eigenbau auf der Messages API, und das Agent SDK nur dann, wenn die Skills `grilling` und `domain-modeling` unverändert pro Sitzung laufen sollen, wofür man einen eigenen Prozess je Sitzung betreiben muss.

## Vergleich

| Kriterium | LibreChat | Open WebUI | Eigenbau (Messages API / Agent SDK) |
| --- | --- | --- | --- |
| 1. Sitzungsmodell | Kein Gastmodus dokumentiert: Auth nur über Konten (E-Mail, LDAP, Passkey, OAuth, OIDC, SAML) [6], `.env.example` ohne Gast-Option [4]. Login per Proxy-Header ist ein offener Feature-Request seit Feb 2024 [10]. Daten in MongoDB [7][8]; Session 15 min, Refresh-Token 7 Tage [4]. | Kein Gastmodus in der README [11]. `WEBUI_AUTH=False` heißt ein Nutzer, alle Chats für alle sichtbar [16], jeder mit Admin-Rechten [17]. Gastmodus-Issues (#3058, #9447, #15217) sind geschlossen, Kommentare nicht lesbar [16]. Umweg: Trusted-Header-Login legt unbekannte E-Mails automatisch an, auch ohne `ENABLE_SIGNUP` [15]; ein Proxy könnte je Klick eine synthetische Identität setzen (meine Schlussfolgerung, nicht erprobt). | Alles eigen: anonyme Session-ID aus dem Klick, eigene DB. Messages API ist zustandslos, die Historie wird mitgeschickt [27]. Agent SDK: Transkripte als JSONL auf lokaler Platte, Wiederaufnahme per `resume`; über mehrere Hosts nur mit `SessionStore`-Adapter [23]. |
| 2. Kosten je Sitzung | Eingebaut: Transaktionen mit Prompt-, Completion-, Cache-Tokens, Guthaben-Credits (1000 = 0,001 USD) [7], optionale Kostenanzeige je Gespräch (v0.8.8) [2][7]. Guthaben standardmäßig aus [5]. Nativer Anthropic-Endpoint [4]. | Admin-Analytics: Tokens je Modell und Nutzer, keine Währung [18]. Anthropic läuft standardmäßig über die OpenAI-kompatible Schnittstelle [19], die laut Anthropic nicht für Produktion gedacht ist, ohne Prompt Caching und mit leeren `prompt_tokens_details` [20]; in langen Fragenrunden teurer und ungenauer. | Messages API: `usage` in jeder Antwort [27], Summe je Sitzung mal Preistabelle [28]. Agent SDK: `total_cost_usd`, laut Doku nur clientseitige Schätzung [22]. Anthropics Usage-API gruppiert nach Key, Workspace, Modell, nicht nach eigener Sitzungs-ID [26]. |
| 3. Prompt, Tools, Datei | `modelSpecs` mit `preset.instructions`, `default: true` sperrt die Nutzerwahl [5]; Agents, MCP, Skills, Code-Interpreter [1][2]. Spec als Datei: nicht geprüft. | Filters, Actions, Pipes, Tools, Skills, MCP [11]. Datei-Ausgabe: nicht geprüft. | Frei. Agent SDK: Skills, Subagents, Hooks, MCP, Write-Tool [21]; `AskUserQuestion` liefert 1–4 Fragen mit je 2–4 Optionen, eigene Fragen lassen sich nicht einschleusen [25]. |
| 4. Einbettung, Schranke | Vollständige App auf Port 3080 [8]; iframe-Embed nur als offener Feature-Request, der selbst Login voraussetzt [9]. MIT ohne Branding-Klausel [3]. Bezahlschranke nicht eingebaut. | Kein Embed-Feature belegt [11]. Seit v0.6.6 muss das „Open WebUI“-Branding bleiben, Ausnahme bis 50 Endnutzer in 30 Tagen oder Enterprise-Lizenz [13][14]; ob anonyme Gäste zählen, ist ungeklärt. Keine Bezahlschranke. | Domain, Layout, Tracking frei; der Chat kann eine eigene Seite statt iframe sein. Schranke ist Serverlogik: Spec erst nach Zahlungs-Webhook ausliefern (Einschätzung). Agent SDK: „Claude Code“ nicht als Name, „Powered by Claude“ erlaubt [21]. |
| 5. Hosting, Lizenz, Pflege | Compose mit 6 Containern (api, MongoDB, Meilisearch, pgvector, RAG-API, Admin-Panel) [8]. MIT [3]. v0.8.8 am 01.10.2026 nach rc1–rc4 seit August [2]; 45,3k Sterne [1]. | Ein Container [11]. BSD-3 plus Branding-Klausel [13][14]. v0.11.4 am 21.09.2026 (Seite ohne Jahr, abgeleitet) [12]; 154k Sterne [11]. | Messages API: gewöhnlicher Webdienst. Agent SDK: ein Subprozess je Sitzung, Richtwert 1 GiB RAM, 1 CPU, 5 GiB Platte je Agent [24]; Auth per API-Key statt claude.ai-Login, Anthropic Commercial Terms [21]. |
| 6. Aufwand | Bauen: Gast-/Konto-Brücke, Zahlung und Freischaltung, Spec-Export, Funnel-Branding, Sitzung↔Klick-ID. Prompt und Limits per Konfiguration, der Rest ist Fremdcode oder Zusatzdienst. | Dasselbe, dazu Anthropic-Pipe oder LiteLLM für Caching [19] und Klärung der Branding-Lizenz. | Bauen: Chat-UI (Baustein z. B. Vercel AI SDK `useChat` [33]), Session-Backend, Prompt, Kostenzähler, Zahlung, Spec-Export; kein Fremdcode zu pflegen. Agent SDK zusätzlich: Container je Sitzung, `SessionStore`. |

**Weitere Projekte.** AnythingLLM (MIT, v1.17.0 am 01.10.2026): Embed-Widget per Script oder iframe, Zufalls-Session-ID ohne Login, System-Prompt und Modell überschreibbar [30]; Kostenanzeige, Fragenrunden, Datei-Ausgabe nicht belegt. Dify (Apache-2.0 plus Zusatz: kein Mehrmandanten-Betrieb ohne Genehmigung, Logo bleibt [31]; v1.17.1 am 10.09.2026 [32]): `user` vergibt der Aufrufer, Gespräche sind nur für denselben `user` sichtbar [31]; ob der Funnel als Mehrmandanten-Betrieb gilt, ist ungeklärt. Managed Agents (Anthropic-gehostet, Beta): Tokens plus 0,08 USD je Session-Stunde, nicht ZDR-fähig [28][29]; nicht vertieft.

## Tendenz und abhängige Entscheidungen

Für den Eigenbau spricht: Anonymer Einstieg und Zahlschranke fehlen in beiden Oberflächen; die Break-even-Kennzahl der Karte braucht Tokenkosten je Sitzung samt Klick und Kauf; Konten, Verlauf und Modellwahl der Oberflächen müsste man im Funnel eher abschalten. Dagegen: Die Oberflächen liefern Chat-UI und Persistenz fertig, für den Prototyp-Lauf könnte LibreChat mit Guthaben-Konten genügen (Einschätzung).

Daran hängen drei Entscheidungen des Auftraggebers:
- Skills `grilling` und `domain-modeling` unverändert nutzen (Agent SDK, Prozess je Sitzung) oder als Prompt und Tool nachbauen (Messages API)?
- Wie hart muss die Kostenobergrenze je Sitzung vor der Zahlung sein, darf eine Sitzung mittendrin abgebrochen werden?
- Soll der Prototyp-Lauf schnell mit einer Fertig-Oberfläche starten oder schon auf der Produktbasis?

## Quellen

[1] https://github.com/danny-avila/LibreChat
[2] https://github.com/danny-avila/LibreChat/releases/tag/v0.8.8
[3] https://raw.githubusercontent.com/danny-avila/LibreChat/main/LICENSE
[4] https://raw.githubusercontent.com/danny-avila/LibreChat/main/.env.example
[5] https://raw.githubusercontent.com/danny-avila/LibreChat/main/librechat.example.yaml
[6] https://raw.githubusercontent.com/LibreChat-AI/librechat.ai/main/content/docs/configuration/authentication/index.mdx
[7] https://raw.githubusercontent.com/LibreChat-AI/librechat.ai/main/content/docs/configuration/token_usage.mdx
[8] https://raw.githubusercontent.com/danny-avila/LibreChat/main/docker-compose.yml
[9] https://github.com/danny-avila/LibreChat/issues/16357
[10] https://github.com/danny-avila/LibreChat/issues/1856
[11] https://github.com/open-webui/open-webui, https://raw.githubusercontent.com/open-webui/open-webui/main/README.md
[12] https://github.com/open-webui/open-webui/releases
[13] https://raw.githubusercontent.com/open-webui/open-webui/main/LICENSE
[14] https://raw.githubusercontent.com/open-webui/docs/main/docs/license.mdx
[15] https://raw.githubusercontent.com/open-webui/open-webui/main/backend/open_webui/routers/auths.py
[16] https://github.com/open-webui/open-webui/issues/9447 (auch #3058, #15217)
[17] https://github.com/open-webui/open-webui/discussions/10982
[18] https://raw.githubusercontent.com/open-webui/docs/main/docs/features/administration/analytics/index.mdx
[19] https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-anthropic (nur als Suchtreffer, Domain gesperrt)
[20] https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk
[21] https://code.claude.com/docs/en/agent-sdk/overview
[22] https://code.claude.com/docs/en/agent-sdk/cost-tracking
[23] https://code.claude.com/docs/en/agent-sdk/sessions, https://code.claude.com/docs/en/agent-sdk/session-storage
[24] https://code.claude.com/docs/en/agent-sdk/hosting
[25] https://code.claude.com/docs/en/agent-sdk/user-input
[26] https://platform.claude.com/docs/en/manage-claude/usage-cost-api
[27] https://platform.claude.com/docs/en/build-with-claude/working-with-messages
[28] https://platform.claude.com/docs/en/about-claude/pricing
[29] https://platform.claude.com/docs/en/managed-agents/overview
[30] https://github.com/Mintplex-Labs/anythingllm-embed, https://github.com/Mintplex-Labs/anything-llm/releases
[31] https://github.com/langgenius/dify, https://raw.githubusercontent.com/langgenius/dify/main/LICENSE, https://raw.githubusercontent.com/langgenius/dify-docs/main/en/api-reference/openapi_service.json
[32] https://github.com/langgenius/dify/releases
[33] https://github.com/vercel/ai

## Offene Punkte

- Tokenvolumen und Kosten einer typischen Grilling-Sitzung sind nicht geschätzt (Historie wird je Runde erneut gesendet; Sonnet 5.5: 2 USD Eingabe, 10 USD Ausgabe je Million Tokens [28]). Gehört in den Prototyp-Lauf.
- Open WebUI: Ob inzwischen ein Gastmodus existiert, ist offen, weil die Kommentare der geschlossenen Issues nicht abrufbar waren.
- Nicht geprüft: Datei-Ausgabe beider Oberflächen (LibreChat Code-Interpreter, Artifacts), iframe-Verhalten, Aufwand in Personentagen.
- Datenschutz und Auftragsverarbeitung für Anthropic-Aufrufe: nicht bewertet, gehört zu `research/recht.md`.
- Methodik: librechat.ai, docs.openwebui.com, docs.dify.ai, openwebui.com waren gesperrt, gelesen wurden stattdessen GitHub-Docs-Repos, READMEs, Quellcode. Das Abrufwerkzeug lieferte Zusammenfassungen statt Volltexte (Restunsicherheit bei Einzelangaben) und nannte bei Releases teils das Jahr 2024, was nicht zu den Inhalten passt; belegt ist 2026 nur für LibreChat v0.8.8, bei den übrigen habe ich es abgeleitet.
