# Making Icon Sets Easy With Web Origami

**来源:** [blog.jim-nielsen.com](https://blog.jim-nielsen.com)
**发布时间:** Mon, 23 Feb 2026 19:00:00 GMT
**链接:** https://blog.jim-nielsen.com/2026/origami-icons/

---

<p>Over the years, I’ve used different icon sets on my blog. Right now I use <a href="https://heroicons.com">Heroicons</a>.</p>
<p><a href="https://github.com/tailwindlabs/heroicons">The recommended way</a> to use them is to copy/paste the source from the website directly into your HTML. It’s a pretty straightforward process:</p>
<ul>
<li>Go to the website</li>
<li>Search for the icon you want</li>
<li>Hover it</li>
<li>Click to “Copy SVG”</li>
<li>Go back to your IDE and paste it</li>
</ul>
<p>If you’re using React or Vue, there are also npm packages you can install so you can import the icons as components.</p>
<p>But I’m not using either of those frameworks, so I need the raw SVGs and there’s no <code>npm i</code> for those so I have to manually grab the ones I want.</p>
<p>In the past, my approach has been to copy the SVGs into individual files in my project, like:</p>
<pre><code>src/
  icons/
    home.svg
    about.svg
    search.svg
</code></pre>
<p>Then I have a “component” for reading those icons from disk which I use in my template files to inline the SVGs in my HTML. For example:</p>
<pre><code class="language language-js"><span class="hljs-comment">// Some page template file</span>
<span class="hljs-keyword">import</span> { <span class="hljs-title class_">Icon</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">&#x27;./Icon.js&#x27;</span>
<span class="hljs-keyword">const</span> template = <span class="hljs-string">`&lt;div&gt;<span class="hljs-subst">${Icon(<span class="hljs-string">&#x27;search.svg&#x27;</span>)}</span> Search&lt;/div&gt;`</span>

<span class="hljs-comment">// Icon.js</span>
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">&#x27;fs&#x27;</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">&#x27;path&#x27;</span>
<span class="hljs-keyword">const</span> __dirname = <span class="hljs-comment">/* Do the stuff to properly resolve the file path */</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title function_">Icon</span> = (<span class="hljs-params">name</span>) =&gt; fs.<span class="hljs-title function_">readFileSync</span>(
  path.<span class="hljs-title function_">join</span>(__dirname, <span class="hljs-string">&#x27;icons&#x27;</span>, name),
  <span class="hljs-string">&#x27;utf8&#x27;</span>
).<span class="hljs-title function_">toString</span>();
</code></pre>
<p>It’s fine. It works. It’s a lot of node boilerplate to read files from disk.</p>
<p>But changing icons is a bit of a pain. I have to find new SVGs, overwrite my existing ones, re-commit them to source control, etc. </p>
<p>I suppose it would be nice if I could just <code>npm i heroicons</code> and get the raw SVGs installed into my <code>node_modules</code> folder and then I could read those. But that has its own set of trade-offs. For example:</p>
<ul>
<li>Names are different between icon packs, so when you switch, names don’t match. For example, an icon might be named <code>search</code> in one pack and <code>magnifying-glass</code> in another. So changing sets requires going through all your templates and updating references.</li>
<li>Icon packs are often quite large and you only need a subset. <code>npm i icon-pack</code> might install hundreds or even thousands of icons I don’t need.</li>
</ul>
<p>So the project’s npm packages don’t provide the raw SVGs. The website does, but I want a more programatic way to easily grab the icons I want.</p>
<p>How can I do this?</p>
<h2 id="enter-origami">Enter Origami</h2>
<p>I’m using <a href="https://weborigami.org">Web Origami</a> for my blog which makes it easy to map icons I use in my templates to Heroicons hosted on Github. It doesn’t require an <code>npm install</code> or a <code>git submodule add</code>. Here’s an snippet of my file:</p>
<pre><code class="language language-ori">{
  home.svg: https://raw.githubusercontent.com/tailwindlabs/heroicons/refs/heads/master/optimized/24/outline/home.svg,
  about.svg: https://raw.githubusercontent.com/tailwindlabs/heroicons/refs/heads/master/optimized/24/outline/question-mark-circle.svg,
  search.svg: https://raw.githubusercontent.com/tailwindlabs/heroicons/refs/heads/master/optimized/24/outline/magnifying-glass.svg
}
</code></pre>
<p>As you can see, I name my icon (e.g. <code>search</code>) and then I point it to the SVG as hosted on Github via the Heroicons repo. Origami takes care of fetching the icons over the network and caching them in-memory.</p>
<p>Beautiful, isn’t it? It kind of reminds me of <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap">import maps</a> where you can map a bare module specifier to a URL (and <a href="https://blog.jim-nielsen.com/2024/deno-de-emphasizes-http-imports/">Deno’s semi-abandoned HTTP imports</a> which were beautiful in their own right).</p>
<h2 id="how-it-works">How It Works</h2>
<p>Origami makes file paths first-class citizens of the language — even “remote” file paths — so it’s very simple to create a single file that maps <em>your</em> icon names in a codebase to <em>someone else’s</em> icon names from a set, whether those are being installed on disk via npm or fetched over the internet.</p>
<p>To simplify my example earlier, I can have a file like <code>icons.ori</code>:</p>
<pre><code class="language language-ori">{
  home.svg: https://example.com/path/to/home.svg
  about.svg: https://example.com/path/to/information-circle.svg
  search.svg: https://example.com/path/to/magnifying-glass.svg
}
</code></pre>
<p>Then I can reference those icons in my templates like this:</p>
<pre><code class="language language-html"><span class="hljs-tag">&lt;<span class="hljs-name">div</span>&gt;</span>${icons.ori/home.svg} Search<span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span>
</code></pre>
<p>Easy-peasy! And when I want to change icons, I simply update the entries in <code>icons.ori</code> to point somewhere else — at a remote or local path.</p>
<p>And if you really want to go the extra mile, you can use Origami’s caching feature:</p>
<pre><code class="language language-ori">Tree.cache(
  {
    home.svg: https://raw.github.com/path/to/home.svg
    about.svg: https://raw.github.com/path/to/information-circle.svg
    search.svg: https://raw.github.com/path/to/magnifying-glass.svg
  },
  Origami.projectRoot()/cache
)
</code></pre>
<p>Rather than just caching the files in memory, this will cache them to a local folder like this:</p>
<pre><code>cache/
  home.svg
  about.svg
  search.svg
</code></pre>
<p>Which is really cool because now when I run my site locally I have a folder of SVG files cached locally that I can look at and explore (useful for debugging, etc.)</p>
<p>This makes <a href="https://blog.jim-nielsen.com/2025/be-mindful-of-what-you-make-easy/">vendoring</a> really easy if I want to put these in my project under source control. Just run the file once and boom, they’re on disk!</p>
<p>There’s something really appealing to me about this. I think it’s because it feels very “webby” — akin to the same reasons I liked HTTP imports in Deno. You declare your dependencies with URLs, then they’re fetched over the network and become available to the rest of your code. No package manager middleman introducing extra complexity like versioning, transitive dependencies, install bloat, etc.</p>
<p>What’s cool about Origami is that handling icons like this isn’t a “feature” of the language. It’s an outcome of the expressiveness of the language. In some frameworks, this kind of problem would require a special feature (that’s why you have special npm packages for implementations of Heroicons in frameworks like react and vue). But because of the way Origami is crafted as a tool, it sort of pushes you towards crafting solutions in the same manner as you would with web-based technologies (HTML/CSS/JS). It helps you speak “web platform” rather than some other abstraction on top of it. I like that.</p>

    <hr />
    

    <p>
      Reply via:
      

      <a href="mailto:jimniels%2Bblog@gmail.com?subject=Re:%20blog.jim-nielsen.com/2026/origami-icons/">Email</a>
      · <a href="https://mastodon.social/@jimniels">Mastodon</a> ·

      <a href="https://bsky.app/profile/jim-nielsen.com">Bluesky</a>
    </p>

---

*抓取时间: 2026-02-24 06:06:52*
