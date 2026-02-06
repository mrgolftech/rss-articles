# Policy of transience

**来源:** https://chiark.greenend.org.uk/~sgtatham
**链接:** https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/transience/
**日期:** 2025-05-09T00:00:00+00:00

---

# Policy of transience

[Simon Tatham, 2025-05-09]

  * Introduction
  * The habits
    * Turn off persistent shell history
    * Clear my GUI desktop regularly
    * Close my entire web browser frequently
    * Turn off X11 session management
    * Use a tmpfs on `~/mem` as my main scratch space
  * Policy of transience
  * Other related practices
    * Corporate records management: scheduled deletion of email
    * Automated operating system setup from a recipe
  * Exceptions to the policy
  * Conclusion



## Introduction

I have several habits in my computer usage which are unusual by many peopleâs standards (although some more so than others), and which all kind of point in the same direction.

At the time I adopted each one, I didnât recognise this. Each habit seemed desirable in its own context for one reason or another, but it wasnât a lot later until I spotted the common theme running through them all. The theme wasnât always the reason I adopted the habit in the first place â but I think itâs the reason Iâve _kept_ all these habits, after trying them out for some other reason.

In this article Iâll describe the habits Iâm thinking of, and the more general idea that theyâre all instances of, which I now think of as a âpolicy of transienceâ.

Iâm not trying to persuade anyone else that they should adopt this general policy, or even any of the specific habits. I just put the ideas out here in case theyâre of interest, for people to consider, and decide _whether_ theyâd find any or all of it useful. If any of this is useful to you, great â and if you decide itâs not for you, thatâs fine too.

## The habits

Hereâs a list of the habits that I now classify under the general heading of âpolicy of transienceâ. I _think_ these are in roughly chronological order of me adopting them, though itâs hard to be sure.

### Turn off persistent shell history

I use the Linux command line, specifically `bash`. Like many other modern Unix shells, `bash` keeps a history of the commands youâve typed, so that you can recall them and run them again, or modify a previous one slightly to do a new thing.

This can be used in the immediate short term: type a command, it doesnât quite work, recall it and edit one typo, try again. But it can also be useful over the long term: recall a command you ran last week, or last year, or that thing you do about once a month. To support the long-term uses of this feature, `bash` saves your shell history to a file when you exit the shell (by default `~/.bash_history`), and reloads that file when it starts up. So you can still recall a command even if youâve logged out or rebooted the whole machine since running it.

Many people find this persistent history feature very useful, and go to some lengths to improve it further â you can configure a larger number of stored commands, some shells will sync their history constantly instead of just on exit, there are plugins to help you search it more easily, and so on. The general view seems to be: shell history is good, more and easier-to-use history is even better.

But I go the opposite way. My unusual habit is: **turn off the history file completely** , by putting the command â`unset HISTFILE`â in my `.bashrc`. I still get history within a single instance of the shell, so I can edit my last command ten times until it works properly; but history isnât shared between my terminal windows, or preserved when I log out and log in again. _All_ the shell history I allow myself is localised and short-term.

I started doing this very early in my Linux-using career, very soon after I found out the history file existed in the first place. I think my initial motivation was an extremely vague privacy concern: it just felt _creepy_ that my shell would be remembering that much detail about stuff Iâd done in the past.

There are certainly valid _specific_ privacy concerns about shell history. Sometimes you write an actual secret, such as a password, on a command line by mistake. (Oops, had focus in the wrong window.) And sometimes you just have to hold your nose and put a secret on a command line on purpose, because some badly designed tool wonât let you pass it in any other way. (Thatâs already a danger, of course, because other users of the system can see it in `ps` â but itâs one thing to take that risk very briefly while the command is actually running, and quite another to have a copy of the secret preserved in `~/.bash_history` for months or years.) But I donât think I had anything that specific in mind to begin with: I just felt generically uneasy with the idea.

(Of course, if you _know_ youâve just written a secret on a command line, you can delete the command from that shellâs history on purpose, before it gets saved to the file. But if you did it by accident, you might not realise you need to; and if you had to recall the command and retry it a few times, you might not manage to clean up every instance of it.)

But after I adopted this policy, and put â`unset HISTFILE`â in the standard snippet of `.bashrc` that I share between all my Unix accounts, I found it had another benefit: it forces me to keep things more organised.

