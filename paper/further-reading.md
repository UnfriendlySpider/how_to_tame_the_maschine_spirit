# Further reading: the evidence for and against

<!--
  NOT the reference list. The build never reads this file; paper/references.md
  stays the only copy of the paper's references. A source moves from here into
  the paper only through /add-reference, after the cited page has been read.
  Status per entry:
    checked YYYY-MM-DD  the source was read on that date and the note quotes it
    to check            listed from a search; not yet read in full here, so the
                        note says what the source asks, not what it found
  An entry cited in the paper carries its reference number, for example [33];
  `tools/build_paper.py --renumber` keeps these numbers in step with the
  paper's.
  An entry that left the paper says when and why in its check note; on
  2026-10-08 eleven did, after every source was read again against the
  sentences that cited it, and three more that evening, to make room for
  chapter 10.
-->

The paper explains how to use each mechanism. This list collects what has been
measured about them, including the studies that find little or no benefit, so
that you can weigh the mechanisms rather than take them on trust. Most studies
measure whether an agent solves more benchmark tasks; the paper's mechanisms
aim mainly at control: whether the assistant keeps your rules, and what it
cannot do at all. Keep that difference in mind when a study reports no gain.
Two more cautions. Most entries from 2026 are preprints that have not yet been
peer reviewed. And several are observational: they show what goes together,
not what causes what. Status as of October 2026.

## Does any of it pay off?

- Google Cloud (DORA). "Announcing the 2025 DORA Report: State of AI-Assisted
  Software Development". September 2025.
  https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
  (checked 2026-10-06; it left the paper on 2026-10-27, when the Conclusion
  made room for the author's view of open models and prices; the talk's 8.2
  still quotes it). AI adoption now goes with higher delivery
  throughput but still with lower stability: "AI doesn't fix a team; it
  amplifies what's already there", and "Without robust control systems [...]
  an increase in change volume leads to instability." Supports the paper's
  premise that the surroundings decide.
- METR. "Measuring the Impact of Early-2025 AI on Experienced Open-Source
  Developer Productivity". July 2025.
  https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  (checked 2026-10-06; read again 2026-10-08, when it left the paper with the
  Conclusion's paragraph on speed, which was off the paper's subject). A
  randomised trial with 16 experienced
  developers and 246 issues from their own projects: "when developers are
  allowed to use AI tools, they take 19% longer to complete issues". They had
  expected a 24% speed-up and afterwards still believed AI had sped them up
  by 20%. The authors warn against reading it as evidence about other
  developers, settings or later tools. Read again 2026-10-08: the page now
  carries a banner, "These results are out of date", and says the
  historical results "no longer reflect the current impact of AI models on
  open-source developer productivity" (still there on 2026-10-28).
- METR. "We are Changing our Developer Productivity Experiment Design".
  February 2026. https://metr.org/blog/2026-02-24-uplift-update/ (checked
  2026-10-06). A second trial from August 2025, 57 developers and over 800
  tasks: an estimated 18% less time with AI for the returning developers
  (confidence interval from 38% less to 9% more) and 4% less for new ones.
  METR calls the data "an unreliable signal": 30 to 50% of developers held
  back tasks they did not want to do without AI, so the gain is probably
  underestimated, and the design is being changed.
- Murphy-Hill, Butler, Savelieva. "Adoption and Impact of Command-Line AI
  Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and
  GitHub Copilot CLI". July 2026. https://arxiv.org/abs/2607.01418 (checked
  2026-10-06; read again 2026-10-08, when it left the paper with the
  paragraph on speed). Tens of thousands of engineers: "adopters merged roughly
  24% more pull requests than they would have otherwise", a lift that held
  over four months, with the caveat that "a merged PR is not the same as the
  value it delivers". The 24% pools both tools; weeks with Claude Code alone
  gave about 11.4%, and the authors are Microsoft employees.
- Agarwal, He, Vasilescu (Carnegie Mellon). "AI IDEs or Autonomous Agents?
  Measuring the Impact of Coding Agents on Software Development". January
  2026. https://arxiv.org/abs/2601.13597 (checked 2026-10-06). A causal
  panel study of open-source repositories: large, front-loaded velocity gains
  only where an agent was the first AI tool, while "static-analysis warnings
  and cognitive complexity rising by roughly 18% and 39%" persisted even
  after the velocity gain faded.
- Baumann et al. "SWE-chat: Coding Agent Interactions From Real Users in the
  Wild". COLM 2026. https://arxiv.org/abs/2604.20779 (checked 2026-10-06).
  Almost 18,000 real sessions from public repositories: "Only 59% of all
  agent-produced code survives into user commits", agent-written code
  introduces more security vulnerabilities than human-written code, and
  users push back on the agent "in 50% of all turns".
- Stack Overflow. 2025 Developer Survey, section on AI.
  https://survey.stackoverflow.co/2025/ai (checked 2026-10-06; read again
  2026-10-08; 49,009 responses in all, about 33,700 to the AI questions,
  fielded May to June 2025; it left the paper on 2026-10-26 for the 2026
  edition below). 84% use or
  plan to use AI tools; 46% distrust the accuracy of their output against
  33% who trust it; the top frustration, named by 66%, is "AI solutions that
  are almost right, but not quite".
- Stack Overflow. 2026 Developer Survey, AI data.
  https://survey.stackoverflow.co/2026/ai/data (checked 2026-10-26; results
  published 6 October 2026, fielded 23 June to 5 August 2026, 30,903 valid
  responses, about 14,300 to the trust question; it left the paper on
  2026-10-27, when the Introduction took another opening). "Trust is
  conditional: 48% trust AI when they can easily verify it, while only 7%
  trust it with important decisions." A self-selected sample of Stack
  Overflow's audience. Its use question asks about current use at work and
  has no "planning to" option, so its 83% cannot be set against 2025's 84%,
  and it has no counterpart to the 66% "almost right" frustration.
- Anthropic. "How AI assistance impacts the formation of coding skills".
  January 2026. https://www.anthropic.com/research/AI-assistance-coding-skills
  (checked 2026-10-06). A randomised trial with 52 mostly junior engineers
  learning a new Python library: the AI group scored 50% on the quiz
  afterwards against 67%, with the largest gap in debugging, the skill a
  review needs. Those who asked for explanations kept more.
- Balepur et al. "(Im)Paired Programming: Coding Agents Improve Productivity
  but Harm Understanding". July 2026. https://arxiv.org/abs/2607.26375
  (checked 2026-10-06). 54 students: agents "aid initial task completion"
  but "harm users' code comprehension"; copy-and-paste prompts and
  auto-accepted edits go with the lowest comprehension.
- Anthropic. "How AI is transforming work at Anthropic". December 2025.
  https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
  (checked 2026-10-06). A survey of 132 engineers and 53 interviews: Claude in
  59% of their work and a self-reported 50% productivity gain, alongside the
  worry that the skills needed to supervise the assistant fade with use.

## Ground rules: do context files help? (chapter 2)

- Decrypt (Jason Nelson). "AI Agent Deletes Startup's Database in 9
  Seconds, Founder Says". 28 April 2026.
  https://decrypt.co/365897/ai-agent-deletes-startup-database-9-seconds-founder-says
  (checked 2026-10-26) [2]. PocketOS's founder, Jeremy Crane: a Cursor agent
  running Claude Opus 4.6 hit a credential mismatch in staging and "deleted
  our production database and all volume-level backups in a single API call
  to Railway"; "It took 9 seconds." Afterwards the agent quoted an all-caps
  instruction never to guess, which it had disobeyed: "I guessed that
  deleting a staging volume via the API would be scoped to staging only. I
  didn't verify." The details are the founder's account; the article does
  not say whether the rule came from Cursor's system prompt or the
  company's own rules. Railway's co-founder says the data was recovered,
  while the founder reports gaps. Cited in chapter 2 as written advice that
  nothing enforced (the author's choice of 2026-10-26).

- Gloaguen, Mündler-Sasahara, Müller, Raychev, Vechev (ETH Zurich).
  "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for
  Coding Agents?". February 2026, revised September 2026.
  https://arxiv.org/abs/2602.11988 (checked 2026-10-06; version 3 read again
  2026-10-08) [11]. Context files, generated or written by developers, do
  "not generally improve task success rates, while increasing inference cost
  by over 20% on average". In the body, the 20% and 23% hold for files a
  model wrote; files written by developers cost 19% more on average (the
  text says "at most", but Table 2 gives Claude Code about 13% and Codex with
  GPT-5.2 about 42%), so the paper says "about 20%". The cited wording first appears
  in version 2; version 1 said context files reduce success. The
  instructions in them "are well followed", but repository overviews "are not
  helpful"; the files are "useful for specifying non-standard coding
  practices".
- McMillan (HxAI Australia). "Instruction Adherence in Coding Agent
  Configuration Files: A Factorial Study of Four File-Structure Variables".
  May 2026. https://arxiv.org/abs/2605.10039 (checked 2026-10-06) [12].
  1,650 Claude Code sessions with a deliberately trivial rule: file size from
  25 to 500 lines, the rule's position, splitting into several files and a
  contradicting file made no detectable difference. The largest effect was
  within the session: "each additional function the agent generates [...] is
  associated with approximately 5.6% lower odds of compliance". The authors
  advise hooks that re-surface the rule, and linters and CI checks after the
  fact. In tension with the documentation's advice to stay under 200 lines,
  which the paper reports as advice.
