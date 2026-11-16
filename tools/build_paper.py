#!/usr/bin/env python3
"""Build the PHUSE EU Connect 2026 paper: Markdown -> Typst -> PDF.

Single entry point. Run with:

    uv run python tools/build_paper.py            # build out/PAP_<number>.pdf
    uv run python tools/build_paper.py --stats    # build, then print page count and style hints
    uv run python tools/build_paper.py --watch    # rebuild on source changes
    uv run python tools/build_paper.py --renumber # number the references in order of first citation

Pipeline
--------
paper/paper.md is the source of the prose. It is plain Markdown plus fenced
"callout" blocks that Markdown parsers ignore:

    ::: note        neutral aside (use sparingly for a small analogy)
    ::: warning
    ::: tip
    ::: disclaimer  how the paper was made (once, after the abstract)
    ::: figure      one image or two side by side, then a caption (optional
                    `placement: none` pins it, optional `height: 63mm` sizes
                    a single image in place of figure-height, optional
                    `side: right|left` sets a single image beside the
                    paragraph before the fence); image paths are relative to
                    paper/ and must exist
    ::: filecard    describe a repository file and link to it on GitHub
    ::: pitfalls    the bullets that close a mechanism chapter, then a `---`
                    line and one warning paragraph; rendered as a red card
    ::: references  render the reference list from paper/references.md

The `filecard` fence is the anti-drift guarantee for the configuration
examples: the paper never carries a pasted copy of a hook, skill or settings
file. It names the file, the build checks the file exists, and the card links
to it on GitHub. The card itself is prose: one line of purpose (the caption)
and a few bullets on what the file does.

    ::: filecard
    .claude/hooks/protect-build-outputs.sh
    kind: hook
    Refuses hand edits to the generated PDF and the files staged for a release.

    - **Reads** the pending call as JSON on standard input
    - **Says no** with exit code 2
    :::

`kind:` is optional and inferred from the path (rules, skill, hook, settings,
agent, script). Cards render as numbered figures of their own kind ("File 3"). When
paper/metadata.yaml names a `repository`, the path in the card header links to
the file on GitHub.

References live in paper/references.md, the only copy: a lead-in paragraph,
then `## Group` headings, each with `[n] Org. "Title". URL (accessed
YYYY-MM-DD).` lines. In the prose you cite with `[4]` or `[4, 5]`; the build
turns each number into a link to its entry. The `::: references` fence marks
where the list goes. The build fails when a citation has no entry or an entry
is never cited, so the list and the prose cannot drift apart. It also fails
when the numbers do not follow the order of first citation, [1] first, with
no gaps; `--renumber` puts them in order in paper.md, references.md and
further-reading.md.

The Markdown itself is rendered by the vendored `cmarker` Typst package. Because
`read()` inside a Typst *package* resolves relative to the package (not the
project), we do NOT inject callouts through cmarker's raw-typst passthrough.
Instead we split the document at the fences in Python, write each piece to
out/seg/NNN.md, and stitch them together in a generated out/main.typ that calls
the helpers from tools/template.typ — where paths resolve against the project
root as expected.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

import typst
import yaml

REPO = Path(__file__).resolve().parent.parent
PAPER_DIR = REPO / "paper"
PAPER_MD = PAPER_DIR / "paper.md"
REFERENCES_MD = PAPER_DIR / "references.md"
METADATA = PAPER_DIR / "metadata.yaml"
OUT = REPO / "out"
SEG = OUT / "seg"
MAIN_TYP = OUT / "main.typ"
# The PDF is named as PHUSE wants the submission named, PAP_<paper number>.pdf,
# from `paper_number` in metadata.yaml; without a number it is out/paper.pdf.
PDF = OUT / "paper.pdf"
FONTS = REPO / "tools" / "fonts"   # bundled Libertinus Mono, see tools/fonts/README.md
PAGE_LIMIT = 12                   # PHUSE: twelve one-sided pages for a 20-25 minute talk
MECHANISM_CHAPTERS = 9            # chapters 2-10 (seven mechanisms, Safety, Data protection), each closed by a pitfalls card

FENCE = re.compile(r"^::: *(\w+)\n(.*?)\n::: *$", re.S | re.M)
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)")   # ![alt](path)
LONG_SENTENCE = 25   # CLAUDE.md, section 3: about 15 words on average, rarely more than 25

# A citation in the prose: [4] or [4, 5]. Never inside code.
CITE = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
CODE = re.compile(r"(```.*?```|`[^`\n]*`)", re.S)

# One reference entry: [n] Org. "Title" (optional note). URL (accessed date).
REF_ENTRY = re.compile(
    r'^\[(?P<n>\d+)\]\s+(?P<org>[^"]+?)\.\s+"(?P<title>[^"]+)"'
    r'(?P<note>\s*\([^)]*\))?\.\s+(?P<url>https?://\S+)\s+'
    r'\(accessed (?P<date>\d{4}-\d{2}-\d{2})\)\.\s*$'
)

FILECARD_KINDS = ("rules", "skill", "hook", "settings", "agent", "script")

# Front and back matter: set as headings without a number, so they neither step
# the chapter counter nor show a number in the PDF bookmarks.
UNNUMBERED = re.compile(r"^# (Abstract|References|Contact Information)[ \t]*$", re.M)

CITED: set[int] = set()   # numbers cited anywhere in the paper, filled by write_seg
COMMENT = re.compile(r"<!--.*?-->", re.S)
FURTHER_READING_MD = PAPER_DIR / "further-reading.md"


def typst_str(value: str) -> str:
    """Escape a Python string for embedding in a Typst string literal."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def split_segments(src: str) -> list[tuple[str, str]]:
    """Split the paper into (kind, text) segments at ::: fences.

    kind is "prose" for ordinary Markdown, or the fence keyword (note, warning,
    tip, disclaimer, figure, filecard, pitfalls, references) for a fenced block.
    """
    segments: list[tuple[str, str]] = []
    pos = 0
    for m in FENCE.finditer(src):
        if m.start() > pos:
            segments.append(("prose", src[pos:m.start()]))
        segments.append((m.group(1), m.group(2).strip()))
        pos = m.end()
    if pos < len(src):
        segments.append(("prose", src[pos:]))
    return segments


