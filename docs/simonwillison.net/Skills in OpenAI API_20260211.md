# Skills in OpenAI API

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-11T19:19:22+00:00
**链接:** https://simonwillison.net/2026/Feb/11/skills-in-openai-api/#atom-everything

---

<p><strong><a href="https://developers.openai.com/cookbook/examples/skills_in_api">Skills in OpenAI API</a></strong></p>
OpenAI's adoption of Skills continues to gain ground. You can now use Skills directly in the OpenAI API with their <a href="https://developers.openai.com/api/docs/guides/tools-shell/">shell tool</a>. You can zip skills up and upload them first, but I think an even neater interface is the ability to send skills with the JSON request as inline base64-encoded zip data, as seen <a href="https://github.com/simonw/research/blob/main/openai-api-skills/openai_inline_skills.py">in this script</a>:</p>
<pre><span class="pl-s1">r</span> <span class="pl-c1">=</span> <span class="pl-en">OpenAI</span>().<span class="pl-c1">responses</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"gpt-5.2"</span>,
    <span class="pl-s1">tools</span><span class="pl-c1">=</span>[
      {
        <span class="pl-s">"type"</span>: <span class="pl-s">"shell"</span>,
        <span class="pl-s">"environment"</span>: {
          <span class="pl-s">"type"</span>: <span class="pl-s">"container_auto"</span>,
          <span class="pl-s">"skills"</span>: [
            {
              <span class="pl-s">"type"</span>: <span class="pl-s">"inline"</span>,
              <span class="pl-s">"name"</span>: <span class="pl-s">"wc"</span>,
              <span class="pl-s">"description"</span>: <span class="pl-s">"Count words in a file."</span>,
              <span class="pl-s">"source"</span>: {
                <span class="pl-s">"type"</span>: <span class="pl-s">"base64"</span>,
                <span class="pl-s">"media_type"</span>: <span class="pl-s">"application/zip"</span>,
                <span class="pl-s">"data"</span>: <span class="pl-s1">b64_encoded_zip_file</span>,
              },
            }
          ],
        },
      }
    ],
    <span class="pl-s1">input</span><span class="pl-c1">=</span><span class="pl-s">"Use the wc skill to count words in its own SKILL.md file."</span>,
)
<span class="pl-en">print</span>(<span class="pl-s1">r</span>.<span class="pl-c1">output_text</span>)</pre>

<p>I built that example script after first having Claude Code for web use <a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/">Showboat</a> to explore the API for me and create <a href="https://github.com/simonw/research/blob/main/openai-api-skills/README.md">this report</a>. My opening prompt for the research project was:</p>
<blockquote>
<p><code>Run uvx showboat --help - you will use this tool later</code></p>
<p><code>Fetch https://developers.openai.com/cookbook/examples/skills_in_api.md to /tmp with curl, then read it</code></p>
<p><code>Use the OpenAI API key you have in your environment variables</code></p>
<p><code>Use showboat to build up a detailed demo of this, replaying the examples from the documents and then trying some experiments of your own</code></p>
</blockquote>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/skills">skills</a>, <a href="https://simonwillison.net/tags/showboat">showboat</a></p>

---

*抓取时间: 2026-02-12 06:02:37*
