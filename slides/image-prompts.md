# Image prompts

The production sheet for the talk's pictures. It says which images to make,
in which order, with which model and settings, and it gives the prompt for
each one, ready to paste. `storyline.md` stays the source of every scene and
of the cast, the props and the places. This sheet turns them into prompts, so
when a scene or a block changes there, change its prompt here in the same
commit.

Rewritten on 2026-10-07 for the look the author chose that day: minimalist
black-and-white line drawings with a light touch of the tech priest, Steve
with face A4 and the four stages of his arc, every story image shown whole.
`studies/README.md` records how the look was found. The comic prompts of
2026-10-06, whose images stood in `beats/` until this sheet's images
replaced them on 2026-10-07, are no longer in this file; the working
repository's history keeps them. Model and price were checked on
2026-10-06 against fal's catalogue and price list, and the studies of
2026-10-07 ran at the same price.

## At a glance

- **28 generations:** three reference plates and 25 slide images. The title
  picture (6) is the study `studies/bw-15-title-amber.jpg`, copied as it is.
  Slide 7b.2, a crop of image 23 made by the deck, was dropped on
  2026-10-15. Image 25 is made in two edits, 25a and 25b. Images 26 and 27,
  for beat 7a, were added on 2026-10-07 after the other 25 were made, and
  images 28 and 29, for beat 7c, on 2026-10-08; in the story 26 and 27 sit
  between 22 and 23, and 28 and 29 follow 24. They carry the next numbers
  so that the others stay as they are.
- **One animation** (2026-10-09): the goodbye of slide 8.3 (9.2 until
  2026-10-28), image 30, a
  loop of eight frames. Nano Banana 2.1 draws its frame and a pose with the
  strip hanging down, `tools/goodbye_wave.py` turns the waving parts, and
  the frames are saved as one GIF rather than a JPEG; its section below has
  every step.
- **The costume arc** (2026-10-12): Steve starts in his own clothes, puts
  the robe on in 1.3 and sheds it piece by piece. Thirteen story images,
  the cast plate's fourth man and the goodbye's frame were changed by an
  edit of each picture, with only the man's box pasted back, and a fourth
  plate, `ref-steve.jpg`, sets out the six stages. The scene prompts below
  made the pictures before that change; the section "Added for the costume
  arc" has the edits that followed.
- **The run-through** (2026-10-15): after the author's first run-through,
  image 23 lost its glass dome and image 27 gained the gatekeeper at the
  foot of the stairs, each by one edit; the section "Changed after the
  run-through" has both. The deck floats the robots' names above them since
  that day, so they are never drawn in.
- **The second run-through** (2026-10-19): image 31 is new, the fresh
  worker of slide 2.2; image 21 gained Steve's right arm and image 5 the
  planted letter run through with a sword, each by one edit with only the
  changed box pasted back; and plate 32, the three robots alone, gave the
  portraits of the cards the deck shows. The section "Changed after the
  second run-through" has all four.
- **The review** (the evening of 2026-10-19): a review of the deck at full
  size found two pictures that said the opposite of the talk and fifteen
  smaller faults. Thirteen pictures were corrected, by an edit with only
  the changed box pasted back where the model could do it and by hand where
  it could not, and the card portraits lost their pieces of floor line.
  Image 33 puts 7b.1, 7c.1 and 7c.2 in motion, turned from the drawings
  like the goodbye. The section "Changed after the review" has every step.
- **The built deck** (late on 2026-10-19): the worker's eyes all take
  6.2's pupil and highlight, drawn in by a script (36); 6.1 builds up through
  three new pictures (35); Steve gains two looks, the robe hitched up from
  3.1 and open from 6.1, first on one figure each (34), then in nine scenes;
  and 7.1's drawing hand became a left hand (21c). The section "Changed
  after the built deck" has every step.
- **The third run-through** (2026-10-20): the lit windows of 7b.3, 7c and
  8.2, yellow with a bare bulb, and 8.2's bulb, drawn by a script (37); the stream of 7b.1 in
  front of the open casement instead of behind it (33a); three checks on
  the wall of 3.1, each marked its own way, and three identical ones in 3.2
  (12b); and the portrait of the threat's card, the planted letter on a
  puppeteer's cross (38). The section "Changed after the third run-through"
  has every step.
- **The secret level** (2026-10-27; beat 10 since 2026-10-28, right after
  the closing slide): two pictures for a question, the EU rapping Steve's
  knuckles (47, its hand set right in 47b) and the calculator that answers
  it (48, its stop button taken out in 48a), and the EU's portrait for its
  card (49). The section "Added for the secret level" has every step.
- **Model:** Nano Banana 2.1 (Google), through fal, on its edit route
  `google/nano-banana-2.1/edit` for every image: each one takes reference
  images, even the cast plate, which starts from the studies.
- **Settings for every image:** `aspect_ratio` `16:9`, `resolution` `2K`
  (2752 × 1536 px), `output_format` `png`, `thinking_level` `high`,
  `num_images` 1. For the cast and basement plates and for the scenes that
  others build on or that are busy (1, 3, 4, 5, 9, 23, 26 and 28) ask for 2
  and keep the better one.
- **Cost:** 0.08 US dollars per image on fal (price list of 2026-10-06), so
  about 2.90 dollars for one pass with the second samples, and 3.55 with
  retries.
- **Order:** the three plates first, then the two images that carry the most
  weight (4 and 5), then the rest in story order. Fix images are edits of
  the image before them, so that image has to exist first.
- **Saving:** fal delivers PNG. Every pixel whose three channels are all
  above 245 is set to pure white, so the picture meets the white slide
  without an edge; then the image is saved as JPEG (quality 90, full colour
  resolution, optimised Huffman tables, which make the file about a fifth
  smaller at no loss) in `slides/beats/` under its file name. A drawing
  moved sideways on its white ground moves in steps of 8 px, the JPEG block
  size, so that saving it again loses as little as possible. Then
  `uv run python tools/build_slides.py --list` shows what is still missing.

## Why this model

Reve, the model the storyline was first written for, closed its image
generation on 27 September 2026; its users can download their library until
31 October. The author chose Nano Banana 2.1 on 2026-10-06, after the same
cast prompt had run on it and on Nano Banana Pro:

- It kept closer to the descriptions than Nano Banana Pro and costs about
  half as much (0.08 against 0.15 US dollars per image on fal).
- It takes several reference images per request, which keeps the cast, the
  props and the basement the same from slide to slide. The comic run used
  up to three, the cast plate below takes four.
- Its edit route changes what the prompt names and keeps the rest of the
  picture, which is how each fix image is made from its pain image.
- In the studies of 2026-10-07 it held the black-and-white line: black on
  white, no grey, no shading and no lettering in the clean line.
- 16:9 at 2K is 2752 px wide, above the 2400 px the deck asks for.
- Through fal's API the images carry no visible watermark.

Stay with one model for all the images: a second model would bring a second
drawing style.

**Fallbacks.** Nano Banana Pro takes the same prompts and settings on fal
(`fal-ai/nano-banana-pro/edit`), without `thinking_level`. Without fal, the
Nano Banana models also run in Google AI Studio: choose the model, set 16:9
and 2K, and attach the references in the listed order. The Gemini app offers
them too, but it puts a visible sparkle on its images unless its Media
Watermark setting can be turned off, and Google does not offer that setting
in every country. GPT Image 2 (`openai/gpt-image-2/edit` on fal) is a
further fallback; check its price and the width of its output before
switching.

## How to make one image

1. **References.** fal takes reference images as URLs. An image made on fal
   already has one, so it can go straight into the next request; a file from
   `slides/beats/` or `slides/studies/` is uploaded once and its URL reused.
   Pass them as `image_urls` in the order the prompt names them: the first
   URL is "image 1", the second "image 2", and so on.
2. **Request.** Use the edit route, the image's prompt and the settings
   above:

   ```json
   {
     "prompt": "…the prompt from this sheet…",
     "image_urls": ["…image 1…", "…image 2…", "…image 3…"],
     "aspect_ratio": "16:9",
     "resolution": "2K",
     "output_format": "png",
     "thinking_level": "high",
     "num_images": 1
   }
   ```

   The route defaults to `aspect_ratio` `auto`, so always set `16:9`.
3. **Fix images** (11, 13, 20, 22, 25, 27, 29) edit the picture before them: it
   is image 1, a plate image 2 or 3 where the section says so, and the prompt
   is the edit instruction. An edit holds best with four to six changes; image
   25 has more and is therefore made in two steps.
4. **Check and save.** Go through the checks below at full size, set the
   near-white to white and save as JPEG as described under Saving, under its
   name in `slides/beats/`, and rebuild.

In a Claude Code session with the fal connector, all of this is one request,
for example "make image 7 from `slides/image-prompts.md`": Claude passes the
references, runs the request, saves the result under its name and looks at
it. A request takes about a minute; independent images can be queued
together. In fal's web playground for the model, paste the prompt, add the
references in order, set 16:9 and 2K, and download the result.

## Where things may go in the frame

The deck shows each image in one of three ways:

| Shown as | Slides | Keep free or keep in |
|---|---|---|
| the whole slide, edge to edge | every story slide from 0.2 to 8.2 | the whole frame is seen; keep the top right corner free (the right 6 % of the width, the top 10 % of the height), where the AI label sits, and the bottom right corner calm (the right 8 % of the width, the lowest 9 % of the height), where the slide number sits and only the floor line may run |
| a closer crop with two rings | 7b.2, from image 23 | the crop takes a little over two thirds of the width and height, from about 11 to 79 % across and 28 to 96 % down (`focus` 0.45, 0.62 and `zoom` 1.45 in `deck.yaml`, set for the edited image of 2026-10-07); the gatekeeper, the dome, the worker and the start of the stream from its antenna must be inside it; the AI label takes the crop's top right corner, about 76 to 78 % across and 29 to 34 % down, just right of the stream |
| small, on the title slide (until 2026-10-28) | 0.1 | one clear shape; the picture was 4.3 inches wide, and the AI label took its top right corner (the right 13 % of the width, the top 22 % of the height); since 2026-10-28 the house fills slide 0.2 |

The author put the slide number in the bottom right corner on 2026-10-07,
in a leaf, and took the leaf away on 2026-10-09; `picture_corner` in
`deck.yaml` sets the side, and with `false` the corner rule goes. The AI
label, the EU's basic icon for AI-generated content, joined the same day.
The build adds it to every image, so it is never drawn into one, and warns
when it would hide part of a drawing. Since 2026-10-15 the deck also floats
the robots' names above their heads and sets labels over objects (`names`
and `labels` in `deck.yaml`), so a picture with room above the heads takes
them best, and a new picture needs its positions set again.

## Checks for every image

- **No text.** Look at full size at the places where image models like to
  write: the paddle, the pictogram, the catalogue cover and pages, the
  envelope, the letter, the whiteboard, the receipt, the badge and the badge
  reader, the arm rack, the gear emblem, the sticky notes and index cards, the
  organisation chart and the gauge.
- **Line.** Black lines on white and a few small areas of solid black: no
  grey, no shading, no gradients, no hatching. No walls where the scene names
  none; the office of 7b.3 and 8.1 and the warehouse of 7c are the only
  buildings with walls besides the house.
- **Bodies.** The worker rolls on one wheel and has no legs. The reviewer has
  no arms. The gatekeeper stands bolted to the floor. The worker wears its
  skill arm only in 3.2.
- **Letter and strings** (7a only). Three thin, straight, taut lines run from
  the foot of the letter to one gripper of the worker, not scribble, not a
  web and not one wide band; in 7a.2 they lie slack on the clerk's desk. The
  letter carries a few thin lines and one short thick one at its foot, with no
  seal, stamp or address.
- **Steve.** Face A4: an oval face, stubble in fine dots, very short hair as
  a thin solid black cap, no glasses. His stage matches the scene
  (`storyline.md`, STEVE'S ARC, since 2026-10-12):
  - his own clothes, bare-headed, in 1.1 and 1.2;
  - the robe, hood up, in 1.3;
  - from 2.1 the hood down behind the shoulder cape, the censer cold on his
    belt until 4.3 and gone from 5.1;
  - from 6.1 only the cape over his shirt and jeans, nothing on his belt;
  - his own clothes again from 7c.2, the keys on his belt.
  The gear sits only on the cape. Nothing is printed on the shirt, and the
  jeans stay in outline, never filled, because solid black means real data.
- **Colour.** Red appears only on the wax seal, the gatekeeper's paddle and
  the pictograms of 4.2; amber only on the candle's flame in 1.3 (lamp yellow
  in the lit windows and bulbs: 7b.3, 7c and 8.2 since 2026-10-20, 0.2 and
  1.1 since 2026-10-29). The
  man corrects with a black pen. The gauge carries no colour.
- **Data.** Black archive boxes stand only on the share behind the steel
  door, on the basement floor in 7b.1, behind the house's window in 7b.3 and,
  where that night's sheets landed, on the warehouse's shelves in 7c.1; none
  ever appears at the office. Sheets in flight are black only in 7c.1's
  drawing; on the slide and in the paper's still the Book of Secrets flies
  in their place (since 2026-10-28, image 33).
- **Continuity.** Each fix leaves an object that stays in the later wide shots
  of that place (the storyline's visual rule 3): the rulebook from 2.3, the
  arm rack from 3.2, the gatekeeper and barrier from 4.3, the glass room from
  5.3, the filing cabinet from 7.1. The candle appears only in 1.3 and 8.2;
  since 2026-10-29 a lamp lights the window of 0.2.
- **Size and white.** 2752 × 1536 px, and the background exactly white after
  saving; the build warns below 2400 px.

## Short forms

The plates carry the full descriptions from `storyline.md`. The scene
prompts repeat a short form of each character, in the same words in every
prompt, because a model holds a reference better when the text names the
traits that matter:

- **The man:** late thirties, medium build, an oval face with heavy stubble
  drawn as fine dots, very short hair drawn as a thin solid black cap, no
  glasses; his own clothes: a plain long-sleeved shirt with a collar and a
  row of small buttons down the front, drawn in outline and left white,
  tucked into plain jeans that are drawn in outline and left white inside,
  with a narrow plain belt, and plain trainers. Then his stage:
  - before: only his own clothes, his head bare;
  - praying: over them a long plain hooded robe like a monk's with a short
    rounded shoulder cape, like a monk's cowl, over the shoulders and upper
    chest, a small gear emblem with square teeth on the cape and a rope
    belt; his hood up over his head, his face clearly visible inside it;
  - learning: the robe, his hood down behind the cape, his sleeves pushed
    up, a small censer hanging cold from his rope belt;
  - organising: the robe, his hood down behind the cape;
  - managing: only the short rounded shoulder cape over his own clothes,
    its hood lying flat behind his neck, the gear on it; nothing on his belt;
  - in control: only his own clothes, a ring of large keys on a clip at his
    right hip.
- **Worker robot:** hip-high, a rounded box body with a solid black band
  round its chest, a square head with two round eyes and a short antenna,
  two thin jointed arms with two-finger grippers, one wheel and no legs.
- **Skill arm** (3.2 only): a slim jointed arm clipped into a socket on the
  worker's back, rising over its head and holding a round magnifying glass
  in front of its eyes.
- **Reviewer robot:** smaller and slimmer than the worker, an egg shape with
  smooth, unbroken sides, one large round lens as its only eye, the same
  solid black band and short antenna as the worker, a narrow strip of paper
  from a slot in its chest.
- **Gatekeeper:** a squat, faceless steel post bolted to the floor on a base
  plate with big bolts, a guard's peaked cap, one round lamp, and one jointed
  arm holding up a blank round red paddle.
- **Letter and strings** (7a only; the props plate does not carry them): a
  long sheet of paper, folded once and held open, showing a few thin lines of
  scribble and, at its foot, one short thick black line; three thin, straight,
  taut lines from its foot to the wrist of a gripper, like a marionette's
  strings.

The robots' size comes from the cast plate alone: the scene prompts say "at
the sizes shown there", so a change of size is made in one place.

Every prompt for a new picture ends with the storyline's STYLE, word for
word, after one line that names the picture's colours:

> Minimalist black ink line drawing on a pure white background, a little
> more than stick figures: simple shapes, few lines, one even line weight, a
> few small areas of solid black. Black and white only: no grey, no shading,
> no gradients, no hatching; colour appears only on objects described as red
> or amber. No walls and no room unless the scene names them: a thin floor
> line and the objects named. One single scene, no panels, no borders.
> Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no
> numbers, no speech bubbles, no captions, no logos, no signs with words.
> Paper shows only a few thin lines; any laptop screen faces away.

## The production list

| # | File | Slide | Made from |
|---|---|---|---|
| 1 | `ref-cast.jpg` | — | studies 8, 10, 2 and 14 |
| 2 | `ref-props.jpg` | — | 1 |
| 3 | `ref-basement.jpg` | — | 1, 2 |
| 4 | `beat-04-hooks-3.jpg` | 4.3 | 1, 2, 3 |
| 5 | `beat-08-team-1.jpg` | 8.1 | 1, 2 |
| 6 | `beat-00-title-1.jpg` | 0.2 | copied from study 15 |
| 7 | `beat-01-alone-1.jpg` | 1.1 | 1, 2, 3 |
| 8 | `beat-01-alone-2.jpg` | 1.2 | 1, 2, 3 |
| 9 | `beat-01-alone-3.jpg` | 1.3 | 1, 2, 3, study 16 |
| 10 | `beat-02-claude-md-1.jpg` | 2.1 | 1, 2, 3 |
| 11 | `beat-02-claude-md-2.jpg` | 2.3 | edit of 10, with 2 |
| 12 | `beat-03-skills-1.jpg` | 3.1 | 1, 2, 3 |
| 13 | `beat-03-skills-2.jpg` | 3.2 | edit of 12, with 1 and 2 |
| 14 | `beat-04-hooks-1.jpg` | 4.1 | 1, 2, 3 |
| 15 | `beat-04-hooks-2.jpg` | 4.2 | 1, 2, 14 |
| 16 | `beat-05-subagents-1.jpg` | 5.1 | 1, 2, 3 |
| 17 | `beat-05-subagents-2.jpg` | 5.2 | 1, 8 |
| 18 | `beat-05-subagents-3.jpg` | 5.3 | 1, 2, 3 |
| 19 | `beat-06-context-1.jpg` | 6.1 | 1, 2 |
| 20 | `beat-06-context-2.jpg` | 6.2 | edit of 19 |
| 21 | `beat-07-memory-1.jpg` | 7.1 | 1, 2, 3 |
| 22 | `beat-07-memory-2.jpg` | 7.2 | edit of 21, with 2 |
| 23 | `beat-07b-isolation-1.jpg` | 7b.1 | 1, 2, 3 |
| 24 | `beat-07b-isolation-3.jpg` | 7b.3 | 1, 2, 5, 6 |
| 25 | `beat-08-team-2.jpg` | 8.2 | two edits of 9, with 1, then 2 |
| 26 | `beat-07a-safety-1.jpg` | 7a.1 | 1, 2, 3, 22 |
| 27 | `beat-07a-safety-2.jpg` | 7a.2 | edit of 26, with 18 |
| 28 | `beat-07c-data-1.jpg` | 7c.1 | 1, 2, 24 |
| 29 | `beat-07c-data-2.jpg` | 7c.2 | edit of 28, with 1 and 2 |
| 30 | `beat-08-team-3.gif` | 8.3 | four cut-outs from 1 and a first sample, then two edits of the frame; turned by `tools/goodbye_wave.py` |
| 31 | `beat-02-claude-md-3.jpg` | 2.2 | edit of 10, with 11 and 1 |
| 32 | `card-worker.png`, `card-reviewer.png`, `card-security.png` | the cards after 1.2, 4.3 and 5.2 | edit of 1, then cut out |
| 33 | `beat-07b-isolation-1.gif`, `beat-07c-data-1.gif`, `beat-07c-data-2.gif` | 7b.1, 7c.1, 7c.2 | turned from 23, 28 and 29 by `tools/flying_sheets.py` |
| 34 | `studies/bw-20-steve-hitched-and-open.jpg` | — | edits of three figures cut from `ref-steve.jpg`, set side by side |
| 35 | `beat-06-context-1a.jpg`, `beat-06-context-1b.jpg`, `beat-06-context-1c.jpg` | 6.1's build-up | three edits of 19, with parts of 19 pasted back |
| 36 | the worker's eyes, in 17 pictures, its card, plate 1 and two animation plates | wherever the worker looks out | drawn by a script in 6.2's proportions |
| 50 | `beat-00-title-2.gif` | 0.3 | zoomed from 6 into 7 by `tools/window_zoom.py` (`tools/door_zoom.py` until 2026-10-29) |

"Study n" is `studies/bw-nn-….jpg` with that number.

---

## The reference plates

### 1 · `ref-cast.jpg` — the cast

- **Used by:** every image with a character; never shown on a slide.
- **Make:** image 1 `studies/bw-08-steve-faces-cowl.jpg` (face A4 is the
  fourth from the left), image 2 `studies/bw-10-steve-evolution.jpg` (the
  four stages), image 3 `studies/bw-02-cast-clean-line.jpg` (the line and
  the robots), image 4 `studies/bw-14-worker-skill-arm.jpg` (the skill arm);
  `num_images` 2. Then edit 1a on the better sample, with image 2
  `studies/bw-08-steve-faces-cowl.jpg` again; `num_images` 2.
- **Shows:** Steve in the four stages of his arc, the worker plain and with
  its skill arm, the reviewer and the gatekeeper, at their true sizes, so
  that every later image can copy them.

```text
A character model sheet for a minimalist comic, one clean drawing on a pure white background, landscape 16:9. Use the attached images as references: image 1 for the man's face, the fourth man from the left there; image 2 for his four poses and props; image 3 only for the drawing style and for the three robots, not for the man; image 4 for the worker robot's extra arm. Draw only what this prompt names.

Eight figures stand in one row on one thin black floor line, drawn at their true sizes relative to each other, with plenty of white space between them. From left to right:

Figures 1 to 4: the same man four times, changing step by step from a man who prays for his machines to a man who has them under control. In all four he is a programmer in his late thirties with an ordinary, medium build, neither thin nor heavy and not muscular; an oval face with heavy stubble drawn as fine dots, a little denser on the chin; very short hair, almost a buzz cut, drawn as a thin solid black cap; no glasses: the face of the fourth man from the left in image 1. He wears a long, plain, hooded robe like a monk's, whose hood lies as a short cowl collar over his shoulders when it is down, a simple gear emblem on the chest, a rope belt and plain trainers under the hem.
1. Praying: his hood is up over his head, his face clearly visible inside it. He holds a short white candle in a small holder in one hand, its flame lit, and in the other a small censer on three thin chains, a round metal bowl with a domed, pierced lid, a thin curl of smoke rising from it. Hopeful and a little anxious.
2. Learning: his hood is down, lying as a short cowl collar over his shoulders. His sleeves are pushed up; he holds a slim booklet open in one hand and a pencil in the other, frowning in concentration. The censer hangs cold from his rope belt, with no smoke.
3. Organising: his hood is down as a short cowl collar. He stands upright, a clipboard under one arm and a plain mug in the other hand, calm and sceptical, one eyebrow raised. The censer is gone.
4. In control: his hood is down as a short cowl collar. Relaxed, with a slight smile, he holds a plain mug of tea in both hands. A ring of a few large keys hangs from his rope belt.

Figure 5: the worker robot, facing the viewer, as in image 3. It stands about as tall as the man's hip: the top of its head is level with his hip. A rounded box body with a solid black band round its chest; a square head with two round eyes set into its face and a short antenna; two thin jointed arms ending in two-finger grippers. Its body ends at the bottom in one single wheel: it rolls, and it has no legs and no feet.

Figure 6: the same worker robot wearing its skill arm, as in image 4: a slim jointed arm clipped into a socket on its back rises over its head and holds a round magnifying glass in front of its eyes, while its own two grippers hold a sheet of paper.

Figure 7: the reviewer robot, facing the viewer, a little smaller and slimmer than the worker robot. An egg shape with smooth, unbroken sides; nothing is attached to its sides. Its only eye is one large round lens. It wears the same solid black band round its middle and the same short antenna on top as the worker robot and glides on a hidden wheel. A narrow slot in its chest lets out one narrow strip of paper. It looks designed this way, not damaged.

Figure 8: the gatekeeper. A squat, faceless steel post whose top reaches the man's hip, bolted to the floor on a heavy base plate with big bolts. It wears a guard's peaked cap with a visor on top and has one round lamp on its front, and one jointed arm holds up a round red paddle with a completely plain, blank face. A fixed installation, not a walking figure.

The candle's flame is amber and the gatekeeper's paddle is red: these are the only two colours on the sheet.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

Edit 1a, the keys, the stubble and the shoulder cape:

```text
Edit image 1, a character model sheet for a minimalist comic. Keep the drawing style, the layout and all eight figures exactly as they are. Change only this:
1. Move the ring of keys from the third man's rope belt to the fourth man's rope belt, the man holding the mug of tea in both hands.
2. Give the fourth man the same heavy stubble drawn as fine dots as the other three men.
3. In figures 2, 3 and 4, where the hood is down, the robe has a short rounded shoulder cape, like a monk's cowl, that covers the shoulders and the upper chest, exactly as on the fourth man from the left in image 2; the gear emblem sits on the cape. Figure 1 keeps his hood up.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the candle's flame stays amber and the gatekeeper's paddle red. No text anywhere. Landscape 16:9.
```

- **Check:** eight figures; face A4 in all four stages, with the black cap of
  hair and the stubble, and from figure 2 the shoulder cape; the keys on the
  fourth man only; the robots hip-high, the worker on one wheel, the
  reviewer's sides smooth; the paddle round and blank; red and amber only
  where named; no labels under the figures.
- **Made on 2026-10-07**, eight images and one edit that returned none:
  - The prompt, two samples. The first had all eight figures and face A4,
    but put the keys on the third man, left the fourth without stubble, drew
    the lowered hoods like a hoodie's, drew two floor lines and let the plain
    worker stand in front of the fourth man. The second left out the plain
    worker.
  - An edit with five changes, edit 1a's three plus one floor line and more
    space, returned no image.
  - Edit 1a on the first sample, two samples: the second is the plate. The
    first lost the third man's stubble.
  - The prompt again, with the cape, the keys and the spacing spelled out:
    one sample drew full black beards, the other merged the two workers.
  - A layout edit for one floor line and more space returned the plate
    unchanged, twice.
  - So the plate keeps its two floor lines and the plain worker in front of
    the fourth man's robe. It is a reference and never shown, and every
    scene prompt sets its own floor line.

### 2 · `ref-props.jpg` — the props

- **Used by:** every scene with a recurring object; never shown on a slide.
- **Make:** image 1 `ref-cast.jpg`, for the drawing style and the robots'
  arms.
- **Shows:** each recurring object once, clearly apart from the others.

```text
Create a prop sheet for the same minimalist comic as image 1, in exactly its drawing style: one clean drawing on a pure white background, landscape 16:9, with no characters in it. Sixteen objects stand well apart from each other in three loose rows, each drawn once, large enough to show its details:

1. a thick folder with a solid black cover, closed with a round red wax seal
2. a plain white folder drawn in outline
3. a clipboard holding a sheet of a few thin lines
4. a slim booklet with a solid black cover, hanging from a nail
5. a small rack hanging from a nail, with three hooks holding spare clip-on arms of the worker robot's kind from image 1: one ending in a round magnifying glass, one in a small pair of tweezers, one in a small brush
6. a short white candle in a small holder, its flame lit
7. a small censer: a round metal bowl with a domed, pierced lid, hanging on three thin chains, a thin curl of smoke rising from it
8. a ring of a few large keys
9. a thick mail-order catalogue whose cover shows only a robot silhouette
10. a round needle gauge whose arc runs from open on the left to solid black at the right end, with no numbers
11. a small two-drawer filing cabinet, its top drawer open and full of index cards with black tabs
12. a small boxy machine with a crank, printing a sheet
13. the same machine under a clear glass bell dome drawn in outline, with two narrow slots in the dome's base, one where paper goes in and one where printed sheets come out
14. a plain card on a lanyard with a small hourglass icon
15. a low boom barrier striped black and white, bolted to the floor, with a heavy padlock hanging on it
16. a plain archive box with a lid, filled in solid black

The wax seal is red and the candle's flame amber: these are the only two colours on the sheet. The catalogue, the card, the index cards and the gauge show nothing but the shapes named here.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** sixteen objects; red only on the seal, amber only on the flame;
  the arms on the rack of the worker's kind; the catalogue cover with a
  silhouette and nothing else; the gauge without numbers; the card with the
  hourglass only.
- **Made on 2026-10-07**, one sample, kept: all sixteen objects, no
  lettering at full size, red and amber where named. The catalogue's
  silhouette is a robot with legs, the machine under the dome has lost its
  crank, and the booklet's cover carries a blank label; none of it matters
  for the scenes, whose prompts name these objects anyway.

### 3 · `ref-basement.jpg` — the basement

- **Used by:** every basement scene; never shown on a slide.
- **Make:** image 1 `ref-cast.jpg`, image 2 `ref-props.jpg`; `num_images` 2.
- **Shows:** the basement as the white page with its few objects, nobody in
  it, in the wide view most scenes use, with the place of every later object
  fixed. From left to right: the steel door to the share in its frame near
  the front; the wall shelf, the sealed folder's place, with free floor in
  front of it for the gatekeeper; two bare nails for the rulebook and the arm
  rack; the workbench in the middle with the machine on it and free floor at
  its left end for the filing cabinet; the cork board above it; the stairs
  rising on the right, the key hook at their foot within reach of the
  bench's right end, and open space under their high end for the glass room
  of 5.3. High up, the small pointed window; from the top edge, the bulb.

```text
Create a set reference for the same minimalist comic, in exactly the drawing style of images 1 and 2: a basement workroom with nobody in it, one single wide scene, landscape 16:9. Use image 2 only for the small boxy printing machine with the crank and the ring of keys; draw none of the characters from image 1.

No walls are drawn: the basement is the white page with a few objects on one thin floor line, seen from the front in a wide view. From left to right:
- near the front on the left, a heavy closed steel door standing upright in its frame, with nothing around it;
- a plain wooden wall shelf at chest height, empty, with open floor in front of it;
- two bare nails at head height, side by side, with nothing on them;
- in the middle, a long wooden workbench with the small boxy printing machine on it and a free patch of floor at its left end; above the workbench, a cork board crowded with blank square sticky notes;
- on the right, a few steep wooden steps of a stair rising towards the top right, with open space under their high end at the back; at the foot of the stairs, within arm's reach of the right end of the workbench, a small key hook holding the ring of keys.
High up in the middle, a small window with a pointed gothic arch, like a tiny chapel window, its panes left white. A single bare bulb hangs on its cord from the top edge of the picture.

There is no colour in this picture.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** nobody in the picture and no walls; the order from left to
  right as listed; the steel door on the left; the space under the stairs
  empty; the key hook within reach of the bench's right end.
- **Made on 2026-10-07**, two samples. The first is the plate: everything in
  the order listed, seen from the front, no colour and no lettering; it adds
  a second, shorter line behind the floor line, which reads as the back of
  the floor. The second drew the floor as a room in perspective, with the
  stairs cut off at the right edge.

---

## The two priority images

### 4 · `beat-04-hooks-3.jpg` — 4.3 Locks, not signs

- **Slide:** 4.3, the whole slide.
- **Make:** image 1 `ref-cast.jpg`, image 2 `ref-props.jpg`, image 3
  `ref-basement.jpg`; `num_images` 2.
- **Shows:** the worker's write is stopped by something bolted to the floor,
  not by a rule, and the way to the work data stays open.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the characters, at the sizes shown there), image 2 the prop sheet (the objects), image 3 the basement plate (the drawing of the place). Draw only what this prompt names.

A corner of the basement in a side view that reads from left to right, on one thin floor line. On the left, the worker robot stands at its wooden workbench and stretches one gripper far to the right, a small feather duster in it, reaching for the thick folder with the solid black cover and the round red wax seal, which stands upright on a low shelf on the far right. In the middle, at a checkpoint, the gatekeeper stands bolted to the floor: its round red paddle, plain and blank, presses flat against the worker's outstretched gripper and stops it. Behind the gatekeeper, directly in front of the sealed folder, the low black-and-white striped barrier with its heavy padlock blocks the way; the folder stays in plain view above it. From the workbench a second path, open and unblocked, curves towards the front to a low table with a plain white folder on it, and the worker's eyes have turned towards that open path.

Characters, as on the cast sheet: the worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The gatekeeper is a squat, faceless steel post bolted to the floor on a base plate with big bolts, a guard's peaked cap, one round lamp, and one jointed arm holding up a blank round red paddle.

The only colours are the red of the wax seal and the red of the paddle.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the paddle touches the gripper and carries no letters; the
  barrier stands between the gatekeeper and the folder, and the folder shows
  above it; the open path leads to the white folder; the worker on one
  wheel.
- **Made on 2026-10-07**, two samples. The second is the image. The first
  drew the open path as three loose lines and laid an open book on the low
  table instead of the white folder.

### 5 · `beat-08-team-1.jpg` — 8.1 One task, seven mechanisms

- **Slide:** 8.1, the whole slide. Image 24 takes its office from this one.
- **Make:** image 1 `ref-cast.jpg`, image 2 `ref-props.jpg`; `num_images` 2.
- **Shows:** the office the workers have moved into: six objects round the
  worker, and the room itself as the seventh.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the characters, at the sizes shown there), image 2 the prop sheet (the objects). Draw only what this prompt names.

A cutaway of a small single-storey office building with its front wall removed, seen slightly from above like a dollhouse: a wide, calm, symmetrical view into one tidy room. The cut edges of the walls show how thick and solid they are. In the left wall is a closed door, and on the wall's outer face beside it a badge reader: a plain box with one small lamp, no keypad and no screen.

Inside, the worker robot works calmly at a wooden workbench in the centre of the room. Around it, each in its own clear place:
- on the back wall, upper left: the slim booklet with the solid black cover hanging from a nail, and beside it the small rack of spare clip-on arms, all three on their hooks;
- in the middle of the back wall: one wide window, and on the wall beside it the round needle gauge, its needle low, at the open end;
- in the back right corner: a small room with a full-height glass wall and a glass door with a letterbox slot, the reviewer robot sitting inside at its own bare desk;
- on the left, between the workbench and the left wall: a low shelf with the thick folder with the solid black cover and the round red wax seal; directly in front of it the low black-and-white striped barrier with its padlock; in front of the barrier, facing the workbench, the gatekeeper, bolted to the floor, its blank round red paddle raised;
- beside the workbench, on its left: the small two-drawer filing cabinet, its top drawer open and holding a single index card.
The only other papers in the room are plain white folders.

Characters, as on the cast sheet: the worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The reviewer robot is smaller and slimmer than the worker, an egg shape with smooth, unbroken sides, one large round lens as its only eye, the same solid black band and short antenna as the worker, a narrow strip of paper from a slot in its chest. The gatekeeper is a squat, faceless steel post bolted to the floor on a base plate with big bolts, a guard's peaked cap, one round lamp, and one jointed arm holding up a blank round red paddle.

The only colours are the red of the wax seal and the red of the paddle.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** all seven read at a glance: booklet, arm rack, gatekeeper with
  barrier and sealed folder, reviewer in its glass room, window with gauge,
  filing cabinet, thick walls with the door and its reader. No black archive
  box; the worker without its skill arm.
- **Made on 2026-10-07**, two samples and one fix. The first is the image:
  it drew the gauge high, at its solid black end, although the prompt says
  low, and an edit that changed only the needle set it low. The second
  added a bookcase that the prompt does not name.

---

## The rest, in story order

### 6 · `beat-00-title-1.jpg` — 0.2 A little house

- **Slide:** 0.2, the whole slide, since 2026-10-28: the house opens the
  story (the author's request). Until then it stood on the title slide,
  shown small (4.3 inches wide) between the title and the Evidenze earth.
- **Make:** no generation. Copy `studies/bw-15-title-amber.jpg` to
  `slides/beats/beat-00-title-1.jpg`. It was made in round 2 of the studies
  by edits O and P (`studies/README.md`), which remake it if needed, and its
  near-white is already white.
- **Shows:** night, and one lit basement window with a pointed arch: someone
  down there is switching something on and hoping.
- **Check:** done on 2026-10-07: one clear shape, the amber window the only
  colour, no text.

### 7 · `beat-01-alone-1.jpg` — 1.1 More ideas than hands

- **Slide:** 1.1, the whole slide.
- **Make:** images 1, 2, 3 (`ref-cast`, `ref-props`, `ref-basement`).
- **Shows:** one man, a wall of ideas, and the folder that must never change.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man), image 2 the prop sheet (the sealed folder), image 3 the basement plate (the place, in the same wide view). Draw only what this prompt names.

The basement at night: the bare bulb is on, and the small pointed window high up is filled with solid black. The man sits hunched on a stool at the workbench, seen from the side, typing on a laptop whose screen faces away from us; one hand rubs his tired eyes. A cold mug stands beside the laptop. Above the workbench the cork board is crowded with blank sticky notes pinned in overlapping layers; a few have come loose and drift to the floor. Left of the workbench, on the wall shelf, the thick folder with the solid black cover and the round red wax seal stands on its own, carefully placed. The heavy steel door on the left is closed. There are no robots anywhere.

The man, as on the cast sheet, at the first stage (praying): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood up over his head, his face clearly visible inside it.

The only colour is the red of the wax seal.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the seal is the only colour; the hood up; no robot.
- **Made on 2026-10-07**, one sample, kept.

### 8 · `beat-01-alone-2.jpg` — 1.2 The catalogue arrives

- **Slide:** 1.2, the whole slide. Image 17 copies the catalogue's two pages
  from this one.
- **Make:** images 1, 2, 3.
- **Shows:** the offer of workers with attributes, and a man not yet
  convinced.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the two robots), image 2 the prop sheet (the catalogue), image 3 the basement plate (the place). Draw only what this prompt names.

Morning in the basement: a few short lines of light fall from the small pointed window high up. The man sits on the bottom step of the wooden stairs on the right and holds the thick mail-order catalogue open in front of his chest, turned towards us, so that both pages face the viewer upright. A small torn plain envelope lies close beside his hip on the step, with no stamp and no address, well clear of the bottom right corner. Each open page shows one large upright drawing of a single robot on plain white: the left page the worker robot from image 1, the right page the reviewer robot from image 1, egg-shaped, with one lens and smooth sides. Above the catalogue the man has one eyebrow raised and his lips pressed together: not yet convinced. Behind him, smaller, the workbench with the printing machine and the crowded cork board.

The man, as on the cast sheet, at the first stage (praying): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood up over his head, his face clearly visible inside it.

Show the man and the open catalogue large, so that both robot drawings read clearly at slide size. The catalogue pages hold only the two drawings.

There is no colour in this picture.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the two drawings are recognisably the worker and the reviewer;
  the pages face us; the envelope and the pages are blank; the envelope
  clear of the slide number's corner.
- **Made on 2026-10-07**, one sample and one fix. The sample laid the
  envelope in the bottom right corner, under the slide number's leaf, and
  the stairs reach the right edge, so the drawing cannot move left. Edit 8a
  made the envelope smaller; its tip now just meets the leaf's edge:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man as drawn. Change only this:
  1. The torn envelope on the step is drawn at half its present size and lies close beside the man's hip, so that its far end stays well clear of the bottom right corner of the picture; the lines of the step run on unbroken where it lay before.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the envelope is plain. Landscape 16:9.
  ```

### 9 · `beat-01-alone-3.jpg` — 1.3 Switching it on

- **Slide:** 1.3, the whole slide. Image 25 is made from this one, so its
  framing returns at the end of the talk.
- **Make:** images 1, 2, 3, and image 4 `studies/bw-16-scene-1-3-a4.jpg`
  for the framing; `num_images` 2.
- **Shows:** the first worker switched on with a candle lit, incense burning
  and fingers crossed: praying for success.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the worker robot, at the sizes shown there), image 2 the prop sheet (the candle and the censer), image 3 the basement plate (the place), image 4 an earlier draft of this scene, for its framing only. Draw only what this prompt names.

