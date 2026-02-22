# How I think about Codex

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-22T15:53:43+00:00
**链接:** https://simonwillison.net/2026/Feb/22/how-i-think-about-codex/#atom-everything

---

<p><strong><a href="https://www.linkedin.com/pulse/how-i-think-codex-gabriel-chua-ukhic">How I think about Codex</a></strong></p>
Gabriel Chua (Developer Experience Engineer for APAC at OpenAI) provides his take on the confusing terminology behind the term "Codex", which can refer to a bunch of of different things within the OpenAI ecosystem:</p>
<blockquote>
<p>In plain terms, Codex is OpenAI’s software engineering agent, available through multiple interfaces, and an agent is a model plus instructions and tools, wrapped in a runtime that can execute tasks on your behalf. [...]</p>
<p>At a high level, I see Codex as three parts working together:</p>
<p><em>Codex = Model + Harness + Surfaces</em> [...]</p>
<ul>
<li>Model + Harness = the Agent</li>
<li>Surfaces = how you interact with the Agent</li>
</ul>
</blockquote>
<p>He defines the harness as "the collection of instructions and tools", which is notably open source and lives in the <a href="https://github.com/openai/codex">openai/codex</a> repository.</p>
<p>Gabriel also provides the first acknowledgment I've seen from an OpenAI insider that the Codex model family are directly trained for the Codex harness:</p>
<blockquote>
<p>Codex models are trained in the presence of the harness. Tool use, execution loops, compaction, and iterative verification aren’t bolted on behaviors — they’re part of how the model learns to operate. The harness, in turn, is shaped around how the model plans, invokes tools, and recovers from failure.</p>
</blockquote>


    <p>Tags: <a href="https://simonwillison.net/tags/definitions">definitions</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/codex-cli">codex-cli</a></p>

---

*抓取时间: 2026-02-23 00:07:01*
