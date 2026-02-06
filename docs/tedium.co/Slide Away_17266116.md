# Slide Away

**来源:** https://tedium.co
**链接:** https://feed.tedium.co/link/15204/17266116/niri-danklinux-scrolling-window-managers
**日期:** 

---

[](https://tedium.co/cdn-cgi/content?id=fnaiqjwCDJspb3b_lal5NJBX71ulexhMBbI04cQjo2c-1770286698.0175917-1.0.1.1-.HumT33HxS6_qceC6dQAENFCbH1XkLIHJWNCDhzeI68)

###  [ ![Tedium.](/content/logo_v3.svg) ](/)

[ __  About ](/what-is-tedium) / [ __  Archives ](/archive) / [ __  Sponsor Us ](/advertising)

Search Tedium __

![Slide Away](https://proxy.tedium.co/F4DUEmVZIzhweqwiC68oO7V82oQ=/smart/filters:quality\(50\):format\(jpeg\)/uploads/danklinux_compressed.gif) ![Slide Away](https://proxy.tedium.co/6Fi_ijZSpMvl0jku69EOTUXqTgw=/filters:quality\(80\)/uploads/danklinux_compressed.gif) [ « Previously … ](/2026/01/22/oneplus-decline-shutdown-rumors-commentary/) __ Subscribe [ __Shuffle ](/2025/10/02/subminiature-tubes-transistors-raytheon-history/ "Tiny Tubes") [__ Support Us On Ko-Fi](https://ko-fi.com/tedium)

##### Share This Post:

[ ![](https://static.tedium.co/uploads/share-openly.svg)  ShareOpenly ](https://shareopenly.org/share/?url=https%3A%2F%2Ftedium.co%2F2026%2F01%2F29%2Fniri-danklinux-scrolling-window-managers&text=https%3A%2F%2Ftedium.co%2F2026%2F01%2F29%2Fniri-danklinux-scrolling-window-managers%3A%20My%20favorite%20UX%20metaphor%2C%20the%20scrolling%20window%20manager%2C%20is%20having%20a%20moment%E2%80%94and%20it%E2%80%99s%20for%20pretty%20dank%20reasons.) [ __ Share Well ](https://toot.kytta.dev/?text=Slide%20Away%3A%20My%20favorite%20UX%20metaphor%2C%20the%20scrolling%20window%20manager%2C%20is%20having%20a%20moment%E2%80%94and%20it%E2%80%99s%20for%20pretty%20dank%20reasons.%0A%0Ahttps%3A%2F%2Ftedium.co%2F2026%2F01%2F29%2Fniri-danklinux-scrolling-window-managers%0A%0A%28via%20%40tedium%40social%2Etedium%2Eco%29) [ __ Share Amazingly ](https://bsky.app/intent/compose?text=Slide%20Away%3A%20My%20favorite%20UX%20metaphor%2C%20the%20scrolling%20window%20manager%2C%20is%20having%20a%20moment%E2%80%94and%20it%E2%80%99s%20for%20pretty%20dank%20reasons.%20https%3A%2F%2Ftedium.co%2F2026%2F01%2F29%2Fniri-danklinux-scrolling-window-managers) [ __ Waste Pixels ](https://twitter.com/intent/tweet?url=https%3A%2F%2Ftedium.co%2F2026%2F01%2F29%2Fniri-danklinux-scrolling-window-managers&via=readtedium&text=Slide%20Away)

# Slide Away

## My favorite UX metaphor, the scrolling window manager, is having a moment—and it’s for pretty dank reasons.

By Ernie Smith • January 29, 2026

https://static.tedium.co/uploads/danklinux_compressed.gif

[ #sliding window manager ](/tag/sliding-window-manager/) [ #scrolling window manager ](/tag/scrolling-window-manager/) [ #paperwm ](/tag/paperwm/) [ #niri ](/tag/niri/) [ #hyprland ](/tag/hyprland/) [ #dank linux ](/tag/dank-linux/) [ #dankmaterialshell ](/tag/dankmaterialshell/) [ #user interface ](/tag/user-interface/) [ #ux ](/tag/ux/)

**I was a pretty early adopter** of perhaps the best GNOME extension, [PaperWM](https://github.com/paperwm/PaperWM), which displays your windows as sliding frames that move fluidly with the press of a keystroke.

When everyone was going nuts over tiling windows, I was quietly calling this scrolling style the real innovation in windowed computing. (For the uninitiated: Think of it kind of like swiping between virtual desktops on Windows or MacOS, except you can do it on every single window, slideshow-style.) It was the best of both worlds—easy to navigate, while remaining mousable.

Eventually more people figured out that this was the ticket, and now PaperWM has grown from quiet experiment to robust extension. As a way to prove an idea, it was basically flawless, to the point where [someone made a MacOS version](https://github.com/mogenson/PaperWM.spoon).

![PaperWM.jpg](https://proxy.tedium.co/0C0qYpwP8n_eHZLfMLztidHSRWE=/2560x1440/filters:quality\(80\)/uploads/PaperWM.jpg)A screenshot of PaperWM, quietly one of the most exciting interface innovations of the past decade.

But it had a problem: It was attached to [GNOME](https://www.gnome.org), with all the extra cruft that implies. GNOME’s interface has a lot of fans (me included), but it’s mature, complex, and prescriptive. It’s controversial in the Linux world because it makes UX decisions for users that sometimes get in the way of user choice. I tend to defend it, but if you were to put “heavy FOSS graphical interface” in the dictionary, GNOME would most assuredly show up.

Retrofitting a new user interface paradigm on top of that dynamic comes with compromises.

![niri-star.jpg](https://proxy.tedium.co/vXUzMp2F9wWKgd9anr0SBeLjgLw=/1000x723/filters:quality\(80\)/uploads/niri-star.jpg)If you want to think about things in terms of GitHub stars, Hyprland is growing fast, but Niri is starting to catch up.

Which is why I’ve been keeping an eye on [niri](https://github.com/YaLTeR/niri), an emerging window manager that is doing for sliding windows what [Hyprland](https://hypr.land) did for tiling. It is less than three years old (Hyprland is about four), but has quickly grown in popularity, [doubling its GitHub star count](https://www.star-history.com/#YaLTeR/niri&hyprwm/Hyprland&type=date&legend=top-left) in the past six months.

Built around the Wayland compositor, the project basically is set up like a kit, one where you need to supply parts in the form of config files. If you like customizing, it may be the project for you. But if you just want to get stuff done, it might not feel like a welcoming experience.

[Omarchy](https://tedium.co/2025/10/13/omarchy-linux-distro-commentary/), which we (controversially) covered a few months ago, exists because of this gap. People want the lightweight customizability of a window manager, but not the work of having to set it up.

To be clear, this is not far from where graphical interfaces for Linux and Unix variants started 40 years ago, but it’s arguably making a comeback because of a combination of sophisticated users and sophisticated tools. But not everyone has time to build their own config files from scratch.

![Niri-DankMaterialShell.jpg](https://proxy.tedium.co/uYXMVYlFTT5co6jvsW37CQD9dCg=/1000x625/filters:quality\(80\)/uploads/Niri-DankMaterialShell.jpg)My setup, combining Niri and the DankMaterialShell.

That’s where the project [Dank Linux](https://danklinux.com) comes in. Pitched as a “modern desktop for Wayland,” it’s a set of “batteries included” tools to get you going in Niri or other window managers based on Wayland. Key to the project is DankMaterialShell, which combines a number of tools into one interface, along with the [Material design](https://m3.material.io) approach. If Hyprland, Sway, niri and their ilk are attempts to deconstruct the desktop environment, Dank Linux tries putting it back together again.

Rather than relying on loose tools like [waybar](https://github.com/Alexays/Waybar) or [rofi](https://github.com/davatorium/rofi) and bringing them together with a best-in-breed approach, DankMaterialShell comes with all the necessary tools already baked in. Plus, it’s highly extensible, and can be edited through a bunch of config files, just like all the really complicated tools. But unlike Omarchy, it’s not prescriptive—you’re not just having to work around one guy’s opinion of what your UX should look like for the rest of time. (Case in point: I don’t like borders or gaps around my windows, a typical trait of scrolling window managers. So … I just removed them.)

That’s because it’s built around [Quickshell](https://quickshell.org), a toolkit that has become very [popular as a modding tool](https://github.com/topics/quickshell) in the Linux community.

But some of us are normies who just want something that works. Hence why DankMaterialShell is making such a splash.

![dankmaterialshell_setup.png](https://proxy.tedium.co/XfhtIuGhUBxyc8cVN_Eie_hvO64=/889x936/filters:quality\(80\)/uploads/dankmaterialshell_setup.png)An example of the graphical interface for DankMaterialShell. It has many of the features of the GNOME setup, including the ability to arrange monitors, with a lean on UI.

The feature set for this software is surprisingly robust, and seems to be growing quickly. [DMS 1.2](https://danklinux.com/blog/v1-2-release), for example, has literally dozens of new features. And despite the fact that this tool is only about six months old, it already has a screenshot tool, numerous plugins, and a robust theming system. The momentum is clearly there. (It’s not alone, either—also covering the same territory is [Noctalia](https://noctalia.dev), which promises a more relaxed aesthetic.)

The Dank Linux team offers a couple of optional utilities—the system overview tool DGOP and the MacOS Spotlight-like file tool dsearch—that can make the experience surprisingly polished.

The one downside of this is that Dank Linux isn’t really supported on Bazzite, the very popular distro I use. But after I mentioned I was interested in that, and I did some off-label testing on my end, one of the creators of [Zirconium](https://github.com/zirconium-dev/zirconium/), a Dank Linux distro for Fedora, reached out. Turns out, they were already working on a “quick and dirty” image that got Bazzite working with Zirconium. (As reflected by the name, [Bazzirco](https://github.com/bazzirco/bazzirco).) They even created a [Bazzite DX](https://dev.bazzite.gg) version for me, so I could easily access my Docker containers from the thing.

([Universal Blue](https://universal-blue.org), the framework upon which Bazzite is based, allows you to make your own custom builds pretty easily. You can even roll back to other versions so you can switch between different builds at will. Think it’s gonna be a GNOME day? Switch to that image.)

There were some glitches here and there—for example, I found that turning variable refresh rate on for my laptop screen caused my external monitors to drag. Plus, running a “quick and dirty” build naturally means you’re going to run into some quick-and-dirty bugs. (I ran into some audio issues while running _Balatro_ on the experimental distro. Not the end of the world. I signed up for this!)

Sure, you can retrofit this—albeit with common engine-swapping issues like broken keyrings—but I think the real magic might be starting fresh with it. Load it up on a new machine, set up your config to your liking, and get sliding.

But overall, this feels like a big step forward for desktop Linux—highly flexible, highly customizable, bleeding edge, yet somewhat approachable to normal people. I would go so far as to call it dank.

##### Sliding Links

**The Muppet Show is[coming back](https://www.hollywoodreporter.com/tv/tv-news/muppet-show-revival-trailer-disney-1236482871/)** next week as a “backdoor pilot” for a potential series. Great—let’s hope it sticks this time! Over at [_The Conversation_](https://theconversation.com/its-easy-making-green-muppets-continue-to-make-a-profit-50-years-into-their-run-272855), there’s a great piece talking about the troupe’s lasting popularity.

**YouTuber John Hancock** has one of the largest game collections known to man, having built complete game sets for numerous consoles, including the biggies. But he didn’t want it to live in a closet forever. He’s been trying to donate it or give it to a museum for years, and [this week he announced](https://www.youtube.com/watch?v=s_TlRGlkmbQ) that he did just that, splitting the collection up between two sources, a video game archive and a podcast.

**It’s actually kind of a good thing** that Google’s forthcoming Aluminum OS, a combination of Android and Chrome OS, is kind of boring, based on [some early leaked interface video](https://9to5google.com/2026/01/27/android-desktop-leak/). It means it’s going to be usable.

\--

Find this one an interesting read? [Share it with a pal](https://tedium.co/2026/01/29/niri-danklinux-scrolling-window-managers/)!

Wanna see a shining example of a user interface? Check out [la machine](https://la-machine.fr/?utm_source=newsletter&utm_medium=email&utm_campaign=tedium)! It only does one thing, but it does it really, really well.

![Ernie Smith](https://proxy.tedium.co/4DURKSI2domRaY9WpcAvjrbLaZM=/150x150/smart/filters:quality\(80\)/uploads/ernie_crop.jpg) Your time was wasted by … [Ernie Smith](/author/ernie/) Ernie Smith is the editor of Tedium, and an active internet snarker. Between his many internet side projects, he finds time to hang out with his wife Cat, who's funnier than he is. [ __](https://writing.exchange/@ernie) [ __](https://bsky.app/profile/ernie.tedium.co) [ __](https://www.threads.net/@shortformernie) [ __](https://erniesmith.net/) [ __](/cdn-cgi/l/email-protection#a7c2d5c9cec2e7d3c2c3ced2ca89c4c8) [ « Minus World ](/2026/01/22/oneplus-decline-shutdown-rumors-commentary/) __ Subscribe

#### Subscribe to Tedium

### Get more bizarre takes in your inbox.

**This is a newsletter that existed before Substack.** (We even turned Substack down!) Our goal is to outlive it. But we will be unable to do so unless you put your email in this box and let us invade your inbox with these messages that we send when we feel like it. It's an important obligation. Are you up to the task? 

Shoryuken!

Tedium can email me random bits of errata and rants about salsa jars. I am signing up for this. 

  ![Tedium T Logo](https://static.tedium.co/uploads/t-logo_nobg_v3.svg) **Once upon a time,** there was an internet that was weird and fascinating and didn’t make you mad. For the past ten years, Tedium has tried to bring that internet back through a commitment to weirdness and a love for the obscure and offbeat. We are nominally a newsletter, but if you share our content on the web, we won’t be upset. But if you email us asking for a backlink, we’ll publicly scold you on social media using the most sarcastic possible language. Them’s the breaks.

  * [What is Tedium?](https://tedium.co/what-is-tedium)
  * [Support us on Patreon](https://www.patreon.com/tedium)
  * [Share your ideas!](https://tedium.co/contribute)
  * [Privacy Policy](https://tedium.co/privacy-policy)
  * [Advertise With Us](https://tedium.co/advertising)
  * [RSS feed](https://feed.tedium.co/)
  * [Ernie on Mastodon](https://writing.exchange/@ernie)



_**Disclosure:** From time to time, we may use affiliate links in our content—but only when it makes sense. Promise._

_**P.S.:** If you email me asking about doing a guest post or posting a backlink, you forfeit ownership of your site to me._

Proudly built using a combination of [Craft CMS](https://craftcms.com/), Eleventy, Tailwind, and general magic.

Copyright (C) 2015-2025 Tedium LLC. All rights reserved. [Please, try the fish](https://www.youtube.com/watch?v=hqi2Jy0UMiA).
