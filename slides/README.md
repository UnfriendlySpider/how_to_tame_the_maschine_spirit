# Slides — the talk

The companion talk for PHUSE EU Connect 2026 lives here. This file is the
story outline; `storyline.md` works it out slide by slide for the 20-minute
slot: scenes, notes and timing, and the reference part that follows
the talk. `image-prompts.md` has the ready prompt for every picture.
`tools/build_slides.py` turns the storyline into a PowerPoint deck, with a
placeholder for every image that is not made yet (see
[Building the deck](#building-the-deck)).

**Division of labour:** the paper (`../paper/`) explains each mechanism step by
step and is a reference with a light touch. The talk carries the story. Steve,
the company arc and the scenes below belong **only** to the talk; the paper
never tells them and never names Steve. It borrows eight pairs and two single drawings of the pictures
(see [Images](#images)), with captions that name roles.

## Premise

Steve is a programmer with more ideas than hands. He works alone
in the basement, and every idea he has costs him an evening. Then he takes on
his first virtual worker, and it is brilliant and useless in equal measure:
fast, tireless, and with no idea how things are done here. Over the talk Steve
learns what every founder learns: that bringing in help is not the hard part.
The hard part is onboarding, procedures, access rights, the right person for
the right job, meeting discipline, a memory that outlasts the day, a post room
for whatever arrives from outside, and an office of its own. Each of those
lessons is one Claude Code mechanism; the post room reuses the reviewer. By the
end Steve is running a small company of virtual workers, and the audience has
seen that a well set-up agent system is organised like a well set-up
company.

## The character

Steve is competent and out of hours in the day. He is not naive about AI and
not a hype believer: he adopts each mechanism only after the previous stage
bites him, and he would rather have written the code himself. That reluctance
is what makes each tool land. The audience feels the pain before they see the
fix, and they recognise the company he ends up building, because they work in
one.

## Beat sheet — one beat, one mechanism

| # | Beat | Steve's problem | Company analogue | Mechanism (Claude Code) |
|---|------|-----------------|------------------|-------------------------|
| 1 | Alone in the basement | ideas pile up, hands do not, and after work he is tired; then word gets round that the Worker Company rents out virtual workers, and its catalogue lets him choose their attributes | the founder before the first hire | — (the hook / setup) |
| 2 | The first hire | it delivers, but in its own style and ignores the house standards; every morning the Worker Company sends a fresh worker that has not seen yesterday's conversation | the onboarding document, read every day and usually followed, but not binding | **CLAUDE.md** |
| 3 | The same briefing every morning | he re-explains the review procedure from scratch, session after session | the procedure binder: written once, taken down by name | **Skills** |
| 4 | Someone wanders into the server room | a worker tidies a page out of the Book of Secrets, which must never change, although the rules forbid it; noticed too late | locks and access rights, not a sign on the door | **Hooks & permissions** |
| 5 | Hiring for attributes | the same worker checks its own work and agrees with itself | a specialist who may look but not touch: a second pair of eyes | **Subagents** |
| 6 | Everyone in one meeting room | cost and attention run out; nobody can think | meeting discipline: one topic at a time, minutes instead of the whole transcript | **Context & token management** |
| 7 | Overnight the team forgets | a decision made in a cleared conversation is lost, and he re-briefs the worker every Monday | the decision log (the staff handbook is `CLAUDE.md`, beat 2) | **Memory** |
| 7a | The post room | the worker reads a supplier's note, and a last line written for machines pulls it towards his keys: a prompt injection | the post room: letters go to the reviewer, who may read but not touch, only a strip comes out, and security stands between the worker and the keys | **Safety**: the seven against one threat. The reviewer as a reader without hands, security at the keys, and the three things a leak needs: private data, outside text, a way out. No mechanism of its own, so no leaf in the tracker |
| 7b | The separate office | "just this once", a worker runs a program against the real data: the hook never sees what a program reads, whatever the worker reads leaves the laptop for the model, and his keys are within reach | separate premises, a contractor's badge that opens one repository and expires, practice material only | **Isolation** (a VM, a container or a cloud session; own user, scoped token, synthetic data) |
| 7c | Where the sheets go | what the worker read that night sits in the model maker's warehouse, kept five years on a personal plan that allows training, and the maker sets the terms and the prices | a contract that says what the warehouse may keep, and procedures another contractor could follow | **Data protection**: the seven applied to personal data and one vendor. A company plan under commercial terms, practice data only, rules in `AGENTS.md`. No mechanism of its own, so no leaf in the tracker |
| 8 | Steve runs a company, not a keyboard | — | the organisation chart | Bringing it together / conclusion |
| 10 | Who does the checking? (after the closing slide, for a question) | he wants to hand his sign-off to the worker for good | the rule from outside: the regulator who wants a person to oversee | None: the AI Act's human oversight (Article 14), and why in the loop may be a stage on the way. Not timed, and not in the paper |

The thread through the beats is the company comparison. Each mechanism is
introduced as the thing a growing company would put in place at that point,
so nobody in the room needs to know Claude Code to follow the argument, and
the ones who do find the same files from the paper in the reference part at
the end of the deck.

## Slide mechanics

The deck has two parts (decided on 2026-10-07).

- **The story, in pictures.** Every story slide is its image, edge to edge,
  with no title, panel or card on it; everything else is spoken, from the
  speaker notes. Nobody in the room has to read while listening. The one
  exception, since 2026-10-15 (the author's request): the robots' names
  float above them, as in a game, with the Claude Code term underneath,
  where each first stands in the room, in 8.1 and in the goodbye, and objects get a
  label where they first matter (see *The names* below).
  Since 2026-10-19 each robot also joins the team with a card, on a copy of
  the picture under a white veil (see *The cards* below).
- **The goodbye.** The story ends on one more picture slide, 8.3: the cast
  waves goodbye in a GIF of eight frames turned from one drawing (the
  author's request, 2026-10-09). Since 2026-10-28 it comes before the
  closing slide, so the QR codes stay up for the whole of the questions (the
  author's request); it followed the questions as 9.2 before, and now takes
  ten seconds of the 20 minutes. PowerPoint for Windows and Mac plays a GIF in the
  show, PowerPoint for the web does not
  ([Microsoft](https://support.microsoft.com/en-us/office/add-an-animated-gif-to-a-slide-3a04f755-25a9-42c4-8cc1-1da4148aef01)).
  LibreOffice 24.2 plays one too, but not inside a group: in a test on
  2026-10-09 the GIF stood still while it was grouped with its AI label, as
  every other picture is, and looped once it stood on its own. So the build
  keeps the GIF out of the label's group. Play 8.3 once in the show before
  the talk.
- **Motion where data moves.** Since the evening of 2026-10-19 three story
  pictures move, each where the worker's reading leaves the house: the
  stream from the antenna in 7b.1, the Book of Secrets into the warehouse in
  7c.1 (black sheets until 2026-10-28) and the white folders in 7c.2 (`storyline.md`, visual rule 8). Like
  the goodbye they are GIFs of eight frames turned from the drawings, and
  the paper keeps still pictures. Since 2026-10-28 the camera moves once as
  well, at the author's request: in 0.3, on the speaker's click, it goes
  in through the house's lit basement window (the front door until
  2026-10-29), and the cellar of 1.1 fades in out of the lamp's light, a
  GIF that plays once and stays on the cellar (`tools/window_zoom.py`). The deck's own motion stays quiet: a fix
  slide that shares its pain's camera fades in (3.2, 7.2, 7c.2), so
  the room sees what the mechanism changes, and 6.2 shows each state of
  its fix on a slide of its own (since 2026-10-22); each card fades in; and 6.1
  builds up (since late on 2026-10-19): three earlier pictures of the same
  meeting come first, while the stacks grow over the worker's head and its
  bar rises. Since 2026-10-27 each is a slide of its own, with its number,
  and waits for the click, so the speaker sets the pace (the author's
  request; until then each stood about a second and moved on by itself).
  `motion: false` in `deck.yaml` switches the fades and the cards' fade
  off, while the build-up's slides and the GIFs stay. LibreOffice reads
  the fades; play the GIFs (0.3's way in among them, which must stop on the
  cellar) and the fades once in PowerPoint's own slide show before the talk.
- **The reference part, to read afterwards.** After the closing slide and
  beat 10, one slide per mechanism, and one each for safety and data
  protection, without
  pictures: the paper's own sentences on what
  it is, when you need it and the case to watch, beside the literal files
  and commands, the concrete `CLAUDE.md`, the `settings.json` hook, the
  `SKILL.md`, quoted from the repository at build time. The closing slide
  points to it. It is the part people download and keep.
- **Beat 10, an answer for a question.** A short story of two pictures,
  10.1 and 10.2, with the EU's card between them, answers the question who
  does the checking: Steve may automate the work, never his sign-off,
  because the EU wants a human who oversees, and for high-risk AI that is
  the law; but nobody checks a calculator's steps, so in the loop may be a
  stage on the way, and the EU scratches its head too. It stands right
  after the closing slide, so one click from the questions brings it, and
  is a beat of its own (since 2026-10-28, the author's request; on
  2026-10-27 it waited hidden at the very end of the deck as the secret
  level, 9s.1 and 9s.2). The build writes the question and the click into
  the notes of 9.1, and the number back to the questions into the notes of
  10.2: type it and press Enter. The narrated deck, which ends on the
  closing slide, and the timing leave it out, and the paper does not
  mention it.

The metaphor does the narrative work and the reference part stays literal,
so nobody has to decode the story to get the tool.

## Images

The story is told in images: minimalist black-and-white line drawings on
white, with a light touch of the tech priest who tends the machine spirit,
made with Nano Banana 2.1 through fal since Reve closed its image generation
in September 2026. They go into `slides/beats/`, one per slide, named after the beat, the
mechanism and the slide within the beat, so the order is obvious without
opening them. Four reference plates, for the cast, Steve's six stages, the
props and the basement, sit outside the numbering. `image-prompts.md` has the prompt for
every image, numbered in production order, with its settings, references and
checks; `storyline.md` has the scenes they come from.

```
slides/beats/ref-cast.jpg                   reference plate: the characters
slides/beats/ref-props.jpg                  reference plate: the props
slides/beats/ref-basement.jpg               reference plate: the basement set
slides/beats/ref-steve.jpg                  reference plate: Steve's six stages (2026-10-12)
slides/studies/bw-20-steve-hitched-and-open.jpg   Steve's two later looks (2026-10-19)
slides/beats/beat-00-title-1.jpg            0.2, the house at night, a lamp in its window (2026-10-29)
slides/beats/beat-00-title-2.gif            0.3, the way in through the window, plays once (2026-10-29)
slides/beats/beat-01-alone-1.jpg … -3.jpg
slides/beats/beat-02-claude-md-1.jpg … -3.jpg
slides/beats/beat-03-skills-1.jpg, -2.jpg
slides/beats/beat-04-hooks-1.jpg … -3.jpg
slides/beats/beat-05-subagents-1.jpg … -3.jpg
slides/beats/beat-06-context-1.jpg, -2.jpg
slides/beats/beat-06-context-1a.jpg … -1c.jpg   6.1's build-up (2026-10-19)
slides/beats/beat-06-context-2a.jpg         6.2's /compact and auto-compact, the stacks in a cupboard (2026-10-22)
slides/beats/beat-07-memory-1.jpg, -2.jpg
slides/beats/beat-07a-safety-1.jpg, -2.jpg
slides/beats/beat-07b-isolation-1.jpg, -3.jpg
slides/beats/beat-07b-isolation-1.gif       7b.1 in motion; the paper keeps the .jpg (2026-10-19)
slides/beats/beat-07c-data-1.jpg, -2.jpg    each one frame of its flight, for the paper
slides/beats/beat-07c-data-1.gif, -2.gif    7c.1 and 7c.2 in motion (2026-10-19)
slides/beats/beat-08-team-1.jpg, -2.jpg
slides/beats/beat-08-team-3.gif             the goodbye that ends the story, animated
slides/beats/beat-10-oversight-1.jpg, -2.jpg    beat 10, who does the checking (2026-10-27)
slides/beats/card-worker.png … card-security.png   the cards' portraits (2026-10-19)
slides/beats/card-letter.png                the threat's portrait, the planted letter (2026-10-20)
slides/beats/card-eu.png                    the EU's portrait, for beat 10 (2026-10-27)
```

That makes 32 generated images, three of them 6.1's build-up, one 6.2's /compact and two beat 10, the title picture taken from the studies,
four plates, the card portraits and five animations, the house's way in among them (0.3, since 2026-10-28). The animation of 8.3 is a loop of eight
frames: `tools/goodbye_wave.py` turns the waving parts of one drawing about
their joints in small steps and saves every frame whole, as a GIF of
2752 × 1536 px in 571 KB (`image-prompts.md`, image 30). Run it again with
`--ms` for another pace, then rebuild the deck. Its name ends in `-3` because
it belongs to slide 8.3 (`beat-09-close-2.gif` until 2026-10-28, when it was
9.2); the closing slide, 9.1, has no picture. Slide
7b.2, a crop of `beat-07b-isolation-1.jpg` with two highlight rings, was
dropped on 2026-10-15, with the sandbox.

The way into the story, 0.3, plays once, from the click that brings it:
`tools/window_zoom.py` dives from the house of `beat-00-title-1.jpg`, which
0.2 shows still, into its lit basement window and fades the cellar of 1.1 in
out of the lamp's light, 59 frames of 2752 × 1536 px (the dive at 25 a
second, then a 0.4-second hold and a fade of 60 ms a frame) in
`beat-00-title-2.gif`, each frame of the house drawn sharp from the drawing,
and its last frame stays, so the cut to 1.1 changes nothing on the screen;
the deck moves on to 1.1 by itself half a second after that frame, so the
next click brings 1.2 (`advance: after_gif`, since 2026-10-29;
`image-prompts.md`, images 50 and 50a).

The three flights are loops of eight frames as well, made by
`tools/flying_sheets.py` (`image-prompts.md`, image 33). For each scene,
`studies/` keeps a plate, the picture with its flying sheets taken off, and
a sprite, one sheet cut out; the tool sets the sprite back along a smooth
path through the places where the drawing had its sheets, so they leave the
antenna or the window and land in the warehouse. For 7c.1 and 7c.2 it also
saves one frame as the JPEG, the still the paper shows, with a sheet just
leaving its window. Run it again with `--ms` for another pace, or with a
slide id for one of them, then rebuild the deck and, for 7c, the paper.

The reference part shows the real file from `CLAUDE.md` or `.claude/`, the
setup this paper and talk are made with (since 2026-10-27, when the
playground left the repository), or the literal command or rule the paper
describes, so talk and paper never drift.

The paper shows sixteen of these images as eight pairs, one after the text
of every chapter from 2 to 10 but 4, whose Excalidraw diagram carries the
cast instead (since 2026-10-26); chapters 2, 6 and 7 joined on 2026-10-08,
and chapter 10 that evening with beat 7c. The Conclusion's pair (1.3 and
8.2) left the paper on 2026-10-27, at the author's suggestion; since that
evening the goodbye's still, `studies/anim-04-goodbye-out-own-clothes.png`,
closes the Conclusion, small, and 1.1's first picture opens the
Introduction. Each carries the same AI icon as on the slides, in
its top right corner, which `tools/template.typ` adds:

| Paper chapter | Pair |
|---|---|
| 2 Ground rules | `beat-02-claude-md-1.jpg`, `beat-02-claude-md-2.jpg` |
| 3 Skills | `beat-03-skills-1.jpg`, `beat-03-skills-2.jpg` |
| 5 Delegation | `beat-05-subagents-1.jpg`, `beat-05-subagents-3.jpg` |
| 6 Context | `beat-06-context-1.jpg`, `beat-06-context-2.jpg` |
| 7 Memory | `beat-07-memory-1.jpg`, `beat-07-memory-2.jpg` |
| 8 Isolation | `beat-07b-isolation-1.jpg`, `beat-07b-isolation-3.jpg` |
| 9 Safety | `beat-07a-safety-1.jpg`, `beat-07a-safety-2.jpg` |
| 10 Data protection | `beat-07c-data-1.jpg`, `beat-07c-data-2.jpg` |

A new version of one of them changes the paper too, so rebuild and check
both. Make the reference plates first, then the two images that carry
the most weight. No text inside the pictures: the build adds the AI label
and the names, and neither is ever drawn in (see *The AI label* and *The names* below). Landscape 16:9, black lines on white,
at least 2400 px wide; every story slide shows its image whole. Before an
image is saved, every pixel brighter than 245 in all three channels is set
to pure white, so the picture meets the white slide without an edge. The
model delivers PNG; the repository keeps JPEG (quality 90, full colour
resolution). The deck embeds each still at what its frame needs at 1920 px
across the slide, a projector's width, and keeps a zoomed crop sharper; the
sources stay whole for the paper (since 2026-10-29, when the deck had
reached 20 MB; `DECK_PX` in `tools/build_slides.py`). `--full` builds a
second deck, `out/PRE_ML19-full.pptx`, with every still embedded whole, for
print or a screen larger than a projector (since 2026-10-29, the author's
request).

The look was chosen on 2026-10-07: black-and-white drawings, a little more
than stick figures, Steve with the author's face (A4 of the studies) and an
arc in which his look changes from praying to control, the worker with a
clip-on arm for its skill. Since 2026-10-12 the arc starts and ends in
Steve's own clothes, jeans and a shirt: he puts the robe on to switch the
first worker on and sheds it piece by piece (`storyline.md`, STEVE'S ARC;
`image-prompts.md`, "Added for the costume arc"). `storyline.md` describes it and
`studies/README.md` records how it was found, and `image-prompts.md` was
rewritten from the storyline for it the same day. The plates and the 21
slide images were made from that sheet on 2026-10-07 and replaced the comic
test run of 2026-10-06, whose prompts the working repository's history
keeps; the note under each image in `image-prompts.md` says how it was made
and what was fixed. The two images of beat 7a (the post room) were added to
the sheet later the same day, and the two of beat 7c (where the sheets go)
on 2026-10-08. After the author's first run-through, on 2026-10-15, two edits
followed: 7b.1 lost the glass dome, and 7a.2 gained security at the foot of
the stairs, where the easel stood (`image-prompts.md`, "Changed after the
run-through"). After a review of the deck on the evening of 2026-10-19,
thirteen pictures were corrected, by an edit with only the changed part
pasted back, or by hand where the model could not do it
(`image-prompts.md`, "Changed after the review"). After the fifth
run-through, on 2026-10-22, the two pictures of the post room took three
edits: the letter's author at the basement window, gleeful in 7a.1 and
sulking in 7a.2, and security in 7a.2 facing the worker
(`image-prompts.md`, "Changed after the fifth run-through").

- `slides/beats/beat-04-hooks-3.jpg`, the hook flow: on the left a small robot
  at a workbench reaches with a feather duster for the Book of Secrets, the
  black book with a red seal on its shelf; security, a post bolted at a
  checkpoint between them, holds a blank red paddle up against the duster,
  and behind him a second, lower barrier with a padlock stands before the
  book.
- `slides/beats/beat-08-team-1.jpg`, the control surface: a cutaway of a small
  office seen slightly from above, a robot at the centre surrounded by six
  separate objects: a rulebook on the wall, a rack of clip-on arms (the
  skills), a gate with a guard before a stack of white folders, synthetic data, a second smaller robot at its own
  desk, a window with a gauge, a new filing cabinet. The room itself is the
  seventh: thick walls and one door with a badge reader.

## Building the deck

```sh
uv run python tools/build_slides.py            # build out/PRE_ML19.pptx
uv run python tools/build_slides.py --list     # which images are in place, which are missing
uv run python tools/build_slides.py --final    # the same, but fail while anything is a placeholder
uv run python tools/build_slides.py --full     # out/PRE_ML19-full.pptx, the drawings at full resolution
```

The deck is built, never edited by hand: every build overwrites it, so a
change goes into one of its sources and the next build carries it.

| Source | Holds |
|---|---|
| `storyline.md` | slide ids and titles, each slide's image and scene, the notes in bullets, the reference part's slides |
| `deck.yaml` | each slide's layout and what its blocks show: the reference part's sentences and files |
| `beats/` | the images |
| `brand/` | the Evidenze logo, the Evidenze Germany earth, the PHUSE EU Connect 2026 logo and the EU's AI icon |
| `../paper/metadata.yaml` | title, author, conference and paper number for the title slide |

PHUSE files a talk's slides as `PRE_<number>` beside the paper's
`PAP_<number>`, so the deck is `out/PRE_ML19.pptx`. `--output` writes it
elsewhere.

**The narrated deck.** A second deck tells the story by itself, for passing
on (the author's request, 2026-10-21):

```sh
uv run --group narration python tools/build_slides.py --narrated   # out/PRE_ML19-narrated.pptx
```

It holds the story from the title to the closing slide, without beat 10
and the reference part. Each slide plays its stretch of the narration, embedded and hidden,
as soon as it begins, and moves on when it ends; the cards and the stages
of 6.1 have stretches of their own. A label that waits for a click in the
talk pops up when the narrator says its word instead, and one the narrator
does not name pops up as the slide begins; the steps of 6.2 have stretches of
their own, as the stages do. The goodbye, 8.3, stays six seconds, and the
show stops on the closing slide, 9.1. `narration/clips.yaml` says which stretch each slide
plays; `narration/script.md` has the text and how it was made. The build
cuts the clips from `narration/takes/` with ffmpeg, which the `narration`
group brings through uv, so only this build needs it. PowerPoint plays the
sound in the show and when it exports the deck as a video; LibreOffice may
not play it.

**Adding an image.** Generate it with its prompt in `image-prompts.md`, save
it in `beats/` as JPEG under the name the storyline gives, and rebuild. A
`.png` or `.webp` of the same name works too, and an animated `.gif` is
placed like any other image and plays in the show, outside its AI label's
group, so that LibreOffice plays it as well. The image takes its
placeholder's place and fills the slide; `focus` and `zoom` in `deck.yaml`
can crop it, and PowerPoint keeps the whole image, so a crop can be checked
there as well. A new picture needs its names placed again (`names` and
`labels`). To try drafts without touching
`beats/`, build with `--images <folder>`.

Until then a placeholder names the file and prints the scene, so the deck can
be rehearsed from the first build.

**The look.** The deck follows the author's PHUSE EU Connect 2025 deck, ML04
([PRE_ML04.pdf](https://phuse.s3.eu-central-1.amazonaws.com/Archive/2025/Connect/EU/Hamburg/PRE_ML04.pdf)
in PHUSE's archive), in the brand of Evidenze Germany, as Chrestos is now
called: white slides in Arial, each slide's title in the top left corner, and
two leaves in the bottom left corner, the larger carrying the slide number.
Lists use the leaf as their bullet. The colours are Evidenze's: navy for
titles, blue for highlights, green for the leaves (see `brand/README.md`).
The slide design follows ML04, for its minimalist layout; the images keep the
look the STYLE block in `storyline.md` sets, black lines on the same white.
The story slides stay black and white outside the pictures' own accents:
since 2026-10-09 their slide number stands in black, without the green leaf
it sat on before (the author's request).

**The AI label.** Every generated image carries the EU icon for
AI-generated content, the basic "AI" in a black circle, as the European
Commission published it on 10 June 2026 with its Code of Practice on
marking and labelling AI-generated content (the author's request,
2026-10-09; the file, its source, its terms and why the deck uses the basic
icon are in `brand/README.md`). The build puts it in the top right corner of
the picture, the place the Code gives as its example, at 5.5 % of the
picture's height: 0.4 inches on a whole slide, never under 0.3 inches, as on
the title slide's small picture until 2026-10-28. A thin white rim behind it, invisible on white, ends any
line of the drawing just short of the icon, as on 1.2, where the banister
runs into the corner. The icon is grouped with its image, so a copied
picture takes it along, and its alternative text reads "AI generated". The
animation of 8.3 carries it too, on top of the GIF but not grouped with it,
since LibreOffice plays no GIF inside a group. The
title slide, before the first drawing, sets the icon beside one line that
says what it marks, "Drawings generated with AI (Nano Banana® 2.1)"
(`ai_legend` in `deck.yaml`); the house at night, its picture until
2026-10-28, opens the story on the next slide, 0.2. The label is the author's choice: the Code is voluntary,
and the Commission's page says that using the icon does not signal
adherence to it.

**The names.** Since 2026-10-15 the robots carry their names above their
heads, as characters do in a game (the author's request after the first
run-through): the name on stage in bold and, below it in angle brackets,
what it is in Claude Code, Worker `<Claude Code>`, Reviewer `<subagent>`,
Security `<hook>`. `cast` in `deck.yaml` holds the words, and each picture
slide's `names` places them at the top of a head, as shares of the picture.
Since the fourth run-through (2026-10-21) a robot carries its name only
where it first stands in the room (1.3, 4.3, 5.3), in 8.1 and in the goodbye (8.3):
once the room knows it, the name only crowds the picture. Steve carries
none: he is the player. A slide's `labels` name an object the
same way, in a thin box, where it first matters, and 8.1 carries them all as
the legend of the seven. Since 2026-10-20 a label with `click` waits for a
click and pops up, growing from its centre, when the speaker names it (the
author's request after the third run-through): AGENTS.md, skill, auto
memory, prompt injection and VM · container · cloud (7b.1's program, from
2026-10-21, came off after the fifth run-through). The second line of the
slide's notes names the clicks; `motion: false` shows them all. A fix that
passes through several states shows each on a slide of its own, with its
own picture, bar and labels (`steps`, since 2026-10-22): after 6.1, 6.2
shows /compact, the stacks filed into a small cupboard and the bar at
half, then auto-compact over the gauge, and last the slide itself, /clear,
the cleared room with a hint left in the bar for the house rules that come
back, the gauge labelled context window again (since 2026-10-28). For a day 6.2's clicks carried these states, a bar's fills and the
pictures coming and going on one slide; PowerPoint did not play them as
built, so a state that changes a picture or a bar gets a slide, and a
click only ever brings a label or rings. The warehouse of 7c carries the
name Worker Company, the story's name for the maker (Anthropic until
2026-10-21). In beat 6 a `bar`, as a game shows energy, is the context
window, alone since 2026-10-21 (`text: false`); through 6.1's `build_up` it
rises from a quarter to three quarters, each stage of the picture with its
own `bars`, and at the last it is full and bursts (`burst: true`), as the
gauge in the picture does; 6.2 lowers it again, slide by slide. Beat 10
(since 2026-10-27) adds the EU, EU `<Art. 14>`, whose name floats
beside its ring of stars in 10.1, since the ring leaves no room above it,
and one label on a click, human oversight. Each line of a name has a white plate behind
it, invisible on white, so the drawing's lines stop just short of the
letters, as at the AI label's rim. The letters are black on white, not white
on black plates, because solid black means real data in the drawings. The
build draws all of it, so no image changes, the text is exact and the
paper's figures carry no names.

**The cards.** Since 2026-10-19 each robot is introduced once, as a game
shows a new team member (the author's request after the second run-through):
on the slide after the one where it joins the team, the picture freezes
under a white veil and the robot's card stands on it, the worker after 1.2,
security after 4.3 and the reviewer after 5.2. A card carries a black tag,
NEW TEAM MEMBER, the robot's portrait with its own AI label, the name and the
Claude Code term, and five rows of what the robot can and cannot do: the
worker's arms, brain, head, memory and weak spot, security's body, brain,
paddle, sight and weak spot, the reviewer's arms, brain, head, eye and weak
spot. Under the rows a strip of two or three values, as a game shows its
stats, holds only what the documentation states (since late on 2026-10-19):
the worker's model and context window, the reviewer's, and security's
events, its exit code and its timeout; `stats` in `cast` holds them, and
`stats_note` names the page for the card's notes. Since the evening of
2026-10-19 the reviewer's card stands beside the
worker's, its rows in the worker's order, so the room reads across: its
brain from the same company, no hands, a head of its own (`beside` in
`deck.yaml`). Since the fifth run-through (2026-10-22) the BRAIN rows say
"at the Worker Company" and "at the Worker Company too", without Claude;
the titles and the strip keep Claude Code, Opus 5.5 and Sonnet 5.5. Each
card fades in over its frozen picture. The rows follow the storyline's checked sentences. `card` on a slide
names the robot, and `cast` holds its card: the portrait file, the rows,
the intention its notes open with and the seconds it adds to the talk. The
portraits are cut from one plate of the three robots alone
(`image-prompts.md`, "Changed after the second run-through"). The card's
notes list its rows, so the speaker can introduce the robot from them.
Since 2026-10-20 the threat has a card too, as a game shows a new enemy:
after 7a.1 the planted letter comes in under the tag NEW THREAT, drawn on a
puppeteer's cross with its strings ending in empty loops
(`card-letter.png`, `image-prompts.md`, image 38). Its rows follow the
paper's chapter 9, and its strip holds what the sources state. Since
2026-10-27 beat 10 brings the EU's card, NEW RULE, after 10.1
(`card-eu.png`, image 49): its rows follow Article 14(4) of the AI Act, and
its strip holds what the law's own text says, "human oversight" 17 times,
"in the loop" never, and the dates Article 14 applies from, under Annex III
and under Annex I.

**The layouts.**

- `title`: as on ML04, the paper number ("ML 19"), the title and subtitle,
  "Glasgow – PHUSE EU Connect 2026" and "Josua Böser" with the e-mail address;
  the conference's logo in the top left corner,
  the Evidenze logo in the top right corner and the Evidenze Germany earth in
  the bottom right corner; since 2026-10-28 no drawing stands between them
  (the house opens the story on 0.2). Below the name, the AI label's icon and
  the line that explains it.
- `picture`: the story slides. The image fills the slide, with three things on
  it: the AI label in the top right corner, the names that float above the
  cast (see *The names*), and the slide number in black at
  the bottom right, on a small white plate that keeps it readable where a
  drawing runs into the corner (`picture_corner` in `deck.yaml`: `right`,
  `left`, or `false` to remove the number). The title stays the slide's title for the outline and screen
  readers, placed just above the slide, where the show never draws it.
- `close`: "Questions" and the contact on the left, the two QR codes on the
  right, the logo in the top right corner, and a line that points to the
  reference part. The codes open the repository and, since 2026-10-27,
  PHUSE's archive with the author filter already set
  (`?Author=B%C3%B6ser`, which the page reads from the address), so it
  lists the author's papers and slides beside the archive's other filters;
  the line beneath each code shows its address readable, "Böser" for the
  encoded name.
- `reference`: the reference part. The title in the top left corner, the
  paper's sentences on the left, the quoted files in a card on the right;
  seven leaves in the top right corner show which mechanism the slide
  explains (`tracker: false` in `deck.yaml` removes them); the safety and
  data-protection slides light none, because each applies the seven to one
  concern.
- `panel` and `full`, the image beside a panel or under the title with an
  inset card, carried the talk until 2026-10-07 and are kept for slides that
  need them.

**What the build checks.** Every storyline slide has one entry in
`deck.yaml`, in order. A reference slide quotes a repository file by line
range at build time, and each excerpt names text it must contain, so an edit
that moves the lines stops the build instead of putting stale code on a
slide. Every sentence it quotes from the paper names its `source`, and the
build stops when the paper no longer says it, its reference numbers aside.
`uv run python tools/check_sources.py` runs the same checks. The text is
sized to fit, and the build names the slides where a code line wraps or a
column does not fit; a lower `split` widens the right-hand card. The build
stops when the AI label's file is missing, and warns when the label would
hide part of a drawing. `ai_label` on that slide then moves it to a free
corner, or, once the slide has been looked at, keeps it where it is. Each
`names` entry must name a robot under `cast` and stay inside the picture,
and the build warns when a name or a label runs off the slide or covers the
AI label.

**What else the file carries.** Speaker notes in bullets, never prose
(the author's request, 2026-10-19): each slide's intention in one sentence,
in bold, its points, at most one line to say word for word, and the note
below a rule, "Background, not spoken" (`storyline.md`, "Telling the story",
says how to deliver them). The points say what to share, never what
happens, and name no data viewer and no example: the picture tells the
plot, and the speaker brings the examples (the author's request, that
evening). The background is short: one guard and at most one
source per slide, with the longer answers in `qa.md` (since 2026-10-12). The reference slides carry
no notes beyond their title. Their `Holds:` line in `storyline.md` says what
each one shows, and the build leaves it out. Also one PowerPoint section per
beat, and each picture's `alt` from deck.yaml, or else its scene, as the
image's alternative text. `--timing` prints the
storyline's Timing table from the seconds each slide plans, the cards
included. Fonts are Arial and Consolas,
which ship with PowerPoint; `deck.yaml` sets them, and the colours, in one place.

## Notes for later

- The slide-by-slide storyline and the timing are in `storyline.md`, the
  image prompts in `image-prompts.md`.
- Seed questions and answer sketches for the Q&A are in `qa.md`.
- Steve should visibly resist each step, then adopt it after the pain — the
  reluctance sells the mechanism.
- The author's first run-through, on 2026-10-15, moved the story towards his
  own telling: the agency, the extra arms, the full head, "again and again",
  and the robots' names floating above them (`storyline.md`, "The
  run-through").
- `narration/script.md` retells the story for a narrator voice, with
  ElevenLabs' audio tags, in parts of one request each (2026-10-20); since
  2026-10-22 in eight parts, merged from the fourth and fifth run-throughs.
- The LinkedIn teaser for the slot, made on 2026-10-20, is in
  `../promo/linkedin/` (since 2026-10-29), with its prompts and the post's
  draft; `tools/promo_teaser.py` sets its words.
- The third run-through, on 2026-10-20, lit the window of the house at work
  in 7b.3 and 7c, sent 7b.1's stream in front of the open casement,
  labelled /compact and auto-compact in 6.2, named the reviewer's model,
  Sonnet 5.5, on its card, pinned three checks on the wall of 3.1, made the
  labels pop up on a click and gave the threat a card (`storyline.md`, "The
  third run-through").
- The fifth run-through, on 2026-10-22, took Claude off the cards' BRAIN
  rows, gave each state of 6.2 a slide of its own from /compact to
  /clear, put the letter's author at the basement
  window in 7a.1 and 7a.2, turned security in 7a.2 to face the worker,
  took 7b.1's program label off and merged the narration (`storyline.md`,
  "The fifth run-through").
- The company analogue is the joke budget: one dry line per beat about how
  familiar the situation is (the welcome pack nobody reads, the meeting that
  should have been an email), never a gag that needs the slide to explain it.
- The analogy has one limit, and 8.2 says it on stage: in a company the
  employee answers for the work; here only you do. `qa.md` answer 3
  expands it.
- Evidence goes on stage sparingly, at most one figure per beat, each with
  its checked source in the slide's note (3.2, 4.3 and 6.1 so far, DORA's
  line in 8.2, the three things a leak needs in 7a.2, and in 7c the five
  years against the thirty days, one comparison from one source; the METR figure of 1.3 was cut for
  time on 2026-10-07 and stays in `qa.md` 21). Further studies, for and
  against, are in `../paper/further-reading.md`.
- Slide tooling, decided on 2026-10-06: a PowerPoint deck built with
  python-pptx (see [Building the deck](#building-the-deck)), because the
  conference laptops run PowerPoint and its presenter view shows the speaker
  notes. The Typst option is dropped. The reference part quotes the
  repository's files and the paper's sentences at build time. Since
  2026-10-08 the paper describes the mechanisms in general terms and names
  no file of the repository, so the reference part is where paper and files
  meet.
