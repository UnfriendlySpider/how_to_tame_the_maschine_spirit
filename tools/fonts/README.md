# Bundled fonts

`LibertinusMono-Regular.otf` — Libertinus Mono 7.051, the monospace face of
the Libertinus family whose serif Typst ships built in. Bundled so that inline
code in the paper matches the body text in weight and width; Typst's own
monospace (DejaVu Sans Mono) is noticeably heavier. Licence: SIL Open Font
License 1.1, see `OFL.txt`. Source: https://github.com/alerque/libertinus.

`tools/build_paper.py` passes this directory to the compiler as a font path,
so no system installation is needed.