Evening in the basement, framed as in image 4: the workbench in the middle on one thin floor line, the bare bulb hanging on its cord from the top edge, switched on. The worker robot stands on the workbench next to a laptop whose screen faces away from us; its two round eyes are just switching on for the first time, shown by a few short lines radiating from them. The man leans towards it from the left, both hands raised in front of his chest with the fingers crossed, hopeful and a little anxious. Beside the robot, on the bench, burns the short white candle in its small holder; the small censer hangs on its three chains from a hook at the right end of the bench, a thin curl of smoke drifting over the robot. Behind them the cork board is crowded with blank sticky notes, and high up the small pointed window is filled with solid black.

Characters, as on the cast sheet: the man at the first stage (praying): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood up over his head, his face clearly visible inside it. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

The only colour is the amber of the candle's flame.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the crossed fingers are clearly visible; the flame amber and the
  censer smoking; the cork board and the window in the frame, because 8.2
  changes both; the laptop screen faces away.
- **Made on 2026-10-07**, two samples. The first is the image; the second
  moved the cork board to the far right, away from its place on the
  basement plate.

### 10 · `beat-02-claude-md-1.jpg` — 2.1 Fast, and in its own style

- **Slide:** 2.1, the whole slide. Image 11 is an edit of this one.
- **Make:** images 1, 2, 3.
- **Shows:** fast work in the wrong house style, corrected by hand.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the worker robot, at the sizes shown there), image 2 the prop sheet, image 3 the basement plate (the place). Draw only what this prompt names.

Morning at the workbench, a medium-wide view of the bench. The worker robot stands on the workbench and proudly holds up one end of a long printed table, a wide sheet with a grid of blank cells. The man stands in front of the bench, holds the other end, frowns, and draws circles round several cells with a black pen. A blank square sticky note is stuck to the robot's black chest band: it is the first note from the top of the cork board behind them, which now has one empty spot at the top. At the left end of the bench a single bare nail sticks out at head height.

Characters, as on the cast sheet: the man at the second stage (learning): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape, his sleeves pushed up, a small censer hanging cold from his rope belt. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

There is no colour in this picture: the man corrects in black.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the circles are black; the cells are empty; the bare nail is in
  the picture, because image 11 hangs the rulebook on it; the hood down.
- **Made on 2026-10-07**, one sample, kept.

### 11 · `beat-02-claude-md-2.jpg` — 2.3 The onboarding document

- **Slide:** 2.3 (2.2 until 2026-10-19), the whole slide.
- **Make:** image 1 `beat-02-claude-md-1.jpg` (the picture being edited),
  image 2 `ref-props.jpg`.
- **Shows:** the worker reads the house rules by itself; nobody corrects
  anything.

```text
Edit image 1. Keep the camera, the framing, the drawing style and the objects exactly as they are, and keep the man and the worker robot exactly as drawn. Use image 2, the prop sheet, only for the slim booklet with the solid black cover. Change only this:
1. The slim booklet with the solid black cover now hangs from the bare nail at the left end of the bench.
2. Remove the long printout, the circles and the pen.
3. The worker robot stands on an upturned wooden crate on the workbench, right beside the hanging booklet, head tilted back, reading its open pages, its eyes bright.
4. The man, a mug in his hand, walks past in the background without stopping, relaxed; his hood stays down and the censer hangs cold from his belt.
Everything else stays exactly as it is. Black and white only, pure white background, no grey. No text anywhere: the booklet's pages show only a few thin lines. Landscape 16:9.
```

- **Check:** same framing as image 10; no printout and no circles; the
  booklet's pages unlettered.
- **Made on 2026-10-07**, one edit, kept.

### 12 · `beat-03-skills-1.jpg` — 3.1 Every check a little different

- **Slide:** 3.1, the whole slide. Image 13 is an edit of this one.
- **Make:** images 1, 2, 3.
- **Shows:** a review without a procedure: the worker makes the spec agree
  with the export by editing the spec.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the worker robot, at the sizes shown there), image 2 the prop sheet (the booklet, the clipboard, the printing machine), image 3 the basement plate (the place). Draw only what this prompt names.

Daytime in the basement, a medium-wide view of the workbench with the stairs on the right. The slim booklet with the solid black cover hangs from its nail at the left end of the bench. On the workbench lies the clipboard, and beside it a loose printout fresh from the small boxy printing machine; the printout's grid has one more column than the sheet on the clipboard. The worker robot, a big eraser in one gripper and a pencil in the other, is busily redrawing the grid on the clipboard sheet to match the printout; eraser crumbs are everywhere. On the stairs at the right, a few steps up and on his way down, the man stops dead, his mug halfway to his mouth.

Characters, as on the cast sheet: the man at the second stage (learning): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape, his sleeves pushed up, a small censer hanging cold from his rope belt. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

There is no colour in this picture.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the grid difference (one column more) is visible; free white
  beside the booklet, where image 13 hangs the arm rack.
- **Made on 2026-10-07**, one sample and two fixes. The sample hung the ring
  of keys from the man's belt, two stages early, and left out the censer;
  an edit moved the keys to a small hook at the foot of the stairs and hung
  the cold censer on his belt. Read without the script, the printout showed
  lines of text, so nothing tied it to the grid being redrawn; edit 12a
  turned it into a grid. Its column count does not show the extra column,
  but the two grids now read as a table and the copy made to match it:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man and the worker robot as drawn. Change only this:
  1. The loose printout coming out of the small printing machine shows a plain grid of empty cells, five columns wide, instead of lines.
  2. The grid on the clipboard has four columns, and the worker robot is drawing a fifth column onto it with its pencil, so that it matches the printout.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the grids have empty cells. Landscape 16:9.
  ```

### 13 · `beat-03-skills-2.jpg` — 3.2 The procedure binder

- **Slide:** 3.2, the whole slide.
- **Make:** image 1 `beat-03-skills-1.jpg`, image 2 `ref-cast.jpg` (figure
  6, the skill arm), image 3 `ref-props.jpg` (the arm rack).
- **Shows:** the procedure clipped on for the job, and the eraser out of
  reach while it runs.

```text
Edit image 1. Keep the camera, the framing, the drawing style and the objects exactly as they are, and keep the man and the worker robot as drawn. Use image 2, the cast sheet, only for the worker robot's skill arm, and image 3, the prop sheet, only for the rack of spare arms. Change only this:
1. Beside the booklet on its nail now hangs the small rack of spare clip-on arms from image 3, with one of its three hooks empty.
2. The worker robot wears the arm from that hook: a slim jointed arm clipped into a socket on its back rises over its head and holds a round magnifying glass in front of its eyes. With its own grippers it lays the printout beside the clipboard and compares them, calm and methodical; the pencil lies untouched.
3. The big eraser lies alone on a high shelf, in plain view and out of the robot's reach. There are no eraser crumbs anywhere, and the sheet on the clipboard is intact and tidy.
4. The man has come down the stairs and now stands near the right end of the workbench, reading a single short sheet and nodding.
Everything else stays exactly as it is. Black and white only, pure white background, no grey. No text anywhere: paper shows only a few thin lines. Landscape 16:9.
```

- **Check:** one hook of the rack empty and its arm on the worker; the
  eraser in plain view and out of reach; the rack unlettered.
- **Made on 2026-10-07**, one edit and two fixes. The edit hung a second
  booklet below the first and lost the man's censer; a second edit took
  the lower booklet away and gave him the censer back. The eraser then sat
  in a closed box, which read as an archive box, and archive boxes stand
  for real data in this talk; edit 13a, with image 2 `beat-03-skills-1.jpg`
  for the eraser's shape, put the eraser itself on the shelf:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man and the worker robot as drawn. Use image 2 only for the shape of the big eraser. Change only this:
  1. The closed box on the high shelf is gone; in its place the big eraser from image 2 lies alone on that high shelf, in plain view and well out of the worker robot's reach.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
  ```

### 14 · `beat-04-hooks-1.jpg` — 4.1 The afternoon it tidied

- **Slide:** 4.1, the whole slide. Image 15 takes its objects from this one.
- **Make:** images 1, 2, 3.
- **Shows:** a rule that is usually followed, on the afternoon it is not:
  the production folder opened and tidied.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the worker robot, at the sizes shown there), image 2 the prop sheet (the sealed folder, the booklet, the rack of arms), image 3 the basement plate (the place, in the same wide view). Draw only what this prompt names.

An afternoon in the basement. The thick folder with the solid black cover lies open on the workbench, its round red wax seal broken in two. The worker robot holds a small feather duster in one gripper and cheerfully lifts a single page out of the folder with the other; a crumpled page already lies in a wastepaper basket beside the bench. A big eraser lies on the bench. Left of the bench hang the slim booklet with the solid black cover on its nail and, beside it, the small rack with all three spare arms on their hooks. Further left, the wall shelf where the folder normally stands is empty. At the foot of the stairs on the right, the man stands frozen, a half-eaten sandwich in his hand, his mouth open.

Characters, as on the cast sheet: the man at the second stage (learning): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape, his sleeves pushed up, a small censer hanging cold from his rope belt. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

The only colour is the red of the broken wax seal.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the seal visibly broken; the empty shelf, the booklet and the
  full rack all in the picture; the worker pleased, not guilty, and without
  its skill arm.
- **Made on 2026-10-07**, one sample and one fix. The sample hung the keys
  from the man's belt; an edit moved them to the hook at the foot of the
  stairs and kept the censer.

### 15 · `beat-04-hooks-2.jpg` — 4.2 A sign on the door

- **Slide:** 4.2, the whole slide.
- **Make:** image 1 `ref-cast.jpg`, image 2 `ref-props.jpg`, image 3
  `beat-04-hooks-1.jpg`.
- **Shows:** saying it louder: a bigger sign, which the worker rolls past.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the worker robot, at the sizes shown there), image 2 the prop sheet (the sealed folder, the booklet, the rack of arms), image 3 the previous scene in the same basement (where things stand). Draw only what this prompt names.

The part of the basement left of the workbench, as in image 3: the slim booklet with the solid black cover on its nail, the rack of spare arms beside it, and further left the wall shelf. The thick folder with the solid black cover stands back on that shelf, its red wax seal visibly cracked. The man, on tiptoe, pins a large pictogram to a small board right beside the booklet: an open hand inside a red circle with a red diagonal bar, and nothing else on it. An identical, smaller pictogram already hangs beside it. Behind his back the worker robot rolls past both signs and the booklet towards the wall shelf, contentedly, not looking up.

Characters, as on the cast sheet: the man at the second stage (learning): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape, his sleeves pushed up, a small censer hanging cold from his rope belt. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

The only colours are the red of the cracked wax seal and the red of the two pictograms.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the pictograms carry no words; the worker heads for the shelf;
  the seal is cracked, not whole.
- **Made on 2026-10-07**, one sample and one fix. In the sample the worker
  stood still; an edit set it rolling towards the shelf, one gripper
  reaching for the folder. Two spare drawing pins below the arm rack stay.

### 16 · `beat-05-subagents-1.jpg` — 5.1 Marking its own homework

- **Slide:** 5.1, the whole slide.
- **Make:** images 1, 2, 3; `num_images` 2.
- **Shows:** the worker approves its own work and misses the blot.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man, the worker robot and the gatekeeper, at the sizes shown there), image 2 the prop sheet (the printing machine), image 3 the basement plate (the drawing of the place). Draw only what this prompt names.

The basement, a medium view of the workbench, which stands in the middle of the picture. On the bench lies a pile of freshly printed sheets, each a grid of blank cells, drawn large and close to the viewer. The top sheet has one solid black blot in one cell, clearly visible. The worker robot stands at the bench and has just stamped a big, bold tick onto that same top sheet, right beside the blot: a large rubber stamp is lifted in one gripper, and the tick on the sheet is the classic check-mark shape, a short stroke down to the left and a long stroke up to the right. The robot's eyes are closed in contentment, drawn as two small upward arcs; it does not look at the blot. At the far end of the bench stands the small boxy printing machine. On the right, at about three quarters of the picture's width, the man leans against a plain wooden door frame standing free on the white page, without rivets and without a door in it; his arms are folded, one eyebrow raised, his mouth a flat, unsmiling line: sceptical. Far back on the left, small, the gatekeeper stands bolted to the floor, its paddle lowered at its side; there is no barrier, no shelf and no folder in this picture.

Characters, as on the cast sheet: the man at the third stage (organising): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape; nothing hangs from his rope belt. The worker robot is hip-high, the top of its head level with the man's hip: a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The gatekeeper is a squat, faceless steel post bolted to the floor on a base plate with big bolts, a guard's peaked cap, one round lamp, and one jointed arm holding a blank round red paddle, here lowered at its side.

Keep the bottom right corner of the picture empty: in the right twelfth of the width and the lowest tenth of the height there is nothing but the floor line.

The only colour is the red of the gatekeeper's paddle. The tick is a plain check-mark shape, and the stamp's face is blank.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the blot and the tick on one sheet and readable at slide size;
  the tick and the stamp have no letters; the man unsmiling, in a plain
  frame, with no censer on his belt; the gatekeeper small, one arm, paddle
  down; the corner free.
