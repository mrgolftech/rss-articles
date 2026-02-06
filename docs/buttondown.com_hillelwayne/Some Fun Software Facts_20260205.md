# Some Fun Software Facts

**来源:** https://buttondown.com_hillelwayne
**链接:** https://buttondown.com/hillelwayne/archive/some-fun-software-facts/
**日期:** Wed, 10 Dec 2025 18:45:37 +0000

---

#  [ Computer Things ](https://buttondown.com/hillelwayne)

[ Archives ](/hillelwayne/archive/)

Search...

[ Subscribe ](https://buttondown.com/hillelwayne#subscribe-form)

December 10, 2025 

# Some Fun Software Facts

Last newsletter of the year!

First some news on _Logic for Programmers_. Thanks to everyone who donated to the [feedchicago charity drive](https://buttondown.com/hillelwayne/archive/get-logic-for-programmers-50-off-support-chicago)! In total we raised $2250 for Chicago food banks. Proof [here](https://link.fndrsp.net/CL0/https:%2F%2Fgiving.chicagosfoodbank.org%2Freceipts%2FBMDDDCAF%3FreceiptType=oneTime%26emailLog=YS699MZW/2/0100019ae2b7eb92-7c917ad0-c94e-4fe2-8ee1-1b9dc521c607-000000/brmxoTOvoJN94I9nQH26s7fRrmyFDj_Jir1FySSoxCw=434).

If you missed buying _Logic for Programmers_ real cheap in the charity drive, you can still get it for $10 off with the holiday code [hannukah-presents](https://leanpub.com/logic/c/hannukah-presents). This will last from now until the end of the year. After that, I'll be raising the price from $25 to $30.

Anyway, to make this more than just some record keeping, let's close out with something light. I'm one of those people who loves hearing "fun facts" about stuff. So here's some random fun facts I accumulated about software over the years:

  * In 2017, a team of eight+ programmers [successfully implemented Tetris](https://codegolf.stackexchange.com/questions/11880/build-a-working-game-of-tetris-in-conways-game-of-life) as a [game of life simulation](https://en.wikipedia.org/wiki/Conway's_Game_of_Life). The GoL grid had an area of 30 trillion pixels and implemented a full programmable CPU as part of the project.


  * Computer systems have to deal with leap seconds in order to keep UTC (where one day is 86,400 seconds) in sync with UT1 (where one day is exactly one full earth rotation). The people in charge recently passed a resolution to abolish the leap second by 2035, letting UTC and UT1 slowly drift out of sync.


  * [Vim is Turing complete](https://buttondown.com/hillelwayne/archive/vim-is-turing-complete/).



  * The backslash character basically didn't exist in writing before 1930, and [was only added to ASCII](http://dump.deadcodersociety.org/ascii.pdf) so mathematicians (and ALGOLists) could write `/\` and `\/`. It's popular use in computing stems entirely from being a useless key on the keyboard.


  * [Galactic Algorithms](https://en.wikipedia.org/wiki/Galactic_algorithm) are algorithms that are theoretically faster than algorithms we use, but only at scales that make them impractical. For example, matrix multiplication of NxN is [normally](https://en.wikipedia.org/wiki/Strassen_algorithm) O(N^2.81). The [Coppersmith Winograd](https://www-auth.cs.wisc.edu/lists/theory-reading/2009-December/pdfmN6UVeUiJ3.pdf) algorithm is O(N^2.38), but is so complex that it's vastly slower for even [10,000 x 10,000 matrices](https://mathoverflow.net/questions/1743/what-is-the-constant-of-the-coppersmith-winograd-matrix-multiplication-algorithm). It's still interesting in advancing our mathematical understanding of algorithms!


  * Cloudflare generates random numbers by, in part, [taking pictures of 100 lava lamps](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/).


  * Mergesort is older than bubblesort. Quicksort is slightly younger than bubblesort but older than the _term_ "bubblesort". Bubblesort, btw, [does have some uses](https://buttondown.com/hillelwayne/archive/when-would-you-ever-want-bubblesort/).


  * Speaking of mergesort, most implementations of mergesort pre-2006 [were broken](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/). Basically the problem was that the "find the midpoint of a list" step _could_ overflow if the list was big enough. For C with 32-bit signed integers, "big enough" meant over a billion elements, which was why the bug went unnoticed for so long.


  * [PDF's drawing model cannot render perfect circles](https://nibblestew.blogspot.com/2023/09/circles-do-not-exist.html).


  * People make fun of how you have to flip USBs three times to get them into a computer, but there's supposed to be a guide: according to the standard, USBs are supposed to be inserted _logo-side up_. Of course, this assumes that the port is right-side up, too, which is why USB-C is just symmetric. 


  * I was gonna write a fun fact about how all spreadsheet software treats 1900 as a leap year, as that was a bug in Lotus 1-2-3 and everybody preserved backwards compatibility. But I checked and Google sheets considers it a normal year. So I guess the fun fact is that things have changed!


  * Speaking of spreadsheet errors, in 2020 [biologists changed the official nomenclature](https://www.engadget.com/scientists-rename-genes-due-to-excel-151748790.html) of 27 genes because Excel kept parsing their names as dates. F.ex MARCH1 was renamed to MARCHF1 to avoid being parsed as "March 1st". Microsoft rolled out a fix for this... three years later.


  * It is possible to encode any valid JavaScript program with just the characters `()+[]!`. This encoding is called [JSFuck](https://en.wikipedia.org/wiki/JSFuck) and was once used to distribute malware on [Ebay](https://arstechnica.com/information-technology/2016/02/ebay-has-no-plans-to-fix-severe-bug-that-allows-malware-distribution/).



Happy holidays everyone, and see you in 2026!

* * *

  1. Current status update: I'm finally getting line by line structural editing done and it's turning up lots of improvements, so I'm doing more rewrites than I expected to be doing. ↩




_If you're reading this on the web, you can subscribe[here](/hillelwayne). Updates are once a week. My main website is [here](https://www.hillelwayne.com)._

_My new book,_ Logic for Programmers _, is now in early access! Get it[here](https://leanpub.com/logic/)._

Don't miss what's next. Subscribe to Computer Things: 

Email address (required)

Subscribe

#### Add a comment:

Comment and Subscribe 

Share this email:

[ Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A//buttondown.com/hillelwayne/archive/some-fun-software-facts/&title=Some%20Fun%20Software%20Facts) [ Share on LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//buttondown.com/hillelwayne/archive/some-fun-software-facts/) [ Share on Hacker News ](https://share.bingo/hn?url=https%3A//buttondown.com/hillelwayne/archive/some-fun-software-facts/) [ Share on Bluesky ](https://share.bingo/bluesky?url=https%3A//buttondown.com/hillelwayne/archive/some-fun-software-facts/)

Powered by [Buttondown](https://buttondown.com/refer/hillelwayne), the easiest way to start and grow your newsletter.
