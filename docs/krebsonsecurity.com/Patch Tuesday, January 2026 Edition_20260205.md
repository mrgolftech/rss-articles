# Patch Tuesday, January 2026 Edition

**来源:** https://krebsonsecurity.com
**链接:** https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/
**日期:** Wed, 14 Jan 2026 00:47:38 +0000

---

Advertisement

[ ![](/b-knowbe4/44.png) ](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

Advertisement

[ ![](/b-knowbe4/45.png) ](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

[__](http://twitter.com/briankrebs)[__](https://krebsonsecurity.com/feed/)[__](https://www.linkedin.com/in/bkrebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[__](http://twitter.com/briankrebs)[__](https://krebsonsecurity.com/feed/)[__](https://www.linkedin.com/in/bkrebs/)

Skip to content

  * [Home](https://krebsonsecurity.com/)
  * [About the Author](https://krebsonsecurity.com/about/)
  * [Advertising/Speaking](https://krebsonsecurity.com/cpm/)



# Patch Tuesday, January 2026 Edition

January 13, 2026

[18 Comments](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comments)

**Microsoft** today issued patches to plug at least 113 security holes in its various **Windows** operating systems and supported software. Eight of the vulnerabilities earned Microsoft's most-dire "critical" rating, and the company warns that attackers are already exploiting one of the bugs fixed today.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

January's Microsoft zero-day flaw -- [CVE-2026-20805](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-20805) -- is brought to us by a flaw in the **Desktop Window Manager** (DWM), a key component of Windows that organizes windows on a user's screen. **Kev Breen** , senior director of cyber threat research at **Immersive** , said despite awarding CVE-2026-20805 a middling CVSS score of 5.5, Microsoft has confirmed its active exploitation in the wild, indicating that threat actors are already leveraging this flaw against organizations.

Breen said vulnerabilities of this kind are commonly used to undermine [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization) (ASLR), a core operating system security control designed to protect against buffer overflows and other memory-manipulation exploits.

"By revealing where code resides in memory, this vulnerability can be chained with a separate code execution flaw, transforming a complex and unreliable exploit into a practical and repeatable attack," Breen said. "Microsoft has not disclosed which additional components may be involved in such an exploit chain, significantly limiting defenders’ ability to proactively threat hunt for related activity. As a result, rapid patching currently remains the only effective mitigation."

**Chris Goettl** , vice president of product management at **Ivanti** , observed that CVE-2026-20805 affects all currently supported and extended security update supported versions of the Windows OS. Goettl said it would be a mistake to dismiss the severity of this flaw based on its "Important" rating and relatively low CVSS score.

"A risk-based prioritization methodology warrants treating this vulnerability as a higher severity than the vendor rating or CVSS score assigned," he said.

Among the critical flaws patched this month are two **Microsoft Office** remote code execution bugs ([CVE-2026-20952](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-20952) and [CVE-2026-20953](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-20953)) that can be triggered just by viewing a booby-trapped message in the Preview Pane.

Our October 2025 Patch Tuesday ["End of 10" roundup](https://krebsonsecurity.com/2025/10/patch-tuesday-october-2025-end-of-10-edition/) noted that Microsoft had removed a modem driver from all versions after it was discovered that hackers were abusing a vulnerability in it to hack into systems. **Adam Barnett** at **Rapid7** said Microsoft today removed another couple of modem drivers from Windows for a broadly similar reason: Microsoft is aware of functional exploit code for an elevation of privilege vulnerability in a very similar modem driver, tracked as [CVE-2023-31096](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2023-31096).

"That’s not a typo; this vulnerability was originally published via MITRE over two years ago, along with a credible public writeup by the original researcher," Barnett said. "Today’s Windows patches remove agrsm64.sys and agrsm.sys. All three modem drivers were originally developed by the same now-defunct third party, and have been included in Windows for decades. These driver removals will pass unnoticed for most people, but you might find active modems still in a few contexts, including some industrial control systems."

According to Barnett, two questions remain: How many more legacy modem drivers are still present on a fully-patched Windows asset; and how many more elevation-to-SYSTEM vulnerabilities will emerge from them before Microsoft cuts off attackers who have been enjoying "living off the land[line] by exploiting an entire class of dusty old device drivers?"

"Although Microsoft doesn’t claim evidence of exploitation for CVE-2023-31096, the relevant 2023 write-up and the 2025 removal of the other Agere modem driver have provided two strong signals for anyone looking for Windows exploits in the meantime," Barnett said. "In case you were wondering, there is no need to have a modem connected; the mere presence of the driver is enough to render an asset vulnerable."

Immersive, Ivanti and Rapid7 all called attention to [CVE-2026-21265](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21265), which is a critical Security Feature Bypass vulnerability affecting Windows Secure Boot. This security feature is designed to protect against threats like rootkits and bootkits, and it relies on a set of certificates that are set to expire in June 2026 and October 2026. Once these 2011 certificates expire, Windows devices that do not have the new 2023 certificates can no longer receive Secure Boot security fixes.

Barnett cautioned that when updating the bootloader and BIOS, it is essential to prepare fully ahead of time for the specific OS and BIOS combination you’re working with, since incorrect remediation steps can lead to an unbootable system.

"Fifteen years is a very long time indeed in information security, but the clock is running out on the Microsoft root certificates which have been signing essentially everything in the Secure Boot ecosystem since the days of Stuxnet," Barnett said. "Microsoft issued replacement certificates back in 2023, alongside CVE-2023-24932 which covered relevant Windows patches as well as subsequent steps to remediate the Secure Boot bypass exploited by the BlackLotus bootkit."

Goettl noted that **Mozilla** has released updates for **Firefox** and **Firefox ESR** resolving a total of 34 vulnerabilities, two of which are suspected to be exploited (CVE-2026-0891 and CVE-2026-0892). Both are resolved in Firefox 147 (MFSA2026-01) and CVE-2026-0891 is resolved in Firefox ESR 140.7 (MFSA2026-03).

"Expect **Google Chrome** and **Microsoft Edge** updates this week in addition to a high severity vulnerability in Chrome WebView that was resolved in the January 6 Chrome update (CVE-2026-0628)," Goettl said.

As ever, the [SANS Internet Storm Center](https://isc.sans.edu/forums/diary/January%202026%20Microsoft%20Patch%20Tuesday%20Summary/32624/) has a per-patch breakdown by severity and urgency. Windows admins should keep an eye on [askwoody.com](https://www.askwoody.com/2026/january-2026-updates/) for any news about patches that don't quite play nice with everything. If you experience any issues related installing January's patches, please drop a line in the comments below.

_This entry was posted on Tuesday 13th of January 2026 07:47 PM_

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Adam Barnett](https://krebsonsecurity.com/tag/adam-barnett/) [Chris Goettl](https://krebsonsecurity.com/tag/chris-goettl/) [CVE-2023-31096](https://krebsonsecurity.com/tag/cve-2023-31096/) [CVE-2026-0628](https://krebsonsecurity.com/tag/cve-2026-0628/) [CVE-2026-0891](https://krebsonsecurity.com/tag/cve-2026-0891/) [CVE-2026-0892](https://krebsonsecurity.com/tag/cve-2026-0892/) [CVE-2026-20805](https://krebsonsecurity.com/tag/cve-2026-20805/) [CVE-2026-20952](https://krebsonsecurity.com/tag/cve-2026-20952/) [CVE-2026-20953](https://krebsonsecurity.com/tag/cve-2026-20953/) [CVE-2026-21265](https://krebsonsecurity.com/tag/cve-2026-21265/) [Desktop Window Manager](https://krebsonsecurity.com/tag/desktop-window-manager/) [Immersive](https://krebsonsecurity.com/tag/immersive/) [Ivanti](https://krebsonsecurity.com/tag/ivanti/) [Kev Breen](https://krebsonsecurity.com/tag/kev-breen/) [Microsoft Office](https://krebsonsecurity.com/tag/microsoft-office/) [Microsoft Patch Tuesday January 2026](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-january-2026/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/)

  


Post navigation

[<- Who Benefited from the Aisuru and Kimwolf Botnets?](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/) [Kimwolf Botnet Lurking in Corporate, Govt. Networks ->](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/)

##  18 thoughts on "Patch Tuesday, January 2026 Edition"

  1. mealy [January 13, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-640347)

Krebsonsecurity under active DDOS? Or something else?

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=640347#respond) ->

     1. mealy [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-641338)

Something else. I won't call it AI because it's just A.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=641338#respond) ->

        1. bob [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-649774)

So, perhaps AOAI?

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=649774#respond) ->

  2. Mike Jackson [January 13, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-640349)

Why the "CAPTCHA" entry required to read this on: <https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/> ??? NEVER had to do this before. What gives?

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=640349#respond) ->

     1. Muffin [January 15, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650293)

Me too.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650293#respond) ->

  3. e e [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-640350)

The DDoS protection broke my RSS reader, maybe an exception can be made for /feed/atom/ ?

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=640350#respond) ->

     1. ramalamadingdong [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-649582)

Noone uses atom or RSS anymore, just like noone needs a no-longer-manufactured Radio Shack frigging crystal from the late 80s/early 90s or stupid crap about movies that are over 30 years old or crappy Wells Fargo ripoffs of said movie.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=649582#respond) ->

        1. Steve [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650226)

I use RSS. Without it, I wouldn't be alerted to krebsonsecurity posts. RSS may be old, but it's simple and effective.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650226#respond) ->

        2. [BrianKrebs](http://www.krebsonsecurity.com) Post author[January 19, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650348)

I beg to differ. Last time I checked we had somewhere near 200,000 subscribers to our RSS feed. Tons of people read this site only through an RSS reader.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650348#respond) ->

        3. JT [January 30, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650512)

No one should spell no one as noone.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650512#respond) ->

  4. [Catwhisperer](https://happycattech.com) [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650224)

Nope. When 10 is done, so is Windows. Got 11 on a partition and it hasn't started for at least a month. That partition will eventually get FreeBSD. There are so many other options now. Mostly free, but it's better to pay for pro versions. You don't even need to be a geek. You won't be paying hundreds of dollars per year for Ascrewme, Micro$lop 365, etc. And finally, some vendors are selling PC's with Linux preinstalled rather than Windows.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650224#respond) ->

  5. Marvin [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650225)

I did not get any updates on Windows 7.

Have they ended those?

The last one I received was December 9, 2025.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650225#respond) ->

     1. [Really](http://N/A) [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650238)

A simple google search would of shown Windows 7 Operating system update are EOL

"Microsoft ended mainstream support for Windows 7 (including security updates and technical assistance) on January 14, 2020, making devices running it vulnerable to new malware and exploits, though paid Extended Security Updates (ESUs) were available for enterprises until January 10, 2023"

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650238#respond) ->

  6. Lynn Sattler [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650233)

We updated 2 windows 11 25h2 systems with this January update and there were no issues.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650233#respond) ->

  7. KingD [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650236)

Verizon is down in Maryland and other states over an hour ago, Its 2:06 pm on Jan 14th 2026. No 2FA possible until resolved.  
Is there any scoop on what is going on?

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650236#respond) ->

  8. CT [January 14, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650241)

I wonder, how far off is the patch that bricks devices installed with TPM or Secure Boot registry workarounds.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650241#respond) ->

  9. Scotty [January 20, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650362)

Thank you Brian! Appreciate all you do Sir.

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650362#respond) ->

  10. [John Crowe](http://krebsonsecurity/com) [January 28, 2026](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comment-650479)

Why are you not covering KB5078127 from Microsoft? OOB on 24 January

[Reply](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/?replytocom=650479#respond) ->




### Leave a Reply [Cancel reply](/2026/01/patch-tuesday-january-2026-edition/#respond)

Your email address will not be published. Required fields are marked *

Comment *

Name *

Email *

Website

Δ

Advertisement

[ ![](/b-knowbe4/46.png) ](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

  


Advertisement

  


Mailing List

[Subscribe here](/subscribe/)

Search KrebsOnSecurity

Search for:

Recent Posts

  * [Please Don't Feed the Scattered Lapsus ShinyHunters](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/)
  * [Who Operates the Badbox 2.0 Botnet?](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/)
  * [Kimwolf Botnet Lurking in Corporate, Govt. Networks](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/)
  * [Patch Tuesday, January 2026 Edition](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/)
  * [Who Benefited from the Aisuru and Kimwolf Botnets?](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/)



Story Categories

  * [A Little Sunshine](https://krebsonsecurity.com/category/sunshine/)
  * [All About Skimmers](https://krebsonsecurity.com/category/all-about-skimmers/)
  * [Ashley Madison breach](https://krebsonsecurity.com/category/ashley-madison-breach/)
  * [Breadcrumbs](https://krebsonsecurity.com/category/breadcrumbs/)
  * [Data Breaches](https://krebsonsecurity.com/category/data-breaches/)
  * [DDoS-for-Hire](https://krebsonsecurity.com/category/ddos-for-hire/)
  * [DOGE](https://krebsonsecurity.com/category/doge/)
  * [Employment Fraud](https://krebsonsecurity.com/category/employment-fraud/)
  * [How to Break Into Security](https://krebsonsecurity.com/category/how-to-break-into-security/)
  * [Internet of Things (IoT)](https://krebsonsecurity.com/category/internet-of-things-iot/)
  * [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/)
  * [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/)
  * [Other](https://krebsonsecurity.com/category/other/)
  * [Pharma Wars](https://krebsonsecurity.com/category/pharma-wars/)
  * [Ransomware](https://krebsonsecurity.com/category/ransomware/)
  * [Russia's War on Ukraine](https://krebsonsecurity.com/category/russias-war-on-ukraine/)
  * [Security Tools](https://krebsonsecurity.com/category/security-tools/)
  * [SIM Swapping](https://krebsonsecurity.com/category/sim-swapping/)
  * [Spam Nation](https://krebsonsecurity.com/category/spam-nation/)
  * [Target: Small Businesses](https://krebsonsecurity.com/category/smallbizvictims/)
  * [Tax Refund Fraud](https://krebsonsecurity.com/category/tax-refund-fraud/)
  * [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)
  * [Time to Patch](https://krebsonsecurity.com/category/patches/)
  * [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)



Why So Many Top Hackers Hail from Russia

[![](https://krebsonsecurity.com/wp-content/uploads/2017/06/computered-580x389.png)](https://krebsonsecurity.com/2017/06/why-so-many-top-hackers-hail-from-russia/)

(C) Krebs on Security - [Mastodon](https://infosec.exchange/@briankrebs)   

