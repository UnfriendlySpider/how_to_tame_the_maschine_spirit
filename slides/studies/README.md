# Style study: black and white

On 2026-10-07 the author asked for a different look for the talk's images:
black-and-white drawings, minimalist, a little more than stick figures, on a
completely white background, with a light touch of the tech priest who tends
the machine spirit. The talk's title already speaks of the machine spirit;
the images should nod, very lightly, to its priests.
The priest is the figure the author identifies with.

This folder holds three rounds of tries from that day. Round 1 tried the
direction; the author then chose the clean line and asked for Steve to change
over the talk, from a man who prays for his machines to one who has them
under control. Round 2 worked that out, and the author chose from it the
same day; round 3 put the chosen face into two scenes. `../storyline.md` now
describes the chosen look, `../image-prompts.md` was rewritten from it the
same day, and the images in `../beats/` were made from that sheet. A section
from 2026-10-09 keeps the poses of the cast's goodbye, the talk's one
animation, and round 4, from 2026-10-12, tries Steve in his own clothes: he
puts the robe on for the machine and sheds it piece by piece.

## Round 1: the direction

### The files

| File | Shows | Made from |
|---|---|---|
| `bw-01-priest-levels.jpg` | the man three times, each a little more devoted: everyday clothes with a gear pendant and a candle; a hooded robe, hood down, a rope belt with tools, a gear on the chest and a censer; hood up, a mechanical arm holding a candle, a cable ending in a plug | prompt A alone; two samples, the first kept |
| `bw-02-cast-clean-line.jpg` | the cast sheet in a clean line: the man in the robe of level 2, the worker, the reviewer and the gatekeeper, whose paddle is the only colour | prompt B alone; two samples, the first kept (the second gave the gatekeeper a second arm) |
| `bw-03-scene-1-3.jpg` | slide 1.3: fingers crossed, a candle, a censer on a hook, the bulb, the worker switching on | prompt C with image 2 as reference; two samples, the first kept (its smoke drifts over the robot, and the man looks less cross) |
| `bw-04-scene-1-3-hood.jpg` | the same scene at level 3: hood up, a mechanical arm swings the censer over the robot | edit D of image 3 |
| `bw-05-title.jpg` | title slide 0.1: a house with black windows and one lit basement window with a pointed arch | prompt E with image 2 as reference for the style; two samples, the second kept (the first drew the window below the ground line, apart from the house) |
| `bw-06-cast-felt-tip.jpg` | the cast sheet of image 2 redrawn in a looser felt-tip line | edit F of image 2 |
| `bw-07-cast-doodle.jpg` | a doodle version of the cast, one figure each, with large round heads | prompt G alone |

### How they were made

Nano Banana 2.1 through fal, the model of `../image-prompts.md`:
`google/nano-banana-2.1` for a prompt alone and
`google/nano-banana-2.1/edit` with reference images, `aspect_ratio` `16:9`,
`resolution` `2K`, `output_format` `png`, `thinking_level` `high`. Eleven
images in all, about 0.90 US dollars at the price of 2026-10-06. A first,
longer wording of F, with two samples requested, returned no image, as a
long edit did for image 25 of the test run of 2026-10-06; the shorter
wording below worked. Each kept image was converted to JPEG (quality 90,
full colour resolution), as the beats are.

The prompts name no game, publisher or emblem. The flavour comes from
generic things (a hooded robe, a gear, a censer, candles, a mechanical arm,
a pointed window), so no third-party symbol can reach a slide.

Prompt A, the man at three levels:

```text
A character study for a minimalist comic, one clean drawing on a pure white background, landscape 16:9. The same man is drawn three times, standing side by side in one row on one thin black floor line, each facing the viewer, with plenty of white space between them. He is a statistical programmer who looks after his computers with the quiet devotion of a monk, and each figure shows a little more of that devotion.

The man in all three: slim, in his late thirties, round dark-rimmed glasses, short untidy dark hair, light stubble, a calm, sceptical expression with one eyebrow slightly raised.

Figure 1, the lightest touch: his everyday clothes, a knitted cardigan over a plain shirt and dark trousers; a small gear-shaped pendant hangs on a cord round his neck, and he holds a short lit candle in one hand.

Figure 2, a little more: a long, plain, hooded robe like a monk's, the hood down on his shoulders, belted with a simple rope from which hang a small screwdriver and a small spanner; a simple gear emblem on the chest; plain trainers peek out under the hem. In one hand he holds a small incense burner on a chain, a thin curl of smoke rising from it.

Figure 3, the strongest touch: the same hooded robe with the hood up, his face still clearly visible with the round glasses; a slim, jointed mechanical arm rises over one shoulder from a small backpack and holds a short lit candle above his head; a thin cable runs out of his sleeve and ends in a plug in his hand; the gear emblem on the chest.

Style: minimalist black ink line drawing, a little more than stick figures: simple shapes, a round head, dot eyes behind the round glasses, simple hands, drawn with as few lines as possible in one even line weight. Black and white only: black lines and a few small areas of solid black, everything else pure white. No grey, no shading, no gradients, no hatching, no colour. Plenty of empty white space. The drawing carries no text at all: no letters, numbers, labels, captions, logos or speech bubbles.
```

Prompt B, the cast sheet:

