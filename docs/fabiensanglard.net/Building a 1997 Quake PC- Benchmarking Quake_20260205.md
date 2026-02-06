# Building a 1997 Quake PC: Benchmarking Quake

**来源:** https://fabiensanglard.net
**链接:** https://fabiensanglard.net/quake_pc/quake/index.html
**日期:** 12 Jan 2026 00:00:00 +0000

---

  


[**FABIEN SANGLARD'S WEBSITE**  
](/)

* * *

[CONTACT](mailto:fabiensanglard.net@gmail.com)    [RSS](../rss.xml)     [DONATE](https://paypal.me/fabiensanglard)

  
  


Jan 12, 2026  
  
This article is part of the [Quake PC series](../).

Building a Quake PC: Benchmarking Quake

* * *

Getting into the benchmark of the software rendered versions of Quake, there were so many questions I wanted to answer.

Is `quake.exe` as fast under Windows 95 as under DOS? What about `winquake.exe` under Windows? What is the impact of the video card bus? How good was Intel compared to Cyrix and the AMD K5? Did the K6 do better than K5? What about RAM, is SDRAM really making a difference compared to EDO? Does AGP really provide an improvement over PCI?

Test conditions

* * *

Unless specified otherwise, all the benchmarks were run under gameplay conditions. That is, from DOS, with sound on, music playing from the CD, and view size set to 101 ([example](quake_screen_101.png)). The graphic card was always a Matrox Mystique or Matrox Millenium. The motherboard for all Socket 7 CPUs was a XA100[1]. I used the `demo1` demo for all my benchmarks.

Running the command `timedemo demo1` will fail in Quake v1.01. The command was only introduced starting in v1.06.

[![](cpu_roaster.webp)](cpu_roaster.webp)_Part of the CPU roaster. The K5 is missing and the ugly one on the right is a[P200](p200.webp)._

Intel benchmark

* * *

[![](chart_pentium.svg)](chart_pentium.svg)

Intel CPUs start to provide an enjoyable experience around 90MHz (at least for my taste) with the Pentium 120Mhz being the sweet spot, clocking at roughly 30 fps.

Checking out June '96 magazine also indicates that Pentium 120MHz were the standard new machine at the time[2] so id's timing was not too bad.

Even a Pentium 75MHz was able to provide 20 fps which, by 1996 standard, was "smooth". A bit of usenet archeology reveals that customer's expectations were quite different from now.

> I have a p133, 16mb ram, 4mb millenium, and I run quake at 512x384, and get 17fps... works and looks great.  
>    
> 
> 
> \- Matthew Lowth (rec.games.computer.quake.playing 1996)[3]

What a time the late '90s were. In these magazines, one could frequently find ads "The demand for computer programmers will double by the year 2005. Train now for a high-career as a computer programmer!"[4].

Intel MMX benchmark

* * *

A Pentium MMX runs _QUAKE_ faster but not because of MMX instructions (_QUAKE_ doesn't use them). With its ability to process up to four times the data via SIMD an MMX CPU is more subject to instructions starvation. Moreover, the pipeline had been extended from five to six stages in order to decode MMX instructions. To fix these two problems, an MMX Pentium features the following improvements.

  * Double dCache and iCache size (16KiB each) to reduce the performance lost from cache misses at high core clock speeds.
  * The longer pipeline has a cost of one extra penalty cycle on a mispredicted branch. To mitigate this downside, the P55C has an enhanced branch target buffer that uses a two- level algorithm similar to the P6.
  * New stage provides other benefits as well: it provides slightly more data-cache access time (another critical path in P54C), so it should improve 200-MHz yield, and it allows non-MMX instructions to be paired for dual-issue in some circumstances that the P54C did not allow. 

[![](chart_mmx.svg)](chart_mmx.svg)

As a result, an MMX CPU is able to run Quake 7% faster than a "normal" Intel CPU running at the same frequency.

Cyrix 6x86 benchmark

* * *

The story of the Cyrix 6x86 and how its abysmal performance contributed to killing the company is quite notorious. But how bad was it really? Really really bad it turned out.

[![](chart_cyrix.svg)](chart_cyrix.svg)

The outcry from players at the time was significant with many taking it to usenet to manifest they disappointment. When a post features 106 exclamation marks (I counted), you know they are for real.

> WARNING: DON’T BUY CYRIX.READ THIS NEWS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!“ 
> 
> \- – comp.sys.ibm.pc.games.action (1996)[5]

The issue was compounded by Cyrix's usage of Performance Rating (PR) to label its processors. A 6x86 P166+ ran at 133MHz but Cyrix was confident to tell consumers it was the equivalent of an Intel Pentium 166MHz. This may have been true for integer operations but not for floating-point, which Quake used a lot of. As a result, a Cyrix CPU ran quake.exe at 50% the speed of an Intel CPU.

> I have done extensive testing of the Cyrix 6x86 P150+ and the Intel P150 in the exact same system (I just swapped CPU’s) and the P150+ is impressive (just a hair faster) as long as applications that use FP math are avoided. However, many newer applications and games are taking advantage of FP math, and the Cyrix REALLY SUCKS on these apps. 
> 
> \- comp.sys.ibm.pc.games.action (1996)[6]

Cyrix degraded their reputation further with their infamous "Floating Point Performance Summary"[7] with benchmarks using a 3D accelerator and statements showing a complete disconnect with the gamer community.

> To achieve smooth motion, the frame rate typically needs to be greater than approximately 13 frames/second. 
> 
> \- Cyrix Floating Point Performance Summary(1996)[8]

A year later, the explanation for these abysmal performances was given by John Carmack.

> The floating-point issue has really hurt AMD and Cyrix. We had AMD and Cyrix down here while we were developing Quake, and we said, ”Look, floating point’s going to be important,” but because there weren’t any benchmarks or any applications they’d used at that time, they brushed it under the rug.  
>    
>  AMD and Cyrix both have non-pipeline FPUs, which is their Achilles’ heel. In terms of integer performance a lot of them are on par or, even in some cases, better than Intel, but we optimize for Intel because the Pentium’s got the FXCH change trick to pipeline all these things. And it’s pretty tweaky but it pervades all of our assembly language code for Quake. So we’re de-optimized for non-Intel chips, but it was the only sensible thing to do. 
> 
> \- John Carmack (1997)[9]

If you want to learn more about Cyrix and Quake, Nostalgia Nerd made a cool video about it[10].

AMD K5 benchmark

* * *

The AMD K5 suffered the same kind of floating-point shortcoming as the Cyrix 6x86. AMD also used a Performance Rating (PR) system which made players feel like they had been deceived.

[![](chart_k5.svg)](chart_k5.svg)

An AMD K5 runs _Quake_ at roughly 50% the framerate of an Intel CPU.

AMD K6 benchmark

* * *

Contrary to Cyrix, AMD survived Quakegueddon. Less than a year later after the K5, they managed to ship the K6. The details of whether they had to improve floating-point because of the K5 fiasco or if they already had it in the pipeline is unknown but they did rectify (but not to the point of beating Intel).

[![](chart_k6.svg)](chart_k6.svg)

If you want to learn more about the internals of the K6, _RTL Engineering_ did a really good video about it[11].

Performance DOS vs Windows 95

* * *

The difference between `quake.exe` running under DOS and Windows is something already covered in a prior article ([Why WinQuake exists and how it works](../../winquake)).

The performance hit is noticeable. While a Pentium MMX 233 MHz can reach 48 fps under DOS, the framerate drops to roughly 38 fps under Windows 95. That is roughly 25% slower. 

I ran into issues to enable SB emulation with the SB Live. I kept on getting this weird error.
    
    
    Error: Config file is incomplete.
    SBPort
    Creative SB16 Emulation Driver NOT Loading.
    

The problem was that I transferred the drivers as a folder over FTP and it messed up the carriage return formatting of text files. As much as possible, files should be transferred as zip archive or iso.

Performance Windows 95 vs WinQuake

* * *

Likewise, this is something already covered in [Why WinQuake exists and how it works](../../winquake). The port to win32 greatly reduced the performance gap. Using its fastest backend, `winquake.exe` brings up the framerate within 6% of `quake.exe` running under DOS.

Configuration | Framerate (P233 MMX)  
---|---  
`quake.exe` on DOS | 48  
`quake.exe` on Windows 9X | 38  
`winquake.exe` (fastvid) on Windows 9X | 45  
  
AGP vs PCI

* * *

I wanted to see if using an AGP card would make things better so I got a Matrox G200 SGRAM ([798-02](https://theretroweb.com/expansioncards/s/matrox-g200-sgram-798-02)). This is not a really fair comparison because this is not the same graphic chip as the one in the Matrox Mystique 220 4MB ([644-03](https://theretroweb.com/expansioncards/s/matrox-mystique-4mb-644-03)) but I thought it was pretty close.

[![](pci_agp.webp)](pci_agp.webp)

I could barely measure any difference. Sometimes performance would be 1fps lower, sometimes 1fps higher.

EDO vs SDRAM

* * *

I purchased 128 MiB of EDO DIMM to compare with SDRAM. On paper, EDO is 33% slower than SDRAM so I was curious to see the impact on _Quake_ framerate.

[![](ram.webp)](ram.webp)

The difference could barely be measured. With EDO, `winquake.exe` in `fastvid` mode ran at 44.6 fps. With SDRAM, I got 45 fps. That is a mere 1% difference. My hypothesis is that the L1 and L2 cache are hit so much that the difference between EDO and SDRAM is not visible.

Pentium Pro

* * *

It was beyond the scope of what I could benchmark on this machine but there was a section of [TECHINFO.TXT](https://raw.githubusercontent.com/id-Software/Quake/refs/heads/master/WinQuake/data/TECHINFO.TXT#:~:text=The%20Pentium%20Pro%20is%20a%20very%20fast%20Quake%20platform) about the P6 that intrigued me.
    
    
    The Pentium Pro is a very fast Quake platform.
    In 640x480 it was very playable (and looked great!).

To run these benchmarks, a fellow retro-enthousiast's W6-LI[12] motherboard was used with a Matrox Mystique (with fastvid.exe to fix the 440FX chipset video bug).

[![](chart_p6.svg)](chart_p6.svg)

The Pentium Pro is faster than even a Pentium MMX at the same frequency. The performance is not surprising since the P6 was a complete departure from the P5, featuring out-of-order execution and a humongous on-board L2. It was so good, its architecture became the basis of the Pentium II.

As for 640x480, it ran "pooly" by 2026 standard, and "butter-smooth" by 1996 standards[13].

[![](chart_p6_640x480.svg)](chart_p6_640x480.svg)

Next

* * *

Benchmarking [VQuake](../vquake/).

References

* * *

^|  [ 1]| Non-Socket 7 benchmarks were run on fellow retro-enthusiasts machines.  
---|---|---  
^|  [ 2]| [PC ads in June 96](https://archive.org/details/home-pc-magazine-1996-07/page/54/mode/2up)  
^|  [ 3]| [How does Quake run on a P133?](https://groups.google.com/g/rec.games.computer.quake.playing/c/8xLgEdgN410/m/IUfM7MFqiJMJ)  
^|  [ 4]| [](https://archive.org/details/home-pc-magazine-1996-07/page/172/mode/2up)  
^|  [ 5]| [WARNING: DON'T BUY CYRIX. READ THIS NEWS!](https://groups.google.com/g/comp.sys.ibm.pc.games.action/c/dtrupvl11tk)  
^|  [ 6]| [WARNING: DON'T BUY CYRIX. READ THIS NEWS!](https://groups.google.com/g/comp.sys.ibm.pc.games.action/c/dtrupvl11tk)  
^|  [ 7]| [Cyrix Floating Point Performance Summary](https://www.alaska.net/~akusedpc/pages/cyrix/fpu-summ.htm)  
^|  [ 8]| [Cyrix Floating Point Performance Summary: Smooth framerate](https://www.alaska.net/~akusedpc/pages/cyrix/fpu-summ.htm#:~:text=To%20achieve%20smooth%20motion%2C%20the%20frame%20rate%20typically%20needs%20to%20be%20greater%20than%20approximately%2013%20frames/second.)  
^|  [ 9]| [John Carmack - The Boot Interview](https://web.archive.org/web/19980130151620/www.bootnet.com/youaskedforit/lip_16_outtakes.html)  
^|  [10]| [Nostalgia Nerd: What Happened to Cyrix Processors?](https://www.youtube.com/watch?v=iWGAdoMz1c0)  
^|  [11]| [RTL Engineering: Quake, Floating Point, and the Intel Pentium](https://www.youtube.com/watch?v=DWVhIvZlytc)  
^|  [12]| [Micronics W6-LI ](https://theretroweb.com/motherboards/s/micronics-w6-li-09-00288-xx)  
^|  [13]| [Comparison of Frame-rates in Quake](https://www.soldcentralfl.com/quakecoop/compare1.htm#:~:text=The%20minimum%20acceptable%20frame%2Drate%20that%20allows%20an%20enjoyable%20game%20of%20Quake%20in%202D%2C%20running%20DOS%20Quake%20WinQuake%2C%20or%20QuakeWorld%2C%20is%2013%20%2D%2015%20FPS)  
  
* * *

*