# --- citations -------------------------------------------------------------

def link_citations(md: str) -> str:
    """Turn `[4]` and `[4, 5]` into links to the reference entries.

    Code fences and inline code are left alone. Each number becomes its own
    link, the brackets stay literal text: `\\[[4](#ref-4), [5](#ref-5)\\]`.
    The label `ref-4` is attached to the entry by the template. The space
    before the bracket and after each comma becomes a non-breaking one, so a
    citation keeps to its word and never splits across lines.
    """
    def cite(m: re.Match[str]) -> str:
        nums = [int(n) for n in m.group(2).split(",")]
        CITED.update(nums)
        links = ",\u00a0".join(f"[{n}](#ref-{n})" for n in nums)
        return ("\u00a0" if m.group(1) else "") + f"\\[{links}\\]"

    # Whitespace before the bracket, unless it follows a table pipe; at the
    # start of a part the text before it was inline code.
    cited = re.compile(r"((?:(?<=[^\s|])|\A)[ \t]*\n?[ \t]*)?" + CITE.pattern)
    parts = CODE.split(md)
    for i in range(0, len(parts), 2):   # even indices are outside code
        parts[i] = cited.sub(cite, parts[i])
    return "".join(parts)


def first_citations(src: str) -> list[int]:
    """Reference numbers in the order the paper first cites them.

    Comments and code do not count. A paper in order reads 1, 2, 3, … from
    its first citation to its last new one.
    """
    order: list[int] = []
    for part in CODE.split(COMMENT.sub("", src))[::2]:
        for m in CITE.finditer(part):
            for n in (int(x) for x in m.group(1).split(",")):
                if n not in order:
                    order.append(n)
    return order


def map_citations(text: str, mapping: dict[int, int], where: str) -> str:
    """Rewrite every `[n]` outside comments and code through `mapping`.

    The numbers of one citation come out in ascending order. A number the
    mapping does not know stops the run, naming the file it came from.
    """
    def renumber(m: re.Match[str]) -> str:
        old = [int(x) for x in m.group(1).split(",")]
        unknown = [n for n in old if n not in mapping]
        if unknown:
            sys.exit(f"error: {where} cites {unknown}, which the paper does not cite")
        return "[" + ", ".join(str(n) for n in sorted(mapping[n] for n in old)) + "]"

    out: list[str] = []
    pos = 0
    for c in COMMENT.finditer(text):
        out.append(_map_outside_code(text[pos:c.start()], renumber))
        out.append(c.group(0))
        pos = c.end()
    out.append(_map_outside_code(text[pos:], renumber))
    return "".join(out)


def _map_outside_code(text: str, renumber) -> str:
    parts = CODE.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = CITE.sub(renumber, parts[i])
    return "".join(parts)


