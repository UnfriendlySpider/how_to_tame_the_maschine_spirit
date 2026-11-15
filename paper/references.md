# References

<!--
  The ONLY copy of the reference list. tools/build_paper.py reads this file
  and renders it where paper.md has its `::: references` fence.
  Rules (see CLAUDE.md, Accuracy rules):
  - Every entry must be retrievable.
  - Every entry carries an access date.
  - Never invent a citation. Add entries with /add-reference.
  - Every entry must be cited from the prose as [n]; the build fails on an
    entry that is never cited and on a citation that has no entry.
  - Numbers follow the order of first citation in paper.md: [1] is the
    first source the paper cites, and the list has no gaps (the author's
    request, 2026-10-26). The build fails when they do not;
    `uv run python tools/build_paper.py --renumber` puts them in order in
    paper.md, this file and further-reading.md. A new entry takes the next
    free number, and --renumber moves it into place. Until 2026-10-26 the
    numbers were stable identifiers with gaps; the notes below name them in
    the numbering of their day.
  Layout: the text before the first `## Group` heading is the lead-in
  paragraph of the References section. Each group holds entries in the
  format below, in ascending order. The groups sort the sources by kind for
  whoever edits this file; the rendered list follows the numbers alone, in
  two columns. A group whose entries share one organisation and one URL
  prefix, the documentation, states its prefix once in the lead-in and shows
  each page by name, and pages of one group cited one after another share an
  entry. The access date most entries share is stated once, in the lead-in
  (the build warns when the lead-in does not name it); an entry read on
  another day shows its own date. A note says what kind of source it is and
  when it appeared: preprint or venue, blog post or report, and the year.
  Format: [n] Author/Org. "Title" (optional note). URL (accessed YYYY-MM-DD).
  Note: the documentation moved from docs.claude.com to code.claude.com in
  2026; the old URLs redirect. Cite the new host.
  On 2026-10-08 every entry was read again and every citing sentence checked
  against it, studies against their full text. Twenty entries left the list
  that day: [1], [5], [7], [12], [15], [18], [21], [24] and [29], whose claims
  other cited pages carry, and [32], [36], [38], [43], [45], [48], [51], [53],
  [54], [57] and [60], which paper/further-reading.md keeps with the reason.
  Fortune refuses requests without a browser user agent; the page opens in a
  browser. Re-check before submission: [2] changes often, [62] is interim
  advice that formal guidance will replace, and [69] to [71] (model
  retirements, regions, prices) change without notice.
  Later on 2026-10-08 chapter 10 (Data protection) brought [66] to [72],
  each read that day before it entered; the Claude Platform pages became a
  group of their own so they render as a compact list. To keep the list on
  one page, [55], [63] and [64] left it; paper/further-reading.md keeps
  them with the reason.
  On 2026-10-26 every entry was read again and every citing sentence
  checked against it, after the paper's review of that day; Claude Code
  statements were checked against the documentation of 2.1.310. [28]
  moved from /engineering/ to /research/ (the old URL redirects), [59]
  appeared at ICLR 2026, and [47] at NeurIPS 2026 in a revised form whose
  figures differ from version 4, so the entry keeps pinning version 4.
  Like Fortune, the Dutch DPA [66] refuses requests without a browser user
  agent, EUR-Lex [68] answers scripts with an empty bot challenge (HTTP 202;
  the same text is at publications.europa.eu/resource/celex/32016R0679)
  and X [56] refuses WebFetch but serves curl; all open in a browser.
  On 2026-10-27 the Conclusion's outlook brought [47] Phoronix, [48] MIT
  Technology Review and [49] OpenCode, each read that day, so each shows
  its date and the lead-in says that undated sources were read on 26
  October; the documentation's version left the lead-in for space (the
  Introduction names it). DORA and the Super Intelligence order, [48] and
  [52] that morning, left the list; paper/further-reading.md keeps both.
  That evening Cherny's thread ([50] that afternoon) left too, when the
  Conclusion was cut to say each thing once; further-reading.md keeps it.
  Later that evening [3] became the 2025 talk's slides (PRE_ML04.pdf, read
  that day) in place of the 2025 paper, and [50] mobiFlip came in for the
  Mac Studio's price. Vals AI's SWE-bench Verified leaderboard was read
  that day too but left out for space (CLAUDE.md, section 7).
  Last that night the Conclusion compared DeepSeek V4 Flash with last
  year's Claude Opus 4.5: Vals AI's leaderboard, Anthropic's Opus 4.5 page,
  Rapid-MLX (memory) and Context Studios (price) came in, all read that
  day, and Hugging Face's DeepSeek page replaced MIT Technology Review;
  mobiFlip and Stack Overflow's survey left. For room, the 2025 talk and
  Context Studios show their main titles only, and Rapid-MLX's title drops
  "— MLX Quants & Benchmarks".
  On 2026-10-28, in the final check before submission, every entry was
  read again against each citing sentence (review/2026-10-28-final-check.md).
  Two sources had changed since 26 October: the best-practices page [9] was
  rewritten on 27 October, and arXiv posted version 2 of SWE-Skills-Bench
  [15] that day; chapters 2 and 3 now say what the current versions carry.
  Since every entry was read that day, all carry the access date
  2026-10-28 and the lead-in says so once; [8] names version 2.1.312 of
  27 October, the newest release, whose changes and 2.1.311's touch no
  claim of the paper.
  On 2026-10-29, at the author's requests, four sources came in, each read
  that day and showing its own date: the prompt-caching page [29] (chapter
  6), Basic Memory's README [32] (chapter 7), OpenCode's "Migrate from V1"
  [55] and TechCrunch's report on OpenAI and two mathematicians [56] (the
  Conclusion). The lead-in now says that sources without an access date
  were read on 28 October. For room, [11], [12], [13], [15], [16], [17],
  [27] and [39] give only their main title, the part before the colon.
