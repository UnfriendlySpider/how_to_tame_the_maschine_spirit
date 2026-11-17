# CLAUDE.md — working rules for this repository

This repo is the source of a conference paper for **PHUSE EU Connect 2026**
(Glasgow, November 2026), titled *"How to Control the Machine Spirit without
Just Praying for Success"*. The paper explains, with Claude Code as the running
example, the control mechanisms available today — CLAUDE.md files, skills,
hooks and permissions, subagents, context and token management, and memory —
and how to use them instead of hoping for good output, plus the isolated
machine the assistant should run on, a chapter on untrusted input (prompt
injection and supply-chain attacks) and one on data protection and the
dependence on one vendor. A companion talk carries
the story; the paper is the friendly, self-contained reference, with a light
touch but no plot.

The repository holds the sources of both, and the Claude Code setup they are
made with: the rules in this file, and the skills, hooks and subagent in
`.claude/`, are the author's working tools, and the talk's reference part
quotes them. The playground of exercises left on 2026-10-27 (the author's
decision); the working repository's history keeps it. See section 6.

---

## 1. Language

The author gives input in German. **Every artefact is English** — without
exception: paper prose, headings, code comments, commit messages, file names,
the README, and example snippets. Only the live conversation with the author is
in German.

## 2. Spelling and style

- **British English** (`organise`, `behaviour`, `-ise`, `colour`, `programme`
  for a schedule but `program` for software). A PostToolUse hook flags common
  American spellings in `paper/paper.md` after every edit; treat its output as a
  proofreading hint, not a verdict.
- No marketing language, no superlatives, nothing "revolutionary" or
  "game-changing".

**Carve-out — never re-spell these:** code identifiers, file names, JSON keys,
CLI flags, and quoted material. A global `color → colour` replace breaks
configuration. Software terms keep their conventional spelling (`program`, not
`programme`).

## 3. Tone: friendly and precise

The paper is written for people who work with data or code, in any field,
and do not know Claude Code. It should read like a good colleague explaining a tool at the next
desk: warm, direct, and exact.

