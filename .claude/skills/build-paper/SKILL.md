---
name: build-paper
description: Build the paper PDF and report the page count against the 8–12 page target. Use after any substantial change to paper/paper.md.
disable-model-invocation: true
allowed-tools: Bash(uv run python tools/build_paper.py *)
---

# Build the paper

1. Run `uv run python tools/build_paper.py --stats`.
2. Report the page count and whether it is inside the 8–12 page target.
3. If the build fails, quote the error and name the segment file under
   `out/seg/` it points at, so the author can find the offending Markdown.
4. If the count is above 12, list the three longest sections as candidates
   for cutting. Never suggest shrinking the font or the margins.
