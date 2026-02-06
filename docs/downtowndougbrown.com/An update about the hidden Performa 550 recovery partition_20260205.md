# An update about the hidden Performa 550 recovery partition

**来源:** https://downtowndougbrown.com
**链接:** https://www.downtowndougbrown.com/2025/08/an-update-about-the-hidden-performa-550-recovery-partition/
**日期:** Thu, 28 Aug 2025 02:28:38 +0000

---

# [Downtown Doug Brown](https://www.downtowndougbrown.com)

## Thoughts from a combined Apple/Linux/Windows geek.

  * [Home](https://www.downtowndougbrown.com)
  * [About](https://www.downtowndougbrown.com/about/)
  * [Mac ROM SIMMs](https://www.downtowndougbrown.com/programmable-mac-rom-simms/)
  * [Software](https://www.downtowndougbrown.com/software/)
  * [Microcontroller lessons](https://www.downtowndougbrown.com/microcontroller-lessons/)
  * [Contact](https://www.downtowndougbrown.com/contact/)



Aug

27

## [An update about the hidden Performa 550 recovery partition](https://www.downtowndougbrown.com/2025/08/an-update-about-the-hidden-performa-550-recovery-partition/ "Permanent Link to An update about the hidden Performa 550 recovery partition")

Doug Brown [Classic Mac](https://www.downtowndougbrown.com/category/classic-mac/) 2025-08-27

Earlier this year, I wrote about [how I rescued a special recovery partition from an old Macintosh Performa 550's dead hard drive](https://www.downtowndougbrown.com/2025/03/apples-long-lost-hidden-recovery-partition-from-1994-has-been-found/). This partition had been lost to time and it was a race to try to save it before the remaining Performa 550 machines out there with their original hard drives were reformatted or destroyed. It [has now been preserved on the Macintosh Garden](https://macintoshgarden.org/apps/system-71p6-performa-550-hidden-recovery-partition). I have a few updates to that post that I'd like to share.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-9.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-9.png)

The first update is that some extra discussion took place in the comments of my original post. Reader "Greg" pointed out that there was an Apple employee named John Yen who worked on the Mac OS during the System 7 era, and suggested he might be the "jy" in the associated "msjy" creator code. That would leave "ms" potentially being Microseeds, which is the company that developed Apple Backup.

This led me to search further, and I stumbled upon [Apple's patent for the automatic OS recovery functionality](https://patents.google.com/patent/US6381694B1/en) filed in 1994. It was granted in 2002 and expired in 2019. John Yen is listed as the inventor. The patent contains some screenshots of the exact UI that I experienced while testing the functionality. I never thought to look through patents, but I should have. They are definitely a useful tool for historical research on this type of stuff. I thought that was a really cool discovery. Thanks, Greg!

Now, onto the second thing. After my research had seemingly concluded, I never turned off my eBay alerts. Last week, I received a notification about a damaged tray-loading Performa 550 (manufacture date February 1994) being parted out. Sure enough, one of the seller's auctions was a working 160 MB hard drive from the same machine. Of course, I couldn't resist snatching it up.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/harddrive-225x300.jpg)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/harddrive.jpg)

As soon as it arrived, I dumped all the contents. I was in for a very pleasant surprise: this hard drive also had the invisible recovery partition intact!

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-15.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-15.png)

Better yet, unlike the last one, it still had all of the original Performa software, including Apple Backup, sitting in the Applications folder.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-1.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-1.png)

At one point during my initial search, I was really concerned that I might never find the lost recovery partition. Now everything has changed, and I'm pleased to be able to say I found it _twice_!

This second hard drive is a huge discovery because I now have two data points, which has led me to gain a little more confidence about how I think the special recovery partition was created in the first place. You may recall from my previous post that [Apple's own tech notes said that Apple Backup was responsible for creating it](https://ia600306.us.archive.org/view_archive.php?archive=/21/items/APPLE_TIL_ARTICLES/TIL00001_to_TIL60496.zip&file=TIL14970-Performa_550-Description_of_Backup_Partition_3-94_%28TA31408%29.pdf), but I was never able to find any evidence supporting that claim. Unfortunately, the original owner had deleted Apple Backup from the first hard drive before I got my hands on it, so I couldn't draw any conclusions.

This new-to-me hard drive was exciting because Apple Backup had not been deleted! I was half expecting to find a weird unpreserved version of Apple Backup hanging around on it, but nope. It's just the same version 1.2 from System 7.1P6 that I had already looked at in depth, right down to the creation/modification dates and the exact number of bytes used.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image.png)

The hidden partition's contents are exactly the same as what I found on the first hard drive. The file sizes are all precisely the same, and the icons are positioned identically too. That solves one mystery: the weird icon positions inside the invisible partition were not something the original owner caused. They were just weird on all machines.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-3.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-3.png) [![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-4.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-4.png)

The only difference I found is that the creation and modification dates of the files are slightly different between the two drives. The easiest place to show this is in the Get Info window of the partition. On the left is the first hard drive, and on the right is the second hard drive.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-5.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-5.png)

You can see that the exact same number of bytes have been used, but the partition on the second hard drive was created about 21 hours later. Also, it appears that on both machines, it took about 4-5 minutes to finish populating it.

One of the things I called out in my first post on this subject was that the System file strangely had a modification date several months later. It turns out that something similar happened with the second hard drive, but it ended up being a date way back in the past -- the August 27, 1956 date that some Macs default to if the PRAM battery goes bad. Again, hard drive #1 on the left and hard drive #2 on the right:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-6.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-6.png)

I still don't have a great explanation for why the System file's modification date changed on both of these partitions. Maybe a third-party utility or installer happened to tweak the modification date at some point. In my earlier post, I had suggested that the At Ease 'INIT' resource being missing from the System file could have potentially explained the modification date change, but that resource was also missing from the second hard drive's recovery partition System file. Plus, At Ease had not been uninstalled from the second machine. So that blows that theory out of the water. Clearly, the At Ease INIT was never part of the recovery partition's System file.

One other interesting thing I found was that the main Hard Disk volume had the exact same creation date on both drives:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-7.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-7.png)

Obviously, I would love to be given the opportunity to analyze a third hard drive in the future to gain even more confidence. With all that in mind, I think I'm much closer to being able to reach a conclusion today:

I still can't be 100% sure, but I think this latest hard drive analysis hammers the final nail in the coffin to the theory that the partition was created based on an action the user performed. I now believe the recovery partition was added by Apple in the factory, and the technote was just wrong about Apple Backup being involved. I can't find any code in Apple Backup that does it, and this second hard drive gives me a good reason to doubt that a customized Performa-550-specific Apple Backup version is hiding out there in the wild somewhere.

I'm still weirded out by the other initials in the creator code being "MS" given that Microseeds developed Apple Backup, but all signs are pointing to this being a factory-programmed thing. I think that makes the most sense anyway. If you're Apple and you've developed this functionality, why would you only enable it after the user has bought a zillion floppy disks and manually performed a backup? Why not just give it to everyone and allow them all to benefit from it?

The fact that the creation date of the recovery partition was not exactly the same between the two hard drives, but it was still within less than a day, is fascinating to me. This means the recovery partition wasn't simply imaged onto every machine at a block level, or the dates would have been exactly the same on every machine. Maybe one of the operations performed at the factory during testing was to run a script that created the partition? This would explain why the creation date of the recovery volume was slightly different between the machines.

Another data point in favor of this theory comes from a recently-preserved Apple Restoration CD: [Market Software Series Volume 1 from March 1994](https://macintoshgarden.org/apps/apple-restoration-cds-market-software-series-1994). It has a bunch of factory Performa software bundles. I found a quick comment about "action atoms" for a backup partition not being included in the configuration that goes with the ultra-rare [Performa 560 Money Magazine Edition](https://512pixels.net/2024/08/performa-month-the-macintosh-performa-560-money-magazine-edition/):

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-8.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-8.png)

I suspect it's referring to the recovery partition, and it's implying that Apple did have some kind of restore/imaging script that created it, and they specifically chose not to put it into this configuration.

Unfortunately, the Performa 550 recovery image on this same CD doesn't mention anything about the recovery partition, and doesn't create it. It's also directed to be used for several other Performa models, so I don't think Apple intended for this recovery CD to comprehensively restore a machine to the _exact_ state it was in when it left the factory. It was just meant to restore it to something operable that was close enough.

With all that out of the way, there's one last update I want to talk about. In the first post, I mentioned that Apple published [another tech note](https://ia600306.us.archive.org/view_archive.php?archive=/21/items/APPLE_TIL_ARTICLES/TIL00001_to_TIL60496.zip&file=TIL16006-Performa_550-System_Folder_Created_w-Dinosaur_Safari_CD_8-94_%28TA32248%29.pdf) describing a bug where an educational Dinosaur Safari CD game would accidentally cause the machine to jump into recovery mode. I went so far as to buy the game, reproduce the problem, and [post a video demonstrating it](https://www.youtube.com/watch?v=A2qp7W5zarI).

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-13.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-13.png)

Looks like Creative Multimedia Corporation beat Apple to the punch at having a Mac app named Safari by almost a decade!

Several people were interested in learning more about why Dinosaur Safari did this. What would even cause an app launched from a CD to trigger the system to enter recovery mode? It's definitely an odd bug, and worthy of a little more investigation.

I spent a little bit of time in MAME tracing what the game did leading up to the machine deciding to reboot. After looking through some CPU execution logs, I found that it was happening in the middle of InitResources(). When I mentioned this in #mac68k on Libera, [Josh Juran](https://www.jjuran.org/) quickly explained to me that apps aren't supposed to call InitResources() in the first place. Inside Macintosh Volume I confirms this:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-14.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-14.png)

So that's the problem. The app is calling a system function that it's not supposed to, which results in the re-initialization of a bunch of system stuff, and somehow this causes the Mac to reboot into recovery mode. Strangely, the problem only happens if the app runs directly from the CD. It doesn't happen if you copy it to your hard drive and launch it from there. Weird. Here's the relevant part of the code as viewed in ResEdit:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-10.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-10.png)

It's alongside a bunch of other standard toolbox initialization routines that are often called early during a classic Mac app's lifetime. The developers of Dinosaur Safari inadvertently added a call to InitResources(). It's kind of funny how it's sitting there [near the top of Apple's public Resources.h header file](https://github.com/elliotnunn/UniversalInterfaces/blob/master/2.2/Interfaces/CIncludes/Resources.h#L114), even though it's not supposed to be called by programs. It's almost like they were just daring someone to do it.

Anyway, to test this theory, I patched the CD to replace the InitResources trap instruction with a nop instead:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-11.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-11.png)

Using this modified CD, Dinosaur Safari runs perfectly fine and doesn't activate the recovery partition.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-12.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/08/image-12.png)

I decided not to dive deeper and figure out the underlying sequence of events that leads to the reboot. It would be way too much reverse engineering work inside the bowels of the classic Mac OS for very little payoff. This experience might be a good clue about why Apple didn't go forward with this functionality. I'd be shocked if Dinosaur Safari was the only program with this bug. Maybe it was too easy to inadvertently jump to recovery mode and confuse users.

This should be the end of my investigation into the Performa 550 recovery partition functionality, unless I happen to stumble upon a third hard drive in the future that radically changes my understanding of everything.

My blog isn't turning solely into an Apple archaeology project, so if you're not interested in old Mac stuff, never despair. I'll write about lots of other fun stuff too. But as a forewarning, I do have another upcoming post about more obscure Apple software from the '90s that was lost and is now found. This time, it was something that I doubt too many people even remembered existing. It'll be a nice little blast to the past.

Address: <https://www.downtowndougbrown.com/2025/08/an-update-about-the-hidden-performa-550-recovery-partition/>

« [Finding a 27-year-old easter egg in the Power Mac G3 ROM](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/)

[Debugging BeagleBoard USB boot with a sniffer: fixing omap_loader on modern PCs](https://www.downtowndougbrown.com/2025/11/debugging-beagleboard-usb-boot-with-a-sniffer-fixing-omap_loader-on-modern-pcs/) »

[Trackback](https://www.downtowndougbrown.com/2025/08/an-update-about-the-hidden-performa-550-recovery-partition/trackback/ "Trackback URI")

### 2 comments

  1. Stefan Arentz @ 2025-08-29 13:54

![](https://secure.gravatar.com/avatar/3c6715ba3f3ab8dae14a9b13f97bf44a146135a713283e7308b0e29f2d90429b?s=32&d=mm&r=g)

It has been a long time since the time I lived daily in MacsBug but I think I remember that , although not recommended, calling InitResources() was actually safe.

It is very possible the crash happens because some system extension (INIT) was installed that patched InitResources() which was I think a common thing to do to hook into the app startup process. And if that INIT runs twice it crashes.

  2. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-08-29 19:31

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

Hi Stefan,

Josh told me that it executes all of the INIT resources in the system file, which can cause a bunch of stuff to be re-executed. Seems like it could expose some weird issues.

For what it's worth, the problem I demonstrated only occurs if you have a recovery partition. If I take the exact hard drive image I was tinkering with, and make a single change of removing the recovery partition, Dinosaur Safari (unpatched) begins working fine. So somehow I think re-running InitResources() ends up somehow jumping into the recovery partition's failure code or something.




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
