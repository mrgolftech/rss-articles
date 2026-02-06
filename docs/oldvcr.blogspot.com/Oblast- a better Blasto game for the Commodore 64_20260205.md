# Oblast: a better Blasto game for the Commodore 64

**来源:** https://oldvcr.blogspot.com
**链接:** https://oldvcr.blogspot.com/2025/12/oblast-better-blasto-game-for-commodore.html
**日期:** 2025-12-06T15:55:00.000-08:00

---

#  [ Old Vintage Computing Research ](https://oldvcr.blogspot.com/)

REWIND and PLAY

## Saturday, December 6, 2025

###  Oblast: a better Blasto game for the Commodore 64 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhINuGmCUTNCNrDvsDyFDwV6ZsiGeseHSBcaraMVoluKhEr70EzuUa5JU8hPw5_SXFQI0sEFeQL9Ar1nhK4zEDGclu8Ao9vvHsul94hO3sXv9DztEpJsNDoa1enzvKrDfIozhKYukvY8EY2apPqfpBorVWd0PzGPJAO1ao1MSGYFvv07UdFpYnoA02jyNo/s320/big-mame-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhINuGmCUTNCNrDvsDyFDwV6ZsiGeseHSBcaraMVoluKhEr70EzuUa5JU8hPw5_SXFQI0sEFeQL9Ar1nhK4zEDGclu8Ao9vvHsul94hO3sXv9DztEpJsNDoa1enzvKrDfIozhKYukvY8EY2apPqfpBorVWd0PzGPJAO1ao1MSGYFvv07UdFpYnoA02jyNo/s1024/big-mame-1.png)

Way back (well, six months ago, anyway), when I was [wiring up a Gremlin Blasto arcade board](/2025/06/refurb-weekend-gremlin-blasto-arcade.html), we talked at length about this 1978 arcade game's history and its sole official home computer port by Milton Bradley to the Texas Instruments 99/4A. In the single player mode you run around in a maze and try to blow up all the mines, which can set off sometimes impressive chain reactions, all the while making sure you yourself don't go up in flames in the process. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha4Uf6wofBVDiOiNW2Kt7CdhVqgrc5_7Zd3L_cNJHZi2NF9qX-QDBOgx0tlmDLvpJO9QrAJ5R-QATxV9luz1xuD9m56U-6ABPdvfR0Bi8JBOkyYekX2oYWvplXRonHBpve4hIgIkuWU1gvoIGLEHmGnE0d0l2EljcG0S5XNeKF8zxlMgM492ZRk5qPXCw/s320/big-0011.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha4Uf6wofBVDiOiNW2Kt7CdhVqgrc5_7Zd3L_cNJHZi2NF9qX-QDBOgx0tlmDLvpJO9QrAJ5R-QATxV9luz1xuD9m56U-6ABPdvfR0Bi8JBOkyYekX2oYWvplXRonHBpve4hIgIkuWU1gvoIGLEHmGnE0d0l2EljcG0S5XNeKF8zxlMgM492ZRk5qPXCw/s1120/big-0011.png)

The TI-99/4A version was the Blasto I originally remember playing as I never did play Blasto in the arcades. (Also, for the record, we're not talking about Sony's unrelated Blasto for the PlayStation which, other than having the voice talents of the late and lamented Phil Hartman, was apparently a traumatic slog both for its developers and the few people who actually played it.) To the credit of its three composite authors, it is a competent and accurate conversion that also adds configurable options, colour graphics and music; in fact, TI's Blasto is probably my favourite game on the /4A, more so than any other cartridge. On the other hand, _because_ it's an accurate conversion, it also inherits all of the original's weaknesses, which admittedly hail from the limited CPU and ROM capacity of the arcade hardware. 

So, in that article, I mentioned two [future Blasto projects](/search/label/blasto). One is to save my pennies for a custom arcade cabinet to put the board in, though I just spent a cool grand plus on tires which used up a lot of those pennies and I've also got Christmas presents to buy. But the second was to write my own take on TI Blasto and soup it up. This project is the second one [from my bucket list](/search/label/bucketlist) that I've completed. It took a couple years of work on it off and on, but it's finally done, with faster action and animation, a massive number of procedurally generated screens, and fully configurable gameplay. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_svymvKybuofKGD5s487gls0qA4pgVHGH_AAilIy0QPFF2RErW4p-CCFN0dZKqLGxD8oBIngkihxn2-TE7o0-hOCjercFGVsurRA8eXdHGf-DQmwTAidegRkVarzkYYdgrUUCyXkF3VjkW433BYrRh98k8o0BudD58vcM48Eft807_Wku4Y-lUBbGfuM/s320/big-vice-screen-2025112520513488.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_svymvKybuofKGD5s487gls0qA4pgVHGH_AAilIy0QPFF2RErW4p-CCFN0dZKqLGxD8oBIngkihxn2-TE7o0-hOCjercFGVsurRA8eXdHGf-DQmwTAidegRkVarzkYYdgrUUCyXkF3VjkW433BYrRh98k8o0BudD58vcM48Eft807_Wku4Y-lUBbGfuM/s1152/big-vice-screen-2025112520513488.png)

I've christened it Oblast, and it's free to play on your real Commodore 64 or emulator. Let's talk about what's the same and what's different. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcl5AbEDAYd-5zeQV82-KLV-g_P0lHMWIaUplVgz6ifdNSj4Nxy6cXDI-CNYcDR3I4l7e4Rf26IVFQT_CQ66imMk8M5Ciozv_bozxnZnSBDEuM_vyE23Oito-JWCOjhs_TnGptC0gQKp_51CtziwusbX_FtrsOtAhRr_KIHsxjXTSDrF28bbsVyxFA2Wg/s320/big-mame.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcl5AbEDAYd-5zeQV82-KLV-g_P0lHMWIaUplVgz6ifdNSj4Nxy6cXDI-CNYcDR3I4l7e4Rf26IVFQT_CQ66imMk8M5Ciozv_bozxnZnSBDEuM_vyE23Oito-JWCOjhs_TnGptC0gQKp_51CtziwusbX_FtrsOtAhRr_KIHsxjXTSDrF28bbsVyxFA2Wg/s1024/big-mame.png)

The antediluvian [1978 Blasto](/2025/06/refurb-weekend-gremlin-blasto-arcade.html) ran on Hustle hardware, which was derived from Gremlin's original (and mercilessly copied) Blockade game as designed by Lane Hauck. Programmer Bill Blewitt managed to squeeze Blasto's entire game code, not counting character graphics, into just 2K of ROM. This code had to generate and draw the maze, handle one or two player inputs, handle their projectiles, check for collisions and trigger the audio and "boom" circuits, all while simultaneously setting off explosions that could trigger other explosions and other collisions. In the upright version it also had free game logic. Given its hardware and software size constraints the arcade game's gameplay limitations, which we'll discuss in a moment, were understandable. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgQlunHkV89K58zEKVceRzNaPjZZFJvBrsVvsG3q75iYjxNUB0nIo21_dUuiYjYutKFX6RsxFzKZ_iJaWlRvCb60xjBDAZhu3qEftxGZEyyXZt4FufCQs7htyHUv_62klsN5rrc2AXhuf2yeQCAJX9cDLMR0_DmuWHry2ZprSF4s82MPQXXxU1J4OckaA/s320/big-0000.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgQlunHkV89K58zEKVceRzNaPjZZFJvBrsVvsG3q75iYjxNUB0nIo21_dUuiYjYutKFX6RsxFzKZ_iJaWlRvCb60xjBDAZhu3qEftxGZEyyXZt4FufCQs7htyHUv_62klsN5rrc2AXhuf2yeQCAJX9cDLMR0_DmuWHry2ZprSF4s82MPQXXxU1J4OckaA/s1120/big-0000.png)

