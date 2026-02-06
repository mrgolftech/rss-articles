# Modifying an HDMI dummy plug’s EDID using a Raspberry Pi

**来源:** https://downtowndougbrown.com
**链接:** https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/
**日期:** Sun, 15 Jun 2025 14:17:58 +0000

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

15

## [Modifying an HDMI dummy plug's EDID using a Raspberry Pi](https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/ "Permanent Link to Modifying an HDMI dummy plug’s EDID using a Raspberry Pi")

Doug Brown [Linux](https://www.downtowndougbrown.com/category/linux/) 2025-06-15

I recently found myself needing to change the monitor that a cheap HDMI "dummy plug" pretended to be. It was a random one I had bought on Amazon several years ago that acted as a 4K monitor, and I needed it to be something simpler that didn't support a 4K resolution. The story behind why is a long one that I'm still figuring out and might eventually become a separate blog post in the future.

If you're not familiar with dummy plugs, here's a quick primer: they are tiny dongles you can plug into an HDMI, DVI, etc. port that don't actually do anything with the video signal. They simply have the minimum circuitry needed for a video source device, like a computer, to think that a monitor is hooked up. In general this entails a pull-up resistor on pin 19 (HPD) to +5V, as well as a little I2C EEPROM chip containing the [Extended Display Identification Data (EDID)](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data). This is useful for headless machines to force the OS to think a monitor is attached.

![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/img_4533-e1748812707110-265x300.jpg)

The EDID contains all the info about the monitor: the manufacturer, manufacture date, supported resolutions, audio channels, color space, and stuff like that. My goal was to replace the dummy plug's EDID with an identical copy of an EDID from one of my many 1080p HDMI capture devices. Then, the computer I plugged it into would think the capture device was plugged in instead of a 4K monitor, and everything would be hunky dory.

I wasn't sure if the dummy plug's EDID EEPROM would be programmable, but I decided to give it a shot. There was a chance that it would have its write-protect pin configured to disable programming, but I figured it wouldn't hurt to try.

Conveniently, I found that my Raspberry Pi Zero has an I2C controller wired to the correct pins on its HDMI port. This makes sense -- the Pi would need to be able to read the EDID of an attached monitor. [This post on the Raspberry Pi Forums](https://forums.raspberrypi.com/viewtopic.php?t=329239#p1970760) and [this GitHub comment](https://github.com/raspberrypi/linux/issues/6207#issuecomment-2149784322) were helpful for explaining which I2C controller(s) to look at in software on various Pi devices:

  * Pi 0-3: 
    * `/dev/i2c-2`
  * Pi 4: 
    * `/dev/i2c-20`
    * `/dev/i2c-21`
  * Pi 5: 
    * `/dev/i2c-11`
    * `/dev/i2c-12`



Before I go further,**I want to make it clear that it may be possible to screw up a monitor if you follow these instructions while a real monitor is plugged in and it doesn 't have its EDID protected**. Be careful to only run these commands if you have something attached to the HDMI port that you're not afraid of bricking, such as a dummy plug! **Also, make sure you are confident you 're on the correct I2C bus! Always read the EDID and parse it first to make sure it actually contains an EDID before you attempt a write.** If you attempt these commands on a PC, it's possible that you could accidentally flash hardware that isn't an EDID, like a RAM module's SPD EEPROM.

Starting from a fresh Raspberry Pi OS Lite install, I performed the following modifications:

  * `sudo raspi-config`
    * Under Interface Options, enable I2C [as described in the Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/configuration.html).
  * `sudo apt install i2c-tools`
    * Unfortunately, this requires network access, which creates a bit of a problem if you are on a Pi Zero. You might need a USB-Ethernet adapter to make this happen. Another slightly crazy option is to temporarily take the SD card out of your Pi, put it into your desktop PC running Debian/Ubuntu, run `sudo apt install binfmt-support qemu-user-static` on your PC, [chroot into the SD card's rootfs](https://wiki.debian.org/RaspberryPi/qemu-user-static) (options 1.3 and 2.1 worked for me), and run the apt install command inside of the chroot.



And with those prerequisites out of the way, I was ready to start tinkering with the dummy plug's EEPROM. Note that I also needed an HDMI-to-Mini-HDMI adapter.

[![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/img_4600-224x300.jpg)](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/img_4600.jpg)

Since I was using a Raspberry Pi Zero, I chose bus 2. You could change the number below to something else on a different model, as listed above (e.g. 20 or 21 on a Pi 4).
    
    
    edid_i2c=2
    

I ran i2cdetect to see if the EDID EEPROM was recognized:
    
    
    i2cdetect -y $edid_i2c
    

This came back with the following result, showing that an I2C device was detected at address 0x50, which is exactly the address used for EDID:
    
    
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f  
    00:                         -- -- -- -- -- -- -- --   
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --   
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --   
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --   
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --   
    50: 50 51 52 53 54 55 56 57 -- -- -- -- -- -- -- --   
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --   
    70: -- -- -- -- -- -- -- --                         

Interestingly, this particular dummy plug also responds with addresses 0x51 through 0x57 present. These other addresses seem to contain copies of the same EDID. Not all dummy plugs show up like this -- another one I have only detects 0x50. Anyway, next, I dumped the original EDID from it:
    
    
    get-edid -b $edid_i2c > edid-orig.bin
    
    
    
    2  
    This is read-edid version 3.0.2. Prepare for some fun.  
    Attempting to use i2c interface  
    Only trying 2 as per your request.  
    256-byte EDID successfully retrieved from i2c bus 2  
    Looks like i2c was successful. Have a good day.

Nice! To make sure I got a good dump, I tried it twice and compared the results to make sure they were identical. Then I printed it in a format suitable for copying/pasting to something like [edidreader.com](https://www.edidreader.com/):
    
    
    od -v -An -txC edid-orig.bin
    

This spit out a nice little hex dump of the EDID that was stored on it:
    
    
     00 ff ff ff ff ff ff 00 1a ae 31 9d 00 00 00 00  
     01 19 01 04 85 58 31 78 3e a4 fd ab 4e 42 a6 26  
     0d 47 4a 2f cf 00 e1 c0 d1 c0 b3 00 a9 40 95 00  
     81 80 81 40 81 c0 02 3a 80 18 71 38 2d 40 58 2c  
     45 00 e0 0e 11 00 00 1e 4d d0 00 a0 f0 70 3e 80  
     30 20 35 00 c0 1c 32 00 00 1a 00 00 00 fc 00 48  
     44 4d 49 20 4d 6f 6e 69 74 6f 72 0a 00 00 00 10  
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 4a  
     02 03 46 70 52 e1 60 5f 5d e6 65 64 62 10 04 03  
     1f 20 21 22 13 12 01 26 09 7f 07 11 7f 50 83 01  
     00 00 6e b9 14 00 40 00 18 78 20 00 60 01 02 03  
     04 67 d8 5d c4 01 78 00 07 6c 03 0c 00 20 00 f0  
     78 20 00 40 01 04 08 e8 00 30 f2 70 5a 80 b0 58  
     8a 10 c0 1c 32 00 00 1e b7 e6 ff 18 f1 70 5a 80  
     58 2c 8a 00 ff 1c 32 00 00 1e 56 5e 00 a0 a0 a0  
     29 50 30 20 35 00 80 68 21 00 00 1a 00 00 00 e9

Pasting it into the site linked above, I could see it was a valid EDID:

![](https://www.downtowndougbrown.com/wp-content/uploads/2025/06/image.png)

Now that I was confident I had the dummy plug's original EDID backed up, I unplugged it from the Pi's HDMI port and plugged my capture device in instead, and repeated the exact same procedure to dump its EDID:
    
    
    get-edid -b $edid_i2c > edid-capture-card.bin
    

I confirmed it was also a valid EDID. Finally, I unplugged the capture device and connected the dummy plug again, and wrote the capture device's EDID to it with this fun little code snippet. [There are tools out there](https://github.com/galkinvv/edid-checked-writer) that can probably do this more efficiently, but hey, this works and doesn't require any special packages other than the standard userspace Linux I2C tools and bash or dash!
    
    
    edidbytes=($(od -v -An -txC edid-capture-card.bin))
    for i in "${!edidbytes[@]}"; do
    	byte=0x${edidbytes[$i]}
    	echo Writing byte $i: $byte...
    	i2cset -f -y $edid_i2c 0x50 $i $byte
    done
    

As a quick explanation, this reads the entire EDID (probably 256 bytes in size) from the dump file created earlier, and formats it into an array of two-digit hex strings using od. Each entry in the array represents one byte in the EDID. Then it loops over each byte, prepending a "0x" prefix and writing it out to the EEPROM using i2cset.

After running this code, I re-read the EDID from the dummy plug and checked to see if it matched the file I started from:
    
    
    get-edid -b $edid_i2c > edid-test.bin
    diff edid-test.bin edid-capture-card.bin
    

The diff command produced no output at all, which indicated that the new dump was identical. The dummy plug's EEPROM had successfully been reprogrammed with the EDID from my capture device!

Of course, at this point I anxiously plugged it into my test computer, powered the computer up, and noticed that everything was great and it acted as though my HDMI capture device was plugged in instead of a 4K monitor. Success!

I thought I'd share this procedure in case it's useful for someone else in the future. You could probably also use this solution to go in the opposite direction -- upgrading an old 1080p dummy plug to add 4K support. **Again, be careful with these commands!** I wouldn't recommend tinkering with I2C writes on an actual PC. Use a Raspberry Pi so you don't accidentally brick your desktop PC.

Address: <https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/>

« [Please don't ship heavy, fragile vintage computers. They will be destroyed.](https://www.downtowndougbrown.com/2025/05/please-dont-ship-heavy-fragile-vintage-computers-they-will-be-destroyed/)

[Finding a 27-year-old easter egg in the Power Mac G3 ROM](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/) »

[Trackback](https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/trackback/ "Trackback URI")

### 4 comments

  1. caralynx @ 2025-06-15 19:19

![](https://secure.gravatar.com/avatar/4028c7737c26895fa725f9d3079ced9bda0ccf25797f8e56fa298e1ef6196f4e?s=32&d=mm&r=g)

I bought a HDMI dummy plug to try to enable HDR for remote game streaming and had to reflash it because apparently I picked the wrong one. If on Windows and not using an Intel graphics card, the easy way is to use EDID/DisplayID Writer by ToastyX. It's a GUI app, can dump/write EDIDs on attached monitors, and also validates before writing.

  2. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-06-15 20:24

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

Thanks for the recommendation, caralynx! That seems like a great solution for people who don't want to tinker in Linux.

  3. [din](https://icedragon.io) @ 2025-06-16 05:36

![](https://secure.gravatar.com/avatar/8b67187239476f2066e2cb40a897c0641f1e0f906736f8069efd6efcfeaf0abf?s=32&d=mm&r=g)

Hey Doug! Love your blog. 

Not all of these devices are read/writable. They are just simple i2c eeprom's on a board 

If you need to make one read/write you can lift the write enable pin and leave it floating.

I had to write a custom edid for my iMac G3's monitor (longer story!) for it to even sync. 

I had a small writeup on my bluesky with photos if you are interested. 

<https://bsky.app/profile/icedragon.io/post/3lawzvxc65s27>

-din

  4. [Doug Brown](http://www.downtowndougbrown.com/) @ 2025-06-16 15:26

![](https://secure.gravatar.com/avatar/68e1f4f59c61beabc7de171b1eabd8b6ff438074c76d1b76e63eef87d418e1d8?s=32&d=mm&r=g)

Thanks, din!

Nice write-up on Bluesky, and thank you for the tip about needing to potentially lift a pin. I definitely worried about that happening, but didn't run into it on any of the ones I tested. Clearly there are some trickier plugs out there though, as you discovered 🙂

I also heard about another concern: fancier EDIDs for modern high-res and high-refresh-rate monitors are more than 256 bytes and won't fit on a simpler device like these.




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
