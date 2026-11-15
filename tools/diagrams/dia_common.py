"""Shared helpers for the paper's Excalidraw diagrams. A diagram is a list of
elements in the Excalidraw MCP's simplified format; export.mjs turns it into
a .excalidraw file and a PNG (README.md in this folder)."""
from pathlib import Path
FONT, CODE = 1, 3
GREEN, GREY, RED = "#d4f0e0", "#e9ecef", "#c92a2a"   # GREEN: Evidenze green #27b564 at 20%
HOLD = dict(backgroundColor=GREEN, fillStyle="solid")
READ = dict(strokeStyle="dashed", backgroundColor=GREY, fillStyle="solid", strokeWidth=2)
# the talk's cast, redrawn in the Excalidraw look (slides/image-prompts.md, image 46)
CAST = str(Path(__file__).resolve().parent / "cast") + "/"


class Diagram:
    def __init__(self, w=1640, h=400):
        self.E = []
        self.rect("frame", 0, w, 0, h, strokeColor="transparent", backgroundColor="#ffffff",
                  strokeWidth=1, roughness=0)

    def rect(self, id, x0, x1, y0, y1, **kw):
        self.E.append({"type": "rectangle", "id": id, "x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0, **kw})

    def text(self, id, x, y, s, size=24, family=None, **kw):
        self.E.append({"type": "text", "id": id, "x": x, "y": y, "text": s, "fontSize": size,
                       "fontFamily": family or FONT, **kw})

    def path(self, id, pts, head="arrow", **kw):
        x0, y0 = pts[0]
        self.E.append({"type": "arrow", "id": id, "x": x0, "y": y0, "width": pts[-1][0] - x0,
                       "height": pts[-1][1] - y0, "points": [[x - x0, y - y0] for x, y in pts],
                       "endArrowhead": head, "startArrowhead": None, **kw})

    def lines(self, prefix, x, y, rows, size=24, step=28, **kw):
        """Rows of text; a tuple alternates hand-written and code parts."""
        for i, r in enumerate(rows):
            parts = r if isinstance(r, tuple) else (r,)
            cx = x
            for j, part in enumerate(parts):
                fam = CODE if j % 2 else FONT
                if part:
                    self.text(f"{prefix}{i}_{j}", cx, y + i * step, part, size, fam, **kw)
                cx += len(part) * (size * (0.6 if fam == CODE else 0.5))

    def figure(self, id, who, x, y, height):
        """A member of the talk's cast: worker, reviewer, security, letter or programmer."""
        self.E.append({"type": "image", "id": id, "x": x, "y": y, "height": height, "src": CAST + who + ".png"})