When Milton Bradley picked up the license (from Gremlin's new owner Sega) as a developer for the new TI 99/4, they kept the gameplay and basic rules in their home computer port almost identical. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHBgiyIkHgfR_xrPHVR8Tug4ORI5TsV-ozc8sKdD8FVH7ELcAuaFR-7nD_tf_0gKGi0WGVDeuGNvu8oVWIkbBQv6YdWckh03qXiOohWx0GniYr-tYrG-fJMh_wkC5poHHLNHuHdhrkD9Xve-ad5HkU33arvWp00sUsmuvneRDKuxPPtJLbicFopZ5ER_4/s320/big-0001.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHBgiyIkHgfR_xrPHVR8Tug4ORI5TsV-ozc8sKdD8FVH7ELcAuaFR-7nD_tf_0gKGi0WGVDeuGNvu8oVWIkbBQv6YdWckh03qXiOohWx0GniYr-tYrG-fJMh_wkC5poHHLNHuHdhrkD9Xve-ad5HkU33arvWp00sUsmuvneRDKuxPPtJLbicFopZ5ER_4/s1120/big-0001.png)

Instead, the programmers added music tracks, a colour display, and multiple configuration options. You could set not only the game's speed (I always played Full Tilt) ... 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDkNWJhZC49mqxssu1OGx_yeHpIeKQIwqivxSJIgdFht8NxEEkZR4e9WJUIK7Cqb7We1Ut1grCkQ7_WLg00O9AtixgcaB2jcfUs4ag1AmPHdq_lQW3HM5Ieybvz1h8TKdbuDi-kNANeAkaIacxvVaumkvwbccFVfab6XsENi6459xmezNo420G_g_9ZCk/s320/big-0016.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDkNWJhZC49mqxssu1OGx_yeHpIeKQIwqivxSJIgdFht8NxEEkZR4e9WJUIK7Cqb7We1Ut1grCkQ7_WLg00O9AtixgcaB2jcfUs4ag1AmPHdq_lQW3HM5Ieybvz1h8TKdbuDi-kNANeAkaIacxvVaumkvwbccFVfab6XsENi6459xmezNo420G_g_9ZCk/s1120/big-0016.png)

... but also how the maze was drawn, including whether trails existed (areas of the map pre-cleared for motion) and how dense the mines were. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIatccqO209TYVzkfl3ArNmodels5pNLuIEA-TFk1_xCJHO1Ki7D8BvgQp_b_Yk1JemJZGQXwReDQIlT2ulEzS1Cw49tI5kuE4VQHAOCQswoyHa5DqlPKS926BpGnhMKSd8lnztFQ5PPFdNqWz3_ufLI6YstVGvtY8NIAS42wFCMZWssnsTyGlMvuc5Xg/s320/big-0037.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIatccqO209TYVzkfl3ArNmodels5pNLuIEA-TFk1_xCJHO1Ki7D8BvgQp_b_Yk1JemJZGQXwReDQIlT2ulEzS1Cw49tI5kuE4VQHAOCQswoyHa5DqlPKS926BpGnhMKSd8lnztFQ5PPFdNqWz3_ufLI6YstVGvtY8NIAS42wFCMZWssnsTyGlMvuc5Xg/s1120/big-0037.png)

Likely as a way to emphasize the TMS9918(A)'s colour capabilities, the MB programmers changed the setting of the game to a green earth-bound landscape with blue (?) mines and reworked the spaceships into tanks. The density option probably had an even greater impact on gameplay than the speed setting because a maze with a lot of mines made for a zippier, more explosive game. You could rig some big bangs this way, though these were sadly were let down by the TMS9919/SN76489's relatively weak noise output. The program also vainly tried to play a simple tune during the game but this was inevitably interrupted and forced to start over by any sound effect (i.e., a tank shooting, mines exploding). 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilLTm84uzcnyfbdJOuUodPsQdwZMO69EvkwUUKWkCxhvb2RhwzHhW9BhFPQFvRaGSsuCehLqNd-GSxiKot0JOy2aLcpH9n0R-BXIErbKy1Day7C-1xQ24sJJ60NgoRKEKRdQIyd-tV67WZTyXbBNJ3L4jLtFK1tUmdF4-6DBD10coWkOlLEceZ8xtsMq0/s320/big-0037a.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilLTm84uzcnyfbdJOuUodPsQdwZMO69EvkwUUKWkCxhvb2RhwzHhW9BhFPQFvRaGSsuCehLqNd-GSxiKot0JOy2aLcpH9n0R-BXIErbKy1Day7C-1xQ24sJJ60NgoRKEKRdQIyd-tV67WZTyXbBNJ3L4jLtFK1tUmdF4-6DBD10coWkOlLEceZ8xtsMq0/s1120/big-0037a.png)

As with the original, you have infinite lives but finite time. If you trip on an explosion, or the other player shoots you in two-player mode, you lose valuable seconds until you respawn. However, you respawn at your original spawn point as if you were teleported there, a conceivable failure mode for a fanciful spaceship but an extremely unlikely one for a terrestrial tank, which makes a good segue into some of its other idiosyncrasies: 

  * Each player can only have a single projectile in motion at any time. However, as soon as that projectile impacts, you can immediately fire another one. This is clearly motivated by the limited memory in the original game, but I don't know of any artillery shell in real life that works like that!
  * As a related phenomenon, although you can _move_ while an explosion or chain reaction is occurring (with a slight reduction in frame rate), you can't _shoot_ -- at least not until the explosions stop, at which point you can once again shoot immediately. This also seems to be a concession to limited available memory as the game can't track multiple chain reactions at once.
  * Tanks absolutely can't go over mines or obstacles; they act as completely impassible barriers. I guess that might make sense with spaceships, but it seems like a rather wussy sort of tank.




[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhY6stQI5ncdRw8NFTfSYwprPoatlvyTIQJnI9l1V3OS-pA9vnfJHCVzr9_4ZkYge6uv9NE34ZxAKrD3CWGAL4M03d6CDWQIHFvQZb1vTRuvanIHmuOxQrRwm1dPmQlFMzT83TqwEy0jRFste8NJOUuZ1z102eukx5GymK1fWa9-KEpCJaHWqtP7pUkGGQ/s320/big-0039.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhY6stQI5ncdRw8NFTfSYwprPoatlvyTIQJnI9l1V3OS-pA9vnfJHCVzr9_4ZkYge6uv9NE34ZxAKrD3CWGAL4M03d6CDWQIHFvQZb1vTRuvanIHmuOxQrRwm1dPmQlFMzT83TqwEy0jRFste8NJOUuZ1z102eukx5GymK1fWa9-KEpCJaHWqtP7pUkGGQ/s1120/big-0039.png)

Also, there's only one screen. If you shoot all the mines before time runs out, the arcade Blasto would give you a free game in the single player mode, if you were playing on the upright version and if you were in a jurisdiction where free games weren't considered illegal gambling, as they were at the time in some areas (pinball also suffered from this). But that was meaningless on the no-coins-needed TI port, where shooting all the mines would win you a free ... game over screen, the same prize you'd get for losing. 

Now, I want to point out that despite those things, I loved TI Blasto and played quite a bit of it. But we can improve on what is already an awful lot of fun. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Iv10HegZ3_m01nUXU3e-h_wE8XXYdkfNQTpe6TJuB4ZKX4xDRmsq2lgiSUnUkxkYpobpForO1BmSkwUIZU0VztH7t9dqymYZ2Ls1Raof9uwdBc0ltqljfeHGTERkiEUNGG3Jva1vhYhrYzuzpvhuI35b0yhQW3JoorOoDercB52MOwoe7tiol-KCzek/s320/big-vice-screen-2025120222025623.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Iv10HegZ3_m01nUXU3e-h_wE8XXYdkfNQTpe6TJuB4ZKX4xDRmsq2lgiSUnUkxkYpobpForO1BmSkwUIZU0VztH7t9dqymYZ2Ls1Raof9uwdBc0ltqljfeHGTERkiEUNGG3Jva1vhYhrYzuzpvhuI35b0yhQW3JoorOoDercB52MOwoe7tiol-KCzek/s1152/big-vice-screen-2025120222025623.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiC1DjaYXuE2VGC6bggaxFlFkD36hHFXJ2Y_D3pv9OQeYsBo_Axujiv5pb_rUprjUXEW-hbzOEtiBvxBCJ2pKFGnzk0MYzpXsAYAeU7DSfqL9dUm1lbXFCFP2Kjhymnt098wkpicfwaAdaZFIeUwBKgA-oF2W4TPQOJoRxsxGiOqZEUNxJEnItuUmTva-8/s320/big-vice-screen-2025120222032992.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiC1DjaYXuE2VGC6bggaxFlFkD36hHFXJ2Y_D3pv9OQeYsBo_Axujiv5pb_rUprjUXEW-hbzOEtiBvxBCJ2pKFGnzk0MYzpXsAYAeU7DSfqL9dUm1lbXFCFP2Kjhymnt098wkpicfwaAdaZFIeUwBKgA-oF2W4TPQOJoRxsxGiOqZEUNxJEnItuUmTva-8/s1152/big-vice-screen-2025120222032992.png)