-->

Sources without an access date were read on 28 October 2026. More studies,
for and against, are available on request.

## Claude Code docs

[5] Anthropic. "Choose a sandbox environment" (sandbox options compared). https://code.claude.com/docs/en/sandbox-environments (accessed 2026-10-28).
[6] Anthropic. "Data usage". https://code.claude.com/docs/en/data-usage (accessed 2026-10-28).
[7] Anthropic. "How Claude remembers your project" (CLAUDE.md files and auto memory). https://code.claude.com/docs/en/memory (accessed 2026-10-28).
[8] Anthropic. "Claude Code changelog" (version 2.1.312 of 27 October 2026). https://code.claude.com/docs/en/changelog (accessed 2026-10-28).
[9] Anthropic. "Explore the context window". https://code.claude.com/docs/en/context-window (accessed 2026-10-28).
[10] Anthropic. "Best practices for Claude Code". https://code.claude.com/docs/en/best-practices (accessed 2026-10-28).
[14] Anthropic. "Extend Claude with skills". https://code.claude.com/docs/en/skills (accessed 2026-10-28).
[18] Anthropic. "Configure permissions". https://code.claude.com/docs/en/permissions (accessed 2026-10-28).
[19] Anthropic. "Configure the sandboxed Bash tool". https://code.claude.com/docs/en/sandboxing (accessed 2026-10-28).
[20] Anthropic. "Hooks reference". https://code.claude.com/docs/en/hooks (accessed 2026-10-28).
[21] Anthropic. "Choose a permission mode" (Manual and auto mode). https://code.claude.com/docs/en/permission-modes (accessed 2026-10-28).
[24] Anthropic. "Create custom subagents". https://code.claude.com/docs/en/sub-agents (accessed 2026-10-28).
[28] Anthropic. "Manage costs effectively". https://code.claude.com/docs/en/costs (accessed 2026-10-28).
[29] Anthropic. "How Claude Code uses prompt caching". https://code.claude.com/docs/en/prompt-caching (accessed 2026-10-29).
[30] Anthropic. "Commands" (built-in slash commands). https://code.claude.com/docs/en/commands (accessed 2026-10-28).
[31] Anthropic. "Configure cloud environments" (network access, GitHub proxy). https://code.claude.com/docs/en/cloud-environments (accessed 2026-10-28).
[36] Anthropic. "Security" (prompt injection, workspace trust, untrusted content). https://code.claude.com/docs/en/security (accessed 2026-10-28).
[37] Anthropic. "Use Claude Code in the cloud" (claude.ai/code). https://code.claude.com/docs/en/claude-code-on-the-web (accessed 2026-10-28).
[46] Anthropic. "Other LLM gateways". https://code.claude.com/docs/en/llm-gateway (accessed 2026-10-28).