- **Made on 2026-10-07**, twice. The first prompt said only "a door frame"
  and named the barrier and the sealed folder; its one sample stamped a
  separate sheet beside the blotted pile, drew the riveted steel door of the
  share, a smiling man and the barrier fixed to the gatekeeper, and read,
  without the script, as "the guardrails work". This prompt then made two
  samples. The first drew the robot almost as tall as the man; the second
  is the image, but its gatekeeper had two arms and held the paddle up. An
  edit that named only the arms drew the gatekeeper twice as large in the
  foreground; edit 16a, which holds its size and place, is the fix:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man and the worker robot as drawn. Keep the small gatekeeper at the far left exactly where it stands and exactly as small as it is now, far back in the picture; do not move it and do not enlarge it. Change only its arms:
  1. The gatekeeper has one single jointed arm on its right side: remove the second arm on its left side. That one arm holds the round red paddle lowered beside the gatekeeper's base, pointing down, not raised.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colour is the red of the gatekeeper's paddle. No text anywhere. Landscape 16:9.
  ```

### 17 · `beat-05-subagents-2.jpg` — 5.2 Back to the catalogue

- **Slide:** 5.2, the whole slide.
- **Make:** image 1 `ref-cast.jpg`, image 2 `beat-01-alone-2.jpg`.
- **Shows:** the one he skipped: a worker that may look but not touch.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the worker robot, at the sizes shown there), image 2 the earlier scene with the open catalogue (its two pages). Draw only what this prompt names.

A close view of the workbench in the basement. The man sits at the bench with the thick mail-order catalogue open in front of him at the same two pages as in image 2: the worker robot on the left page, the reviewer robot on the right page. One of his fingers rests on the drawing of the reviewer robot. The worker robot peers over his shoulder, slightly put out, its round eyes narrowed.

Characters, as on the cast sheet: the man at the third stage (organising): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

Show the open catalogue large enough that both robot drawings read clearly at slide size.

There is no colour in this picture.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the pages match image 8; the finger is on the reviewer; the
  drawn reviewer has no arms.
- **Made on 2026-10-07**, one sample, kept.

### 18 · `beat-05-subagents-3.jpg` — 5.3 A fresh pair of eyes

- **Slide:** 5.3, the whole slide.
- **Make:** images 1, 2, 3.
- **Shows:** a reviewer in a room of its own, with nothing to write with;
  only its strip comes out.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the reviewer robot), image 2 the prop sheet (the clipboard, the printing machine), image 3 the basement plate (the open space under the high end of the stairs at the back on the right). Draw only what this prompt names.

The basement, looking towards the open space under the high end of the stairs at the back on the right. A small new glass room stands there, drawn in outline: a full-height glass wall with a glass door, and a letterbox slot in the door. Inside, the reviewer robot sits at its own small, bare desk with nothing on it to write with, bending its large lens over the clipboard and a printout. One narrow strip of paper is pushed halfway out through the letterbox slot. In the front left is the worker's cluttered side: the corner of the workbench with papers, tools and the small boxy printing machine. From there the man, seen from behind at the edge of the picture, reaches for the strip.

Characters, as on the cast sheet: the man at the third stage (organising), seen from behind: his very short hair a thin solid black cap, his hood down behind the short rounded shoulder cape of his long plain robe, a rope belt. The reviewer robot is smaller and slimmer than the worker, an egg shape with smooth, unbroken sides, one large round lens as its only eye, the same solid black band and short antenna as the worker, a narrow strip of paper from a slot in its chest.

There is no colour in this picture.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the reviewer has no arms and its desk no pen; the strip passes
  through the slot; the glass room under the stairs, as on the plate.
- **Made on 2026-10-07**, one sample and one fix. The reviewer grew arms at
  its desk and held the clipboard; an edit gave it the smooth sides of the
  cast sheet and laid the clipboard flat on the desk. The glass room's right
  edge stood under the slide number's leaf, so the drawing was moved 168 px
  to the left on its white ground, the floor line run on to its old end.

### 19 · `beat-06-context-1.jpg` — 6.1 The meeting that never ends

- **Slide:** 6.1, the whole slide. Image 20 is an edit of this one.
- **Make:** image 1 `ref-cast.jpg`, image 2 `ref-props.jpg`.
- **Shows:** one conversation never closed: the room fills up, the worker
  blurs, the bill grows.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man, the worker robot and the reviewer robot, at the sizes shown there), image 2 the prop sheet (the gauge). Draw only what this prompt names.

A meeting room in the evening, drawn without walls: a table on one thin floor line; behind it, in the middle, a wide window frame standing free on the white page; the round needle gauge directly to the right of the window; and on the right a door frame standing free, through which the reviewer robot sits at its own desk behind its glass wall in the next room.

The table is buried under stacks of paper, and more sheets are taped over the wide window until hardly any of it shows. Among the stacks lies a small heap of the reviewer's narrow paper strips, and a long blank paper receipt hangs off the edge of the table and curls across the floor. The worker robot sits at the table, dizzy, its eyes dim and drawn as small spirals. The gauge's needle stands high, close to the solid black end, not pinned. An empty recycling bin stands by the door frame. At the head of the table the man clutches a stack of paper to his chest and adds another sheet to it.

Characters, as on the cast sheet: the man at the third stage (organising): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The reviewer robot is smaller and slimmer than the worker, an egg shape with smooth, unbroken sides, one large round lens as its only eye, the same solid black band and short antenna as the worker, a narrow strip of paper from a slot in its chest.

There is no colour in this picture. The receipt is blank.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the needle is high but not pinned; the gauge has no numbers; the
  receipt is blank; the window and the gauge in the middle, because image 20
  keeps the frame.
- **Made on 2026-10-07**, one sample and one fix. The reviewer grew arms at
  its desk again; the same kind of edit took them off and cleared the desk.

### 20 · `beat-06-context-2.jpg` — 6.2 Meeting discipline

- **Slide:** 6.2, the whole slide.
- **Make:** image 1 `beat-06-context-1.jpg`.
- **Shows:** one topic, the minutes on the table, the rest in the bin.

```text
Edit image 1. Keep the camera, the framing, the furniture and the drawing style exactly as they are, and keep every character as drawn. Change only this:
1. The window is clear, with one neat sheet pinned in its corner.
2. The gauge's needle sits low, at the open end.
3. The table holds only a single plain white folder and one narrow paper strip; the stacks of paper and the long receipt are gone.
4. The worker robot sits upright, its round eyes bright.
5. The recycling bin by the door frame is full.
6. The man sits down at the table with an empty notepad.
The reviewer robot in the next room stays as it is. Everything else stays exactly as it is. Black and white only, pure white background, no grey. No text anywhere. Landscape 16:9.
```

- **Check:** same framing as image 19; the needle low; the bin full.
- **Made on 2026-10-07**, one edit of the fixed image 19, kept.
- **Since 2026-10-22** the window has no sheet and the table no strip
  (edit 45): the slide's clicks show /compact in a picture of its own, so
  this one shows /clear alone.

### 21 · `beat-07-memory-1.jpg` — 7.1 The Monday re-briefing

- **Slide:** 7.1, the whole slide. Image 22 is an edit of this one.
- **Make:** images 1, 2, 3.
- **Shows:** last week's briefing drawn again, while the filing cabinet
  stands unused.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man, the worker robot and the reviewer robot, at the sizes shown there), image 2 the prop sheet (the filing cabinet), image 3 the basement plate (the place). Draw only what this prompt names.

The basement on a Monday morning, the view running from the workbench on the left to the stairs on the right: a few short lines of first light fall from the small pointed window high up. Beside the workbench stands the small two-drawer filing cabinet, closed, a little dusty, ignored; at the far left hang the slim booklet with the solid black cover on its nail and the rack of spare arms. In the middle, the man stands at a whiteboard on an easel and draws a simple diagram of boxes and arrows; last week's identical diagram is still faintly visible as a complete ghost in thin dotted lines, in the same places, so that every box he has already drawn appears twice and the rest shows only as the ghost. The worker robot sits in front of him like a pupil, attentive and blank. In the background on the right, under the high end of the stairs, the reviewer robot sits undisturbed at its desk behind the glass wall of its small glass room. Above the workbench the cork board is filling up with new blank sticky notes again.

Characters, as on the cast sheet: the man at the third stage (organising): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The reviewer robot is smaller and slimmer than the worker, an egg shape with smooth, unbroken sides, one large round lens as its only eye, the same solid black band and short antenna as the worker, a narrow strip of paper from a slot in its chest.

There is no colour in this picture. The whiteboard shows only boxes and arrows.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the ghost diagram reads as the same diagram; the whiteboard has
  no letters; the filing cabinet closed and in the picture.
- **Made on 2026-10-07**, one sample and one fix. The worker stands beside
  the easel rather than before it like a pupil. The dotted boxes sat only
  where the man had not drawn yet, so they read as the rest of a plan, not
  as last week's copy; edit 21a drew the complete ghost under the fresh
  lines. Then the drawing moved 192 px to the left on its white ground, as
  did image 22, because the reviewer's wheel stood under the slide
  number's leaf; only the front floor line runs on to its old end:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every character as drawn. Change only this:
  1. On the whiteboard, last week's diagram is still faintly visible as a complete ghost in thin dotted lines: the same boxes and arrows the man is drawing now, in the same places, shifted only very slightly down and to the right. Where he has already drawn, his fresh solid lines run right beside the dotted ones, so every finished box appears twice; where he has not drawn yet, only the dotted ghost shows.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the whiteboard shows only boxes and arrows. Landscape 16:9.
  ```

### 22 · `beat-07-memory-2.jpg` — 7.2 The decision log

- **Slide:** 7.2, the whole slide.
- **Make:** image 1 `beat-07-memory-1.jpg`, image 2 `ref-props.jpg`.
- **Shows:** a log both can read: the worker before it starts, the man to
  check it.

```text
Edit image 1. Keep the camera, the framing, the drawing style and the objects exactly as they are, and keep every character as drawn. Use image 2, the prop sheet, only for the index cards in the filing cabinet. Change only this:
1. The filing cabinet's top drawer is open; it is full of index cards with black tabs.
2. The worker robot now stands beside the open drawer and, before starting work, reads one index card it has taken from it.
3. The man stands beside it, a mug in his hand, has pulled out another card and reads it himself, nodding.
4. The whiteboard is clean and unused.
The reviewer robot behind its glass wall stays as it is. Everything else stays exactly as it is. Black and white only, pure white background, no grey. No text anywhere: the cards show only a few thin lines. Landscape 16:9.
```

- **Check:** same framing as image 21; both read cards; the whiteboard is
  blank.
- **Made on 2026-10-07**, one edit, kept, and later moved 192 px to the left
  with image 21, so the two keep one camera.

### 23 · `beat-07b-isolation-1.jpg` — 7b.1 Just this once

- **Slide:** 7b.1, the whole slide. Slide 7b.2, a closer crop of it with
  rings round the gatekeeper and the dome, was dropped on 2026-10-15, and the
  dome came off by edit 23c ("Changed after the run-through").
- **Make:** images 1, 2, 3; `num_images` 2. This is the busiest scene.
- **Shows:** the real data on the bench, the reads leaving through the
  antenna, the keys within reach; the gatekeeper watches only the worker's
  own moves.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man, the worker robot and the gatekeeper, at the sizes shown there), image 2 the prop sheet (the dome over the machine, the black archive box, the sealed folder, the keys), image 3 the basement plate (the place, in the same wide view). Draw only what this prompt names.

The basement in the evening, the bare bulb on; the small pointed window high up is filled with solid black. On the left, the heavy steel door stands wide open in its frame: behind it a tall open steel rack full of plain solid black archive boxes. One archive box, carried out from the rack and filled in solid black like the boxes there, stands open on the floor in front of the workbench, and a continuous paper feed runs from it up into a slot in the base of the clear glass dome on the workbench. Under the dome the small boxy printing machine prints by itself, its crank turning, and printed sheets slide out through the dome's second slot. The worker robot sits on the workbench just right of the dome, outside it, reading each sheet as it comes out; a few short lines radiate from its antenna, and a thin stream of small white sheets leaves the antenna and rises in one curved trail to the small pointed window, each sheet a little smaller than the one before, with short motion lines pointing back towards the antenna; one pane of the window stands open, and the last sheets are already outside it in the night. Left of the workbench the gatekeeper stands bolted to the floor, alone, in front of the wall shelf with the sealed folder, whose cover carries only its red wax seal; it faces the bench, its paddle lowered and idle. The striped barrier is left out of this crowded scene. At the foot of the stairs on the right the ring of keys hangs on its hook, within easy reach of the robot's gripper, untouched. Halfway up the stairs, the man waves an absent-minded go-ahead over his shoulder without looking back.

Characters, as on the cast sheet: the man at the third stage (organising): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The gatekeeper is a squat, faceless steel post bolted to the floor on a base plate with big bolts, a guard's peaked cap, one round lamp, and one jointed arm holding a blank round red paddle, here lowered at its side.

Keep the gatekeeper, the dome and the worker robot close together in the lower middle of the picture, between about a sixth and three quarters of its width: the next slide shows a closer crop of that part.

The only colours are the red of the wax seal and the red of the gatekeeper's paddle.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the worker sits outside the dome; the stream starts at the
  antenna and leaves through an open pane; the keys hang within its reach;
  the paddle is down and the gatekeeper has no boom; the box is filled solid
  black and is fed into the dome; the sealed folder has no label. If the scene is too full, leave out the man on the
  stairs first; the spoken text says what he does.
- **After saving:** check the names on 7b.1 in `deck.yaml`; they were set
  for the picture of 2026-10-15.
- **Made on 2026-10-07**, two samples and one fix. The first is the image:
  it held the paddle up, as the gatekeeper's short form said, although the
  scene says lowered, and an edit lowered it; the short form in this prompt
  now says so too. The second drew a jointed arm over the barrier.
- **Fixed on 2026-10-07**, two edits, after the image was read without the
  script as sheets coming in through a closed window. It also drew the
  archive box white with a black lid, gave the sealed folder the rulebook's
  blank label and fixed the barrier's boom to the gatekeeper. The prompt
  above now says what the edits did. Edit 23a:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is. Change only this:
  1. The stream of small white sheets clearly flies away from the worker robot: it starts at the tip of the robot's antenna, between its short radiating lines, and rises in one curved trail up to the small pointed window, each sheet a little smaller than the one before, with two or three short motion lines behind each sheet pointing back towards the antenna.
  2. One pane of the small pointed window stands open, and the last two sheets of the trail are already outside it, small white shapes against the black night beyond the window.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red of the wax seal and the red of the gatekeeper's paddle. No text anywhere. Landscape 16:9.
  ```

  Edit 23b, on the result, with image 2 `ref-props.jpg`:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every figure as drawn. Use image 2, the prop sheet, only for the solid black archive box. Change only this:
  1. The open archive box on the floor in front of the workbench is filled in solid black, exactly like the boxes on the rack behind the open steel door; its lid lies beside it.
  2. The continuous paper feed comes out of that open black box and runs up into a narrow slot in the base of the glass dome; the printed sheets come out of a second slot on the other side of the dome's base, towards the worker robot.
  3. The thick black folder on the wall shelf carries only its round red wax seal: there is no white label on its cover.
  4. The gatekeeper stands alone, bolted to the floor: remove the striped boom from its post.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red of the wax seal and the red of the gatekeeper's paddle. No text anywhere. Landscape 16:9.
  ```

  The crop for 7b.2 in `deck.yaml` was then reset to this image and widened
  to take in the start of the stream. Both went on 2026-10-15.

### 24 · `beat-07b-isolation-3.jpg` — 7b.3 An office of its own

- **Slide:** 7b.3, the whole slide.
- **Make:** image 1 `ref-cast.jpg`, image 2 `ref-props.jpg`, image 3
  `beat-00-title-1.jpg` (the house), image 4 `beat-08-team-1.jpg` (the
  office).
- **Shows:** the workers move into an office of their own with a badge; the
  real data and the keys stay in the house.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man and the worker robot, at the sizes shown there), image 2 the prop sheet (the badge, the white folder, the filing cabinet, the black archive box, the keys), image 3 the house from the title picture, image 4 the office from the cutaway scene (its walls, window and door, now seen from outside). Draw only what this prompt names.

Night, told by solid black windows; the sky stays white. One thin ground line runs across a yard. On the left stands the narrow two-storey house from image 3, its upper windows solid black. Its basement window with the pointed arch is lit and left white inside, with no candle in it, and through it a few solid black archive boxes on a rack and the small filing cabinet are visible, both staying behind. The man stands at the house door. On the right, across the yard, stands the small single-storey office building from image 4: thick solid walls, one wide window, lit and left white, showing only its light, and one door with a badge reader beside it, a plain box with one small lamp. At that door the worker robot, carrying a plain white folder, holds its badge up to the reader: a plain card on a lanyard with a small hourglass icon. The black archive boxes appear only inside the house.

Characters, as on the cast sheet: the man at the fourth stage (in control): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape, a ring of keys hanging from his rope belt. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

There is no colour in this picture. The badge shows only the hourglass.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** no black box anywhere outside the house; the badge and the
  reader without lettering; the keys on the man's belt; no amber in the
  basement window. If the scene is too full, leave out the view through the
  basement window, as the storyline allows, and say on stage that the share
  stays behind.
- **Made on 2026-10-07**, one sample, kept.

### 25 · `beat-08-team-2.jpg` — 8.2 A company, not a keyboard

- **Slide:** 8.2, the whole slide.
- **Make:** two edits of image 9, because a single edit with all the changes
  would hold too many (one with seven returned no image on 2026-10-06). Step
  25a edits image 1 `beat-01-alone-3.jpg` with image 2 `ref-cast.jpg`; step
  25b edits the result of 25a with image 2 `ref-props.jpg` and is saved as
  `beat-08-team-2.jpg`.
- **Shows:** the frame of 1.3 again, in an evening much later: the same
  bench, bulb and candle, the man at the last stage, the candle just blown
  out, the wall down to one column, the office lit across the yard.

Step 25a:

```text
Edit image 1. Keep the camera, the framing, the drawing style, the workbench, the laptop, the candle and its holder, the hanging bulb, the hook at the right end of the bench, the cork board and the window exactly as they are. Use image 2, the cast sheet, only for the man at the fourth stage, the fourth man from the left. Change only this:
1. Replace the man with the man at the fourth stage from image 2: very short hair drawn as a thin solid black cap, heavy stubble drawn as fine dots, no glasses, his hood down behind the short rounded shoulder cape, a ring of keys on his rope belt. He now sits back relaxed on a simple wooden stool beside the left end of the workbench, a mug of tea held in both hands, fingers uncrossed, with a slight, content smile.
2. The worker robot is gone from the workbench, and the laptop is closed.
3. The candle has just been blown out: no flame, only a thin thread of smoke rising from its wick.
4. The censer on the hook hangs cold, with no smoke.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
```

Step 25b:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man exactly as drawn. Use image 2, the prop sheet, only for the filing cabinet. Change only this:
1. The cork board is tidy: its blank sticky notes hang in one neat column with plenty of room to spare, and none lie on the floor.
2. Beside the cork board hangs a simple organisation chart drawn as exactly three boxes joined by lines: a small person silhouette in the top box and, below it, two boxes side by side, the left one with a small silhouette of the worker robot (a square head with a short antenna, a box body with a black band, one wheel), the right one with a small silhouette of the reviewer robot (an egg shape with one round lens and a black band).
3. The small two-drawer filing cabinet stands on the floor just right of the workbench, close beside the censer, well clear of the bottom right corner of the picture.
4. The small pointed window high up keeps its white glazing bars and tracery; in one of its lower panes, far away across a yard, shows exactly one small, wide, lit window of the low single-storey office, left white inside the black. No other lit windows and no other buildings.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the chart has no words. Landscape 16:9.
```

- **Check:** same framing as image 9; no colour left in the picture; the
  smoke thread visible; the keys on the belt; the chart without words, a
  person in its top box and the worker and the reviewer below; one lit
  office window in the pointed window, which keeps its glazing bars.
- **Made on 2026-10-07**, steps 25a and 25b, one sample each, and one fix.
  Step 25b put a robot in the chart's top box and people below it, which
  turns the closing line on its head; an edit put the person on top and
  the robots below, and step 25b now says so. The filing cabinet stood in
  the bottom right corner, under the leaf, and the censer hangs too close
  beside it for the cabinet to move alone; so, as the author asked, the
  whole drawing was moved 120 px to the left on its white ground, with
  the floor line kept at its old ends, and step 25b now places the
  cabinet.
- **Fixed on 2026-10-07**, two edits, after the image was read without the
  script. The chart held four identical robots in two rows, so the cast of
  the story did not show in it, and the window held a lit block of many
  storeys instead of the low office. Edit 25c, with image 2 `ref-cast.jpg`
  and image 3 `beat-07b-isolation-3.jpg`, set both right but took the
  window's glazing bars; edit 25d, with the earlier image as image 2, put
  them back. Step 25b above now asks for both. Edit 25c:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man exactly as drawn. Use image 2, the cast sheet, only for the shapes of the two robots, and image 3 only for the low office building. Change only this:
  1. The organisation chart on the wall shows exactly three boxes joined by lines: a small person silhouette in the top box and, below it, two boxes side by side: the left one holds a small silhouette of the worker robot (a square head with a short antenna, a box body with a black band, one wheel), the right one a small silhouette of the reviewer robot (an egg shape with one round lens and a black band). No other boxes and no further rows.
  2. Through the small pointed window high up, far away across the yard, shows exactly one small, wide, lit window, low down and left white inside the black: the one window of the low single-storey office from image 3. No other lit windows and no other buildings.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the chart has no words. Landscape 16:9.
  ```

  Edit 25d:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man, the organisation chart and every object as drawn. Use image 2 only for the window. Change only this:
  1. The small pointed window high up gets back its white glazing bars and its pointed tracery, exactly as in image 2, with the panes solid black between them; in one of the lower panes, far away, shows the one small lit window of the low office, a small white rectangle. No other lit windows and no other buildings.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the chart has no words. Landscape 16:9.
  ```

## Added for beat 7a (2026-10-07)

Beat 7a, the post room, joined the storyline after the other 25 images were
made. Its two pictures sit between images 22 and 23 in the story and carry
the next numbers. The letter and its strings are new props, described in the
prompts only; the props plate was not made again for two pictures.

### 26 · `beat-07a-safety-1.jpg` — 7a.1 A letter for the worker

- **Slide:** 7a.1, the whole slide. Image 27 is an edit of this one.
- **Make:** images 1, 2, 3, and image 4 `beat-07-memory-2.jpg` for the camera;
  `num_images` 2.
- **Shows:** a letter whose strings pull the worker's gripper towards the
  keys, the reviewer undisturbed in its glass room, the man busy at the
  whiteboard and unaware.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man, the worker robot and the reviewer robot, at the sizes shown there), image 2 the prop sheet (the ring of keys, the filing cabinet), image 3 the basement plate (the place), image 4 a finished picture of the same place, used only for the camera and the framing. Draw only what this prompt names.

The basement on a Monday morning, framed exactly as image 4: the workbench on the left, the small two-drawer filing cabinet beside it, closed, and on the right a few steep wooden steps rising, with a hook at their foot holding the ring of keys. Under the high end of the stairs, at the back on the right, stands the small glass room, drawn in outline, with the reviewer robot sitting undisturbed at its own bare desk behind the glass. In the right foreground, at the foot of the stairs, the worker robot holds a long sheet of paper open in one gripper, tilted towards us: the letter shows only a few thin lines of scribble and, at its foot, one short thick black line. From the foot of the letter three thin, straight, taut lines run like a marionette's strings to the wrist of the worker robot's other gripper and pull that gripper out stiffly towards the ring of keys on its hook, one gripper's length away. The worker robot's eyes are wide, plain circles. On the left the man stands at a whiteboard on an easel, seen from behind, and draws a simple diagram of boxes and arrows; he has not noticed anything. Keep the bottom right corner of the picture empty.

Characters, as on the cast sheet: the man at the third stage (organising), seen from behind: very short hair drawn as a thin solid black cap, his hood down behind the short rounded shoulder cape of his long plain robe, a rope belt and plain trainers. The worker robot is hip-high, a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The reviewer robot is smaller and slimmer than the worker, an egg shape with smooth, unbroken sides, one large round lens as its only eye, the same solid black band and short antenna as the worker, a narrow strip of paper from a slot in its chest.

There is no colour in this picture. The letter has no seal, no stamp and no address. The whiteboard shows only boxes and arrows.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** three thin straight lines from the letter's foot to one gripper,
  not a scribble, a web or a band; the letter without lettering, seal or
  stamp; the keys on their hook; the reviewer without arms; no red or amber;
  the bottom right corner calm. If the model will not draw strings, ask for
  one thick straight rope from the letter to the gripper instead.
- **Made on 2026-10-08**, two samples and one fix. The first sample is the
  image: three thin lines run from the letter's foot to the worker's gripper,
  the key ring hangs from a hook on the stairs, and the reviewer sits under
  them. The second ran the lines between the keys and the worker's wheel,
  hung the hook in mid-air and gave the reviewer a booklet in its hand. The
  first gave the reviewer a small arm and hand on its desk; edit 26a, with
  image 2 `ref-cast.jpg`, took them off and changed nothing else. The glass
  room's right wall then stood in the slide number's corner, so the drawing
  was moved 160 px to the left on its white ground, the front floor line run
  on to its old end. Edit 26a:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every other character and object as drawn. Use image 2, the cast sheet, only for the reviewer robot. Change only this:
  1. The reviewer robot in the small glass room under the stairs has smooth, unbroken sides with nothing attached, exactly as the reviewer robot on the cast sheet: remove the small arm and hand that rest on the desk. It sits at its bare desk with its large lens turned towards the room.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
  ```

### 27 · `beat-07a-safety-2.jpg` — 7a.2 The post room

- **Slide:** 7a.2, the whole slide.
- **Make:** image 1 the picture 26 after edit 26a and before it is moved,
  image 2 `beat-05-subagents-3.jpg` (for the glass door and its slot);
  `num_images` 2.
- **Shows:** the letter on the clerk's desk, the strings slack, one strip
  through the slot into the worker's gripper, the keys untouched.

```text
Edit image 1. Keep the camera, the framing, the drawing style and the objects exactly as they are, and keep every character as drawn. Use image 2, a picture of the glass room, only for the glass door and its letterbox slot. Change only this:
1. The long sheet of paper is no longer in the worker robot's gripper: it lies open on the reviewer robot's bare desk inside the small glass room under the stairs, and the reviewer robot bends its large lens over it.
2. The three thin lines that ran from the foot of the sheet to the worker robot's gripper now lie slack and curled on the desk, their loose ends tied to nothing.
3. The front of the small glass room gets a glass door with a letterbox slot in it, as in image 2. The worker robot has rolled up to that door, beside the foot of the stairs, and holds up one gripper, calm, as one narrow strip of paper comes through the slot into it; its other gripper hangs relaxed at its side. The ring of keys still hangs untouched on its hook, in plain view.
4. The man now stands beside the easel, turned half towards us, a mug in his hand, watching; the whiteboard is clean.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the strip and the sheet show only a few thin lines. Landscape 16:9.
```

