# OpenAI’s Codex

**来源:** https://daringfireball.net
**链接:** https://simonwillison.net/2026/Feb/2/introducing-the-codex-app/
**日期:** 2026-02-04T01:40:24Z

---

# [Simon Willison’s Weblog](/)

[Subscribe](/about/#subscribe)

**[Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)**. OpenAI just released a new macOS app for their Codex coding agent. I've had a few days of preview access - it's a solid app that provides a nice UI over the capabilities of the Codex CLI agent and adds some interesting new features, most notably first-class support for [Skills](https://developers.openai.com/codex/skills), and [Automations](https://developers.openai.com/codex/app/automations) for running scheduled tasks.

![Screenshot of a macOS desktop application with a dark sidebar and light main content area. Left sidebar shows navigation items "New thread", "Automations", "Skills", and a "Threads" section containing two project folders: "local-codex-scratch" with tasks "Reply to greeting task 2h" and "List Codex.app contents 3h", and "shot-scraper" with tasks "Validate tests on dependency... 3h", "Document shot-scraper CLI usage 18h" \(highlighted\), and "Run this: uv run pytest -x 1d". Bottom left shows "Personal". Top bar displays "Document shot-scraper CLI usage shot-scraper" with "Open" and "Commit" dropdown buttons. Main content shows a conversation: user message "Build a skill describing how to use the shot-scraper CLI tool" followed by assistant responses: "I'll use the skill-creator skill, scan the repo for existing shot-scraper docs/commands, then draft a concise skill in this workspace and sanity-check it." then "I've confirmed the skill-creator scripts exist. Next I'll inspect the CLI entrypoint and docs, then scaffold a skill under skills/ in this repo." then "I've scaffolded skills/shot-scraper-cli/. I'll now replace the template SKILL.md with a task-focused skill and add a compact CLI reference under references/." then "I'll run the skill packager/validator next to ensure the new skill structure is valid." then "Done — I created and packaged the skill. Key outputs: • Skill definition: SKILL.md • Compact reference: cli-reference.md • Packaged skill: shot-scraper-cli.skill". Bottom shows input field with placeholder "Ask for follow-up changes", "+ Custom Medium" dropdown, and "Local" and "main" branch indicators.](https://static.simonwillison.net/static/2026/codex-app.jpg)

The app is built with Electron and Node.js. Automations track their state in a SQLite database - here's what that looks like if you explore it with `uvx datasette ~/.codex/sqlite/codex-dev.db`:

![Database schema documentation on light gray background showing three tables: "automation_runs" \(teal underlined link\) with italic columns "thread_id, automation_id, status, read_at, thread_title, source_cwd, inbox_title, inbox_summary, created_at, updated_at, archived_user_message, archived_assistant_message, archived_reason" and "1 row"; "automations" \(teal underlined link\) with italic columns "id, name, prompt, status, next_run_at, last_run_at, cwds, rrule, created_at, updated_at" and "1 row"; "inbox_items" \(teal underlined link\) with italic columns "id, title, description, thread_id, read_at, created_at" and "0 rows".](https://static.simonwillison.net/static/2026/codex-dev-sqlite.jpg)

Here’s an interactive copy of that database [in Datasette Lite](https://lite.datasette.io/?url=https%3A%2F%2Fgist.githubusercontent.com%2Fsimonw%2F274c4ecfaf959890011810e6881864fe%2Fraw%2F51fdf25c9426b76e9693ccc0d9254f64ceeef819%2Fcodex-dev.db#/codex-dev).

The announcement gives us a hint at some usage numbers for Codex overall - the holiday spike is notable:

> Since the launch of GPT‑5.2-Codex in mid-December, overall Codex usage has doubled, and in the past month, more than a million developers have used Codex.

Automations are currently restricted in that they can only run when your laptop is powered on. OpenAI promise that cloud-based automations are coming soon, which will resolve this limitation.

They chose Electron so they could target other operating systems in the future, with Windows “[coming very soon](https://news.ycombinator.com/item?id=46859054#46859673)”. OpenAI’s Alexander Embiricos noted [on the Hacker News thread](https://news.ycombinator.com/item?id=46859054#46859693) that:

> it's taking us some time to get really solid sandboxing working on Windows, where there are fewer OS-level primitives for it.

Like Claude Code, Codex is really a general agent harness disguised as a tool for programmers. OpenAI acknowledge that here:

> Codex is built on a simple premise: everything is controlled by code. The better an agent is at reasoning about and producing code, the more capable it becomes across all forms of technical and knowledge work. [...] We’ve focused on making Codex the best coding agent, which has also laid the foundation for it to become a strong agent for a broad range of knowledge work tasks that extend beyond writing code.

Claude Code had to [rebrand to Cowork](https://simonwillison.net/2026/Jan/12/claude-cowork/) to better cover the general knowledge work case. OpenAI can probably get away with keeping the Codex name for both.

OpenAI have made Codex available to free and [Go](https://simonwillison.net/2026/Jan/16/chatgpt-ads/) plans for "a limited time" (update: Sam Altman [says two months](https://x.com/sama/status/2018437537103269909)) during which they are also doubling the rate limits for paying users.

Posted [2nd February 2026](/2026/Feb/2/) at 7:54 pm

## Recent articles

  * [Distributing Go binaries like sqlite-scanner through PyPI using go-to-wheel](/2026/Feb/4/distributing-go-binaries/) \- 4th February 2026
  * [Moltbook is the most interesting place on the internet right now](/2026/Jan/30/moltbook/) \- 30th January 2026
  * [Adding dynamic features to an aggressively cached website](/2026/Jan/28/dynamic-features-static-site/) \- 28th January 2026



[ sandboxing 33 ](/tags/sandboxing/) [ sqlite 312 ](/tags/sqlite/) [ ai 1814 ](/tags/ai/) [ datasette 454 ](/tags/datasette/) [ electron 9 ](/tags/electron/) [ openai 387 ](/tags/openai/) [ generative-ai 1606 ](/tags/generative-ai/) [ llms 1572 ](/tags/llms/) [ ai-agents 101 ](/tags/ai-agents/) [ coding-agents 137 ](/tags/coding-agents/) [ codex-cli 22 ](/tags/codex-cli/)

###  Monthly briefing 

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments. 

Pay me to send you less! 

[ Sponsor & subscribe ](https://github.com/sponsors/simonw/)

  * [Colophon](/about/#about-site)
  * (C)
  * [2002](/2002/)
  * [2003](/2003/)
  * [2004](/2004/)
  * [2005](/2005/)
  * [2006](/2006/)
  * [2007](/2007/)
  * [2008](/2008/)
  * [2009](/2009/)
  * [2010](/2010/)
  * [2011](/2011/)
  * [2012](/2012/)
  * [2013](/2013/)
  * [2014](/2014/)
  * [2015](/2015/)
  * [2016](/2016/)
  * [2017](/2017/)
  * [2018](/2018/)
  * [2019](/2019/)
  * [2020](/2020/)
  * [2021](/2021/)
  * [2022](/2022/)
  * [2023](/2023/)
  * [2024](/2024/)
  * [2025](/2025/)
  * [2026](/2026/)
  * 

