# Finding a 27-year-old easter egg in the Power Mac G3 ROM

**来源:** https://downtowndougbrown.com
**链接:** https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/
**日期:** Tue, 24 Jun 2025 07:49:28 +0000

---

# [Downtown Doug Brown](https://www.downtowndougbrown.com)

## Thoughts from a combined Apple/Linux/Windows geek.

  * [Home](https://www.downtowndougbrown.com)
  * [About](https://www.downtowndougbrown.com/about/)
  * [Mac ROM SIMMs](https://www.downtowndougbrown.com/programmable-mac-rom-simms/)
  * [Software](https://www.downtowndougbrown.com/software/)
  * [Microcontroller lessons](https://www.downtowndougbrown.com/microcontroller-lessons/)
  * [Contact](https://www.downtowndougbrown.com/contact/)



Jun

24

## [Finding a 27-year-old easter egg in the Power Mac G3 ROM](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/ "Permanent Link to Finding a 27-year-old easter egg in the Power Mac G3 ROM")

Doug Brown [Classic Mac](https://www.downtowndougbrown.com/category/classic-mac/), [Reverse engineering](https://www.downtowndougbrown.com/category/reverse-engineering/) 2025-06-24

I was recently poking around inside the original Power Macintosh G3's ROM and accidentally discovered an easter egg that nobody has documented until now.

This story starts with me on a lazy Sunday using [Hex Fiend](https://hexfiend.com/) in conjunction with [Eric Harmon's Mac ROM template (ROM Fiend)](https://github.com/eharmon/rom_fiend) to look through the resources stored in the Power Mac G3's ROM. This ROM was used in the beige desktop, minitower, and all-in-one G3 models from 1997 through 1999.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-12.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-12.png)

As I write this post in mid-2025, I'm having a really difficult time accepting the fact that the Power Mac G3 is now over 27 years old. Wow!

While I was browsing through the ROM, two things caught my eye:

First, there was a resource of type `HPOE` which contained a JPEG image of a bunch of people, presumably people who worked on these Mac models.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/G3Picture.jpg)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/G3Picture.jpg)

This wasn't anything new; [Pierre Dandumont wrote about it back in 2014](https://www.journaldulapin.com/2014/08/19/easter-egg-les-images-cachees-dans-les-roms/). However, in his post, he mentioned that he hadn't figured out how to display this particular hidden image on the actual machine. Several older Macs have secret keypress combinations to show similar pictures, but the mechanism for displaying this one was a complete mystery.

The second thing I found was a big clue: I kept looking for other interesting information in the ROM, and eventually I stumbled upon `nitt` resource ID 43, named "Native 4.3". Thanks to [Keith Kaisershot's earlier Pippin research](https://blitter.net/blog/2021/02/09/pippin-kickstart-1-1/), I was quickly able to conclude that this was the PowerPC-native SCSI Manager 4.3 code. The SCSI Manager wasn't what piqued my interest about this resource though. At the very end of the data, I found some interesting Pascal strings:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-1.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-1.png)

These strings were definitely intriguing:

  * .Edisk
  * secret ROM image
  * The Team



The "secret ROM image" text in particular seemed like it could be related to the picture shown above. I decided to dive deeper to see if I could figure out why the SCSI Manager contained these strings, in the hopes that I could solve the mystery. Would this be the clue I needed in order to figure out how to instruct the Power Mac G3 to display this picture?

Some quick Internet searching for the phrase "secret ROM image" revealed that [it had been used for easter eggs with earlier PowerPC Macs](https://www.mackido.com/EasterEggs/HW-PCIROM.html). On those machines, you just had to type the text, select it, and drag it to the desktop. Then, the picture would appear. That approach didn't work on the G3.

I suspected there was some similar way to access this hidden image, but nobody had documented it, at least not as far as I could find. So I had no choice but to disassemble the code and see where this text was used. What is it with me and all these crazy rabbit holes?

I extracted the entire `nitt` resource ID 43 to a file and inspected it:
    
    
    $ file nitt43  
    nitt43: header for PowerPC PEF executable

That wasn't too surprising, considering that the first twelve bytes were "Joy!peffpwpc". I fed this entire file into [Ghidra](https://github.com/NationalSecurityAgency/ghidra), which immediately recognized it as a PEF file and had no trouble loading it. Although I'm pretty familiar with reading x86 and ARM assembly, I know essentially nothing about PowerPC assembly code. Thankfully, Ghidra's decompiler worked very well with this file.

There was one problem, though: it didn't detect any references to the "secret ROM image" string, other than inside of a huge list of pointers to variables. After scratching my head a little bit, I realized that Ghidra wasn't doing a great job of finding references to several variables. Luckily, running Auto Analyze a second time after the initial analysis seemed to help it find several more references to things, including all of the strings I was interested in! I didn't change any options with the analyzer; it just found more stuff on the second run.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-2.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-2.png)

The function that used all of these strings was definitely doing something with the .EDisk driver, which I already knew was the RAM disk driver because of past hackery. It seemed to be using `strncmp()` to see if a string was equal to "secret ROM image", and if so, it would create/open/write a file named "The Team".

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-3.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-3.png)

I cleaned up this decompilation quite a bit by giving names to variables and figuring out data types. Fortunately, a lot of the functions like `PBGetVInfoSync()` had lots of public documentation, so I just had to tell Ghidra about the various Mac Toolbox structs being used.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-4.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-4.png)

Okay, that's a lot easier to understand!

I couldn't figure out how to format the 32-bit function arguments such as 0x48504f45 into four-letter codes like `HPOE`, so that's what the comments are. Ghidra simply wouldn't let me display them as ASCII in the decompilation no matter what I did, even though hovering over the constant showed a tooltip with the equivalent text. This is easy to do in IDA, but I couldn't figure out how to convince Ghidra to do it. I tried Set Equate, but it didn't change anything. If someone knows how to make it work, I'd love to hear how!

Anyway, the decompiled code shown above makes sense, and here's a summary of what it does:

  * It looks for a driver called .Edisk. (The driver is really named .EDisk, but I guess Mac OS doesn't care about case sensitivity for this.)
  * It finds a disk associated with that driver (the RAM disk).
  * It looks for a volume associated with that disk.
  * If the volume is named "secret ROM image": 
    * It loads `HPOE` resource ID 1, which contains the JPEG image data.
    * It creates a file of creator `ttxt` and type `JPEG` called "The Team".
    * It opens the file, writes the JPEG data to it, and closes it.
    * Then it does something with the driver control entry that I didn't bother trying to understand further.



Okay, interesting! So this code was clearly looking for the RAM disk to be named "secret ROM image", but I wasn't sure exactly how to trigger it. This function was only ever called in one other place: another function, which was checking to see if its first argument was equal to the value 0x3DA (decimal 986).

I didn't have my beige G3 handy for tinkering, so instead, I mentioned what I had discovered in #mac68k on Libera. [^alex came to the rescue](https://infosec.exchange/@atax1a/114729277160021527) after playing around in Infinite Mac with the hints I had given. They quickly figured out that the trick was to format the RAM disk, and type the special text into the format dialog:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-5.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-5.png)

I got out my desktop G3, tested it out on real hardware, and sure enough, it worked! If you want to try it for yourself just like ^alex did, you can [run Infinite Mac in your browser using this link, which sets up an emulated beige G3 running Mac OS 8.1](https://infinitemac.org/1998/Mac%20OS%208.1?infinite_hd=false&saved_hd=false&machine=Power+Macintosh+G3+%28Beige%29) using DingusPPC. There's a quirk that causes it to fail to resolve an alias at startup. I intentionally disabled it; just click Stop when the error pops up. Here are instructions:

  * Enable the RAM Disk in the Memory control panel.
  * Choose Restart from the Special menu.
  * After the desktop comes back up, select the RAM Disk icon.
  * Choose Erase Disk from the Special menu.
  * Type the _secret ROM image_ text exactly as depicted above.
  * Click Erase.



When you open the newly-formatted RAM disk, you should see a file named "The Team":

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-6.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-6.png)

If you double-click the file, SimpleText will open it:

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-8.png)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image-8.png)

Based on various people's tests, including my own, it sounds like [this trick works all the way up through Mac OS 9.0.4](https://bsky.app/profile/eaglebtc.bsky.social/post/3lsaz3jqsds2w), but 9.1 may have been the first version where it finally stopped working.

As far as I have been able to determine, this particular secret was undiscovered until now. People definitely knew the image was there in the ROM, but nobody had figured out how to actually activate it. This is probably one of the last easter eggs that existed in the Mac prior to [Steve Jobs reportedly banning them in 1997 when he returned to Apple](https://gizmodo.com/the-easter-eggs-are-back-in-os-x-and-this-one-is-insane-5929286). I wonder if he ever knew about this one?

Special thanks to ^alex for figuring out that the RAM Disk needed to be erased in order to activate the easter egg! I'm not sure I would have thought to try that, and it would have taken a lot more work to trace through the rest of the code to figure it out.

If you are reading this post and you were on "The Team", I'd love to hear about it! I'm curious if anyone who worked at Apple in the era remembers this little secret.

Address: <https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/>

« [Modifying an HDMI dummy plug's EDID using a Raspberry Pi](https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/)

[An update about the hidden Performa 550 recovery partition](https://www.downtowndougbrown.com/2025/08/an-update-about-the-hidden-performa-550-recovery-partition/) »

[Trackback](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/trackback/ "Trackback URI")

### 22 comments

  1. [Doug Brown Found a Power Mac G3 Rom Easter Egg Nearly 30 Years After Launch - 512 Pixels](https://512pixels.net/2025/06/doug-brown-g3-rom/) @ 2025-06-24 06:35

[…] Doug Brown Found a Power Mac G3 Rom Easter Egg Nearly 30 Years After Launch -> […]

  2. Anon @ 2025-06-24 07:28

![](https://secure.gravatar.com/avatar/e3eee336b0968f93554afdae5ee49f00c14a4f25be66a9f75355b5ca429096d5?s=32&d=mm&r=g)

What about the "Break at Event Match - Native" part?

  3. Ben Shelton @ 2025-06-24 08:26

![](https://secure.gravatar.com/avatar/313e1bb1126e4f188d73f0d731c3951de42f6afd2b171a706ab8462a8e63fe52?s=32&d=mm&r=g)

FYI, the Ghidra bug for not displaying the FourCC strings properly is here: <https://github.com/NationalSecurityAgency/ghidra/issues/5209>

I filed it a couple of years ago and it hasn't been fixed yet, and I haven't had the cycles to fix it myself.

  4. [pete twentythree](https://pete23.com) @ 2025-06-24 11:16

![](https://secure.gravatar.com/avatar/52ad5fc2e08b532159c644cd7c3848d335fdb4f392d6fad5bdcb91b072f37742?s=32&d=mm&r=g)

super cool - and thanks for the spur to verify that infinitemac works perfectly on an ipad in the bath:-)

  5. ^alex @ 2025-06-24 12:48

![](https://secure.gravatar.com/avatar/de1ea5899f53e50782a946ddb7e29fecdddfdf317ded0b6d36704ed0d404474c?s=32&d=mm&r=g)

@anon "Break at Event Match - Native" doesn't seem easter-eggy, it's more likely a debugging feature for the SCSI manager.

  6. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-06-24 15:23

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

^alex is right, that was a separate string used by a different function, totally unrelated to the easter egg. At first glance in a hex editor, it confused me because I thought it was a big string like "The Team Break at…" but then Ghidra set me straight. Also you can see the 0x1D after The Team.

Thank you Ben! It's good to know I'm not going crazy with Ghidra's lack of FourCC support.

Haha, very cool you got it working on an iPad, pete!

  7. [Salih Muhammed](https://larr.net) @ 2025-06-24 16:18

![](https://secure.gravatar.com/avatar/c7826fae64fdf86e9ebafdc1ced3b59f0af152881a75e985fcd5f535cb534e07?s=32&d=mm&r=g)

Wow that's super cool. Can't wait to listen to the story from The Team side

  8. [Bradley Dichter](https://bradmacpro.com) @ 2025-06-25 05:42

![](https://secure.gravatar.com/avatar/c2352a053cc57804734dbe0f062c70e36427becd0027c1eed35e732bacbd8325?s=32&d=mm&r=g)

I wonder if one could determine the names associated with the images as a first step. Who worked on the project?

  9. Andrew @ 2025-06-25 06:15

![](https://secure.gravatar.com/avatar/c7443f367b6ec5a676167e9d201b2d621381dd68988e439d551fd57038680200?s=32&d=mm&r=g)

Thanks, that was fun to replicate in the emulator. Super nostalgic to load the old OS again.

  10. Bill Saperstein @ 2025-06-25 12:56

![](https://secure.gravatar.com/avatar/fd0ae217ad801fc7c3189104759a017a8de79afc841c0633a09dac6633f765c5?s=32&d=mm&r=g)

Doug, you resurfaced some old memories. I was the leader of that team (fourth from left in second row) that did all the G3 products. For Apple, the team was very small to develop three outstanding products and drove the Apple desktop line for two years…btw, Steve hated the industrial design of the G3 family and he basically took the G3 architecture and put it in the all-in-one iMac.  
We all new about the easter egg, but as you mention; the technique to extract it changed from previous Mac's (although the location was the same). This resulted from an easter egg in the original PowerMac that contained Paula Abdul (without permissions, of course). So the G3 team wanted to still have our pictures in the ROM, but we had to keep it very secret.

  11. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-06-25 16:09

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

Thank you Salih!

I'm glad you enjoyed it Andrew!

Bradley, I was wondering the same thing, and then Bill chimed in today 🙂

Thanks for commenting, Bill! That's really cool that you saw this post and still remember the easter egg. It's very impressive that a small team developed such a cool set of products. I for one very much enjoyed the all-in-one beige G3 machines in my middle school's computer lab that your team worked on!

Now I'm curious about the Paula Abdul easter egg and if it was in ROM or the OS. I found an article in the Wall Street Journal that referred to it being in the 8100-110 but then removed. Maybe I'll have to dig deeper.

You might be interested in reading [this post on 68kmla](https://68kmla.org/bb/index.php?threads/getting-g3-whisper-perch-usb-working.43681/) where croissantking figured out how to add a USB port to the beige G3 by soldering in unpopulated components on the personality card. I found it interesting that Apple decided against putting the USB port on those machines even though it was clearly in the plans at some point.

  12. Bill Saperstein @ 2025-06-26 08:06

![](https://secure.gravatar.com/avatar/fd0ae217ad801fc7c3189104759a017a8de79afc841c0633a09dac6633f765c5?s=32&d=mm&r=g)

Doug,  
The Paula Abdul egg was in the ROM, I think, and it was removed before the product was released (although some machines may have snuck thru with it remaining)l…so you won't probably won't be able to re-surface it on your machine.  
The G3 line of Macs was an interesting development. It was essentially a skunk works project that my team started after we had stopped developing cross-platform Macs (DOS and windows compatible). We set out to make a <$1000 Mac that was really fast and leveraged components from the PC world when possible. I worked with IBM to develop a high performance Power PC processor with a backside high speed cache…that was the key factor that made the G3 line so performing…now it's common practice, but the G3 was probably the first PC with that cache architecture.  
The all-in-one you talk about was designed for the education market and was really successful there…it had video in/out on the AV card which was really popular and great for schools.  
We didn't put USB on the G3 because we had ADB which was legacy. Since the devices had PCI, USB would have been straightforward as an I/O card, but I don't know if any were developed after market.  
My team at Apple was a bunch of rag tag engineers and techs that were not considered the A-team (or even the B-team). And I was a true rebel at Apple not following any of the legacy established by Steve…in fact, I got labelled a heretic when I designed the Mac DOS/Windows compatible Mac :^) It was voted the best system of the year at COMDEX, but Apple refused to accept the award!  
The team was really a group of talented people (both hw and sw) that were believers in the architecture I presented, and executed the design behind the scenes for a year until Jon Rubenstein got wind of it and presented it to Steve and the rest is 'history'.

  13. David Hollway @ 2025-06-26 10:52

![](https://secure.gravatar.com/avatar/52685ab78c0ceba18b2b07252f549388a1791e42142b27aafa374a298b2d06f1?s=32&d=mm&r=g)

Thanks Doug for discovering and documenting this (I came here from today's link on Hackaday - gratitude to HaD for alerting me, too)  
And Bill, thank you for taking the time to post your reminiscences. I've been in the tech industry since the early-90s and it was definitely a different - more optimistic, although perhaps that's just the nostalgia of age talking? - time. Stories such as yours provide fascinating color to a history that most of us only witnessed from the other side of the curtain. I was (well, still am) an Amiga superfan back then, and I recognize much of the spirit of that team in what you've said.  
Thank you both!

  14. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-06-26 15:48

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

Bill, thank you for all that wonderful info! David worded it much more eloquently than me, but I just want to second all the thanks for taking the time to post about it. (And thank you for your kind comment too, David!)

It's really interesting hearing your tidbits about these projects. I actually have a Centris 610 and added a Houdini card to it fairly recently, so I think I've played around with even more cool technologies that your team worked on. I also enjoyed the (already known) easter egg in the PC Setup control panel with the fake DOS prompt!

On the topic of the talented people on the team -- that was something I had wondered: whether the people in the photo were only the ROM team, or if it was people involved in the hardware and other software pieces as well. Sounds like it was a mix of everyone!

  15. [After 27 years, engineer discovers how to display secret photo in Power Mac ROM - Ars Technica](https://arstechnica.com/gadgets/2025/06/after-27-years-engineer-discovers-how-to-display-secret-photo-in-power-mac-rom/) @ 2025-06-27 15:08

[…] Tuesday, software engineer Doug Brown published his discovery of how to trigger a long-known but previously inaccessible Easter egg in the Power […]

  16. Adespoton @ 2025-06-27 16:05

![](https://secure.gravatar.com/avatar/0a834fd8a9b53395c5614af0b21b754269c9564832b79f223bbc0ab702dffdd2?s=32&d=mm&r=g)

Congrats, Doug! You've now been picked up by the press!

Also, congrats on connecting these dots; I've been busy and totally missed this!

  17. [↦ Finding a 27-year-old easter egg in the Power Mac G3 ROM](https://camiel.schoonens.nl/2025/%e2%86%a6-finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/) @ 2025-06-28 04:48

[…] 🔗 Finding a 27-year-old easter egg in the Power Mac G3 ROM […]

  18. Jonathan @ 2025-06-28 07:54

![](https://secure.gravatar.com/avatar/a400e9f456460cfdb29e9674474294d8bcdb199c746119a6306f9471cbf84baa?s=32&d=mm&r=g)

Bill, I just wanted to thank you for the work of yourself and your team on the G3 line. I was ready to abandon the Mac in 1998 or so after being a campus sales person during college. I started with a IIsi and was stuck on the 7100/66 at the time. But then the Beige G3 line came out and it was the single best Mac I have ever owned- fast, expandable, affordable. I did add a PCI USB card, as well as a better video card to upgrade from the Rage II onboard chip. Used the jumpers to speed up the stock 233 MHz CPU and then eventually replaced the CPU with a faster G3. That computer made me believe in the Mac again, and I've been here ever since. 

I do have one question- was there any pushback from within apple about how easy it was to buy the 233 MHz version and speed it up by just changing the motherboard jumpers? I was able to get to 266 MHz without issues, and even could run higher with the 83 MHz bus option at pretty good stability (not perfect). It was clear that you wanted this platform to last a long time, but it was surprising at how much headroom was in the initial, low cost model. Hell, they even gave me a free digital camera for buying it!

  19. Dusty Modem @ 2025-06-28 09:23

![](https://secure.gravatar.com/avatar/e4b3776ae73f70651e5b372947669779b7a7923c60c33f8708e584e8e8db806d?s=32&d=mm&r=g)

I think the most fascinating part of the “secret rom image” story is that the Power Mac G3 platform was a skunkworks project going on under the noses of Ruby and Jobs. Has this been written about? I’m sure I’m not alone in wanting to hear more about this!

  20. [D Liu](https://dan-liu.net) @ 2025-06-29 06:11

![](https://secure.gravatar.com/avatar/2a6bb8ccb2a9092a2e36ab4cc786c6206342c81035508e40eb48c9c5d401c139?s=32&d=mm&r=g)

I think it's incredible that you found this easter egg by finding Pascal comments buried in the SCSI Manager, but that revealing the easter egg required nothing more of the user than typing a phrase in plain English into the Finder's Erase Disk dialog. There is something that's so Classic Mac about this — OS X would have you to recite some commands and incantations in the Terminal.

  21. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-06-29 10:07

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

Thanks Adespoton!

I totally agree, Dusty. It's fascinating to learn that the G3 was a skunkworks project started by the same team that developed the DOS compatibility cards. I wonder where the Power Mac 9700/PowerExpress project fits into all of that. Was that a completely different team and project? I know there are a few prototypes of that system floating around. Looks like the dumped ROMs from it might even have the same easter egg entry method as the G3.

Thanks D Liu, and I agree!

  22. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-07-04 08:22

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

For anyone looking for more details about the Paula Abdul easter egg that Bill mentioned, Pierre did some excellent sleuthing:

<https://www.journaldulapin.com/2025/07/01/easter-egg-paula-abdul/>

It turns out that it's actually in the PowerPC Enabler version 1.1 which Apple pulled and replaced with 1.1.1 after they found out about it. Sounds like the egg caused a whole fiasco that delayed the release of the Power Mac 8100/110. But, the Spanish version of the 1.1 enabler, with the easter egg intact, did survive on a developer CD.

More discussion here. I was eventually able to reproduce it in joevt's fork of DingusPPC: <https://68kmla.org/bb/index.php?threads/paula-abdul-and-the-power-mac-8100-110.50347/>




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
