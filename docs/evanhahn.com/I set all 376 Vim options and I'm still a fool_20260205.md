# I set all 376 Vim options and I'm still a fool

**来源:** https://evanhahn.com
**链接:** https://evanhahn.com/i-set-all-376-vim-options-and-im-still-a-fool/
**日期:** Fri, 16 Jan 2026 00:00:00 +0000

---

# I set all 376 Vim options and I'm still a fool

by [Evan Hahn](/), posted Jan 16, 2026

I set all of Vim's configuration options. I still feel far from mastery.

## First impressions of Vim: _wow_

I first saw someone use Vim during an internship in 2012.

I had been coding for many years and I fancied myself pretty good at shortcuts, but I was quickly humbled. I watched in awe as experienced users zipped around the code. A single keystroke could move the cursor halfway across the file to exactly the right spot. Code was ripped apart and reshaped like putty.

"_Wow_ ," I thought to myself, and probably said out loud.

## 13 years later, still clumsy

I vowed to master this editor but I was slow. When I wasn't accidentally opening some unknown menu, I was taking an uneconomical path through the code. I pressed `j` twenty times instead of running `20j`, or manually deleted code inside parenthesis instead of running `di(`. Sometimes I'd open another text editor to give my mind a break from all the key bindings!

Fast-forward to 2025. After tons of practice, I felt much more capable. Code _did_ feel more like putty. I was working closer to the speed of thought. I could get code where I wanted much more quickly. 13 years of practice paid off!

But Vim still felt clumsy. I was still accidentally opening menus I didn't recognize. I would do silly things like converting the whole file to lowercase, or trigger some scary error message. "Surely I shouldn't be making these mistakes," I thought. What could be done to finally master this editor?

## My goal: set every Vim option

That desire for expertise led me on a quest to _set all of Vim 's options_. I would make an informed decision about all 376 of Vim's settings and drop them in my `.vimrc`. In other words, I wanted to 100% Vim.

Surely, setting every Vim option would make me the fluent expert I wanted to be…right?

I pored over every single Vim option and made a decision. What did the option do, and what did I want it to be set to? My goal was to be thorough; leave no stone unturned. I only set the option after I understood it.

Eventually, after countless hours, I had done it. I had set every single Vim option.

## I learned a lot…

This exercise taught me plenty about day-to-day usage and the editor's inner workings. I spent a lot of time with the documentation, Vim's source code, and online forums.

Here's a grab bag of things I learned:

  * _How to use external commands._ I didn't realize I could send text from a Vim buffer to an external command, and vice-versa. Now I can write regular programs that operate on stdin. For example, I now frequently use [a program to remove "smart quotes"](https://codeberg.org/EvanHahn/dotfiles/src/commit/f7a9d94ae2254cb7e5f67e6e5bdb74b6467f6dec/home/bin/bin/straightquote), which I call without leaving the editor. See [`:help filter`](https://neovim.io/doc/user/change.html#filter) and [`:help write_c`](https://neovim.io/doc/user/editing.html#%3Awrite_c) for details.

  * _Vim 's docs are mixed._ I frequently ran the `:help` command for something, read the docs, and came away clueless. Thanks to the great people of the internet for so many great explanations! One of the flags stumped me so much that [I had to ask my own question on Vi Stack Exchange](https://vi.stackexchange.com/q/46863) because nobody had really documented it before.

  * _How Vim writes files._ When you run `:w`, it's just saving the file—how hard could it be? Turns out, it's complicated! If you're overwriting a file, Vim (by default) creates a backup of the old version, then overwrites it with the new version. This can help avoid data loss in some situations. But there's a lot of complexity here: in [the fate of that backup file after a successful write](https://vi.stackexchange.com/a/16846), in [how the backup switcharoo happens](https://neovim.io/doc/user/options.html#'backupcopy'), and [where the backup is saved](https://neovim.io/doc/user/options.html#'backupdir'). This is probably irrelevant for most people, but I had to understand the details in order to set every option.

  * _The command-line window—which I 'd always open by accident—is super useful._ The [`cedit` option](https://neovim.io/doc/user/options.html#'cedit') taught me about the [command-line window](https://neovim.io/doc/user/cmdline.html#_7.-command-line-window). I frequently opened this by running `q:` instead of `:q`, and didn't know what I had done. Now I know: a useful way to search and edit the history of previous commands and searches. For example, if I run some long command and make a typo, I can open the command-line window and fix the error using regular Vim keybindings.

  * _Digraphs are an obscure feature for typing obscure characters._ For example, you can enter "½" in Insert mode with `CTRL-K` `1` `2`. There's a big list in `:digraphs`. I don't use this much, except for typing fractions, but I use this more than I thought I would.

  * _How to set options conditionally._ I knew about regular `if` conditionals with things like `if has('nvim')`. But I didn't know that you could set a Vim option only if it's supported with code like `if exists('+option')`.

  * _Vim and Neovim have more differences than I thought._ Among [the many changes](https://neovim.io/doc/user/vim_diff.html), I was pleased to learn that [pasting is smoother in Neovim](https://neovim.io/doc/user/vim_diff.html#'pastetoggle'), that [`Q` repeats the last recorded macro](https://neovim.io/doc/user/repeat.html#Q), it [makes running arbitrary code safer](https://neovim.io/doc/user/editing.html#_12.-trusted-files), and has a much nicer default color scheme.

  * _Vim used to have a different name._ Today, "Vim" stands for "Vi IMproved", an old Unix editor from the 1970s. But it was originally called [Vi IMitation](https://github.com/vim/vim-history/tree/v1.24)!




This is just a sample of my many discoveries. For more, see [my heavily-annotated `init.vim`](https://codeberg.org/EvanHahn/dotfiles/src/commit/91685f0a629b584eb99ba715c441b918b9565ff0/home/vim/.config/nvim/init.vim).

## …but I'm still not fluent

As of this writing, my configuration file is nearly 2900 lines long.

This exercise was fun. It also taught me a lot about the editor I use every day. I definitely feel more skilled!

Yet the feeling of awkwardness remains. Even after ~14 years, I still accidentally open the command-line window all the time. I mess up filtering commands, or get lost in the [jumplist](https://neovim.io/doc/user/motion.html#jumplist). I still sometimes press `k` ten times instead of running `10k`.

I discovered one thing about myself. The feeling of true Vim fluency—one where every keystroke is exact, I never make mistakes, and I'm exploiting every obscure feature—is a fantasy, at least for me. That's a comforting constant in this topsy-turvy life: I'll always have more to learn about Vim.

[Click here to see the finished product.](https://codeberg.org/EvanHahn/dotfiles/src/commit/91685f0a629b584eb99ba715c441b918b9565ff0/home/vim/.config/nvim/init.vim)

[![](/images/logo_white.png)](/)

  * [About me](/)
  * [Contact](/contact/)
  * [Projects](/projects/)
  * [Guides](/guides/)
  * [Blog](/blog/)


  * [RSS](https://evanhahn.com/blog/index.xml)
  * [Newsletter](https://buttondown.com/evanhahn)
  * [Mastodon](https://bigshoulders.city/@EvanHahn)



Unless noted otherwise, content is licensed under the [Creative Commons Attribution-NonCommercial License](https://creativecommons.org/licenses/by-nc/4.0/) and code under the [Unlicense](https://unlicense.org/). Logo by [Lulu Tang](http://luluspice.com/). Profile photo by [Ali Boschert-Downs](https://www.instagram.com/boschertdowns/).