- Denisov-Blanch, Agarwal, Azaletskiy, He, Schaeffer, Miranda, Vasilescu,
  Koyejo (Stanford, Carnegie Mellon and others). "A Few Pages of Markdown:
  Committed AI Configuration and Lower Quality Cost after Coding-Agent
  Adoption". August 2026, revised September 2026; accepted at ASE 2026
  (DOI 10.1145/3832783.3837546).
  https://arxiv.org/abs/2608.25241 (checked 2026-10-06; read again
  2026-10-08) [13]. Re-analyses
  the panel of Agarwal et al. by how much AI configuration a repository
  commits. Agents raised commits by 28 to 38% whatever the configuration, but
  among repositories whose first AI tool was an agent, "those without
  committed AI configuration show roughly twice the increase in cognitive
  complexity (+53% versus +27%) and 1.7x the increase in static-analysis
  warnings". Also: "73.8% of artifacts are committed once and never
  modified". The authors call the result "hypothesis-generating": disciplined
  teams may simply write both better code and more configuration. Probably
  the new study most relevant to the paper.
- Galster, Mohsenimofidi, Lulla, Abubakar, Treude, Baltes. "Harness
  Engineering for Agentic AI Coding Tools: An Exploratory Study". February
  2026. https://arxiv.org/abs/2602.14690 (checked 2026-10-06; full text read
  2026-10-08, when it left the paper: it set the scene but carried no
  advice; a peer-reviewed short version appeared at AIware 2026). 2,853
  GitHub repositories with at least one
  configuration artifact: context files dominate and are often the only
  mechanism, "few repositories adopt advanced mechanisms such as Skills and
  Subagents", and Claude Code users employ the broadest range. The full text
  counts "601 Skills in 158 repositories" and "450 Subagents across 131
  repositories"; CLAUDE.md is the most common context file (1,640 files).
- Anthropic. "Best practices for Claude Code".
  https://code.claude.com/docs/en/best-practices (checked 2026-10-06; read
  again 2026-10-28, after the page was rewritten on 27 October) [10].
  CLAUDE.md loads into every session, "which means every line in it takes a
  little of Claude's attention on *every* task, whether it's relevant or
  not". Its test before anything goes into the file: "Could it find this by
  reading the code?" and "Would it actually go and look?"; "If both are yes,
  leave it out." The earlier version's "Treat CLAUDE.md like code" and its
  test, whether removing a line would cause a mistake, are gone.

## Skills: do they help? (chapter 3)

- Han et al. "SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World
  Software Engineering?". March 2026, revised October 2026.
  https://arxiv.org/abs/2603.15401 (checked 2026-10-06; read again
  2026-10-08; version 2 of 27 October 2026, abstract and section 4, read
  2026-10-28) [16]. Version 2: 98 public skills, ten requirements each,
  under four agent–model configurations (Codex with GPT-5.4-mini or
  Kimi-K2.6, Claude Code with Kimi-K2.6 or Haiku 4.5), 3,920 paired runs:
  "92 of 98 skills have no statistically significant effect, and adding
  skills raises the average pass ratio only from 76.6% to 76.9%". Four
  skills help, by up to 17.7 points, by supplying "procedures that the agent
  would otherwise omit"; two hurt, by up to 17.0 points, when their
  templates "override the task's explicit instructions". The unchanged
  outcomes "are not explained solely by ceiling effects", and the effect
  depends on the configuration: with Kimi-K2.6 in both, 40 of the 98 skills
  change sign between Codex and Claude Code. Caveats from the full text:
  each task runs once with and once without the skill, the skill is invoked
  explicitly at the start of the prompt, and "Ineffective means that no
  directional effect was detected with ten requirements, not that the
  effect is zero". Version 1 (March 2026, 49 skills, Claude Code with Haiku
  4.5 only) had reported "39 of 49 skills yield zero pass-rate improvement".
- Li et al. "SkillsBench: Benchmarking How Well Agent Skills Work Across
  Diverse Tasks". February 2026, revised June 2026.
  https://arxiv.org/abs/2602.12670 (checked 2026-10-06; v4 read again
  2026-10-08) [17]. 87 tasks in eight
  domains: "Curated Skills raise the average pass rate from 33.9% to 50.5%",
  and focused skills with at most three modules beat large bundles. The
  positive counterpart to SWE-Skills-Bench. Accepted at NeurIPS 2026 in a
  revised form (84 tasks, 7 configurations, +16.4 points; seen 2026-10-26),
  whose abstract no longer gives 33.9% and 50.5%, so the paper keeps citing
  version 4.
- Hu, Jiang, Liang, Dey, Wu, Tan. "Analyzing and Mitigating Cost-Inefficient
  Behaviors in Coding Agents". September 2026.
  https://arxiv.org/abs/2609.30725 (checked 2026-10-06). On Claude Code and
  Mini-SWE-Agent, "developer-designed skills [...] reducing cost by up to
  41.73%, roughly twice the maximum gain from agent-synthesized skills".
  Repeated searches, near-identical scripts and test re-runs affect 79 to 98%
  of tasks and up to 22.75% of their cost.
- Vercel (Jude Gao). "AGENTS.md outperforms skills in our agent evals".
  January 2026.
  https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
  (checked 2026-10-06; read again 2026-10-08, when it left the paper: the
  post names neither agent nor model, and Vercel promotes its own AGENTS.md
  tooling). In 56% of cases the
  agent never invoked the skill on its own; skills reached 79% only with
  explicit instructions, a compressed docs index in AGENTS.md 100%. Supports
  calling an important skill by name. The evals target Next.js 16 and name
  no agent.
- Tank, Nama. "The Regression Tax: Decomposing Why Skills Help and Hurt LLM
  Agents". July 2026. https://arxiv.org/abs/2607.22520 (checked 2026-10-06).
  Nearly 6,000 runs: the best skills win "primarily by regressing less, not
  by gaining more". A skill changes behaviour "simply by being present in
  context, even when it is never invoked", and a prescribed procedure can
  suppress checks the agent would otherwise make.
- Dong, Gao, Li, Xu, Hua, Yang. "Agent Skills Can Be Harmful: An Empirical
  Study of Skill-Induced Failures in LLM Agents". August 2026.
  https://arxiv.org/abs/2608.11888 (checked 2026-10-06). 307 skill-induced
  failures on SkillsBench and SWE-Skills-Bench; they "are rarely caused by
  obviously irrelevant skills", but by "seemingly relevant skills".
- Jiang et al. "Demystifying Agent Skills: Why They Work-Until They Don't".
  August 2026. https://arxiv.org/abs/2608.14036 (checked 2026-10-06). Skills
  work as "procedural anchors" (65.7% of cases) rather than by adding facts
  (4.5%); as the pool grows from 5 to 100 skills, the precision of picking
  the right one falls from 29.6% to 3.3%.
- Huang et al. "From Raw Experience to Skill Consumption: A Systematic Study
  of Model-Generated Agent Skills". May 2026.
  https://arxiv.org/abs/2605.23899 (checked 2026-10-06). Skills written by a
  model "are beneficial on average but exhibit non-trivial negative
  transfer".
- Liu et al. "Agent Skills in the Wild: An Empirical Study of Security
  Vulnerabilities at Scale". January 2026. https://arxiv.org/abs/2601.10338
  (checked 2026-10-06; read again 2026-10-08). 31,132 of 42,447 skills
  collected from two marketplaces: 26.1% with at least one vulnerability,
  13.3% with data-exfiltration patterns. The "2.12x" for skills with scripts
  is an odds ratio; the rates are 40.6% with scripts and 24.2% without. The
  authors read the findings as "patterns warranting review" rather than
  "confirmed malicious skills".
- Zhong, Raghunathan, Carlini. "ImpossibleBench: Measuring LLMs' Propensity
  of Exploiting Test Cases". October 2025; ICLR 2026.
  https://arxiv.org/abs/2510.20270 (checked 2026-10-08; venue seen
  2026-10-26) [15]. "An LLM agent with access to unit tests may
  delete failing tests rather than fix the underlying bug"; the benchmark
  measures a "cheating rate" on tasks whose tests contradict their
  specification. The paper cites it for the review skill's first rule,
  report, do not repair, and dates it to 2025: an audit posted on 12 October
  2026 (Mendelsohn, "Good Evals Are Hard: An ImpossibleBench Audit", a blog
  post, not peer-reviewed;
  https://www.lesswrong.com/posts/qnrjAhiqire7JeoN2/good-evals-are-hard-an-impossiblebench-audit,
  read 2026-10-26) re-ran the LiveCodeBench half on October 2026 models: the
  Claude and GPT models it tested "almost never cheated", two Gemini models
  "~15-20% of the time". It found defects in 13 of the 103 tasks.
- Anthropic. "Test plugins with evals".
  https://code.claude.com/docs/en/plugin-evals (checked 2026-10-06; left the
  paper on 2026-10-08, since other cited pages carry its claim). "If
  a case scores 1.0 both with and without the plugin, the plugin isn't what
  made it pass." Each case runs three times with and without the plugin.

## Guardrails: prompts, classifiers and hooks (chapter 4)

- Anthropic (John Hughes). "How we built Claude Code auto mode: a safer way to skip
  permissions". March 2026.
  https://www.anthropic.com/research/claude-code-auto-mode (checked
  2026-10-06; moved from /engineering/ by 2026-10-26, figures unchanged)
  [22]. "Manual prompts sit in the middle, and in practice users accept 93%
  of them anyway" (the page's summary says "Claude Code users approve 93% of
  permission prompts"; checked 2026-10-29). The
  classifier missed 17% of 52 real overeager actions and flagged 0.4% of
  10,000 ordinary ones; "it is not a drop-in replacement for careful human
  review on high-stakes infrastructure." Against prompt injection, a probe
  warns when a tool result "looks like an injection attempt", and the
  classifier never sees tool results.