```text
A character model sheet for a minimalist comic, one clean drawing on a pure white background, landscape 16:9. Eight figures stand in one row on one thin black floor line, drawn at their true sizes relative to each other, with plenty of white space between them. From left to right:

Figures 1 and 2: the same man, once facing the viewer and once in a three-quarter view. Slim, in his late thirties, round dark-rimmed glasses, short untidy dark hair, light stubble. He wears a long, plain, hooded robe like a monk's, the hood down on his shoulders, belted with a simple rope from which hang a small screwdriver and a small spanner; a simple gear emblem on the chest; plain trainers under the hem. In the second view he holds a plain mug. He looks sceptical and alert, one eyebrow slightly raised.

Figures 3 and 4: the worker robot, once facing the viewer and once in a three-quarter view. It stands about as tall as the man's hip: the top of its head is level with his hip. A rounded box body with a solid black band round its chest; a square head with two round eyes set into its face and a short antenna; two thin jointed arms ending in two-finger grippers. Its body ends at the bottom in one single wheel: it rolls, and it has no legs and no feet.

Figures 5 and 6: the reviewer robot, once facing the viewer and once in a three-quarter view, a little smaller and slimmer than the worker robot. An egg shape with smooth, unbroken sides; nothing is attached to its sides. Its only eye is one large round lens. It wears the same solid black band round its middle and the same short antenna on top as the worker robot and glides on a hidden wheel. A narrow slot in its chest lets out one narrow strip of paper. It looks designed this way, not damaged.

Figures 7 and 8: the gatekeeper, once facing the viewer and once in a three-quarter view. A squat, faceless steel post whose top reaches the man's hip, bolted to the floor on a heavy base plate with big bolts. It wears a guard's peaked cap with a visor on top and has one round lamp on its front, and in both views one jointed arm holds up a round red paddle with a completely plain, blank face. A fixed installation, not a walking figure.

Style: minimalist black ink line drawing, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only, with one exception: the gatekeeper's paddle is red, the only colour in the picture. No grey, no shading, no gradients, no hatching. Plenty of empty white space. The sheet carries no text at all: no names, labels, numbers, arrows, captions, logos or speech bubbles; the paddle and the mug are blank.
```

Prompt C, slide 1.3 (its image 1 is `bw-02-cast-clean-line.jpg`):

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use image 1, the cast sheet, as the reference and match it exactly: its drawing style, the man in his hooded robe and the worker robot, at the sizes shown there. Draw only what this prompt names.

Evening. A plain wooden workbench, drawn in a few lines, stands in the middle of the picture on one thin floor line. The worker robot stands on the workbench next to a laptop whose screen faces away from us; its two round eyes are just switching on for the first time, shown by a few short lines radiating from them. Beside the robot, on the bench, burns a short candle in a small holder, and a small incense burner hangs from a hook at the end of the bench, a thin curl of smoke drifting over the robot. The man in his hooded robe leans towards the robot from the left, both hands raised in front of his chest with the fingers crossed, hopeful and a little sceptical. A bare light bulb hangs on its cord from the top edge of the picture.

Keep the robot, the man's crossed fingers and the candle inside the middle three quarters of the width.

Style: minimalist black ink line drawing in exactly the style of image 1, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching, no colour. The background is pure white: no walls and no room, nothing behind the figures except the hanging bulb. One single scene drawn edge to edge, no panels, no borders. No text anywhere: no letters, numbers, words, labels, logos, captions or speech bubbles.
```

Edit D, level 3 in the scene (its image 1 is `bw-03-scene-1-3.jpg`):

```text
Edit image 1. Keep the camera, the framing, the drawing style, the workbench, the laptop, the candle, the hanging bulb and the robot exactly as they are. Change only this:
1. The man now wears the hood of his robe up over his head; his face, with the round glasses, stays clearly visible inside the hood.
2. A slim jointed mechanical arm rises over his shoulder from a small pack on his back and holds the small incense burner on its chain above the robot, a thin curl of smoke drifting from it.
3. The hook and the incense burner at the end of the bench are gone.
4. He still crosses the fingers of both hands in front of his chest, hopeful and a little sceptical.
Everything else stays exactly as it is. Black and white only, pure white background, no grey and no shading. No text anywhere. Landscape 16:9.
```

Prompt E, title slide 0.1 (its image 1 is `bw-02-cast-clean-line.jpg`, for the style):

```text
Create a title picture for the same minimalist comic, in exactly the drawing style of image 1: black ink lines on a pure white background, landscape 16:9. Use image 1 only for the style; draw none of its characters.

A narrow two-storey brick house stands alone in the middle of the picture on one thin ground line, drawn in a few clean lines; a few bricks are hinted at with short strokes. It is night: every window of the house is filled with solid black. Only one window is lit: the small basement window just above the ground line, whose top is a pointed gothic arch like a tiny chapel window. It stays white inside, a small candle flame burns in it, and a few short lines radiate from it like a glow. Nobody is in the picture.

The picture is shown small on a white slide, so keep it simple and bold: the house reads as one clear shape and the lit basement window is the point the eye goes to. The sky and the ground are pure white: no stars, no moon, no clouds.

