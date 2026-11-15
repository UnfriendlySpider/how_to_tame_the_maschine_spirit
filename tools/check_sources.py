#!/usr/bin/env python3
"""Check the sources the paper and the talk rely on, and fail if one is broken.

    uv run python tools/check_sources.py

The accuracy rule says every file the slides quote must say what they claim.
The talk's reference part quotes the repository's own Claude Code setup, the
rules, skills, hooks and subagent this paper and talk are made with, and the
paper's sentences. This script makes that testable:

  * hooks      — each script in .claude/hooks/ is fed crafted tool-call JSON on
                 stdin and must return the expected exit code (2 = block);
                 the build-output hook must also fail closed without jq and
                 refuse edits to the release files staged in dist/;
  * skills     — every SKILL.md has YAML frontmatter with a description, and a
                 name (if given) equal to its directory; every review skill
                 (a name ending in -review, such as style-review) takes every
                 tool that writes or runs commands away with
                 disallowed-tools (Edit, Write, NotebookEdit, Bash,
                 PowerShell, Monitor);
  * agents     — every .claude/agents/*.md has a lowercase-hyphen name equal to
                 its file stem, and a description; reference-checker, which
                 the reference part shows as the read-only reviewer, grants
                 only reading tools (no write, MCP or Agent tool: a subagent
                 it starts would bring tools of its own) and has no memory
                 field (it gives Read, Write and Edit back);
  * settings   — .claude/settings.json is valid JSON, every hook command points
                 at an existing executable, the build-output hook is matched
                 for Edit and Write, every PreToolUse hook sets
                 onFailure: "block", and no path rule names a tool that
                 Claude Code never consults for paths (Write, Glob, …);
  * filecards  — every ::: filecard fence in paper/paper.md names a real file
                 and a known kind (the paper carries none since 2026-10-08);
  * pitfalls   — each ::: pitfalls fence parses (bullets, `---`, warning) and
                 there are exactly nine (chapters 2 to 10);
  * references — paper/references.md parses, every entry carries an
                 access date and the numbers follow the order of first
                 citation (the build also checks that every entry is cited);
  * slides     — slides/deck.yaml has one entry per storyline slide, in
                 order, and every file the slides quote exists, its line
                 ranges lie inside it and still contain their expected text;
                 every sentence the reference part quotes, most of them from
                 the paper, still stands in its source; the narrated deck's
                 clips match its slides; the paper's template places the
                 slides' AI label where its file has it.

Until 2026-10-27 the script was tools/check_examples.py and also ran the
playground, its data viewer and its example configuration; the playground left
the repository that day, and the working repository's history keeps it.

Standard library plus PyYAML, the fence parser from build_paper.py so the
fence grammar lives in one place, and the deck reader from build_slides.py
(with Pillow, which it brings, to measure the AI label).
Exit code 1 on any failure.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

import build_paper  # same directory; owns the fence grammar

REPO = Path(__file__).resolve().parent.parent
CLAUDE = REPO / ".claude"
HOOKS = CLAUDE / "hooks"
SKILLS = CLAUDE / "skills"
AGENTS = CLAUDE / "agents"
SETTINGS = CLAUDE / "settings.json"
PAPER_MD = REPO / "paper" / "paper.md"

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
AGENT_NAME = re.compile(r"^[a-z][a-z0-9-]*$")
# Split a tool field on commas, or on spaces outside a rule such as Bash(git *).
TOOL_SEPARATOR = re.compile(r",\s*|\s+(?![^()]*\))")
WRITE_TOOLS = {"Edit", "Write", "NotebookEdit", "Bash", "PowerShell", "Monitor"}
SPAWN_TOOLS = {"Agent", "Task"}   # Task is the Agent tool's old name, still accepted as an alias
# What the read-only reviewer may hold. Anything else, an MCP server's tools included, can act.
READ_ONLY_TOOLS = {"Read", "Grep", "Glob", "WebFetch", "WebSearch"}
READ_ONLY_REVIEWER = "reference-checker"   # R.5 shows it as the reviewer that cannot change a file

failures: list[str] = []
passes = 0


def ok(msg: str) -> None:
    global passes
    passes += 1
    print(f"  ok   {msg}")


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"  FAIL {msg}")


# --- hooks -----------------------------------------------------------------

def run_hook(script: Path, payload: dict, env: dict | None = None) -> tuple[int, str]:
    proc = subprocess.run(
        [str(script)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=REPO,
        env={**os.environ, "CLAUDE_PROJECT_DIR": str(REPO), **(env or {})},
    )
    return proc.returncode, proc.stderr.strip()


def tool_call(tool: str, **tool_input: str) -> dict:
    return {
        "session_id": "check-sources",
        "cwd": str(REPO),
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": tool_input,
    }


def check_hooks() -> None:
    print("hooks")
    if shutil.which("jq") is None:
        fail("jq is not on PATH; the hooks need it (and refuse to run without it)")
        return

    cases: list[tuple[str, dict, int]] = [
        ("protect-build-outputs.sh", tool_call("Write", file_path=str(REPO / "out" / "main.typ")), 2),
        ("protect-build-outputs.sh", tool_call("Edit", file_path=str(REPO / "out" / "PRE_ML19.pptx")), 2),
        ("protect-build-outputs.sh", tool_call("Edit", file_path=str(REPO / "dist" / "v1.0" / "PAP_ML19.pdf")), 2),
        ("protect-build-outputs.sh", tool_call("Write", file_path=str(REPO / "dist" / "v1.0" / "notes.md")), 2),
        ("protect-build-outputs.sh", tool_call("Edit", file_path=str(PAPER_MD)), 0),
    ]
    for name, payload, expected in cases:
        script = HOOKS / name
        if not script.exists():
            fail(f"{name} missing")
            continue
        if not os.access(script, os.X_OK):
            fail(f"{name} is not executable (chmod +x)")
            continue
        code, err = run_hook(script, payload)
        label = f"{name} {payload['tool_name']} {list(payload['tool_input'].values())[0]!s:.60}"
        if code == expected:
            ok(f"{label} -> exit {code}")
        else:
            fail(f"{label} -> exit {code}, expected {expected}. stderr: {err}")

    # Fail closed: without jq the guarding hook must refuse even a harmless
    # write. Give it a PATH that holds only what it needs before the jq check.
    guard = HOOKS / "protect-build-outputs.sh"
    if guard.exists():
        with tempfile.TemporaryDirectory() as tmp:
            for tool in ("bash", "cat"):
                found = shutil.which(tool)
                if found:
                    os.symlink(found, Path(tmp) / tool)
            code, err = run_hook(guard, tool_call("Edit", file_path=str(PAPER_MD)), env={"PATH": tmp})
        if code == 2 and "jq" in err:
            ok("protect-build-outputs.sh without jq on PATH -> exit 2 (fails closed)")
        else:
            fail(f"protect-build-outputs.sh without jq on PATH -> exit {code}, expected 2 naming jq. stderr: {err}")

    # The spelling hook is advisory and reads the file it is told about, so
    # give it two throwaway paper.md files: one with an American spelling and
    # one without.
    spelling = HOOKS / "check-british-spelling.sh"
    if spelling.exists():
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp) / "paper" / "paper.md"
            fake.parent.mkdir()
            fake.write_text("We prefer this color.\n\n```json\n{\"color\": 1}\n```\n", encoding="utf-8")
            code, err = run_hook(spelling, {**tool_call("Edit", file_path=str(fake)), "hook_event_name": "PostToolUse"})
            if code == 2 and "color" in err:
                ok("check-british-spelling.sh flags 'color' in prose")
            else:
                fail(f"check-british-spelling.sh should flag 'color' (exit {code}, stderr: {err})")
            fake.write_text("We prefer this colour.\n\n```json\n{\"color\": 1}\n```\n", encoding="utf-8")
            code, err = run_hook(spelling, {**tool_call("Edit", file_path=str(fake)), "hook_event_name": "PostToolUse"})
            if code == 0:
                ok("check-british-spelling.sh ignores code fences and British spellings")
            else:
                fail(f"check-british-spelling.sh false positive (exit {code}, stderr: {err})")
    else:
        fail("check-british-spelling.sh missing")


# --- frontmatter -----------------------------------------------------------

def frontmatter(path: Path) -> dict | None:
    m = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not m:
        return None
    data = yaml.safe_load(m.group(1))
    return data if isinstance(data, dict) else None


def tool_names(value: object) -> set[str]:
    """Tool names in a frontmatter field: 'Read, Grep', 'Read Grep' or a YAML list."""
    items = TOOL_SEPARATOR.split(value.strip()) if isinstance(value, str) else [str(v) for v in value or []]
    return {item.split("(")[0].strip() for item in items if item.strip()}


def check_skills() -> None:
    print("skills")
    found = sorted(SKILLS.glob("*/SKILL.md"))
    if not found:
        fail("no skills under .claude/skills/")
    for skill in found:
        fm = frontmatter(skill)
        rel = skill.relative_to(REPO)
        if fm is None:
            fail(f"{rel}: no YAML frontmatter")
            continue
        if not fm.get("description"):
            fail(f"{rel}: description missing")
            continue
        name = fm.get("name")
        if name and name != skill.parent.name:
            fail(f"{rel}: name '{name}' differs from directory '{skill.parent.name}'")
            continue
        if skill.parent.name.endswith("-review"):
            removed = tool_names(fm.get("disallowed-tools"))
            if not WRITE_TOOLS <= removed:
                fail(f"{rel}: disallowed-tools must name {', '.join(sorted(WRITE_TOOLS))} (commands write files too); the review reports, it does not repair")
                continue
            ok(f"{rel}: disallowed-tools removes {', '.join(sorted(removed))}")
        ok(f"{rel}")


def check_agents() -> None:
    print("agents")
    found = sorted(AGENTS.glob("*.md"))
    if not found:
        fail("no agents under .claude/agents/")
    for agent in found:
        fm = frontmatter(agent)
        rel = agent.relative_to(REPO)
        if fm is None:
            fail(f"{rel}: no YAML frontmatter")
            continue
        name = fm.get("name", "")
        if not AGENT_NAME.match(name):
            fail(f"{rel}: name '{name}' must be lowercase letters, digits and hyphens")
            continue
        if name != agent.stem:
            fail(f"{rel}: name '{name}' differs from file stem '{agent.stem}'")
            continue
        if not fm.get("description"):
            fail(f"{rel}: description missing")
            continue
        for skill_name in fm.get("skills", []) or []:
            if not (SKILLS / skill_name / "SKILL.md").exists():
                fail(f"{rel}: preloads unknown skill '{skill_name}'")
        if name == READ_ONLY_REVIEWER:
            # Without a tools field the agent would inherit every tool.
            granted = tool_names(fm.get("tools"))
            if not granted or granted & WRITE_TOOLS:
                writers = ", ".join(sorted(granted & WRITE_TOOLS)) or "every tool (no tools field)"
                fail(f"{rel}: grants {writers}, but the reference part (R.5) shows it as a reviewer that cannot change a file")
                continue
            # A memory field turns Read, Write and Edit back on for the memory files.
            if "memory" in fm:
                fail(f"{rel}: has a memory field, which gives Read, Write and Edit back, "
                     "but the reference part (R.5) shows it as a reviewer that cannot change a file")
                continue
            # Agent (Task before 2.1.63) lets it start subagents, which bring tools of their own.
            spawners = granted & SPAWN_TOOLS
            if spawners:
                fail(f"{rel}: grants {', '.join(sorted(spawners))}, so it could start a subagent with write tools, "
                     "but the reference part (R.5) shows it as a reviewer that cannot change a file")
                continue
            # Only reading tools: an MCP server's tools (mcp__…) or any other tool may write or post.
            others = {t for t in granted if t.split("(", 1)[0] not in READ_ONLY_TOOLS}
            if others:
                fail(f"{rel}: grants {', '.join(sorted(others))}, which are not reading tools, "
                     "but the reference part (R.5) shows it as a reviewer that cannot change a file")
                continue
            ok(f"{rel}: read-only tools ({', '.join(sorted(granted))}), no memory field, no Agent tool")
        ok(f"{rel}")
    if not (AGENTS / f"{READ_ONLY_REVIEWER}.md").exists():
        fail(f".claude/agents/{READ_ONLY_REVIEWER}.md missing; the reference part (R.5) quotes it")


# --- settings --------------------------------------------------------------

UNCONSULTED_PATH_TOOLS = ("Write", "Glob", "NotebookEdit", "MultiEdit")


def check_settings() -> None:
    print("settings")
    try:
        data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f".claude/settings.json unreadable: {exc}")
        return
    ok(".claude/settings.json is valid JSON")

    for event, groups in (data.get("hooks") or {}).items():
        for group in groups:
            matcher = group.get("matcher", "")
            if matcher and not re.fullmatch(r"[A-Za-z0-9_\-, |]*", matcher):
                # Regex matchers are allowed, but the repository's settings use plain lists.
                fail(f"hooks.{event}: matcher '{matcher}' is a regex; keep the settings to plain names")
            for hook in group.get("hooks", []):
                cmd = hook.get("command", "")
                path = cmd.replace('"$CLAUDE_PROJECT_DIR"', str(REPO)).replace("${CLAUDE_PROJECT_DIR}", str(REPO)).replace("$CLAUDE_PROJECT_DIR", str(REPO))
                script = Path(path.split()[0]) if path else None
                if script and script.exists() and os.access(script, os.X_OK):
                    ok(f"hooks.{event} [{matcher}] -> {script.relative_to(REPO)}")
                else:
                    fail(f"hooks.{event} [{matcher}] -> '{cmd}' does not resolve to an executable file")

    # The build-output hook must see both file tools.
    needed = {"Edit", "Write"}
    guard = [
        group.get("matcher", "") for group in (data.get("hooks") or {}).get("PreToolUse", [])
        if any("protect-build-outputs.sh" in h.get("command", "") for h in group.get("hooks", []))
    ]
    if guard and all(needed <= set(re.split(r"[\s,|]+", matcher)) for matcher in guard):
        ok(f"protect-build-outputs.sh is matched for {', '.join(sorted(needed))}")
    else:
        fail(f"PreToolUse: protect-build-outputs.sh needs a matcher naming {', '.join(sorted(needed))}, found {guard or 'no entry'}")

    # A guarding hook that cannot start, times out or exits with an unexpected
    # code lets the call through unless it sets onFailure: "block" (2.1.295+).
    loose = [Path(h.get("command", "")).name.strip('"')
             for group in (data.get("hooks") or {}).get("PreToolUse", [])
             for h in group.get("hooks", []) if h.get("onFailure") != "block"]
    if loose:
        fail(f"PreToolUse: {', '.join(loose)} must set \"onFailure\": \"block\", or a failing hook lets the call through")
    else:
        ok('every PreToolUse hook sets "onFailure": "block" (fails closed)')

    perms = data.get("permissions") or {}
    for kind in ("allow", "deny", "ask"):
        for rule in perms.get(kind, []) or []:
            m = re.fullmatch(r"(\w+)\((.*)\)", rule)
            if m and m.group(1) in UNCONSULTED_PATH_TOOLS and m.group(2):
                fail(f"permissions.{kind}: '{rule}' — Claude Code only consults Edit(path) and Read(path) rules; use Edit(...)")
            else:
                ok(f"permissions.{kind}: {rule}")


# --- file cards and references --------------------------------------------

def check_filecards() -> None:
    print("filecards")
    cards = [
        body for kind, body in build_paper.split_segments(PAPER_MD.read_text(encoding="utf-8"))
        if kind == "filecard"
    ]
    if not cards:
        ok("no filecard fences (the paper names no file of the repository)")
    for body in cards:
        try:
            rel, kind, _caption, _rest = build_paper.parse_filecard(body)
        except SystemExit as exc:
            fail(str(exc))
            continue
        ok(f"filecard {rel.as_posix()} ({kind})")


def check_pitfalls() -> None:
    print("pitfalls")
    cards = [
        body for kind, body in build_paper.split_segments(PAPER_MD.read_text(encoding="utf-8"))
        if kind == "pitfalls"
    ]
    for body in cards:
        try:
            bullets, warning = build_paper.parse_pitfalls(body)
        except SystemExit as exc:
            fail(str(exc).splitlines()[0])
            continue
        n = sum(1 for line in bullets.splitlines() if line.startswith("- "))
        ok(f"pitfalls card: {n} bullet(s){', with warning' if warning else ''}")
    if len(cards) == build_paper.MECHANISM_CHAPTERS:
        ok(f"one pitfalls card per mechanism chapter ({len(cards)})")
    else:
        fail(f"expected {build_paper.MECHANISM_CHAPTERS} pitfalls cards, found {len(cards)}")


def check_references() -> None:
    print("references")
    try:
        _lead, groups = build_paper.parse_references()
    except SystemExit as exc:
        fail(str(exc))
        return
    n = sum(len(g.entries) for g in groups)
    ok(f"references.md parses: {n} entries in {len(groups)} group(s), all with access dates")
    order = build_paper.first_citations(PAPER_MD.read_text(encoding="utf-8"))
    if order == list(range(1, len(order) + 1)):
        ok(f"references numbered in order of first citation, 1 to {len(order)}")
    else:
        fail("references not numbered in order of first citation; run tools/build_paper.py --renumber")


# --- the talk's slides -------------------------------------------------------

def check_slides() -> None:
    print("slides")
    import build_slides  # same directory; imported here so a broken deck fails only this step

    try:
        story = build_slides.parse_storyline()
        deck = build_slides.load_deck(story)
        resolved = build_slides.resolve_all(story, deck)
    except SystemExit as exc:
        fail(str(exc))
        return
    ok(f"slides/deck.yaml lays out the storyline's {len(story)} slides, in order")
    blocks = [b for spec in deck["slides"].values()
              for b in (spec.get("panel") or []) + (spec.get("explain") or [])]
    quoted = [b for b in blocks if "file" in b]
    ok(f"{len(quoted)} quoted file excerpt(s) still hold their expected text")
    sourced = [b for b in blocks if "source" in b]
    ok(f"{len(sourced)} quoted sentence(s) still stand in their source, most of them in the paper")
    ok(f"every panel resolves ({sum(len(r['panel']) + len(r['inset']) + len(r['explain']) for r in resolved.values())} items)")
    try:
        plan = build_slides.narration_plan(story, deck)
    except SystemExit as exc:
        fail(str(exc))
    else:
        clips = sum(1 for entry in plan.values() if entry["pieces"])
        ok(f"slides/narration/clips.yaml gives the narrated deck's {len(plan)} slides {clips} clips and "
           f"{len(plan) - clips} hold(s); the clips play every word of the takes once")

    # The paper's template cannot measure an image, so it holds the AI label's place in its
    # file by hand. Both must still match the file deck.yaml names.
    label = deck["brand"].get("ai_label")
    if label:
        template = (REPO / "tools" / "template.typ").read_text(encoding="utf-8")
        m = re.search(r"let px = ai-label-size / (\d+).*?dx: -(\d+) \* px, dy: -(\d+) \* px,\s*"
                      r'image\("/([^"]+)".*?width: (\d+) \* px, height: (\d+) \* px', template, re.S)
        if not m:
            fail("tools/template.typ: `ai-label` no longer has the form this check reads")
            return
        from PIL import Image
        with Image.open(REPO / str(label)) as im:
            left, top, right, _ = im.getchannel("A").getbbox()
            actual = (right - left, left, top, *im.size)
        expected = tuple(int(v) for v in m.group(1, 2, 3, 5, 6))
        if m.group(4) != str(label):
            fail(f"tools/template.typ labels the paper's figures with {m.group(4)}, deck.yaml the slides with {label}")
        elif expected != actual:
            fail(f"tools/template.typ places the AI label at {expected}, but {label} needs {actual} "
                 "(the icon's width, its left and top edge, the file's width and height, in px)")
        else:
            ok(f"the paper's figures carry the slides' AI label, {label}, cut to the icon")


def main() -> None:
    for step in (check_hooks, check_skills, check_agents, check_settings, check_filecards, check_pitfalls,
                 check_references, check_slides):
        step()
    print()
    if failures:
        print(f"{len(failures)} failure(s), {passes} passed")
        sys.exit(1)
    print(f"all {passes} checks passed")


if __name__ == "__main__":
    main()