- Anthropic. "Choose a permission mode".
  https://code.claude.com/docs/en/permission-modes (checked 2026-10-06; read
  again 2026-10-28) [21]. Auto mode is the starting mode of interactive
  terminal and VS Code sessions; edits inside the working directory,
  protected paths aside, skip the classifier; "Auto mode reduces
  permission prompts but does not guarantee safety"; a boundary stated only
  in the conversation can be lost
  at compaction, so "for a hard guarantee, add a deny rule instead";
  "`bypassPermissions` offers no protection against prompt injection or
  unintended actions."
- Anthropic. "Beyond permission prompts: making Claude Code more secure and
  autonomous". October 2025.
  https://www.anthropic.com/research/claude-code-sandboxing (checked
  2026-10-06; read again 2026-10-08, when it left the paper: parts are out
  of date, such as read-only as the default mode and a git proxy that pushes
  only to one branch; moved from /engineering/ by 2026-10-28, figures
  unchanged). Names "approval fatigue"; the sandbox cut permission prompts by
  84% in Anthropic's own use, and needs both filesystem and network
  isolation.
- Jing. "Separation of Duties for Privileged LLM Agents: A Governed Execution
  Architecture with Measured Security-Utility Trade-offs". September 2026.
  https://arxiv.org/abs/2609.38224 (checked 2026-10-06). Separate planner,
  policy gate, executor and auditor: "Effective attack success falls from
  98.3% under direct execution to 7.7% deployed", at a false-denial rate of
  11.1%. The last step, "from 30.8% to 7.7%", is "attributable to the
  operating-system sandbox". Supports enforcing outside the model.
- Docker. "Coding Agent Horror Stories: The rm -rf ~/ Incident". June 2026.
  https://www.docker.com/blog/coding-agent-horror-stories-the-rm-rf-incident/
  (checked 2026-10-06; read again 2026-10-08). Claude Code ran
  `rm -rf tests/ patches/ plan/ ~/` and deleted a user's home directory, as
  a Reddit user reported on 8 December 2025. A vendor's secondary account
  that promotes Docker Sandboxes; it does not say whether the user had
  switched the permission prompts off. Not cited in the paper for that
  reason.
- Fortune (Beatrice Nolan). "An AI-powered coding tool wiped out a software
  company's database, then apologized for a 'catastrophic failure on my
  part'". July 2025.
  https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/
  (checked 2026-10-06; read again 2026-10-08, Fortune refuses requests
  without a browser user agent) [3]. "An AI coding agent from Replit
  reportedly deleted a live database during a code freeze", "violating
  explicit instructions not to proceed without human approval"; CEO Amjad
  Masad: "Replit agent in development deleted data from the production
  database. Unacceptable and should never be possible". Replit then rolled
  out "automatic separation between development and production databases".

## Untrusted input: prompt injection, foreign repositories and packages (chapters 4, 8 and 9)

- Railway (Mahmoud Abdelwahab). "Your AI wants to nuke your database.
  Guardrails fix that." 29 April 2026.
  https://blog.railway.com/p/your-ai-wants-to-nuke-your-database (checked
  2026-10-08; it left the paper later that day to make room for chapter 10: the advice on scoped tokens keeps its source). "The agent found a Railway API token stored locally on
  the user's machine and used it to call volumeDelete on a production
  volume"; "the token was provisioned with account scoped access, the
  maximum access possible". Railway recovered the database and made API
  deletes reversible for 48 hours. Other accounts name Cursor as the tool.
- Wiz (Merav Bar, Rami McCarthy). "keyv and cacheable npm Package Hijacked
  in Supply Chain Attack". 4 August 2026.
  https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
  (checked 2026-10-08; it left the paper later that day to make room for chapter 10: chapter 9 keeps two
  other outside sources). A worm of the Shai-Hulud family that
  "propagated to over 400 distinct npm packages"; "Persistence is attempted
  via Claude Code hooks and VS Code tasks.json". Written during a live
  incident.

- Anthropic. "Security" (Claude Code documentation).
  https://code.claude.com/docs/en/security (checked 2026-10-06) [36]. Defines
  prompt injection as an attempt "to override or manipulate an AI
  assistant's instructions by inserting malicious text"; lists the
  safeguards (trust dialog, network approval, WebFetch summaries in a
  separate model call) and advises to "Use virtual machines (VMs) to run
  scripts and make tool calls, especially when interacting with external web
  services". "No system is completely immune to all attacks."
- Anthropic. "Hooks reference", section Workspace trust; "Configure
  permissions", section What runs before you trust a folder; "Extend Claude
  with skills", section Pre-approve tools for a skill.
  https://code.claude.com/docs/en/hooks,
  https://code.claude.com/docs/en/permissions,
  https://code.claude.com/docs/en/skills (checked 2026-10-06; read again
  2026-10-28) [14, 18, 20]. In
  a `-p` or SDK session "Claude Code never shows the dialog and treats the
  folder as trusted, so hooks committed in a repository's
  `.claude/settings.json` run in a folder you've never trusted"; servers in
  `.mcp.json` connect "without asking". Before scripting `claude -p` over a
  repository you did not write, review its `.claude/` settings, or start the
  run with `--setting-sources user`, which reads neither the project's
  settings files nor its `.mcp.json`, or with `--bare`, which reads none of
  its hooks, skills, subagents, plugins or `.mcp.json` servers but still
  applies its `env` block. `--settings '{"disableAllHooks": true}'` turns
  off the hooks only, so the `.mcp.json` servers still connect. A skill's
  `allowed-tools` is applied "even in a `-p` run in a folder you've never
  trusted", so "review the `allowed-tools` of skills checked into a
  repository before you run Claude Code there."
- Check Point Research (Aviv Donenfeld, Oded Vanunu). "Check Point
  Researchers Expose Critical Claude Code Flaws". February 2026.
  https://blog.checkpoint.com/research/check-point-researchers-expose-critical-claude-code-flaws/
  (checked 2026-10-06; read again 2026-10-08, when it left the paper to make
  room for the documented case of a download unpacked into a trusted folder).
  Two flaws "triggered simply by cloning and
  opening an untrusted project": hooks, MCP settings and environment
  variables in a repository could "execute hidden shell commands, and
  redirect authenticated API traffic before user consent". The CVE records
  (https://cveawg.mitre.org/api/cve/CVE-2025-59536, fixed in 1.0.111, and
  https://cveawg.mitre.org/api/cve/CVE-2026-21852, fixed in 2.0.65, both
  checked 2026-10-06) say the code ran "before the user accepted the startup
  trust dialog" and the requests went out "before showing the trust prompt".
  The lesson: "repository configuration files now function as part of the
  execution layer".
- Simon Willison. "The lethal trifecta for AI agents: private data,
  untrusted content, and external communication". June 2025.
  https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ (checked
  2026-10-06; read again 2026-10-07) [38]. If an agent combines access to
  private data, exposure to untrusted content and a way to communicate
  externally, "an attacker can easily trick it" into leaking the data; "we
  still don't know how to 100% reliably prevent this from happening", so
  "avoid that lethal trifecta combination entirely."
- Invariant Labs (Marco Milanta, Luca Beurer-Kellner). "GitHub MCP Exploited:
  Accessing private repositories via MCP". May 2025.
  https://invariantlabs.ai/blog/mcp-github-vulnerability (checked
  2026-10-06; read again 2026-10-08; it left the paper later that day to make room for chapter 10:
  chapter 9 keeps the Nx attack as its example). An issue in a public repository
  told an agent with GitHub access to copy private repository contents into
  a public pull request. "Importantly, this is not a flaw in the GitHub MCP
  server code itself, but rather a fundamental architectural issue". A
  research demonstration with Claude Desktop and Claude 4 Opus, on a client
  whose user had set tool calls to "Always Allow".
- Adnan Khan. "Clinejection — Compromising Cline's Production Releases just
  by Prompting an Issue Triager". February 2026.
  https://adnanthekhan.com/posts/clinejection/ (checked 2026-10-06). An issue
  title made an AI triage workflow, open to any GitHub user and allowed to run
  shell commands, install an attacker's package, a first step towards the
  project's release tokens. Snyk's account,
  https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions/
  (checked 2026-10-06): eight days after the disclosure, "an unknown actor
  exploited the same flaw to publish an unauthorized version" of the package,
  through a token that had not been properly revoked; it was live for
  roughly eight hours.
- Aonan Guan et al. "Comment and Control: Prompt Injection to Credential Theft
  in Claude Code, Gemini CLI, and GitHub Copilot Agent". April 2026.
  https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/
  (checked 2026-10-06). Pull request titles and hidden HTML comments made
  three CI agents post their API keys. Anthropic stated that its GitHub
  action "is not designed to be hardened against prompt injection", blocked
  the command used, and later reclassified the report; whoever runs such an
  agent decides what it can reach.
- Pillar Security (Ziv Karliner). "New Vulnerability in GitHub Copilot and
  Cursor: How Hackers Can Weaponize Code Agents". March 2025.
  https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents
  (checked 2026-10-06). The "Rules File Backdoor": instructions in a rules
  file hidden with invisible Unicode characters, "undetectable to human
  reviewers but fully readable by AI models".
- Nx. "Malicious versions of Nx and some supporting plugins were published"
  (security advisory). August 2025.
  https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c (checked
  2026-10-06). A compromised package whose install script scanned the file
  system for credentials.
