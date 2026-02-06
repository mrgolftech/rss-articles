# Is QSpy still cool? Let's play QuakeWorld!

**来源:** https://fabiensanglard.net
**链接:** https://fabiensanglard.net/quakeworld/index.html
**日期:** 16 Jan 2026 00:00:00 +0000

---

  


[**FABIEN SANGLARD'S WEBSITE**  
](/)

* * *

[CONTACT](mailto:fabiensanglard.net@gmail.com)    [RSS](../rss.xml)     [DONATE](https://paypal.me/fabiensanglard)

  
  


Jan 16, 2026

Is QSpy still cool? Let's play QuakeWorld!

* * *

With the Internet being grossly expensive in France until 1999, I never got a chance to experience _Quakeworld_. Don't feel bad, I came back with great vengeance when it came to trading on Diablo II to become a SOJilionaire. But I digress.

With the [Quake PC](../quake_pc) finished, the game I was the most eager to finally discover was naturally _QuakeWorld_. Being thirty years late to the game (literally), would any of that still run on my precious 233MHz relic? Let's find out.

[![](../quake_pc/post/finished_perspective.webp)](../quake_pc/post/finished_perspective.webp)

QuakeWorld 101

* * *

QuakeWorld does not stand alone. When it starts, a splash screen indicates that further instructions are available at [www.quakeworld.net](www.quakeworld.net). However that URL now redirects to ign.com since the two entities merged in 2004.

[![](qw_start_with_splash.png)](qw_start_with_splash.png)

You obviously can't play _Single Player_.

[![](solo.png)](solo.png)

And you can't select _Multiplayer_ either. There is no integrated menu to search/select a server or join a game.

[![](multi.png)](multi.png)

Thanks to the Wayback Machine we can still see what quakeworld.net [used to look like](https://web.archive.org/web/19971210063857/http://www.quakeworld.net/). There is also a [good description](https://web.archive.org/web/19971210063857/http://www.quakeworld.net/) of how players used the service.

QuakeWorld Master Server

* * *

To run properly, _QuakeWorld Client_ must be started with parameters on the command-line pointing to a _QuakeWorld Server_ (e.g.: `-connect 192.168.01.`). To make it easy to find them, each _QuakeWorld Server_ registers itself with _QuakeWorld MasterServer_ when it starts. The most convenient way to play QuakeWorld is to use a tool that has a list of master servers, retrieve all the servers available, let you pick one, and start the _QuakeWorld_ client with the proper command-line parameters.

The MasterServer protocol is based on simple text-based messages. It was [documented](https://web.archive.org/web/19970709203940/http://www.home.aone.net.au/nick/qwlocal/protocol.html) in 1997 by Nicholas Maher.

QSpy is cool

* * *

Instead of building this tool, id Software selected something that was already popular in the Quake community. The communication about how to make it happen was even published.
    
    
    From: John Carmack <johnc@idnewt.idsoftware.com>
    To: jep@sclsis.navy.mil
    Subject: Quake World
    Date: Wednesday, August 07, 1996 11:03 AM
    
    Qspy is cool.
    
    Want to be the official front end for the QuakeWorld project?
    
    I think the initial research releases of QuakeWorld are going to be native
    win32 apps only, and they will listen on a control socket, so an external
    windows app can very nicely send them from server to server.
    
    If you are interested, I can go over the new features we are considering
    that would be pertinent, and solicit some opinions from you.
    
    John Carmack[1]

Is QSpy still cool?

* * *

It was easy to find since QSpy came bundled with Quakeworld installer, [qw1022.exe](https://github.com/Jason2Brownlee/QuakeOfficialArchive).

[![](qspy_install.png)](qspy_install.png)_QSpy was renamed GameSpy 3D._

During the installation, I was supposed to be able to [pick the colors of my skin](qspy_player_profile.gif). I was unable to make this work but I could still progress to the next step.

[![](qspy_config3.png)](qspy_config3.png)

Once installed, _GameSpy 3D_ hit the net and came back with an empty list of QuakeWorld servers. That was unsurprising. I fully expected the master server list to be obsolete thirty years later.

[![](qspy_refresh.png)](qspy_refresh.png)

But GameSpy had the good idea to allow users to update the list. I found a few master servers on [quakeservers.net](https://www.quakeservers.net/quakeworld/master_servers). Bless your soul whoever is maintaining this.

[![](qspy_add_masterserver.png)](qspy_add_masterserver.png)

I hit refresh and it looked like "something" was happening!

[![](qspy_refresh2.png)](qspy_refresh2.png)

Within seconds I saw thousands of servers popping up (with players). I cannot describe the joy and overall awe to see this whole stack still able to run.

[![](qspy_huge_list.png)](qspy_huge_list.png)

Gamespy.com closed in 2013 when it merged with ign.com. But they had the good taste of keeping the website up. It actually still renders well with IE4.

[![](gamespy.png)](gamespy.png)

[![](gamespy2.png)](gamespy2.png)

I picked a game and Quakeworld started. The excitement kept on growing since it looked like it was downloading the bsp map.

[![](bravado.png)](bravado.png)

Downloading content was one of the improvements of _Quakeworld_ , the regular quake could only play games where all players already had the bsp in their id1 folder.

And then the map would not actually load. The screen only mentioned something about the version. Oh my. Are they running servers for which there is no client on Windows 9X. Is it only for Quakeworld modern ports like EZQuake?

[![](error.png)](error.png)

I noticed I was using v2.10. The server claimed to be v2.40. The latest version of Quakeworld Client available for Windows 9X was v2.34. This did not look good. I went on the amazing Quake Offical Archive[2] by Jason Brownlee and got client v2.34. And it worked! I was able to start the game and officially took my first step in QuakeWorld.

[![](first_step.png)](first_step.png)

And the game crashed immediately. I had seen perhaps six frames and a half of it. Brief but intense.
    
    
    Z_Malloc: failed on allocation of 40 bytes
    

[![](qspy_error.png)](qspy_error.png)

Failing on such a small amount made me wonder again if v2.34 client would actually work with v2.40 server. Are the packets different? I have 340MiB installed on this machine, could it be too much and something wraparound?

A little bit of Googling revealed a treasure trove of players helping each other. It turned out the problem was the amount of RAM [dedicated to small strings and structs](https://forums.insideqc.com/viewtopic.php?t=1925). Adding `-zone 1024` to the QSpy launcher fixed the problem.

[![](qspy_zone_workaround.png)](qspy_zone_workaround.png)

All you need it kill

* * *

With the `Z_Malloc` issue solved, quakeworld ran flawlessly. For hours. I quickly got my first frag. Using the grenade launcher because I was too busy having fun to figure out how to select the rocket launcher.

[![](gibbed.png)](gibbed.png)

The "frag" messages, revolving around shafts and pinnaples, were super childish and I loved it.

[![](pinnacle.png)](pinnacle.png)

My first accomplishment was to "not finish last".

[![](game.png)](game.png)

And then I spent an entire week-end playing deathmatch, completely hooked. Gosh this game is good. And I played in 320x200, proof that great games are all about mechanics.

QSpy IS still cool!!

* * *

That old-new MMX 233Mhz can still play QuakeWorld in 2026. QSpy was cool. And QSpy _is still cool_!

It is thirty years later and there are still server and master servers up and running. More importantly, there are people out there who still love the game enough to maintain all that infrastructure.

There is no better testament to a game quality than players enduring love, decades later.

References

* * *

^|  [1]| [QSpy is cool](https://www.gamers.org/dEngine/quake/archive/a_aug96/0007.html)  
---|---|---  
^|  [2]| [Quake Official Archive](https://github.com/Jason2Brownlee/QuakeOfficialArchive)  
  
* * *

*
