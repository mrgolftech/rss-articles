# The Browser’s Little White Lies

**来源:** [blog.jim-nielsen.com](https://blog.jim-nielsen.com)
**发布时间:** Sun, 01 Feb 2026 19:00:00 GMT
**链接:** https://blog.jim-nielsen.com/2026/browsers-white-lies/

---

<p>So I’m making a thing and I want it to be styled different if the link’s been visited.</p>
<p>Rather than build something myself in JavaScript, I figure I’ll just hook into the browser’s mechanism for tracking if a link’s been visited (a sensible approach, <a href="https://blog.jim-nielsen.com/2025/browser-apis-as-sass/">if I do say so myself</a>). </p>
<p>Why write JavaScript when a little CSS will do? So I craft this:</p>
<pre><code class="language language-css"><span class="hljs-selector-class">.entry</span><span class="hljs-selector-pseudo">:has</span>(<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:visited</span>) {
  <span class="hljs-attribute">opacity</span>: .<span class="hljs-number">5</span>;
  <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">grayscale</span>(<span class="hljs-number">1</span>);
}
</code></pre>
<p>But it doesn’t work.</p>
<p><code>:has()</code> is relatively new, and I’ve been known to muff it, so it’s probably just a syntax issue.</p>
<p>I start researching.</p>
<p>Wouldn’t you know it? We can’t have nice things. <code>:visited</code> doesn’t always work like you’d expect because we (not me, mind you) exploited it.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited">Here’s MDN</a>:</p>
<blockquote>
<p>You can style visited links, but there are limits to which styles you can use.</p>
</blockquote>
<p>While <code>:has()</code> is not mentioned specifically, other tricks like sibling selectors are:</p>
<blockquote>
<p>When using a sibling selector, such as <code>:visited + span</code>, the adjacent element (<code>span</code> in this example) is styled as though the link were unvisited.</p>
</blockquote>
<p>Why? You guessed it. Security and privacy reasons.</p>
<p>If it were not so, somebody could come along with a little JavaScript and uncover a user’s browsing history (imagine, for example, setting styles for visited and unvisited links, then using <code>window.getComputedStyle</code> and checking style computations).</p>
<p>MDN says browsers tell little white lies:</p>
<blockquote>
<p>To preserve users' privacy, browsers lie to web applications under certain circumstances</p>
</blockquote>
<p>So, from what I can tell, when I write <code>.entry:has(a:visited)</code> the browser is telling the engine that handles styling that all <code>.entry</code> items have never been <code>:visited</code> (even if they have been).</p>
<p>So where does that leave me?</p>
<p>Now I will abandon CSS and go use JavaScript for something only JavaScript can do.</p>
<p>That’s a good reason for JS.</p>

    <hr />
    

    <p>
      Reply via:
      

      <a href="mailto:jimniels%2Bblog@gmail.com?subject=Re:%20blog.jim-nielsen.com/2026/browsers-white-lies/">Email</a>
      · <a href="https://mastodon.social/@jimniels">Mastodon</a> ·

      <a href="https://bsky.app/profile/jim-nielsen.com">Bluesky</a>
    </p>

---

*抓取时间: 2026-02-05 08:40:59*
