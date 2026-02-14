# The evolution of OpenAI's mission statement

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-13T23:38:29+00:00
**链接:** https://simonwillison.net/2026/Feb/13/openai-mission-statement/#atom-everything

---

<p>As a USA <a href="https://en.wikipedia.org/wiki/501(c)(3)_organization">501(c)(3)</a> the OpenAI non-profit has to file a tax return each year with the IRS. One of the required fields on that tax return is to "Briefly describe the organization’s mission or most significant activities" - this has actual legal weight to it as the IRS can use it to evaluate if the organization is sticking to its mission and deserves to maintain its non-profit tax-exempt status.</p>
<p>You can browse OpenAI's <a href="https://projects.propublica.org/nonprofits/organizations/810861541">tax filings by year</a> on ProPublica's excellent <a href="https://projects.propublica.org/nonprofits/">Nonprofit Explorer</a>.</p>
<p>I went through and extracted that mission statement for 2016 through 2024, then had Claude Code <a href="https://gisthost.github.io/?7a569df89f43f390bccc2c5517718b49/index.html">help me</a> fake the commit dates to turn it into a git repository and share that as a Gist - which means that Gist's <a href="https://gist.github.com/simonw/e36f0e5ef4a86881d145083f759bcf25/revisions">revisions page</a> shows every edit they've made since they started filing their taxes!</p>
<p>It's really interesting seeing what they've changed over time.</p>
<p>The original 2016 mission reads as follows (and yes, the apostrophe in "OpenAIs" is missing <a href="https://projects.propublica.org/nonprofits/organizations/810861541/201703459349300445/full">in the original</a>):</p>
<blockquote>
<p>OpenAIs goal is to advance digital intelligence in the way that is most likely to benefit humanity as a whole, unconstrained by a need to generate financial return. We think that artificial intelligence technology will help shape the 21st century, and we want to help the world build safe AI technology and ensure that AI's benefits are as widely and evenly distributed as possible. Were trying to build AI as part of a larger community, and we want to openly share our plans and capabilities along the way.</p>
</blockquote>
<p>In 2018 they dropped the part about "trying to build AI as part of a larger community, and we want to openly share our plans and capabilities along the way."</p>
<p><img alt="Git diff showing the 2018 revision deleting the final two sentences: &quot;Were trying to build AI as part of a larger community, and we want to openly share our plans and capabilities along the way.&quot;" src="https://static.simonwillison.net/static/2026/mission-3.jpg" /></p>
<p>In 2020 they dropped the words "as a whole" from "benefit humanity as a whole". They're still "unconstrained by a need to generate financial return" though.</p>
<p><img alt="Git diff showing the 2020 revision dropping &quot;as a whole&quot; from &quot;benefit humanity as a whole&quot; and changing &quot;We think&quot; to &quot;OpenAI believes&quot;" src="https://static.simonwillison.net/static/2026/mission-5.jpg" /></p>
<p>Some interesting changes in 2021. They're still unconstrained by a need to generate financial return, but here we have the first reference to "general-purpose artificial intelligence" (replacing "digital intelligence"). They're more confident too: it's not "most likely to benefit humanity", it's just "benefits humanity".</p>
<p>They previously wanted to "help the world build safe AI technology", but now they're going to do that themselves: "the companys goal is to develop and responsibly deploy safe AI technology".</p>
<p><img alt="Git diff showing the 2021 revision replacing &quot;goal is to advance digital intelligence&quot; with &quot;mission is to build general-purpose artificial intelligence&quot;, changing &quot;most likely to benefit&quot; to just &quot;benefits&quot;, and replacing &quot;help the world build safe AI technology&quot; with &quot;the companys goal is to develop and responsibly deploy safe AI technology&quot;" src="https://static.simonwillison.net/static/2026/mission-6.jpg" /></p>
<p>2022 only changed one significant word: they added "safely" to "build ... (AI) that safely benefits humanity". They're still unconstrained by those financial returns!</p>
<p><img alt="Git diff showing the 2022 revision adding &quot;(AI)&quot; and the word &quot;safely&quot; so it now reads &quot;that safely benefits humanity&quot;, and changing &quot;the companys&quot; to &quot;our&quot;" src="https://static.simonwillison.net/static/2026/mission-7.jpg" /></p>
<p>No changes in 2023... but then in 2024 they deleted almost the entire thing, reducing it to simply:</p>
<blockquote>
<p>OpenAIs mission is to ensure that artificial general intelligence benefits all of humanity.</p>
</blockquote>
<p>They've expanded "humanity" to "all of humanity", but there's no mention of safety any more and I guess they can finally start focusing on that need to generate financial returns!</p>
<p><img alt="Git diff showing the 2024 revision deleting the entire multi-sentence mission statement and replacing it with just &quot;OpenAIs mission is to ensure that artificial general intelligence benefits all of humanity.&quot;" src="https://static.simonwillison.net/static/2026/mission-9.jpg" /></p>

<p><strong>Update</strong>: I found loosely equivalent but much less interesting documents <a href="https://simonwillison.net/2026/Feb/13/anthropic-public-benefit-mission/">from Anthropic</a>.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/ai-ethics">ai-ethics</a>, <a href="https://simonwillison.net/tags/propublica">propublica</a></p>

---

*抓取时间: 2026-02-15 00:03:07*