- Wiz (Rami McCarthy). "s1ngularity's Aftermath: AI, TTPs, and Impact in the
  Nx Supply Chain Attack". September 2025.
  https://www.wiz.io/blog/s1ngularitys-aftermath (checked 2026-10-06; read
  again 2026-10-07) [39]. The malware checked for Claude, Gemini and Amazon Q
  and started them, among them `claude --dangerously-skip-permissions -p`,
  with prompts that asked for wallet, secret and configuration files.
  "roughly 50% of all victims had at least one AI CLI installed"; "almost a
  quarter of Claude interactions were rejected", and "AI only exfiltrated
  data successfully in under a quarter of cases".
- BleepingComputer (Lawrence Abrams). "Laravel Lang packages hijacked to
  deploy credential-stealing malware". 23 May 2026.
  https://www.bleepingcomputer.com/news/security/laravel-lang-packages-hijacked-to-deploy-credential-stealing-malware/
  (checked 2026-10-26) [40]. A news report that draws on StepSecurity,
  Aikido and Socket: "the attacker rewrote every existing git tag in each
  repository to point at a new malicious commit" in a fork; a new
  `src/helpers.php` in the autoload section made Composer load it; the
  payload collects cloud credentials, Kubernetes secrets, Vault tokens, Git
  credentials, CI/CD secrets, SSH keys, browser data, wallets and `.env`
  files. The counts differ by vendor: "233 versions across three
  repositories" (Aikido), "roughly 700 historical versions may have been
  impacted" (Socket). Packagist removed the versions and unlisted the
  packages. The author's request of 2026-10-26 brought it into chapter 9 as
  the PHP case of a supply-chain attack.
- Mend (Alina Podoba). "Laravel-Lang Composer Tag-Rewrite Supply-Chain
  Attack". 22 May 2026.
  https://www.mend.io/blog/laravel-lang-composer-tag-rewrite-supply-chain-attack/
  (checked 2026-10-26). The rewrite of every tag in four packages ran from
  22 May into the early hours of 23 May; the malicious commits are "not
  reachable from any branch". Entries in `autoload.files` "execute the
  moment the autoloader is bootstrapped": on every request in Laravel, on
  every Composer command and in the first CI step. Version constraints
  "resolve to whatever the rewritten tag now points at"; a `composer.lock`
  that pinned commits from before 22 May stays safe while nobody runs
  `composer update`. A vendor's analysis; it would carry a sentence on what
  a lockfile does against a moved tag.
- Aikido (Ilyas Makari). "Supply Chain Attack Targets Laravel-Lang Packages
  with Credential Stealer". 23 May 2026, updated 3 June 2026.
  https://www.aikido.dev/blog/supply-chain-attack-targets-laravel-lang-packages-with-credential-stealer
  (checked 2026-10-26). The vendor that reported it to Packagist. "GitHub
  allows version tags to point to commits from a fork of the same
  repository"; the code "runs once on every machine it infects", and the
  list of what it collects runs from cloud and CI tokens and SSH keys to
  password-manager vaults, wallets and chat tokens. No download figures.
- San Francisco Standard (Zara Stone). "She runs AI safety at Meta. Her AI
  agent still went rogue". 25 February 2026.
  https://sfstandard.com/2026/02/25/openclaw-goes-rogue/ (checked
  2026-10-26) [1]. Summer Yue, "director of alignment at Meta
  Superintelligence Labs", had told her OpenClaw agent to "confirm before
  acting"; it began "deleting her email inbox" and ignored her stop
  messages. The agent "had run out of working memory and condensed prior
  messages to make room for new ones", which likely lost her instruction.
  "I couldn't stop it from my phone. I had to RUN to my Mac mini like I was
  defusing a bomb." Her own account; OpenClaw is a personal assistant
  agent, not a coding assistant, and no count of lost mail is given. The
  author's choice of 2026-10-26 for the Introduction's opening.
- Simon Willison. "A quote from Summer Yue". 23 February 2026.
  https://simonwillison.net/2026/Feb/23/summer-yue/ (checked 2026-10-26).
  Her posts word for word: the instruction "Check this inbox too and suggest
  what you would archive or delete, don't action until I tell you to", and
  her reading of the cause: "my real inbox was too huge and triggered
  compaction. During the compaction, it lost my original instruction."
  Names no job title.
- Spracklen, Wijewickrama, Sakib, Maiti, Viswanath, Jadliwala. "We Have a
  Package for You! A Comprehensive Analysis of Package Hallucinations by Code
  Generating LLMs". USENIX Security 2025 (Distinguished Paper).
  https://arxiv.org/abs/2406.10279 (checked 2026-10-07; read again 2026-10-08,
  when it left the paper for space: chapter 9 keeps five other outside
  sources). 576,000 code samples from 16 models: hallucinated packages averaged "at least 5.2% for
  commercial models and 21.7% for open-source models", 205,474 unique names.
  The authors call it a "novel form of package confusion attack". The models
  are those of 2024; the abstract does not say whether newer ones do better.

## Delegation: do more agents help? (chapter 5)

- Purnachandra Reddy, Lolla, Sanku. "Articulate but Wrong: Self-Review
  Failures in LLM-Based Code Modernization". May 2026.
  https://arxiv.org/abs/2605.21537 (checked 2026-10-08, when it left the
  paper: it repeats [23] on weaker evidence). Eleven models
  ported Python 2 code and reviewed their own output: "31.7% are silently
  endorsed by the same model that produced them (83/262)", with a
  per-model rate from 0% to 100%. A preprint on 60 snippets; the parallel
  to a SAS-to-R migration is ours, not the authors'.

- Anthropic. "How we built our multi-agent research system". June 2025.
  https://www.anthropic.com/research/multi-agent-research-system (checked
  2026-10-06; read again 2026-10-08, when it left the paper: the figures are
  for the claude.ai Research feature and measured against a chat, not a
  single agent; moved from /engineering/ by 2026-10-28, figures
  unchanged). Agents use about 4 times, multi-agent systems about 15 times
  the tokens of a chat, and "most coding tasks involve fewer truly
  parallelizable tasks than research".
- Google Research (Yubin Kim, Xin Liu). "Towards a science of scaling agent
  systems: When and why agent systems work". January 2026.
  https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
  (checked 2026-10-06). Coordinated agents gained 81% on a parallelisable
  financial task, while every multi-agent variant lost 39 to 70% on a
  sequential planning task; independent agents amplified errors 17.2 times,
  centrally coordinated ones 4.4 times.
- Cognition (Walden Yan). "Don't Build Multi-Agents". June 2025.
  https://cognition.com/blog/dont-build-multi-agents (checked 2026-10-06).
  "Share context" and "Actions carry implicit decisions". It notes that
  Claude Code's subtask agent "is usually only tasked with answering a
  question, not writing any code", the narrow use the paper recommends.
- Cemri et al. "Why Do Multi-Agent LLM Systems Fail?". 2025.
  https://arxiv.org/abs/2503.13657 (checked 2026-10-06). Over 1,600
  annotated traces from seven frameworks; gains on benchmarks "are often
  minimal"; 14 failure modes in three groups: system design, inter-agent
  misalignment, task verification.
- Kim, Garg, Peng, Garg. "Correlated Errors in Large Language Models". ICML
  2025. https://arxiv.org/abs/2506.07962 (checked 2026-10-06; read again
  2026-10-28) [25]. Over 350 models on two leaderboards and a hiring task.
  The 60% is the mean over Helm's 71 open and proprietary models from 15
  companies, where "models agree 60% of the time when both models err",
  against a third by chance; over HuggingFace's 349 open-source models the
  mean is 42%, against 13% by chance. The authors also find that "larger
  and more accurate models have highly correlated errors, even with
  distinct architectures and providers". A reviewer subagent on the same
  model is a fresh pair of eyes, not an independent one.
- Huang et al. "Large Language Models Cannot Self-Correct Reasoning Yet".
  ICLR 2024. https://arxiv.org/abs/2310.01798 (checked 2026-10-06; read
  again 2026-10-08) [23]. Without
  external feedback, models "struggle to self-correct their responses", and
  their performance sometimes "even degrades after self-correction".

## Context (chapter 6)

- Anthropic. "Effective context engineering for AI agents". September 2025.
  https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
  (checked 2026-10-06; moved from /engineering/ by 2026-10-28, quotes
  unchanged). Context is "a finite resource with diminishing
  marginal returns"; aim for "the smallest possible set of high-signal
  tokens".
- Hong, Troynikov, Huber (Chroma). "Context Rot: How Increasing Input Tokens
  Impacts LLM Performance". July 2025.
  https://www.trychroma.com/research/context-rot (checked 2026-10-06; read
  again 2026-10-08; the old address research.trychroma.com redirects) [27].
  18 models: "performance
  grows increasingly unreliable as input length grows", even on simple tasks.
- Modarressi et al. "NoLiMa: Long-Context Evaluation Beyond Literal
  Matching". ICML 2025. https://arxiv.org/abs/2502.05167 (checked
  2026-10-20). Of 13 models that claim at least 128K tokens, "At 32K, for
  instance, 11 models drop below 50% of their strong short-length
  baselines"; GPT-4o falls "from an almost-perfect baseline of 99.3% to
  69.7%". Models of 2024, and a task of finding one fact without word
  overlap. The talk's note on 6.1 quotes it (`slides/qa.md` 29).
- Martin, Roger. "Classifier Context Rot: Monitor Performance Degrades with
  Context Length". Preprint, May 2026.
  https://arxiv.org/abs/2605.12366 (checked 2026-10-20). Authors from the
  Anthropic Fellows Program and Anthropic. "Opus 4.6 (with thinking)'s
  recall drops from 99.7% when such an attack is inserted in a 100K
  transcript to 69% when the same attack is inserted in an 800K
  transcript." A monitoring task at very long lengths, not everyday work,
  but the newest figure for a Claude model found.
