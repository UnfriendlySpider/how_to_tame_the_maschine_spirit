#!/usr/bin/env python3
"""Build the talk's PowerPoint deck from the storyline, the deck recipe and the images.

Single entry point. Run with:

    uv run python tools/build_slides.py           # build out/PRE_<number>.pptx
    uv run python tools/build_slides.py --list    # which images are there, which are missing
    uv run python tools/build_slides.py --final   # build, but fail while anything is a placeholder
    uv run python tools/build_slides.py --output ~/Desktop/talk.pptx   # write it elsewhere
    uv run python tools/build_slides.py --images ~/reve-drafts          # try images from another folder
    uv run python tools/build_slides.py --timing  # slides and minutes per beat, from the planned seconds
    uv run --group narration python tools/build_slides.py --narrated   # the deck that tells itself
    uv run python tools/build_slides.py --full    # out/PRE_<number>-full.pptx, the drawings at full resolution

Sources
-------
slides/storyline.md is the script. Every slide is one bullet with its fields:

    - **4.3 Locks, not signs** (about 60 seconds)
      - Scene (no text in the image): "..."
      - Image: slides/beats/beat-04-hooks-3.png
      - Intention: What must never happen needs a lock, not a louder sign.
      - Points:
        - Name it: hook, a small script that runs just before the worker uses a tool, and can say no
      - Line: "If the worker can do it, one day it will."
      - Note: the source or the trap, not spoken

The build takes the id, the title, the image, the scene and the notes from it
and never writes to it. The beats (`### Beat 4 — ...`) become PowerPoint
sections. The speaker notes are bullets, never prose (the author's request,
2026-10-19): the slide's intention in one sentence, set in bold, a few points
that say what to share, not what happens, at most one line to say word for
word, and the Note below a rule, since it is not spoken.

slides/deck.yaml is the recipe: one entry per slide id with its layout and
the blocks of its panel. A `file` block quotes a repository file by line range
at build time, so the slide shows the file as it is today, and its `expect`
strings stop the build when an edit moves the lines away. A `text` block with
a `source` must still be found in that file, the paper's reference numbers
and its comments aside. It is the slides' counterpart of the paper's file
cards: one truth, no drift. A `text` or `caption` block with `talk_only: true`
stays out of the narrated deck, for a line that holds only in the room, such
as a pointer to the reference part the narrated deck does not have.

The deck has two parts. The story is told in pictures: on a `picture` slide
the image fills the slide, and everything else is spoken from the notes.
After the cast's goodbye and the closing slide, which stays up for the
questions, come the beats that answer a question, each one click away, and
the reference part, to read after the talk: on a `reference` slide the
paper's own sentences stand beside the files and commands the story is
about, all quoted at build time.

slides/beats/ holds the images under their storyline names. A missing image
becomes a placeholder that names the file and prints the scene, so the deck is
complete and can be rehearsed from the first build. Save the image, rebuild,
and it takes the placeholder's place, cropped as the layout asks: the whole
slide on a picture slide, a 4:3 crop beside a panel, the whole frame on a
full slide. `focus` and `zoom` in the
recipe move the crop; PowerPoint keeps the whole image, so the crop can also
be adjusted there. An animated GIF is placed like any other image, and
PowerPoint and LibreOffice play it in the show: the goodbye before the
closing slide is one.

paper/metadata.yaml gives the title, the author line and the paper number.
PHUSE files a talk's slides as PRE_<number> beside the paper's PAP_<number>,
so the deck is written to out/PRE_<number>.pptx.

python-pptx writes the file. The deck is 16:9, like the PHUSE EU Connect 2024
decks, uses fonts that ship with PowerPoint (set in deck.yaml), and every
image carries alternative text: its `alt` in deck.yaml, or else its scene. Its core properties name the
title and the author from paper/metadata.yaml and the time of the build,
never python-pptx's template values for them.

The look follows the author's PHUSE EU Connect 2025 deck (ML04, in PHUSE's
archive) in the brand of Evidenze Germany: white slides in Arial, the title
in the top left corner, a leaf with the slide number in the bottom left
corner and leaves as bullets; the title slide carries the paper number, the
title, place and conference, name and e-mail, the Evidenze logo in the top
right corner and the Evidenze Germany earth in the bottom right corner. The
pictures stay black and white: their slide number stands in black, without
a leaf.

Every generated image carries the EU icon for AI-generated content
(`ai_label` under `brand` in deck.yaml) in its top right corner, the place
the EU's Code of Practice on marking and labelling AI-generated content
gives as its example. The icon is grouped with its image, so a copied image
takes it along, except an animated GIF, which LibreOffice would not play in
a group; the build warns when the icon would hide part of a drawing.
The title slide, before the first drawing, says once beside the icon what it
marks (`ai_legend`); the narrated deck, whose voice is generated too, says so
in its own words where the title slide gives them (`ai_legend_narrated`).

The robots carry their names over their heads, as characters do in a game:
the name in the story and, in angle brackets below it, what it is in Claude
Code (`cast` in deck.yaml, placed by each slide's `names`). A slide's `labels`
name an object the same way, in a thin box, where it first matters. Where a
robot first joins the team, the next slide freezes the picture, dimmed, and
sets the robot's card on it, as a game shows a new team member: its portrait,
its name, a few lines on what it can and cannot do and a strip of values the
documentation states (`card` on the slide, the card itself under `cast`). A
picture slide's `build_up` shows earlier stages of its picture first, and
its `steps` show the states a fix passes through, each on a slide of its own
that waits for the click, before the slide shows the last. A beat after the
closing slide answers a question: the closing slide's notes name it, its
last slide's notes give the number back to the questions, and the narrated
deck, which ends on the closing slide, leaves it out.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
import uuid
import wave
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from itertools import zip_longest
from pathlib import Path
from urllib.parse import unquote as url_unquote

import segno
import yaml
from lxml import etree
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.lang import MSO_LANGUAGE_ID
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.media import Video
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls, qn
from pptx.util import Emu, Pt

REPO = Path(__file__).resolve().parent.parent
SLIDES = REPO / "slides"
STORYLINE = SLIDES / "storyline.md"
DECK = SLIDES / "deck.yaml"
METADATA = REPO / "paper" / "metadata.yaml"
OUT = REPO / "out"
CACHE = OUT / "slides"   # QR codes and converted images; disposable like the rest of out/
NARRATION = SLIDES / "narration"
CLIPS = NARRATION / "clips.yaml"   # which stretch of which take each slide of the narrated deck plays
TAKES = NARRATION / "takes"        # the narrator's takes, MP3, each with its alignment as JSON

# Geometry in inches. 13.333 x 7.5 is PowerPoint's 16:9; the ML04 deck's
# 10 x 5.625 positions are scaled by 4/3.
SLIDE_W, SLIDE_H = 13.333, 7.5
MARGIN = 0.61                     # left and right
TITLE_Y = 0.5                     # top of a slide's title
TOP, BOTTOM = 1.45, 6.8           # the content band below the title
GAP = 0.35                        # between the image and the panel
CARD_PAD_X, CARD_PAD_Y = 0.25, 0.22
CHUNK_GAP = 0.16                  # between a text chunk and a table in one panel

IMAGE_MIN_WIDTH = 2400            # px; the storyline asks for at least this much
DECK_PX = 1920                    # px across the slide, a projector's width: a still is embedded
                                  # at what its frame needs at this width, its source kept whole
                                  # (since 2026-10-29, the author's request: the deck had reached
                                  # 20 MB, a third of it in drawings sharper than a projector shows)
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".gif")
GIF_SETTLE_MS = 500               # after a GIF's last frame appears, before the deck moves on

# The EU icon for AI-generated content on every generated image: 5.5 % of the
# picture's height, so 0.4 inches on a whole slide, and never under 0.3 inches,
# so that it stays readable on a small picture (the title slide's, until 2026-10-28).
LABEL_SHARE, LABEL_MIN, LABEL_MAX = 0.055, 0.3, 0.4
LABEL_INSET = 0.625               # its gap to the picture's edges, as a share of its height
LABEL_RIM = 0.12                  # the white rim round it, as a share of its height
LABEL_INK = 0.01                  # warn when the drawing fills more than this share of its box

# The names that float above the cast on the story slides, as in a game (since 2026-10-15): the
# name in the story in bold, and below it, in angle brackets, what it is in Claude Code. Labels
# name an object the same way, in a thin box. Sizes in pt, lengths in inches.
NAME_SIZE, TITLE_SIZE, ITEM_SIZE = 22, 15, 16
NAME_ADVANCE = 0.6                # Arial Bold averages about 0.55 in these words; the white plate may be wider
NAME_GAP = 0.07                   # between the top of the head and the nameplate
BAR_W, BAR_H = 1.15, 0.12         # the bar under a name, which beat 6 uses for the context window

# The card that introduces a robot when it joins the team (since 2026-10-19), on a copy of the
# picture under a white veil. Lengths in inches, sizes in pt.
CARD_VEIL = 0.72                  # the share of white over the frozen picture
CARD_W, CARD_H = 5.5, 6.6
CARD_RIGHT = 0.7                  # the card's gap to the slide's right edge
CARD_GAP = 0.45                   # between two cards side by side (`beside`)
BESIDE_TAG = "ON THE TEAM"        # the tag of the card that stands beside a new one
CARD_PAD = 0.32
PORTRAIT_H = 2.05
CARD_NAME, CARD_TITLE, CARD_KEY, CARD_VALUE, CARD_TAG = 34, 18, 12.5, 15.5, 11
CARD_KEY_W = 1.35                 # the column of the keys, ARMS, BRAIN and so on
CARD_SECONDS = 20                 # what a card adds to the talk, unless the card says otherwise
POP_MS = 350                      # a label with `click` pops up this fast: it grows from its centre and fades in

# Evidenze's colours as evidenze.com defines them: navy #091A40, blue #1D4EBD
# and green #27B564 (the three bars of the logo's E).
DEFAULT_STYLE = {
    "fonts": {"heading": "Arial", "body": "Arial", "code": "Consolas"},
    "colours": {
        "heading": "091A40", "ink": "202536", "accent": "1D4EBD", "brand": "27B564",
        "grey": "5F6B7A", "rule": "D5DCE6", "panel": "F3F5F9", "mark": "E4EBF5",
        "drawing": "000000",
    },
    "tracker": True,
    "picture_corner": "right",
    "motion": True,
}
PICTURE_CORNERS = ("left", "right")
TRANSITIONS = ("fade",)

LAYOUTS = ("title", "picture", "panel", "full", "close", "reference")
SLIDE_KEYS = {
    "title": {"layout", "focus", "zoom", "ai_label", "ai_legend", "ai_legend_narrated"},
    "picture": {"layout", "focus", "zoom", "rings", "ai_label", "names", "labels", "card", "beside",
                "transition", "build_up", "steps", "advance", "alt"},
    "panel": {"layout", "split", "focus", "zoom", "rings", "panel", "ai_label"},
    "full": {"layout", "focus", "zoom", "rings", "inset", "ai_label"},
    "close": {"layout", "heading", "panel"},
    "reference": {"layout", "mechanism", "split", "explain", "panel"},
}
CORNERS = ("top-left", "top-right", "bottom-left", "bottom-right")

# The seven mechanisms in story order, for the tracker in the top right corner. Beat 7a
# (safety) is no mechanism of its own, so the memory leaf stays lit until 7b.
MECHANISM_OF_BEAT = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "7a": 6, "7b": 7, "8": 8}


# --- text styles and the size estimate --------------------------------------
#
# python-pptx cannot measure text, so the panels are fitted with an estimate:
# a character's advance as a share of the font size. Monospaced text uses 0.6
# (Consolas is 0.55; the preview renderer substitutes a 0.6 font), so a panel
# that fits in the preview fits in PowerPoint. Line spacing is set exactly, so
# a paragraph's height is its line count times its spacing.

MONO = 0.6
MONO_REAL = 0.55     # Consolas, for hanging indents that must line up in PowerPoint
PROP = 0.5           # body text (Arial averages about 0.45), with an allowance for ragged line ends
CAPS = 0.72          # spaced capitals in labels
SLACK = 0.96         # use only this share of a line, so a line that just fits stays whole
CODE_IN_PROSE = 0.92 # `code` inside prose is set a little smaller, as monospaced glyphs look larger
BULLET_INDENT = 16   # pt


@dataclass(frozen=True)
class TextStyle:
    font: str        # heading | body | code
    base: float      # size in pt at scale 1
    lo: float        # never smaller
    hi: float        # never larger
    colour: str
    line: float      # line spacing as a multiple of the size
    gap: float       # space before a paragraph inside a block, in ems
    bold: bool = False
    italic: bool = False
    caps: bool = False
    advance: float = PROP   # a table row grows with its text, so cells can be estimated tighter


STYLES = {
    "label": TextStyle("body", 11, 9, 12, "accent", 1.2, 0.0, bold=True, caps=True),
    "path": TextStyle("code", 11, 9, 12, "grey", 1.2, 0.0),
    "code": TextStyle("code", 16, 10.5, 26, "ink", 1.18, 0.0),
    "elide": TextStyle("code", 16, 10.5, 26, "grey", 1.18, 0.0),
    "text": TextStyle("body", 18, 12, 22, "ink", 1.2, 0.4),
    "bullet": TextStyle("body", 17, 12, 21, "ink", 1.2, 0.35),
    "caption": TextStyle("body", 13, 10, 15, "grey", 1.2, 0.3),
    "cell": TextStyle("body", 14, 10, 17, "ink", 1.15, 0.0, advance=0.47),
}
BLOCK_GAP = 0.85                                  # ems before each block after the first
SCALES = [round(1.5 - 0.05 * i, 2) for i in range(19)]   # 1.5 down to 0.6


def size_of(style: str, scale: float) -> float:
    st = STYLES[style]
    return round(min(st.hi, max(st.lo, st.base * scale)) * 2) / 2


@dataclass
class Para:
    """One paragraph of a panel: a style and its runs.

    A run's mark is "" (plain), "code", "bold", "italic", "hl" (highlighted
    text in a quoted file) or "dim" (the prompt before a command).
    """
    style: str
    runs: list[tuple[str, str]]
    hang: int = 0                 # hanging indent of a code line, in characters
    gap: float | None = None      # ems before; None takes the style's gap
    bullet: bool = False
    wrap_ok: bool = False         # a reflowed Markdown line may wrap; a code line should not


@dataclass
class Table:
    rows: list[list[str]]
    header: list[str] | None = None
    bold: set[int] = field(default_factory=set)   # body rows, from 1
    widths: list[float] | None = None
    row_headers: bool = False


@dataclass
class QrCode:
    label: str
    url: str | None


def run_width(text: str, mark: str, style: str, size: float) -> float:
    st = STYLES[style]
    if st.font == "code":
        factor = MONO
    elif mark == "code":
        factor = MONO * CODE_IN_PROSE
    elif st.caps:
        factor = CAPS
    else:
        factor = st.advance * (1.1 if st.bold or mark == "bold" else 1.0)
    return len(text) * factor * size


def para_lines(para: Para, size: float, width_pt: float) -> int:
    width_pt *= SLACK
    total = sum(run_width(t, m, para.style, size) for t, m in para.runs)
    if para.bullet:
        return max(1, math.ceil(total / max(width_pt - BULLET_INDENT, 1)))
    if total <= width_pt:
        return 1
    hang = para.hang * MONO * size
    rest = max(width_pt - hang, width_pt * 0.3)
    return 1 + math.ceil((total - width_pt) / rest)


def text_height(paras: list[Para], scale: float, width_in: float) -> tuple[float, int]:
    """Height in inches of a run of paragraphs, and how many extra lines wrapped code takes."""
    width_pt = width_in * 72
    height, wraps = 0.0, 0
    for i, para in enumerate(paras):
        st = STYLES[para.style]
        size = size_of(para.style, scale)
        n = para_lines(para, size, width_pt)
        if st.font == "code" and not para.wrap_ok:
            wraps += n - 1
        if i:
            height += (st.gap if para.gap is None else para.gap) * size
        height += n * size * st.line
    return height / 72, wraps


CELL_PAD = 0.07   # inches, inside each table cell


def column_widths(table: Table, width_in: float) -> list[float]:
    cols = len(table.rows[0]) if table.rows else len(table.header or [])
    if table.widths:
        weights = [float(w) for w in table.widths]
    else:
        lengths = [max(len(r[j]) for r in table.rows + ([table.header] if table.header else []))
                   for j in range(cols)]
        weights = [min(max(n, 8), 60) for n in lengths]
    total = sum(weights)
    return [width_in * w / total for w in weights]


def cell_lines(text: str, size: float, width_in: float, bold: bool = False) -> int:
    total = sum(run_width(t, "bold" if bold and m == "" else m, "cell", size) for t, m in inline(text))
    return max(1, math.ceil(total / max((width_in - 2 * CELL_PAD) * 72 * SLACK, 1)))


def table_rows(table: Table) -> list[list[str]]:
    return ([table.header] if table.header else []) + table.rows


def cell_is_bold(table: Table, i: int, j: int) -> bool:
    """Header, rows listed under `bold`, and the first column of a table with row headers."""
    offset = 1 if table.header else 0
    return (offset == 1 and i == 0) or (i - offset + 1) in table.bold or (table.row_headers and j == 0)


def row_heights(table: Table, scale: float, width_in: float) -> list[float]:
    size = size_of("cell", scale)
    line = size * STYLES["cell"].line / 72
    widths = column_widths(table, width_in)
    # A table row grows with its text, so a little slack keeps the next block clear of it.
    return [1.05 * max(cell_lines(c, size, w, cell_is_bold(table, i, j))
                       for j, (c, w) in enumerate(zip(row, widths))) * line + 2 * CELL_PAD
            for i, row in enumerate(table_rows(table))]


def broken_words(table: Table, scale: float, width_in: float) -> int:
    """Words wider than their column, which PowerPoint would break mid-word (long paths)."""
    size = size_of("cell", scale)
    count = 0
    for row in table_rows(table):
        for text, w in zip(row, column_widths(table, width_in)):
            room = (w - 2 * CELL_PAD) * 72 * SLACK
            count += sum(1 for part, mark in inline(text) for word in part.split()
                         if run_width(word, mark, "cell", size) > room)
    return count


def chunk_height(chunk: list[Para] | Table, scale: float, width_in: float) -> tuple[float, int]:
    if isinstance(chunk, Table):
        return sum(row_heights(chunk, scale, width_in)), broken_words(chunk, scale, width_in)
    return text_height(chunk, scale, width_in)


def group_chunks(items: list[Para | Table]) -> list[list[Para] | Table]:
    """Consecutive paragraphs share one text box; a table stands on its own."""
    chunks: list[list[Para] | Table] = []
    for item in items:
        if isinstance(item, Table):
            chunks.append(item)
        elif chunks and isinstance(chunks[-1], list):
            chunks[-1].append(item)
        else:
            chunks.append([item])
    return chunks


def fit(chunks: list, width_in: float, max_h: float,
        max_scale: float = SCALES[0]) -> tuple[float, float, int, bool]:
    """Pick the scale: as few wrapped code lines as possible, then as large as fits.

    Returns the scale, the content height, the extra lines wrapped code takes
    and whether the content fits at all.
    """
    def measure(scale: float) -> tuple[float, int]:
        parts = [chunk_height(c, scale, width_in) for c in chunks]
        height = sum(h for h, _ in parts) + CHUNK_GAP * (len(parts) - 1)
        return height, sum(w for _, w in parts)

    best: tuple[tuple[int, float], float, float] | None = None
    for scale in (s for s in SCALES if s <= max_scale):
        height, wraps = measure(scale)
        if height <= max_h and (best is None or (wraps, -scale) < best[0]):
            best = ((wraps, -scale), scale, height)
    if best is None:
        height, wraps = measure(SCALES[-1])
        return SCALES[-1], height, wraps, False
    (wraps, _), scale, height = best
    return scale, height, wraps, True


# --- the storyline ------------------------------------------------------------

SLIDE_LINE = re.compile(r"^- \*\*(?P<id>(?:\d+[a-z]?|R)\.\d+) (?P<title>.+?)\*\*(?: \((?P<timing>[^)]*)\))?\s*$")
FIELD_LINE = re.compile(r"^  - (?P<key>Scene|Image|Right panel|Intention|Points|Line|Note)\b[^:]*:\s*(?P<value>.*)$")
SECTION_LINE = re.compile(r"^### (?P<name>.+?)\s*$")
BEAT_NAME = re.compile(r"^Beat (?P<key>\d+[a-z]?) — (?P<title>.+)$")
IMAGE_PATH = re.compile(r"slides/beats/[\w.-]+\.(?:png|jpe?g|webp|gif)")


@dataclass
class StorySlide:
    id: str
    title: str
    seconds: int | None
    section: str             # "Beat 4 — Someone wanders into the server room"
    beat: str                # "Someone wanders into the server room"
    mechanism: int | None    # 1-7 while a mechanism is told, 0 before, 8 after; None outside the beats
    image: str | None = None
    scene: str = ""
    intention: str = ""      # what the audience takes away, in one sentence
    points: list[str] = field(default_factory=list)
    line: str = ""           # at most one line to say word for word
    note: str = ""           # background below the rule, not spoken


def bullet_items(text: str) -> list[str]:
    """The items of a field written as `- ` bullets; a line without a dash continues the item before."""
    items: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("- "):
            items.append(line[2:].strip())
        elif items:
            items[-1] += " " + line
        else:
            items.append(line)
    return items


def unquote(value: str) -> str:
    """`"words" [direction]` -> `words [direction]`; anything else unchanged."""
    m = re.match(r'^"(?P<q>.*)"(?P<rest>\s*\[.*\])?\s*$', value.strip(), re.S)
    return (m.group("q") + (m.group("rest") or "")) if m else value.strip()


def scene_text(value: str) -> str:
    """The scene prompt without its STYLE tag and reference list, or the plain scene."""
    value = value.strip()
    if value.startswith('"'):
        prompt = re.split(r'"\s+References?:', value, maxsplit=1)[0].strip().strip('"')
        return re.sub(r"\s*STYLE\.?$", "", prompt).strip()
    return value


def parse_storyline(path: Path = STORYLINE) -> list[StorySlide]:
    """Read the slides of the storyline's `## Slides` section, in order. Fails loudly."""
    if not path.exists():
        sys.exit(f"error: {path} not found")
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## Slides[ \t]*$(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"error: {path.relative_to(REPO)} has no '## Slides' section")
    slides: list[StorySlide] = []
    fields: dict[str, str] = {}
    section = beat = ""
    beat_key: str | None = None
    key: str | None = None

    def close() -> None:
        if not slides or not fields:
            return
        s = slides[-1]
        image = IMAGE_PATH.search(fields.get("Image", ""))
        s.image = image.group(0) if image else None
        s.scene = scene_text(fields.get("Scene", ""))
        s.intention = fields.get("Intention", "").strip()
        s.points = bullet_items(fields.get("Points", ""))
        s.line = unquote(fields.get("Line", ""))
        s.note = fields.get("Note", "").strip()
        fields.clear()

    for line in m.group(1).splitlines():
        heading = SECTION_LINE.match(line)
        if heading:
            close()
            section = heading.group("name")
            named = BEAT_NAME.match(section)
            beat_key = named.group("key") if named else None
            beat = named.group("title") if named else section.split(" — ")[0]
            key = None
            continue
        if not section:
            continue   # the list of decisions before the first slide
        start = SLIDE_LINE.match(line)
        if start:
            close()
            seconds = re.search(r"about (\d+) seconds", start.group("timing") or "")
            slides.append(StorySlide(
                id=start.group("id"),
                title=start.group("title").strip(),
                seconds=int(seconds.group(1)) if seconds else None,
                section=section,
                beat=beat,
                mechanism=MECHANISM_OF_BEAT.get(beat_key) if beat_key else None,
            ))
            fields["Image"] = ""
            key = None
            continue
        item = FIELD_LINE.match(line)
        if item and slides:
            key = item.group("key")
            fields[key] = item.group("value")
            continue
        if key and (line.startswith("    ") or not line.strip()):
            fields[key] += "\n" + line.strip()
            continue
        key = None
    close()
    if not slides:
        sys.exit(f"error: no slides found in {path.relative_to(REPO)}")
    ids = [s.id for s in slides]
    doubles = sorted({i for i in ids if ids.count(i) > 1})
    if doubles:
        sys.exit(f"error: slide ids appear twice in the storyline: {doubles}")
    return slides


