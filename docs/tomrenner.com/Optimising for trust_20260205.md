# Optimising for trust

**来源:** https://tomrenner.com
**链接:** https://tomrenner.com/posts/optimising-for-trust/
**日期:** Mon, 18 Aug 2025 00:00:00 +0000

---

[ My place to put things ](/)

  * [ About ](/about/ "About page")
  * [ Contact ](/contact/ "Contact page")
  * [ Posts ](/posts/ "Posts page")



[ ](https://mastodon.social/@trenner "follow on Mastodon - Opens in a new window")[ ](https://github.com/tr325 "follow on GitHub - Opens in a new window")[ ](http://linkedin.com/in/tom-renner "follow on LinkedIn - Opens in a new window")[ ]( "follow on  - Opens in a new window")[ ](https://tomrenner.com/index.xml "follow on RSS - Opens in a new window")

Optimising for trust

Posts 

[ ](https://bsky.app/intent/compose?&text=https%3A%2F%2Ftomrenner.com%2Fposts%2Foptimising-for-trust%2F "Share on Bluesky")[ ](https://news.ycombinator.com/submitlink?&t=TDD%2C+BDD%2C+DDD%2C+Agile%2C+SAFe%2C+Scrum%2C+Kanban%2C+XP%26amp%3Bhellip%3B+there%26amp%3Brsquo%3Bs+a+lot+of+ways+to+skin+a+cat+write+code+in+a+professional+environment.%0AI+take+pride+in+being+a+person+who+is+a+non-ideologue+when+it+comes+to+my+code.+There+are+many+good+ways+of+working%2C+and+they+are+all+context-dependent.%0AYou+can%26amp%3Brsquo%3Bt+apply+the+same+things+that+worked+when+you+were+a+two-person+startup+operating+out+of+the+proverbial+garage+and+expect+them+to+work+once+your+hypothetical+unicorn+has+reached+a+thousand-plus+developers.+Even+within+the+same+organisation%2C+processes+that+work+for+one+team+can+be+catastrophic+when+applied+to+their+neighbouring+team.%0A&u=https%3A%2F%2Ftomrenner.com%2Fposts%2Foptimising-for-trust%2F "Share on Hacker News")[ ](https://www.linkedin.com/shareArticle?&mini=true&source=https%3A%2F%2Ftomrenner.com%2Fposts%2Foptimising-for-trust%2F&summary=TDD%2C+BDD%2C+DDD%2C+Agile%2C+SAFe%2C+Scrum%2C+Kanban%2C+XP%26amp%3Bhellip%3B+there%26amp%3Brsquo%3Bs+a+lot+of+ways+to+skin+a+cat+write+code+in+a+professional+environment.%0AI+take+pride+in+being+a+person+who+is+a+non-ideologue+when+it+comes+to+my+code.+There+are+many+good+ways+of+working%2C+and+they+are+all+context-dependent.%0AYou+can%26amp%3Brsquo%3Bt+apply+the+same+things+that+worked+when+you+were+a+two-person+startup+operating+out+of+the+proverbial+garage+and+expect+them+to+work+once+your+hypothetical+unicorn+has+reached+a+thousand-plus+developers.+Even+within+the+same+organisation%2C+processes+that+work+for+one+team+can+be+catastrophic+when+applied+to+their+neighbouring+team.%0A&title=Optimising+for+trust&url=https%3A%2F%2Ftomrenner.com%2Fposts%2Foptimising-for-trust%2F "Share on LinkedIn")[ ](https://reddit.com/submit/?&resubmit=true&title=Optimising+for+trust&url=https%3A%2F%2Ftomrenner.com%2Fposts%2Foptimising-for-trust%2F "Share on Reddit")

# Optimising for trust

**Tom Renner**

August 18, 2025 \- 7 minutes read  \- 1302 words 

TDD, BDD, DDD, Agile, SAFe, Scrum, Kanban, XP… there's a lot of ways to ~~skin a cat~~ write code in a professional environment.

I take pride in being a person who is a non-ideologue when it comes to my code. There are many good ways of working, and they are all context-dependent.

You can't apply the same things that worked when you were a two-person startup operating out of the proverbial garage and expect them to work once your hypothetical unicorn has reached a thousand-plus developers. Even within the same organisation, processes that work for one team can be catastrophic when applied to their neighbouring team.

> People are the hardest problem in Computer Science. - Ben Summers

The fact is that computers can be persuaded to do almost anything, if you kick them hard enough. It is very rarely the case that the reason we struggle to produce shippable features is because we are doing something truly novel in Computer Science.

No, the problem of producing software at scale is a sociotechnical one. It's about wrangling the _humans_ involved in the production of code to all be pulling in the same direction, building on top of each other's achievements, and making consistent and reliable progress week over week.

"But Tom", I hear you cry, "we know this already - it's how to do that that's the hard thing!". And yes, putative wailer, you are correct. So let's examine how we might achieve this kind of interpersonal alignment.

* * *

Sophie is reviewing Drew's code. Sophie has read online, however, that you should have at least two reviewers sign off on any change before it can be merged, so she forwards the PR to another colleague. Drew thinks this is overkill - one reviewer is fine, and in adding another Sophie has literally doubled the review work required, creating busywork and slowing the team down.

Who is right? Is Sophie a diligent developer who understands the need for quality, and Drew a shoot-from-the-hip rogue whose slapdash efforts will cause pain for years to come? Or are the Sophies of the world preventing us from ever finishing our work, introducing ever-more hurdles to releasing, slowing down the entrepreneurial go-getters who actually want to change things?

Well, as is possibly unsurprising, it depends. It depends on the context of the team, on the personalities involved, on the product being developed… on any number of factors that are way too numerous to go over in a hastily-spewed blog post such as this one.

* * *

So, we (finally) come to my recommendation.

Since, as we discussed, the humans are the hard part, any processes you have in place need to centre the human experience above all. So what are we doing then? How are we assessing the multitudes of ways to work as a team on a technical product. You need a heuristic that you can apply to your processes and tools, to assess whether they will work, and work well in your context.

Optimise for trust.

That's the take. Whenever you think about making a change to how your team works, or see a shiny new tool you want everyone to use, think about how it will affect your teammates' trust in each other.

Let's look at some examples:

  1. Code review



Why do we do this? To find bugs, at the surface level. One layer deeper, it's to ensure that our code is built in a sensible way, not just that it works. Deeper still, and it's to check that the change will be easy to build with, build on, and for future engineers to understand.

In my opinion, this can be summed up in the question "do I trust the change". And ultimately, the way we can trust that changes made by other developers are something we can work with in future, is by the process of code review.1

  2. Writing tests



Here, the purpose is to build trust in our understanding of the application. Tests are an attempt to define the behaviour of the system in an understandable way, and to verify that we have built a system that matches our expectations.

You can see the theory of this trust-building exercise in action in any codebase that uses [BDD-style](https://en.wikipedia.org/wiki/Behavior-driven_development) tests. By using domain language to define the tests, you explicitly make the tests a communication exercise, explaining the business cases the application should fulfil in understandable terms.

  3. Team-building exercises



Perhaps I'm stating the obvious here, but the primary aim of these activities is to strengthen inter-personal relationships. Creating that social connection builds trust between colleagues, enabling the team to work together more closely. It's very hard to rely on someone in a pressure situation when you've never had a conversation with them.

  4. Agile methodologies



Whether you're unfortunate enough to be at a company trying to implement SAFe, or a wizened guru working in an XP-only team, one of the key problems you're trying to solve with whatever agile methodology you employ is predictability of output. And why do we care about that? Because the wider company needs to be able to trust your ability to deliver.

The _whole point_ of breaking work down into small chunks, fast feedback cycles, iterative development, etc. is to build in repeatability and reliability to an otherwise unreliable process. It is impossible to build a company on a completely unpredictable delivery schedule.

But software development is complex, and estimates in this industry are as reliable as tea leaves. So, to enable other teams to rely on our work, to trust our ability to either deliver on time or give early signals about changes to planned schedules, we create frameworks that try to reduce some of that inherent uncertainty.

* * *

Examining these four examples you can see the work of trust-building being carried out in many different areas on a daily basis by every member of a technical team.

  * **Technical trust:** that your collection of classes solves a customer problem, by writing BDD-style tests
  * **Architectural trust:** that your software is sensibly constructed, extensible, and maintainable, by performing code review
  * **Inter-personal trust:** that your colleagues are people who understand you and on that you can rely on, by holding team-building events (or more generally encouraging socialising within a company)
  * **Organisational trust:** that technical teams in your organisation are able to deliver features reliably, communication problems early, and react to changes swiftly, by following an agile methodology



A high-performing team is one that builds trust successfully in all of these four areas (and possibly more - [let me know](/contact) if you think I've missed any!). But what is also important to note is that the level of activity that is required to build the necessary trust in each of these areas will vary between teams based on the level of experience of the technical team, how long each of them has worked together, how the rest of the organisation around them behaves, or any other number of factors.

This also, therefore, explains why there is no one-size-fits-all approach to forming a successful technical team2. The appropriate course to take to build trust is highly context-dependent.

So, if you are finding that your processes are no longer working for you - that your team is rubbing up against some sharp edges in your daily work - take a step back and examine whether you can trust your code, your architecture, your teammates, and your ability to deliver. If any of those is uncertain, that's where you need to make changes.

* * *

  1. There's an interesting extended network dynamic here as well, where if I trust person A, and they review person B's code, I _implicitly_ gain trust in person B's output. This effect then chains across a whole organisation, and we get a functioning department. Cool huh? ↩︎

  2. … and therefore why top-down enforced processes like SAFe are doomed to failure. ↩︎




  * [Development Processes](/tags/development-processes/)
  * [Teamwork](/tags/teamwork/)
  * [Management](/tags/management/)



Related

  * [XTC discusses Basecamp's Shape-Up](/posts/xtc-basecamp-shape-up/)
  * [The Temple of Fail](/posts/temple-of-fail/)
  * [A quick guide for productive development](/posts/a-quick-guide-for-productive-development/)
  * [The customer is always right](/posts/the-customer-is-always-right/)
  * [Things that made me think: Enshittification, apathy, and discrimination](/posts/ttmmt-1/)
  * [Cull your dependencies](/posts/cull-your-dependencies/)
  * [DORA? I barely know her!](/posts/dora-i-barely-know-her/)
  * [Getting the right scale](/posts/getting-the-right-scale/)



[Optimising for trust](https://tomrenner.com/posts/optimising-for-trust/) [Tom Renner](/)

[ (C) My place to put things 2026 ](https://tomrenner.com/)

[ ](https://mastodon.social/@trenner "follow on Mastodon - Opens in a new window")[ ](https://github.com/tr325 "follow on GitHub - Opens in a new window")[ ](http://linkedin.com/in/tom-renner "follow on LinkedIn - Opens in a new window")[ ]( "follow on  - Opens in a new window")[ ](https://tomrenner.com/index.xml "follow on RSS - Opens in a new window")
