# How to Control the Machine Spirit without Just Praying for Success

Source repository for a paper and talk at **PHUSE EU Connect 2026** (Glasgow,
November 2026): the paper, the slides and the narrated deck, and the Claude
Code setup they are made with.

## Abstract

AI talk is everywhere right now, and most of it is either sales pitches or doomsaying. What most of us actually want is something more practical: how to force the magical black box to stop using certain styles, to write structured code without burning through our tokens, and to leave our database alone when it stumbles on an API key.

This paper shows what current techniques can do about exactly that, with Claude Code as our example. We will walk through system prompts for setting the ground rules, skills for teaching the model reusable patterns, hooks for catching dangerous actions before they fire, token management for keeping the bill sane, and ways to give the AI memory of what it has learned.

AI shouldn't be a gamble, and it shouldn't be a séance either. Let's try to tame the machine spirit together, with the tools we already have.

## What is in here

```
paper/          paper.md (single source of truth), metadata, references, figures,
                and further-reading.md: the studies for and against
slides/         the talk: storyline, the deck recipe (deck.yaml), images in
                slides/beats/, the AI label and the logos * in slides/brand/,
                the narration, the questions to expect *
promo/ *        what points people to the talk: the LinkedIn teaser, its
                prompts and the post's draft, a brainstorm of further posts
                and a carousel
.claude/        the Claude Code setup the paper and talk are made with:
                settings, hooks, skills and a subagent
tools/          build_paper.py, build_slides.py, check_sources.py,
                release.py, export_public.py *, promo_teaser.py *,
                promo_ideas.py *, promo_carousel.py *, the Typst template,
                the diagrams and the animated drawings
review/ *       the records of the reviews and of each public copy
submission/ *   the paper and the decks as uploaded to PHUSE
CHANGELOG.md    what changed in each release
```

\* Only in the working repository. The work happens in a private working
repository, and `tools/export_public.py` makes the public copy from it: a
fresh start without the working history, and without the parts marked
above. On GitHub, `UnfriendlySpider/how_to_tame_the_maschine_spirit` is the
public copy. Where a note names one of the marked parts, a commit or the
git history, it means the working repository. Without the logos the deck builds with a
placeholder in each place, and `--final` refuses.

