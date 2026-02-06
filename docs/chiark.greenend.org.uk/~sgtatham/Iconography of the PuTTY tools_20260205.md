# Iconography of the PuTTY tools

**来源:** https://chiark.greenend.org.uk/~sgtatham
**链接:** https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/putty-icons/
**日期:** 2025-03-12T00:00:00+00:00

---

# Iconography of the PuTTY tools

[Simon Tatham, 2025-03-12]

  * Introduction
  * Hand-drawn era
    * PuTTY itself
    * PSCP (and PSFTP): file transfer
    * Pageant: SSH agent
    * PuTTYgen: key generator
    * Configuration dialog box
  * Scripted era
    * pterm
    * Installer
  * SVG revamp
  * Thatâs all, folks!



## Introduction

In March 2025 I received an email asking about PuTTYâs âlogoâ â the icon used by the Windows executable. The sender wanted to know where it had come from, and how it had evolved over time.

Sometimes I receive an email asking a question, and by the time Iâve finished answering it, I realise itâs worth turning into a blog post. This time I knew it was going to be one of those before I even started typing, because thereâs a graphic design angle to the question _and_ a technical angle. So I had a lot to say.

PuTTYâs icon designs date from the late 1990s and early 2000s. Theyâve never had a major _stylistic_ redesign, but over the years, the icons have had to be re-rendered under various constraints, which made for a technical challenge as well.

## Hand-drawn era

When I first started drawing PuTTY icons, I didnât know I was going to need lots of them at different sizes. So I didnât start off with any automation â I just drew each one by hand in the MSVC icon editor.

### PuTTY itself

Expanded to a visible size, hereâs the earliest version of the original PuTTY icon that I still have in my source control. That means it was current in early 1999; my source control doesnât go all the way back to the very project start in the summer of 1996, but if it did, I expect this was _probably_ the same icon I originally drew. Iâd have drawn one quite early, because Windows GUI programs look pretty unhelpful without an icon.

![\[putty-original.png\]](putty-original.png)

![\[putty-original-bw.png\]](putty-original-bw.png)

The original PuTTY icon, in colour and in monochrome

Itâs 32Â ÃÂ 32 pixels, and uses a limited palette of primary colours and shades of grey. Thatâs because I started the project in the mid-1990s, when non-truecolour displays were very common. There was a fixed 16-colour palette recommended for use in icons, consisting of the obvious primary and secondary colours and dim versions of them, plus a couple of spare shades of grey. That way all the icons in the entire GUI could reuse the same 16 palette entries and not run the display out of colours. So this icon is drawn using that palette.

Providing a plain black-and-white version was another standard recommendation at the time. But I canât remember why â I certainly never actually _saw_ a computer running Win95 or later with a B&W display! My best guess is that the recommendation was intended for use with the âWin32sâ extension that would let 32-bit programs at least _try_ to run on Windows 3.1 (on suitable underlying hardware). Probably Windows 3 still supported black and white displays.

I donât think I thought about the design very much. I just dashed it off because I needed _some_ kind of an icon. The two computers are drawn in a style that was common in the â90s: a system box sitting under a CRT monitor, with a floppy disk drive visible at the right-hand end. Theyâre connected with a lightning bolt to suggest electrical communication between them. I didnât _believe_ I was being very original: I had the vague idea that several icons of this kind already existed (although Iâve never been able to find any specific example of what I was thinking of), so in my head, it fit with the general iconography of the day, and seemed as if it would be immediately understandable.

I canât remember why the lightning bolt was _yellow_. With hindsight that seems the strangest thing about it; cyan would have been a more obvious choice for electricity. Possibly it was just to contrast more with the blue screens of the computers.

Speaking of which â¦ I canât remember why the screens were blue, either. I _think_ I just intended it as a neutral-ish sort of colour which wasnât black, so that it was clear that the screens were turned on. Iâm pretty sure the blue _wasnât_ an allusion to the Windows Blue Screen of Death â that wouldnât make sense, because in a typical use of PuTTY, only _one_ end of the connection is running Windows, and neither end has crashed!

