#!/usr/bin/env python3
"""Make the moving pictures of 7b.1, 7c.1 and 7c.2: what the worker reads, in flight.

Run with:

    uv run python tools/flying_sheets.py            # all three
    uv run python tools/flying_sheets.py 7c.2       # one of them
    uv run python tools/flying_sheets.py --ms 90    # a slower flight

Like tools/goodbye_wave.py, it turns drawings into frames and draws nothing by hand but the
speed lines. Each scene has a plate, its picture with the flying things taken off, and a
sprite, one of them cut out, both in slides/studies/ (anim-05 to anim-07; slides/image-prompts.md,
image 33, says how they were made). The sprite is set back along a smooth path through the
places where the drawing had its sheets, turned and sized as they were there, with a few
speed lines behind it. In each frame every sprite moves an eighth of the way to the next place,
so eight frames loop without a seam: a sprite fades in where the stream starts and fades out
where it ends, as the next one takes its place.

- 7b.1: the stream leaves the worker's antenna, passes in front of the open casement and goes
  out into the dark, each sheet smaller than the last. The deck shows the GIF; the paper keeps
  the drawing, slides/beats/beat-07b-isolation-1.jpg.
- 7c.1: the Book of Secrets rises out of the lit basement window, tumbles over the yard and
  lands upright in the warehouse's cabinet, behind the edge of its door, where the plate keeps
  one standing (since 2026-10-28, the author's request; black sheets flew there before).
- 7c.2: the white folders rise out of the office's lit window and land on the warehouse's top
  shelf.

For 7c.1 and 7c.2 one frame is also saved as the still the paper shows, one where a sprite is
just leaving the window, so the still's trail starts at the window too. Every pixel brighter than 245 in all three channels is set to pure
white, as the image sheet asks, and the frames share one palette, so nothing flickers.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

REPO = Path(__file__).resolve().parent.parent
STUDIES = REPO / "slides" / "studies"
BEATS = REPO / "slides" / "beats"
DRAWING_FORMATS = ("PNG", "JPEG")   # what the drawings are; Pillow would otherwise read any format

# Everything below is in pixels of the 2752 x 1536 drawings.


@dataclass
class Scene:
    plate: str                  # the picture without the flying things
    sprite: str                 # one of them, cut out with its own alpha
    sprite_turn: float          # how far the sprite is turned in the drawing it was cut from
    start: tuple                # where the stream comes from
    places: list                # (x, y, turn, size) where the drawing had its sheets, in order
    end: tuple | None           # (x, y, turn, size) where a sprite disappears, or None: it lands
                                # on the last place, which the plate keeps drawn
    start_size: float = 0.25    # the sprite's size where it appears, against the sprite
    fade_in: float = 0.5        # how far, in steps, a sprite takes to appear
    trail: tuple = (3, 4.0, 15.0, 0.30, 0.68)   # strokes, width, spacing, from and to (in steps back)
    occluder: list = field(default_factory=list)   # a polygon the sprites pass behind
    target: str = ""            # the GIF, without its extension
    still: int | None = None    # the frame also saved as the picture's JPEG: one with a sprite
                                # just leaving the window, so the still shows where they come from


SCENES = {
    "7b.1": Scene(
        plate="anim-07-stream-7b1-plate.png", sprite="anim-07-stream-7b1-sprite.png", sprite_turn=0.0,
        start=(1733.0, 668.0),
        places=[(1857.3, 615.6, -96, 1.55), (1966.2, 561.3, -70, 1.29), (1999.0, 466.7, 0, 1.0),
                (1951.4, 385.8, 34, 0.80), (1943.2, 327.2, 60, 0.67), (1800.0, 352.0, 70, 0.6),
                (1685.6, 401.3, 90, 0.52), (1702.5, 354.2, 110, 0.36)],
        end=(1712.0, 318.0, 130, 0.05), start_size=0.3,
        trail=(2, 3.0, 9.0, 0.32, 0.58),
        # The sheets pass in front of the open casement, which is swung into the room, and on
        # into the dark (the author's request, 2026-10-20: behind it they looked odd).
        target="beat-07b-isolation-1"),
    "7c.1": Scene(
        # The book is cut from 1.1, where it leans 14 degrees, so it stands upright where it lands.
        plate="anim-05-book-7c1-plate.png", sprite="anim-05-book-7c1-sprite.png", sprite_turn=-14.6,
        start=(441.0, 1280.0),       # inside the open basement window's lit arch, below its bulb
        places=[(506.0, 1154.0, -138.6, 1), (564.0, 1000.6, -133.0, 1), (646.9, 794.0, -133.1, 1),
                (733.1, 622.0, -127.6, 1), (824.2, 481.3, -122.6, 1), (927.0, 362.3, -111.7, 1),
                (1102.7, 242.4, -96.4, 1), (1253.7, 201.4, -73.8, 1), (1394.3, 210.7, -56.6, 1),
                (1524.9, 259.9, -45.9, 1), (1626.7, 324.5, -32.9, 1), (1716.6, 406.8, -25.3, 1),
                (1803.6, 513.4, -13.0, 1), (1877.4, 633.3, -5.8, 1), (1937.9, 758.8, -1.9, 1),
                (1986.4, 888.6, -0.6, 0.85), (2011.5, 1006.3, -0.6, 0.7)],
        end=None, start_size=0.25, fade_in=0.15,
        trail=(3, 4.0, 15.0, 0.30, 0.68),
        occluder=[(2029, 944), (2160, 925), (2160, 1345), (2029, 1345)],   # the cabinet's right door
        target="beat-07c-data-1", still=3),
    "7c.2": Scene(
        plate="anim-06-folders-7c2-plate.png", sprite="anim-06-folders-7c2-sprite.png", sprite_turn=0.0,
        start=(1355.0, 1140.0),      # the office's lit window
        places=[(1447.8, 862.0, 60, 1.0), (1570.4, 707.2, 38, 1.0), (1745.4, 652.6, 0, 1.0),
                (1905.7, 742.8, -32, 0.92), (1994.7, 902.5, -42, 0.86)],
        end=(1998.0, 1006.0, 0, 0.32), start_size=0.3, fade_in=0.3,
        trail=(3, 3.0, 13.0, 0.30, 0.66),
        target="beat-07c-data-2", still=2),
}

FRAMES = 8
SS = 2   # the speed lines are drawn at this multiple of the size, then scaled down


def smooth(t: float) -> float:
    t = min(max(t, 0.0), 1.0)
    return t * t * (3 - 2 * t)


class Path_:
    """A Catmull-Rom curve through the start, the places and the end; u = -1 at the start,
    u = k at place k, and u = len(places) at the end (if there is one)."""

    def __init__(self, scene: Scene) -> None:
        pts = [scene.start] + [p[:2] for p in scene.places] + ([scene.end[:2]] if scene.end else [])
        self.n = len(pts) - 1                 # steps from the start to the last point
        first = (2 * pts[0][0] - pts[1][0], 2 * pts[0][1] - pts[1][1])
        last = (2 * pts[-1][0] - pts[-2][0], 2 * pts[-1][1] - pts[-2][1])
        self.pts = [first] + pts + [last]
        turns = [scene.places[0][2]] + [p[2] for p in scene.places] + ([scene.end[2]] if scene.end else [])
        sizes = [scene.start_size] + [p[3] for p in scene.places] + ([scene.end[3]] if scene.end else [])
        self.turns, self.sizes = turns, sizes

    def at(self, u: float) -> tuple[float, float]:
        s = min(max(u + 1, 0.0), float(self.n))
        k = min(int(s), self.n - 1)
        t = s - k
        p0, p1, p2, p3 = self.pts[k], self.pts[k + 1], self.pts[k + 2], self.pts[k + 3]

        def cr(a, b, c, d):
            return 0.5 * (2 * b + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t * t + (-a + 3 * b - 3 * c + d) * t ** 3)
        return cr(p0[0], p1[0], p2[0], p3[0]), cr(p0[1], p1[1], p2[1], p3[1])

    def lerp(self, values: list, u: float) -> float:
        s = min(max(u + 1, 0.0), float(self.n))
        k = min(int(s), self.n - 1)
        t = smooth(s - k)
        return values[k] * (1 - t) + values[k + 1] * t

    def tangent(self, u: float) -> tuple[float, float]:
        a, b = self.at(u - 0.02), self.at(u + 0.02)
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy) or 1.0
        return dx / n, dy / n


def frame(scene: Scene, path: Path_, plate: Image.Image, sprite: Image.Image, cover: Image.Image | None,
          f: int) -> Image.Image:
    """Frame f: the plate, the speed lines and every sprite in flight."""
    w, h = plate.size
    canvas = plate.copy()
    strokes, width, spacing, back0, back1 = scene.trail
    ink = Image.new("L", (w * SS, h * SS), 0)
    draw = ImageDraw.Draw(ink)
    flights = []
    last = path.n - 1                                     # u of the last point
    for i in range(-1, last):
        u = i + f / FRAMES
        size = path.lerp(path.sizes, u)
        turn = path.lerp(path.turns, u)
        fade = smooth((u + 1) / scene.fade_in)            # in, out of the start
        # out, at the end; a landing sprite only in its last steps, onto the sheet drawn there
        span = 0.6 if scene.end else 0.3
        fade *= 1 - smooth((u - (last - span)) / span)
        flights.append((u, size, turn, fade))
        # the speed lines behind it, never back into the window or the antenna it came from
        hi, lo = u - back0, max(u - back1, -0.45)
        if size * fade > 0.55 and hi - lo > 0.12:
            for s in range(strokes):
                off = (s - (strokes - 1) / 2) * spacing * size
                pts = []
                for k in range(9):
                    uu = hi - (hi - lo) * k / 8
                    px, py = path.at(uu)
                    tx, ty = path.tangent(uu)
                    pts.append(((px - ty * off) * SS, (py + tx * off) * SS))
                draw.line(pts, fill=int(255 * fade), width=int(round(width * SS)), joint="curve")
    lines = ink.resize((w, h), Image.LANCZOS)
    if cover is not None:
        lines = ImageChops.subtract(lines, cover)
    canvas.paste((0, 0, 0), (0, 0), lines)
    for u, size, turn, fade in flights:
        if fade <= 0.01:
            continue
        x, y = path.at(u)
        piece = sprite.rotate(turn - scene.sprite_turn, resample=Image.BICUBIC, expand=True)
        pw, ph = max(1, round(piece.width * size)), max(1, round(piece.height * size))
        piece = piece.resize((pw, ph), Image.LANCZOS)
        box = (round(x - pw / 2), round(y - ph / 2), round(x - pw / 2) + pw, round(y - ph / 2) + ph)
        alpha = piece.getchannel("A").point(lambda a: int(a * fade))
        if cover is not None:
            alpha = ImageChops.subtract(alpha, cover.crop(box))
        canvas.paste(Image.composite(piece.convert("RGB"), canvas.crop(box), alpha), box[:2])
    return whiten(canvas)


def whiten(img: Image.Image) -> Image.Image:
    """Every pixel brighter than 245 in all three channels becomes pure white, as the sheet asks."""
    r, g, b = img.split()
    bright = ImageChops.multiply(ImageChops.multiply(r.point(lambda v: 255 if v > 245 else 0),
                                                     g.point(lambda v: 255 if v > 245 else 0)),
                                 b.point(lambda v: 255 if v > 245 else 0))
    out = img.copy()
    out.paste((255, 255, 255), (0, 0), bright)
    return out


def palette_for(img: Image.Image) -> Image.Image:
    """One palette for every frame: a ramp of greys, and the drawing's own colours if it has any,
    the red of the seal and the paddle or the yellow of a lit window. An adaptive palette of the
    whole frame folds those few pixels into a dull brown, so they are collected on their own."""
    r, g, b = img.split()
    chroma = ImageChops.subtract(ImageChops.lighter(r, ImageChops.lighter(g, b)),
                                 ImageChops.darker(r, ImageChops.darker(g, b)))
    coloured = chroma.point(lambda v: 255 if v > 40 else 0)
    colours = [(v, v, v) for v in range(0, 256, 8)] + [(255, 255, 255)]
    box = coloured.getbbox()
    if box:
        tints = Image.new("RGB", (box[2] - box[0], box[3] - box[1]), (255, 255, 255))
        tints.paste(img.crop(box), (0, 0), coloured.crop(box))
        flat = tints.quantize(colors=48, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).getpalette()
        colours += [tuple(flat[i:i + 3]) for i in range(0, 48 * 3, 3)]
    pal = Image.new("P", (1, 1))
    pal.putpalette([c for rgb in colours for c in rgb] + [0] * (768 - 3 * len(colours)))
    return pal


def make(name: str, ms: int) -> None:
    scene = SCENES[name]
    plate = Image.open(STUDIES / scene.plate, formats=DRAWING_FORMATS).convert("RGB")
    sprite = Image.open(STUDIES / scene.sprite, formats=DRAWING_FORMATS).convert("RGBA")
    cover = None
    if scene.occluder:
        cover = Image.new("L", plate.size, 0)
        ImageDraw.Draw(cover).polygon(scene.occluder, fill=255)
    path = Path_(scene)
    frames = [frame(scene, path, plate, sprite, cover, f) for f in range(FRAMES)]
    if scene.still is not None:
        # The loop starts on the still, so a viewer that shows only the first frame, a PDF of
        # the deck among them, shows the same picture as the paper.
        frames = frames[scene.still:] + frames[:scene.still]
    palette = palette_for(frames[0])
    gif = [fr.quantize(palette=palette, dither=Image.Dither.NONE) for fr in frames]
    target = BEATS / f"{scene.target}.gif"
    gif[0].save(target, save_all=True, append_images=gif[1:], duration=ms, loop=0, disposal=2, optimize=False)
    print(f"wrote {target.relative_to(REPO)}: {FRAMES} frames of {ms} ms, {target.stat().st_size // 1024} KB")
    if scene.still is not None:
        still = BEATS / f"{scene.target}.jpg"
        frames[0].save(still, "JPEG", quality=90, subsampling=0, optimize=True)
        print(f"wrote {still.relative_to(REPO)}: frame {scene.still}, the still the paper shows")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("scenes", nargs="*", metavar="SLIDE", help=f"which pictures: {', '.join(SCENES)} (default: all)")
    parser.add_argument("--ms", type=int, default=70, help="milliseconds per frame (default 70)")
    args = parser.parse_args()
    unknown = [s for s in args.scenes if s not in SCENES]
    if unknown:
        parser.error(f"no moving picture for {', '.join(unknown)}; there are {', '.join(SCENES)}")
    for name in args.scenes or SCENES:
        make(name, args.ms)


if __name__ == "__main__":
    main()