- Hu et al. (2026, under Skills above) measures where Claude Code spends
  tokens it need not.

## Memory (chapter 7)

- Cisco (Idan Habler, Amy Chang). "Identifying and remediating a persistent
  memory compromise in Claude Code". 1 April 2026.
  https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code
  (checked 2026-10-08) [33]. An npm install in a cloned repository rewrote
  memory files, so that Claude Code gave manipulated advice "into every
  project, every session, and even after reboots"; Anthropic "pushed a
  change to Claude Code v2.1.50 that removes this capability from the
  system prompt". Vendor research; the user had approved the install. Read
  again 2026-10-08: the change "significantly reduces" the vector rather than
  ending it, and a planted MEMORY.md still loads every session, so the paper
  says the change weakens such notes but does not stop them.

- Anthropic. "Managing context on the Claude Developer Platform". September
  2025. https://claude.com/resources/articles/context-management (checked
  2026-10-06; moved from /blog/ by 2026-10-28, figures unchanged). On
  an internal agentic-search evaluation, the memory tool with context editing
  improved performance by 39% (context editing alone 29%); in a 100-turn
  web-search evaluation, context editing cut token use by 84%. A vendor figure for
  the API's memory tool, not for Claude Code's auto memory.
- Srivastava, He. "MemoryGraft: Persistent Compromise of LLM Agents via
  Poisoned Experience Retrieval". December 2025.
  https://arxiv.org/abs/2512.16962 (checked 2026-10-06; read again
  2026-10-08, when it left the paper: its measurements cover what the agent
  retrieved, 47.9% poisoned records, not a measured change in behaviour).
  Planted "successful
  experiences" in an agent's long-term memory lead to "persistent behavioral
  drift across sessions". Shown on MetaGPT's DataInterpreter agent with
  GPT-4o, not on Claude Code, but a reason to read the memory folder now and
  then.

## Regulators and our own community

- The White House. "Inaugurating the Era of Super Intelligence". Executive
  Order 14434, signed 29 September 2026.
  https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/
  (checked 2026-10-26; the Federal Register's public-inspection copy,
  document 2026-20321, read in full; it left the paper on 2026-10-27, when
  the Conclusion made room for the author's view of open models and
  prices). Sec. 2(a): agencies "shall use
  "Super Intelligence" and "SI" in place of "Artificial Intelligence" and
  "AI"" in their non-statutory documents, "to the maximum extent permitted
  by law". Sec. 3(a): the terms "mean the technologies and systems
  encompassed by the term "artificial intelligence"" in 15 U.S.C. 9401(3).
  Sec. 3(b) asks for a proposed legislative definition within 60 days, so
  the definition may change. The Conclusion's dry line rested on it (the
  author's choice of 2026-10-26); quote the order, never comment on its
  politics.

- EMA and FDA. "Guiding principles of good AI practice in drug
  development". January 2026.
  https://www.ema.europa.eu/en/documents/other/guiding-principles-good-ai-practice-drug-development_en.pdf
  (checked 2026-10-08) [57]. Ten principles on two pages for AI that is
  "used to generate or analyse evidence across the drug product life
  cycle", among them "a risk-based approach with proportionate validation"
  and adherence to GxP. The text does not mention code, programming or
  language models; principle 7 names "software engineering" once.
- UK National Cyber Security Centre. "Managing the cyber risk of agentic
  AI". 20 August 2026.
  https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai
  (checked 2026-10-08) [34]. Interim advice for any agentic system: "Always
  run AI agents within a sandboxed environment that controls and manages
  what resources can and cannot be communicated with, both locally and over
  a network"; an agent without compute isolation "may also be able to use
  credentials that are available to the user account under which it is
  running".

- FDA. "Artificial Intelligence for Drug Development".
  https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development
  (checked 2026-10-06; content current as of 1 May 2026). The draft guidance
  of January 2025 covers "the use of AI to produce information or data
  intended to support regulatory decision-making", not AI as a programming
  aid; the page links the FDA–EMA "Guiding Principles of Good AI Practice in
  Drug Development" of January 2026.
- PHUSE EU Connect 2025, Machine Learning, AI and Large Language Models
  stream. lexjansen.com, the usual index, was down on 2026-10-06, and the
  Internet Archive holds no copy of its stream page. PHUSE keeps the papers
  in its own archive, one file per paper:
  https://phuse.s3.eu-central-1.amazonaws.com/Archive/2025/Connect/EU/Hamburg/PAP_ML04.pdf
  and so on for ML01 to ML16 (checked 2026-10-06, abstracts read). The ones
  on AI for programmers:
  - Böser (Chrestos). "Neither Magic Wand Nor Terminator: Finding the Sweet
    Spot in AI-Assisted Coding". Paper ML04, Best in Connect 2025 (PHUSE,
    "EU Connect 2025 Summary & Award Winners",
    https://phuse.global/Communications/PHUSE_Blog/eu-connect-2025-summary-and-award-winners,
    checked 2026-10-06; since 2026-10-27 the paper cites the talk's slides,
    PRE_ML04.pdf in the same folder, instead). The author's own predecessor
    to this paper: it
    "cuts through the hype to show how AI coding tools work in the
    trenches", where this paper asks how to keep them under control.
  - Cao, Jiang (Bristol Myers Squibb). "Leveraging Gen AI for R Shiny App
    Code Development: A Case Study with Event Prediction". Paper ML05.
    Advice on "modular code design, effective prompting from simple to
    complex, the provision of examples, debugging, validation, and ensuring
    consistency and data security".
  - Kraus, Stöckinger, Bauer (HMS Analytical Software, Boehringer
    Ingelheim). "Leveraging AI for Seamless SAS to R Migration: Challenges
    and Opportunities". Paper ML11. Translating SAS macros for PK/PD analyses
    into R with GenAI, and why such work needs a guiding framework.
  - Cayssol, Centner (Roche). "Everyday AI for Statistical Programmers:
    Global Implementation of a Clinical Analysis Assistant". Paper ML15. A
    code search agent over more than 70,000 indexed programs, so that
    validated code is found and reused.
  - Skliar (Intego Group). "Detecting Logical Errors in Clinical Programming
    by Applying ChatGPT". Paper ML16. A model reviews SAS code against the
    SAP and protocol; "To verify the validity of GPT responses, several
    approaches are suggested: manual validation, comparison with legacy
    code, and peer-review logic by colleagues." The community's version of
    the reviewer in chapter 5, with the same caveat.

## Data protection and dependence (chapter 10)

Collected on 2026-10-08 for chapter 10, on what leaves the machine and
on the dependence a team builds on one model provider. Research agents read
each page that day; the quotes are verbatim, and translations from German
are ours. Chapter 10 cites seven sources from here, with documentation
entries already in the list; a source enters only through `/add-reference`. None of this is legal advice: it
says what the sources say.

### Law and court judgments

- European Union. "Regulation (EU) 2016/679 (General Data Protection
  Regulation)". OJ L 119, 4 May 2016.
  https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
  (checked 2026-10-08) [42]. Recital 26: "Personal data which have undergone
  pseudonymisation, which could be attributed to a natural person by the
  use of additional information should be considered to be information on
  an identifiable natural person." Article 9 makes "data concerning health"
  a special category; Article 28 allows only processors "providing
  sufficient guarantees", bound by a contract; Article 35 asks for an impact
  assessment before "processing on a large scale of special categories of
  data"; Article 33 asks for notice of a breach "not later than 72 hours
  after having become aware of it". Binding law; the Digital Omnibus change
  below is only proposed.
- Court of Justice of the EU. Judgment of 4 September 2025, EDPS v SRB,
  C-413/23 P.
  https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62023CJ0413
  (checked 2026-10-08). "pseudonymised data must not be regarded as
  constituting, in all cases and for every person, personal data" (para
  86), but where "it cannot be ruled out that those third parties have
  means reasonably allowing them to attribute pseudonymised data to the
  data subject, such as cross-checking with other data at their disposal,
  the data subject must be regarded as identifiable" (para 85). For the
  controller's own duties, identifiability is assessed "from the point of
  view of the controller" (para 111). Decided under Regulation 2018/1725,
  whose definitions mirror the GDPR. For a sponsor that holds the key,
  coded trial data stay personal.
- European Data Protection Board. Guidelines 01/2025 on pseudonymisation
  (16 January 2025), Guidelines 1/2026 on processing personal data for
  scientific research (15 April 2026) and Guidelines 02/2026 on
  anonymisation (7 July 2026, consultation until 30 October 2026).
  https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf,
  https://www.edpb.europa.eu/system/files/2026-05/edpb_guidelines_202601_scientificresearch_en.pdf,
  https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202602_anonymisation_v1_en_0.pdf
  (checked 2026-10-08). Pseudonymised data "is to be considered information
  on an identifiable natural person, and is therefore personal", even when
  data and key "are not in the hands of the same person" (01/2025, para 22;
  written before the SRB judgment and being reworked). "The sponsor, which
  mainly process pseudonymised data, is nonetheless still regarded as a
  controller" (1/2026, para 136). An entity that processes data on behalf
  of another takes "the controlling entity's perspective" and "should,
  therefore, be considered a processor" (02/2026, para 15). All three are
  drafts.
- EDPB and EDPS. Joint Opinion 2/2026 on the Digital Omnibus. 10 February
  2026.
  https://www.edpb.europa.eu/system/files/documents/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf
  (checked 2026-10-08). The Commission proposes that information "shall not
  be personal for a given entity where that entity cannot identify the
  natural person"; the two bodies "strongly urge the co-legislators to not
  adopt the proposed changes to the definition of personal data". The
  European Parliament's Legislative Train, updated 20 September 2026, lists
  the file as tabled: the Council's mandate vote planned for 26 June "was
  ultimately cancelled".
  https://www.europarl.europa.eu/legislative-train/package-digital-package/file-digital-package