Looking back, I suppose I might also have considered making the two computers look different from each other, on the theory that the client machine might be sitting on someoneâs desk, and the server might be in a rack in a datacentre? But I was a student when I started writing PuTTY, and _my_ Linux server you could remotely log into was on my desk and not in a rack. So I think that just never even occurred to me.

### PSCP (and PSFTP): file transfer

In 1999, a contributor sent an SCP implementation, and PSCP was born. I decided to draw it an icon of its own.

It wasnât especially important for PSCP to have an icon at all. You donât run it _from_ a GUI (itâs useless without command-line arguments), so it doesnât need an icon for you to find it in Explorer or identify it in the Start Menu. And it doesnât put up GUI windows, so it wouldnât need an icon to identify those in the taskbar either. But I drew an icon anyway. I canât remember why. Maybe it was just for completeness, or I felt like doing a bit of drawing, or something.

I made the PSCP icon by modifying the existing PuTTY icon, replacing one of the two computers with a piece of paper with variable-length lines on it, suggesting a written document:

![\[pscp-original.png\]](pscp-original.png)

![\[pscp-original-bw.png\]](pscp-original-bw.png)

The original PSCP icon, in colour and in monochrome

I kept the lightning bolt connecting the remaining computer to that document, the theory being that you use PSCP to remotely access documents. (In some fairly vague sense.)

Later on, we gained a second file transfer tool, PSFTP, and I reused the same icon for that, on the basis that theyâre both file transfer tools and the icon doesnât really say anything specific to one of them. PSFTP is still a command-line application, but unlike PSCP, itâs possible to run it _from_ the GUI (by clicking on it in Explorer or the Start Menu), because it has an interactive prompt, so if you donât run it with any command-line arguments, you can tell it at the prompt where to connect to. So PSFTP put the same icon to a more practical use than PSCP did.

(On the other hand, giving two tools the same icon means you have to check carefully which one youâre dragging around in Explorer! Perhaps it would have been better to make the PSCP and PSFTP icons different in some way. But I couldnât easily think of a visual depiction of the ways the two tools differ.)

### Pageant: SSH agent

Pageant, our SSH agent, was the next tool in the suite that needed an icon.

My original idea for an icon depicting an SSH agent was to draw the face of a _secret_ agent â in the stereotypical outfit from the sillier end of spy fiction, with a wide-brimmed hat and a turned-up collar.

But Iâm terrible at drawing faces. After a few failed attempts, I realised that Pageant would never get released _at all_ if I waited until Iâd drawn the icon I wanted. So instead I took the secret agentâs hat â the only part which I _had_ drawn to my satisfaction â and simply sat it on top of a larger version of the computer from the original PuTTY icon, at a rakish angle.

![\[pageant-original.png\]](pageant-original.png)

The original Pageant icon

Iâd intended that as a placeholder, planning to come back and have another try later at drawing my original idea of a human secret agent. But then I realised the icon Iâd already drawn was simply _better!_ It fits visually with the rest of the suite by reusing the same computer design; itâs more appropriate because the âagentâ in question _is_ computerised rather than human. And most importantly of all, a computer wearing a hat turned out to be cute. So I kept it.

On the technical side: Pageantâs original icon _didnât_ come with a black and white version. I donât remember why not; perhaps, with Windows 3 a few more years in the past, it just didnât seem important enough any more. But on the other hand, Pageant introduced a new requirement: I had to draw a _small_ version of the icon. Up to this point Iâd just drawn everything at the (then) standard icon size of 32Â ÃÂ 32; but Pageant puts an icon in the System Tray on the taskbar, so it needed a smaller 16Â ÃÂ 16 icon to fit there. If you just let Windows scale down the 32Â ÃÂ 32 version, it didnât do such a good job of it.

![\[pageant-original-small.png\]](pageant-original-small.png)

Half-size version of the original Pageant icon

Drawing a small version of the same computer logo was a challenge, especially while still using that 16-colour fixed palette. You can see that Iâve done some tricks with the darker palette entries, âhand-antialiasingâ the hatband, and replacing the internal black outline at the bottom of the computer monitor with a dark grey one to try to make it less prominent â as if the original 1-pixel black outline had been scaled down to half a pixel.

