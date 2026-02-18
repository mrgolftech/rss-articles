# Rodney v0.4.0

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-17T23:02:33+00:00
**链接:** https://simonwillison.net/2026/Feb/17/rodney/#atom-everything

---

<p><strong><a href="https://github.com/simonw/rodney/releases/tag/v0.4.0">Rodney v0.4.0</a></strong></p>
My <a href="https://github.com/simonw/rodney">Rodney</a> CLI tool for browser automation attracted quite the flurry of PRs since I announced it <a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#rodney-cli-browser-automation-designed-to-work-with-showboat">last week</a>. Here are the release notes for the just-released v0.4.0:</p>
<blockquote>
<ul>
<li>Errors now use exit code 2, which means exit code 1 is just for for check failures. <a href="https://github.com/simonw/rodney/pull/15">#15</a></li>
<li>New <code>rodney assert</code> command for running JavaScript tests, exit code 1 if they fail. <a href="https://github.com/simonw/rodney/issues/19">#19</a></li>
<li>New directory-scoped sessions with <code>--local</code>/<code>--global</code> flags. <a href="https://github.com/simonw/rodney/pull/14">#14</a></li>
<li>New <code>reload --hard</code> and <code>clear-cache</code> commands. <a href="https://github.com/simonw/rodney/pull/17">#17</a></li>
<li>New <code>rodney start --show</code> option to make the browser window visible. Thanks, <a href="https://github.com/antocuni">Antonio Cuni</a>. <a href="https://github.com/simonw/rodney/paull/13">#13</a></li>
<li>New <code>rodney connect PORT</code> command to debug an already-running Chrome instance. Thanks, <a href="https://github.com/pnf">Peter Fraenkel</a>. <a href="https://github.com/simonw/rodney/pull/12">#12</a></li>
<li>New <code>RODNEY_HOME</code> environment variable to support custom state directories. Thanks, <a href="https://github.com/senko">Senko Rašić</a>. <a href="https://github.com/simonw/rodney/pull/11">#11</a></li>
<li>New <code>--insecure</code> flag to ignore certificate errors. Thanks, <a href="https://github.com/zgolus">Jakub Zgoliński</a>. <a href="https://github.com/simonw/rodney/pull/10">#10</a></li>
<li>Windows support: avoid <code>Setsid</code> on Windows via build-tag helpers. Thanks, <a href="https://github.com/adm1neca">adm1neca</a>. <a href="https://github.com/simonw/rodney/pull/18">#18</a></li>
<li>Tests now run on <code>windows-latest</code> and <code>macos-latest</code> in addition to Linux.</li>
</ul>
</blockquote>
<p>I've been using <a href="https://github.com/simonw/showboat">Showboat</a> to create demos of new features - here those are for <a href="https://github.com/simonw/rodney/tree/v0.4.0/notes/assert-command-demo">rodney assert</a>, <a href="https://github.com/simonw/rodney/tree/v0.4.0/notes/clear-cache-demo">rodney reload --hard</a>, <a href="https://github.com/simonw/rodney/tree/v0.4.0/notes/error-codes-demo">rodney exit codes</a>, and <a href="https://github.com/simonw/rodney/tree/v0.4.0/notes/local-sessions-demo">rodney start --local</a>.</p>
<p>The <code>rodney assert</code> command is pretty neat: you can now Rodney to test a web app through multiple steps in a shell script that looks something like this (adapted from <a href="https://github.com/simonw/rodney/blob/v0.4.0/README.md#combining-checks-in-a-shell-script">the README</a>):</p>
<div class="highlight highlight-source-shell"><pre><span class="pl-c"><span class="pl-c">#!</span>/bin/bash</span>
<span class="pl-c1">set</span> -euo pipefail

FAIL=0

<span class="pl-en">check</span>() {
    <span class="pl-k">if</span> <span class="pl-k">!</span> <span class="pl-s"><span class="pl-pds">"</span><span class="pl-smi">$@</span><span class="pl-pds">"</span></span><span class="pl-k">;</span> <span class="pl-k">then</span>
        <span class="pl-c1">echo</span> <span class="pl-s"><span class="pl-pds">"</span>FAIL: <span class="pl-smi">$*</span><span class="pl-pds">"</span></span>
        FAIL=1
    <span class="pl-k">fi</span>
}

rodney start
rodney open <span class="pl-s"><span class="pl-pds">"</span>https://example.com<span class="pl-pds">"</span></span>
rodney waitstable

<span class="pl-c"><span class="pl-c">#</span> Assert elements exist</span>
check rodney exists <span class="pl-s"><span class="pl-pds">"</span>h1<span class="pl-pds">"</span></span>

<span class="pl-c"><span class="pl-c">#</span> Assert key elements are visible</span>
check rodney visible <span class="pl-s"><span class="pl-pds">"</span>h1<span class="pl-pds">"</span></span>
check rodney visible <span class="pl-s"><span class="pl-pds">"</span>#main-content<span class="pl-pds">"</span></span>

<span class="pl-c"><span class="pl-c">#</span> Assert JS expressions</span>
check rodney assert <span class="pl-s"><span class="pl-pds">'</span>document.title<span class="pl-pds">'</span></span> <span class="pl-s"><span class="pl-pds">'</span>Example Domain<span class="pl-pds">'</span></span>
check rodney assert <span class="pl-s"><span class="pl-pds">'</span>document.querySelectorAll("p").length<span class="pl-pds">'</span></span> <span class="pl-s"><span class="pl-pds">'</span>2<span class="pl-pds">'</span></span>

<span class="pl-c"><span class="pl-c">#</span> Assert accessibility requirements</span>
check rodney ax-find --role navigation

rodney stop

<span class="pl-k">if</span> [ <span class="pl-s"><span class="pl-pds">"</span><span class="pl-smi">$FAIL</span><span class="pl-pds">"</span></span> <span class="pl-k">-ne</span> 0 ]<span class="pl-k">;</span> <span class="pl-k">then</span>
    <span class="pl-c1">echo</span> <span class="pl-s"><span class="pl-pds">"</span>Some checks failed<span class="pl-pds">"</span></span>
    <span class="pl-c1">exit</span> 1
<span class="pl-k">fi</span>
<span class="pl-c1">echo</span> <span class="pl-s"><span class="pl-pds">"</span>All checks passed<span class="pl-pds">"</span></span></pre></div>


    <p>Tags: <a href="https://simonwillison.net/tags/browsers">browsers</a>, <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/testing">testing</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/rodney">rodney</a></p>

---

*抓取时间: 2026-02-18 18:04:17*
