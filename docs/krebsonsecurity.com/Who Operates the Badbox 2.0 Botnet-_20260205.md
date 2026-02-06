# Who Operates the Badbox 2.0 Botnet?

**来源:** https://krebsonsecurity.com
**链接:** https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/
**日期:** Mon, 26 Jan 2026 16:11:38 +0000

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



# Who Operates the Badbox 2.0 Botnet?

January 26, 2026

[15 Comments](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comments)

The cybercriminals in control of **Kimwolf** -- a disruptive botnet that has infected more than 2 million devices -- recently shared a screenshot indicating they'd compromised the control panel for **Badbox 2.0** , a vast China-based botnet powered by malicious software that comes pre-installed on many Android TV streaming boxes. Both the FBI and Google say they are hunting for the people behind Badbox 2.0, and thanks to bragging by the Kimwolf botmasters we may now have a much clearer idea about that.

Our first story of 2026, [The Kimwolf Botnet is Stalking Your Local Network](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/), detailed the unique and highly invasive methods Kimwolf uses to spread. The story warned that the vast majority of Kimwolf infected systems were unofficial Android TV boxes that are typically marketed as a way to watch unlimited (pirated) movie and TV streaming services for a one-time fee.

Our January 8 story, [Who Benefitted from the Aisuru and Kimwolf Botnets?](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/), cited multiple sources saying the current administrators of Kimwolf went by the nicknames "**Dort** " and "**Snow**." Earlier this month, a close former associate of Dort and Snow shared what they said was a screenshot the Kimwolf botmasters had taken while logged in to the Badbox 2.0 botnet control panel.

That screenshot, a portion of which is shown below, shows seven authorized users of the control panel, including one that doesn't quite match the others: According to my source, the account "**ABCD** " (the one that is logged in and listed in the top right of the screenshot) belongs to Dort, who somehow figured out how to add their email address as a valid user of the Badbox 2.0 botnet.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/01/badboxpanel.png)](https://krebsonsecurity.com/wp-content/uploads/2026/01/badboxpanel.png)

The control panel for the Badbox 2.0 botnet lists seven authorized users and their email addresses. Click to enlarge.

Badbox has a storied history that well predates Kimwolf's rise in October 2025. In July 2025, Google filed a “John Doe” [lawsuit](https://storage.courtlistener.com/recap/gov.uscourts.nysd.643466/gov.uscourts.nysd.643466.22.0.pdf) (PDF) against 25 unidentified defendants accused of operating Badbox 2.0, which Google described as a botnet of over ten million unsanctioned Android streaming devices engaged in advertising fraud. Google said Badbox 2.0, in addition to compromising multiple types of devices prior to purchase, also can infect devices by requiring the download of malicious apps from unofficial marketplaces.