def display_title(title: str) -> str:
    """A storyline title with typographic quotes, as it goes on the slide."""
    return re.sub(r'"([^"]+)"', "“\\1”", title)


def plain(text: str) -> str:
    """Markdown emphasis and code spans removed, for the speaker notes."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])", r"\1", text)
    return text.replace("`", "")


NOTES_RULE = "— Background, not spoken —"


def capital(text: str) -> str:
    return text[:1].upper() + text[1:]


def waiting_rings(spec: dict) -> bool:
    """Whether a slide's rings wait for a click (`click: true` on a ring)."""
    return any(isinstance(r, dict) and r.get("click") for r in spec.get("rings") or [])


def click_labels(spec: dict) -> list[str]:
    """What a slide shows on its clicks, in order, each on one line: the labels that wait, then
    the rings that wait, all on one click."""
    clicks = [" ".join(str(e["text"]).split("\n")) for e in spec.get("labels") or [] if e.get("click")]
    return clicks + (["the rings"] if waiting_rings(spec) else [])


def notes_text(s: StorySlide, clicks: list[str] | None = None) -> str:
    """The speaker notes, in bullets: the intention, the points, the one line, then the background.

    The speaker tells the story in their own words, so the notes hold what each slide must
    land and the words it must name, never a text to read out. The Note, sources and traps,
    stands below a rule, because it is not spoken.
    """
    head = f"{s.id} {s.title}" + (f" (about {s.seconds} seconds)" if s.seconds else "")
    parts = [head]
    if clicks:
        parts += ["Click to pop up: " + ", then ".join(clicks)]
    if s.intention:
        parts += ["", "Intention: " + plain(s.intention)]
    if s.points:
        parts += [""] + [f"• {plain(p)}" for p in s.points]
    if s.line:
        parts += ["", f"Line: “{plain(s.line)}”"]
    if s.note:
        items = bullet_items(s.note)
        parts += ["", NOTES_RULE, ""]
        parts += ([f"• {capital(plain(i))}" for i in items] if s.note.lstrip().startswith("- ")
                  else [capital(plain(s.note))])
    return "\n".join(parts)


def set_notes(slide, text: str) -> None:
    """Write the speaker notes, with the intention in bold: it is what the slide must land."""
    tf = slide.notes_slide.notes_text_frame
    tf.text = text
    for p in tf.paragraphs:
        if p.text.startswith("Intention: "):
            for run in p.runs:
                run.font.bold = True


def card_notes(s: StorySlide, who: dict, beside: dict | None = None) -> str:
    """The notes of a card slide: whom it introduces, and the card's lines to talk through; with a
    card beside it, each row with what the other robot's card says under the same key."""
    card = who["card"]
    seconds = int(card.get("seconds", CARD_SECONDS))
    joins = "joins the team" if not card.get("tag") else f"comes in ({str(card['tag']).lower()})"
    head = f"{s.id} · card: {who['name']} {joins}" + (f", beside the {beside['name']}" if beside else "")
    parts = [f"{head} (about {seconds} seconds)", ""]
    parts.append("Intention: " + plain(str(card.get("intention")
                                            or f"Meet the {who['name'].lower()}: what it can do, and what it cannot.")))
    theirs = {str(k).upper(): v for k, v in beside["card"]["rows"]} if beside else {}
    parts += [""] + [f"• {key}: {value}" + (f" (the {beside['name'].lower()}: {theirs[str(key).upper()]})"
                                           if str(key).upper() in theirs else "")
                     for key, value in card["rows"]]
    if card.get("stats"):
        their_stats = {str(k).upper(): v for k, v in (beside["card"].get("stats") or [])} if beside else {}
        parts += ["", "Stats, as the sources state them:"] + [
            f"• {key}: {value}" + (f" (the {beside['name'].lower()}: {their_stats[str(key).upper()]})"
                                   if str(key).upper() in their_stats else "")
            for key, value in card["stats"]]
        if card.get("stats_note"):
            parts += ["", str(card["stats_note"])]
    return "\n".join(parts)


def print_timing(slides: list[StorySlide], deck: dict) -> None:
    """The storyline's Timing table: the seconds each slide plans, "(about N seconds)", and each card.

    The notes are bullets, so the time comes from the plan, not from a word count. Only slides
    with a plan count; the beats that answer a question and the reference part are not timed. A
    card slide counts with its picture, at the seconds its card names.
    """
    timed = [s for s in slides if s.seconds is not None]
    beats: dict[str, list[StorySlide]] = {}
    for s in timed:
        beats.setdefault(s.section, []).append(s)

    def label(section: str) -> str:
        named = BEAT_NAME.match(section)
        if named:
            return f"{named.group('key')} {named.group('title')}"
        return {"Opening": "Title", "Close": "Close"}.get(section.split(" — ")[0], section)

    def clock(seconds: float) -> str:
        whole = round(seconds)
        return f"{whole // 60}:{whole % 60:02d}"

    def card_of(s: StorySlide) -> dict | None:
        who = (deck["slides"].get(s.id) or {}).get("card")
        return deck["cast"][who]["card"] if who else None

    print("| Beat | Slides | Minutes |")
    print("|---|---|---|")
    total_slides = total_seconds = 0
    for section, group in beats.items():
        cards = [c for c in (card_of(s) for s in group) if c]
        count = len(group) + len(cards)
        seconds = sum(s.seconds for s in group) + sum(int(c.get("seconds", CARD_SECONDS)) for c in cards)
        total_slides += count
        total_seconds += seconds
        print(f"| {label(section)} | {count} | {clock(seconds)} |")
    print(f"| **Total** | **{total_slides}** | **{clock(total_seconds)}** |")


# --- the recipe ----------------------------------------------------------------

def load_deck(story: list[StorySlide], path: Path = DECK) -> dict:
    """Read deck.yaml and check it against the storyline. Fails loudly."""
    if not path.exists():
        sys.exit(f"error: {path} not found")
    deck = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    entries = deck.get("slides") or {}
    bad_ids = [k for k in entries if not isinstance(k, str)]
    if bad_ids:
        sys.exit(f"error: quote the slide ids in {path.name}, YAML read these as numbers: {bad_ids}")
    story_ids = [s.id for s in story]
    missing = [i for i in story_ids if i not in entries]
    extra = [i for i in entries if i not in story_ids]
    if missing or extra:
        sys.exit(f"error: {path.name} and the storyline disagree. "
                 f"Missing in {path.name}: {missing or 'none'}; not in the storyline: {extra or 'none'}")
    if list(entries) != story_ids:
        sys.exit(f"error: the slides in {path.name} are not in storyline order: {story_ids}")
    cast = deck.get("cast") or {}
    if not isinstance(cast, dict):
        sys.exit(f"error: {path.name}: cast maps each id to its name and title")
    for who, entry in cast.items():
        if (not isinstance(entry, dict) or not str(entry.get("name") or "").strip()
                or set(entry) - {"name", "title", "card"}):
            sys.exit(f"error: {path.name}: cast {who} needs a name and may have a title and a card, nothing else")
        if "card" in entry:
            check_card(entry["card"], f"{path.name}: cast {who}: card")
    deck["cast"] = cast
    carded: dict[str, str] = {}
    for sid, spec in entries.items():
        spec = spec or {}
        entries[sid] = spec
        layout = spec.get("layout")
        if layout not in LAYOUTS:
            sys.exit(f"error: slide {sid}: layout must be one of {LAYOUTS}, got {layout!r}")
        unknown = set(spec) - SLIDE_KEYS[layout]
        if unknown:
            sys.exit(f"error: slide {sid}: unknown option(s) for a {layout} slide: {sorted(unknown)}")
        if spec.get("advance") not in (None, "after_gif"):
            sys.exit(f"error: slide {sid}: advance must be after_gif")
        inset = spec.get("inset")
        if inset and inset.get("corner", "bottom-right") not in CORNERS:
            sys.exit(f"error: slide {sid}: inset corner must be one of {CORNERS}")
        if spec.get("ai_label", "top-right") not in CORNERS:
            sys.exit(f"error: slide {sid}: ai_label is the corner of the AI label, one of {CORNERS}")
        if "mechanism" in spec and spec["mechanism"] not in range(1, 8):
            sys.exit(f"error: slide {sid}: mechanism must be a number from 1 to 7, got {spec['mechanism']!r}")
        for entry in spec.get("names") or []:
            where = f"slide {sid}: names"
            if not isinstance(entry, dict) or not {"who", "at"} <= set(entry) <= {"who", "at", "bar", "burst", "text"}:
                sys.exit(f"error: {where}: each entry has `who` and `at`, and may have `bar`, `burst` and `text`")
            if not isinstance(entry.get("text", True), bool) or (entry.get("text") is False and "bar" not in entry):
                sys.exit(f"error: {where}: `text: false` leaves only the bar, so the entry needs a `bar`")
            if entry["who"] not in cast:
                sys.exit(f"error: {where}: {entry['who']!r} is not in the cast ({', '.join(cast) or 'empty'})")
            check_point(entry["at"], where)
            if "bar" in entry and not (isinstance(entry["bar"], (int, float)) and 0 <= entry["bar"] <= 1):
                sys.exit(f"error: {where}: `bar` is a share from 0 to 1, got {entry['bar']!r}")
            if "burst" in entry and (entry["burst"] is not True or entry.get("bar") != 1):
                sys.exit(f"error: {where}: `burst: true` bursts a full bar, so the entry needs `bar: 1`")
        if "build_up" in spec:
            check_build_up(spec, f"slide {sid}: build_up")
        if "steps" in spec:
            if "build_up" in spec:
                sys.exit(f"error: slide {sid}: a slide has a build-up or steps, not both")
            check_steps(spec, f"slide {sid}: steps")
        if spec.get("transition", "fade") not in TRANSITIONS:
            sys.exit(f"error: slide {sid}: transition must be one of {TRANSITIONS}, got {spec['transition']!r}")
        for entry in spec.get("labels") or []:
            where = f"slide {sid}: labels"
            if (not isinstance(entry, dict) or not {"text", "at"} <= set(entry) <= {"text", "at", "click"}
                    or not str(entry["text"]).strip()):
                sys.exit(f"error: {where}: each entry has a `text` and `at`, and may have `click`")
            if not isinstance(entry.get("click", False), bool):
                sys.exit(f"error: {where}: `click` is true or false, got {entry['click']!r}")
            check_point(entry["at"], where)
        for ring in spec.get("rings") or []:
            at = ring.get("at") if isinstance(ring, dict) else ring
            if (isinstance(ring, dict) and (set(ring) - {"at", "click"} or not isinstance(ring.get("click", False), bool))
                    or not isinstance(at, list) or len(at) != 4
                    or not all(isinstance(v, (int, float)) and 0 <= v <= 1 for v in at)):
                sys.exit(f"error: slide {sid}: rings: each ring is [x, y, w, h] as shares of the picture, "
                         "or {at: [x, y, w, h], click: true} for one that waits for a click")
        if "build_up" in spec and (any(e.get("click") for e in spec.get("labels") or []) or waiting_rings(spec)):
            sys.exit(f"error: slide {sid}: the stages of a build-up repeat its labels and rings, so they cannot "
                     "wait for a click")
        if (spec.get("names") or spec.get("labels")) and float(spec.get("zoom", 1)) != 1:
            sys.exit(f"error: slide {sid}: names and labels sit on the whole picture, so the slide cannot zoom")
        if "card" in spec:
            who = spec["card"]
            if who not in cast or "card" not in cast[who]:
                sys.exit(f"error: slide {sid}: card {who!r} is not a cast member with a card")
            if who in carded:
                sys.exit(f"error: slide {sid}: the {who}'s card already follows slide {carded[who]}; "
                         "a robot joins the team once")
            if "beside" in spec and spec["beside"] not in carded:
                sys.exit(f"error: slide {sid}: beside {spec['beside']!r} must name a robot that joined the "
                         f"team before ({', '.join(carded) or 'none yet'})")
            carded[who] = sid
        elif "beside" in spec:
            sys.exit(f"error: slide {sid}: `beside` sets a card next to the slide's `card`, which it lacks")
    style = deck.get("style") or {}
    deck["style"] = {
        "fonts": {**DEFAULT_STYLE["fonts"], **(style.get("fonts") or {})},
        "colours": {**DEFAULT_STYLE["colours"], **{k: str(v) for k, v in (style.get("colours") or {}).items()}},
        "tracker": bool(style.get("tracker", DEFAULT_STYLE["tracker"])),
        "picture_corner": style.get("picture_corner", DEFAULT_STYLE["picture_corner"]),
        "motion": bool(style.get("motion", DEFAULT_STYLE["motion"])),
    }
    if deck["style"]["picture_corner"] not in (*PICTURE_CORNERS, False):
        sys.exit(f"error: style picture_corner must be one of {PICTURE_CORNERS} or false, "
                 f"got {deck['style']['picture_corner']!r}")
    for name, value in deck["style"]["colours"].items():
        if not re.fullmatch(r"[0-9A-Fa-f]{6}", value):
            sys.exit(f"error: style colour {name} must be six hex digits without '#', got {value!r}")
    deck["brand"] = deck.get("brand") or {}
    # No placeholder for the AI label: a deck whose images are not labelled is not built.
    label = deck["brand"].get("ai_label")
    if label and not (REPO / str(label)).is_file():
        sys.exit(f"error: brand ai_label: {label} does not exist; restore it from slides/brand/README.md "
                 "or delete the line to build without the label")
    deck["slides"] = entries
    return deck


