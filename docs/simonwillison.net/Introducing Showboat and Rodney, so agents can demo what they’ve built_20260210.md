# Introducing Showboat and Rodney, so agents can demo what they’ve built

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-10T17:45:29+00:00
**链接:** https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#atom-everything

---

<p>A key challenge working with coding agents is having them both test what they’ve built and demonstrate that software to you, their overseer. This goes beyond automated tests - we need artifacts that show their progress and help us see exactly what the agent-produced software is able to do. I’ve just released two new tools aimed at this problem: <a href="https://github.com/simonw/showboat">Showboat</a> and <a href="https://github.com/simonw/rodney">Rodney</a>.</p>

<ul>
  <li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#proving-code-actually-works">Proving code actually works</a></li>
  <li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#showboat-agents-build-documents-to-demo-their-work">Showboat: Agents build documents to demo their work</a></li>
  <li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#rodney-cli-browser-automation-designed-to-work-with-showboat">Rodney: CLI browser automation designed to work with Showboat</a></li>
  <li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#test-driven-development-helps-but-we-still-need-manual-testing">Test-driven development helps, but we still need manual testing</a></li>
  <li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#i-built-both-of-these-tools-on-my-phone">I built both of these tools on my phone</a></li>
</ul>

<h4 id="proving-code-actually-works">Proving code actually works</h4>
<p>I recently wrote about how the job of a software engineer isn't to write code, it's to <em><a href="https://simonwillison.net/2025/Dec/18/code-proven-to-work/">deliver code that works</a></em>. A big part of that is proving to ourselves and to other people that the code we are responsible for behaves as expected.</p>
<p>This becomes even more important - and challenging - as we embrace coding agents as a core part of our software development process.</p>
<p>The more code we churn out with agents, the more valuable tools are that reduce the amount of manual QA time we need to spend.</p>
<p>One of the most interesting things about <a href="https://simonwillison.net/2026/Feb/7/software-factory/">the StrongDM software factory model</a> is how they ensure that their software is well tested and delivers value despite their policy that "code must not be reviewed by humans". Part of their solution involves expensive swarms of QA agents running through "scenarios" to exercise their software. It's fascinating, but I don't want to spend thousands of dollars on QA robots if I can avoid it!</p>
<p>I need tools that allow agents to clearly demonstrate their work to me, while minimizing the opportunities for them to cheat about what they've done.</p>