- **Check:** the sheet only on the desk, with its scribble and the thick line
  at its foot; the lines slack, not pulling; the strip passes through the
  slot into the gripper; the keys in view and untouched; the reviewer without
  arms, magnifying glass or booklet; the bottom right corner calm.
- **Made on 2026-10-08**, one edit with two samples and two fixes. The edit
  did not keep image 26's camera: it redrew the scene with a larger glass
  room under the stairs, a door with a slot and a chair, and the worker at
  the door. It read well, so the two pictures no longer share one camera.
  The first sample is the image: the strip passes into the worker's gripper,
  thin cords lie slack on the desk and the floor, the keys hang beside the
  worker. The second had no cords and a gripper that held nothing at the slot.
  The first gave the reviewer an arm and a magnifying glass; edit 27a, with
  `ref-cast.jpg`, took both off and left the sheet on the desk as a blank
  rectangle; edit 27b, with image 26 as image 2, gave it back its scribble
  and the thick line at its foot, in two samples, of which the first is kept.
  Edit 27a:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every other character and object as drawn. Use image 2, the cast sheet, only for the reviewer robot. Change only this:
  1. The reviewer robot inside the glass room has smooth, unbroken sides with nothing attached, exactly as the reviewer robot on the cast sheet: remove the magnifying glass and the small arm. It sits at the desk and bends its one large round lens over the sheet of paper.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
  ```

  Edit 27b:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every character as drawn; the reviewer robot keeps its smooth, unbroken sides with nothing attached. Use image 2 only for the look of the letter. Change only this:
  1. The sheet of paper lying on the desk inside the glass room is the letter from image 2: a long sheet showing a few thin lines of scribble and, at its foot, one short thick black line. The slack cords lie across it and over the edge of the desk as they do now.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
  ```

## Added for beat 7c (2026-10-08)

Beat 7c, where the sheets go, joined the storyline on 2026-10-08 with the
paper's chapter 10, whose figure its two pictures are. They follow image 24
in the story and carry the next numbers. The warehouse and the hourglass on
its wall are new props, described in the prompts only; the props plate was
not made again for two pictures.

### 28 · `beat-07c-data-1.jpg` — 7c.1 Where the sheets went

- **Slide:** 7c.1, the whole slide. Image 29 is an edit of this one.
- **Make:** image 1 `ref-cast.jpg`, image 2 `ref-props.jpg`, image 3
  `beat-07b-isolation-3.jpg` (the house, the office and the yard at night);
  `num_images` 2.
- **Shows:** the night of 7b.1 seen from the yard: black sheets fly from the
  open basement window into the gate of the model maker's warehouse, whose
  shelves hold black boxes, while the man, at the stage of that night,
  follows them with his eyes.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man, at the size shown there), image 2 the prop sheet (the solid black archive box, whose solid black fill the small sheets take), image 3 a finished picture of the same yard at night, used for the house, the office and the night. Draw only what this prompt names.

Night, told by solid black windows; the sky stays white. One thin ground line runs across a wide yard. On the left stands the narrow two-storey house from image 3, its upper windows solid black; its small basement window with the pointed arch, just above the ground, stands open. In the middle of the yard, smaller and a little further back, stands the small single-storey office from image 3, its one wide window solid black and its door closed. Far away on the right, on the ground line in the right third of the picture, stands one long, plain building much larger than the office: a flat roof, no windows, and one wide gate standing open; inside the gate, lit and left white, stand rows of tall shelves. Its right end stays well clear of the right edge of the picture. From the open basement window of the house a long trail of small sheets rises in one high curved arc over the yard and comes down into the open gate of the large building; every sheet is filled in solid black, exactly like the archive boxes, and each is a little smaller than the one before, with two or three short motion lines behind each sheet pointing back towards the house. Inside the gate, the lower shelves already hold a few solid black archive boxes, like the one on the prop sheet. In the yard between the house and the office the man stands with a plain mug in his hand and follows the trail with his eyes, one eyebrow raised. Keep the bottom right corner of the picture empty.

Characters, as on the cast sheet: the man at the third stage (organising): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem on the cape, a rope belt and plain trainers; his hood down behind the cape; nothing hangs from his rope belt.

There is no colour in this picture. The large building has no sign, no logo and no lettering.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** every sheet in flight filled solid black, the trail starting at
  the open basement window and ending in the gate; the office window dark;
  no lettering on the large building; the man at the third stage, without
  keys; the bottom right corner calm.
- **Made on 2026-10-08**, two samples. The first is the image: the arc reads
  from the house to the gate, and the man stands between the house and the
  office. Asked for "many small solid black sheets" on the shelves, it drew
  black archive boxes and a small stack of papers, which say the same, so
  the storyline's scene and this prompt now ask for boxes. It also ran the
  building to the right edge; the corner below it stays calm. The second
  sample drew heaps of sheets that shrank as asked, but stood the man by the
  house and added a line like a wall.

### 29 · `beat-07c-data-2.jpg` — 7c.2 Kept for a while

- **Slide:** 7c.2, the whole slide.
- **Make:** image 1 the picture 28, image 2 `ref-cast.jpg` (the man at the
  fourth stage), image 3 `ref-props.jpg` (the hourglass on the badge, the
  white folder); `num_images` 2.
- **Shows:** the same yard with the basement window shut: only a few white
  folders cross from the lit office into the warehouse, an hourglass hangs
  on its wall, and the man, his keys now on his belt, watches with a slight
  smile.

```text
Edit image 1. Keep the camera, the framing, the drawing style, the house, the office, the large building and the yard exactly as they are. Use image 2, the cast sheet, only for the man at the fourth stage, the fourth man from the left, and image 3, the prop sheet, only for the small hourglass on the badge and for the plain white folder. Change only this:
1. The small basement window of the house is closed, with no lines around it, and the long trail of black sheets is gone completely.
2. The office's wide window is lit and left white, and from it a short trail of exactly four small white sheets, drawn in outline like the plain white folder, rises in a low arc over the office roof and comes down into the open gate of the large building; each sheet is a little smaller than the one before, with short motion lines behind each sheet pointing back towards the office.
3. Inside the gate the shelves hold only those few small white sheets: the black boxes are gone. Above the gate hangs a plain hourglass, drawn like the one on the badge, about a third as tall as the gate.
4. The man is now the man at the fourth stage from image 2: very short hair drawn as a thin solid black cap, heavy stubble drawn as fine dots, no glasses, his hood down behind the short rounded shoulder cape, which keeps its small gear emblem with square teeth, a ring of keys hanging from his rope belt. He stands calmly in the same place with the mug in his hand and watches the short white trail with a slight smile.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere: the hourglass and the building carry no lettering. Landscape 16:9.
```

- **Check:** no black left in the warehouse and no black sheet in the air;
  the folders white and in outline; the hourglass without lettering, on the
  warehouse and not on the mug; the keys on the man's belt and the gear on
  his cape; the bottom right corner calm.
- **Made on 2026-10-08**, two samples and two fixes. The first sample is the
  image: it hung the hourglass on the wall beside the gate rather than above
  it, which reads as well, and drew five folders in the air instead of four.
  It also turned the gear on the man's cape into a flower. The second drew
  the hourglass on the man's mug. Edit 29a, with image 28 as image 2 for the
  emblem, brought image 28's black boxes back onto the shelves and was
  discarded; edit 29b, with `ref-cast.jpg`, put the gear back and kept the
  white folders. Item 4 above now names the gear, which the run did not.
  Edit 29b:

  ```text
  Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep the man exactly as drawn; keep the white folders on the shelves inside the open gate exactly as they are, with nothing black on those shelves. Use image 2, the cast sheet, only for the gear emblem on the man's cape. Change only this:
  1. The small emblem on the man's short rounded shoulder cape is a small gear with square teeth and a round hole in its middle, as on the capes in image 2, not a flower.
  Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
  ```

## Added for the goodbye (2026-10-09)

The author asked on 2026-10-09 for the cast to wave goodbye at the end of the
talk, in a GIF. It is image 30, shown on slide 8.3 at the end of the story
(on 9.2, after the questions, until 2026-10-28): a
loop of eight frames turned from one drawing, not a video, so it keeps the
line of every other picture.

### 30 · `beat-08-team-3.gif` — 8.3 Goodbye

- **Slide:** 8.3, the whole slide, before the closing slide (9.2, after the
  questions, as `beat-09-close-2.gif` until 2026-10-28). PowerPoint and
  LibreOffice play the GIF in the show.
- **Make:** in four steps.
  1. *The frame,* pose A, on Nano Banana 2.1's edit route with the settings
     above and `num_images` 2. The four characters go in as separate
     cut-outs on white, each with its neighbours' lines painted out: image 1
     the worker and image 2 the man, both already waving, from the first
     sample of the first try below; image 3 the reviewer and image 4 the
     gatekeeper from `ref-cast.jpg`. In pose A the waving parts lean out.
  2. *Two more poses,* as edits of the frame with the settings above: pose
     B, in which every waving part leans the other way (`num_images` 1), and
     pose M, in which every waving part points straight up and the strip
     hangs down (`num_images` 2). An edit redraws the whole picture a
     little, so step 4 takes only the hanging strip from pose M. Pose B
     belonged to the first GIF (below) and is no longer used.
  3. *Seven colours.* Turn each pose grey, set every grey above 225 to white
     and every grey below 60 to black, and put the colour back where the
     saturation is above 90 of 255, which is the paddle. Then map it without
     dithering onto seven colours: white, three even greys for the edges,
     black, the red (200, 40, 45) and a light red for the paddle's rim. The
     three poses are kept that way, 58 KB each, as `studies/anim-01` (A) to
     `anim-03` (B).
  4. *The GIF,* with `uv run python tools/goodbye_wave.py`. Its frame is
     pose A with the hanging strip of pose M, pasted where the two differ by
     more than 90 of 255 in grey, grown by 20 px. Each waving part is cut
     out along its own outline and put back turned by a sine of the frame
     number. The robots' forearms turn stiffly about their elbow balls, which
     are laid over them again. The man's hand and the strip bend: they do
     not turn where they leave the cuff and the belt, and turn fully towards
     the fingertips and the strip's end. The turns are 12° either way for
     the hand and the strip's end, 14° for the worker and 10° for the
     paddle, each part a quarter of a wave after the one before: the man,
     the paddle, the worker, the strip. Where the fold hid the reviewer's
     outline, the outline is drawn in. Every frame is mapped onto the seven
     colours and written whole, without transparency: eight frames of
     90 ms that loop for ever, 2752 × 1536 px and 571 KB since the worker's new eyes (569 KB with the frame in his own clothes, 548 KB before). The script holds
     the joints, the outlines' cuts and the turns in pixels of the frame.