The builds write to `out/`, a release is staged in `dist/`, and both are
git-ignored. The [GitHub releases](https://github.com/UnfriendlySpider/how_to_tame_the_maschine_spirit/releases)
of the public copy carry the built files: the paper as submitted, and the
deck once the talk is given.

## The Claude Code setup

The rules in `CLAUDE.md` and the files in `.claude/` are the working tools
the paper and the talk are made with, and the talk's reference part quotes
them: a hook that refuses hand edits to the built paper and decks and to
the files staged for a release, one that flags American spellings, skills that build the paper,
check a claim against the documentation, add a source or review a chapter's
style, and a read-only subagent that audits the reference list. Install
[uv](https://docs.astral.sh/uv/) and `jq` to use them.

Hooks are shell scripts that run on your machine. Read `.claude/settings.json`
and `.claude/hooks/` first, as you should for any repository you did not write.

## Build the paper

The paper is written in Markdown (`paper/paper.md`) and rendered to a PDF via
Typst. The reference list comes from `paper/references.md`; citations in the
prose are `[n]`, and the build fails on a citation without an entry or an
entry that is never cited. Everything runs through `uv`; no system pandoc,
LaTeX or fonts required.

```sh
uv run python tools/build_paper.py            # build out/PAP_ML19.pdf
uv run python tools/build_paper.py --stats    # build, then print page count and style hints
uv run python tools/build_paper.py --watch    # rebuild on source changes
uv run python tools/check_sources.py          # verify the setup, the references and the slides' quotes
```

## Build the slides

The talk's deck is a PowerPoint file built from `slides/storyline.md` and
`slides/deck.yaml`. Every image that is not made yet shows as a placeholder
with its scene, so the deck is complete from the first build; see
`slides/README.md`. The narrated deck tells the story by itself: each slide
plays its stretch of the narration and moves on when it ends.

```sh
uv run python tools/build_slides.py            # build out/PRE_ML19.pptx
uv run python tools/build_slides.py --list     # which slide images are still missing
uv run python tools/build_slides.py --final    # fail while anything is a placeholder
uv run --group narration python tools/build_slides.py --narrated   # build out/PRE_ML19-narrated.pptx
uv run python tools/build_slides.py --full     # build out/PRE_ML19-full.pptx, the drawings at full resolution
```

The deck scales its drawings down to what a projector shows, to keep the
file small; `--full` builds a second deck with every drawing whole, for
print or a large screen. It combines with `--narrated`
(`out/PRE_ML19-narrated-full.pptx`).

## Make a release

A release carries the paper and the deck as PHUSE names them,
`PAP_ML19.pdf` and `PRE_ML19.pptx`. Write the tag's section in
`CHANGELOG.md` and commit everything first; the script refuses a dirty
working tree or a tag that exists already. The first release,
`v1.0-submission`, is the exception: it carries the paper alone and is
made by hand, because the script always stages both files and the decks
as uploaded are not released.

```sh
uv run python tools/release.py v1.1-conference                  # check, build, stage dist/v1.1-conference/
uv run python tools/release.py v1.1-conference --use DIR        # stage files already built instead
uv run python tools/release.py v1.1-conference --full           # attach PRE_ML19-full.pptx as well
```

It checks the sources, builds both files (the deck with `--final`),
copies them into `dist/<tag>/` with the release notes, and prints the `gh release create` command to run. It never
publishes by itself. A published release is the frozen copy: to change
something, cut a new tag. The printed command names no repository, so it
publishes where it is run: a release of the public copy is made in a clone
of the public repository, with `--use DIR` on files built in the working
repository, because without the logos the public copy cannot build the
final deck.

## Make the public copy

In the working repository only:

```sh
uv run python tools/export_public.py ../public-stage --record review/<date>-public-export.md
```

The script copies the tracked files of the current commit into an empty
folder, without the parts marked above, and checks the copy before anything
can be pushed: for secrets, for the entries of a deny-list kept in
`review/`, for e-mail addresses the paper does not print, for commits of
the working history and for metadata in pictures and takes, and it runs the
source checks and both builds in the copy. Its header lists every gate. A
single finding deletes the copy. It never pushes, and the public repository
changes only through such a copy.

## The talk

The talk is deliberately different from the paper. It follows Steve, a
programmer with more ideas than hands, who takes on one virtual
worker, then several, and discovers that the hard part is not the hiring but
the onboarding, the procedures, the access rights, the right worker for the
right job, the meeting discipline, a memory that outlasts the day, and an
office of its own. Each of those is one Claude Code mechanism, and the point
of the talk is that a well set-up agent system is organised like a well
set-up company. The story lives only in the talk; the paper is the reference
and borrows eight pairs and two single drawings of its pictures. See `slides/README.md`.

See `CLAUDE.md` for the working rules (language, tone, accuracy, structure).

## Licence

The repository is published under the MIT License (`LICENSE`), with these
exceptions, which keep their own terms:

- `tools/vendor/cmarker/`: the cmarker Typst package, MIT, with its own `LICENSE`.
- `tools/fonts/LibertinusMono-Regular.otf`: SIL Open Font License 1.1, see
  `tools/fonts/OFL.txt`.
- `slides/brand/eu-ai-black.png`: the European Commission's icon for
  AI-generated content, free to use (`slides/brand/README.md`).
- `slides/brand/phuse-connect-2026.png` and the Evidenze logos in
  `slides/brand/`: their owners' marks, not licensed for reuse, and not part
  of the public copy.

The drawings in `slides/` and `promo/` \* and the cast in `tools/diagrams/cast/` were
generated with Nano Banana® 2.1, and Claude Code drew the two diagrams in
`paper/figures/` with Excalidraw® around that cast. The narration was
generated with ElevenLabs Eleven v4. Both models were used through fal.
The drawings in `promo/linkedin/ideas/` \* and `promo/linkedin/carousel/` \*
were generated with Nano Banana 2 through Meshy.
