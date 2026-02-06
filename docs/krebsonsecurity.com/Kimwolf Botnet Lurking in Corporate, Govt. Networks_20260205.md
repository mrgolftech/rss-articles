# Kimwolf Botnet Lurking in Corporate, Govt. Networks

**来源:** https://krebsonsecurity.com
**链接:** https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/
**日期:** Tue, 20 Jan 2026 18:19:13 +0000

---

Advertisement

[ ![](/b-ninjio/9.png) ](https://ninjio.com/lp46d-krebs/)

Advertisement

[ ![](/b-knowbe4/45.png) ](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

[__](http://twitter.com/briankrebs)[__](https://krebsonsecurity.com/feed/)[__](https://www.linkedin.com/in/bkrebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[__](http://twitter.com/briankrebs)[__](https://krebsonsecurity.com/feed/)[__](https://www.linkedin.com/in/bkrebs/)

Skip to content

  * [Home](https://krebsonsecurity.com/)
  * [About the Author](https://krebsonsecurity.com/about/)
  * [Advertising/Speaking](https://krebsonsecurity.com/cpm/)



# Kimwolf Botnet Lurking in Corporate, Govt. Networks

January 20, 2026

[15 Comments](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comments)

A new Internet-of-Things (IoT) botnet called **Kimwolf** has spread to more than 2 million devices, forcing infected systems to participate in massive distributed denial-of-service (DDoS) attacks and to relay other malicious and abusive Internet traffic. Kimwolf's ability to scan the local networks of compromised systems for other IoT devices to infect makes it a sobering threat to organizations, and new research reveals Kimwolf is surprisingly prevalent in government and corporate networks.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/ss-botnet.png)

Image: Shutterstock, @Elzicon.

Kimwolf grew rapidly in the waning months of 2025 by tricking various "residential proxy" services into relaying malicious commands to devices on the local networks of those proxy endpoints. Residential proxies are sold as a way to anonymize and localize one's Web traffic to a specific region, and the biggest of these services allow customers to route their Internet activity through devices in virtually any country or city around the globe.

The malware that turns one's Internet connection into a proxy node is often quietly bundled with various mobile apps and games, and it typically forces the infected device to relay malicious and abusive traffic -- including ad fraud, account takeover attempts, and mass content-scraping.

Kimwolf mainly targeted proxies from **IPIDEA** , a Chinese service that has millions of proxy endpoints for rent on any given week. The Kimwolf operators discovered they could [forward malicious commands](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) to the internal networks of IPIDEA proxy endpoints, and then programmatically scan for and infect other vulnerable devices on each endpoint's local network.

Most of the systems compromised through Kimwolf's local network scanning have been unofficial Android TV streaming boxes. These are typically Android Open Source Project devices -- not Android TV OS devices or Play Protect certified Android devices -- and they are generally marketed as a way to watch unlimited (read:pirated) video content from popular subscription streaming services for a one-time fee.

However, a great many of these TV boxes ship to consumers with residential proxy software pre-installed. What's more, they have no real security or authentication built-in: If you can communicate directly with the TV box, you can also easily compromise it with malware.

While IPIDEA and other affected proxy providers recently have taken steps to block threats like Kimwolf from going upstream into their endpoints (reportedly with varying degrees of success), the Kimwolf malware remains on millions of infected devices.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/ipidea2023.png)

A screenshot of IPIDEA's proxy service.

Kimwolf's close association with residential proxy networks and compromised Android TV boxes might suggest we'd find relatively few infections on corporate networks. However, the security firm **Infoblox** said a recent review of its customer traffic found _nearly 25 percent of them made a query to a Kimwolf-related domain name since October 1, 2025_ , when the botnet first showed signs of life.

Infoblox found the affected customers are based all over the world and in a wide range of industry verticals, from education and healthcare to government and finance.

"To be clear, this suggests that nearly 25% of customers had at least one device that was an endpoint in a residential proxy service targeted by Kimwolf operators," Infoblox [explained](https://www.infoblox.com/blog/threat-intelligence/kimwolf-howls-from-inside-the-enterprise/). "Such a device, maybe a phone or a laptop, was essentially co-opted by the threat actor to probe the local network for vulnerable devices. A query means a scan was made, not that new devices were compromised. Lateral movement would fail if there were no vulnerable devices to be found or if the DNS resolution was blocked."

**Synthient** , a startup that tracks proxy services and was [the first to disclose on January 2](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) the unique methods Kimwolf uses to spread, found proxy endpoints from IPIDEA were present in alarming numbers at government and academic institutions worldwide. Synthient said it spied at least 33,000 affected Internet addresses at universities and colleges, and nearly 8,000 IPIDEA proxies within various U.S. and foreign government networks.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/top50targetedomains.jpeg)

The top 50 domain names sought out by users of IPIDEA's residential proxy service, according to Synthient.

In a webinar on January 16, experts at the proxy tracking service **Spur** profiled Internet addresses associated with IPIDEA and 10 other proxy services that were thought to be vulnerable to Kimwolf's tricks. Spur found residential proxies in nearly 300 government owned and operated networks, 318 utility companies, 166 healthcare companies or hospitals, and 141 companies in banking and finance.

"I looked at the 298 [government] owned and operated [networks], and so many of them were DoD [U.S. Department of Defense], which is kind of terrifying that DoD has IPIDEA and these other proxy services located inside of it," Spur Co-Founder **Riley Kilmer** said. "I don't know how these enterprises have these networks set up. It could be that [infected devices] are segregated on the network, that even if you had local access it doesn't really mean much. However, it's something to be aware of. If a device goes in, anything that device has access to the proxy would have access to."

Kilmer said Kimwolf demonstrates how a single residential proxy infection can quickly lead to bigger problems for organizations that are harboring unsecured devices behind their firewalls, noting that proxy services present a potentially simple way for attackers to probe other devices on the local network of a targeted organization.

"If you know you have [proxy] infections that are located in a company, you can chose that [network] to come out of and then locally pivot," Kilmer said. "If you have an idea of where to start or look, now you have a foothold in a company or an enterprise based on just that."

This is the third story in our series on the Kimwolf botnet. Next week, we'll shed light on the myriad China-based individuals and companies connected to the [**Badbox 2.0 botnet**](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/), the collective name given to [a vast number of Android TV streaming box models](https://github.com/synthient/public-research/blob/main/2026/01/kimwolf/product_devices.csv) that ship with no discernible security or authentication built-in, and with residential proxy malware pre-installed.

Further reading:

[The Kimwolf Botnet is Stalking Your Local Network](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/)

[Who Benefitted from the Aisuru and Kimwolf Botnets?](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/)

[A Broken System Fueling Botnets](https://synthient.com/blog/a-broken-system-fueling-botnets) (Synthient).

_This entry was posted on Tuesday 20th of January 2026 01:19 PM_

[DDoS-for-Hire](https://krebsonsecurity.com/category/ddos-for-hire/) [Internet of Things (IoT)](https://krebsonsecurity.com/category/internet-of-things-iot/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[BadBox 2.0](https://krebsonsecurity.com/tag/badbox-2-0/) [Infoblox](https://krebsonsecurity.com/tag/infoblox/) [IPidea](https://krebsonsecurity.com/tag/ipidea/) [Kimwolf](https://krebsonsecurity.com/tag/kimwolf/) [residential proxies](https://krebsonsecurity.com/tag/residential-proxies/) [Riley Kilmer](https://krebsonsecurity.com/tag/riley-kilmer/) [Spur](https://krebsonsecurity.com/tag/spur/) [Synthient](https://krebsonsecurity.com/tag/synthient/)

  


Post navigation

[<- Patch Tuesday, January 2026 Edition](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/) [Who Operates the Badbox 2.0 Botnet? ->](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/)

##  15 thoughts on "Kimwolf Botnet Lurking in Corporate, Govt. Networks"

  1. krebs fan no. 1 [January 20, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650360)

we love you krebby

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650360#respond) ->

  2. WENQIANG MA [January 20, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650361)

Why is this largely identical to the January 8 post?

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650361#respond) ->

     1. JB [January 20, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650369)

Its actually very different, but each article has to have some sort of explanation of kimwolf so that the article makes sense if you haven't read the other article(s).

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650369#respond) ->

  3. Tim [January 20, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650363)

Wow this is scary

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650363#respond) ->

  4. Will Chen [January 21, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650373)

Just a reminder that Dort, the individual allegedly running this, lost clash of code to a known paster: <https://youtu.be/yntHEanT3u8> and then failed to  
make a google account

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650373#respond) ->

  5. bob [January 21, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650374)

“I looked at the 298 [government] owned and operated [networks], and so many of them were DoD [U.S. Department of Defense], which is kind of terrifying that DoD has IPIDEA and these other proxy services located inside of it,” Spur Co-Founder Riley Kilmer said.“

No doubt unofficial Android TV streaming boxes connected to every television in every DoD facility in the universe, all broadcasting Fox News.

Meanwhile Pentagon Pete does jumping jacks.

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650374#respond) ->

     1. Jon Marcus [January 22, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650388)

Yeah, wondered if it might be something like that. Or families living on post?

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650388#respond) ->

  6. Harpy [January 21, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650378)

What a time to be alive

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650378#respond) ->

     1. ineluctable doom [January 30, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650508)

Might be an even better time to not be, I suppose!

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650508#respond) ->

  7. Fr00tL00ps [January 22, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650385)

Testing, testing. 1 2 3.

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650385#respond) ->

     1. ramalamadingdong [January 30, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650511)

Footlong tuna! Three years ago! Subway line thousands of miles away! 6 7 8!

All the same!

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650511#respond) ->

  8. Not Jana Eva [January 23, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650397)

Seems third world crypto scammers have figured that Krebs' comment section is an excellent place for their testimonies on how they recovered "loosed" coins via a helpful gmail address…..

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650397#respond) ->

     1. mealy [January 27, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650453)

I found lost pokemon cards by following the helpful advice at lostpokemoncards.ir irl.  
Big windfalls, no downsides, security always, just click now. Be a millionaire!

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650453#respond) ->

        1. ineluctable doom [January 30, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650509)

Magic the Gathering dude just died. Guess he picked the wrong card game/Albertson's hat 26ish years ago.

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650509#respond) ->

  9. Vincent L [January 23, 2026](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#comment-650398)

That Spur[.]us presentation was great!

I wonder if journalists and others covering this matter should or are aware of the Spur's /context/me URL, which could be handy to include articles to help bring awareness to infected devices, the same way haveibeenpwned has been liberally tossed around.

[Reply](https://krebsonsecurity.com/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/?replytocom=650398#respond) ->




### Leave a Reply [Cancel reply](/2026/01/kimwolf-botnet-lurking-in-corporate-govt-networks/#respond)

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