- **Shows:** the cast in one row on one floor line, waving goodbye, each in
  its own rhythm: the worker with a gripper, the man at the last stage
  with his left hand and a mug in his right (the model drew the mirror of
  the prompt's hands, and it reads just as well), the reviewer's strip swinging
  from side to side, the gatekeeper with its red paddle.

Step 1, the frame:

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. The attached images are four separate character references; draw each character exactly as drawn there, in the same drawing style: image 1 the worker robot, image 2 the man, image 3 the reviewer robot, image 4 the gatekeeper. Draw each of them exactly once and nothing else.

The cast says goodbye to the audience: the four stand side by side on one thin black floor line that runs across the picture, all facing the viewer, like actors taking their leave at the end of a play. They stand close together in the middle of the picture with white space on both sides; the man is about two thirds as tall as the picture. From left to right:
1. The worker robot from image 1, hip-high: the top of its head is level with the man's hip. It raises one gripper high beside its head and waves to us; its other gripper hangs relaxed at its side.
2. The man from image 2: he holds a plain mug of tea in his left hand in front of his chest and raises his right hand high beside his head in a friendly wave, the open palm towards us, with a warm, slight smile.
3. The reviewer robot from image 3, a little smaller and slimmer than the worker: it turns its one large round lens towards us, and the narrow strip of paper from the slot in its chest flutters out to one side like a small waving ribbon.
4. The gatekeeper from image 4, its top level with the man's hip, bolted to the floor on its base plate: it raises its one jointed arm high and holds its blank round red paddle up, tilted to one side like a hand that waves goodbye.
Keep the top right corner and the bottom right corner of the picture empty.

Characters: the man: late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; a long plain hooded robe like a monk's with a short rounded shoulder cape over the shoulders and upper chest, a small gear emblem with square teeth on the cape, a rope belt and plain trainers; his hood down behind the cape, a ring of keys hanging from his rope belt. The worker robot: a rounded box body with a solid black band round its chest, a square head with two round eyes and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs. The reviewer robot: an egg shape with smooth, unbroken sides with nothing attached, one large round lens as its only eye, the same solid black band and short antenna as the worker, a narrow strip of paper from a slot in its chest. The gatekeeper: a squat, faceless steel post bolted to the floor on a base plate with big bolts, a guard's peaked cap, one round lamp, and one jointed arm holding up a blank round red paddle.

The gatekeeper's paddle is red: the only colour in this picture.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

Step 2, pose B:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every figure exactly where it stands and as drawn. This is the second frame of a simple waving animation, so change only the waving parts:
1. The man's raised right hand and forearm lean the other way: tilted over towards his head, the open palm still towards us.
2. The worker robot's raised gripper and forearm lean the other way: tilted over towards its head.
3. The gatekeeper's raised arm swings the round red paddle the other way: tilted over towards its cap.
4. The reviewer robot's paper ribbon flutters out to the other side of its body.
Everything else stays exactly as it is: the faces, the bodies, the floor line and every other line. Black and white only, pure white background, no grey; the paddle stays red. No text anywhere. Landscape 16:9.
```

Step 2, pose M:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every figure exactly where it stands and as drawn. This is the middle frame of a simple waving animation, so change only the waving parts:
1. The man's raised right hand and forearm point straight up, the open palm towards us.
2. The worker robot's raised gripper and forearm point straight up.
3. The gatekeeper's raised arm holds the round red paddle straight up.
4. The reviewer robot's paper ribbon hangs straight down from the slot in its chest, curling only a little at its end.
Everything else stays exactly as it is: the faces, the bodies, the floor line and every other line. Black and white only, pure white background, no grey; the paddle stays red. No text anywhere. Landscape 16:9.
```

- **Check:** in every frame, the reviewer without arms and the worker
  without legs; the man's black cap of hair, his stubble, his own clothes
  (since 2026-10-12) and the keys on his belt; red only on the paddle; no lettering; the
  top right corner free for the AI label; and, at full size, no gap where a
  turned part meets its joint, and no line left behind where a part was.
  Play the slide once in PowerPoint's show.
- **Made on 2026-10-09**, seven pictures and three videos, about 1.65 US
  dollars at the listed prices:
  - The frame, first try: the prompt with `ref-cast.jpg` as its only
    reference, two samples. Both edited the plate instead of drawing a new
    scene: the first kept two waving men and both workers of the plate, the
    second three men and the worker with its skill arm.
  - The frame, second try: the four cut-outs above, two samples, both right.
    The second is the frame; it centres the group better. Both drew the
    robots larger beside the man than the plate does, which suits a curtain
    call, and the author kept them so.
  - The video route came first. Kling 3.0 Pro
    (`fal-ai/kling-video/v3/pro/image-to-video`, five seconds, 0.70 US
    dollars) animated the frame with it as first and last frame: the loop
    closed and the line held, but the GIF weighed 2.8 MB. MiniMax H3 Max
    (0.15) jumped at the loop and flickered, and Wan 3.0 Prime (0.25) lost
    the line. The author chose a few drawn frames instead the same day, and
    the video drafts were not kept.
  - Pose B came first, for a flip-book of two frames, which ticked rather
    than waved. Pose M, two samples, the second kept, made the swing. Its
    strip hangs down below the box first drawn round the strip, so the box
    gained its hanging end.
  - The first GIF ran through four frames, A, M, B, M, at 180 ms each, with
    each part pasted from its pose (130 KB). The author saw an odd
    afterimage in it. The likely cause: for three of the four parts poses A
    and M are almost the same, so each part stood still for three frames
    and flicked to pose B in the fourth, and the strip jumped between
    hanging down and flying out at belt height. That evening the GIF was
    made again from the frame alone, as in step 4: eight frames, each part
    a small step on from the one before, and no new picture.

---

## Added for the costume arc (2026-10-12)

At the author's request Steve now starts in his own clothes, jeans and a
shirt, puts the robe on in 1.3 and sheds it piece by piece. `storyline.md`
(STEVE'S ARC) gives the stages, and `studies/README.md` (round 4) the
study and its cold read, which came first. Every picture with Steve after
1.3 already existed, so each was changed by an edit of itself, not drawn
afresh.

**References.** Image 1 is the scene. Image 2 is a cut-out of one figure of
`studies/bw-18-steve-own-clothes.jpg` on white, with a floor line: the
first figure for *before*, the second (the cape) for *managing*, the third
for *in control*. For 6.2 and 7.2, image 3 is the new 6.1 or 7.1, so that
each pair matches.

**Settings.** As above, with `num_images` 2.

**The prompt.** Every scene edit opens with the same lines, then names one
of three looks and the scene's pose:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: every object, every robot, every line and the white background. Keep the man's face, his very short hair drawn as a thin solid black cap, his heavy stubble drawn as fine dots, his pose, his hands and everything he holds exactly as drawn. Use image 2 only for the man's clothes. Change only this:
```

- *Before:* "1. The man wears only his own clothes, exactly as the man in image 2:
  a plain long-sleeved shirt with a collar and a row of small buttons down
  the front, drawn in outline and left white, tucked into plain jeans that
  are drawn in outline and left white inside, with a narrow plain belt, and
  the same plain trainers. His head is bare. The long robe, the shoulder
  cape, the hood and the rope belt are gone, and nothing hangs from his
  belt."
- *Managing:* "1. Over his own clothes the man wears only the short rounded
  shoulder cape of image 2, like a monk's cowl, over his shoulders and the
  upper chest, its hood lying flat behind his neck, with the small gear
  emblem with square teeth on it where it shows. Below the cape his own
  clothes show, exactly as on the man in image 2: [the clothes as above].
  The long robe and the rope belt are gone, so his two legs in jeans show."
- *In control:* the *before* look without "nothing hangs from his belt",
  then "2. A ring of a few large keys, drawn clearly and about as long as
  his hand, hangs from a small clip on his belt at his right hip, against
  his jeans." The keys arrive in 7c.2, not in 7b.3: in the paper, 7b.3
  (chapter 8) comes before 7a (chapter 9), where they hang on their hook.

Then the pose, in one sentence that says what he still does:

| Slide | Look | The sentence |
|---|---|---|
| 1.1 | before | He still sits hunched on the stool at the workbench, typing on the laptop, one hand rubbing his tired eyes; his knees are bent and his feet rest on the stool's rung. |
| 1.2 | before | He still sits on the bottom step of the stairs and holds the open catalogue in front of his chest, turned towards us; the catalogue, its two pages with the two robots drawn on them, and the small envelope beside him stay exactly as they are. Below the catalogue his legs in jeans, knees bent, feet on the floor. |
| 6.1 | managing | He still stands at the head of the table, clutching a stack of paper to his chest and adding another sheet to it. |
| 6.2 | managing | He still sits down at the table with an empty notepad; his knees are bent. |
| 7.1 | managing | He still stands at the whiteboard on its easel and draws boxes and arrows. 2. His face looks tired and weary: eyelids half closed, mouth flat, no smile. |
| 7.2 | managing | He still stands with a mug in his hand, reading an index card and nodding. |
| 7a.1 | managing | He is still seen from behind, standing at the whiteboard on its easel and drawing boxes and arrows; from behind, the cape covers his shoulders and upper back, its hood lying on it. |
| 7a.2 | managing | He still stands beside the easel and watches, a plain mug held in both hands in front of his chest; both his forearms are in front of him, and nothing hangs at his sides. He has exactly two arms and two hands. (The first edit said "with a mug in his hand" and drew three hands.) |
| 7b.1 | managing | He is still halfway up the stairs on his way out, waving an absent-minded go-ahead without looking back; his legs in jeans stand on two different steps. |
| 7b.3 | managing | He still stands at the door of the house exactly as drawn. Nothing hangs from his belt: no keys. (The first edit put the keys on his belt.) |
| 7c.1 | managing | He still stands in the yard between the house and the office, a mug in his hand. Nothing hangs from his belt. |
| 7c.2 | in control | He still stands in the yard in the same place, a mug in his hand, and watches with a slight smile. |
| 8.2 | in control | He still sits back on his stool with a mug of tea in both hands and a slight smile; his knees are bent and his feet rest on the stool's rung. |

Every prompt ends: "Everything else stays exactly as it is. Black and
white only, apart from any colour already in image 1; no grey and no
shading. No text anywhere: nothing printed on the shirt. Landscape 16:9."

**8.2, the robe hung up,** a second edit of the new 8.2, with the cast
plate's third figure, cut out, as image 2:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, the man included: his face, his shirt and jeans, the keys at his hip and the mug of tea in his hands; the bench, the closed laptop, the blown-out candle with its thread of smoke, the cold censer on its hook, the hanging bulb, the small pointed window with its glazing bars and its one lit pane, the tidy cork board, the organisation chart, the filing cabinet with its open drawer and the stool. Use image 2 only for the look of the robe, not for the man. Change only this:
1. In the empty space above the filing cabinet, right of the pointed window, a small plain wooden coat rack hangs: a short horizontal board with two round wooden pegs. From one peg hangs the long plain robe of image 2, empty, limp and flat, as clothes hang on a peg: at the top the short rounded shoulder cape, like a monk's cowl, with the small gear emblem with square teeth on it, its empty hood hanging limp behind the cape; below it the robe with its wide sleeves hanging straight down, and its hem ending just above the top of the filing cabinet. The rope belt hangs looped over the second peg. Nobody is inside the robe.
Everything else stays exactly as it is. Black and white only; this picture has no colour. No text anywhere. Landscape 16:9.
```

**The cast plate and the goodbye.** `ref-cast.jpg` changed only its
fourth man, the one with the keys, to the *in control* look ("Edit image 1,
a character sheet. Keep everything in it exactly as it is: the first three
men from the left, the worker robots, the reviewer robot, the gatekeeper
with its red paddle, …"). The goodbye's frame, pose A, got the same look,
with "His right shirt sleeve ends in a plain buttoned cuff at the wrist,
just below his raised waving hand". It is kept as
`studies/anim-04-goodbye-out-own-clothes.png`, mapped onto the seven
colours as in step 3 of image 30, and `tools/goodbye_wave.py` takes it as
pose A. Its cut along the cuff, the wrist's pivot and the cover were
measured again for the shirt's cuff, and the strip's first box starts at
x 1400, right of the man, whose clothes now differ from pose M's.

**Only the man goes back.** Every edit lined up with its picture to the
pixel, 7b.3 to one pixel, which was shifted back. So only the man's box was
pasted onto the original, with a soft edge of 6 px, and every other line
stays as it was, including the fixes of the read without the script.
Then the near-white was set to white.

| Image | Sample kept | The man's box (x0, y0, x1, y1) |
|---|---|---|
| 1.1 | first | 1060, 680, 1530, 1460 |
| 1.2 | first, which kept his sceptical face; a grey trace of the old hood's top at the box's edge was set to white | 1010, 140, 2410, 1536 |
| 6.1 | first | 100, 320, 690, 1460 |
| 6.2 | second | 60, 320, 660, 1470 |
| 7.1 | second, the tired face | 1020, 560, 1450, 1460 |
| 7.2 | second | 870, 560, 1345, 1460 |
| 7a.1 | first | 270, 380, 790, 1460 |
| 7a.2 | second of the second edit | 420, 390, 833, 1460 |
| 7b.1 | second | 2160, 280, 2620, 1180 |
| 7b.3 | first of the second edit | 130, 700, 520, 1460 |
| 7c.1 | first | 890, 760, 1170, 1460 |
| 7c.2 | first | 890, 760, 1180, 1460 |
| 8.2 | first, then the robe's second, whose rack has three pegs | 330, 310, 1000, 1470; the robe 2120, 260, 2630, 1060 |
| `ref-cast.jpg` | first | 1420, 250, 1830, 1420 |
| goodbye frame | first | 920, 120, 1545, 1470 |

`ref-steve.jpg` is `studies/bw-19-steve-arc-six-stages.jpg`, put together
without the model: the study's three figures around the cast plate's first
three, with the study's figures set down onto the floor line and the rest of
the study's floor line under their shoes taken out. On `ref-cast.jpg` the
worker's head hides the fourth man's keys, so `ref-steve.jpg` is the
costume reference.

**Cost.** 38 pictures, about 3.05 US dollars at 0.08 each: two for the
study, two samples each of 13 scenes, the plate, the goodbye's frame, the
robe on its rack, and second edits of 7a.2 and 7b.3 after a check found
three hands in 7a.2 and the keys a step too early in 7b.3.

## Changed after the run-through (2026-10-15)

After the author's first run-through the sandbox left the talk, and security
joined the post room. Two edits made it, each with two samples, through fal
on the settings above: 4 pictures, about 0.32 US dollars. The deck floats
the robots' names above them since the same day; they are never drawn in.

### 23c · `beat-07b-isolation-1.jpg` — the dome comes off

Image 1 is the picture of 2026-10-07 after edits 23a and 23b.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every figure as drawn. Change only this:
1. Remove the clear glass bell dome over the small boxy printing machine on the workbench, together with the dome's round base and the knob on its top. The machine now stands in the open on the bench and prints by itself, its crank turning.
2. The continuous paper feed still runs from the open black archive box on the floor up into a slot in the machine, and the printed sheets still slide out of the machine onto the bench towards the worker robot.
Everything else stays exactly as it is: the open steel door and its rack of black archive boxes, the wall shelf with the sealed folder, the gatekeeper with its lowered red paddle, the worker robot reading a sheet, the stream of small sheets from its antenna to the open window, the bulb, the keys, the man on the stairs. Black and white only, pure white background, no grey; the only colours are the red of the wax seal and the red of the gatekeeper's paddle. No text anywhere. Landscape 16:9.
```

- **Made:** both samples took the dome off cleanly and redrew the rest with
  small shifts. Only the box from (1195, 785) to (1591, 1266) px of the
  first sample was pasted into the picture, the machine, the feed and the
  bench under it; the lines crossing its edges lie within one pixel of the
  old ones, so the seam does not show. The paper's chapter 8 figure uses
  this picture, and its alternative text no longer names a dome.

### 27c · `beat-07a-safety-2.jpg` — security at the foot of the stairs

Image 1 is the picture of 2026-10-08, image 2 `ref-cast.jpg`.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is, and keep every character as drawn: the man with his mug on the left, the worker robot at the glass door taking the narrow strip from the slot, the reviewer robot at its desk in the glass room, the ring of keys on its hook by the stairs. Use image 2, the cast sheet, only for the gatekeeper, the faceless steel post on the far right of that sheet. Change only this:
1. Remove the easel with its blank whiteboard. Where it stood, the lower steps of the stairs and the floor show through, drawn like the rest of the stairs.
2. In that free space, at the foot of the stairs between the man and the worker robot, the gatekeeper stands bolted to the floor on its heavy base plate with big bolts: a squat, faceless steel post with a guard's peaked cap, one round lamp and one jointed arm. It is about as tall as the worker robot. It faces the worker robot and holds its blank round red paddle up between the worker robot's free gripper and the keys, as at a checkpoint.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colour is the red of the gatekeeper's paddle. No text anywhere: the paddle is blank. Landscape 16:9.
```

- **Made:** the second sample is the picture, kept whole: the man stays where
  he stood, the stairs run on where the easel was, and the gatekeeper holds
  its paddle up beside the worker's head, its arm across the keys. The first
  sample moved the man to the left edge. Pasting back only the new part would
  have left a step of five pixels in the worker's head, which the edit drew a
  little lower, and the rest of the second sample matches the old picture
  line for line, so it was taken as it is. The paper's chapter 9 figure uses
  this picture; its alternative text names the guard post.

## Changed after the second run-through (2026-10-19)

The author recorded the talk a second time and asked for four pictures:
the slide he found odd fixed, a fresh worker delivered every morning, the
planted letter defeated in 8.1, and portraits for the robots' cards. All
four went through fal on the settings above in one batch: 7 pictures,
about 0.56 US dollars. Image 1 is always the picture named, and only the
changed box of an edit was pasted back where the rest matched.

### 21b · `beat-07-memory-1.jpg` — Steve's right arm

Image 1 is the picture of 2026-10-12.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man's head, face, stubble and short hair, his short rounded shoulder cape with the gear emblem, his shirt, belt, jeans and trainers, the flip chart with its diagram, the worker robot, the reviewer robot under the stairs, the filing cabinet, the workbench, the cork board, the arm rack, the rulebook, the window. Change only the man's two arms, which are drawn wrongly: one now grows out of the middle of his chest below the cape.
1. His left arm, on the right side of the picture, comes out of his left shoulder, from under the edge of the shoulder cape: the upper arm goes out and slightly forward, the elbow bends, and the forearm rises to the flip chart, so that his hand still holds the marker on the second box of the diagram, as now.
2. His right arm, on the left side of the picture, comes out of his right shoulder from under the cape and hangs relaxed at his side, the hand open beside his thigh.
Both arms are in the plain long sleeves of his shirt, drawn in outline and left white, equally thick and in proportion to his body. Nothing else changes. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the fault was the right arm, which was missing: only a bulge
  behind his back stood for it. Both samples drew it hanging at his side and
  left the drawing arm as it was, which comes out from under the cape. Only
  the box from (1010, 772) to (1265, 1185) px of the first sample was pasted
  in, below the stubble, whose dots the edit had redrawn. The paper's
  chapter 7 figure uses this picture; its alternative text needs no change.

### 31 · `beat-02-claude-md-3.jpg` — 2.2 A new worker every morning

Image 1 is image 10 (2.1), image 2 image 11 (the crate), image 3 `ref-cast.jpg`.

```text
Edit image 1. Keep the camera, the framing, the drawing style, the cork board with its sticky notes, the workbench and the man exactly as they are drawn: his face, his long plain hooded robe with the short rounded shoulder cape and the gear emblem, his hood down, his sleeves pushed up, his rope belt with the small cold censer. It is the next morning. Change only this:
1. Yesterday's worker robot is no longer at the bench. On the far left it sits switched off inside an open wooden crate like the crate in image 2: its two round eyes are drawn as two short flat lines, its head tilted, its arms hanging limp over the crate's edge, the crate's loose lid leaning against the crate, ready to be sent back.
2. In front of the workbench stands a second, identical wooden crate, its lid lying on the floor beside it and a few curls of packing straw spilling out. A brand-new worker robot of exactly the same make, as drawn on the cast sheet (image 3, the plain worker robot without an extra arm), rises out of it: its two round eyes wide open, its antenna upright, one gripper lifted in greeting towards the man.
3. The long printed sheet lies rolled up on the workbench, covered with the man's black pen corrections. The man stands where he stood, holding one corrected sheet, and looks at the new robot with a tired, resigned face.
Black and white only, pure white background, no grey; no colour: the censer is cold, no smoke. No text anywhere: paper shows only a few thin lines. Landscape 16:9.
```

- **Made:** both samples told it; the second is the picture, kept whole,
  because its man looks resigned rather than surprised and the old worker
  slumps clearly in its crate. The crate is the one the worker stands on in
  2.3, which now reads as the crate it came in.

### 5b · `beat-08-team-1.jpg` — the letter, run through

Image 1 is the picture of 2026-10-07, image 2 image 26 (7a.1), for the letter.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the cutaway office with its thick walls, the gatekeeper post with its red paddle and the striped barrier, the sealed folder with its red seal, the rulebook, the arm rack, the window with the gauge, the worker robot at its desk, the filing cabinet, the reviewer robot in its glass room. Use image 2 only for the long folded letter that the worker robot reads there. Change only this:
1. On the bare floor at the front of the room, between the gatekeeper's base plate and the front legs of the worker's desk, lies that letter: a long sheet of paper, folded once and lying open, with a few thin lines of scribble and one short thick black line at its foot; no words, no stamp, no seal.
2. A plain straight sword is driven down through the middle of the letter into the floor and stands upright, pinning it: a simple straight cross guard, a straight narrow blade, a plain grip and a round pommel about level with the top of the worker's desk, drawn in the same thin black lines and left white.
3. Three thin marionette strings run from the foot of the letter and lie slack and curled on the floor beside it, attached to nothing.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red wax seal and the red paddle. No text anywhere. Landscape 16:9.
```

- **Made:** the second sample is the one: its sword leans into the letter
  at an angle and reads as run through, where the first stood upright in
  front of the desk and read as stuck in it. Only the box from (1290, 700)
  to (1990, 1335) px was pasted in. The deck labels the letter "prompt
  injection".

### 32 · the card portraits — the three robots alone

Image 1 is `ref-cast.jpg`.

```text
Edit image 1. Keep the drawing style and keep these three figures exactly as they are drawn, with every line: the plain worker robot without an extra arm (the fifth figure from the left), the slim egg-shaped reviewer robot with one large round lens (the seventh), and the gatekeeper, the steel post with the peaked cap holding up the red paddle (on the far right). Remove everything else: the four men, and the worker robot with the extra arm and the sheet of paper. Place the three remaining figures far apart along one thin floor line, the worker robot on the left, the reviewer robot in the middle, the gatekeeper on the right, each standing alone and complete, with wide empty white space around it, at the sizes shown. Black and white only, pure white background, no grey; the only colour is the red of the paddle. No text anywhere. Landscape 16:9.
```

- **Made:** one sample. It drew the worker alone on the left, a second
  reviewer without its strip in the middle, and the reviewer with its strip
  close beside the gatekeeper. The worker and the strip-carrying reviewer
  were cut out, the gatekeeper with the reviewer's edge painted white, and
  the floor line taken off under each: `card-worker.png`,
  `card-reviewer.png` and `card-security.png` in `slides/beats/`, PNG, as
  cut. The plate itself is not kept. In ref-cast.jpg the worker stands in
  front of a man's legs, which a cut-out could not clear.

## Changed after the review (the evening of 2026-10-19)

That evening a review of the deck read every drawing at full size, as the
room sees it and tile by tile. Two pictures said the opposite of the talk:
8.2's cork board read as a television, and in 7a.2 the keys hung on a hook
just behind security's forearm, as if security carried them. Fifteen
smaller faults missed a slide's point, broke the cast's rules or jumped
between two slides that share a camera, which shows more now that the deck
fades one into the other (`storyline.md`, visual rule 4). The author asked
for all of them to be fixed, and for the slides where data moves to move.
`storyline.md`, "The review of the pictures", has the decisions.

Seventeen edits went through fal on the settings above, each with two
samples: 34 pictures, about 2.72 US dollars. Eleven were used, and only the
changed box of the sample kept was pasted back, with a soft edge, as for
the costume arc. Six did not hold, and what they asked for was done by
hand, as were a few small things no edit was asked for. Then the
near-white was set to white. Image 1 is always the picture named, as it
stood before.

### 10a · `beat-02-claude-md-1.jpg` — 2.1, the worker hip-high

Image 2 is `ref-cast.jpg`.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man in his robe with the hood down and the cold censer, drawing circles with his black pen, the long printed table, the cork board with its sticky notes and the empty spot, the workbench, the single bare nail. Change only the worker robot, which is drawn far too big:
1. Make the worker robot smaller, hip-high to the man, as the worker robot on the cast sheet (image 2) is to the men there: its head level with the man's belt. It still stands on its one wheel on the floor in front of the bench, the first sticky note still stuck to its black chest band, and it still holds up its end of the long printed table with one gripper.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour: the censer is cold. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the picture. The worker was about 1.45
  times the cast plate's size, its head at the man's chin; now its head is
  level with his belt, as in 2.2, and it still holds its end of the table.
  Only the box from (470, 430) to (1135, 1450) px was pasted in. The
  paper's chapter 2 figure uses this picture.

### 31a to 31c · `beat-02-claude-md-3.jpg` — 2.2, a greeting and a shorter bench

Image 2 is image 10 as it stood before edit 10a.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the cork board with its sticky notes, yesterday's worker robot switched off in its open crate on the left, the new worker robot rising out of its crate in the packing straw, the leaning lids, the man in his robe with the hood down and the cold censer, holding one corrected sheet. Change only this:
1. The workbench is as long as in image 2: its right end and its right legs stand exactly where they stand in image 2, and white space shows between the end of the bench and the man.
2. The new worker robot holds its raised gripper up open in the white space to the right of the cork board, clear of the board's frame, in greeting towards the man.
3. Every pen mark on the sheets is a plain black circle round a single cell or a short straight stroke: no handwriting, no squiggles, no symbols.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour: the censer is cold, no smoke. No text anywhere. Landscape 16:9.
```

- **Made:** the second sample is the one. Its new worker holds its open
  gripper up in the white space right of the board, where it had clamped
  the board's frame, and the pen marks are circles and short strokes where
  they read as handwriting. The boxes from (1490, 560) to (2125, 975) and
  from (945, 880) to (1070, 975) px were pasted in. The bench stayed as long
  as before: 240 px longer than in 2.1, nearly touching the man.
- **31b and 31c** asked only for the shorter bench, once with 2.1 as image 2
  and once on the corrected picture alone. All four samples drew it as long
  again.
- **By hand:** a slice of the bench and of the sheet on it, 195 px wide from
  x 1654 px, was taken out, and what lay right of it moved left. The bench
  now ends near where 2.1 has it, with white wall before the man. The roll
  and the crate's leaning lid, which lie in front, stay where they were.
  Right of the cut the sheet lay 1 to 2 px higher, so it was shifted down
  there by fractions of a pixel until its own curve takes over. The bare
  nail of 2.1, which this picture had lost, was pasted back from 2.1: the
  box from (460, 355) to (535, 430) px.

### 12 · `beat-03-skills-1.jpg` — 3.1, the rulebook where 3.2 has it

- **By hand:** the rulebook and its nail moved 49 px left and 505 px up, to
  where 3.2 shows them. The deck fades 3.1 into 3.2, and a jump would show.
  The paper's chapter 3 figure uses this picture.

### 13b to 13d · `beat-03-skills-2.jpg` — 3.2, grids and a forearm

Image 2 is image 12, for its grids.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the rulebook on its nail, the rack of spare arms, the worker robot with the clip-on arm holding the magnifying glass before its eyes, the eraser on its high shelf, the printing machine, the stairs, the keys on their hook, the man with his sheet. Change only this:
1. The sheet on the clipboard, the sheet laid out on the bench and the printout coming out of the machine each show a plain grid of empty cells, drawn like the grids in image 2; the clipboard's grid is tidy and complete. No scribbles and no dashes on them.
2. The man's arm that holds the left edge of his sheet is a normal forearm, as wide as his other arm, coming out of his pushed-up robe sleeve at the elbow.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the one for the grids. The clipboard, the
  sheet on the bench and the printout show plain grids again, as in 3.1,
  where they had turned into scribbles. Only the box from (850, 880) to
  (1485, 1230) px was pasted in; the forearm came back unchanged.
- **13c and 13d** asked only for the forearm, once on the picture and once
  on a close-up of the man, enlarged 2.87 times so the model could see the
  arm. All four samples drew the same thin loop of two lines again, and one
  swelled the sleeve of the other arm. 13c:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the rulebook on its nail, the rack of spare arms, the worker robot with the clip-on arm holding the magnifying glass before its eyes, the eraser on its high shelf, the printing machine, the grids on every sheet, the stairs, the keys on their hook, and the man: his face, his stubble drawn as fine dots, his short hair drawn as a thin solid black cap, his robe with the hood down, the short rounded shoulder cape with the gear emblem, the rope belt with the cold censer, and both his hands exactly where they hold his sheet. Change only the man's right forearm, on the left side of the picture, which is drawn wrongly: below the hand that holds the left edge of the sheet it is only a thin, narrow loop of two lines.
1. Draw it as a normal forearm, as wide as his other forearm: from the wrist below that hand it runs down and inwards to his elbow at his side, just below the edge of the shoulder cape, where the wide sleeve of his robe is pushed up and gathers in soft folds, exactly like the pushed-up sleeve on his other arm.
2. The sheet stays in front of it, so the forearm shows only where the sheet does not cover it.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour: the censer is cold. No text anywhere. Landscape 16:9.
```

- **By hand:** the loop's inner line was taken out. The forearm is now one
  shape between its outer line and the sheet, partly behind the sheet and
  bending at the elbow below it. The paper's chapter 3 figure uses this
  picture.

### 14a · `beat-04-hooks-1.jpg` — 4.1, the streak, the nails and the sleeves

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the open black folder with its broken red seal on the bench, the worker robot with the feather duster lifting out a page, the wastepaper basket, the eraser, the rulebook and the rack of spare arms, the man frozen at the foot of the stairs with his sandwich, the steel door, the shelf, the bulb and the window. Change only this:
1. Remove the curved double motion line that runs from the open folder across the worker robot's round body to the lifted page. The robot's body is plain white there and its black chest band is solid and unbroken.
2. Remove the two small loose nails that float in the air below the rack of spare arms.
3. The man's robe sleeves are pushed up to his elbows.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colour is the red of the broken wax seal. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the picture. Three boxes were pasted in: the
  worker's body from (1620, 850) to (1805, 1035) px, without the motion
  streak that read as a crack in it; the wall under the arm rack from
  (1105, 760) to (1290, 840) px, without the two loose nails; and the man's
  arms from (2260, 780) to (2640, 1040) px, the sleeves pushed up as in
  every other picture of his learning stage.

### 15 · `beat-04-hooks-2.jpg` — 4.2, the arm rack back beside the rulebook

- **By hand:** the arm rack hangs beside the rulebook in 4.1 but hung at the
  far right in 4.2, where the small sign had stood. The rulebook sits at
  the same pixels in both pictures, so 4.1's rack, the box from (1095, 495)
  to (1315, 770) px, was copied in beside it. The rack at the right and its
  two loose nails were taken off, and the small sign now hangs in their
  place, right of the large board. The paper's chapter 4 figure uses this
  picture.

### 4a · `beat-04-hooks-3.jpg` — 4.3, the paddle that stops

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the worker robot at the bench reaching out with the feather duster, the gatekeeper post bolted to the floor with its peaked cap and its round lamp, the striped barrier with its padlock, the sealed black folder with its red wax seal on its shelf, the open curved path to the plain white folder on the low table. Change only this:
1. Lower the gatekeeper's jointed arm so that its blank round red paddle is held flat out in front of it at the height of the worker robot's outstretched gripper, and the paddle presses against that gripper and stops it.
2. The feather duster's feathers end at the paddle: nothing of the worker robot reaches past the paddle or touches the gatekeeper.
3. The worker robot's other gripper, resting on the bench, is a two-finger claw like the outstretched one.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red of the paddle and the red of the wax seal. No text anywhere: the paddle is blank. Landscape 16:9.
```

- **Made:** the first sample is the picture. The paddle was held overhead,
  and the duster's feathers ended at the guard's fist; now the paddle is
  lowered to the gripper's height and the feathers end at it. The resting
  gripper on the bench is a two-finger claw, where it was a curled hand.
  The boxes from (1330, 370) to (1580, 845) and from (370, 755) to
  (495, 845) px were pasted in. The paper's chapter 4 figure uses this
  picture.

### 16b and 16c · `beat-05-subagents-1.jpg` — 5.1, the paddle on its handle

16b asked for the paddle "lowered at its side on a long thin handle",
turned partly edge-on; both samples left it lying on the base plate like a
red ball. 16c says what is wrong and where the hand holds the handle:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the worker robot stamping a tick beside the black blot on the top sheet, the pile of sheets, the printing machine on the bench, the man leaning in the plain wooden door frame with folded arms. Change only the small gatekeeper post far back on the left, whose red paddle now lies on its base plate like a ball:
1. The gatekeeper keeps exactly one jointed arm, which comes out of the side of the post at a round ball joint, as drawn now, and bends at a round elbow.
2. Its hand holds the end of the paddle's thin straight handle, and the paddle hangs straight down from the hand beside the post, the round red paddle turned edge-on so that it shows as a narrow upright red oval. The bottom of the paddle hangs well above the base plate, with white space between them.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colour is the red of the paddle. No text anywhere: the paddle is blank. Landscape 16:9.
```

- **Made:** the first sample is the picture, after one fix by hand: it had
  drawn a second, short arm on the post's left side, which was painted out,
  with the post's edge run on through it. Then the box from (85, 500) to
  (690, 1005) px was pasted in. The paper's chapter 5 figure uses this
  picture.

### 22a · `beat-07-memory-2.jpg` — 7.2, the worker reads its card

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man with his mug reading his own index card, the open top drawer of the filing cabinet, the clean whiteboard on its easel, the cork board, the rulebook, the rack of spare arms, the window, the stairs and the reviewer robot under them. Change only the worker robot at the filing cabinet, which now faces us with blank eyes and holds its card out beside its head:
1. It holds the index card up in front of its face with one gripper and reads it: its square head turned a little towards the card, small black pupils in its two round eyes looking at the card.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere: the card shows only a few thin lines. Landscape 16:9.
```

- **Made:** the first sample is the picture. The worker faced the room with
  blank eyes and held its card beside its head, as if showing it; now its
  pupils turn to the card it holds up, and it reads. Only the box from
  (470, 815) to (880, 1195) px was pasted in. The paper's chapter 7 figure
  uses this picture.

### 26b and 26c · `beat-07a-safety-1.jpg` — 7a.1, the strings and the gripper

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man at the whiteboard seen from behind, the filing cabinet, the stairs with the keys on their hook, the reviewer robot under the stairs, the worker robot at the foot of the stairs holding the long letter. Change only this:
1. The three thin, straight, taut strings run from the foot of the letter to the wrist of the worker robot's outstretched arm and end there, tied to the rim of its round wrist joint: none of them crosses the joint, and none curls under the gripper.
2. The gripper that holds the letter is a two-finger claw with a round wrist joint, the same as the gripper on the outstretched arm.
3. The worker robot's two round eyes are plain and empty, with no dots in them.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere: the letter shows only a few thin lines and one short thick black line at its foot. Landscape 16:9.
```

- **Made:** only the gripper that holds the letter was taken from the first
  sample, the box from (1110, 1045) to (1260, 1165) px: a two-finger claw,
  where it was two pads. Neither sample ended the strings at the wrist.
- **26c** asked only for the strings' ends, and both samples ran them
  through the joint again.
- **By hand:** the part of the top string inside the wrist's ball and the
  curled tails under the gripper were painted out, so two strings end on
  the ball and the third on the gripper's lower jaw. A tail had lain on
  that jaw, so the jaw was drawn again as the mirror image of the upper one.
  The two stray dots in the eyes were taken out, their outlines kept. The
  paper's chapter 9 figure uses this picture.

### 27d · `beat-07a-safety-2.jpg` — 7a.2, the keys behind the post

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man with his mug on the left, the filing cabinet and the bench, the stairs, the gatekeeper post at the foot of the stairs with its peaked cap, its round lamp, its jointed arm and its raised round red paddle, the worker robot at the glass door taking the narrow strip from the letterbox slot, the reviewer robot at its desk in the glass room with the letter and the slack strings. Change only the ring of keys, which now hangs on a loose hook right behind the gatekeeper's arm:
1. Remove that ring of keys and its small J-shaped hook from behind the gatekeeper's arm. The gatekeeper's arm, hand and paddle stay exactly as drawn, and the space behind them is plain white.
2. Hang the same ring of keys on the same small J-shaped hook under the stairs on the left side of the gatekeeper's post, between the man and the post, at about the height of the gatekeeper's lamp, touching nothing else, so that the post and its raised paddle stand between the keys and the worker robot.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colour is the red of the paddle. No text anywhere: the paddle is blank. Landscape 16:9.
```

- **Made:** the first sample is the picture. The keys hang on their hook
  under the stairs, on the far side of the post from the worker, so the
  post and its raised paddle stand between them. Two boxes were pasted in:
  the keys' new place, from (850, 1090) to (1005, 1295) px, and their old
  one, now plain white, from (1150, 885) to (1315, 1095) px. The paper's
  chapter 9 figure uses this picture.

### 23d · `beat-07b-isolation-1.jpg` — 7b.1, two claws

Image 2 is `ref-cast.jpg`.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the open steel door to the rack of black archive boxes, the printing machine fed from the open black box, the stream of small sheets from the worker robot's antenna through the open window, the gatekeeper with its lowered red paddle, the shelf with the sealed folder and its red seal, the keys on their hook, the man on the stairs, the bulb. Change only the worker robot's two grippers, which are drawn as hands:
1. Its hanging left gripper is the two-finger claw of the worker robot on the cast sheet (image 2): two curved fingers round a gap, no thumb and no extra fingers.
2. Its right gripper, which holds the sheet it is reading, is the same two-finger claw, holding the sheet between its two fingers.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red of the wax seal and the red of the paddle. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the picture. The hanging gripper, which had
  three fingers and a thumb, and the one that holds the sheet, which was two
  pads, are both two-finger claws. Only the box from (1590, 880) to
  (1895, 1135) px was pasted in. The deck shows this picture in motion
  (image 33), and the paper's chapter 8 figure keeps the drawing.

### 25e · `beat-08-team-2.jpg` — 8.2, a cork board, not a television

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man on his stool with his mug of tea and the ring of keys on his belt, the bare bulb, the small pointed window, the organisation chart, the candle with its thin thread of smoke, the cold censer on its hook, the coat rack with the empty robe and the rope belt, the filing cabinet, the workbench. Change only the cork board behind the bench, which now looks like a flat television on a stand:
1. Make it read as a cork pinboard hanging on the wall: a plain, thin wooden frame instead of the thick bevelled one, hung from a single nail by a short string, with plain white space between its lower edge and the bench.
2. Each of the four square sticky notes in the tidy column at its left is held by one small round pushpin.
3. The closed laptop lies flat at the left end of the bench, near the man, no longer under the board.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour: the candle is out. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the picture. The nearly empty board in its
  bevelled frame read as a widescreen television, and the closed laptop
  under it as its soundbar. Now it hangs from a nail by a string, in a thin
  frame, each note on a pushpin, and the laptop lies at the left end of the
  bench. Only the box from (880, 370) to (1630, 968) px was pasted in. The
  paper's Conclusion figure uses this picture.

### 32 · the card portraits

- **By hand:** the short pieces of floor line under each robot were painted
  out, and white was added where a robot sat close to its edge, so each
  stands about 20 px from it.

### 33 · the flights — 7b.1, 7c.1 and 7c.2 in motion

No new picture: like the goodbye, the flights are turned from the
drawings, in eight frames that loop. `tools/flying_sheets.py` makes them,
and `studies/` keeps what it starts from, a plate and a sprite for each
scene (`anim-05` to `anim-07`).

- **The plate** is the picture with its flying sheets and their speed lines
  taken off. Where they covered a line, the line was joined again: at the
  house of 7c.1 from 7c.2, which shows the wall without sheets, and at the
  warehouse with straight lines drawn through, each clipped to the sheet it
  ran behind. 7c.1 kept the sheet that had landed until 2026-10-28 (now the
  Book of Secrets stands there, below), 7c.2 the folders on the
  top shelf, and 7b.1 the antenna's rays and the window. Two hand fixes in
  7c.1 took off a speed line left on the warehouse gate and joined the
  cabinet's top line it had cut.
- **The sprite** is one of the drawn sheets, cut out with its own alpha: in
  7c.1 the sheet at the top of the arc (until 2026-10-28), in 7c.2 a flying
  folder, in 7b.1 the third sheet, alone on the wall.
- **The Book of Secrets (2026-10-28).** At the author's request the black
  sheet that flies in 7c.1 became the Book of Secrets. The sealed book of
  1.1 is cut out with its own alpha, the shelf's back line taken off
  between its edges, and scaled to 0.42, so it flies at about a sheet's
  size (`studies/anim-05-book-7c1-sprite.png`). It tumbles with the
  sheets' turns and stands upright where it lands: on the cabinet's top
  shelf, where the plate now has it standing in place of the landed sheet
  (`studies/anim-05-book-7c1-plate.png`), behind the edge of the cabinet's
  right door, which the tool keeps in front. The paper's still changed with
  it, and its alternative text.
- **The flight.** The tool sets the sprite back along a smooth path through
  the places where the drawing had its sheets, turned and sized as they
  were there, with two or three speed lines behind it. In each frame every
  sprite moves one place on, so the loop has no seam: a sprite fades in at
  the window or the antenna and fades out where the stream ends, as the
  next takes its place. In 7b.1 the sheets pass in front of the open
  casement and shrink into the dark (behind it until 2026-10-20, 33a); in 7c.1 and 7c.2 they rise out of the window
  and land in the warehouse.
- **The colours.** The frames share one palette, a ramp of greys and the
  picture's own colours, so the seal and the paddle stay red, the lit
  windows of 7c yellow (since 2026-10-20), and nothing flickers. Each frame shows for 70 ms; `--ms` sets another pace.
- **The stills.** The paper keeps still pictures. 7b.1 keeps its drawing,
  whose stream already leaves through the open pane. For 7c.1 and 7c.2 the
  tool saves one frame as the JPEG, one with a sheet just leaving its
  window, so the trail on paper starts there too. Before, the sheets slid up
  the house wall and the folders rose above the office roof. Each loop
  starts on that frame, so a viewer that shows only the first frame, a PDF
  of the deck among them, shows the paper's picture.
- **Size:** 1478 KB for 7b.1 (with the worker's new eyes), 1068 KB for 7c.1 (with the Book of
  Secrets, 2026-10-28) and 841 KB for 7c.2 (with the lit windows of 2026-10-20), at the drawings' 2752 × 1536 px.

## Changed after the built deck (late on 2026-10-19)

Late that evening the author went through the built deck and asked for five
changes: one kind of eyes for the worker, 6.1 to build up instead of a bar
that fills, a few hard values on the cards, two more steps in Steve's
costume, and a left hand in 7.1. `storyline.md`, "The built deck, looked
through", has the decisions. The cards needed no picture, and the eyes no
model.

Eighteen edits went through fal on the settings above, each with two
samples: 36 pictures, about 2.88 US dollars. As before, only the changed box
of the sample kept was pasted back, with a soft edge, and the near-white was
set to white. One edit, for the height of 35b's stacks, was refused twice
for credit, the second time just after the account was topped up, and ran
at the third try (image 35).

### 21c · `beat-07-memory-1.jpg` — 7.1, a left hand

Image 1 is the picture of edit 21b.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man's head, face, stubble and short hair, his short rounded shoulder cape with the gear emblem, his shirt, belt, jeans and trainers, his right arm hanging at his side, the flip chart with its diagram, the worker robot, the reviewer robot under the stairs, the filing cabinet, the workbench, the cork board, the arm rack, the rulebook and the window. Change only the man's left hand, the one that draws on the flip chart on the right of the picture, which is drawn wrongly as a right hand:
1. Draw it as his left hand seen from the back: the back of the hand and the knuckles towards us, the four fingers curled round the marker, and the thumb on the lower side of the hand, under the marker. It holds the marker like a pen, and the marker's tip still touches the second box of the diagram.
2. The cuff of his sleeve and his forearm stay exactly where they are.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the second sample is the one. The hand on the flip chart read as
  a right hand, its thumb on top; now the back of his left hand faces us and
  the thumb sits under the marker. Only the box from (1308, 760) to
  (1552, 894) px, the hand and the marker, was pasted in.

### 34 · `studies/bw-20-steve-hitched-and-open.jpg` — two new looks

Steve's look changed at only four points between 2.1 and 7c.1, so two
steps were added (`storyline.md`, STEVE'S ARC): the robe hitched up for work
from 3.1, and from 6.1 the rope belt off and the robe open like a coat. Each
look was first drawn on one figure alone, then carried into the scenes.
Image 1 is one figure of `ref-steve.jpg`, cut out and set on a white 16:9
canvas with a floor line: the learning figure for 34a, the organising figure
for 34b, the managing figure for 34c.

34a, the robe hitched up, the censer still on the belt:

```text
Edit image 1, a drawing of one man on white. Keep the man exactly as he is drawn: his face, his heavy stubble drawn as fine dots, his very short hair drawn as a thin solid black cap, his hood down, the short rounded shoulder cape with the small gear emblem, his pushed-up sleeves, his hands with the pencil and the open notebook, the rope belt with the small cold censer hanging from it, his trainers, his pose and the floor line. Change only his long robe: he has hitched it up for work.
1. The front of the robe's skirt is pulled up and tucked into the rope belt at both hips, so that the robe now ends just below his knees in a few soft folds.
2. Below it his two legs show in plain jeans, drawn in outline and left white inside, down to his plain trainers.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour: the censer is cold, no smoke. No text anywhere. Landscape 16:9.
```

34b is the same edit of the organising figure. It names his clipboard and
mug instead of the pencil and notebook, leaves out the pushed-up sleeves,
says "Nothing hangs from the rope belt.", and ends without the censer.

34c, the robe open like a coat:

```text
Edit image 1, a drawing of one man on white. Keep the man exactly as he is drawn: his face, his heavy stubble drawn as fine dots, his very short hair drawn as a thin solid black cap, the short rounded shoulder cape with the small gear emblem and its hood lying flat behind his neck, his shirt, his narrow belt, his jeans, his trainers, the mug in his hand, his pose and the floor line. Change only this:
1. Under the shoulder cape and over his shirt and jeans he wears the long plain robe again, without any belt, hanging open down the front like an unbuttoned long coat: its two front edges fall straight from under the cape to just above his ankles, so that his shirt, his belt and his jeans show in the gap between them.
2. The robe's wide sleeves are pushed up to his elbows, and the robe is drawn in outline and left white, like the cape.
Nothing hangs from his belt. Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample of each. Set side by side on one floor line,
  without the model, they make the study; each one is image 2 of the scene
  edits below.

### 3.1 to 6.2 · the robe hitched up, then open

Image 1 is the picture as it stood, image 2 the figure of 34 for the
scene's stage: 34a for 3.1 to 4.2, 34b for 5.1 to 5.3, 34c for 6.1 and 6.2.
Every edit opens as the costume arc's do:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: every object, every robot, every line and the white background. Keep the man's face, his very short hair drawn as a thin solid black cap, his heavy stubble drawn as fine dots, his pose, his hands and everything he holds exactly as drawn. Use image 2 only for the man's clothes. Change only this:
```

Then it names the look:

- *Working* (3.1 to 4.2): "1. The man wears his long robe hitched up for work, exactly as the man in image 2: the front of its skirt is pulled up and tucked into the rope belt at both hips, so that the robe ends just below his knees in a few soft folds, and below it his legs show in plain jeans, drawn in outline and left white inside, down to his trainers. His hood is down, his sleeves are pushed up, the short rounded shoulder cape with the small gear emblem stays, and the small cold censer still hangs from his rope belt."
- *Organising* (5.1 to 5.3): "1. The man wears his long robe hitched up for work, exactly as the man in image 2: the front of its skirt is pulled up and tucked into the rope belt at both hips, so that the robe ends just below his knees in a few soft folds, and below it his legs show in plain jeans, drawn in outline and left white inside, down to his trainers. His hood is down, the short rounded shoulder cape with the small gear emblem stays, and nothing hangs from his rope belt: the censer is gone."
- *Delegating* (6.1, 6.2): "1. Over his own clothes, a plain shirt and jeans, the man wears the long plain robe hanging open down the front like an unbuttoned long coat, exactly as the man in image 2, without any belt: its two front edges fall straight from under the short rounded shoulder cape with the small gear emblem to just above his ankles, so that his shirt, his narrow belt and his jeans show between them, and its wide sleeves are pushed up to his elbows. Nothing hangs from his belt."

Then the pose, in one sentence that says what he still does:

| Slide | The sentence |
|---|---|
| 3.1 | He still stands on the stairs, stopped dead, a mug halfway to his mouth, his feet on the steps. |
| 3.2 | He still stands near the right end of the workbench, reading the single short sheet he holds in both hands. |
| 4.1 | He still stands frozen at the foot of the stairs, a half-eaten sandwich in his hand. |
| 4.2 | He still stands on tiptoe with both arms raised, pinning the large pictogram on the board. |
| 5.1 | He still leans in the plain wooden door frame with his arms folded, one eyebrow raised. |
| 5.2 | He still sits at the workbench with the open catalogue in front of him, one finger on the drawing of the reviewer robot; his knees are bent, and below the hitched-up robe his jeans show from the knees down. |
| 5.3 | He is still seen from behind at the edge of the picture, reaching for the narrow strip of paper in the letterbox slot of the glass door. |
| 6.1 | He still stands at the head of the table, clutching a stack of paper to his chest and adding another sheet to it. |
| 6.2 | He still sits at the table with an empty notepad; his knees are bent, and the open robe falls over his knees on both sides. |

5.3 shows him from behind, so its opening keeps "the man's head, his very
short hair drawn as a thin solid black cap" without the face and the
stubble, and its look says "the skirt of the robe" for "the front of its
skirt". Every prompt ends: "Everything else stays exactly as it is. Black and white only, apart from any colour already in image 1; no grey and no shading. No text anywhere. Landscape 16:9."

- **Made:** the first sample of each held, and only the man's box went back:

| Image | The man's box (x0, y0, x1, y1) |
|---|---|
| 3.1 | 1843, 600, 2320, 1411 |
| 3.2 | 1700, 600, 2140, 1457 |
| 4.1 | 2270, 640, 2700, 1454 |
| 4.2 | 1845, 800, 2142, 1449 |
| 5.1 | 1880, 600, 2217, 1141 |
| 5.2 | 1300, 780, 1900, 1453 |
| 5.3 | 400, 900, 1050, 1536 |
| 6.1 | 50, 560, 520, 1455 |
| 6.2 | 40, 560, 620, 1465 |

The paper's figures for chapters 3 to 6 use these pictures; their
alternative texts name no costume and need no change.

### 35 · `beat-06-context-1a.jpg` to `-1c.jpg` — 6.1's build-up

The worker's bar used to fill while 6.1 stood still, and on its own it did
not read. Now the slide builds up: three earlier moments of the same
meeting, each shown for about a second, then 6.1 itself. Image 1 is the new
6.1 of the edits above. Each edit changes only the table, the window, the
gauge and the worker's eyes.

35a, one low stack:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man at the head of the table with his long open robe, his stack of paper and the sheet he adds, the table and its legs, the worker robot sitting behind the table, the wide window frame standing free, the gauge on its stand, the empty recycling bin, the door frame and the reviewer robot at its own desk in the next room. It is the start of the same meeting. Change only this:
1. The table holds only one low, neat stack of a few sheets in front of the worker robot. All the other stacks of paper, the tangle of narrow paper strips and the long receipt hanging from the table to the floor are gone, so the table top and the floor under it are plain.
2. The window is clear: no sheets are taped on its panes.
3. The gauge's needle stands low, near the open left end of its arc.
4. The worker robot sits upright, its two eyes round and bright, each with a black pupil and a small white highlight.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

35b opens the same way with "It is earlier in the same meeting.", then:

```text
1. The table holds two stacks of paper, one on each side of the worker robot, each about as high as the worker robot's chin. The tangle of narrow paper strips and the long receipt are gone, so the floor under the table is plain.
2. Only two sheets are taped on the window; the rest of its panes are clear.
3. The gauge's needle stands in the middle of its arc.
4. The worker robot's eyes are round, each with a black pupil and a small white highlight, and it looks at the stacks.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

35c opens with "It is a little earlier in the same meeting.", then:

```text
1. The stacks of paper on the table reach only as high as the top of the worker robot's head, not above it, and a short paper receipt hangs over the front edge of the table without reaching the floor. The tangle of narrow paper strips is gone.
2. About half of the window's panes are covered with taped sheets; the others are clear.
3. The gauge's needle stands at about three quarters of its arc, just before the solid black end.
4. The worker robot's eyes are tired: in each round eye a heavy straight lid line runs across the middle, and a black pupil shows below it.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample for 35a and 35c, the second for 35b. Into each,
  three boxes of 6.1 were pasted back, so that only what grows changes from
  stage to stage: the man, from (40, 300) to (470, 1470) px; the sheet he
  adds, from (470, 540) to (700, 775); and the reviewer's room, from
  (2060, 230) to (2640, 1470). 35b's eyes were drawn again by the script of
  image 36; 35a keeps the model's pupils, which already have the highlight,
  and 35c its tired lids.
- **On the slide:** `build_up` in `deck.yaml` shows the three before 6.1,
  with the worker's bar at a quarter, half and three quarters, each on a
  slide of its own that waits for the click (since 2026-10-27; until then
  each stood 1.2 s, without a slide number, and moved on by itself); 6.1
  then shows the bar full and bursting (40). The stages carry 6.1's notes
  and their slide numbers. The paper's chapter 6 figure keeps 6.1.
- **Taller stacks:** in 35b the right stack already reached the worker's
  head, and in 6.1 the stacks stood only a little above it, where the author
  asked for stacks that grow over its head. Edit 19a below raised 6.1's
  stacks: its second sample is the one, the stacks leaning a little. Only
  the box from (470, 215) to (1330, 975) px went back, and inside it Steve's
  arm, hand and sheet were set back from 6.1 as they were, found as the
  lines that enter from the box's left edge and what they enclose, so he
  stays the same in all four stages. Edit 35d drew 35b again with both
  stacks at chin height: its second sample is the one, which kept the
  window's two sheets. The man, his sheet and the reviewer were pasted back
  from 6.1 as it stood before 19a, as for the other stages. The edit drew
  the worker's eyes with a slanted lid, so the script of image 36 drew them
  again whole, ring included, at the rings fitted to the drawing. Until 35d
  ran, a hand fix stood in: a band of sheets cut out of the right stack.

Edit 19a, which raised the stacks of 6.1:

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man at the head of the table with his long open robe, his stack of paper and the sheet he adds, the table and its legs, the worker robot sitting behind the table with its spiral eyes, the tangle of narrow paper strips, the long receipt curling across the floor, the wide window frame covered with taped sheets, the gauge with its needle at the solid black end, the empty recycling bin, the door frame and the reviewer robot at its own desk in the next room. Change only this:
1. The stacks of paper on the table on both sides of the worker robot tower high above its head: each stack is about twice as tall as it is now, a little crooked, its top far above the worker robot's antenna, but below the top of the window frame.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

Edit 35d, which drew 35b again with lower stacks, opens as 35b does:

```text
1. The table holds two short stacks of paper, one on each side of the worker robot. Each stack is low: its top is level with the worker robot's chin, well below its eyes, and nothing on the table reaches higher. The tangle of narrow paper strips and the long receipt are gone, so the floor under the table is plain.
2. Only two sheets are taped on the window; the rest of its panes are clear.
3. The gauge's needle stands straight up, in the middle of its arc.
4. The worker robot's eyes are round, each with a black pupil and a small white highlight, and it looks at the stacks.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

### 36 · the worker's eyes — drawn by a script

No new picture. Most pictures drew the worker's eyes as empty circles, a
few as dots, and only 6.2 with a pupil and a small highlight, which the
author chose for every picture. A script found each eye as a round white
area inside a dark ring, cleared it and drew a pupil and a highlight in
6.2's proportions, measured on its pixels:

- the pupil 0.71 of the eye's inner radius, turned towards what the worker
  looks at, as far as the eye leaves room;
- the highlight 0.29 of the pupil, at its upper right;
- drawn at four times the size and scaled down, so the edges stay smooth.

It drew them into 1.2 (the worker on the catalogue's page), 1.3, 2.1, 2.2,
2.3, 3.1, 3.2, 4.1, 4.3, 35b, 7.1, 7.2, 7a.1, 7a.2, 7b.1, 7b.3 and 8.1, the
worker card's portrait, both box-headed robots of `ref-cast.jpg`, so that a
new picture made from the plate draws them the same way, and the plates of
the two animations with the worker: the goodbye's pose A and 7b.1's plate.
In 4.3 the worker had only two dots, so the script drew the whole eye, its
ring included. `tools/goodbye_wave.py` and `tools/flying_sheets.py 7b.1`
then made the two animations again. A scene keeps another look where it
tells something (`storyline.md`, WORKER).

## Changed after the third run-through (2026-10-20)

After the author's third run-through, the lit windows and the stream of
7b.1 were changed without the model; the checks on the wall of 3.1 and the
threat's portrait took two edits through fal on the settings above, each
with two samples: four pictures, about 0.32 US dollars. `storyline.md`,
"The third run-through", has the decisions.

### 37 · the lit windows — 7b.3, 7c.1, 7c.2 and 8.2, drawn by a script

No new picture. On a white page a window "lit and left white" did not read
as lit, so the slides did not say which house was at work. Now the window
where the work happens glows lamp yellow, `#FCD64A`, lighter than the
candle's amber (`#F0B048` in the title picture), with a bare bulb in it, the
basement's bulb of 7b.1 drawn small: a cord, a black socket and a round
white glass in black lines (`storyline.md`, visual rule 2).

- **7c.1**, on `studies/anim-05-sheets-7c1-plate.png`: the dark inside of
  the open basement arch (393 to 455 by 1206 to 1300 px) turned yellow, its
  anti-aliased edge blended towards white, and a bulb hung from the apex.
  The rays already drawn beside the window stay. The upper windows and the
  office window stay black.
- **7c.2**, on `studies/anim-06-folders-7c2-plate.png`: the office's two
  panes (1267 to 1351 and 1360 to 1442 by 1062 to 1179 px) turned yellow,
  their edge blended towards black, with a bulb and six short rays in the
  left pane and three short rays on each side of the window, as at the
  basement window of 7c.1. The shut basement window turned solid black,
  like the house's other windows at night, its knob a white dot like the
  front door's.
- **The flights**: `tools/flying_sheets.py` made both loops and their
  stills again. Its palette now keeps any colour of a picture, not only
  red, and in 7c.1 the sheets start in the arch below the bulb and appear
  faster, since a half-faded black sheet read as an olive blot on yellow.
- **The paper** shows the two stills in chapter 10, so its figure changed
  with them; only the alternative text needed new words.
- **7b.3**, on `beats/beat-07b-isolation-3.jpg` itself, since it does not
  move: the office's two panes (1652 to 1870 and 1891 to 2110 by 784 to
  1086 px) turned yellow, with a larger bulb and its six rays in the left
  pane. No rays outside: the badge reader stands close on the right, with
  its own lamp. The basement window keeps its rays and the boxes that stay
  behind. The paper shows 7b.3 in chapter 8.
- **8.2**, on `beats/beat-08-team-2.jpg`: the office's far window in the
  pointed basement window (1965 to 1978 by 382 to 403 px) and, at the
  author's request, the glass of the bulb over the bench, both regions of
  it, inside and between the filament wires, turned the same yellow. The
  socket, the filament and the rays stay black and white. The paper shows
  8.2 in its Conclusion.
- A new generation of images 24, 25, 28 or 29 from their prompts would lose the
  light, since the prompts ask for no colour: draw it in again the same way.

### 12b · `beat-03-skills-1.jpg` and `-2.jpg` — 3.1 and 3.2, the checks on the wall

Image 1 is `beat-03-skills-1.jpg`. The picture did not show its title,
"every check a little different": it showed one check going wrong.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man on the stairs with his mug, his robe hitched up and the censer on his rope belt, the worker robot at the bench with its pencil and eraser, the clipboard, the eraser crumbs, the printout, the small printing machine, the booklet on its nail at the left, the stairs and the keys on their hook. Change only this:
1. On the empty white wall above the printing machine, to the left of the man's head and well clear of it, pin three small sheets of paper side by side in one neat row, each held by one small round pushpin at its top centre. Each sheet shows the same small grid of empty cells, like the printout: four columns and five rows.
2. Each sheet is marked by hand in black pen in its own different way: the first sheet has a small tick in a few cells, the second has circles drawn round a few other cells, the third has a small cross in a few cells and one cell struck through. The marks sit in different cells on each sheet, so no two sheets look alike.
3. Each sheet is about as tall as the worker robot's head. The row leaves clear white wall above the worker robot's head and around the man's head.
Everything else stays exactly as it is. Black and white only, pure white background, no grey, no colour. No text anywhere: no letters and no numbers on the sheets. Landscape 16:9.
```

- **Made:** the second sample is the one: ticks, circles and crosses, each
  sheet clearly its own. The model placed the row between the worker and
  the man, where 3.2 has its eraser shelf and the skill's label, so only
  the three sheets were cut out, scaled to 0.767 and set in a row from
  (1300, 140) px, on white wall in both pictures, clear of the man's head.
- **3.2** carries the first sheet, the ticks, three times in the same
  places, copied by hand: the same check every time. The fade from 3.1
  shows the circles and crosses turn into ticks while the arm comes and
  the eraser goes.
- The paper shows both in chapter 3; their alternative text names the
  sheets.

### 38 · `card-letter.png` — the threat's portrait

Image 1 is `beat-07a-safety-1.jpg`, for the letter and its strings.

```text
Create a new drawing for the same minimalist comic, one single object on a pure white page, landscape 16:9. Use image 1 only as the reference for the drawing style and for the long letter with its three strings: the worker robot there holds a long letter, and three thin strings run from the foot of the letter to the wrist of its other gripper. Draw only this, alone, large, in the middle of the picture, filling about four fifths of the picture's height and with wide white space on both sides:
The same long sheet of paper, folded once and held open, showing only a few thin lines of scribble and, at its foot, one short thick solid black line. Its top edge is clamped to the middle of a small wooden marionette control cross, the cross of two flat sticks that a puppeteer holds, drawn in outline. From the foot of the letter three thin, straight, taut strings run down and slightly apart and end in three small open loops, empty, waiting for a wrist. Nothing holds the cross and nothing is tied to the loops: no hand, no person, no robot, no floor line, no shadow.
The letter carries no wax seal, no stamp, no address. Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching, no colour. No text anywhere: no letters, no numbers, no words on the letter. Landscape 16:9.
```

- **Made:** the first sample is the one: the letter hangs from a clip under
  the cross, and the strings end in plain rings. The second clamped the
  letter with a peg that hid its top. The portrait was cut from 1119 to 1647
  by 82 to 1497 px, its near-white set to white, and every line thickened by
  two pixels (a minimum filter of 5), so that at the card's size its lines
  match the robots'. PNG, as cut, like the robots' portraits.
- Strings, not a bug: a bug reads as a fault in the program, and the
  strings are the story's own picture of outside text steering a worker
  (7a.1).

### 33a · 7b.1 — the stream in front of the casement

The sheets passed behind the open casement, swung into the room, and
appeared again in the dark of the window, which the author found odd: they
seemed to slip behind a door. `tools/flying_sheets.py` no longer hides them
behind the casement, so they cross in front of it and shrink into the dark.
The path, the plate and the paper's drawing stay as they were.

## Changed after the fourth run-through (2026-10-21)

After the author's fourth run-through, four pictures took an edit through
fal on the settings above, each with two samples: eight pictures, about 0.64
US dollars. The hourglass of 7c.2 came off without the model.
`storyline.md`, "The fourth run-through", has the decisions.

### 37a · 7c.2 — the hourglass gone

No new picture. The hourglass on the warehouse wall meant nothing to the
author, so on `studies/anim-06-folders-7c2-plate.png` the box from (2328,
722) to (2482, 1012) px, plain wall round the hourglass and its nail, was
painted white, and `tools/flying_sheets.py 7c.2` made the loop and the still
again. The badge of 7b.3 keeps its small hourglass. The paper shows the
still in chapter 10; its alternative text lost the hourglass. A new
generation of image 29 from its prompt would bring the hourglass back: paint
it out again.

### 39 · `beat-07b-isolation-1.jpg` — 7b.1, the reviewer and the rulebook

Image 2 is `beat-07-memory-2.jpg` (the same basement, the reviewer under the
stairs and the rulebook on its nail), image 3 `beat-07a-safety-1.jpg` (the
reviewer behind its glass under the same stairs).

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the open steel door to the rack of black archive boxes, the shelf with the black sealed folder and its red wax seal, the gatekeeper post with its lowered red paddle, the printing machine on the bench fed from the open black box, the worker robot reading its sheet, the stream of small sheets from its antenna through the open pointed window, the hanging bulb, the keys on their hook, and the man climbing the stairs. Add only two things, both taken from image 2, which shows the same basement on another day, and image 3:
1. Under the staircase on the right, in the white triangle below its slope and well below the man's feet, the small egg-shaped reviewer robot from images 2 and 3 (smooth sides, one large round lens as its only eye, a solid black band round its middle, a short antenna) sits on a small stool behind a pane of glass, exactly as it sits under the stairs in image 3: the glass drawn as a thin vertical frame with a few short diagonal glint lines. It is small, fits wholly under the stairs, and looks out towards the worker robot.
2. On the empty white wall between the shelf and the hanging bulb, higher than the shelf and well clear of the bulb, the slim booklet with a solid black cover and a small white label on it, hanging from a nail by a short loop of string, exactly as it hangs on the wall in image 2.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red of the wax seal and the red of the paddle. No text anywhere: no letters on the booklet's label. Landscape 16:9.
```

- **Made:** the second sample is the one: the reviewer's lens looks out
  towards the worker, where the first sample turned it away. Only two
  regions were taken from it, into the drawing and into the flight's plate
  `studies/anim-07-stream-7b1-plate.png` alike: the booklet's box from
  (1010, 350) to (1225, 660) px, and the white triangle under the stairs'
  outer stringer, nine pixels clear of it, down to the front floor line.
  `tools/flying_sheets.py 7b.1` made the loop again. The paper's chapter 8
  figure shows the drawing, so its alternative text names both.

### 39a · `beat-07b-isolation-1.jpg` — 7b.1, the arm rack

After his review of the same day the author wanted the arms on the wall as
well. Image 1 is the picture after edit 39, image 2 `beat-07-memory-2.jpg`.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the open steel door to the rack of black archive boxes, the shelf with the black sealed folder and its red wax seal, the black booklet hanging on its nail, the gatekeeper post with its lowered red paddle, the printing machine on the bench fed from the open black box, the worker robot reading its sheet, the stream of small sheets from its antenna through the open pointed window, the hanging bulb, the keys on their hook, the man climbing the stairs and the small reviewer robot behind its glass under the stairs. Add only one thing, taken from image 2, which shows the same basement on another day: the small rack that hangs from a nail beside the booklet in image 2, with its three hooks holding three spare jointed robot arms, one ending in a round magnifying glass, one in a small pair of tweezers, one in a small brush. Hang it on the empty white wall to the left of the booklet, above the shelf with the sealed folder and well clear of the folder, at the same height as the booklet, the same size as in image 2.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red of the wax seal and the red of the paddle. No text anywhere. Landscape 16:9.
```

- **Made:** both samples hung the rack in the same place; the first is the
  one. Only the box from (595, 250) to (890, 625) px, white wall in the
  picture before, was taken, into the drawing and the flight's plate alike,
  and `tools/flying_sheets.py 7b.1` made the loop again. The same day the
  deck gave the printing machine a label, program, on a click: it is the
  program the worker starts, which reads the real data.

### 40 · `beat-06-context-1.jpg` — 6.1, the last stage bursts

Image 1 is `beat-06-context-1.jpg` as it stood. Its gauge stood lower than
in `beat-06-context-1c.jpg`, so the build-up's last step went back instead
of over the edge.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man in his robe on the left holding a stack of paper and one sheet, the worker robot at the table with spiral eyes, the tall stacks of paper on the table, the tangle and the long printout spilling to the floor, the wide window with the notes pinned to it, the wastepaper basket, the door frame and the slim reviewer robot behind its glass wall on the right. Change only these:
1. The round needle gauge beside the window bursts: its needle is bent and slammed hard past the solid black right end of its arc, its glass cover is cracked by a few jagged lines, a small coil spring and two tiny screws fly off it into the air, and eight short straight burst lines radiate round the whole gauge.
2. The two tallest stacks of paper over the worker robot's head lean over and start to topple: their top sheets slide off and flutter down through the air, about ten loose sheets in flight between the stacks and the floor, a few already lying on the floor by the table.
3. Two small puffs of steam rise from the worker robot's antenna.
Everything else stays exactly as it is: the man, the reviewer and the window do not change. Black and white only, pure white background, no grey, no colour. No text anywhere: no letters, no numbers on the gauge. Landscape 16:9.
```

- **Made:** the first sample is the one: the cracked gauge throws a spring
  and two screws, and the sheets fall the whole way to the floor. Only the
  room between the man and the door frame was taken from it, from x = 500
  to 2098 px and from x = 470 below y = 1300, so the man and the reviewer
  keep their pixels through the build-up and the fade to 6.2. The deck
  fills the worker's bar and lets it burst with the gauge (`burst: true`),
  and the label context window moved above the flying spring. The paper's
  chapter 6 figure shows the picture; its alternative text says so.

### 41 · `beat-08-team-1.jpg` — 8.1, the letter in the post slot

Image 2 is `beat-07a-safety-2.jpg`, the worker posting the letter to the
reviewer.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the office cut open with its front wall removed, the door with the badge reader, the black-and-white barrier with its padlock, the gatekeeper post with its red paddle, the shelf with the black sealed folder and its red wax seal, the black booklet on its nail, the rack of three spare arms, the wide window, the needle gauge, the worker robot at its desk with its white folder, and the egg-shaped reviewer robot in its glass room on the right with the post slot in the front of the glass. Change only these:
1. Remove the sword and the long letter lying on the floor in front of the desk, with its loose wavy strings: the floor there is plain empty white.
2. Put that same long letter, folded once, a few thin scribble lines and one short thick black line at its foot, in the post slot in the front of the reviewer's glass room, half pushed through, the way the worker robot posts it in image 2. Its three thin strings hang slack and loose down the front of the glass, tied to nothing, their ends lying curled on the floor.
3. The small two-drawer filing cabinet between the shelf and the desk: draw it standing squarely on the floor against the back wall, seen straight on like the desk, not turned at an angle, its top drawer pulled out and holding a single index card.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colours are the red of the wax seal and the red of the paddle. No text anywhere: no letters on the letter. Landscape 16:9.
```

- **Made:** the second sample is the one: its letter sits in the slot at
  the size of a posted letter, where the first one's covered the front
  panel. Neither sample moved the filing cabinet, so only the box from
  (1180, 690) to (2470, 1395) px was taken, the desk, the floor and the
  front of the glass room; the cabinet keeps its place, and the deck sets
  the label auto memory on it instead, so the box in the middle explains
  itself. The paper does not show 8.1.

## Changed after the fifth run-through (2026-10-22)

After the author's fifth run-through, the two pictures of the post room
took three edits through fal on the settings above, each with two samples:
six pictures, about 0.48 US dollars. The planted letter now has an author,
a cartoon villain who watches through the basement window: gleeful in 7a.1,
sulking in 7a.2, where the post room holds. Security in 7a.2 faces the
worker, not Steve. After his look at the built deck, 6.2's /compact got a
picture of its own, edit 44, and a smile for the man in it, edit 44a; a
pass through the series step by step then cleared the minutes from 6.2's
own picture, edit 45. Each took two samples, six in all, for about 0.48
US dollars.
`storyline.md`, "The fifth run-through", has the decisions.

### 42 · `beat-07a-safety-1.jpg` — 7a.1, the villain at the window

Image 2 is `beat-07b-isolation-1.jpg`, for the small pointed window of the
basement.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man at the whiteboard on its easel seen from behind, the filing cabinet and the bench on the left, the worker robot at the foot of the stairs holding the long letter, the three taut strings from the foot of the letter to the wrist of its outstretched arm, the stairs with the ring of keys on its hook, and the egg-shaped reviewer robot behind its glass under the stairs. Add only one thing, in the empty white space high up, above the worker robot's head, between the top of the whiteboard and the top of the stairs:
1. A small basement window set high in the wall, with a pointed arch at its top like a tiny chapel window and a thin frame, the same shape as the small pointed window in image 2; its glass is plain white.
2. Outside, filling that window, a cartoon villain peers in: a thin man with a tall black top hat, a long black moustache curled up at both ends, narrow eyes and a wide sly grin. He rubs his two hands together just under his chin, with three short curved motion lines beside them, and looks down at the worker robot and its letter. Only his head, his hat, his hands and the top of his shoulders show in the window.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the second sample is the one: its window is whole, where the
  first one's villain spilled out of a half-drawn frame. Edit 42a followed.

### 42a · the villain's nose

Image 1 is the second sample of 42.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man at the whiteboard, the worker robot with its letter and strings, the stairs with the keys, the reviewer robot under the stairs, the pointed window high up, and the villain in it with his tall black top hat, his narrowed eyes, his raised eyebrows, his long black moustache curled up at both ends, his wide grin, his black coat and his two hands rubbing together with the short motion lines beside them. Change only his nose: draw it small, short and straight, a small neat button nose sitting just above the moustache, so that the face reads as a thin, clean-shaven silent-film villain with a big curled moustache. Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the one: a small straight nose and a neat
  grin. Only the window's box, from (1512, 100) to (1880, 592) px, plain
  white wall before, was taken into the picture. The paper's chapter 9
  figure uses it; its alternative text names the villain. Keep the nose
  small in any later edit of him.

### 43 · `beat-07a-safety-2.jpg` — 7a.2, security faces the worker, the villain sulks

Image 2 is the first sample of 42a, for the villain.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man with his mug on the left, the filing cabinet and the bench, the stairs, the ring of keys on its hook under the stairs, the worker robot at the glass door taking the narrow strip from the letterbox slot, the reviewer robot at its desk in the glass room with the letter and the slack strings, and the gatekeeper post bolted to the floor with its base plate, its jointed arm and its raised round red paddle. Change only these:
1. The gatekeeper faces the worker robot on its right: turn its peaked cap so that the black visor points right, towards the worker robot, and move its round lamp to the right-hand face of the post, facing the worker. The post, its base plate with the bolts, its arm and its red paddle stay exactly where they are.
2. High up on the left, in the empty white space above the man's head and clear of the stairs, the small window with a pointed arch from image 2, the same size, and in it the same villain from image 2, with the same tall black top hat, the same small straight nose and the same long curled moustache. Now he sulks: his arms are folded, his mouth is turned down under the moustache, his eyebrows are drawn together, and he glares at the reviewer's glass room.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colour is the red of the paddle. No text anywhere: the paddle is blank. Landscape 16:9.
```

- **Made:** both samples turned the cap and the lamp; the first is the
  one, since its window sits in the empty corner, clear of the man's head.
  Two boxes were taken: the window, from (96, 72) to (464, 560) px, plain
  white wall before, and the post's head, from (952, 776) to (1208, 1072)
  px, where the visor now points at the worker and the lamp sits on the
  post's right face. The keys, the paddle and the room keep their pixels.
  The paper's chapter 9 figure uses this picture.

### 44 · `beat-06-context-2a.jpg` — 6.2, /compact files the stacks

6.2 shows the room's states one after the other. At /compact, 6.1's
second stage stood in at first; the author asked
for a picture of its own, a small, orderly cupboard with the documents in
it. Image 1 is `beat-06-context-1b.jpg`, so the man and his stack stay as
they stand in 6.1.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man at the head of the table with his long open robe, his stack of paper and the sheet he adds, the table and its legs, the worker robot sitting behind the table with its round bright eyes, the wide window frame with its few taped sheets, the gauge on its stand with its needle straight up in the middle of its arc, the door frame and the reviewer robot at its own desk in the next room. The meeting has just been tidied up. Change only this:
1. The two stacks of paper on the table are gone, so the table top on both sides of the worker robot is plain. In their place, on the table to the right of the worker robot, stands one small, neat cupboard, about as tall as the stacks were and a little narrower than one of them: a plain wooden cupboard with its two doors open, and inside, on two shelves, a short row of slim folders standing upright in good order, each with a small blank tab.
2. The recycling bin by the door holds a few crumpled sheets of paper, up to about half its height.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the one: its bin is drawn as in 6.2, the
  crumpled sheets above the rim, where the second drew the bin as if it
  were glass. It lay on image 1 to the pixel, so three boxes were taken
  into image 1: the worker's head and the table on its right with the
  cupboard, from (680, 640) to (1560, 992) px; the left stack's place,
  from (495, 830) to (680, 992); and the sheets in the bin, from
  (1865, 1140) to (2090, 1263). The man, his stack and his sheet, the
  window's three sheets, the gauge and the reviewer's room keep their
  pixels. The cupboard's folders carry no lettering.
- **On the slide:** 6.2's two `steps`, the slides for /compact and for
  auto-compact, show it with the bar at half; the slide itself, /clear,
  follows with the cleared room and a hint in the bar.

### 44a · `beat-06-context-2a.jpg` — Steve smiles

The man kept the worried face of 6.1 at first; the author asked for a
happier one once the stacks are filed. Image 1 is the picture of 44.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man at the head of the table with his long open robe, his stack of paper and the sheet he adds, his head, his short black hair, his ears and his stubble, the table, the worker robot, the small cupboard with its folders, the window with its taped sheets, the gauge, the recycling bin, the door frame and the reviewer robot in the next room. Change only the man's face: he looks relieved and happy now, with a warm, contented smile, his eyebrows relaxed and a little raised, his eyes calm and friendly, looking at the worker robot. His head stays exactly where it is, the same size and at the same angle. Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** both samples smiled; the second, with the warmer smile, is the
  one. Only the head, from (260, 330) to (445, 605) px, was taken in; its
  edges lie on image 1 to the pixel, so the hood, the stack and the sheet
  keep their pixels.

### 45 · `beat-06-context-2.jpg` — 6.2, /clear keeps nothing

A pass through the context series step by step, slide by slide and click
by click, found the cleared room still carrying the minutes of the old
6.2, which showed all three tools in one picture: a sheet pinned in the
window's corner and a narrow strip on the table. With /compact in a
picture of its own, they contradicted "Everything goes". Image 1 is
`beat-06-context-2.jpg`.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man sitting on his stool at the table with his open robe and his empty notepad, the table and its legs, the plain white folder standing on the table, the worker robot behind the table with its round bright eyes, the wide window frame, the gauge on its stand with its needle low, the full recycling bin with the two crumpled sheets beside it, the door frame and the reviewer robot at its own desk in the next room. Everything has been cleared away. Change only this:
1. The window is completely clear: the sheet taped in the top corner of its right pane is gone, with its two strips of tape, so both panes are plain white inside their frames.
2. The narrow paper strip that curls over the front edge of the table and hangs down is gone, so the table top, its front edge and the space below it are plain.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** each sample did one of the two cleanly. The second cleared
  the window and left the rest in place, while the first redrew the
  window frame; the first took the strip away and kept the table's lines,
  while the second moved them a little. So two boxes were taken: the
  window's top corner from the second sample, from (1540, 275) to
  (1720, 495) px, and the table's front edge from the first, from
  (1305, 955) to (1520, 1140), where the table leg now runs whole. Both
  lay on image 1 to the pixel; the man, the folder, the gauge, the bin and
  the reviewer's room keep their pixels.
- **In the paper:** chapter 6's figure uses this picture, so its
  alternative text and caption no longer name the strip.

## Added for the paper's diagrams (2026-10-26)

Since 2026-10-26 the paper draws two diagrams in Excalidraw, the tool call of
chapter 4 and the lethal trifecta of chapter 9, and puts the talk's cast
into them where each acts. The talk's portraits looked pasted in beside the
diagrams' hand-drawn boxes, so the author asked for the cast in the
diagrams' own look. One character sheet holds all five, so they share one
hand. The slides keep their drawings; only the paper's diagrams use these.

### 46 · the diagram cast, in the Excalidraw look

- **Model and settings:** as for every image above, on the edit route
  `google/nano-banana-2.1/edit`, with `num_images` 2.
- **References:** image 1, the four card portraits and the man of
  `ref-steve.jpg` in his own clothes, side by side on white
  (`card-worker.png`, `card-reviewer.png`, `card-security.png`,
  `card-letter.png`);
  image 2, a small Excalidraw scene of boxes, arrows, a circle and a red
  dot, with no text, exported from the same pipeline as the diagrams.
- **Prompt:**

```
A character sheet of five figures for a whiteboard diagram, on a pure white background, landscape 16:9. Use the attached images as references: image 1 for what each figure looks like (the five figures from left to right), image 2 only for the drawing style, the look of the Excalidraw whiteboard app. Draw only what this prompt names.

Drawing style, as in image 2: rough hand-drawn lines like a felt-tip marker on a whiteboard, one medium line weight, every line with a slight wobble, some lines drawn with a second stroke that does not quite match the first, corners that overshoot a little, simple geometric shapes. Much simpler than image 1: fewer lines, no bolts, no fine details, no dotted stubble. Small areas of solid black stay solid black, filled loosely by hand. Black and white only: no grey, no shading, no gradients, no hatching; the only colour is the round paddle, in the red of image 2.

Five figures stand in one row with plenty of white space between them, each whole, each about two thirds of the image height, no floor line, no ground, no shadows. From left to right:
1. The worker robot, as figure 1 in image 1, facing the viewer: a square head with two round eyes, each with a black pupil and a small white highlight, and a short antenna; a rounded box body with a solid black band round its chest; two thin jointed arms ending in two-finger grippers; one single wheel instead of legs. It holds a sheet of paper in one gripper and writes on it with a pencil in the other: it is doing the work.
2. The reviewer robot, as figure 2 in image 1: a tall egg-shaped body with one large round eye near the top and a short antenna, a solid black band round its middle with a slot, smooth sides with no arms. A short strip of paper hangs out of the slot, and its eye looks down at the strip.
3. The guard post, as figure 3 in image 1: a tall square post on a flat base plate, a peaked guard's cap on top, one round porthole eye, and one thin arm that holds up a round red stop paddle on a short stick. The paddle is blank.
4. The planted letter, as figure 4 in image 1: a long sheet of paper with a few short scribbled lines, held by a clip under a puppeteer's wooden cross; three thin strings run down from the cross past the sheet to three small rings.
5. The programmer, the man of figure 5 in image 1: short dark hair drawn as a solid black cap, a few short marks for stubble, an open-collared shirt, trousers, a small ring of keys on his belt. He holds a clipboard in one hand and a pencil in the other, about to tick a box: he decides.

No text anywhere: no letters, no numbers, no question marks, no speech bubbles, no labels, no logos. Paper shows only a few short scribbled lines.
```

- **Check:** the five in order; the worker writing, its eyes with pupil
  and highlight, one wheel; the reviewer without arms, the strip from its
  slot; the guard with one paddle, red, blank; the letter on its cross with
  three strings and rings; the man with clipboard and pencil; no text, no
  floor line.
- **Made on 2026-10-26**, two samples; the first, the rougher of the two
  and closer to Excalidraw's stroke (its paddle is hatched like an
  Excalidraw fill), is kept as `studies/excalidraw-cast-sheet.jpg`. The
  guard gained a second, hanging arm, which the diagrams can bear.
- **Cut and thickened by script:** each figure is cut at the empty columns
  between them, the white outside its outline made transparent (the white
  between the letter's strings too) and the white inside kept, so a figure
  stands on a shaded box without showing it through. Its lines are then
  thickened by seven pixels, a minimum filter on the colour and a maximum
  filter on the alpha, so that drawn at 130 to 210 diagram units they print
  as thick as the boxes' strokes.
- **Cost:** two images, 0.16 US dollars.

## Added for the secret level (2026-10-27)

At the author's request the deck gained a short story for the questions,
hidden at the very end (`storyline.md`, "The secret level"); since
2026-10-28 it is beat 10, right after the closing slide, and its pictures
are `beat-10-oversight-1.jpg` and `-2.jpg` (`beat-09s-…` before). The EU raps
Steve's knuckles when he hands the worker his stamp, and a pocket
calculator answers it. The EU is a new character, a ring of twelve stars
with two gloves and a gavel, black and white like the cast; the deck floats
its name, EU `<Art. 14>`, beside it. Ten generations with the two fixes of
that evening (47b, 48a), 0.80 US dollars.

### 47 · `beat-10-oversight-1.jpg` — 10.1 A rap on the knuckles

- **Slide:** 10.1, the whole slide (hidden as 9s.1 until 2026-10-28).
- **Make:** image 1 `ref-cast.jpg`, image 2 `beat-05-subagents-1.jpg` (the
  stamp and the sheets), image 3 `beat-08-team-2.jpg` (the man on his
  stool); `num_images` 2.
- **Shows:** the man holds his stamp out to the worker, and the EU's gavel
  comes down on his knuckles before the worker has it.

```text
Create a new drawing for the same minimalist comic, one single scene, landscape 16:9. Use the attached images as references and match them exactly: image 1 is the cast sheet (the man at the fourth stage, the fourth man from the left, in his own clothes with a mug, and the worker robot with pupils in its eyes, at the sizes shown there), image 2 shows the large rubber stamp and the pile of printed sheets, image 3 shows the man sitting relaxed on his wooden stool with his mug, and the plain wooden workbench. Draw only what this prompt names.

On a thin floor line: on the left, the man sits back on his simple wooden stool, relaxed, a mug of tea in his left hand resting on his knee. He stretches out his right arm and holds out the large rubber stamp from image 2, handle first, to the worker robot, which rolls up close in front of him in the middle of the picture and reaches eagerly for the handle with one gripper, its eyes wide and bright. Behind the robot, on the right, stands a plain wooden workbench with a tall, neat pile of freshly printed sheets on it, each a grid of blank cells.

Above the man and the robot, with a clear band of white space above it, floats a new character, the EU: twelve small five-pointed stars drawn in outline, all pointing upwards, set evenly in a circle like the hours on a clock face, the circle about twice the width of the man's head. Inside the circle of stars there is a simple face: two round eyes with black pupils, two short stern eyebrows slanting down towards the middle, and a small flat mouth. It has no body and no arms. Beside the circle float two plump white cartoon gloves with no arms attached. One glove brings a small wooden judge's gavel down on the knuckles of the man's outstretched right hand: three short curved motion lines above the gavel, and a small burst of short straight lines where it lands. The other glove is raised with its index finger up, as if saying no.

The man winces: his eyes squeezed shut, his mouth a wavy line, his fingers springing open around the stamp's handle; the stamp is still in his hand, it has not reached the robot.

Characters, as on the cast sheet: the man at the fourth stage (in control): late thirties, medium build, an oval face with heavy stubble drawn as fine dots, very short hair drawn as a thin solid black cap, no glasses; his own clothes: a plain long-sleeved shirt with a collar and a row of small buttons down the front, drawn in outline and left white, tucked into plain jeans that are drawn in outline and left white inside, with a narrow plain belt, and plain trainers; a ring of large keys on a clip at his right hip. The worker robot is hip-high, the top of its head level with a standing man's hip: a rounded box body with a solid black band round its chest, a square head with two round eyes, each with a black pupil and a small white highlight, and a short antenna, two thin jointed arms with two-finger grippers, one wheel and no legs.

Keep the top right corner of the picture empty: the right sixth of the width and the top fifth of the height are plain white. Keep the bottom right corner empty: in the right twelfth of the width and the lowest tenth of the height there is nothing but the floor line.

This picture has no colour: the stars are black outlines on white, not blue and not gold. The stamp's face is blank, the sheets carry only grid lines, and the gavel and the gloves carry no marks.

Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching; colour appears only on objects described as red or amber. No walls and no room unless the scene names them: a thin floor line and the objects named. One single scene, no panels, no borders. Landscape 16:9, at least 2400 px wide. No text anywhere: no letters, no numbers, no speech bubbles, no captions, no logos, no signs with words. Paper shows only a few thin lines; any laptop screen faces away.
```

- **Check:** the stamp still in the man's hand and the gavel over his
  knuckles; the worker's gripper open, reaching; twelve stars, no circle
  round them, no colour; the face A4; no text on stamp, gavel or sheets;
  the top right corner free.
- **Made on 2026-10-27**, two samples. The first is the image: the stamp
  is still in the man's hand, where the second had already passed it to
  the worker. Its EU, though, stood on a disc, a circle drawn round the
  stars, which read as a medal; the second drew the ring of the emblem,
  stars alone. Edit 47a below drew that ring but thinned the stars, so a
  script took the circle off the first sample instead: it fits the circle
  to the outline at 720 angles (centre 1411, 324 px, radius 238 px) and
  paints the line white along 7,200 rays, three pixels to spare on either
  side of it, the stars and the face untouched. The ring nearly reaches the top edge, so the deck floats the
  EU's name beside it, right of the raised finger.

### 47a · the ring without its circle (tried, not kept)

Image 1 is the first sample of 47, image 2 the second.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man on his stool with his mug, his outstretched hand holding the stamp, the glove with the gavel and its motion lines, the raised glove with its index finger up, the worker robot reaching out, and the workbench with the pile of sheets. Change only one thing:
1. The EU character: remove the large circular outline around it, so that its twelve small five-pointed stars stand free in a ring around its face, with nothing joining them, exactly like the ring of stars in image 2. Keep the stars where they are, at the same size, all pointing upwards, and keep its face exactly as it is: the stern eyebrows, the two round eyes with black pupils and the small flat mouth.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
```

- **Made on 2026-10-27**, one sample: the circle went, but the stars and
  the face came back in a thinner line than the rest of the picture, and
  the whole drawing moved by a few pixels. The script described under 47
  did the job instead.

### 47b · `beat-10-oversight-1.jpg` — 10.1, one hand

The author found the hand wrong: it held the stamp in a fist, and four more
fingers splayed out beside it, from the prompt's "fingers springing open".
Image 1 is the picture as made under 47.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man on his stool with his wincing face, his mug and his outstretched right arm, the large rubber stamp and its position, the floating glove with the gavel above his hand and its motion lines, the burst of short lines beside the gavel, the ring of twelve stars with its stern face, the raised glove with its index finger up, the worker robot reaching out, and the workbench with the pile of sheets. Change only the man's right hand:
1. It is one single, normal hand with exactly four fingers and one thumb, closed firmly in a fist round the round wooden handle of the stamp, seen from the side, the back of the hand and its knuckles facing up towards the gavel. Remove the extra open fingers that stick out to the right of the fist and the short curved lines between them: there are no other fingers anywhere near the stamp.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour. No text anywhere. Landscape 16:9.
```

- **Made on 2026-10-27**, two samples, both with one fist; the first is
  kept. Only the hand's box, from (955, 595) to (1175, 790) px, was taken
  into the picture, after a search for the best shift found none, and the
  edit's faint grey specks in that box were set white (a light pixel with
  no dark one within 3 px).

### 48 · `beat-10-oversight-2.jpg` — 10.2 But: the calculator

- **Slide:** 10.2, the whole slide (hidden as 9s.2 until 2026-10-28).
- **Make:** an edit of image 47, `beat-10-oversight-1.jpg`, as image 1;
  `num_images` 2.
- **Shows:** the same framing; the man asks with a calculator, and the EU,
  puzzled, offers him a stop button while the worker works on.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything else in the picture exactly as it is: the stool, the floor line, the workbench with its pile of sheets, the EU's ring of twelve stars with its face in the middle and its two floating white gloves, the man's face, his shirt, his jeans, his belt and keys, and his left hand with the mug. Change only these:
1. The man no longer holds out the stamp: the large rubber stamp now rests in his lap, under his left forearm. With his right hand he holds up an old pocket calculator towards the EU: a small upright rectangular box with a blank display window at its top and a grid of small blank square keys. A small sticking plaster sits across the knuckles of that hand. He looks up at the EU with one eyebrow raised and a small, friendly smile, as if asking a question.
2. The EU is no longer stern: its eyes look at the calculator, its eyebrows raised high, its mouth small and open, puzzled. The glove with the gavel hangs lowered beside the ring of stars, the gavel pointing down, with no motion lines and no burst lines. Its other glove, open and palm up, holds out towards the man a big round red push button on a small square box.
3. The worker robot has rolled over to the workbench on the right and works calmly through the pile of sheets, one sheet held in its grippers, its eyes on the sheet.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; the only colour is the red of the push button. No text anywhere: no numbers, letters or symbols on the calculator's keys or display, and no lettering on the button. Landscape 16:9.
```

- **Check:** the plaster on the knuckles; the calculator's keys and window
  blank; the stamp in the man's lap, not with the worker; the gavel down;
  red only on the button; the ring of stars where 47 has it.
- **Made on 2026-10-27**, two samples. The first is the image: the button
  is offered between the man and the worker, where the second held it out
  over the worker's head, and its stamp in the lap read as a gavel. Its
  button came out again in 48a.

### 48a · `beat-10-oversight-2.jpg` — 10.2, the button taken out

The red button stood for Article 14(4)(e) of the AI Act, a "'stop' button
or a similar procedure", but the author did not read it so; the EU now
scratches its ring of stars, and the open question stays in the picture.
Image 1 is the picture as made under 48.

```text
Edit image 1. Keep the camera, the framing, the drawing style and everything in the picture exactly as it is: the man on his stool holding up the calculator, with the plaster on his knuckles, his mug and the stamp in his lap, the ring of twelve stars with its puzzled face looking at the calculator, the glove with the lowered gavel, the worker robot at the workbench with its sheet, and the workbench with the pile of sheets. Change only the EU's second glove:
1. Remove the red push button and its small box completely: nothing is held out to the man any more.
2. That glove now floats beside the upper right of the ring of stars and scratches the ring with one finger, as a puzzled person scratches their head, with two or three short curved lines beside the finger.
Everything else stays exactly as it is. Black and white only, pure white background, no grey; this picture has no colour at all. No text anywhere: no question marks, no symbols. Landscape 16:9.
```

- **Made on 2026-10-27**, two samples; the first is kept, since its face
  still looks at the calculator, where the second crossed its eyes. Two
  boxes were taken, the button's place, from (1370, 540) to (1610, 735)
  px, and the scratching glove's, from (1550, 100) to (1790, 330) px, both
  without a shift and cleared of the edit's grey specks. The picture has
  no colour left.

### 49 · `card-eu.png` — the EU's portrait

Image 1 is `beat-10-oversight-1.jpg`, for the EU.

```text
Create a new drawing for the same minimalist comic, one single character on a pure white page, landscape 16:9. Use image 1 only as the reference for the drawing style and for the EU character: the ring of twelve small stars with a face in the middle, and the two floating white cartoon gloves, one of them holding a small wooden judge's gavel. Draw only this character, alone, large, in the middle of the picture, filling about four fifths of the picture's height, with wide white space on both sides:
The same twelve small five-pointed stars drawn in outline, all pointing upwards, set evenly in a ring like the hours on a clock face, with nothing joining them. Inside the ring the same simple face: two round eyes with black pupils, two short eyebrows, slightly stern, and a small mouth with the hint of a smile. On the left of the ring floats one glove, holding the small wooden gavel upright, ready; on the right floats the other glove, raised with its index finger up. No man, no robot, no stamp, no floor line, no shadow, no motion lines.
Minimalist black ink line drawing on a pure white background, a little more than stick figures: simple shapes, few lines, one even line weight, a few small areas of solid black. Black and white only: no grey, no shading, no gradients, no hatching, no colour: the stars are black outlines on white, not blue and not gold. No text anywhere: no letters, no numbers, no words. Landscape 16:9.
```

- **Made on 2026-10-27**, one sample, kept. The portrait was cut 24 px
  outside the drawing, from 400 to 2402 by 183 to 1366 px, scaled to
  800 px high and its near-white set to white. Its lines were not
  thickened: drawn this large, they already stand a little heavier on the
  card than the robots' do.

## Changed after the author's look at the built deck (2026-10-28)

The author went through the built deck once more before the submission and
found three pictures to mend: 4.3's low table with the plain folder, which
drew the eye from the lock; 5.1's tick, which lay backwards on the sheet,
while the stamp's face stayed blank; and Steve's lowered hood in 6.1's four
pictures and the picture of /compact, broken on the viewer's left, where a
straight cut ended its outline and loose strokes lay under it. Three edits
went through fal on the settings above, each with two samples: six
pictures; 5.1 took two rounds more and a script (16d). Then the villain of
7a.1 took his letter into his own hand (42b), and the Book of Secrets left
the office of 8.1 (5c). Each result went in only where it changed something, so
everything else keeps its pixels, and each picture was saved again at the
quality the others carry. `storyline.md`, "The last look at the pictures",
has the decisions.

### 4b · `beat-04-hooks-3.jpg` — 4.3, the low table gone

```text
Edit image 1. Keep the camera, the framing, the drawing style, the line weight and everything in the picture exactly as it is: the worker robot at its workbench with the feather duster in its outstretched gripper, the gatekeeper post bolted to the floor with its peaked cap, its lamp and its round red paddle pressed against the gripper, the striped barrier with its padlock, the low wall shelf on the far right with the black sealed folder and its red wax seal, and the thin floor line. Change only this: remove the small low table in the bottom centre of the picture together with the white folder standing on it, and remove the two long curved lines that run across the floor from the worker robot's wheel towards that table. Where they were, leave plain white paper, and let the thin floor line run on unbroken. Nothing new appears in their place. Everything else stays exactly as it is, to the pixel where possible. Black and white only, pure white background, no grey; the only colours stay the red of the paddle and the red of the wax seal. No text anywhere. Landscape 16:9.
```

- **Made:** both samples cleared the table, the folder and the two lines.
  Only the clearing was taken from the first: in the box from (690, 1110)
  to (1760, 1536) px, every pixel the edit left white, 3 px clear of its
  own lines, was set to white, so the wheel, the bench's legs and the bases
  of the post and the barrier keep their pixels. The paper does not use
  this picture.

### 16d · `beat-05-subagents-1.jpg` — 5.1, the stamp and its print

```text
Edit image 1. Keep the camera, the framing, the drawing style, the line weight and everything in the picture exactly as it is: the worker robot with its contented closed eyes, the large rubber stamp in its raised gripper, the hand-cranked printer and its paper strip, the table, the pile of grid sheets with the solid black blot on the top sheet, the gatekeeper post far back with its lowered red paddle, the man leaning in the free-standing door frame with his arms folded, and the floor lines. Change only these two things:
1. The tick on the top sheet, right beside the blot, is redrawn as a clear, upright check mark as the viewer sees it: a short stroke going down from the upper left to the lowest point, then a much longer stroke rising steeply from that point to the upper right, like the symbol ✓. It stands upright on the sheet, not lying flat, in the same solid black line as before, about the same size.
2. The flat rubber face on the underside of the stamp, the large rectangle that faces the viewer, now shows the same check mark, drawn in a bold black line in the middle of the rubber face, so it is clear that the stamp printed the tick.
Everything else stays exactly as it is, to the pixel where possible. Black and white only, pure white background, no grey; the only colour stays the red of the gatekeeper's paddle. No letters, no numbers, no other text anywhere. Landscape 16:9.
```

- **Made:** both samples drew a tick on the stamp's face, but neither drew
  the sheet's well: the first left it lying backwards, the second stood a
  large one up over the sheet's edge. The author then pointed out that a
  stamp carries the mirror image of its print, and that the robot, which
  stands behind the table and faces the room, stamps the sheet the right
  way round for itself. Two more edits, each with two prompts and two
  samples, eight pictures, mirrored the stamp's tick, first left to right,
  then top to bottom; none was kept, since the sheet's tick had to turn as
  well. So a script drew both marks in an 11 px black line with round ends,
  on the picture with the old tick taken off the sheet and the stamp's face
  blank as before the first edit:
  - the sheet: a tick that reads right from the robot's side and stands
    upside down for the room, its corner at the top, (1300, 975) px, its
    short stroke down to the right to (1323, 1006), its long stroke down to
    the left to (1219, 1024);
  - the stamp's face: the mirror image of that print as the face shows it
    once the robot has tipped it up towards the room, turned over top to
    bottom: its corner at the bottom, (1140, 805), its long stroke rising
    to the left to (1051, 751), its short stroke to the right to (1165, 771).

  Everything else keeps its pixels.
- **In the paper:** chapter 5's figure uses this picture; its alternative
  text and caption still hold.

### 35a · `beat-06-context-1a.jpg` to `-1c.jpg`, `-1.jpg` and `-2a.jpg` — Steve's hood

Image 1 is `beat-06-context-1a.jpg`, image 2 `ref-steve.jpg`, whose fourth
figure wears the hood lowered.

```text
Edit image 1. Image 2 is the reference sheet of the same man. Keep the camera, the framing, the drawing style, the line weight and everything in image 1 exactly as it is: the man standing at the left with his worried face, his short black hair, his ears and his stubble, his long open robe, the short rounded shoulder cape with the small gear emblem, his sleeves, his hands holding the stack of paper and the single sheet, his trousers and trainers, and the whole room: the table, the worker robot, the window, the gauge, the bin, the door and the reviewer robot. Change only the man's lowered hood behind his neck: redraw it as one simple, soft, rounded cowl that lies flat behind his neck and rests evenly on the shoulder cape, symmetric on both sides of his neck, exactly like the lowered hood of the fourth man from the left in image 2. Remove the stray pointed flap that now sticks out sideways over his left shoulder (on the viewer's left), so the outline of his shoulder and cape is smooth there. The hood's front edge meets his neck cleanly below the jaw on both sides and does not touch his face. His head stays exactly where it is, the same size and at the same angle. Everything else stays exactly as it is, to the pixel where possible. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** both samples drew a whole hood; the first is the one, its
  hood closest to the reference. It lay on image 1 to the pixel, its jaw
  line included, but it drew the stubble anew. So only the box from
  (170, 470) to (440, 650) px was taken, without the inside of the face,
  which is filled from the cheek in each picture: the hood and the neck
  are new, the jaw line lies where it lay, and the stubble keeps its dots.
  The box held the same pixels in 6.1's four pictures and nearly the same
  in /compact's, whose face is another, so the one hood went into all five.
  The edit's light grey specks were set to white.
- **In the paper:** chapter 6's figure uses `beat-06-context-1.jpg`; its
  alternative text and caption name no hood.

### 42b · `beat-07a-safety-1.jpg` — 7a.1, the letter in the villain's hand

The strings ran from the letter in the worker's own gripper to its other
wrist, and the villain only rubbed his hands at the window, so nothing
showed who pulls them. The author asked for the puppeteer's cross of the
threat's card in the villain's hand. Image 1 is the picture as made under
42a, image 2 `card-letter.png`. Three ideas went out, each with two samples:
the cross steering the worker's wrist directly (A), the villain holding the
letter on the cross with the letter's strings pulling the wrist (B), and
the cross working the letter in the worker's gripper (C). The author chose
the first sample of B.

```text
Edit image 1. Image 2 shows the planted letter: a long letter clipped under a small wooden marionette control cross, the cross of two flat sticks a puppeteer holds, with three thin strings running from the foot of the letter. Keep the camera, the framing, the drawing style, the line weight and everything else in image 1 exactly as it is: the man at the whiteboard on its easel seen from behind, the filing cabinet and the bench on the left, the stairs with the ring of keys on its hook under them, the egg-shaped reviewer robot behind its glass under the stairs, the worker robot at the foot of the stairs with its arm stretched out stiffly towards the stairs, and the small pointed window high up with the villain in it: his tall black top hat, his narrow eyes, his long black moustache curled up at both ends, his sly grin and his small, short, straight nose. Change only this: 1. The villain reaches out of the window and holds up, in one hand, the planted letter exactly as in image 2: the small wooden control cross in his hand, the long letter hanging from a clip under the middle of the cross, just below and in front of the window. His other hand rests on the window sill. 2. The worker robot no longer holds the letter: its first gripper is empty and lowered, and it looks up at the hanging letter and reads it, its eyes wide, its pupils on the letter. 3. From the foot of the hanging letter three thin, straight, taut strings run down through the air to the wrist of the worker robot's outstretched arm and pull it stiffly towards the keys. Remove the old strings that ran from the letter in its gripper. Black and white only, pure white background, no grey; no colour. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample is the one; its villain keeps the small,
  straight nose. It lay on image 1 to the pixel, so two areas were taken:
  the window, the villain, the cross and the letter, from (1420, 95) to
  (1890, 800) px, and the worker with the strings, from (1090, 780) down to
  the floor, bounded on the right by a line 18 px left of the stairs' edge.
  Steve, the easel, the stairs, the keys and the reviewer keep their
  pixels, and the edit's light grey was set to white.
- **On the slide:** the label prompt injection moved beside the hanging
  letter; the threat's card after it shows the same cross.
- **In the paper:** chapter 9's figure uses this picture; its alternative
  text now names the villain holding the letter, and its caption still
  holds.

### 5c · `beat-08-team-1.jpg` — 8.1, synthetic data behind the gate

The Book of Secrets lay on the shelf behind the barrier in the office, where
it must never be: the office works on practice data only (7b, 7c.2). The
author asked for something in its place; three ideas went out, each with two
samples: a stack of white folders, a small open box of white folders, and a
small filing cabinet. The author chose the first sample of the stack.

```text
Edit image 1. Keep the camera, the framing, the drawing style, the line weight and everything in the picture exactly as it is: the cutaway office with its thick walls and the door with the badge reader on the left, the black rulebook hanging on the wall, the rack of clip-on arms, the filing cabinet with its open drawer, the worker robot at its desk with its papers, the window and the gauge, the egg-shaped reviewer robot in its glass room with the post slot and the letter with slack strings, the security post with its peaked cap and red paddle, the striped barrier with its padlock, and the low shelf behind the barrier. Change only this: the black book with the red wax seal that lies on the low shelf behind the barrier is gone completely, with its seal. In its place, on that shelf, lies a neat stack of three plain white folders drawn in outline, left white inside, with no seal, no stamp and no colour. Everything else stays exactly as it is, to the pixel where possible. Black and white only, pure white background, no grey; the only colour is the red of the security post's paddle. No text anywhere. Landscape 16:9.
```

- **Made:** the first sample lay on image 1 to the pixel. Only the box
  from (525, 615) to (765, 781) px, where the book lay, was taken in, down
  to just above the shelf's front edge, and the edit's light grey was set
  to white; the shelf, the barrier, the post and the rest keep their
  pixels. The only red left is the paddle's.
- **On the slide:** the label synthetic data stands over the folders. The
  two samples of the filing cabinet were not kept: beside the large one,
  whose label is auto memory, a second cabinet would have asked which is
  which.

### 50 · `beat-00-title-2.gif` — 0.3, the way in

No generation. `uv run python tools/door_zoom.py` turned two drawings into
the GIF. 0.2 shows the house at night of image 6 still; the click that
brings 0.3 starts the GIF, in which the camera closes in on a point in the
black of the front door, above its knob, fifty frames of 40 ms up to twenty
times closer, along a smoothstep, so it sets off gently and slows as the
door fills the frame; after 120 ms of dark the cellar of image 7 fades in
over fifteen frames of 40 ms. Each frame of the house is drawn again from
the drawing at twice the GIF's size, its grey pixels set to black or white
and the coloured ones, the lit window, kept, then halved, so the ink stays
sharp at every scale. The last frame is the cellar as 1.1 shows it and
stays for ten minutes, and the GIF carries no loop block, so it plays once:
62 frames of 2752 × 1536 px (Pillow merges the dark ones), 2.7 seconds
before the last, 5.2 MB. The
narration of 0.3, "And down... into the cellar of the house.", runs over
it. The paper does not show it.

A first version, the same day, sat on 0.2 and started as the house
appeared, held it a second and dived at 70 ms a frame, faster as it went;
blown up thirty times, the raster drawing went soft. The author asked for
the click, a sharper picture and a smoother dive. On 2026-10-29 the camera
took the window instead (50a).

## Changed on 2026-10-29: the lamp in the window

The author asked that the way in go through the window, that the window
show a lamp in place of the candle, and that the bulb of 1.1 glow yellow
too. No generation: two scripts recoloured the drawings and drew the bulb,
and the zoom was made again. `storyline.md`, "The lamp in the window", has
the decisions.

### 5d · `beat-00-title-1.jpg` — 0.2, a lamp in the window

The basement window's candle gave way to a bare bulb, the basement's bulb
of 7b.1 drawn small, as at the lit windows of image 37. Inside the window's
inner frame (1465 to 1543 by 1283 to 1405 px), taken row by row between the
frame's inner edges because the candle stood on the sill and touched it,
every pixel turned lamp yellow, `#FCD64A`, which took the candle away. The
window's amber lines and the eight rays around it turned black, their soft
edges grey, measured by how far each pixel's blue stood from white. A cord
of 5 px hangs from the apex, at x 1504, to a black socket of 20 by 15 px and
a round white glass of 28 px in a black line, drawn at four times the size
and halved. Everything else keeps its pixels. The picture has no amber now;
the candle keeps it for 1.3 (in 8.2 it is out).

### 6b · `beat-01-alone-1.jpg` — 1.1, the bulb lit

The glass of the bulb over the bench (1345 to 1407 by 297 to 372 px),
flooded from a point below the filament, and the small patches the
filament encloses turned lamp yellow, as 8.2's bulb is: each pixel keeps
its darkness over yellow, so the filament and the glass's outline stay
black. The socket stays white, the rays black. The paper's Introduction
shows the same picture, so its bulb glows there too.

### 50a · `beat-00-title-2.gif` — 0.3, through the window

`uv run python tools/window_zoom.py` makes the GIF. The camera makes for a
point in the lit window below its bulb (1504, 1380 px) and closes in to
forty-six times, along the same smoothstep; the point drifts from its place
low in the picture to the middle of the frame along the same curve, so the
window comes to the middle as it grows, the bulb leaves the frame at the
top, and the window's yellow fills it. Early on the drift would push the
cut-out past the picture's edge, so it is held inside. Each frame is drawn
again at twice the GIF's size, softened by 0.6 of a drawing pixel so the
lines lose their steps, and every pixel becomes black, white or the lamp's
yellow before the frame is halved. The zoom's last frames lie wholly in the
yellow and hold it for 0.4 seconds; the cellar of image 7, its bulb now
yellow (6b), fades in out of that light over eight frames of 60 ms
(fifteen of 40 ms on the first build that day; each is a whole drawing, a
quarter of a megabyte, and the deck had reached 20 MB). The last frame is
the cellar as 1.1 shows it and stays for ten minutes, and the GIF carries no
loop block: 59 frames of 2752 × 1536 px, 2.82 seconds before the last,
5.1 MB. The narration of 0.3 runs over it as before. In the talk's deck the
slide moves on to 1.1 by itself half a second after the last frame
(`advance: after_gif` in `deck.yaml`): the cut shows nothing, so a click
spent on it seemed lost, and the author needed two to reach 1.2.

## What earlier runs taught

The comic run of 2026-10-06 made all 25 images of the old sheet in 33
generations for about 2.70 US dollars. The studies of 2026-10-07 tried the
new look (`studies/README.md`), and the run of the same day made this
sheet's 24 images in 46 generations, 11 for the plates and 35 for the
scenes, for about 3.70 US dollars; they replaced the comic images in
`beats/`. A reading of the picture slides without the script that evening
led to new versions of nine images: seven changed through the model, in 11
requests for 12 images and about one US dollar, and three moved on their
white ground. The prompts
above carry what all of it showed:

- **Positions follow the plates.** The model put the steel door to the share
  on the left, and the storyline followed; the prompts name "on the left".
- **The catalogue faces us** only when the prompt says the man holds it
  towards the viewer; otherwise its pages face him (1.2).
- **The gauge** sits directly to the right of the window, in the middle of
  the frame, so the fix image keeps it (6.1, 6.2).
- **Edits hold three to six local changes.** One with seven changes, and one
  with five that also asked to move figures, returned no image; an edit that
  only asks to move figures returns the picture unchanged. So 8.2 is made in
  two steps, and a layout is fixed by drawing afresh, not by an edit.
- **No lettering** appeared at full size on the risky spots in any run,
  and no worker grew legs. The reviewer grew arms four times, every time at
  a desk (5.3, 6.1, 7a.1, 7a.2), once with a magnifying glass as well; an edit
  that asks for "smooth, unbroken sides with nothing attached, exactly as
  the reviewer robot on the cast sheet" takes them off. The checks stay,
  because one image is enough to spoil a slide.
- **Stage props run ahead.** In 3.1 and 4.1 the model hung the fourth
  stage's keys from the man's belt, taken from the cast sheet, and the edit
  for 3.2 lost his censer. An edit that says where the keys hang instead
  and what hangs on his belt puts it right; check his stage in every
  picture with the man.
- **Defaults beat the prompt.** The gauge came out high in 8.1 although
  the prompt says low, and in 7b.1 the short form's paddle "holding up"
  won over the scene's "lowered and idle". An edit with that one change
  fixed each.
- **A chart needs its order spelled out.** "Each box holding only a small
  robot or person silhouette" let the model put a robot on top (8.2).
- **Fix edits with one or two changes** held every time: the nine fixes
  of 2026-10-07 were each right at the first try.
- **A crowded corner can be cleared without the model.** On white, the
  whole drawing can move sideways by a few per cent, with the floor line
  redrawn at its old ends; 8.2 moved 120 px to the left so its filing
  cabinet clears the leaf.
- **A face drifts** when only a reference image carries it: in one study
  edit the hair turned to dots and the hood to a hoodie's. Every prompt with
  the man names the black cap of hair and the shoulder cape. "A short cowl
  collar" drew a hoodie's hood; "a short rounded shoulder cape, like a
  monk's cowl" drew the cape of face A4.
- **An edit that changes only the man** keeps the rest of the picture, so
  1.3 and 8.2 can share one camera.
- **"A censer with a domed, pierced lid on three chains"** reads as a
  censer; "an incense burner" read as a hanging scale.
- **Read the pictures cold.** Read without the script, three of the 22
  picture slides told the opposite of their beat (5.1, 7b.1, 7b.2) and four
  told it only in part. A check against the prompt does not catch this; a
  reader who has not seen the prompt does.
- **A stream needs a direction.** Sheets drawn between an antenna and a
  closed window read as coming in. A trail that starts at the source,
  shrinks as it goes and leaves through an open pane reads one way.
- **A colour code needs the fill.** "One black archive box" came out white
  with a black lid; "filled in solid black, like the boxes on the rack"
  held.
- **A frame borrows the nearest door.** "A door frame standing free" became
  the riveted steel door of the share; "a plain wooden door frame, without
  rivets and without a door in it" held.
- **Labels travel.** The blank label of the prop sheet's booklet turned up
  on the sealed folder in 7b.1; the folder's cover now carries "only its red
  wax seal".
- **An edit can grow what it touches.** Asked to change only the
  gatekeeper's arms, one edit drew it twice as large in the foreground;
  naming where it stands and how small it is kept it in place.
- **An edit can drop what it was not asked to change.** A new view through
  8.2's window cost the window its glazing bars; a second edit with the
  earlier image as a reference put them back.
- **Moving a drawing needs a free edge.** The corner can be cleared by
  moving the drawing only where nothing touches the right edge (5.3, 7.1,
  7.2); in 1.2 the stairs do, so the envelope was made smaller instead. Two
  images that share a camera move by the same amount, and a back floor line
  that ends at a wall is not run on.
- **Strings read as three thin lines** from a letter's foot to a gripper's
  wrist (7a.1); one sample ran them between the keys and a wheel instead, so
  the prompt names both ends. Slack, they lie as thin cords on a desk and the
  floor (7a.2).
- **A hook needs something to hang from.** "A hook at the foot of the stairs"
  came out attached to the stairs once and hung in mid-air once.
- **An edit that moves a figure redraws the scene.** Asked to bring the
  worker to the glass room, the edit drew a larger room with a door, a chair
  and the worker at the door, in a new camera (7a.2). It read better than the
  old framing, so it stayed; check the framing after such an edit, and
  expect the pain and fix images to differ.
- **A fix can blank its neighbour.** Taking the magnifying glass from the
  reviewer's hand also took the scribble from the letter beside it (7a.2); a
  second edit with the earlier picture as a reference put it back.
- **The cost of beat 7a** was eight generations on 2026-10-08 (two samples of
  image 26, one fix, two samples of image 27, two fixes, the second in two
  samples), about 0.65 US dollars at 0.08 each.
- **A reference lends more than it is asked for.** Image 28, passed as the
  reference for an emblem, brought its black boxes back onto the shelves of
  29 (edit 29a); the cast sheet gave the emblem and left the scene alone
  (29b). Take a fix's reference from the plates when they carry what is
  needed.
- **On a shelf, black sheets become boxes.** Sheets "filled in solid black,
  exactly like the archive boxes" stayed sheets in flight but stood on the
  warehouse's shelves as the prop sheet's archive boxes (28). It says the
  same, so the scene now asks for boxes.
- **An edit can redraw an emblem it was not asked to touch.** The edit for
  29, which changed the man's stage, turned the gear on his cape into a
  flower; its prompt now names the gear.
- **The cost of beat 7c** was six generations on 2026-10-08 (two samples each
  of images 28 and 29, and two fixes of one sample each), about 0.48 US
  dollars at 0.08 each.
- **One reference is a canvas.** Given the cast plate as its only image, the
  edit route edited the plate instead of drawing a new scene, twice (image
  30). Cut-outs of one character each made the new scene at the first try.
- **A wave needs no video.** Five seconds from Kling 3.0 Pro made a GIF of
  2.8 MB; eight frames turned from one drawing make 548 KB, in the line of
  every other picture (image 30).
- **A pose edit redraws the whole picture a little**, the man's stubble
  included. Taking only the parts that move keeps every other line still
  from frame to frame (image 30).
- **In-betweens come from turning, not from redrawing.** Drawn poses moved
  some parts hardly at all and others a long way, so four frames flickered.
  Turned about its joint in small even steps, each part waves, and its
  lines stay the drawing's own (image 30).
- **Seven colours keep a GIF clean.** Mapped onto white, three greys, black
  and the paddle's red, every frame keeps an exactly white ground and
  takes about 70 KB written whole (image 30).
- **A study figure carries a costume into a scene.** A cut-out of one
  figure as image 2, with "Use image 2 only for the man's clothes", changed
  the clothes in all 13 scenes at the first try, and kept the pose, the
  face and what he held (2026-10-12).
- **An edit lines up to the pixel,** so the changed part alone can go back
  onto the original. Measure the shift first; one of 15 was off by a pixel.
- **A box must take in the whole figure.** 7.2's first box stopped at the
  cape's edge and left the old robe's rope belt and hood showing beside the
  new jeans; a wider box put it right.
- **Count the hands.** "With a mug in his hand" gave 7a.2 a third hand
  hanging at his side. Say where both hands are, and count them before the
  box goes back.
- **A hung robe with a peaked hood reads as a figure.** On a hanger, its
  cape and gear at the top, it reads as clothes.
- **The cost of the goodbye** was seven pictures and three videos on
  2026-10-09, about 1.65 US dollars; the first flip-book's three pictures
  cost about 0.24 of it, and the eight-frame wave needed no new picture.
- **An edit does not shorten furniture.** Three edits asked for 2.2's bench
  to end where 2.1 has it, and all six samples drew it as long as before
  (31a to 31c). On white, a slice taken out by hand did it.
- **A limb the model drew wrongly, it draws again.** Three edits asked for a
  normal forearm in 3.2, one of them on a close-up enlarged nearly three
  times, and all six samples returned the same thin loop (13b to 13d).
  Taking one line out by hand fixed it.
- **Name what is wrong, and where.** 16b asked for the paddle "lowered at
  its side on a long thin handle" and got the red ball again; 16c said that
  it lies on the base plate like a ball and where the hand holds the
  handle, and held.
- **A retouch can cut what it crosses.** Taking a string's curled tail off
  in 7a.1 also took a piece of the gripper's jaw it lay on. Check a retouch
  at full size, as you check an edit.
- **The cost of the review** was 34 pictures on 2026-10-19, about 2.72 US
  dollars; the flights needed none.
- **A costume step goes onto one figure first.** Edited alone on white
  (34), each look then went into every scene of its stage at the first
  try, as image 2.
- **Say which hand, which side and where the thumb is.** "His left hand
  seen from the back … the thumb on the lower side of the hand" turned a
  right hand into a left one in one sample of two (21c).
- **Earlier moments come from the last picture.** Edits that take a busy
  scene back in time keep its camera, and pasting back what must not move,
  the man and the reviewer, keeps the stages of a build-up still where they
  should be (35).
- **Heights drift upwards.** Asked for stacks "about as high as the worker
  robot's chin", one sample drew the right stack up to its head (35b). Name
  a landmark the stack must stay below.
- **Eyes are cheaper by script.** Proportions measured on one picture and
  drawn into the others give one look everywhere, at no cost and without
  redrawing a face (36).
- **A refusal right after a top-up can pass.** Minutes after the author
  topped up the account, one edit of a batch of two was refused for credit
  and the other ran; the same edit ran on its own an hour later (35d).
  Check the account once, then submit the refused edit again on its own.
- **An edit draws its own eyes.** Both samples of 35d gave the worker
  slanted lids, although the prompt asked for the standard eyes; the script
  of image 36 draws them again, ring included, where a lid crosses the eye.
- **A stack can be lowered by hand.** Cut between two sheet edges, a stack
  closes without a seam, and a picture with the same camera gives the wall
  behind it. It stood in for 35d for an hour.
- **The cost of the built deck's changes** was 36 pictures on 2026-10-19,
  about 2.88 US dollars; the eyes and the cards needed none.