Style: minimalist black ink line drawing, a few areas of solid black, one even line weight. Black and white only: no grey, no shading, no gradients, no colour. One single scene, no panels, no borders. No text anywhere: no letters, numbers, house numbers, signs, logos or captions.
```

Edit F, the felt-tip line (its image 1 is `bw-02-cast-clean-line.jpg`):

```text
Redraw image 1 in a simpler, looser style, closer to stick figures but still a little more than stick figures: one slightly irregular black felt-tip line, plain round heads, dot eyes, thin arms and legs, small round hands, very few details. Keep the same eight figures in the same order and at the same sizes on the same floor line, and keep what identifies each one: the man's round glasses, untidy hair, hooded robe with the gear emblem and the rope belt; the robots' shapes, black bands, antennas, grippers, wheel, lens and paper strip; the gatekeeper's cap, post, bolted base and red round paddle. Pure white background, black and white except the red paddle. No text anywhere. Landscape 16:9.
```

Prompt G, the doodle:

```text
A character sheet for a minimalist comic drawn like quick felt-tip doodles: one slightly irregular black line on a pure white background, landscape 16:9, closer to stick figures but with a little more body. Four characters stand in one row on one thin floor line, with plenty of white space between them:
1. a slim man with a plain round head, untidy hair in a few strokes, round glasses drawn as two small circles round dot eyes, a short line for a mouth and one raised eyebrow, wearing a long hooded robe like a monk's, the hood down, a small gear emblem on the chest and a rope belt; plain trainers under the hem;
2. a small hip-high robot: a box body with a solid black band, a square head with two round eyes and a short antenna, two thin arms with two-finger grippers, one wheel and no legs;
3. a smaller egg-shaped robot with smooth, unbroken sides, one large round lens as its only eye, the same black band and antenna, a narrow paper strip coming from a slot in its chest;
4. a squat post bolted to the floor with big bolts, a guard's peaked cap on top, one round lamp on its front, and one thin arm holding up a round red paddle with a blank face.
Black and white only, except the red paddle; no grey, no shading, no hatching. No text anywhere: no names, labels, numbers, captions, logos or speech bubbles.
```

### What round 1 showed

- The model holds the style: black lines on white with no grey and no
  shading in the clean and the felt-tip line; only the doodle (7) adds
  hatching and a grey lens. None of the images carries lettering: the seven
  kept ones were checked at full size where models like to write (paper
  strips, paddles, laptop lids, emblems, cap badges), the other four at
  preview size.
- The robots and the gatekeeper carry over one to one. The purple band
  becomes a solid black band, which keeps the worker and the reviewer
  visibly of one make.
- Red as the only colour makes the paddle the first thing the eye finds.
  The wax seal of the production folder would be the second red object, and
  the rule "red means what must never change, and what guards it" reads
  more strongly than in the purple style.
- A white background takes the basement's walls away. The place is then
  told by a few objects: the workbench, the bulb, the pointed window of the
  title. `ref-basement.jpg` would become a plate of those objects.
- A preview deck (`tools/build_slides.py --images` with image 5 as the title
  picture and image 4 as slide 1.3) shows the pictures merging with the
  white ML04 slides, without a frame. Their background is near-white
  (252 to 255), and in the LibreOffice render of that deck the picture area
  sits one or two levels below the slide's pure white, which a good screen
  can show as a faint rectangle. Round 2 set near-white to white before
  saving; what that changed is noted there.
- The title picture is shown 4.3 inches wide, and there the house of
  image 5 is too small for its lit window to carry: the house should fill
  most of the frame's height.
- The censer reads as a small hanging scale in images 3 and 4; next time,
  "a censer with a domed, pierced lid on three chains".
- The man looks crosser than "sceptical" in the scenes; "hopeful" needs
  more weight in a scene prompt.
- The felt-tip redraw (6) lost the eyes behind the glasses; if that line is
  chosen, ask for dot eyes.

## Round 2: Steve's arc

### The author's choices after round 1

- The clean line of image 2.
- Steve changes over the talk, from a man who prays for his machines to one
  who has them under control.
- Steve looks like the author: no glasses, a small beard, very short hair, a
  medium build, not muscular.
- Accent colours, very sparingly; the red of the seal stays.
- The title house with its pointed basement window, worked out further.
- When the worker learns a skill, it gains an extra arm or a specialised
  variant of itself.

### The files

| File | Shows | Made from |
|---|---|---|
| `bw-08-steve-faces-cowl.jpg` | Steve six times in a robe with a cowl collar, hood down, each with another face and beard: a trimmed full beard, a full beard and moustache, a goatee, heavy stubble, a boxed beard, a chin beard | prompt H alone; two samples, both kept (8 and 9) |
| `bw-09-steve-faces-hood.jpg` | the same six faces with a plain hood instead of the cowl | the second sample of prompt H |
| `bw-10-steve-evolution.jpg` | Steve's arc in four stages, the beard solid black | prompt I alone; two samples, both kept (10 and 11) |
| `bw-11-steve-evolution-hatched.jpg` | the same four stages with a hatched beard | the second sample of prompt I |
| `bw-12-scene-1-3-praying.jpg` | slide 1.3 at the start of the arc: hood up, fingers crossed, the censer smoking over the robot | edit L of image 3 with image 10; two samples, the second kept (the gear on the robe shows) |
| `bw-13-scene-8-2-in-control.jpg` | slide 8.2 at the end of the arc, in the same frame: hood down, tea, the keys on his belt, the candle just blown out, the censer cold, the robot gone | edit M of image 3 with image 10; two samples, the second kept (he sits closer to the bench) |
| `bw-14-worker-skill-arm.jpg` | the worker plain, with an extra arm holding a magnifier before its eyes, and with a magnifier in place of a gripper; a rack of spare arms and tools | prompt N with image 2 as reference; two samples, the second kept (the first added a floating robot) |
| `bw-15-title-amber.jpg` | the title house filling the frame's height, the pointed basement window larger and amber, the only colour | edit O of image 5, then edit P of its result |

Round 2 also made images that were not kept: a first robot sheet (two
samples; one drew the old Steve beside the robots, the other's extra arm was
hard to read) and the amber title in a single edit, which added two lines
to the facade.

A1 to A6 are the faces of image 8 from left to right, B1 to B6 those of
image 9.

### Steve's arc, as proposed

| Stage | Slides | Steve | The worker |
|---|---|---|---|
| Praying | 0.1 to 1.3 | hood up; candle and censer lit; fingers crossed in 1.3 | plain, as on the cast sheet |
| Learning | 2.1 to 4.3 | hood down, sleeves pushed up, booklet and pencil; the censer hangs cold from his belt | in 3.2 an extra arm with a magnifier, taken from a rack for the review and put back afterwards |
| Organising | 5.1 to 7.2 | upright, clipboard and mug; the censer is gone | the reviewer joins as a second robot of the same make (5.3) |
| In control | 7b.3 to 8.2 | relaxed, tea in both hands, the ring of keys on his belt; in 8.2 the candle goes out | the badge on its lanyard (7b.3) |

The extra arm follows what the paper says of skills: a skill is loaded only
when it is called by name or fits the request, so the arm is clipped on for
the job and goes back on the rack. An arm that never comes off would rather
stand for `CLAUDE.md`, which is loaded in every session. The reviewer has
its review skill preloaded in full, which its one large lens can stand for.
The keys on Steve's belt from 7b.3 on show that they stay with him, out of
the worker's reach.

### How they were made

The same model and settings as round 1; fifteen images, about 1.20 US
dollars, so about 2.10 for both rounds. Before saving, every pixel whose
three channels are all above 245 was set to pure white, so the backgrounds
of files 8 to 15 are exactly white; round 1's files were saved as the model
delivered them.

Prompt H, six faces:

```text
A character study for a minimalist comic, one clean drawing on a pure white background, landscape 16:9. Six versions of the same kind of man stand side by side in one row on one thin black floor line, each facing the viewer, with plenty of white space between them, so that one of them can be chosen.