(But the _external_ outline is still solid black, so that it separates the entire icon clearly from whatever background colour itâs shown on. The taskbar is grey, and so is most of the icon, so thatâs still important!)

### PuTTYgen: key generator

After that came PuTTYgen. I drew another âcomputer + lightning bolt + objectâ icon, this time with the other object being a key â a weak visual pun, since PuTTYgen generates and works with cryptographic keys.

![\[puttygen-original.png\]](puttygen-original.png)

The original PuTTYgen icon

The lightning bolt indicating network communication was particularly inappropriate in this tool. It was already fairly tenuous in PSCP, but PuTTYgen doesnât do any network communication _at all_ , so the lightning bolt was completely inaccurate. I really put it in there for visual consistency with the rest of the icons: itâs there to signal âthis is a tool from the same suite as PuTTYâ.

(Iâm still not _very_ happy with the drawing of the key.)

This icon is the other way up from the PSCP one: here, Iâve kept the computer in the lower left corner from the main PuTTY icon, and replaced the top right one with a different weird object, whereas in PSCP, I kept the top right computer and replaced the _other_ one with an object. I donât remember having any particular reason for that â perhaps I just didnât even bother to check which way round Iâd drawn the previous icon! But Iâm not too unhappy with it, because it makes the two icons more different from each other, so easier to tell apart.

### Configuration dialog box

The next icon we needed wasnât for a separate tool at all: it was for PuTTYâs configuration dialog box.

The taskbar entry for the config box had the boring âdefaultâ icon, just representing a generic window frame, that Windows uses for any window that doesnât supply a better one. Iâd decided that looked ugly.

Rather than just reuse the main PuTTY icon unmodified, I drew an icon to specifically represent configuration or modification, by overlaying a large spanner on top:

![\[puttycfg-original.png\]](puttycfg-original.png)

![\[puttycfg-original-bw.png\]](puttycfg-original-bw.png)

The PuTTY configuration dialog icon, in colour and in monochrome

For this icon I went back to including a monochrome version. I canât remember why. Perhaps it was just that I was modifying an existing icon which _did_ have a monochrome version!

## Scripted era

Nothing else happened in this area until 2007.

That was about when people started to complain that the 32Â ÃÂ 32 pixel icons had started to look nasty. Displays had become bigger, and Windows was defaulting to displaying 48Â ÃÂ 48 icons instead of 32Â ÃÂ 32. So if your application only had a 32Â ÃÂ 32 icon, Windows would stretch it.

It wouldnât have looked great if a 32Â ÃÂ 32 icon had been magnified by an exact factor of 2 to 64Â ÃÂ 64, copying each input pixel the same number of times. But 48 isnât even a multiple of 32, so instead Windows had to stretch my icons _unevenly_ , which looked even worse.

Rather than hand-draw another full set of icons, I decided to get more ambitious. So I wrote a piece of code that drew all the components of each icon image in a programmatic way, so that I could run the script to auto-generate a full set of icons for every tool. That eliminated the inconsistency about which icons had tiny versions, and which ones had black and white versions: now _all_ the icons had _all_ versions.

The hard part of that was the tiny 16Â ÃÂ 16 icons. Iâd only drawn one of those so far, for Pageant. Now I had to try to capture the artistic judgment Iâd used for the âhand-antialiasingâ in that icon, and try to make a piece of software do the same thing for _all_ the graphical components of the icon suite.

I remember that being pretty hard work, but in the end I managed to make something I was happy with. After that, _every_ icon had 48Â ÃÂ 48, 32Â ÃÂ 32 and 16Â ÃÂ 16 icons.

![\[putty-script-48.png\]](putty-script-48.png)

![\[putty-script-32.png\]](putty-script-32.png)

![\[putty-script-16.png\]](putty-script-16.png)

![\[pscp-script-48.png\]](pscp-script-48.png)

![\[pscp-script-32.png\]](pscp-script-32.png)

![\[pscp-script-16.png\]](pscp-script-16.png)

![\[pageant-script-48.png\]](pageant-script-48.png)

![\[pageant-script-32.png\]](pageant-script-32.png)

![\[pageant-script-16.png\]](pageant-script-16.png)

![\[puttygen-script-48.png\]](puttygen-script-48.png)

