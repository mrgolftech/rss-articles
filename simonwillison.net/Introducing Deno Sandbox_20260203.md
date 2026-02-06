# Introducing Deno Sandbox

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-03T22:44:50+00:00
**链接:** https://simonwillison.net/2026/Feb/3/introducing-deno-sandbox/#atom-everything

---

<p><strong><a href="https://deno.com/blog/introducing-deno-sandbox">Introducing Deno Sandbox</a></strong></p>
Here's a new hosted sandbox product from the Deno team. It's actually unrelated to Deno itself - this is part of their Deno Deploy SaaS platform. As such, you don't even need to use JavaScript to access it - you can create and execute code in a hosted sandbox using their <a href="https://pypi.org/project/deno-sandbox/">deno-sandbox</a> Python library like this:</p>
<div class="highlight highlight-source-shell"><pre><span class="pl-k">export</span> DENO_DEPLOY_TOKEN=<span class="pl-s"><span class="pl-pds">"</span>... API token ...<span class="pl-pds">"</span></span>
uv run --with deno-sandbox python</pre></div>
<p>Then:</p>
<pre><span class="pl-k">from</span> <span class="pl-s1">deno_sandbox</span> <span class="pl-k">import</span> <span class="pl-v">DenoDeploy</span>

<span class="pl-s1">sdk</span> <span class="pl-c1">=</span> <span class="pl-en">DenoDeploy</span>()

<span class="pl-k">with</span> <span class="pl-s1">sdk</span>.<span class="pl-c1">sandbox</span>.<span class="pl-c1">create</span>() <span class="pl-k">as</span> <span class="pl-s1">sb</span>:
    <span class="pl-c"># Run a shell command</span>
    <span class="pl-s1">process</span> <span class="pl-c1">=</span> <span class="pl-s1">sb</span>.<span class="pl-c1">spawn</span>(
        <span class="pl-s">"echo"</span>, <span class="pl-s1">args</span><span class="pl-c1">=</span>[<span class="pl-s">"Hello from the sandbox!"</span>]
    )
    <span class="pl-s1">process</span>.<span class="pl-c1">wait</span>()
    <span class="pl-c"># Write and read files</span>
    <span class="pl-s1">sb</span>.<span class="pl-c1">fs</span>.<span class="pl-c1">write_text_file</span>(
        <span class="pl-s">"/tmp/example.txt"</span>, <span class="pl-s">"Hello, World!"</span>
    )
    <span class="pl-en">print</span>(<span class="pl-s1">sb</span>.<span class="pl-c1">fs</span>.<span class="pl-c1">read_text_file</span>(
        <span class="pl-s">"/tmp/example.txt"</span>
    ))</pre>
<p>There’s a JavaScript client library as well. The underlying API isn’t documented yet but appears <a href="https://tools.simonwillison.net/zip-wheel-explorer?package=deno-sandbox#deno_sandbox/sandbox.py--L187">to use WebSockets</a>.</p>
<p>There’s a lot to like about this system. Sandboxe instances can have up to 4GB of RAM, get 2 vCPUs, 10GB of ephemeral storage, can mount persistent volumes and can use snapshots to boot pre-configured custom images quickly. Sessions can last up to 30 minutes and are billed by CPU time, GB-h of memory and volume storage usage.</p>
<p>When you create a sandbox you can configure network domains it’s allowed to access.</p>
<p>My favorite feature is the way it handles API secrets.</p>
<pre><span class="pl-k">with</span> <span class="pl-s1">sdk</span>.<span class="pl-c1">sandboxes</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">allowNet</span><span class="pl-c1">=</span>[<span class="pl-s">"api.openai.com"</span>],
    <span class="pl-s1">secrets</span><span class="pl-c1">=</span>{
        <span class="pl-s">"OPENAI_API_KEY"</span>: {
            <span class="pl-s">"hosts"</span>: [<span class="pl-s">"api.openai.com"</span>],
            <span class="pl-s">"value"</span>: <span class="pl-s1">os</span>.<span class="pl-c1">environ</span>.<span class="pl-c1">get</span>(<span class="pl-s">"OPENAI_API_KEY"</span>),
        }
    },
) <span class="pl-k">as</span> <span class="pl-s1">sandbox</span>:
    <span class="pl-c"># ... $OPENAI_API_KEY is available</span></pre>
<p>Within the container that <code>$OPENAI_API_KEY</code> value is set to something like this:</p>
<pre><code>DENO_SECRET_PLACEHOLDER_b14043a2f578cba...
</code></pre>
<p>Outbound API calls to <code>api.openai.com</code> run through a proxy which is aware of those placeholders and replaces them with the original secret.</p>
<p>In this way the secret itself is not available to code within the sandbox, which limits the ability for malicious code (e.g. from a prompt injection) to exfiltrate those secrets.</p>
<p>From <a href="https://news.ycombinator.com/item?id=46874097#46874959">a comment on Hacker News</a> I learned that Fly have a project called <a href="https://github.com/superfly/tokenizer">tokenizer</a> that implements the same pattern. Adding this to my list of tricks to use with sandoxed environments!

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=46874097">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/sandboxing">sandboxing</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/deno">deno</a>, <a href="https://simonwillison.net/tags/fly">fly</a></p>

---

*抓取时间: 2026-02-06 06:02:30*
