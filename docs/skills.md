# Skills in Cloud-Sessions

## Was bereitgestellt ist

Die Skills aus [mattpocock/skills](https://github.com/mattpocock/skills) Version **1.3.1** (Commit `4588b32`, 2026-10-05) liegen unter `.claude/skills/`. Claude Code lädt Projekt-Skills, wenn eine Session dieses Repo enthält. Enthalten sind die 27 Skills aus dem Plugin-Manifest des Upstream-Repos, abzüglich der beiden unten genannten, also 25: Engineering (`wayfinder`, `to-spec`, `to-tickets`, `prototype`, `implement`, `implement-spec`, `research`, `domain-modeling`, `tdd`, `triage`, `code-review`, `pr`, `retro`, `wizard`, `ask-matt`, `setup-matt-pocock-skills`, `grill-with-docs`, `improve-codebase-architecture`, `diagnosing-bugs`, `codebase-design`) und Productivity (`grill-me`, `handoff`, `teach`, `wait-what`, `writing-for-agents`).

Nicht übernommen, weil sie auf dem Account in angepasster Fassung existieren und eine zweite Kopie sie überschreiben oder doppeln könnte: `grilling` und `to-questionnaire`.

Lizenz der Skills: MIT, siehe `docs/third-party/mattpocock-skills-LICENSE`.

## Erster Aufruf

In einer neuen Cloud-Session mit diesem Repo `/` tippen. Es müssen `wayfinder`, `to-spec`, `to-tickets`, `prototype`, `implement` und `teach` erscheinen. Danach einmal `/setup-matt-pocock-skills` laufen lassen; das legt fest, dass die Wayfinder-Karte als GitHub-Issues im Projekt https://github.com/users/Storypapst/projects/1 liegt.

## Aktualisieren

Upstream-Repo klonen, die Skills aus `.claude-plugin/plugin.json` (ohne `grilling`, `to-questionnaire`) nach `.claude/skills/<name>/` kopieren, Version und Commit oben ändern, per PR einspielen.

## Account-weit statt pro Repo (optional)

Das Plugin „Skills For Real Engineers" im Anthropic-Verzeichnis enthält dieselben Skills, im Verzeichnis lag am 2026-10-05 aber die Fassung 1.2.3. Aktivierung im Browser auf claude.ai im Bereich für Plugins/Skills; Menüpunkte nicht raten, bei Unklarheit nachfragen. Ein Playwright-Agent muss bei Login, 2FA, Zahlung und Berechtigungsdialogen stoppen. Prüfen: neue Session, `/` tippen.

## Offen

`pstack`: welche Variante gemeint ist, ist nicht geklärt (siehe Issue #1).