- EDPB Support Pool of Experts (Isabel Barberá). "AI Privacy Risks &
  Mitigations – Large Language Models (LLMs)". April 2025.
  https://www.edpb.europa.eu/system/files/documents/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf
  (checked 2026-10-08). "Users may unknowingly or inadvertently input
  sensitive personal data, such as names, addresses, financial information,
  or medical details." When providers "collect or retain data for their own
  purposes (e.g., model fine-tuning or feature improvement), they assume
  the role of controller too." The EDPB notes: "This document was not
  produced by the EDPB".
- EU–US Data Privacy Framework. European Commission, "EU-US data
  transfers"; General Court, Latombe v Commission, T-553/23, 3 September
  2025; appeal C-703/25 P.
  https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en,
  https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62023TJ0553,
  https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62025CN0703
  (checked 2026-10-08). Data "can flow freely from the EU to companies in
  the United States that participate in the Data Privacy Framework"; the
  General Court "Dismisses the action"; the appeal, lodged on 31 October
  2025, asks the Court to "annul Commission Implementing Decision (EU)
  2023/1795", and EUR-Lex shows no judgment yet. Valid, but contested.
- EU AI Act, Regulation (EU) 2024/1689, as amended by Regulation (EU)
  2026/1744 (Digital Omnibus on AI, in force since 27 July 2026).
  https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744
  (checked 2026-10-08). A company that uses an assistant is a "deployer".
  Its main duty is AI literacy, now "to support the development of AI
  literacy of their staff", which "does not require providers or deployers
  to guarantee any specific level of AI literacy of any individual". "This
  Regulation shall not affect Regulation (EU) 2016/679".

### Medicines regulators and GCP

- EMA and HMA. "Guiding principles on the use of large language models in
  regulatory science and for medicines regulatory activities". 29 August
  2024.
  https://www.ema.europa.eu/en/documents/other/guiding-principles-use-large-language-models-regulatory-science-medicines-regulatory-activities_en.pdf
  (checked 2026-10-08). "check the text to avoid inputting sensitive
  information including personal data, trade secrets, data that is
  protected by intellectual property law, data where existing contracts
  impose restrictions on sharing and other secrets like passwords and
  tokens", and know whether models "are deployed locally and fully
  controlled by the organisation or if they are open online models that
  may reuse the data from prompts". Addressed to the staff of the medicines
  regulatory network, not to industry.
- EMA. "Reflection paper on the use of artificial intelligence (AI) in the
  medicinal product lifecycle". September 2024.
  https://www.ema.europa.eu/en/documents/scientific-guideline/reflection-paper-use-artificial-intelligence-ai-medicinal-product-lifecycle_en.pdf
  (checked 2026-10-08). "As a general recommendation in the case of any
  personal data processing by AI, a specific risk assessment focusing on
  the AI system should be performed." Aimed at AI in evidence generation.
- EMA. External guidance on the implementation of the policy on the
  publication of clinical data (Policy 0070), version 1.5. 14 May 2025.
  https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/external-guidance-implementation-european-medicines-agency-policy-publication-clinical-data-medicinal-products-human-use-version-15_en.pdf
  (checked 2026-10-08). "pseudonymisation is not an anonymisation method
  but a useful security measure" (section 3.3.2). EMA's own view of coded
  trial data, in the audience's language.
- ICH. "E6(R3) Guideline for Good Clinical Practice". 6 January 2025.
  https://database.ich.org/sites/default/files/ICH_E6%28R3%29_Step4_FinalGuideline_2025_0106.pdf
  (checked 2026-10-08). "The confidentiality of information that could
  identify participants should be protected in accordance with applicable
  privacy and data protection requirements" (principle 1.6), and
  "Computerised systems used in clinical trials should be fit for purpose"
  (9.3). Whether the assistant itself is such a system is an
  interpretation; the programs it writes for trial outputs are in scope.
- US Code of Federal Regulations. 45 CFR 164.514 (HIPAA de-identification).
  https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514
  (checked 2026-10-08). Safe Harbor removes "All elements of dates (except
  year) for dates directly related to an individual", so ADaM data with
  visit dates are not de-identified under it. HIPAA binds covered entities
  and their business associates; whether a sponsor is either is for legal
  to say.

### Data protection authorities and security agencies

- ANSSI and BSI. "AI Coding Assistants". September 2024.
  https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/ANSSI_BSI_AI_Coding_Assistants.pdf
  (checked 2026-10-08) [45]. "The use of uncontrolled access to coding
  assistants (e.g. through private accounts of employees) in the cloud
  should be prohibited for business software development." "When using
  cloud services, the contractual conditions should be carefully examined,
  particularly with regard to the further use of your own data for AI
  training." The most direct official advice on the paper's subject.
- Autoriteit Persoonsgegevens (the Dutch data protection authority).
  "Caution: use of AI chatbot may lead to data breaches". 6 August 2024.
  https://www.autoriteitpersoonsgegevens.nl/en/current/caution-use-of-ai-chatbot-may-lead-to-data-breaches
  (checked 2026-10-08) [41]. "an employee of a GP practice had entered medical
  data of patients into an AI chatbot, contrary to the agreements." "If
  personal data have been entered in the process, this means there is a
  data breach." "Organisations could also arrange with the provider of a
  chatbot that this provider will not store the data entered."
- DSK (the conference of German data protection authorities).
  "Orientierungshilfe Künstliche Intelligenz und Datenschutz", version 1.0.
  6 May 2024.
  https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf
  (checked 2026-10-08). In our translation: removing names and addresses
  from an input is usually not enough to avoid personal data (no. 49);
  technically closed systems are preferable (no. 20), and so are
  applications that do not train on inputs and outputs (no. 24); use
  company accounts, not private ones (nos. 41 and 42).
- CNIL. "CNIL's Q&A on the use of generative AI systems". 18 July 2024.
  https://www.cnil.fr/en/cnils-qa-use-generative-ai-systems (checked
  2026-10-08). Through an API, "the control of the system is then almost
  exclusively in the hands of its supplier", so avoid "as far as possible
  inputs containing personal data"; where personal data must be provided,
  "it generally seems more appropriate and secure to favour the deployment
  of on-premise solutions".
- UK Information Commissioner's Office. "Guidance on AI and data
  protection". Updated 15 March 2023, under review.
  https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
  (checked 2026-10-08). "In the vast majority of cases, the use of AI will
  involve a type of processing likely to result in a high risk", which
  calls for an impact assessment.
- Irish Data Protection Commission. "AI, Large Language Models and Data
  Protection". 18 July 2024.
  https://www.dataprotection.ie/en/dpc-guidance/blogs/AI-LLMs-and-Data-Protection
  (checked 2026-10-08). Understand "where the personal data goes in
  situations where a third-party is involved in the processing, whether it
  is retained by the provider of the AI product or re-used in any way".
- Hamburg Commissioner for Data Protection. "Discussion Paper: Large
  Language Models and Personal Data". 15 July 2024.
  https://datenschutz-hamburg.de/fileadmin/user_upload/HmbBfDI/Datenschutz/Informationen/240715_Discussion_Paper_Hamburg_DPA_KI_Models.pdf
  (checked 2026-10-08). The GDPR applies to processing in an LLM-supported
  system, "in particular to the output". Its thesis that a model stores no
  personal data conflicts with EDPB Opinion 28/2024.
- BSI. "Generative KI-Modelle – Chancen und Risiken für Industrie und
  Behörden", version 2.0. 17 January 2025.
  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KI/Generative_KI-Modelle.pdf
  (checked 2026-10-08). In our translation: the risk extends in principle
  to all information made available to a model while it performs its task,
  which for an agent means every file it reads.

### The running example: Anthropic's terms and documentation

- Anthropic. "Data usage" (Claude Code documentation).
  https://code.claude.com/docs/en/data-usage (checked 2026-10-08) [6].
  Consumer plans: a "5-year retention period" for users who allow data use
  for model improvement, otherwise a "30-day retention period". Commercial
  users: "Standard: 30-day retention period", and "Anthropic does not train
  generative models using code or prompts sent to Claude Code under
  commercial terms, unless the customer has chosen to provide their data".
  "Claude Code clients store session transcripts locally in plaintext under
  `~/.claude/projects/` for 30 days by default". "When you run the
  `/feedback` command, a copy of your conversation history including code
  is sent to Anthropic"; such transcripts "are retained for 5 years".
- Anthropic. "Zero data retention", "Legal and compliance", "Configure
  permissions" and "Settings reference" (Claude Code documentation).
  https://code.claude.com/docs/en/zero-data-retention,
  https://code.claude.com/docs/en/legal-and-compliance,
  https://code.claude.com/docs/en/permissions,
  https://code.claude.com/docs/en/settings-reference (checked 2026-10-08)
  [18]. Zero data retention is for "qualified accounts on Claude for
  Enterprise", and "Data processed by third-party tools, MCP servers, or
  other external integrations is not covered by ZDR." A Business Associate
  Agreement "extends to Claude Code in two configurations". Read deny rules
  "don't apply to a command that reads files without naming them, such as
  `grep -r pattern .` [...], or to arbitrary subprocesses"; "For OS-level
  enforcement that blocks all processes from accessing a path, enable the
  sandbox." The sandbox's `denyRead` list "adds the paths from your
  `Read(...)` deny permission rules".