If I type a shell command thatâs _valuable_ â one that did something useful enough that I might want it again in future, and long and complicated enough that Iâd be annoyed to have to figure it out a second time from scratch â then I canât rely on it just happening to be in my `.bash_history`. So instead I put it somewhere else: maybe a shell function in my `.bashrc`, or maybe a shell script in my directory of random useful scriptlets. Or maybe just in a file of notes jotted down to myself about useful shell runes to remember.

I find this a more useful way to remember shell commands. Firstly, this procedure separates the _working_ version of the command from all the failed attempts just before it. Even within the context of one instance of `bash` Iâll sometimes accidentally recall a _wrong_ version of a command when I was aiming for the corrected one two commands later; the idea of having a _yearâs worth_ of my own false starts available for accidental recall seems horrifying! Instead, I deliberately save _just_ the working version, and let all the failed attempts go in the trash when I close the shell.

Secondly, when I save a command on purpose in any of these ways, I give it a name, and write a comment explaining what it was useful for, and what I might find it useful for again. And most likely I commit it to one of my small personal Git repositories, so that it stays around, is shared between my machines, and I can keep it up to date later if it doesnât quite work in some new context.

Of course, this means itâs more effort at the moment I _do_ save the command for later. But my impression is that the effort pays off in the long run.

### Clear my GUI desktop regularly

I mostly donât stay logged in to a single GUI session for months on end.

(This is probably one of the _less_ unusual things on the list, but this is where it appears in the chronological order of me adopting the habits.)

I turn laptops completely off more often than I suspend them. I see suspending as a tool for very temporary pauses in what Iâm doing: if I was using my laptop on a train and now I have to get up and change to another train, that seems like a good use for a 20-minute suspend. But when I reach my final destination, Iâll shut the laptop down completely. I never leave a laptop suspended overnight (except by mistake).

Machines that also function as remote login servers, or build machines, or both, have to stay on. But even there, I donât like to leave a single login session live for a long time. In years when I have an office desktop machine (though right at the moment Iâm using a laptop), Iâll log in at the start of the day and log out before going home, rather than just locking my screen and leaving all my windows there until the next morning.

Even if I donât actually log out of a machine on a daily basis, Iâll `apt upgrade` it on a daily basis, and reboot _promptly_ if `apt` tells me I need to, like because itâs installed a kernel update â Iâm not one of those people who leaves a reboot pending for months because of all the stuff in my open windows that I donât want to lose. So nothing I run will normally have an uptime of more than a couple of weeks. And more often than _that_ , even if I donât actually log out, Iâll close all my open applications, clear the desktop, and start again from scratch.

Of course, this adds a bit of effort to my morning routine when I power up a machine, log in, and start doing something with it. I minimise that by having a streamlined workflow for opening the usual applications I use â a mixture of keyboard shortcuts (I donât have to click through the GUI start menu for any of my usual tools) and smart window-manager configuration (my WM places the windows automatically in the locations I prefer).

Why did I start behaving like this? I think itâs more that I never _stopped_ behaving like it. When I was a child, the computers in the house were shared with other family members, so you couldnât leave your session running for ages, because someone else wanted to use the machine. âSuspendâ and âSwitch Userâ werenât a thing on that generation of computers. And there wasnât usually any point leaving a machine on all the time, because it wasnât connected to the network, so it wouldnât be doing anything useful.

But I do have some more specific reasons not to want to leave a session, or even a particular pile of terminal windows, running forever.

One reason is that itâs a defence against accumulated state changes. In a particular terminal, I might have messed about with environment variables like `PATH`, and then that terminal isnât in its default state any more. Probably I did that because it was sensible for a particular thing I was using that terminal window for. But if I forget Iâve done it, and reuse the same window for something else, then the leftover state could confuse me. In the _good_ case, something I wanted to do doesnât work. In the bad case, something I try _does_ work, which wouldnât work in the terminalâs default state, and then I put it in a script (or worse, send it to somebody else) and it unexpectedly fails later when it runs in an unmodified environment! For this kind of reason, Iâll often avoid using the same terminal window for two unrelated projects: itâs a habit to ^D the window and open a fresh one in the same screen location if Iâm going to stop working on (say) PuTTY and start working on (as it might be) my puzzle games.

