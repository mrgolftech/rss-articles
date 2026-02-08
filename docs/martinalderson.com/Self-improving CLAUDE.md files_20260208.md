# Self-improving CLAUDE.md files

**来源:** [martinalderson.com](https://martinalderson.com)
**发布时间:** Sun, 08 Feb 2026 00:00:00 GMT
**链接:** https://martinalderson.com/posts/self-improving-claude-md-files/?utm_source=rss

---

One of the biggest things to improve how agentic tools like Claude Code/Cowork and Codex work is by using CLAUDE.md or AGENTS.md files
[1]
- which give the agent context on the project.
I have found that it starts out being easy to keep on track of them with new projects, but quickly becomes a nightmare to keep them updated as complexity grows, and doing it by hand is quite tedious.
One quick trick I figured out recently is to use the agent's logs to identify common problems with the CLAUDE.md file. With Claude Code, these sessions are stored in
~/.claude/projects
, with Codex storing them in
~/.codex/sessions
. These agent logs are JSONL files which contain everything that happened in the agent session, including what
you
asked the agent to do, what
it
did. NB - while both use JSONL format files, the schema is totally different.
Now the "trick" is to get the agent to search through your existing chat logs and reference the current CLAUDE.md to spot potential optimisation efforts. This works ludicrously well in my experience and takes updating CLAUDE.md from a chore to a 30 second job for each project.
A prompt like "please search through my claude jsonl history files for this project, and analyse improvements to the current claude.md file. Note any times I get frustrated or any patterns of me asking the same thing between sessions" works very well.
One issue I did have was it struggles a bit to parse the JSONL efficiently, writing superhuman-level complexity jq bash commands.
As such I built a little CLI to abstract the searching - I've
open sourced it on GitHub
with prebuilt binaries for Mac and Linux, but I suspect this screenshot alone is enough to allow your agent to build one exactly to your liking (!):
This allows the agent to search the logs
extremely
efficiently. Without it, it took a good few minutes to come up with suggestions on projects with even a moderate amount of chat sessions to analyse - with it, a few seconds. There's really no reason this couldn't run as a scheduled task every day/week and just improve itself. I've found that curating the suggestions quickly helps, but I'm sure with a more detailed prompt it could be better at self-improving itself.
I hope this is useful. I've got some further thoughts on how to manage this in an organisation/enterprise sense at scale, but in the meantime enjoy a much easier CLAUDE.md file.
I really wish Anthropic would adopt AGENTS.md, if for no other reason than making my writing less clunky.
↩︎
If you found this useful, I send a newsletter every month with all my posts. No spam and no ads.
Subscribe

---

*抓取时间: 2026-02-09 06:02:19*