Google’s lawsuit came on the heels of a [June 2025 advisory](https://www.ic3.gov/PSA/2025/PSA250605) from the **Federal Bureau of Investigation** (FBI), which warned that cyber criminals were gaining unauthorized access to home networks by either configuring the products with malware prior to the user’s purchase, or infecting the device as it downloads required applications that contain backdoors — usually during the set-up process.

The FBI said Badbox 2.0 was discovered after [the original Badbox campaign](https://www.humansecurity.com/learn/blog/trojans-all-the-way-down-badbox-and-peachpit/) was disrupted in 2024. The original Badbox was identified in 2023, and primarily consisted of Android operating system devices (TV boxes) that were compromised with backdoor malware prior to purchase.

KrebsOnSecurity was initially skeptical of the claim that the Kimwolf botmasters had hacked the Badbox 2.0 botnet. That is, until we began digging into the history of the qq.com email addresses in the screenshot above.

## CATHEAD

An online search for the address **34557257@qq.com** (pictured in the screenshot above as the user "**Chen** ") shows it is listed as a point of contact for a number of China-based technology companies, including:

-**Beijing Hong Dake Wang Science & Technology Co Ltd.**  
-**Beijing Hengchuang Vision Mobile Media Technology Co. Ltd.**  
-**Moxin Beijing Science and Technology Co. Ltd.**

The website for Beijing Hong Dake Wang Science is**asmeisvip[.]net** , a domain that was flagged in a [March 2025 report](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/) by **HUMAN Security** as one of several dozen sites tied to the distribution and management of the Badbox 2.0 botnet. Ditto for **moyix[.]com** , a domain associated with Beijing Hengchuang Vision Mobile.

A search at the breach tracking service **Constella Intelligence** finds 34557257@qq.com at one point used the password "**cdh76111**." Pivoting on that password in Constella shows it is known to have been used by just two other email accounts: **daihaic@gmail.com** and **cathead@gmail.com**.

Constella found cathead@gmail.com registered an account at jd.com (China's largest online retailer) in 2021 under the name "陈代海," which translates to "**Chen Daihai**." According to **DomainTools.com** , the name Chen Daihai is present in the original registration records (2008) for moyix[.]com, along with the email address **cathead@astrolink[.]cn**.

Incidentally, astrolink[.]cn also is among the Badbox 2.0 domains identified in [HUMAN Security's 2025 report](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/). DomainTools finds cathead@astrolink[.]cn was used to register more than a dozen domains, including **vmud[.]net** , yet another Badbox 2.0 domain tagged by HUMAN Security.

## XAVIER

A cached copy of astrolink[.]cn preserved at archive.org shows the website belongs to a mobile app development company whose full name is **Beijing Astrolink Wireless Digital Technology Co. Ltd**. The archived website reveals [a "Contact Us" page](https://web.archive.org/web/20070317191651/http://www.astrolink.cn/contact/index.htm) that lists a Chen Daihai as part of the company's technology department. The other person featured on that contact page is **Zhu Zhiyu** , and their email address is listed as **xavier@astrolink[.]cn**.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/beijingastrolink.png)

A Google-translated version of Astrolink's website, circa 2009. Image: archive.org.

Astute readers will notice that the user **Mr.Zhu** in the Badbox 2.0 panel used the email address **xavierzhu@qq.com**. Searching this address in Constella reveals a jd.com account registered in the name of Zhu Zhiyu. A rather unique password used by this account matches the password used by the address **xavierzhu@gmail.com** , which DomainTools finds was the original registrant of astrolink[.]cn.

## ADMIN

The very first account listed in the Badbox 2.0 panel -- "admin," registered in November 2020 -- used the email address **189308024@qq.com**. DomainTools shows this email is found in the 2022 registration records for the domain **guilincloud[.]cn** , which includes the registrant name "**Huang Guilin**."

Constella finds 189308024@qq.com is associated with the China phone number **18681627767**. The open-source intelligence platform **osint.industries** reveals this phone number is connected to a Microsoft profile created in 2014 under the name **Guilin Huang (桂林 黄)**. The cyber intelligence platform **Spycloud** says that phone number was used in 2017 to create an account at the Chinese social media platform Weibo under the username "**h_guilin**."

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/guilinhuang.png)

The public information attached to Guilin Huang's Microsoft account, according to the breach tracking service osintindustries.com.

The remaining [three users and corresponding qq.com email addresses](https://krebsonsecurity.com/wp-content/uploads/2026/01/badbox2-1.png) were all connected to individuals in China. However, none of them (nor Mr. Huang) had any apparent connection to the entities created and operated by Chen Daihai and Zhu Zhiyu -- or to any corporate entities for that matter. Also, none of these individuals responded to requests for comment.

The mind map below includes search pivots on the email addresses, company names and phone numbers that suggest a connection between Chen Daihai, Zhu Zhiyu, and Badbox 2.0.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/01/mm-chen-xavier.png)](https://krebsonsecurity.com/wp-content/uploads/2026/01/mm-chen-xavier.png)

This mind map includes search pivots on the email addresses, company names and phone numbers that appear to connect Chen Daihai and Zhu Zhiyu to Badbox 2.0. Click to enlarge.

## UNAUTHORIZED ACCESS

The idea that the Kimwolf botmasters could have direct access to the Badbox 2.0 botnet is a big deal, but explaining exactly why that is requires some background on how Kimwolf spreads to new devices. The botmasters figured out they could trick residential proxy services into relaying malicious commands to vulnerable devices behind the firewall on the unsuspecting user's local network.

The vulnerable systems sought out by Kimwolf are primarily Internet of Things (IoT) devices like unsanctioned Android TV boxes and digital photo frames that have no discernible security or authentication built-in. Put simply, if you can communicate with these devices, you can compromise them with a single command.

Our [January 2 story](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) featured [research](https://synthient.com/blog/a-broken-system-fueling-botnets) from the proxy-tracking firm **Synthient** , which alerted 11 different residential proxy providers that their proxy endpoints were vulnerable to being abused for this kind of local network probing and exploitation.

Most of those vulnerable proxy providers have since taken steps to prevent customers from going upstream into the local networks of residential proxy endpoints, and it appeared that Kimwolf would no longer be able to quickly spread to millions of devices simply by exploiting some residential proxy provider.

However, the source of that Badbox 2.0 screenshot said the Kimwolf botmasters had an ace up their sleeve the whole time: Secret access to the Badbox 2.0 botnet control panel.

"Dort has gotten unauthorized access," the source said. "So, what happened is normal proxy providers patched this. But Badbox doesn't sell proxies by itself, so it's not patched. And as long as Dort has access to Badbox, they would be able to load" the Kimwolf malware directly onto TV boxes associated with Badbox 2.0.

The source said it isn't clear how Dort gained access to the Badbox botnet panel. But it's unlikely that Dort's existing account will persist for much longer: All of our notifications to the qq.com email addresses listed in the control panel screenshot received a copy of that image, as well as questions about the apparently rogue ABCD account.

_This entry was posted on Monday 26th of January 2026 11:11 AM_

[Breadcrumbs](https://krebsonsecurity.com/category/breadcrumbs/) [Internet of Things (IoT)](https://krebsonsecurity.com/category/internet-of-things-iot/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[18681627767](https://krebsonsecurity.com/tag/18681627767/) [189308024@qq.com](https://krebsonsecurity.com/tag/189308024qq-com/) [34557257@qq.com](https://krebsonsecurity.com/tag/34557257qq-com/) [BadBox 2.0](https://krebsonsecurity.com/tag/badbox-2-0/) [Beijing Astrolink Wireless Digital Technology Co. Ltd](https://krebsonsecurity.com/tag/beijing-astrolink-wireless-digital-technology-co-ltd/) [Beijing Hengchuang Vision Mobile Media Technology Co. Ltd.](https://krebsonsecurity.com/tag/beijing-hengchuang-vision-mobile-media-technology-co-ltd/) [Beijing Hong Dake Wang Science & Technology Co Ltd.](https://krebsonsecurity.com/tag/beijing-hong-dake-wang-science-technology-co-ltd/) [cathead@gmail.com](https://krebsonsecurity.com/tag/catheadgmail-com/) [Chen Daihai](https://krebsonsecurity.com/tag/chen-daihai/) [Constella Intelligence](https://krebsonsecurity.com/tag/constella-intelligence/) [daihaic@gmail.com](https://krebsonsecurity.com/tag/daihaicgmail-com/) [Dort](https://krebsonsecurity.com/tag/dort/) [Federal Bureau of Investigation](https://krebsonsecurity.com/tag/federal-bureau-of-investigation/) [Guilin Huang](https://krebsonsecurity.com/tag/guilin-huang/) [HUMAN Security](https://krebsonsecurity.com/tag/human-security/) [Moxin Beijing Science and Technology Co. Ltd.](https://krebsonsecurity.com/tag/moxin-beijing-science-and-technology-co-ltd/) [osint.industries](https://krebsonsecurity.com/tag/osint-industries/) [residential proxies](https://krebsonsecurity.com/tag/residential-proxies/) [Snow](https://krebsonsecurity.com/tag/snow/) [SpyCloud](https://krebsonsecurity.com/tag/spycloud/) [xavierzhu@gmail.com](https://krebsonsecurity.com/tag/xavierzhugmail-com/) [xavierzhu@qq.com](https://krebsonsecurity.com/tag/xavierzhuqq-com/) [Zhu Zhiyu](https://krebsonsecurity.com/tag/zhu-zhiyu/) [桂林 黄](https://krebsonsecurity.com/tag/%e6%a1%82%e6%9e%97-%e9%bb%84/) [陈代海](https://krebsonsecurity.com/tag/%e9%99%88%e4%bb%a3%e6%b5%b7/)

  


Post navigation

[<- Kimwolf Botnet Lurking in Corporate, Govt. Networks](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/) [Please Don't Feed the Scattered Lapsus ShinyHunters ->](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/)

##  15 thoughts on "Who Operates the Badbox 2.0 Botnet?"

  1. Curios [January 26, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650443)

What does the column 3rd from right say, is that when the account was created? If so, surely the caohuiming user (that is an admin) would have seen this ABCD rouge account there?

Also, on the top right it shows that ABCD is logged in. Did he share this picture with you or did he for some reason share it with your source who then shared it with you?

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650443#respond) ->

     1. inelectubale doom [January 30, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650504)

Maybe ABCD just forgot he was a bluebox.

So, so close to homemade… but no lumps.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650504#respond) ->

  2. Cary Carter [January 26, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650444)

Hey krebbs, we literally setup that trail for you to follow. I'm glad you're having fun though hun, you're welcome for the career 🙂

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650444#respond) ->

     1. mealy [January 27, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650451)

You literally are a convincing spelling champ too bud.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650451#respond) ->

     2. ineluctable doom [January 30, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650505)

Krebs is still sore he didn't break the curse of the bambino.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650505#respond) ->

  3. shawnb [January 27, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650462)

One of the underreported aspects of this is the impact on small site owners. Small businesses, forums (yep they're still around), neighborhood & club sites, etc., are facing dramatically increased crawl activity from these botnets. Not easily blocked, because their IPs are all over the place. 

This blew up in July-Oct 2025 (mostly BR & VN), subsided a bit, but I'm still seeing at least 3x normal crawl rate from rando bots (lots of CN, though it varies by week/month…). Not uncommon to have hundreds of thousands of queries across hundreds of thousands of IPs. Yep, most with one hit per IP. 

Many smaller sites that are having a hard time staying afloat. They just don't have the technical skills or budget to keep their sites up. Simple things - railroad fan sites, personal photography sites, guitar fx junkies, antique woodworking tools, small gaming sites. Twenty years ago they all opened up sites on various ISPs. Little labors of love all over the internet.

Small sites are shutting down, leaving the monoliths, making the internet increasingly less democratic & diverse. Of course they could bump up to hosting plans with greater support, but most are running on shoestring budgets & cannot afford to do that. 

Many are resorting to Cloudflare, which, TBH, to me, introduces privacy concerns, especially in the long run. Also it feels a bit too much like racketeering… And I occasionally see the bad guys acting from behind CF.

It's becoming all big guys, bad guys, & bots.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650462#respond) ->

     1. BigP [January 27, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650464)

I'm currently looking into Tollbit to monetize AI scraping traffic. Apparently it's free, and gives the AI a paywall. They also partner with HUMAN which is mentioned in the article. Hopefully it doesn't block "good" bots or normal user bots.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650464#respond) ->

     2. Nerdy Fi [January 28, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650478)

Yeah, this kind of behavior is what killed a minivan forum that was beloved by hundreds (it was very niche so smaller impact, but painful for all) and is unforgivable. These wretches will have their day, they just don't know it yet and think it won't matter when it's hammer time.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650478#respond) ->

  4. tomoko kuroki [January 27, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650463)

it saddens me to see thousands of bots used for mundane things like ddos or scraping your grandma's wordpress blog. imagine if they were all tor nodes. imagine if they were part of i2p. imagine if they were seeding books and powering peertube. instead some loser gets off by taking down minecraft servers for minutes at a time and some techbro redownloads every git commit from some forgejo for the 6 billionth time.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650463#respond) ->

  5. Wanderer [January 27, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650466)

What has been missed in many of these stories is how many android TV box's get the infected firmware.

Various forums have people who create custom firmware's for the android box's mostly for fun but some criminals create infected versions and offer them on the forums. It might be offered as a better working firmware than what comes with the box or often its a newer android version. Manufacturers or suppliers of some android TV box clones based on Amlogic, Allwinner, Rockchip etc SoC use them. If you can say your version of a T95 has a newer android version than another clone, it makes that firmware desirable for sellers who have no idea its infected or has a dropper on it.

Its the same on forums that have custom firmwares for generic tablets. They get offered as firmwares that will pretend to have more RAM and storage space so sellers can sell for more than the hardware is worth. The sellers are criminals themselves but not usually aware the firmware offered is also infected

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650466#respond) ->

  6. Sergey Shevtchenko [January 28, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650481)

Hi Brian! This article did not post to your RSS feed, just FYI. If you've discontinued it, please let us know!

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650481#respond) ->

  7. Shahraw [January 28, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650483)

What’s interesting to me is how much of this becomes an ecosystem problem rather than a pure malware one. Once control infrastructure and device fleets persist for years, the resulting traffic patterns start to look like background internet noise. Thousands of IPs, minimal requests, constantly shifting geography. That’s where smaller operators get hurt.

Large platforms absorb it. Small, independently run sites don’t. They either move behind intermediaries, accept degraded functionality, or shut down entirely.

I first started thinking about this framing after reading a few posts on long lived infrastructure and domain reuse on the SafeAeon blog at <https://safeaeon.com/>  
. It helped connect how botnets like this don’t just enable fraud, but quietly raise the cost of staying online for everyone else.

The technical details here are important, but the second order effects feel just as consequential.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650483#respond) ->

  8. Russ [January 28, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650486)

From the WSJ…

Google Aims Knockout Blow at Chinese Company Linked to Massive Cyber Weapon  
Company targets global network employed by hackers that often use devices running in homes of everyday Americans

Paywall  
<https://www.wsj.com/tech/google-aims-knockout-blow-at-chinese-company-linked-to-massive-cyber-weapon-3c3fdc40>

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650486#respond) ->

     1. Dan [January 29, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650492)

Not good that the headline emphasises that the company is foreign, especially considering that most of what we know about this botnet comes from a Chinese security research firm

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650492#respond) ->

        1. mealy [January 30, 2026](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/#comment-650502)

Actually? It says it's a Chinese company… one time… because -wait for it- that's where the company is based. It's a pretty obvious datapoint to denote about a company. Calling it "foreign" would be less informative and much more weirdly antagonistic. Also I see nothing from any Chinese security research firm on this article. 

Don't let Xi's good looks dissuade you from calling out "Chinese" threat actors, that's just silly.

[Reply](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/?replytocom=650502#respond) ->




### Leave a Reply [Cancel reply](/2026/01/who-operates-the-badbox-2-0-botnet/#respond)

Your email address will not be published. Required fields are marked *

Comment *

Name *

Email *

Website

Δ

Advertisement

[ ![](/b-ninjio/6.png) ](https://ninjio.com/lp46d-krebs/)

  


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

