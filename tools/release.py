#!/usr/bin/env python3
"""Stage a GitHub release of the paper and the deck, and print the command that publishes it.

Run with:

    uv run python tools/release.py v1.1-conference                   # check, build, stage
    uv run python tools/release.py v1.1-conference --use DIR          # stage files already built
    uv run python tools/release.py v1.1-conference --use DIR --target <commit>
    uv run python tools/release.py v1.1-conference --full            # add the full-resolution deck

A release carries PAP_<number>.pdf and PRE_<number>.pptx, the names PHUSE files them under,
with the number from paper/metadata.yaml. With --full it carries PRE_<number>-full.pptx as
well, the deck with its drawings at full resolution (tools/build_slides.py --full). The script

  * refuses a working tree with uncommitted changes to tracked files, a tag that exists
    already, and a tag without its own section in CHANGELOG.md (a "## <tag>" heading);
  * without --use, runs tools/check_sources.py, tools/build_paper.py and
    tools/build_slides.py --final (and --final --full with --full), and takes the files from out/;
  * with --use DIR, takes the files from DIR instead and builds nothing, for files that
    must stay byte for byte what was uploaded (a rebuild gets a new creation date);
  * copies them into dist/<tag>/, writes the tag's CHANGELOG.md section beside them as
    notes.md, and prints the `gh release create` command.

It never publishes by itself: the author reads the command and runs it. A published release
is the frozen copy of what was handed in or shown, so a change gets a new tag, never a new
upload over an old one. dist/ is git-ignored, and the build-output hook refuses hand edits there.
"""
from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "out"
DIST = REPO / "dist"
METADATA = REPO / "paper" / "metadata.yaml"
CHANGELOG = REPO / "CHANGELOG.md"
TAG = re.compile(r"^v[0-9A-Za-z][0-9A-Za-z.\-]*$")


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"error: git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def run(*args: str) -> None:
    print(f"$ {' '.join(args)}", flush=True)
    if subprocess.run([sys.executable, *args], cwd=REPO).returncode != 0:
        sys.exit(f"error: {args[0]} failed; nothing staged")


def notes_for(tag: str) -> tuple[str, str]:
    """The heading and the body of the tag's section in CHANGELOG.md."""
    if not CHANGELOG.exists():
        sys.exit("error: CHANGELOG.md not found")
    text = CHANGELOG.read_text(encoding="utf-8")
    m = re.search(rf"^## +({re.escape(tag)}(?![\w.\-])[^\n]*)\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    if not m or not m.group(2).strip():
        sys.exit(f"error: CHANGELOG.md has no section '## {tag}' with notes under it")
    return m.group(1).strip(), m.group(2).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Stage a GitHub release of the paper and the deck.")
    parser.add_argument("tag", help="the release tag, such as v1.1-conference")
    parser.add_argument("--use", type=Path, metavar="DIR",
                        help="take PAP_<number>.pdf and PRE_<number>.pptx (and with --full PRE_<number>-full.pptx) "
                             "from DIR instead of building them")
    parser.add_argument("--target", default="HEAD", metavar="REF",
                        help="the commit the tag points at (default HEAD); another commit only with --use")
    parser.add_argument("--full", action="store_true",
                        help="also attach PRE_<number>-full.pptx, the deck with its drawings at full resolution")
    args = parser.parse_args()

    tag = args.tag
    if not TAG.fullmatch(tag):
        sys.exit(f"error: '{tag}' is not a tag like v1.0 or v1.1-conference")
    if args.target != "HEAD" and args.use is None:
        sys.exit("error: --target needs --use; a build always comes from the working tree at HEAD")

    if git("status", "--porcelain", "--untracked-files=no"):
        sys.exit("error: the working tree has uncommitted changes; commit them first")
    remote = subprocess.run(["git", "ls-remote", "--tags", "origin", f"refs/tags/{tag}"],
                            cwd=REPO, capture_output=True, text=True,
                            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    if git("tag", "--list", tag) or remote.stdout.strip():
        sys.exit(f"error: the tag {tag} exists already; a published release stays frozen, cut a new tag")
    if remote.returncode != 0:
        print("WARNING: could not ask origin for its tags; gh will refuse a tag that exists there")
    target = git("rev-parse", "--verify", f"{args.target}^{{commit}}")
    if not git("branch", "--remotes", "--contains", target):
        print(f"WARNING: {target[:7]} is not on any remote branch yet; push it before you publish")

    title, notes = notes_for(tag)
    meta = yaml.safe_load(METADATA.read_text(encoding="utf-8")) or {}
    number = str(meta.get("paper_number", "") or "").strip()
    if not number:
        sys.exit("error: paper/metadata.yaml has no paper_number")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", number):
        sys.exit(f"error: paper/metadata.yaml: paper_number {number!r} is not a file-name part "
                 "(letters, digits, - and _)")
    names = [f"PAP_{number}.pdf", f"PRE_{number}.pptx"]
    if args.full:
        names.append(f"PRE_{number}-full.pptx")

    if args.use is None:
        run("tools/check_sources.py")
        run("tools/build_paper.py")
        run("tools/build_slides.py", "--final")
        if args.full:
            run("tools/build_slides.py", "--final", "--full")
        source = OUT
    else:
        source = args.use if args.use.is_absolute() else Path.cwd() / args.use
    missing = [n for n in names if not (source / n).is_file()]
    if missing:
        sys.exit(f"error: {', '.join(missing)} not found in {source}")

    stage = DIST / tag
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    for name in names:
        shutil.copy2(source / name, stage / name)
    (stage / "notes.md").write_text(notes, encoding="utf-8")

    print(f"\nstaged {stage.relative_to(REPO)}/ from {target[:7]}:")
    for name in names:
        print(f"  {name}  {(stage / name).stat().st_size // 1024} KB")
    assets = [str((stage / n).relative_to(REPO)) for n in names]
    command = ["gh", "release", "create", tag, *assets,
               "--target", target, "--title", title,
               "--notes-file", str((stage / "notes.md").relative_to(REPO))]
    print("\nCheck the files, then publish from the repository root with:\n")
    print("  " + shlex.join(command))


if __name__ == "__main__":
    main()