- Anthropic. "Data residency" (Claude Platform documentation).
  https://platform.claude.com/docs/en/manage-claude/data-residency (checked
  2026-10-08) [47]. "Inference geo: Only `"us"` and `"global"` are available";
  "On Amazon Bedrock and Google Cloud, the inference region is determined
  by the endpoint URL or inference profile". So an EU region means a cloud
  provider, not Anthropic's own API, as of October 2026.
- Anthropic. "Data Processing Addendum". Effective 24 February 2025.
  https://www.anthropic.com/legal/data-processing-addendum (checked
  2026-10-08). "Customer is the controller and Anthropic is Customer's
  processor"; standard contractual clauses are incorporated. Whether
  Anthropic is certified under the Data Privacy Framework was not checked.
- Anthropic. "Updates to Consumer Terms and Privacy Policy". 28 August 2025.
  https://www.anthropic.com/news/updates-to-our-consumer-terms (checked
  2026-10-08). "We're now giving users the choice to allow their data to be
  used to improve Claude"; it applies to the Free, Pro and Max plans,
  "including when they use Claude Code"; "We are also extending data
  retention to five years, if you allow us to use your data for model
  training." A change of terms that reached existing users, who had until
  8 October 2025 to decide.

### What went wrong: incidents

People put data into chatbots; providers had bugs and legal holds; agents
were steered into sending data out. Most cases involve chat tools rather
than coding agents, and none found was from a pharmaceutical company or a
clinical trial. The Dutch authority's case is under the authorities above.

- NSW Reconstruction Authority. "Northern Rivers Resilient Homes Program
  data breach" (media release, 6 October 2025) and the information page
  updated 26 March 2026.
  https://www.nsw.gov.au/departments-and-agencies/nsw-reconstruction-authority/media-releases/northern-rivers-resilient-homes-program-data-breach,
  https://www.nsw.gov.au/RHPdatabreach (checked 2026-10-08). "Between 12 and
  15 March 2025, personal information was uploaded by a former contractor of
  the RA to the Artificial Intelligence platform ChatGPT." "The data shared
  was a Microsoft Excel spreadsheet with 10 columns and more than 12,000
  rows of information"; "2031 people [...] had some of their data uploaded
  to ChatGPT". It came to light about seven months later. "There is no
  evidence that any of the uploaded data is publicly available online".
  The closest case to a programmer uploading a dataset.
- Office of the Victorian Information Commissioner. "Investigation into the
  use of ChatGPT by a Child Protection worker". 24 September 2024.
  https://ovic.vic.gov.au/regulatory-action/investigation-into-the-use-of-chatgpt-by-a-child-protection-worker/
  (checked 2026-10-08). A worker "entered a significant amount of personal
  and delicate information into ChatGPT, including names and information
  about risk assessments relating to the child"; "Even where a person tries
  to de-identify information by removing names, it may be re-identified
  using the rest of the information as well as other information sources."
  Found on the balance of probabilities; the worker denied it. The
  department had to block such tools for its child protection staff.
- Eindhoven municipality. Reported by Omroep Brabant (19 December 2025)
  and NL Times (30 December 2025).
  https://www.omroepbrabant.nl/nieuws/6001041/datalek-gemeente-eindhoven-deelt-persoonsgegevens-met-openbare-ai-websites,
  https://nltimes.nl/2025/12/30/dutch-privacy-watchdog-warns-rising-ai-chatbot-data-leaks
  (checked 2026-10-08). One month of traffic showed files with personal
  data, among them youth-care documents and CVs, sent to public AI sites;
  the city could not establish how much had left, since the logs were kept
  for 30 days. The Dutch authority counted "dozens of such AI-related data
  breach reports" in 2025 (second-hand, via Het Financieele Dagblad). News
  reports; the council's letter was not found.
- Health New Zealand. Reported by RNZ, 26 March 2026.
  https://www.rnz.co.nz/news/health/590645/health-nz-staff-told-to-stop-using-chatgpt-to-write-clinical-notes
  (checked 2026-10-08). Its memo: "The use of free AI tools (e.g. ChatGPT,
  Claude, Gemini) for clinical purposes is strictly prohibited [...] even
  if you anonymise the patient information." A news report quoting a memo.
- Samsung. Economist Korea (30 March 2023) and TechCrunch (2 May 2023).
  https://economist.co.kr/article/view/ecn202303300057,
  https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/
  (checked 2026-10-08). Engineers pasted source code into ChatGPT to debug
  it; Samsung then restricted generative AI "through company devices".
  Samsung confirmed only the restriction, not the incidents. The
  programmer's version of the problem.
- OpenAI. "March 20 ChatGPT outage: Here's what happened". 24 March 2023.
  https://openai.com/index/march-20-chatgpt-outage/ (checked 2026-10-08
  through the Internet Archive; the live site refuses scripts). A bug "allowed
  some users to see titles from another active user's chat history" and
  exposed payment details of "1.2% of the ChatGPT Plus subscribers" active
  in a nine-hour window. The Italian authority's EUR 15 million fine of
  2024, which cited this breach, was annulled by the Court of Rome on 18
  March 2026 (Garante press release,
  https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432,
  checked 2026-10-08): never cite it as standing.
- Shared chats in search engines. Fast Company (30 July 2025) and Forbes
  (20 August 2025).
  https://www.fastcompany.com/91376687/google-indexing-chatgpt-conversations,
  https://www.forbes.com/sites/iainmartin/2025/08/20/elon-musks-xai-published-hundreds-of-thousands-of-grok-chatbot-conversations/
  (checked 2026-10-08 through the Internet Archive). About 4,500 shared
  ChatGPT conversations, shared with an opt-in setting, appeared in Google;
  for Grok, "more than 370,000 user conversations", and uploaded
  "spreadsheets and some text documents" could be reached too. A share link
  is a publication.
- Wiz Research. "Wiz Research Uncovers Exposed DeepSeek Database Leaking
  Sensitive Information, Including Chat History". 29 January 2025.
  https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak
  (checked 2026-10-08). An open database with "over a million lines of log
  streams containing chat history, secret keys, backend details". Vendor
  research; no report of access by others.
- US District Court, S.D.N.Y. Preservation order in The New York Times v.
  Microsoft and OpenAI (ECF 551). 13 May 2025.
  https://storage.courtlistener.com/recap/gov.uscourts.nysd.612697/gov.uscourts.nysd.612697.551.0.pdf
  (checked 2026-10-08). OpenAI was "DIRECTED to preserve and segregate all
  output log data that would otherwise be deleted", "whether such data might
  be deleted at a user's request" or by law. OpenAI says the duty ended on
  26 September 2025 and "does not impact ChatGPT Enterprise or ChatGPT Edu
  customers" (https://openai.com/index/response-to-nyt-data-demands/,
  through the Internet Archive). "Deleted" is a promise a court can
  suspend; the plan and the contract decide what can be held.
- Johann Rehberger. "Claude Code: Data Exfiltration with DNS
  (CVE-2025-55284)". 11 August 2025.
  https://embracethered.com/blog/posts/2025/claude-code-exfiltration-via-dns-requests/
  (checked 2026-10-08). Planted text made Claude Code "leak sensitive
  information from the developer's machine, e.g. API keys, to external
  servers by issuing DNS requests"; fixed on 6 June 2025. A demonstration,
  on the paper's own tool.
- PromptArmor. "Claude Cowork Exfiltrates Files". January 2026.
  https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files
  (checked 2026-10-08). A hidden instruction in a document made Cowork
  upload a file with personal data through the allowlisted Anthropic API,
  to the attacker's account. A demonstration; whether and when it was
  fixed was not checked.
- Microsoft Threat Intelligence. "Securing CI/CD in an agentic world:
  Claude Code Github action case". 5 June 2026.
  https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/
  (checked 2026-10-08). Untrusted issue and pull request text could make
  the action read workflow secrets; Anthropic fixed it in 2.1.128 "by
  blocking access to sensitive /proc files". A lab demonstration.
- Aim Labs, "EchoLeak" (CVE-2025-32711, Microsoft 365 Copilot, June 2025),
  PromptArmor on Slack AI (August 2024) and Legit Security, "CamoLeak"
  (GitHub Copilot Chat, October 2025).
  https://www.aim.security/lp/aim-labs-echoleak-blogpost,
  https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via,
  https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code
  (checked 2026-10-08; Aim through the Internet Archive). Three assistants
  that read both private data and outside text, steered into sending the
  data out; all demonstrations by security vendors, all fixed.

### What went wrong: measurements

- Rocher, Hendrickx, de Montjoye. "Estimating the success of
  re-identifications in incomplete datasets using generative models".
  Nature Communications 10:3069, 23 July 2019.
  https://www.nature.com/articles/s41467-019-10933-3 (checked 2026-10-08).
  "99.98% of Americans would be correctly re-identified in any dataset
  using 15 demographic attributes." A model estimate on US census data, not
  about language models; it is why masked subject IDs are not enough.
- Carlini et al. "Extracting Training Data from Large Language Models"
  (USENIX Security 2021) and Nasr et al. "Scalable Extraction of Training
  Data from (Production) Language Models" (ICLR 2025).
  https://arxiv.org/abs/2012.07805, https://arxiv.org/abs/2311.17035
  (checked 2026-10-08, abstracts and venue pages). Training data can be
  recovered from models, "thousands of training examples from popular
  proprietary aligned models such as OpenAI's ChatGPT". This matters only
  where your inputs are used for training.
- Huang et al. "Your Code Secret Belongs to Me: Neural Code Completion
  Tools Can Memorize Hard-Coded Credentials" (FSE 2024). https://arxiv.org/abs/2309.07639 (checked
  2026-10-08). Code assistants reproduce credentials from their training
  data; the widely quoted 2,702 credentials are in the preprint only, the
  accepted version reports "two valid credentials".