CARD_KEYS = {"portrait", "rows", "stats", "stats_note", "tag", "seconds", "intention"}
CARD_STAT_KEY, CARD_STAT_VALUE = 10, 15   # the stats strip: a small key above a bold value


def check_card(card: object, where: str) -> None:
    """A robot's card: a portrait file and one to six rows of [key, value], up to three stats, real
    values checked against the documentation, an optional tag above the card, the seconds it adds
    to the talk and the intention its notes give."""
    if not isinstance(card, dict) or not {"portrait", "rows"} <= set(card) <= CARD_KEYS:
        sys.exit(f"error: {where} has a `portrait` and `rows`, and may have {sorted(CARD_KEYS - {'portrait', 'rows'})}")
    if not (REPO / str(card["portrait"])).is_file():
        sys.exit(f"error: {where}: the portrait {card['portrait']} does not exist")
    rows = card["rows"]
    if (not isinstance(rows, list) or not 1 <= len(rows) <= 6
            or not all(isinstance(r, list) and len(r) == 2 and all(str(v).strip() for v in r) for r in rows)):
        sys.exit(f"error: {where}: rows are one to six pairs, [KEY, what it says]")
    stats = card.get("stats")
    if stats is not None and (not isinstance(stats, list) or not 1 <= len(stats) <= 3 or not all(
            isinstance(r, list) and len(r) == 2 and all(str(v).strip() for v in r) for r in stats)):
        sys.exit(f"error: {where}: stats are one to three pairs, [KEY, value]")
    if "seconds" in card and not (isinstance(card["seconds"], int) and card["seconds"] > 0):
        sys.exit(f"error: {where}: seconds is a whole number above 0, got {card['seconds']!r}")


def check_build_up(spec: dict, where: str) -> None:
    """Earlier stages of a picture, each on a slide of its own that waits for the click: `stages`,
    each an `image`, the `bars` it shows, by cast id, and the `alt` text that describes it."""
    build = spec["build_up"]
    if not isinstance(build, dict) or set(build) != {"stages"}:
        sys.exit(f"error: {where} has `stages` and nothing else: each stage waits for the click "
                 "(since 2026-10-27), so it has no `seconds`")
    stages = build["stages"]
    if not isinstance(stages, list) or not 1 <= len(stages) <= 6:
        sys.exit(f"error: {where}: stages is a list of one to six stages")
    barred = {e["who"] for e in spec.get("names") or [] if isinstance(e, dict) and "bar" in e}
    for k, stage in enumerate(stages, 1):
        if (not isinstance(stage, dict) or not {"image"} <= set(stage) <= {"image", "bars", "alt"}
                or not str(stage["image"]).strip()):
            sys.exit(f"error: {where}: stage {k} has an `image` and may have `bars` and `alt`")
        check_bars(stage.get("bars") or {}, barred, f"{where}: stage {k}")


def check_steps(spec: dict, where: str) -> None:
    """The states a fix passes through before the slide itself shows the last, each on a slide of
    its own: an `image`, the `bars` it shows by cast id, the `labels` it carries and the `alt` text
    that describes it. A step is its own click, so its labels stand from the start."""
    steps = spec["steps"]
    if not isinstance(steps, list) or not 1 <= len(steps) <= 6:
        sys.exit(f"error: {where} is a list of one to six steps")
    barred = {e["who"] for e in spec.get("names") or [] if isinstance(e, dict) and "bar" in e}
    for k, step in enumerate(steps, 1):
        if (not isinstance(step, dict) or not {"image"} <= set(step) <= {"image", "bars", "labels", "alt"}
                or not str(step["image"]).strip()):
            sys.exit(f"error: {where}: step {k} has an `image` and may have `bars`, `labels` and `alt`")
        check_bars(step.get("bars") or {}, barred, f"{where}: step {k}")
        for entry in step.get("labels") or []:
            if not isinstance(entry, dict) or set(entry) != {"text", "at"} or not str(entry["text"]).strip():
                sys.exit(f"error: {where}: step {k}: each label has a `text` and `at`, and no `click`, "
                         "since the step is its own click")
            check_point(entry["at"], f"{where}: step {k}")


def check_bars(bars: object, barred: set, where: str) -> None:
    """The bars a stage or a step shows: cast ids, each with a bar on the slide, and shares from 0 to 1."""
    if not isinstance(bars, dict):
        sys.exit(f"error: {where}: `bars` maps cast ids to shares")
    for who, share in bars.items():
        if who not in barred:
            sys.exit(f"error: {where} sets a bar for {who!r}, whose name on the slide has none")
        if not (isinstance(share, (int, float)) and 0 <= share <= 1):
            sys.exit(f"error: {where}: a bar is a share from 0 to 1, got {share!r}")


def check_point(value: object, where: str) -> None:
    """A point on a picture: [x, y], each a share of its width or height."""
    if (not isinstance(value, list) or len(value) != 2
            or not all(isinstance(v, (int, float)) and 0 <= v <= 1 for v in value)):
        sys.exit(f"error: {where}: `at` is [x, y], each a share of the picture from 0 to 1, got {value!r}")


# --- panel blocks ----------------------------------------------------------------

BLOCK_KEYS = {
    "file": {"file", "lines", "highlight", "expect", "reflow", "label"},
    "shell": {"shell", "output", "label"},
    "code": {"code", "highlight"},
    "text": {"text", "source", "talk_only"},
    "caption": {"caption", "source", "talk_only"},
    "label": {"label"},
    "bullets": {"bullets"},
    "table": {"table"},
    "table_from": {"table_from"},
    "qr": {"qr"},
}
INLINE = re.compile(r"(`[^`]+`|\*\*[^*]+\*\*|\*[^*\s][^*]*\*)")
LIST_MARK = re.compile(r"^(\s*)([-*+] |\d+\. )?")
LONG_LINE = 90   # characters; a quoted line this long wraps in any panel, so the fit ignores it


def inline(text: str) -> list[tuple[str, str]]:
    """`code`, **bold** and *italic* inside prose, as runs."""
    runs: list[tuple[str, str]] = []
    for part in INLINE.split(text):
        if not part:
            continue
        if len(part) > 1 and part[0] == part[-1] == "`":
            runs.append((part[1:-1], "code"))
        elif len(part) > 4 and part.startswith("**") and part.endswith("**"):
            runs.append((part[2:-2], "bold"))
        elif len(part) > 2 and part[0] == part[-1] == "*":
            runs.append((part[1:-1], "italic"))
        else:
            runs.append((part, ""))
    return runs


def marked(line: str, needles: list[str]) -> list[tuple[str, str]]:
    """Split a code line into plain and highlighted runs."""
    spans = sorted((m.start(), m.end()) for n in needles for m in re.finditer(re.escape(n), line))
    runs: list[tuple[str, str]] = []
    pos = 0
    for start, end in spans:
        if start < pos:
            continue
        if start > pos:
            runs.append((line[pos:start], ""))
        runs.append((line[start:end], "hl"))
        pos = end
    if pos < len(line) or not runs:
        runs.append((line[pos:], ""))
    return runs


def parse_ranges(value: object, where: str) -> list[tuple[int, int]]:
    items = value if isinstance(value, list) else [value]
    ranges = []
    for item in items:
        m = re.fullmatch(r"\s*(\d+)\s*(?:[-–]\s*(\d+))?\s*", str(item))
        if not m:
            sys.exit(f"error: {where}: lines must look like \"46-53\" or [\"9-10\", \"17-26\"], got {item!r}")
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        ranges.append((a, b))
    return ranges


def describe_ranges(ranges: list[tuple[int, int]]) -> str:
    parts = [f"{a}–{b}" if b != a else f"{a}" for a, b in ranges]
    return ("lines " if len(ranges) > 1 or ranges[0][0] != ranges[0][1] else "line ") + ", ".join(parts)


def reflow(lines: list[str]) -> list[str]:
    """Join the hard-wrapped lines of Markdown list items and paragraphs."""
    out: list[str] = []
    for line in lines:
        joinable = (out and out[-1].strip() and line.strip()
                    and not LIST_MARK.match(line).group(2)
                    and not line.lstrip().startswith(("#", "---", "|")))
        if joinable:
            out[-1] = out[-1].rstrip() + " " + line.strip()
        else:
            out.append(line)
    return out


CITATION = re.compile(r"\s*\[\d+(?:,\s*\d+)*\]")   # the paper's reference numbers, "[4]" or "[6, 16]"
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)       # notes in a source, never quoted on a slide


def normalised(text: str) -> str:
    text = CITATION.sub("", text)
    return " ".join(re.sub(r"[*`\"“”‘’]", "", text).lower().split())


def repo_file(rel: str, where: str) -> Path:
    path = (REPO / rel).resolve()
    if not path.is_file() or REPO not in path.parents:
        sys.exit(f"error: {where}: {rel} does not exist in the repository")
    return path


def file_block(block: dict, where: str, state: dict) -> list[Para]:
    rel = str(block["file"])
    lines = repo_file(rel, where).read_text(encoding="utf-8").splitlines()
    if "lines" not in block:
        sys.exit(f"error: {where}: the file block for {rel} needs `lines`")
    ranges = parse_ranges(block["lines"], where)
    for a, b in ranges:
        if not 1 <= a <= b <= len(lines):
            sys.exit(f"error: {where}: {rel} has {len(lines)} lines; {a}-{b} is outside it")
    pieces = [lines[a - 1:b] for a, b in ranges]
    quoted = "\n".join("\n".join(p) for p in pieces)
    for expected in block.get("expect") or []:
        if expected not in quoted:
            sys.exit(f"error: {where}: {describe_ranges(ranges)} of {rel} no longer contain {expected!r}. "
                     "The file has changed: update the range in slides/deck.yaml.")
    highlights = [str(h) for h in block.get("highlight") or []]
    for h in highlights:
        if h not in quoted:
            sys.exit(f"error: {where}: highlight {h!r} is not in {describe_ranges(ranges)} of {rel}")
    if block.get("reflow"):
        pieces = [reflow(p) for p in pieces]
    indent = min((len(l) - len(l.lstrip()) for p in pieces for l in p if l.strip()), default=0)
    pieces = [[l[indent:] for l in p] for p in pieces]

    head = describe_ranges(ranges)
    runs = [(head, "")] if state.get("file") == rel else [(rel, ""), (f"  ·  {head}", "")]
    state["file"] = rel
    paras = [Para("label", [(str(block["label"]), "")])] if block.get("label") else []
    paras.append(Para("path", runs))
    first = len(paras)
    for k, piece in enumerate(pieces):
        if k:
            paras.append(Para("elide", [("⋮", "")]))
        for line in piece:
            lead, mark = LIST_MARK.match(line).groups()
            # Reflowed prose wraps by design, and so does a line too long for any panel.
            paras.append(Para("code", marked(line, highlights),
                              hang=len(lead) + (len(mark) if mark else 2),
                              wrap_ok=bool(block.get("reflow")) or len(line) > LONG_LINE))
    paras[first].gap = 0.35
    return paras


def check_source(text: str, block: dict, where: str) -> None:
    """A quoted sentence must still stand in its source. Comments do not count, as in the paper's
    build: a sentence that survives only in a note on the edit history no longer stands."""
    if "source" not in block:
        return
    rel = str(block["source"])
    content = HTML_COMMENT.sub("", repo_file(rel, where).read_text(encoding="utf-8"))
    if normalised(text) not in normalised(content):
        sys.exit(f"error: {where}: {rel} does not contain the quoted words: {text!r}")


def markdown_table(rel: str, header: list[str], where: str) -> list[list[str]]:
    """The body rows of the Markdown table in a file whose header row is `header`."""
    lines = repo_file(rel, where).read_text(encoding="utf-8").splitlines()

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    for i, line in enumerate(lines):
        if line.startswith("|") and cells(line) == header:
            body = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                body.append(cells(row))
            return body
    sys.exit(f"error: {where}: no table in {rel} has the header {header}")


def table_block(spec: dict, where: str, literal: bool) -> Table:
    if literal:
        rows = [[str(c) for c in r] for r in spec.get("rows") or []]
        header = [str(c) for c in spec["header"]] if spec.get("header") else None
    else:
        for k in ("file", "header", "columns", "rows"):
            if k not in spec:
                sys.exit(f"error: {where}: table_from needs `{k}`")
        header_in = [str(c) for c in spec["header"]]
        body = markdown_table(str(spec["file"]), header_in, where)
        for c in spec["columns"]:
            if c not in header_in:
                sys.exit(f"error: {where}: table_from column {c!r} is not in the header {header_in}")
        idx = [header_in.index(c) for c in spec["columns"]]
        by_first = {r[0]: r for r in body}
        for r in spec["rows"]:
            if r not in by_first:
                sys.exit(f"error: {where}: the table in {spec['file']} has no row {r!r}")
        # The slides carry no reference list, so the paper's numbers, "[4]", stay out of the cells.
        rows = [[CITATION.sub("", by_first[r][j]) for j in idx] for r in spec["rows"]]
        header = [header_in[j] for j in idx]
    if not rows:
        sys.exit(f"error: {where}: a table needs rows")
    if len({len(r) for r in rows + ([header] if header else [])}) != 1:
        sys.exit(f"error: {where}: every table row needs the same number of cells")
    widths = spec.get("widths")
    if widths and len(widths) != len(rows[0]):
        sys.exit(f"error: {where}: `widths` needs one number per column")
    return Table(rows=rows, header=header, bold={int(b) for b in spec.get("bold") or []},
                 widths=widths, row_headers=bool(spec.get("row_headers")))


def resolve_blocks(blocks: list, where: str, allow_qr: bool = False,
                   narrated: bool = False) -> list[Para | Table | QrCode]:
    """Turn the recipe's blocks into paragraphs, tables and QR codes. A text or caption block with
    `talk_only: true` is checked like any other, but the narrated deck leaves it out."""
    items: list[Para | Table | QrCode] = []
    state: dict = {}
    for n, block in enumerate(blocks or [], start=1):
        here = f"{where}, block {n}"
        if not isinstance(block, dict):
            sys.exit(f"error: {here}: a block is a mapping such as {{text: ...}}, got {block!r}")
        kinds = [k for k in BLOCK_KEYS if k in block]
        # `label` is a block of its own, or a key of file and shell blocks.
        if len(kinds) > 1 and "label" in kinds:
            kinds.remove("label")
        if len(kinds) != 1:
            sys.exit(f"error: {here}: say what the block is with one of {sorted(BLOCK_KEYS)}")
        kind = kinds[0]
        unknown = set(block) - BLOCK_KEYS[kind]
        if unknown:
            sys.exit(f"error: {here}: unknown key(s) for a {kind} block: {sorted(unknown)}")
        new: list[Para | Table | QrCode]
        if kind == "file":
            new = file_block(block, here, state)
        elif kind == "shell":
            new = ([Para("label", [(str(block["label"]), "")])] if block.get("label") else [])
            new.append(Para("code", [("$ ", "dim"), (str(block["shell"]), "bold")], hang=4))
            new += [Para("code", [(l, "")], hang=2)
                    for l in str(block.get("output") or "").rstrip("\n").splitlines()]
        elif kind == "code":
            needles = [str(h) for h in block.get("highlight") or []]
            new = [Para("code", marked(l, needles), hang=2) for l in str(block["code"]).splitlines()]
        elif kind in ("text", "caption"):
            if not isinstance(block.get("talk_only", False), bool):
                sys.exit(f"error: {here}: `talk_only` is true or false, got {block['talk_only']!r}")
            check_source(str(block[kind]), block, here)
            new = [Para(kind, inline(str(block[kind])))]
            if narrated and block.get("talk_only"):
                continue   # a line for the room only, such as a pointer to the reference part
        elif kind == "label":
            new = [Para("label", [(str(block["label"]), "")])]
        elif kind == "bullets":
            new = [Para("bullet", inline(str(b)), bullet=True) for b in block["bullets"] or []]
        elif kind in ("table", "table_from"):
            new = [table_block(block[kind] or {}, here, literal=kind == "table")]
        else:  # qr
            if not allow_qr:
                sys.exit(f"error: {here}: QR codes belong on the close layout")
            new = [QrCode(label=str(q.get("label", "")), url=q.get("url")) for q in block["qr"] or []]
        if not new:
            sys.exit(f"error: {here}: the {kind} block is empty")
        if items and isinstance(new[0], Para):
            new[0].gap = BLOCK_GAP
        items.extend(new)
    return items


def resolve_all(story: list[StorySlide], deck: dict, narrated: bool = False) -> dict[str, dict]:
    """Every slide's panel and inset items, checked against the files they quote; for the narrated
    deck without the blocks marked `talk_only`."""
    resolved: dict[str, dict] = {}
    for s in story:
        spec = deck["slides"][s.id]
        where = f"slide {s.id}"
        resolved[s.id] = {
            "panel": resolve_blocks(spec.get("panel"), where, allow_qr=spec["layout"] == "close",
                                    narrated=narrated),
            "inset": resolve_blocks((spec.get("inset") or {}).get("blocks"), f"{where} inset", narrated=narrated),
            "explain": resolve_blocks(spec.get("explain"), f"{where} explain", narrated=narrated),
        }
    return resolved


# --- images ----------------------------------------------------------------------

IMAGE_DIR: Path | None = None   # --images: look for the images here instead of slides/beats/
FULL = False                    # --full: embed every still whole, not scaled down to DECK_PX


def find_image(rel: str | None) -> Path | None:
    """The image file for a storyline path; a .png, .jpg, .jpeg, .webp or .gif of the same name also counts."""
    if not rel:
        return None
    base = IMAGE_DIR / Path(rel).name if IMAGE_DIR else REPO / rel
    for candidate in [base] + [base.with_suffix(e) for e in IMAGE_EXTS if e != base.suffix]:
        if candidate.is_file():
            return candidate
    return None


def cache_tag(path: Path) -> str:
    """A short tag for one version of one source file: its full path, its size and its time, so a
    draft taken with --images never stands in for the drawing of the same name, or the reverse."""
    st = path.stat()
    return hashlib.sha1(f"{path.resolve()}:{st.st_size}:{st.st_mtime_ns}".encode()).hexdigest()[:10]