But another reason is: I find closing all my applications regularly imposes a useful discipline on me. If Iâm still half way through some coding when I shut my laptop down (for example because the train has arrived), then _because_ Iâm about to shut it down, Iâll make sure to leave it all in a good state: make local git commits from my work, write some notes to myself about what I still have to do, and generally make sure that when I next boot the laptop up and try to resume what I was doing, I can remember what it was and where Iâd got to. This clarifies my thoughts in any case, and allows me to come back with a fresh mind next time, re-read my notes, and maybe have new ideas.

It also helps transferrability between machines. After I make those git commits of my half-finished work, Iâll often push them to another machine (at least if I have networking at the time). Partly thatâs a defence against data loss. But also, if the next time I work on the same thing is on another machine like my home desktop, I can pick up _there_ where I left off on the laptop. If all my working state was contained in the laptopâs GUI session, Iâd _have_ to keep working on the laptop, even if Iâd got back home where I have a bigger display.

### Close my entire web browser frequently

In the previous section I mentioned that I close _all_ my GUI applications frequently, including the web browser. But it goes further than that: I close the web browser much _more_ often than I close the terminal and editor windows alongside it.

A lot of the time, if Iâm working on something like coding, I donât have a browser open at all. If I need to refer to web-based documentation, as often as not Iâll have to start Firefox up from scratch in order to do it. I might open a handful of tabs as I follow hyperlinks, but when Iâm done, Iâll make the effort to close those tabs, and ideally, close the whole browser.

One thing I _donât_ do is to use the open browserâs list of tabs as a long-term to-read list. (Not even âto read over the course of todayâ, much less over weeks.) I know thatâs a common way that many people use browsers, to the extent of needing browser plugins or extensions to help manage hundreds or thousands of tabs. If I ever have 100 tabs open in a browser, itâs because I opened them all in rapid succession for some immediate purpose (either with a script, or by clicking every hyperlink on a large index) and Iâm about to go through them all right now looking for whatever I was after, and then close them again as quickly as possible to get rid of the horrible mess.

Why do I work this way? Again, one reason is that it made sense a couple of decades ago when machines were smaller â your browser consumed memory which you wanted to use for something else, so youâd only have it open when needed. So this is _somewhat_ a 1990s habit that I never bothered to change.

But, again, I have some more specific reasons too. One is my cookie-management policy. I configure Firefox to delete _all_ cookies when I close the browser, apart from a very small number of sites I configured as exceptions. That seems to me like a good balance between allowing all cookies (everything tracks you everywhere) and refusing cookies completely (some sites donât even work). This way, my browser _accepts_ the cookies for some website I want to use, so nothing actually fails to work â but the next time I use the website, the browser has no memory of them. But this only delivers a privacy benefit if I didnât leave the browser running between those visits, and closing the whole browser many times a day is a good way to do that.

And the other effect of not using my tab bar as my to-read list is that if I _do_ want to maintain a to-read list, I have to do it some other way â and that way will likely involve writing the URL down somewhere, with a reminder to myself about what it was _for_ , maybe where I got it from, and (if applicable) what I planned to do with the page when I got to it.

(Even with only a handful of tabs and a short time lapse I can be quite absent-minded about that last part! For websites like my employerâs CI system, which I might want to open for lots of different detailed reasons, itâs not at all unusual for me to open a tab with a specific intention, get to it two minutes later, and have forgotten what I wanted it for. Remembering the point of a URL after a week is right out.)

### Turn off X11 session management

At some point in my Linux-using career, desktop environments introduced a feature to save the layout of your desktop on logout â which applications you had open, where each oneâs windows were on the screen, and what each one was doing. The _idea_ is that even if you have to log out, power down, and log back in again when you next turn the machine on, you can still pick up where you left off.

I expect this might work all right, if youâre the kind of computer user who mostly runs office-suite applications. You could certainly imagine that a word processor or a spreadsheet application would be able to record the important aspects of its working state in very little information â âI had a window _this_ size, _here_ , editing _this_ document [specified by pathname], with the viewport showing _this_ section of the document, and the cursor right _here_ â â and set all of that back up when restarted with the right option.

But if youâre mostly a terminal user, who uses the GUI as a convenient way to switch focus between half a dozen shell prompts and maybe the occasional text editor or web browser, itâs hopeless. Thereâs no possible way to save the state of a shell session so that you can pick it up where you left off the next day. Or rather, there is, but it involves saving the complete internal state of all processes involved â in other words, hibernating the machine rather than shutting it down. And some things, like an SSH session, wouldnât even survive that.