- Netskope. "Threat Labs Report: Healthcare 2026". 3 March 2026.
  https://www.netskope.com/resources/threat-labs-reports/threat-labs-report-healthcare-2026
  (checked 2026-10-08). In healthcare, "regulated data overwhelmingly
  dominates exposures, accounting for 89% of incidents". Harmonic Security
  (22.4 million prompts, 15 January 2026,
  https://www.harmonic.security/resources/what-22-million-enterprise-ai-prompts-reveal-about-shadow-ai-in-2025)
  found 16.9% of sensitive exposures going "through personal free-tier
  accounts", and Cyberhaven (11 February 2026,
  https://www.cyberhaven.com/blog/sensitive-data-flowing-into-ai-tools)
  that "39.7 percent of all AI interactions involve sensitive data". All
  three sell tools against the problem and measure their own customers.

### Dependence: prices, terms and the way out

Read on 2026-10-08 by a research agent whose fetch tool extracted the
quotes; spot-check the wording on the page before a quote enters the
paper. The evidence supports a risk, not a forecast: subscription terms
have tightened, while prices per token have fallen.

- Anthropic. "Plans & pricing". https://claude.com/pricing (checked
  2026-10-08) [43]. "Price and plans are subject to change at Anthropic's
  discretion."
- Anthropic. "Model deprecations" (Claude Platform documentation).
  https://platform.claude.com/docs/en/about-claude/model-deprecations
  (checked 2026-10-08) [44]. "at least 60 days' notice before model retirement
  for publicly released models"; "Requests to retired models fail." These
  dates apply to Anthropic-operated platforms; Amazon Bedrock and Google
  Cloud's Agent Platform "set their own retirement schedules" (read
  2026-10-26). Claude Sonnet 4.5 retires from the Claude API on 30 November
  2026, the month of the conference. A validated workflow pinned to one model meets this date.
- Anthropic's weekly limits for Claude Code. TechCrunch, "Anthropic unveils
  new rate limits to curb Claude Code power users", 28 July 2025, and the
  Claude Help Center, "Claude Code May–August 2026 weekly limits promotion".
  https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/,
  https://support.claude.com/en/articles/15910845 (checked 2026-10-08).
  Weekly limits came in August 2025; a 2026 promotion raised them by 50%,
  and from 14 September 2026 they are 25% above the old level.
- GitHub (Mario Rodriguez). "GitHub Copilot is moving to usage-based
  billing". 27 April 2026.
  https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
  (checked 2026-10-08). "GitHub has absorbed much of the escalating
  inference cost behind that usage", and "the current premium request model
  is no longer sustainable." The clearest admission by a vendor that the
  old price did not cover the cost. Cursor's apology for its June 2025
  change ("Clarifying our pricing", https://cursor.com/blog/june-2025-pricing,
  checked 2026-10-08) is the earlier case.
- Epoch AI (Jack Edwards, Luke Emberson). "Open models lag state-of-the-art
  closed models by 4 months". 29 May 2026.
  https://epoch.ai/data-insights/open-closed-eci-gap (checked 2026-10-08;
  left out of chapter 10 for space, which states the way out as a
  condition: if open-weight models keep improving). "Since January 2026, the most capable open-weight models have lagged
  frontier closed models by an average of four months." In October 2025
  Epoch measured about three months
  (https://epoch.ai/data-insights/open-weights-vs-closed-weights-models).
- Stanford HAI. "The 2026 AI Index Report", chapter Technical Performance.
  https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance
  (checked 2026-10-08). "The open model performance gap reopened in 2025
  after briefly closing in 2024"; "As of March 2026, the top closed model
  leads the top open model by 3.3%, up from 0.5% in August 2024." On the
  chatbot leaderboard, not on coding. The 2025 report had the gap shrinking
  from 8.04% to 1.70%.
- Against the hope: on hard agentic coding, open models stay clearly behind.
  Artificial Analysis, "Recent open weights model launches", 30 April 2026,
  https://www.artificialanalysis.ai/articles/recent-open-weights-model-launches:
  "The gap to proprietary remains wide on the hardest reasoning and agentic
  coding evaluations." NIST CAISI, "CAISI Evaluation of DeepSeek V4 Pro", 1
  May 2026,
  https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro:
  about "8 months" behind the frontier, and better on its own evaluations
  than on CAISI's. Epoch rates SWE-bench Verified "Flawed"
  (https://epoch.ai/benchmarks/swe-bench-verified/review). All checked
  2026-10-08.
- Running them yourself. Moonshot AI's deployment guide puts the smallest
  vLLM deployment of Kimi K2, for "FP8 weights with 128k seqlen on
  mainstream H200 or H20 platform", at "a cluster with 16 GPUs"
  (https://github.com/MoonshotAI/Kimi-K2/blob/main/docs/deploy_guidance.md,
  read again 2026-10-28);
  gpt-oss-120b runs "on a single 80GB GPU", gpt-oss-20b "within 16GB of
  memory" (https://huggingface.co/openai/gpt-oss-120b). A preprint puts the
  break-even of in-house large models at about five years (Pan et al.,
  https://arxiv.org/abs/2509.18101), and Epoch finds prices at constant
  performance falling "between 9x and 900x per year"
  (https://epoch.ai/data-insights/llm-inference-price-trends). All checked
  2026-10-08.
- Anthropic. "Other LLM gateways" (Claude Code documentation).
  https://code.claude.com/docs/en/llm-gateway (checked 2026-10-08) [46].
  Anthropic "doesn't support routing Claude Code to non-Claude models
  through any gateway." vLLM and Ollama document how to do it anyway; the
  supported way out is another agent, such as Codex CLI, OpenCode or Aider,
  which run local models.
- Portability. Linux Foundation, "Linux Foundation Announces the Formation
  of the Agentic AI Foundation (AAIF), Anchored by New Project Contributions
  Including Model Context Protocol (MCP), goose and AGENTS.md", 9 December
  2025,
  https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation:
  MCP, goose and AGENTS.md under one neutral foundation. https://agents.md/
  lists Codex, Cursor, Copilot's coding agent, Gemini CLI and others;
  https://agentskills.io/ lists the clients of the open skills format,
  among them Codex, Gemini CLI, GitHub Copilot, Cursor and OpenCode. OpenCode
  reads `CLAUDE.md` as a fallback, and Copilot reads skills from
  `.claude/skills`. Hooks, permission rules and subagents belong to no
  standard and stay with the tool. All checked 2026-10-08.
- ANSSI and BSI. "AI Coding Assistants" (above), section 4.1: "local hosting
  of open-source models can prevent the loss of sensitive information";
  section 3.2: "Programmers should be able to continue business operations
  without AI assistance (e.g. in case of incident)."
- Bundesnetzagentur. "Data processing services and provider switching" (EU
  Data Act).
  https://bundesnetzagentur.de/EN/Areas/Digitalisation/DataAct/background/3-provider/start.html
  (checked 2026-10-08). "From 12 January 2027, no switching charges at all
  may be imposed" for cloud services; whether an AI service is covered is a
  legal question the page does not answer.

## Practitioners

- Boris Cherny. Thread on using Claude Code day to day, posted on X on 2
  January 2026. https://x.com/bcherny/status/2007179832300581177, read through
  Thread Reader App:
  https://threadreaderapp.com/thread/2007179832300581177.html (checked
  2026-10-06; read again 2026-10-08, when X served the thread without a
  login; it left the paper on 2026-10-27, when the Conclusion was cut
  short at the author's request). The first post opens "I'm Boris and I created Claude Code."
  The thread: "My setup might be surprisingly vanilla!
  Claude Code works great out of the box, so I personally don't customize
  it much." The same thread then lists the paper's mechanisms at team
  level: "Our team shares a single CLAUDE.md for the Claude Code repo. We
  check it into git, and the whole team contributes multiple times a week.
  Anytime we see Claude do something incorrectly we add it to the
  CLAUDE.md"; slash
  commands checked into git; subagents such as code-simplifier and
  verify-app; a PostToolUse hook that formats code; "I don't use
  --dangerously-skip-permissions", with safe commands pre-allowed in a
  shared `.claude/settings.json` instead. Its closing tip: "give Claude a way
  to verify its work. If Claude has that feedback loop, it will 2-3x the
  quality of the final result." The 2-3x is his estimate, not a measurement.
  Post 12 adds that for long tasks he does use "--permission-mode=dontAsk or
  --dangerously-skip-permissions in a sandbox", which matches chapter 8. A
  counterpoint in tone, an endorsement in substance: few personal tweaks on
  top of team rules that are written down.
- Fortune (Sharon Goldman). "Anthropic's Boris Cherny, creator of Claude
  Code, says there are days he manages tens of thousands of AI agents at
  once". 8 June 2026.
  https://fortune.com/2026/06/08/anthropics-boris-cherny-creator-of-claude-code-says-there-are-days-he-manages-tens-of-thousands-of-ai-agents-at-once/
  (checked 2026-10-08; Fortune refuses requests without a browser user
  agent; it left the paper on 2026-10-08, since the thread's own first line
  says who he is). "Boris Cherny, the creator and head of Anthropic's Claude
  Code, hasn't handwritten a line of code in eight months."
- Park, Arvi, Lee, Lim, Ma, Kim. "The Work Behind Delegation: A Framework for
  Supervising AI Coding Agents". September 2026.
  https://arxiv.org/abs/2609.24234 (checked 2026-10-06). 19 experienced
  developers: they concentrate effort in planning, delegate supervision to
  other agents, and turn "recurring guidance into reusable assets", the step
  from chat to `CLAUDE.md` and skills.