def embeddable(path: Path, px: int | None = None) -> Path:
    """PowerPoint takes PNG, JPEG and GIF, and plays an animated GIF in the show; a WebP is converted
    into out/slides/ once. With `px`, a still wider than that is scaled down to it there, once,
    JPEG at the quality the drawings carry; a GIF stays as it is. The cached file's name carries
    the source's tag, so a changed or another source is converted afresh."""
    suffix = path.suffix.lower()
    if suffix == ".gif":
        return path
    with Image.open(path) as im:
        width = im.width
    if px and width > px:
        ext = ".png" if suffix in (".png", ".webp") else ".jpg"
        target = CACHE / f"{path.stem}-{cache_tag(path)}-{px}w{ext}"
        if not target.exists():
            CACHE.mkdir(parents=True, exist_ok=True)
            with Image.open(path) as im:
                small = im.resize((px, round(im.height * px / im.width)), Image.LANCZOS)
                if ext == ".jpg":
                    small.convert("RGB").save(target, quality=90, subsampling=0)
                else:
                    small.save(target)
        return target
    if suffix != ".webp":
        return path
    target = CACHE / f"{path.stem}-{cache_tag(path)}.png"
    if not target.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with Image.open(path) as im:
            im.save(target)
    return target


def gif_play_ms(path: Path) -> int:
    """How long a GIF plays before its last frame, in milliseconds."""
    with Image.open(path) as im:
        durations = []
        for k in range(getattr(im, "n_frames", 1)):
            im.seek(k)
            durations.append(im.info.get("duration", 0))
    return sum(durations[:-1])


def crop_window(img_w: int, img_h: int, frame_w: float, frame_h: float,
                focus: tuple[float, float], zoom: float) -> tuple[float, float, float, float]:
    """The visible part of the image as fractions (left, top, right, bottom) to crop away."""
    frame, image = frame_w / frame_h, img_w / img_h
    win_w, win_h = (frame / image, 1.0) if image > frame else (1.0, image / frame)
    win_w, win_h = win_w / zoom, win_h / zoom
    left = min(max(focus[0] - win_w / 2, 0.0), 1.0 - win_w)
    top = min(max(focus[1] - win_h / 2, 0.0), 1.0 - win_h)
    return left, top, 1.0 - left - win_w, 1.0 - top - win_h


