# New Blog Post: Some Silly Z3 Scripts I Wrote

**来源:** [buttondown.com/hillelwayne](https://buttondown.com/hillelwayne)
**发布时间:** Mon, 23 Feb 2026 16:49:10 +0000
**链接:** https://buttondown.com/hillelwayne/archive/new-blog-post-some-silly-z3-scripts-i-wrote/

---

<p>Now that I'm not spending all my time on Logic for Programmers, I have time to update my website again! So here's the first blog post in five months: <a href="https://www.hillelwayne.com/post/z3-examples/" target="_blank">Some Silly Z3 Scripts I Wrote</a>.</p>
<p>Normally I'd also put a link to the Patreon notes but I've decided I don't like publishing gated content and am going to wind that whole thing down. So some quick notes about this post:</p>
<ul>
<li>Part of the point is admittedly to hype up the eventual release of LfP. I want to start marketing the book, but don't want the marketing material to be devoid of interest, so tangentially-related-but-independent blog posts are a good place to start.</li>
<li>The post discusses the concept of "chaff", the enormous quantity of material (both code samples and prose) that didn't make it into the book. The book is about 50,000 words… and considerably shorter than the total volume of chaff! I don't <em>think</em> most of it can be turned into useful public posts, but I'm not entirely opposed to the idea. Maybe some of the old chapters could be made into something?</li>
<li>Coming up with a conditioned mathematical property to prove was a struggle. I had two candidates: <code>a == b * c =&gt; a / b == c</code>, which would have required a long tangent on how division must be total in Z3, and  <code>a != 0 =&gt; some b: b * a == 1</code>, which would have required introducing a quantifier (SMT is real weird about quantifiers). Division by zero has already caused me enough grief so I went with the latter. This did mean I had to reintroduce "operations must be total" when talking about arrays.</li>
<li>I have no idea why the array example returns <code>2</code> for the max profit and not <code>99999999</code>. I'm guessing there's some short circuiting logic in the optimizer when the problem is ill-defined?</li>
<li>One example I could not get working, which is unfortunate, was a demonstration of how SMT solvers are undecidable via encoding Goldbach's conjecture as an SMT problem. Anything with multiple nested quantifiers is a pain.</li>
</ul>

---

*抓取时间: 2026-02-24 06:06:52*
