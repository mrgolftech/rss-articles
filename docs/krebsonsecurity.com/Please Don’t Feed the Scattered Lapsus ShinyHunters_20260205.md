# Please Don’t Feed the Scattered Lapsus ShinyHunters

**来源:** https://krebsonsecurity.com
**链接:** https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/
**日期:** Mon, 02 Feb 2026 16:15:16 +0000

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



# Please Don't Feed the Scattered Lapsus ShinyHunters

February 2, 2026

[13 Comments](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comments)

A prolific data ransom gang that calls itself **Scattered Lapsus ShinyHunters** (SLSH) has a distinctive playbook when it seeks to extort payment from victim firms: Harassing, threatening and even swatting executives and their families, all while notifying journalists and regulators about the extent of the intrusion. Some victims reportedly are paying -- perhaps as much to contain the stolen data as to stop the escalating personal attacks. But a top SLSH expert warns that engaging at all beyond a "We're not paying" response only encourages further harassment, noting that the group's fractious and unreliable history means the only winning move is not to pay.

![](https://krebsonsecurity.com/wp-content/uploads/2026/02/dontfeed.png)

Image: Shutterstock.com, @Mungujakisa

Unlike traditional, highly regimented Russia-based ransomware affiliate groups, SLSH is an unruly and somewhat fluid English-language extortion gang that appears uninterested in building a reputation of consistent behavior whereby victims might have some measure of confidence that the criminals will keep their word if paid.

That's according to **Allison Nixon** , director of research at the New York City based security consultancy [Unit 221B](https://unit221b.com). Nixon has been closely tracking the criminal group and individual members as they bounce between various Telegram channels used to extort and harass victims, and she said SLSH differs from traditional data ransom groups in other important ways that argue against trusting them to do anything they say they'll do -- such as destroying stolen data.

Like SLSH, many traditional Russian ransomware groups have employed high-pressure tactics to force payment in exchange for a decryption key and/or a promise to delete stolen data, such as publishing a dark web shaming blog with samples of stolen data next to a countdown clock, or notifying journalists and board members of the victim company. But Nixon said the extortion from SLSH quickly escalates way beyond that -- to threats of physical violence against executives and their families, DDoS attacks on the victim's website, and repeated email-flooding campaigns.

SLSH is known for breaking into companies by phishing employees over the phone, and using the purloined access to steal sensitive internal data. In [a January 30 blog post](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft), Google's security forensics firm **Mandiant** said SLSH's most recent extortion attacks stem from incidents spanning early to mid-January 2026, when SLSH members pretended to be IT staff and called employees at targeted victim organizations claiming that the company was updating MFA settings.

"The threat actor directed the employees to victim-branded credential harvesting sites to capture their SSO credentials and MFA codes, and then registered their own device for MFA," the blog post explained.

Victims often first learn of the breach when their brand name is uttered on whatever ephemeral new public Telegram group chat SLSH is using to threaten, extort and harass their prey. According to Nixon, the coordinated harassment on the SLSH Telegram channels is part of a well-orchestrated strategy to overwhelm the victim organization by manufacturing humiliation that pushes them over the threshold to pay.

Nixon said multiple executives at targeted organizations have been subject to "swatting" attacks, wherein SLSH communicated a phony bomb threat or hostage situation at the target's address in the hopes of eliciting a heavily armed police response at their home or place of work.

"A big part of what they're doing to victims is the psychological aspect of it, like harassing executives' kids and threatening the board of the company," Nixon told KrebsOnSecurity. "And while these victims are getting extortion demands, they're simultaneously getting outreach from media outlets saying, 'Hey, do you have any comments on the bad things we're going to write about you."

In [a blog post today](https://blog.unit221b.com/dont-read-this-blog/harassment-scare-tactics-why-victims-should-never-pay-shinyhunters), Unit 221B argues that no one should negotiate with SLSH because the group has demonstrated a willingness to extort victims based on promises that it has no intention to keep. Nixon points out that all of SLSH's known members hail from **The Com** , shorthand for a constellation of cybercrime-focused Discord and Telegram communities which serve as a kind of [distributed social network that facilitates instant collaboration](https://krebsonsecurity.com/2024/09/the-dark-nexus-between-harm-groups-and-the-com/).

Nixon said Com-based extortion groups tend to instigate feuds and drama between group members, leading to lying, betrayals, credibility destroying behavior, backstabbing, and sabotaging each other.

"With this type of ongoing dysfunction, often compounding by substance abuse, these threat actors often aren’t able to act with the core goal in mind of completing a successful, strategic ransom operation," Nixon wrote. "They continually lose control with outbursts that put their strategy and operational security at risk, which severely limits their ability to build a professional, scalable, and sophisticated criminal organization network for continued successful ransoms - unlike other, more tenured and professional criminal organizations focused on ransomware alone."

Intrusions from established ransomware groups typically center around encryption/decryption malware that mostly stays on the affected machine. In contrast, Nixon said, ransom from a Com group is often structured the same as violent sextortion schemes against minors, wherein members of The Com will steal damaging information, threaten to release it, and "promise" to delete it if the victim complies without any guarantee or technical proof point that they will keep their word. She writes:

A key component of SLSH's efforts to convince victims to pay, Nixon said, involves manipulating the media into hyping the threat posed by this group. This approach also borrows a page from the playbook of sextortion attacks, she said, which encourages predators to keep targets continuously engaged and worrying about the consequences of non-compliance.

"On days where SLSH had no substantial criminal ‘win’ to announce, they focused on announcing death threats and harassment to keep law enforcement, journalists, and cybercrime industry professionals focused on this group," she said.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/02/comtutsh.png)](https://krebsonsecurity.com/wp-content/uploads/2026/02/comtutsh.png)

An excerpt from a sextortion tutorial from a Com-based Telegram channel. Image: Unit 221B.

Nixon knows a thing or two about being threatened by SLSH: For the past several months, the group's Telegram channels have been replete with threats of physical violence against her, against Yours Truly, and against other security researchers. These threats, she said, are just another way the group seeks to generate media attention and achieve a veneer of credibility, but they are useful as indicators of compromise because SLSH members tend to name drop and malign security researchers even in their communications with victims.

"Watch for the following behaviors in their communications to you or their public statements," Unit 221B's advisory reads. "Repeated abusive mentions of Allison Nixon (or "A.N"), Unit 221B, or cybersecurity journalists—especially Brian Krebs—or any other cybersecurity employee, or cybersecurity company. Any threats to kill, or commit terrorism, or violence against internal employees, cybersecurity employees, investigators, and journalists."

Unit 221B says that while the pressure campaign during an extortion attempt may be traumatizing to employees, executives, and their family members, entering into drawn-out negotiations with SLSH incentivizes the group to increase the level of harm and risk, which could include the physical safety of employees and their families.

"The breached data will never go back to the way it was, but we can assure you that the harassment will end," Nixon said. "So, your decision to pay should be a separate issue from the harassment. We believe that when you separate these issues, you will objectively see that the best course of action to protect your interests, in both the short and long term, is to refuse payment."

_This entry was posted on Monday 2nd of February 2026 11:15 AM_

[Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Ransomware](https://krebsonsecurity.com/category/ransomware/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Allison Nixon](https://krebsonsecurity.com/tag/allison-nixon/) [Mandiant](https://krebsonsecurity.com/tag/mandiant/) [Scattered Lapsus Shiny Hunters](https://krebsonsecurity.com/tag/scattered-lapsus-shiny-hunters/) [sextortion](https://krebsonsecurity.com/tag/sextortion/) [SLSH](https://krebsonsecurity.com/tag/slsh/) [Unit 221](https://krebsonsecurity.com/tag/unit-221/)

  


Post navigation

[<- Who Operates the Badbox 2.0 Botnet?](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/)

##  13 thoughts on "Please Don't Feed the Scattered Lapsus ShinyHunters"

  1. Jay [February 2, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650545)

Re: :…all while notifying journalists and regulators about the extent of the intrusion",  
The article does not name any journalist or media entity which has published any of of the attack data. Nor have the researchers recommended in the article any cautions that should be going to such media so the media can be schooled in how to exercise restraint against being co-opted into furthering these attacks.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650545#respond) ->

  2. Seashells by the seashore [February 2, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650553)

This is another fascinating article by Mr. Krebs, conflating an actual extortion attempt by a large, quasi-organized group of executives and fine 'business institutions' (some of the very same upstanding people involved in the Ashley Madison, Panama papers and Paradise papers 'leaks', among others) with these folks.

But Mr. Krebs and his ilk do not like actual rabbit holes (I am averse to the term 'warren'), only things that fit his/their narrative(s). It is kind of a pity; for a short while, about a year and a half or so ago, I thought maybe he had turned a new leaf.

Folks like Phineas and myself know better.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650553#respond) ->

  3. [Admirer](http://JTR.com) [February 2, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650557)

This was an interesting read. Although I would like to say a few things because it doesn't seem like you know how this works.

Advising victims not to pay is reasonable. Everyone has done this historically, even law enforcement. But we know a lot of companies give in, or they used to, not as much anymore.

Asserting or implying that this specific group (SLSH/SLH or ShinyHunters, ShinyHunters seems like a completely different group btw) habitually breaks agreements requires evidence that hasn't been publicly shown.

As a piece of genuine advice, before you make articles like these the best way to do it is provide evidence, back up your claims. 

Do you remember when the NCA and FBI shut down Lockbit in 2024? Do you remember how they did it? They clearly showed that Lockbit is not trustable. Look at Lockbit now… dead… and they probably don't make any money.

What you are doing here isn't wrong but rather incorrect. I sincerely hope you don't take this critism the wrong way, just my two cents.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650557#respond) ->

     1. Sergi Tolstoy [February 3, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650564)

Like 5 vents, imo

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650564#respond) ->

  4. John Wilks Booth [February 3, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650565)

are they ddos-ing your site?

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650565#respond) ->

  5. cleaning [February 3, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650567)

The winning move isn't to 'not play', because that just encourages further attacks just as much as responding in the first place. Life isn't wargames unfortunately.

Articles like THIS, which continue to mention them by name are their fuel. Because the articles don't stop, the ransom, extortion, beatings, underage children being groomed into becoming callers, etc, won't stop, it's a parasitic relationship.

To continue the silly chess analogies, journalists are used as pawns (a tale as old as time). The winning move is to remove all coverage and refuse all coverage, but journalists don't want that, they want clicks, that's what their livelihood depends on, and there's no sense with one independent journalist refusing to cover when 25 other massive publications will write about the weekly ransom, even if it's a mom and pop shop ISP servicing 350 customers.  
Even if by some miracle, every single cybersecurity journalist stopped, all it takes is one or a few "independents" or twitter accounts to tweet it, get a few thousand likes, and it's back to the beginning. These groups don't care WHO writes, just as long as it gets written.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650567#respond) ->

     1. ramalamadingdong [February 4, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650579)

It seems to me that 'these groups' (or, anyway, only quasi-organized groups of people barely loosely in communication, from what I can make out) aren't that interested in being written about (this isn't a decade or two ago). It is conceivable, though, that articles like this do encourage some people to seek 'people like this' out.

I haven't really figured out the exact motive for these guys. It doesn't seem to be fame, or money (despite whatever requests they make; they don't seem to be spending it, or fleeing), or political. The people that have been arrested and are awaiting whatever the justice department decides to do with their cases, however loosely related they are to one another or this 'group', had the means to flee, and yet did not.

Maybe they are merely young, simply bored, and just wanted to see what they could get away with.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650579#respond) ->

     2. JB [February 4, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650581)

The single largest goad to making companies secure PII is being revealed publicly to have not protected it. Otherwise many companies would only bother to secure operations against encryption ransoming (and then would probably get encrypted anyway because of allowing easier access, more persistence and more lateral movement).

Its massively advantageous to the consumer that the companies get named and shamed.

Incidentally these articles are extremely helpful for me to explain to my execs how someone that has access to your inside data will probably not go away until they extract as much value as they can, ie its not a mastercard expense, its as much money as they can extract.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650581#respond) ->

        1. ramalamadingdong [February 4, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650582)

I don't think it is ever advantageous to any given consumer for a company they want to trust to be named and shamed by a 'breach' or leak unless the goal is to expose actual, unethical, illegal and/or illicit activity that affects the consumer.

Perhaps some of the companies being 'named and shamed' are really guilty of other, actual, deliberate crimes (or perhaps totally other companies are guilty of those malfeasances and the 'leakers' are merely frustrated and attempting to encourage someone with the proper access to expose a deeper corporate malfeasance, who knows?).

What is it about the impropriety of people exposing the possibility of doing large extractions of personally identifying data is so difficult for people to accept or understand? Are they all just seeking some sorta schafefreude for making everyone as vulnerable as people in something like the old breaches like RockYou and whatever that are included in every Kali DVD? Do you wanna be a member of a 'club' like that?

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650582#respond) ->

           1. ramalamadingdong [February 4, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650583)

schadenfreude, that is.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650583#respond) ->

  6. Will Smith [February 3, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650569)

This post does a great job explaining how fragmented groups like Scattered Lapsus ShinyHunters thrive on attention and panic. The reminder not to amplify unverified claims or reward extortion tactics is important, especially as these actors rely more on noise than real impact.

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650569#respond) ->

  7. job [February 4, 2026](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#comment-650576)

job where?

[Reply](https://krebsonsecurity.com/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/?replytocom=650576#respond) ->




### Leave a Reply [Cancel reply](/2026/02/please-dont-feed-the-scattered-lapsus-shiny-hunters/#respond)

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