All six: a man in his late thirties with an ordinary, medium build, neither thin nor heavy and not muscular; no glasses; very short hair, almost a buzz cut; a small beard; a calm, sceptical expression with one eyebrow slightly raised. He wears a long, plain, hooded robe like a monk's, the hood down on his shoulders, belted with a simple rope, a simple gear emblem on the chest, plain trainers under the hem.

The six differ only in face and beard, from left to right:
1. an oval face with a short, neatly trimmed full beard;
2. a rounder face with a short full beard and moustache, a little fuller on the chin;
3. an angular face with a goatee: moustache and chin beard, bare cheeks;
4. an oval face with heavy stubble drawn as fine dots, a little denser on the chin;
5. a square face with a short boxed beard and a clean line along the cheeks;
6. a longer face with a short chin beard and no moustache.

Style: minimalist black ink line drawing, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black; the very short hair is a thin solid black cap close to the head. Black and white only: no grey, no shading, no gradients, no hatching, no colour. Plenty of empty white space. The drawing carries no text at all: no numbers, letters, labels, captions, logos or speech bubbles.
```

Prompt I, the arc:

```text
A character study for a minimalist comic, one clean drawing on a pure white background, landscape 16:9. The same man is drawn four times, side by side in one row on one thin black floor line, with plenty of white space between them. From left to right he changes, step by step, from a man who prays for his machines to a man who has them under control.

The man in all four: late thirties, an ordinary, medium build, neither thin nor heavy and not muscular; no glasses; very short hair, almost a buzz cut; a short, neatly trimmed full beard. He wears a long, plain, hooded robe like a monk's, belted with a simple rope, a simple gear emblem on the chest, plain trainers under the hem.

Figure 1, praying: the hood is up over his head, his face clearly visible inside it. He holds a short lit candle in one hand and, in the other, a small censer: a round metal bowl with a domed, pierced lid, hanging on three thin chains, a thin curl of smoke rising from it. His expression is hopeful and a little anxious.

Figure 2, learning: the hood is down on his shoulders. He has pushed up his sleeves and holds a slim booklet open in one hand and a pencil in the other, frowning in concentration. The censer hangs from his rope belt, cold, with no smoke.

Figure 3, organising: the hood is down. He stands upright, a clipboard under one arm and a plain mug in the other hand, calm and sceptical, one eyebrow raised. The censer is gone.

Figure 4, in control: the hood is down. Relaxed, with a slight smile, he holds a plain mug of tea in both hands. A ring of keys hangs from his rope belt.

Style: minimalist black ink line drawing, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black; the very short hair is a thin solid black cap close to the head. Black and white only: no grey, no shading, no gradients, no hatching, no colour. Plenty of empty white space. The drawing carries no text at all: no numbers, letters, labels, captions, logos or speech bubbles; the booklet and the clipboard show only a few thin lines.
```

Edit L, slide 1.3 at the start (its image 1 is `bw-03-scene-1-3.jpg`, its image 2 `bw-10-steve-evolution.jpg`):

```text
Edit image 1, a scene from a minimalist comic. Keep the camera, the framing, the drawing style, the workbench, the laptop, the candle, the hanging bulb and the robot exactly as they are. Change only this:
1. Replace the man with the man from image 2, figure 1 (praying): very short hair, a short full beard, no glasses, his hood up over his head, his face clearly visible inside it. He keeps the same pose: leaning towards the robot, both hands raised in front of his chest with the fingers crossed, hopeful and a little anxious.
2. The incense burner at the end of the bench becomes a small censer: a round metal bowl with a domed, pierced lid, hanging from the hook on three thin chains, a thin curl of smoke drifting from it over the robot.
Everything else stays exactly as it is. Black and white only, pure white background, no grey. No text anywhere. Landscape 16:9.
```

Edit M, slide 8.2 at the end (its images 1 and 2 as for L):

```text
Edit image 1, a scene from a minimalist comic. Keep the camera, the framing, the drawing style, the workbench, the laptop, the candle holder, the hanging bulb and the hook at the end of the bench exactly as they are. Change only this:
1. Replace the man with the man from image 2, figure 4 (in control): very short hair, a short full beard, no glasses, the hood down, a ring of keys on his rope belt. He now sits relaxed on a simple wooden stool beside the left end of the workbench, a mug of tea held in both hands, with a slight, content smile.
2. The robot is gone from the workbench, and the laptop is closed.
3. The candle has just been blown out: no flame, only a thin thread of smoke rising from its wick.
4. The incense burner on the hook is a small censer, a round metal bowl with a domed, pierced lid on three thin chains, hanging cold, with no smoke.
Everything else stays exactly as it is. Black and white only, pure white background, no grey. No text anywhere. Landscape 16:9.
```

Prompt N, the worker with a skill (its image 1 is `bw-02-cast-clean-line.jpg`):

```text
Create a new character study for the same minimalist comic, in exactly the drawing style of image 1: one clean drawing on a pure white background, landscape 16:9. The picture shows robots only, no people. Use image 1 only for the worker robot: the box-shaped robot with the solid black chest band, the square head with two round eyes and a short antenna, two thin gripper arms and one single wheel.

The worker robot is drawn three times, side by side on one thin floor line, facing the viewer, with plenty of white space between them:
1. exactly as on the cast sheet.
2. with an extra arm: a slim jointed arm, plugged into a socket on its back, rises over its head and holds a round magnifying glass in front of its eyes, while its own two grippers hold a sheet of paper.
3. as a specialised variant of itself: its right gripper has been swapped for a round magnifying glass on the end of that arm, and it holds a sheet of paper in its left gripper.
Between figures 2 and 3, a small rack on a short piece of wall drawn as a single line holds spare parts of the same kind on three hooks: a spare clip-on arm, a small pair of tweezers and a small brush.

