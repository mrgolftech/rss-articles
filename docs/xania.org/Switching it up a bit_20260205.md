# Switching it up a bit

**来源:** https://xania.org
**链接:** http://xania.org/202512/23-switching-it-up?utm_source=feed&utm_medium=rss
**日期:** 

---

  * # [Matt Godbolt's blog](/)

  * Menu



  * Tags
    * [AI](/AI)
    * [Amusing Stuff](/Amusing-Stuff)
    * [AoCO2025](/AoCO2025)
    * [Blog](/Blog)
    * [Coding](/Coding)
    * [Compiler Explorer](/Compiler-Explorer)
    * [Emulation](/Emulation)
    * [Games](/Games)
    * [Microarchitecture](/Microarchitecture)
    * [New Zealand Trip](/New-Zealand-Trip)
    * [Personal](/Personal)
    * [Python](/Python)
    * [Rants](/Rants)
    * [Rust](/Rust)
    * [WeeBox Project](/WeeBox-Project)
  * Archive
    * [AI](/AI-archive)
    * [Amusing Stuff](/Amusing-Stuff-archive)
    * [AoCO2025](/AoCO2025-archive)
    * [Blog](/Blog-archive)
    * [Coding](/Coding-archive)
    * [Compiler Explorer](/Compiler-Explorer-archive)
    * [Emulation](/Emulation-archive)
    * [Games](/Games-archive)
    * [Microarchitecture](/Microarchitecture-archive)
    * [New Zealand Trip](/New-Zealand-Trip-archive)
    * [Personal](/Personal-archive)
    * [Python](/Python-archive)
    * [Rants](/Rants-archive)
    * [Rust](/Rust-archive)
    * [WeeBox Project](/WeeBox-Project-archive)
  * About
    * [About me](/MattGodbolt)
    * [Contact me](mailto:matt@godbolt.org)
    * [ ![View Matt Godbolt's profile on LinkedIn](https://www.linkedin.com/img/webpromo/btn_liprofile_blue_80x15.gif)](https://www.linkedin.com/in/godbolt)
  * 


## Switching it up a bit

Written by me, proof-read by an LLM.   
Details at end.

The standard wisdom is that switch statements compile to jump tables. And they do - when the compiler can't find something cleverer to do instead.

Let's start with a really simple example:

Here the compiler has spotted the relationship between `x` and the return value, and rewritten the code as: `if (x < 5) return (x+1) * 100; else return 0;` \- pretty neat. No jump table, just maths!

If we mix up the code a bit so there's no obvious relationship between the input and the return value:

Still no jump table: Now the compiler has built a bespoke lookup table (`CSWTCH.1`) and then uses `x` to index into it (after checking it's in bounds).

For "dense" case statements, like the ones above, the compiler can be smart. But even with relatively sparse inputs, the compiler can work its magic. Consider this "is it whitespace?" routine1:

That _still_ avoids any kind of jump table; and in fact even avoids a branch:
    
    
    is_whitespace(char):
      sub edi, 9            ; edi = x - 9 (`\t`)
      mov eax, 8388631      ; eax = 0b100000000000000000010111
      bt rax, rdi           ; test bit edi in the eax bitmask
      setc al               ; al = (bit was set) ? 1 : 0
      xor edx, edx          ; edx = 0
      cmp dil, 24           ; compare edi with 24
      cmovnb eax, edx       ; replace al with edx (0) if not below
      ret                   ; return
    

The compiler has built a bitmask where each bit says "should we consider this character to be whitespace". To fit the range of bits needed to cover all the whitespace characters, the compiler indexes into the bitmask with `(x - 9)`. The bit test instruction ([`bt`](https://www.felixcloutier.com/x86/bt)) will test any bit position, but our 32-bit bitmask only has meaningful data in positions 0-31. The compiler checks that `(x - 9) <= 24` to ensure we're within the valid range 2 of the bitmask (covering tab at position 0 through space at position 23), and replaces the result with 0 for anything outside this range.

Just to see what else the compiler can generate, let's take a look at both a dense and sparse example that the compiler can't replace with a table (you'll need to scroll around in the Compiler Explorer panes to see more):

For the dense case, the compiler does make a jump table, and indexes by `x` to jump to the right `func` routine3. For the sparse case, the compiler has to fall back to essentially a set of `if()` statements, comparing and branching. However, it's clever enough to compare a "mid-range" value first (`2511`), and if the `x` value is greater, jumps to code that only looks at the `5284` and `4865`. So it's essentially a binary serarch tree of comparisons.

Different compilers employ quite different tricks, so take some time to see what clang does for all the above examples.

Write clear switch statements; let the compiler decide whether that means multiplication, bitmasks, or jump tables. It's pretty darned good at it!

_See[the video](https://youtu.be/aSljdPafBAw) that accompanies this post._

* * *

_This post is day 23 of[Advent of Compiler Optimisations 2025](/AoCO2025-archive), a 25-day series exploring how compilers transform our code._

_â[Clever memory tricks](/202512/22-memory-cunningness) | [When compilers surprise you](/202512/24-cunning-clang) â_

_This post was written by a human ([Matt Godbolt](/MattGodbolt)) and reviewed and proof-read by LLMs and humans._

_Support Compiler Explorer on[Patreon](https://patreon.com/c/mattgodbolt) or [GitHub](https://github.com/sponsors/compiler-explorer), or by buying CE products in the [Compiler Explorer Shop](https://shop.compiler-explorer.com)_.

* * *

  1. Of course you should use `isspace()`. ↩

  2. The `bt` instruction uses the bit position modulo the operand size. In this particular case the compiler emits a `bt rax, rdi` so values of (x-9) greater than 64 would potentially map onto some of the set bits. ↩

  3. If you comment out the `case 4`, at least for GCC, you'll see the compiler goes back to compare-and-branch. ↩




[Permalink](/202512/23-switching-it-up)

Filed under: [Coding](/Coding) [AoCO2025](/AoCO2025)

Posted at 06:00:00 CST on 23rd December 2025.

### About Matt Godbolt

[Matt Godbolt](/MattGodbolt) is a C++ developer living in Chicago. He works for [Hudson River Trading](https://www.hudsonrivertrading.com/) on super fun but secret things. He is one half of the [Two's Complement](https://twoscomplement.org) podcast. Follow him on [Mastodon](https://hachyderm.io/@mattgodbolt) or [Bluesky](https://bsky.app/profile/matt.godbolt.org). 

Copyright 2007-2026 Matt Godbolt. Unless otherwise stated, all content is licensed under the [Creative Commons Attribution-Noncommercial 3.0 Unported License](https://creativecommons.org/licenses/by-nc/3.0/). This blog is powered by the MalcBlogSystem by [Malcolm Rowe](https://www.farside.org.uk/). **Note:** This is my personal website. The views expressed on these pages are mine alone and not those of my employer. 
