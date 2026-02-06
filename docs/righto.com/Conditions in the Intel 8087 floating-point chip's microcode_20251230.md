# Conditions in the Intel 8087 floating-point chip's microcode

**来源:** [righto.com](https://www.righto.com)
**发布时间:** 2025-12-30T10:00:00.000-08:00
**链接:** http://www.righto.com/2025/12/8087-microcode-conditions.html

---

{'type': 'text/html', 'language': None, 'base': 'https://www.righto.com/feeds/posts/default', 'value': '
In the 1980s, if you wanted your computer to do floating-point calculations faster, you could buy\nthe Intel 8087 floating-point coprocessor chip.\nPlugging it into your IBM PC would make operations up to 100 times faster, a big boost for spreadsheets\nand other number-crunching applications.\nThe 8087 uses complicated algorithms to compute trigonometric, logarithmic, and exponential functions.\nThese algorithms are implemented inside the chip in microcode.\nI\'m part of a group that is reverse-engineering this microcode.\nIn this post, I examine the 49 types of conditional tests that the 8087\'s microcode uses inside its algorithms.\nSome conditions are simple, such as checking if a number is zero or negative, while others are specialized,\nsuch as determining what direction to round a number.
\n
To explore the 8087\'s circuitry, I opened up an 8087 chip and took numerous photos of the silicon die with a microscope.\nAround the edges of the die, you can see the hair-thin bond wires that connect the chip to its 40 external pins.\nThe complex patterns on the die are formed by its metal wiring, as well as the polysilicon and silicon underneath.\nThe bottom half of the chip is the "datapath", the circuitry that performs calculations on 80-bit floating point values. \nAt the left of the datapath, a
constant ROM
holds important constants such as π.\nAt the right are the eight registers that the\nprogrammer uses to hold floating-point values; in an unusual design decision,\nthese registers are arranged as a
stack
.
\n
Die of the Intel 8087 floating point unit chip, with main functional blocks labeled. The die is 5mm×6mm.  Click for a larger image.
\n
The chip\'s instructions are defined by the large
microcode ROM
in the middle.\nTo execute a floating-point instruction, the 8087 decodes the instruction and the microcode engine starts executing\nthe appropriate micro-instructions from the microcode ROM.\nThe microcode decode circuitry to the right of the ROM generates the appropriate control signals from each micro-instruction.
1
\nThe bus registers and control circuitry handle interactions with the main 8086 processor and the rest of the system.
\n
The 8087\'s microcode
\n
Executing an 8087 instruction such as arctan requires hundreds of internal steps to compute the result.\nThese steps are implemented in microcode with micro-instructions specifying each step of the algorithm.\n(Keep in mind the difference between the assembly language instructions used by a programmer and the\nundocumented low-level micro-instructions used internally by the chip.)\nThe microcode ROM holds 1648 micro-instructions, implementing the 8087\'s instruction set.\nEach micro-instruction is 16 bits long and performs a simple operation such as moving data inside the chip, adding two values, or
shifting
data.\nI\'m working with the "Opcode Collective" to reverse engineer the micro-instructions and fully understand the microcode (
link
).
\n
The microcode engine (below) controls the execution of micro-instructions, acting as the mini-CPU inside the 8087.\nSpecifically, it generates an 11-bit micro-address, the address of a micro-instruction in the ROM.\nThe microcode engine implements jumps, subroutine calls, and returns within the microcode.\nThese jumps, subroutine calls, and returns are all conditional; the microcode engine will either perform the\noperation or skip it, depending on the value of a specified condition.
\n
The microcode engine. In this image, the metal is removed, showing the underlying silicon and polysilicon.
\n
I\'ll write more about the microcode engine later, but I\'ll give an overview here.\nAt the top, the Instruction Decode PLA
2
decodes an 8087 instruction to determine the starting address in\nmicrocode.\nBelow that, the Jump PLA holds microcode addresses for jumps and subroutine calls.\nBelow this, six 11-bit registers implement the microcode stack, allowing six levels of subroutine calls inside the\nmicrocode.\n(Note that this stack is completely different from the 8087\'s register stack that holds eight floating-point values.)\nThe stack registers have associated read/write circuitry.\nThe incrementer adds one to the micro-address to step through the code.\nThe engine also implements relative jumps, using an adder to add an offset to the current location.\nAt the bottom, the address latch and drivers boost the 11-bit address output\nand send it to the microcode ROM.
\n
Selecting a condition
\n
A micro-instruction can say "jump ahead 5 micro-instructions if a register is zero" and the\nmicrocode engine will either perform the jump or ignore it, based on the register value.\nIn the circuitry, the condition causes the microcode engine to either perform the jump or block the jump.\nBut how does the hardware select one condition out of the large set of conditions?
\n
Six bits of the micro-instruction can specify one of 64 conditions.\nA circuit similar to the idealized diagram below selects the specified condition.\nThe key component is a multiplexer, represented by a trapezoid below.\nA multiplexer is a simple circuit that selects one of its four inputs.\nBy arranging multiplexers in a tree, one of the 64 conditions on the left is selected and becomes the output,\npassed to the microcode engine.
\n
A tree of multiplexers selects one of the conditions. This diagram is simplified.
\n
For example, if bits J and K of the microcode are 00, the rightmost multiplexer will select the first input.\nIf bits LM are 01, the middle multiplexer will select the second input, and if bits NO are 10, the left\nmultiplexer will select its third input. The result is that condition 06 will pass through the tree and become the output.
3
\nBy changing the bits that control the multiplexers, any of the inputs can be used.\n(We\'ve arbitrarily given the 16 microcode bits the letter names A through P.)
\n
Physically, the conditions come from locations scattered across the die. For instance, conditions involving the opcode\ncome from the instruction decoding part of the chip, while conditions involving a register are evaluated\nnext to the register.\nIt would be inefficient to run 64 wires for all the conditions to the microcode engine.\nThe tree-based approach reduces the wiring since the "leaf" multiplexers can be located\nnear the associated condition circuitry. Thus, only one wire needs to travel a long distance rather than multiple wires.\nIn other words, the condition selection circuitry is distributed across the chip instead of being implemented as\na centralized module.
\n
Because the conditions don\'t always fall into groups of four, the actual implementation is slightly different from\nthe idealized diagram above.\nIn particular, the top-level multiplexer has five inputs, rather than four.
4
\nOther multiplexers don\'t use all four inputs.\nThis provides a better match between the physical locations of the condition circuits and the multiplexers.\nIn total, 49 of the possible 64 conditions are implemented in the 8087.
\n
The circuit that selects one of the four conditions is called a multiplexer.\nIt is constructed from pass transistors, transistors that are configured to either pass a signal through\nor block it.\nTo operate the multiplexer, one of the select lines is energized, turning on the corresponding pass transistor.\nThis allows the selected input to pass through the transistor to the output, while the other inputs are blocked.
\n
A 4-1 multiplexer, constructed from four pass transistors.
\n
The diagram below shows how a multiplexer appears on the die. The pinkish regions are doped silicon. The white\nlines are polysilicon wires.\nWhen polysilicon crosses over doped silicon, a transistor is formed.\nOn the left is a four-way multiplexer, constructed from four pass transistors. It takes inputs (black) for four conditions,\nnumbered 38, 39, 3a, and 3b.\nThere are four control signals (red) corresponding to the four combinations of bits N and O.\nOne of the inputs will pass through a transistor to the output, selected by the active control signal.\nThe right half contains the logic (four NOR gates and two inverters) to generate the control signals from the\nmicrocode bits.\n(Metal lines run horizontally from the logic to the control signal contacts, but I dissolved the metal for this\nphoto.)\nEach multiplexer in the 8087 has a completely different layout,\nmanually optimized based on the location of the signals and surrounding circuitry.\nAlthough the circuit for a multiplexer is regular (four transistors in parallel), the physical layout looks\nsomewhat chaotic.
\n
Multiplexers as they appear on the die. The metal layer has been removed to show the polysilicon and silicon. The "tie-die" patterns are due to thin-film effects where the oxide layer wasn\'t completely removed.
\n
The 8087 uses pass transistors for many circuits, not just multiplexers.\nCircuits with pass transistors are different from regular logic gates\nbecause the pass transistors provide no amplification. Instead, signals get weaker as they go through pass\ntransistors.\nTo solve this problem, inverters or buffers are inserted into the condition tree to boost signals;\nthey are omitted from the diagram above.
\n
The conditions
\n
Of the 8087\'s 49 different conditions, some are widely used in the microcode, while others are designed for\na specific purpose and are only used once.\nThe full set of conditions is described in a footnote
7
but I\'ll give some highlights here.
\n
Fifteen conditions examine the bits of the current instruction\'s opcode. This allows\none microcode routine to handle a group of similar instructions and then change behavior based on the specific\ninstruction. For example, conditions test if the instruction is multiplication, if the instruction is an FILD/FIST\n(integer load or store), or if the bottom bit of the opcode is set.
5
\n
The 8087 has three temporary registers—tmpA, tmpB, and tmpC—that hold values during computation.\nVarious conditions examine the values in the tmpA and tmpB registers.
6
\nIn particular, the 8087 uses an interesting way to store numbers internally: each 80-bit floating-point value also \nhas two "tag" bits.\nThese bits are mostly invisible to the programmer and can be thought of as metadata.\nThe tag bits indicate if a register is empty, contains zero, contains a "normal" number, or contains a special\nvalue such as NaN (Not a Number) or infinity.\nThe 8087 uses the tag bits to optimize operations.\nThe tags also detect stack overflow (storing to a non-empty stack register) or stack underflow (reading from\nan empty stack register).
\n
Other conditions are highly specialized. For instance, one condition looks at the rounding mode setting and\nthe sign of the value to determine if the value should be rounded up or down.\nOther conditions deal with exceptions such as numbers that are too small (i.e. denormalized) or numbers that\nlose precision.\nAnother condition tests if two values have the same sign or not.\nYet another condition tests if two values have the same sign or not, but inverts the result if the current\ninstruction is subtraction.\nThe simplest condition is simply "true", allowing an unconditional branch.
\n
For flexibility, conditions can be "flipped", either jumping if the condition is true or jumping if the condition is false.\nThis is controlled by bit P of the microcode.\nIn the circuitry, this is implemented by a gate that XORs the P bit with the condition. The result is that the\nstate of the condition is flipped if bit P is set.
\n
For a concrete example of how conditions are used, consider the\n
microcode routine
\nthat implements
FCHS
and
FABS
, the\ninstructions to change the sign and compute the absolute value, respectively.\nThese operations are almost the same (toggling the sign bit versus clearing the sign bit), so the same\nmicrocode routine handles both instructions, with a jump instruction to handle the difference.\nThe
FABS
and
FCHS
instructions were designed with identical opcodes,\nexcept that the bottom bit is set for
FABS
.\nThus, the microcode routine uses a condition that tests the bottom bit, allowing the routine to branch and\nchange its behavior for
FABS
vs
FCHS
.
\n
Looking at the relevant micro-instruction, it has the hex value\n
0xc094
, or in binary
110 000001 001010 0
.\nThe first three bits (ABC=110) specify the relative jump operation (100 would jump to a fixed target and 101 would\nperform a subroutine call.)\nBits D through I (
000010
) indicate the amount of the jump (+`). \nBits J through O (
001010
, hex 0a) specify the condition to test, in this case, the last bit of the instruction opcode.\nThe final bit (P) would toggle the condition if set, (i.e. jump if false).\nThus, for
FABS
, the jump instruction will jump ahead one micro-instruction.\nThis has the effect of skipping the next micro-instruction, which sets the appropriate sign bit for\n
FCHS
.
\n
Conclusions
\n
The 8087 performs floating-point operations much faster than the 8086 by using\nspecial hardware, optimized for floating-point.\nThe condition code circuitry is one example of this: the 8087\ncan test a complicated condition in a single operation.\nHowever, these complicated conditions make it much harder to understand the microcode.\nBut by a combination of examining the circuitry and looking at the micocode, we\'re making progress.\nThanks to the members of the "Opcode Collective" for their hard work, especially Smartest Blob and Gloriouscow.
\n
For updates, follow me on\n Bluesky (
@righto.com
),\nMastodon (
@kenshirriff@oldbytes.space
),\nor
RSS
.
\n
Notes and references
\n
\n
\n
\n
The section of the die that I\'ve labeled "Microcode decode" performs some of the microcode decoding, but\nlarge parts of the decoding are scattered across the chip, close to the circuitry that needs the signals.\nThis makes reverse-engineering the microcode much more difficult.\nI thought that understanding the microcode would be straightforward, just examining a block of decode circuitry.\nBut this project turned out to be much more complicated and I need to reverse-engineer the entire chip.
↩
\n
\n
\n
A PLA is a "Programmable Logic Array". It is a technique to implement logic functions with grids of transistors.\nA PLA can be used as a compressed ROM, holding data in a more compact representation.\n(Saving space was very important in chips of this era.)\nIn the 8087, PLAs are used to hold tables of microcode addresses.
↩
\n
\n
\n
Note that the multiplexer circuit selects the condition corresponding to the binary value of the bits.\nIn the example, bits 000110 (0x06) select condition 06.
↩
\n
\n
\n
The five top-level multiplexer inputs correspond to bit patterns 00, 011, 10, 110, and 111.\nThat is, two inputs depend on bits J and K, while three inputs depend on bits J, K, and L.\nThe bit pattern 010 is unused, corresponding to conditions 0x10 through 0x17, which aren\'t implemented.
↩
\n
\n
\n
The 8087 acts as a co-processor with the 8086 processor.\nThe 8086 instruction set is designed so instructions with a special "ESCAPE" sequence in the top 5 bits\nare processed by the co-processor, in this case the 8087.\nThus, the 8087 receives a 16-bit instruction, but only the bottom 11 bits are usable.\nFor a memory operation, the second byte of the instruction is an 8086-style
ModR/M
byte.\nFor instructions that don\'t access memory, the second byte specifies more of the instruction and sometimes specifies the\nstack register to use for the instruction.
\n
The relevance of this is that the 8087\'s microcode engine uses the 11 bits of the instruction to determine\nwhich microcode routine to execute.\nThe microcode also uses various condition codes to change behavior depending on different bits of the\ninstruction.
↩
\n
\n
\n
There is a complication with the tmpA and tmpB registers: they can be swapped with the micro-instruction\n"ABC.EF". \nThe motivation behind this is that if you have two arguments, you can use a micro-subroutine to load\nan argument into tmpA, swap the registers, and then use the same subroutine to load the second argument\ninto tmpA. The result is that the two arguments end up in tmpB and tmpA without any special coding in\nthe subroutine.
\n
The implementation doesn\'t physically swap the registers, but renames them internally, which is\nmuch more efficient.\nA flip-flop is toggled every time the registers are swapped. If the flip-flop is set, a request goes\nto one register, while if the flip-flop is clear, a request goes to the other register.\n(Many processors use the same trick. For instance, the Intel 8080 has an instruction to exchange the\nDE and HL registers. The Z80 has an instruction to swap register banks. In both cases, a flip-flop\nrenames the registers, so the data doesn\'t need to move.)
↩
\n
\n
\n
The table below is the real meat of this post, the result of much circuit analysis. These details probably aren\'t\ninteresting to most people, so I\'ve relegated the table to a footnote.\nDescriptions in italics are provided by Smartest Blob based on examination of the microcode.\nGrayed-out lines are unused conditions.
\n
The table has five sections, corresponding to the 5 inputs to the top-level condition multiplexer.\nThese inputs come from different parts of the chip, so the sections correspond to different categories of\nconditions.
\n
The first section consists of instruction parsing, with circuitry near the microcode engine.\nThe description shows the 11-bit opcode pattern that triggers the condition, with 0 bits and 1 bits as\nspecified, and X indicating a "don\'t care" bit that can be 0 or 1.\nWhere simpler, I list the relevant instructions instead.
\n
The next section indicates conditions on the exponent. I am still investigating these conditions, so\nthe descriptions are incomplete.\nThe third section is conditions on the temporary registers or conditions related to the control register.\nThese circuits are to the right of the microcode ROM.
\n
Conditions in the fourth section examine the floating-point bus, with circuitry near the bottom of the chip.\nConditions 34 and 35 use a special 16-bit bidirectional shift register, at the far right of the chip.\nThe top bit from the floating-point bus is shifted in. Maybe this shift register is used for CORDIC\ncalculations?\nThe conditions in the final block are miscellaneous, including the always-true condition 3e, which is used\nfor unconditional jumps.
\n
\n
\n
Cond.
Description
\n
00
not XXX 11XXXXXX
\n
01
1XX 11XXXXXX
\n
02
0XX 11XXXXXX
\n
03
X0X XXXXXXXX
\n
04
not cond 07 or 1XX XXXXXXXX
\n
05
not FLD/FSTP temp-real or BCD
\n
06
110 xxxxxxxx or 111 xx0xxxxx
\n
07
FLD/FSTP temp-real
\n
08
FBLD/FBSTP
\n
09
\n
0a
XXX XXXXXXX1
\n
0b
XXX XXXX1XXX
\n
0c
FMUL
\n
0d
FDIV FDIVR
\n
0e
FADD FCOM FCOMP FCOMPP FDIV FDIVR FFREE FLD FMUL FST FSTP FSUB FSUBR FXCH
\n
0f
FCOM FCOMP FCOMPP FTST
\n
10
\n
11
\n
12
\n
13
\n
14
\n
15
\n
16
\n
17
\n
18
exponent condition
\n
19
exponent condition
\n
1a
exponent condition
\n
1b
exponent condition
\n
1c
exponent condition
\n
1d
exponent condition
\n
1e
eight exponent zero bits
\n
1f
exponent condition
\n
20
tmpA tag ZERO
\n
21
tmpA tag SPECIAL
\n
22
tmpA tag VALID
\n
23
stack overflow
\n
24
tmpB tag ZERO
\n
25
tmpB tag SPECIAL
\n
26
tmpB tag VALID
\n
27
st(i) doesn\'t exist (A)?
\n
28
tmpA sign
\n
29
tmpB top bit
\n
2a
tmpA zero
\n
2b
tmpA top bit
\n
2c
Control Reg bit 12: infinity control
\n
2d
round up/down
\n
2e
unmasked interrupt
\n
2f
DE (denormalized) interrupt
\n
30
top reg bit
\n
31
\n
32
reg bit 64
\n
33
reg bit 63
\n
34
Shifted top bits, all zero
\n
35
Shifted top bits, one out
\n
36
\n
37
\n
38
const latch zero
\n
39
tmpA vs tmpB sign, flipped for subtraction
\n
3a
precision exception
\n
3b
tmpA vs tmpB sign
\n
3c
\n
3d
\n
3e
unconditional
\n
3f
\n
\n
This table is under development and undoubtedly has errors.
↩
\n
\n
\n
'}

---

*抓取时间: 2026-02-05 12:51:49*