Style: minimalist black ink line drawing in exactly the style of image 1: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no colour. No text anywhere: no letters, numbers, labels, captions or logos; the paper shows only a few thin lines.
```

Edit O, the title house larger (its image 1 is `bw-05-title.jpg`):

```text
Edit image 1. Redraw the same house much larger, so that it fills about 85 percent of the picture's height, centred, standing on the same thin ground line close to the bottom edge. Keep its shape, its solid black windows, its door, its chimney and its few hinted bricks. Make the lit basement window with its pointed gothic arch larger too, so that it stays clearly visible when the picture is shown small: white inside, a small candle flame, a few short lines radiating from it. Everything else stays pure white. Black and white only, no grey, no colour. No text anywhere. Landscape 16:9.
```

Edit P, the amber window (its image 1 is the result of O):

```text
Edit image 1. Keep the house, its windows, its door, its chimney, its bricks and the ground line exactly as they are. Change only the lit basement window with the pointed gothic arch: make it about one and a half times as large, and colour its inside, the small candle flame and the short lines radiating from it a warm amber, the only colour in the picture. Everything else stays black lines on pure white. No text anywhere. Landscape 16:9.
```

### What round 2 showed

- The six beards come out distinct and read at slide size. The cowl collar
  (8) looks more monastic, the plain hood (9) more like a modern hoodie.
- The arc reads at a glance: the hood goes down, the props of prayer leave
  one by one, the posture relaxes.
- 1.3 and 8.2 share one camera, so the pair tells the arc without words: the
  same bench, bulb and candle, a different man.
- The extra arm from the back, over the head, reads at once as an added
  ability. The swapped tool looks like a robot holding a magnifier.
- The title picture is 4.3 inches wide on the slide, so even a house that
  fills the frame's height stays small; the amber window is what draws the
  eye there.
- Setting near-white to white makes the files' backgrounds exactly white. In
  the LibreOffice render of a preview deck the picture area still sits one
  level below the slide (254 against 255); that comes from the PDF export,
  not from the files.

## The author's choices after round 2

On 2026-10-07 the author chose face A4 (image 8, fourth from the left: an
oval face, heavy stubble drawn as fine dots, very short hair, the cowl
collar), kept the clean line and the arc, and decided that the talk shows
pictures only, with a reference part to read after it. The storyline now
carries all of it: the STYLE, STEVE, STEVE'S ARC and SKILL ARM blocks of
`../storyline.md` describe the look, and their slide ranges replace the
table under "Steve's arc, as proposed". Still open there: whether the
candle keeps its amber flame.

## Round 3: face A4 in two scenes

### The files

| File | Shows | Made from |
|---|---|---|
| `bw-16-scene-1-3-a4.jpg` | slide 1.3 with face A4: hood up, stubble in fine dots, fingers crossed, candle and censer lit | edit R of image 12 with image 8 |
| `bw-17-scene-8-2-a4.jpg` | slide 8.2 with face A4: hood down, tea, the keys on his belt, the candle just out | edit S of image 13 with image 8 |

A third edit, Q, was to give the four stages of image 10 face A4, so that
the arc carries the chosen face before any scene is drawn. fal finished it,
but its result could not be fetched afterwards, and the edit was not run
again.

### How they were made

The model and settings of round 1, one sample each, near-white set to white
as in round 2. Image 2 of every edit is `bw-08-steve-faces-cowl.jpg`, where
face A4 is the fourth from the left. Two images, about 0.16 US dollars.

Edit Q, the arc with face A4 (its image 1 is `bw-10-steve-evolution.jpg`;
two samples requested, result not fetched):

```text
Edit image 1, a character study for a minimalist comic showing the same man four times. Keep the four poses, the props, the robes, the floor line and the drawing style exactly as they are. Change only the man's face and collar, in all four figures, to match the fourth figure from the left in image 2: an oval face; heavy stubble drawn as fine dots, a little denser on the chin, instead of a full beard; very short hair, almost a buzz cut; no glasses; and when the hood is down it lies as a short cowl collar over his shoulders. In figure 1 the hood stays up over his head, his face clearly visible inside it. Keep each figure's expression: hopeful and a little anxious; frowning in concentration; calm and sceptical; relaxed with a slight smile. Everything else stays exactly as it is. Black and white only, pure white background, no grey. No text anywhere. Landscape 16:9.
```

Edit R, slide 1.3 (its image 1 is `bw-12-scene-1-3-praying.jpg`):

```text
Edit image 1, a scene from a minimalist comic. Keep everything exactly as it is: the camera, the framing, the drawing style, the workbench, the laptop, the candle, the censer, the bulb, the robot, and the man's pose, hood and robe. Change only the man's beard: replace the full black beard with heavy stubble drawn as fine dots, a little denser on the chin, like the fourth figure from the left in image 2. Black and white only, pure white background. No text anywhere. Landscape 16:9.
```

Edit S, slide 8.2 (its image 1 is `bw-13-scene-8-2-in-control.jpg`):

```text
Edit image 1, a scene from a minimalist comic. Keep everything exactly as it is: the camera, the framing, the drawing style, the workbench, the closed laptop, the blown-out candle with its thread of smoke, the cold censer, the bulb, the stool, and the man's pose, mug, keys and robe. Change only his face to match the fourth figure from the left in image 2: an oval face with heavy stubble drawn as fine dots, a little denser on the chin, instead of the full black beard; very short hair, almost a buzz cut; a slight, content smile. Black and white only, pure white background. No text anywhere. Landscape 16:9.
```

### What round 3 showed

- An edit that changes only the face keeps everything else in place: bench,
  bulb, candle, censer, robot and pose. The two scenes still share one
  camera, so the pair tells the arc as before.
- The stubble of A4 carries over in both scenes. In 1.3 the hood leaves only
  a thin black hairline, which fits A4's black cap of hair.
- In 8.2 the model drew the hair as fine dots too, so the head looks shaved,
  and the lowered hood lies like a hoodie's: neither matches A4, whose hair
  is a thin solid black cap and whose hood lies as a cowl collar. A face
  taken from a reference is not enough; the plate of Steve's four stages
  should be drawn with A4 first, and every scene prompt should name the
  black cap of hair and the cowl collar.
- No lettering in either image, checked at full size on the laptop, the
  gear emblem and the keys.
- In a preview of the two-part deck both scenes fill the slide edge to edge,
  and the slide-number leaf sits on the floor line at the bottom left.

## Then

The author confirmed the four stages, the skill arm and the amber flame the
same day. `../image-prompts.md` was then rewritten from the storyline for the
new look, and the three plates in `../beats/` were made from it: the cast
with Steve's four stages in face A4, drawn afresh rather than by edit Q; the
props; and the basement as a white page with its objects. The sheet records
how each came out. Next, once the author has seen the plates: the 21 scene
images, about 2 to 3 US dollars, each with its near-white set to white
before it is saved.

## The goodbye animation (2026-10-09)

On 2026-10-09 the author asked for the cast to wave goodbye at the end of the
talk, in a GIF. The animation on the slide is `../beats/beat-08-team-3.gif`
(`beat-09-close-2.gif` until 2026-10-28, when the goodbye moved from 9.2 to 8.3),
image 30 of `../image-prompts.md`, which has the prompts, the settings and
the run. This folder keeps its three poses. The GIF is made from the first
two by `../../tools/goodbye_wave.py`; the third belonged to the first GIF.

### The files

| File | Shows | Made from |
|---|---|---|
| `anim-01-goodbye-out.png` | pose A, the frame: the worker, the man at the fourth stage, the reviewer and the gatekeeper in one row, the waving parts leaning out | Nano Banana 2.1, step 1 of image 30; the second of two samples |
| `anim-02-goodbye-middle.png` | pose M: the waving parts straight up, the strip hanging down | an edit of pose A; the second of two samples |
| `anim-03-goodbye-in.png` | pose B: the waving parts leaning the other way; used by the first GIF only | an edit of pose A; one sample |

All three are mapped onto the GIF's seven colours, as step 3 of image 30
describes, which keeps each at 58 KB.

### What it showed

- A video model came first. Kling 3.0 Pro closed its loop well, but five
  seconds made a GIF of 2.8 MB. MiniMax H3 Max jumped at the loop and
  flickered, and Wan 3.0 Prime lost the line. Their drafts were not kept.
- Two poses ticked rather than waved. Three poses, run as A, M, B, M, swung,
  but the author saw an odd afterimage in them, most likely because poses A
  and M are almost the same for three of the four parts: each of them stood
  still for three frames and flicked to pose B in the fourth.
- An edit redraws the whole picture a little: the man's stubble came out new
  in each pose. So only the parts that move are taken from a pose, and
  every other line stays still.
- Eight frames turned from one drawing wave evenly. Each part turns about
  its joint by a small step per frame, and its lines stay the drawing's own.
- Out of step, each figure waves in its own rhythm, which reads livelier
  than all four in time. To put them in time, give every part the same
  phase in `../../tools/goodbye_wave.py`.

## Round 4: Steve's own clothes (2026-10-12)

A joint review of paper and talk on 2026-10-12 found that Steve's arc hardly
shows. He wears the full robe in 1.1 and 1.2, before there is anything to
pray to, and the same robe from 2.1 to 8.2. Only the hood, the censer and
keys a few pixels high tell the stages apart, so 8.2 reads as the same monk,
relaxed. The author asked for a different arc the same day:

- Steve starts in his own clothes, before the first worker arrives.
- He puts the robe on for the machine, in 1.3.
- He loses it piece by piece, and ends in his own clothes again.
- His own clothes are what the author will wear on stage: jeans and a
  shirt, white in the talk's black and white.

The plan has six stages. Each step changes one outline that the back row
can see: the head, the legs or the shoulders.

| Stage | Slides | Steve |
|---|---|---|
| Before | 1.1, 1.2 | his own clothes, bare head, nothing on his belt |
| Praying | 1.3 | the robe over his clothes, hood up, candle and censer lit |
| Learning | 2.1 to 4.3 | the robe, hood down, the censer cold on the rope belt |
| Organising | 5.1 to 5.3 | the robe, the censer gone |
| Managing | 6.1 to 7b.3, and 7c.1 | only the shoulder cape, with its hood and gear, over his shirt and jeans; the keys from 7b.3 |
| In control | 7c.2, 8.2, 8.3 | his own clothes again, the keys on his belt; in 8.2 the robe hangs up |

The last step falls at 7c.2, not at 7b.3, because the paper shows 7b
(chapter 8) before 7a (chapter 9). A change at 7b.3 would put the cape back
on him from page 8 to page 9. At 7c.2 the arc runs one way in the talk's
order and in the paper's.

This round is the gate before any scene changes: one study of the three new
looks, set beside the three robe stages of the cast plate.

### The files

| File | Shows | Made from |
|---|---|---|
| `bw-18-steve-own-clothes.jpg` | Steve three times: his own clothes (a shirt with a collar, buttoned, tucked into jeans, with a belt and his trainers), tired, with a mug; the shoulder cape alone over the same clothes; the same clothes again, relaxed, tea in both hands, the keys on a clip at his right hip | prompt T with a cut-out of the cast plate's third figure; two samples, the second kept |
| `bw-19-steve-arc-six-stages.jpg` | the six stages on one floor line: the three figures of image 18 around the cast plate's first three figures, praying, learning and organising | put together without the model (below) |

### How they were made

Nano Banana 2.1 through fal, on the edit route, with the settings of
`../image-prompts.md`: `aspect_ratio` `16:9`, `resolution` `2K`,
`thinking_level` `high`, two samples, about 0.16 US dollars. Image 1 was the
cast plate's third figure, the organising stage, cut out on white, without
the edge of the second figure's booklet and the worker's arm beside it. It
lent the face, the cape and the trainers. One cut-out was enough: the model
drew a new sheet rather than editing it.

Prompt T, the three new looks:

```text
A character study for the same minimalist comic, one clean drawing on a pure white background, landscape 16:9. Image 1 shows the man and the drawing style: match exactly his face, his very short hair drawn as a thin solid black cap, his heavy stubble drawn as fine dots, his medium build, his plain trainers, the line and the size. Draw the same man three times, standing side by side in one row on one thin black floor line, each facing the viewer, with plenty of white space between them.

