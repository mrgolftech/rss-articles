# Unusual circuits in the Intel 386's standard cell logic

**来源:** [righto.com](https://www.righto.com)
**发布时间:** 2025-11-22T08:15:00.000-08:00
**链接:** http://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html

---

{'type': 'text/html', 'language': None, 'base': 'https://www.righto.com/feeds/posts/default', 'value': '
I\'ve been studying the standard cell circuitry in the Intel 386 processor recently.\nThe 386, introduced in 1985, was Intel\'s most complex processor at the time, containing 285,000 transistors.\nIntel\'s existing design techniques couldn\'t handle this complexity and the chip began to fall behind schedule.\nTo meet the schedule, the 386 team started using a technique called standard cell logic.\nInstead of laying out each transistor manually, the layout process was performed by a computer.
\n
The idea behind standard cell logic is to create standardized circuits (standard cells) for each type of logic element, such\nas an inverter, NAND gate, or latch.\nYou feed your circuit description into software that selects the necessary cells, \npositions these cells into columns, and then routes the wiring between the cells.\nThis "automatic place and route" process creates the chip layout much faster than manual layout.\nHowever, switching to standard cells was a risky decision since if the software couldn\'t create a\ndense enough layout, the chip couldn\'t be manufactured.\nBut in the end, the 386 finished ahead of schedule, an almost unheard-of accomplishment.
1
\n
The 386\'s standard cell circuitry contains a few circuits that I didn\'t expect.\nIn this blog post, I\'ll take a quick look at some of these circuits:\nsurprisingly large multiplexers, a transistor that doesn\'t fit into the standard cell layout,\nand inverters that turned out not to be inverters.\n(If you want more background on standard cells in the 386, see my earlier post,\n"
Reverse engineering standard cell logic in the Intel 386 processor
".)
\n
The photo below shows the 386 die with the automatic-place-and-route regions highlighted; I\'m focusing\non the red region in the lower right.\nThese blocks of logic have cells arranged in rows, giving them a characteristic striped appearance.\nThe dark stripes are the transistors that make up the logic gates, while the lighter regions between the stripes are the\n"routing channels" that hold the wiring that connects the cells.\nIn comparison,\nfunctional blocks\nsuch as the datapath on the left\nand the microcode ROM in the lower right\nwere designed manually to optimize density and performance, giving them a more solid appearance.
\n
The 386 die with the standard-cell regions highlighted.
\n
As for other features on the chip,\nthe black circles around the border are bond wire connections that go to the chip\'s external pins.\nThe chip has two metal layers, a small number by modern\nstandards, but a jump from the single metal layer of earlier processors such as the 286.\n(Providing two layers of metal made automated routing practical: one layer can hold horizontal wires while the other layer\ncan hold vertical wires.)\nThe metal appears white in larger areas, but\npurplish where circuitry underneath roughens its surface.\nThe underlying silicon and the polysilicon wiring are obscured by the metal layers.
\n
The giant multiplexers
\n
The standard cell circuitry that I\'m examining (red box above) is part of the control logic that selects registers\nwhile executing an instruction.\nYou might think that it is easy to select which registers take part in an instruction, but\ndue to the complexity of the x86 architecture, it is more difficult.\nOne problem is that a 32-bit register such as EAX can also be treated as the 16-bit register AX,\nor two 8-bit registers AH and AL.\nA second problem is that some instructions include a "direction" bit that switches the source and\ndestination registers.\nMoreover, sometimes the register is specified by bits in the instruction, but in other cases,\nthe register is specified by the microcode.\nDue to these factors, selecting the registers for an operation is a complicated process with many\ncases, using control bits from the instruction, from the microcode, and from other sources.
\n
Three registers need to be selected for an operation—two source registers and a destination register—and there\nare about 17 cases that need to be handled.\nRegisters are specified with 7-bit control signals that select one of the 30 registers and control\nwhich part of the register is accessed.\nWith three control signals, each 7 bits wide, and about 17 cases for each, you can see that\nthe register control logic is large and complicated.\n(I wrote more about the 386\'s registers
here
.)
\n
I\'m still reverse engineering the register control logic, so I won\'t go into details.\nInstead, I\'ll discuss how the register control circuit uses multiplexers, implemented with standard cells.\nA multiplexer is a circuit that combines multiple\ninput signals into a single output by selecting one of the inputs.
2
\nA multiplexer can be implemented with logic gates, for instance, by ANDing each input with the\ncorresponding control line, and then ORing the results together.\nHowever, the 386 uses a different approach—CMOS switches—that avoids a large AND/OR gate.
\n
Schematic of a CMOS switch.
\n
The schematic above shows how a CMOS switch is constructed from two MOS transistors.\nWhen the two transistors are on, the output is connected to the input, but when the two transistors are\noff, the output is isolated.\nAn NMOS transistor is turned on when its input is high, but a PMOS transistor is turned on when its\ninput is
low
. Thus, the switch uses two control inputs, one inverted.\nThe motivation for using two transistors is that an NMOS transistor is better at pulling the output\nlow, while a PMOS transistor is better at pulling the output high, so combining them yields the best performance.
3
\nUnlike a logic gate, the CMOS switch has no amplification, so a signal is weakened as it passes through the switch.\nAs will be seen below, inverters can be used to amplify the signal.
\n
The image below shows how CMOS switches appear under the microscope.\nThis image is very hard to interpret because the two layers of metal on the 386 are packed together densely, but you\ncan see that some wires run horizontally and others run vertically.\nThe bottom layer of metal (called M1) runs vertically in the routing area, as well as providing internal\nwiring for a cell.\nThe top layer of metal (M2) runs horizontally; unlike M1, the M2 wires can cross a cell.\nThe large circles are vias that connect the M1 and M2 layers, while the small circles are connections\nbetween M1 and polysilicon or M1 and silicon.\nThe central third of the image is a column of standard cells with two CMOS switches outlined in green.\nThe cells are bordered by the vertical ground rail and\n+5V rail that power the cells. \nThe routing areas are on either side of the cells, holding the wiring that connects the cells.
\n
Two CMOS switches, highlighted in green. The lower switch is flipped vertically compared to the upper switch.
\n
Removing the metal layers reveals the underlying silicon with a layer of polysilicon wiring on top.\nThe doped silicon regions show up as dark outlines.\nI\'ve drawn the polysilicon in green; it forms a transistor (brighter green) when it crosses doped silicon.\nThe metal ground and power lines are shown in blue and red, respectively, with other metal wiring in purple.\nThe black dots are vias between layers.\nNote how metal wiring (purple) and polysilicon wiring (green) are combined to route signals within\nthe cell.\nAlthough this standard cell is complicated, the important thing is that it only needs to be designed once.\nThe standard cells for different functions are all designed to have the same width, so the cells can be arranged in\ncolumns, snapped together like Lego bricks.
\n
A diagram showing the silicon for a standard-cell switch. The polysilicon is shown in green. The bottom metal is shown in blue, red, and purple.
\n
To summarize, this switch circuit allows the input to be connected to the output or disconnected, controlled by the select signal.\nThis switch is more complicated than the earlier schematic because it includes two inverters to amplify\nthe signal.\nThe data input and the two select lines are connected to the polysilicon (green); the cell is designed so\nthese connections can be made on either side.\nAt the top, the input goes through a standard two-transistor inverter.\nThe lower left has two transistors, combining the NMOS half of an inverter with the NMOS half of the switch.\nA similar circuit on the right combines the PMOS part of an inverter and switch.\nHowever, because PMOS transistors are weaker, this part of the circuit is duplicated.
\n
A multiplexer is constructed by combining multiple switches, one for each input.\nTurning on one switch will select the corresponding input.\nFor instance, a four-to-one multiplexer has four switches, so it can select one of the four inputs.
\n
A four-way multiplexer constructed from CMOS switches and individual transistors.
\n
The schematic above shows a hypothetical multiplexer with four inputs.\nOne optimization is that if an input is always 0, the PMOS transistor can be omitted. Likewise,\nif an input is always 1, the NMOS transistor can be omitted.\nOne set of select lines is activated at a time to select the corresponding input.\nThe pink circuit selects 1,\ngreen selects input A, yellow selects input B, and blue selects 0.\nThe multiplexers in the 386 are similar, but have more inputs.
\n
The diagram below shows how much circuitry is devoted to multiplexers in this block of standard cells.\nThe green, purple, and red cells correspond to the multiplexers driving the three register control\noutputs.\nThe yellow cells are inverters that generate the inverted control signals for the CMOS switches.\nThis diagram also shows how the automatic layout of cells results in a layout that appears random.
\n
A block of standard-cell logic with multiplexers highlighted. The metal and polysilicon layers were removed for this photo, revealing the silicon transistors.
\n
The misplaced transistor
\n
The idea of standard-cell logic is that standardized cells are arranged in columns.\nThe space between the cells is the "routing channel", holding the wiring that links the cells.\nThe 386 circuitry follows this layout, except for one single transistor, sitting between two columns\nof cells.
\n
The "misplaced" transistor, indicated by the arrow. The irregular green regions are oxide that was incompletely removed.
\n
I wrote some software tools to help me analyze the standard cells. Unfortunately, my tools\nassumed that all the cells were in columns, so this one wayward transistor caused me considerable inconvenience.
\n
The transistor turns out to be a PMOS transistor, pulling a signal high as part of a multiplexer.\nBut why is this transistor out of place?\nMy hypothesis is that the transistor is a bug fix.\nRegenerating the cell layout was very costly, taking many hours on an IBM mainframe computer.\nPresumably, someone found that they could just stick the necessary transistor into an unused spot in the\nrouting channel, manually add the necessary wiring, and avoid the delay of regenerating all the cells.
\n
The fake inverter
\n
The simplest CMOS gate is the inverter, with an NMOS transistor to pull the output low and a\nPMOS transistor to pull the output high.\nThe standard cell circuitry that I examined contains over a hundred inverters of various\nsizes.\n(Performance is improved by using inverters that aren\'t too small but also aren\'t\nlarger than necessary for a particular circuit. Thus, the standard cell library includes inverters of multiple sizes.)
\n
The image below shows a medium-sized standard-cell inverter under the microscope.\nFor this image, I removed the two metal layers with acid to show the underlying polysilicon\n(bright green) and silicon (gray).\nThe quality of this image is\npoor—it is difficult to remove the metal without destroying the polysilicon—but the diagram below\nshould clarify the circuit.\nThe inverter has two transistors: a PMOS transistor connected to +5 volts to pull the output high when\nthe input is 0, and an NMOS transistor connected to ground to pull the output low when the input is 1.\n(The PMOS transistor needs to be larger because PMOS transistors don\'t function as well as NMOS transistors due to\nsilicon physics.)
\n
An inverter as seen on the die. The corresponding standard cell is shown below.
\n
The polysilicon input line plays a key role: where it crosses the doped silicon, a transistor gate is\nformed.\nTo make the standard cell more flexible, the input to the inverter\ncan be connected on either the left or the right; in this case, the input\nis connected on the right and there is no connection on the left.\nThe inverter\'s output can be taken from the polysilicon on the upper left or the right, but in this case, it\nis taken from the upper metal layer (not shown).\nThe power, ground, and output lines are in the lower metal layer, which I have represented by\nthe thin red, blue, and yellow lines. The black circles are connections between the metal layer and\nthe underlying silicon.
\n
This inverter appears dozens of times in the circuitry.\nHowever, I came across a few inverters that didn\'t make sense. The problem was\nthat the inverter\'s output was connected to the output of a multiplexer.\nSince an inverter is either on or off, its value would clobber the output of the multiplexer.
4
\nThis didn\'t make any sense.\nI double- and triple-checked the wiring to make sure I hadn\'t messed up.\nAfter more investigation, I found another problem: the input to a "bad" inverter didn\'t make sense\neither. The input consisted of two signals shorted together, which doesn\'t work.
\n
Finally, I realized what was going on. A "bad inverter" has the exact silicon layout of an inverter,\nbut it wasn\'t an inverter: it was independent NMOS and PMOS transistors with separate inputs.\nNow it all made sense.\nWith two inputs, the input signals were independent, not shorted together.\nAnd since the transistors were controlled separately, the NMOS transistor could pull the output\nlow in some circumstances, the PMOS transistor could pull the output high in other circumstances,\nor both transistors could be off, allowing the multiplexer\'s output to be used undisturbed.\nIn other words, the "inverter" was just two more cases for the multiplexer.
\n
The "bad" inverter. (Image is flipped vertically for comparison with the previous inverter.)
\n
If you compare the "bad inverter" cell below with the previous cell, they look
almost
the same, but\nthere are subtle differences.\nFirst, the gates of the two transistors are connected in the real inverter, but disconnected\nby a small gap in the transistor pair.\nI\'ve indicated this gap in the photo above; it is hard to tell if the gap is real or just an imaging\nartifact, so I didn\'t spot it.\nThe second difference is that the "fake" inverter has two input connections, one to each transistor,\nwhile the inverter has a single input connection.\nUnfortunately, I assumed that the two connections were just a trick to route the signal across\nthe inverter without requiring an extra wire.\nIn total, this cell was used 32 times as a real inverter and 9 times\nas independent transistors.
\n
Conclusions
\n
Standard cell logic and automatic place and route have a long history before the 386,\nback to the early 1970s, so this isn\'t an Intel invention.
5
\nNonetheless, the 386 team deserves the credit for deciding to use this technology at a time when it\nwas a risky decision.\nThey needed to develop custom software for their placing and routing needs, so this wasn\'t a trivial undertaking.\nThis choice paid off and they completed the 386 ahead of schedule.\nThe 386 ended up being a huge success for Intel, moving the x86 architecture to 32 bits and defining the dominant computer\narchitecture for the rest of the 20th century.
\n
If you\'re interested in standard cell logic, I also wrote about
standard cell logic in an IBM chip
.\nI plan to write more about the 386, so \nfollow me on\n
Mastodon
,
Bluesky
,\nor RSS for updates.\nThanks to Pat Gelsinger and Roxanne Koester for providing helpful papers.
\n
For more on the 386 and other chips, follow me on\nMastodon (
@kenshirriff@oldbytes.space
),\nBluesky (
@righto.com
),\nor
RSS
.  (I\'ve given up on Twitter.)\nIf you want to read more about the 386, I\'ve written about the
clock pin
,\n
prefetch queue
,
die versions
,
packaging
, and
I/O circuits
.
\n
Notes and references
\n
\n
\n
\n
The decision to use automatic place and route is described on page 13 of the
Intel 386 Microprocessor Design and Development Oral History Panel
, a very interesting document on the 386 with discussion from\nsome of the people involved in its development.
↩
\n
\n
\n
Multiplexers often take a binary control signal to select the desired input.\nFor instance, an 8-to-1 multiplexer selects one of 8 inputs, so a 3-bit control signal\ncan specify the desired input.\nThe 386\'s multiplexers use a different approach with one control signal per input.\nOne of the 8 control signals is activated to select the desired input.\nThis approach is called a "one-hot encoding" since one control line is activated (hot)\nat a time.
↩
\n
\n
\n
Some chips, such as the MOS Technology 6502 processor, are built with NMOS technology, without PMOS transistors.\nMultiplexers in the 6502 use a single NMOS transistor, rather than the two transistors in the CMOS switch.\nHowever, the performance of the switch is worse.
↩
\n
\n
\n
One very common circuit in the 386 is a latch constructed from an inverter loop and a switch/multiplexer.\nThe inverter\'s output and the switch\'s output are connected together.\nThe trick, however, is that the inverter is constructed from special weak transistors.\nWhen the switch is disabled, the inverter\'s weak output is sufficient to drive the loop.\nBut to write a value into the latch, the switch is enabled and its output overpowers the weak\ninverter.
\n
The point of this is that there
are
circuits where an inverter and a multiplexer have their\noutputs connected. However, the inverter must be constructed with special weak transistors, which is not the situation\nthat I\'m discussing.
↩
\n
\n
\n
I\'ll provide more history on standard cells in this footnote.\n RCA
patented
a bipolar standard cell in 1971,\n but this was a fixed arrangement of transistors and resistors, more of a gate array than a modern\n standard cell.\n Bell Labs researched standard cell layout techniques in the early 1970s, calling them Polycells, including\n a
1973 paper
by Brian Kernighan.\n By 1979,
A Guide to LSI Implementation
discussed the standard cell approach and\n it was described as well-known in
this patent application
.\n Even so,
Electronics
called these design methods "futuristic" in 1980.
\n
Standard cells became popular in the mid-1980s as faster computers and improved design software made\n it practical to produce semi-custom designs that used standard cells.\n Standard cells made it to the cover of
Digital Design
in August 1985, and the article inside described numerous vendors and products.\n Companies like
Zymos
and
VLSI Technology
(VTI) focused on standard cells.\n Traditional companies such as
Texas Instruments
, NCR, GE/RCA,
Fairchild
, Harris,
ITT
, and Thomson introduced lines of standard cell products in\n the mid-1980s.\n
\n
↩
\n
\n
\n
'}

---

*抓取时间: 2026-02-05 12:51:49*