![\[puttygen-script-32.png\]](puttygen-script-32.png)

![\[puttygen-script-16.png\]](puttygen-script-16.png)

![\[puttycfg-script-48.png\]](puttycfg-script-48.png)

![\[puttycfg-script-32.png\]](puttycfg-script-32.png)

![\[puttycfg-script-16.png\]](puttycfg-script-16.png)

A full set of icons generated by the script

I stopped short of trying to make the program recreate _every_ decision Iâd made in the original drawing. I made quite a few of those decisions in a hurry without much thought, after all. So I just got the script to a point I was happy _enough_ with. And I took the opportunity to improve on a few things: for example, _all_ versions of the Pageant hatband are now antialiased, not just the tiny version.

But there are other ways that the scripted icons donât _exactly_ match the original hand-drawn versions. The radio buttons below should let you flip back and forth between two example icons in the original and script-generated versions:

Original![\[pair-originals.png\]](pair-originals.png) Scripted![\[pair-script.png\]](pair-script.png)

![](double-icon-spacer-32.png)

Use the radio buttons to switch between the original PuTTY and Pageant icons and the 32Â ÃÂ 32 output from the script

The actual PuTTY icon is a pretty close match â only a small number of pixels changed. But the Pageant icon is quite different: apart from the deliberate change of the antialiased hatband, the computer in the icon isnât even the same _size!_ I canât remember if that was a pure accident (maybe I didnât flip back and forth between the two versions of that icon while I was writing the script), or a deliberate style change.

(Of course, if Iâd _wanted_ to change the size of the computer, it would have been easier to do it using the script than redrawing by hand. So it would have made sense for it to be a deliberate change, now that the opportunity was available. But I donât remember that it _was_ deliberate.)

As I said earlier, I made sure the script could generate a full set of black-and-white icons too, just in case. In 2007 I think it was even less likely that anyone would still be running Windows (or anything else) on a B&W display, but one of the nice things about having this stuff done by a script is that you can get it to do a lot of hard work for you just in case. So now I have a full set of black and white icons too, even at the new size of 48 pixels:

![\[putty-script-48bw.png\]](putty-script-48bw.png)

![\[pscp-script-48bw.png\]](pscp-script-48bw.png)

![\[pageant-script-48bw.png\]](pageant-script-48bw.png)

![\[puttygen-script-48bw.png\]](puttygen-script-48bw.png)

![\[puttycfg-script-48bw.png\]](puttycfg-script-48bw.png)

All five icons, in black and white, at 48 pixels

### pterm

In 2002 I had ported a lot of the PuTTY code to Linux. I wrote a Linux version of the full GUI PuTTY application, and also reused part of the code as an X11 terminal emulator `pterm` which you could use in place of existing ones like `xterm`.

Linux GUI applications can also have icons if they want to: an X11 program can set a property on its window, containing a bitmap to be used as its icon. Window managers vary in _what_ they use this for â they might minimise the whole window to an icon in Windows 3.1 style, or display the icon in a taskbar entry in the style of more modern Windows, or display the icon somewhere in the applicationâs window frame, or anything else they can think of.

I hadnât done anything about this in 2002, partly because as far as I knew the toolkit library I was using (GTK 1) didnât support setting an icon on the window, and also because it would have been a pain to provide the same icons in multiple bitmap file formats.

But now that I was generating the icons from a script, it was suddenly much easier to make the script output multiple file formats. Also I found out that GTK 1 _did_ let you set an icon property after all. (In any case, I already knew GTK 2 could do that, and was planning an upgrade to that.) So, for both reasons, it was now practical to provide icons for the X11 versions of the PuTTY tools.

So I had to draw an icon for `pterm`, which didnât already have one!

This time, I really did run out of imagination. Since `pterm` doesnât do any network communication, I simply drew an icon consisting of _just one_ copy of the same computer logo seen in all the other icons, expanding it to the full size of the icon image. (A little bigger than it was for Pageant, since this time it didnât have to fit under a hat.)

`pterm` also has a configuration dialog box, so I made a separate icon for that, reusing the same spanner overlay from PuTTY proper.

![\[pterm-script-48.png\]](pterm-script-48.png)