His own clothes, exactly the same in all three figures: a plain long-sleeved shirt with a collar, buttoned, the top button open, drawn in outline and left white, with no pocket, no pattern and no print; the shirt is tucked into plain jeans; the jeans are drawn in outline and left white inside, with a narrow plain belt and two seams down the legs; the plain trainers of image 1. His two legs show clearly.

Figure 1, on the left: only his own clothes. His head is bare. Nothing hangs from his belt. He stands a little tired, shoulders slightly slumped, a plain mug in one hand, sceptical.

Figure 2, in the middle: over his own clothes he wears only the short rounded shoulder cape of image 1, like a monk's cowl, over his shoulders and the upper chest, its hood lying flat behind his neck, the small gear emblem with square teeth on the cape. Below the cape his shirt sleeves, the front of his shirt, his belt and his jeans show, exactly as in figure 1; the long robe and the rope belt of image 1 are gone. Upright, calm and sceptical, one eyebrow raised, a plain mug in one hand.

Figure 3, on the right: only his own clothes again, exactly as in figure 1, standing upright and relaxed with a slight smile, holding a plain mug of tea in both hands in front of his chest. A ring of a few large keys hangs from a small clip on his belt at his right hip.

This picture has no colour. Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching. No walls and no room: a thin floor line and the figures named. One single drawing, no panels, no borders. Landscape 16:9. No text anywhere: no letters, no numbers, no labels, no captions, no logos, nothing printed on the clothes.
```

Image 19 was put together with Pillow, without the model:

- Each figure was cut from its sheet.
- The floor line and any piece of a neighbour at the cut's edge were dropped.
- In the plate, the smoke of the first figure's censer drifts across the
  second, so it was taken out of the learning figure.
- The study's figures were scaled to the plate's size.
- All six were set on one new floor line.

Both images had their near-white set to white before they were saved as
JPEG.


### What round 4 showed

- **The sheet came out at the first try.** One cut-out was enough: face A4,
  the cape with its hood and gear, the trainers.
- **The second sample is kept.** Its shirt has a row of buttons, so it reads
  as a shirt. The first sample drew the front without buttons, and under the
  cape the shirt looked like a jacket.
- **The line held.** The jeans stayed white inside, and at full size there is
  no grey and no lettering.
- **At about 550 px wide, five of six stages read from the outline.**
  - The test scales image 19 so that each man is about 190 px tall, as he
    would be in a scene on a small screen.
  - Learning and organising are the exception. They differ only by the
    censer, as they did before.
- **Three readers read image 19 cold**, knowing neither the prompts nor the
  script. One read it as a programmer in the back row, one as a manager with
  English as a second language, one as an illustrator.
  - **The story.** All three told the intended one: an ordinary man puts on
    the habit of a machine cult and swaps the ritual for notes and a
    clipboard. Then he sheds the robe and ends in his own clothes, "holding
    the keys".
  - **The cape.** All three read the fifth figure's cape as what is left of
    the robe. Small and on its own, it could pass for a poncho or a hoodie.
    Beside the robe it reads, and the gear helps.
  - **The hardest pairs.** All three found learning and organising hardest
    to tell apart. The fifth and sixth figures came next, because at small
    size the keys are a smudge.
  - **The joke.** All three read it as aimed at treating technology with
    ritual, not at faith, and called the risk low. Two noted that the habit
    looks Franciscan, and that the gear makes it a joke.
  - **The gear.** Two said that at small size it reads as a sun or a flower.
  - **A drawing slip.** Two saw a tangled stroke where the first figure's
    fingers meet the mug's handle. The scene edits take only the clothes
    from this sheet, so the slip stays here.
- **For the scenes:**
  - Draw the keys larger in 7c.2 and 8.2 than on this sheet, so that the end
    does not read as the start.
  - 8.2 adds its own signs as well: the candle out, the tidy board and the
    robe hung up.

The author decides at this gate:

- **Go:** first the bookends, then the cape stage.
- **The bookends only:** 1.1, 1.2, 7c.2, 8.2 and the goodbye, if the cape
  stage does not convince.
- **Stop:** the arc stays as it is.

The author chose to go the same day, with the bookends and the cape stage
both. The 13 scenes, the cast plate's fourth man and the goodbye's frame
were changed by edits of their own pictures (`../image-prompts.md`, "Added
for the costume arc"), and image 19 became the plate `../beats/ref-steve.jpg`.

## Round 5: names that float (2026-10-15)

After the first run-through the author asked for the mechanisms' names on
the slides, preferably as a picture, and then for the cast's names to float
above them "like in a game". Three ways were drawn on the real pictures, in
mock-ups made with Pillow, before the build learnt any of them:

- **A paper tag on a string**, tied to the object, its name on the tag. It
  read well and fitted the line, but a tag on every robot looked like a
  price tag, and on small objects it hid the drawing.
- **A callout**, a dot on the object and a thin line to its name in the
  white space, as in a technical drawing. Exact, but it read as a diagram,
  not as the story.
- **A nameplate, as in a game**: the name in bold and, below it in angle
  brackets, what it is in Claude Code, centred over the head. Drawn twice:
  black letters with a white halo, and white letters on black plates. The
  black plates were louder and put solid black, which means real data in
  these drawings, on every slide.

The author chose the nameplates with the halo, on every slide where a robot
appears, labels over the objects where they first matter, and a bar for the
context window in beat 6. The build draws them from `cast`, `names` and
`labels` in `../deck.yaml`, with a white plate behind each line in place of
the halo, which PowerPoint and LibreOffice both show the same way.

## Round 6: cards for the new team members (2026-10-19)

After the second run-through the author asked for a sheet for each robot,
the worker, the reviewer and security, so that each is introduced once and
can be described. A mock-up made with Pillow on the real slides tried one
form: the picture where the robot joins the team, frozen under a white
veil, and on it a card like a game's new team member, with a black tag, a
portrait, the name and the Claude Code term, and five rows of what the robot
can and cannot do, KEY beside its words. The rows replace invented game
statistics, such as dots for strength, which would have claimed numbers
nobody measured. The author took it as drawn. The build draws the cards from
`cast` in `../deck.yaml` on the slides after 1.2, 4.3 and 5.2; the portraits
come from a plate of the three robots alone (`../image-prompts.md`, image 32).

## The flights (the evening of 2026-10-19)

After a review of the deck the author asked for the slides where data moves
to move, as the goodbye does. A prototype of 7c.1 came first, with the
review: one sheet cut from the drawing and set back along a path through the
drawn sheets, eight frames a loop. The author took it, and
`../../tools/flying_sheets.py` now makes all three flights, image 33 of
`../image-prompts.md`, from the files below. The same evening the reviewer's
card moved beside the worker's, from a mock-up made with the deck's own card
code; it is not kept.

### The files

| File | Shows | Made from |
|---|---|---|
| `anim-05-sheets-7c1-plate.png` | 7c.1 without its flying sheets and their speed lines; the sheet that has landed stays (used until 2026-10-28) | the drawing of 7c.1, with the house's wall from 7c.2 and the warehouse's lines drawn through |
| `anim-05-sheets-7c1-sprite.png` | one black sheet, with its own alpha (used until 2026-10-28) | the sheet at the top of the arc |
| `anim-05-book-7c1-plate.png` | the plate of 7c.1 with the Book of Secrets standing on the cabinet's top shelf in place of the landed sheet, behind the door's edge | `anim-05-sheets-7c1-plate.png` and the sprite below |
| `anim-05-book-7c1-sprite.png` | the Book of Secrets, with its own alpha | the sealed book on the shelf of 1.1, `../beats/beat-01-alone-1.jpg`, at 0.42 |
| `anim-06-folders-7c2-plate.png` | 7c.2 without its flying folders and their speed lines; the folders on the shelf stay | the drawing of 7c.2, with the warehouse's lines drawn through |
| `anim-06-folders-7c2-sprite.png` | one white folder | the folder at the top of the arc |
| `anim-07-stream-7b1-plate.png` | 7b.1 without its stream of sheets; the antenna's rays and the window stay | `../beats/beat-07b-isolation-1.jpg` |
| `anim-07-stream-7b1-sprite.png` | one small sheet | the third sheet of the stream, alone on the wall |

### What they showed

- A sprite cut from the drawing keeps the drawing's own line, so the flight
  looks drawn, not rendered. The tool draws nothing but the speed lines.
- A sheet is one rigid shape, so it flies without hand work. The goodbye's
  turned limbs needed it at every joint, which is one reason the motion
  stays with things that fly.
- A palette made from the whole frame folded the few red pixels of the seal
  and the paddle into brown. A ramp of greys with the picture's own reds
  keeps them red.
- At full size and half faded, a sprite on the wall read as a grey ghost in
  the still. Starting at a quarter of its size and fading in quickly, it
  comes out of the window.
- Where a GIF cannot play, as in a PDF of the deck, its first frame stands.
  So each loop starts on the frame the paper keeps.

## Round 7: two more steps for Steve (late on 2026-10-19)

Going through the built deck, the author found that Steve's look hardly
changes between 2.1, where the hood comes down, and 7c.2, where the cape
comes off. Only the censer (5.1) and the robe (6.1) went in between: ten
pictures showed the same robe, and nine the same cape. The author asked
for steps that show. Two were added, each changing an outline the back row can see,
the legs or the front of the robe, so his look now changes at every beat
from 2 to 7:

| Stage | Slides | Steve |
|---|---|---|
| Before | 1.1, 1.2 | his own clothes, bare head, nothing on his belt |
| Praying | 1.3 | the robe over his clothes, hood up, candle and censer lit |
| Learning | 2.1 to 2.3 | the robe, hood down, the censer cold on the rope belt |
| Working | 3.1 to 4.2 | the robe hitched up into the rope belt, his jeans and trainers showing below it; the censer still cold |
| Organising | 5.1 to 5.3 | the robe still hitched up, the censer gone |
| Delegating | 6.1, 6.2 | the rope belt off, the robe open like a coat under the cape |
| Managing | 7.1 to 7b.3, and 7c.1 | only the shoulder cape over his shirt and jeans |
| In control | 7c.2, 8.2, 8.3 | his own clothes again, the keys on his belt; in 8.2 the robe hangs up |

### The files

| File | Shows | Made from |
|---|---|---|
| `bw-20-steve-hitched-and-open.jpg` | Steve three times: the robe hitched up, with the censer and a notebook; the same without the censer, with a clipboard and a mug; the robe open like a coat over his shirt and jeans, with a mug | edits of the learning, organising and managing figures of `../beats/ref-steve.jpg`, each cut out on white; the first sample of each, set side by side on one floor line without the model |

The edits and their prompts are images 34 and 35 of `../image-prompts.md`.

### What round 7 showed

- **One figure carries the look.** Each edit kept the face, the hands and
  what they hold, and changed only the robe. As image 2, each figure then
  carried its look into every scene of its stage at the first try.
- **Hitched up, the robe reads as work clothes.** Tucked into the rope belt
  at both hips, it ends below the knees in soft folds, and the jeans and
  trainers below it already show the man in his own clothes.
- **Open, the robe reads as a coat.** Without the rope belt it hangs
  straight from under the cape, and the shirt, belt and jeans show between
  its edges: the step before the cape alone.
- **No cold read this time.** The author chose the two steps from the plan,
  and the scenes followed the same evening; the deck's run-through is the
  test.

## The diagram cast (2026-10-26)

`excalidraw-cast-sheet.jpg` redraws the four card portraits and the man of
`ref-steve.jpg` in the look of
the paper's Excalidraw diagrams (`image-prompts.md`, image 46).

- **The portraits looked pasted in.** Cut from the cards, the talk's clean
  line sat beside the diagrams' wobbly boxes like a photograph on a
  whiteboard; the author asked for the cast in the diagrams' own hand.
- **A shape-only scene carries the stroke.** A small Excalidraw export of
  boxes, arrows and a red dot, with no text, gave the model the stroke
  without any lettering to copy.
- **The rougher sample wins.** Of two samples, the one with hatched solids
  and doubled lines matched Excalidraw; the cleaner one matched the talk.
- **Thin lines vanish in print.** Drawn 13 to 22 mm tall, the sheet's lines
  print as hairlines; thickened by seven pixels they match the boxes.
