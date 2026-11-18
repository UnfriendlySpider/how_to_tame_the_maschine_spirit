#!/usr/bin/env python3
"""Build the paper and the talk, and turn them into pictures an agent can look at.

Run from the repository root with uv, so the project's own dependencies are used:

    uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py check
    uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py paper [--pages 1,3-5] [--ppi 110]
    uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py stats
    uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py slides [--ids 9.1,R.4] [--dpi 80]
    uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py all

Everything it renders lands in out/shots/ (generated and git-ignored, like the rest of out/):

    paper-pNN.png        one page of out/PAP_<number>.pdf, rendered by Typst itself
    paper-sheet.png      all pages side by side, to see the page breaks at a glance
    slide-NN-<id>.png    one slide of out/PRE_<number>.pptx, through LibreOffice and pdftoppm
    slides-sheet.png     every slide that was rendered, side by side
    deck/                LibreOffice's PDF of the deck

The driver creates out/shots/ itself: the project's deny rule Edit(/out/**) also stops an
agent's own mkdir or cp into out/, while a script the build runs may write there.
Exit code: that of the first step that failed, else 0.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
OUT = REPO / "out"
SHOTS = OUT / "shots"
FONTS = REPO / "tools" / "fonts"


def say(msg: str) -> None:
    print(f"[driver] {msg}", flush=True)


def run(cmd: list[str], **kw) -> int:
    say("$ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=REPO, **kw).returncode


def paper_number() -> str:
    import yaml  # a project dependency
    meta = yaml.safe_load((REPO / "paper" / "metadata.yaml").read_text(encoding="utf-8"))
    return str(meta["paper_number"])


def parse_ranges(spec: str | None, last: int) -> list[int]:
    """'1,3-5' -> [1, 3, 4, 5]; None -> every number from 1 to last."""
    if not spec:
        return list(range(1, last + 1))
    numbers: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            numbers += range(int(a), int(b) + 1)
        elif part:
            numbers.append(int(part))
    bad = [n for n in numbers if not 1 <= n <= last]
    if bad:
        sys.exit(f"[driver] no such page or slide: {bad} (there are {last})")
    return numbers


def contact_sheet(images: list[Path], labels: list[str], target: Path, columns: int, width: int) -> None:
    from PIL import Image, ImageDraw
    if not images:
        return
    thumbs = []
    for path in images:
        im = Image.open(path).convert("RGB")
        im.thumbnail((width, width * 4))
        thumbs.append(im)
    cell_h = max(t.height for t in thumbs) + 22
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * (width + 8) + 8, rows * (cell_h + 8) + 8), "white")
    draw = ImageDraw.Draw(sheet)
    for k, (thumb, label) in enumerate(zip(thumbs, labels)):
        x = 8 + (k % columns) * (width + 8)
        y = 8 + (k // columns) * (cell_h + 8)
        draw.text((x, y), label, fill=(200, 0, 0))
        sheet.paste(thumb, (x, y + 18))
        draw.rectangle([x - 1, y + 17, x + thumb.width, y + 18 + thumb.height], outline=(180, 180, 180))
    sheet.save(target)
    say(f"wrote {target.relative_to(REPO)}")


# --- commands ----------------------------------------------------------------

def cmd_check(_args) -> int:
    return run([sys.executable, "tools/check_sources.py"])


def cmd_stats(_args) -> int:
    return run([sys.executable, "tools/build_paper.py", "--stats"])


def cmd_paper(args) -> int:
    if not args.no_build:
        code = run([sys.executable, "tools/build_paper.py"])
        if code:
            return code
    import typst  # a project dependency; the same compiler that made the PDF
    main = OUT / "main.typ"
    if not main.exists():
        say("out/main.typ is missing: build first (drop --no-build)")
        return 1
    pages = typst.compile(str(main), root=str(REPO), font_paths=[str(FONTS)], format="png", ppi=args.ppi)
    pages = pages if isinstance(pages, list) else [pages]
    say(f"out/PAP_{paper_number()}.pdf has {len(pages)} pages")
    SHOTS.mkdir(parents=True, exist_ok=True)
    for old in SHOTS.glob("paper-p*.png"):
        old.unlink()
    wanted = parse_ranges(args.pages, len(pages))
    written = []
    for n in wanted:
        target = SHOTS / f"paper-p{n:02d}.png"
        target.write_bytes(pages[n - 1])
        written.append(target)
        say(f"wrote {target.relative_to(REPO)}")
    contact_sheet(written, [f"page {n}" for n in wanted], SHOTS / "paper-sheet.png", columns=6, width=260)
    return 0


def slide_ids(pptx: Path) -> list[str]:
    """The story id of every slide (0.1, 6.1, R.4, '1.2 · card'), read from the first line of its notes."""
    from pptx import Presentation
    ids = []
    for slide in Presentation(str(pptx)).slides:
        first = slide.notes_slide.notes_text_frame.text.split("\n")[0] if slide.has_notes_slide else ""
        m = re.match(r"(\S+(?: · card)?)", first)
        ids.append(m.group(1) if m else "?")
    return ids


def cmd_slides(args) -> int:
    number = paper_number()
    pptx = OUT / f"PRE_{number}.pptx"
    if not args.no_build:
        code = run([sys.executable, "tools/build_slides.py"])
        if code:
            return code
    if not pptx.exists():
        say(f"{pptx.relative_to(REPO)} is missing: build first (drop --no-build)")
        return 1
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    pdftoppm = shutil.which("pdftoppm")
    if not soffice or not pdftoppm:
        say("needs LibreOffice and pdftoppm: apt-get install -y libreoffice-impress poppler-utils")
        return 1
    ids = slide_ids(pptx)
    if args.ids:
        want = {i.strip() for i in args.ids.split(",") if i.strip()}
        numbers = [k for k, sid in enumerate(ids, 1) if sid in want or sid.split(" ")[0] in want]
        missing = want - {ids[k - 1].split(" ")[0] for k in numbers} - {ids[k - 1] for k in numbers}
        if missing:
            sys.exit(f"[driver] no slide with id {sorted(missing)}; ids run from {ids[0]} to {ids[-1]}")
    else:
        numbers = parse_ranges(args.index, len(ids))
    deck = SHOTS / "deck"
    deck.mkdir(parents=True, exist_ok=True)
    pdf = deck / f"PRE_{number}.pdf"
    if args.no_build and pdf.exists() and pdf.stat().st_mtime >= pptx.stat().st_mtime:
        say(f"reusing {pdf.relative_to(REPO)}")
    else:
        # A private LibreOffice profile: a second soffice (or a stale lock) otherwise makes it exit
        # 0 without writing anything.
        with tempfile.TemporaryDirectory(prefix="lo-profile-") as profile:
            code = run([soffice, f"-env:UserInstallation=file://{profile}", "--headless",
                        "--convert-to", "pdf", "--outdir", str(deck), str(pptx)],
                       timeout=600, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if code or not pdf.exists():
            say(f"LibreOffice did not write {pdf.relative_to(REPO)} (exit {code})")
            return code or 1
    for old in SHOTS.glob("slide-*.png"):
        old.unlink()
    written = []
    for n in numbers:
        safe = re.sub(r"[^A-Za-z0-9.]+", "_", ids[n - 1]).strip("_")
        prefix = SHOTS / f"slide-{n:02d}-{safe}"
        code = subprocess.run([pdftoppm, "-r", str(args.dpi), "-png", "-singlefile", "-f", str(n), "-l", str(n),
                               str(pdf), str(prefix)], cwd=REPO, stdout=subprocess.DEVNULL).returncode
        if code:
            say(f"pdftoppm failed on slide {n} (exit {code})")
            return code
        written.append(Path(f"{prefix}.png"))   # not with_suffix: an id such as 9.1 has a dot
        say(f"wrote {written[-1].relative_to(REPO)}")
    contact_sheet(written, [f"{n}: {ids[n - 1]}" for n in numbers], SHOTS / "slides-sheet.png",
                  columns=6, width=300)
    return 0


def cmd_all(args) -> int:
    for step in (cmd_check, cmd_paper, cmd_slides):
        code = step(args)
        if code:
            return code
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check", help="run tools/check_sources.py")
    sub.add_parser("stats", help="build the paper and print page count and style hints")
    p = sub.add_parser("paper", help="build the paper and render pages to out/shots/")
    p.add_argument("--pages", help="pages to render, such as 1,3-5 (default: all)")
    p.add_argument("--ppi", type=int, default=110, help="resolution of the page pictures (default 110)")
    p.add_argument("--no-build", action="store_true", help="render the last build without building again")
    s = sub.add_parser("slides", help="build the deck and render slides to out/shots/")
    g = s.add_mutually_exclusive_group()
    g.add_argument("--ids", help="story ids to render, such as 9.1,R.4 (6.1 renders all four of its slides)")
    g.add_argument("--index", help="slide numbers to render, such as 1-5 (default: all)")
    s.add_argument("--dpi", type=int, default=80, help="resolution of the slide pictures (default 80)")
    s.add_argument("--no-build", action="store_true", help="reuse the last deck (and its PDF, if newer)")
    a = sub.add_parser("all", help="check, then render every page and every slide")
    a.set_defaults(pages=None, ppi=60, no_build=False, ids=None, index=None, dpi=40)
    args = parser.parse_args()
    os.chdir(REPO)
    return {"check": cmd_check, "stats": cmd_stats, "paper": cmd_paper,
            "slides": cmd_slides, "all": cmd_all}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
