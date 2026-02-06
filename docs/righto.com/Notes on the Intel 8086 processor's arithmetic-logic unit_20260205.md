# Notes on the Intel 8086 processor's arithmetic-logic unit

**来源:** https://righto.com
**链接:** http://www.righto.com/2026/01/notes-on-intel-8086-processors.html
**日期:** 2026-01-23T09:09:00.000-08:00

---

#  [ Ken Shirriff's blog ](http://www.righto.com/)

Computer history, restoring vintage computers, IC reverse engineering, and whatever

###  Notes on the Intel 8086 processor's arithmetic-logic unit 

In 1978, Intel introduced the 8086 processor, a revolutionary chip that led to the modern x86 architecture. Unlike modern 64-bit processors, however, the 8086 is a 16-bit chip. Its arithmetic/logic unit (ALU) operates on 16-bit values, performing arithmetic operations such as addition and subtraction, as well as logic operations including bitwise AND, OR, and XOR. The 8086's ALU is a complicated part of the chip, performing 28 operations in total.1

In this post, I discuss the circuitry that controls the ALU, generating the appropriate control signals for a particular operation. The process is more complicated than you might expect. First, a machine code instruction results in the execution of multiple microcode instructions. Using the ALU is a two-step process: one microcode instruction (micro-instruction) configures the ALU for the desired operation, while a second micro-instruction gets the results from the ALU. Moreover, based on both the microcode micro-instruction and the machine code instruction, the control circuitry sends control signals to the ALU, reconfiguring it for the desired operation. Thus, this circuitry provides the "glue" between the micro-instructions and the ALU.

The die photo below shows the 8086 processor under a microscope. I've labeled the key functional blocks. Architecturally, the chip is partitioned into a Bus Interface Unit (BIU) at the top and an Execution Unit (EU) below. The BIU handles bus and memory activity as well as instruction prefetching, while the Execution Unit (EU) executes the instructions. In the lower right corner, the microcode ROM holds the micro-instructions. The ALU is in the lower left corner, with bits 7-0 above and bits 15-8 below, sandwiching the status flag circuitry. The ALU control circuitry, highlighted in red at the bottom of the chip, is the focus of this article.

