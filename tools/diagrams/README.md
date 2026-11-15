# The paper's diagrams

The two diagrams of the paper, the tool call of chapter 4 and the lethal
trifecta of chapter 9, are Excalidraw drawings. Each one is written by a
script here and exported to `paper/figures/<name>.png` and
`paper/figures/<name>.excalidraw`. The `.excalidraw` file opens in
Excalidraw, or in Obsidian with its Excalidraw plugin, so a diagram can also
be changed by hand there and exported at scale 3 with padding 10.

| File | What it does |
|---|---|
| `dia_common.py` | boxes, text, arrows and the cast; the key: shaded green holds whatever the model decides, dashed grey is text the model reads, red stops |
| `tool_call.py` | chapter 4, 1480 by 560 units, printed at the full text width (`height: 63mm` in the figure fence) |
| `trifecta.py` | chapter 9, 1640 by 400 units, at the template's 40 mm |
| `cast/` | the talk's cast in the diagrams' look: worker, reviewer, security, letter, programmer |
| `cut_cast.py` | cuts `cast/` out of the character sheet (`slides/image-prompts.md`, image 46) |
| `export.mjs` | renders a script's elements with Excalidraw's own export library in Chromium |
| `fetch-lib.sh` | fetches that library and Excalidraw's two fonts into `lib/` (git-ignored), checksums pinned |

## Rebuild a diagram

The scripts need Python's standard library only; the export needs Node 18 or
later and Playwright with Chromium, as a Claude Code cloud session has them.
They sit outside `uv` on purpose: the paper's build never runs them, it reads
the PNGs.

```sh
tools/diagrams/fetch-lib.sh                       # once
uv run python tools/diagrams/tool_call.py /tmp/tool-call.json
node tools/diagrams/export.mjs /tmp/tool-call.json paper/figures/tool-call 3 10
uv run python tools/diagrams/trifecta.py /tmp/trifecta.json
node tools/diagrams/export.mjs /tmp/trifecta.json paper/figures/trifecta 3 10
uv run python tools/build_paper.py --stats
```

Keep the top right corner of each canvas empty: the template puts the EU's
AI icon there. Check the rendered page after an export, not only the PNG:
a label that fits on screen can touch a box border in print.