def renumber_references() -> None:
    """Number the references in the order the paper first cites them.

    Rewrites the citations in paper.md, the entries in references.md (kept
    in ascending order within each group) and the markers in
    further-reading.md. Comments keep their numbers: a note in a comment is
    history, written in the numbering of its day. All three rewrites are
    worked out before any file is written, so a run that stops on an error
    leaves every file as it was.
    """
    order = first_citations(PAPER_MD.read_text(encoding="utf-8"))
    _, groups = parse_references()
    listed = {e.n for g in groups for e in g.entries}
    if set(order) != listed:
        sys.exit(f"error: cited but not listed {sorted(set(order) - listed)}, "
                 f"listed but not cited {sorted(listed - set(order))}; fix that first")
    mapping = {old: new for new, old in enumerate(order, start=1)}
    if all(old == new for old, new in mapping.items()):
        print("references already numbered in order of first citation")
        return

    rewrites: dict[Path, str] = {}
    for path in (PAPER_MD, FURTHER_READING_MD):
        if path.exists():
            rewrites[path] = map_citations(path.read_text(encoding="utf-8"), mapping, path.name)

    # references.md: renumber each entry line and sort each run of entries.
    lines = REFERENCES_MD.read_text(encoding="utf-8").split("\n")
    out: list[str] = []
    run: list[tuple[int, str]] = []
    in_comment = False

    def flush() -> None:
        out.extend(line for _, line in sorted(run))
        run.clear()

    for line in lines:
        if not in_comment and line.startswith("[") and (m := REF_ENTRY.match(line)):
            new = mapping[int(m.group("n"))]
            run.append((new, f"[{new}]" + line[m.end("n") + 1:]))
            continue
        flush()
        if "<!--" in line and "-->" not in line.split("<!--", 1)[1]:
            in_comment = True
        elif in_comment and "-->" in line:
            in_comment = False
        out.append(line)
    flush()
    rewrites[REFERENCES_MD] = "\n".join(out)

    # Only now, with every rewrite known, touch the files: a stray number in
    # further-reading.md must not leave paper.md renumbered and the list not.
    for path, text in rewrites.items():
        path.write_text(text, encoding="utf-8")
    moved = sum(1 for old, new in mapping.items() if old != new)
    print(f"renumbered {moved} of {len(mapping)} references in order of first citation")


# --- file cards ------------------------------------------------------------

def infer_kind(rel: Path) -> str | None:
    """Guess a card's kind from where the file lives."""
    p = rel.as_posix()
    if ".claude/hooks/" in p:
        return "hook"
    if ".claude/skills/" in p:
        return "skill"
    if ".claude/agents/" in p:
        return "agent"
    if rel.name in ("settings.json", "settings.local.json"):
        return "settings"
    if rel.name == "CLAUDE.md" or ".claude/rules/" in p:
        return "rules"
    if p.startswith("tools/"):
        return "script"
    return None


def parse_filecard(body: str) -> tuple[Path, str, str, str]:
    """Parse a filecard fence into (path, kind, caption Markdown, body Markdown).

    The first line is the repository-relative path, optionally followed by a
    `kind:` line. The first paragraph after that is the caption; the rest is
    the card body.
    """
    lines = body.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i == len(lines):
        sys.exit("error: filecard fence without a file path")
    rel = Path(lines[i].strip())
    i += 1
    kind: str | None = None
    while i < len(lines) and lines[i].strip().startswith("kind:"):
        kind = lines[i].strip()[len("kind:"):].strip()
        i += 1
    target = (REPO / rel).resolve()
    if not target.is_file() or REPO not in target.parents:
        sys.exit(f"error: filecard points at a file that does not exist in the repo: {rel}")
    kind = kind or infer_kind(rel)
    if kind not in FILECARD_KINDS:
        sys.exit(f"error: filecard {rel} needs a kind from {FILECARD_KINDS}, got {kind!r}")
    rest = "\n".join(lines[i:]).strip()
    if not rest:
        sys.exit(f"error: filecard {rel} needs a one-line purpose after the path")
    caption, _, card_body = rest.partition("\n\n")
    return rel, kind, caption.strip(), card_body.strip()


REPO_URL: str = ""   # set from metadata.yaml by build(); empty means no links
REPO_BRANCH: str = "main"


def file_url(rel: Path) -> str:
    """GitHub URL of a repository file."""
    return f"{REPO_URL.rstrip('/')}/blob/{REPO_BRANCH}/{rel.as_posix()}"


# --- references ------------------------------------------------------------

@dataclass
class Entry:
    n: int
    org: str
    title: str
    note: str
    url: str
    date: str


@dataclass
class Group:
    title: str
    lead: list[str] = field(default_factory=list)
    entries: list[Entry] = field(default_factory=list)


