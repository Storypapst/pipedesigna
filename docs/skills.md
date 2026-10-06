# Skills in Cloud-Sessions

## Warum Projekt-Skills

Laut Claude-Code-Doku lädt eine Cloud-Session `.claude/skills/`, `.claude/agents/` und `.claude/commands/` eines Repos, weil sie Teil des Klons sind. Plugins und Marketplaces, die ein Repo in `.claude/settings.json` einschaltet, installiert eine Cloud-Session dagegen nicht. Skills im Home-Verzeichnis des Nutzers fehlen ebenfalls; Skills, die auf claude.ai aktiviert sind, laden Cloud-Sessions automatisch. Quelle: https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup

Deshalb liegen die Skills in diesem Repo unter `.claude/skills/` und `.claude/agents/`.

## Matt Pocock, Version 1.3.1

Quelle: [mattpocock/skills](https://github.com/mattpocock/skills), Commit `4588b32` (2026-10-05). Es sind 25 Skills aus dem Plugin-Manifest des Upstream-Repos: Engineering (`wayfinder`, `to-spec`, `to-tickets`, `prototype`, `implement`, `implement-spec`, `research`, `domain-modeling`, `tdd`, `triage`, `code-review`, `pr`, `retro`, `wizard`, `ask-matt`, `setup-matt-pocock-skills`, `grill-with-docs`, `improve-codebase-architecture`, `diagnosing-bugs`, `codebase-design`) und Productivity (`grill-me`, `handoff`, `teach`, `wait-what`, `writing-for-agents`).

Nicht übernommen: `grilling` und `to-questionnaire`. Beide gibt es auf dem Account in angepasster Fassung, und eine zweite Kopie könnte sie überschreiben oder doppeln.

Lizenz: MIT, siehe `docs/third-party/mattpocock-skills-LICENSE`.

## pstack (Poteto / Lauren Tan), Claude-Port

Quelle: [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude), Verzeichnis `plugins/pstack`, Version 0.9.73, Commit `4d4e159` (2026-10-06). Das ist ein Drittanbieter-Port von Potetos pstack (Original: `cursor/plugins`, Ordner `pstack`). Lizenzen und Hinweise: `docs/third-party/pstack-claude/`.

- **Umbenennung:** Jeder Skill und jeder Agent bekommt das Suffix `-pstack` (`tdd` wird `tdd-pstack`, `poteto-mode` wird `poteto-mode-pstack`). `setup-pstack` heißt schon so und bleibt. Damit gibt es keinen Konflikt mit den Pocock-Skills (`tdd`, `teach`). Die Verweise in den Markdown-Dateien sind angepasst: `pstack:<name>`, Namen in Backticks, `/name` und relative Pfade. Skripte (`.ts`, `.mjs`, `.sh`) sind unverändert.
- **Umfang:** 58 Skills unter `.claude/skills/*-pstack/`, 12 Agents unter `.claude/agents/*-pstack.md`.
- **Nicht übernommen:** der SessionStart-Hook, `models.json` und `pi/`. Der Hook weist jede Session an, bei größeren Aufgaben `poteto-mode` zu starten. Das konkurriert mit dem Wayfinder-Ablauf, deshalb ist er nicht aktiv. Er enthält kein Netzwerk und schreibt nichts.
- **Aufruf:** `/poteto-mode-pstack` zu Beginn einer Aufgabe, `/poteto-help-pstack` für die Übersicht.
- **Kosten:** Die Skill-Liste der pstack-Skills belegt grob 3.500 Tokens pro Session (Schätzung: Zeichen geteilt durch 4), davon etwa 1.400 für die 24 `principle-*`-Skills. Wer weniger will, löscht Ordner unter `.claude/skills/`.
- **Bekannte Lücken:** Wo ein Skill einen anderen nur im Fließtext ohne Backticks nennt („run how and why"), blieb der Text unverändert; das Modell muss es aus dem Zusammenhang auflösen. Skripte unter `poteto-mode-pstack/scripts/` brauchen Bun, und einzelne Pfade gehen von einem installierten Plugin aus. In einer Cloud-Session ist das noch nicht ausprobiert.

## Erster Aufruf

In einer neuen Cloud-Session mit diesem Repo `/` tippen. Es müssen `wayfinder`, `to-spec`, `to-tickets`, `prototype`, `implement`, `teach` und `poteto-mode-pstack` erscheinen. Danach einmal `/setup-matt-pocock-skills` laufen lassen; das legt fest, dass die Wayfinder-Karte als GitHub-Issues im Projekt https://github.com/users/Storypapst/projects/1 liegt.

## Aktualisieren

- **Pocock:** Upstream klonen, die Skills aus `.claude-plugin/plugin.json` (ohne `grilling`, `to-questionnaire`) nach `.claude/skills/<name>/` kopieren, Version und Commit oben ändern, per PR einspielen.
- **pstack:** Upstream klonen, `python3 tools/vendor-pstack.py <klon>/plugins/pstack` ausführen, Version und Commit oben ändern, per PR einspielen. Das Skript löscht vorher die alten `*-pstack`-Ordner und Agents. Neue Upstream-Skills mit gleichem Namen wie ein Pocock-Skill bekommen automatisch das Suffix.

## Account-weit statt pro Repo (optional)

Das Plugin „Skills For Real Engineers" im Anthropic-Verzeichnis enthält die Pocock-Skills, im Verzeichnis lag am 2026-10-05 aber die Fassung 1.2.3. Aktivierung im Browser auf claude.ai im Bereich für Plugins/Skills; Menüpunkte nicht raten, bei Unklarheit nachfragen. Ein Playwright-Agent muss bei Login, 2FA, Zahlung und Berechtigungsdialogen stoppen. Doppelte Namen mit den Projekt-Skills sind möglich; wie die Doku Konflikte zwischen Projekt- und Plugin-Skills auflöst, ist nicht belegt.