It took a while to get the fundamentals laid down, and it was immediately obvious that the most important mechanic in the game had to be the chain reaction since everybody likes to blow %@#$ up. Consequently, the code that handles the explosions was the first part of the game I wrote, as I reasoned the game wouldn't be worth completing if I couldn't get it fast or frantic enough. This very early draft was a simple proof of concept using PETSCII graphic characters to model the algorithm; character graphics were a must because doing this on the high-resolution screen would have played like molasses. 

The game doesn't track explosions anywhere else but the screen itself: everything it needs to determine the next frame of animation is by looking at what's set on the characters present. It scans the entire playfield each time to do this which necessarily locks the animation to a constant frame rate -- even if the whole screen were alive with multiple explosions, it would take nearly exactly as much time as if only one single bomb were being detonated, keeping gameplay speed consistent. I did a lot of code unrolling to make this work as quick as possible and the final draft of the original "screen test" is what's in Oblast now. 

The black area is because I already knew I'd be using sprites for the tank and I didn't want to mess around with having to manage the high bit for X coordinates greater than 255, so I reserved the right-hand portion of the screen for an information pane. This also had the nice side effect of reducing how much of the screen must be scanned. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSxIkTKu-fG1WUcCqkFwTrTYjrWVH-ap60gboFYbmmiZCXUGgeeTEHZlbmAaiW9K5ACXOGwhAZm1e2iCfBPI3GzxiNl7uSpn6r6XYnmAjP_Fl2lXZzx7v9FqeThCh4McM4yprglCFIdT-lfTCr-1A4UmoiJ9as6VA7c2-LtZOzQtIXEkuXT-jjH9BwIIo/s320/big-vice-screen-2025112521225555.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSxIkTKu-fG1WUcCqkFwTrTYjrWVH-ap60gboFYbmmiZCXUGgeeTEHZlbmAaiW9K5ACXOGwhAZm1e2iCfBPI3GzxiNl7uSpn6r6XYnmAjP_Fl2lXZzx7v9FqeThCh4McM4yprglCFIdT-lfTCr-1A4UmoiJ9as6VA7c2-LtZOzQtIXEkuXT-jjH9BwIIo/s1152/big-vice-screen-2025112521225555.png)

For Oblast, I've concentrated exclusively on the single-player mode in which I played Blasto most, which also simultaneously solved some technical issues. (I may make a two-player version in the future if I figure out good solutions to them.) Although I've kept the spirit of TI Blasto's configurability, I made it extend not just to maze generation but even to the game's core rule set. The configuration portion is largely written as a BASIC stub with some 6502 assembly language helpers for speed, with the bulk of the remainder and the entirety of the main game loop also in assembly language. 

There are four preset games, the parameters for which I selected after tweaking them during repeated playtesting. The first is the one I consider "typical" for most players to start with (and the one you'll see the computer attempt to play during Oblast's attract mode), the second has an increased number of bombs, the third adds trails and more Blasto-like rules for more classic gameplay, and the fourth is a completely gonzo game mode which has become my personal favourite after a rough day at work. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1500uXUGufWVwNEJkbc_5xqJqqrOupTIxna1zh-dCyVtUDyK-O-fjmRyUreVH9WpJdBwdruuI30MSGpYsBlkznSvy-OylTng7DIlzuBkbLcqQ9vdcUOCs6oCcii1j89oyXGsGZyLUwwUpBgJEVVDByFTgP6gg5gjIRnHb0hNrmVC2aNUcaBTXdujHB1k/s320/big-vice-screen-2025112521231508.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1500uXUGufWVwNEJkbc_5xqJqqrOupTIxna1zh-dCyVtUDyK-O-fjmRyUreVH9WpJdBwdruuI30MSGpYsBlkznSvy-OylTng7DIlzuBkbLcqQ9vdcUOCs6oCcii1j89oyXGsGZyLUwwUpBgJEVVDByFTgP6gg5gjIRnHb0hNrmVC2aNUcaBTXdujHB1k/s1152/big-vice-screen-2025112521231508.png)

If you don't like those presets, or want to tweak them further, there is a full game configuration screen letting you set game modes and the starting level/screen. The game supports up to 384 procedurally generated screens and you can start on any of them from 0 to 255. The screens are generated from constant seed data (in this case the 64's BASIC ROM) and thus designed to generate the same screen with the same parameters, facilitating muscle memory for longer play if you get good. 

Like the two versions of Blasto, Oblast has mines (bombs) and obstacles (trees). You can very precisely control the densities of both. You can also have the game generate Blasto-style trails horizontally, vertically or both, you can set how quickly your tank's fuel is exhausted (i.e., your time limit, the only option which cannot be zero), and you can indicate if your tank is invulnerable to explosions and how quickly to cycle your shells. I'll talk about how that works in a moment. If you press one of the preset function keys in the configuration screen, then its settings are loaded as a starting point for you to modify. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzIN8t84_zsgS3315rr-i03P53Ozn-EnEsrpe03eCBHmuH5bWxZ8vMEqoTVaD351DVPH-yON8x4yHoBJI1z8hEHA4UYjvP27AbF9w_z11HpBK9Bg6r21LVaRwJ4TTIpXKX2RVOUPmGusn7686qYpUfbfNr41iFqDtTCgCISqMntmWmDzUmOE2p_J3TTg0/s320/big-vice-screen-2025112522054967.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzIN8t84_zsgS3315rr-i03P53Ozn-EnEsrpe03eCBHmuH5bWxZ8vMEqoTVaD351DVPH-yON8x4yHoBJI1z8hEHA4UYjvP27AbF9w_z11HpBK9Bg6r21LVaRwJ4TTIpXKX2RVOUPmGusn7686qYpUfbfNr41iFqDtTCgCISqMntmWmDzUmOE2p_J3TTg0/s1152/big-vice-screen-2025112522054967.png)

For the presets, where a new player wouldn't know exactly the game conditions they trigger, I pondered various in-game ways of informing them and hit on an easy-to-implement "dot matrix printout" motif where the BASIC stub scrolls a "briefing" before starting play, making asynchronous "printer" noises based on the bit pattern of each line's ASCII codes. This same motif is used for the basic built-in help since I had some extra space available. 

Once you've got the settings the way you want, or you just want to keep playing the same preset, after a game ends you can bypass the presets and game configuration screens and jump right into a new game with the same settings by pressing the fire button. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxG4AGNZ1usFMF1PU6CpvD3wakNoyuAj1Gu8MdbNH0ii-sw5E2pgWXt5RGYZEKdYLI9gsvn24nNTMFR9UgvYE5VLD4ekt8jLFWdWee4O2XF3BOWkk7tIB929pxMg3YvNUnUwgQd9BIICc60cIPiSlzKgH0lH-e8fy3bIJwN7C_Tc39A895uiJWjRUVQK8/s320/big-vice-screen-2025112521275980.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxG4AGNZ1usFMF1PU6CpvD3wakNoyuAj1Gu8MdbNH0ii-sw5E2pgWXt5RGYZEKdYLI9gsvn24nNTMFR9UgvYE5VLD4ekt8jLFWdWee4O2XF3BOWkk7tIB929pxMg3YvNUnUwgQd9BIICc60cIPiSlzKgH0lH-e8fy3bIJwN7C_Tc39A895uiJWjRUVQK8/s1152/big-vice-screen-2025112521275980.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYIKdUm8bga1v_Eofw1dAc3XNZtpbqH2_mYtoZMbmoAW_Q0oVzsSLszDmo5YZTZJJcfmJldqmBV1JyJ-9xFrJV55pWeRLm1i-t0RhY8QOxFeN_lAi9zbiwwRE1_XdmRl5hDG6cQRAxxzzh7tHdp_3FsVdnYt8NJPswz7Y_5hyphenhyphenq7F1KyKmzAwnEJ45neR8/s320/big-vice-screen-2025112521282471.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYIKdUm8bga1v_Eofw1dAc3XNZtpbqH2_mYtoZMbmoAW_Q0oVzsSLszDmo5YZTZJJcfmJldqmBV1JyJ-9xFrJV55pWeRLm1i-t0RhY8QOxFeN_lAi9zbiwwRE1_XdmRl5hDG6cQRAxxzzh7tHdp_3FsVdnYt8NJPswz7Y_5hyphenhyphenq7F1KyKmzAwnEJ45neR8/s1152/big-vice-screen-2025112521282471.png)

