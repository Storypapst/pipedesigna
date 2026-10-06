# Prompts worth copying

Swap in the real paths, skills, and done checks. Informal wording works.

## Understand

- `/poteto-mode-pstack read <thread>. restate the underlying issue in your own words, in plain english.`
- `/poteto-mode-pstack investigate why <symptom>. give me what we know, what data you used, and your best hypotheses. don't change any code yet.`
- `use /how-pstack to understand <subsystem>. then use /why-pstack to find out why it broke recently.`
- `/recall-pstack my work on <topic> from last week, then read <issue>.`
- `/teach-pstack me why you implemented it this way and not <other way>. what did you trade off?`
- `/poteto-mode-pstack take over this branch. read the decision log, find what's done, and continue. don't redo finished work.`

## Build

- Bug: `/poteto-mode-pstack <symptom>. repro first, then fix and verify.`
- Bug in an app: `/poteto-mode-pstack repro this with /verify. if it repros on main, fix it and show me a video as proof.`
- Bug with a cheap test: `/poteto-mode-pstack repro <bug> first. if there's a cheap test path, /tdd-pstack it. then fix and rerun.`
- Feature: `/poteto-mode-pstack add <behavior>. <current output> stays byte-identical. verify both.`
- Refactor: `/poteto-mode-pstack move <code> into one module, zero behavior change. record the current output first and prove it's unchanged after.`
- Perf: `/poteto-mode-pstack <operation> takes <time> on <fixture>. trace it, fix the measured cause, show me before and after.`

## Design and plan

- `/poteto-mode-pstack prototype a few options for <feature>. take screenshots or videos for me to compare.`
- `/poteto-mode-pstack we need <feature>. /architect-pstack it first, and answer open questions with prototypes. let me review before proceeding.`
- `/poteto-mode-pstack write a tutorial for how i would use <new package> first. then /teach-pstack me why it beats the current one.`
- `ask /arena-pstack for a second opinion on this thread and our approach.`
- `/poteto-mode-pstack turn this design into a plan. small verifiable PRs, each with its own verification steps.`
- `/poteto-mode-pstack plan the migration of <library> to <target>. small verifiable PRs. the result must match the original exactly, bugs included.`

## Review and ship

- `/interrogate-pstack the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's a real bug or regression.` Read the dismissals too.
- `/swarm-pstack check every package under <dir> against its check script. one worker per package. one report.`
- `/poteto-mode-pstack open the pr. small ordered commits, evidence in the description.`
- `/poteto-mode-pstack babysit this pr. get it green.` For status only: `/poteto-mode-pstack check on pr <number>. anything outstanding?`
- `/poteto-mode-pstack land the stack.`

## Away and back

- `/poteto-mode-pstack im going to bed. <goal> in a fresh worktree off <base>. done means <checks>. keep a decision log. don't ask me before committing. /loop until done. if you're truly stuck after a few hours, stop and write up why.`
- `/show-me-your-work-pstack catch me up on what you did last night.` Read its Attention section first.
- `/poteto-mode-pstack full autopilot on this queue. each item is independent.`
- `/poteto-mode-pstack autopilot these changes but stack them, don't ship. i'll land the stack.`
- `/reflect-pstack capture what we learned so the next run doesn't repeat it.` Approve only edits that change a future decision.
- `/bro-pstack` restates the last reply in plain words.
