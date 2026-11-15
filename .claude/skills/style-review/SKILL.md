---
name: style-review
description: Review one chapter of paper/paper.md for sentence style, against the rules in CLAUDE.md section 3 (actor as subject, verb early, new information last, one hedge per claim, citations where their clause ends). Reports wording to change and never edits. Use when asked to polish, tighten or check the style of a chapter.
argument-hint: "[chapter title or number]"
allowed-tools: Read Grep Glob
disallowed-tools: Edit Write NotebookEdit Bash PowerShell Monitor
---

# Style review of one chapter

Review the chapter of `paper/paper.md` named in `$ARGUMENTS`: its prose, its
figure caption, its table cells and its pitfalls card. The Abstract is
frozen: if it is named, say so and stop.

## Procedure

1. Read the chapter, and the sentences just before and after it, so that you
   know what the reader already has in mind.
2. If the author pasted the output of `build_paper.py --stats`, start with
   the sentences it lists for this chapter: those over 25 words, empty
   openers and stacked hedges. They are hints, not verdicts.
3. Read each paragraph sentence by sentence and check:
   - **Actor as subject.** Claude, Claude Code, the hook, you: who acts is
     the subject, and the action is the verb, not a noun ending in *-tion*
     or *-ment*.
   - **Verb early.** Subject and verb stand close together. An aside of six
     words or more between them belongs elsewhere.
   - **Known first, new last.** A sentence starts with what the previous one
     left in mind and ends on its new or important word. Read only the last
     words of each sentence: they should carry the paragraph.
   - **Empty openers.** "It is", "There are" and a bare "This" or "That" go,
     unless they put the point at the end of the sentence.
   - **Links.** Where ", and" joins a cause and its effect, or a contrast,
     *so*, *because* or *but* says it.
   - **Hedges.** One per claim, and only where the facts need it. A hedge the
     source requires stays.
   - **Citations.** Each number stands where the clause it supports ends.
   - **Length.** About 15 words on average, rarely over 25, and not choppy.
4. Propose only what clearly improves a sentence. A sentence that already
   works stays as it is.

## Report

A numbered list, one finding per line, in this form:

`"quoted words" — rule — proposed wording`

End with one line: how many findings, and whether the chapter would grow or
shrink. Every chapter keeps to its page (CLAUDE.md, section 10).

## Rules

- Report, do not repair. You have no tool to edit, and you never ask for one.
- Never change a fact, a number, a date, a quote or a citation number, and
  never move a citation to a clause its source does not support.
- Keep the terms the paper defines ("front matter", "token") and British
  spelling. Advice stays in the imperative and speaks to *you*.