Here's two examples of the procedural screen generation at work, both level 0. The top screen is what you'd start at if you chose the "Regular Duty" (F1) preset; the second is "More Like Classic Blasto" (F5). Both have the same seed pointer, and you can see some commonalities in bomb and tree positions, but the second screen has a slightly lower bomb density and a slightly higher tree density plus trails going both horizontally and vertically. Each collection of settings will always generate the same screens on your machine. The game code manually counts the number of bombs and trees at the end of map generation since they may be taken away by trails or in the process of ensuring the tank has a cleared starting position. 

Although we're using a custom character set for speed, I still wanted the colour flexibility of high resolution where you can have different text and background colours. To do so Oblast is something of a love letter to one of the VIC-II's more underutilized display modes, extended background colour mode (ECM). ECM supports up to four background colours on the same screen and the main game uses two additional colours besides the green background, the most obvious being the black background of the information pane, but also a yellow background as part of animating explosions. The price you pay for this flexibility is that only 64 characters of the standard 256-entry character set can be used; the two high bits instead become a bit pair to select the background colour. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXiyBAnTnajhT7OkpWTiuNZivgrQE1Gi7ARuXvhwtA3zLsBKXByXO_v-6RqjaBdTTw5tK3Q4WgtFo3BP-eNw435YMK_9kaq1UbPVrfKNhhwVZtLi07mtrhyNG-kTmaqz3jJaH9ifTpLBBMOFTgqHpk8wcXyw2B4BUBm5ZEGHLsCRYDq8nVZ6UC0P4rhNw/s320/big-vice-screen-2025120320502278.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXiyBAnTnajhT7OkpWTiuNZivgrQE1Gi7ARuXvhwtA3zLsBKXByXO_v-6RqjaBdTTw5tK3Q4WgtFo3BP-eNw435YMK_9kaq1UbPVrfKNhhwVZtLi07mtrhyNG-kTmaqz3jJaH9ifTpLBBMOFTgqHpk8wcXyw2B4BUBm5ZEGHLsCRYDq8nVZ6UC0P4rhNw/s1152/big-vice-screen-2025120320502278.png)

That meant making a lot of careful decisions about what I was going to actually display and getting those shapes into the first 64 character glyphs, shown here [in Ultrafont+](/2024/11/one-parting-some-commodore-64-utilities.html). You'll notice that I've replaced some of the letters and typographic characters with graphic shapes because I knew I would never actually need to display those letters or symbols. Everything you see on the screen except for the tank and the shells is a character in this custom font. On the bright side, this character limit also means we can reduce the memory needed by the game font by 75 percent. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8XtN78mgxUOK_SO47zdDgzQoKDrKodEnFVXELLnKlbfGm6DizxdvY_uJGQISbpn_NmP1grV9lV2MXcwwDThRkDmY2l22tDfi35VOYIrY8pHhVMLSieQhuyuVfQyuyCGttbtegsq2gcYzylTpveVbuoRSgEGqpZPfuHhKfbLMhZphjtmnXGSCNufmiiKM/s320/big-vice-screen-2025112522101417.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8XtN78mgxUOK_SO47zdDgzQoKDrKodEnFVXELLnKlbfGm6DizxdvY_uJGQISbpn_NmP1grV9lV2MXcwwDThRkDmY2l22tDfi35VOYIrY8pHhVMLSieQhuyuVfQyuyCGttbtegsq2gcYzylTpveVbuoRSgEGqpZPfuHhKfbLMhZphjtmnXGSCNufmiiKM/s1152/big-vice-screen-2025112522101417.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi91bYbIH5NzUkcF3AoOI2IYw8iPgZ0IkXwoUVW4jsBKKevjVurhF05fNmnU9NK9jfsxOyovh8QFeYhJ7liNKvs13bY9dOPHJ1mG3ObuXe9qBHb-GjyMHz_9FNdOEPevuP5VqDn_Xhy-B31q-CkFvdFFOpYFoowetsXiYdgW4Vqs2i2TtgU34e20jaGZhk/s320/big-vice-screen-2025112522130237.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi91bYbIH5NzUkcF3AoOI2IYw8iPgZ0IkXwoUVW4jsBKKevjVurhF05fNmnU9NK9jfsxOyovh8QFeYhJ7liNKvs13bY9dOPHJ1mG3ObuXe9qBHb-GjyMHz_9FNdOEPevuP5VqDn_Xhy-B31q-CkFvdFFOpYFoowetsXiYdgW4Vqs2i2TtgU34e20jaGZhk/s1152/big-vice-screen-2025112522130237.png)

By looking for the bit set for the black background of the (impervious) information pane, as well as the wall character that also has this bit set, the game knows not to propagate explosions into that area. The yellow background comes in for knowing what needs to detonate _next_ frame: the routine uses that bit as a deferred marker so that as it sweeps sequentially through the screen it doesn't update the same bomb twice in the same frame and prematurely snuff it out. Since setting that bit will also cause a different background colour to be used, we use yellow to make the explosion visually interesting as another side effect. 

Parenthetically, the TMS9918 and TMS9918A also have a feature like this which TI Blasto itself appears to use: each 32 character block of its 256-character fonts can have its own colours. Unlike the VIC-II's ECM which must be specially enabled, this is a standard feature of the 32x24 text mode (which TI calls "Graphic I"), but the character shapes remain unchanged in each block which may require making duplicates (whereas with ECM they are always drawn from the first 64 glyphs). 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQOecgJE2UFgWJWhU95hlB9GGvb_DywD5l4pKkmTFmG2ORbWgdVqnghixkdP71fXny8DW5_csxkf4Uxo8PjzdzM6HtsIq5Zzp1yg5UjzUO6E59UWofskuUBQA_stAgVObHxUeQsZ7KFna0eWJtAVts-3QGm9JO2x60Wtm00F30FpiP2tIH98kIzwFqfsU/s320/big-vice-screen-2025112521285810.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQOecgJE2UFgWJWhU95hlB9GGvb_DywD5l4pKkmTFmG2ORbWgdVqnghixkdP71fXny8DW5_csxkf4Uxo8PjzdzM6HtsIq5Zzp1yg5UjzUO6E59UWofskuUBQA_stAgVObHxUeQsZ7KFna0eWJtAVts-3QGm9JO2x60Wtm00F30FpiP2tIH98kIzwFqfsU/s1152/big-vice-screen-2025112521285810.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi90ZiDnd9uIOZNX5NBvxAu_9nvsULzuwun0bE7sTPH-XEex47Q0l-jyRjULWvCzimLwIB2yQdtEgQJ4xNUSbV5eQE_3sNr1rM8GH3nnqeItOLpw8IQkFHmznzjjo9JbhmE7VEIg-gcGlTQUnzeqUNeEdEQpsd-ssDJto7NU2bfRuTVOqeBBNga3Lkgb7U/s320/big-vice-screen-2025112521294299.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi90ZiDnd9uIOZNX5NBvxAu_9nvsULzuwun0bE7sTPH-XEex47Q0l-jyRjULWvCzimLwIB2yQdtEgQJ4xNUSbV5eQE_3sNr1rM8GH3nnqeItOLpw8IQkFHmznzjjo9JbhmE7VEIg-gcGlTQUnzeqUNeEdEQpsd-ssDJto7NU2bfRuTVOqeBBNga3Lkgb7U/s1152/big-vice-screen-2025112521294299.png)

If there are a lot of bombs on screen, as is the case in the fourth preset and my favourite gameplay mode, nearly the entire screen will be consumed with the explosion which animates around you as you shoot other things. This wasn't possible in either of the original Blastos. Also, instead of trying to play music during game play, all three SID voices are used for noise generation (with a low-pass filter and some resonance smeared on for a woofer-like effect). Voice 1 is triggered when you fire your gun and voice 2 is always running as the tank's engine, with its frequency varying with motion and tank rotation. Voice 3 is used specifically for explosions because it's the only SID voice where you can directly sample both the oscillator waveform output and the current amplitude of the audio envelope. We take these samples, scale them to the activity on screen, and feed the result into the VIC-II's screen fine X scroll. Lots of explosions cause lots of shaking, yet the shaking is always in sync with the audio. 

Besides the character graphics, the other major screen component are the sprites. The tank is a composite of three sprites: an animated set for the tank tread, the main tank body, and an accent layer. This is sharper than using multicolour sprites where your horizontal resolution is halved. These three sprites move together and the build system automatically precalculates frames to rotate them off a template, which are played back on screen when you turn. Unlike both versions of Blasto where the tank is limited to integral character positions, the tank in Oblast is larger than the bombs and trees and can move in single pixels, though I still limited movement to 90 degree angles so I didn't have to do expensive trig computations to figure out a shell's trajectory. 

