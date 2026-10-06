#!/usr/bin/env python3
"""Spielt pstack als Projekt-Skills und Projekt-Agents mit Suffix "-pstack" ein.

Quelle: michael-denyer/pstack-claude, Verzeichnis plugins/pstack.
Aufruf:  python3 tools/vendor-pstack.py <pfad/zu/pstack-claude/plugins/pstack>

Warum: Cloud-Sessions laden keine Plugins, die ein Repo in .claude/settings.json
einschaltet. Projekt-Skills unter .claude/skills/ und Projekt-Agents unter
.claude/agents/ werden geladen. Das Suffix verhindert Namenskonflikte (z. B. tdd).

Umgeschrieben werden nur Markdown-Dateien: der Name im Kopf, `pstack:<name>`,
`<name>` in Backticks, /<name> und Pfade auf andere pstack-Skills. Skripte (.ts,
.mjs, .sh) bleiben unverändert. Nicht übernommen: Hooks, models.json, pi/.
Das Skript ist wiederholbar: es löscht zuerst die früheren *-pstack-Ordner.
"""
import os
import re
import shutil
import sys

SUFFIX = "-pstack"
TEXT_EXT = (".md",)
IGNORE = shutil.ignore_patterns("node_modules", "__pycache__", ".DS_Store")


def new(name):
    return name if "pstack" in name else name + SUFFIX


def main(src, root):
    skills_src = os.path.join(src, "skills")
    agent_src = [os.path.join(src, "agents"), os.path.join(src, "effort-agents")]
    skills = sorted(d for d in os.listdir(skills_src) if os.path.isdir(os.path.join(skills_src, d)))
    agents = sorted(os.path.splitext(f)[0] for d in agent_src for f in os.listdir(d) if f.endswith(".md"))
    names = set(skills) | set(agents)
    assert not (set(skills) & set(agents)), "Name ist Skill und Agent zugleich"
    alts = "|".join(sorted(map(re.escape, names), key=len, reverse=True))

    re_ns = re.compile(r"pstack:([a-z][a-z0-9]*(?:-[a-z0-9]+)*(?:-<[a-z]+>)?)")
    re_bt = re.compile(r"`(" + alts + r")`")
    re_sl = re.compile(r"(?<![\w/.\-:<>])/(" + alts + r")(?!(?:[\w\-/]|\.[a-z]))")
    re_up = re.compile(r"(\.\./)(" + alts + r")/")
    re_sk = re.compile(r"(?<![\w.\-/])skills/(" + alts + r")/")
    stats = {"ns": 0, "backtick": 0, "slash": 0, "path": 0, "name": 0}
    leftovers = []

    def sub_ns(m):
        t = m.group(1)
        if t in names or t.endswith(">"):
            stats["ns"] += 1
            return new(t)
        leftovers.append(m.group(0))
        return m.group(0)

    def rewrite(text, path):
        text = text.replace("<plugin>/skills/", ".claude/skills/")
        text = re_ns.sub(sub_ns, text)
        text, n = re_bt.subn(lambda m: "`" + new(m.group(1)) + "`", text)
        stats["backtick"] += n
        text, n = re_sl.subn(lambda m: "/" + new(m.group(1)), text)
        stats["slash"] += n
        text, n = re_up.subn(lambda m: m.group(1) + new(m.group(2)) + "/", text)
        stats["path"] += n
        text, n = re_sk.subn(lambda m: ".claude/skills/" + new(m.group(1)) + "/", text)
        stats["path"] += n
        return text

    def fix_frontmatter(text, expected):
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        assert m, "kein Frontmatter: " + expected
        fm = m.group(1)
        nm = re.search(r"^name:\s*[\"']?([^\"'\s]+)[\"']?\s*$", fm, re.M)
        assert nm and nm.group(1) == expected, "Name passt nicht: " + expected
        fm2 = fm[: nm.start()] + "name: " + new(expected) + fm[nm.end():]
        stats["name"] += 1
        return "---\n" + fm2 + "\n---\n" + text[m.end():]

    skills_dst = os.path.join(root, ".claude", "skills")
    agents_dst = os.path.join(root, ".claude", "agents")
    os.makedirs(skills_dst, exist_ok=True)
    os.makedirs(agents_dst, exist_ok=True)
    for d in os.listdir(skills_dst):
        if d.endswith(SUFFIX):
            shutil.rmtree(os.path.join(skills_dst, d))
    for f in os.listdir(agents_dst):
        if f.endswith(SUFFIX + ".md"):
            os.remove(os.path.join(agents_dst, f))

    for s in skills:
        dst = os.path.join(skills_dst, new(s))
        shutil.copytree(os.path.join(skills_src, s), dst, ignore=IGNORE)
        for dp, _, fs in os.walk(dst):
            for f in fs:
                p = os.path.join(dp, f)
                if not f.endswith(TEXT_EXT):
                    continue
                t = open(p, encoding="utf-8").read()
                if p == os.path.join(dst, "SKILL.md"):
                    t = fix_frontmatter(t, s)
                open(p, "w", encoding="utf-8").write(rewrite(t, p))

    for d in agent_src:
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            a = os.path.splitext(f)[0]
            t = open(os.path.join(d, f), encoding="utf-8").read()
            t = rewrite(fix_frontmatter(t, a), f)
            open(os.path.join(agents_dst, new(a) + ".md"), "w", encoding="utf-8").write(t)

    print("Skills:", len(skills), "Agents:", len(agents))
    print("Ersetzungen:", stats)
    print("pstack:-Verweise ohne Zuordnung:", sorted(set(leftovers)) or "keine")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(os.path.abspath(sys.argv[1]), os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