For this reason I turned off session management as soon as I encountered it. I couldnât see the point of respawning _half_ my windows, and not only that, the half that werenât that hard to recreate by hand.

(Iâve also never got round to implementing the application side of the session management API in any of my GUI software. It wouldnât make much sense in PuTTY or `pterm`, for the reason Iâve just mentioned, but my puzzle collection could support this much more easily. However, nobodyâs ever complained about the lack of it.)

You can probably guess what the running theme is going to be by now: because I donât rely on the system to restart everything in the same state I left it, I have to make an effort to remember myself what that state _was_. Ideally, this is done by making the state simple in the first place, like finishing up a task completely and not starting the next. If I do have to leave a thing half done (and Iâm not just doing a quick reboot and getting right back into it), Iâll write down some notes to myself to remind myself where Iâd got to. And if the half-done thing was relying heavily on a particular terminalâs shell history (like I kept recalling some complicated test command to re-run after each build), that command too is copied into my notes, or into a tiny `test.sh` file, or some such, so that itâs still available when I start a fresh terminal after the next boot.

### Use a tmpfs on `~/mem` as my main scratch space

When I first got a machine with an SSD instead of an old-fashioned spinning-rust hard disk, I had heard of SSD wear, and I was a bit worried about it, but I wasnât quite sure _how_ worried I ought to be, and wanted to err on the side of caution.

I happened to be working on something at the time that involved a lot of vigorous disk access in every run, _and_ needed to be run a lot of times. (It involved databases, so it was doing a lot of `fsync`. I was only ever planning to run it once on _live_ data â it was a one-time format conversion â but I had to run it again and again on test data until I got it right.) I didnât want my first act as an SSD user to be wearing the whole thing out in the first week by running that unfinished program too many times.

My computer at the time had enough RAM that I was able to solve the problem by simply making a Linux âtmpfsâ â a filesystem backed only by RAM (and swap if you have any enabled), which vanishes on reboot, or even on umount. I just ran a pair of commands along the lines of
    
    
    mkdir ~/mem  
    sudo mount -t tmpfs -o size=32g none ~/mem

and then I did all my test runs of that disk-heavy conversion tool in there, so it wouldnât be writing to my nice new SSD at all.

Once this exercise had given me the idea of mounting a tmpfs inside my home directory, I thought Iâd leave it around for a while, because I could see other ways it might be useful. I ended up keeping it as a permanent part of my workflow, and now Iâve set up the same arrangement on all the Linux machines where I have root.

In particular, I often want to download some piece of softwareâs source code (via `git clone`, `apt source` or just downloading and unpacking a tarball), in order to find out one tiny thing about it. Usually, once Iâve done that, I donât need the source code any more â but at the moment Iâve answered my initial question, Iâm never _quite_ sure of that, so Iâll leave it around in case I want to know something else half an hour later. And then of course I forget to delete it.

I used to do that kind of thing in `~/tmp`, which was (and is) an ordinary persistent directory on my disk. Of course it gradually got more and more full of source trees I downloaded once and never used again, and other similar kinds of clutter, like large data files Iâd generated, `strace` logs, etc. Going through and cleaning up `~/tmp` was a chore every so often to stop my disk filling up.

But it never happens to me any more, because now I put all those one-off downloads and log files in `~/mem`, and they automatically vanish on the next reboot.

(I still have a `~/tmp`, but now itâs used for _less_ temporary things â stuff that might need to persist for a week or two and survive a reboot, instead of the next half hour. I deal with the cleanup issue by datestamping most of its subdirectories, so I can see at a glance that something was from last year or last decade and guess itâs not needed any more.)

Of course, the flip side of this is that I risk losing data I actually wanted to keep. But when I put a file or a source tree in `~/mem`, I _know_ thatâs what Iâve done, so I keep an eye open for any reason I might want to keep it. And if I do want to keep it, I donât just migrate it to `~/tmp` with the same throwaway name: I think of somewhere more organised to put it, and give it a more sensible name, and maybe write myself a README about what I wanted it for. That would be a huge effort if I did it for _every_ one-shot download, but itâs not so bad at all if I only do it for the small number of things I promote out of `~/mem` to persistent storage.