def qr_png(url: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    target = CACHE / f"qr-{uuid.uuid5(uuid.NAMESPACE_URL, url).hex[:12]}.png"
    if not target.exists():
        segno.make(url, error="m").save(str(target), kind="png", scale=20, border=0, dark="#091A40")
    return target


# --- drawing helpers ---------------------------------------------------------------

def E(inches: float) -> Emu:
    return Emu(int(round(inches * 914400)))


class Ctx:
    """What every drawing function needs: style, metadata and the build's findings."""

    def __init__(self, deck: dict, meta: dict) -> None:
        self.fonts = deck["style"]["fonts"]
        self.colours = deck["style"]["colours"]
        self.tracker = deck["style"]["tracker"]
        self.picture_corner = deck["style"]["picture_corner"]
        self.motion = deck["style"]["motion"]
        self.cast = deck.get("cast") or {}
        self.brand = deck["brand"]
        self.label = REPO / str(self.brand["ai_label"]) if self.brand.get("ai_label") else None
        self._label_crop: tuple[tuple[float, float, float, float], float] | None = None
        self.contact = str(deck.get("contact") or "")
        self.meta = meta
        self.placeholders: list[str] = []
        self.warnings: list[str] = []
        self.wraps: list[str] = []
        self.images: list[str] = []
        self.narrated = False      # the narrated deck: labels wait for a spoken word, not a click
        self.pops: list = []       # the steps of the slide just laid out that wait for a word

    def rgb(self, key: str) -> RGBColor:
        return RGBColor.from_string(self.colours.get(key, key))

    def label_crop(self) -> tuple[tuple[float, float, float, float], float]:
        """The crop that keeps only the label's own shape, and that shape's width over its height.

        The EU's files have a transparent margin round the icon; PowerPoint keeps the whole file
        and crops it on the slide, so the file stays as the EU published it.
        """
        if self._label_crop is None:
            with Image.open(self.label) as im:
                width, height = im.size
                box = im.getchannel("A").getbbox() if "A" in im.getbands() else None
            left, top, right, bottom = box or (0, 0, width, height)
            self._label_crop = ((left / width, top / height, 1 - right / width, 1 - bottom / height),
                                (right - left) / (bottom - top))
        return self._label_crop


def style_run(run, ctx: Ctx, *, size: float, font: str = "body", colour: str = "ink",
              bold: bool = False, italic: bool = False, spacing: int | None = None) -> None:
    f = run.font
    f.size = Pt(size)
    f.name = ctx.fonts[font]
    f.bold = bold
    f.italic = italic
    f.color.rgb = ctx.rgb(colour)
    f.language_id = MSO_LANGUAGE_ID.ENGLISH_UK
    if spacing:
        run._r.get_or_add_rPr().set("spc", str(spacing))


def frame(tf, *, margins: tuple[float, float, float, float] = (0, 0, 0, 0),
          anchor=MSO_ANCHOR.TOP, wrap: bool = True) -> None:
    tf.word_wrap = wrap
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = anchor
    tf.margin_left, tf.margin_top, tf.margin_right, tf.margin_bottom = (E(m) for m in margins)


def add_box(slide, x: float, y: float, w: float, h: float, ctx: Ctx, *, fill: str | None = None,
            line: str | None = None, line_w: float = 1.0, dash: bool = False,
            shape=MSO_SHAPE.RECTANGLE, name: str | None = None, radius: float = 0.0):
    if radius:
        shape = MSO_SHAPE.ROUNDED_RECTANGLE
    box = slide.shapes.add_shape(shape, E(x), E(y), E(w), E(h))
    if radius:
        box.adjustments[0] = radius / min(w, h)   # the corner radius, as PowerPoint measures it
    # Drop the theme style python-pptx gives every shape: its effect reference
    # draws a shadow in some renderers, and fill and line are set below anyway.
    style = box._element.find(qn("p:style"))
    if style is not None:
        box._element.remove(style)
    box.shadow.inherit = False
    if fill:
        box.fill.solid()
        box.fill.fore_color.rgb = ctx.rgb(fill)
    else:
        box.fill.background()
    if line:
        box.line.color.rgb = ctx.rgb(line)
        box.line.width = Pt(line_w)
        if dash:
            box.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    else:
        box.line.fill.background()
    if name:
        box.name = name
    return box


def add_lines(slide, x: float, y: float, w: float, h: float, ctx: Ctx,
              lines: list[dict], *, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT, shape=None,
              margins: tuple[float, float, float, float] = (0, 0, 0, 0), wrap: bool = True):
    """A text box (or the given shape's text frame) with one paragraph per dict.

    Each dict holds `text` and the keyword arguments of style_run, plus `gap`
    (points before the paragraph), `line` (line spacing as a multiple) and
    `markup` (parse `code` and emphasis).
    """
    if shape is None:
        shape = slide.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = shape.text_frame
    frame(tf, anchor=anchor, margins=margins, wrap=wrap)
    for i, spec in enumerate(lines):
        spec = dict(spec)
        text, gap, markup = spec.pop("text"), spec.pop("gap", 0), spec.pop("markup", False)
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spec.pop("line", 1.0)
        if gap:
            p.space_before = Pt(gap)
        for part, mark in (inline(text) if markup else [(text, "")]):
            run = p.add_run()
            run.text = part
            style_run(run, ctx, **{**spec, **({"font": "code"} if mark == "code" else {}),
                                   **({"bold": True} if mark == "bold" else {}),
                                   **({"italic": True} if mark == "italic" else {})})
    return shape


def set_title(slide, x: float, y: float, w: float, h: float, ctx: Ctx, lines: list[dict],
              *, anchor=MSO_ANCHOR.TOP):
    """Fill the layout's title placeholder, so the slide keeps a real title for the outline."""
    title = slide.shapes.title
    title.left, title.top, title.width, title.height = E(x), E(y), E(w), E(h)
    title.text_frame.clear()
    add_lines(slide, x, y, w, h, ctx, lines, anchor=anchor, shape=title)
    return title


def slide_child(slide, element) -> None:
    """Put a transition or a timing tree where the slide's schema wants it: after the colour map,
    the transition before the timing, both before any extension list."""
    order = [qn("p:cSld"), qn("p:clrMapOvr"), qn("p:transition"), qn("p:timing"), qn("p:extLst")]
    sld = slide._element
    for old in sld.findall(element.tag):
        sld.remove(old)
    rank = order.index(element.tag)
    for i, child in enumerate(sld):
        if child.tag in order and order.index(child.tag) > rank:
            sld.insert(i, element)
            return
    sld.append(element)


def set_transition(slide, speed: str | None, advance_ms: int | None = None) -> None:
    """The slide fades in from the one before (no fade when `speed` is None) and, with
    `advance_ms`, moves on to the next by itself after that time; a click still moves on too.
    PowerPoint and LibreOffice play both in the show."""
    element = etree.SubElement(etree.Element("x"), qn("p:transition"))
    if speed:
        element.set("spd", speed)
    if advance_ms:
        element.set("advTm", str(advance_ms))
    if speed:
        etree.SubElement(element, qn("p:fade"))
    slide_child(slide, element)


class TimingTree:
    """A slide's `p:timing` tree, built node by node: the time nodes are numbered from 1 in the
    order they are made, as PowerPoint numbers them."""

    P = "http://schemas.openxmlformats.org/presentationml/2006/main"

    def __init__(self) -> None:
        self.ids = iter(range(1, 10_000))
        self.timing = etree.Element(qn("p:timing"), nsmap={"p": self.P})

    def el(self, parent, tag: str, **attrs):
        node = etree.SubElement(parent, qn(f"p:{tag}"))
        for key, value in attrs.items():
            node.set(key, str(value))
        return node

    def ctn(self, parent, **attrs):
        return self.el(parent, "cTn", id=next(self.ids), **attrs)

    def target(self, bhvr, spid: int) -> None:
        self.el(self.el(bhvr, "tgtEl"), "spTgt", spid=spid)

    def main_sequence(self):
        """The root, its sequence and the sequence's main time node, which the effects go into."""
        root = self.ctn(self.el(self.el(self.timing, "tnLst"), "par"), dur="indefinite", restart="never",
                        nodeType="tmRoot")
        seq = self.el(self.el(root, "childTnLst"), "seq", concurrent="1", nextAc="seek")
        return root, seq, self.ctn(seq, dur="indefinite", nodeType="mainSeq")

    def close_sequence(self, seq) -> None:
        for event, tag in (("onPrev", "prevCondLst"), ("onNext", "nextCondLst")):
            self.el(self.el(self.el(seq, tag), "cond", evt=event, delay="0"), "tgtEl").append(
                etree.Element(qn("p:sldTgt")))

    def visibility(self, parts, spid: int, value: str, delay: int = 0) -> None:
        """Show or hide the shape at once, `delay` ms into its effect."""
        bhvr = self.el(self.el(parts, "set"), "cBhvr")
        self.el(self.el(self.ctn(bhvr, dur="1", fill="hold"), "stCondLst"), "cond", delay=delay)
        self.target(bhvr, spid)
        self.el(self.el(bhvr, "attrNameLst"), "attrName").text = "style.visibility"
        self.el(self.el(bhvr.getparent(), "to"), "strVal", val=value)

    def pop(self, parent, spid: int, node_type: str, delay: int = 0) -> None:
        """The pop-up entrance: the shape grows from its centre and fades in, PowerPoint's Zoom."""
        effect = self.ctn(self.el(parent, "par"), presetID="53", presetClass="entr", presetSubtype="16",
                          fill="hold", grpId="0", nodeType=node_type)
        self.el(self.el(effect, "stCondLst"), "cond", delay=delay)
        parts = self.el(effect, "childTnLst")
        self.visibility(parts, spid, "visible")
        for attr in ("ppt_w", "ppt_h"):
            anim = self.el(parts, "anim", calcmode="lin", valueType="num")
            grow = self.el(anim, "cBhvr")
            self.ctn(grow, dur=POP_MS, fill="hold")
            self.target(grow, spid)
            self.el(self.el(grow, "attrNameLst"), "attrName").text = attr
            tavs = self.el(anim, "tavLst")
            self.el(self.el(self.el(tavs, "tav", tm="0"), "val"), "fltVal", val="0")
            self.el(self.el(self.el(tavs, "tav", tm="100000"), "val"), "strVal", val=f"#{attr}")
        fade = self.el(self.el(parts, "animEffect", transition="in", filter="fade"), "cBhvr")
        self.ctn(fade, dur=POP_MS)
        self.target(fade, spid)

    def play(self, parent, step: Step, first: str, delay: int = 0) -> None:
        """One step: its shapes pop up, the first as `first` and the rest with it."""
        for k, shape in enumerate(step.shapes):
            self.pop(parent, shape.shape_id, first if k == 0 else "withEffect", delay)

    def builds(self, steps: list[Step]) -> None:
        """One build entry per shape that pops up. Each has a single effect, so all share group 0;
        PowerPoint gives a second effect on the same shape a group of its own, and one slide that
        let a bar's fills come and go in one group did not play in PowerPoint as built
        (2026-10-22), so a state that changes a picture or a bar gets a slide of its own."""
        builds = self.el(self.timing, "bldLst")
        for step in steps:
            for shape in step.shapes:
                self.el(builds, "bldP", spid=shape.shape_id, grpId="0", animBg="1")


@dataclass
class Step:
    """What one click of a story slide shows, or one word of the narration: a label, or the rings,
    popping up (`shapes`). `key` names the step for the narration's cues: the label's text on one
    line, or "rings"."""
    key: str
    shapes: list


def pop_on_click(slide, steps: list[Step]) -> None:
    """Each step comes on a click of its own, in order: its label or rings grow from their centre
    and fade in, PowerPoint's Zoom entrance, so a label pops up when the speaker names it.
    PowerPoint and LibreOffice play it in the show; a viewer that ignores animations shows every
    label and ring."""
    t = TimingTree()
    _, seq, main = t.main_sequence()
    clicks = t.el(main, "childTnLst")
    for step in steps:
        click = t.ctn(t.el(clicks, "par"), fill="hold")
        t.el(t.el(click, "stCondLst"), "cond", delay="indefinite")
        par = t.ctn(t.el(t.el(click, "childTnLst"), "par"), fill="hold")
        t.el(t.el(par, "stCondLst"), "cond", delay="0")
        t.play(t.el(par, "childTnLst"), step, "clickEffect")
    t.close_sequence(seq)
    t.builds(steps)
    slide_child(slide, t.timing)


# --- the narrated deck ---------------------------------------------------------------------
#
# A second deck that tells the story by itself (the author's request, 2026-10-21): each slide plays
# its stretch of the narrator's takes and moves on when it ends; a label pops up when the narrator
# says its word. slides/narration/clips.yaml says which stretch each slide plays.

@dataclass
class Clip:
    """A slide's narration: the file cut for it, how long the slide stays (None: until the show is
    ended), and when each of its labels pops up, in ms from the slide's start."""
    path: Path | None
    ms: int | None
    cues: dict[str, int] = field(default_factory=dict)


def narration_names(story: list[StorySlide], deck: dict) -> list[str]:
    """The slides of the narrated deck, by the names clips.yaml uses, in the order they are shown:
    the story from the title to the closing slide, its build-up stages, steps and cards included.
    The beats after it answer questions, and the narrated deck takes none."""
    names = []
    for s in story:
        spec = deck["slides"][s.id]
        if spec["layout"] == "reference":
            break
        names += [f"{s.id} stage {k}" for k in range(1, len((spec.get("build_up") or {}).get("stages") or []) + 1)]
        names += [f"{s.id} step {k}" for k in range(1, len(spec.get("steps") or []) + 1)]
        names.append(s.id)
        if spec.get("card"):
            names.append(f"{s.id} card")
        if spec["layout"] == "close":
            break
    return names


def take_text(take: str) -> tuple[str, list[int], dict]:
    """A take's words as spoken: its alignment's characters with the tags left out and the spaces
    collapsed, with each character's index in the alignment, and the alignment itself."""
    path = TAKES / f"{take}.json"
    if not path.is_file():
        sys.exit(f"error: {path.relative_to(REPO)} is missing: a take used in part needs its alignment")
    align = json.loads(path.read_text(encoding="utf-8"))
    text, chars, index, i = align["text"], [], [], 0
    while i < len(text):
        if text[i] == "[":
            i = text.index("]", i) + 1
            continue
        c = " " if text[i].isspace() else text[i]
        if not (c == " " and (not chars or chars[-1] == " ")):
            chars.append(c)
            index.append(i)
        i += 1
    return "".join(chars), index, align


def narration_plan(story: list[StorySlide], deck: dict) -> dict[str, dict]:
    """Read clips.yaml and hold it against the deck and the takes. Every slide of the narrated deck
    has a clip or a hold; each piece's words stand in its take; the pieces of a take follow each
    other and cover every word of it once; every cue is a label of its slide that waits, and its
    word is spoken in the slide's clip. Returns, per slide, its pieces as (take, first, last)
    indices into the take's alignment (None for a whole take), its cues as (take, index), its hold."""
    where = CLIPS.relative_to(REPO)
    if not CLIPS.is_file():
        sys.exit(f"error: {where} is missing")
    data = yaml.safe_load(CLIPS.read_text(encoding="utf-8")) or {}
    entries = data.get("slides") or {}
    names = narration_names(story, deck)
    unknown = [n for n in entries if n not in names]
    if unknown:
        sys.exit(f"error: {where}: no such slide in the narrated deck: {', '.join(unknown)}")
    missing = [n for n in names if n not in entries]
    if missing:
        sys.exit(f"error: {where}: these slides have neither a clip nor a hold: {', '.join(missing)}")
    plan, spans, texts = {}, {}, {}
    for name in names:
        entry = entries[name] or {}
        if ("clip" in entry) == ("hold" in entry):
            sys.exit(f"error: {where}: {name} has a `clip` or a `hold`, not both")
        hold = entry.get("hold")
        if "hold" in entry and not (hold == "end" or isinstance(hold, (int, float)) and hold > 0):
            sys.exit(f"error: {where}: {name}: `hold` is seconds above 0, or `end`")
        if hold == "end" and name != names[-1]:
            sys.exit(f"error: {where}: only the last slide, {names[-1]}, can hold to the end")
        pieces = []
        for piece in entry.get("clip") or []:
            take = piece.get("take")
            if not (TAKES / f"{take}.mp3").is_file():
                sys.exit(f"error: {where}: {name}: no take {TAKES.relative_to(REPO)}/{take}.mp3")
            if "from" not in piece and "to" not in piece:
                pieces.append((take, None, None))
                continue
            if take not in texts:
                texts[take] = take_text(take)
            spoken, index, _ = texts[take]
            first, last = spoken.find(str(piece.get("from"))), spoken.find(str(piece.get("to")))
            if first < 0 or last < 0:
                sys.exit(f"error: {where}: {name}: \"{piece.get('from') if first < 0 else piece.get('to')}\" "
                         f"is not in {take}; write it exactly as in script.md, tags left out")
            last += len(str(piece["to"])) - 1
            if last < first:
                sys.exit(f"error: {where}: {name}: its `to` comes before its `from` in {take}")
            spans.setdefault(take, []).append((first, last, name))
            pieces.append((take, first, last))
        cues = {}
        slide_spec = deck["slides"][name.split()[0]]
        labels = {" ".join(str(e["text"]).split("\n")): e for e in slide_spec.get("labels") or []}
        for label, word in (entry.get("cues") or {}).items():
            label = " ".join(str(label).split("\n"))
            waits = waiting_rings(slide_spec) if label == "rings" else labels.get(label, {}).get("click")
            if " " in name or not waits:
                sys.exit(f"error: {where}: {name}: {label!r} is not a label of this slide that waits, "
                         "nor `rings` for its rings that wait")
            for take, first, last in pieces:
                if first is not None:
                    at = texts[take][0].find(str(word), first)
                    if 0 <= at <= last:
                        cues[label] = (take, at)
                        break
            else:
                sys.exit(f"error: {where}: {name}: the cue {word!r} is not spoken in the slide's clip")
        plan[name] = {"pieces": pieces, "cues": cues, "hold": hold}
    for take, found in spans.items():
        spoken = texts[take][0]
        at = 0
        for first, last, name in sorted(found):
            if re.search(r"[A-Za-z0-9]", spoken[at:first]):
                sys.exit(f"error: {where}: no slide plays \"{spoken[at:first].strip()[:60]}\" of {take}"
                         if first > at else f"error: {where}: {name} plays words of {take} another slide plays")
            at = last + 1
        if re.search(r"[A-Za-z0-9]", spoken[at:]):
            sys.exit(f"error: {where}: no slide plays \"{spoken[at:].strip()[:60]}\" at the end of {take}")
    return plan


def ffmpeg() -> str:
    """The ffmpeg that cuts the clips: the one imageio-ffmpeg ships, else one on the PATH."""
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        found = shutil.which("ffmpeg")
        if found:
            return found
    sys.exit("error: the narrated deck needs ffmpeg; build it with "
             "`uv run --group narration python tools/build_slides.py --narrated`")


def cut_narration(plan: dict[str, dict]) -> dict[str, Clip]:
    """Cut each slide's clip from the takes. A piece starts and ends in the silence next to its
    first and last word, so no word is clipped and a short breath stays; pieces are joined with
    the paragraph pause, and every clip gets a little silence before and after. Writes mono MP3
    to out/slides/narration/ and returns the clips with their lengths and cue times."""
    data = yaml.safe_load(CLIPS.read_text(encoding="utf-8")) or {}
    lead, pause, tail = (float(data.get(k, d)) for k, d in (("lead", 0.4), ("pause", 0.7), ("tail", 0.8)))
    exe, work, rate = ffmpeg(), CACHE / "narration", 44100
    work.mkdir(parents=True, exist_ok=True)
    pcm, quiet, aligned = {}, {}, {}

    def decode(take: str) -> None:
        wav = work / f"{take}.wav"
        subprocess.run([exe, "-y", "-loglevel", "error", "-i", str(TAKES / f"{take}.mp3"), "-ac", "1",
                        "-ar", str(rate), "-c:a", "pcm_s16le", str(wav)], check=True)
        with wave.open(str(wav)) as w:
            pcm[take] = w.readframes(w.getnframes())
        log = subprocess.run([exe, "-hide_banner", "-nostats", "-i", str(wav), "-af",
                              "silencedetect=noise=-40dB:d=0.08", "-f", "null", "-"],
                             capture_output=True, text=True).stderr
        quiet[take] = list(zip((float(x) for x in re.findall(r"silence_start: ([0-9.]+)", log)),
                               (float(x) for x in re.findall(r"silence_end: ([0-9.]+)", log))))

    def silence(seconds: float) -> bytes:
        return bytes(2 * round(seconds * rate))

    def cut_before(take: str, t: float) -> float:
        near = [(a, b) for a, b in quiet[take] if t - 0.8 <= b <= t + 0.15]
        if not near:
            return max(0.0, t - 0.03)
        a, b = max(near, key=lambda q: q[1])
        return max(a, min(b, t) - 0.25)

    def cut_after(take: str, t: float) -> float:
        near = [(a, b) for a, b in quiet[take] if t - 0.15 <= a <= t + 0.8]
        if not near:
            return t + 0.05
        a, b = min(near, key=lambda q: q[0])
        return min(b, max(a, t) + 0.3)

    clips = {}
    for name, entry in plan.items():
        if not entry["pieces"]:
            clips[name] = Clip(None, None if entry["hold"] == "end" else round(1000 * float(entry["hold"])))
            continue
        out, cues = bytearray(silence(lead)), {}
        for k, (take, first, last) in enumerate(entry["pieces"]):
            if take not in pcm:
                decode(take)
            if k:
                out += silence(pause)
            if first is None:
                a, b = 0.0, len(pcm[take]) / 2 / rate
            else:
                if take not in aligned:
                    aligned[take] = take_text(take)
                spoken, index, align = aligned[take]
                # the last letter, not the full stop: a stop's time runs on into the pause after it
                end = max(i for i in range(first, last + 1) if spoken[i].isalnum())
                a = cut_before(take, align["start"][index[first]])
                b = cut_after(take, align["end"][index[end]])
                for label, (cue_take, at) in entry["cues"].items():
                    if cue_take == take and first <= at <= last:
                        cues[label] = round(1000 * (len(out) / 2 / rate + align["start"][index[at]] - a))
            out += pcm[take][2 * round(a * rate):2 * round(b * rate)]
        out += silence(tail)
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        wav, mp3 = work / f"clip-{slug}.wav", work / f"clip-{slug}.mp3"
        with wave.open(str(wav), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(rate)
            w.writeframes(bytes(out))
        subprocess.run([exe, "-y", "-loglevel", "error", "-i", str(wav), "-c:a", "libmp3lame", "-b:a", "64k",
                        "-metadata", "comment=AI-generated voice: ElevenLabs Eleven v4", str(mp3)], check=True)
        wav.unlink()
        clips[name] = Clip(mp3, round(1000 * len(out) / 2 / rate), cues)
    return clips


def speaker_png() -> Path:
    """The icon PowerPoint shows for an audio clip; it sits off the slide and is never seen."""
    path = CACHE / "speaker.png"
    if not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        im = Image.new("RGBA", (96, 96), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.polygon([(14, 36), (34, 36), (58, 14), (58, 82), (34, 60), (14, 60)], fill=(0, 0, 0, 255))
        for r in (14, 26):
            d.arc([58 - r, 48 - r, 58 + r, 48 + r], -45, 45, fill=(0, 0, 0, 255), width=5)
        im.save(path)
    return path


def add_audio(slide, path: Path, name: str) -> int:
    """Embed an MP3 in the slide as PowerPoint embeds a sound, its icon off the slide; returns the
    shape id the timing plays."""
    media_part = slide.part.package.get_or_add_media_part(Video.from_path_or_file_like(str(path), "audio/mpeg"))
    media_rid, audio_rid = slide.part.relate_to(media_part, RT.MEDIA), slide.part.relate_to(media_part, RT.AUDIO)
    _, icon_rid = slide.part.get_or_add_image_part(str(speaker_png()))
    spid = slide.shapes._next_shape_id
    side = E(0.4)
    slide.shapes._spTree.append(parse_xml(
        f'<p:pic {nsdecls("a", "p", "r")}><p:nvPicPr>'
        f'<p:cNvPr id="{spid}" name="{name}" descr="Narration, an AI-generated voice">'
        '<a:hlinkClick r:id="" action="ppaction://media"/></p:cNvPr>'
        '<p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr>'
        f'<p:nvPr><a:audioFile r:link="{audio_rid}"/><p:extLst>'
        '<p:ext uri="{DAA4B4D4-6D71-4841-9C94-3DE7FCFB9230}">'
        f'<p14:media xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" r:embed="{media_rid}"/>'
        '</p:ext></p:extLst></p:nvPr></p:nvPicPr>'
        f'<p:blipFill><a:blip r:embed="{icon_rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
        f'<p:spPr><a:xfrm><a:off x="{E(SLIDE_W + 0.3)}" y="{E(0.3)}"/><a:ext cx="{side}" cy="{side}"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'))
    return spid


def narrate(slide, clip: Clip, steps: list[Step], name: str) -> None:
    """The slide plays its clip as soon as it begins, the clip's icon hidden, and each waiting label
    or ring pops up at its cue, or as the slide begins when it has none. PowerPoint plays it in the
    show and when it exports the deck as a video; the slide's timing moves it on when the clip ends."""
    spid = add_audio(slide, clip.path, f"Narration {name}")
    t = TimingTree()
    root, seq, main = t.main_sequence()
    group = t.ctn(t.el(t.el(main, "childTnLst"), "par"), fill="hold")
    conds = t.el(group, "stCondLst")
    t.el(conds, "cond", delay="indefinite")
    t.el(t.el(conds, "cond", evt="onBegin", delay="0"), "tn", val=main.get("id"))
    step = t.ctn(t.el(t.el(group, "childTnLst"), "par"), fill="hold")
    t.el(t.el(step, "stCondLst"), "cond", delay="0")
    effects = t.el(step, "childTnLst")
    play = t.ctn(t.el(effects, "par"), presetID="1", presetClass="mediacall", presetSubtype="0",
                 fill="hold", nodeType="afterEffect")
    t.el(t.el(play, "stCondLst"), "cond", delay="0")
    call = t.el(t.el(play, "childTnLst"), "cmd", type="call", cmd="playFrom(0.0)")
    bhvr = t.el(call, "cBhvr")
    t.ctn(bhvr, dur=clip.ms, fill="hold")
    t.target(bhvr, spid)
    for step in steps:
        t.play(effects, step, "withEffect", clip.cues.get(step.key, 0))
    t.close_sequence(seq)
    node = t.el(t.el(root.find(qn("p:childTnLst")), "audio"), "cMediaNode", vol="100000")
    sound = t.ctn(node, fill="hold", display="0")
    t.el(t.el(sound, "stCondLst"), "cond", delay="indefinite")
    t.el(t.el(t.el(sound, "endCondLst"), "cond", evt="onStopAudio", delay="0"), "tgtEl").append(
        etree.Element(qn("p:sldTgt")))
    t.target(node, spid)
    if steps:
        t.builds(steps)
    slide_child(slide, t.timing)


def to_front(shape) -> None:
    element = shape._element
    tree = element.getparent()
    tree.remove(element)
    tree.append(element)


def set_alt(shape, text: str) -> None:
    shape._element.xpath("./*[1]/p:cNvPr")[0].set("descr", text)


def add_brand_picture(slide, key: str, y: float, h: float, ctx: Ctx, *, x: float | None = None,
                      alt: str) -> None:
    """A brand file from deck.yaml at height h; without x it is set flush with the right margin."""
    rel = ctx.brand.get(key)
    if not rel:
        return
    path = REPO / str(rel)
    if not path.is_file():
        ctx.placeholders.append(f"{key}: {rel}")
        add_lines(slide, x if x is not None else SLIDE_W - MARGIN - 3.0, y, 3.0, h, ctx,
                  [{"text": f"{key}: {rel}", "size": 9, "font": "code", "colour": "grey"}])
        return
    with Image.open(path) as im:
        w = h * im.width / im.height
    pic = slide.shapes.add_picture(str(embeddable(path)), E(SLIDE_W - MARGIN - w if x is None else x),
                                   E(y), E(w), E(h))
    pic.name = alt
    set_alt(pic, alt)


# The leaf of the ML04 template, in a 1000 x 1500 box: the tip at the top
# left, a round base. Two leaves carry the slide number in the bottom left
# corner, seven mark the mechanisms, and one is the bullet of a list.
LEAF = [
    ((250, 0),),
    ((700, 100), (1000, 550), (1000, 900)),
    ((1000, 1250), (750, 1500), (500, 1500)),
    ((200, 1500), (0, 1250), (0, 900)),
    ((0, 550), (50, 250), (250, 0)),
]


def leaf_geometry():
    """The leaf as DrawingML custom geometry, so PowerPoint draws it as a vector shape."""
    geom = etree.Element(qn("a:custGeom"))
    for tag in ("a:avLst", "a:gdLst", "a:ahLst", "a:cxnLst"):
        etree.SubElement(geom, qn(tag))
    etree.SubElement(geom, qn("a:rect"), l="0", t="0", r="r", b="b")
    path = etree.SubElement(etree.SubElement(geom, qn("a:pathLst")), qn("a:path"), w="1000", h="1500")
    (start,), *curves = LEAF
    etree.SubElement(etree.SubElement(path, qn("a:moveTo")), qn("a:pt"), x=str(start[0]), y=str(start[1]))
    for curve in curves:
        bezier = etree.SubElement(path, qn("a:cubicBezTo"))
        for px, py in curve:
            etree.SubElement(bezier, qn("a:pt"), x=str(px), y=str(py))
    etree.SubElement(path, qn("a:close"))
    return geom


def add_leaf(slide, x: float, y: float, w: float, h: float, ctx: Ctx, *, fill: str | None = None,
             line: str | None = None, flip: bool = False, name: str = "Leaf"):
    leaf = add_box(slide, x, y, w, h, ctx, fill=fill, line=line, line_w=0.75, name=name)
    sppr = leaf._element.spPr
    preset = sppr.find(qn("a:prstGeom"))
    preset.addprevious(leaf_geometry())
    sppr.remove(preset)
    if flip:
        sppr.find(qn("a:xfrm")).set("flipH", "1")
    return leaf


def leaf_png(ctx: Ctx) -> Path:
    """The leaf as a small PNG in the brand colour, for picture bullets."""
    colour = ctx.colours["brand"]
    target = CACHE / f"leaf-{colour}.png"
    if target.exists():
        return target
    (start,), *curves = LEAF
    points, p0 = [start], start
    for c1, c2, p3 in curves:
        for i in range(1, 25):
            t = i / 24
            points.append(tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * d
                                for a, b, c, d in zip(p0, c1, c2, p3)))
        p0 = p3
    big = Image.new("RGBA", (400, 600), (0, 0, 0, 0))
    ImageDraw.Draw(big).polygon([(px * 0.4, py * 0.4) for px, py in points], fill="#" + colour)
    CACHE.mkdir(parents=True, exist_ok=True)
    big.resize((64, 96), Image.LANCZOS).save(target)
    return target


def draw_tracker(slide, story: StorySlide, ctx: Ctx) -> None:
    """Seven leaves in the top right corner, one per mechanism: told, being told, to come."""
    if story.mechanism is None or not ctx.tracker:
        return
    w, h, g = 0.12, 0.18, 0.08
    x = SLIDE_W - MARGIN - (7 * w + 6 * g)
    for i in range(1, 8):
        if story.mechanism == 8 or i < story.mechanism:
            fill, line = "brand", None
        elif i == story.mechanism:
            fill, line = "accent", None
        else:
            fill, line = None, "rule"
        add_leaf(slide, x, TITLE_Y + 0.14, w, h, ctx, fill=fill, line=line, name=f"Mechanism {i} of 7")
        x += w + g


def add_slide_number(p, number: int, ctx: Ctx, *, size: float, colour: str, bold: bool) -> None:
    """A slide-number field, so PowerPoint renumbers the slide when slides move."""
    fld = etree.SubElement(p._p, qn("a:fld"), id="{B6F15528-21DE-4FAA-801E-634DDDAF4B2B}", type="slidenum")
    rpr = etree.SubElement(fld, qn("a:rPr"), lang="en-GB", sz=str(round(size * 100)), b="1" if bold else "0")
    fill = etree.SubElement(rpr, qn("a:solidFill"))
    etree.SubElement(fill, qn("a:srgbClr"), val=ctx.colours.get(colour, colour))
    etree.SubElement(rpr, qn("a:latin"), typeface=ctx.fonts["body"])
    etree.SubElement(fld, qn("a:t")).text = str(number)


def draw_corner(slide, ctx: Ctx, number: int | None) -> None:
    """The ML04 corner: two leaves running off the bottom left edge, the slide number on the larger."""
    add_leaf(slide, 0.17, 7.16, 0.28, 0.42, ctx, fill="brand", flip=True)
    add_leaf(slide, 0.47, 6.86, 0.52, 0.78, ctx, fill="brand")
    if number is None:
        return
    box = slide.shapes.add_textbox(E(0.47), E(7.06), E(0.52), E(0.3))
    box.name = "Slide number"
    frame(box.text_frame)
    p = box.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    add_slide_number(p, number, ctx, size=10.5, colour="FFFFFF", bold=True)


def draw_picture_number(slide, ctx: Ctx, number: int, side: str) -> None:
    """The slide number on a picture: black and without a leaf, so the slide stays black and white.

    A white plate behind it is invisible on the white below the floor line and keeps the number
    readable where a drawing runs into the corner. It lines up with the AI label's edge.
    """
    w, h, pad = 0.34, 0.2, 0.05     # just round two digits, so the plate cuts little of a drawing
    inset = LABEL_INSET * LABEL_MAX
    x = SLIDE_W - inset + pad - w if side == "right" else inset - pad
    box = add_box(slide, x, SLIDE_H - 0.2 - h, w, h, ctx, fill="FFFFFF", name="Slide number")
    frame(box.text_frame, margins=(pad, 0, pad, 0), anchor=MSO_ANCHOR.BOTTOM)
    p = box.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT if side == "right" else PP_ALIGN.LEFT
    add_slide_number(p, number, ctx, size=12, colour="drawing", bold=False)


def draw_header(slide, story: StorySlide, ctx: Ctx, width: float = 10.6) -> None:
    """The slide's title in the top left corner, as on every ML04 slide, and the tracker."""
    set_title(slide, MARGIN, TITLE_Y, width, 0.7, ctx, [
        {"text": display_title(story.title), "size": 28, "font": "heading", "colour": "heading",
         "bold": True}])
    draw_tracker(slide, story, ctx)


# --- pictures and placeholders --------------------------------------------------------

def label_box(x: float, y: float, w: float, h: float, ctx: Ctx,
              corner: str = "top-right") -> tuple[float, float, float, float]:
    """Where the AI label goes on a picture in this frame: in its top right corner, unless the
    slide's `ai_label` names another."""
    _, aspect = ctx.label_crop()
    lh = min(LABEL_MAX, max(LABEL_MIN, LABEL_SHARE * h))
    lw, inset = lh * aspect, LABEL_INSET * lh
    lx = x + inset if corner.endswith("left") else x + w - inset - lw
    ly = y + inset if corner.startswith("top") else y + h - inset - lh
    return lx, ly, lw, lh


def add_label(slide, box: tuple[float, float, float, float], ctx: Ctx, *, name: str, alt: str):
    """The EU icon in a box from label_box, cropped to its own shape."""
    bx, by, bw, bh = box
    label = slide.shapes.add_picture(str(ctx.label), E(bx), E(by), E(bw), E(bh))
    label.crop_left, label.crop_top, label.crop_right, label.crop_bottom = ctx.label_crop()[0]
    label.name = name
    set_alt(label, alt)
    return label


def drawing_under(im, crop: tuple[float, float, float, float], frame_box: tuple[float, float, float, float],
                  box: tuple[float, float, float, float]) -> float:
    """The share of a box on the slide that the drawing fills, the image cropped as on the slide."""
    left, top, right, bottom = crop
    x, y, w, h = frame_box
    bx, by, bw, bh = box
    sx, sy = (1 - left - right) * im.width / w, (1 - top - bottom) * im.height / h
    x0, y0 = left * im.width + (bx - x) * sx, top * im.height + (by - y) * sy
    hist = im.convert("L").crop((int(x0), int(y0), int(x0 + bw * sx), int(y0 + bh * sy))).histogram()
    return sum(hist[:200]) / max(sum(hist), 1)


def dimmed(path: Path) -> Path:
    """A copy of an image under a white veil, for the frozen picture behind a card; made in
    out/slides/ once for each version of the image, which its name carries."""
    target = CACHE / f"{path.stem}-{cache_tag(path)}-veiled.jpg"
    if not target.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with Image.open(path) as im:
            frame = im.convert("RGB")   # an animated GIF gives its first frame
            Image.blend(frame, Image.new("RGB", frame.size, "white"), CARD_VEIL).save(target, quality=90)
    return target


def place_picture(slide, story: StorySlide, x: float, y: float, w: float, h: float, ctx: Ctx, *,
                  focus=(0.5, 0.5), zoom: float = 1.0, corner: str | None = None, kind: str = "",
                  source: Path | None = None) -> None:
    """The slide's image cropped to the frame, or a placeholder that says what will go there.

    Every image is generated, so it carries the AI label in a corner, grouped with it. A thin
    white rim behind the label, invisible on white, ends any line of the drawing just short of
    it. A slide whose `ai_label` names the corner has been looked at, so it gets no warning.
    An animated GIF stays outside the label's group, under it: LibreOffice 24.2 plays a GIF in
    the show, but not one inside a group. `source` puts another file in the image's place, such
    as its veiled copy behind a card; the checks ran on the image itself.
    """
    path = source or find_image(story.image)
    if path:
        with Image.open(path) as im:
            img_w, img_h = im.size
            moving = path.suffix.lower() == ".gif" and getattr(im, "is_animated", False)
            crop = crop_window(img_w, img_h, w, h, focus, zoom)
            box = label_box(x, y, w, h, ctx, corner or "top-right") if ctx.label else None
            hidden = drawing_under(im, crop, (x, y, w, h), box) if box else 0.0
        if source is None:
            if img_w < IMAGE_MIN_WIDTH:
                ctx.warnings.append(f"{story.id}: {path.name} is {img_w} px wide; the storyline asks for {IMAGE_MIN_WIDTH}")
            if abs(img_w / img_h - 16 / 9) > 0.03:
                ctx.warnings.append(f"{story.id}: {path.name} is not 16:9 ({img_w} x {img_h})")
            if hidden > LABEL_INK and corner is None:
                ctx.warnings.append(f"{story.id}: the AI label hides part of {path.name} in the top-right corner "
                                    f"({hidden:.0%} of its box is drawing); look at the slide, then move the "
                                    "label or keep it there with `ai_label` in deck.yaml")
        # The visible part of the image needs DECK_PX * (frame width / slide width) pixels; a
        # zoomed crop shows less of the image, so it keeps more of them.
        need = None if FULL else math.ceil(DECK_PX * (w / SLIDE_W) / (1.0 - crop[0] - crop[2]))
        pic = slide.shapes.add_picture(str(embeddable(path, need)), E(x), E(y), E(w), E(h))
        pic.crop_left, pic.crop_top, pic.crop_right, pic.crop_bottom = crop
        pic.name = f"Image {story.id}"
        set_alt(pic, story.scene or story.title)
        if source is None:
            ctx.images.append(story.image)
        if box:
            bx, by, bw, bh = box
            rim = LABEL_RIM * bh
            # The EU's icons are round-ended (a circle or a pill), so a fully rounded box fits them.
            plate = add_box(slide, bx - rim, by - rim, bw + 2 * rim, bh + 2 * rim, ctx, fill="FFFFFF",
                            name="AI label rim", radius=bh / 2 + rim)
            label = add_label(slide, box, ctx, name="AI label", alt="AI generated")
            group = slide.shapes.add_group_shape(([] if moving else [pic]) + [plate, label])
            group.name = "AI label" if moving else f"Image {story.id} with AI label"
        return
    if not story.image:
        return
    ctx.placeholders.append(f"{story.id}: {story.image}")
    box = add_box(slide, x, y, w, h, ctx, fill="panel", line="brand", line_w=1.25, dash=True,
                  name=f"Placeholder {story.id}")
    set_alt(box, f"Placeholder for {story.image}")
    big = w > 10
    pad_x = 1.6 if big else 0.35
    size = 14 if big else 12
    room = (h - 1.4) * 72 / (size * 1.25)
    per_line = (w - 2 * pad_x) * 72 / (PROP * size)
    scene = story.scene
    limit = int(room * per_line * 0.9)
    if len(scene) > limit:
        scene = scene[:limit].rsplit(" ", 1)[0] + " …"
    note = f"image to come · {kind}" + (f", zoom {zoom}" if zoom != 1 else "")
    add_lines(slide, 0, 0, 0, 0, ctx, [
        {"text": note.upper(), "size": 11, "colour": "accent", "bold": True, "spacing": 120},
        {"text": story.image, "size": size, "font": "code", "gap": 6},
        {"text": scene, "size": size, "colour": "grey", "italic": True, "gap": 8, "line": 1.05},
    ], shape=box, anchor=MSO_ANCHOR.MIDDLE, margins=(pad_x, 0.3, pad_x, 0.3))


def draw_rings(slide, rings: list, x: float, y: float, w: float, h: float, ctx: Ctx) -> list:
    """Highlight rings over the picture; returns those that wait for a click, which pop up together."""
    waiting = []
    for n, ring in enumerate(rings or [], start=1):
        rx, ry, rw, rh = (float(v) for v in (ring["at"] if isinstance(ring, dict) else ring))
        shape = add_box(slide, x + rx * w, y + ry * h, rw * w, rh * h, ctx, line="brand", line_w=4.5,
                        shape=MSO_SHAPE.OVAL, name=f"Highlight ring {n}")
        if isinstance(ring, dict) and ring.get("click"):
            waiting.append(shape)
    return waiting


def bar_fill(slide, left: float, top: float, share: float, ctx: Ctx, name: str):
    """The black fill of a bar, `share` of its length; None for an empty bar."""
    if share <= 0:
        return None
    inset = 0.035
    inner = BAR_H - 2 * inset
    return add_box(slide, left + inset, top + inset, max((BAR_W - 2 * inset) * share, inner), inner, ctx,
                   fill="drawing", radius=inner / 2, name=name)


def burst_rays(slide, left: float, top: float, ctx: Ctx, name: str) -> list:
    """Short lines flying from the end of a full bar, as the gauge in the picture bursts."""
    end, mid = left + BAR_W, top + BAR_H / 2
    rays = []
    for k, deg in enumerate((-55, -25, 5, 35)):
        t = math.radians(deg)
        ray = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                         E(end + 0.06 * math.cos(t)), E(mid + 0.06 * math.sin(t)),
                                         E(end + 0.2 * math.cos(t)), E(mid + 0.2 * math.sin(t)))
        ray.line.color.rgb = ctx.rgb("drawing")
        ray.line.width = Pt(1.75)
        ray.name = f"{name} bar burst {k + 1}"
        rays.append(ray)
    return rays


def draw_names(slide, sid: str, spec: dict, ctx: Ctx) -> list:
    """The names that float above the cast, as in a game, and the labels over the objects.

    A name is centred over the top of a head: the name in the story in bold and, below it in angle
    brackets, what it is in Claude Code (`cast` in deck.yaml). Each line has a white plate behind
    it, invisible on white, so the drawing's lines stop just short of the letters, as the AI label's
    rim does. A `bar` under the name shows a share the way a game shows energy; beat 6 uses it for
    the context window, and a full bar with `burst` has short lines flying from its end, as the
    gauge in the picture bursts. A label names an object in a thin box, like a new item, and may break
    its text into lines. `at` is a share of the picture, which fills the slide. A label with
    `click` waits for a click, so it pops up when the speaker names it; the labels that do are
    returned as steps, in their order, for the slide's timing.
    """
    avoid = label_box(0, 0, SLIDE_W, SLIDE_H, ctx, label_corner(spec) or "top-right") if ctx.label else None
    for entry in spec.get("names") or []:
        who = ctx.cast[entry["who"]]
        x, y = entry["at"][0] * SLIDE_W, entry["at"][1] * SLIDE_H - NAME_GAP
        shapes, boxes = [], []
        if "bar" in entry:
            left = x - BAR_W / 2
            shapes.append(add_box(slide, left, y - BAR_H, BAR_W, BAR_H, ctx, fill="FFFFFF", line="drawing",
                                  line_w=1.75, radius=BAR_H / 2, name=f"{who['name']} bar"))
            fill = bar_fill(slide, left, y - BAR_H, entry["bar"], ctx, f"{who['name']} bar fill")
            if fill is not None:
                shapes.append(fill)
            boxes.append((left, y - BAR_H, BAR_W, BAR_H))
            if entry.get("burst"):
                shapes += burst_rays(slide, left, y - BAR_H, ctx, who["name"])
                boxes.append((left + BAR_W, y - BAR_H / 2 - 0.2, 0.2, 0.4))
            y -= BAR_H + 0.05
        lines = [(f"<{who['title']}>", "code", TITLE_SIZE, False)] if who.get("title") else []
        lines.append((who["name"], "heading", NAME_SIZE, True))
        if entry.get("text") is False:
            lines = []   # the bar alone: the name was given where the robot joined the team
        for text, font, size, bold in lines:
            w = len(text) * (MONO_REAL if font == "code" else NAME_ADVANCE) * size / 72 + 0.16
            h = size * 1.18 / 72
            shapes.append(add_box(slide, x - w / 2, y - h, w, h, ctx, fill="FFFFFF", radius=h / 2,
                                  name=f"{who['name']} plate"))
            box = add_lines(slide, x - w / 2, y - h, w, h, ctx,
                            [{"text": text, "size": size, "font": font, "colour": "drawing", "bold": bold}],
                            anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, wrap=False)
            box.name = f"{who['name']} {'title' if font == 'code' else 'name'}"
            shapes.append(box)
            boxes.append((x - w / 2, y - h, w, h))
            y -= h - 0.02   # the two lines sit close, as a game sets them
        group = slide.shapes.add_group_shape(shapes)
        group.name = f"Name: {who['name']}"
        set_alt(group, who["name"] + (f", {who['title']}" if who.get("title") else ""))
        check_room(boxes, avoid, f"{sid}: the name {who['name']}", ctx)
    steps = []
    for entry in spec.get("labels") or []:
        text = str(entry["text"])
        rows = text.split("\n")
        x, y = entry["at"][0] * SLIDE_W, entry["at"][1] * SLIDE_H
        w = max(len(r) for r in rows) * MONO_REAL * ITEM_SIZE / 72 + 0.26
        h = len(rows) * ITEM_SIZE * 1.15 / 72 + 0.1
        box = add_box(slide, x - w / 2, y - h, w, h, ctx, fill="FFFFFF", line="drawing", line_w=1.75,
                      radius=0.07, name=f"Label: {' '.join(rows)}")
        add_lines(slide, 0, 0, 0, 0, ctx, [{"text": r, "size": ITEM_SIZE, "font": "code", "colour": "drawing",
                                            "bold": True, "line": 1.0} for r in rows],
                  shape=box, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, wrap=False)
        set_alt(box, f"Label: {' '.join(rows)}")
        check_room([(x - w / 2, y - h, w, h)], avoid, f"{sid}: the label {' '.join(rows)}", ctx)
        if entry.get("click"):
            steps.append(Step(" ".join(rows), [box]))
    return steps


def check_room(boxes: list[tuple[float, float, float, float]], avoid, what: str, ctx: Ctx) -> None:
    """Warn when a name or label runs off the slide or covers the AI label."""
    for bx, by, bw, bh in boxes:
        if bx < 0.05 or by < 0.05 or bx + bw > SLIDE_W - 0.05 or by + bh > SLIDE_H - 0.05:
            ctx.warnings.append(f"{what} runs off the slide; move it in deck.yaml")
            return
        if avoid and bx < avoid[0] + avoid[2] and avoid[0] < bx + bw \
                and by < avoid[1] + avoid[3] and avoid[1] < by + bh:
            ctx.warnings.append(f"{what} covers the AI label; move it in deck.yaml")
            return


# --- panels ------------------------------------------------------------------------------

def draw_paragraphs(slide, paras: list[Para], x: float, y: float, w: float, h: float,
                    scale: float, ctx: Ctx) -> None:
    box = slide.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = box.text_frame
    frame(tf)
    for i, para in enumerate(paras):
        st = STYLES[para.style]
        size = size_of(para.style, scale)
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = Pt(size * st.line)
        if i:
            p.space_before = Pt((st.gap if para.gap is None else para.gap) * size)
        ppr = p._p.get_or_add_pPr()
        if para.bullet:
            # A picture bullet: the leaf, as on the ML04 slides.
            ppr.set("marL", str(int(BULLET_INDENT * 12700)))
            ppr.set("indent", str(-int(BULLET_INDENT * 12700)))
            etree.SubElement(ppr, qn("a:buSzPct"), val="80000")
            _, rid = slide.part.get_or_add_image_part(str(leaf_png(ctx)))
            blip = etree.SubElement(etree.SubElement(ppr, qn("a:buBlip")), qn("a:blip"))
            blip.set(qn("r:embed"), rid)
        elif para.hang:
            hang = int(para.hang * MONO_REAL * size * 12700)
            ppr.set("marL", str(hang))
            ppr.set("indent", str(-hang))
        for text, mark in para.runs:
            run = p.add_run()
            run.text = text.upper() if st.caps else text
            colour = st.colour
            if mark == "hl":
                colour = "accent"
            elif mark == "dim":
                colour = "grey"
            inline_code = mark == "code" and st.font != "code"
            style_run(run, ctx, size=round(size * CODE_IN_PROSE * 2) / 2 if inline_code else size,
                      font="code" if mark == "code" else st.font, colour=colour,
                      bold=st.bold or mark in ("bold", "hl"), italic=st.italic or mark == "italic",
                      spacing=120 if st.caps else None)


def cell_border(cell, side: str, colour: str | None, width_pt: float = 0.75) -> None:
    tcpr = cell._tc.get_or_add_tcPr()
    tag = qn(f"a:ln{side}")
    old = tcpr.find(tag)
    if old is not None:
        tcpr.remove(old)
    line = etree.Element(tag, w=str(int(width_pt * 12700)) if colour else "0")
    if colour:
        fill = etree.SubElement(line, qn("a:solidFill"))
        etree.SubElement(fill, qn("a:srgbClr"), val=colour)
    else:
        etree.SubElement(line, qn("a:noFill"))
    order = ["L", "R", "T", "B"]
    position = sum(1 for s in order[:order.index(side)] if tcpr.find(qn(f"a:ln{s}")) is not None)
    tcpr.insert(position, line)


def draw_table(slide, table: Table, x: float, y: float, w: float, scale: float, ctx: Ctx) -> None:
    rows = table_rows(table)
    heights = row_heights(table, scale, w)
    widths = column_widths(table, w)
    frame_shape = slide.shapes.add_table(len(rows), len(widths), E(x), E(y), E(w), E(sum(heights)))
    frame_shape.name = "Table"
    tbl = frame_shape.table
    tbl._tbl.tblPr.find(qn("a:tableStyleId")).text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"  # no style, no grid
    tbl.first_row = bool(table.header)
    tbl.horz_banding = False
    for j, cw in enumerate(widths):
        tbl.columns[j].width = E(cw)
    size = size_of("cell", scale)
    offset = 1 if table.header else 0
    for i, row in enumerate(rows):
        tbl.rows[i].height = E(heights[i])
        is_header = bool(table.header) and i == 0
        bold_row = (i - offset + 1) in table.bold and not is_header   # shaded as well as bold
        for j, text in enumerate(row):
            cell = tbl.cell(i, j)
            cell.margin_left = cell.margin_right = E(CELL_PAD)
            cell.margin_top = cell.margin_bottom = E(CELL_PAD)
            cell.vertical_anchor = MSO_ANCHOR.TOP
            if bold_row:
                cell.fill.solid()
                cell.fill.fore_color.rgb = ctx.rgb("mark")
            else:
                cell.fill.background()
            for side in ("L", "R", "T"):
                cell_border(cell, side, None)
            cell_border(cell, "B", ctx.colours["accent" if is_header else "rule"], 1.0 if is_header else 0.75)
            p = cell.text_frame.paragraphs[0]
            p.line_spacing = Pt(size * STYLES["cell"].line)
            for part, mark in inline(text):
                run = p.add_run()
                run.text = part
                style_run(run, ctx, size=round(size * CODE_IN_PROSE * 2) / 2 if mark == "code" else size,
                          font="code" if mark == "code" else "body",
                          colour="accent" if is_header else "ink",
                          bold=is_header or bold_row or mark == "bold" or (table.row_headers and j == 0),
                          italic=mark == "italic")


def panel(slide, items: list[Para | Table], x: float, y: float, w: float, max_h: float, ctx: Ctx,
          where: str, *, min_h: float = 0.0, card: str | None = "panel", border: str | None = None,
          corner: str | None = None, max_scale: float = SCALES[0]) -> float:
    """Fit the items into a card of width w, draw it, and return its height."""
    chunks = group_chunks([i for i in items if not isinstance(i, QrCode)])
    if not chunks:
        return 0.0
    inner_w = w - 2 * CARD_PAD_X
    scale, content_h, wraps, fits = fit(chunks, inner_w, max_h - 2 * CARD_PAD_Y, max_scale)
    if not fits:
        ctx.warnings.append(f"{where}: the panel does not fit; shorten it or lower `split`")
    if wraps:
        ctx.wraps.append(f"{where.removeprefix('slide ')} ({wraps})")
    card_h = min(max(content_h + 2 * CARD_PAD_Y, min_h), max_h)
    if corner and corner.startswith("bottom"):
        y = y + max_h - card_h
    if card or border:
        add_box(slide, x, y, w, card_h, ctx, fill=card, line=border, line_w=1.0, name="Panel", radius=0.12)
    top = y + CARD_PAD_Y + max(0.0, (card_h - 2 * CARD_PAD_Y - content_h) / 2)
    for chunk in chunks:
        height, _ = chunk_height(chunk, scale, inner_w)
        if isinstance(chunk, Table):
            draw_table(slide, chunk, x + CARD_PAD_X, top, inner_w, scale, ctx)
        else:
            draw_paragraphs(slide, chunk, x + CARD_PAD_X, top, inner_w, height * 1.04, scale, ctx)
        top += height + CHUNK_GAP
    return card_h


# --- layouts ------------------------------------------------------------------------------

def focus_of(spec: dict) -> tuple[float, float]:
    fx, fy = spec.get("focus") or (0.5, 0.5)
    return float(fx), float(fy)


def label_corner(spec: dict) -> str | None:
    """The corner a slide names for its AI label; None takes the top right without a word."""
    return str(spec["ai_label"]) if spec.get("ai_label") else None


def layout_title(slide, story: StorySlide, spec: dict, items: dict, ctx: Ctx, number: int) -> None:
    """The ML04 title slide: number, title, place and conference, name and e-mail; logo and earth."""
    meta = ctx.meta
    add_brand_picture(slide, "logo", 0.55, 0.42, ctx, alt="Evidenze logo")
    slot = ctx.brand.get("conference_logo")
    if slot:
        if (REPO / str(slot)).is_file():
            add_brand_picture(slide, "conference_logo", 0.5, 0.55, ctx, x=MARGIN, alt="Conference logo")
        else:
            ctx.placeholders.append(f"conference logo: {slot}")
            box = add_box(slide, MARGIN, 0.45, 2.6, 0.62, ctx, line="brand", line_w=1.0, dash=True,
                          name="Conference logo placeholder")
            add_lines(slide, 0, 0, 0, 0, ctx, [
                {"text": "CONFERENCE LOGO", "size": 9, "colour": "accent", "bold": True, "spacing": 120},
                {"text": str(slot), "size": 8, "font": "code", "colour": "grey", "gap": 2},
            ], shape=box, anchor=MSO_ANCHOR.MIDDLE, margins=(0.12, 0.05, 0.12, 0.05))

    left = 1.25
    number_label = re.sub(r"^([A-Za-z]+)\s*(\d+)$", r"\1 \2", str(meta.get("paper_number", "")))
    add_lines(slide, left, 1.3, 6.0, 0.8, ctx, [
        {"text": number_label, "size": 44, "font": "heading", "colour": "heading"}])
    set_title(slide, left, 2.3, 10.9, 1.4, ctx, [
        {"text": str(meta.get("title", story.title)), "size": 40, "font": "heading", "colour": "heading"},
        {"text": str(meta.get("subtitle", "")), "size": 24, "font": "heading", "gap": 6},
    ])
    # "PHUSE EU Connect 2026, Glasgow" reads "Glasgow – PHUSE EU Connect 2026", as on ML04.
    conference, _, place = str(meta.get("conference", "")).rpartition(", ")
    venue = f"{place} – {conference}" if conference else place
    speaker = " – ".join(p for p in (str(meta.get("author", "")), ctx.contact) if p)
    add_lines(slide, left, 3.9, 7.4, 1.0, ctx, [
        {"text": venue, "size": 20},
        {"text": speaker, "size": 18, "gap": 12},
    ])

    # The earth where ML04 had it. The talk's own picture, the house at night, stood between
    # them until 2026-10-28; it opens the story on the next slide now (the author's request).
    add_brand_picture(slide, "earth", 3.5, 4.15, ctx, x=9.25, alt="Evidenze Germany earth")
    if story.image:
        frame_box = (4.75, 4.95, 4.3, 4.3 * 9 / 16)
        place_picture(slide, story, *frame_box, ctx, focus=focus_of(spec),
                      zoom=float(spec.get("zoom", 1)), corner=label_corner(spec), kind="16:9")
    # Before the first drawing, one line says what the icon on every drawing marks: the icon,
    # then the words, below the name. The narrated deck's voice is generated too, so its build
    # takes `ai_legend_narrated` where the slide has one.
    words = (ctx.narrated and spec.get("ai_legend_narrated")) or spec.get("ai_legend")
    if words and ctx.label:
        _, _, lw, lh = label_box(0, 0, 4.3, 4.3 * 9 / 16, ctx)
        ly = 5.35
        add_label(slide, (left, ly, lw, lh), ctx, name="AI legend icon", alt="EU icon for AI-generated content")
        legend = add_lines(slide, left + lw + 0.12, ly, 4.6, lh, ctx, [
            {"text": str(words), "size": 14, "colour": "grey"}], anchor=MSO_ANCHOR.MIDDLE)
        legend.name = "AI legend"
    draw_corner(slide, ctx, None)


def layout_panel(slide, story: StorySlide, spec: dict, items: dict, ctx: Ctx, number: int) -> None:
    draw_header(slide, story, ctx)
    split = float(spec.get("split", 0.55))
    content_w = SLIDE_W - 2 * MARGIN
    img_w = split * (content_w - GAP)
    img_h = img_w * 3 / 4
    if img_h > BOTTOM - TOP:
        img_h = BOTTOM - TOP
        img_w = img_h * 4 / 3
    place_picture(slide, story, MARGIN, TOP, img_w, img_h, ctx, focus=focus_of(spec),
                  zoom=float(spec.get("zoom", 1)), corner=label_corner(spec), kind="4:3 crop")
    draw_rings(slide, spec.get("rings"), MARGIN, TOP, img_w, img_h, ctx)
    px = MARGIN + img_w + GAP
    panel(slide, items["panel"], px, TOP, SLIDE_W - MARGIN - px, BOTTOM - TOP, ctx,
          f"slide {story.id}", min_h=img_h)
    if ctx.brand.get("footer_logo"):
        add_brand_picture(slide, "logo", 7.08, 0.2, ctx, alt="Evidenze logo")
    draw_corner(slide, ctx, number)


def layout_full(slide, story: StorySlide, spec: dict, items: dict, ctx: Ctx, number: int) -> None:
    """The title on top and the whole 16:9 picture below it, centred, as ML04 shows a scene."""
    draw_header(slide, story, ctx)
    h = SLIDE_H - 0.3 - TOP
    w = h * 16 / 9
    x = (SLIDE_W - w) / 2
    place_picture(slide, story, x, TOP, w, h, ctx, focus=focus_of(spec),
                  zoom=float(spec.get("zoom", 1)), corner=label_corner(spec), kind="full frame, 16:9")
    draw_rings(slide, spec.get("rings"), x, TOP, w, h, ctx)
    inset = spec.get("inset")
    if inset and items["inset"]:
        iw = float(inset.get("width", 4.6))
        corner = inset.get("corner", "bottom-right")
        ix = x + 0.25 if corner.endswith("left") else x + w - 0.25 - iw
        panel(slide, items["inset"], ix, TOP + 0.25, iw, h - 0.5, ctx, f"slide {story.id} inset",
              card="FFFFFF", border="rule", corner=corner, max_scale=1.0)
    if ctx.brand.get("footer_logo"):
        add_brand_picture(slide, "logo", 7.08, 0.2, ctx, alt="Evidenze logo")
    draw_corner(slide, ctx, number)


def layout_close(slide, story: StorySlide, spec: dict, items: dict, ctx: Ctx, number: int) -> None:
    """Questions and contact on the left, the QR codes on the right, the logo on top."""
    draw_header(slide, story, ctx, width=8.0)
    add_brand_picture(slide, "logo", 0.55, 0.36, ctx, alt="Evidenze logo")
    speaker = " – ".join(p for p in (str(ctx.meta.get("author", "")), ctx.contact) if p)
    contact = add_lines(slide, MARGIN, 1.9, 5.6, 1.5, ctx, [
        {"text": str(spec.get("heading", "Questions")), "size": 44, "font": "heading", "colour": "accent"},
        {"text": speaker, "size": 18, "gap": 10},
    ])
    if ctx.contact:
        contact.click_action.hyperlink.address = f"mailto:{ctx.contact}"
    rest = [i for i in items["panel"] if not isinstance(i, QrCode)]
    if rest:
        rest[0].gap = None
        panel(slide, rest, MARGIN - CARD_PAD_X, 3.7, 5.9 + CARD_PAD_X, BOTTOM - 3.7, ctx,
              f"slide {story.id}", card=None, max_scale=1.0)

    codes = [i for i in items["panel"] if isinstance(i, QrCode)]
    card_w, card_h, qr_side, y, gap = 2.85, 3.75, 2.35, 1.65, 0.4
    x0 = SLIDE_W - MARGIN - len(codes) * card_w - (len(codes) - 1) * gap
    for n, code in enumerate(codes):
        cx = x0 + n * (card_w + gap)
        add_box(slide, cx, y, card_w, card_h, ctx, fill="FFFFFF", line="rule", name=f"QR card {n + 1}",
                radius=0.12)
        add_lines(slide, cx, y + 0.2, card_w, 0.3, ctx, [
            {"text": code.label.upper(), "size": 12, "colour": "accent", "bold": True, "spacing": 120}],
            align=PP_ALIGN.CENTER)
        qx, qy = cx + (card_w - qr_side) / 2, y + 0.6
        if code.url:
            pic = slide.shapes.add_picture(str(qr_png(code.url)), E(qx), E(qy), E(qr_side), E(qr_side))
            pic.name = f"QR code {n + 1}"
            set_alt(pic, f"QR code: {code.url}")
            pic.click_action.hyperlink.address = code.url
            # the code keeps the address as it is; the line beneath shows it readable, "ö" for "%C3%B6"
            shown = url_unquote(re.sub(r"^https?://", "", code.url))
        else:
            ctx.placeholders.append(f"{story.id}: QR code for {code.label!r} (set its url in deck.yaml)")
            box = add_box(slide, qx, qy, qr_side, qr_side, ctx, fill="panel", line="brand", dash=True,
                          name=f"QR placeholder {n + 1}")
            add_lines(slide, 0, 0, 0, 0, ctx, [
                {"text": "QR CODE TO COME", "size": 10, "colour": "accent", "bold": True, "spacing": 120},
                {"text": "set its url in slides/deck.yaml once the target is online", "size": 10,
                 "colour": "grey", "gap": 4}], shape=box, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER,
                margins=(0.15, 0.15, 0.15, 0.15))
            shown = "url to come"
        add_lines(slide, cx + 0.08, qy + qr_side + 0.12, card_w - 0.16, 0.5, ctx, [
            {"text": shown, "size": 9, "font": "code", "colour": "grey"}], align=PP_ALIGN.CENTER)
    draw_corner(slide, ctx, number)


def layout_picture(slide, story: StorySlide, spec: dict, items: dict, ctx: Ctx, number: int | None) -> None:
    """The story in pictures: the image fills the slide, with nothing on it but the AI label, the
    slide number, and the names that float above the cast with the labels over the objects.

    The title stays a real title, for the outline, the presenter's list of slides and screen
    readers, but it sits just above the slide's top edge, where the show never draws it.
    """
    set_title(slide, MARGIN, -1.0, 10.6, 0.7, ctx, [
        {"text": display_title(story.title), "size": 28, "font": "heading", "colour": "heading",
         "bold": True}])
    place_picture(slide, story, 0, 0, SLIDE_W, SLIDE_H, ctx, focus=focus_of(spec),
                  zoom=float(spec.get("zoom", 1)), corner=label_corner(spec), kind="whole slide, 16:9")
    rings = draw_rings(slide, spec.get("rings"), 0, 0, SLIDE_W, SLIDE_H, ctx)
    steps = draw_names(slide, story.id, spec, ctx) + ([Step("rings", rings)] if rings else [])
    if ctx.picture_corner and number is not None:
        draw_picture_number(slide, ctx, number, ctx.picture_corner)
    if ctx.motion and steps:
        if ctx.narrated:
            ctx.pops = steps       # the narration times them
        else:
            pop_on_click(slide, steps)


def layout_card(slide, story: StorySlide, spec: dict, ctx: Ctx, number: int) -> None:
    """The slide after a robot's first entrance: the same picture frozen under a white veil, and
    on it the robot's card, as a game shows a new team member. The AI label stays clear. A card
    with its own tag, such as the threat's, takes the tag into the slide's title.

    With `beside`, the card of a robot already on the team stands on its left, the rows lined up,
    so the room reads the two across: what the new one can do that the other cannot, and back."""
    who = ctx.cast[spec["card"]]
    tag = who["card"].get("tag")
    set_title(slide, MARGIN, -1.0, 10.6, 0.7, ctx, [
        {"text": f"{who['name']}, {str(tag).lower()}" if tag else f"{who['name']} joins the team",
         "size": 28, "font": "heading", "colour": "heading", "bold": True}])
    path = find_image(story.image)
    if path:
        place_picture(slide, story, 0, 0, SLIDE_W, SLIDE_H, ctx, focus=focus_of(spec),
                      zoom=float(spec.get("zoom", 1)), corner=label_corner(spec) or "top-right",
                      source=dimmed(path))
    if spec.get("beside"):
        other = ctx.cast[spec["beside"]]
        lines = [max(a, b) for a, b in zip_longest(card_lines(other["card"]), card_lines(who["card"]), fillvalue=1)]
        left = (SLIDE_W - 2 * CARD_W - CARD_GAP) / 2
        draw_card(slide, story.id, other, ctx, x=left, tag=BESIDE_TAG, lines=lines)
        draw_card(slide, story.id, who, ctx, x=left + CARD_W + CARD_GAP, lines=lines)
    else:
        draw_card(slide, story.id, who, ctx)
    if ctx.picture_corner:
        draw_picture_number(slide, ctx, number, ctx.picture_corner)


def card_lines(card: dict) -> list[int]:
    """How many lines each row's text takes on a card."""
    per_line = (CARD_W - 2 * CARD_PAD - CARD_KEY_W) * 72 * SLACK / (PROP * CARD_VALUE)
    return [max(1, math.ceil(len(str(value)) / per_line)) for _, value in card["rows"]]


def draw_card(slide, sid: str, who: dict, ctx: Ctx, *, x: float | None = None, tag: str | None = None,
              lines: list[int] | None = None) -> None:
    """A robot's card: a black tag above it, the portrait with its AI label, the name and, in angle
    brackets, what it is in Claude Code, then a rule and the rows, KEY beside what it says. `x`
    places it (the default keeps it right of the centre), `tag` replaces its tag and `lines` sets
    each row's number of lines, so two cards side by side line up."""
    card = who["card"]
    x = SLIDE_W - CARD_RIGHT - CARD_W if x is None else x
    y = (SLIDE_H - CARD_H) / 2
    shapes = [add_box(slide, x, y, CARD_W, CARD_H, ctx, fill="FFFFFF", line="drawing", line_w=3.0,
                      radius=0.28, name=f"Card {who['name']}")]
    # The portrait sits in a frame as wide as the card's inside, so the AI label takes the
    # frame's top right corner, on white and clear of the drawing.
    fx, fy, fw = x + CARD_PAD, y + CARD_PAD + 0.05, CARD_W - 2 * CARD_PAD
    portrait = REPO / str(card["portrait"])
    with Image.open(portrait) as im:
        pw = PORTRAIT_H * im.width / im.height
    pic = slide.shapes.add_picture(str(embeddable(portrait)), E(fx + (fw - pw) / 2), E(fy), E(pw), E(PORTRAIT_H))
    pic.name = f"Portrait {who['name']}"
    set_alt(pic, f"{who['name']}, as drawn in the story")
    shapes.append(pic)
    if ctx.label:
        shapes.append(add_label(slide, label_box(fx, fy, fw, PORTRAIT_H, ctx), ctx,
                                name="AI label", alt="AI generated"))
    ty = fy + PORTRAIT_H + 0.12
    for text, font, size, bold in [(who["name"], "heading", CARD_NAME, True)] + (
            [(f"<{who['title']}>", "code", CARD_TITLE, False)] if who.get("title") else []):
        h = size * 1.2 / 72
        shapes.append(add_lines(slide, x, ty, CARD_W, h, ctx, [
            {"text": text, "size": size, "font": font, "colour": "drawing", "bold": bold}],
            anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, wrap=False))
        ty += h
    ty += 0.14
    shapes.append(add_box(slide, x + CARD_PAD, ty, CARD_W - 2 * CARD_PAD, 0.03, ctx, fill="drawing",
                          name="Card rule"))
    ty += 0.2
    vx = x + CARD_PAD + CARD_KEY_W
    vw = x + CARD_W - CARD_PAD - vx
    lift = (CARD_VALUE - CARD_KEY) * 0.75 / 72   # sets the smaller key on the value's baseline
    for (key, value), n in zip(card["rows"], lines or card_lines(card)):
        rh = n * CARD_VALUE * 1.15 / 72
        shapes.append(add_lines(slide, x + CARD_PAD, ty + lift, CARD_KEY_W, rh, ctx, [
            {"text": str(key).upper(), "size": CARD_KEY, "font": "code", "colour": "drawing", "bold": True}],
            wrap=False))
        shapes.append(add_lines(slide, vx, ty, vw, rh, ctx, [
            {"text": str(value), "size": CARD_VALUE, "colour": "drawing", "line": 1.15}]))
        ty += rh + 0.1
    stats = card.get("stats") or []
    if stats:
        # The stats strip, as a game shows its numbers: a thin rule, then each value in a cell of
        # its own, a small key above it. Only values the documentation states go here.
        sy = y + CARD_H - CARD_PAD + 0.06 - 0.72
        shapes.append(add_box(slide, x + CARD_PAD, sy, CARD_W - 2 * CARD_PAD, 0.02, ctx, fill="drawing",
                              name="Card stats rule"))
        cw = (CARD_W - 2 * CARD_PAD) / len(stats)
        for k, (key, value) in enumerate(stats):
            cx = x + CARD_PAD + k * cw
            if k:
                shapes.append(add_box(slide, cx, sy + 0.14, 0.015, 0.5, ctx, fill="rule", name="Card stats divider"))
            shapes.append(add_lines(slide, cx, sy + 0.1, cw, CARD_STAT_KEY * 1.2 / 72, ctx, [
                {"text": str(key).upper(), "size": CARD_STAT_KEY, "font": "code", "colour": "drawing",
                 "spacing": 40}], align=PP_ALIGN.CENTER, wrap=False))
            shapes.append(add_lines(slide, cx, sy + 0.1 + CARD_STAT_KEY * 1.3 / 72, cw, CARD_STAT_VALUE * 1.2 / 72, ctx, [
                {"text": str(value), "size": CARD_STAT_VALUE, "colour": "drawing", "bold": True}],
                align=PP_ALIGN.CENTER, wrap=False))
        bottom = sy - 0.05
    else:
        bottom = y + CARD_H - 0.15
    if ty > bottom:
        ctx.warnings.append(f"{sid}: the {who['name']}'s card runs past its bottom edge; shorten its rows")
    tag = str(tag or card.get("tag") or "NEW TEAM MEMBER")
    tw, th = len(tag) * MONO_REAL * CARD_TAG / 72 + 0.4, 0.34
    pill = add_box(slide, x + 0.35, y - th / 2, tw, th, ctx, fill="drawing", radius=th / 2, name="Card tag")
    add_lines(slide, 0, 0, 0, 0, ctx, [
        {"text": tag, "size": CARD_TAG, "font": "code", "colour": "FFFFFF", "bold": True, "spacing": 60}],
        shape=pill, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, wrap=False)
    shapes.append(pill)
    group = slide.shapes.add_group_shape(shapes)
    group.name = f"Card: {who['name']}"
    set_alt(group, f"Card: {who['name']}" + (f", {who['title']}" if who.get("title") else "") + ". "
            + "; ".join(f"{k}: {v}" for k, v in card["rows"] + (card.get("stats") or [])))


def layout_reference(slide, story: StorySlide, spec: dict, items: dict, ctx: Ctx, number: int) -> None:
    """The reference part: the paper's sentences on the left, the quoted files in a card on the right.

    `mechanism` (1 to 7) lights that leaf of the tracker. A slide with only one of `explain` and
    `panel` gives it the whole width.
    """
    shown = replace(story, mechanism=int(spec["mechanism"])) if spec.get("mechanism") else story
    draw_header(slide, shown, ctx)
    explain, quoted = items["explain"], items["panel"]
    content_w = SLIDE_W - 2 * MARGIN
    where = f"slide {story.id}"
    if explain and quoted:
        left_w = float(spec.get("split", 0.45)) * (content_w - GAP)
        panel(slide, explain, MARGIN - CARD_PAD_X, TOP, left_w + CARD_PAD_X, BOTTOM - TOP, ctx, where,
              card=None, max_scale=1.0)
        px = MARGIN + left_w + GAP
        panel(slide, quoted, px, TOP, SLIDE_W - MARGIN - px, BOTTOM - TOP, ctx, where, max_scale=1.0)
    elif quoted:
        panel(slide, quoted, MARGIN, TOP, content_w, BOTTOM - TOP, ctx, where, max_scale=1.0)
    elif explain:
        panel(slide, explain, MARGIN - CARD_PAD_X, TOP, content_w + CARD_PAD_X, BOTTOM - TOP, ctx, where,
              card=None, max_scale=1.0)
    if ctx.brand.get("footer_logo"):
        add_brand_picture(slide, "logo", 7.08, 0.2, ctx, alt="Evidenze logo")
    draw_corner(slide, ctx, number)


LAYOUT_FUNCTIONS = {"title": layout_title, "picture": layout_picture, "panel": layout_panel,
                    "full": layout_full, "close": layout_close, "reference": layout_reference}


# --- the presentation ------------------------------------------------------------------------

def widen_template(prs) -> None:
    """Make the default template 16:9 and stretch its placeholders to match.

    Only slides added later by hand in PowerPoint use the template's
    placeholders; the built slides position everything themselves.
    """
    factor = E(SLIDE_W) / prs.slide_width
    for layout in prs.slide_layouts:
        for ph in layout.placeholders:
            left, width = ph.left, ph.width
            if left is not None and width is not None:
                ph.left, ph.width = Emu(int(left * factor)), Emu(int(width * factor))
    for ph in prs.slide_master.placeholders:
        ph.left, ph.width = Emu(int(ph.left * factor)), Emu(int(ph.width * factor))
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)


