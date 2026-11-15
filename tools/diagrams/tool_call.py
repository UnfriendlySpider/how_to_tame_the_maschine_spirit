"""Chapter 4: one tool call, in the order Claude Code checks it, drawn large
to take the place of the chapter's pair of talk drawings (2026-10-26). The
cast is the talk's, redrawn in the Excalidraw look: the guard on the hook,
the programmer on the prompt, the worker where the tool runs. Canvas 1480 by
560 units, printed at the full text width, so 24 units of text print at
about 7.5 pt. Usage: tool_call.py out.json (README.md in this folder)."""
import json, sys
from dia_common import Diagram, HOLD, READ, RED

W, H = 1480, 560
d = Diagram(W, H)

# the model, with the CLAUDE.md rule it reads
d.rect("model", 0, 178, 60, 550, roundness={"type": 3})
d.lines("mt", 14, 72, ["Claude,", "the model:"], 26, 32)
d.lines("ms", 14, 150, ["can only", "be asked"], 24, 30)
d.rect("rule", 10, 170, 382, 540, **READ)
d.lines("rt", 18, 388, [("", "CLAUDE.md", ":"), "never write", ("to ", "prod/"), "checks", "nothing"], 24, 29)

# the program
d.rect("prog", 190, 1472, 60, 550, strokeWidth=4)
d.text("progt", 204, 14, "Claude Code, the program", 28)
d.path("call", [(178, 318), (296, 318)])
d.lines("ct", 204, 254, ["a tool", "call"], 24, 28)

# 1 the hook, with the guard on it
d.figure("guard", "security", 376, 84, 206)
d.rect("b1", 296, 548, 290, 460, strokeWidth=3, **HOLD)
d.lines("b1t", 308, 300, [("1  ", "PreToolUse"), "hook: reads the", ("whole call as ", "JSON"), ("e.g. refuses ", "prod/")], 24, 34)
d.path("y1", [(548, 375), (590, 375)])

# 2 permission rules
d.rect("b2", 590, 846, 290, 460, strokeWidth=3, **HOLD)
d.lines("b2t", 602, 300, ["2  permission rules", ("paths: ", "Edit", ", ", "Read"), ("commands:  ", "Bash"),
                          "e.g. deny", ("", "Edit(/prod/**)")], 24, 31)
d.path("y2", [(846, 410), (932, 410)])
d.lines("y2t", 852, 338, ["ask or", "no rule"], 21, 27)
# allow: over the programmer's head, straight to the tool (straight segments:
# the exporter draws a path of more than two points as a curve)
d.path("allow1", [(816, 290), (816, 76)], head=None)
d.path("allow2", [(816, 76), (1262, 76)], head=None)
d.path("allow3", [(1262, 76), (1262, 290)])
d.text("allowt", 826, 180, "allow", 24)

# 3 you or the mode, with the programmer on it
d.figure("you", "programmer", 1020, 98, 192)
d.rect("b3", 932, 1192, 290, 460, strokeWidth=2)
d.lines("b3t", 944, 300, ["3  you or the mode", "ask rule or manual", "mode: asks you", "auto mode: the",
                          "classifier checks"], 24, 31)
d.path("y3", [(1192, 335), (1230, 335)])

# the worker, and the tool it runs
d.figure("worker", "worker", 1336, 106, 184)
d.rect("run", 1230, 1462, 290, 375, strokeWidth=2)
d.lines("runt", 1244, 298, ["the tool runs:", "the file changes"], 24, 32)
d.path("r4", [(1346, 375), (1346, 400)])
d.rect("b4", 1230, 1462, 400, 535, strokeWidth=2)
d.lines("b4t", 1244, 408, [("4  ", "PostToolUse"), "hook: runs after", "it, too late to", "stop the call"], 24, 31)

# no: stopped before the tool runs
for id, x, lab in [("n1", 422, "exit 2"), ("n2", 718, "deny"), ("n3", 1062, "no")]:
    d.path(id, [(x, 460), (x, 495)], strokeColor=RED, strokeWidth=3)
    d.text(id + "t", x + 10, 462, lab, 24, strokeColor=RED)
d.rect("stop", 296, 1192, 495, 535, strokeColor=RED, strokeWidth=2)
d.text("stopt", 610, 500, "stopped before it runs", 24, strokeColor=RED)

json.dump(d.E, open(sys.argv[1], "w"), indent=1)
