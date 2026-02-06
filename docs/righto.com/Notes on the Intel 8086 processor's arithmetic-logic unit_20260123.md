# Notes on the Intel 8086 processor's arithmetic-logic unit

**来源:** [righto.com](https://www.righto.com)
**发布时间:** 2026-01-23T09:09:00.000-08:00
**链接:** http://www.righto.com/2026/01/notes-on-intel-8086-processors.html

---

{'type': 'text/html', 'language': None, 'base': 'https://www.righto.com/feeds/posts/default', 'value': '
In 1978, Intel introduced the 8086 processor, a revolutionary chip that led to the modern x86 architecture.\nUnlike modern 64-bit processors, however, the 8086 is a 16-bit chip.\nIts arithmetic/logic unit (ALU) operates on 16-bit values, performing arithmetic operations such as addition and subtraction,\nas well as logic operations including bitwise AND, OR, and XOR.\nThe 8086\'s ALU is a complicated part of the chip, performing 28 operations in total.
1
\n
In this post, I discuss the circuitry that controls the ALU, generating the appropriate control signals for a\nparticular operation.\nThe process is more complicated than you might expect. First, a machine code instruction results in the execution of multiple\nmicrocode instructions.\nUsing the ALU is a two-step process: one microcode instruction (micro-instruction) configures the ALU for the desired operation,\nwhile a second\nmicro-instruction gets the results from the ALU.\nMoreover, based on both the microcode micro-instruction and the machine code instruction, the control circuitry sends control signals to the ALU,\nreconfiguring it for the desired operation.\nThus, this circuitry provides the "glue" between the micro-instructions and the ALU.
\n
The die photo below shows the 8086 processor under a microscope.\nI\'ve labeled the key functional blocks.\nArchitecturally, the chip is partitioned into a Bus Interface Unit (BIU) at the top and an Execution Unit (EU) below.\nThe BIU handles bus and memory activity as well as instruction prefetching, while the Execution Unit (EU) executes the instructions.\nIn the lower right corner, the microcode ROM holds the micro-instructions.\nThe ALU is in the lower left corner, with bits 7-0 above and bits 15-8 below, sandwiching the status flag circuitry.\nThe ALU control circuitry, highlighted in red at the bottom of the chip, is the focus of this article.
\n
The die of the 8086. Click this image (or any other) for a larger version.
\n
Microcode
\n
The 8086 processor implements most machine instructions in microcode, with a micro-instruction for each step of the machine instruction.\n(I discuss the 8086\'s microcode in detail
here
.)\nThe 8086 uses an interesting architecture for microcode:\neach micro-instruction performs two unrelated operations. The first operation moves data between a source and a destination.\nThe second operation can range from a jump or subroutine call to a memory read/write or an ALU operation.\nAn ALU operation has a five-bit field to specify a particular operation and a two-bit field to specify\nwhich temporary register provides the input. As you\'ll see below, these two fields play an important role in the ALU circuitry.
\n
In many cases, the 8086\'s micro-instruction doesn\'t specify the ALU operation, leaving the details to be substituted from the machine instruction opcode.\nFor instance, the ADD, SUB, ADC, SBB, AND, OR, XOR, and CMP\nmachine instructions share the same microcode, while the hardware selects the ALU operation from the instruction opcode.\nLikewise, the increment and decrement instructions use the same microcode, as do the decimal adjust instructions DAA and DAS, and the\nASCII adjust instructions AAA and AAS.\nInside the micro-instruction, all these operations are performed with a "pseudo" ALU operation called XI (for some reason).\nIf the microcode specifies an XI ALU operation, the hardware replaces it with the ALU operation specified in the instruction.\nAnother important feature of the microcode is \nthat you need to perform one ALU micro-instruction to configure the ALU\'s operation, but the result isn\'t\navailable until a later micro-instruction, which moves the result to a destination.\nThis has the consequence that the hardware must remember the ALU operation.
\n
To make this concrete, here is the microcode that implements a typical arithmetic instruction such as
ADD AL, BL
or
XOR [BX+DI], CX
.\nThis microcode consists of three micro-instructions. \nThe left half of each micro-instruction specifies a data movement, first moving the two arguments to ALU temporary registers\nand then storing the ALU result (called Σ).\nThe right half of each micro-instruction performs the second task.\nFirst, the ALU is configured to perform an
XI
operation using temporary register A. Recall that
XI
indicates the ALU operation\nis filled in from the machine instruction; this is how the same microcode handles eight different types of machine instructions.\nIn the second micro-instruction, the next machine instruction is started unless a memory writeback is required (
WB
).\nThe last micro-instruction is
RNI
(Run Next Instruction) to start a new machine instruction. It also indicates that the\nprocessor status flags (
F
) should be updated to indicate if the ALU result is zero, positive, overflow, and so forth.
2
\n\n
\nM → tmpa   XI   tmpa
Load first argument, configure ALU.
\nR → tmpb   WB,NXT
Load second argument, start Next instruction if no memory writeback
\nΣ → M      RNI  F
Store ALU result, Run Next Instruction, update status Flags
\n
\n\n
The ALU circuit
\n
The ALU is the heart of a processor, performing arithmetic and logic operations.\nMicroprocessors of the 1970s typically supported addition and subtraction; logical AND, OR, and XOR; and various bit shift operations.\n(Although the 8086 had multiply and divide instructions, these were implemented in microcode, not in the ALU.)\nSince an ALU is both large and critical to performance, chip architects try to optimize its design.\nAs a result, different microprocessors have widely different ALU designs.\nFor instance, the 6502 microprocessor has separate circuits for addition and each logic operation; a multiplexer selects the appropriate\noutput.\nThe Intel 8085, on the other hand, uses an optimized clump of gates that performs the desired operation based on control signals (
details
), while the Z80\'s 4-bit ALU uses a different clump of gates (
details
).
\n
The 8086 takes a different approach, using two lookup tables (along with other gates) to generate the carry and output signals for each bit in the ALU.\nBy setting the lookup tables appropriately, the ALU can be configured to perform the desired operation.\n(This is similar to how an FPGA implements arbitrary functions through lookup tables.)\nThe schematic below shows the circuit for one bit of the ALU.\nI won\'t explain this circuit in detail since I explained it in
an earlier article
.
3
\nThe relevant part of this circuit is the six control signals at the left.\nThe two multiplexers (trapezoidal symbols) implement the lookup tables by using the two input argument bits to select outputs from\nthe control signals to control carry generation and carry propagation.\nThus, by feeding appropriate control signals into the ALU, the 8086 can reconfigure the ALU to perform the desired operation.\nFor instance, with one set of control signals, this circuit will add. Other sets of control signals will cause the circuit to subtract\nor compute a logical operation, such as AND or XOR.\nThe 8086 has 16 copies of this circuit, so it operates on 16-bit values.
\n
The circuit that implements one bit in the 8086\'s ALU.
\n
The 8086 is a complicated processor, and its instructions have many special cases, so controlling the ALU is\nmore complex than described above.\nFor instance, the compare operation is the same as a subtraction, except the numerical result of a compare is discarded; just the\nstatus flags are updated.\nThe add versus add-with-carry instructions require different values for the carry into bit 0, while subtraction requires the\ncarry flag to be inverted since it is treated as a borrow.\nThe 8086\'s ALU supports increment and decrement operations, but also increment and decrement by 2, which requires an increment signal into bit\n1 instead of bit 0.\nThe bit-shift operations all require special treatment. For instance, a rotate can use the carry bit or exclude the carry bit, while\nand arithmetic shift right requires the top bit to be duplicated.\nAs a result, along with the six lookup table (LUT) control signals, the ALU also requires numerous control signals to adjust its\nbehavior for specific instructions.\nIn the next section, I\'ll explain how these control signals are generated.
\n
ALU control circuitry on the die
\n
The diagram below shows the components of the ALU control logic as they appear on the die.\nThe information from the micro-instruction enters at the right and is stored in the latches.\nThe PLAs (Programmable Logic Arrays) decode the instruction and generate the control signals.\nThese signals flow to the left, where they control the ALU.
\n
The ALU control logic as it appears on the die. I removed the metal layer to show the underlying polysilicon and silicon. The reddish lines are remnants of the metal.
\n
As explained earlier, if the microcode specifies the
XI
operation, the operation field is replaced with a value based on the machine instruction opcode.\nThis substitution is performed by the
XI
multiplexer before the value is stored in the operation latch.\nBecause of the complexity of the 8086 instruction set, the
XI
operation is not as straightforward as you might expect.\nThis multiplexer gets three instruction bits from a special register called the "X" register, another instruction bit from the instruction\nregister, and the final bit from a decoding circuit called the Group Decode ROM.
4
\n
Recall that one micro-instruction specifies the ALU operation, and a later micro-instruction accesses the result. Thus, the\nALU control circuitry must remember the specified operation so it can be used later. \nIn particular, the control circuitry must keep track of the ALU operation to perform and the temporary register specified.\nThe control circuitry uses three flip-flops to keep track of the specified temporary register, one flip-flop for each register.\nThe micro-instruction contains a two-bit field that specifies the temporary register. The control circuitry decodes this field and\nactivates the associated flip-flop.\nThe outputs from these flip-flops go to the ALU and enable the associated temporary register.\nAt the start of each machine instruction,
5
the flip-flops are reset, so temporary register A is selected by default.
\n
The control circuitry uses five flip-flops to store the five-bit operation field from the micro-instruction.\nAt the start of each machine instruction, the flip-flops are reset so operation 0 (ADD) is specified by default.\nOne important consequence is that an add operation can potentially be performed without a micro-instruction to configure the ALU,\nshortening the microcode by one micro-instruction and thus shortening the instruction time by one cycle.
\n
The five-bit output from the operation flip-flops goes to the operation PLA (Programmable Logic Array)
7
, which decodes the operation\ninto 27 control signals.
6
\nMany of these signals go to the ALU, where they control the behavior of the ALU for special cases.\nAbout 15 of these signals go to the Lookup Table (LUT) PLA, which generates the six lookup table signals for the ALU.\nAt the left side of the LUT PLA, special high-current driver circuits amplify the control signals before they are sent to the ALU.\nDetails on these drivers are in the footnotes.
8
\n
Conclusions
\n
Whenever I look at the circuitry of the 8086 processor, I see the differences between a RISC chip and a CISC chip.\nIn a RISC (Reduced Instruction Set Computer) processor such as ARM, instruction decoding is straightforward, as is the processor circuitry.\nBut in the 8086, a CISC (Complex Instruction Set Computer) processor, there are corner cases and complications everywhere.\nFor instance, an 8086 machine instruction sometimes specifies the ALU operation in the first byte and sometimes in the second byte,\nand sometimes elsewhere, so the X register latch, the XI multiplexer, and the Group Decode ROM are needed.\nThe 8086\'s ALU includes obscure operations including four types of BCD adjustments and seven types of shifts, making the ALU more\ncomplicated.\nOf course, the continuing success of x86 shows that this complexity also has benefits.
\n
This article has been a deep dive into the details of the 8086\'s ALU, but I hope you have found it interesting.\nIf it\'s too much detail for you, you might prefer my overview of the
8086 ALU
.
\n
For updates, follow me on\n Bluesky (
@righto.com
),\nMastodon (
@kenshirriff@oldbytes.space
),\nor
RSS
.
\n
Credits:\nThanks to Marcin Peczarski for discussion.\nMy microcode analysis is based on Andrew Jenner\'s
8086 microcode disassembly
.
\n
Notes and references
\n
\n
\n
\n
\n
The operations implemented by the ALU are:
\n
\n
00
ADD
Add
\n
01
OR
Logical OR
\n
02
ADC
Add with carry in
\n
03
SBB
Subtract with borrow in
\n
04
AND
Logical AND
\n
05
SUBT
Subtract
\n
06
XOR
Logical XOR
\n
07
CMP
Comparison
\n
08
ROL
Rotate left
\n
09
ROR
Rotate right
\n
0a
LRCY
Left rotate through carry
\n
0b
RRCY
Right rotate through carry
\n
0c
SHL
Shift left
\n
0d
SHR
Shift right
\n
0e
SETMO
Set to minus one (
questionable
)
\n
0f
SAR
Arithmetic shift right
\n
10
PASS
Pass argument unchanged
\n
11
XI
Instruction specifies ALU op
\n
14
DAA
Decimal adjust after addition
\n
15
DAS
Decimal adjust after subtraction
\n
16
AAA
ASCII adjust after addition
\n
17
AAS
ASCII adjust after subtraction
\n
18
INC
Increment
\n
19
DEC
Decrement
\n
1a
COM1
1\'s complement
\n
1b
NEG
Negate
\n
1c
INC2
Increment by 2
\n
1d
DEC2
Decrement by 2
\n
\n
Also see Andrew Jenner\'s
code
.
↩
\n
\n
\n
You might wonder how this microcode handles the 8086\'s complicated addressing modes such as
[BX+DI]
.\nThe trick is that microcode subroutines implement the addressing modes.\nFor details, see my article on
8086 addressing microcode
.
↩
\n
\n
\n
The 8086\'s ALU has a separate circuit to implement shift-right.\nThe problem is that data in an ALU normally flows right-to-left as carries flow from lower bits to higher bits.\nShifting data to the right goes against this direction, so it requires a special path.\n(Shifting to the left is straightforward; you can add a number to itself.)
\n
The adjust operations (DAA, DAS, AAA, AAS) also use completely separate circuitry.\nThese operations generate correction factors for BCD (binary-coded decimal) arithmetic based on the value and flags.\nThe circuitry for these operations is located with the flags circuitry, separate from the rest of the ALU circuitry.
↩
\n
\n
\n
In more detail, the 8086 stores bits 5-3 of the machine instruction in the "X" register.\nFor an XI operation, the X register bits become bits 2-0 of the ALU operation specification, while bit 3 comes from bit 6 of the\ninstruction, and bit 4 comes from the
Group Decode ROM
for\ncertain instructions.\nThe point of this is that the instruction set is designed so bits of the instruction correspond to bits of the ALU operation\nspecifier, but the mapping is more complicated than you might expect.\nThe eight basic arithmetic/logic operations (ADD, SUB, OR, etc) have a straightforward mapping that is visible from\nthe
8086 opcode table
, but the mapping for other instructions isn\'t as obvious.\nMoreover, sometimes the operation is specified in the first byte of the machine instruction, but sometimes it is specified\nin the second byte, which is why the X register needs to store the relevant bits.
↩
\n
\n
\n
The flip-flops are reset by a signal in the 8086, called "Second Clock". When a new machine instruction is started, the "First Clock" signal\nis generated on the instruction\'s first byte and the "Second Clock" signal is generated on the instruction\'s second byte.\n(Note that these signals are not necessarily on consecutive clock cycles, because a memory fetch may be required if the\ninstruction queue is empty.)\nWhy are the flip-flops reset on Second Clock and not First Clock? The 8086 has a small degree of pipelining, so the previous\nmicro-instruction may still be finishing up during First Clock of the next instruction. By Second Clock, it is safe to reset\nthe ALU state.
↩
\n
\n
\n
For reference, the 27 outputs from the PLA are triggered by the following ALU micro-operations:
\n
Output 0: RRCY (right rotate through carry) \n
Output 1: ROR (Rotate Right) \n
Output 2: BCD Adjustments: DAA (Decimal Adjust after Addition), DAS (Decimal Adjust after Subtraction), AAA (ASCII Adjust after Subtraction), or AAS (ASCII Adjust after Subtraction) \n
Output 3: SAR (Shift Arithmetic Right)\n
Output 4: Left shift: ROL (Rotate Left), RCL (Rotate through Carry Left), SHL (Shift Left), or SETMO (Set Minus One)\n
Output 5: Right shift: ROR (Rotate Right), RCR (Rotate through Carry Right), SHR (Shift Right), or SAR (Shift Arithmetic Right)\n
Output 6: INC2 (increment by 2) \n
Output 7: ROL (Rotate Left) \n
Output 8: RCL (Rotate through Carry Left)\n
Output 9: ADC (add with carry) \n
Output 10: DEC2 (decrement by 2) \n
Output 11: INC (increment) \n
Output 12: NEG (negate) \n
Output 13: ALU operation 12 (unused?)\n
Output 14: SUB (Subtract), CMP (Compare), DAS (Decimal Adjust after Subtraction), AAS (ASCII Adjust after Subtraction)\n
Output 15: SBB (Subtract with Borrow) \n
Output 16: ROL (Rotate Left) or RCL (Rotate through Carry Left)\n
Output 17: ADD or ADC (Add with Carry)\n
Output 18: DEC or DEC2 (Decrement by 1 or 2)\n
Output 19: PASS (pass-through) or INC (Increment)\n
Output 20: COM1 (1\'s Complement) or NEG (Negate) \n
Output 21: XOR \n
Output 22: OR \n
Output 23: AND \n
Output 24: SHL (Shift Left)\n
Output 25: DAA or AAA (Decimal/ASCII Adjust after Addition)\n
Output 26: CMP (Compare)
↩
\n
\n
\n
A Programmable Logic Array is a way of implementing logic gates in a structured grid. PLAs are often used in microprocessors because\nthey provide a dense way of implementing logic.\nA PLA normally consists of two layers: an "OR" layer and an "AND" layer. Together, the layers produce "sum-of-products" outputs,\nconsisting of multiple terms OR\'d together.\nThe ALU\'s PLA is a bit unusual because many outputs are taken directly from the OR layer, while only about 15 outputs from the\nfirst layer are fed into the second layer.
↩
\n
\n
\n
The control signals pass through the driver circuit below.\nThe operation of this circuit puzzled me for years, since the transistor with its gate at +5V seems to be stuck on.\nBut I was looking at the book
DRAM Circuit Design
and spotted the same circuit, called \nthe "Bootstrap Wordline Driver".\nThe purpose of this circuit is to boost the output to a higher voltage than a regular NMOS circuit, providing better performance.\nThe problem with NMOS circuitry is that NMOS transistors aren\'t very good at pulling a signal high: due to the properties of the\ntransistor, the output voltage is less than the gate voltage, lower by the threshold voltage V
TH
, half a volt or more.
\n
The drive signals to the ALU gates are generated with this dynamic circuit.
\n
The bootstrap circuit takes advantage of capacitance to get more voltage out of the circuit.\nSpecifically, suppose the input is +5V, while the clock is high. Point A will be about 4.5V, losing half a volt due to the threshold.\nNow, suppose the clock goes low, so the inverted clock driving the upper transistor goes high.\nDue to capacitance in the second transistor, as the source and drain go high, the gate will\nbe pulled above its previous voltage, maybe gaining a couple of volts.\nThe high voltage on the gate produces a full-voltage output, avoiding\nthe drop due to V
TH
.\nBut why the transistor with its gate at +5V? This transistor acts somewhat like a diode, preventing the boosted voltage from flowing\nbackward through the input and dissipating.
\n
The bootstrap circuit is used on the ALU\'s lookup table control signals for two reasons.\nFirst, these control signals drive pass transistors. A pass transistor suffers from a voltage drop due to the threshold voltage,\nso you want to start with a control signal with as high a voltage as possible.\nSecond, each control signal is connected to 16 transistors (one for each bit).\nThis is a large number of transistors to drive from one signal, since each transistor has gate capacitance.\nIncreasing the voltage helps overcome the R-C (resistor-capacitor) delay, improving performance.
\n
A close-up of the bootstrap drive circuits, in the left half of the LUT PLA.
\n
The diagram above shows six bootstrap drivers on the die. At the left are the transistors that ground the signals when clock is\nhigh. The +5V transistors are scattered around the image; two of them are labeled.\nThe six large transistors provide the output signal, controlled by clock\'.\nNote that these transistors are much larger than the other transistors because they must produce the high-current output,\nwhile the other transistors have more of a supporting role.
\n
(Bootstrap circuits go way back; Federico Faggin designed a bootstrap circuit for the
Intel 8008
that he claimed "proved essential to the microprocessor realization.")
↩
\n
\n
\n
'}

---

*抓取时间: 2026-02-05 12:51:49*
