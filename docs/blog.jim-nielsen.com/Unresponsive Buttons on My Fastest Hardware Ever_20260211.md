# Unresponsive Buttons on My Fastest Hardware Ever

**来源:** [blog.jim-nielsen.com](https://blog.jim-nielsen.com)
**发布时间:** Wed, 11 Feb 2026 19:00:00 GMT
**链接:** https://blog.jim-nielsen.com/2026/unresponsive-buttons/

---

<p>This is one of those small things that drives me nuts.</p>
<p>Why? I don’t know. I think it has something to do with the fact that I have a computer that is faster than any computer I’ve ever used in my entire life — and yet, clicking on buttons results in slight but perceptible delays.</p>
<p>Let me explain.</p>
<p>Imagine a button that looks like this:</p>
<pre><code class="language language-jsx">&lt;<span class="hljs-title class_">Button</span>
  onClick={<span class="hljs-title function_">async</span> () =&gt; {
    <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> <span class="hljs-title function_">getSessionUrlFromStripe</span>(id);
    <span class="hljs-variable language_">window</span>.<span class="hljs-property">location</span> = data.<span class="hljs-property">url</span>;
  }
&gt;<span class="hljs-title class_">Upgrade</span> to <span class="hljs-title class_">Pro</span>&lt;/<span class="hljs-title class_">Button</span>&gt;
</code></pre>
<p>For SPA apps, when the user clicks that button it takes a split second (even on a fast connection) for anything to happen because:</p>
<ul>
<li>The browser makes a request to the server</li>
<li>The server talks to Stripe to get a session</li>
<li>The server responds with the session data to the client</li>
<li>The client redirects</li>
</ul>
<p>When clicking on that button, even on a fast connection, my brain glitches for a second, my thought process going something like:</p>
<ul>
<li>I click</li>
<li>[nothing happens]</li>
<li>I think “Did that work?”</li>
<li>Just as I’m about to click again, I see the URL bar change</li>
<li>I think, “Oh, ok, it’s doing <em>something</em>.”</li>
<li>I stop myself from clicking again while I wait for the UI to redraw</li>
</ul>
<p>Granted those thoughts occur in my brain in under a second, but I hate that pause of indetermination.</p>
<p>I clicked, I want (perceptibly) <em>instant</em> feedback. If something is happening, tell me!</p>
<p>For SPA apps, you could put some state in there, like:</p>
<pre><code class="language language-jsx"><span class="hljs-keyword">const</span> [isLoading, setIsLoading] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);

<span class="hljs-keyword">return</span> (
  <span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">Button</span>
  <span class="hljs-attr">onClick</span>=<span class="hljs-string">{async</span> () =&gt;</span> {
    setIsLoading(true);
    const data = await getSessionUrlFromStripe(id);
    window.location = data.url;
  }
  &gt;{isLoading ? &#x27;Upgrading...&#x27; : &#x27;Upgrade to Pro&#x27;}<span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span></span>
)
</code></pre>
<p>This would provide more immediate feedback. But it also raises a whole set of other questions:</p>
<ul>
<li>Is that actually the interaction you want, where the text changes? That’s probably gonna shift layout. Maybe you want something different, like a spinner in place of the text. How do you handle that?</li>
<li>What if you have multiple places to upgrade? Do you have to implement <code>isLoading</code> state in all those places too? What if the trigger in each place is slightly different? A button here, some text there, and icon over yonder? How do you handle all of those different interactions in a standard, immediate way?</li>
<li>Errors. What if it fails? Well, we already weren’t handling that in the first code example were we? But maybe we should…</li>
</ul>
<p>Oh boy, this is getting complicated isn’t it?</p>
<p>This is why, I assume, lots of apps just don’t deal with it. </p>
<p>They accept there will be a slight delay in the responsiveness of the UI (and that it might error, but the user can just click again) and justify that it’s really not that big of a deal if there’s a slight, almost imperceptible delay between clicking a button and seeing the UI respond.</p>
<p>“We’ve got bigger fish to fry.”</p>
<p>And it makes sense. I mean, a slight delay in UI responsiveness, is that why people will or won’t buy your thing? Seems like a small detail. Who’s got the time to spend on details like this?Who cares? </p>
<p>I care. That’s why I’m writing this post.</p>
<p>To my original point, every piece of hardware I currently own is the fastest version of that device I’ve ever had in my life. And yet, everywhere I go I encounter lag. <a href="https://world.hey.com/jason/the-big-regression-da7fc60d">Lag everywhere.</a></p>
<p>And I’m grumpy about it, hence this post.</p>

    <hr />
    

    <p>
      Reply via:
      

      <a href="mailto:jimniels%2Bblog@gmail.com?subject=Re:%20blog.jim-nielsen.com/2026/unresponsive-buttons/">Email</a>
      · <a href="https://mastodon.social/@jimniels">Mastodon</a> ·

      <a href="https://bsky.app/profile/jim-nielsen.com">Bluesky</a>
    </p>

---

*抓取时间: 2026-02-12 00:02:59*
