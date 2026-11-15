"""Cut the five figures of the diagram cast out of their character sheet
(slides/image-prompts.md, image 46) into tools/diagrams/cast/.

Each figure is cut at the empty columns between them. The white outside its
outline becomes transparent, the white between the letter's strings too, and
the white inside stays, so a figure stands on a shaded box without showing
it through. Its lines are then thickened by seven pixels, a minimum filter
on the colour and a maximum filter on the alpha, so that drawn 130 to 210
diagram units tall they print as thick as the boxes' strokes.

Usage: uv run python tools/diagrams/cut_cast.py SHEET
SHEET is the PNG that fal returned (2752 x 1536); the kept JPEG,
slides/studies/excalidraw-cast-sheet.jpg, gives nearly the same cut."""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

OUT = Path(__file__).resolve().parent / "cast"
# the empty columns between the figures on the sheet of 2026-10-26
COLUMNS = {"worker": (70, 702), "reviewer": (765, 1147), "security": (1148, 1680),
           "letter": (1690, 2109), "programmer": (2150, 2670)}
# background enclosed by the letter's cross, strings and sheet (fractions of its box)
LETTER_SEEDS = [(0.2, 0.4), (0.8, 0.4), (0.2, 0.62), (0.8, 0.62), (0.5, 0.75), (0.4, 0.15),
                (0.6, 0.15), (0.35, 0.12), (0.65, 0.12), (0.35, 0.22), (0.65, 0.22), (0.3, 0.2), (0.7, 0.2)]
THICKEN = 7
PAD, MARGIN = 40, 12


def cut(sheet: np.ndarray, name: str, x0: int, x1: int) -> Image.Image:
    sub = sheet[:, x0 + PAD - 20: x1 + PAD + 20].copy()
    sub[:, :20] = 255; sub[:, -20:] = 255          # the neighbours' margins
    ink = sub.min(axis=2) < 200
    rows = np.where(ink.any(axis=1))[0]; cols = np.where(ink.any(axis=0))[0]
    c = sub[rows[0] - MARGIN: rows[-1] + 1 + MARGIN, cols[0] - MARGIN: cols[-1] + 1 + MARGIN].copy()
    c[(c > 245).all(axis=2)] = 255
    ink = c.min(axis=2) < 230
    closed = Image.fromarray((ink * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))
    ImageDraw.floodfill(closed, (0, 0), 128)       # the outside, with small gaps in the outline closed
    if name == "letter":
        h, w = ink.shape
        for sx, sy in LETTER_SEEDS:
            p = (int(w * sx), int(h * sy))
            if closed.getpixel(p) == 0:
                ImageDraw.floodfill(closed, p, 128)
    outside = np.asarray(closed) == 128
    grown = np.asarray(Image.fromarray((outside * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))) > 0
    alpha = np.where(grown, np.clip((255 - c.min(axis=2)) * 2, 0, 255), 255).astype(np.uint8)
    return Image.fromarray(np.dstack([c.astype(np.uint8), alpha]), "RGBA")


def thicken(im: Image.Image, size: int = THICKEN) -> Image.Image:
    big = Image.new("RGBA", (im.width + 2 * size, im.height + 2 * size), (255, 255, 255, 0))
    big.paste(im, (size, size))
    rgb = Image.new("RGB", big.size, "white"); rgb.paste(big, (0, 0), big)
    out = rgb.filter(ImageFilter.MinFilter(size))
    out.putalpha(big.getchannel("A").filter(ImageFilter.MaxFilter(size)))
    return out


def main() -> None:
    sheet = np.asarray(Image.open(sys.argv[1]).convert("RGB")).astype(np.int32)
    sheet = np.pad(sheet, ((PAD, PAD), (PAD, PAD), (0, 0)), constant_values=255)
    OUT.mkdir(exist_ok=True)
    for name, (x0, x1) in COLUMNS.items():
        thicken(cut(sheet, name, x0, x1)).save(OUT / f"{name}.png")
        print(f"wrote {OUT / name}.png")


if __name__ == "__main__":
    main()