- Address the reader as **you**. Use **we** for what the paper does ("we walk
  through…"), never as a royal plural for the author's opinions.
- The author speaks as **I**, never as "the author" (APA 7, §4.16; the
  author's decision, 2026-10-27), and only where the author acted or speaks
  in person: the disclaimer, the Introduction and the Conclusion (the
  personal frame below), and the observations below. Advice stays in the
  imperative and speaks to *you*.
  The one exception is PHUSE's template line in the Contact Information,
  "Contact the author at:", which stays as the template has it.
- Explain every term the first time it appears (context window, hook, token,
  subagent). One plain sentence is enough.
- Short analogies are welcome when they make a mechanism click, but a single
  sentence each. Never build one out, never let one carry a section.
- Plain words over impressive ones. Everyday words first: use, need, check,
  keep, show. "Claude reads the file at the start of every session" beats
  "the file is ingested during session initialisation". Technical terms stay
  and are explained once.
- **Sentences that flow.** About 15 words on average, rarely more than 25
  (the author's direction, 2026-10-26: at 12 words the text read choppy).
  Mix short and longer sentences. Join a claim and its example, a contrast
  or a cause and its consequence in one sentence with *but*, *so*, *while*,
  *because* or a colon, rather than in two stubs that each restate their
  subject. A short sentence stays where it lands a point. A list of three or
  more goes into bullets or a table, not a colon chain. Semicolons
  sparingly. `--stats` lists the longer sentences (section 8).
- **Plain language, checked against the guides** (2026-10-09). The Plain
  English Campaign and the European Commission's *How to write clearly* ask
  for 15 to 20 words on average, GOV.UK splits sentences over 25. Never
  drop a *because*, *so* or *but* to keep a sentence short: choppy text
  hides the logic. Put what the reader knows first and the new or important
  word last (Gopen and Swan).
  One term per thing, defined where it first appears: "front matter", not
  also "header block"; "token" for text, "access token" for the key.
- **Sentences, checked against the craft books** (2026-10-27, from the
  author's research on Williams, Gopen and Swan, Sword and Pinker). Who acts
  is the subject and the action is the verb, not a noun ending in *-tion*.
  Subject and verb stand close together, so the verb comes early. "It is",
  "There are" and a bare "This" go unless they put the point last. One hedge
  per claim, and a hedge the source needs stays. Each citation stands where
  the clause it supports ends. `--stats` lists empty openers and stacked
  hedges beside the long sentences, and `/style-review <chapter>` reports a
  chapter's sentences without editing them. Both give hints, not verdicts.
- **Observations from making this paper** (the author's decision,
  2026-10-27). A chapter may carry one first-person observation of at most
  two lines, where its page has room: chapters 3, 4, 5 and 7 do. The record
  (a commit, this file) must carry every word, and a hook's or skill's
  behaviour is tried before it is described. An observation has no number
  in brackets, is never offered as evidence, and names no repository and no
  path (a mechanism's own name, such as `CLAUDE.md`, may stand). It is the
  one exception to the rule below that every claim carries a source the
  reader can open, and it does not count as the chapter's light remark.
- **Firm.** Give advice in the imperative ("Write the rule down."). Say
  *never* where never is meant. Keep *usually* and *may* only where the
  facts need them.
- **Honest, and inviting with it** (the author's direction, 2026-10-08).
  Every claim carries a source the reader can open: the documentation for
  what Claude Code does, a study, a report or an incident for everything
  else. Say where the evidence is mixed, and name a source's limits when
  they matter: a preprint, a vendor figure, a demonstration rather than an
  attack, results their authors now call out of date. A warm tone is never a
  licence to round up.
- A light, dry remark or a one- or two-sentence anecdote from everyday data
  work is welcome: the afternoon the assistant offered to tidy
  the production folder, the Monday re-briefing. At most one per chapter,
  never at the expense of a fact, and never a running gag.
- The Conclusion is the one place for a warmer, lightly playful voice (the
  author's direction, 2026-10-08). It thanks the reader, invites them to
  start small and share the work, and sends them off cheerfully. It is still
  a paper: every claim keeps its source, and the light touch never costs a
  fact.
- **A personal frame** (the author's direction, 2026-10-27). The
  Introduction and the Conclusion are the paper's personal part; the
  chapters between stay a reference. The Introduction greets the reader
  with "Moin" (glossed as the north German hello), thanks them, guesses
  that whoever downloaded it wants to learn how to program sensibly with AI
  in 2026 and says the paper is made for that, then names the dangers:
  Summer Yue's inbox in one sentence and the production databases coding
  agents deleted (chapters 2 and 4 carry those cases). The Stack Overflow
  survey and, after it, the quiet evening left the opening on 2026-10-27
  (the author found neither the right icebreaker). It then
  follows the author's line of 2026-10-27: last year's talk showed AI as a
  brilliant baby junior given one small task at a time; today the author
  would hire it as a senior; like a project manager you now organise
  seniors, and seniors need structure, which a company gives with standard
  operating procedures and an AI gets from a harness, the program around
  the model. Claude Code is such a harness: the program enforces, the model
  is only asked. It promises that the chapters look at such cases closely
  and show the seven mechanisms that set up the harness, with experiments
  on a machine of the assistant's own. The junior's source is the 2025
  talk's slides (slides 12
  and 13 show the baby robot under "How to give a junior serious tasks?
  One task at a time"); the 2025 paper says "handling trust is the most
  important thing", and its "try asking again" was a tip, not its point. The disclaimer says that
  the ideas are the author's, dictated mostly in German, that Claude Code
  drafted and revised the text under the author's direction, that the author
  read and reworked every page, and that they tried with Claude not to drop a
  slop bomb ("the ideas are mine" since 2026-10-28, the author's decision:
  PHUSE's Code of Conduct V5 of April 2026 permits AI tools but asks that
  "the ideas, and the expression of those ideas" be the author's and that
  AI use be disclosed). The Conclusion
  thanks the reader, sends them to ask a model what is possible and for its
  sources, gives the author's outlook (AI-built software pressing on
  vendors' prices; the data kraken of the 2025 talk, so decide what you
  share at all; the author's favourite way out, an open-source agent with
  an open-weight model on a server of one's own, and an invitation to help build
  such projects; DeepSeek's open V4 models, argued with a benchmark: V4
  Flash at 88.8% on SWE-bench Verified against 76.4% for last year's Claude
  Opus 4.5; the catch, hardware, since V4 Flash runs on a Mac Studio with
  256 GB (Rapid-MLX's floor is 192 GB, "comfortable" only for its 2-bit
  build, so the paper says "runs on" since 2026-10-29),
  from 10,999 euros in Germany; since 2026-10-29, at the author's
  request, a wink that a paper about Claude Code recommends OpenCode:
  Claude Code was the easier start, most of the seven are there in
  OpenCode too (its own files: chapter 10 says Claude Code's stay
  behind), Claude Code supports only one vendor's models (never "keeps
  you": it runs others unsupported), and in September 2026 OpenAI could
  not rule out that de-identified data from two mathematicians' use of
  its products helped improve its models, one of whom works for
  Anthropic, which the paper says; AI
  where it helps and not where the hype says,
  every bit of power given to it weighed against the security of your
  systems), starts the reader small, names the three mechanisms that hold
  for validation, and ends on the closed room and the prayer, with a small
  drawing of the cast waving goodbye below. An opinion is marked as the author's ("I expect", "I
  welcome", "my favourite"), and every fact in it keeps its source. **Say
  each thing once, and keep both short** (the author's direction, later on
  2026-10-27, after a first draft said things twice): the Introduction
  makes the reader want the chapters and does not brief them in advance.
- The talk's cast appears only in the figures (section 9): the programmer,
  the worker (Claude Code), security (a hook; GATEKEEPER in the image
  prompts) and the reviewer (a subagent). Captions name roles, never Steve and never the plot. The prose
  tells no story.
- Every section stays usable as a reference: a reader who jumps to one chapter
  must be able to act on it without reading the others.

**Voice sample** (the register to match):

> A hook is a small script that Claude Code runs at a fixed moment, for
> example just before it writes a file. The script sees what is about to
> happen and can say no. A rule in CLAUDE.md is advice that Claude usually
> follows. A hook is enforced by the tool itself. So anything that must never
> happen belongs in a hook, such as a write to the production dataset. Most
> teams write their first hook the afternoon the assistant offers to tidy
> that folder. The afternoon before is the better time.

## 4. Two deliverables, two registers

The paper explains each mechanism step by step and is a **reference first**.
It reads as a complete, standalone piece; the light touch from section 3 is
seasoning, not structure.

The story lives **only in the talk**: Steve, a programmer alone in
the basement with more ideas than hands, discovers that he can bring in
workers with different attributes, and every problem of his growing team is
one Claude Code mechanism. The talk's thesis is that a well set-up agent
system is organised like a well set-up company (outlined in
`slides/README.md`). The paper never tells the story and never names Steve. It
borrows two single pictures and eight pairs of the talk's pictures, with captions that
name roles (section 9). Each of the paper's mechanism chapters maps onto one beat of the talk
(the Safety chapter, 9, onto beat 7a, the post room, and Data protection, 10,
onto beat 7c, where the sheets go), so the two
reinforce each other without the paper carrying any narrative.
References to the talk are allowed but sparse.

The deck has two parts. The talk is told in pictures only, one scene per
slide, edge to edge, everything else spoken; after the cast's goodbye, an
animated GIF (2026-10-09), and the closing slide, which stays up for the
questions (the goodbye followed them until 2026-10-28), come beat 10, which
answers a question, and a reference part to read afterwards, one text slide per
mechanism (and one each
for safety and data protection) with the paper's own sentences beside the literal files and commands. The speaker
notes are bullets, never prose (the author's request, 2026-10-19, after his
second run-through: written-out text does not help on stage): per slide the
intention in one sentence, a few points with the words it must name, at most
one line to say word for word, and the background below a line. The points
say what the slide must share, never what happens in it: the picture carries
the plot, and the author brings the examples, so the story's notes name no
data viewer and no example (the author's request, that evening). The
background is short: one accuracy guard and at most one short source per
slide, never edit history, and the reference slides carry none (the author's
request, 2026-10-12). Since the author's first run-through
(2026-10-15) the robots' names float above them on the story slides, as in a
game: Worker `<Claude Code>`, Reviewer `<subagent>`, Security `<hook>`, with a
label over each object where it first matters; Steve carries none, and the
build draws them, never the image. Since the second (2026-10-19) each robot
joins the team once with a card, as a game shows a new team member: the slide
after its first entrance repeats the picture under a white veil with the
robot's portrait, name, term and five rows of what it can and cannot do;
the reviewer's card stands beside the worker's, the rows lined up (since
that evening), and under the rows a strip of two or three values the
documentation states, as a game shows its stats (since late that evening).
Since the third (2026-10-20) the threat gets a card as well, NEW THREAT
after 7a.1, the planted letter on a puppeteer's cross, and the labels over
the objects pop up on a click when the speaker names them. Since the fourth
(2026-10-21) a robot's name floats only where it first stands in the room, in 8.1 and
at the goodbye; the black book is the Book of Secrets, whatever must never
change, the agency is the Worker Company, whose name stands over the
warehouse, and the house rules carry the label AGENTS.md (the author's
requests). Since the fifth (2026-10-22) the cards' brain is "at the Worker
Company", without Claude, 6.2 shows each state on a slide of its own
(/compact: the stacks filed into a small cupboard, Steve relieved, the bar
at half; auto-compact; /clear: the cleared room, a hint left in the bar, the
gauge labelled context window again since 2026-10-28;
the clicks of one slide did not play in PowerPoint as built), a cartoon villain
watches the planted letter through the basement window (gleeful in 7a.1,
where since 2026-10-28 he holds it out on its puppeteer's cross, as its card
shows it, sulking in 7a.2, his nose kept small and straight), and security in 7a.2
faces the worker; the narration merges the fourth and fifth tellings, with
a building-site sign where the toilet was.
The pictures are
minimalist black-and-white line drawings with a light touch of the tech
priest (`slides/studies/` records how the look was chosen); the worker's
eyes carry a pupil with a small highlight, as 6.2 drew them, and Steve's
robe is hitched up from 3.1 and open from 6.1 (the author's requests, late
on 2026-10-19); a window lit at night where the work happens glows lamp
yellow with a bare bulb, in 7b.3, 7c and 8.2, and so does 8.2's bulb
(2026-10-20); since 2026-10-29 the house's basement window in 0.2 glows the
same, a lamp in place of the candle, and 1.1's bulb with it (the author's
request), so the candle's amber stays for 1.3 and 8.2. The images
are made with Nano Banana 2.1 through fal, from the prompts in
`slides/image-prompts.md` (Reve, the first choice, closed its image
generation on 2026-09-27). The goodbye before the closing slide is a GIF of
eight frames turned from one such drawing by `tools/goodbye_wave.py`, not a
video. Since the review of the evening of 2026-10-19 three story pictures
move as well, only where data moves (7b.1, 7c.1, 7c.2): loops that
`tools/flying_sheets.py` turns from the drawings, while the paper keeps
stills; since 2026-10-28 the camera moves once, in 0.3, on the speaker's
click, into the cellar of 1.1, a GIF that plays once (the author's
request: the house left the title slide that day to open the story on a
slide of its own); since 2026-10-29 it goes in through the house's lit
basement window, not its front door, and the cellar fades in out of the
lamp's light (`tools/window_zoom.py`, the author's request), and the deck
moves on to 1.1 by itself once the GIF settles, since a click spent on that
invisible cut seemed lost. The deck's own motion stays quiet, a fade where a fix shares its
pain's camera, each card fading in and the labels popping up on a click
(since 2026-10-20), and `motion: false` in `slides/deck.yaml` switches it
off. 6.1 builds up through four pictures (since late on 2026-10-19), each a
slide of its own that waits for the speaker's click since 2026-10-27 (the
author's request; they moved on by themselves before). Since 2026-10-27
the talk answers who does the checking (the author's request, after
feedback): 10.1, the EU, a ring of twelve stars with two gloves and a
gavel, named EU `<Art. 14>`, raps Steve's knuckles as he hands the worker
his stamp; its card, NEW RULE; 10.2, Steve answers with a pocket
calculator, and the EU scratches its head (a red stop button stood there
for an evening, but did not read as one). It waited hidden at the very end
for a day as the secret level (9s.1, 9s.2); since 2026-10-28 it is beat 10,
"Who does the checking?", visible right after the closing slide, so one
click from the questions brings it (the author's request). The build
writes the question and the click into 9.1's notes and the number back into
10.2's; it is not timed, and neither the paper nor the narrated deck, which
ends on the closing slide, carries it. On 2026-10-27 9.1's second QR code
became PHUSE's archive with the author filter already set
(`?Author=B%C3%B6ser`), in place of the paper's PDF. On 2026-10-28 the
goodbye moved before the closing slide, as 8.3, so the QR codes stay up for
the questions, and in 7c.1 the Book of Secrets itself flies into the
warehouse, in place of the black sheets (the author's requests). Every generated image, on
a slide and in the
paper's figures, carries the EU icon for AI-generated content, which the
builds add, never the image (the author's request, 2026-10-09;
`slides/brand/README.md` has the source and terms). The deck is a PowerPoint file that
`tools/build_slides.py` builds with python-pptx from `slides/storyline.md`
(the script) and `slides/deck.yaml` (layouts and blocks); the images go into
`slides/beats/`, the logos into `slides/brand/`, and a missing image is a
placeholder until it arrives.

## 5. Audience

PHUSE attendees, but written so that anyone who works with data or code can
follow it (the author's decision, 2026-10-12). The paper and the talk carry
**no pharma examples**: no ADSL, ADaM or SDTM, no studies, subjects, sponsors
or treatment variables, no QC or SOP as bare acronyms. Pharma readers tend to
check a pharma example against their own practice, and a detail that is off
costs the argument; a neutral example has nothing to correct. The examples
are everyday data work: production data that must not change, a spec, a
written procedure, a review, a project and its data owner, data about real
people, a duration in days ("Monday to Friday: five days, or four nights?").
Pharma stays only where it is the point and anyone can follow it: health data
under the GDPR and the EMA and FDA principles on validation in the paper, and
the PHUSE seed questions (SAS, GxP, patient data) in `slides/qa.md`, because
the room will ask them. Keep the concerns this audience brings in view —
production data that must not change, independent review, isolation,
controlled change, vendor data and packages nobody here wrote — in words any
reader knows. Until 2026-10-27 the playground, a small data viewer in Python
with a made-up table, was the one concrete instance the story's words mapped
onto; it left the repository that day (section 6). Do not assume readers
know Claude Code or any industry; do assume they can read a little Python.

## 6. The repository holds the sources and their setup

The repository holds the paper, the slides and the narrated deck, and the
Claude Code setup they are made with: the rules in this file and the hooks,
skills and subagent in `.claude/`. The talk's reference part quotes those
files, and the closing slide's QR code leads to the repository's public
copy. The playground of exercises, its data viewer and its example
configuration left on 2026-10-27 (the author's decision, to keep the
repository on the paper and the slides); the working repository's history
keeps them. The work happens in a private working repository, and its
public copy stands under the MIT License (`LICENSE`, the author's decision
of 2026-10-28); README's Licence section names the files that keep their
own terms (cmarker, Libertinus Mono, the EU icon, and the PHUSE and
Evidenze logos, which are not licensed for reuse).

The public copy is a fresh start, without the working history (the
author's decisions of 2026-11-15, after a check of the whole repository
and its history; `review/` keeps the plan). `tools/export_public.py` makes
it: the tracked files of one commit, without the review records
(`review/`), the notes for the Q&A (`slides/qa.md`), the promotion drafts
(`promo/` and `tools/promo_*.py`), the files as uploaded (`submission/`),
the PHUSE and Evidenze logos and the script itself. The public repository
changes only through that export. Never push a branch of the working
repository there, never give one clone the other's remote, and never make
the working repository public: its history holds what the public copy
leaves out.

The README greets the reader first, in the author's own voice ("Moin,
everyone", and "I" as in the paper's personal frame), lists only what the
public copy holds, and says what it leaves out in a short note at its end
(the author's request, 2026-11-15: the first copy led with what was
missing).

Rules that follow from this:

- **No repository in the paper** (the author's decisions, 2026-10-08 and
  2026-10-26). The paper describes each mechanism precisely, with general
  examples from everyday data work (section 5); it is no guide to steps in
  a repository. It names no file of the repository, carries no file card
  and walks through no exercise, and it names no repository at all, neither
  in the Introduction nor in the disclaimer, the References lead-in or the
  Contact Information: the paper knows only itself and the talk.
- **Never paste a copy of a configuration into `paper.md`, and no code in
  the paper.** The paper explains; the repository holds the files.
  Identifiers and the odd flag stay in inline code; code blocks do not
  appear in the paper. The `::: filecard` fence (section 8) still builds,
  but the paper no longer uses it.
- **Every file the slides quote must pass `uv run python tools/check_sources.py`**
  (`tools/check_examples.py` until 2026-10-27). The script feeds the hooks
  crafted tool calls, validates skill and agent frontmatter, checks that
  review skills and the read-only `reference-checker` hold no write tool
  (for the reviewer also no `memory` field and no `Agent`, since 2026-10-28),
  checks the settings file, any file-card path, the pitfalls cards and the
  reference list, and checks every file excerpt and sentence the slides
  quote. Since 2026-11-16, after a security review of the repository, it
  also refuses a skill whose `allowed-tools` pre-approve every use of a tool
  that writes, runs commands, starts a subagent or fetches a page. It
  refuses a review skill that keeps `Agent` too, and a reviewer that holds a
  web tool beside a tool that reads files, since what it reads it could send
  out.
- The same mechanisms serve the author: a hook refuses hand edits to `out/` and
  `dist/`; `/build-paper`, `/verify-claim`, `/add-reference` and
  `/style-review` are the author's skills (the last, like every review
  skill, takes the write tools away); the `reference-checker` agent audits
  the reference list it is handed, since it holds no tool that reads files.
  The committed settings pre-approve no command (since
  2026-11-16): a pre-approved build would run scripts that Claude can edit
  without a prompt in `acceptEdits` and auto mode. `/build-paper`
  pre-approves the build for the turn that invokes it, and a personal rule
  belongs in `.claude/settings.local.json`.
- Subagents may be launched without asking wherever they help: bulk reading,
  broad searches, a second check of a change, independent tasks in parallel.
  That includes the repo's own agents and the built-in ones. What a subagent
  reports is input, not a verdict: a claim about Claude Code still goes
  through `/verify-claim` before it enters the paper.

## 7. Accuracy rules (the most important section)

The costliest failure mode is a paper *about* Claude Code that asserts a feature
which does not exist.

- Verify every claim about hooks, skills, settings, permissions, subagents,
  memory, slash commands, or token behaviour against the official docs
  **before** it enters the prose. Use `/verify-claim <sentence>`; it fetches
  the relevant page at `https://code.claude.com/docs/en/…` and answers
  Confirmed / Refuted / Not documented with a quote. Never confirm from memory.
- **Never invent a reference.** Every source in `paper/references.md` must be
  retrievable and carry an access date. Add sources with `/add-reference`.
- **Cite in the prose.** A claim taken from a source carries its number,
  `[4]` or `[4, 5]`, directly in `paper.md`; the build turns the numbers into
  links to the entries, with a non-breaking space before the bracket so a
  number never starts a line. The build fails on a number without an entry
  and on an entry that is never cited, so an added source must be cited in
  the same change. Confirm the cited page supports the sentence before placing the
  number (`/verify-claim`). The numbers follow the order of first citation,
  [1] first and no gaps, so a reader meets them counting up (the author's
  request, 2026-10-26); the build fails when they do not, and
  `uv run python tools/build_paper.py --renumber` restores the order in
  `paper.md`, `references.md` and `further-reading.md`. Never renumber by
  hand.
- Date feature availability ("as of October 2026"). The field moves fast and
  the conference is in November. Note the Claude Code version the paper was
  last checked against (currently 2.1.312, 2026-10-28: the final check
  before submission read every source again against the sentences that
  cite it and checked every uncited claim against that day's
  documentation, after the full reviews of 2026-09-28 with 2.1.283,
  2026-10-08 with 2.1.294 and 2026-10-26 with 2.1.310; its findings and
  what was done about them are in `review/2026-10-28-final-check.md`). On 2026-10-08 every
  source was read again,
  studies in full text, against each sentence that cites it: eighteen
  sentences said more than their source and were corrected, and twenty
  sources whose claims other cited pages carry, or which the paper did not
  need, left the list for `paper/further-reading.md`.
- Known traps, already verified: path rules are consulted only for `Edit(...)`
  and `Read(...)`, so `Write(path)` rules are accepted but never checked; a
  PostToolUse hook cannot stop the call, it can only report or replace the
  output Claude sees; the `/agents` command no longer
  opens a wizard; `#` is not a documented memory shortcut; a skill's
  `allowed-tools` pre-approves tools and restricts none (`disallowed-tools`
  or a subagent's `tools` list does); a Bash deny rule matches the command
  as written, so `git push -f` passes `Bash(git push --force *)`; a hook exit
  code other than 2, even 1, blocks nothing by itself (since 2.1.295 a
  command or HTTP hook with `onFailure: "block"` blocks the action when it
  cannot start, times out or exits with an unexpected code; verified
  2026-10-19); output styles can be switched
  mid-session, so "only at launch" is wrong for them; since 2.1.283 a
  terminal or VS Code session starts in auto mode, where file edits inside
  the working directory are approved without a prompt and skip the
  classifier (protected paths aside), and cloud sessions pre-approve file
  edits in every mode, so "Claude asks before every edit" is wrong by
  default (verified 2026-10-06); a `claude -p` or SDK run never shows the
  trust dialog, so a repository's hooks run and its `.mcp.json` servers
  connect without asking, and workspace trust never gates a skill's
  `allowed-tools`, so "the trust dialog protects you from a cloned
  repository" is wrong for scripted runs (verified 2026-10-06); `--tools`
  limits the built-in tools only, so MCP tools stay unless
  `--disallowedTools "mcp__*"` removes them; a `Bash(curl *)` deny rule misses
  `/usr/bin/curl` and `sh -c 'curl …'`, and the sandbox's `allowedDomains` do
  not limit `WebFetch`, which has its own deny rule (verified 2026-10-07).
  Verified 2026-10-08: a cloud session's GitHub proxy refuses tags and branch
  deletions but does not limit which branch a push updates, so "it pushes
  only to its own branch" is wrong (protect `main` with a GitHub rule); an
  installed mod, a kind of plugin, decides after the hooks, and without
  managed settings or a Team or Enterprise login it can approve a call that
  a hook blocked or a deny rule refused, so "deny always wins" is wrong
  (verified again 2026-10-26: the condition is the session's login, not the
  plan, so an API-key session on a Team plan is not covered, and with that
  login a hook's block now holds too); if the sandbox cannot start, commands run without it unless
  `sandbox.failIfUnavailable` is set; a subagent without a `model` field
  takes the model Claude passes for that call, then
  `CLAUDE_CODE_SUBAGENT_MODEL`, then the main conversation's, so it does not
  simply inherit; the user's fork command is `/subtask` (since 2.1.212;
  `/fork` now copies the session); `/doctor prompt-audit` exists (2.1.283
  and later); a subdirectory `CLAUDE.md` loads when Claude reads, writes or
  edits a file there; the docs date auto mode as the starting mode to 2.1.283 and
  the changelog to 2.1.284 for every plan, so the paper names no version for
  it; the glossary's 3.5 English characters per token predate the newer
  tokenizer (about 30% more tokens from Claude 4.7 on), so the paper says "a
  few characters"; a path rule with one leading
  slash starts at the project (in project settings), two slashes start at
  the disk's root; without `strictAllowlist` (user, managed or `--settings`,
  never a repository file) an unlisted host in auto mode is the classifier's
  call, and `allowUnsandboxedCommands: false` stops the unsandboxed retry;
  `--settings '{"disableAllHooks": true}'` leaves a repository's `.mcp.json`
  servers connected, while `--bare` reads none of its hooks, skills,
  subagents, plugins or `.mcp.json`; a committed settings file reaches
  everyone who clones it, but only while Claude Code works in the folder
  that holds it (no parent fallback; since 2.1.246 `/cd` there applies it,
  and an Anthropic-hosted cloud session with several repositories loads no
  repository's hooks), and each person can switch its hooks
  off locally; no other settings file lifts a committed deny rule, but
  `--setting-sources user` skips the project's settings for a run, and
  without managed settings or a Team or Enterprise login a mod can approve
  past it (corrected 2026-10-26); a memory note records its write time only if it has front
  matter. Verified on 2026-10-08 in the source audit: a subagent with a
  `memory` field gets `Read`, `Write` and `Edit` back, so a read-only
  reviewer must not have one; Bash writes files too (`sed`, `tee`,
  redirections), so a review skill's `disallowed-tools` names `Bash` beside
  `Edit` and `Write`, and since 2026-10-26 also `NotebookEdit`, `PowerShell`
  and `Monitor` (PowerShell is on by default on Windows without Git Bash,
  and no page says a skill's `disallowed-tools: Bash` removes it); `AGENTS.md` is read only when neither `CLAUDE.md` nor
  `CLAUDE.local.md` exists; trust given to a folder covers a subfolder
  without its own Git history, such as an unpacked download, whose hooks
  then run without a dialog, while a nested clone gets its own dialog; the
  sandbox covers shell commands only, so for `WebFetch` and MCP tools the
  deny rule is the control, not a back-up; `--dangerously-skip-permissions`
  is meant for containers or VMs in the permissions page, while the sandbox
  page also accepts the sandbox runtime, so "never on your own machine" is
  the paper's advice, cited to the permissions page.
  Verified on the evening of 2026-10-08 for chapter 10: a `Read(...)` deny
  rule stops Claude's file tools and the file commands it recognises, but
  not `grep -r` or a script that opens the file itself; the sandbox's
  `denyRead` stops those and takes in the `Read(...)` deny paths; personal
  plans keep sessions 30 days, or five years if training is allowed, and
  commercial terms keep them 30 days without training unless the customer
  opts in; `/feedback` sends the transcript with code and Anthropic keeps
  it five years (on Anthropic's own API only: on Bedrock, Google Cloud or
  without Anthropic credentials it stays in a local archive; checked
  2026-10-29); transcripts on disk are plain text, 30 days by default
  (`cleanupPeriodDays`); Anthropic's own API runs inference in the US or
  "global" only, so an EU region means Amazon Bedrock or Google Cloud;
  Anthropic does not support Claude Code with non-Claude models through any
  gateway. The Italian authority's EUR 15 million fine on OpenAI was
  annulled by the Court of Rome on 18 March 2026: never cite it as
  standing.
  Verified on 2026-10-09 in the full review: workspace trust never gates a
  skill's `allowed-tools` in any session, so "an interactive session asks
  first" does not cover a skill's pre-approved tools, and a download
  unpacked in a trusted folder uses them at once; `AGENTS.md` is skipped
  when a `CLAUDE.md` exists *by default* (a setting changes it); auto mode
  is the starting mode of *interactive* terminal and VS Code sessions; the
  `/memory` toggle writes `autoMemoryEnabled` to the user settings; a
  plugin is a bundle of skills, agents, hooks or MCP servers installed as
  one unit. Gloaguen et al.'s abstract says "over 20%", but files written by
  developers cost 19% more on average (the text says "at most", while its
  Table 2 has Codex with GPT-5.2 at about 42%), so the paper says "about
  20%" (since 2026-10-26); ImpossibleBench gives deleting
  tests only as an example and measured agents *changing* them. After
  CJEU C-413/23 P (4 September 2025) pseudonymised data is personal for
  whoever can reasonably link it back, so never write "while a key exists
  somewhere"; for whoever can link it back, coded health data stays
  personal data.
  Verified on 2026-10-26 against 2.1.310: since 2.1.295 a command or HTTP
  hook with `onFailure: "block"` blocks when it fails, times out or cannot
  start, so the paper advises it for every guarding hook and the
  repository's guarding hook sets it; on Windows without Git Bash a shell-form
  `PreToolUse` command hook that fails, exit 1 included, blocks by default;
  a single leading slash in a path rule anchors at the settings source (the
  project for project settings), so in user settings `/prod/**` means
  `~/.claude/prod/**`; `--bare` still applies the project's `env` block and
  helpers such as `awsAuthRefresh`; `strictAllowlist` works in user,
  managed or `--settings` settings, but against a repository you did not
  write the sandbox holds only when it is admin-required, which takes
  `allowUnsandboxedCommands: false` in managed settings or `--settings`: a
  `false` in user settings "doesn't make the sandbox admin-required", so a
  repository's `enabled: false` (against your `true`) and `excludedCommands`
  still apply, and its `allowedDomains` too unless `strictAllowlist` is set
  in user, managed or `--settings` settings (corrected 2026-10-28);
  idle compaction (2.1.299) summarises a session past 200K tokens left idle
  for about an hour, in interactive local sessions on the one-hour cache
  only (checked 2026-10-29); a subdirectory `CLAUDE.md` over a size limit loads only its start
  (2.1.309); on Pro and Max a new conversation can look up the old one
  (2.1.304), so a new session "starts without" the last conversation rather
  than "does not see" it; zero data retention is enabled per organisation
  by Anthropic's account team, never automatic; Desktop and Cowork
  transcripts are exempt from the 30-day cleanup by default; `/bug` and
  `/share` send the session like `/feedback` and are kept five years; on
  Bedrock the region comes from the endpoint *or inference profile*, and
  Claude Code's default profiles may fall back to a `global.` one; the
  60 days' notice before a model retires holds on Anthropic's platforms,
  while Bedrock and Google Cloud's Agent Platform set their own dates;
  `/web-setup` stores the GitHub CLI token in the Claude account, never in
  the session's VM; Cherny's thread says his setup "might be" surprisingly
  vanilla.
  Verified on 2026-10-27 for the talk's secret level (beat 10 since
  2026-10-28), against the Official
  Journal's texts: the AI Act (Regulation (EU) 2024/1689) says "human
  oversight" 17 times and "human in the loop" never, so never write that it
  requires a human in the loop; its Article 14 binds high-risk AI only
  (Annex I products, Annex III uses), and Regulation (EU) 2026/1744, the
  Digital Omnibus on AI, in force since 27 July 2026, moved it to 2 December
  2027 (Annex III) and 2 August 2028 (Annex I) and softened Article 4 to
  "support the development of AI literacy"; Article 14(4)(e) names a
  "'stop' button or a similar procedure"; decisions about people fall under
  the GDPR's Article 22; the expert group's guidelines of 2019, not law,
  call a human in every decision cycle "in many cases … neither possible
  nor desirable"; the EMA and FDA principles of January 2026 say
  "Human-centric by design" but never "human oversight"; and H shows the
  next hidden slide in PowerPoint's show, but not in Presenter View on
  Windows. Narrowed on 2026-10-28: the GDPR's Article 22 covers decisions
  based solely on automated processing with legal or similarly significant
  effects, not every decision about people; the 2019 guidelines come from an
  independent expert group the Commission set up, not from "the EU itself";
  the EMA and FDA principles ask for "oversight based on the context of
  use", though never "human oversight". The EU's draft GMP Annex 22
  (consultation July to October 2025, not adopted as of October 2026) says
  generative AI and LLMs should not be used in critical GMP applications
  and calls the qualified person who answers for their output in
  non-critical ones "a human-in-the-loop": say "draft", and that it covers
  manufacturing.
  Verified on 2026-10-28 in the final check before submission: the
  best-practices page was rewritten on 2026-10-27, so its "would removing
  it cause a mistake?" test and its "performance degrades as it fills" are
  gone; it now lists "the context window is your main constraint" among
  advice you can stop following, since running out is rare, while "a
  focused context gets you better answers and costs less". SWE-Skills-Bench
  posted version 2 on 2026-10-27 (98 skills, four configurations, "92 of 98
  skills have no statistically significant effect", 76.6% to 76.9%); v1's
  "39 of 49" and "nine in ten" are gone from the current version. Excalidraw
  is a registered US mark (Reg. 6,863,755, 2022), so it carries ®, as do
  Cursor, VS Code, Windows, Nx, Amazon Bedrock, OpenCode and Mac Studio
  (USPTO TSDR, read that day). PHUSE's final deadline for paper and
  presentation is Friday 30 October 2026 (key-dates page); its Code of
  Conduct V5 forbids using PHUSE's logos "for any business or commercial
  venture" without the Board's pre-clearance, and declares Connect
  proceedings "freely available for public, unlimited and unrestricted
  global use". PHUSE's programme lists a second speaker for ML19, a
  colleague who is the author's backup in case he cannot speak; the paper
  and the deck do not name her, and neither does the public copy (the
  author's decisions, 2026-10-28 and 2026-11-15). SWE-Skills-Bench is cited
  in its version 2, pinned in [16].
  Decrypt calls the April 2026 case "a Cursor agent running Anthropic's
  Claude Opus", so the paper says "in a Cursor agent", not "editor".
  Rapid-MLX gives V4 Flash a floor of 192 GB (2-bit), "256 GB
  comfortable" for that 2-bit build of the April checkpoint only; the 0731
  checkpoint Vals measured is "192 GB+", and the 4- and 8-bit builds "leave
  little headroom even on a 256 GB Mac" (read 2026-10-29). A subagent starts without the main conversation's auto
  memory, a fork aside. The narrated deck's voice is ElevenLabs' stock
  voice Brian, no clone, so it is no deep fake under the AI Act; its title
  slide says the voice is generated all the same.
  Verified on 2026-10-29, when chapter 2 began to say what the system
  prompt is (the author's request; the labels rule left the good-rule
  examples to make room): the context-window page's timeline calls it
  "Core instructions for behavior, tool use, and response formatting.
  Always loaded first. You never see it." The words stand in the page's
  interactive timeline only, not in its Markdown version; the memory page
  says `CLAUDE.md` arrives "as a user message after the system prompt, not
  as part of the system prompt itself".
  Verified on 2026-10-29 for chapters 6, 7 and the Conclusion (the
  author's requests): Claude Code caches prompts on its own; a cached
  re-read is billed "below the standard input rate"; the main
  conversation's cache lives one hour by default only on a subscription
  within its included usage, five minutes otherwise, and "Each model has
  its own cache", so a model switch reads the whole history uncached
  (prompt-caching page); the costs page says a long session still "draws
  usage for the whole conversation". The memory page names auto memory on
  in local sessions and off in self-hosted environments, but says nothing
  about Anthropic-hosted cloud sessions, so never write that it is on or
  off there: it is "machine-local", and each cloud session gets a fresh
  VM (cloud environments page), so its notes do not reach the next
  session. `@path` imports load in full with the `CLAUDE.md` that imports
  them, so a decision log imported that way costs context every session.
  Basic Memory (AGPL-3.0) keeps notes as Markdown on your disk that "both
  you and your AI can read, write, and search"; its default folder lies
  outside the repository, so the paper names it for your own machine; no
  US registration was found. OpenCode has two versions; the current docs
  (OpenCode 2) read `AGENTS.md` only, without the `CLAUDE.md` fallback of
  OpenCode 1, read skills from `.claude/skills`, put hooks into plugins,
  and have allow, ask and deny rules (last match wins, permissive
  defaults) but no built-in memory or sandbox; the Conclusion cites its
  "Migrate from V1" page, which names all five it lists. The September
  2026 case, from TechCrunch (8 September): Tristan Buckmaster and Levent
  Alpöge worked "relying primarily on OpenAI's Codex"; OpenAI published a
  proof of the Navier–Stokes problem their work "had taken steps towards";
  OpenAI said it did not see their work "until they released it publicly"
  and "While unlikely, we cannot rule out that de-identified data derived
  from their usage of our products helped improve our models". The word
  "drafts" is not in the article, so the paper does not use it, and it
  quotes "de-identified data" as OpenAI's term. Andreas Thom's similar
  account rests on his own posts and stays out. OpenAI's word mark is
  pending, not registered (Serial 97/238,896), so OpenAI carries no ®.
- Evidence beyond the documentation: each chapter from 2 to 10 cites at
  least one source that is not Anthropic's documentation, a study, a report,
  an incident, a regulator or the law, so the reader gets links worth following and the paper
  stays honest about what is known. `paper/further-reading.md` lists studies
  for and against the mechanisms; the build does not read it, and the
  References lead-in says that more studies are available on request
  (since 2026-10-26 the paper links no repository file; "on request" since
  2026-10-27, when the author began to speak as "I"). An entry there is marked checked only
  after its page was read, and a study enters the paper only through
  `/add-reference`, like any other source. Fortune refuses scripts without a
  browser user agent. METR marks its 2025 study out of date (seen
  2026-10-08); it left the paper that day with the Conclusion's paragraph on
  speed, and `further-reading.md` keeps it with the note. Chapter 9's PHP
  case, Laravel-Lang (May 2026, the author's choice of 2026-10-26 over the
  PHP2Shell flaws of October 2026, which were no supply-chain attack), cites
  BleepingComputer's report, which draws on StepSecurity, Aikido and Socket.
  The vendors count 233 or about 700 versions, so the paper gives no count
  of versions; since 2026-10-29 it counts the four packages the report
  names.
  Two more cases came in on 2026-10-26 at the author's request. Chapter 2:
  a Claude model in Cursor deleted a startup's production database and
  backups in nine seconds, despite a written rule never to guess (Decrypt);
  the details are the founder's account, so the sentence says so, and the
  article does not say whether the rule came from Cursor or the company.
  Conclusion: US Executive Order 14434 of 29 September 2026 tells federal
  agencies to call artificial intelligence "Super Intelligence", with the
  same definition (Sec. 2(a), 3(a)); quote the order, never its politics.
  On 2026-10-27 it left the Conclusion and the list with DORA's line, to
  make room for the author's outlook; `further-reading.md` keeps both, and
  the talk's 8.2 and R.12 keep DORA. The outlook's sources, read that day:
  Phoronix (7 October 2026) says "Claude Code and AI agents have created"
  ArtCraft's open-source rebuilds of Photoshop, Premiere and Lightroom; the
  project's README names no AI, and the model named in other reports comes
  from secondary coverage, so the paper names no model, and it says
  "Adobe's photo and video editors", which needs no trademark symbol. MIT
  Technology Review (24 April 2026) calls DeepSeek's V4 open source,
  "available for anyone to download, use, and modify", and its API "a
  fraction of the cost of comparable models from OpenAI and Anthropic".
  OpenCode's homepage says "The open source AI coding agent" and "75+ LLM
  providers through Models.dev, including local models". Today's prices
  being "cross-subsidised" found no source a reader can open, so the
  Conclusion states the author's wish instead. Micron's exit from its
  Crucial consumer brand (press release of 3 December 2025, to supply AI
  data centres) would carry "if we can still buy it by then", but the
  reference page had no room. That evening the cut for repetition took
  Cherny's thread out of the Conclusion; `further-reading.md` keeps it.
  Last that evening, at the author's request, [3] (now [4]) became the 2025 talk's
  slides (PRE_ML04.pdf in the PHUSE archive, beside the paper): slides 12
  and 13 carry the baby junior, 15 the data kraken fed by OpenAI, Claude,
  DeepSeek and others, and 32 "Online AI use = Data donation". mobiFlip
  (26 August 2026) prices the fully loaded Mac Studio (M5 Ultra, 256 GB,
  16 TB) at 20,679 euros, 512 GB to follow in late October. The author
  wanted DeepSeek "roughly at Opus 5": Vals AI's SWE-bench Verified (9/1/2026)
  has Claude Opus 5 at 97.0% and DeepSeek V4 Pro at 96.4%, but Vals has
  archived the benchmark as saturated.
  Later that night, at the author's request, the comparison became one with
  last year's model: on the same Vals page and harness, DeepSeek V4 Flash
  0731 scores 88.8% and Claude Opus 4.5 (Thinking) 76.4%; the saturation
  sits near 97%, so this gap still tells. Anthropic's model page dates Opus
  4.5 to 24 November 2025. For the hardware the author asked for the
  smallest Mac Studio that runs DeepSeek properly: Rapid-MLX lists V4
  Flash's 4-bit build as a download of about 152 GB with a 256 GB Mac Studio
  as its memory floor (the 2-bit build's floor is 192 GB), and
  Context Studios read the German Apple Store on 24 September 2026: M5
  Ultra (30-core CPU, 64-core GPU) with 256 GB and 1 TB, 10,999 euros. The
  larger V4 Pro and the newer V4.1 Flash need more than 400 GB in 4 bits,
  so the paper names V4 Flash only. Hugging Face's DeepSeek page carries
  "a Chinese company" and the V4 downloads, in place of MIT Technology
  Review; mobiFlip and Stack Overflow's survey left the list. To keep the
  list on one page, two entries give only their main title (the 2025 talk,
  Context Studios) and Rapid-MLX's title drops its suffix; on 2026-10-29,
  when four sources came in, eight more lost the part after the colon
  (Gloaguen et al., McMillan, Denisov-Blanch et al., ImpossibleBench,
  SWE-Skills-Bench, SkillsBench, Context Rot and Wiz's s1ngularity post).
- Submission format, verified 2026-09-15 against the PHUSE paper guidelines
  (US Connect 2022 edition, the current one returns 403 to scripts):
  one-column PDF, page numbers on every page, at most twelve pages for a
  20–25 minute talk, paper number centred above the title, "Author, Company,
  City, Country" below it, no job titles or addresses, PDF properties filled
  (title, keywords, author, subject `XXnn – PHUSE EU 2026`), file name
  `PAP_XXnn.pdf`, trademark symbol at the first mention of a registered
  name. Fonts and margins are only recommended. Exception to the symbol:
  Anthropic's trademark guidelines say not to use one with its names, so
  Claude and Claude Code carry none and the Contact Information names them.

## 8. Build contract

- **`uv run python tools/build_paper.py`** builds the PDF as
  `out/PAP_<paper_number>.pdf`, the file name PHUSE asks for, taking the
  number from `paper/metadata.yaml`. `--stats` prints the page count and
  lists, per chapter, the sentences over 25 words, the empty openers and
  the stacked hedges (proofreading hints, the Abstract skipped; section 3);
  `--watch` rebuilds on source changes; `--renumber`
  numbers the references in order of first citation before it builds.
- **`uv run python tools/check_sources.py`** verifies the `.claude/` setup,
  the reference list and every file and sentence the slides quote. Run both
  after any substantial change.
- **`uv run python tools/build_slides.py`** builds the talk as
  `out/PRE_<paper_number>.pptx`, PHUSE's name for a talk's slides. `--list`
  shows which images are still missing, `--final` fails while any placeholder
  remains. The deck embeds each still at what its frame needs at 1920 px
  across the slide (`DECK_PX`), a zoomed crop sharper, while the sources stay
  whole for the paper (since 2026-10-29, when the deck had reached 20 MB).
  `--full` builds `out/PRE_<paper_number>-full.pptx` with every still
  whole instead (since 2026-10-29), and combines with `--narrated`
  (`-narrated-full`). The deck is never edited by hand either: change
  `slides/storyline.md` or `slides/deck.yaml` and rebuild.
  `uv run --group narration python tools/build_slides.py --narrated`
  builds a second deck, `out/PRE_<paper_number>-narrated.pptx`, that tells
  the story by itself (since 2026-10-21): each slide plays its stretch of
  the narration from `slides/narration/takes/`, as
  `slides/narration/clips.yaml` maps it, and moves on when it ends. A reference slide
  quotes a repository file by line range at build time, and its `expect`
  strings stop the build when the file changes underneath it; a sentence it
  quotes from the paper stops the build when the paper no longer says it.
- `paper/paper.md` is the source of the prose and `paper/references.md` the
  only copy of the reference list; the build renders the list where the
  `::: references` fence stands, in number order and in two columns of
  equal height (since 2026-10-26), in a compact form: a documentation page
  by its page name, with the address it shares stated once in the lead-in,
  and pages cited one after another in one entry; other URLs without
  `https://www.` and arXiv as `arXiv:<id>`; and the access date most entries
  share stated once, in the lead-in (the build warns when the lead-in does
  not name it), which says that the entries without a date of their own
  were read on that day (since 2026-10-27; on 2026-10-28 every entry
  shared the date of the final check, and since 2026-10-29, when four
  sources read that day came in with their own date, the lead-in says
  "Sources without an access date were read on 28 October 2026"; the
  documentation's version left the lead-in for space and stands in the
  Introduction). The list and the Contact
  Information share one page; since
  2026-10-26 its entries stand 2 pt apart with 0.45 em leading, the least
  that keeps fifty-three sources and the Contact Information on it (fifty-seven since 2026-10-29). The PDF is
  **never** edited by hand; a hook refuses it anyway.
- `out/` is generated, disposable and git-ignored.
- **`uv run python tools/release.py <tag>`** (since 2026-10-29) checks the
  sources, builds the paper and the deck with `--final`, stages
  `PAP_<paper_number>.pdf` and `PRE_<paper_number>.pptx` in `dist/<tag>/`
  (git-ignored, and the hook refuses hand edits there too) with that tag's
  section of `CHANGELOG.md` as the notes, and prints the `gh release create`
  command; the author runs it. `--use DIR` stages files already built, such
  as the ones uploaded to PHUSE, instead of building them; `--full` adds
  `PRE_<paper_number>-full.pptx`, built with `build_slides.py --full`. A published
  release is the frozen copy of what was handed in or shown: never upload
  over one, cut a new tag. The files as uploaded to PHUSE are in
  `submission/`, in the working repository only. Of these only the paper
  is released, by hand, as `v1.0-submission`; the decks as uploaded are
  not released, and the deck's release is a new build after the talk (the
  author's decision, 2026-11-15; `review/` keeps the reason). The script
  prints `gh release create` without a repository, so run in the working
  repository it would publish there: a release of the public copy is made
  in a clone of the public repository, with `--use DIR`.
- **`uv run python tools/export_public.py DIR`** (since 2026-11-15) stages
  the public copy in the empty folder `DIR` and checks it; it never pushes.
  It copies the tracked files of `HEAD` without the paths its list leaves
  out (section 6) and deletes the copy again unless every gate passes: no
  secret, no entry of the deny-list in `review/public-denylist.txt`, no
  e-mail address the paper does not print, no commit of the working
  history beyond the two that the paper's hidden comment names, no path
  with a user name, no metadata in the pictures and takes, both hooks
  executable, no file above 50 MB, and in the copy itself all checks of
  `check_sources.py` passing and the paper and the deck building.
  `--record FILE` writes the export's record, every file with its SHA-256,
  for `review/`. The script stays in the working repository.
- No `pip install`, no `brew install`. All dependencies go through
  `pyproject.toml` and `uv`.

### Toolchain (why it is what it is)

- One native dependency for the paper: the `typst` wheel (ships the compiler
  and embedded fonts; Libertinus Serif renders without a system install on
  Linux and macOS).
  Libertinus Mono for code is bundled in `tools/fonts/` (OFL) and passed to
  the compiler as a font path, so it needs no installation either.
  Markdown is rendered by the **vendored** `cmarker` Typst package in
  `tools/vendor/cmarker/` — imported by path, so builds are fully offline and
  reproducible.
- **pandoc is deliberately not used.** `pypandoc-binary` 1.17 bundles an
  x86_64-only pandoc (in *both* macOS wheels, including the arm64-tagged one),
  which will not run natively on Apple Silicon. Do not reintroduce it.
- `tools/template.typ` owns all layout (margins, fonts, headings, callout,
  figure and table styling, title block). Tables sit on striped rows under a
  light accent band, with a bold first column for each row's key (the
  author's choice of 2026-10-08). The accent is Evidenze green, as in the
  talk (since 2026-10-26, at the author's request, in place of purple):
  `#27b564` for rules, a darker `#1b7e46` for headings and links, which
  keeps 5:1 contrast on white. `tools/build_paper.py` splits `paper.md` at the
  `:::` fences, writes segments to `out/seg/`, and stitches `out/main.typ` from
  the template helpers.
- `paper/metadata.yaml` feeds the title block and the PDF properties:
  `paper_number` (ML19, assigned by PHUSE), `city` and `country` for
  the author line, `subject` and `keywords`. The title block follows the PHUSE
  layout (number above, centred title, author line below); the typography
  is ours. The slides' title slide reads the same file.
- The paper's two diagrams are made outside the build (since
  2026-10-26): `tools/diagrams/` writes them as Excalidraw scenes
  with the standard library and exports them with Excalidraw's own library
  in Chromium, which needs Node and Playwright, not `uv`. The build only
  reads the PNGs in `paper/figures/`; `tools/diagrams/README.md` says how to
  rebuild one.
- The slides add `python-pptx` (which brings lxml and Pillow, with arm64
  wheels) and `segno` for the QR codes. The deck names Arial and Consolas,
  which ship with PowerPoint, so nothing is installed for them. Its slide
  design follows the minimalist layout of the author's PHUSE EU Connect 2025
  deck (ML04) in the brand of Evidenze Germany; the images keep their own
  black-and-white look. `slides/README.md` and `slides/brand/README.md` say how.

### Authoring callouts

Fenced blocks that plain Markdown ignores:

```
::: note        neutral aside — use sparingly for a small analogy
::: warning
::: tip
::: disclaimer  how the paper was made — used once, between Abstract and Introduction
::: figure      one image, or two side by side, with a caption; `placement: none` pins it,
                `height: 63mm` sizes a single image (a diagram) in place of figure-height,
                `side: right` sets a single image beside the paragraph before the fence
::: filecard    describe a repository file and link to it (not used in the paper since 2026-10-08)
::: pitfalls    closes a mechanism chapter: bullets, then a `---` line and one warning paragraph
::: references  the reference list, rendered from paper/references.md
```

Callout bodies may span multiple paragraphs — they are rendered as real
Markdown. Images appear only in a `figure` fence: one or two `![alt](path)`
lines, each path relative to `paper/` (the talk's images are
`../slides/beats/…`), then the caption. The build fails on a missing file,
and the alt text goes into the PDF.
A file card (no longer used in the paper, section 6) names a repo-relative
path on its first line, may add
`kind: hook|skill|agent|rules|settings|script` (otherwise inferred from the path),
then one paragraph of purpose that becomes the caption, a blank line, and
bullets on what the file does. A missing file or unknown kind fails the build.
Cards render as numbered figures of their own kind ("File 3") with a coloured
kind tag and the path linked to GitHub, and the prose refers to them by
number. The `references` fence has an empty body; the lead-in paragraph and
the grouped entries come from `paper/references.md`, and a group's title
sticks to its first entry. A figure would float;
the paper's figures carry a `placement: none` line, which pins them where
they stand (section 9). An unknown fence name renders as a
loud orange "Unknown callout" box so typos are caught in proofreading — the
valid kinds are exactly the eight above.

A `pitfalls` fence renders as one red card: the bullets on the left and the
warning as a narrower box on the right. The build refuses a fence that does
not start with a bullet, lacks the `---` line and its warning, has more than
one `---`, or has a `---` with nothing after it, and warns when the paper
does not carry exactly nine such cards (chapters 2 to 10).

## 9. Paper structure

Fixed section skeleton — do not reinvent it each session. **Never number the
headings by hand**: numbering comes from `#set heading(numbering: "1.")` in the
template and will drift if typed into `paper.md`.

```
Abstract
1. Introduction
2. Ground rules — CLAUDE.md and system prompts
3. Reusable procedures — skills
4. Guardrails — hooks and permissions
5. Delegation — subagents
6. Context and token management
7. Memory — what persists between sessions
8. Isolation — a separate machine, a separate user, synthetic data
9. Safety — prompt injection and supply-chain attacks
10. Data protection — where your data goes, and who you depend on
11. Putting it together — a walkthrough
12. Conclusion
References
Contact Information
```

**No sub-headings.** The chapter titles above are the paper's only headings
(decided on 2026-10-08). Numbered sections in the middle of a page broke the
reading and invited text that only filled a slot. `build_paper.py` warns when
a chapter from 2 to 10 carries one.

Instead, each chapter from 2 to 10 follows the **same page pattern**, so it is
not reinvented per session and the paper stays scannable: read on top, look
things up below. Chapter 9 is not an eighth mechanism: it applies the seven
to one threat, text and code nobody here wrote, and "the seven" stays seven
everywhere else. Chapter 10 is no mechanism either: it applies the seven to
personal data and to the dependence on one vendor (added on 2026-10-08 at
the author's request, on the page PHUSE still allowed).

```
Text           three or four short paragraphs: when you need it, what it is,
               how to set it up, and what the evidence says (at least one
               source beyond the documentation)
Figure         a pair from slides/beats/, in every chapter from 2 to 10
               but 4, which carries its diagram instead
Table          the essentials to look up, about five rows (4 and 9: a
               diagram instead)
Pitfalls card  bullets, then the warning that names the genuinely dangerous case
```

Open with the moment the reader knows, when that reads better than the
definition: "Nobody signs off their own work" opens chapter 5. Each fact
appears once per chapter. The text carries the reasoning and the evidence,
the table the facts to look up and the pitfalls card the warnings. At most
one sentence introduces a table.

**Page rule.** Chapters 2–11 and the reference list each start on a new page;
the template inserts the breaks, never `paper.md`. A chapter keeps to its page
or pages; when it spills only a little onto the next one, cut it, and when it
needs the next page, let it take the whole page. Space left at the foot of a
page is fine: never pad a chapter to fill it. The Abstract, the disclaimer
and the Introduction share page 1, and the Conclusion follows chapter 11 on
its page. The Introduction is there to catch the reader (the author's
direction, 2026-10-26): its heading is just "Introduction", it opens with
the author's greeting (since 2026-10-27, in place of a late evening the
reader knows, which the drawing now shows), and it carries a picture
instead of a table. Level-1 headings render as chapter openers (large number, title,
rule); the pitfalls card closes each chapter from 2 to 10.

No chapter carries a file card (since 2026-10-08, section 6). Chapter 11
walks one task through the seven in general terms. Abstract, References
and Contact Information are unnumbered: the build emits them without a
number, and the template styles them. The
`::: disclaimer` box sits between Abstract and Introduction.

**One table per chapter from 2 to 10**, below the text and the figure.
Chapters 4 and 9 are the exceptions: each shows its path as a diagram
instead (below), chapter 4's straight after the opening paragraph,
chapter 9's after the paragraph that names the trifecta, above its pair. Chapter 6 has one table, the four commands, whose `/compact` cell says
what comes back (since 2026-10-29, at the author's request: the second
table, what survives `/compact` versus `/clear`, made room for prompt
caching). Enumerations go into bullets or tables; prose carries the
reasoning. Sentences flow: one thought each, with its link kept (section 3). No stage directions ("Here
is…", "Notice that…", "It is worth knowing…").

**One drawing in the Introduction** (since 2026-10-26, in place of the
table of the seven mechanisms): `beat-01-alone-1`, the programmer alone at
the bench late at night, the board full of notes, with a caption that names
the role only, never Steve and no allusion to the talk's story. Page 1 has
no line to spare, so the drawing stands 30 mm high beside the first
paragraph (`side: right`; since 2026-10-27 it opens the chapter, beside the
greeting, the reader's aim and the dangers), whose text fills its height, so
no white patch is left beside the caption (the author's request); below
the text it would push the Introduction onto page 2.

**One drawing after the Conclusion** (since 2026-10-27, at the author's
request): the cast waving goodbye, the still
`slides/studies/anim-04-goodbye-out-own-clothes.png` that
`tools/goodbye_wave.py` turns into the talk's goodbye GIF, 28 mm high
(`height: 28mm`), centred, its caption naming roles.

**Eight pairs of drawings**, each from `slides/beats/` at a fixed height
(`figure-height` in the template), pinned where it stands, with a caption of
a few short sentences that names roles. Each pair sets the problem on the
left beside the mechanism at work on the right. Each drawing carries the
EU's AI icon in its top right corner, which the template adds (`ai-label`),
and the disclaimer says once what it marks.

| Chapter | Pair | Left / right |
|---|---|---|
| 2 Ground rules | `beat-02-claude-md-1` \| `-2` | the worker in its own style, corrected by hand / it reads the house rules first |
| 3 Skills | `beat-03-skills-1` \| `-2` | the worker redraws the spec / the skill makes it compare and report |
| 5 Delegation | `beat-05-subagents-1` \| `-3` | the worker passes its own work / the reviewer behind glass |
| 6 Context | `beat-06-context-1` \| `-2` | the meeting that never ends / one topic, the rest in the bin |
| 7 Memory | `beat-07-memory-1` \| `-2` | the Monday re-briefing / the decision log |
| 8 Isolation | `beat-07b-isolation-1` \| `-3` | what the worker reads leaves the laptop / an office of its own |
| 9 Safety | `beat-07a-safety-1` \| `-2` | a planted letter pulls at the keys / the post room |
| 10 Data protection | `beat-07c-data-1` \| `-2` | the Book of Secrets flies into the provider's warehouse (black sheets until 2026-10-28) / only synthetic data leaves, kept for a while |

Chapters 2, 6 and 7 gained theirs on 2026-10-08, at the author's request,
and chapter 10 that evening with the talk's beat 7c, so every chapter from
2 to 10 carried one. On the evening of 2026-10-26, at the author's request,
chapter 4 gave its pair (the sign on the wall, the guard bolted to the
floor) to its diagram: the diagram carries the same cast and the same
point, and drawn large it reads in print. Later on 2026-10-27 the
Conclusion gave up its pair (the programmer before and after), at the
author's suggestion: it repeated the closing line. More figures only on the
author's request.

**Two diagrams** (since 2026-10-26, at the author's request; tried first
as a side version, then made the main one). A diagram earns its place only where the text describes a path,
steps in order or a boundary something crosses, and only in the chapter that
defines its terms. It replaces that chapter's table and the sentences it
draws; a table of facts to look up stays a table. Its caption walks the
reader through it in reading order, numbered as the diagram is, with the
citations, so the figure is usable without the text around it. One key
everywhere: shaded green (Evidenze green at 20%, since 2026-10-26; lavender
before) with a thick border holds whatever the model
decides, dashed grey is text the model reads, red is where a call stops.
The talk's cast stands where it acts, and the caption names its role. The
cast is redrawn in the diagrams' own hand-drawn look, from the talk's
portraits, by the same image model (Nano Banana 2.1 on fal, one character
sheet of 2026-10-26, its lines thickened to the diagrams' stroke), so the
diagram reads as one drawing; the talk's slides keep their own drawings.

| Chapter | Diagram | What it shows |
|---|---|---|
| 4 Guardrails | `figures/tool-call` | one tool call through hook, permission rules and mode; the guard on the hook, the programmer on the prompt, the worker where the tool runs; 63 mm high, the full text width |
| 9 Safety | `figures/trifecta` | the lethal trifecta as a path with the control on each leg; the planted letter, the reviewer reading it, the worker in its closed environment |

Each diagram's source, `paper/figures/<name>.excalidraw`, lies beside its
PNG and opens in Excalidraw (or in Obsidian with its Excalidraw plugin). The PNG is exported at three times the
canvas, and the top right corner stays empty for the AI icon. The trifecta
is 1640 by 400 units at the template's 40 mm; the tool call is 1480 by 560
units at 63 mm, the full text width, so its 24-unit labels print at about
7.5 pt. The template treats each diagram like a drawing, so each carries
the icon too. The slides keep the two tables as literal blocks
(R.4, R.9).

**The Abstract is frozen.** It is the submitted text: never change a word of
it, neither in `paper/paper.md` nor in `README.md`.

## 10. Length discipline

Target **8–12 pages**; twelve is PHUSE's hard limit for a 20–25 minute talk
and `--stats` warns above it. After any substantial addition, run
`uv run python tools/build_paper.py --stats` — the count comes from the compiled
document, not a word-count estimate. With the seven mechanisms, Safety, Data
protection and a reference list that shares one page with the Contact
Information, the paper has 12 pages, PHUSE's limit (since the evening of
2026-10-08): chapters 2 to 10 take one page each, every one with a
figure, and no page is left to spare. Aim for about 300 words of text
in a chapter; the figure, the table and the pitfalls card take the rest of
the page. The reference list has no room to spare: a new source costs
another one or a line elsewhere on that page. Keep each chapter to its page. Because every chapter starts on a new page, the unit
to watch is each chapter's own length, not only the total: a chapter that
overruns its page by a few lines costs a whole page. Check the rendered pages
after a change, not only the count. If it runs long, cut content; do not
shrink the font. A pair costs about twelve lines, a diagram with its walk-through caption
sixteen (chapter 9) to twenty (chapter 4); its chapter pays for them.

## 11. Git

English commit messages, imperative mood. Commit only when the author asks.
Never commit `out/` or `.DS_Store`.
