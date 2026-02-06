# Logic for Programmers New Release and Next Steps

**来源:** https://buttondown.com_hillelwayne
**链接:** https://buttondown.com/hillelwayne/archive/logic-for-programmers-new-release-and-next-steps/
**日期:** Wed, 04 Feb 2026 14:00:00 +0000

---

#  [ Computer Things ](https://buttondown.com/hillelwayne)

[ Archives ](/hillelwayne/archive/)

Search...

[ Subscribe ](https://buttondown.com/hillelwayne#subscribe-form)

February 4, 2026 

# Logic for Programmers New Release and Next Steps

## Logic for Programmers v0.13, now with 20% more content!

![cover.jpg](https://assets.buttondown.email/images/f821145f-d310-403c-88f4-327758a66606.jpg?w=480&fit=max)

It's taken four months, but the next release of [Logic for Programmers is now available](https://logicforprogrammers.com)! v0.13 is over 50,000 words, making it both 20% larger than v0.12 and officially the longest thing I have ever written.1 Full release notes are [here](https://github.com/logicforprogrammers/book-assets/blob/master/CHANGELOG.md), but I'll talk a bit about the biggest changes. 

For one, every chapter has been rewritten. Every single one. They span from _relatively_ minor changes to complete chapter rewrites. After some rough git diffing, I think I deleted about 11,000 words?2 The biggest change is probably to the Alloy chapter. After many sleepless nights, I realized the right approach wasn't to teach Alloy as a _data modeling_ tool but to teach it as a _domain modeling_ tool. Which technically means the book no longer covers data modeling.

There's also a lot more connections between the chapters. The introductory math chapter, for example, foreshadows how each bit of math will be used in the future techniques. I also put more emphasis on the general "themes" like the expressiveness-guarantees tradeoff (working title). One theme I'm really excited about is compatibility (extremely working title). It turns out that the [Liskov substitution principle](https://buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/)/subtyping in general, [database migrations](https://buttondown.com/hillelwayne/archive/refinement-without-specification/), backwards-compatible API changes, and [specification refinement](https://hillelwayne.com/post/refinement/) all follow _basically_ the same general principles. I'm calling this "compatibility" for now but prolly need a better name.

Finally, there's just a lot more new topics in the various chapters. `Testing` properly covers structural and metamorphic properties. `Proofs` covers proof by induction and proving recursive functions (in an exercise). `Logic Programming` now finally has a section on answer set programming. You get the picture.

### Next Steps

There's a lot I still want to add to the book: proper data modeling, data structures, type theory, model-based testing, etc. But I've added new material for two year, and if I keep going it will never get done. So with this release, all the content is in!

Just like all the content was in [two Novembers ago](https://buttondown.com/hillelwayne/archive/five-unusual-raku-features/) and [two Januaries ago](https://buttondown.com/hillelwayne/archive/logic-for-programmers-project-update/) and [last July](https://buttondown.com/hillelwayne/archive/logic-for-programmers-turns-one/). To make it absolutely 100% for sure that I won't be tempted to add anything else, I passed the whole manuscript over to a copy editor. So if I write more, it won't get edits. That's a pretty good incentive to stop.

I also need to find a technical reviewer and proofreader. Once all three phases are done then it's "just" a matter of fixing the layout and finding a good printer. I don't know what the timeline looks like but I really want to have something I can hold in my hands before the summer.

(I also need to get notable-people testimonials. Hampered a little in this because I'm trying real hard not to quid-pro-quo, so I'd like to avoid anybody who helped me or is mentioned in the book. And given I tapped most of my network to help me... I've got some ideas though!)

There's still a lot of work ahead. Even so, for the first time in two years I don't have research to do or sections to write and it feels so crazy. Maybe I'll update my blog again! Maybe I'll run a workshop! Maybe I'll go outside if Chicago ever gets above 6°F! 

* * *

## Conference Season

After a pretty slow 2025, the 2026 conference season is looking to be pretty busy! Here's where I'm speaking so far:

  * [QCon London](https://qconlondon.com/), March 16-19
  * [Craft Conference](https://craft-conf.com/2026), Budapest, June 4-5
  * [Software Should Work](https://softwareshould.work/), Missouri, July 16-17
  * [Houston Functional Programmers](https://hfpug.org/), Virtual, December 3



For the first three I'm giving variations of my talk "How to find bugs in systems that don't exist", which I gave last year at [Systems Distributed](https://systemsdistributed.com/). Last one will ideally be a talk based on LfP. 

* * *

  1. The second longest was my 2003 NaNoWriMo. The third longest was _Practical TLA+_. ↩

  2. This means I must have written 20,000 words total. For comparison, the v0.1 release was 19,000 words. ↩




_If you're reading this on the web, you can subscribe[here](/hillelwayne). Updates are once a week. My main website is [here](https://www.hillelwayne.com)._

_My new book,_ Logic for Programmers _, is now in early access! Get it[here](https://leanpub.com/logic/)._

Don't miss what's next. Subscribe to Computer Things: 

Email address (required)

Subscribe

#### Add a comment:

Comment and Subscribe 

Share this email:

[ Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A//buttondown.com/hillelwayne/archive/logic-for-programmers-new-release-and-next-steps/&title=Logic%20for%20Programmers%20New%20Release%20and%20Next%20Steps) [ Share on LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//buttondown.com/hillelwayne/archive/logic-for-programmers-new-release-and-next-steps/) [ Share on Hacker News ](https://share.bingo/hn?url=https%3A//buttondown.com/hillelwayne/archive/logic-for-programmers-new-release-and-next-steps/) [ Share on Bluesky ](https://share.bingo/bluesky?url=https%3A//buttondown.com/hillelwayne/archive/logic-for-programmers-new-release-and-next-steps/)

Powered by [Buttondown](https://buttondown.com/refer/hillelwayne), the easiest way to start and grow your newsletter.
