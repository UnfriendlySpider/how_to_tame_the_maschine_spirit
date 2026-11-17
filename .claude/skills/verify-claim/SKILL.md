---
name: verify-claim
description: Check a claim about a Claude Code feature (hooks, skills, settings, subagents, memory, context, slash commands) against the official documentation before it goes into the paper. Use whenever a sentence asserts what Claude Code does or supports.
argument-hint: "[the claim in one sentence]"
allowed-tools: WebFetch(domain:code.claude.com)
disallowed-tools: Edit Write NotebookEdit Bash PowerShell Monitor Agent
---

# Verify a feature claim

The claim to check: `$ARGUMENTS`

The costliest failure of this paper is asserting a feature that does not exist.
So:

1. Pick the documentation page that would settle the claim. Pages live at
   `https://code.claude.com/docs/en/<page>`; the index is at
   `https://code.claude.com/docs/llms.txt`. Typical pages: `hooks`,
   `hooks-guide`, `settings`, `permissions`, `skills`, `sub-agents`, `memory`,
   `context-window`, `commands`.
2. Fetch the page and quote the sentence or table row that confirms or refutes
   the claim. If nothing on the page settles it, say so and try one more page.
3. Answer with exactly one of: **Confirmed**, **Refuted**, **Not documented**.
   Add the quote, the URL and today's date in the form the references file
   uses: `Anthropic. "Page title". URL (accessed YYYY-MM-DD).`
4. If the claim is refuted, propose the corrected sentence.

Never confirm from memory. If the fetch fails, report the failure instead of
guessing.
