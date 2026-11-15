"""Chapter 9: the lethal trifecta as a path, with the control on each leg and
the talk's cast: the planted letter is outside text, the reviewer is the
subagent that reads it, the worker is Claude Code in its closed environment.
Dashed grey is outside text, shaded holds whatever the model decides, a red
cross closes a way. Canvas 1640 by 400 units at the template's 40 mm.
Usage: trifecta.py out.json (README.md in this folder)."""
import json, sys
from dia_common import Diagram, HOLD, READ, RED

d = Diagram()
WALL = dict(strokeWidth=4, **HOLD)


def cross(id, x, y, r=18):
    """A red X centred on (x, y): the path is closed here."""
    d.path(id + "a", [(x - r, y - r), (x + r, y + r)], head=None, strokeWidth=4, strokeColor=RED)
    d.path(id + "b", [(x + r, y - r), (x - r, y + r)], head=None, strokeWidth=4, strokeColor=RED)


# 1 outside text, two kinds, each with its control
d.text("h1", 8, 4, "1  Outside text", 28)
d.rect("l1", 8, 300, 56, 200, **READ)
d.lines("l1t", 22, 72, ["a web page,", "a PDF,", "a vendor note"], 24, 34)
d.figure("letter", "letter", 224, 60, 138)
d.rect("l2", 8, 300, 222, 392, **READ)
d.lines("l2t", 22, 236, ["a repository you did", "not write, a package,", "an MCP server,", "a plugin, a skill"], 24, 34)
d.rect("g1", 340, 660, 56, 200, **WALL)
d.lines("g1t", 354, 68, ["a subagent", "reads it, with no", "shell, web, write", "or MCP tools"], 24, 32)
d.figure("reviewer", "reviewer", 594, 60, 138)
d.rect("g2", 340, 660, 222, 392, **WALL)
d.lines("g2t", 354, 236, [("read ", ".claude/", " and"), ("", ".mcp.json", " first,"), "commit the lockfile,",
                          "pin each version"], 24, 34)
d.path("a1", [(300, 128), (340, 128)])
d.path("a2", [(300, 307), (340, 307)])

# the worker inside the closed environment (the wall is a control too)
d.rect("wall", 810, 1080, 40, 300, **WALL)
d.rect("room", 828, 1062, 58, 282, backgroundColor="#ffffff", fillStyle="solid", strokeWidth=1)
d.text("wallt", 826, 18, "closed environment", 26, bg=8)
d.text("wallc", 902, 62, "(chapter 8)", 24)
d.figure("worker", "worker", 906, 92, 150)
d.text("workert", 880, 246, "Claude Code", 24)
d.path("a3", [(660, 128), (900, 155)])
d.lines("a3t", 680, 26, ["its report", "is outside", "text too"], 24, 26)
d.path("a4", [(660, 307), (900, 205)])

# 2 private data, kept outside the wall
d.rect("p", 810, 1080, 324, 394)
d.lines("pt", 826, 330, ["2  Private data:", "keys, real data"], 24, 30)
d.path("a5", [(945, 278), (945, 322)], strokeStyle="dashed")
cross("x1", 945, 302, 16)

# 3 a way out, with its controls; both doors are closed
d.rect("g3a", 1120, 1410, 56, 150, **WALL)
d.lines("g3at", 1134, 62, ["deny rules for", ("", "WebFetch", " and"), "MCP tools that post"], 24, 28)
d.rect("g3b", 1120, 1410, 166, 340, **WALL)
d.lines("g3bt", 1134, 176, ["sandbox for commands", ("such as  ", "curl", ":"), "no allowed domains,",
                            ("", "strictAllowlist", " on,"), "no retries outside it"], 24, 30)
d.path("a6", [(990, 150), (1120, 103)])
d.path("a7", [(990, 200), (1120, 253)])
d.rect("r", 1460, 1632, 80, 330)
d.text("h3", 1472, 90, "3  Way out", 24)
d.lines("rt", 1472, 134, ["the network,", ("", "git push", ","), "an MCP tool", "that posts"], 24, 34)
d.path("a8", [(1410, 103), (1460, 103)], strokeColor=RED, strokeWidth=3)
d.path("a9", [(1410, 253), (1460, 253)], strokeColor=RED, strokeWidth=3)
cross("x2", 1432, 103, 12)
cross("x3", 1432, 253, 12)

# legend
d.rect("leg", 1120, 1160, 356, 388, **WALL)
d.text("legt", 1172, 358, "holds whatever the model decides", 24)

json.dump(d.E, open(sys.argv[1], "w"), indent=1)
