# Building a 1997 Quake PC: Benchmarking Vquake

**来源:** https://fabiensanglard.net
**链接:** https://fabiensanglard.net/quake_pc/vquake/index.html
**日期:** 13 Jan 2026 00:00:00 +0000

---

  


[**FABIEN SANGLARD'S WEBSITE**  
](/)

* * *

[CONTACT](mailto:fabiensanglard.net@gmail.com)    [RSS](../rss.xml)     [DONATE](https://paypal.me/fabiensanglard)

  
  


Jan 13, 2026  
  
This article is part of the [Quake PC series](../).

Building a Quake PC: VQuake

* * *

The Rendition Verite 1000 is _Quake_ legend. It was the first hardware-accelerated card supported by an id title with a dedicated binary, `vquake.exe`. It was also the one used during the final round of 16 in the notorious _Red Annihilation_ tournament where _Thresh_ won[1] John Carmack's 1987 Ferrari 328 GTS Cabriolet.

In 1997, the enthusiasm for vquake and these 3D accelerators was palpable in magazines.

> Quake is almost a completely different game with the 3D Blaster. Performance was about 50% better than standard Quake on a P166-with features such as bilinear filtering and full MIP mapping turned on at 640x480, The image quality was, to put it simply, superb.  
>    
> 
> 
> \- Computer Gaming World #149[2]

Four vendors, Creative, Intergraph, Sierra, and Canopus picked up the v1000. Sierra's _Screamin’ 3D_ enjoyed good reviews[3]. That is the one I managed to find on eBay. It cost its weight in diamond but I was happy to own such an iconic piece of technology.

[![](v1000.webp)](v1000.webp)

The v1000 graphic pipeline is programmed via speedy 3D micro-code. To this effect, `vquake.exe` ships with a `SPD3D.UC`. Upgrading quake to the latest version of vquake directly will result in error "SPD3D.UC file not found or not compatible". That file was only included in vquake's first release.

Bilinear texture filtering, aka Lerp

* * *

Something that was deemed cool at the time was bilinear filtering. It was "hiding" pixels and everybody loved the effect back in the days. Thirty years later, pixels are cool again.

[![](d_lerp1.png)](d_lerp1.png)

Lerp:0      Lerp:1

Weirdly, the acronym for **l** inear int**erp** olation came to be "lerp". I used the same term in this article.

VQuake screenshots use BMP instead of PCX. This makes sense because the renderer is 16-bit color instead of palette indexed.

VQuake is indeed a game changer

* * *

As soon as Vquake started, it was obvious how much of an improvement it was over the software rendered version. The framerate is higher and the resolution as well. Despite its visual prowess the port is faithful in terms of lighting and colors. It is as dark as the original game intended.

[![](QUAKE06.png)](QUAKE06.png) [![](QUAKE12.png)](QUAKE12.png) [![](QUAKE35.png)](QUAKE35.png)

Vquake bilinear filtering has a "signature" look with a peculiar and easily recognizable type of dithering.

[![](quake49.png)](quake49.png)

Lerp:0      Lerp:1

The software renderer of Quake supports something called "full_bright" to allow textures to shine in the dark. This was an effect showcased in the E1M1 staircase to keep the player on their toes. glQuake would later fail to replicate that effect but Vquake does it perfectly.

[![](vquake_fullbright.png)](vquake_fullbright.png)

vquake      software     glquake

2D performance from DOS

* * *

Before testing its hardware-accelerated feature, I took the time to benchmark the _Screamin'3D_ with `quake.exe` software renderer. I used a Pentium MMX 233MHz under DOS with 101 view size, and sound enabled. The result was terrible with 26.2 fps. That is 50% of the framerate achieved with a Matrox Mystique (48 fps)! What a terrible VGA card!

Performance

* * *

How does vquake with Rendition Verite compare to quake running on a Matrox Mystique?

P51 MMX 233MHz | 320x200 | 320x240 | 384x288 | 400x300 | 512x384 | 640x400 | 640x480 | 720x480 | 768x576  
---|---|---|---|---|---|---|---|---|---  
Matrox Mystique | 48.0 | 45.5 |  |  |  | 18.5 | 15.7 |  |   
Rendition Verite | 52.8 | 48.9 | 44.0 | 40.6 | 30.6 | 27.1 | 23.6 | 18.1 | 14.0  
  
While there is not much of an improvement at low resolution, the v1000 does shine at higher resolution with even an MMX 233MHz unable to keep up.

Under-clocking the CPU to 133MHz showed that Vquake is not very sensitive to CPU frequency. The framerate is actually very close to what the same processor running at 233MHz could produce.

P51 MMX 133MHz | 320x200 | 320x240 | 384x288 | 400x300 | 512x384 | 640x400 | 640x480 | 720x480 | 768x576  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Matrox Mystique | 37.9 | 33.0 |  |  |  | 15.3 | 13.1 |  |   
Rendition Verite | 46.4 | 43.6 | 40.4 | 37.4 | 29.6 | 26.5 | 23.3 | 18.0 | 14.0  
  
Performance: DOS vs Windows

* * *

Next on the list, I wanted to measure perf from DOS and Windows to see if the v1000 suffered the same type of penalty as the software renderer.

| 320x200 | 320x240 | 384x288 | 400x300 | 512x384 | 640x400 | 640x480 | 720x480 | 768x576  
---|---|---|---|---|---|---|---|---|---  
DOS | 52.8 | 48.9 | 44.0 | 40.6 | 30.6 | 27.1 | 23.6 | 18.1 | 14.0  
Windows | 47.6 | 44.7 | 41.6 | 38.5 | 29.9 | 26.7 | 23.4 | 18.0 | 14.0  
  
Like `quake.exe`, `vquake.exe` does suffer a noticeable penalty when started from Windows 9X. This is only true at low resolution. As the resolution increases, the gap almost disappears.

Texture filtering

* * *

Out of all vquake's cvar[4], the most interesting one is `d_bilerp`. It allows to disable bi-linear filtering and bring back the pixels.

| 320x200 | 320x240 | 384x288 | 400x300 | 512x384 | 640x400 | 640x480 | 720x480 | 768x576  
---|---|---|---|---|---|---|---|---|---  
d_bilerp=1 | 52.8 | 48.9 | 44.0 | 40.6 | 30.6 | 27.1 | 23.6 | 18.1 | 14.0  
d_bilerp=0 | 53.2 | 49.8 | 48.5 | 42.2 | 32.6 | 33.4 | 25.6 | 21.3 | 16.3  
  
Not using bi-linear filtering improves the framerate noticeably at higher resolution. That's because the v1000 does not have any special bus/interleave to handle the extra need of sampling. This is very different from 3dfx cards where GL_LINEAR held the same performance as GL_NEAR.

Even though I much prefer the crisp pixels, this is not what players used at the time. In order to gather historically relevant metrics, I ran benchmarks with bi-linear filtering enabled (d_bilerp=1).

latest BIOS (phx2105.com)

* * *

Rendition released a TSR, [phx2105.com](phx2105.com), which updated their chip BIOS. It looks really cool to load it in the DOS prompt.

[![](v1000_bios.png)](v1000_bios.png)

The new BIOS adds two new resolutions (720x400 and 856x480) but provides next to no framerate improvement.

320x200 | 320x240 | 384x288 | 400x300 | 512x384 | 640x400 | 640x480 | 720x400 | 720x480 | 768x576 | 856x480  
---|---|---|---|---|---|---|---|---|---|---  
52.8 | 48.9 | 44.0 | 40.6 | 30.6 | 27.1 | 23.6 |  | 18.1 | 14.0 |   
53.1 | 48.8 | 44.0 | 39.4 | 30.6 | 27.1 | 23.5 | 22.0 | 18.1 | 14.0 | 16.0  
  
Impact of CPU frequency

* * *

I took the "impact of frequency" benchmark a bit further and tested various clocks on an MMX CPU.

320x200 | 320x240 | 384x288 | 400x300 | 512x384 | 640x400 | 640x480 | 720x400 | 720x480 | 768x576 | 856x480  
---|---|---|---|---|---|---|---|---|---|---  
53.1 | 48.8 | 44.0 | 39.4 | 30.6 | 27.1 | 23.5 | 22.0 | 18.1 | 14.0 | 16.0  
51.4 | 47.9 | 43.4 | 39.1 | 30.5 | 27.1 | 23.5 | 21.9 | 18.1 | 14.0 | 16.0  
49.3 | 46.1 | 42.5 | 38.5 | 30.2 | 26.9 | 23.4 | 21.9 | 18.1 | 14.1 | 16.0  
46.4 | 43.6 | 40.4 | 37.4 | 29.6 | 26.5 | 23.3 | 21.8 | 18.0 | 14.0 | 16.0  
[![](freqs.svg)](freqs.svg)

This confirmed the initial finding. The CPU speed does not affect the framerate as soon as resolution reaches 512x384.

AMD K5

* * *

The last thing I tested with Vquake was how much the v1000 was able to rehabilitate the K5 and Cyrix 6x86. Unfortunately, due to how the v1000 was used, a lot is still done on the CPU. This really seems to limit the ability of the Rendition Verite to fly on a K5/6x86.

I ran the test in the same conditions, with screen size 101, sound enabled, and from DOS. The K5 ran at 30.6 fps at 320X200, 21.2fps in 512X384, and 15.4fps in 640X480. Not a good combo (as confirmed by usenet thread[5] from 1996).

Next

* * *

Benchmarking [GLQuake](../glquake/).

References

* * *

^|  [1]| [Red Annihilation](https://en.wikipedia.org/wiki/Red_Annihilation)  
---|---|---  
^|  [2]| [Computer Gaming World #149](https://archive.org/details/Computer_Gaming_World_Issue_149/page/n269/mode/2up?q=vquake)  
^|  [3]| [NEXT_Generation #26: Rendition Verite review](https://archive.org/details/NEXT_Generation_26/page/n65/mode/2up?q=vquake\);)  
^|  [4]| [List of vquake cvars](https://www.vogonswiki.com/index.php/VQuake)  
^|  [5]| [AMD K5-133 FP performance](https://groups.google.com/g/rec.games.computer.quake.misc/c/EBB6eJBEjY8#:~:text=RESOLUTION%20VQUAKE%2C%20Beta9,640X480%2020.8%209.9)  
  
* * *

*