def parse_references(path: Path = REFERENCES_MD) -> tuple[str, list[Group]]:
    """Read references.md into (lead-in Markdown, groups). Fails loudly."""
    if not path.exists():
        sys.exit(f"error: {path} not found")
    src = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
    lead: list[str] = []
    groups: list[Group] = []
    seen: dict[int, str] = {}
    for raw in src.splitlines():
        line = raw.rstrip()
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            groups.append(Group(title=line[3:].strip()))
            continue
        if line.startswith("["):
            m = REF_ENTRY.match(line)
            if not m:
                sys.exit(
                    "error: reference line does not match "
                    '[n] Org. "Title" (note). URL (accessed YYYY-MM-DD).\n  ' + line
                )
            if not groups:
                sys.exit(f"error: reference entry before the first '## Group' heading: {line}")
            n = int(m.group("n"))
            if n in seen:
                sys.exit(f"error: reference number [{n}] appears twice")
            seen[n] = line
            groups[-1].entries.append(Entry(
                n=n,
                org=m.group("org").strip(),
                title=m.group("title").strip(),
                note=(m.group("note") or "").strip(),
                url=m.group("url"),
                date=m.group("date"),
            ))
            continue
        (groups[-1].lead if groups else lead).append(line)
    return "\n".join(lead).strip(), groups


def shared_prefix(urls: list[str]) -> str:
    """Longest common URL prefix that ends in '/' and goes past the host."""
    if len(urls) < 2:
        return ""
    prefix = urls[0]
    for u in urls[1:]:
        while not u.startswith(prefix):
            prefix = prefix[:-1]
    prefix = prefix[: prefix.rfind("/") + 1]
    host_end = prefix.find("/", len("https://"))
    return prefix if host_end != -1 and len(prefix) > host_end + 1 else ""


MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


def long_date(iso: str) -> str:
    """2026-10-08 -> 8 October 2026, the form the lead-in uses."""
    year, month, day = (int(p) for p in iso.split("-"))
    return f"{day} {MONTHS[month - 1]} {year}"


def short_url(url: str) -> str:
    """A URL as the list shows it: no scheme, no www., arXiv as arXiv:<id>."""
    shown = re.sub(r"^https?://(www\.)?", "", url)
    return re.sub(r"^arxiv\.org/abs/", "arXiv:", shown)


def render_references(lead_in: str, groups: list[Group], extra: str, emit, seg) -> None:
    """Emit the Typst calls for the reference list.

    The entries follow their numbers, which follow the order of first
    citation, in two columns. Every entry in references.md carries its access
    date. The list states the date most entries share once, in the lead-in,
    and shows a date only on an entry read on another day. The groups in
    references.md sort the sources by kind; in the list they only shorten
    entries. A group with one organisation and one URL prefix, the
    documentation, shows each page by its group's name and its page name,
    the lead-in states the prefix once, and pages of one group cited one
    after another share an entry. Every other entry shows
    organisation, title, note and a shortened URL that links to the full
    one.
    """
    dates = [e.date for g in groups for e in g.entries]
    common = max(sorted(set(dates)), key=dates.count) if dates else ""
    if common and long_date(common) not in lead_in:
        print(f"WARNING: the References lead-in does not name the access date most entries share, {long_date(common)}")
    pages: list[str] = []
    entries: list[tuple[int, str, str]] = []   # (number, pages group or "", text or page name)
    urls: dict[int, str] = {}
    for g in groups:
        if any(line.strip() for line in g.lead):
            sys.exit(f"error: the list shows no group text, but '{g.title}' has some:\n" + "\n".join(g.lead))
        orgs = {e.org for e in g.entries}
        prefix = shared_prefix([e.url for e in g.entries])
        pages_group = len(orgs) == 1 and bool(prefix)
        if pages_group:
            pages.append(f"[{short_url(prefix)}]({prefix})")
        for e in g.entries:
            date = "" if e.date == common else f", accessed {e.date}"
            urls[e.n] = e.url
            if pages_group:
                entries.append((e.n, g.title, e.url[len(prefix):] + date))
                continue
            text = f'{e.org}. "{e.title}"'
            if e.note:
                text += f" {e.note}"
            text += f". [`{short_url(e.url)}`]({e.url}){date}."
            entries.append((e.n, "", text))
    if pages:
        lead_in += " The documentation pages are under " + " and ".join(pages) + "."
    intro = "\n\n".join(t for t in (lead_in, extra) if t)
    if intro:
        emit(f'#md("{seg(intro)}")')
    # Pages of one group cited one after another share an entry.
    items: list[str] = []
    entries.sort()
    i = 0
    while i < len(entries):
        n, group, text = entries[i]
        if not group:
            items.append(f'({n}, "{seg(text)}")')
            i += 1
            continue
        run = [entries[i]]
        while i + len(run) < len(entries) and entries[i + len(run)][1] == group:
            run.append(entries[i + len(run)])
        parts = []
        for m, _, page in run:
            name, _, note = page.partition(", accessed ")
            parts.append(f'({m}, "{typst_str(name)}", "{typst_str(urls[m])}", "{typst_str(", accessed " + note if note else "")}")')
        items.append(f'({n}, "{typst_str(group)}", ({", ".join(parts)},))')
        i += len(run)
    emit(f"#reflist(({', '.join(items)},))")


