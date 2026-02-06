# Finding a broken trace on my old Mac with the help of its ROM diagnostics

**来源:** https://downtowndougbrown.com
**链接:** https://www.downtowndougbrown.com/2025/12/finding-a-broken-trace-on-my-old-mac-with-the-help-of-its-rom-diagnostics/
**日期:** Tue, 30 Dec 2025 01:52:17 +0000

---

# [Downtown Doug Brown](https://www.downtowndougbrown.com)

## Thoughts from a combined Apple/Linux/Windows geek.

  * [Home](https://www.downtowndougbrown.com)
  * [About](https://www.downtowndougbrown.com/about/)
  * [Mac ROM SIMMs](https://www.downtowndougbrown.com/programmable-mac-rom-simms/)
  * [Software](https://www.downtowndougbrown.com/software/)
  * [Microcontroller lessons](https://www.downtowndougbrown.com/microcontroller-lessons/)
  * [Contact](https://www.downtowndougbrown.com/contact/)



Dec

29

## [Finding a broken trace on my old Mac with the help of its ROM diagnostics](https://www.downtowndougbrown.com/2025/12/finding-a-broken-trace-on-my-old-mac-with-the-help-of-its-rom-diagnostics/ "Permanent Link to Finding a broken trace on my old Mac with the help of its ROM diagnostics")

Doug Brown [Classic Mac](https://www.downtowndougbrown.com/category/classic-mac/), [Computer repair](https://www.downtowndougbrown.com/category/computer-repair/) 2025-12-29

Yesterday, for the first time in about a year, I tried powering on the Macintosh Performa 450 (LC III) from my [past writeup about Apple's backwards capacitor](https://www.downtowndougbrown.com/2024/11/the-capacitor-that-apple-soldered-incorrectly-at-the-factory/).

[![](https://www.downtowndougbrown.com/wp-content/uploads/2024/11/performa450-1024x425.jpg)](https://www.downtowndougbrown.com/wp-content/uploads/2024/11/performa450.jpg)

It didn't work. The screen was black, it played the startup sound, and then immediately followed up with the "Chimes of Death". Nothing else happened from that point on. Here's what it sounded like:

This was a little frustrating because last year I had already replaced all of the capacitors and cleaned where they had leaked, so I didn't expect to encounter any problems with it so soon. The machine had worked fine the last time I'd tried it! But despite all that, something was failing during the power-on tests in Apple's ROM, prompting it to play the chimes of death. I remembered that [people have been working towards documenting the Mac ROM startup tests](https://docs.google.com/spreadsheets/d/1zsc7ET5fyiOYWj1_AzOgafbrCVFED-7jzLH6ruCiAVE/edit?usp=sharing) and [using them to diagnose problems](https://www.youtube.com/watch?v=W1biFIdQZDw), so I decided to give it a shot and see if Apple's Serial Test Manager could identify my Performa's issue. Where was the fault on this complicated board? Sure, I could test a zillion traces by hand, but why bother when the computer already knows what is wrong?

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/lciiitop-1024x831.jpg)](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/lciiitop.jpg)

I hooked up the Mac's RS-422 modem port to my computer's RS-232 serial port using a couple of adapter cables to convert from Mini-DIN-8 to DB-25 and then DB-25 to DE-9. Next I opened up PuTTY, configured the serial port on my PC for 9600 baud, 8 data bits, no parity, and 2 stop bits (8N2), and tried typing the command to put the Serial Test Manager into ASCII mode:
    
    
    *A

It echoed the command back to me, so it was working! Next, I typed the command to return the status:
    
    
    *R

It printed this back to me:
    
    
    2F1E122B0003*R

According to the documentation I linked earlier, this result shows that the status register contained the value 0x2F1E122B and the major error code was 0x0003. Error code 3 means RAM Bank A failure. The 0x2F1E122B seemed like gibberish, but I thought it was supposed to be a bitmask of bad bits. I later figured out that the value in the status register is always junk after the chimes of death play, because the code that plays the sound overwrites it.

The RAM test definitely knew which part of the RAM was failing though. I just needed it to give me all of the details. So I manually ran a test over a small range of RAM addresses:
    
    
    *4  
    *000001000  
    *100002000  
    *T000200010001

What these commands do according to the documentation:

  * *4 clears the result of any previous test
  * *0 sets the value of register A0, containing the start address of the test. I set it to 0x00001000.
  * *1 sets the value of register A1 for the end address of the test. I set it to 0x00002000.
  * *T runs a "critical test". 0x0002 is the test (mod3 RAM test), the first 0x0001 is the number of times the test will run, and the second 0x0001 contains option flags.



Here is the printout I got back from the Mac when I ran these commands:
    
    
    *4  
    *0  
    *1  
    *ERROR**T

This was actually really good news! It accepted the first three commands, and then the RAM test failed. This was consistent with what I expected to see. I tried to display the results again, hopeful that this time the status register would contain useful info about the failed RAM.
    
    
    *R

It happily printed this back:
    
    
    000008000000*R

Yay! This meant the status register was 0x00000800. The status register value showed which bit(s) in the RAM were acting up. In other words, the test was telling me that bit 11 was the problem.

I didn't have a RAM SIMM installed, so the problem was clearly with the 4 MB of onboard memory. It was very doubtful that a RAM chip had just randomly gone bad since the last time I'd powered up this machine. More likely, the leaked capacitor goo had eaten away another trace over time because I hadn't cleaned the board well enough. I grabbed my multimeter and checked the continuity of D11 between the RAM chip and various other components on the board. Luckily, Bomarc reverse-engineered the LC III logic board a while ago and [their schematics are floating around on the internet these days](https://macdat.net/files/pdf/apple/schematics/bomarc/lc_iii.pdf).

The schematics indicate that onboard RAM data bit 11 is supplied by U28, pin 25. It's hooked directly to the CPU's data bus, which goes to the RAM SIMM slot, the CPU itself, an optional FPU, the PDS slot, one of the ROM chips (U19), and other random chips on the board.

Thanks to [max1zzz's LC III Reloaded replica of the LC III logic board](https://github.com/max234252/Macintosh_LCIII-Reloaded), I was easily able to follow the traces and verify where things were hooked up. Sometimes Bomarc's schematics can be a little iffy, so it's always good to double check them.

I confirmed that U28 pin 25 had a connection to the RAM SIMM socket right next to it (pin 55), but it wasn't connected to anything else. The ROM chip U19 was the easiest to test against. I also checked that other nearby data lines did indeed have good continuity between the RAM and ROM, so it was just this one data line that was bad. This all made sense and was consistent with the RAM test results. There was definitely a broken trace somewhere. Following along with max1zzz's replica board Gerber files, I had a pretty good idea of where the damage was: a cluster of tiny vias near where an electrolytic capacitor had badly leaked. Several of these vias look pretty icky. Also, please ignore my terrible alignment on the replacement tantalum cap.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/lciiicap-951x1024.jpg)](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/lciiicap.jpg)

I was in a hurry to get this Performa running again. Instead of trying to repair the bad trace/via, I opted for a quick bodge wire on the bottom of the board between pin 55 of the RAM SIMM socket and pin 21 of the relevant ROM socket (U19). That was easier than trying to repair a tiny via. I might experiment more with via repair in the future, though!

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/lciiibot-1024x815.jpg)](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/lciiibot.jpg)

With the bodge wire in place, my Performa 450 is alive once again! For now, anyway. My board probably still has some issues. That's the tricky thing with capacitor leakage. You might think you've cleaned it well, but electrolyte could still be lurking there somewhere, slowly eating away more and more copper. I know some people have had good luck using ultrasonic cleaners, although I hear that they can damage oscillators.

If you're feeling nostalgic and/or have way too much time on your hands, and you're comfortable with building MAME from source, you can replicate my successful diagnosis in an emulator using MAME on Linux. Here's a quick patch I applied to screw up bit 11 of the RAM on the emulated LC III:
    
    
    diff --git a/src/mame/apple/sonora.cpp b/src/mame/apple/sonora.cpp
    index 141e3e9950d..7d07addc29e 100644
    --- a/src/mame/apple/sonora.cpp
    +++ b/src/mame/apple/sonora.cpp
    @@ -191,6 +191,9 @@ u32 sonora_device::rom_switch_r(offs_t offset)
                    offs_t memory_mirror = memory_end & ~memory_end;
     
                    space.install_ram(0x00000000, memory_end & ~memory_mirror, memory_mirror, memory_data);
    +               space.install_write_tap(0x0000, 0xffff, "faulty_ram", [&](offs_t offset, u32 &data, u32 mem_mask) {
    +                       data &= ~0x0800;
    +               });
                    m_overlay = false;
            }
    
    

Then, you can run MAME with this command:
    
    
    ./mame maclc3 -window -nomaximize -printer pty

This allocates a pseudo terminal that acts as the serial port. You may notice that I included `-printer` instead of `-modem` in the command, even though the physical port I used is definitely the modem port. That's because the current version of MAME as of this writing seems to have them swapped! Sometime in the future when that is fixed, you'll likely need to correctly type `-modem` instead.

With my patch applied, running MAME like this should give you the startup sound followed immediately by the error sound. Figure out which pseudo-terminal is linked to the port (it was `/dev/pts/1` on my machine) and open it with your favorite serial program, such as [minicom](https://salsa.debian.org/minicom-team/minicom). You can now type all the commands I used to diagnose the problem.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/image.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/12/image.png)

Anyway, this was a successful use of Apple's ROM diagnostics to quickly solve my issue. It was much easier than manually checking continuity of a zillion PCB traces! Back in the day, Apple had a service tool called the [TechStep](https://appletothecore.me/files/1991_techstep.php) that was capable of performing some of these diagnostics. [There's even a modern clone of it](https://68kmla.org/bb/threads/recreateing-the-apple-techstep.41293/), which happens to also be created by max1zzz. However, I'm not sure exactly how useful this device would have been for service techs other than as a pass/fail indicator. Wasn't Apple's policy just to replace full boards, similar to how it is today? Maybe they repaired faulty returned boards and reused them as service part stock. I'm not sure!

By the way, this wasn't my first successful use of the Serial Test Manager. Earlier this year, I also fixed a Performa 410 (LC II) that was experiencing the Chimes of Death. The failure code was 0x30, indicating an Egret error. Egret is the name of the logic board's microcontroller that handles the Apple Desktop Bus, battery-backed PRAM, and some power on stuff. After the ROM diagnostics pointed me in that direction, I did a much better job of cleaning the cap leakage around it, and the problem completely went away. So that's now two times that this cool functionality has helped me.

I'll talk more about my somewhat special Performa 410 in a future post!

Address: <https://www.downtowndougbrown.com/2025/12/finding-a-broken-trace-on-my-old-mac-with-the-help-of-its-rom-diagnostics/>

« [Debugging BeagleBoard USB boot with a sniffer: fixing omap_loader on modern PCs](https://www.downtowndougbrown.com/2025/11/debugging-beagleboard-usb-boot-with-a-sniffer-fixing-omap_loader-on-modern-pcs/)

[Trackback](https://www.downtowndougbrown.com/2025/12/finding-a-broken-trace-on-my-old-mac-with-the-help-of-its-rom-diagnostics/trackback/ "Trackback URI")

### no comments

### Add your comment now

Name (required)

Email (Will NOT be published) (required)

URL

Δ

  * ## Subscribe

    * [![Bluesky](https://www.downtowndougbrown.com/wp-content/plugins/subscribe-connect-follow-widget/images/32px/bsky.png)](https://bsky.app/profile/downtowndougbrown.com "Follow downtowndougbrown.com on Bluesky")
    * [![Twitter](https://www.downtowndougbrown.com/wp-content/plugins/subscribe-connect-follow-widget/images/32px/twitter.png)](https://twitter.com/dt_db "Follow dt_db on Twitter")
    * [![YouTube](https://www.downtowndougbrown.com/wp-content/plugins/subscribe-connect-follow-widget/images/32px/youtube.png)](https://www.youtube.com/user/doogulass "doogulass - YouTube")
    * [![GitHub](https://www.downtowndougbrown.com/wp-content/plugins/subscribe-connect-follow-widget/images/32px/github.png)](https://github.com/dougg3 "dougg3 on GitHub")
    * [![LinkedIn](https://www.downtowndougbrown.com/wp-content/plugins/subscribe-connect-follow-widget/images/32px/linkedin.png)](https://www.linkedin.com/in/doug-brown-60100519 "LinkedIn")
  * ## Recent Posts

    * [Finding a broken trace on my old Mac with the help of its ROM diagnostics](https://www.downtowndougbrown.com/2025/12/finding-a-broken-trace-on-my-old-mac-with-the-help-of-its-rom-diagnostics/)
    * [Debugging BeagleBoard USB boot with a sniffer: fixing omap_loader on modern PCs](https://www.downtowndougbrown.com/2025/11/debugging-beagleboard-usb-boot-with-a-sniffer-fixing-omap_loader-on-modern-pcs/)
    * [An update about the hidden Performa 550 recovery partition](https://www.downtowndougbrown.com/2025/08/an-update-about-the-hidden-performa-550-recovery-partition/)
    * [Finding a 27-year-old easter egg in the Power Mac G3 ROM](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/)
    * [Modifying an HDMI dummy plug's EDID using a Raspberry Pi](https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/)
    * [Please don't ship heavy, fragile vintage computers. They will be destroyed.](https://www.downtowndougbrown.com/2025/05/please-dont-ship-heavy-fragile-vintage-computers-they-will-be-destroyed/)
    * [How I fixed the infamous Basilisk II Windows "Black Screen" bug in 2013](https://www.downtowndougbrown.com/2025/05/how-i-fixed-the-infamous-basilisk-ii-windows-black-screen-bug-in-2013/)
    * [Apple's long-lost hidden recovery partition from 1994 has been found](https://www.downtowndougbrown.com/2025/03/apples-long-lost-hidden-recovery-partition-from-1994-has-been-found/)
  * ## Categories

    * [Bug fixes](https://www.downtowndougbrown.com/category/bug-fixes/) (7) 
    * [Chumby 8 kernel](https://www.downtowndougbrown.com/category/chumby-8-kernel/) (13) 
    * [Classic Mac](https://www.downtowndougbrown.com/category/classic-mac/) (16) 
    * [Computer repair](https://www.downtowndougbrown.com/category/computer-repair/) (11) 
    * [Electronics repair](https://www.downtowndougbrown.com/category/electronics-repair/) (8) 
    * [iOS](https://www.downtowndougbrown.com/category/ios/) (3) 
    * [Linux](https://www.downtowndougbrown.com/category/linux/) (45) 
    * [Mac ROM hacking](https://www.downtowndougbrown.com/category/mac-rom-hacking/) (11) 
    * [Microcontroller lessons](https://www.downtowndougbrown.com/category/microcontroller-programming/) (11) 
    * [Microcontrollers](https://www.downtowndougbrown.com/category/microcontrollers/) (4) 
    * [Product reviews](https://www.downtowndougbrown.com/category/product-reviews/) (5) 
    * [Python](https://www.downtowndougbrown.com/category/python/) (1) 
    * [Qt](https://www.downtowndougbrown.com/category/qt/) (5) 
    * [Reverse engineering](https://www.downtowndougbrown.com/category/reverse-engineering/) (4) 
    * [Uncategorized](https://www.downtowndougbrown.com/category/uncategorized/) (20) 
    * [Windows](https://www.downtowndougbrown.com/category/windows/) (8) 
  * ## Archives

    * [December 2025](https://www.downtowndougbrown.com/2025/12/) (1)
    * [November 2025](https://www.downtowndougbrown.com/2025/11/) (1)
    * [August 2025](https://www.downtowndougbrown.com/2025/08/) (1)
    * [June 2025](https://www.downtowndougbrown.com/2025/06/) (2)
    * [May 2025](https://www.downtowndougbrown.com/2025/05/) (2)
    * [March 2025](https://www.downtowndougbrown.com/2025/03/) (2)
    * [January 2025](https://www.downtowndougbrown.com/2025/01/) (2)
    * [December 2024](https://www.downtowndougbrown.com/2024/12/) (1)
    * [November 2024](https://www.downtowndougbrown.com/2024/11/) (1)
    * [October 2024](https://www.downtowndougbrown.com/2024/10/) (2)
    * [September 2024](https://www.downtowndougbrown.com/2024/09/) (1)
    * [August 2024](https://www.downtowndougbrown.com/2024/08/) (1)
    * [July 2024](https://www.downtowndougbrown.com/2024/07/) (3)
    * [June 2024](https://www.downtowndougbrown.com/2024/06/) (4)
    * [May 2024](https://www.downtowndougbrown.com/2024/05/) (1)
    * [April 2024](https://www.downtowndougbrown.com/2024/04/) (2)
    * [December 2023](https://www.downtowndougbrown.com/2023/12/) (1)
    * [November 2023](https://www.downtowndougbrown.com/2023/11/) (2)
    * [September 2023](https://www.downtowndougbrown.com/2023/09/) (3)
    * [August 2023](https://www.downtowndougbrown.com/2023/08/) (3)
    * [June 2023](https://www.downtowndougbrown.com/2023/06/) (1)
    * [May 2023](https://www.downtowndougbrown.com/2023/05/) (1)
    * [April 2023](https://www.downtowndougbrown.com/2023/04/) (1)
    * [March 2023](https://www.downtowndougbrown.com/2023/03/) (2)
    * [January 2023](https://www.downtowndougbrown.com/2023/01/) (1)
    * [December 2022](https://www.downtowndougbrown.com/2022/12/) (3)
    * [August 2022](https://www.downtowndougbrown.com/2022/08/) (1)
    * [May 2022](https://www.downtowndougbrown.com/2022/05/) (2)
    * [March 2022](https://www.downtowndougbrown.com/2022/03/) (1)
    * [December 2021](https://www.downtowndougbrown.com/2021/12/) (1)
    * [June 2021](https://www.downtowndougbrown.com/2021/06/) (1)
    * [April 2021](https://www.downtowndougbrown.com/2021/04/) (1)
    * [January 2021](https://www.downtowndougbrown.com/2021/01/) (1)
    * [September 2020](https://www.downtowndougbrown.com/2020/09/) (1)
    * [August 2020](https://www.downtowndougbrown.com/2020/08/) (1)
    * [July 2020](https://www.downtowndougbrown.com/2020/07/) (1)
    * [May 2020](https://www.downtowndougbrown.com/2020/05/) (1)
    * [June 2019](https://www.downtowndougbrown.com/2019/06/) (1)
    * [April 2019](https://www.downtowndougbrown.com/2019/04/) (1)
    * [December 2018](https://www.downtowndougbrown.com/2018/12/) (1)
    * [August 2018](https://www.downtowndougbrown.com/2018/08/) (1)
    * [May 2018](https://www.downtowndougbrown.com/2018/05/) (1)
    * [April 2018](https://www.downtowndougbrown.com/2018/04/) (3)
    * [February 2018](https://www.downtowndougbrown.com/2018/02/) (1)
    * [October 2017](https://www.downtowndougbrown.com/2017/10/) (1)
    * [July 2017](https://www.downtowndougbrown.com/2017/07/) (1)
    * [May 2017](https://www.downtowndougbrown.com/2017/05/) (3)
    * [March 2017](https://www.downtowndougbrown.com/2017/03/) (1)
    * [October 2016](https://www.downtowndougbrown.com/2016/10/) (1)
    * [June 2015](https://www.downtowndougbrown.com/2015/06/) (1)
    * [March 2015](https://www.downtowndougbrown.com/2015/03/) (1)
    * [November 2014](https://www.downtowndougbrown.com/2014/11/) (1)
    * [August 2014](https://www.downtowndougbrown.com/2014/08/) (3)
    * [July 2014](https://www.downtowndougbrown.com/2014/07/) (1)
    * [April 2014](https://www.downtowndougbrown.com/2014/04/) (1)
    * [March 2014](https://www.downtowndougbrown.com/2014/03/) (1)
    * [February 2014](https://www.downtowndougbrown.com/2014/02/) (1)
    * [November 2013](https://www.downtowndougbrown.com/2013/11/) (1)
    * [August 2013](https://www.downtowndougbrown.com/2013/08/) (1)
    * [June 2013](https://www.downtowndougbrown.com/2013/06/) (3)
    * [April 2013](https://www.downtowndougbrown.com/2013/04/) (1)
    * [March 2013](https://www.downtowndougbrown.com/2013/03/) (1)
    * [January 2013](https://www.downtowndougbrown.com/2013/01/) (2)
    * [December 2012](https://www.downtowndougbrown.com/2012/12/) (2)
    * [August 2012](https://www.downtowndougbrown.com/2012/08/) (1)
    * [July 2012](https://www.downtowndougbrown.com/2012/07/) (2)
    * [June 2012](https://www.downtowndougbrown.com/2012/06/) (1)
    * [May 2012](https://www.downtowndougbrown.com/2012/05/) (1)
    * [February 2012](https://www.downtowndougbrown.com/2012/02/) (3)
    * [January 2012](https://www.downtowndougbrown.com/2012/01/) (1)
    * [November 2011](https://www.downtowndougbrown.com/2011/11/) (1)
    * [October 2011](https://www.downtowndougbrown.com/2011/10/) (2)
    * [August 2011](https://www.downtowndougbrown.com/2011/08/) (3)
    * [May 2011](https://www.downtowndougbrown.com/2011/05/) (1)
    * [April 2011](https://www.downtowndougbrown.com/2011/04/) (1)
    * [March 2011](https://www.downtowndougbrown.com/2011/03/) (2)
    * [November 2010](https://www.downtowndougbrown.com/2010/11/) (2)
    * [October 2010](https://www.downtowndougbrown.com/2010/10/) (3)
    * [July 2010](https://www.downtowndougbrown.com/2010/07/) (5)
  * ## Recent Comments

    * Eli on [Fixing a knockoff Altera USB Blaster that never worked](https://www.downtowndougbrown.com/2024/06/fixing-a-knockoff-altera-usb-blaster-that-never-worked/#comment-573432)
    * h4rm0n1c on [The capacitor that Apple soldered incorrectly at the factory](https://www.downtowndougbrown.com/2024/11/the-capacitor-that-apple-soldered-incorrectly-at-the-factory/#comment-573343)
    * James on [Connecting an RCA Viking Pro 10.1″ tablet to your computer through USB](https://www.downtowndougbrown.com/2018/08/connecting-an-rca-viking-pro-10-1-tablet-to-your-computer-through-usb/#comment-572876)
    * [Doug Brown](http://www.downtowndougbrown.com/) on [Parallel Port Tester](https://www.downtowndougbrown.com/2013/06/parallel-port-tester/#comment-572493)
    * Mark Hooper on [Parallel Port Tester](https://www.downtowndougbrown.com/2013/06/parallel-port-tester/#comment-572489)
    * [Arbee's WIP Emporium » Dropping the ball on 2025, my MAME year-in-review](https://rbelmont.mameworld.info/?p=1697) on [The invalid 68030 instruction that accidentally allowed the Mac Classic II to successfully boot up](https://www.downtowndougbrown.com/2025/01/the-invalid-68030-instruction-that-accidentally-allowed-the-mac-classic-ii-to-successfully-boot-up/#comment-571920)
    * [warpdesign](https://warpdesign.fr) on [The invalid 68030 instruction that accidentally allowed the Mac Classic II to successfully boot up](https://www.downtowndougbrown.com/2025/01/the-invalid-68030-instruction-that-accidentally-allowed-the-mac-classic-ii-to-successfully-boot-up/#comment-571793)
    * Erik on [Fixing a knockoff Altera USB Blaster that never worked](https://www.downtowndougbrown.com/2024/06/fixing-a-knockoff-altera-usb-blaster-that-never-worked/#comment-571075)
    * Hieu on [Fixing a knockoff Altera USB Blaster that never worked](https://www.downtowndougbrown.com/2024/06/fixing-a-knockoff-altera-usb-blaster-that-never-worked/#comment-570437)
    * Roger Wolff on [Fixing a knockoff Altera USB Blaster that never worked](https://www.downtowndougbrown.com/2024/06/fixing-a-knockoff-altera-usb-blaster-that-never-worked/#comment-570140)
  * ## Spam Blocked

[ **316,338 spam** blocked by **Akismet** ](https://akismet.com?utm_source=akismet_plugin&utm_campaign=plugin_static_link&utm_medium=in_plugin&utm_content=widget_stats)




[Downtown Doug Brown](https://www.downtowndougbrown.com "Downtown Doug Brown") * [coogee theme](http://imotta.cn/ "Coogee Theme") * 2008 * [Privacy Policy](/privacy-policy/)

[RSS Feed](https://www.downtowndougbrown.com/feed/ "Subscribe Downtown Doug Brown") * [WordPress](http://wordpress.org/ "Powered by WordPress 6.9.1") * TOP