## Policy of transience

The common theme between all of those habits is probably obvious by now, but Iâll state it more formally anyway.

I consider all of these habits to be instances of a general âpolicy of transienceâ, which says: **things should either be _deliberately_ permanent in an organised way, or strictly temporary**. I dislike things _accidentally turning out_ to last for ever.

All the habits Iâve described above can be seen through this lens:

  * My shell history is either temporary (vanishes when I close that shell), or deliberately permanent (saved a command in a script with a name and an explanation).
  * A cluster of related applications on my desktop, like a terminal and a text editor and a `gitk` or something, is either temporary (I close the whole lot frequently and in any case it goes away when I log out or reboot), or deliberately permanent (if I keep wanting the same cluster a lot then I make hot keys and short command aliases to restart it any time I want).
  * Files on my computer are either temporary (because theyâre in `~/mem` which will be emptied on the next reboot), or deliberately permanent (in a sensible directory so Iâll know where to find them again, and with an explanation if needed).
  * URLs I want to do something with are either temporary (in my browser, which I keep closing down completely) or deliberately permanent (saved somewhere else, again with an explanation).



The idea of making things deliberately permanent âin an organised wayâ is fairly vague. Some things I think are often important (although not all of them apply in every case):

  * _Stored somewhere reliable_. If Iâm going to make something permanent, it should live somewhere thatâs properly backed up. Even worse than a temporary thing accidentally becoming permanent is a permanent thing accidentally becoming temporary: thatâs called âdata lossâ, and we hates it, preciouss.
  * _Easy to find_. It should be named in a way that matches how I expect to look for it later. Iâve had some remarkable successes with this, sometimes finding a 15-year-old item exactly where I expected my past self to have left it. Iâve also had some spectacular failures, and I know which I prefer to encourage!
  * _Explained_. If I find it in passing while looking for something else, I shouldnât need to scratch my head and wonder what itâs there for.
  * _Change-controlled_. If itâs evolved over time, it should be possible to remember how it changed and what all the changes were for, typically by keeping it in version control.
  * _Portable_. If itâs going to be long-term useful to me, itâll probably be useful on more than one machine, so I should be able to transfer it between machines: it should live in a git repository or something like that, and should have minimal (and ideally documented) dependencies on stuff provided by the host machine.
  * _Usable by other people_. I havenât talked about this aspect much, because most of my examples above have been about my personal workflow. But âsave that useful command in a scriptâ, taken one step further, becomes âwrite a man page for the script and publish itâ, and that can be useful too! In the next section Iâll mention another case where this comes up.



## Other related practices

In this section Iâll mention a couple of practices that other people do, which also seem to me as if theyâre in line with this policy of transience. I donât impose these on myself personally (although in one case Iâm considering it), but theyâre relevant.

### Corporate records management: scheduled deletion of email

Some companies have an internal policy of deleting all email older than some specified age (say, a year).

The usual reason, as I understand it, is related to the âdiscoveryâ stage of a lawsuit, in which (in some circumstances) the opposing company gets quite far-reaching rights to dig out stuff from inside your company like internal emails, and try to find evidence supporting their case. Even if they donât find the evidence they wanted, they still get to find out lots of _unrelated_ stuff from those emails, which could be disadvantageous to you even if they lose the actual lawsuit. For both reasons, the less there is for them to dig up in the first place, the better.

Of course, if you hastily deleted all your email _after_ a lawsuit started, that would be obviously illegal destruction of evidence. So the idea is to have a fixed policy in advance, and follow it, so that you have defensible grounds for having deleted relevant emails: âweâve been doing that all along on the same schedule, itâs our standard policy, it had nothing to do with you suing usâ. Even so, you probably have to suspend your one-year deletion policy while a particular suit is ongoing. But at least this way, when the lawsuit starts, they only have one year of dirt from _before_ the start date to dig up.

I donât know that I approve of this in general, either ethically or from a systems-design perspective. (Surely if the discovery rules have over-broad scope, or whatever it is, then thatâs a problem that should be fixed rather than worked around?) But just like a lot of my own habits above, a policy adopted for one reason can have unrelated side benefits.

If youâre in an organisation which subjects you to this policy, what do you do? Your email archive probably has actually useful information in it, and if you have to delete it after a year, youâll lose stuff you wanted to keep.

