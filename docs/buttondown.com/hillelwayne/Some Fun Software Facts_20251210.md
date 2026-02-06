# Some Fun Software Facts

**来源:** [buttondown.com/hillelwayne](https://buttondown.com/hillelwayne/rss)
**发布时间:** Wed, 10 Dec 2025 18:45:37 +0000
**链接:** https://buttondown.com/hillelwayne/archive/some-fun-software-facts/

---

Last newsletter of the year!
First some news on
Logic for Programmers
. Thanks to everyone who donated to the
feedchicago charity drive
! In total we raised $2250 for Chicago food banks. Proof
here
.
If you missed buying
Logic for Programmers
real cheap in the charity drive, you can still get it for $10 off with the holiday code
hannukah-presents
. This will last from now until the end of the year. After that, I'll be raising the price from $25 to $30.
Anyway, to make this more than just some record keeping, let's close out with something light. I'm one of those people who loves hearing "fun facts" about stuff. So here's some random fun facts I accumulated about software over the years:
In 2017, a team of eight+ programmers
successfully implemented Tetris
as a
game of life simulation
. The GoL grid had an area of 30 trillion pixels and implemented a full programmable CPU as part of the project.
Computer systems have to deal with leap seconds in order to keep UTC (where one day is 86,400 seconds) in sync with UT1 (where one day is exactly one full earth rotation). The people in charge recently passed a resolution to abolish the leap second by 2035, letting UTC and UT1 slowly drift out of sync.
Vim is Turing complete
.
The backslash character basically didn't exist in writing before 1930, and
was only added to ASCII
so mathematicians (and ALGOLists) could write
/\
and
\/
. It's popular use in computing stems entirely from being a useless key on the keyboard.
Galactic Algorithms
are algorithms that are theoretically faster than algorithms we use, but only at scales that make them impractical. For example, matrix multiplication of NxN is
normally
O(N^2.81). The
Coppersmith Winograd
algorithm is O(N^2.38), but is so complex that it's vastly slower for even
10,000 x 10,000 matrices
. It's still interesting in advancing our mathematical understanding of algorithms!
Cloudflare generates random numbers by, in part,
taking pictures of 100 lava lamps
.
Mergesort is older than bubblesort. Quicksort is slightly younger than bubblesort but older than the
term
"bubblesort". Bubblesort, btw,
does have some uses
.
Speaking of mergesort, most implementations of mergesort pre-2006
were broken
. Basically the problem was that the "find the midpoint of a list" step
could
overflow if the list was big enough. For C with 32-bit signed integers, "big enough" meant over a billion elements, which was why the bug went unnoticed for so long.
PDF's drawing model cannot render perfect circles
.
People make fun of how you have to flip USBs three times to get them into a computer, but there's supposed to be a guide: according to the standard, USBs are supposed to be inserted
logo-side up
. Of course, this assumes that the port is right-side up, too, which is why USB-C is just symmetric.
I was gonna write a fun fact about how all spreadsheet software treats 1900 as a leap year, as that was a bug in Lotus 1-2-3 and everybody preserved backwards compatibility. But I checked and Google sheets considers it a normal year. So I guess the fun fact is that things have changed!
Speaking of spreadsheet errors, in 2020
biologists changed the official nomenclature
of 27 genes because Excel kept parsing their names as dates. F.ex MARCH1 was renamed to MARCHF1 to avoid being parsed as "March 1st". Microsoft rolled out a fix for this... three years later.
It is possible to encode any valid JavaScript program with just the characters
()+[]!
. This encoding is called
JSFuck
and was once used to distribute malware on
Ebay
.
Happy holidays everyone, and see you in 2026!
Current status update: I'm finally getting line by line structural editing done and it's turning up lots of improvements, so I'm doing more rewrites than I expected to be doing.
↩

---

*抓取时间: 2026-02-05 13:04:48*
