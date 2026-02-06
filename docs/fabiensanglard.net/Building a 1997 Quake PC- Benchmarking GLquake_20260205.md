# Building a 1997 Quake PC: Benchmarking GLquake

**来源:** https://fabiensanglard.net
**链接:** https://fabiensanglard.net/quake_pc/glquake/index.html
**日期:** 14 Jan 2026 00:00:00 +0000

---

  


[**FABIEN SANGLARD'S WEBSITE**  
](/)

* * *

[CONTACT](mailto:fabiensanglard.net@gmail.com)    [RSS](../rss.xml)     [DONATE](https://paypal.me/fabiensanglard)

  
  


Jan 14, 2026  
  
This article is part of the [Quake PC series](../).

Building a Quake PC: GLQuake

* * *

To play GLQuake, I wanted to get the card labeled by John Caramak as "The benchmark against which everything else is measured."[1]. I found a "tested" Orchid Righteous 3Dfx Voodoo on eBay for what might as well be its weight in diamonds.

[![](3dfx_righteous.webp)](3dfx_righteous.webp)

These are the earliest consumer grade 3D accelerators. Many things give them an "artisanal" feel. For example, they completely take over the VGA output via a passthrough cable, there is no windowed mode support. The Orchid Righteous have mechanical relays (later revisions of the card removed them) which makes a very loud "click" sound when the 3Dfx card takes over or releases the signal!

I suspect these mechanical parts are components begging to fail. I seriously expected this card to die any day I used it.

All flavors of Quake use a different image format for their screenshot. While quake.exe uses PCX, vquake.exe generates BMP, and glquale.exe uses TGA!

First impression

* * *

I installed the latest 3DFX Voodoo Orchid Righteous drivers [v3.00.00](https://www.philscomputerlab.com/drivers-for-voodoo.html) (satisfying it is to make sense of the drivers files now that I understand VxDs). As I launched `glquake.exe`, the game did not start right away. First it generated a palette translation file (`15to8.pal`).

[![](palette.png)](palette.png)

Then it "meshed" all the alias models. It is a step that converts all mdl files to a structure made of `GL_TRIANGLE_FAN`/`GL_TRIANGLE_STRIP` and cache them into [ms2](https://www.celephais.net/board/view_thread.php?id=61319) files.

[![](meshing.png)](meshing.png)

My first impression of GLQuake was terrible. The feeling came from a combination of small annoyances and bigger problems. In the small things, I thought the menu was kind of blurry compared to VQuake.

[![](menu.png)](menu.png)

glquake      vquake

There is also no way to change the resolution at runtime. It was quite annoying to see a screen telling you to do it via command-line given that all other versions of Quake (quake.exe, winquake.exe, and vquake.exe) are capable of it.

[![](vmodes.png)](vmodes.png)

If a user messes up the parameters into an incompatible configuration, they are welcomed with a crude error message which lacks polish. Moreover, most of the modes listed are not supported, which means it is trial and error to discover what works and what doesn't.

[![](crude_glquake_error.png)](crude_glquake_error.png)

In the end, it turned out that only 640x480 and 512x384 worked in my configuration. Sadly no 400x300 which I thought was the sweet spot when enjoying vquake.exe.

It gets worse!

* * *

The impression got worse when I started a new game. While the explosions looked really good, the colors looked washed out.

[![](explosion6.png)](explosion6.png)

Doing some research, it turned out I was not the only one being thrown off. Only people used more colorful terms back in the days.

> Glquake looks like shit. I know a few of you may argue here, but really, lets face it - it looks terrible, especially on NVidia cards.  
>    
> 
> 
> \- @Frib, Unofficial Glquake & QW Guide[2]

There is a cool list of the difference between quake.exe and glquake.exe on [quakeaddicted](https://www.quaddicted.com/engines/software_vs_glquake)(texture filtering, over-bright, fullbrights, Non-square pixels, and Affine texture mapping on alias models).

There is also a partial explanation of why the colors are different.

> The original quake (software) engine used overbright lighting, which means the lightmap brightness can go up to 200%. So, light.exe creates BSP files with lightmaps that go up to 200%.  
>    
>  In glquake […] there is no overbright lighting, so every part of the lightmap that goes above 100% is flattened to equal 100%. This is why glquake looks just fine in darker rooms, but in bright areas the lighting looks very flat.  
>    
> 
> 
> \- quakeaddicted[3]

Second impression

* * *

The thing I had to understand is that GLQuake does not work like VQuake. VQuake was tailored made for one chip, the v1000. It is designed to work "out of the box" with next to no parameters to tweak. GLQuake on the other hand had to cater for anything via OpenGL standard. It is up to the user to tune it down for their particular card. GLQuake is a la carte.

And GLQuake has many items on the menu. Some are 3DFX specific environment variables while some are in-game engine cvars. John Bye (aka Gestalt666) put together a fantastic site[4][5] to summarize them all and even provided a [glquake.bat](glquake.bat) and a [glquake.cfg](glquake.cfg) (to be placed in the id1 folder).

The environment variables range from quality of life like `FX_GLIDE_NO_SPLASH` to skip the 3dfx splash screen to deep change such as overlocking from 50MHz to 56MHz (`SST_GRXCLK=56`). The biggest improvement for me is that it fixed the colors `SST_GAMMA=1.2`.
    
    
    SET SST_SCREENREFRESH=72
    SET SST_SWAP_EN_WAIT_ON_VSYNC=0
    SET SST_VIDEO_24BPP=1
    SET SST_GAMMA=1.2
    SET FX_GLIDE_NO_SPLASH=1
    SET FX_GLIDE_SWAPINTERVAL=0
    SET SST_FASTMEM=1
    SET SST_FASTPCIRD=1
    SET SST_GRXCLK=56
    

I am not sure I would recommend overclocking to 56MHz. The card ran hot HOT *HOT*!

[![](explosion3_gamma.png)](explosion3_gamma.png)

Stock      Gamma 1.2

The colors can also be fixed with a program like IdGamma[6] to overload the palette.

While the environment variable controls the 3dfx chip, the Quake cvar configures the engine. One of my favorite options was to disable bilinear filtering and get to see these cute pixels.

[![](GL_LINEAR.png)](GL_LINEAR.png)

GL_LINEAR      GL_NEAREST

Bilinear texture filtering costs nothing on a 3dfx thanks to the four-way interleaved VRAM storing the textures. GL_LINEAR/GL_NEAREST does not affect the framerate contrary to v1000 cards.

There are many cvar that provide a trade-off between performance and visual improvement. A quite impressive one for 1997 is that Quake is able to [draw real projected](https://github.com/id-Software/Quake/blob/bf4ac424ce754894ac8f1dae6a3981954bc9852d/WinQuake/gl_rmain.c#L579) shadows. It looks however that it was an experimental feature (disabled by default) since I saw quite a bit of peter-panning.

[![](shadow.png)](shadow.png)

Another cool trade-off is flash configuration. GLQuake can either regenerate surfaces to be lit according to dynamic light source (slow and involves the CPU). Alternatively, it can throw the 3fdx and its fillrate at it by [blending](https://github.com/id-Software/Quake/blob/bf4ac424ce754894ac8f1dae6a3981954bc9852d/WinQuake/gl_rmain.c#L718) a blast sphere. The latter is enabled by default and looks quite good.

[![](gl_flashblend.png)](gl_flashblend.png)

gl_flashblend 0      gl_flashblend 1

It seems there was support for alpha transparency of water but I found it quite buggy. Also Quake maps had to be re-processed to have the PVS include surfaces that would otherwise be opaque in the software renderer.

[![](water.png)](water.png)_This was supposed to be water._

GLQuake had to find a way to replicate "palette shift" where the whole screen briefly fades to yellow when picking up an item or red when taking damage. That is something that consumes a lot of fillrate in glquake because it is done by blending a quad over the whole screen. This was identified as a performance hit and could be disabled.

[![](particles.png)](particles.png)

In this ocean of features and parameters, I settled for little visual embellishment close to the software renderer in favor of high framerate.
    
    
    r_drawviewmodel 1        // Enable/Disable drawing the weapon held by the player.
    r_mirroralpha 0          // Turn some surfaces into mirrors. See readme.glquake.
    [r_shadows](https://quakewiki.org/wiki/r_shadows) 0              // Make alias models cast a shadow. Pretty cool.
    r_wateralpha 1           // Buggy. Alpha blend water but poor map support. 1 mandatory.
    gl_texturemode GL_LINEAR // Blurry or pixelated textures.
    [gl_flashblend](https://quakewiki.org/wiki/Gl_flashblend) 1          // Blend to simulate explosions instead of regenerating surfaces.
    [gl_polyblend](https://quakewiki.org/wiki/gl_polyblend) 1           // Simulate palette shift with a GL_QUAD over the screen.
    [gl_ztrick](https://quakewiki.org/wiki/Gl_ztrick) 1              // Trick to avoid clearing the depth buffer
    [gl_keeptjunctions](https://quakewiki.org/wiki/Gl_keeptjunctions) 0      // Remove collinear vertices when it reloads the level.
    gl_subdivide_size 256    // Sets the division value for the sky brushes.
    

GLQuake rules

* * *

With all the tuning done, I changed my mind about GLQuake. It was insanely cool and the framerate was a dream at 640x480. I loved it. It was time to run some benchmarks.

Benchmarking

* * *

The Orchid Righteous 3dfx only really supports 640x480. The resolution 512x384 did work but displayed weird and unpleasant vertical "bands".

| MMX 233 MHz | MMX 200 MHz | MMX 166 MHz | MMX 133 MHz  
---|---|---|---|---  
quake.exe | 27.8 | 27.0  | 27.2 | 26.9  
gl_quake.bat | 33.8 | 33.4 | 33.6 | 29.4 Pretty impressive how little impact the CPU frequency has on the framerate when rendering via the 3dfx. It would mean the framerate is dominated by rasterization and pushing the pixels to the video card which in the case of glquake is not done by the CPU. But since all the projection and clipping is done on the CPU in the glide driver, this could mean that Gary's team may have had aces in their sleeve that id did not. After all, they knew about the InvSqrt that surfaced in Quake III (1999) since 1995[7]. I think it is fairly safe to say the InvSqrt[8] trick helped to run the 3dfx 1. To take things to an extreme level, one could download [GLQPlus](http://ftp.oldskool.org/pub/drivers/3dfx/voodoo1/game_patches/) which reportedly push cards to deliver 5 - 10+ fps[9]. I did not want to push grandpa too hard so I did not try it. K5

* * *

Like for the v1000, I wanted to see how much a 3dfx 1 could enable a K5/6x86 to play Quake. I ran a basic test with an AMD K5 PR166. The machine did reach a playable framerate with 26.3fps at 640x480[10]. Going Voodoo2

* * *

It does not make much sense to use a 3Dfx Voodoo2 in a Pentium 1 build. But this is a card I ava adore, and we must never be apart. The Voodoo2 embodies excellence[11]. I even find the PCB beautiful. Back in the day this card dominated consumer 3D and nothing came close to challenge its performance. I never owned one until now. So I decided to use it anyway despite the anachronism (the Voodoo2 was released in Feb 1998, after Quake II came out). Most of the environment variables changed (see them all on [mdgx.com](https://www.mdgx.com/3dfx.htm)) so I crafted two launch scripts, [3dfx2_640_480.bat](3dfx2_640_480.bat) and [3dfx2_800_600.bat](3dfx2_800_600.bat). The [glquake.cfg](glquake.cfg) script remained the same. [![](voodoo2.webp)](voodoo2.webp) The Creative Voodoo2 does not have a mechanical relay. Switching to 3D rendering is reassuringly silent. Benchmark running at 640x480. |  | MMX 233 MHz | MMX 200 MHz | MMX 166 MHz | MMX 133 MHz  
---|---|---|---|---  
quake.exe |  58.5 |  57.2 |  55.1 |  51.9  
gl_quake.bat | 78.3 | 72.9 | 64.8 | 57.8 Benchmark running at 800x600. |  | MMX 233 MHz | MMX 200 MHz | MMX 166 MHz | MMX 133 MHz  
---|---|---|---|---  
quake.exe | 46.9 | 46.5 | 45.9 | 44.8  
gl_quake.bat | 46.8 | 60.1 | 57.7 | 54.2 The numbers speak for themselves. More benchmarks are available on [Voodoo2 Support Guide and FAQ](https://groups.google.com/g/3dfx.products.voodoo2/c/5BFm3u-je6U). Next

* * *

[Epilogue](../disclaimer/).References

* * *

| ^|  [ 1]| [Johm Carmack .plan, FEB 12, 1998](https://fabiensanglard.net/fd_proxy/doom3/pdfs/johnc-plan_1998.pdf)  
---|---|---  
^|  [ 2]| [Unofficial Glquake & QW Guide](https://web.archive.org/web/20190805025615/https://www.quakewiki.net/archives/frib/glquake.htm#:~:text=Glquake%20looks%20like%20shit.)  
^|  [ 3]| [Differences between software rendered Quake and GLQuake](https://www.quaddicted.com/engines/software_vs_glquake)  
^|  [ 4]| [GLQuake FAQs](https://www.oocities.org/gestalt666/faquake4.html#2)  
^|  [ 5]| [GLQuake Troubleshooting FAQs](https://www.oocities.org/gestalt666/faquake5.html)  
^|  [ 6]| [idGamma and tools webpage](https://www.quaketerminus.com/exe.shtml)  
^|  [ 7]| [Origin of Quake3's Fast InvSqrt()](https://web.archive.org/web/20070104021541/https://www.beyond3d.com/articles/fastinvsqrt/)  
^|  [ 8]| [Fast inverse square root](https://en.wikipedia.org/wiki/Fast_inverse_square_root)  
^|  [ 9]| [Comparison of Frame-rates in GLQuake Using Voodoo & Voodoo 2 3D Cards](https://www.soldcentralfl.com/quakecoop/compare1.htm)  
^|  [10]| [Project: High-End Win95 Computer without MMX!](https://dosreloaded.de/forum/thread/2123-projekt-highend-win95-rechner-ohne-mmx/ )  
^|  [11]| [The story of the 3dfx Voodoo1](../../3dfx_sst1)  
  
* * *

*