def parse_pitfalls(text: str) -> tuple[str, str | None]:
    """Split a `::: pitfalls` body into the bullet list and its mandatory warning.

    The body is a Markdown bullet list, then a line that is exactly `---` and
    one warning paragraph that names the genuinely dangerous case (CLAUDE.md,
    section 9). The card renders the bullets on the left and the warning as a
    narrower box on the right.
    """
    parts = re.split(r"^---\s*$", text.strip(), flags=re.M)
    if len(parts) > 2:
        sys.exit("error: a pitfalls fence may carry at most one '---' separator:\n" + text)
    bullets = parts[0].strip()
    if not bullets.startswith("- "):
        sys.exit("error: a pitfalls fence must start with a bullet list ('- '):\n" + text)
    if len(parts) < 2:
        sys.exit("error: a pitfalls fence needs a '---' line and one warning paragraph:\n" + text)
    warning = parts[1].strip()
    if warning == "":
        sys.exit("error: a pitfalls fence has a '---' separator but no warning after it:\n" + text)
    return bullets, warning


# --- segments and the document body ----------------------------------------

def write_seg(index: int, text: str) -> str:
    """Write a segment file and return its project-root-absolute Typst path."""
    path = SEG / f"{index:03d}.md"
    path.write_text(link_citations(text), encoding="utf-8")
    return f"/out/seg/{index:03d}.md"


