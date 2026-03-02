# AMD Am386 released March 2, 1991

**来源:** [dfarq.homeip.net](https://dfarq.homeip.net)
**发布时间:** Mon, 02 Mar 2026 12:00:23 +0000
**链接:** https://dfarq.homeip.net/amd-am386-released-march-2-1991/?utm_source=rss&utm_medium=rss&utm_campaign=amd-am386-released-march-2-1991

---

Dave Farquhar
Retro Computing
March 2, 2026
January 4, 2026
0 Comment
There is a popular misconception that AMD wasn’t good at cloning Intel CPUs. This is largely based on the observation that Intel released its 386 CPU in 1985, and AMD didn’t counter with its Am386 clone until March 2, 1991, nearly six years later. In this blog post, we will explore what took AMD so long, and how that delay played into future AMD CPUs.
Intel and its agreement with IBM
AMD was finally able to release its Am386 in March 1992, even as legal battles with Intel continued until 1995.
When IBM selected the
Intel 8088 CPU
to power its
IBM PC 5150
, IBM insisted on Intel licensing the design to at least one other chip manufacturer. This was to ensure that IBM would have a sufficient supply of chips to meet demand. It was also not a particularly unusual request. Both Apple and Atari had multiple sources for the chips they used in their computers, for instance.
Intel did IBM one better. Not only did they license the design to AMD, but they licensed it to several other companies as well. And after IBM selected the
80286 CPU
to power its
PC/AT
, Intel amended the agreement with AMD and several others so they could manufacture not only 8088 and 8086 CPUs, but 80286 CPUs as well.
But the 386 was different.
It wasn’t just that Intel got greedy
The now-popular story is that with the 386 generation, Intel got greedy and decided to shut everyone out. At best, that’s an oversimplification of what happened. When Intel released the 80386 on October 17, 1985, IBM didn’t want it. Today this sounds absurd. Why would IBM not want Intel’s most advanced CPU?
In the mid 1980s, IBM still had a very lucrative business selling minicomputers. These were medium-sized computers designed for applications where a mainframe would be overkill but a PC wasn’t powerful enough. And IBM’s pricing didn’t scale linearly. Mainframes were the most profitable systems for IBM, and microcomputers–what we now call desktops–were the least. Minicomputers were in between.
IBM didn’t want the Intel 386 because it performed like a minicomputer chip. IBM could price its low-end System/36 minicomputers at $20,000 circa 1985, so they saw an Intel 386-based PC priced at $10,000 as a threat, not an opportunity. They didn’t want businesses buying a 386-based PC and loading Unix on it instead of buying a traditional minicomputer that cost twice as much.
That meant Intel had no reason to amend its agreement and extend the 386 to second sources. IBM wasn’t asking.
Compaq famously released a
386-based PC in 1986
, forcing IBM to do the same within 12 months. By then, IBM was in no position to demand Intel license the 386 to second sources like AMD. All IBM could do was use its existing agreements to make Intel processors itself, in effect, being its own second source.
IBM had its own chip fabrication plant in Burlington, Vt. and was capable of manufacturing CPUs. Eventually IBM did produce 386 and 486 CPUs, but not immediately. According to the April 10, 1989 issue of
Infoworld
, it wasn’t until early April 1989 that IBM exercised its option to start making 386 CPUs itself.
It was IBM’s initial disinterest more than anything else that locked out AMD.
How AMD cloned the 386 CPU
Contrary to popular narrative today, it didn’t take AMD six years to clone the 386 CPU. It only took AMD’s engineers about two years to reverse engineer the 386 and implement their own clean-room design on top of what they already knew from making 286 CPUs that was compatible with Intel’s 386. But the two companies battled in court for a total of eight years, until 1995, and spent a total of $100 million in the process. Intel’s goal was to keep the AMD chips off the market altogether, and where they failed at that, they settled to delay the AMD chips as long as possible. The longer the court battles dragged on, the more Intel was able to bleed AMD.
Intel tried everything, including claiming the number 386 was a trademark, and when AMD started ramping up clock rates of 286 processors to 16 and 20 MHz to try to compete while its 386 was tied up in court, Intel tried to rescind AMD’s rights to manufacture 286s. Both of those efforts proved unsuccessful.
On March 2, 1991, AMD prevailed in arbitration and was clear to release its 386 CPU. Intel then moved on to trying to keep AMD from releasing a clone of the 486. In that case as well, Intel was able to delay AMD’s 486 but not block it. Intel
was
successful in blocking a Pentium clone that used any Intel IP. And
that
was why AMD used its own design for its fifth-generation
K5 CPU
, not because AMD was bad at reverse engineering Intel designs.
AMD’s reputation as an off-brand company
There seems to be a conception that AMD, at this stage in the late 1980s and early 1990s, was a second-tier, off-brand chip maker. This has more to do with the effectiveness of Intel’s marketing than anything AMD was doing. AMD was not a stranger to the enterprise market. When you look at teardowns of 1970s and 1980s minicomputers, you frequently find AMD chips like the AMD2900 series ALUs inside them. The IT managers who shunned AMD CPUs in the 1990s most likely used AMD technology earlier in their careers on minicomputers without having any idea.
Companies that used AMD2900-family chips included Apollo, AT&T, Centurion, Data General, Digital Equipment Corporation, Floating Point Systems, Hewlett-Packard, NCR, Tektronix, and Xerox. Basically, almost anything that wasn’t an IBM System/36. These were the same systems that the 386 and 486 threatened and then displaced over time.
So one can argue that Intel encroached on AMD’s territory with the i386. Then, with the Am386, AMD started trying to claw back in.
Effects of the delay in releasing AMD’s 386 and 486
Neither company was happy with the outcome of the legal battles, which cost the companies a total of $100 million and finally ended January 11, 1995. But the legal action favored Intel more than it favored AMD. Effectively, Intel forced AMD into remaining a CPU generation behind for more than a decade. That meant Intel could sell its highest-margin CPUs at the top end of the market without competition, while AMD sold entry-level CPUs at the low end of the market.
Since Intel enjoyed higher profit margins, it could invest those profits by building additional chip fabrication plants, or fabs, and idling some number of its existing fabs while it modernized them. More modern fabs meant lower production cost, which meant better profit margins.
AMD couldn’t beat Intel at its own game. During the 386 generation at least, AMD had to concentrate on staying in the game, and over time, figure out its own game that would work. It is possible to prevail in court but spend so much money in doing so that you effectively lose anyway, and that almost what happened to AMD in the 90s.
It wasn’t just AMD. Intel sued anyone who did anything x86-related they didn’t approve of, including
NEC
,
Chips & Technologies
,
UMC
, and
Cyrix
.
Advantages and disadvantages of the AMD Am386
As much as Intel tried to paint AMD’s Am386 as a second-rate CPU, it wasn’t. AMD released it at speeds ranging from 20 MHz to 40 MHz, and both
SX (16-bit externally) and DX (fully 32-bit) versions
. By 1991, the 16 MHz 386 was obsolete. Running at the same clock rate, AMD’s version of the 386 had essentially identical performance to the Intel original.
386 performance vs 486
It also helped that a fast 386 could keep pace with the slowest 486s. The 40 MHz version of the Am386 enjoyed an especially long shelf life as a value CPU. The 486 was more efficient than the 386 but it wasn’t twice as efficient, so a 40 MHz 386 was faster than a 20 MHz Intel 486SX, and roughly comparable to a 25 MHz 486SX. It also held the additional advantage of taking an external math coprocessor. Part of the point of the 486 was the integrated math coprocessor improved performance, but an external math coprocessor was faster than none. So while a 40 MHz 386 plus a 40 MHz 387 wasn’t as fast as a full 486DX at 25 MHz, depending on whose FPU you used, you could get 75-90 percent of the performance at less than 75 percent of the price.
The Am386’s biggest fans
Value-oriented power users favored the AMD Am386DX-40 well into the 486 era for this reason. It provided 486-level performance at a lower price, and you could invest some or all of the savings into whatever performance enhancements you needed, whether that was more RAM, a faster hard drive, a faster video card, or a math coprocessor.
Disadvantages of the Am386
Compared to the Intel 386, there was no disadvantage to speak of with going AMD. The chips were fully compatible and interchangeable. While I’ve heard claims Intel chips were more reliable, I never saw it. I never saw a 386 or 486 CPU fail unless someone plugged it into its socket the wrong way around. Even then, sometimes the CPU survived.
The disadvantage of the Am386 versus the 486 was that the 386 bus was an evolutionary dead end. The 386 topped out at 40 MHz,with the only upgrade path being one of TI and Cyrix’s
clock-multiplied 386/486 mashups
. Meanwhile, the 486 reached speeds of
133 MHz
by September 1995. But since most 40 MHz 386-based PCs were open architecture clones built from
off-the-shelf AT parts
, you could swap the motherboard and CPU while carrying over most of the rest of your parts. This was more expensive and labor intensive than swapping a CPU, but it was much cheaper to buy a 40 MHz 386 and upgrade to a faster 486 after 2-3 years than it was to buy the fastest 486 at the start.
Ultimately it was
Windows 95
that did the Am386 in. Technically, the Am386 could run Windows 95, but it wasn’t a great experience. Windows 95 really ran better on clock-doubled 486DX2 processors. Am386-based systems continued to be sold past 1995 for use as DOS or Windows 3.1 machines, but that market rapidly diminished with time. The 386 survived outside the PC market much longer as an affordable CPU for embe

... (内容已截断)

---

*抓取时间: 2026-03-03 00:03:20*