![\[ptermcfg-script-48.png\]](ptermcfg-script-48.png)

The icon for `pterm`, and its configuration dialog

_Much_ later, in 2021, it became possible to write a version of `pterm` that would run on Windows, and act as an alternative GUI container for an ordinary Windows `cmd.exe` or Powershell session. This icon became the one for Windows pterm as well, once that happened.

### Installer

The flexible icon-drawing script also let me support true colour icons as an extra output mode, so I wasnât limited to the old 16-colour palette any more.

That came in handy when I needed an icon for the PuTTY _installer_. I thought it would be nice to draw a cardboard box as part of that icon, with the flaps open at the top and a lightning bolt coming out of it pointing at a computer, suggesting âPuTTY is zapping out of this box on to your machineâ. Cardboard boxes are brown, and brown wasnât in the 16-colour icon palette â but now we werenât limited to that palette any more, so I could draw a true-colour icon using _actual_ brown!

But I still wanted to support the 16-colour icons, because I never like to throw away backwards compatibility if I can avoid it. And I noticed that you could make _several_ acceptable shades of brown by taking two different colours in the old Windows 16-colour icon palette, and mixing them 50:50. All my mixes involved the dark red (`#800000`); I got three different browns, or brown-enough colours, by mixing it with black (`#000000`), dark yellow (`#808000`), and full yellow (`#ffff00`).

So I made the cardboard box out of those three 50-50 mixes, using them all to show that different parts of the box were at different angles to the light. That way, in the true-colour icon I could use a single colour that was the mean of the two old colours, and in the 16-colour version I halftoned it by alternating pixels of the _actual_ two old colours.

![\[puttyins-script-48tc.png\]](puttyins-script-48tc.png)

![\[puttyins-script-48.png\]](puttyins-script-48.png)

The PuTTY installer icon, in true-colour and halftoned versions

## SVG revamp

My icon-drawing script works well at the ordinary 32Â ÃÂ 32 and 48Â ÃÂ 48 sizes, and scales _down_ to 16Â ÃÂ 16 reasonably well, but it doesnât work so well when you start scaling _up_.

So, if anyone needs _really big_ versions of the icons, generating them by just running the same script with a bigger image size wonât produce very nice output. In one of my failed attempts to port PuTTY to the Mac, I found that MacOS wanted a 128Â ÃÂ 128 icon to use in the dock, and the output of my script at that size was definitely not great.

Iâve more or less given up on that Mac port now, but I thought that a fully scalable version of all the icons might still be a useful thing to have around. For one thing, it allows using them in contexts other than GUI icons. (Gratuitous merch, anyone? T-shirts? Laptop decals? 🙂)

So, partly âjust in caseâ but also for fun, Iâve been working on a second icon-drawing script. It mimics the same âthought processesâ of the original script, but it outputs SVG files instead of bitmaps â keeping the artwork still as close as possible to the original style.

As of now, these are my best efforts at the SVG versions:

![\[putty.svg\]](putty.svg)

![\[puttycfg.svg\]](puttycfg.svg)

![\[pterm.svg\]](pterm.svg)

![\[ptermcfg.svg\]](ptermcfg.svg)

![\[pscp.svg\]](pscp.svg)

![\[pageant.svg\]](pageant.svg)

![\[puttygen.svg\]](puttygen.svg)

![\[puttyins.svg\]](puttyins.svg)

All eight icons, in fully scalable SVG

For the tiny icons, I still think my original script is doing a better rendering job, because SVG has no idea at all how best to do that antialiasing. But for _large_ icons, especially in true colour, I think my recommendation is going to be to base them on these SVGs â just render to a big bitmap.

## Thatâs all, folks!

Thatâs the history and the current state of the PuTTY icon set.

People sometimes object to the entire 1990s styling, and volunteer to design us a complete set of replacements in a different style. Weâve never liked any of them enough to adopt them. I think thatâs probably _because_ the 1990s styling is part of what makes PuTTY what it is â âreassuringly old-fashionedâ. I donât know if thereâs _any_ major redesign that weâd really be on board with.

So I expect by now weâre likely to keep these icons, or something basically the same, for the whole lifetime of the project!