def render_body(segments: list[tuple[str, str]]) -> str:
    """Turn segments into Typst calls against tools/template.typ helpers."""
    lines: list[str] = []
    idx = 0

    def seg(text: str) -> str:
        nonlocal idx
        ref = write_seg(idx, text)
        idx += 1
        return ref

    # A figure with a `side:` line stands beside the paragraph that precedes
    # it: that paragraph leaves the prose before the fence and goes with it.
    beside: dict[int, str] = {}
    segments = list(segments)
    for i, (kind, text) in enumerate(segments):
        if kind == "figure" and re.search(r"^\s*side:", text, re.M):
            if i == 0 or segments[i - 1][0] != "prose":
                sys.exit("error: a figure with `side:` must follow a paragraph of prose")
            head, _, para = segments[i - 1][1].rstrip().rpartition("\n\n")
            if not para.strip() or re.match(r"\s*(#|\||- |:::)", para):
                sys.exit("error: a figure with `side:` must follow a plain paragraph")
            segments[i - 1] = ("prose", head + "\n")
            beside[i] = para

    has_references = False
    pitfall_cards = 0
    for i, (kind, text) in enumerate(segments):
        if kind == "references":
            has_references = True
            lead_in, groups = parse_references()
            render_references(lead_in, groups, text, lines.append, seg)
            continue
        if not text.strip():
            continue
        if kind == "prose":
            pos = 0
            for m in UNNUMBERED.finditer(text):
                if text[pos:m.start()].strip():
                    lines.append(f'#md("{seg(text[pos:m.start()])}")')
                lines.append(f"#heading(level: 1, numbering: none)[{m.group(1)}]")
                pos = m.end()
            if text[pos:].strip():
                lines.append(f'#md("{seg(text[pos:])}")')
        elif kind == "filecard":
            rel, card_kind, caption, card_body = parse_filecard(text)
            url = f'"{typst_str(file_url(rel))}"' if REPO_URL else "none"
            lines.append(
                f'#filecard(kind: "{card_kind}", path: "{typst_str(rel.as_posix())}", '
                f'url: {url}, "{seg(caption)}", "{seg(card_body)}")'
            )
        elif kind == "pitfalls":
            bullets, warning = parse_pitfalls(text)
            pitfall_cards += 1
            lines.append(f'#pitfallcard("{seg(bullets)}", warning: "{seg(warning)}")')
        elif kind == "figure":
            # An optional `placement: none|top|bottom|auto` line pins the figure
            # instead of letting it float (the default, `auto`). An optional
            # `height: <n>mm` line sets a single image's height in place of the
            # template's figure-height, for a diagram drawn to fill the width.
            # Then one or two images, `![alt](path)` with the path relative to
            # paper/, side by side, and the caption.
            # An optional `side: right|left` line sets a single image beside
            # the paragraph before the fence, the caption under the image.
            placement = "auto"
            height = None
            side = None
            kept: list[str] = []
            for line in text.splitlines():
                if line.strip().startswith("placement:"):
                    placement = line.strip()[len("placement:"):].strip()
                elif line.strip().startswith("height:"):
                    height = line.strip()[len("height:"):].strip()
                elif line.strip().startswith("side:"):
                    side = line.strip()[len("side:"):].strip()
                else:
                    kept.append(line)
            if side not in (None, "right", "left"):
                sys.exit(f"error: figure side must be right or left, got {side!r}")
            if placement not in ("auto", "none", "top", "bottom"):
                sys.exit(f"error: figure placement must be auto, none, top or bottom, got {placement!r}")
            if height is not None and not re.fullmatch(r"\d{2}mm", height):
                sys.exit(f"error: figure height must be whole millimetres, such as 64mm, got {height!r}")
            text = "\n".join(kept).strip()
            images = list(IMAGE.finditer(text))
            if not 1 <= len(images) <= 2:
                sys.exit(f"error: a figure takes one or two images, found {len(images)}:\n{text}")
            if height is not None and len(images) != 1:
                sys.exit("error: a figure's height applies to a single image, not to a pair")
            if side is not None and len(images) != 1:
                sys.exit("error: only a single image can stand beside a paragraph")
            paths: list[str] = []
            alts: list[str] = []
            for m in images:
                target = (PAPER_DIR / m.group(2).strip()).resolve()
                if not target.is_file() or REPO not in target.parents:
                    sys.exit(f"error: figure points at an image that does not exist in the repo: {m.group(2)}")
                paths.append("/" + target.relative_to(REPO).as_posix())
                alts.append(m.group(1).strip())
            caption = IMAGE.sub("", text).strip()
            if not caption:
                sys.exit(f"error: a figure needs a caption after its images:\n{text}")
            path_list = "(" + "".join(f'"{typst_str(p)}", ' for p in paths) + ")"
            alt_list = "(" + "".join(f'"{typst_str(a)}", ' for a in alts) + ")"
            if side is not None:
                lines.append(
                    f'#sidefigure("{seg(beside[i])}", {path_list}, {alt_list}, "{seg(caption)}", '
                    f'side: "{side}"' + (f', height: {height}' if height else '') + ')'
                )
                continue
            lines.append(
                f'#figurebox({path_list}, {alt_list}, "{seg(caption)}", placement: {placement}'
                + (f', height: {height}' if height else '') + ')'
            )
        else:  # note / warning / tip / disclaimer — unknown kinds render as a loud orange box
            lines.append(f'#callout(kind: "{kind}")[#md("{seg(text)}")]')

    if pitfall_cards != MECHANISM_CHAPTERS:
        print(f"WARNING: expected {MECHANISM_CHAPTERS} pitfalls fences (one per chapter from 2 to {1 + MECHANISM_CHAPTERS}), found {pitfall_cards}")
    if CITED and not has_references:
        sys.exit("error: the paper cites references but has no '::: references' fence")
    if has_references:
        _, groups = parse_references()
        numbers = {e.n for g in groups for e in g.entries}
        missing = sorted(CITED - numbers)
        unused = sorted(numbers - CITED)
        if missing:
            sys.exit(f"error: cited but not in references.md: {missing}")
        if unused:
            sys.exit(f"error: in references.md but never cited: {unused}")
    return "\n\n".join(lines)


