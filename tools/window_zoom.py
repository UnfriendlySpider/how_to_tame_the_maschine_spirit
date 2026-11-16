#!/usr/bin/env python3
"""Make 0.3's way into the story: the camera goes into the house at night through its lit
basement window and comes out in the cellar of 1.1.

Run with:

    uv run python tools/window_zoom.py            # slides/beats/beat-00-title-2.gif
    uv run python tools/window_zoom.py --ms 40    # the zoom's frame time

Like tools/goodbye_wave.py and tools/flying_sheets.py, it turns drawings into frames and draws
nothing by hand. 0.2 shows the house (slides/beats/beat-00-title-1.jpg) still; the speaker's
click brings 0.3, and its GIF starts as the slide appears: the camera closes in on the small
basement window, where a bare bulb burns lamp yellow, easing in and out and drawing the window
to the middle of the frame, until its light fills the frame; out of that light the cellar of
1.1 (slides/beats/beat-01-alone-1.jpg), whose bulb burns the same yellow, fades in. The last
frame is the cellar as 1.1 shows it, so the cut to 1.1 changes nothing on the screen. The GIF
plays once, and its last frame stays for ten minutes in case a player loops it anyway.

A raster drawing blurs when it is blown up forty-six times, so every frame of the house is drawn
again from it: the window is cut out at twice the GIF's size and softened by half a pixel of the
drawing, so its lines lose their steps; every pixel becomes black, white or the lamp's yellow,
and the result is halved. The edges stay sharp and round at every scale, and the halving
smooths them. (Since 2026-10-28, the author's request: the story begins as we go into
Steve's house, on his click; through the window since 2026-10-29, when its candle became a
lamp.)
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

REPO = Path(__file__).resolve().parent.parent
BEATS = REPO / "slides" / "beats"

HOUSE = BEATS / "beat-00-title-1.jpg"
CELLAR = BEATS / "beat-01-alone-1.jpg"
TARGET = BEATS / "beat-00-title-2.gif"
DRAWING_FORMATS = ("PNG", "JPEG", "GIF")   # the drawings, and the GIF this tool reads back;
                                           # Pillow would otherwise read any format

SIZE = (2752, 1536)      # the GIF's frame, the drawings' own size
SUPER = 2                # the house is drawn at twice that size, then halved
GREY = 45                # a pixel whose channels lie closer together than this is ink or paper
LAMP = (0xFC, 0xD6, 0x4A)  # the lamp yellow of the lit windows (slides/image-prompts.md, image 37)

# In pixels of the 2752 x 1536 drawing: the point the camera makes for, in the lit window below
# its bulb. It moves from its place in the picture to the middle of the frame as the camera
# closes in; at forty-six times closer the frame lies wholly in the window's yellow.
WINDOW = (1504.0, 1380.0)
ZOOM = 46.0
FADE = 8                 # frames of the cellar fading in out of the light (15 until 2026-10-29,
                         # when the deck had to shrink: each is a whole drawing, 0.25 MB)
FADE_MS = 60             # each, so the fewer frames still take about half a second
LAST_MS = 600_000        # the cellar stays; a GIF frame lasts at most 655 s


def whiten(im: Image.Image) -> Image.Image:
    """Every pixel brighter than 245 in all three channels becomes pure white."""
    r, g, b = im.split()
    bright = ImageChops.multiply(ImageChops.multiply(r.point(lambda v: 255 if v > 245 else 0),
                                                     g.point(lambda v: 255 if v > 245 else 0)),
                                 b.point(lambda v: 255 if v > 245 else 0))
    out = im.copy()
    out.paste((255, 255, 255), mask=bright)
    return out


def ease(t: float) -> float:
    """Smooth at both ends: sets off gently, speeds up and slows to a stop."""
    return t * t * (3 - 2 * t)


def view(house: Image.Image, scale: float, centre: float) -> Image.Image:
    """The house seen `scale` times closer, the window's point `centre` of the way to the middle."""
    w, h = house.size
    px, py = WINDOW
    cw, ch = w / scale, h / scale
    # Where the point stands on the screen: its share of the picture at first, the middle at the
    # end. The window around it keeps that share of its width and height.
    sx = px / w + (0.5 - px / w) * centre
    sy = py / h + (0.5 - py / h) * centre
    # Early on, the drift can outrun the zoom and push the window past the picture's edge; it
    # stays inside, so the point lags a little behind the middle until the zoom catches up.
    left = min(max(px - sx * cw, 0.0), w - cw)
    top = min(max(py - sy * ch, 0.0), h - ch)
    big = house.resize((SIZE[0] * SUPER, SIZE[1] * SUPER), Image.BICUBIC,
                       box=(left, top, left + cw, top + ch))
    # One pixel of the drawing covers SUPER * scale pixels here; softening by about half of
    # that rounds the steps of the drawing's own pixels before the edges are cut sharp.
    big = big.filter(ImageFilter.GaussianBlur(0.6 * SUPER * scale))
    r, g, b = big.split()
    spread = ImageChops.subtract(ImageChops.lighter(ImageChops.lighter(r, g), b),
                                 ImageChops.darker(ImageChops.darker(r, g), b))
    grey = spread.point(lambda v: 255 if v < GREY else 0)
    ink = big.convert("L").point(lambda v: 0 if v < 128 else 255).convert("RGB")
    # A coloured pixel lies between the lamp's yellow and black, or between it and white: dark
    # ones become black, pale ones white, the rest yellow.
    dark = big.convert("L").point(lambda v: 255 if v < 104 else 0)
    pale = b.point(lambda v: 255 if v > 165 else 0)
    lit = Image.new("RGB", big.size, LAMP)
    lit.paste((0, 0, 0), mask=dark)
    lit.paste((255, 255, 255), mask=ImageChops.subtract(pale, dark))
    return Image.composite(ink, lit, grey).resize(SIZE, Image.LANCZOS)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ms", type=int, default=40, help="frame time of the zoom, in milliseconds")
    ap.add_argument("--frames", type=int, default=60, help="frames of the zoom")
    ap.add_argument("--output", type=Path, default=TARGET)
    args = ap.parse_args()

    house = Image.open(HOUSE, formats=DRAWING_FORMATS).convert("RGB")
    cellar = Image.open(CELLAR, formats=DRAWING_FORMATS).convert("RGB")
    if house.size != cellar.size:
        raise SystemExit(f"error: {HOUSE.name} and {CELLAR.name} differ in size")

    frames: list[Image.Image] = []
    durations: list[int] = []
    for i in range(args.frames):
        e = ease(i / (args.frames - 1))
        # The closeness grows by equal factors along the easing, and the window drifts to the
        # middle along the same curve, so the camera moves as one.
        frames.append(view(house, math.exp(math.log(ZOOM) * e), e))
        durations.append(args.ms)
    # The zoom's last frames lie wholly in the window's light, which holds it for a moment.
    light = frames[-1]
    room = whiten(cellar.resize(SIZE, Image.LANCZOS))
    for i in range(1, FADE + 1):
        frames.append(Image.blend(light, room, i / FADE))
        durations.append(FADE_MS if i < FADE else LAST_MS)

    gif = [f.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
           for f in frames]
    out = args.output.resolve()
    # No `loop`: the GIF carries no loop block, so it plays once.
    gif[0].save(out, save_all=True, append_images=gif[1:], duration=durations,
                disposal=1, optimize=False)
    shown = out.relative_to(REPO) if REPO in out.parents else out
    with Image.open(out, formats=DRAWING_FORMATS) as written:   # Pillow merges frames that repeat, such as the lit ones
        count = written.n_frames
    print(f"wrote {shown}: {count} frames, {sum(durations[:-1]) / 1000:.2f} s before the last, "
          f"{out.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