def add_sections(prs, groups: list[tuple[str, list]]) -> None:
    """PowerPoint sections, one per beat, so the slide sorter reads like the storyline."""
    p14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
    pres = prs.part._element
    ext_lst = pres.find(qn("p:extLst"))
    if ext_lst is None:
        ext_lst = etree.SubElement(pres, qn("p:extLst"))
    ext = etree.SubElement(ext_lst, qn("p:ext"), uri="{521415D9-36F7-43E2-AB2F-B90AF26B5E84}")
    lst = etree.SubElement(ext, f"{{{p14}}}sectionLst", nsmap={"p14": p14})
    for name, slides in groups:
        guid = "{" + str(uuid.uuid5(uuid.NAMESPACE_URL, "section:" + name)).upper() + "}"
        section = etree.SubElement(lst, f"{{{p14}}}section", name=name, id=guid)
        ids = etree.SubElement(section, f"{{{p14}}}sldIdLst")
        for s in slides:
            etree.SubElement(ids, f"{{{p14}}}sldId", id=str(s.slide_id))


def point_to_answers(prs, story_of: dict[int, StorySlide], deck: dict, close_at: int) -> None:
    """The beats between the closing slide and the reference part each answer a question (since
    2026-10-28; the day before they waited hidden at the end of the deck). The closing slide's notes
    name each beat's question and how to reach it, a click for the first and its number for the
    rest, and each beat's last slide gives the number that leads back to the questions."""
    slides = list(prs.slides)
    runs: list[list[int]] = []                 # the first and the last slide of each beat
    for i in range(close_at + 1, len(slides)):
        s = story_of[i]
        if deck["slides"][s.id]["layout"] == "reference":
            break
        if runs and story_of[runs[-1][0]].section == s.section:
            runs[-1][1] = i
        else:
            runs.append([i, i])
    for first, last in reversed(runs):
        s = story_of[first]
        named = BEAT_NAME.match(s.section)
        question = named.group("title") if named else s.section
        how = "click on" if first == close_at + 1 else f"type {first + 1} and press Enter"
        add_note_line(slides[close_at], f"Asked “{question}”: {how}, {s.id} answers it.")
        add_note_line(slides[last], f"Back to the questions: type {close_at + 1} and press Enter.")


