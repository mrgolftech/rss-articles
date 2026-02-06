# Clever memory tricks

**来源:** https://xania.org
**链接:** http://xania.org/202512/22-memory-cunningness?utm_source=feed&utm_medium=rss
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


## Clever memory tricks

Written by me, proof-read by an LLM.   
Details at end.

After exploring SIMD vectorisation over the last [couple](/202512/20-simd-city) of [days](/202512/21-vectorising-floats), let's shift gears to look at another class of compiler cleverness: memory access patterns. String comparisons seem straightforward enough - check the length, compare the bytes, done. But watch what Clang does when comparing against compile-time constants, and you'll see some rather clever tricks involving overlapping memory reads and bitwise operations. What looks like it should be a call to `memcmp` becomes a handful of inline instructions that exploit the fact that the comparison value is known at compile time1.

I've set up nine functions that each compare a `std::string_view` against a constant string of increasing length, from one to nine characters. This gives us a chance to see how the compiler's approach changes based on the length of the comparison.

As we learned when looking at [calling conventions](/202512/16-calling-conventions), a `std::string_view` is a pointer and a length, passed in two registers on x86 Linux. Each of these functions receives a `std::size_t` length in `rdi` and a `const char *` pointer in `rsi`2. One might reasonably expect a call to `memcmp`, but the compiler has both [inlined](/202512/17-inlining-the-ultimate-optimisation) and specialised the comparison for each constant string. Let's take a look at some of these comparison functions, starting with `t1`:
    
    
    t1:
      cmp rdi, 1                ; is length 1?
      jne .LBB0_1               ; if not 1, goto "return false"
      cmp byte ptr [rsi], 65    ; is the byte 65 ('A')?
      sete al                   ; set result to 0 or 1 accordingly
      ret                       ; return
    .LBB0_1:
      xor eax, eax              ; set result to false
      ret                       ; return
    

We see the length is checked first, and if it's not 1, then we return. Otherwise, we check the one character to see if it's `A` or not, and then set the return value accordingly. The compiler has used a conditional set `sete` instruction to avoid a second branch.

The pattern holds for power-of-two sizes: Looking at `t2`, `t4` and `t8` we see that the compiler does the same length check, and then cleverly realises it can compare a 2, 4 or 8-byte value directly with a constant of either `AB`, `ABCD` or `ABCDEFGH` (mouse over the constants in the view to see Compiler Explorer interpret them as ASCII).

Things get more interesting with the 7 character case, `t7`:
    
    
    t7:
      cmp rdi, 7                    ; is length 7?
      jne .LBB6_1                   ; if not, goto "return false"
      mov eax, 1145258561           ; set eax to "ABCD"
      xor eax, dword ptr [rsi]      ; eax ^= first four chars of sv
      mov ecx, 1195787588           ; set ecx to "DEFG"
      xor ecx, dword ptr [rsi + 3]  ; ecx ^= chars 3,4,5,6 of sv
      or ecx, eax                   ; ecx |= eax
      sete al                       ; result = 1 if "zero flag" else 0
      ret                           ; return
    

The check for the length is the same as the other cases, but once we know we're going to be comparing 7 bytes, some cunning tricks come into play. First, the compiler isn't directly comparing, as you might expect: It uses the fact that XORing identical values will result in a zero. Secondly, it has used two _overlapping_ reads - reading bytes 0,1,2,3 and then 3,4,5,6. The redundant read of byte 3 doesn't matter, but doing two 32-bit reads is cheaper than having to read individual bytes.

Once the two XORs have happened, we have "zero only if first four bytes match ABCD" in `eax` and "zero only if bytes 3,4,5,6 match DEFG" in `ecx`. Simply logical-ORing the two together gives us zero if and only if both were zero - only if all bytes matched. Then a simple `sete` turns the "zero flag" into either 0 or 1 for the `true`/`false` return value needed. Cute!

This optimisation works well on x86 as reading unaligned 32-bit values is free. You can play around with the compiler choice and see what neat tricks are conjured up by different compilers and architecture choices.

And that's what makes modern compilers remarkable - all this cleverness is conjured up from a simple `sv == "ABCDEFG"sv`. The overlapping reads, the XOR operations, the branchless conditionals - they're all applied automatically. Your job is to write clear code; the compiler's job is to make it fast. Leave it to do its thing, and try not to get in its way!

_See[the video](https://youtu.be/kXmqwJoaapg) that accompanies this post._

* * *

_This post is day 22 of[Advent of Compiler Optimisations 2025](/AoCO2025-archive), a 25-day series exploring how compilers transform our code._

_â[When SIMD Fails: Floating Point Associativity](/202512/21-vectorising-floats) | [Switching it up a bit](/202512/23-switching-it-up) â_

_This post was written by a human ([Matt Godbolt](/MattGodbolt)) and reviewed and proof-read by LLMs and humans._

_Support Compiler Explorer on[Patreon](https://patreon.com/c/mattgodbolt) or [GitHub](https://github.com/sponsors/compiler-explorer), or by buying CE products in the [Compiler Explorer Shop](https://shop.compiler-explorer.com)_.

* * *

  1. GCC generates more obvious, but slightly worse code, with some unnecessary logic operations. I [filed a bug](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=122315) to investigate. ↩

  2. libstdc++'s `std::string_view` is defined as [length then pointer](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/libstdc++/api/a00227_source.html#l00102), which is why we see length in `rdi` before pointer in `rsi`. ↩




[Permalink](/202512/22-memory-cunningness)

Filed under: [Coding](/Coding) [AoCO2025](/AoCO2025)

Posted at 06:00:00 CST on 22nd December 2025.

### About Matt Godbolt

[Matt Godbolt](/MattGodbolt) is a C++ developer living in Chicago. He works for [Hudson River Trading](https://www.hudsonrivertrading.com/) on super fun but secret things. He is one half of the [Two's Complement](https://twoscomplement.org) podcast. Follow him on [Mastodon](https://hachyderm.io/@mattgodbolt) or [Bluesky](https://bsky.app/profile/matt.godbolt.org). 

Copyright 2007-2026 Matt Godbolt. Unless otherwise stated, all content is licensed under the [Creative Commons Attribution-Noncommercial 3.0 Unported License](https://creativecommons.org/licenses/by-nc/3.0/). This blog is powered by the MalcBlogSystem by [Malcolm Rowe](https://www.farside.org.uk/). **Note:** This is my personal website. The views expressed on these pages are mine alone and not those of my employer. 
