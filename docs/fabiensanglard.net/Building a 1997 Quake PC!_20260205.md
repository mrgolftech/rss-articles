# Building a 1997 Quake PC!

**来源:** https://fabiensanglard.net
**链接:** https://fabiensanglard.net/quake_pc/index.html
**日期:** 08 Jan 2026 00:00:00 +0000

---

  


[**FABIEN SANGLARD'S WEBSITE**  
](/)

* * *

[CONTACT](mailto:fabiensanglard.net@gmail.com)    [RSS](../rss.xml)     [DONATE](https://paypal.me/fabiensanglard)

  
  


Jan 8, 2026

Building a Quake PC

* * *

After I finished restoring the IBM 2168 486 DX2-66MHz ([my childhood dream DOOM PC](../2168/)), there was another box that I wanted to check.

Released in June 1996, _Quake_ received many updates to ride the triple technological shock-wave of the late 90s. Originally a DOS, software rendered, LAN oriented game, _Quake_ transitioned to Windows with `winquake`, gained 3D hardware acceleration with `vquake`/`glquake`, and got a dedicated deathmatch fork with QuakeWorld (`qwcl`/`qwsv`).

This is an era that I completely missed when I was a teenager because I did not have the money to upgrade my PC. On top of that, France only really got access to the Internet many years later, in 1999, when AOL came with its 99 Frcs/monthly unlimited plan.

Here is the story of my "Quake PC", built thirty years later.

Parts

* * *

[Part 1: Sourcing Parts](.)  
[Part 2: Turning it on](post/)  
[Part 3: The essentials programs to run](tools/)  
[Part 4: Running DOOM & Duke Nukem 3D](dad/)  
[Part 5: Benchmarking Quake ](quake/)  
[Part 6: Benchmarking VQuake](vquake/)  
[Part 7: Benchmarking GLQuake](glquake/)  
_Part 8: Benchmarking Quake2 and Voodoo 2 SLI_  
[Part 9: Epilogue](disclaimer/)  


Sourcing hardware parts

* * *

When I restored the [DOOM machine](../2168), I sourced parts in a slightly eccentric way. Having grown up with second hand components, I treated myself with boxes and manuals. That was expensive but so satisfactory that I did the same for this build.

[![](parts.webp)](parts.webp) [![](boxes.webp)](boxes.webp)

The European box for the 3dfx Voodoo2 is smaller. In Europe the card came with three games, while the US one came with four ([photo of both boxes](voodoos.webp)).

[![](all_boxes.webp)](all_boxes.webp)

Picking an era

* * *

Before starting the project, the most important decision was to settle on a time period from which I would choose the parts. I landed in 1997-1998 since the hardware would allow me to comfortably run all versions of _Quake_ released from 1996 to 1997 and even dab into Quake II (Dec '97) territories.

Motherboard

* * *

The choice of the mobo was crucial since every other component would connect to it. First was the question of going AT vs ATX. Given the nightmare of cables that an AT motherboard was going to be, I was dead set on finding an ATX.

On the **CPU** side, I intended to benchmark as many Pentiums as possible, possibly from 60Mhz (1993) to 223Mhz (1997). I also wanted to see with my eyes the infamous Cyrix 6x86 (1995), and AMD K6 (1997) processors perform.

For the **graphic cards** , I wanted to test the VGA king Matrox Mystique (1996) but also the three milestones of the graphic hardware accelerators, Rendition Verite (1996), 3dfx Voodoo (1996), and SLI 3dfx Voodoo2 (1998). I was also curious to measure how AGP (1997) helped the software renderer vs a PCI card.

Finally for the **RAM** , I wanted to be able to test EDO (1995) but also have the option to use SDRAM (1998).

[![](xa100.webp)](xa100.webp)_Iwill XA100 motherboard_

I lucked out with this Iwill XA100 v1.2 on ebay. Built in 1998, it seems to be stable for the technology it supports[1] and fits all my technical requirements. More importantly, the manual is readily available online[2].

CPUs

* * *

It turned out that a motherboard able to run Pentium from 60Mhz to 223Mhz could not exist for the good reason that all these CPUs use different sockets. 

Socket Name | Year | Processor Type | Fronside Bus Frequency | Multiplier | Frequency  
---|---|---|---|---|---  
Socket 4 | 1993 | P5 | 60MHz | 1 | 60MHz  
Socket 4 | 1993 | P5 | 66MHz | 1 | 66MHz  
Socket 5 | 1994 | P54C | 50MHz | 1.5 | 75MHz  
Socket 5 | 1994 | P54C | 60MHz | 1.5 | 90MHz  
Socket 5 | 1994 | P54C | 66MHz | 1.5 | 100MHz  
Socket 5 | 1995 | P54C | 60Hz | 2.0 | 120MHz  
Socket 5 | 1995 | P54C | 66MHz | 2.0 | 133MHz  
Socket 7 | 1996 | P54CS | 60MHz | 2.5 | 150MHz  
Socket 7 | 1996 | P54CS | 66MHz | 2.5 | 166MHz  
Socket 7 | 1996 | P54CS | 66MHz | 3.0 | 200MHz  
Socket 7 | 1997 | P5CC MMX | 66MHz | 2.5 | 166MHz  
Socket 7 | 1997 | P5CC MMX | 66MHz | 3.0 | 200MHz  
Socket 7 | 1997 | P5CC MMX | 66MHz | 3.5 | 233MHz  
  
The XA100 motherboard was a good choice since its Socket 7 supports a wide range of Intel CPUs, and also Cyrix and AMD. I got a Pentium MMX 233Mhz to get the build started.

What happened to Socket 6? It does exist but it was meant to run 486 DX4 and Pentium Overdrive CPUs. There is also a Socket 8 but these were meant for Pentium Pros.

CPU cooling

* * *

![](AAVID_socket_7.webp)

It was hard to find brand new Socket 7 fans for sale. However I found a 50mm AAVID [on Amazon](https://www.amazon.com/dp/B00IELN18U?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_9) that fit the bill. It was super easy to attach (at least compared to modern coolers). But in retrospect I should have gone on ebay right away.

The sound coming out of the AAVID fan was unbearable. We were definitely just happy to have something up and running back then, regardless of the noise it made. I ended up purchasing a [Noctua NF-A4x10 FLX](https://www.amazon.com/dp/B009NQLT0M?) which turned out whisper silent and a testimony to how much the field of PCs has improved since the late 90s.

If you build your own machine, be careful about picking the right voltage. There is an almost identical version, the [Noctua NF-A4x10](https://www.amazon.com/dp/B00NEMGCIA) which runs on 5V instead of 12V. I felt validated to have picked a mobo with good documentation that explicitly stated the voltage of its fan connectors.

RAM

* * *

Since there was going to be next to no difference for game benchmarks yet provide a huge quality of life improvement, I went anachronic and purchased an obscene (for the time) amount of RAM.

I got 3x128MB PC133 168 pin for a total of 384 MiB. A realistic consumer PC at the time would have featured 8 MiB. That is nearly 40x the amount. At $60/MiB that would have cost nearly $18,000 in 1997 ($37,865.28 in 2025).

Graphic card

* * *

The graphic card manufacturer choice was a no-brainer. At that time, the undisputed king of VGA was Matrox. The Canadian company had released its mythical Matrox Millenium in 1995. However, intended for professionals, the $549 price tag kept most gamers away despite its (lone) support for 3D hardware acceleration of Nascar Racing.

The Matrox Mystique from Aug 1996 was much more consumer friendly with a 2MiB version at $149. I treated myself to a [Matrox Mystique 220](https://vintage3d.org/mga1.php) 4MB allowing 1280x1024 in 16-bit colors.

Sound card

* * *

Many motherboards in the late '90s shipped with audio chips providing Sound Blaster emulation. There was a version of the XA100 that had one but mine did not so I had to buy a sound card.

At first, I was going to get another Sound Blaster 16 ASP, the same model I got for the 486 DOOM machine. But these did not fit the time period. I had read many good things about the Sound Blaster Live and I liked the color coded connectors on the back so I got a [CT4830](https://theretroweb.com/expansioncards/s/creative-sound-blaster-live-ct4830). I was concerned about DOS compatibility but discovered a delightful SB16 emulation setting. I ran into zero problems (except when running `duke3d.exe` and driver installation which I will discuss in the next section).

[![](sb_live_dos_emualtion.webp)](sb_live_dos_emualtion.webp)

FDD/HDD

* * *

[![](hdd.webp)](hdd.webp)

I had a FDD remaining from the 486 project so I used that. The HDD was a nightmare. I tried various kinds of IDE-SD/IDE-CF adapters. Most of them did not work. Some worked with DOS but prevented Windows 98 from creating a swap file because the media was marked as "removable".

In the end, I threw money at the problem and got a Maxtor on eBay for the price of its weight in gold. It likely came from an Apple computer but it worked great.

The IDEs HDDs had to be configured into "slave" or "master" via jumpers. This Maxtor frustrated me a great deal because the top simply said "J50" without showing which of the [four jumpers on the back](hdd_no_jumpers.webp) was J50.

As I ranted against the '90s and "how hard it was back then to have access to information", my wife came over the workbench, looked at the HDD, and then calmly informed me the J50 was the pins on the left. Hein, mais comment tu sais ca? Then she flipped the HDD to show me the PCB pins were labeled!

[![](hdd_jumpers_labels.webp)](hdd_jumpers_labels.webp)_Jumper J50? Easy ! It is the one one the left she, nonchalantly, informed me._

CD-ROM

* * *

[![](cd_cannot_play_digital.webp)](cd_cannot_play_digital.webp)

I was so relieved to get into an era where motherboards came with two IDEs connectors. A simple IDE CD-ROM could be picked without having to worry about what connector the sound card supported. I found a gorgeous boxed CREATIVE BLASTER CD 48x and was very happy with it.

The true dilemma was whether to connect the audio CD sound cable or not. I hate cables and I wanted to keep the inside of the machine as neat as possible. With Windows 98, there is an option to _Enable digital CD audio for this CD-ROM device_. Having the data stream go through the PCI bus instead of messing up the inside was tempting.

In theory, according to Vogons forum, this required to install WDM drivers instead of VxD drivers[3] and would enable audio playback without the cable. However I found out that `winamp.exe` was able to do that with VxD drivers.

The problem remaining is that most games, Quake especially, are not compatible with WDM drivers. Running them showed the CD-ROM spin but no music could be heard. In the end, I dropped my aesthetic consideration of inside beauty and connected a cable. But I used a SPDIF Cable digital since the SoundBlaster Live supported it!

[![](cd_rom.webp)](cd_rom.webp)

Network card

* * *

I had a flawless experience using a _10BaseT ISA Network Card Linksys_ in the 486 build so I went back to the same ebay seller and ordered again. To my delight, this time they sent me a shrink wrapped one. In retrospect I should have bought more boxes to have spare parts.

[![](nic.webp)](nic.webp)

Of course these cards came without antenna or wireless drivers so I used the same "trick" as for the 486. I connected the Ethernet port to a Google Mesh Router.

Case

* * *

I had a hard time finding a pretty case. Despite much research I feel like the lines of the IBM 2168 spoiled me and I could not find anything as elegant. It seems it was a trend of the late '90s since even IBM refresh, the [2168 Aptiva](IBM_aptiva_2168.webp), did not appeal to me.

I ended up settling on a minimalist ATX MITAC case. The turquoise button was, let's say, not my favorite, but there was a nice moving sliding panel on the front to cover it all. It also came with a Power Supply Unit so I jumped on it.

[![](mitac1.webp)](mitac1.webp)[![](mitac2.webp)](mitac2.webp)[![](mitac3.webp)](mitac3.webp) [![](case.webp)](case.webp)_Late '90s PC cases. No amount of nostalgia can make me love them but this one was tolerable._ [![](thumb_screws.webp)](thumb_screws.webp)[![](screws_set.webp)](screws_set.webp)

The case came without any screws to mount the motherboard and drives but there are plenty of "screw packs" available on Amazon.

I was also anticipating having to open the case over and over so I replaced the screws fastening the side panels with thumb screws. This way I could open it fast and without a screwdriver.

Cables

* * *

[![](round_cable.webp)](round_cable.webp)

Anybody who actually owned a '90s PC will tell you the inside was a mess of cables, with the main offenders being the HDD and FDD ribbon cables. There is a way nowadays to make the inside pretty by using "round cables". 

But vendors on eBay don't always pay attention. My Iwill XA100 motherboard uses 40-pins cable connectors so I explicitly ordered these. What ended up delivered were unfortunately 39-pin cables. Why oh why did manufacturers block that pin? Perhaps to prevent the ribbon from being connected the wrong way? But there was already a knot for that. The mystery lives on.

After a little bit of googling I learned I could just drill it. And it worked!

[![](39pins.webp)](39pins.webp)_39 pins before._ [![](40pins.webp)](40pins.webp)_40 pins after. I could have been a surgeon._

Keyboard

* * *

[![](intergraph_listing.webp)](intergraph_listing.webp)

Nothing screams QUAKE to me like the RT-9100W keyboard. Now, contrary to popular belief, all of _Quake_ was not written with one of these. There are numerous photos of the id Software war room with no Intergraph in sight. These entered the picture when id bought RealiZm workstations running Windows NT. These keyboards "only" contributed to `winquake.exe`, `glquake.exe`, and quakeworld.

I searched for a RT-9100W for a very long time. The ones I found on eBay were in disastrous condition. I ended up lucking out on FB Marketplace (I never thought I would ever buy something there) where I found one still in the box and wrapped in plastic.

[![](concert_master_keyboard-ad.webp)](concert_master_keyboard-ad.webp)

It is not a mechanical keyboard (the connectors are membrane based) but the sound quality of the speakers was EXCEPTIONAL! I could not believe my ears. Additionally, not having to install speakers saved a lot of space on the desk. I instantly fell in love with this gem.

[![](keyboard.webp)](keyboard.webp)

Even though the manual mentions a power brick, my model came without one. Even powered only by the PS/2 connectors, the sound is unbelievable.

Monitor

* * *

[![](Dell UltraSharp 2007FPb.webp)](Dell UltraSharp 2007FPb.webp)

I had mixed feelings about the Checkmate 1500 I used for the 486 build. The form factor was splendid but there was a post-processing of the VGA signal that made the image blurry and I did not like it.

I tried the Dell UltraSharp 2007FPb 20” LCD and the image was crisp. It is a pretty solid Windows 98/NT monitor with a native resolution of 1600X1200 pixels. I was a bit concerned about rumors that it would not run DOS games in 320x200 at 70Hz well but I never experienced any visual discomfort or "frame skipping". I highly recommend it.

Oddly, I found the black casing was a nice homage to a time period where PCs started to be assembled by teenagers from diverse parts instead of being bought by parents from a major manufacturer. In the end, I liked that it did not match with the beige color of the case.

Turning it on

* * *

I assembled everything. I found it particularly pleasant to play contemporary music in the background while doing so ([Perfect](https://www.youtube.com/watch?v=VKYY8DxVZHE), [All I Need](https://www.youtube.com/watch?v=xpahYJ7UpP4), [Ava Adore](https://www.youtube.com/watch?v=9uWwvQKGjLI), and [Novocaine for the Soul](https://www.youtube.com/watch?v=V2yy141q8HQ)). Once I was done, I had absolutely zero hope it was going to boot, much less POST on the first try since every single component except the CPU fan was 30 years old.

[![](first_draft.webp)](first_draft.webp)

Next

* * *

[First boot!](post)

References

* * *

^|  [1]| [Tomshardware review of the XA100](https://www.tomshardware.com/reviews/socket-7-board-review-july-1998,79-13.html)  
---|---|---  
^|  [2]| [Iwill XA100 documentation](https://theretroweb.com/motherboards/s/iwill-xa100)  
^|  [3]| [Enabling CDROM digital playback - Where to find WDM drivers for a SB16?](https://www.vogons.org/viewtopic.php?t=108543&view=unread#unread)  
  
* * *

*