def add_note_line(slide, line: str) -> None:
    """Add a line to a slide's notes, just under their first line, the slide's id and title."""
    lines = slide.notes_slide.notes_text_frame.text.split("\n")
    set_notes(slide, "\n".join(lines[:1] + [line] + lines[1:]))


VARIANTS = ("-narrated-full", "-narrated", "-full", "")   # longest first, for variant_of()


def variant_suffix(narrated: bool = False, full: bool = False) -> str:
    return ("-narrated" if narrated else "") + ("-full" if full else "")


def variant_of(path: Path) -> str:
    """Which deck a built file is: its suffix among VARIANTS."""
    return next(v for v in VARIANTS if path.stem.endswith(v))


def output_path(meta: dict, narrated: bool = False, full: bool = False) -> Path:
    number = str(meta.get("paper_number", "") or "").strip()
    suffix = variant_suffix(narrated, full)
    return OUT / (f"PRE_{number}{suffix}.pptx" if number else f"talk{suffix}.pptx")


def build(final: bool, output: Path | None = None, narrated: bool = False) -> Ctx:
    story = parse_storyline()
    deck = load_deck(story)
    resolved = resolve_all(story, deck, narrated)
    meta = (yaml.safe_load(METADATA.read_text(encoding="utf-8")) if METADATA.exists() else {}) or {}
    ctx = Ctx(deck, meta)
    ctx.narrated = narrated
    clips: dict[str, Clip] = {}
    if narrated:
        if not ctx.motion:
            sys.exit("error: the narrated deck moves by itself, so it needs `motion: true` in slides/deck.yaml")
        clips = cut_narration(narration_plan(story, deck))

    def timed(slide, name: str, speed: str | None) -> bool:
        """In the narrated deck the slide plays its clip and moves on when it ends, or stays for
        its hold; the labels laid out on it wait for their words. False in the talk's own deck."""
        if not narrated:
            return False
        clip = clips[name]
        if clip.path:
            narrate(slide, clip, ctx.pops, name)
        set_transition(slide, speed, advance_ms=clip.ms)
        ctx.pops = []
        return True

    prs = Presentation()
    widen_template(prs)
    layout = prs.slide_layouts.get_by_name("Title Only")
    groups: list[tuple[str, list]] = []
    number = 0
    story_of: dict[int, StorySlide] = {}   # each slide's index in the deck, to its storyline slide
    close_at: int | None = None            # the closing slide's index, where the questions are taken
    for s in story:
        spec = deck["slides"][s.id]
        if narrated and (close_at is not None or spec["layout"] == "reference"):
            break   # the narrated deck ends on the closing slide: what follows answers questions
        if not groups or groups[-1][0] != s.section:
            groups.append((s.section, []))
        start = len(prs.slides)
        # The alt text a screen reader speaks: the storyline's Scene, the design source of the
        # image prompts, unless deck.yaml describes the picture as it was finally drawn (`alt`).
        seen = replace(s, scene=str(spec["alt"]).strip()) if spec.get("alt") else s
        # A build-up: earlier stages of the picture, each on a slide of its own, so the room
        # watches it fill before the slide itself shows the last. Each waits for the click, so
        # the speaker sets the pace (since 2026-10-27, the author's request; until then they
        # moved on by themselves after a moment). They carry the slide's notes and a number, the
        # later ones fade in from the one before, and motion or not, they stay.
        build = spec.get("build_up")
        for k, stage in enumerate((build or {}).get("stages") or []):
            number += 1
            slide = prs.slides.add_slide(layout)
            bars = stage.get("bars") or {}
            # an earlier stage shows its own bar, and only the last one bursts
            staged = {**spec, "names": [{**{k: v for k, v in e.items() if k != "burst"},
                                         "bar": bars.get(e["who"], e["bar"])} if "bar" in e else e
                                        for e in spec.get("names") or []]}
            layout_picture(slide, replace(seen, image=stage["image"], scene=str(stage.get("alt") or seen.scene).strip()),
                           staged, resolved[s.id], ctx, number)
            set_notes(slide, notes_text(s))
            speed = "med" if k and ctx.motion else None
            if not timed(slide, f"{s.id} stage {k + 1}", speed) and speed:
                set_transition(slide, speed)
            groups[-1][1].append(slide)
        # The steps of a fix: the states it passes through, each on a slide of its own with its
        # picture, bars and labels, before the slide itself shows the last (since 2026-10-22, the
        # author's request, after one slide's clicks did not play in PowerPoint as built). They
        # carry the slide's notes and a number, since the speaker stays on each; the first fades
        # in as the fix would, the rest as the room changes. Motion or not, they stay.
        for k, step in enumerate(spec.get("steps") or []):
            number += 1
            slide = prs.slides.add_slide(layout)
            bars = step.get("bars") or {}
            staged = {**spec, "labels": step.get("labels") or [],
                      "names": [{**{key: v for key, v in e.items() if key != "burst"},
                                 "bar": bars.get(e["who"], e["bar"])} if "bar" in e else e
                                for e in spec.get("names") or []]}
            layout_picture(slide, replace(seen, image=step["image"], scene=str(step.get("alt") or seen.scene).strip()),
                           staged, resolved[s.id], ctx, number)
            set_notes(slide, notes_text(s))
            speed = ("slow" if k == 0 and spec.get("transition") else "med") if ctx.motion else None
            if not timed(slide, f"{s.id} step {k + 1}", speed) and speed:
                set_transition(slide, speed)
            groups[-1][1].append(slide)
        number += 1
        slide = prs.slides.add_slide(layout)
        LAYOUT_FUNCTIONS[spec["layout"]](slide, seen, spec, resolved[s.id], ctx, number)
        set_notes(slide, notes_text(s, clicks=click_labels(spec) if ctx.motion and not narrated else []))
        if ctx.motion and build:
            speed = "med"                   # the last stage fades into the picture itself
        elif ctx.motion and spec.get("steps"):
            speed = "med"                   # the last step of a fix fades into the slide itself
        elif ctx.motion and spec.get("transition"):
            speed = "slow"                  # a pain and its fix share one camera: the fix fades in
        else:
            speed = None
        if not timed(slide, s.id, speed) and speed:
            set_transition(slide, speed)
        if not narrated and spec.get("advance") == "after_gif":
            # A GIF that plays once and ends on the next slide's picture: the deck moves on by
            # itself once it has settled, so the speaker's next click is not spent on a cut that
            # shows nothing (since 2026-10-29, the author's request; 0.3 into 1.1).
            path = find_image(s.image)
            if not path or path.suffix.lower() != ".gif":
                sys.exit(f"error: {s.id} has `advance: after_gif` but no GIF")
            set_transition(slide, speed, advance_ms=gif_play_ms(path) + GIF_SETTLE_MS)
        groups[-1][1].append(slide)
        if spec["layout"] == "close":
            close_at = len(prs.slides) - 1
        if spec.get("card"):
            # A robot's first entrance: the next slide freezes the picture and shows its card.
            number += 1
            slide = prs.slides.add_slide(layout)
            layout_card(slide, seen, spec, ctx, number)
            set_notes(slide, card_notes(s, ctx.cast[spec["card"]], ctx.cast.get(spec.get("beside") or "")))
            if not timed(slide, f"{s.id} card", "med" if ctx.motion else None) and ctx.motion:
                set_transition(slide, "med")
            groups[-1][1].append(slide)
        for k in range(start, len(prs.slides)):
            story_of[k] = s
    if not narrated and close_at is not None:
        point_to_answers(prs, story_of, deck, close_at)
    add_sections(prs, groups)

    # python-pptx's template brings its own last author and its dates of 2013: the build overwrites
    # them, and takes the title from the metadata, the paper's title and subtitle in one line.
    props = prs.core_properties
    props.title = " ".join(str(meta.get(k, "")).strip() for k in ("title", "subtitle")).strip() or story[0].title
    props.author = str(meta.get("author", ""))
    props.last_modified_by = props.author
    built_at = datetime.now(timezone.utc).replace(microsecond=0)
    props.created = built_at
    props.modified = built_at
    props.subject = str(meta.get("subject", ""))
    props.keywords = ", ".join(str(k) for k in meta.get("keywords") or [])
    props.language = "en-GB"
    props.comments = "Built by tools/build_slides.py from slides/storyline.md and slides/deck.yaml."
    props.revision = 1

    if final and ctx.placeholders:
        print("not final: these are still placeholders:")
        for p in ctx.placeholders:
            print(f"  {p}")
        sys.exit(1)
    target = output or output_path(meta, narrated, FULL)
    if output is None:
        OUT.mkdir(exist_ok=True)
        # A renamed paper number must not leave yesterday's deck next to today's.
        for stale in OUT.glob("PRE_*.pptx"):
            if stale != target and variant_of(stale) == variant_suffix(narrated, FULL):
                stale.unlink()
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        prs.save(target)
    except PermissionError:
        sys.exit(f"error: cannot write {target}; close it in PowerPoint and build again")
    shown = target.relative_to(REPO) if REPO in target.resolve().parents else target
    print(f"built {shown}: {len(prs.slides)} slides, "
          f"{len(ctx.images)} image(s) in place, {len(ctx.placeholders)} placeholder(s)")
    if narrated:
        ms = sum(c.ms or 0 for c in clips.values())
        print(f"narrated: {sum(1 for c in clips.values() if c.path)} clips; it plays by itself for "
              f"{ms // 60000}:{ms // 1000 % 60:02d} and stops on the last slide")
    for w in ctx.warnings:
        print(f"WARNING: {w}")
    if ctx.wraps:
        print("code lines wrap on slides " + ", ".join(ctx.wraps)
              + "; a lower `split` widens a panel")
    if ctx.placeholders and not final:
        print("run with --list to see what is still missing")
    return ctx


