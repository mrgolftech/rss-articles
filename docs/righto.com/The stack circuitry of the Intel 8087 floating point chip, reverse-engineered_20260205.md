# The stack circuitry of the Intel 8087 floating point chip, reverse-engineered

**来源:** https://righto.com
**链接:** http://www.righto.com/2025/12/8087-stack-circuitry.html
**日期:** 2025-12-09T09:54:00.000-08:00

---

#  [ Ken Shirriff's blog ](http://www.righto.com/)

Computer history, restoring vintage computers, IC reverse engineering, and whatever

###  The stack circuitry of the Intel 8087 floating point chip, reverse-engineered 

Early microprocessors were very slow when operating with floating-point numbers. But in 1980, Intel introduced the 8087 floating-point coprocessor, performing floating-point operations up to 100 times faster. This was a huge benefit for IBM PC applications such as AutoCAD, spreadsheets, and flight simulators. The 8087 was so effective that today's computers still use a floating-point system based on the 8087.1

The 8087 was an extremely complex chip for its time, containing somewhere between 40,000 and 75,000 transistors, depending on the source.2 To explore how the 8087 works, I opened up a chip and took numerous photos of the silicon die with a microscope. Around the edges of the die, you can see the hair-thin bond wires that connect the chip to its 40 external pins. The complex patterns on the die are formed by its metal wiring, as well as the polysilicon and silicon underneath. The bottom half of the chip is the "datapath", the circuitry that performs calculations on 80-bit floating point values. At the left of the datapath, a [constant ROM](https://www.righto.com/2020/05/extracting-rom-constants-from-8087-math.html) holds important constants such as π. At the right are the eight registers that form the stack, along with the stack control circuitry.

[![Die of the Intel 8087 floating point unit chip, with main functional blocks labeled. The die is 5mm×6mm.  Click for a larger image.](https://static.righto.com/images/8087-stack/8087-die-labeled-w450.jpg)](https://static.righto.com/images/8087-stack/8087-die-labeled.jpg)

Die of the Intel 8087 floating point unit chip, with main functional blocks labeled. The die is 5mm×6mm. Click for a larger image.

The chip's instructions are defined by the large [microcode ROM](https://www.righto.com/2018/09/two-bits-per-transistor-high-density.html) in the middle. This ROM is very unusual; it is semi-analog, storing two bits per transistor by using four transistor sizes. To execute a floating-point instruction, the 8087 decodes the instruction and the microcode engine starts executing the appropriate micro-instructions from the microcode ROM. The decode circuitry to the right of the ROM generates the appropriate control signals from each micro-instruction. The bus registers and control circuitry handle interactions with the main 8086 processor and the rest of the system. Finally, the [bias generator](https://www.righto.com/2018/08/inside-die-of-intels-8087-coprocessor.html) uses a charge pump to create a negative voltage to bias the chip's substrate, the underlying silicon.

The stack registers and control circuitry (in red above) are the subject of this blog post. Unlike most processors, the 8087 organizes its registers in a stack, with instructions operating on the top of the stack. For instance, the square root instruction replaces the value on the top of the stack with its square root. You can also access a register relative to the top of the stack, for instance, adding the top value to the value two positions down from the top. The stack-based architecture was intended to improve the instruction set, simplify compiler design, and make function calls more efficient, although it didn't work as well as hoped.

[![The stack on the 8087. From The 8087 Primer, page 60.](https://static.righto.com/images/8087-stack/stack-diagram-w350.jpg)](https://static.righto.com/images/8087-stack/stack-diagram.jpg)

The stack on the 8087. From _The 8087 Primer_ , page 60.

The diagram above shows how the stack operates. The stack consists of eight registers, with the Stack Top (ST) indicating the current top of the stack. To push a floating-point value onto the stack, the Stack Top is decremented and then the value is stored in the new top register. A pop is performed by copying the value from the stack top and then incrementing the Stack Top. In comparison, most processors specify registers directly, so register 2 is always the same register.

## The registers

The stack registers occupy a substantial area on the die of the 8087 because floating-point numbers take many bits. A floating-point number consists of a fractional part (sometimes called the mantissa or significand), along with the exponent part; the exponent allows floating-point numbers to cover a range from extremely small to extremely large. In the 8087, floating-point numbers are 80 bits: 64 bits of significand, 15 bits of exponent, and a sign bit. An 80-bit register was very large in the era of 8-bit or 16-bit computers; the eight registers in the 8087 would be equivalent to 40 registers in the 8086 processor.

[![The registers in the 8087 form an 8×80 grid of cells. The close-up shows an 8×8 block. I removed the metal layer with acid to reveal the underlying silicon circuitry.](https://static.righto.com/images/8087-stack/registers-w500.jpg)](https://static.righto.com/images/8087-stack/registers.jpg)

The registers in the 8087 form an 8×80 grid of cells. The close-up shows an 8×8 block. I removed the metal layer with acid to reveal the underlying silicon circuitry.

The registers store each bit in a static RAM cell. Each cell has two inverters connected in a loop. This circuit forms a stable feedback loop, with one inverter on and one inverter off. Depending on which inverter is on, the circuit stores a 0 or a 1. To write a new value into the circuit, one of the lines is pulled low, flipping the loop into the desired state. The trick is that each inverter uses a very weak transistor to pull the output high, so its output is easily overpowered to change the state.

[![Two inverters in a loop can store a 0 or a 1.](https://static.righto.com/images/8087-stack/inverter-loop-w250.png)](https://static.righto.com/images/8087-stack/inverter-loop.png)

Two inverters in a loop can store a 0 or a 1.

These inverter pairs are arranged in an 8 × 80 grid that implements eight words of 80 bits. Each of the 80 rows has two _bitlines_ that provide access to a bit. The bitlines provide both read and write access to a bit; the pair of bitlines allows either inverter to be pulled low to store the desired bit value. Eight vertical _wordlines_ enable access to one word, one column of 80 bits. Each wordline turns on 160 pass transistors, connecting the bitlines to the inverters in the selected column. Thus, when a wordline is enabled, the bitlines can be used to read or write that word.

Although the chip looks two-dimensional, it actually consists of multiple layers. The bottom layer is silicon. The pinkish regions below are where the silicon has been "doped" to change its electrical properties, making it an active part of the circuit. The doped silicon forms a grid of horizontal and vertical wiring, with larger doped regions in the middle. On top of the silicon, polysilicon wiring provides two functions. First, it provides a layer of wiring to connect the circuit. But more importantly, when polysilicon crosses doped silicon, it forms a transistor. The polysilicon provides the gate, turning the transistor on and off. In this photo, the polysilicon is barely visible, so I've highlighted part of it in red. Finally, horizontal metal wires provide a third layer of interconnecting wiring. Normally, the metal hides the underlying circuitry, so I removed the metal with acid for this photo. I've drawn blue lines to represent the metal layer. Contacts provide connections between the various layers.

[![A close-up of a storage cell in the registers. The metal layer and most of the polysilicon have been removed to show the underlying silicon.](https://static.righto.com/images/8087-stack/memory-cell-layers-w500.jpg)](https://static.righto.com/images/8087-stack/memory-cell-layers.jpg)

A close-up of a storage cell in the registers. The metal layer and most of the polysilicon have been removed to show the underlying silicon.

The layers combine to form the inverters and selection transistors of a memory cell, indicated with the dotted line below. There are six transistors (yellow), where polysilicon crosses doped silicon. Each inverter has a transistor that pulls the output low and a weak transistor to pull the output high. When the word line (vertical polysilicon) is active, it connects the selected inverters to the bit lines (horizontal metal) through the two selection transistors. This allows the bit to be read or written.

[![The function of the circuitry in a storage cell.](https://static.righto.com/images/8087-stack/memory-cell-labeled-w500.jpg)](https://static.righto.com/images/8087-stack/memory-cell-labeled.jpg)

The function of the circuitry in a storage cell.

Each register has two tag bits associated with it, an unusual form of metadata to indicate if the register is empty, contains zero, contains a valid value, or contains a special value such as infinity. The tag bits are used to optimize performance internally and are mostly irrelevant to the programmer. As well as being accessed with a register, the tag bits can be accessed in parallel as a 16-bit "Tag Word". This allows the tags to be saved or loaded as part of the 8087's state, for instance, during interrupt handling.

## The decoder

The decoder circuit, wedged into the middle of the register file, selects one of the registers. A register is specified internally with a 3-bit value. The decoder circuit energizes one of the eight register select lines based on this value.

The decoder circuitry is straightforward: it has eight 3-input NOR gates to match one of the eight bit patterns. The select line is then powered through a high-current driver that uses large transistors. (In the photo below, you can compare the large serpentine driver transistors to the small transistors in a bit cell.)

[![The decoder circuitry has eight similar blocks to drive the eight select lines.](https://static.righto.com/images/8087-stack/decoder-w600.jpg)](https://static.righto.com/images/8087-stack/decoder.jpg)

The decoder circuitry has eight similar blocks to drive the eight select lines.

The decoder has an interesting electrical optimization. As shown earlier, the register select lines are eight polysilicon lines running vertically, the length of the register file. Unfortunately, polysilicon has fairly high resistance, better than silicon but much worse than metal. The problem is that the resistance of a long polysilicon line will slow down the system. That is, the capacitance of transistor gates in combination with high resistance causes an RC (resistive-capacitive) delay in the signal.

The solution is that the register select lines also run in the metal layer, a second set of lines immediately to the right of the register file. These lines branch off from the register file about 1/3 of the way down, run to the bottom, and then connect back to the polysilicon select lines at the bottom. This reduces the maximum resistance through a select line, increasing the speed.

[![A diagram showing how 8 metal lines run parallel to the main select lines. The register file is much taller than shown; the middle has been removed to make the diagram fit.](https://static.righto.com/images/8087-stack/select-w300.jpg)](https://static.righto.com/images/8087-stack/select.jpg)

A diagram showing how 8 metal lines run parallel to the main select lines. The register file is much taller than shown; the middle has been removed to make the diagram fit.

## The stack control circuitry

A stack needs more control circuitry than a regular register file, since the circuitry must keep track of the position of the top of the stack.3 The control circuitry increments and decrements the top of stack (TOS) pointer as values are pushed or popped (purple).4 Moreover, an 8087 instruction can access a register based on its offset, for instance the third register from the top. To support this, the control circuitry can temporarily add an offset to the top of stack position (green). A multiplexer (red) selects either the top of stack or the adder output, and feeds it to the decoder (blue), which selects one of the eight stack registers in the register file (yellow), as described earlier.

[![The register stack in the 8087. Adapted from Patent USRE33629E. I don't know what the GRX field is. I also don't know why this shows a subtractor and not an adder.](https://static.righto.com/images/8087-stack/patent-diagram-w700.jpg)](https://static.righto.com/images/8087-stack/patent-diagram.jpg)

The register stack in the 8087. Adapted from [Patent USRE33629E](https://patents.google.com/patent/USRE33629E). I don't know what the GRX field is. I also don't know why this shows a subtractor and not an adder.

The physical implementation of the stack circuitry is shown below. The logic at the top selects the stack operation based on the 16-bit micro-instruction.5 Below that are the three latches that hold the top of stack value. (The large white squares look important, but they are simply "jumpers" from the ground line to the circuitry, passing under metal wires.)

[![The stack control circuitry. The blue regions on the right are oxide residue that remained when I dissolved the metal rail for the 5V power.
](https://static.righto.com/images/8087-stack/stack-circuitry-w350.jpg)](https://static.righto.com/images/8087-stack/stack-circuitry.jpg)

The stack control circuitry. The blue regions on the right are oxide residue that remained when I dissolved the metal rail for the 5V power. 

The three-bit adder is at the bottom, along with the multiplexer. You might expect the adder to use a simple "full adder" circuit. Instead, it is a faster [carry-lookahead](https://en.wikipedia.org/wiki/Carry-lookahead_adder) adder. I won't go into details here, but the summary is that at each bit position, an AND gate produces a Carry Generate signal while an XOR gate produces a Carry Propagate signal. Logic gates combine these signals to produce the output bits in parallel, avoiding the slowdown of the carry rippling through the bits.

The incrementer/decrementer uses a completely different approach. Each of the three bits uses a toggle flip-flop. A few logic gates determine if each bit should be toggled or should keep its previous value. For instance, when incrementing, the top bit is toggled if the lower bits are 11 (e.g. incrementing from 011 to 100). For decrementing, the top bit is toggled if the lower bits are 00 (e.g. 100 to 011). Simpler logic determines if the middle bit should be toggled. The bottom bit is easier, toggling every time whether incrementing or decrementing.

The schematic below shows the circuitry for one bit of the stack. Each bit is implemented with a moderately complicated flip-flop that can be cleared, loaded with a value, or toggled, based on control signals from the microcode. The flip-flop is constructed from two set-reset (SR) latches. Note that the flip-flop outputs are crossed when fed back to the input, providing the inversion for the toggle action. At the right, the multiplexer selects either the register value or the sum from the adder (not shown), generating the signals to the decoder.

[![Schematic of one bit of the stack.](https://static.righto.com/images/8087-stack/stack-schematic-w700.jpg)](https://static.righto.com/images/8087-stack/stack-schematic.jpg)

Schematic of one bit of the stack.

## Drawbacks of the stack approach

According to the designers of the 8087,7 the main motivation for using a stack rather than a flat register set was that instructions didn't have enough bits to address multiple register operands. In addition, a stack has "advantages over general registers for expression parsing and nested function calls." That is, a stack works well for a mathematical expression since sub-expressions can be evaluated on the top of the stack. And for function calls, you avoid the cost of saving registers to memory, since the subroutine can use the stack without disturbing the values underneath. At least that was the idea.

The main problem is "stack overflow". The 8087's stack has eight entries, so if you push a ninth value onto the stack, the stack will overflow. Specifically, the top-of-stack pointer will wrap around, obliterating the bottom value on the stack. The 8087 is designed to detect a stack overflow using the register tags: pushing a value to a non-empty register triggers an invalid operation exception.6

The designers expected that stack overflow would be rare and could be handled by the operating system (or library code). After detecting a stack overflow, the software should dump the existing stack to memory to provide the illusion of an infinite stack. Unfortunately, bad design decisions made it difficult "both technically and commercially" to handle stack overflow.

One of the 8087's designers (Kahan) attributes the 8087's stack problems to the time difference between California, where the designers lived, and Israel, where the 8087 was implemented. Due to a lack of communication, each team thought the other was implementing the overflow software. It wasn't until the 8087 was in production that they realized that "it might not be possible to handle 8087 stack underflow/overflow in a reasonable way. It's not impossible, just impossible to do it in a reasonable way."

As a result, the stack was largely a problem rather than a solution. Most 8087 software saved the full stack to memory before performing a function call, creating more memory traffic. Moreover, compilers turned out to work better with regular registers than a stack, so compiler writers awkwardly used the stack to emulate regular registers. The `GCC` compiler [reportedly](https://langdev.stackexchange.com/a/2408) needs 3000 lines of extra code to support the x87 stack.

In the 1990s, Intel introduced a new floating-point system called [SSE](https://www.cs.uaf.edu/2012/fall/cs301/lecture/11_02_other_float.html), followed by AVX in 2011. These systems use regular (non-stack) registers and provide parallel operations for higher performance, making the 8087's stack instructions largely obsolete.

## The success of the 8087

At the start, Intel was unenthusiastic about producing the 8087, viewing it as unlikely to be a success. John Palmar, a principal architect of the chip, had little success convincing skeptical Intel management that the market for the 8087 was enormous. Eventually, he said, "I'll tell you what. I'll relinquish my salary, provided you'll write down your number of how many you expect to sell, then give me a dollar for every one you sell beyond that."7 Intel didn't agree to the deal--which would have made a fortune for Palmer--but they reluctantly agreed to produce the chip.

Intel's Santa Clara engineers shunned the 8087, considering it unlikely to work: the 8087 would be two to three times more complex than the 8086, with a die so large that a wafer might not have a single working die. Instead, Rafi Nave, at Intel's Israel site, took on the risky project: "Listen, everybody knows it's not going to work, so if it won't work, I would just fulfill their expectations or their assessment. If, by chance, it works, okay, then we'll gain tremendous respect and tremendous breakthrough on our abilities."

A small team of seven engineers developed the 8087 in Israel. They designed the chip on Mylar sheets: a millimeter on Mylar represented a micron on the physical chip. The drawings were then digitized on a Calma system by clicking on each polygon to create the layout. When the chip was moved into production, the yield was very low but better than feared: two working dies per four-inch wafer.

The 8087 ended up being a large success, said to have been Intel's most profitable product line at times. The success of the 8087 (along with the 8088) cemented the reputation of Intel Israel, which eventually became Israel's largest tech employer. The benefits of floating-point hardware proved to be so great that Intel integrated the floating-point unit into later processors starting with the 80486 (1989). Nowadays, most modern computers, from cellphones to mainframes, provide floating point based on the 8087, so I consider the 8087 one of the most influential chips ever created.

For more, follow me on Bluesky ([@righto.com](https://bsky.app/profile/righto.com)), Mastodon ([@[email protected]](https://oldbytes.space/@kenshirriff)), or [RSS](http://www.righto.com/feeds/posts/default). I wrote some articles about the 8087 a few years ago, including [the die](https://www.righto.com/2018/08/inside-die-of-intels-8087-coprocessor.html), [the ROM](https://www.righto.com/2018/09/two-bits-per-transistor-high-density.html), the [bit shifter](https://www.righto.com/2020/05/die-analysis-of-8087-math-coprocessors.html), and [the constants](https://www.righto.com/2020/05/extracting-rom-constants-from-8087-math.html), so you may have seen some of this material before.

## Notes and references

  1. Most computers now use the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) floating-point standard, which is based on the 8087. This standard has been awarded a [milestone](https://ethw.org/Milestones:IEEE_Standard_754_for_Binary_Floating-Point_Arithmetic,_1985) in computation. ↩

  2. Curiously, reliable sources differ on the number of transistors in the 8087 by almost a factor of 2. Intel says [40,000](https://www.intel.com/content/dam/www/public/us/en/documents/case-studies/floating-point-case-study.pdf?page=5), as does designer William Kahan ([link](https://web.archive.org/web/20190301193516/http://www.drdobbs.com/architecture-and-design/a-conversation-with-william-kahan/184410314)). But in [A Numeric Data Processor](https://doi.org/10.1109/ISSCC.1980.1156144), designers Rafi Nave and John Palmer wrote that the chip contains "the equivalent of over 65,000 devices" (whatever "equivalent" means). This number is echoed by a contemporary [article](https://www.worldradiohistory.com/Archive-Electronics/80s/80/Electronics-1980-02-14.pdf) in _Electronics_ (1980) that says "over 65,000 H-MOS transistors on a 78,000-mil2 die." Many other sources, such as [Upgrading & Repairing PCs](https://vtda.org/books/Computing/Hardware/Upgrading%20and%20Repairing%20PCs/URP_4th_edition.pdf?page=238), specify 45,000 transistors. Designer Rafi Nave [stated](https://www.computerhistory.org/collections/catalog/300000148/) that the 8087 has 63,000 or 64,000 transistors if you count the ROM transistors directly, but if you count ROM transistors as equivalent to two transistors, then you get about 75,000 transistors. ↩

  3. The 8087 has a 16-bit Status Word that contains the stack top pointer, exception flags, the four-bit condition code, and other values. Although the Status Word appears to be a 16-bit register, it is not implemented as a register. Instead, parts of the Status Word are stored in various places around the chip: the stack top pointer is in the stack circuitry, the exception flags are part of the interrupt circuitry, the condition code bits are next to the datapath, and so on. When the Status Word is read or written, these various circuits are connected to the 8087's internal data bus, making the Status Word appear to be a monolithic entity. Thus, the stack circuitry includes support for reading and writing it. ↩

  4. Intel filed several patents on the 8087, including [Numeric data processor](https://patents.google.com/patent/USRE33629E), another [Numeric data processor](https://patents.google.com/patent/US4338675A), [Programmable bidirectional shifter](https://patents.google.com/patent/US4509144A), [Fraction bus for use in a numeric data processor](https://patents.google.com/patent/US4484259A), and [System bus arbitration, circuitry and methodology](https://patents.google.com/patent/US4257095A). ↩

  5. I started looking at the stack in detail to reverse engineer the micro-instruction format and determine how the 8087's microcode works. I'm working with the "Opcode Collective" on Discord on this project, but progress is slow due to the complexity of the micro-instructions. ↩

  6. The 8087 detects stack underflow in a similar manner. If you pop more values from the stack than are present, the tag will indicate that the register is empty and shouldn't be accessed. This triggers an invalid operation exception. ↩

  7. The 8087 is described in detail in [The 8086 Family User's Manual, Numerics Supplement](https://ethw.org/w/images/2/2f/Intel_8086_family_users_numeric_supp.pdf). An overview of the stack is on page 60 of _The 8087 Primer_ by Palmer and Morse. More details are in Kahan's [On the Advantages of the 8087's Stack](https://web.archive.org/web/20170118054747/https://cims.nyu.edu/~dbindel/class/cs279/87stack.pdf), an unpublished course note (maybe for [CS 279](https://www.researchgate.net/profile/David-Bindel/publication/2585992_CS_279_Annotated_Course_Bibliography/links/545794630cf26d5090ab49a6/CS-279-Annotated-Course-Bibliography.pdf)?) with a date of Nov 2, 1990 or perhaps [August 23, 1994](https://www.netlib.org/bibnet/authors/k/kahan-william-m.pdf#page=21). Kahan discusses why the 8087's design makes it hard to handle stack overflow in [How important is numerical accuracy](https://web.archive.org/web/20190301193516/http://www.drdobbs.com/architecture-and-design/a-conversation-with-william-kahan/184410314), Dr. Dobbs, Nov. 1997. Another information source is the [Oral History of Rafi Nave](https://www.youtube.com/watch?v=JRSUmuWiTOs) ↩↩




[ ![](http://img1.blogblog.com/img/icon18_email.gif) ](https://www.blogger.com/email-post/6264947694886887540/1883798277085402615 "Email Post") [ ![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=6264947694886887540&postID=1883798277085402615&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=1883798277085402615&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=1883798277085402615&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=1883798277085402615&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=1883798277085402615&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=6264947694886887540&postID=1883798277085402615&target=pinterest "Share to Pinterest")

Labels: [8087](http://www.righto.com/search/label/8087), [electronics](http://www.righto.com/search/label/electronics), [intel](http://www.righto.com/search/label/intel), [reverse-engineering](http://www.righto.com/search/label/reverse-engineering)

#### 5 comments:

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

I worked on the Intel iAPX 432 project for nearly four years as a lead technical writer, on the subsequent Gemini/BiiN project that developed the i960 from its inception as manager of technical publications/writer/writing team manager, and later wrote the Intel 960 Extended Architecture Programmer's Reference Manual on contract to Intel. The 8087 was an important foundation, as IEEE floating-point was supported in both the 432 chips and in most of the i960 chips. (The i960 core architecture did not support floating-point in hardware; the numerics, protected, and extended architectures did.) I always appreciate your posts. Sincerely, Martin L Buchanan/[[email protected]](/cdn-cgi/l/email-protection). 

     [ December 9, 2025 at 11:14 AM ](http://www.righto.com/2025/12/8087-stack-circuitry.html?showComment=1765307659857#c1600436775218743440 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/1600436775218743440 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

I've had the opportunity to work closely with Intel's processor architecture over the years. I spent nearly four years on the Intel iAPX 432 project as a lead technical writer, then continued on the Gemini/BiiN project--where the i960 originated--as the manager of technical publications, writer, and writing team lead. I later authored the Intel 960 Extended Architecture Programmer's Reference Manual as a contractor.  
  
The 8087 also played a key role, since IEEE floating-point was supported in both the 432 family and most versions of the i960 (with floating-point implemented in the numerics, protected, and extended architectures).  
  
Really appreciate your posts--always insightful. 

     [ December 10, 2025 at 5:10 AM ](http://www.righto.com/2025/12/8087-stack-circuitry.html?showComment=1765372226832#c8061497947649313501 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/8061497947649313501 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

I think one of the problems about the stack design is that it made it difficult to read fpu code and understand what it was doing, you really had to concentrate and think about each line. Today I wasted a day tracking down a bug in legacy x86 fpu code that I have to convert to x64 SSE and it turned out to be due to a partial calculation that was left on the stack and then re-used a couple of hundred instructions later! So I specially loved learning about the stack in your article. Thanks and keep up the good work 

     [ December 11, 2025 at 7:03 PM ](http://www.righto.com/2025/12/8087-stack-circuitry.html?showComment=1765508611494#c7678477152832986131 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/7678477152832986131 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

You say that: "I don't know what the GRX field is."  
  
Isn't it the "R" field ("reg") of the ModRM byte?  
  
In the data sheet https://datasheets.chipdb.org/Intel/x86/808x/datashts/8087/205835-007.pdf, on page 20, I see the opcode for FADD, for example. With MOD = 11, the R/M bits are the i of ST(i) if I read it correctly.   
  
This is also true for other commands like FLD, FST(P), FCOM(P), FSUB and FFREE.  
Adder or subtractor would not make any difference other than the way the stack is organized - or does it allow direct access to registers other than relative? 

     [ December 18, 2025 at 11:43 AM ](http://www.righto.com/2025/12/8087-stack-circuitry.html?showComment=1766087005271#c5509500415797154902 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/5509500415797154902 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said... 
    

My personal beef with the 8087 stack comes from when I was trying to write optimized floating point assembly code for the original Pentium processor. There were definitely some potential gains to be had by not ordering your computations in stack order, I think some things could run in parallel? To accommodate such optimisations, Intel noted helpfully that a floating point instruction in the U pipe would pair with an FXCH instruction in the V pipe, and issue in the same cycle. So I tried to write code that used that "free" stack exchange instruction every cycle to effectively have floating point instructions that could choose both their register inputs. But I think I gave up pretty quickly, because it was utterly confusing... 

     [ December 25, 2025 at 10:47 AM ](http://www.righto.com/2025/12/8087-stack-circuitry.html?showComment=1766688450355#c1075117884670181036 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/6264947694886887540/1075117884670181036 "Delete Comment")

[Post a Comment](https://www.blogger.com/comment/fullpage/post/6264947694886887540/1883798277085402615)

[Newer Post](http://www.righto.com/2025/12/8087-microcode-conditions.html "Newer Post") [Older Post](http://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html "Older Post") [Home](http://www.righto.com/)

[Subscribe](https://righto.kit.com/20bf534dff
)

[Contact info and site index](https://www.righto.com/p/index.html)

## Popular Posts

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_t5PKnrEF1fLjjQMJ1zf8UxFcfPawLITDCr0WNUtFW6MIIxrS6IudrPt1-W7zVHnA97AzVE41-UiFToXaEconRtOoduXW2eW9B_4T1sILyCoow=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html)

[A Multi-Protocol Infrared Remote Library for the Arduino](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_uo1KLY6cKndrrJWcDDoa8dUlh97njRoAGoW0SVgwep70n5OXUeDIaSS1Qzh-Qh6pQhQ0p_otQB65DdtrcUVegfBkJIDgreT5mMxPHIo6yOeFyQCYRK_NRt5rU2ZNH2NMxbWTERYGc1-Q=w72-h72-p-k-no-nu) ](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)

[Notes on the Intel 8086 processor's arithmetic-logic unit](http://www.righto.com/2026/01/notes-on-intel-8086-processors.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_swxZd70ysen4R8ivBelCJa1S8moZ5n7WMk_qBGA4jR1pupa6VI56DieiiUZGpPY4vTItTIhdMeSTt02mygnDrDfVR4QTqjqOj-t-ThDwbV8eL2hNbqPsGCEUWLGgY=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html)

[A dozen USB chargers in the lab: Apple is very good, but not quite the best](http://www.righto.com/2012/10/a-dozen-usb-chargers-in-lab-apple-is.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sB0xWSaLLTAiCdpvmN7Z9HQDS7BusrQOVxWxE37kvzblCiG5IXfRJBj0EAjjwBwpk59HCY62x7mpxzSocjG67K0s30uTQlrYEdio05YGGw_2l04AOy6OH3DQd_k516DtlMBZTI7ifk-IUeSZBenxOz2sA=w72-h72-p-k-no-nu) ](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html)

[Apple iPhone charger teardown: quality in a tiny expensive package](http://www.righto.com/2012/05/apple-iphone-charger-teardown-quality.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_tLuRlv1pr3Y55WTXqO7O9Tnq-QNYV8Ko-fXIEdYB2qPZTLavUO7cg0KxVUs1Dj9hUcUN8aWa7QSYoU6rSHlJlwT-7IPQ2C7YBvpQh28u8-9t-P12mrRwKs3f-16k1DwZD7QRWBK2CS8BOkLjik=w72-h72-p-k-no-nu) ](http://www.righto.com/2025/12/8087-microcode-conditions.html)

[Conditions in the Intel 8087 floating-point chip's microcode](http://www.righto.com/2025/12/8087-microcode-conditions.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_s7w0iYcjt66-9B3Al0qouosfmjkXxf7nCfReUKuHNzeMQBK_KAQnQiBzuoiwxdRY6p4_4CaPoIq5kzIzGUBzpgWF0w0leatGGNausbFxR4E9yDJb1l7XzPPMbIwx_wb9amMDC1Zp30G_i9Z04=w72-h72-p-k-no-nu) ](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html)

[Teardown and exploration of Apple's Magsafe connector](http://www.righto.com/2013/06/teardown-and-exploration-of-magsafe.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sE7Ptz5al8KfBlCHim3ytsezk6nSOTMcZbvGBt6R9ZKDCjGKvCikjxVMNmxBH64gC38x4PNrPnVZYZFcdMHepMEkOTfs02h3YUb-mEA-rUEL7q1iLSH7WWWC9A7Jj0nqis=w72-h72-p-k-no-nu) ](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html)

[Mining Bitcoin with pencil and paper: 0.67 hashes per day](http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html)

  * [ ![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_v8XWCKRvmI7Jmjtj7XPniyJLaC55pZAQdwebJIZ4q2MTfWdPF_AmhhaVy8YjISGQL2ZmXhZIZzeETT7dlTJxyFRTs7G44zo1-6JG2HN10B=w72-h72-p-k-no-nu) ](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html)

[An Arduino universal remote: record and playback IR signals](http://www.righto.com/2009/09/arduino-universal-remote-record-and.html)




## Search This Blog

|   
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