So you get into the habit of _knowing_ that things in email are temporary, and if you receive any particuarly useful-looking information in email, you make an effort to put it somewhere else more sensible. And, just like all the other cases above, you put it in a well-thought-out location, directly related to its subject matter. That makes it actually _easier_ to find later than if you had to dig it up in your email by a vague memory of who had sent it to you.

(I donât think this violates the spirit of the records-management doctrine from the companyâs point of view. The kind of thing Iâm thinking about saving here is more in the area of âuseful coding and debugging tipsâ or âhow to do some complicated thing with that internal web systemâ, not âjuicy gossip about who claimed who had violated whose IP rightsâ!)

In a corporate environment, another thing youâre probably concerned about (or should be) is reducing âbus factorâ: there shouldnât be any important task that only one person can do, or important information that only one person knows. Thatâs another reason why keeping useful stuff in your disorganised email archive is a bad idea: if youâre on holiday the day someone needs to know that crucial fact, or have completely left the company, maybe nobody else has that email saved to look it up in. So when you copy useful information out of an email you just received, you might also make the effort to copy it to somewhere _shared_ , like your teamâs wiki, or a git repository full of documentation, or whatever your organisation uses for that kind of thing. The scheduled deletion policy helps to encourage that, because once itâs forced you to move the useful information _somewhere_ , itâs not a lot more effort to put it somewhere shared than somewhere private. (Perhaps even _less_ effort.)

I donât adopt this practice for my personal email, though! Itâs one thing to have it imposed on you by an employer and look for the silver lining, but I wouldnât do it on my own initiative.

### Automated operating system setup from a recipe

Another kind of data thatâs not well organised and lasts a long time is the configuration of a specific computer. On Linux, Iâm thinking of all those files you found reasons to edit in `/etc`, over the course of years, probably forgetting half of the changes you made a week after youâd done each one; the precise set of distro packages you installed, and why; the stuff you did with `update-alternatives` or similar; and so on. On Windows itâd be Control Panel settings and registry tinkering, the set of applications youâd installed from all over the place (on Windows itâs less likely itâs all come from the same place, unless you use nothing but the Store). And on both OSes the applications themselves may maintain ongoing state of some kind, in `/var` or wherever the Windows analogue is.

Of course, you back the whole system up, if itâs important to you. But that seems like a wasteful way of doing things. It would surely be possible in principle to _describe_ the configuration of any one of my computers in a small text file, along the lines of âstart from version [_n_] of [distro], install [list of packages], make [these] changes to config files, run [this] set of `mkdir`, `chown`, `chmod` commands etc and [that] set of `update-alternatives`â. A file like that would contain all the important details of what the system is like, and youâd be able to manage it much more easily. It would take up Kb rather than Gb; youâd keep it in version control; and you could lay out the file itself in a way that was easy to read, with each cluster of related changes (even if they were in different config files) kept together with a comment explaining what theyâre there for.