def list_status() -> None:
    """Print which images and brand files are there, which are missing."""
    story = parse_storyline()
    deck = load_deck(story)
    shown: set[str] = set()
    rows = []
    for s in story:
        if not s.image or s.image in shown:
            continue
        shown.add(s.image)
        found = find_image(s.image)
        name = s.image
        if found:
            name = found.relative_to(REPO).as_posix() if REPO in found.resolve().parents else str(found)
        rows.append((found is not None, s.id, name, s.title))
    for sid, spec in deck["slides"].items():
        for k, stage in enumerate((spec.get("build_up") or {}).get("stages") or [], 1):
            if stage["image"] in shown:
                continue
            shown.add(stage["image"])
            found = find_image(stage["image"])
            name = found.relative_to(REPO).as_posix() if found and REPO in found.resolve().parents else stage["image"]
            rows.append((found is not None, sid, name, f"stage {k} of its build-up"))
        for k, step in enumerate(spec.get("steps") or [], 1):
            if step["image"] in shown:
                continue
            shown.add(step["image"])
            found = find_image(step["image"])
            name = found.relative_to(REPO).as_posix() if found and REPO in found.resolve().parents else step["image"]
            rows.append((found is not None, sid, name, f"step {k} of its fix"))
    present = sum(1 for r in rows if r[0])
    print(f"images: {present} of {len(rows)} in place")
    for ok, sid, rel, title in rows:
        print(f"  {'ok     ' if ok else 'missing'}  {sid:<5} {rel:<45} {title}")
    print("brand:")
    for key in ("logo", "earth", "conference_logo", "ai_label"):
        rel = deck["brand"].get(key)
        if rel:
            print(f"  {'ok     ' if (REPO / str(rel)).is_file() else 'missing'}  {key:<16} {rel}")
    for spec in deck["slides"].values():
        for block in spec.get("panel") or []:
            codes = block.get("qr") or [] if isinstance(block, dict) else []
            for code in codes:
                state = "ok     " if code.get("url") else "missing"
                print(f"  {state}  QR code          {code.get('label')} ({code.get('url') or 'no url yet'})")


def main() -> None:
    global IMAGE_DIR, FULL
    parser = argparse.ArgumentParser(description="Build the talk's PowerPoint deck.")
    parser.add_argument("--list", action="store_true", help="list present and missing images, then stop")
    parser.add_argument("--final", action="store_true", help="fail while any placeholder remains")
    parser.add_argument("--output", type=Path, help="write the deck here instead of out/PRE_<number>.pptx")
    parser.add_argument("--images", type=Path, help="take the images from this folder instead of slides/beats/, "
                                                    "to try drafts without touching the repository")
    parser.add_argument("--narrated", action="store_true",
                        help="build the narrated deck, out/PRE_<number>-narrated.pptx, which plays by itself; "
                             "needs `uv run --group narration`")
    parser.add_argument("--full", action="store_true",
                        help="embed the drawings at full resolution instead of scaling them to a projector's "
                             "width; writes out/PRE_<number>-full.pptx (with --narrated, -narrated-full)")
    parser.add_argument("--timing", action="store_true",
                        help="print the storyline's Timing table from the planned seconds, then stop")
    args = parser.parse_args()
    if args.timing:
        story = parse_storyline()
        print_timing(story, load_deck(story))
        return
    if args.images:
        if not args.images.is_dir():
            sys.exit(f"error: {args.images} is not a folder")
        IMAGE_DIR = args.images.resolve()
    if args.list:
        list_status()
        return
    FULL = args.full
    build(final=args.final, output=args.output.resolve() if args.output else None, narrated=args.narrated)


if __name__ == "__main__":
    main()
