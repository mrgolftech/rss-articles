# Practical Defenses Against Technofascism

**来源:** https://micahflee.com
**链接:** https://micahflee.com/practical-defenses-against-technofascism/
**日期:** Sun, 26 Oct 2025 03:57:00 GMT

---

[ ![micahflee](https://micahflee.com/content/images/2025/02/programming-1.png) ](https://micahflee.com)

  * [Blog](https://micahflee.com/)
  * [About](https://micahflee.com/about/)
  * [Contact](https://micahflee.com/contact/)
  * [Lockdown Systems](https://lockdown.systems/)
  * [Cyd](https://cyd.social/)
  * [Hacks & Leaks](https://hacksandleaks.com/)



Sign in Subscribe

# Practical Defenses Against Technofascism

![Practical Defenses Against Technofascism](/content/images/size/w1200/2025/10/slide-000.png)

I gave the Saturday morning keynote at BSidesPDX! I spoke honestly and frankly about the terrifying reality that Americans are facing under Trump's fascist regime, alongside practical advice for communities to defend themselves.

Watch my talk below. Of if you prefer reading articles over watching video, I've added a copy of my whole talk below the video, mildly edited, and with added links to my sources.

## Sign up for micahflee

Hi, I'm Micah. I help journalists, researchers, and activists stay safe and productive.

Subscribe

Email sent! Check your inbox to complete your signup. 

No spam. Unsubscribe anytime.

Good morning, BSides Portland! I’ve worked in journalism for over a decade, but this is the first time I’ve traveled to an **active war zone**!

It’s hard to believe that we’re not even one year into Trump’s fascist takeover of the government. The onslaught of horrifying news is happening too fast to keep track of. But what’s clear to me is that the Trump administration, and ICE in particular, is tooling up for technological repression that Americans have _never_ been subject to before.

Today I’ll go over the disturbing signs of the coming Age of Technofascism, along with practical ways to defend yourself and your communities against it.

I’m Micah Lee. I’m an independent security researcher, a journalist, and a software engineer. I spent the last decade and a half reporting on classified documents, helping journalists protect their sources, building open-source privacy tools, and teaching people how to analyze leaked datasets. These days, I work closely with journalists, researchers, and activists, doing what I can to keep them safe and productive.

The views I’m expressing in this talk are entirely my own, and not the views of any of the organizations that I work with.

# Technofascism

Since Trump’s inauguration, the US has slid into **technofascism**.

Fascism is a slippery ideology that’s difficult to define. Sometimes it borrows from conservatives, or from liberals, or even from Leftists. But in the end, none of those beliefs are genuine. It’s all about accumulating _unlimited power_ for an in-group, at the expense of _everyone else_.

💡

****fascism**** (noun)  
Imperialism turned inward.

One common definition of fascism is “imperialism turned inward.”

Here's a bit of recent US imperialism history, since September 11, 2001:

  * We launched **wars of aggression** , based on lies, in Afghanistan and Iraq.
  * We ran a **covert torture program** , and **imprisoned and tortured innocent people for decades** at Guantanamo Bay.
  * We built a **global surveillance system** and spied on _entire populations_ , all without probable cause.
  * We ran a massive **drone assassination program** , bombing wedding across the Middle East and Africa in countries we weren't at war with, in the name of American freedom.
  * Right now, we’re **funding and arming Israel while it commits genocide in Gaza**.



Huge swaths of the world are subjected to intense state repression, violence, surveillance, and censorship. In many places, this repression is explicitly supported by the US government and by US companies.

The thing that makes the Trump era different is _fascism_. Under Trump, this complete disregard for human rights is now pointed _inward_ , at the “enemies within,” as Trump calls Americans he doesn’t like.

What we’ve been seeing on the streets of the US, with ICE kidnappings and military invasions of cities, is the normal American disregard for human rights, but this time turned inward, _targeted against us_.

💡

****technofascism**** (noun)  
A form of fascism that uses modern technologies to attain its ends.

And the American tech industry is totally on board with it.

  * Elon Musk, the richest and **most divorced** person in the world, donated hundreds of millions of dollars to make sure Trump got elected. He then bought Twitter and turned it into X, a cesspool of propaganda, disinformation, and hate.
  * Mark Zuckerberg got a haircut, went on Joe Rogan, and shut down Meta’s _diversity_ program.
  * Jeff Bezos, owner of Amazon and the Washington Post, _personally_ intervened to prevent the Post from endorsing Kamala Harris, and he restructured its opinion page to make it _friendly to fascism_.
  * Tim Cook _personally donated one million dollars_ to Trump’s inauguration committee.



You know how right now, while the government is shut down and food stamps for millions of Americans are set to expire one week from now, Trump is tearing down the East Wing of the White House to build himself a privately funded ballroom? Some of the companies who are funding Trump’s ballroom include: Amazon, Apple, Coinbase, Google, Meta, and Microsoft.

This talk _mostly_ isn’t about reactionary tech billionaires and their complicit companies. Instead, it’s about attacks that we should be prepared for during this Age of Technofascism, and ways we can defend against them.

In this talk, I’m going to try to give some specific, actionable advise about three three topics: mercenary spyware, device searches, and app censorship.

But don’t think of this as a checklist that all you have to do is finish and then you’re good. Ultimately, what we all need to do, is build an intentional and forgiving **security culture**. These are things to talk over with your friends, colleagues, and family members as shared practices. 

Fascists are targeting _everyone_ outside their in-group. If we want to keep our communities safe, our defenses need to be **collective** , not individual.

I also want to warn you that this talk is pretty intense. So, just to lighten the mood a bit, I’m going to wear some frog eyes.

![](https://micahflee.com/content/images/2025/10/vlcsnap-2025-10-25-17h23m14s422.png)This is when I put on the frog eyes, though I accidentally called them "frog ears"

I’m not going to sugarcoat the awful reality of our current situation. But, at least I’ll be somewhat dressed up like a frog while I’m giving you all anxiety.

# Mercenary Spyware

It used to be that government spy agencies, like the NSA, developed the most sophisticated hacking tools in the world in-house. But over the last decade or so, this has shifted to the private sector.

Now, private companies make the world’s most sophisticated hacking tools. And they sell them basically as _subscription services_ to government agencies and police departments around the world, many of which would _never_ have been able to build these capabilities in-house themselves.

![](https://micahflee.com/content/images/2025/10/slide-009.png)Forbidden Stories: [About the Pegasus Project](https://forbiddenstories.org/about-the-pegasus-project/)

Americans have been largely shielded from this type of attack.

  * NSO Group’s Pegasus spyware is typically configured to not be able to target US phone numbers (though, they could easily disable this setting if they decide to target US phone numbers).
  * Mercenary spyware firms are on US sanctions lists.
  * And in 2023, Biden published an executive order prohibiting mercenary spyware use by the US government without first going through a review process.



Those days _are over_. Mercenary spyware is officially _welcome_ in America.

Last year, during the Biden administration, ICE tried to sign a contract with Paragon Solutions, another sketchy Israeli firm that makes spyware called Graphite. But the Biden administration blocked this contract from going through.

But a few months ago, the “stop-work” order was dismissed, and [ICE’s contract with Paragon officially began](https://jackpoulson.substack.com/p/exclusive-ice-has-reactivated-its). According to [this reporting](https://jackpoulson.substack.com/p/exclusive-ice-has-reactivated-its) by Jack Poulson, the US company REDLattice acquired Paragon Solutions. Now that Paragon is American-owned, ICE is allowed to use the Graphite spyware.

![](https://micahflee.com/content/images/2025/10/slide-012.png)From Paragon Solution's website

Paragon bills Graphite as the “ethical alternative” to Pegasus. The difference between Graphite and Pegasus is that Pegasus takes over the entire phone. It does location tracking, listens through the microphone, steals all the data it can get, and so on. But Graphite is narrowly targeted at just spying on encrypted messaging apps like Signal, WhatsApp, and iMessage.

But _obviously_ governments abuse it to violate human rights too.

Here’s a [recent report from The Citizen Lab](https://citizenlab.ca/2025/03/a-first-look-at-paragons-proliferating-spyware-operations/), published in June, where they caught Graphite being used against prominent journalists in Europe. In this case, Graphite relied on a zero-click vulnerability in iOS that exploited a bug in iMessage.

And here’s [an earlier Citizen Lab report](https://citizenlab.ca/2025/06/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/), published in March. In this one, they helped discover and fix a zero-click exploit for WhatsApp that targeted dozens of people in Italy, including journalists and the founder of the Italian organization that _rescues migrants_ from the Mediterranean Sea.

404 Media has [launched a Freedom of Information Act lawsuit against ICE](https://www.404media.co/were-suing-ice-for-its-2-million-spyware-contract/), demanding documents related to its contract with Paragon. In this post, the journalists mention Paragon’s stance that it’s an “ethical alternative” in the spyware industry. It says, quote:

> Selling to ICE, an agency that has flaunted due process, accountability, and transparency, may complicate that stance for Paragon. ICE has arrested people who were [_following the steps necessary for legal immigration_](https://www.cbsnews.com/news/immigrants-at-ice-check-ins-detained-and-held-in-basement-of-federal-building-in-los-angeles/?ref=404media.co); waited outside courtrooms to immediately detain people after [_their immigration cases were dismissed_](https://www.npr.org/2025/06/12/nx-s1-5409403/trump-immigration-courts-arrests?ref=404media.co) to rush them out of the country; [_“de-documented” people who had valid work permits_](https://bsky.app/profile/reichlinmelnick.bsky.social/post/3lrg2u5linc2s?ref=404media.co) in order to deport them; and continues to pick up people around the country while masking their faces and declining to provide their names.

![](https://micahflee.com/content/images/2025/10/slide-017.png)CNN: [37 people arrested and American kids separated from parents after ICE raid at Chicago apartments](https://www.cnn.com/2025/10/03/us/chicago-apartment-ice-raid)

There’s nothing ethical about _anything_ that ICE does. There’s _no way_ that ICE will use Graphite in a way that _isn't_ abusing human rights.

But, hey, at least the Trump administration isn’t using Pegasus, right?

Earlier this month, [news broke](https://techcrunch.com/2025/10/10/spyware-maker-nso-group-confirms-acquisition-by-us-investors/) that American investors appear to have purchased NSO Group. Right now, NSO Group is still on the US sanctions list. Biden’s executive order making it harder for the government to use mercenary spyware is still in effect. There’s a trail of dozens of US officials that were hacked with Pegasus, which normally wouldn’t be a good sign for NSO Group.

But in the Age of Technofascism, I really don’t see those old rules lasting much longer. I wouldn’t be surprised at all if we started to find Pegasus infections on the phones of immigrant defense activists. Or advocates for trans health care. Or even people just trying to get an abortion.

Also, just to add to the absurdity of this, the main investor is Robert Simonds, a Hollywood producer of B-movie films. If you haven’t heard of Robert Simonds before, perhaps you’ve heard of this 1996 Adam Sandler film…

![](https://micahflee.com/content/images/2025/10/Screenshot-2025-10-25-at-5.40.57---PM.png)Photo of Simonds by Alex Berliner, [CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=32173349)

Robert Simonds produced Happy Gilmore, along with a bunch of other Adam Sandler films. His entire experience is in the entertainment industry, not in tech or cybersecurity. He also has a bunch of business dealing with Chinese companies.

[According to](https://www.calcalistech.com/ctechnews/article/1gny8rqwd) the Israeli tech site Calcalist, for some reason he’s been on the board of NSO group’s parent company for a few years. And in 2023, he tried, and failed, to purchase NSO Group. It appears that he just tried again and was successful.

Also in this article, it mentions that in 2018, Sophie Watts, the president of his production company STX Entertainment, complained of harassment, and called him “obsessive.”

Quite likely, _this guy_ is the new owner of the most notorious mercenary spyware firm in the world. And quite likely, he’s going to be selling Pegasus to fascist law enforcement agencies under Trump.

![](https://micahflee.com/content/images/2025/10/slide-024.png)Reuters: [Inside the UAE’s secret hacking team of American mercenaries Ex-NSA operatives reveal how they helped spy on targets for the Arab monarchy — dissidents, rival leaders and journalists](https://www.reuters.com/investigates/special-report/usa-spying-raven/)

But even if the current rules against Pegasus stick, there are plenty of American technofascists who don’t have any qualms with violating human rights.

Remember how I said that the most sophisticated hacking tools used to be developed in-house by agencies like the NSA? This was a big story back in 2019, when [Reuters exposed](https://www.reuters.com/investigates/special-report/usa-spying-raven/) that over a dozen former NSA operatives went to work for the United Arab Emirates _royal family_ , helping them spy on dissidents, journalists, and activists.

It’s a _bad sign_ that the US government is embracing mercenary spyware from sketchy Israeli firms. And that US companies are buying up those firms, presumably to make it easier to sell to the government.

But I honestly think there’s enough home-grown and talented American technofascists to support a domestic spyware industry anyway, even _without_ the Israeli technology.

Last month, Bruce Schneier [blogged about](https://www.schneier.com/blog/archives/2025/09/digital-threat-modeling-under-authoritarianism.html) Digital Threat Modeling Under Authoritarianism. It’s worth a read. He wrote:

> Imagine there is a government official assigned to your neighborhood, or your block, or your apartment building. It’s worth that person’s time to scrutinize everybody’s social media posts, email, and chat logs.

In it, he described the “shifting risks of decentralization,” which is something I hadn’t considered before.

Spyware is _targeted_ surveillance, not _mass_ surveillance, which means that it doesn’t scale easily. If all you had to worry about is staying off the radar of high-level fascists like JD Vance and Kash Patel, then most people probably don’t need to worry too much about it for themselves

But if repression is _decentralized_ , with every state and city having its own _local fascists_ in charge of picking targets they don’t like, then _everyone_ needs to fear it. It’s too early to know how mercenary spyware will be abused by the Trump administration, but it’s prudent for _everyone_ to get prepared _now_.

# Defenses Against Mercenary Spyware

This is bad, but it’s not hopeless. There’s a _lot_ that we can do to defend ourselves against mercenary spyware.

![](https://micahflee.com/content/images/2025/10/slide-027.png)

Zero-click exploits – which can hack your device without any interaction from you – can feel like magic, and like it’s hopeless to even try to defend against them. But it’s _not_ magic.

Exploits are only possible because of _bugs_. And these bugs are routinely fixed in _software updates_. Zero-day exploits cost attackers millions of dollars to purchase, which means it’s _very expensive_ to hack a fully updated phone or laptop. Exploits for bugs that are already patched, though, are _basically free_.

Never put off installing updates.

You should not only always install updates, but you should also get _everyone you know_ to always install updates too.

![](https://micahflee.com/content/images/2025/10/slide-028.png)

Apple added [Lockdown Mode](https://micahflee.com/unfortunately-the-iceblock-app-is-activism-theater/) to iOS in 2022. If you enable it, it prevents your phone from using certain features that are frequently exploited. Basically, it reduces your _attack surface_.

For example, it blocks fonts in Safari, which might make some websites look worse and the icons might be missing, but it cuts off an _entire attack vector_. I’ve been using Lockdown Mode in iOS since it came out and it’s actually quite usable.

In the Age of Technofascism, you should not only turn on Lockdown Mode, but get _everyone you know who uses an iPhone or a Mac_ to do the same. To my knowledge, no researchers have found a successful infection of a device while Lockdown Mode was turned on.

![](https://micahflee.com/content/images/2025/10/slide-029.png)

You, and _everyone you know who uses an iPhone_ , should also enable [Advanced Data Protection](https://micahflee.com/in-war-torn-portland-watch-me-speak-at-bsidespdx/) in your iCloud account. Without it, iCloud is basically a government backdoor into your phone. If your phone gets backed up to iCloud, including your messages, photos, and all the data in all your apps, Apple can give this data to the police, the FBI, ICE, or whoever else asks.

If you use Advanced Data Protection, most of this data is encrypted with a key that only _you_ control. The recovery key is a long sequence of random characters, so everyone who enables it either needs to keep this key written on a piece of paper, or store it in a password manager. If you’re helping people in your community enabled Advanced Data Protection for iCloud, it might be a good idea to also make sure they get set up with a password manager.

![](https://micahflee.com/content/images/2025/10/slide-030.png)

Earlier this year, Google launched [Android Advanced Protection](https://support.google.com/android/answer/16339980?hl=en), which works in similar ways. If you use Android, _enable this_ , and you’ll be far less vulnerable to mercenary spyware.

I don’t have much love for Apple. As I’ll talk about soon, they recently categorized ICE officers as a “targeted group” in order to comply with Trump’s censorship demands. But I _am_ excited about [Memory Integrity Enforcement](https://security.apple.com/blog/memory-integrity-enforcement/), which is built into the hardware of the new iPhone 17.

Basically, if you’re using the new hardware, every time software allocates a block of memory, this memory is tagged with a secret. If the software ever tries accessing that memory again without the correct tag, the request is blocked, and the process is killed.

This should effectively _eliminate entire classes_ of memory corruption bugs, including buffer overflows, use-after free, and out-of-bound bugs.

![](https://micahflee.com/content/images/2025/10/slide-032.png)Apple: [Memory Integrity Enforcement: A complete vision for memory safety in Apple devices](https://security.apple.com/blog/memory-integrity-enforcement/)

This diagram shows an analysis of _real exploit chains_ – these were the exploits included in actual mercenary spyware – and how each class of bug would perform against an iPhone with Memory Integrity Enforcement. It would prevent _all_ of them from fully hacking the device.

So, if you can afford it, this is one of the few reasons I’d recommend considering buying a new iPhone. Of course, if you do get a new iPhone, you should _also_ enable Lockdown Mode on it, and enabled iCloud Advanced Data Protection.

# Device Searches

Mercenary spyware relies on exploits to hack your devices _remotely_. But there’s a whole different set of _local_ attacks against devices too. Device searches have been a risk for as long as people have carried around computers with personal data. But in the Age of Technofascism, we should prepare for device searches _way_ more frequently.

Cellebrite – another Israeli surveillance company – is the most notorious firm that does device searches. They make products that are currently already used by law enforcement across the US, but they’re aiming for a _much_ bigger slice of the market. Last year, Cellebrite [announced](https://cellebrite.com/en/cellebrite-advances-plans-to-transform-and-elevate-its-strategic-relationship-with-the-u-s-federal-government/) that it formed a US-based subsidiary specifically for selling to the federal government.

Cellebrite makes hardware and software used to break into locked phones and extract all the data from them. It works by exploiting vulnerabilities in lock screens, by brute forcing passcodes, including using exploits to bypass rate limits, and by rooting devices to get access to all the data in them.

![](https://micahflee.com/content/images/2025/10/slide-035.png)Signal: [Exploiting vulnerabilities in Cellebrite UFED and Physical Analyzer from an app's perspective](https://signal.org/blog/cellebrite-vulnerabilities/)

This photo is from a 2021 post on the Signal blog by Moxie Marlinspike. He said, “By a truly unbelievable coincidence, I was recently out for a walk when I saw a small package fall off a truck ahead of me.” It turns out, it was Cellebrite equipment. Specifically, just the software used to extract data from phones, and a bunch of cables, but not the actual hardware that hacks into phones.

Moxie also wrote about some security vulnerabilities he discovered in it. He discovered that, “it’s possible to execute arbitrary code on a Cellebrite machine simply by including a specially formatted but otherwise innocuous file in any app on a device that is subsequently plugged into Cellebrite and scanned.”

Like other Israeli surveillance firms, Cellebrite has a history of being abused to violate human rights:

  * In 2020, police in the African country Botswana used Cellebrite to break into the phones of detained journalists, [according to](https://cpj.org/2021/05/equipped-us-israeli-firms-botswana-police/) Committee to Protect Journalists.
  * In 2021 during the protests in Hong Kong, Chinese police used Cellebrite to hack the phones of pro-democracy protesters, [according to](https://theintercept.com/2021/08/26/cellebrite-china-cellphone-hack/) reporting in The Intercept.
  * In 2022, Russia used Cellebrite to hack the phones of anti-Putin opposition activists, [according to](https://www.haaretz.com/israel-news/security-aviation/2022-10-21/ty-article/.premium/russia-still-using-israeli-tech-to-hack-detainees-cellphones/00000183-eb6c-d15c-a5eb-ff6cf86e0000) reporting in Haaretz.



Last month, ICE entered [a new $11 million contract](https://reason.com/2025/09/29/ice-doesnt-want-you-to-know-why-they-bought-a-phone-cracking-system/) with Cellebrite. But ICE already has a long history of working with them. In 2017, they first spent $2.2 million on a Cellebrite contract, immediately after Trump’s travel ban. In 2019, they spent somewhere between $30 and $35 million on another contract. And now, they’re starting a _new_ $11 million contract.

It’s fair to assume that ICE is using Cellebrite to hack the phones, and steal all the data, from _every single person_ they arrest, regardless of immigration status.

When your device is searched, authorities _stealing your data_ is only one of the risks that you face. Another is that they might _install spyware_ , and hope that you keep using it. Here’s [an article](https://techcrunch.com/2024/12/05/russian-programmer-says-fsb-agents-planted-spyware-on-his-android-phone/) from last year about a pro-Ukraine activist in Russia named Kirill Parubets.

Armed FSB agents violently raided his house. From the article:

> On April 18, 2024, six FSB agents armed with machine guns burst into Parubets and his wife’s apartment in Moscow at around 6:30 in the morning. “They threw us to the floor, they dragged my wife into a small room, I was lying in the hallway. They didn’t let us get dressed,” according to his recollection of the events, which Parubets wrote in a document he shared with TechCrunch. 

One of them picked up his Android phone and said, “What’s your fucking password?” And Parubets told them. From the article:

> “What’s your f—king password?” one of the agents asked Parubets when they picked up his Android phone, according to his recollection of the events. Intimidated, Parubets said he gave away its password. 

They threatened to keep him in prison unless he agreed to spy on Ukrainians for the Russians, so he agreed, even though he says he didn’t plan on actually doing it. When they released him, they gave him back his phone and it had spyware on it.

According to [an analysis of Parubets’s Android phone](https://citizenlab.ca/2024/12/device-confiscated-by-russian-authorities-returned-with-monokle-type-spyware-installed/) by The Citizen Lab and the legal assistance group First Department, the spyware they found “allows the operator to track a target device’s location, record phone calls, keystrokes, and read messages from encrypted messaging apps, among other capabilities.”

And the report also point out:

> Any person whose device was confiscated and later returned by [a security service] should assume that the device can no longer be trusted without detailed, expert analysis.

In the Age of Technofascism, this applies when your device is seized by DHS, ICE, CPB, the FBI, and in many situations probably local police too.

![](https://micahflee.com/content/images/2025/10/slide-044.png)

Sometimes it’s legal for authorities to search your device, and sometimes it’s illegal. But all of that is pretty abstract when it’s clear that the Trump administration doesn’t care about breaking the law, and gets away with it all the time.

Whenever you cross a border or go to a protest, you should be prepared for the fact that authorities _might_ try to search your devices.

![](https://micahflee.com/content/images/2025/10/slide-045.png)

It’s still important to **know your rights** , even if fascist authorities are likely to violate them. You should consult actual lawyers for legal advice, but here are just some quick tips:

  * You have the right to remain silent, so **don't talk to the police** except to assert your rights.
  * Police are kind of like vampires, they can only legally enter your home if you invite them in. So if police or federal agents show up at your house or your business, **do not invite them in**. If they say they have a warrant, it needs to be a valid warrant, signed by a real judge. ICE tries to use their own fake warrants, and those aren’t legally binding.
  * If they try to search you, tell them you **do not consent**.
  * If they want you to unlock your phone or computer, **don't comply** , and **don't share your passwords**. There’s a good chance that this will result in them stealing your devices, but at least they’ll be encrypted.



**Before I go into the defenses against device searches, I want to take a minute to plug the**[**Access Now Digital Security Helpline**](https://www.accessnow.org/help/)**.**

Researchers at places like The Citizen Lab, Access Now, and Amnesty International have done an _amazing_ job exposing spyware firms and their flagrant abuse of human rights. Detecting spyware is hard, and none of this research is possible without the cooperation of the victims of spyware.

If you think your device has been hacked by the Trump administration, or _if there is anyone in your community who might have been hacked_ , please reach out to the Access Now Helpline for help. If anyone you know has had their phone seized by federal agents, and then later given back to them, they should _definitely not trust that phone_ , and contact the Access Now Helpline.

# Defenses Against Device Searches

While I can’t give you legal advice, I _can_ give you technical advice on defenses against device searches. These mostly all revolve around disk encryption.

![](https://micahflee.com/content/images/2025/10/slide-048.png)

If someone gains access to your phone or computer and you aren’t using disk encryption, _nothing_ stops them from accessing all your data. But even with disk encryption, your data is only as secure as how you’re able to unlock your device, as well as your lock screen settings.

For example, let’s say you have an iPhone and a strong passcode, but you unlock your phone with your face. This means that when you get arrested at a protest, the cop can _also_ unlock your phone with your face, and then access all the data in your phone.

Because of tools like Cellebrite, your phone’s passcode is also really important. It’s orders of magnitude harder to hack into a phone with 10-digit passcode than with a 6-digit passcode.

![](https://micahflee.com/content/images/2025/10/slide-049.png)

You should also harden your devices. If these defenses against device searches look familiar, it’s because they’re _also_ defenses again mercenary spyware.

Cellebrite, and similar tools that attack computers, rely on vulnerabilities to help them bypass your lock screen or brute force your password without rate limiting. Install updates. When you’re using the latest version of your OS, there are fewer vulnerabilities in your lock screen that can be exploited.

And again, enable Lockdown Mode in iOS and macOS. And enable Advanced Protection in Android.

When your device is seized, but in a locked state, you also should be careful about what information is on your lock screen. They can access that data without even needing to hack your device. Make sure that sensitive notifications – like the content of your Signal messages – don’t get displayed on your lock screen. This applies to both computers and phones.

![](https://micahflee.com/content/images/2025/10/slide-050.png)The Windows 95 shut down screen

If you have disk encryption, the very best thing you can do to keep your device secure is to **completely power off your device** when you’re not using it. A powered off device, before you’ve entered any password to unlock the encryption, is much harder to hack into than one that’s powered on but locked.

So, when you’re going through a security checkpoint at the airport, completely power of your phone and your computer _first_.

When you’re at a protest, if it looks like you might get arrested imminently, power off your phone before you get detained. You can always power it back on when you’re safe.

And finally, turn off all of your computers _every night_ when you’re not using them. Police most often raid people’s homes in the middle of the night or the very early morning. Powering off your computers every night means that if you get raided, your devices will be harder to hack into, giving your disk encryption a fighting chance.

![](https://micahflee.com/content/images/2025/10/slide-054.png)

People often talk about anonymous burner phones. Except in very specific situations, truly anonymous burner phones aren’t that useful. Using a [_secondary phone_](https://activistchecklist.org/secondary/) that you don’t even try to keep anonymous, on the other hand, is easy to maintain, and it has some major benefits. If you get detained at an airport, or you get arrested at a protest, the authorities either already know who you are, or they’re about to, so anonymity isn’t important here.

When you set up a secondary device, use a separate Google or Apple account, so it can't access the data in your main account. Make a separate Signal account, and just add the contacts and groups you'll need. If authorities hack into your secondary device, there won’t be much data to extract. It won’t have your messaging apps, your contacts, your browser history, your photos, your documents, or anything else like that.

Since secondary devices are just for temporary use – to take on an international trip, or to bring to a protest – you should factory reset them between uses. This should protect you in case they install spyware on your device and give it back to you. Although, ideally you should contact the Access Now Helpline to let researchers to get a sample of that spyware first.

![](https://micahflee.com/content/images/2025/10/slide-055.png)

Even on your main devices, _minimize_ the data that you retain. **They can't steal your data if you don't have anything to steal.**

We’ll all be better off if we start treating most online communication as ephemeral and delete it after we’ve read it. If you want to retain anything, take a screenshot, but delete everything else.

If you go into the Signal app, you can go to Settings, Privacy, Disappearing Messages, and set Signal to use disappearing messages by default for every chat. And while you’re at it, get everyone you know to stop sending you messages in iMessage, WhatsApp, Instagram DMs, or anything else, and switch to Signal.

You should minimize other data too, not just in messaging apps. Basically, think about what data you have on your phones and computers, and regularly take steps to reduce your risk if those devices are ever searched.

# Cell-Site Simulators

This isn’t about mercenary spyware or device searches, but I wanted to slip this into my talk too. We’ve known for years that ICE, and local police departments across the US, use _cell-site simulaors_. Here’s [recent reporting](https://techcrunch.com/2025/10/07/ice-bought-vehicles-equipped-with-fake-cell-towers-to-spy-on-phones/) from earlier this month about yet another ICE contract for these street level surveillance devices.

If you’re not familiar with cell-site simulators, which are also called IMSI catchers or Stingrays, they’re devices that pretend to be legitimate cell phone towers, tricking all nearby phones into connecting directly to them rather than real towers. We know that these are in use across the US, but there’s a real challenging in detecting them.

[Rayhunter](https://efforg.github.io/rayhunter/) is open-source custom firmware for cheap mobile hotspots that can detect cell-site simulators. It’s developed by Cooper Quintin and others at EFF. You need to plug in a SIM card, but you don't need to pay for phone service, so it’s a cheap one-time cost. It’s incredibly easy to flash the Rayhunter firmware onto these. If you’re interested in trying to detect cell-site simulators, check out the Rayhunter project.

# There's NOT an App for That

A different way that technofascism is expressing itself is app censorship. Apple and Google, the companies that control exactly what software anyone is allowed to install on their phones, are actively collaborating with the Trump administration by censoring their App Stores without even a fight.

A few weeks ago, at the request of the Trump administration, Apple [kicked](https://www.404media.co/iceblock-owner-after-apple-removes-app-we-are-determined-to-fight-this/) the ICEBlock app out of the App Store. This was an iPhone app that allowed users to anonymously report ICE sightings within a 5 mile radius and get notifications when others reported ICE sightings near them.

The developer, Joshua Aaron, points out that:

> ICEBlock is no different from crowd sourcing speed traps, which every notable mapping application, including Apple's own Maps app, implements as part of its core services.

To justify its decision, Apple has decided to treat ICE officers as a “targeted group,” and to treat apps that help inform the public about abuses by ICE agents – whose job is _racial profiling_ and _violence against people based on their national and ethnic origin_ – as the same as _discriminating_ against people for their religion, race, sexual orientation, gender, or national or ethnic origin.

To be clear, the government didn’t send a court order to Apple demanding that they do this. The Justice Department asked Apple, and Apple simply agreed without a fight.

Here’s a quick video of Attorney General Pam Bondi **lying to the Senate** about ICEBlock:

0:00

/0:41

1×

October 7, 2025: Attorney General Pam Bondi lies to the Senate Judiciary Committee about ICEBlock ([YouTube link](https://www.youtube.com/watch?v=E1JroBFodGk))

First, ICEBlock did _not_ post “where ICE officers live.” They just posted ICE _sightings_ , which then automatically got deleted after a few hours. Also, ICEBlock was never available for Android.

But don’t worry, **Google _also_ voluntarily **[**chose to collaborate**](https://www.404media.co/google-calls-ice-agents-a-vulnerable-group-removes-ice-spotting-app-red-dot/)**with the fascists** at the request of the Trump administration. And in fact, they used pretty much the same justification. Both Apple and Google removed the [Red Dot app](https://www.red-dot.app/) from their app stores.

Red Dot is an app that’s similar to ICEBlock, in that it lets people report ICE sightings and get alerts when they’re nearby. Since it’s been banned by both Apple and Google, it’s now _only_ available for Android as an APK that you can sideload.

Google _claims_ that the Justice Department didn’t ask them to ban Red Dot, but I find that kind of hard to believe considering Pam Bondi keeps giving interviews saying that she asked Google to ban these apps.

But even more disturbingly, Google’s justification for banning Red Dot is that working at ICE makes you part of a vulnerable group that is “associated with systemic discrimination or marginalization.” **This is just offensive.**

And even worse, Apple [banned an app called Eyes Up](https://www.404media.co/apple-banned-an-app-that-simply-archived-videos-of-ice-abuses/) from the App Store. Unlike ICEBlock and Red Dot, Eyes Up doesn’t do any real-time tracking or alerting of ICE sightings. It simply archives verified videos of ICE abuse, and puts them on a map to _preserve evidence of their crimes_.

Also unlike ICEBlock or Red Dot, Eyes Up is a _web application_. So it’s still online and active at [**eyesupapp.com**](https://eyesupapp.com/). Here’s a screenshot of Eyes Up, zoomed into part of Portland.

![](https://micahflee.com/content/images/2025/10/eyes-up-screenshot.png)

Apple is **voluntarily helping the fascists censor videos of violence** from DHS officers like this one:

0:00

/0:59

1×

See the original video at [Eyes Up](https://eyesupapp.com/video/0bcb359b-849c-44e0-b233-4626a0be3acd).

It’s not just Apple and Google though. Last week, Facebook [deleted a group](https://www.nytimes.com/2025/10/15/technology/meta-removes-ice-facebook-page.html) called “ICE Sighting-Chicagoland” with _over 80,000 members in it_ , at the request of Attorney General Pam Bondi. Just like Apple and Google’s excuses, Meta claimed that this Facebook group was violating policies “against coordinated harm.”

On a [recent episode](https://www.wnycstudios.org/podcasts/otm/articles/big-tech-is-silencing-the-ice-watchers-plus-why-a-scholar-of-antifa-fled-the-country) of the podcast On the Media, the 404 Media reporter Joseph Cox spoke about this Facebook group:

> I have seen a limited archive of that Facebook page. It’s difficult to access now, of course, because it has been taken offline. But the section that I scrolled through, I did not see any evidence of ICE officials being doxed, or specifically targeted. It was more just reporting, ‘Hey, there are ICE officials at this location,’ very much in the same sort of way that apps like ICEBlock were doing.

Here's a recording from the podcast:

![audio-thumbnail]()

Excerpt from On the Media episode: Big Tech is Silencing the ICE Watchers. Plus, Why a Scholar of Antifa Fled the Country.

0:00

/40.019592

1×

**So in other words, in the Age of Technofascism, American tech companies are collaborators.**

Before going to solutions, I want to share one final story from earlier this week. [This article](https://www.forbes.com/sites/the-wiretap/2025/10/21/ice-spies-on-whatsapp/) describes a search warrant that ICE sent to Meta, demanding real-time metadata about who a WhatsApp user was communicating with.

WhatsApp messages are end-to-end encrypted, but Meta freely gives law enforcement all of the metadata. If you’re using WhatsApp for any sort of antifascist activism, _stop and switch to Signal_. Signal has features like Sealed Sender that prevent them from even accessing the metadata themselves, and so they can’t be forced to hand it over to ICE.

From the article:

> The warrant reviewed by _Forbes_ , filed towards the end of last week, now allows the government to force unlock that suspect’s phone by applying the defendant’s fingerprints to the device, or holding up the phone to their face, depending on what, if any, biometric access features they’re using.

This warrant also specifically allows the government to unlock the suspects phone using their biometrics. So again, _don't use biometrics_ for unlocking your phone or your computer.

# The Open Web is Our Best Hope

Of these four instances of censorship, ICEBlock, Red Dot, Eyes Up, and the “ICE Sighting-Chicagoland” Facebook group, Eyes Up is the only one that’s still online. And the reason is because it’s a _website_.

![](https://micahflee.com/content/images/2025/10/slide-074.png)

What this censorship tells me is that companies like Apple, Google, and Meta cannot be trusted or relied on.

If you want to make an app that the Trump administration won’t like, unfortunately, you should make it with censorship in mind. Just like Eyes Up, make it a website that works without a native app, so when Apple and Google turn on your, your tool can still be useful.

The internet is a global network. There are domain name registrars and hosting providers all over the world, including many that won’t cooperate with the US government.

There isn’t much internet censorship in the US, yet. But if that changes, thanks to activists in places like China, Iran, and Russia, we have decades of experience circumventing online censorship. We can use the same techniques here if we need to.

# Community

Finally, we should all step back from our computers, put down our phones, and devote real energy into strengthening our communities.

![](https://micahflee.com/content/images/2025/10/slide-076.png)

Things are _really bad_ right now, and it’s easy to feel isolated and alone. Whenever possible, talk with people _in person_ instead of in group chats or video calls.

People are facing harassment from Trump-supporting fascists. Their loved ones are getting disappeared by the secret police. The state is making example out of people for trying to get gender affirming or reproductive health care, or for protesting genocide.

When they come after you, your friends, or your neighbors, the _worst_ thing you can do is to keep staring at your phone. We need real community ties with people who have our backs. And we need to have solidarity with _everyone else_ they’re going after.

![](https://micahflee.com/content/images/2025/10/slide-077.png)

People living under repressive regimes have learned throughout history is the importance of **security culture**. A security culture is a set of customs and measures shared by a community to keep everyone safe.

As shit gets more real, keeping your community safe is everyone's responsibility.

Don’t panic if you haven’t done all of the things I proposed in this talk. Don’t judge others who haven’t done them either. It takes time to incorporate these practices into our communities as a security culture, but we’ll all be better off if we commit to it.

The fascists are probably going to start hacking our phones.

They’re going to plug them into Cellebrite to try to see see exactly who we’re talking to and what we’re saying.

They might try to plant spyware on them and hope we keep using them.

They’re going to pressure tech platforms to prevent us from organizing – they already are.

And they’re going to use data from companies like Google and Meta to decide which of us to target.

It’s not enough to just lock down your own devices. **If we want to stay safe and productive in the Age of Technofascism, we all need to work together.**

* * *

_If you found this interesting,  _[_subscribe_](https://micahflee.com/#/portal/signup) _  to get these posts emailed directly to your inbox. If you want to support my work, considering becoming a paid supporter._

[ ![Micah Lee](https://www.gravatar.com/avatar/73aa6b8ef40730e5cbcce3137400120e?s=250&r=x&d=mp) ](/author/micah/)

[Micah Lee](/author/micah/)

25 Oct 2025

## 

[← Previous](/in-war-torn-portland-watch-me-speak-at-bsidespdx/)

[Next →](/i-spoke-about-iceblock-and-trumps-app-censorship-on-the-kill-switch-podcast/)

  * Subscribe



Posts are licensed under CC BY-NC 4.0 
