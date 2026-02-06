# The stack circuitry of the Intel 8087 floating point chip, reverse-engineered

**来源:** [righto.com](https://www.righto.com)
**发布时间:** 2025-12-09T09:54:00.000-08:00
**链接:** http://www.righto.com/2025/12/8087-stack-circuitry.html

---

{'type': 'text/html', 'language': None, 'base': 'https://www.righto.com/feeds/posts/default', 'value': '
Early microprocessors were very slow when operating with floating-point numbers.\nBut in 1980, Intel introduced the 8087 floating-point coprocessor, performing\nfloating-point operations up\nto 100 times faster.\nThis was a huge benefit for IBM PC\napplications such as AutoCAD, spreadsheets, and flight simulators.\nThe 8087 was so effective that today\'s computers still use a floating-point system based on the 8087.
1
\n
\n\n
The 8087 was an extremely complex chip for its time, containing somewhere between\n40,000 and 75,000 transistors, depending on the source.
2
\nTo explore how the 8087 works, I opened up a chip and took numerous photos of the silicon die with a microscope.\nAround the edges of the die, you can see the hair-thin bond wires that connect the chip to its 40 external pins.\nThe complex patterns on the die are formed by its metal wiring, as well as the polysilicon and silicon underneath.\nThe bottom half of the chip is the "datapath", the circuitry that performs calculations on 80-bit floating point values. \nAt the left of the datapath, a
constant ROM
holds important constants such as π.\nAt the right are the eight registers that form the stack, along with the stack control circuitry.
\n
Die of the Intel 8087 floating point unit chip, with main functional blocks labeled. The die is 5mm×6mm.  Click for a larger image.
\n
The chip\'s instructions are defined by the large
microcode ROM
in the middle.\nThis ROM is very unusual; it is semi-analog, storing two bits per transistor by using four transistor sizes.\nTo execute a floating-point instruction, the 8087 decodes the instruction and the microcode engine starts executing\nthe appropriate micro-instructions from the microcode ROM.\nThe decode circuitry to the right of the ROM generates the appropriate control signals from each micro-instruction.\nThe bus registers and control circuitry handle interactions with the main 8086 processor and the rest of the system.\nFinally, the
bias generator
\nuses a charge pump to create a negative voltage to bias the chip\'s substrate, the underlying silicon.
\n
The stack registers and control circuitry (in red above) are the subject of this blog post. \nUnlike most processors, the 8087 organizes its registers in a stack, with instructions operating on the top of the stack.\nFor instance, the square root instruction replaces the value on the top of the stack with its square root.\nYou can also access a register relative to the top of the stack, for instance, adding the top value to the value two positions down from the top.\nThe stack-based architecture was intended to improve the instruction set, simplify compiler design, and make function\ncalls more efficient, although it didn\'t work as well as hoped.
\n
The stack on the 8087. From
The 8087 Primer
, page 60.
\n
The diagram above shows how the stack operates. The stack consists of eight registers, with the Stack Top\n(ST) indicating the current top of the stack.\nTo push a floating-point value onto the stack, the Stack Top is decremented and then the value is stored in the new top register.\nA pop is performed by copying the value from the stack top and then incrementing the Stack Top.\nIn comparison, most processors specify registers directly, so register 2 is always the same register.
\n
The registers
\n
The stack registers occupy a substantial area on the die of the 8087 because floating-point numbers take many bits.\nA floating-point number consists of a fractional part (sometimes called the mantissa or significand), along with\nthe exponent part; the exponent allows floating-point numbers to cover a range from extremely small to extremely\nlarge.\nIn the 8087, floating-point numbers are 80 bits: 64 bits of significand, 15 bits of exponent, and a sign bit.\nAn 80-bit register was very large in the era of 8-bit or 16-bit computers; the eight registers in the 8087\nwould be equivalent to 40 registers in the 8086 processor.
\n
The registers in the 8087 form an 8×80 grid of cells. The close-up shows an 8×8 block. I removed the metal layer with acid to reveal the underlying silicon circuitry.
\n
The registers store each bit in a static RAM cell. Each cell has two inverters connected in a loop.\nThis circuit forms a stable feedback loop, with one inverter on and one inverter off.\nDepending on which inverter is on, the circuit stores a 0 or a 1.\nTo write a new value into the circuit, one of the lines is pulled low, flipping the loop into the desired state.\nThe trick is that each inverter uses a very weak transistor to pull the output high, so its output is easily overpowered\nto change the state.
\n
Two inverters in a loop can store a 0 or a 1.
\n
These inverter pairs are arranged in an 8 × 80 grid that implements eight words of 80 bits. Each of the 80 rows has two
bitlines
that provide access to a bit.\nThe bitlines provide both read and write access to a bit; the pair of bitlines allows either inverter to be pulled low to store the desired bit value.\nEight vertical
wordlines
enable access to one word, one column of 80 bits.\nEach wordline turns on 160 pass transistors, connecting the bitlines to the inverters in the selected column.\nThus, when a wordline is enabled, the bitlines can be used to read or write that word.
\n
Although the chip looks two-dimensional, it actually consists of multiple layers.\nThe bottom layer is silicon.\nThe pinkish regions below are where the silicon has been "doped" to change its electrical properties, making it an active\npart of the circuit.\nThe doped silicon forms a grid of horizontal and vertical wiring, with larger doped regions in the middle.\nOn top of the silicon, polysilicon wiring provides two functions. First, it provides a layer of wiring to connect the circuit.\nBut more importantly, when polysilicon crosses doped silicon, it forms a transistor. The polysilicon provides the gate, turning the transistor on and off.\nIn this photo, the polysilicon is barely visible, so I\'ve highlighted part of it in red.\nFinally, horizontal metal wires provide a third layer of interconnecting wiring.\nNormally, the metal hides the underlying circuitry, so I removed the metal with acid for this photo.\nI\'ve drawn blue lines to represent the metal layer.\nContacts provide connections between the various layers.
\n
A close-up of a storage cell in the registers. The metal layer and most of the polysilicon have been removed to show the underlying silicon.
\n
The layers combine to form the inverters and selection transistors of a memory cell, indicated with the dotted line below.\nThere are six transistors (yellow), where polysilicon crosses doped silicon. Each inverter has a transistor that\npulls the output low and a weak transistor to pull the output high.\nWhen the word line (vertical polysilicon) is active, it connects the selected inverters to the bit lines (horizontal metal) through the two selection\ntransistors.\nThis allows the bit to be read or written.
\n
The function of the circuitry in a storage cell.
\n
Each register has two tag bits associated with it, an unusual form of metadata to indicate\nif the register is empty, contains zero, contains a valid value, or\ncontains a special value such as infinity.\nThe tag bits are used to optimize performance internally and are mostly irrelevant to the programmer.\nAs well as being accessed with a register, the tag bits can be accessed in parallel as a 16-bit "Tag Word".\nThis allows the tags to be saved or loaded as part of the 8087\'s state, for instance,\nduring interrupt handling.
\n
The decoder
\n
The decoder circuit, wedged into the middle of the register file, selects one of the registers.\nA register is specified internally with a 3-bit value. The decoder circuit energizes one of the eight register select\nlines based on this value.
\n
The decoder circuitry is straightforward: it has eight 3-input NOR gates to match one of the eight bit patterns.\nThe select line is then powered through a high-current driver that uses large transistors.\n(In the photo below, you can compare the large serpentine driver transistors to the small transistors in a bit cell.)
\n
The decoder circuitry has eight similar blocks to drive the eight select lines.
\n
The decoder has an interesting electrical optimization.\nAs shown earlier, the register select lines are eight polysilicon lines running vertically, the length of the\nregister file. \nUnfortunately, polysilicon has fairly high resistance, better than silicon but much worse than metal.\nThe problem is that the resistance of a long polysilicon line will slow down the system.\nThat is, the capacitance of transistor gates in combination with high resistance causes an RC (resistive-capacitive) delay in the signal.
\n
The solution is that the register select lines also run in the metal layer, a second set of lines immediately to the\nright of the register file.\nThese lines branch off from the register file about 1/3 of the way down, run to the bottom, and then connect back\nto the polysilicon select lines at the bottom.\nThis reduces the maximum resistance through a select line, increasing the speed.
\n
A diagram showing how 8 metal lines run parallel to the main select lines. The register file is much taller than shown; the middle has been removed to make the diagram fit.
\n
The stack control circuitry
\n
A stack needs more control circuitry than a regular register file, since the circuitry must keep track of the\nposition of the top of the stack.
3
\nThe control circuitry increments and decrements the top of stack (TOS) pointer as values are pushed or popped\n(purple).
4
\nMoreover, an 8087 instruction can access a register based on its offset, for instance the third register\nfrom the top.\nTo support this, the control circuitry can temporarily add an offset to the top of stack position (green).\nA multiplexer (red) selects either the top of stack or the adder output, and feeds it to the decoder (blue),\nwhich selects one of the eight stack registers in the register file (yellow), as described earlier.
\n
The register stack in the 8087. Adapted from
Patent USRE33629E
. I don\'t know what the GRX field is. I also don\'t know why this shows a subtractor and not an adder.
\n
\n\n
The physical implementation of the stack circuitry is shown below.\nThe logic at the top selects the stack operation based on the 16-bit micro-instruction.
5
\nBelow that are the three latches that hold the top of stack value.\n(The large white squares look important, but they are simply "jumpers" from the ground line to the circuitry, passing\nunder metal wires.)
\n
The stack control circuitry. The blue regions on the right are oxide residue that remained when I dissolved the metal rail for the 5V power.\n
\n
The three-bit adder is at the bottom, along with the multiplexer.\nYou might expect the adder to use a simple "full adder" circuit. Instead, it is\na faster
carry-lookahead
adder.\nI won\'t go into details here, but the summary is that at each bit position, an AND gate produces a Carry Generate\nsignal while an XOR gate produces a Carry Propagate signal.\nLogic gates combine these signals to produce the output bits in parallel, avoiding the slowdown of the carry rippling\nthrough the bits.
\n
The incrementer/decrementer uses a completely different approach.\nEach of the three bits uses a toggle flip-flop.\nA few logic gates determine if each bit should be toggled or should keep its previous value.\nFor instance, when incrementing, the top bit is toggled if the lower bits are 11 (e.g. incrementing from 011 to 100).\nFor decrementing, the top bit is toggled if the lower bits are 00 (e.g. 100 to 011).\nSimpler logic determines if the middle bit should be toggled.\nThe bottom bit is easier, toggling every time whether incrementing or decrementing.
\n
The schematic below shows the circuitry for one bit of the stack.\nEach bit is implemented with a moderately complicated flip-flop that can be cleared, loaded with\na value, or toggled, based on control signals from the microcode.\nThe flip-flop is constructed from two set-reset (SR) latches. Note that the flip-flop outputs are crossed when fed back\nto the input, providing the inversion for the toggle action.\nAt the right, the multiplexer selects either the register value or the sum from the adder (not shown), generating the signals\nto the decoder.
\n
Schematic of one bit of the stack.
\n
Drawbacks of the stack approach
\n
According to the designers of the 8087,
7
\nthe main motivation for using a stack rather than a flat register set was that instructions didn\'t have enough bits to address multiple register operands.\nIn addition, a stack has "advantages over general registers for expression parsing and nested function calls."\nThat is, a stack works well for a mathematical expression since sub-expressions can be evaluated on the top\nof the stack.\nAnd for function calls, you avoid the cost of saving registers to memory, since the subroutine can use the stack without disturbing the values underneath.\nAt least that was the idea.
\n
\n\n
The main problem is "stack overflow".\nThe 8087\'s stack has eight entries, so if you push a ninth value onto the stack, the stack will overflow.\nSpecifically, the top-of-stack pointer will wrap around, obliterating the bottom value on the stack.\nThe 8087 is designed to detect a stack overflow using the register tags:\npushing a value to a non-empty register triggers an invalid operation exception.
6
\n
The designers expected that stack overflow would be rare and could be handled by the operating system (or library code).\nAfter detecting a stack overflow, the software should dump the existing stack to memory to\nprovide the illusion of an infinite stack.\nUnfortunately, bad design decisions made it difficult "both technically and commercially" to handle stack overflow.
\n
One of the 8087\'s designers (Kahan) attributes the 8087\'s stack problems to the time difference between California,\nwhere the designers lived, and Israel, where the 8087 was implemented.\nDue to a lack of communication, each team thought the other was implementing the overflow software.\nIt wasn\'t until the\n8087 was in production that they realized that "it might not be possible to handle 8087 stack underflow/overflow in a reasonable way. It\'s not impossible, just impossible to do it in a reasonable way."
\n
As a result, the stack was largely a problem rather than a solution.\nMost 8087 software saved the full stack to memory before performing\na function call, creating more memory traffic.\nMoreover, compilers turned out to work better with regular registers than a stack,\nso compiler writers awkwardly used the stack to emulate regular registers.\nThe
GCC
compiler
reportedly
needs 3000 lines of extra code to support the x87 stack.
\n
In the 1990s, Intel introduced a new floating-point system called
SSE
, followed by AVX in 2011.\nThese systems use regular (non-stack) registers and provide parallel operations for higher performance,\nmaking the 8087\'s stack instructions largely obsolete.
\n
The success of the 8087
\n
At the start, Intel was unenthusiastic about producing the 8087, viewing it as unlikely to be a success.\nJohn Palmar, a principal architect of the chip, had little success convincing\nskeptical Intel management that the market for the 8087 was enormous.\nEventually,\nhe said, "I\'ll tell you what. I\'ll relinquish my salary, provided you\'ll write down your number of how many you expect to sell, then give me a dollar for every one you sell beyond that."
7
\nIntel didn\'t agree to the deal—which would have made a fortune for Palmer—but they reluctantly agreed to produce the chip.
\n
Intel\'s Santa Clara engineers shunned the 8087, considering it unlikely to work:\nthe 8087 would be two to three times more complex than the 8086,\nwith a die so large that a wafer might not have a single working die.\nInstead, Rafi Nave, at Intel\'s Israel site, took on the risky project: “Listen, everybody knows it\'s not going to work, so if it won\'t work, I would just fulfill their expectations or their assessment.\nIf, by chance, it works, okay, then we\'ll gain tremendous respect and tremendous breakthrough on our abilities.”
\n
A small team of seven engineers developed the 8087 in Israel.\nThey designed the chip on Mylar sheets: a millimeter on Mylar represented a micron on the physical chip.\nThe drawings were then digitized on a Calma system by clicking on each polygon to create the layout.\nWhen the chip was moved into production,\nthe yield was very low but better than feared: two working dies per four-inch wafer.
\n
The 8087 ended up being a large success, said to have been Intel\'s most profitable product line at times.\nThe success of the 8087 (along with the 8088) cemented the reputation of Intel Israel, which eventually became Israel\'s largest tech employer.\nThe benefits of floating-point hardware proved to be so great that Intel integrated the floating-point unit into later processors\nstarting with the 80486 (1989).\nNowadays, most modern computers, from cellphones to mainframes, provide floating point based on the\n8087,\nso I consider the 8087 one of the most influential chips ever created.
\n
For more, follow me on\n Bluesky (
@righto.com
),\nMastodon (
@kenshirriff@oldbytes.space
),\nor
RSS
.\nI wrote some articles about the 8087 a few years ago, including
the die
,\n
the ROM
,\nthe
bit shifter
,\nand
the constants
, so you may have seen some of this material before.
\n
Notes and references
\n
\n
\n
\n
Most computers now use the
IEEE 754
floating-point standard,\nwhich is based on the 8087.\nThis standard has been awarded a\n
milestone
in computation.
↩
\n
\n
\n
Curiously, reliable sources differ on the number of transistors in the 8087 by almost a factor of 2.\n  Intel says
40,000
, as does designer William Kahan (
link
).\n  But in
A Numeric Data Processor
, designers Rafi Nave and John Palmer wrote that the chip contains "the equivalent of over 65,000 devices" (whatever "equivalent" means).\n  This number is echoed by a contemporary
article
in
Electronics
(1980) that says "over 65,000 H-MOS transistors on a 78,000-mil
2
die."\n  Many other sources, such as
Upgrading & Repairing PCs
, specify 45,000 transistors.\n  Designer Rafi Nave
stated
that the 8087 has\n  63,000 or 64,000 transistors if you count the ROM transistors directly, but if you count ROM transistors as\n  equivalent to two transistors, then you get about 75,000 transistors.
↩
\n
\n
\n
The 8087 has a 16-bit Status Word that\ncontains the stack top pointer, exception flags, the four-bit\ncondition code, and other values.\nAlthough the Status Word appears to be a 16-bit register, it is not implemented as a register.\nInstead, parts of the Status Word are stored in various places around the chip: the stack top pointer is\nin the stack circuitry, the exception flags are part of the interrupt circuitry, the condition code bits are\nnext to the datapath, and so on.\nWhen the Status Word is read or written, these various circuits are connected to the 8087\'s internal data\nbus, making the Status Word appear to be a monolithic entity.\nThus, the stack circuitry includes support for reading and writing it.
↩
\n
\n
\n
Intel filed several patents on the 8087, including
Numeric data processor
,\nanother
Numeric data processor
,\n
Programmable bidirectional shifter
,\n
Fraction bus for use in a numeric data processor
, and\n
System bus arbitration, circuitry and methodology
.
↩
\n
\n
\n
I started looking at the stack in detail to reverse engineer the micro-instruction format and determine how the\n8087\'s microcode works.\nI\'m working with the "Opcode Collective" on Discord on this project, but progress is slow due to the complexity of\nthe micro-instructions.
↩
\n
\n
\n
The 8087 detects stack underflow in a similar manner. If you pop more values from the stack than are present,\nthe tag will indicate that the register is empty and shouldn\'t be accessed. This triggers an invalid operation\nexception.
↩
\n
\n
\n
The 8087 is described in detail in
The 8086 Family User\'s Manual, Numerics Supplement
.\n  An overview of the stack is on page 60 of
The 8087 Primer
by Palmer and Morse.\n  More details are in Kahan\'s
On the Advantages of the 8087\'s Stack
, \n  an unpublished course note (maybe for
CS 279
?) with a date of Nov 2, 1990 or perhaps
August 23, 1994
.\n  Kahan discusses why the 8087\'s design makes it hard to handle stack overflow in
How important is numerical accuracy
, Dr. Dobbs, Nov. 1997.\n  Another information source is the
Oral History of Rafi Nave
↩
↩
\n
\n
\n
'}

---

*抓取时间: 2026-02-05 12:51:49*