## Claude Platform docs

[26] Anthropic. "Glossary" (entry Tokens). https://platform.claude.com/docs/en/about-claude/glossary#tokens (accessed 2026-10-28).
[44] Anthropic. "Model deprecations". https://platform.claude.com/docs/en/about-claude/model-deprecations (accessed 2026-10-28).
[47] Anthropic. "Data residency". https://platform.claude.com/docs/en/manage-claude/data-residency (accessed 2026-10-28).
[52] Anthropic. "Claude Opus 4.5" (model page, released 24 November 2025). https://platform.claude.com/docs/en/models/opus-4-5/overview (accessed 2026-10-28).

## Other documentation

[32] Basic Machines. "Basic Memory" (project README, 2026). https://github.com/basicmachines-co/basic-memory (accessed 2026-10-29).
[35] GitHub. "Managing your personal access tokens" (classic and fine-grained tokens). https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens (accessed 2026-10-28).
[43] Anthropic. "Plans & pricing". https://claude.com/pricing (accessed 2026-10-28).
[49] OpenCode. "The open source AI coding agent" (project website). https://opencode.ai/ (accessed 2026-10-28).
[53] Rapid-MLX. "DeepSeek V4-Flash on Apple Silicon" (documentation, 2026). https://rapidmlx.com/docs/models/deepseek-v4-flash (accessed 2026-10-28).
[55] OpenCode. "Migrate from V1" (documentation, 2026). https://opencode.ai/v2/docs/migrate-v1 (accessed 2026-10-29).

## Studies and surveys

[11] Gloaguen et al. "Evaluating AGENTS.md" (preprint, 2026). https://arxiv.org/abs/2602.11988 (accessed 2026-10-28).
[12] McMillan. "Instruction Adherence in Coding Agent Configuration Files" (preprint, 2026). https://arxiv.org/abs/2605.10039 (accessed 2026-10-28).
[13] Denisov-Blanch et al. "A Few Pages of Markdown" (ASE 2026). https://arxiv.org/abs/2608.25241 (accessed 2026-10-28).
[15] Zhong, Raghunathan, Carlini. "ImpossibleBench" (ICLR 2026). https://arxiv.org/abs/2510.20270 (accessed 2026-10-28).
[16] Han et al. "SWE-Skills-Bench" (preprint, 2026, version 2). https://arxiv.org/abs/2603.15401v2 (accessed 2026-10-28).
[17] Li et al. "SkillsBench" (preprint, 2026, version 4). https://arxiv.org/abs/2602.12670v4 (accessed 2026-10-28).
[23] Huang et al. "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2024). https://arxiv.org/abs/2310.01798 (accessed 2026-10-28).
[25] Kim et al. "Correlated Errors in Large Language Models" (ICML 2025). https://arxiv.org/abs/2506.07962 (accessed 2026-10-28).
[51] Vals AI. "SWE-bench Verified Leaderboard and Methodology" (leaderboard, 2026). https://www.vals.ai/benchmarks/swebench (accessed 2026-10-28).

## Reports, incidents and posts