<h4 id="showboat-agents-build-documents-to-demo-their-work">Showboat: Agents build documents to demo their work</h4>
<p><strong><a href="https://github.com/simonw/showboat">Showboat</a></strong> is the tool I built to help agents demonstrate their work to me.</p>
<p>It's a CLI tool (a Go binary, optionally <a href="https://simonwillison.net/2026/Feb/4/distributing-go-binaries/">wrapped in Python</a> to make it easier to install) that helps an agent construct a Markdown document demonstrating exactly what their newly developed code can do.</p>
<p>It's not designed for humans to run, but here's how you would run it anyway:</p>
<div class="highlight highlight-source-shell"><pre>showboat init demo.md <span class="pl-s"><span class="pl-pds">'</span>How to use curl and jq<span class="pl-pds">'</span></span>
showboat note demo.md <span class="pl-s"><span class="pl-pds">"</span>Here's how to use curl and jq together.<span class="pl-pds">"</span></span>
showboat <span class="pl-c1">exec</span> demo.md bash <span class="pl-s"><span class="pl-pds">'</span>curl -s https://api.github.com/repos/simonw/rodney | jq .description<span class="pl-pds">'</span></span>
showboat note demo.md <span class="pl-s"><span class="pl-pds">'</span>And the curl logo, to demonstrate the image command:<span class="pl-pds">'</span></span>
showboat image demo.md <span class="pl-s"><span class="pl-pds">'</span>curl -o curl-logo.png https://curl.se/logo/curl-logo.png &amp;&amp; echo curl-logo.png<span class="pl-pds">'</span></span></pre></div>
<p>Here's what the result looks like if you open it up in VS Code and preview the Markdown:</p>
<p><img alt="Screenshot showing a Markdown file &quot;demo.md&quot; side-by-side with its rendered preview. The Markdown source (left) shows: &quot;# How to use curl and jq&quot;, italic timestamp &quot;2026-02-10T01:12:30Z&quot;, prose &quot;Here's how to use curl and jq together.&quot;, a bash code block with &quot;curl -s https://api.github.com/repos/simonw/rodney | jq .description&quot;, output block showing '&quot;CLI tool for interacting with the web&quot;', text &quot;And the curl logo, to demonstrate the image command:&quot;, a bash {image} code block with &quot;curl -o curl-logo.png https://curl.se/logo/curl-logo.png &amp;&amp; echo curl-logo.png&quot;, and a Markdown image reference &quot;2056e48f-2026-02-10&quot;. The rendered preview (right) displays the formatted heading, timestamp, prose, styled code blocks, and the curl logo image in dark teal showing &quot;curl://&quot; with circuit-style design elements." src="https://static.simonwillison.net/static/2026/curl-demo.jpg" /></p>
<p>Here's that <a href="https://gist.github.com/simonw/fb0b24696ed8dd91314fe41f4c453563#file-demo-md">demo.md file in a Gist</a>.</p>
<p>So a sequence of <code>showboat init</code>, <code>showboat note</code>, <code>showboat exec</code> and <code>showboat image</code> commands constructs a Markdown document one section at a time, with the output of those <code>exec</code> commands automatically added to the document directly following the commands that were run.</p>
<p>The <code>image</code> command is a little special - it looks for a file path to an image in the output of the command and copies that image to the current folder and references it in the file.</p>
<p>That's basically the whole thing! There's a <code>pop</code> command to remove the most recently added section if something goes wrong, a <code>verify</code> command to re-run the document and check nothing has changed (I'm not entirely convinced by the design of that one) and a <code>extract</code> command that reverse-engineers the CLI commands that were used to create the document.</p>
<p>It's pretty simple - just 172 lines of Go.</p>
<p>I packaged it up with my <a href="https://github.com/simonw/go-to-wheel">go-to-wheel</a> tool which means you can run it without even installing it first like this:</p>
<div class="highlight highlight-source-shell"><pre>uvx showboat --help</pre></div>
<p>That <code>--help</code> command is really important: it's designed to provide a coding agent with <em>everything it needs to know</em> in order to use the tool. Here's <a href="https://github.com/simonw/showboat/blob/main/help.txt">that help text in full</a>.</p>
<p>This means you can pop open Claude Code and tell it:</p>
<blockquote>
<p><code>Run "uvx showboat --help" and then use showboat to create a demo.md document describing the feature you just built</code></p>
</blockquote>
<p>And that's it! The <code>--help</code> text acts <a href="https://simonwillison.net/2025/Oct/16/claude-skills/">a bit like a Skill</a>. Your agent can read the help text and use every feature of Showboat to create a document that demonstrates whatever it is you need demonstrated.</p>
<p>Here's a fun trick: if you set Claude off to build a Showboat document you can pop that open in VS Code and watch the preview pane update in real time as the agent runs through the demo. It's a bit like having your coworker talk you through their latest work in a screensharing session.</p>
<p>And finally, some examples. Here are documents I had Claude create using Showboat to help demonstrate features I was working on in other projects:</p>
<ul>
<li>
<a href="https://github.com/simonw/showboat-demos/blob/main/shot-scraper/README.md">shot-scraper: A Comprehensive Demo</a> runs through the full suite of features of my <a href="https://shot-scraper.datasette.io/">shot-scraper</a> browser automation tool, mainly to exercise the <code>showboat image</code> command.</li>
<li>
<a href="https://github.com/simonw/sqlite-history-json/blob/main/demos/cli.md">sqlite-history-json CLI demo</a> demonstrates the CLI feature I added to my new <a href="https://github.com/simonw/sqlite-history-json">sqlite-history-json</a> Python library.
<ul>
<li>
<p><a href="https://github.com/simonw/sqlite-history-json/blob/main/demos/row-state-sql.md">row-state-sql CLI Demo</a> shows a new <code>row-state-sql</code> command I added to that same project.</p>
</li>
<li>
<p><a href="https://github.com/simonw/sqlite-history-json/blob/main/demos/change-grouping.md">Change grouping with Notes</a> demonstrates another feature where groups of changes within the same transaction can have a note attached to them.</p>
</li>
</ul>
</li>
<li>
<a href="https://github.com/simonw/research/blob/main/libkrun-go-cli-tool/demo.md">krunsh: Pipe Shell Commands to an Ephemeral libkrun MicroVM</a> is a particularly convoluted example where I managed to get Claude Code for web to run a libkrun microVM inside a QEMU emulated Linux environment inside the Claude gVisor sandbox.</li>
</ul>
<p>I've now used Showboat often enough that I've convinced myself of its utility.</p>
<p>(I've also seen agents cheat! Since the demo file is Markdown the agent will sometimes edit that file directly rather than using Showboat, which could result in command outputs that don't reflect what actually happened. Here's <a href="https://github.com/simonw/showboat/issues/12">an issue about that</a>.)</p>
<h4 id="rodney-cli-browser-automation-designed-to-work-with-showboat">Rodney: CLI browser automation designed to work with Showboat</h4>
<p>Many of the projects I work on involve web interfaces. Agents often build entirely new pages for these, and I want to see those represented in the demos.</p>
<p>Showboat's image feature was designed to allow agents to capture screenshots as part of their demos, originally using my <a href="https://shot-scraper.datasette.io/">shot-scraper tool</a> or <a href="https://www.playwright.dev">Playwright</a>.</p>
<p>The Showboat format benefits from CLI utilities. I went looking for good options for managing a multi-turn browser session from a CLI and came up short, so I decided to try building something new.</p>
<p>Claude Opus 4.6 pointed me to the <a href="https://github.com/go-rod/rod">Rod</a> Go library for interacting with the Chrome DevTools protocol. It's fantastic - it provides a comprehensive wrapper across basically everything you can do with automated Chrome, all in a self-contained library that compiles to a few MBs.</p>
<p>All Rod was missing was a CLI.</p>
<p>I built the first version <a href="https://github.com/simonw/research/blob/main/go-rod-cli/README.md">as an asynchronous report prototype</a>, which convinced me it was worth spinning out into its own project.</p>
<p>I called it Rodney as a nod to the Rod library it builds on and a reference to <a href="https://en.wikipedia.org/wiki/Only_Fools_and_Horses">Only Fools and Horses</a> - and because the package name was available on PyPI.</p>
<p>You can run Rodney using <code>uvx rodney</code> or install it like this:</p>
<div class="highlight highlight-source-shell"><pre>uv tool install rodney</pre></div>
<p>(Or grab a Go binary <a href="https://github.com/simonw/rodney/releases/">from the releases page</a>.)</p>
<p>Here's a simple example session:</p>
<div class="highlight highlight-source-shell"><pre>rodney start <span class="pl-c"><span class="pl-c">#</span> starts Chrome in the background</span>
rodney open https://datasette.io/
rodney js <span class="pl-s"><span class="pl-pds">'</span>Array.from(document.links).map(el =&gt; el.href).slice(0, 5)<span class="pl-pds">'</span></span>
rodney click <span class="pl-s"><span class="pl-pds">'</span>a[href="/for"]<span class="pl-pds">'</span></span>
rodney js location.href
rodney js document.title
rodney screenshot datasette-for-page.png
rodney stop</pre></div>
<p>Here's what that looks like in the terminal:</p>
<p><img alt=";~ % rodney start
Chrome started (PID 91462)
Debug URL: ws://127.0.0.1:64623/devtools/browser/cac6988e-8153-483b-80b9-1b75c611868d
~ % rodney open https://datasette.io/
Datasette: An open source multi-tool for exploring and publishing data
~ % rodney js 'Array.from(document.links).map(el =&gt; el.href).slice(0, 5)'
[
&quot;https://datasette.io/for&quot;,
&quot;https://docs.datasette.io/en/stable/&quot;,
&quot;https://datasette.io/tutorials&quot;,
&quot;https://datasette.io/examples&quot;,
&quot;https://datasette.io/plugins&quot;
]
~ % rodney click 'a[href=&quot;/for&quot;]'
Clicked
~ % rodney js location.href
https://datasette.io/for
~ % rodney js document.title
Use cases for Datasette
~ % rodney screenshot datasette-for-page.png
datasette-for-page.png
~ % rodney stop
Chrome stopped" src="https://static.simonwillison.net/static/2026/rodney-demo.jpg" /></p>
<p>As with Showboat, this tool is not designed to be used by humans! The goal is for coding agents to be able to run <code>rodney --help</code> and see everything they need to know to start using the tool. You can see <a href="https://github.com/simonw/rodney/blob/main/help.txt">that help output</a> in the GitHub repo.</p>
<p>Here are three demonstrations of Rodney that I created using Showboat:</p>
<ul>
<li>
<a href="https://github.com/simonw/showboat-demos/blob/main/rodney/README.md">Rodney's original feature set</a>, including screenshots of pages and executing JavaScript.</li>
<li>
<a href="https://github.com/simonw/rodney/blob/main/notes/accessibility-features/README.md">Rodney's new accessibility testing features</a>, built during development of those features to show what they could do.</li>
<li>
<a href="https://github.com/simonw/showboat-demos/blob/main/datasette-database-page-accessibility-audit/README.md">Using those features to run a basic accessibility audit of a page</a>. I was impressed at how well Claude Opus 4.6 responded to the prompt "Use showboat and rodney to perform an accessibility audit of <a href="https://latest.datasette.io/fixtures">https://latest.datasette.io/fixtures</a>" - <a href="https://gisthost.github.io/?dce6b2680db4b05c04469ed8f251eb34/index.html">transcript here</a>.</li>
</ul>
<h4 id="test-driven-development-helps-but-we-still-need-manual-testing">Test-driven development helps, but we still need manual testing</h4>
<p>After being a career-long skeptic of the test-first, maximum test coverage school of software development (I like <a href="https://simonwillison.net/2022/Oct/29/the-perfect-commit/#tests">tests included</a> development instead) I've recently come around to test-first processes as a way to force agents to write only the code that's necessary to solve the problem at hand.</p>
<p>Many of my Python coding agent sessions start the same way:</p>
<blockquote>
<p><code>Run the existing tests with "uv run pytest". Build using red/green TDD.</code></p>
</blockquote>
<p>Telling the agents how to run the tests doubles as an indicator that tests on this project exist and matter. Agents will read existing tests before writing their own so having a clean test suite with good patterns makes it more likely they'll write good tests of their own.</p>
<p>The frontier models all understand that "red/green TDD" means they should write the test first, run it and watch it fail and then write the code to make it pass - it's a convenient shortcut.</p>
<p>I find this greatly increases the quality of the code and the likelihood that the agent will produce the right thing with the smallest amount of prompts to guide it.</p>
<p>But anyone who's worked with tests will know that just because the automated tests pass doesn't mean the software actually works! That’s the motivation behind Showboat and Rodney - I never trust any feature until I’ve seen it running with my own eye.</p>
<p>Before building Showboat I'd often add a “manual” testing step to my agent sessions, something like:</p>
<blockquote>
<p><code>Once the tests pass, start a development server and exercise the new feature using curl</code></p>
</blockquote>
<h4 id="i-built-both-of-these-tools-on-my-phone">I built both of these tools on my phone</h4>
<p>Both Showboat and Rodney started life as Claude Code for web projects created via the Claude iPhone app. Most of the ongoing feature work for them happened in the same way.</p>
<p>I'm still a little startled at how much of my coding work I get done on my phone now, but I'd estimate that the majority of code I ship to GitHub these days was written for me by coding agents driven via that iPhone app.</p>
<p>I initially designed these two tools for use in asynchronous coding agent environments like Claude Code for the web. So far that's working out really well.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/go">go</a>, <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/testing">testing</a>, <a href="https://simonwillison.net/tags/markdown">markdown</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/async-coding-agents">async-coding-agents</a></p>

---

*抓取时间: 2026-02-11 06:02:39*