def build() -> None:
    """Read sources, generate out/main.typ, compile to out/PAP_<number>.pdf."""
    if not PAPER_MD.exists():
        sys.exit(f"error: {PAPER_MD} not found")

    meta = yaml.safe_load(METADATA.read_text(encoding="utf-8")) if METADATA.exists() else {}
    meta = meta or {}
    global REPO_URL, REPO_BRANCH, PDF
    REPO_URL = str(meta.get("repository", "") or "")
    REPO_BRANCH = str(meta.get("branch", "main") or "main")
    number = str(meta.get("paper_number", "") or "").strip()
    if number and not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", number):
        sys.exit(f"error: paper/metadata.yaml: paper_number {number!r} is not a file-name part "
                 "(letters, digits, - and _)")
    PDF = OUT / (f"PAP_{number}.pdf" if number else "paper.pdf")
    # A renamed paper number must not leave yesterday's PDF next to today's.
    for stale in list(OUT.glob("PAP_*.pdf")) + [OUT / "paper.pdf"]:
        if stale != PDF and stale.exists():
            stale.unlink()

    # Clean and recreate the segment dir so stale segments never leak in.
    if SEG.exists():
        shutil.rmtree(SEG)
    SEG.mkdir(parents=True, exist_ok=True)
    CITED.clear()

    source = PAPER_MD.read_text(encoding="utf-8")
    for chapter, heading in sub_headings(source):
        print(f"WARNING: chapters 2 to {1 + MECHANISM_CHAPTERS} have no sub-headings, but '{chapter}' has '{heading}'")
    segments = split_segments(COMMENT.sub("", source))
    body = render_body(segments)
    order = first_citations(source)
    if order != list(range(1, len(order) + 1)):
        sys.exit(
            "error: the references are not numbered in order of first citation; the paper "
            f"cites {', '.join(map(str, order[:10]))}, … first. Run "
            "`uv run python tools/build_paper.py --renumber`."
        )

    def meta_field(key: str, default: str = "") -> str:
        return typst_str(str(meta.get(key, default)))

    subtitle = meta.get("subtitle")
    subtitle_arg = f'subtitle: "{typst_str(str(subtitle))}",' if subtitle else "subtitle: none,"

    keywords = meta.get("keywords") or []
    if isinstance(keywords, str):
        keywords = [k.strip() for k in keywords.split(",") if k.strip()]
    keywords_arg = "(" + "".join(f'"{typst_str(str(k))}", ' for k in keywords) + ")"

    header = "\n".join([
        '#import "/tools/template.typ": *',
        "#show: conf.with(",
        f'  title: "{meta_field("title")}",',
        f"  {subtitle_arg}",
        f'  author: "{meta_field("author")}",',
        f'  affiliation: "{meta_field("affiliation")}",',
        f'  city: "{meta_field("city")}",',
        f'  country: "{meta_field("country")}",',
        f'  conference: "{meta_field("conference")}",',
        f'  date: "{meta_field("date")}",',
        f'  paper-number: "{meta_field("paper_number")}",',
        f'  subject: "{meta_field("subject")}",',
        f"  keywords: {keywords_arg},",
        ")",
        "",
    ])
    MAIN_TYP.write_text(header + "\n" + body + "\n", encoding="utf-8")

    pdf_bytes = typst.compile(str(MAIN_TYP), root=str(REPO), font_paths=[str(FONTS)])
    PDF.write_bytes(pdf_bytes if isinstance(pdf_bytes, bytes) else pdf_bytes[0])
    print(f"built {PDF.relative_to(REPO)}")


def prose_sentences(src: str) -> list[tuple[str, list[str]]]:
    """Per chapter, the prose sentences, for the proofreading hints of --stats.

    The sentence split is rough. The Abstract is frozen and skipped. File
    cards, the reference list, tables, figure images, comments and fence lines
    do not count; a blank line or a list item ends a sentence, and a code span
    counts as one word.
    """
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    src = re.sub(r"^::: *(filecard|references)\n.*?^::: *$", "", src, flags=re.S | re.M)
    chapters: list[tuple[str, list[str]]] = []
    for chapter in re.split(r"^# ", src, flags=re.M)[1:]:
        title, _, body = chapter.partition("\n")
        if title.strip() == "Abstract":
            continue
        kept = [l for l in body.splitlines()
                if not re.match(r"\s*(\||:::|---\s*$|#|!\[|placement:|height:|side:)", l)]
        sentences: list[str] = []
        for block in re.split(r"\n\s*\n|\n\s*- ", "\n".join(kept)):
            block = CITE.sub("", block)
            block = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block)
            block = CODE.sub(lambda m: m.group(0).replace(" ", "·"), block)   # one word
            block = re.sub(r"^\s*-\s+", "", re.sub(r"\s+", " ", block)).strip()
            # A sentence ends at . ! or ?, also inside a closing quote: entry." Then
            sentences += [s for s in re.split(r"(?:(?<=[.!?])|(?<=[.!?][\"”]))\s+(?=[A-Z\"“*(`])", block) if s]
        chapters.append((title.strip(), sentences))
    return chapters


def long_sentences(src: str, limit: int = LONG_SENTENCE) -> list[tuple[str, list[str]]]:
    """Per chapter, the opening words of every prose sentence over `limit` words."""
    report: list[tuple[str, list[str]]] = []
    for title, sentences in prose_sentences(src):
        found = [f"[{len(s.split())}] " + " ".join(s.split()[:8]) + " …"
                 for s in sentences if len(s.split()) > limit]
        if found:
            report.append((title, found))
    return report


