# Conditions in the Intel 8087 floating-point chip's microcode

**来源:** https://righto.com
**链接:** http://www.righto.com/2025/12/8087-microcode-conditions.html
**日期:** 2025-12-30T10:00:00.000-08:00

---

#  [ Ken Shirriff's blog ](http://www.righto.com/)

Computer history, restoring vintage computers, IC reverse engineering, and whatever

###  Conditions in the Intel 8087 floating-point chip's microcode 

In the 1980s, if you wanted your computer to do floating-point calculations faster, you could buy the Intel 8087 floating-point coprocessor chip. Plugging it into your IBM PC would make operations up to 100 times faster, a big boost for spreadsheets and other number-crunching applications. The 8087 uses complicated algorithms to compute trigonometric, logarithmic, and exponential functions. These algorithms are implemented inside the chip in microcode. I'm part of a group that is reverse-engineering this microcode. In this post, I examine the 49 types of conditional tests that the 8087's microcode uses inside its algorithms. Some conditions are simple, such as checking if a number is zero or negative, while others are specialized, such as determining what direction to round a number.

To explore the 8087's circuitry, I opened up an 8087 chip and took numerous photos of the silicon die with a microscope. Around the edges of the die, you can see the hair-thin bond wires that connect the chip to its 40 external pins. The complex patterns on the die are formed by its metal wiring, as well as the polysilicon and silicon underneath. The bottom half of the chip is the "datapath", the circuitry that performs calculations on 80-bit floating point values. At the left of the datapath, a [constant ROM](https://www.righto.com/2020/05/extracting-rom-constants-from-8087-math.html) holds important constants such as π. At the right are the eight registers that the programmer uses to hold floating-point values; in an unusual design decision, these registers are arranged as a [stack](https://www.righto.com/2025/12/8087-stack-circuitry.html).

