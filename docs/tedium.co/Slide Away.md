# Slide Away

**来源:** [tedium.co](https://tedium.co/feed)
**发布时间:** Unknown
**链接:** https://tedium.co/2026/01/29/niri-danklinux-scrolling-window-managers/

---

{'type': 'text/html', 'language': None, 'base': '', 'value': '
My favorite UX metaphor, the scrolling window manager, is having a moment—and it’s for pretty dank reasons.
I was a pretty early adopter
of perhaps the best GNOME extension,
PaperWM
, which displays your windows as sliding frames that move fluidly with the press of a keystroke.
When everyone was going nuts over tiling windows, I was quietly calling this scrolling style the real innovation in windowed computing. (For the uninitiated: Think of it kind of like swiping between virtual desktops on Windows or MacOS, except you can do it on every single window, slideshow-style.) It was the best of both worlds—easy to navigate, while remaining mousable.
Eventually more people figured out that this was the ticket, and now PaperWM has grown from quiet experiment to robust extension. As a way to prove an idea, it was basically flawless, to the point where
someone made a MacOS version
.
A screenshot of PaperWM, quietly one of the most exciting interface innovations of the past decade.
But it had a problem: It was attached to
GNOME
, with all the extra cruft that implies. GNOME’s interface has a lot of fans (me included), but it’s mature, complex, and prescriptive. It’s controversial in the Linux world because it makes UX decisions for users that sometimes get in the way of user choice. I tend to defend it, but if you were to put “heavy FOSS graphical interface” in the dictionary, GNOME would most assuredly show up.
Retrofitting a new user interface paradigm on top of that dynamic comes with compromises.
If you want to think about things in terms of GitHub stars, Hyprland is growing fast, but Niri is starting to catch up.
Which is why I’ve been keeping an eye on
niri
, an emerging window manager that is doing for sliding windows what
Hyprland
did for tiling. It is less than three years old (Hyprland is about four), but has quickly grown in popularity,
doubling its GitHub star count
in the past six months.
Built around the Wayland compositor, the project basically is set up like a kit, one where you need to supply parts in the form of config files. If you like customizing, it may be the project for you. But if you just want to get stuff done, it might not feel like a welcoming experience.
Omarchy
, which we (controversially) covered a few months ago, exists because of this gap. People want the lightweight customizability of a window manager, but not the work of having to set it up.
To be clear, this is not far from where graphical interfaces for Linux and Unix variants started 40 years ago, but it’s arguably making a comeback because of a combination of sophisticated users and sophisticated tools. But not everyone has time to build their own config files from scratch.
My setup, combining Niri and the DankMaterialShell.
That’s where the project
Dank Linux
comes in. Pitched as a “modern desktop for Wayland,” it’s a set of “batteries included” tools to get you going in Niri or other window managers based on Wayland. Key to the project is DankMaterialShell, which combines a number of tools into one interface, along with the
Material design
approach. If Hyprland, Sway, niri and their ilk are attempts to deconstruct the desktop environment, Dank Linux tries putting it back together again.
Rather than relying on loose tools like
waybar
or
rofi
and bringing them together with a best-in-breed approach, DankMaterialShell comes with all the necessary tools already baked in. Plus, it’s highly extensible, and can be edited through a bunch of config files, just like all the really complicated tools. But unlike Omarchy, it’s not prescriptive—you’re not just having to work around one guy’s opinion of what your UX should look like for the rest of time. (Case in point: I don’t like borders or gaps around my windows, a typical trait of scrolling window managers. So … I just removed them.)
That’s because it’s built around
Quickshell
, a toolkit that has become very
popular as a modding tool
in the Linux community.
But some of us are normies who just want something that works. Hence why DankMaterialShell is making such a splash.
An example of the graphical interface for DankMaterialShell. It has many of the features of the GNOME setup, including the ability to arrange monitors, with a lean on UI.
The feature set for this software is surprisingly robust, and seems to be growing quickly.
DMS 1.2
, for example, has literally dozens of new features. And despite the fact that this tool is only about six months old, it already has a screenshot tool, numerous plugins, and a robust theming system. The momentum is clearly there. (It’s not alone, either—also covering the same territory is
Noctalia
, which promises a more relaxed aesthetic.)
The Dank Linux team offers a couple of optional utilities—the system overview tool DGOP and the MacOS Spotlight-like file tool dsearch—that can make the experience surprisingly polished.
The one downside of this is that Dank Linux isn’t really supported on Bazzite, the very popular distro I use. But after I mentioned I was interested in that, and I did some off-label testing on my end, one of the creators of
Zirconium
, a Dank Linux distro for Fedora, reached out. Turns out, they were already working on a “quick and dirty” image that got Bazzite working with Zirconium. (As reflected by the name,
Bazzirco
.) They even created a
Bazzite DX
version for me, so I could easily access my Docker containers from the thing.
(
Universal Blue
, the framework upon which Bazzite is based, allows you to make your own custom builds pretty easily. You can even roll back to other versions so you can switch between different builds at will. Think it’s gonna be a GNOME day? Switch to that image.)
There were some glitches here and there—for example, I found that turning variable refresh rate on for my laptop screen caused my external monitors to drag. Plus, running a “quick and dirty” build naturally means you’re going to run into some quick-and-dirty bugs. (I ran into some audio issues while running
Balatro
on the experimental distro. Not the end of the world. I signed up for this!)
Sure, you can retrofit this—albeit with common engine-swapping issues like broken keyrings—but I think the real magic might be starting fresh with it. Load it up on a new machine, set up your config to your liking, and get sliding.
But overall, this feels like a big step forward for desktop Linux—highly flexible, highly customizable, bleeding edge, yet somewhat approachable to normal people. I would go so far as to call it dank.
Sliding Links
The Muppet Show is
coming back
next week as a “backdoor pilot” for a potential series. Great—let’s hope it sticks this time! Over at
The Conversation
, there’s a great piece talking about the troupe’s lasting popularity.
YouTuber John Hancock
has one of the largest game collections known to man, having built complete game sets for numerous consoles, including the biggies. But he didn’t want it to live in a closet forever. He’s been trying to donate it or give it to a museum for years, and
this week he announced
that he did just that, splitting the collection up between two sources, a video game archive and a podcast.
It’s actually kind of a good thing
that Google’s forthcoming Aluminum OS, a combination of Android and Chrome OS, is kind of boring, based on
some early leaked interface video
. It means it’s going to be usable.
--
Find this one an interesting read?
Share it with a pal
!
Wanna see a shining example of a user interface? Check out
la machine
! It only does one thing, but it does it really, really well.
'}

---

*抓取时间: 2026-02-05 12:59:14*