[![The die of the 8086 with the metal layer removed to show the silicon and polysilicon underneath. Click this image \(or any other\) for a larger version.](https://static.righto.com/images/8086-alu-notes/die-labeled2-w600.jpg)](https://static.righto.com/images/8086-alu-notes/die-labeled2.jpg)

The die of the 8086. Click this image (or any other) for a larger version.

## Microcode

The 8086 processor implements most machine instructions in microcode, with a micro-instruction for each step of the machine instruction. (I discuss the 8086's microcode in detail [here](https://www.righto.com/2022/11/how-8086-processors-microcode-engine.html).) The 8086 uses an interesting architecture for microcode: each micro-instruction performs two unrelated operations. The first operation moves data between a source and a destination. The second operation can range from a jump or subroutine call to a memory read/write or an ALU operation. An ALU operation has a five-bit field to specify a particular operation and a two-bit field to specify which temporary register provides the input. As you'll see below, these two fields play an important role in the ALU circuitry.

In many cases, the 8086's micro-instruction doesn't specify the ALU operation, leaving the details to be substituted from the machine instruction opcode. For instance, the ADD, SUB, ADC, SBB, AND, OR, XOR, and CMP machine instructions share the same microcode, while the hardware selects the ALU operation from the instruction opcode. Likewise, the increment and decrement instructions use the same microcode, as do the decimal adjust instructions DAA and DAS, and the ASCII adjust instructions AAA and AAS. Inside the micro-instruction, all these operations are performed with a "pseudo" ALU operation called XI (for some reason). If the microcode specifies an XI ALU operation, the hardware replaces it with the ALU operation specified in the instruction. Another important feature of the microcode is that you need to perform one ALU micro-instruction to configure the ALU's operation, but the result isn't available until a later micro-instruction, which moves the result to a destination. This has the consequence that the hardware must remember the ALU operation.

To make this concrete, here is the microcode that implements a typical arithmetic instruction such as `ADD AL, BL` or `XOR [BX+DI], CX`. This microcode consists of three micro-instructions. The left half of each micro-instruction specifies a data movement, first moving the two arguments to ALU temporary registers and then storing the ALU result (called Σ). The right half of each micro-instruction performs the second task. First, the ALU is configured to perform an `XI` operation using temporary register A. Recall that `XI` indicates the ALU operation is filled in from the machine instruction; this is how the same microcode handles eight different types of machine instructions. In the second micro-instruction, the next machine instruction is started unless a memory writeback is required (`WB`). The last micro-instruction is `RNI` (Run Next Instruction) to start a new machine instruction. It also indicates that the processor status flags (`F`) should be updated to indicate if the ALU result is zero, positive, overflow, and so forth.2
    
    
    M -> tmpa   XI   tmpa  Load first argument, configure ALU.
    R -> tmpb   WB,NXT     Load second argument, start Next instruction if no memory writeback
    Σ -> M      RNI  F     Store ALU result, Run Next Instruction, update status Flags
    

## The ALU circuit

The ALU is the heart of a processor, performing arithmetic and logic operations. Microprocessors of the 1970s typically supported addition and subtraction; logical AND, OR, and XOR; and various bit shift operations. (Although the 8086 had multiply and divide instructions, these were implemented in microcode, not in the ALU.) Since an ALU is both large and critical to performance, chip architects try to optimize its design. As a result, different microprocessors have widely different ALU designs. For instance, the 6502 microprocessor has separate circuits for addition and each logic operation; a multiplexer selects the appropriate output. The Intel 8085, on the other hand, uses an optimized clump of gates that performs the desired operation based on control signals ([details](https://www.righto.com/2013/01/inside-alu-of-8085-microprocessor.html)), while the Z80's 4-bit ALU uses a different clump of gates ([details](https://www.righto.com/2013/09/the-z-80-has-4-bit-alu-heres-how-it.html)).

The 8086 takes a different approach, using two lookup tables (along with other gates) to generate the carry and output signals for each bit in the ALU. By setting the lookup tables appropriately, the ALU can be configured to perform the desired operation. (This is similar to how an FPGA implements arbitrary functions through lookup tables.) The schematic below shows the circuit for one bit of the ALU. I won't explain this circuit in detail since I explained it in [an earlier article](https://www.righto.com/2020/08/reverse-engineering-8086s.html).3 The relevant part of this circuit is the six control signals at the left. The two multiplexers (trapezoidal symbols) implement the lookup tables by using the two input argument bits to select outputs from the control signals to control carry generation and carry propagation. Thus, by feeding appropriate control signals into the ALU, the 8086 can reconfigure the ALU to perform the desired operation. For instance, with one set of control signals, this circuit will add. Other sets of control signals will cause the circuit to subtract or compute a logical operation, such as AND or XOR. The 8086 has 16 copies of this circuit, so it operates on 16-bit values.

[![The circuit that implements one bit in the 8086's ALU.](https://static.righto.com/images/8086-alu-notes/alu-schematic-w600.png)](https://static.righto.com/images/8086-alu-notes/alu-schematic.png)

The circuit that implements one bit in the 8086's ALU.

The 8086 is a complicated processor, and its instructions have many special cases, so controlling the ALU is more complex than described above. For instance, the compare operation is the same as a subtraction, except the numerical result of a compare is discarded; just the status flags are updated. The add versus add-with-carry instructions require different values for the carry into bit 0, while subtraction requires the carry flag to be inverted since it is treated as a borrow. The 8086's ALU supports increment and decrement operations, but also increment and decrement by 2, which requires an increment signal into bit 1 instead of bit 0. The bit-shift operations all require special treatment. For instance, a rotate can use the carry bit or exclude the carry bit, while and arithmetic shift right requires the top bit to be duplicated. As a result, along with the six lookup table (LUT) control signals, the ALU also requires numerous control signals to adjust its behavior for specific instructions. In the next section, I'll explain how these control signals are generated.

## ALU control circuitry on the die

The diagram below shows the components of the ALU control logic as they appear on the die. The information from the micro-instruction enters at the right and is stored in the latches. The PLAs (Programmable Logic Arrays) decode the instruction and generate the control signals. These signals flow to the left, where they control the ALU.

[![The ALU control logic as it appears on the die. I removed the metal layer to show the underlying polysilicon and silicon. The reddish lines are remnants of the metal.](https://static.righto.com/images/8086-alu-notes/logic-labeled-w500.jpg)](https://static.righto.com/images/8086-alu-notes/logic-labeled.jpg)

The ALU control logic as it appears on the die. I removed the metal layer to show the underlying polysilicon and silicon. The reddish lines are remnants of the metal.

As explained earlier, if the microcode specifies the `XI` operation, the operation field is replaced with a value based on the machine instruction opcode. This substitution is performed by the `XI` multiplexer before the value is stored in the operation latch. Because of the complexity of the 8086 instruction set, the `XI` operation is not as straightforward as you might expect. This multiplexer gets three instruction bits from a special register called the "X" register, another instruction bit from the instruction register, and the final bit from a decoding circuit called the Group Decode ROM.4

Recall that one micro-instruction specifies the ALU operation, and a later micro-instruction accesses the result. Thus, the ALU control circuitry must remember the specified operation so it can be used later. In particular, the control circuitry must keep track of the ALU operation to perform and the temporary register specified. The control circuitry uses three flip-flops to keep track of the specified temporary register, one flip-flop for each register. The micro-instruction contains a two-bit field that specifies the temporary register. The control circuitry decodes this field and activates the associated flip-flop. The outputs from these flip-flops go to the ALU and enable the associated temporary register. At the start of each machine instruction,5 the flip-flops are reset, so temporary register A is selected by default.

The control circuitry uses five flip-flops to store the five-bit operation field from the micro-instruction. At the start of each machine instruction, the flip-flops are reset so operation 0 (ADD) is specified by default. One important consequence is that an add operation can potentially be performed without a micro-instruction to configure the ALU, shortening the microcode by one micro-instruction and thus shortening the instruction time by one cycle.

The five-bit output from the operation flip-flops goes to the operation PLA (Programmable Logic Array)7, which decodes the operation into 27 control signals.6 Many of these signals go to the ALU, where they control the behavior of the ALU for special cases. About 15 of these signals go to the Lookup Table (LUT) PLA, which generates the six lookup table signals for the ALU. At the left side of the LUT PLA, special high-current driver circuits amplify the control signals before they are sent to the ALU. Details on these drivers are in the footnotes.8

## Conclusions

Whenever I look at the circuitry of the 8086 processor, I see the differences between a RISC chip and a CISC chip. In a RISC (Reduced Instruction Set Computer) processor such as ARM, instruction decoding is straightforward, as is the processor circuitry. But in the 8086, a CISC (Complex Instruction Set Computer) processor, there are corner cases and complications everywhere. For instance, an 8086 machine instruction sometimes specifies the ALU operation in the first byte and sometimes in the second byte, and sometimes elsewhere, so the X register latch, the XI multiplexer, and the Group Decode ROM are needed. The 8086's ALU includes obscure operations including four types of BCD adjustments and seven types of shifts, making the ALU more complicated. Of course, the continuing success of x86 shows that this complexity also has benefits.

This article has been a deep dive into the details of the 8086's ALU, but I hope you have found it interesting. If it's too much detail for you, you might prefer my overview of the [8086 ALU](https://www.righto.com/2020/08/reverse-engineering-8086s.html).

For updates, follow me on Bluesky ([@righto.com](https://bsky.app/profile/righto.com)), Mastodon ([@[email protected]](https://oldbytes.space/@kenshirriff)), or [RSS](http://www.righto.com/feeds/posts/default).

Credits: Thanks to Marcin Peczarski for discussion. My microcode analysis is based on Andrew Jenner's [8086 microcode disassembly](https://www.reenigne.org/blog/8086-microcode-disassembled/).

## Notes and references

  1. The operations implemented by the ALU are:

00| ADD| Add  
---|---|---  
01| OR| Logical OR  
02| ADC| Add with carry in  
03| SBB| Subtract with borrow in  
04| AND| Logical AND  
05| SUBT| Subtract  
06| XOR| Logical XOR  
07| CMP| Comparison  
08| ROL| Rotate left  
09| ROR| Rotate right  
0a| LRCY| Left rotate through carry  
0b| RRCY| Right rotate through carry  
0c| SHL| Shift left  
0d| SHR| Shift right  
0e| SETMO| Set to minus one ([questionable](https://www.righto.com/2023/07/undocumented-8086-instructions.html#fn:setmo))  
0f| SAR| Arithmetic shift right  
10| PASS| Pass argument unchanged  
11| XI| Instruction specifies ALU op  
14| DAA| Decimal adjust after addition  
15| DAS| Decimal adjust after subtraction  
16| AAA| ASCII adjust after addition  
17| AAS| ASCII adjust after subtraction  
18| INC| Increment  
19| DEC| Decrement  
1a| COM1| 1's complement  
1b| NEG| Negate  
1c| INC2| Increment by 2  
1d| DEC2| Decrement by 2  
  
Also see Andrew Jenner's [code](https://github.com/reenigne/reenigne/blob/master/8088/8086_microcode/8086_microcode.cpp). ↩

  2. You might wonder how this microcode handles the 8086's complicated addressing modes such as `[BX+DI]`. The trick is that microcode subroutines implement the addressing modes. For details, see my article on [8086 addressing microcode](https://www.righto.com/2023/02/8086-modrm-addressing.html). ↩

  3. The 8086's ALU has a separate circuit to implement shift-right. The problem is that data in an ALU normally flows right-to-left as carries flow from lower bits to higher bits. Shifting data to the right goes against this direction, so it requires a special path. (Shifting to the left is straightforward; you can add a number to itself.)

The adjust operations (DAA, DAS, AAA, AAS) also use completely separate circuitry. These operations generate correction factors for BCD (binary-coded decimal) arithmetic based on the value and flags. The circuitry for these operations is located with the flags circuitry, separate from the rest of the ALU circuitry. ↩

  4. In more detail, the 8086 stores bits 5-3 of the machine instruction in the "X" register. For an XI operation, the X register bits become bits 2-0 of the ALU operation specification, while bit 3 comes from bit 6 of the instruction, and bit 4 comes from the [Group Decode ROM](https://www.righto.com/2023/05/8086-processor-group-decode-rom.html) for certain instructions. The point of this is that the instruction set is designed so bits of the instruction correspond to bits of the ALU operation specifier, but the mapping is more complicated than you might expect. The eight basic arithmetic/logic operations (ADD, SUB, OR, etc) have a straightforward mapping that is visible from the [8086 opcode table](http://www.mlsite.net/8086/), but the mapping for other instructions isn't as obvious. Moreover, sometimes the operation is specified in the first byte of the machine instruction, but sometimes it is specified in the second byte, which is why the X register needs to store the relevant bits. ↩

  5. The flip-flops are reset by a signal in the 8086, called "Second Clock". When a new machine instruction is started, the "First Clock" signal is generated on the instruction's first byte and the "Second Clock" signal is generated on the instruction's second byte. (Note that these signals are not necessarily on consecutive clock cycles, because a memory fetch may be required if the instruction queue is empty.) Why are the flip-flops reset on Second Clock and not First Clock? The 8086 has a small degree of pipelining, so the previous micro-instruction may still be finishing up during First Clock of the next instruction. By Second Clock, it is safe to reset the ALU state. ↩

  6. For reference, the 27 outputs from the PLA are triggered by the following ALU micro-operations:

Output 0: RRCY (right rotate through carry)   
Output 1: ROR (Rotate Right)   
Output 2: BCD Adjustments: DAA (Decimal Adjust after Addition), DAS (Decimal Adjust after Subtraction), AAA (ASCII Adjust after Subtraction), or AAS (ASCII Adjust after Subtraction)   
Output 3: SAR (Shift Arithmetic Right)   
Output 4: Left shift: ROL (Rotate Left), RCL (Rotate through Carry Left), SHL (Shift Left), or SETMO (Set Minus One)   
Output 5: Right shift: ROR (Rotate Right), RCR (Rotate through Carry Right), SHR (Shift Right), or SAR (Shift Arithmetic Right)   
Output 6: INC2 (increment by 2)   
Output 7: ROL (Rotate Left)   
Output 8: RCL (Rotate through Carry Left)   
Output 9: ADC (add with carry)   
Output 10: DEC2 (decrement by 2)   
Output 11: INC (increment)   
Output 12: NEG (negate)   
Output 13: ALU operation 12 (unused?)   
Output 14: SUB (Subtract), CMP (Compare), DAS (Decimal Adjust after Subtraction), AAS (ASCII Adjust after Subtraction)   
Output 15: SBB (Subtract with Borrow)   
Output 16: ROL (Rotate Left) or RCL (Rotate through Carry Left)   
Output 17: ADD or ADC (Add with Carry)   
Output 18: DEC or DEC2 (Decrement by 1 or 2)   
Output 19: PASS (pass-through) or INC (Increment)   
Output 20: COM1 (1's Complement) or NEG (Negate)   
Output 21: XOR   
Output 22: OR   
Output 23: AND   
Output 24: SHL (Shift Left)   
Output 25: DAA or AAA (Decimal/ASCII Adjust after Addition)   
Output 26: CMP (Compare) ↩

  7. A Programmable Logic Array is a way of implementing logic gates in a structured grid. PLAs are often used in microprocessors because they provide a dense way of implementing logic. A PLA normally consists of two layers: an "OR" layer and an "AND" layer. Together, the layers produce "sum-of-products" outputs, consisting of multiple terms OR'd together. The ALU's PLA is a bit unusual because many outputs are taken directly from the OR layer, while only about 15 outputs from the first layer are fed into the second layer. ↩

  8. The control signals pass through the driver circuit below. The operation of this circuit puzzled me for years, since the transistor with its gate at +5V seems to be stuck on. But I was looking at the book [DRAM Circuit Design](https://amzn.to/49JlB8M) and spotted the same circuit, called the "Bootstrap Wordline Driver". The purpose of this circuit is to boost the output to a higher voltage than a regular NMOS circuit, providing better performance. The problem with NMOS circuitry is that NMOS transistors aren't very good at pulling a signal high: due to the properties of the transistor, the output voltage is less than the gate voltage, lower by the threshold voltage VTH, half a volt or more.

[![The drive signals to the ALU gates are generated with this dynamic circuit.](https://static.righto.com/images/8086-alu-notes/signal-drive-w250.png)](https://static.righto.com/images/8086-alu-notes/signal-drive.png)

The drive signals to the ALU gates are generated with this dynamic circuit.

The bootstrap circuit takes advantage of capacitance to get more voltage out of the circuit. Specifically, suppose the input is +5V, while the clock is high. Point A will be about 4.5V, losing half a volt due to the threshold. Now, suppose the clock goes low, so the inverted clock driving the upper transistor goes high. Due to capacitance in the second transistor, as the source and drain go high, the gate will be pulled above its previous voltage, maybe gaining a couple of volts. The high voltage on the gate produces a full-voltage output, avoiding the drop due to VTH. But why the transistor with its gate at +5V? This transistor acts somewhat like a diode, preventing the boosted voltage from flowing backward through the input and dissipating.

The bootstrap circuit is used on the ALU's lookup table control signals for two reasons. First, these control signals drive pass transistors. A pass transistor suffers from a voltage drop due to the threshold voltage, so you want to start with a control signal with as high a voltage as possible. Second, each control signal is connected to 16 transistors (one for each bit). This is a large number of transistors to drive from one signal, since each transistor has gate capacitance. Increasing the voltage helps overcome the R-C (resistor-capacitor) delay, improving performance.

[![A close-up of the bootstrap drive circuits, in the left half of the LUT PLA.](https://static.righto.com/images/8086-alu-notes/bootstrap-diagram-w400.jpg)](https://static.righto.com/images/8086-alu-notes/bootstrap-diagram.jpg)

A close-up of the bootstrap drive circuits, in the left half of the LUT PLA.

The diagram above shows six bootstrap drivers on the die. At the left are the transistors that ground the signals when clock is high. The +5V transistors are scattered around the image; two of them are labeled. The six large transistors provide the output signal, controlled by clock'. Note that these transistors are much larger than the other transistors because they must produce the high-current output, while the other transistors have more of a supporting role.

(Bootstrap circuits go way back; Federico Faggin designed a bootstrap circuit for the [Intel 8008](https://www.righto.com/2020/10/how-bootstrap-load-made-historic-intel.html) that he claimed "proved essential to the microprocessor realization.") ↩




[ ![](http://img1.blogblog.com/img/icon18_email.gif) ](https://www.blogger.com/email-post/6264947694886887540/7538688365288775324 "Email Post") [ ![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=6264947694886887540&postID=7538688365288775324&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=7538688365288775324&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=7538688365288775324&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=7538688365288775324&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=7538688365288775324&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=7538688365288775324&target=pinterest "Share to Pinterest")

#### 7 comments:

[![](//resources.blogblog.com/img/blank.gif) ](https://int10h.org/blog)

[VileR](https://int10h.org/blog) said... 
    

The full die photo shows the 8088, not the 8086 as written. The overall layout of the functional blocks is still the same of course, so no big deal... just a heads-up. 

     [ January 23, 2026 at 5:35 PM ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html?showComment=1769218549111#c587018746851893738 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/587018746851893738 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png) ](https://www.blogger.com/profile/08097301407311055124)

[Ken Shirriff](https://www.blogger.com/profile/08097301407311055124) said... 
    

Thanks, VileR. I don't know how I mixed up the die images. I've updated with the correct die. 

     [ January 23, 2026 at 6:10 PM ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html?showComment=1769220637709#c4974916204990240088 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/4974916204990240088 "Delete Comment")

[![](//resources.blogblog.com/img/blank.gif) ](https://cmrxrtos.org/)

[Eduard Drusa](https://cmrxrtos.org/) said... 
    

> The 8086 uses an interesting architecture for microcode: each micro-instruction performs two unrelated operations.  
  
Is this a slight hint of VLIW? Where "very long" stands for "just two". Intel was very intimate with VLIW both before and after 8086. Or is this just a common way of designing microcoded CPU cores? 

     [ January 24, 2026 at 3:10 AM ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html?showComment=1769253004836#c3334855146608660349 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/3334855146608660349 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

Can anyone point me in the direction of similar work on the first ARM architecture, over here in the UK that was a very important design. Its a story that is little known in the US despite ARMs now massively out numbering everything else, 300 Billion produced. 

     [ January 24, 2026 at 4:51 AM ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html?showComment=1769259072679#c9063186280672952442 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/9063186280672952442 "Delete Comment")

[![](//resources.blogblog.com/img/blank.gif) ](http://simon.mooli.org.uk)

[Simon N Goodwin](http://simon.mooli.org.uk) said... 
    

Fascinating as usual, but with deference I reckon you meant to type ALU not CPU here: "the Z80's 4-bit CPU" \- most of us owe you the fascinating insight that Z80s chomp nybbles internally, of course. But it's surely too late to reclassify the CPU itself, and if so where does that leave the 8080? 😄 

     [ January 24, 2026 at 11:51 AM ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html?showComment=1769284273791#c8582019956613248973 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/8582019956613248973 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

ken said... 
    

Where you say "the Z80's 4-bit CPU", do you mean ALU? 

     [ January 24, 2026 at 3:12 PM ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html?showComment=1769296350127#c6123997160327012146 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/6123997160327012146 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

To Ken Shirriff  
Have you ever seen these before? I haven't.  
https://m.facebook.com/groups/1082975419579024/permalink/1745167016693191/?ref=share&mibextid=NOb6eG 

     [ February 1, 2026 at 5:19 PM ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html?showComment=1769995179780#c1809749202069771089 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/1809749202069771089 "Delete Comment")

[Post a Comment](https://www.blogger.com/comment/fullpage/post/6264947694886887540/7538688365288775324)

[Older Post](http://www.righto.com/2025/12/8087-microcode-conditions.html "Older Post") [Home](http://www.righto.com/)

[Subscribe](https://righto.kit.com/20bf534dff
)

[Contact info and site index](https://www.righto.com/p/index.html)

## Popular Posts

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_uLY5KNf3x9Myo0lDjP4mzQbEN6MfDSwjYs2E3KJfLFxcKPLSVOpEqRCmkwbAD3tUJVC9KQfPjmwL8Gi5UkdWc0kPlz7s7W2bRPc4iRgGiyjnI=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html)

[A Multi-Protocol Infrared Remote Library for the Arduino](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_siZ65p5v8Uc_RO66tYcenq44H0h8KTPpAZKtP6lx6gv0Iq55c8N9xjZvvHcNc8KlaLDEynlytWaXkYF-zg0BaGV_OvykqfL7fwBKB4rz_yDOvOAw3N3el88Vupwwpr8geDGLCU_XEnyA=w72-h72-p-k-no-nu) ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)

[Notes on the Intel 8086 processor's arithmetic-logic unit](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_ulO4vNZlQvy1pUA6qvR-X-QjS610PAKJz74L-kTjgO0JMybd7yyh5hUWdRdKHxLbUuxtx4H_h1dIagVLHRMMHtavvDU--F8SMJKgjuBZflXMZpG4vXfrrbrrVG0M8=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html)

[A dozen USB chargers in the lab: Apple is very good, but not quite the best](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_vSqTXpdlGCfgOKxtJlPZOsntb7rO6ao0lI6C0Ml4NnaPqFBgmfsZ1HcjmN_QHsPd2yFSW8sBRADjK3yaTjzYe1fG64n0rqEiMkKKd5j-nHasmOo0B-GoB9_6JcKeAoWoCKv58hVyHaksFYXVLwso7WWwI=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html)

[Apple iPhone charger teardown: quality in a tiny expensive package](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_s1e6gehDXY4fmCii6BXr7h5R-djrHvFfI08yz1UzGMqdBH3ZaoUe-M7fBUBQeJA9DIpRliUYrlOTon_FJjFu7iU3jFRS7WUSCl3ziV_kVMrWbWJIucVKMY_cXG1sWwjKBcypiWKxWIiW6wPD8x=w72-h72-p-k-no-nu) ](http://www.righto.com/2025/12/8087-microcode-conditions.html)

[Conditions in the Intel 8087 floating-point chip's microcode](http://www.righto.com/2025/12/8087-microcode-conditions.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_u8t8yA32E8s7cuozZSV8QOBO2Pk-pp_glLUSeOj4JhL4XJO-dd1JkMuzQxwPZuThcsAlqU-e0gWoGUwZKF_xHK9khWDwtd-skLwCHQtu1u0CdXmQrBVrtohtVbEHElhq3ha3-fBoY5OSaNDvg=w72-h72-p-k-no-nu) ](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html)

[Teardown and exploration of Apple's Magsafe connector](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_tSH9n147iSI4YiHezhJ2tDIalLgp-Wlvs6Ip9MAVypi5l6cAD5QZOCk_aVeSxHEMNLJYGDcoaTLAYw5RbmKhybFUuCw5_zr1rc1FiHX6oQObl9rIzVNgNm--uDHi2iuAFG=w72-h72-p-k-no-nu) ](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html)

[Mining Bitcoin with pencil and paper: 0.67 hashes per day](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_vYyCjz5MB-mu5_AE3ROtY4dhcuIJ_Enw4_PwrBWUXUNxt7bHRNZchVCakFuW5WHuHJTrxpOU6uffHD_GMlFo_ZVP1hLAuAC3A-HVi59i6m=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html)

[An Arduino universal remote: record and playback IR signals](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html)




## Search This Blog

|   
---|---  
  
## Labels

[386](http://www.righto.com/search/label/386) [6502](http://www.righto.com/search/label/6502) [8008](http://www.righto.com/search/label/8008) [8085](http://www.righto.com/search/label/8085) [8086](http://www.righto.com/search/label/8086) [8087](http://www.righto.com/search/label/8087) [8088](http://www.righto.com/search/label/8088) [aerospace](http://www.righto.com/search/label/aerospace) [alto](http://www.righto.com/search/label/alto) [analog](http://www.righto.com/search/label/analog) [Apollo](http://www.righto.com/search/label/Apollo) [apple](http://www.righto.com/search/label/apple) [arc](http://www.righto.com/search/label/arc) [arduino](http://www.righto.com/search/label/arduino) [arm](http://www.righto.com/search/label/arm) [beaglebone](http://www.righto.com/search/label/beaglebone) [bitcoin](http://www.righto.com/search/label/bitcoin) [c#](http://www.righto.com/search/label/c%23) [cadc](http://www.righto.com/search/label/cadc) [calculator](http://www.righto.com/search/label/calculator) [chips](http://www.righto.com/search/label/chips) [css](http://www.righto.com/search/label/css) [datapoint](http://www.righto.com/search/label/datapoint) [dx7](http://www.righto.com/search/label/dx7) [electronics](http://www.righto.com/search/label/electronics) [f#](http://www.righto.com/search/label/f%23) [fairchild](http://www.righto.com/search/label/fairchild) [fpga](http://www.righto.com/search/label/fpga) [fractals](http://www.righto.com/search/label/fractals) [genome](http://www.righto.com/search/label/genome) [globus](http://www.righto.com/search/label/globus) [haskell](http://www.righto.com/search/label/haskell) [HP](http://www.righto.com/search/label/HP) [html5](http://www.righto.com/search/label/html5) [ibm](http://www.righto.com/search/label/ibm) [ibm1401](http://www.righto.com/search/label/ibm1401) [ibm360](http://www.righto.com/search/label/ibm360) [intel](http://www.righto.com/search/label/intel) [ipv6](http://www.righto.com/search/label/ipv6) [ir](http://www.righto.com/search/label/ir) [java](http://www.righto.com/search/label/java) [javascript](http://www.righto.com/search/label/javascript) [math](http://www.righto.com/search/label/math) [microcode](http://www.righto.com/search/label/microcode) [oscilloscope](http://www.righto.com/search/label/oscilloscope) [Pentium](http://www.righto.com/search/label/Pentium) [photo](http://www.righto.com/search/label/photo) [power supply](http://www.righto.com/search/label/power%20supply) [random](http://www.righto.com/search/label/random) [reverse-engineering](http://www.righto.com/search/label/reverse-engineering) [sheevaplug](http://www.righto.com/search/label/sheevaplug) [snark](http://www.righto.com/search/label/snark) [space](http://www.righto.com/search/label/space) [spanish](http://www.righto.com/search/label/spanish) [synth](http://www.righto.com/search/label/synth) [teardown](http://www.righto.com/search/label/teardown) [theory](http://www.righto.com/search/label/theory) [unicode](http://www.righto.com/search/label/unicode) [Z-80](http://www.righto.com/search/label/Z-80)

## Blog Archive

  * [ ▼ ](javascript:void\(0\)) [ 2026 ](http://www.righto.com/2026/) (1)
    * [ ▼ ](javascript:void\(0\)) [ January ](http://www.righto.com/2026/01/) (1)
      * [Notes on the Intel 8086 processor's arithmetic-log...](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)


  * [ ► ](javascript:void\(0\)) [ 2025 ](http://www.righto.com/2025/) (22)
    * [ ► ](javascript:void\(0\)) [ December ](http://www.righto.com/2025/12/) (2)
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
