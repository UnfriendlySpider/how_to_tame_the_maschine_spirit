---
name: run-how-to-tame-the-maschine-spirit
description: Build, check, render and look at the paper (PDF) and the talk's deck (PPTX) in this repository. Use when asked to build or run the paper or the slides, run the checks or tests, take a screenshot of a page or a slide, see what a change to paper.md, references.md, deck.yaml or storyline.md looks like, or count the pages.
---

This repository has no server and no window: it is two build pipelines, `tools/build_paper.py`
(Markdown, then Typst, then `out/PAP_ML19.pdf`) and `tools/build_slides.py` (storyline and
`deck.yaml`, then python-pptx, then `out/PRE_ML19.pptx`), with `tools/check_sources.py` as its
test suite. Drive them with `.claude/skills/run-how-to-tame-the-maschine-spirit/driver.py`: it
builds, then renders pages and slides to PNG files in `out/shots/` that you open with the Read
tool to see the result. All paths are relative to the repository root.

## Prerequisites

`uv` on PATH (0.11 here); it brings Python and every project dependency from `uv.lock`. The
paper needs nothing else. Rendering slides needs LibreOffice and poppler (Ubuntu 24.04, as root):

```bash
apt-get install -y libreoffice-impress poppler-utils
```

## Setup and build

No setup step: the first `uv run` creates `.venv/` from `uv.lock` (about 45 MB, a few seconds).

```bash
uv run python tools/build_paper.py
uv run python tools/build_slides.py
```

They print `built out/PAP_ML19.pdf` (about 4 s) and `built out/PRE_ML19.pptx: 55 slides, 36
image(s) in place, 4 placeholder(s)` (about 7 s).

## Run (agent path): the driver

```bash
uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py check
uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py paper --pages 4
uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py slides --ids 9.1,R.4
uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py slides --no-build --ids 6.1
uv run python .claude/skills/run-how-to-tame-the-maschine-spirit/driver.py all
```

Then look: Read `out/shots/paper-p04.png`, `out/shots/slide-40-9.1.png` or the overview sheets.

| command | what it does | output in `out/shots/` |
|---|---|---|
| `check` | runs `tools/check_sources.py`; exit 0 = "all 53 checks passed" | none |
| `stats` | `build_paper.py --stats`: page count (limit 12), long sentences, empty openers | none |
| `paper [--pages 1,3-5] [--ppi 110] [--no-build]` | builds the PDF, renders pages with Typst itself | `paper-pNN.png`, `paper-sheet.png` (every page side by side: page breaks at a glance) |
| `slides [--ids 9.1,R.4 \| --index 1-5] [--dpi 80] [--no-build]` | builds the deck, LibreOffice makes `deck/PRE_ML19.pdf`, pdftoppm renders the slides | `slide-NN-<id>.png`, `slides-sheet.png` |
| `all` | `check`, then every page and every slide at low resolution | both sheets |

A slide's id is the first word of its speaker notes, as in `slides/storyline.md`: `0.1` to
`10.2`, then `R.1` to `R.12`. `--ids 6.1` renders the four slides of that build-up, and
`--ids 1.2` renders the slide and its card (`slide-06-1.2_card.png`). `slides` takes about
35 s, because LibreOffice converts the whole deck each time; `--no-build` reuses the deck and
its PDF while the deck is unchanged. The driver exits with the first failing step's code.

## Other builds

```bash
uv run python tools/build_slides.py --list
uv run --group narration python tools/build_slides.py --narrated
```

`--list` shows which images and logos are present. `--narrated` builds
`out/PRE_ML19-narrated.pptx` (40 slides, plays 17:39 by itself); the first run downloads
imageio-ffmpeg (65 MB).

## Run (human path)

Open `out/PAP_ML19.pdf` in a PDF viewer and `out/PRE_ML19.pptx` in PowerPoint. The deck's
clicks, fades and narration are made for PowerPoint; the PNG files show each slide as one still.

## Test

```bash
uv run python tools/check_sources.py
```

Expect `all 53 checks passed` and exit 0 (the count grows with every skill added). It feeds
the hooks crafted tool calls and checks the frontmatter of every skill (this one included),
the settings, the reference list and every file excerpt and sentence the slides quote. Run it
after any change to `.claude/`, `paper/` or `slides/`.

## Gotchas

- **You cannot `mkdir` into `out/` yourself.** `.claude/settings.json` denies `Edit(/out/**)`
  and `Edit(/dist/**)`, and Claude Code applies that to file commands such as `mkdir` too:
  `mkdir to '…/out/shots' was blocked by a deny rule`. The build scripts and the driver may
  write there; never hand-edit `out/`, rebuild instead.
- **This is the public copy: three logos are missing on purpose** (Evidenze, Evidenze earth,
  PHUSE Connect; they are not licensed for reuse). The deck builds with 4 placeholders, the
  title slide shows `CONFERENCE LOGO`, and `uv run python tools/build_slides.py --final`
  exits 1 with `not final: these are still placeholders`.
- **`tools/release.py` refuses most tags here:** a tag that exists already (`a published
  release stays frozen, cut a new tag`) and a tag without its own `## <tag>` section in
  `CHANGELOG.md`. It is the author's step; do not stage a release to test something.
- **LibreOffice is not PowerPoint.** The deck names Arial and Consolas, which Linux lacks
  (`fc-match` gives Liberation Sans and DejaVu Sans Mono), so line breaks can differ; the
  build's own message (`code lines wrap on slides R.3 (1), R.4 (1)`) is the one that counts.
  The animated GIF slides (0.3, 7b.1, 7c.1, 7c.2, 8.3) show their first frame, and labels that
  pop up on a click are all visible.
- **Paper pages need no LibreOffice:** the driver renders them from `out/main.typ` with the
  same Typst compiler that writes the PDF, so the PNG and the PDF match.
- **`--stats` hints are not failures.** Sentences over 25 words and empty openers are listed
  for the author's proofreading (CLAUDE.md, section 3); only the page count has a hard limit.
- **`/build-paper` is the author's own command** (it cannot be invoked by the model); it runs
  the same `build_paper.py --stats` as `driver.py stats`.

## Troubleshooting

- **`[driver] no slide with id ['99.9']; ids run from 0.1 to R.12`**: the id is not the first
  word of any slide's notes. Look up the id in `slides/storyline.md`, or use `--index`.
- **`[driver] no such page or slide: [13] (there are 12)`**: pages and slides count from 1.
- **`[driver] out/main.typ is missing`** or **`… PRE_ML19.pptx is missing`** with
  `--no-build`: nothing was built in this clone yet; run once without `--no-build`.