In the containers world, thereâs a thing exactly like this: the Dockerfile. (Personally I use [Podman](https://podman.io/) in preference to Docker itself, because of the really nice rootless mode, but the Dockerfile format is common between the two.) I keep a collection of rarely-used OS configurations in the form of Dockerfiles for various purposes, such as the very minimal Kerberos installation I occasionally boot up to test PuTTYâs Kerberos integration; itâs convenient not to have the fully installed version of that system taking up space all the time, and itâs also nice that every time I remake it fresh I know it matches the config file, and hasnât gradually diverged over years of accidentally-undocumented tweaking.

But I donât run my _physical_ machines in this way. Those are installed in a more conventional way, and are subject to exactly this problem â if I did have a total backup failure and had to reinstall one of my machines completely from scratch, Iâm sure it would be months before I stopped tripping over missing packages or confusingly different behaviour and got the system back to more or less how it had started out. If I could even remember.

(Iâm mostly talking about _systemwide_ configuration here. Home directories are a separate consideration, although an individual userâs collection of dotfiles has some of the same properties. Iâm more on top of that side of things: I do have an organised git repository containing some of my standard dotfiles, and scripts to set up the configuration I like in others.)

I think this has something to do with the metaphor Iâve heard here and there of treating computer systems âas cattleâ â relatively interchangeable and somewhat disposable â rather than âas petsâ, where you have an ongoing relationship with a single one and if it died it would be like losing a member of your family.

Iâm vaguely aware that there _are_ methods of managing physical computer systems via configuration files of some kind. Words like âAnsibleâ and âPuppetâ spring to mind. But Iâve never gone to the effort of learning one and deploying it in my personal computing infrastructure. I keep toying with the idea, though. My firewall machine in particular has been reinstalled from scratch at least twice more than is reasonable (though because it changed CPU architecture, rather than because the backups failed). Even if I only converted _that_ machine into a tiny config file of some kind, itâd be a win. The bigger things like desktop boxes could come later.

Another advantage of managing machines this way is that it would be easier to rearrange roles later. If I have a machine that currently does two separate jobs, and later I decide there should be a separate machine for each of those jobs, it wouldnât be too hard to go through a well commented Dockerfile or similar thing and work out which parts of it related to which of the tasks, and then I could set up two new install scripts for the separated systems.

So I donât do this _currently_ , but Iâm tempted by the idea, and some day I may start!

## Exceptions to the policy

I donât apply this policy of transience to _all_ parts of my life, or even all parts of my computer use. Itâs not a thing I decided on early and planned my whole life around: itâs a thing I gradually _noticed_ seemed to be a recurring theme about how I behave. But itâs not universal.

The biggest exception, as Iâve already mentioned above, is that I keep all my personal email permanently â I donât records-manage it as if I were a lawsuit-fearing company.

Another exception is my web browser _history_. I keep my open tab collection very small, and I keep my bookmarks well organised and version-controlled; but the history of pages Iâve visited is persistent and uncontrolled in just the way I didnât want my shell history to be. And I do use it, when I want to dig up that page I visited some time last week for some reason I couldnât have predicted in advance (like somebody else has just asked me about it).

Why are these two things exceptions to my usual policy? Iâm not 100% sure, because I didnât do it on purpose. But I have a thought. Email and browser history have two things in common:

  1. Theyâre content created by other people, not by me (or at least not _mostly_ by me).
  2. Itâs difficult to predict in advance which parts of them will turn out to be useful later.



My shell history (to take an example I _do_ treat as transient) has neither of these properties. Itâs almost _all_ commands I wrote myself â so if I do occasionally lose a useful command from my history, Iâm not too bothered, because I created it from scratch last time and Iâm confident I can do that again. A draconian policy of discarding history might occasionally waste me a bit of time rewriting something, but itâs much rarer that it makes me lose something _irreplaceable_. And most shell commands are totally boring (the usual round of `cd`, `mv`, `rm` and the absolutely endless `ls`); the ones that are even _potentially_ worth saving are easy to spot, because theyâre the ones that stretch across three lines of my terminal and took ten tries to get right.

But emails from friends, family and ex-lovers (for example) have sentimental value, and obviously wouldnât be at all the same if I rewrote them myself from scratch later. (Not even my own emails _to_ those people would be.) And emails about technical stuff can come in handy later for all kinds of hard-to-predict reasons: for example, someone reports a weird error message in a program of mine and I find it was reported once before, and now I can maybe see what thing the two cases have in common â but it could be _any_ of those past problem reports, and the vital clue could be any part of the message.

Similarly with my browsing history: a lot of the URLs in there were delivered to me by websites when I followed links, without me typing them in on purpose, and again, itâs hard to predict _which_ one Iâm suddenly going to realise next week is just the thing I need to help someone out.

But I do at least promote things from browser history into my bookmarks, as soon as I notice Iâve recalled the same one more than once or twice. I go to the history for things I couldnât have known in advance I was going to need again, but as soon as I _can_ reasonably predict Iâll need a thing again, itâs worth making it into a bookmark.

So these two things arenât subject to my usual policy of transience. I feel vaguely dissatisfied about that (the browsing history in particular), but donât currently have any plans to change it.

## Conclusion

As I said at the start, Iâm not intending to _persuade_ anyone of the rightness of behaving this way. It works for me, but different things work for different people.

But I think a lot of the opposite habits are treated as âthe defaultâ without really considering it. So perhaps some people reading this article might not have even _considered_ some of these possibilities, and might be doing the opposite thing (for example, _increasing_ their reliance on shell history instead of reducing it) simply because it seemed like the only possibility.

So I offer all of this simply as possibilities to think about. If any of these things seems useful to you, great â and if you think about it and decide you still donât want to do it, also fine.