[1] San Francisco Standard (Zara Stone). "She runs AI safety at Meta. Her AI agent still went rogue" (news report, 2026). https://sfstandard.com/2026/02/25/openclaw-goes-rogue/ (accessed 2026-10-28).
[2] Decrypt (Jason Nelson). "AI Agent Deletes Startup’s Database in 9 Seconds, Founder Says" (news report, 2026). https://decrypt.co/365897/ai-agent-deletes-startup-database-9-seconds-founder-says (accessed 2026-10-28).
[3] Fortune (Beatrice Nolan). "An AI-powered coding tool wiped out a software company's database, then apologized for a 'catastrophic failure on my part'" (2025). https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ (accessed 2026-10-28).
[4] Josua Böser. "Neither Magic Wand Nor Terminator" (PHUSE EU Connect 2025, talk ML04). https://phuse.s3.eu-central-1.amazonaws.com/Archive/2025/Connect/EU/Hamburg/PRE_ML04.pdf (accessed 2026-10-28).
[22] Anthropic (John Hughes). "How we built Claude Code auto mode: a safer way to skip permissions" (engineering blog, 2026). https://www.anthropic.com/research/claude-code-auto-mode (accessed 2026-10-28).
[27] Chroma (Hong, Troynikov, Huber). "Context Rot" (technical report, 2025). https://www.trychroma.com/research/context-rot (accessed 2026-10-28).
[33] Cisco (Idan Habler, Amy Chang). "Identifying and remediating a persistent memory compromise in Claude Code" (blog post, 2026). https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code (accessed 2026-10-28).
[38] Simon Willison. "The lethal trifecta for AI agents: private data, untrusted content, and external communication" (blog post, 2025). https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ (accessed 2026-10-28).
[39] Wiz (Rami McCarthy). "s1ngularity's Aftermath" (blog post, 2025). https://www.wiz.io/blog/s1ngularitys-aftermath (accessed 2026-10-28).
[40] BleepingComputer (Lawrence Abrams). "Laravel Lang packages hijacked to deploy credential-stealing malware" (news report, 2026). https://www.bleepingcomputer.com/news/security/laravel-lang-packages-hijacked-to-deploy-credential-stealing-malware/ (accessed 2026-10-28).
[48] Phoronix (Michael Larabel). "AI Makes 'Open-Source, Clean Room' Implementations Of Adobe Photoshop & Premier In Rust" (news report, 2026). https://www.phoronix.com/news/Photocraft-Filmcraft-AI (accessed 2026-10-28).
[50] DeepSeek. "deepseek-ai" (Hugging Face page). https://huggingface.co/deepseek-ai (accessed 2026-10-28).
[54] Context Studios (Michael Kerkhoff). "Mac Studio M5 Ultra for Local AI" (blog post, 2026). https://www.contextstudios.ai/blog/mac-studio-m5-ultra-local-ai-guide (accessed 2026-10-28).
[56] TechCrunch (Russell Brandom). "OpenAI fought dirty on career-making math problem, says NYU mathematician" (news report, 2026). https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/ (accessed 2026-10-29).

## Law and guidance from public bodies

[34] UK National Cyber Security Centre. "Managing the cyber risk of agentic AI" (interim advice, 2026). https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai (accessed 2026-10-28).
[41] Dutch Data Protection Authority. "Caution: use of AI chatbot may lead to data breaches" (2024). https://www.autoriteitpersoonsgegevens.nl/en/current/caution-use-of-ai-chatbot-may-lead-to-data-breaches (accessed 2026-10-28).
[42] European Union. "Regulation (EU) 2016/679" (GDPR, 2016). https://eur-lex.europa.eu/eli/reg/2016/679/oj (accessed 2026-10-28).
[45] ANSSI and BSI. "AI Coding Assistants" (recommendations, 2024). https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/ANSSI_BSI_AI_Coding_Assistants.pdf?__blob=publicationFile&v=7 (accessed 2026-10-28).
[57] EMA and FDA. "Guiding principles of good AI practice in drug development" (2026). https://www.ema.europa.eu/en/documents/other/guiding-principles-good-ai-practice-drug-development_en.pdf (accessed 2026-10-28).
