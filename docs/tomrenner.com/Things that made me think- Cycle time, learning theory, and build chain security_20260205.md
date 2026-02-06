# Things that made me think: Cycle time, learning theory, and build chain security

**来源:** https://tomrenner.com
**链接:** https://tomrenner.com/posts/ttmmt-3/
**日期:** Tue, 09 Dec 2025 00:00:00 +0000

---

[ My place to put things ](/)

  * [ About ](/about/ "About page")
  * [ Contact ](/contact/ "Contact page")
  * [ Posts ](/posts/ "Posts page")



[ ](https://mastodon.social/@trenner "follow on Mastodon - Opens in a new window")[ ](https://github.com/tr325 "follow on GitHub - Opens in a new window")[ ](http://linkedin.com/in/tom-renner "follow on LinkedIn - Opens in a new window")[ ]( "follow on  - Opens in a new window")[ ](https://tomrenner.com/index.xml "follow on RSS - Opens in a new window")

Things that made me think: Cycle time, learning theory, and build chain security

Posts 

[ ](https://bsky.app/intent/compose?&text=https%3A%2F%2Ftomrenner.com%2Fposts%2Fttmmt-3%2F "Share on Bluesky")[ ](https://news.ycombinator.com/submitlink?&t=+This+series+is+a+place+to+collect+interesting+things+I%26amp%3Brsquo%3Bve+seen%2C+read%2C+or+heard%2C+along+with+some+brief+thoughts+%28often+incomplete+and%2For+inconclusive%29+that+they+provoked.%0AMeasuring+Cyle+Time+with+Dr.+Cat+Hicks+-+The+Hanger+DX+Podcast%2C+Ankit+Jain+Cycle+time+is+a+measure+lots+of+people+use%2C+but+has+no+clear+audience+-+developers%2C+managers%2C+CTOs+all+care+about+it.+This+makes+it+dangerous.+Metrics+have+to+be+designed+and+used+with+psychological+safety+in+mind.+If+people+don%26amp%3Brsquo%3Bt+trust+the+intention+behind+the+metrics+use%2C+they%26amp%3Brsquo%3Bll+game+it.%0A&u=https%3A%2F%2Ftomrenner.com%2Fposts%2Fttmmt-3%2F "Share on Hacker News")[ ](https://www.linkedin.com/shareArticle?&mini=true&source=https%3A%2F%2Ftomrenner.com%2Fposts%2Fttmmt-3%2F&summary=+This+series+is+a+place+to+collect+interesting+things+I%26amp%3Brsquo%3Bve+seen%2C+read%2C+or+heard%2C+along+with+some+brief+thoughts+%28often+incomplete+and%2For+inconclusive%29+that+they+provoked.%0AMeasuring+Cyle+Time+with+Dr.+Cat+Hicks+-+The+Hanger+DX+Podcast%2C+Ankit+Jain+Cycle+time+is+a+measure+lots+of+people+use%2C+but+has+no+clear+audience+-+developers%2C+managers%2C+CTOs+all+care+about+it.+This+makes+it+dangerous.+Metrics+have+to+be+designed+and+used+with+psychological+safety+in+mind.+If+people+don%26amp%3Brsquo%3Bt+trust+the+intention+behind+the+metrics+use%2C+they%26amp%3Brsquo%3Bll+game+it.%0A&title=Things+that+made+me+think%3A+Cycle+time%2C+learning+theory%2C+and+build+chain+security&url=https%3A%2F%2Ftomrenner.com%2Fposts%2Fttmmt-3%2F "Share on LinkedIn")[ ](https://reddit.com/submit/?&resubmit=true&title=Things+that+made+me+think%3A+Cycle+time%2C+learning+theory%2C+and+build+chain+security&url=https%3A%2F%2Ftomrenner.com%2Fposts%2Fttmmt-3%2F "Share on Reddit")

# Things that made me think: Cycle time, learning theory, and build chain security

**Tom Renner**

December 9, 2025 \- 3 minutes read  \- 555 words 

> _[This series](/tags/ttmmt) is a place to collect interesting things I've seen, read, or heard, along with some brief thoughts (often incomplete and/or inconclusive) that they provoked._

* * *

### [Measuring Cyle Time with Dr. Cat Hicks](https://www.aviator.co/podcast/dr-cat-hicks-cycle-time) \- The Hanger DX Podcast, Ankit Jain

Cycle time is a measure lots of people use, but has no clear audience - developers, managers, CTOs all care about it. This makes it dangerous. Metrics have to be designed and used with psychological safety in mind. If people don't trust the intention behind the metrics use, they'll game it.

Cycle time is **massively variable** ; between developers, within one developer's year, annual variations (christmas, summer holidays, OKR timetables, etc.) - you need a _really long_ timeframe over which to measure to use it sensibly.

Once you have a metric you've measured semi-successfully, don't use it to benchmark, don't assume it covers all work (plenty is not tracked by cycle time), and make sure you always connect it to outcomes - eg. shorter cycle time doesn't mean customers are happy.

… all of which makes me just very cautious about measuring anything in my team! I'm not sure that's the takeaway I was meant to have…

* * *

### [Stop building AI tools backwards](https://hazelweakly.me/blog/stop-building-ai-tools-backwards/) - Hazel Weakly

Firstly, Hazel is such a badass, and I love everything she writes. This post really shaped my thinking about how to successfully use LLMs and not just keep feeding text into the software slot machine in the hope that it eventually gives the right answer.

It made me realise that I need to learn more about learning! Because by building learning theory into the design of our interactions with AI, Hazel superbly articulates what _better_ could look like for these tools, and how a sensible product that supported its users' development might work.

Now I need to review the EDGE framework she mentions in more detail, and reflect on how I approach learning-on-the-job. And if I'm really aiming to be an overachiever, I should put that into terms my team will connect with, so they get the most out of our LLM toolsets as well.

* * *

### [Pwning the Entire Nix Ecosystem](https://ptrpa.ws/nixpkgs-actions-abuse) - ptrpaws

Github Actions are shockingly insecure (it turns out). I was not aware of this previously, and could easily see myself falling into some of the pitfalls that were exploited here. Ellie ([@ptrpaws](https://wetdry.world/@ptrpaws), the author) used them to gain read/write access to nixpgs, giving them the ability to nuke the entire system from orbit, had they so chosen.

Supply-chain attacks are so scary - it's so much harder conceptually to treat your build chain with the same security mindset you treat application code (and most developers sadly don't treat that very carefully either!), but really that's the higher-risk attack surface.

And finally - this kind of "not my problem, guv" warning from tools is _never_ helpful:

> 
>     It is not possible for xargs to be used securely
>     

taken directly from the [man page](https://man7.org/linux/man-pages/man1/xargs.1.html#:~:text=It%20is%20not%20possible%20for%20xargs%20to%20be%20used%20securely). Sigh. Almost as useless as the legalese telling users not to rely on Tesla's "Fully Self Driving" system to actually, you know, drive the car.

If you market the tool as functional, you get zero credit from me for stating in the fine print that a use case is unsupported. Users use the tools you give them, it's on you to make sure it's safe to do so.

  * [Self-Improvement](/tags/self-improvement/)
  * [AI](/tags/ai/)
  * [Technologies](/tags/technologies/)
  * [Development Processes](/tags/development-processes/)
  * [TTmmT](/tags/ttmmt/)



* * *

_Reactions collected from around the web using[webmentions](https://indieweb.org/Webmention)_

**❤️ Likes:** [ ![Cat Hicks](https://avatars.webmention.io/files.mastodon.social/9f19ea64a8c279618d5ae9272cedb03a3777682071d46700c76401dca172d87f.jpg) ](https://mastodon.social/@grimalkina "Cat Hicks")[ ![Hazel Weakly](https://avatars.webmention.io/files.mastodon.social/c287b36451e9ac126b3a1a3f4ef0e857c62ff04850bbb864ba11a938126a0bff.jpg) ](https://hachyderm.io/@hazelweakly "Hazel Weakly")[ ![Troels Thomsen](https://avatars.webmention.io/files.mastodon.social/5bc2d975b2d1b1e160f1cc9a3668af3596ca7b2af5bc7eb322db5fb54cf5fa5d.jpg) ](https://mastodon.social/@tt "Troels Thomsen")[ ![Sebastian Hans](https://avatars.webmention.io/files.mastodon.social/0a6d651307c735da1e877ec202d1bbf75580ca701b97ef75c65d536189470495.jpg) ](https://hachyderm.io/@sebhans "Sebastian Hans")[ ![Kevin Karhan :verified:](https://avatars.webmention.io/files.mastodon.social/f94ef5099d9ccdd0abb798e368ee89478c79934567f4b8a0881e0d60af933d09.png) ](https://infosec.space/@kkarhan "Kevin Karhan :verified:") **🔄 Reposts:** [ ![Hazel Weakly](https://avatars.webmention.io/files.mastodon.social/c287b36451e9ac126b3a1a3f4ef0e857c62ff04850bbb864ba11a938126a0bff.jpg) ](https://hachyderm.io/@hazelweakly "Hazel Weakly")[ ![Kevin Karhan :verified:](https://avatars.webmention.io/files.mastodon.social/f94ef5099d9ccdd0abb798e368ee89478c79934567f4b8a0881e0d60af933d09.png) ](https://infosec.space/@kkarhan "Kevin Karhan :verified:")

**💬 Comments:**

[ ![Hazel Weakly](https://avatars.webmention.io/files.mastodon.social/c287b36451e9ac126b3a1a3f4ef0e857c62ff04850bbb864ba11a938126a0bff.jpg) Hazel Weakly ](https://hachyderm.io/@hazelweakly "Hazel Weakly")@trenner @grimalkina @ptrpaws Thanks for the kind words! And that’s a great roundup :) 

Related

  * [Things that made me think: Digital gardening, web degradation, and digital ghosts](/posts/ttmmt-2/)
  * [Things that made me think: Enshittification, apathy, and discrimination](/posts/ttmmt-1/)
  * [Does my toaster love me?](/posts/does-my-toaster-love-me/)
  * [The sound of inevitability](/posts/llm-inevitabilism/)
  * [Saying the quiet part out loud](/posts/saying-the-quiet-part-out-loud/)
  * ["Efficiency" is bad for your health, and your learning](/posts/efficiency-is-bad-for-your-health/)
  * [Offline knowledge, buses, and note-taking](/posts/offline-knowledge/)
  * [A quick guide for productive development](/posts/a-quick-guide-for-productive-development/)
  * [Why am I doing this again?](/posts/why-am-i-doing-this-again/)



[Things that made me think: Cycle time, learning theory, and build chain security](https://tomrenner.com/posts/ttmmt-3/) [Tom Renner](/)

[ (C) My place to put things 2026 ](https://tomrenner.com/)

[ ](https://mastodon.social/@trenner "follow on Mastodon - Opens in a new window")[ ](https://github.com/tr325 "follow on GitHub - Opens in a new window")[ ](http://linkedin.com/in/tom-renner "follow on LinkedIn - Opens in a new window")[ ]( "follow on  - Opens in a new window")[ ](https://tomrenner.com/index.xml "follow on RSS - Opens in a new window")
