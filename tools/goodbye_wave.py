#!/usr/bin/env python3
"""Make the goodbye of slide 8.3: the cast waves, in a loop of frames turned from one drawing.

Run with:

    uv run python tools/goodbye_wave.py                 # writes slides/beats/beat-08-team-3.gif
    uv run python tools/goodbye_wave.py --ms 110        # a slower wave
    uv run python tools/goodbye_wave.py --output /tmp/try.gif

The frame is pose A of the goodbye with the man in his own clothes
(slides/studies/anim-04-goodbye-out-own-clothes.png; anim-01 is the robe of 2026-10-09) with the
hanging strip of pose M (anim-02-goodbye-middle.png). Each waving part is cut out along its own outline, its
lines and whatever they enclose, and put back turned by a sine of the frame number:

- the robots' forearms turn stiffly about their elbow balls, and the ball is laid over the
  forearm again, so the forearm runs on under it;
- the man's hand and the reviewer's strip bend: the turn is nil where they leave the cuff and the
  belt and grows towards the fingertips and the strip's end, so they never come loose.

The four parts wave out of step. Every other line is the drawing's own and never moves. Where the
strip's fold hides the reviewer's outline, the outline is drawn in, so it shows when the fold
swings away. The frames are mapped onto the drawing's seven colours and written whole, without
transparency, so a viewer never has to put a frame together from the one before.

slides/image-prompts.md (image 30) says how the two poses were drawn.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parent.parent
POSE_A = REPO / "slides" / "studies" / "anim-04-goodbye-out-own-clothes.png"
POSE_M = REPO / "slides" / "studies" / "anim-02-goodbye-middle.png"
TARGET = REPO / "slides" / "beats" / "beat-08-team-3.gif"
DRAWING_FORMATS = ("PNG", "JPEG")   # what the drawings are; Pillow would otherwise read any format

# Everything below is in pixels of the 2752 x 1536 drawing.

# Where pose M's hanging strip replaces pose A's flying one: where the two differ, grown a little.
# The first box starts right of the man, whose clothes differ between the two poses since 2026-10-12.
STRIP_BOXES = [(1400, 949, 1933, 1128), (1569, 1121, 1754, 1376)]

# The upper side of the shirt cuff's top edge, left to right: the hand is cut off along it.
CUFF = [(1330, 377), (1403, 377), (1414, 378), (1414, 388), (1420, 390), (1428, 391), (1436, 392),
        (1446, 393), (1453, 392), (1453, 383), (1470, 382), (1530, 382)]
# The top of the cuff: below it the wrist sits in the sleeve and does not move.
CUFF_TOP = [(1330, 378), (1403, 378), (1414, 385), (1430, 391), (1446, 393), (1453, 390), (1470, 382),
            (1530, 382)]
# The reviewer's outline where the strip's fold hides it, from just above to just below the fold.
HIDDEN_OUTLINE = [(1745, 1290), (1740, 1300), (1734, 1311), (1727, 1322), (1721, 1331), (1716, 1338)]

# For each part: how it moves, how far (degrees) and when (a phase in frames of 8), the joint it
# turns about, the region it is cut from, white points outside it there (`seeds`), a point on it
# (`keep`), and what is laid over it again (`cover`, or the ball's radius).
PARTS = {
    "man": dict(kind="bend", amp=12.0, phase=0, pivot=(1434, 395), ramp=60,
                region=[(1330, 195), (1530, 195)] + CUFF[::-1],
                seeds=[(1335, 200), (1525, 200), (1525, 370), (1335, 372)], keep=(1440, 300),
                box=(1280, 140, 1580, 432),
                cover=[(1384, 377)] + CUFF[1:] + [(1500, 440), (1384, 440)]),
    "worker": dict(kind="stiff", amp=14.0, phase=4, pivot=(859, 757), ball=26.6, under=22,
                   region=[(752, 482), (912, 482), (912, 757), (752, 757)],
                   seeds=[(756, 486), (908, 486), (908, 700), (760, 600)], keep=(830, 600)),
    "strip": dict(kind="bend", amp=12.0, phase=2, pivot=(1632, 1029), span=(1029, 1336),
                  region=[(1584, 1029), (1702, 1029), (1726, 1180), (1733, 1298), (1736, 1302),
                          (1758, 1302), (1758, 1337), (1598, 1337), (1580, 1150)],
                  seeds=[(1588, 1035), (1698, 1035), (1715, 1200), (1590, 1200), (1755, 1320)],
                  keep=(1640, 1200), box=(1470, 1029, 1860, 1420),
                  cover=[(1556, 970), (1712, 970), (1712, 1029), (1556, 1029)]),
    "paddle": dict(kind="stiff", amp=10.0, phase=6, pivot=(2008, 897), ball=20.4, under=16,
                   region=[(1848, 498), (2050, 498), (2050, 690), (2034, 700), (2040, 860), (2008, 897),
                           (1980, 905), (1900, 862), (1848, 760)],
                   seeds=[(1852, 502), (2046, 502), (1852, 755), (2030, 860)], keep=(1947, 600)),
}

# The drawing's seven colours: white, three greys for the edges, black, the paddle's red and a
# light red for its rim.
RED = (200, 40, 45)
COLOURS = [(255, 255, 255), (191, 191, 191), (128, 128, 128), (64, 64, 64), (0, 0, 0), RED, (228, 150, 152)]


def polygon_mask(size: tuple[int, int], points) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).polygon(points, fill=255)
    return mask


def disc(size: tuple[int, int], centre: tuple[int, int], r: float) -> Image.Image:
    mask = Image.new("L", size, 0)
    cx, cy = centre
    ImageDraw.Draw(mask).ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
    return mask


def silhouette(img: Image.Image, inside: Image.Image, seeds, keep) -> Image.Image:
    """A part's lines and what they enclose: the region minus the white reached from the seeds,
    then only the piece that holds `keep`, so a stray speck nearby does not travel along."""
    lum = img.convert("L").point(lambda v: 255 if v > 200 else 0)
    work = Image.composite(lum, Image.new("L", img.size, 128), inside)
    for seed in seeds:
        if work.getpixel(seed) == 100:
            continue
        if work.getpixel(seed) != 255:
            raise SystemExit(f"error: seed {seed} is not white; the drawing has changed")
        ImageDraw.floodfill(work, seed, 100)
    sil = ImageChops.subtract(inside, work.point(lambda v: 255 if v == 100 else 0))
    if sil.getpixel(keep) != 255:
        raise SystemExit(f"error: {keep} is not on the part; the drawing has changed")
    ImageDraw.floodfill(sil, keep, 254)
    return sil.point(lambda v: 255 if v == 254 else 0)


def strip_from_m(a: Image.Image, m: Image.Image) -> Image.Image:
    out = a.copy()
    for box in STRIP_BOXES:
        diff = ImageChops.difference(a.crop(box), m.crop(box)).convert("L").point(lambda v: 255 if v > 90 else 0)
        grown = diff.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.MaxFilter(21))
        out.paste(m.crop(box), box[:2], grown)
    return out


def height_at(points, x: float) -> float:
    """The y of a polyline, given left to right, at x; level beyond its ends."""
    if x <= points[0][0]:
        return points[0][1]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y1
    return points[-1][1]


def smoothstep(t: float) -> float:
    t = min(max(t, 0.0), 1.0)
    return t * t * (3 - 2 * t)


def bend(layer: Image.Image, box, pivot, angle_at) -> Image.Image:
    """Every pixel of box taken from the layer turned about pivot by angle_at(x, y) degrees."""
    x0, y0, x1, y1 = box
    src = layer.load()
    width, height = layer.size
    out = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    dst = out.load()
    px, py = pivot
    for y in range(y0, y1):
        for x in range(x0, x1):
            a = math.radians(angle_at(x, y))
            c, s = math.cos(a), math.sin(a)
            # Where did this pixel come from? Turn it back.
            sx = px + c * (x - px) - s * (y - py)
            sy = py + s * (x - px) + c * (y - py)
            ix, iy = math.floor(sx), math.floor(sy)
            if ix < 0 or iy < 0 or ix + 1 >= width or iy + 1 >= height:
                continue
            fx, fy = sx - ix, sy - iy
            near = (src[ix, iy], src[ix + 1, iy], src[ix, iy + 1], src[ix + 1, iy + 1])
            weights = ((1 - fx) * (1 - fy), fx * (1 - fy), (1 - fx) * fy, fx * fy)
            alpha = sum(p[3] * w for p, w in zip(near, weights))
            if alpha <= 0:
                continue
            # Weighted by alpha, so an edge takes no colour from outside the part.
            rgb = [sum(p[i] * p[3] * w for p, w in zip(near, weights)) / alpha for i in range(3)]
            dst[x, y] = (round(rgb[0]), round(rgb[1]), round(rgb[2]), round(alpha))
    return out


def seven_colours(frame: Image.Image) -> Image.Image:
    """Near-white to white and near-black to black, then the drawing's palette without dithering;
    a pixel keeps its colour where it is clearly red."""
    rgb = frame.convert("RGB")
    lum = rgb.convert("L").point(lambda v: 255 if v > 225 else (0 if v < 60 else v))
    red = rgb.convert("HSV").getchannel("S").point(lambda s: 255 if s > 90 else 0)
    snapped = Image.composite(rgb, Image.merge("RGB", (lum, lum, lum)), red)
    palette = Image.new("P", (1, 1))
    flat = [c for colour in COLOURS for c in colour]
    palette.putpalette(flat + [0] * (768 - len(flat)))
    return snapped.quantize(palette=palette, dither=Image.Dither.NONE)


def make_frames(count: int) -> list[Image.Image]:
    base = strip_from_m(
        Image.open(POSE_A, formats=DRAWING_FORMATS).convert("RGB"),
        Image.open(POSE_M, formats=DRAWING_FORMATS).convert("RGB"),
    )
    size = base.size
    silhouettes, covers = {}, {}
    for name, part in PARTS.items():
        inside = polygon_mask(size, part["region"])
        if part["kind"] == "stiff":
            # The forearm runs on under the ball's ring, which is laid over it again.
            inside = ImageChops.subtract(inside, disc(size, part["pivot"], part["under"]))
            covers[name] = disc(size, part["pivot"], part["ball"])
        else:
            covers[name] = polygon_mask(size, part["cover"])
        silhouettes[name] = silhouette(base, inside, part["seeds"], part["keep"])

    plate = base.copy()
    for mask in silhouettes.values():
        plate.paste((255, 255, 255), mask=mask)
    ImageDraw.Draw(plate).line(HIDDEN_OUTLINE, fill=(0, 0, 0), width=7, joint="curve")
    layers = {name: Image.merge("RGBA", (*base.split(), silhouettes[name])) for name in PARTS}

    def turn(name: str, theta: float):
        part = PARTS[name]
        if name == "man":
            return lambda x, y: theta * smoothstep((height_at(CUFF_TOP, x) - y) / part["ramp"])
        top, end = part["span"]
        return lambda x, y: theta * min(max((y - top) / (end - top), 0.0), 1.0) ** 1.2

    frames = []
    for t in range(count):
        canvas = plate.convert("RGBA")
        for name, part in PARTS.items():
            theta = part["amp"] * math.sin(2 * math.pi * (t + part["phase"] * count / 8) / count)
            if part["kind"] == "stiff":
                moved = layers[name].rotate(theta, resample=Image.Resampling.BICUBIC, center=part["pivot"])
            else:
                moved = bend(layers[name], part["box"], part["pivot"], turn(name, theta))
            canvas.alpha_composite(moved)
        canvas = canvas.convert("RGB")
        for mask in covers.values():
            canvas.paste(base, mask=mask)
        frames.append(seven_colours(canvas))
    return frames


def main() -> None:
    parser = argparse.ArgumentParser(description="Make the goodbye GIF of slide 8.3.")
    parser.add_argument("--frames", type=int, default=8, help="frames in one wave (default 8)")
    parser.add_argument("--ms", type=int, default=90, help="time on screen per frame (default 90)")
    parser.add_argument("--output", type=Path, default=TARGET, help="where to write the GIF")
    args = parser.parse_args()

    frames = make_frames(args.frames)
    # Disposal 2 makes Pillow write every frame whole; nothing in it is transparent.
    frames[0].save(args.output, save_all=True, append_images=frames[1:], duration=args.ms, loop=0,
                   disposal=2, optimize=False)
    shown = args.output.relative_to(REPO) if REPO in args.output.resolve().parents else args.output
    print(f"wrote {shown}: {len(frames)} frames of {args.ms} ms, {args.output.stat().st_size / 1e3:.0f} KB")


if __name__ == "__main__":
    main()