[![Die of the Intel 8087 floating point unit chip, with main functional blocks labeled. The die is 5mm×6mm.  Click for a larger image.](https://static.righto.com/images/8087-conditions/8087-die-labeled-w450.jpg)](https://static.righto.com/images/8087-conditions/8087-die-labeled.jpg)

Die of the Intel 8087 floating point unit chip, with main functional blocks labeled. The die is 5mm×6mm. Click for a larger image.

The chip's instructions are defined by the large [microcode ROM](https://www.righto.com/2018/09/two-bits-per-transistor-high-density.html) in the middle. To execute a floating-point instruction, the 8087 decodes the instruction and the microcode engine starts executing the appropriate micro-instructions from the microcode ROM. The microcode decode circuitry to the right of the ROM generates the appropriate control signals from each micro-instruction.1 The bus registers and control circuitry handle interactions with the main 8086 processor and the rest of the system.

## The 8087's microcode

Executing an 8087 instruction such as arctan requires hundreds of internal steps to compute the result. These steps are implemented in microcode with micro-instructions specifying each step of the algorithm. (Keep in mind the difference between the assembly language instructions used by a programmer and the undocumented low-level micro-instructions used internally by the chip.) The microcode ROM holds 1648 micro-instructions, implementing the 8087's instruction set. Each micro-instruction is 16 bits long and performs a simple operation such as moving data inside the chip, adding two values, or [shifting](https://www.righto.com/2020/05/die-analysis-of-8087-math-coprocessors.html) data. I'm working with the "Opcode Collective" to reverse engineer the micro-instructions and fully understand the microcode ([link](https://github.com/a-mcego/granite/blob/main/tools/8087mc/bin/8087.md)).

The microcode engine (below) controls the execution of micro-instructions, acting as the mini-CPU inside the 8087. Specifically, it generates an 11-bit micro-address, the address of a micro-instruction in the ROM. The microcode engine implements jumps, subroutine calls, and returns within the microcode. These jumps, subroutine calls, and returns are all conditional; the microcode engine will either perform the operation or skip it, depending on the value of a specified condition.

[![The microcode engine. In this image, the metal is removed, showing the underlying silicon and polysilicon.](https://static.righto.com/images/8087-conditions/engine-w200.jpg)](https://static.righto.com/images/8087-conditions/engine.jpg)

The microcode engine. In this image, the metal is removed, showing the underlying silicon and polysilicon.

I'll write more about the microcode engine later, but I'll give an overview here. At the top, the Instruction Decode PLA2 decodes an 8087 instruction to determine the starting address in microcode. Below that, the Jump PLA holds microcode addresses for jumps and subroutine calls. Below this, six 11-bit registers implement the microcode stack, allowing six levels of subroutine calls inside the microcode. (Note that this stack is completely different from the 8087's register stack that holds eight floating-point values.) The stack registers have associated read/write circuitry. The incrementer adds one to the micro-address to step through the code. The engine also implements relative jumps, using an adder to add an offset to the current location. At the bottom, the address latch and drivers boost the 11-bit address output and send it to the microcode ROM.

## Selecting a condition

A micro-instruction can say "jump ahead 5 micro-instructions if a register is zero" and the microcode engine will either perform the jump or ignore it, based on the register value. In the circuitry, the condition causes the microcode engine to either perform the jump or block the jump. But how does the hardware select one condition out of the large set of conditions?

Six bits of the micro-instruction can specify one of 64 conditions. A circuit similar to the idealized diagram below selects the specified condition. The key component is a multiplexer, represented by a trapezoid below. A multiplexer is a simple circuit that selects one of its four inputs. By arranging multiplexers in a tree, one of the 64 conditions on the left is selected and becomes the output, passed to the microcode engine.

[![A tree of multiplexers selects one of the conditions. This diagram is simplified.](https://static.righto.com/images/8087-conditions/muxtree2-w400.jpg)](https://static.righto.com/images/8087-conditions/muxtree2.jpg)

A tree of multiplexers selects one of the conditions. This diagram is simplified.

For example, if bits J and K of the microcode are 00, the rightmost multiplexer will select the first input. If bits LM are 01, the middle multiplexer will select the second input, and if bits NO are 10, the left multiplexer will select its third input. The result is that condition 06 will pass through the tree and become the output.3 By changing the bits that control the multiplexers, any of the inputs can be used. (We've arbitrarily given the 16 microcode bits the letter names A through P.)

Physically, the conditions come from locations scattered across the die. For instance, conditions involving the opcode come from the instruction decoding part of the chip, while conditions involving a register are evaluated next to the register. It would be inefficient to run 64 wires for all the conditions to the microcode engine. The tree-based approach reduces the wiring since the "leaf" multiplexers can be located near the associated condition circuitry. Thus, only one wire needs to travel a long distance rather than multiple wires. In other words, the condition selection circuitry is distributed across the chip instead of being implemented as a centralized module.

Because the conditions don't always fall into groups of four, the actual implementation is slightly different from the idealized diagram above. In particular, the top-level multiplexer has five inputs, rather than four.4 Other multiplexers don't use all four inputs. This provides a better match between the physical locations of the condition circuits and the multiplexers. In total, 49 of the possible 64 conditions are implemented in the 8087.

The circuit that selects one of the four conditions is called a multiplexer. It is constructed from pass transistors, transistors that are configured to either pass a signal through or block it. To operate the multiplexer, one of the select lines is energized, turning on the corresponding pass transistor. This allows the selected input to pass through the transistor to the output, while the other inputs are blocked.

[![A 4-1 multiplexer, constructed from four pass transistors.](https://static.righto.com/images/8087-conditions/multiplexer-w250.jpg)](https://static.righto.com/images/8087-conditions/multiplexer.jpg)

A 4-1 multiplexer, constructed from four pass transistors.

The diagram below shows how a multiplexer appears on the die. The pinkish regions are doped silicon. The white lines are polysilicon wires. When polysilicon crosses over doped silicon, a transistor is formed. On the left is a four-way multiplexer, constructed from four pass transistors. It takes inputs (black) for four conditions, numbered 38, 39, 3a, and 3b. There are four control signals (red) corresponding to the four combinations of bits N and O. One of the inputs will pass through a transistor to the output, selected by the active control signal. The right half contains the logic (four NOR gates and two inverters) to generate the control signals from the microcode bits. (Metal lines run horizontally from the logic to the control signal contacts, but I dissolved the metal for this photo.) Each multiplexer in the 8087 has a completely different layout, manually optimized based on the location of the signals and surrounding circuitry. Although the circuit for a multiplexer is regular (four transistors in parallel), the physical layout looks somewhat chaotic.

[![Multiplexers as they appear on the die. The metal layer has been removed to show the polysilicon and silicon. The "tie-die" patterns are due to thin-film effects where the oxide layer wasn't completely removed.](https://static.righto.com/images/8087-conditions/mux-diagram-w500.jpg)](https://static.righto.com/images/8087-conditions/mux-diagram.jpg)

Multiplexers as they appear on the die. The metal layer has been removed to show the polysilicon and silicon. The "tie-die" patterns are due to thin-film effects where the oxide layer wasn't completely removed.

The 8087 uses pass transistors for many circuits, not just multiplexers. Circuits with pass transistors are different from regular logic gates because the pass transistors provide no amplification. Instead, signals get weaker as they go through pass transistors. To solve this problem, inverters or buffers are inserted into the condition tree to boost signals; they are omitted from the diagram above.

## The conditions

Of the 8087's 49 different conditions, some are widely used in the microcode, while others are designed for a specific purpose and are only used once. The full set of conditions is described in a footnote7 but I'll give some highlights here.

Fifteen conditions examine the bits of the current instruction's opcode. This allows one microcode routine to handle a group of similar instructions and then change behavior based on the specific instruction. For example, conditions test if the instruction is multiplication, if the instruction is an FILD/FIST (integer load or store), or if the bottom bit of the opcode is set.5

The 8087 has three temporary registers--tmpA, tmpB, and tmpC--that hold values during computation. Various conditions examine the values in the tmpA and tmpB registers.6 In particular, the 8087 uses an interesting way to store numbers internally: each 80-bit floating-point value also has two "tag" bits. These bits are mostly invisible to the programmer and can be thought of as metadata. The tag bits indicate if a register is empty, contains zero, contains a "normal" number, or contains a special value such as NaN (Not a Number) or infinity. The 8087 uses the tag bits to optimize operations. The tags also detect stack overflow (storing to a non-empty stack register) or stack underflow (reading from an empty stack register).

Other conditions are highly specialized. For instance, one condition looks at the rounding mode setting and the sign of the value to determine if the value should be rounded up or down. Other conditions deal with exceptions such as numbers that are too small (i.e. denormalized) or numbers that lose precision. Another condition tests if two values have the same sign or not. Yet another condition tests if two values have the same sign or not, but inverts the result if the current instruction is subtraction. The simplest condition is simply "true", allowing an unconditional branch.

For flexibility, conditions can be "flipped", either jumping if the condition is true or jumping if the condition is false. This is controlled by bit P of the microcode. In the circuitry, this is implemented by a gate that XORs the P bit with the condition. The result is that the state of the condition is flipped if bit P is set.

For a concrete example of how conditions are used, consider the [microcode routine](https://raw.githubusercontent.com/a-mcego/granite/refs/heads/main/tools/8087mc/bin/8087mc_out.txt#:~:text=%230896%09AB%20%20%20%20%20%20I%20%20L%20N%20%20%09c094%09%2Bjmp%2D%3E%230898%20cond%3D0x0a%20opcode%261) that implements `FCHS` and `FABS`, the instructions to change the sign and compute the absolute value, respectively. These operations are almost the same (toggling the sign bit versus clearing the sign bit), so the same microcode routine handles both instructions, with a jump instruction to handle the difference. The `FABS` and `FCHS` instructions were designed with identical opcodes, except that the bottom bit is set for `FABS`. Thus, the microcode routine uses a condition that tests the bottom bit, allowing the routine to branch and change its behavior for `FABS` vs `FCHS`.

Looking at the relevant micro-instruction, it has the hex value `0xc094`, or in binary `110 000001 001010 0`. The first three bits (ABC=110) specify the relative jump operation (100 would jump to a fixed target and 101 would perform a subroutine call.) Bits D through I (`000010`) indicate the amount of the jump (+`). Bits J through O (`001010`, hex 0a) specify the condition to test, in this case, the last bit of the instruction opcode. The final bit (P) would toggle the condition if set, (i.e. jump if false). Thus, for `FABS`, the jump instruction will jump ahead one micro-instruction. This has the effect of skipping the next micro-instruction, which sets the appropriate sign bit for `FCHS`.

## Conclusions

The 8087 performs floating-point operations much faster than the 8086 by using special hardware, optimized for floating-point. The condition code circuitry is one example of this: the 8087 can test a complicated condition in a single operation. However, these complicated conditions make it much harder to understand the microcode. But by a combination of examining the circuitry and looking at the micocode, we're making progress. Thanks to the members of the "Opcode Collective" for their hard work, especially Smartest Blob and Gloriouscow.

For updates, follow me on Bluesky ([@righto.com](https://bsky.app/profile/righto.com)), Mastodon ([@[email protected]](https://oldbytes.space/@kenshirriff)), or [RSS](http://www.righto.com/feeds/posts/default).

## Notes and references

  1. The section of the die that I've labeled "Microcode decode" performs some of the microcode decoding, but large parts of the decoding are scattered across the chip, close to the circuitry that needs the signals. This makes reverse-engineering the microcode much more difficult. I thought that understanding the microcode would be straightforward, just examining a block of decode circuitry. But this project turned out to be much more complicated and I need to reverse-engineer the entire chip. ↩

  2. A PLA is a "Programmable Logic Array". It is a technique to implement logic functions with grids of transistors. A PLA can be used as a compressed ROM, holding data in a more compact representation. (Saving space was very important in chips of this era.) In the 8087, PLAs are used to hold tables of microcode addresses. ↩

  3. Note that the multiplexer circuit selects the condition corresponding to the binary value of the bits. In the example, bits 000110 (0x06) select condition 06. ↩

  4. The five top-level multiplexer inputs correspond to bit patterns 00, 011, 10, 110, and 111. That is, two inputs depend on bits J and K, while three inputs depend on bits J, K, and L. The bit pattern 010 is unused, corresponding to conditions 0x10 through 0x17, which aren't implemented. ↩

  5. The 8087 acts as a co-processor with the 8086 processor. The 8086 instruction set is designed so instructions with a special "ESCAPE" sequence in the top 5 bits are processed by the co-processor, in this case the 8087. Thus, the 8087 receives a 16-bit instruction, but only the bottom 11 bits are usable. For a memory operation, the second byte of the instruction is an 8086-style [ModR/M](https://en.wikipedia.org/wiki/ModR/M) byte. For instructions that don't access memory, the second byte specifies more of the instruction and sometimes specifies the stack register to use for the instruction.

The relevance of this is that the 8087's microcode engine uses the 11 bits of the instruction to determine which microcode routine to execute. The microcode also uses various condition codes to change behavior depending on different bits of the instruction. ↩

  6. There is a complication with the tmpA and tmpB registers: they can be swapped with the micro-instruction "ABC.EF". The motivation behind this is that if you have two arguments, you can use a micro-subroutine to load an argument into tmpA, swap the registers, and then use the same subroutine to load the second argument into tmpA. The result is that the two arguments end up in tmpB and tmpA without any special coding in the subroutine.

The implementation doesn't physically swap the registers, but renames them internally, which is much more efficient. A flip-flop is toggled every time the registers are swapped. If the flip-flop is set, a request goes to one register, while if the flip-flop is clear, a request goes to the other register. (Many processors use the same trick. For instance, the Intel 8080 has an instruction to exchange the DE and HL registers. The Z80 has an instruction to swap register banks. In both cases, a flip-flop renames the registers, so the data doesn't need to move.) ↩

  7. The table below is the real meat of this post, the result of much circuit analysis. These details probably aren't interesting to most people, so I've relegated the table to a footnote. Descriptions in italics are provided by Smartest Blob based on examination of the microcode. Grayed-out lines are unused conditions.

The table has five sections, corresponding to the 5 inputs to the top-level condition multiplexer. These inputs come from different parts of the chip, so the sections correspond to different categories of conditions.

The first section consists of instruction parsing, with circuitry near the microcode engine. The description shows the 11-bit opcode pattern that triggers the condition, with 0 bits and 1 bits as specified, and X indicating a "don't care" bit that can be 0 or 1. Where simpler, I list the relevant instructions instead.

The next section indicates conditions on the exponent. I am still investigating these conditions, so the descriptions are incomplete. The third section is conditions on the temporary registers or conditions related to the control register. These circuits are to the right of the microcode ROM.

Conditions in the fourth section examine the floating-point bus, with circuitry near the bottom of the chip. Conditions 34 and 35 use a special 16-bit bidirectional shift register, at the far right of the chip. The top bit from the floating-point bus is shifted in. Maybe this shift register is used for CORDIC calculations? The conditions in the final block are miscellaneous, including the always-true condition 3e, which is used for unconditional jumps.

Cond.| Description  
---|---  
  
00| not XXX 11XXXXXX | 01| 1XX 11XXXXXX | 02| 0XX 11XXXXXX | 03| X0X XXXXXXXX | 04| not cond 07 or 1XX XXXXXXXX | 05| not FLD/FSTP temp-real or BCD | 06| 110 xxxxxxxx or 111 xx0xxxxx | 07| FLD/FSTP temp-real | 08| FBLD/FBSTP | 09|  __|  0a| XXX XXXXXXX1 | 0b| XXX XXXX1XXX | 0c| FMUL | 0d| FDIV FDIVR | 0e| FADD FCOM FCOMP FCOMPP FDIV FDIVR FFREE FLD FMUL FST FSTP FSUB FSUBR FXCH | 0f| FCOM FCOMP FCOMPP FTST | 10|  __|  11|  __|  12|  __|  13|  __|  14|  __|  15|  __|  16|  __|  17|  __|  18| exponent condition | 19| exponent condition | 1a| exponent condition | 1b| exponent condition | 1c| exponent condition | 1d| exponent condition | 1e| eight exponent zero bits | 1f| exponent condition | 20| tmpA tag ZERO | 21| tmpA tag SPECIAL | 22| tmpA tag VALID | 23|  _stack overflow_ | 24| tmpB tag ZERO | 25| tmpB tag SPECIAL | 26| tmpB tag VALID | 27|  _st(i) doesn't exist (A)?_ | 28| tmpA sign | 29| tmpB top bit | 2a| tmpA zero | 2b| tmpA top bit | 2c| Control Reg bit 12: infinity control | 2d| round up/down | 2e| unmasked interrupt | 2f| DE (denormalized) interrupt | 30| top reg bit | 31|  __|  32| reg bit 64 | 33| reg bit 63 | 34| Shifted top bits, all zero | 35| Shifted top bits, one out | 36|  __|  37|  __|  38| const latch zero | 39| tmpA vs tmpB sign, flipped for subtraction | 3a| precision exception | 3b| tmpA vs tmpB sign | 3c|  __|  3d|  __|  3e| unconditional | 3f|  __ This table is under development and undoubtedly has errors. ↩

[ ![](http://img1.blogblog.com/img/icon18_email.gif) ](https://www.blogger.com/email-post/6264947694886887540/52646111832574839 "Email Post") [ ![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=6264947694886887540&postID=52646111832574839&from=pencil "Edit Post") [Email This](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=52646111832574839&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=52646111832574839&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=52646111832574839&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=52646111832574839&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=52646111832574839&target=pinterest "Share to Pinterest") Labels: [8087](http://www.righto.com/search/label/8087), [chips](http://www.righto.com/search/label/chips), [electronics](http://www.righto.com/search/label/electronics), [intel](http://www.righto.com/search/label/intel), [reverse-engineering](http://www.righto.com/search/label/reverse-engineering)

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/6264947694886887540/52646111832574839) [Newer Post](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html "Newer Post") [Older Post](http://www.righto.com/2025/12/8087-stack-circuitry.html "Older Post") [Home](http://www.righto.com/) [Subscribe](https://righto.kit.com/20bf534dff
) [Contact info and site index](https://www.righto.com/p/index.html)

## Popular Posts

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_vtCZCd6I2eEGvoKC-Vkizh0bxJKvSC5D2u4aTGpgX-f4Ojpy4k9kb79oQQ5sGmRhOOziB4nfB_1g2c8zv8twAF2eu4RkeDxWx-GPa7NFDzbhg=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html) [A Multi-Protocol Infrared Remote Library for the Arduino](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html)
  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_ty6E6R0RWcYjL18ma0miSQYK_vhmhifjp34ZGkPeJfrTELN8bFwxc1zeNPjZ15YO6hlWevHRiCDJipI6DJi0XQPbMmCpHNgbZAzX016l0i16_5mvKLweY5XeGkueF7OOl2ybk5X2LzPQ=w72-h72-p-k-no-nu) ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html) [Notes on the Intel 8086 processor's arithmetic-logic unit](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)
  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sE745igru2h0824H9fxZrM6nbTOTA3QotwQ5cui68LD97yMGJWRQs5JnjqPakBRQwfLzgq842NQXhP3IjbyrffdakHGUCh69fx2mPlDr-zxgS6YtHG5lzbj_FeojA=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html) [A dozen USB chargers in the lab: Apple is very good, but not quite the best](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html)
  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_uLq9hZI_QHNGK_SpdEyFGaw4qWsyYCzkDoKfUFZS5E5qG5KN3H_3w7YPsE57Un_Xk2kbP9pZxSQSOciZZKfUToobq4UNHXJDn7uHkEgpOlr6L06oZ-VTDlpSimplShFPPWaPdiC2fLXuHSTcNrjwmLU6o=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html) [Apple iPhone charger teardown: quality in a tiny expensive package](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html)
  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_t1qL1SRGsUZ1yPmUbfFaX8AYvP0Nu8YgI1vjh77CTBD4Y4Z4DX5sdJ2vW0C3R63r7Ap-Lrpf54VZ0VNlEoO3PMCE2RkrrpSJsgQchvTB3s94WPcNxi0XQGFBKa81WNsVlOewrKsnqss2IYHryR=w72-h72-p-k-no-nu) ](http://www.righto.com/2025/12/8087-microcode-conditions.html) [Conditions in the Intel 8087 floating-point chip's microcode](http://www.righto.com/2025/12/8087-microcode-conditions.html)
  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_vaBAMUx8zqaJtZh57Y8jcQ_UjEoRlvtPz0MErZqMi6b4vwFLQJXtiDsJizgIQMOrn6mDOk5vOfkow12L9EHmWD-7fk-gBXgPnDoQf_E0VLkUyyDJkFrX9W1U7D3BNJwKz_0I50jRNzddPnJ1E=w72-h72-p-k-no-nu) ](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html) [Teardown and exploration of Apple's Magsafe connector](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html)
  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sORJ-6TatijwQ3XQ18dVZOQ-b_ow1O5EQgJFXXQxluOG4m6sKAchDkvwr8ooUzw9iibVZK6EfGzTKXOX7v2q0VO3PaI4ZXCV0wDeOJDG7rAp3ynKvn-bFv4zSY2yNxbNkv=w72-h72-p-k-no-nu) ](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html) [Mining Bitcoin with pencil and paper: 0.67 hashes per day](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html)
  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_tZhtHJr8RqJgaXsDd7CQ4Ca73N2vycjBJgOa3dDmMod2qK7vUTLJiw-OqNab_55800jC1mqtmQMIwmugDSc0guh6Ersv_7LCVsNqXXajiQ=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html) [An Arduino universal remote: record and playback IR signals](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html)



## Search This Blog

|  |   
---|---  
  
## Labels

[386](http://www.righto.com/search/label/386) [6502](http://www.righto.com/search/label/6502) [8008](http://www.righto.com/search/label/8008) [8085](http://www.righto.com/search/label/8085) [8086](http://www.righto.com/search/label/8086) [8087](http://www.righto.com/search/label/8087) [8088](http://www.righto.com/search/label/8088) [aerospace](http://www.righto.com/search/label/aerospace) [alto](http://www.righto.com/search/label/alto) [analog](http://www.righto.com/search/label/analog) [Apollo](http://www.righto.com/search/label/Apollo) [apple](http://www.righto.com/search/label/apple) [arc](http://www.righto.com/search/label/arc) [arduino](http://www.righto.com/search/label/arduino) [arm](http://www.righto.com/search/label/arm) [beaglebone](http://www.righto.com/search/label/beaglebone) [bitcoin](http://www.righto.com/search/label/bitcoin) [c#](http://www.righto.com/search/label/c%23) [cadc](http://www.righto.com/search/label/cadc) [calculator](http://www.righto.com/search/label/calculator) [chips](http://www.righto.com/search/label/chips) [css](http://www.righto.com/search/label/css) [datapoint](http://www.righto.com/search/label/datapoint) [dx7](http://www.righto.com/search/label/dx7) [electronics](http://www.righto.com/search/label/electronics) [f#](http://www.righto.com/search/label/f%23) [fairchild](http://www.righto.com/search/label/fairchild) [fpga](http://www.righto.com/search/label/fpga) [fractals](http://www.righto.com/search/label/fractals) [genome](http://www.righto.com/search/label/genome) [globus](http://www.righto.com/search/label/globus) [haskell](http://www.righto.com/search/label/haskell) [HP](http://www.righto.com/search/label/HP) [html5](http://www.righto.com/search/label/html5) [ibm](http://www.righto.com/search/label/ibm) [ibm1401](http://www.righto.com/search/label/ibm1401) [ibm360](http://www.righto.com/search/label/ibm360) [intel](http://www.righto.com/search/label/intel) [ipv6](http://www.righto.com/search/label/ipv6) [ir](http://www.righto.com/search/label/ir) [java](http://www.righto.com/search/label/java) [javascript](http://www.righto.com/search/label/javascript) [math](http://www.righto.com/search/label/math) [microcode](http://www.righto.com/search/label/microcode) [oscilloscope](http://www.righto.com/search/label/oscilloscope) [Pentium](http://www.righto.com/search/label/Pentium) [photo](http://www.righto.com/search/label/photo) [power supply](http://www.righto.com/search/label/power%20supply) [random](http://www.righto.com/search/label/random) [reverse-engineering](http://www.righto.com/search/label/reverse-engineering) [sheevaplug](http://www.righto.com/search/label/sheevaplug) [snark](http://www.righto.com/search/label/snark) [space](http://www.righto.com/search/label/space) [spanish](http://www.righto.com/search/label/spanish) [synth](http://www.righto.com/search/label/synth) [teardown](http://www.righto.com/search/label/teardown) [theory](http://www.righto.com/search/label/theory) [unicode](http://www.righto.com/search/label/unicode) [Z-80](http://www.righto.com/search/label/Z-80)

## Blog Archive

  * [ ► ](javascript:void\(0\)) [ 2026 ](http://www.righto.com/2026/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2026/01/) (1)


  * [ ▼ ](javascript:void\(0\)) [ 2025 ](http://www.righto.com/2025/) (22)
    * [ ▼ ](javascript:void\(0\)) [ December ](http://www.righto.com/2025/12/) (2)
      * [Conditions in the Intel 8087 floating-point chip's...](http://www.righto.com/2025/12/8087-microcode-conditions.html)
      * [The stack circuitry of the Intel 8087 floating poi...](http://www.righto.com/2025/12/8087-stack-circuitry.html)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2025/11/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2025/10/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2025/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2025/08/) (4)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2025/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2025/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2025/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2025/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2025/03/) (3)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2025/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2025/01/) (4)


  * [ ► ](javascript:void\(0\)) [ 2024 ](http://www.righto.com/2024/) (21)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2024/12/) (1)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2024/11/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2024/10/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2024/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2024/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2024/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2024/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2024/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2024/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2024/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2024/02/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2024/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2023 ](http://www.righto.com/2023/) (35)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2023/12/) (4)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2023/11/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2023/10/) (3)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2023/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2023/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2023/07/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2023/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2023/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2023/03/) (4)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2023/02/) (5)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2023/01/) (8)


  * [ ► ](javascript:void\(0\)) [ 2022 ](http://www.righto.com/2022/) (18)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2022/11/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2022/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2022/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2022/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2022/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2022/04/) (4)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2022/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2022/02/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2022/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2021 ](http://www.righto.com/2021/) (26)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2021/12/) (4)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2021/11/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2021/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2021/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2021/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2021/06/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2021/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2021/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2021/03/) (4)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2021/02/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2021/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2020 ](http://www.righto.com/2020/) (33)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2020/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2020/11/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2020/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2020/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2020/08/) (5)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2020/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2020/06/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2020/05/) (4)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2020/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2020/03/) (5)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2020/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2019 ](http://www.righto.com/2019/) (18)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2019/11/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2019/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2019/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2019/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2019/07/) (4)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2019/04/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2019/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2019/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2018 ](http://www.righto.com/2018/) (17)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2018/12/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2018/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2018/08/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2018/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2018/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2018/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2018/03/) (3)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2018/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2018/01/) (4)


  * [ ► ](javascript:void\(0\)) [ 2017 ](http://www.righto.com/2017/) (21)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2017/12/) (5)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2017/11/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2017/10/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2017/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2017/07/) (2)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2017/06/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2017/04/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2017/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2017/02/) (1)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2017/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2016 ](http://www.righto.com/2016/) (34)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2016/12/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2016/10/) (5)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2016/09/) (8)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2016/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2016/07/) (3)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2016/06/) (4)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2016/05/) (1)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2016/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2016/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2016/02/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2016/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2015 ](http://www.righto.com/2015/) (12)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2015/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2015/11/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2015/10/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2015/08/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2015/05/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2015/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2015/02/) (1)


  * [ ► ](javascript:void\(0\)) [ 2014 ](http://www.righto.com/2014/) (13)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2014/12/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2014/10/) (1)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2014/09/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2014/05/) (2)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2014/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2014/02/) (5)


  * [ ► ](javascript:void\(0\)) [ 2013 ](http://www.righto.com/2013/) (24)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2013/11/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2013/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2013/08/) (4)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2013/07/) (4)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2013/06/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2013/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2013/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2013/02/) (2)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2013/01/) (3)


  * [ ► ](javascript:void\(0\)) [ 2012 ](http://www.righto.com/2012/) (10)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2012/12/) (1)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2012/11/) (5)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2012/10/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2012/05/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2012/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2012/02/) (1)


  * [ ► ](javascript:void\(0\)) [ 2011 ](http://www.righto.com/2011/) (11)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2011/12/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2011/07/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2011/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2011/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2011/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2011/02/) (3)


  * [ ► ](javascript:void\(0\)) [ 2010 ](http://www.righto.com/2010/) (22)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2010/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2010/11/) (4)
    * [ ► ](javascript:void\(0\)) [ October ](http://www.righto.com/2010/10/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2010/08/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2010/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2010/05/) (2)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2010/04/) (3)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2010/03/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2010/01/) (2)


  * [ ► ](javascript:void\(0\)) [ 2009 ](http://www.righto.com/2009/) (22)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2009/12/) (2)
    * [ ► ](javascript:void\(0\)) [ November ](http://www.righto.com/2009/11/) (5)
    * [ ► ](javascript:void\(0\)) [ September ](http://www.righto.com/2009/09/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](http://www.righto.com/2009/08/) (3)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2009/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2009/06/) (3)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2009/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2009/03/) (3)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2009/02/) (2)
    * [ ► ](javascript:void\(0\)) [ January ](http://www.righto.com/2009/01/) (1)


  * [ ► ](javascript:void\(0\)) [ 2008 ](http://www.righto.com/2008/) (27)
    * [ ► ](javascript:void\(0\)) [ July ](http://www.righto.com/2008/07/) (3)
    * [ ► ](javascript:void\(0\)) [ June ](http://www.righto.com/2008/06/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](http://www.righto.com/2008/05/) (3)
    * [ ► ](javascript:void\(0\)) [ April ](http://www.righto.com/2008/04/) (4)
    * [ ► ](javascript:void\(0\)) [ March ](http://www.righto.com/2008/03/) (10)
    * [ ► ](javascript:void\(0\)) [ February ](http://www.righto.com/2008/02/) (6)



## Don't miss a post!

Subscribe to get updates by email.




Subscribe

​

[Built with Kit](https://kit.com/features/forms?utm_campaign=poweredby&utm_content=form&utm_medium=referral&utm_source=dynamic)

|   
---|---  
  
Powered by [Blogger](https://www.blogger.com). 