One sprite being used as the fuel gauge needle left four sprites for the shells. I had earlier considered using character graphics for them too, but animating shells that way would be slower and less smooth than moving sprites. On the other hand, then, [without resorting to tricks](https://www.linusakesson.net/scene/nine/index.php) there can only be four shells onscreen at once which also didn't seem very tank-like. After some thought I came up with a game mechanic to explain it. In the information pane in these two shots, you see the level number, the fuel gauge which acts as your timer, and then four blue shell indicators. Three of these indicators are dark blue, indicating they are reloading (the fourth is a bright cyan, indicating ready). We'll simply define the reloading time for any shell chamber as the maximum length of time it takes a shell to get across the screen in any direction. Thus, no matter how much you fire, you can only ever have four on-screen because the reloading time will lock you out. (Blasto-style fire control where shells recycle immediately as they hit something is preserved for that game mode, or if you turn on "fast cycl[ing] shells" from the configuration screen.) 

While propagating explosions is approximately constant-time, other operations in the game may not be, and there's no reason to walk the screen if nothing's marked as needing it. That means we need a timebase to keep frame rates stable. For this purpose I used the Kernal jiffy clock, which on both PAL and NTSC systems is triggered by the Timer A interrupt to tick about every 1/60 second. The game loop locks to this and uses it to know when to move game objects and trigger screen updates. Still, even this isn't fast enough for moving very speedy things like the shells you fire and the game felt too slow. So ... we make the Timer A interrupt even faster, flogging it at 240Hz instead of 60Hz (the game has prescaler values for both PAL and NTSC), making jiffies 1/240 of a second instead and moving objects at that rate. 

This does have interesting interactions when the VIC-II is still drawing your screen at either 50 or 60Hz even as you update it four times as quickly, and most of these interactions have to do with collisions because you can move objects faster than the VIC-II can detect they intersect. The bombs are as big as they are because that gives lots of opportunities to detect a shell striking one, but tank collisions remained unreliable with smaller graphics like trees. Fortunately, however, we've already declared we didn't like the fact that trees and bombs (i.e., obstacles and mines) were impassible objects, so we can make this deficiency into a virtue. The game keeps running track of [where the tank last was](https://www.youtube.com/watch?v=bZe5J8SVCYQ) and if a collision is detected immediately moves it back to that position. However, because collisions are detected inconsistently at this rate of motion and the game updates the tank's coordinates faster than the VIC will draw them, it ends up manifesting onscreen as the tank simply slowing down when it has to cross an obstacle. I like that better than just coming to a dead halt. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKBKWsBBeB-8FEecvnCMlsdP4GbXyONVsKPT5jwilKanZaiU1IIbHTvjucpva2hrfwLkmlgIz9ivqpssYrEBNJDzI9Wq6ShDLPrkxMQhhknjrYci6kyMEXuki125qVU3Bu9iXCWNZfos8v370p1-vnLzfUg_FzoE9AtreYXA7Gb_zHu68Bqvw4v4236ow/s320/big-vice-screen-2025112521532570.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKBKWsBBeB-8FEecvnCMlsdP4GbXyONVsKPT5jwilKanZaiU1IIbHTvjucpva2hrfwLkmlgIz9ivqpssYrEBNJDzI9Wq6ShDLPrkxMQhhknjrYci6kyMEXuki125qVU3Bu9iXCWNZfos8v370p1-vnLzfUg_FzoE9AtreYXA7Gb_zHu68Bqvw4v4236ow/s1152/big-vice-screen-2025112521532570.png)

Explosions, however, are nice big targets and we have no problem detecting when the tank gets nailed by one of those. In the game modes where your tank is vulnerable, we throw your tank into a temporary tailspin, start flashing the border and the information pane (which is just a matter of setting its colour register), turn on voice 1 and voice 3 at the same time for an even bigger boom, and take the envelope and waveform from voice 3 and put it into the fine Y scroll register as well as the X to really throw the screen around. My favourite game mode allows you to blow up the entire playfield with impunity, of course. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKlu3e6BcUNRWtnDKk4glAXVSxOjvYWhgbFe9zUagEjMaoRGgvMqIcdRgOmxuDxQDUQ4AKSrSsuyGeN6w_30zXPHsvt52N9sHhOOB_Ruc_PofjgxROpG7yfyRj1-GS0raPnbGzQIcP6V-Z_kXQdPpGTi_W46-4QPiV0HwmGndTWMwmThMcF3dNkd87Esc/s320/big-vice-screen-2025112521430338.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKlu3e6BcUNRWtnDKk4glAXVSxOjvYWhgbFe9zUagEjMaoRGgvMqIcdRgOmxuDxQDUQ4AKSrSsuyGeN6w_30zXPHsvt52N9sHhOOB_Ruc_PofjgxROpG7yfyRj1-GS0raPnbGzQIcP6V-Z_kXQdPpGTi_W46-4QPiV0HwmGndTWMwmThMcF3dNkd87Esc/s1152/big-vice-screen-2025112521430338.png)

I also decided to overhaul the scoring with special bonuses silently awarded after completing a screen and detailed cumulatively at the end when your score is added up (total bombs exploded plus total bonuses earned). Don't cheat and look at the source code, but the descriptions of the bonuses should give you a clue as to how you win them. Note that some bonuses are mutually exclusive, and some are explicitly disabled ("n/a") in certain game configurations that make them impossible or unavoidable. 

Should you beat the default high score, you'll see another use of extended background colour mode for the champion medal (you'll just have to beat it fair and square, no spoiler screenshots). This segment [uses FLD](https://bumbershootsoft.wordpress.com/2015/09/17/flexible-line-distance-fld/) to scroll the medal into view and then cycles the ECM registers for a masked multiple colour bar effect without having to split the screen horizontally. It's a simple effect that I threw together in an afternoon but I think it looks nice. While the game configuration screen _looks_ like it might use ECM for the top title, it actually doesn't because I needed lowercase letters, so I employ a much simpler trick for that screen which shouldn't take you long to figure out. 

A key goal was to get the entire game in memory at once without additional loading or disk access, meaning you can even run it from cassette tape if you want to. In memory everything is arranged around the two character sets, the bank of sprites and the two hi-res title screens which are in fixed locations to deal with the VIC-II's more constrained view of memory (one of the hi-res screens is slotted under the BASIC ROM so I could free up 8K for something else). I then redistributed the various machine language subroutines and the three music tracks around those assets while also ensuring the BASIC menu stub had enough free memory to maintain its variables. After the core game was done I added two more extras on, the attract mode (which required some reworking to fit) and a really silly credits sequence, which implements a double-buffered screen scroller and takes advantage of the fact that the main music track sounds pretty neat slowed down. The entire mess is then single-parted using my custom cross-linker and optionally compressed. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd2TLL47lAZvo4fnrPQYxUJnGpv3wEd5umqBtRvCFB2Frl-DS7K-X6xqkI1dJe2Ye5Yr-7uqHR7glb9aICjl_pIKJuTB9gx4Dv_wja3gwOXSVA3rYbOREK2-vohN1Zgk6F93nbGnzQmiNlCz1jf4MWWpQIxiew3dLjsbybZ7AyRGjNylArIBCFDEj-EaU/s320/big-vice-screen-2025112522133005.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd2TLL47lAZvo4fnrPQYxUJnGpv3wEd5umqBtRvCFB2Frl-DS7K-X6xqkI1dJe2Ye5Yr-7uqHR7glb9aICjl_pIKJuTB9gx4Dv_wja3gwOXSVA3rYbOREK2-vohN1Zgk6F93nbGnzQmiNlCz1jf4MWWpQIxiew3dLjsbybZ7AyRGjNylArIBCFDEj-EaU/s1152/big-vice-screen-2025112522133005.png)

Oblast is [freeware and open source on Github](https://github.com/classilla/oblast). You can build it with Perl 5, the [`xa65` cross assembler](http://www.floodgap.com/retrotech/xa) and optionally the [`pucrunch` compressor](https://a1bert.kapsi.fi/Dev/pucrunch/). The Perl tools to generate the sprites, the tokenized BASIC code and the uncompressed runnable linked version are all included. Say that you want to change the presets to your own preferred settings: just change the corresponding `DATA` statement in the BASIC code, do a `make` and instantly have your modified binary. All I ask is that modified binaries that you provide to others should use a different name so they aren't confused with the original, and note that this game and any derivative works based on it or its components are under the [Floodgap Free Software License](http://www.floodgap.com/software/ffsl/). 

If you just want to play it, [the Github releases tab](https://github.com/classilla/oblast/releases) provides compressed (for actual floppy disks or tape or other media with limited space) and uncompressed (for fast DMA cartridges and emulators) builds as `.prg` files you can run directly. You'll need a joystick or equivalent in port 2, and the game should run on any PAL or NTSC Commodore 64. This is hardly the last game, let alone project, on [my bucketlist](/search/label/bucketlist), but it's good to knock another one off it. Also, please don't blow up trees in real life. 

If you've enjoyed playing, [buy me a ~~coffee~~ Pibb](https://ko-fi.com/classichasclass). 

Posted by  [ ClassicHasClass ](https://www.blogger.com/profile/17331846076856918359 "author profile") at  [3:55 PM](https://oldvcr.blogspot.com/2025/12/oblast-better-blasto-game-for-commodore.html "permanent link")

[Email This](https://www.blogger.com/share-post.g?blogID=8349470052336612452&postID=7899002469633843088&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=8349470052336612452&postID=7899002469633843088&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=8349470052336612452&postID=7899002469633843088&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=8349470052336612452&postID=7899002469633843088&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=8349470052336612452&postID=7899002469633843088&target=pinterest "Share to Pinterest")

Labels: [blasto](https://oldvcr.blogspot.com/search/label/blasto), [bucketlist](https://oldvcr.blogspot.com/search/label/bucketlist), [c64](https://oldvcr.blogspot.com/search/label/c64), [commodore](https://oldvcr.blogspot.com/search/label/commodore), [software](https://oldvcr.blogspot.com/search/label/software), [ti](https://oldvcr.blogspot.com/search/label/ti)

#### 2 comments:

  1. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrTM9JoCfmJiM9jXhlnwfjgcCMxUfv3N8WR5gqeAYgjPIKReZ5kBQ1A0nnGsgIA1WtnYPM2NAECYECOTRQWHzH7mBVEhl_9JiFBugW8OoT_OKehfV1DI_OGmEvecsqtIo/s45-c/Photo_on_2009-10-12_at_11.11.jpg)

[Brendan](https://www.blogger.com/profile/08675330988765544946)[December 17, 2025 at 11:01 AM](https://oldvcr.blogspot.com/2025/12/oblast-better-blasto-game-for-commodore.html?showComment=1765998109260#c838937259760727906)

Blasto was my favorite TI-99 game too... well, maybe tied with Parsec, but I was a lot better at Blasto as an eight-year-old. What a cool project!

Reply[Delete](https://www.blogger.com/comment/delete/8349470052336612452/838937259760727906)

Replies

     1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[ClassicHasClass](https://www.blogger.com/profile/17331846076856918359)[December 17, 2025 at 2:52 PM](https://oldvcr.blogspot.com/2025/12/oblast-better-blasto-game-for-commodore.html?showComment=1766011932334#c4211755048332672022)

Hey, thanks! It was fun to write. Hopefully you found it a worthy homage to the original(s).

[Delete](https://www.blogger.com/comment/delete/8349470052336612452/4211755048332672022)

Replies

Reply

Reply




Add comment

Load more...

Comments are subject to moderation. Be nice.

[](https://www.blogger.com/comment/frame/8349470052336612452?po=7899002469633843088&hl=en&saa=85391&origin=https://oldvcr.blogspot.com)

[Newer Post](https://oldvcr.blogspot.com/2025/12/the-texas-instruments-cc-40-invades.html "Newer Post") [Older Post](https://oldvcr.blogspot.com/2025/11/rebecca-heineman-has-died.html "Older Post") [Home](https://oldvcr.blogspot.com/)

Subscribe to: [Post Comments (Atom)](https://oldvcr.blogspot.com/feeds/7899002469633843088/comments/default)

## Welcome to Old VCR

My general vintage computing projects, mostly microcomputers, 6502, PalmOS, 68K/Power Mac and Unix workstations, but that's not all you'll see. While over the decades I've written for publications like _COMPUTE_ , _TidBITS_ and _Ars Technica_ , these articles are all original and just for you. My promise: No AI-generated article text, ever. All em-dashes are intentional and inserted _by hand_. Be kind, REWIND and PLAY. _\-- Cameron Kaiser_  
  
Old VCR is advertisement- and donation-funded, and what I get goes to maintaining the hardware here at Floodgap. I don't drink coffee, but the Mr Pibb doesn't buy itself. :-) Thanks for reading.  
  
[![Buy Me a Coffee at ko-fi.com](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/A0A5D7C0F)

## Greatest hits

  * [The April Fools joke that might have got me fired](https://oldvcr.blogspot.com/2025/04/the-april-fools-joke-that-might-have.html)
  * [The MIPS ThinkPad, kind of](https://oldvcr.blogspot.com/2022/09/the-mips-thinkpad-kind-of.html)
  * [What went wrong with wireless USB](https://oldvcr.blogspot.com/2025/05/what-went-wrong-with-wireless-usb.html)
  * [Dusting off Dreamcast Linux](https://oldvcr.blogspot.com/2023/02/dusting-off-dreamcast-linux.html)
  * [Meet your new two-factor authenticator: your Commodore 64](https://oldvcr.blogspot.com/2022/11/meet-your-new-two-factor-authenticator.html)
  * [So thieves broke into your storage unit - again](https://oldvcr.blogspot.com/2024/10/so-thieves-broke-into-your-storage-unit.html)
  * [If one GUI's not enough for your SPARC workstation, try four](https://oldvcr.blogspot.com/2022/10/if-one-guis-not-enough-for-your-sparc.html)
  * [Refurb weekend: Canon Cat](https://oldvcr.blogspot.com/2024/05/refurb-weekend-canon-cat.html)
  * [The Apple Network Server's all-too-secret weapon (featuring PPC Toolbox)](https://oldvcr.blogspot.com/2023/11/the-apple-network-servers-all-too.html)
  * [So long, home T1 line; hello, hacking the T1 router](https://oldvcr.blogspot.com/2022/05/so-long-home-t1-line-hello-hacking-t1.html)



## Other stuff I write

  * [Other classic computing posts from TenFourFox Development](http://tenfourfox.blogspot.com/search/label/anfscd)
  * [Talospace: OpenPOWER news and experiences from the free computing frontier](https://www.talospace.com/)
  * [Jerk Music Critic: music reviews worth what you paid for them](http://www.jerkmusiccritic.com/)



## About Me

[ ClassicHasClass ](https://www.blogger.com/profile/17331846076856918359)
[View my complete profile](https://www.blogger.com/profile/17331846076856918359)

## Blog Archive

  * [ ► ](javascript:void\(0\)) [ 2026 ](https://oldvcr.blogspot.com/2026/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](https://oldvcr.blogspot.com/2026/01/) (1)


  * [ ▼ ](javascript:void\(0\)) [ 2025 ](https://oldvcr.blogspot.com/2025/) (30)
    * [ ▼ ](javascript:void\(0\)) [ December ](https://oldvcr.blogspot.com/2025/12/) (4)
      * [Stewart Cheifet has died](https://oldvcr.blogspot.com/2025/12/stewart-cheifet-has-died.html)
      * [A Christmas 2007 video present from Old VCR with J...](https://oldvcr.blogspot.com/2025/12/a-christmas-2007-video-present-from-old.html)
      * [The Texas Instruments CC-40 invades Gopherspace (p...](https://oldvcr.blogspot.com/2025/12/the-texas-instruments-cc-40-invades.html)
      * [Oblast: a better Blasto game for the Commodore 64](https://oldvcr.blogspot.com/2025/12/oblast-better-blasto-game-for-commodore.html)
    * [ ► ](javascript:void\(0\)) [ November ](https://oldvcr.blogspot.com/2025/11/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](https://oldvcr.blogspot.com/2025/10/) (3)
    * [ ► ](javascript:void\(0\)) [ September ](https://oldvcr.blogspot.com/2025/09/) (2)
    * [ ► ](javascript:void\(0\)) [ August ](https://oldvcr.blogspot.com/2025/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](https://oldvcr.blogspot.com/2025/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](https://oldvcr.blogspot.com/2025/06/) (4)
    * [ ► ](javascript:void\(0\)) [ May ](https://oldvcr.blogspot.com/2025/05/) (3)
    * [ ► ](javascript:void\(0\)) [ April ](https://oldvcr.blogspot.com/2025/04/) (5)
    * [ ► ](javascript:void\(0\)) [ March ](https://oldvcr.blogspot.com/2025/03/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](https://oldvcr.blogspot.com/2025/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2024 ](https://oldvcr.blogspot.com/2024/) (25)
    * [ ► ](javascript:void\(0\)) [ December ](https://oldvcr.blogspot.com/2024/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](https://oldvcr.blogspot.com/2024/11/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](https://oldvcr.blogspot.com/2024/10/) (4)
    * [ ► ](javascript:void\(0\)) [ September ](https://oldvcr.blogspot.com/2024/09/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://oldvcr.blogspot.com/2024/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](https://oldvcr.blogspot.com/2024/06/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](https://oldvcr.blogspot.com/2024/05/) (3)
    * [ ► ](javascript:void\(0\)) [ April ](https://oldvcr.blogspot.com/2024/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](https://oldvcr.blogspot.com/2024/03/) (4)
    * [ ► ](javascript:void\(0\)) [ February ](https://oldvcr.blogspot.com/2024/02/) (2)
    * [ ► ](javascript:void\(0\)) [ January ](https://oldvcr.blogspot.com/2024/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2023 ](https://oldvcr.blogspot.com/2023/) (39)
    * [ ► ](javascript:void\(0\)) [ December ](https://oldvcr.blogspot.com/2023/12/) (1)
    * [ ► ](javascript:void\(0\)) [ November ](https://oldvcr.blogspot.com/2023/11/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](https://oldvcr.blogspot.com/2023/10/) (3)
    * [ ► ](javascript:void\(0\)) [ September ](https://oldvcr.blogspot.com/2023/09/) (5)
    * [ ► ](javascript:void\(0\)) [ August ](https://oldvcr.blogspot.com/2023/08/) (4)
    * [ ► ](javascript:void\(0\)) [ July ](https://oldvcr.blogspot.com/2023/07/) (4)
    * [ ► ](javascript:void\(0\)) [ June ](https://oldvcr.blogspot.com/2023/06/) (4)
    * [ ► ](javascript:void\(0\)) [ May ](https://oldvcr.blogspot.com/2023/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](https://oldvcr.blogspot.com/2023/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](https://oldvcr.blogspot.com/2023/03/) (3)
    * [ ► ](javascript:void\(0\)) [ February ](https://oldvcr.blogspot.com/2023/02/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](https://oldvcr.blogspot.com/2023/01/) (6)


  * [ ► ](javascript:void\(0\)) [ 2022 ](https://oldvcr.blogspot.com/2022/) (36)
    * [ ► ](javascript:void\(0\)) [ December ](https://oldvcr.blogspot.com/2022/12/) (5)
    * [ ► ](javascript:void\(0\)) [ November ](https://oldvcr.blogspot.com/2022/11/) (4)
    * [ ► ](javascript:void\(0\)) [ October ](https://oldvcr.blogspot.com/2022/10/) (6)
    * [ ► ](javascript:void\(0\)) [ September ](https://oldvcr.blogspot.com/2022/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](https://oldvcr.blogspot.com/2022/08/) (3)
    * [ ► ](javascript:void\(0\)) [ July ](https://oldvcr.blogspot.com/2022/07/) (3)
    * [ ► ](javascript:void\(0\)) [ June ](https://oldvcr.blogspot.com/2022/06/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](https://oldvcr.blogspot.com/2022/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](https://oldvcr.blogspot.com/2022/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](https://oldvcr.blogspot.com/2022/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](https://oldvcr.blogspot.com/2022/02/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](https://oldvcr.blogspot.com/2022/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2021 ](https://oldvcr.blogspot.com/2021/) (26)
    * [ ► ](javascript:void\(0\)) [ December ](https://oldvcr.blogspot.com/2021/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](https://oldvcr.blogspot.com/2021/11/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](https://oldvcr.blogspot.com/2021/10/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](https://oldvcr.blogspot.com/2021/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](https://oldvcr.blogspot.com/2021/08/) (5)
    * [ ► ](javascript:void\(0\)) [ June ](https://oldvcr.blogspot.com/2021/06/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](https://oldvcr.blogspot.com/2021/04/) (3)
    * [ ► ](javascript:void\(0\)) [ March ](https://oldvcr.blogspot.com/2021/03/) (4)
    * [ ► ](javascript:void\(0\)) [ February ](https://oldvcr.blogspot.com/2021/02/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](https://oldvcr.blogspot.com/2021/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2020 ](https://oldvcr.blogspot.com/2020/) (25)
    * [ ► ](javascript:void\(0\)) [ December ](https://oldvcr.blogspot.com/2020/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](https://oldvcr.blogspot.com/2020/11/) (5)
    * [ ► ](javascript:void\(0\)) [ October ](https://oldvcr.blogspot.com/2020/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](https://oldvcr.blogspot.com/2020/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](https://oldvcr.blogspot.com/2020/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](https://oldvcr.blogspot.com/2020/07/) (3)
    * [ ► ](javascript:void\(0\)) [ June ](https://oldvcr.blogspot.com/2020/06/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](https://oldvcr.blogspot.com/2020/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](https://oldvcr.blogspot.com/2020/04/) (3)



## Labels

  * [3d](https://oldvcr.blogspot.com/search/label/3d) (3)
  * [6502](https://oldvcr.blogspot.com/search/label/6502) (33)
  * [65816](https://oldvcr.blogspot.com/search/label/65816) (9)
  * [6800](https://oldvcr.blogspot.com/search/label/6800) (2)
  * [68000](https://oldvcr.blogspot.com/search/label/68000) (20)
  * [6809](https://oldvcr.blogspot.com/search/label/6809) (1)
  * [8051](https://oldvcr.blogspot.com/search/label/8051) (2)
  * [8080](https://oldvcr.blogspot.com/search/label/8080) (1)
  * [9995](https://oldvcr.blogspot.com/search/label/9995) (2)
  * [a/ux](https://oldvcr.blogspot.com/search/label/a%2Fux) (2)
  * [administrivia](https://oldvcr.blogspot.com/search/label/administrivia) (1)
  * [aix](https://oldvcr.blogspot.com/search/label/aix) (5)
  * [alpha micro](https://oldvcr.blogspot.com/search/label/alpha%20micro) (2)
  * [amiga](https://oldvcr.blogspot.com/search/label/amiga) (1)
  * [ans](https://oldvcr.blogspot.com/search/label/ans) (6)
  * [apple](https://oldvcr.blogspot.com/search/label/apple) (2)
  * [apple ii](https://oldvcr.blogspot.com/search/label/apple%20ii) (7)
  * [appletalk](https://oldvcr.blogspot.com/search/label/appletalk) (3)
  * [arcade](https://oldvcr.blogspot.com/search/label/arcade) (1)
  * [arduino](https://oldvcr.blogspot.com/search/label/arduino) (1)
  * [atari 8-bit](https://oldvcr.blogspot.com/search/label/atari%208-bit) (1)
  * [atari st](https://oldvcr.blogspot.com/search/label/atari%20st) (2)
  * [atarilab](https://oldvcr.blogspot.com/search/label/atarilab) (1)
  * [basic](https://oldvcr.blogspot.com/search/label/basic) (1)
  * [bebox](https://oldvcr.blogspot.com/search/label/bebox) (3)
  * [beos](https://oldvcr.blogspot.com/search/label/beos) (6)
  * [blasto](https://oldvcr.blogspot.com/search/label/blasto) (2)
  * [browser](https://oldvcr.blogspot.com/search/label/browser) (9)
  * [bucketlist](https://oldvcr.blogspot.com/search/label/bucketlist) (2)
  * [c128](https://oldvcr.blogspot.com/search/label/c128) (9)
  * [c264](https://oldvcr.blogspot.com/search/label/c264) (1)
  * [c64](https://oldvcr.blogspot.com/search/label/c64) (16)
  * [canon](https://oldvcr.blogspot.com/search/label/canon) (2)
  * [cap-x comp-x](https://oldvcr.blogspot.com/search/label/cap-x%20comp-x) (1)
  * [casio](https://oldvcr.blogspot.com/search/label/casio) (1)
  * [cc40](https://oldvcr.blogspot.com/search/label/cc40) (1)
  * [classilla](https://oldvcr.blogspot.com/search/label/classilla) (1)
  * [cobalt](https://oldvcr.blogspot.com/search/label/cobalt) (1)
  * [commodore](https://oldvcr.blogspot.com/search/label/commodore) (28)
  * [console](https://oldvcr.blogspot.com/search/label/console) (2)
  * [cp/m](https://oldvcr.blogspot.com/search/label/cp%2Fm) (1)
  * [cp1600](https://oldvcr.blogspot.com/search/label/cp1600) (1)
  * [cray](https://oldvcr.blogspot.com/search/label/cray) (1)
  * [crypto ancienne](https://oldvcr.blogspot.com/search/label/crypto%20ancienne) (4)
  * [data general](https://oldvcr.blogspot.com/search/label/data%20general) (2)
  * [dec](https://oldvcr.blogspot.com/search/label/dec) (3)
  * [dec alpha](https://oldvcr.blogspot.com/search/label/dec%20alpha) (1)
  * [decpro](https://oldvcr.blogspot.com/search/label/decpro) (2)
  * [dectalk](https://oldvcr.blogspot.com/search/label/dectalk) (1)
  * [dick smith](https://oldvcr.blogspot.com/search/label/dick%20smith) (2)
  * [dos](https://oldvcr.blogspot.com/search/label/dos) (2)
  * [dreamcast](https://oldvcr.blogspot.com/search/label/dreamcast) (2)
  * [emulation](https://oldvcr.blogspot.com/search/label/emulation) (1)
  * [firewire](https://oldvcr.blogspot.com/search/label/firewire) (1)
  * [forth](https://oldvcr.blogspot.com/search/label/forth) (2)
  * [fouo](https://oldvcr.blogspot.com/search/label/fouo) (1)
  * [future](https://oldvcr.blogspot.com/search/label/future) (1)
  * [geos](https://oldvcr.blogspot.com/search/label/geos) (1)
  * [gopher](https://oldvcr.blogspot.com/search/label/gopher) (8)
  * [graphics](https://oldvcr.blogspot.com/search/label/graphics) (6)
  * [hohoho](https://oldvcr.blogspot.com/search/label/hohoho) (2)
  * [hp](https://oldvcr.blogspot.com/search/label/hp) (4)
  * [hpux](https://oldvcr.blogspot.com/search/label/hpux) (3)
  * [humour](https://oldvcr.blogspot.com/search/label/humour) (3)
  * [iannetta](https://oldvcr.blogspot.com/search/label/iannetta) (1)
  * [ibm](https://oldvcr.blogspot.com/search/label/ibm) (3)
  * [intellivision](https://oldvcr.blogspot.com/search/label/intellivision) (1)
  * [inty](https://oldvcr.blogspot.com/search/label/inty) (1)
  * [irix](https://oldvcr.blogspot.com/search/label/irix) (1)
  * [itanium](https://oldvcr.blogspot.com/search/label/itanium) (1)
  * [ivory](https://oldvcr.blogspot.com/search/label/ivory) (1)
  * [kim-1](https://oldvcr.blogspot.com/search/label/kim-1) (9)
  * [linux](https://oldvcr.blogspot.com/search/label/linux) (1)
  * [lisp](https://oldvcr.blogspot.com/search/label/lisp) (1)
  * [lynx](https://oldvcr.blogspot.com/search/label/lynx) (4)
  * [mac](https://oldvcr.blogspot.com/search/label/mac) (16)
  * [mae](https://oldvcr.blogspot.com/search/label/mae) (1)
  * [magic cap](https://oldvcr.blogspot.com/search/label/magic%20cap) (2)
  * [mattel](https://oldvcr.blogspot.com/search/label/mattel) (1)
  * [mechanical](https://oldvcr.blogspot.com/search/label/mechanical) (1)
  * [memorials](https://oldvcr.blogspot.com/search/label/memorials) (17)
  * [microsoft](https://oldvcr.blogspot.com/search/label/microsoft) (1)
  * [mips](https://oldvcr.blogspot.com/search/label/mips) (7)
  * [netware](https://oldvcr.blogspot.com/search/label/netware) (1)
  * [networking](https://oldvcr.blogspot.com/search/label/networking) (15)
  * [nextstep](https://oldvcr.blogspot.com/search/label/nextstep) (1)
  * [nubus](https://oldvcr.blogspot.com/search/label/nubus) (1)
  * [osx](https://oldvcr.blogspot.com/search/label/osx) (1)
  * [palm](https://oldvcr.blogspot.com/search/label/palm) (8)
  * [panasonic](https://oldvcr.blogspot.com/search/label/panasonic) (1)
  * [parisc](https://oldvcr.blogspot.com/search/label/parisc) (5)
  * [pdp-11](https://oldvcr.blogspot.com/search/label/pdp-11) (2)
  * [pocket handheld](https://oldvcr.blogspot.com/search/label/pocket%20handheld) (4)
  * [pong](https://oldvcr.blogspot.com/search/label/pong) (7)
  * [power mac](https://oldvcr.blogspot.com/search/label/power%20mac) (23)
  * [powerpc](https://oldvcr.blogspot.com/search/label/powerpc) (12)
  * [prior art](https://oldvcr.blogspot.com/search/label/prior%20art) (4)
  * [protip](https://oldvcr.blogspot.com/search/label/protip) (4)
  * [refurb weekend](https://oldvcr.blogspot.com/search/label/refurb%20weekend) (24)
  * [review](https://oldvcr.blogspot.com/search/label/review) (6)
  * [science](https://oldvcr.blogspot.com/search/label/science) (1)
  * [sega](https://oldvcr.blogspot.com/search/label/sega) (2)
  * [sgi](https://oldvcr.blogspot.com/search/label/sgi) (2)
  * [sharp](https://oldvcr.blogspot.com/search/label/sharp) (1)
  * [smartwatch](https://oldvcr.blogspot.com/search/label/smartwatch) (3)
  * [software](https://oldvcr.blogspot.com/search/label/software) (58)
  * [solbourne](https://oldvcr.blogspot.com/search/label/solbourne) (4)
  * [sparc](https://oldvcr.blogspot.com/search/label/sparc) (4)
  * [spreadsheet](https://oldvcr.blogspot.com/search/label/spreadsheet) (1)
  * [sugarwater](https://oldvcr.blogspot.com/search/label/sugarwater) (1)
  * [sun](https://oldvcr.blogspot.com/search/label/sun) (2)
  * [sunray](https://oldvcr.blogspot.com/search/label/sunray) (2)
  * [superh](https://oldvcr.blogspot.com/search/label/superh) (3)
  * [symbolics](https://oldvcr.blogspot.com/search/label/symbolics) (1)
  * [tadpole](https://oldvcr.blogspot.com/search/label/tadpole) (1)
  * [tandy radio shack](https://oldvcr.blogspot.com/search/label/tandy%20radio%20shack) (2)
  * [terminal](https://oldvcr.blogspot.com/search/label/terminal) (13)
  * [thomson](https://oldvcr.blogspot.com/search/label/thomson) (1)
  * [ti](https://oldvcr.blogspot.com/search/label/ti) (7)
  * [tomy tutor](https://oldvcr.blogspot.com/search/label/tomy%20tutor) (5)
  * [toshiba](https://oldvcr.blogspot.com/search/label/toshiba) (1)
  * [unboxing](https://oldvcr.blogspot.com/search/label/unboxing) (1)
  * [unix](https://oldvcr.blogspot.com/search/label/unix) (16)
  * [unscreenshotable](https://oldvcr.blogspot.com/search/label/unscreenshotable) (5)
  * [usb](https://oldvcr.blogspot.com/search/label/usb) (5)
  * [usenet](https://oldvcr.blogspot.com/search/label/usenet) (1)
  * [venix](https://oldvcr.blogspot.com/search/label/venix) (1)
  * [video](https://oldvcr.blogspot.com/search/label/video) (1)
  * [vtech](https://oldvcr.blogspot.com/search/label/vtech) (1)
  * [wince](https://oldvcr.blogspot.com/search/label/wince) (2)
  * [windows](https://oldvcr.blogspot.com/search/label/windows) (4)
  * [winnt](https://oldvcr.blogspot.com/search/label/winnt) (1)
  * [wireless](https://oldvcr.blogspot.com/search/label/wireless) (1)
  * [workslate](https://oldvcr.blogspot.com/search/label/workslate) (2)
  * [x86](https://oldvcr.blogspot.com/search/label/x86) (3)
  * [x86_64](https://oldvcr.blogspot.com/search/label/x86_64) (1)
  * [yaddayaddayadda](https://oldvcr.blogspot.com/search/label/yaddayaddayadda) (1)
  * [z80](https://oldvcr.blogspot.com/search/label/z80) (3)



[![Buy Me a Coffee at ko-fi.com](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/A0A5D7C0F)

|   
---|---  
  
Copyright 2020-25 Cameron Kaiser. CC BY-NC-ND 4.0. Powered by [Blogger](https://www.blogger.com). 
  *[3:55 PM]: 2025-12-06T15:55:00-08:00