# An empty opener (Helen Sword's waste words): "It is", "There are", or a bare
# "This" or "That" straight before its verb. Often it can go, so the sentence
# starts with what it is about; sometimes it serves the stress position.
EMPTY_OPENER = re.compile(
    r"^\W*(?:(?:It|There) (?:is|are|was|were)\b"
    r"|(?:This|That|These|Those) (?:is|are|was|were|has|have|does|do|means|shows|makes|can|will|would|may|might|must)\b)")
# More than one hedge in a sentence: keep one, where the facts need it.
HEDGE = re.compile(r"\b(?:may|might|could|usually|often|tends?|generally|possibly|perhaps|probably|likely)\b", re.I)


def style_hints(src: str) -> list[tuple[str, list[str]]]:
    """Per chapter, sentences with an empty opener or more than one hedge.

    A proofreading hint for --stats, not a check, after the sentence rules in
    CLAUDE.md, section 3: what each flags may be the right choice in place.
    """
    report: list[tuple[str, list[str]]] = []
    for title, sentences in prose_sentences(src):
        found: list[str] = []
        for s in sentences:
            opening = " ".join(s.split()[:8]) + " …"
            if EMPTY_OPENER.match(s):
                found.append(f"[opener] {opening}")
            hedges = HEDGE.findall(s)
            if len(hedges) > 1:
                found.append(f"[hedges: {', '.join(h.lower() for h in hedges)}] {opening}")
        if found:
            report.append((title, found))
    return report


def sub_headings(src: str) -> list[tuple[str, str]]:
    """(chapter, heading) for every sub-heading in chapters 2 to 10.

    Those chapters carry none: text, figure, table, card and pitfalls card
    follow each other without numbered sections (CLAUDE.md, section 9).
    """
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    found: list[tuple[str, str]] = []
    number = 0
    for chapter in re.split(r"^# ", src, flags=re.M)[1:]:
        title, _, body = chapter.partition("\n")
        if UNNUMBERED.match("# " + title):
            continue
        number += 1
        if 2 <= number <= 1 + MECHANISM_CHAPTERS:
            found += [(title.strip(), h.strip()) for h in re.findall(r"^##+ (.+)$", body, flags=re.M)]
    return found


def page_count() -> int:
    """Compile to SVG (one item per page) and count the pages."""
    pages = typst.compile(str(MAIN_TYP), root=str(REPO), format="svg", font_paths=[str(FONTS)])
    return len(pages) if isinstance(pages, list) else 1


def source_mtime() -> float:
    """Newest mtime across the sources a build reads — the watch trigger."""
    newest = 0.0
    for base in (PAPER_DIR, REPO / "tools", REPO / ".claude"):
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file():
                newest = max(newest, p.stat().st_mtime)
    return newest


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the PHUSE 2026 paper PDF.")
    parser.add_argument("--stats", action="store_true", help="print the page count, the long sentences and the style hints after building")
    parser.add_argument("--watch", action="store_true", help="rebuild on source changes")
    parser.add_argument("--renumber", action="store_true", help="number the references in order of first citation, then build")
    args = parser.parse_args()

    if args.renumber:
        renumber_references()
    build()

    if args.stats:
        n = page_count()
        status = "within 8-12 range" if 8 <= n <= 12 else "OUT OF 8-12 RANGE"
        print(f"pages: {n} ({status})")
        if n > PAGE_LIMIT:
            print(f"WARNING: PHUSE allows at most {PAGE_LIMIT} pages for a 20-25 minute talk")
        report = long_sentences(PAPER_MD.read_text(encoding="utf-8"))
        total = sum(len(found) for _, found in report)
        print(f"sentences over {LONG_SENTENCE} words: {total} (a hint; CLAUDE.md, section 3)")
        for title, found in report:
            print(f"  {title}: {len(found)}")
            for line in found:
                print(f"    {line}")
        hints = style_hints(PAPER_MD.read_text(encoding="utf-8"))
        total = sum(len(found) for _, found in hints)
        print(f"empty openers and stacked hedges: {total} (a hint; CLAUDE.md, section 3)")
        for title, found in hints:
            print(f"  {title}: {len(found)}")
            for line in found:
                print(f"    {line}")

    if args.watch:
        print("watching paper/, tools/ and .claude/ for changes (Ctrl-C to stop)...")
        last = source_mtime()
        try:
            while True:
                time.sleep(1.0)
                now = source_mtime()
                if now > last:
                    last = now
                    try:
                        build()
                    except SystemExit as exc:  # a bad card path or citation: report, keep watching
                        print(f"build failed: {exc}")
                    except Exception as exc:  # keep watching after a bad edit
                        print(f"build failed: {exc}")
        except KeyboardInterrupt:
            print("\nstopped.")


if __name__ == "__main__":
    main()
