# Cursed circuits #4: PLL frequency multiplier

**来源:** https://lcamtuf.substack.com
**链接:** https://lcamtuf.substack.com/p/cursed-circuits-4-pll-frequency-multiplier
**日期:** Fri, 26 Dec 2025 17:47:58 GMT

---

[![lcamtuf’s thing](https://substackcdn.com/image/fetch/$s_!WvGP!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F57b73d90-d717-4de9-bfb7-30a0f2913607_400x400.png)](/)

# [lcamtuf’s thing](/)

SubscribeSign in

# Cursed circuits #4: PLL frequency multiplier

### How do you turn 1 MHz into 100 MHz? With magic, of course.

Dec 26, 2025

20

1

Share

Welcome to another installment of _Cursed Circuits._ My goal for the series is to highlight a small collection of common yet mind-bending circuits that must’ve taken a stroke of genius to invent, but that are usually presented on the internet without explaining how or why they work.

In today’s episode, let’s have a look at a phase-locked loop clock multiplier: a circuit that, among other things, can take a 20 MHz timing signal produced by a quartz crystal and turn it into a perfectly-synchronized computer clock that’s running at 500 MHz, 3 GHz, or any other frequency of your choice.

### A primer on latches

To understand the PLL frequency multiplier, it’s probably good to cover latches first. A latch is a fundamental data-storage circuit capable of holding a single bit. The simplest variant is the set-reset (S-R) latch, which can be constructed from basic logic gates in a couple of ways. Perhaps the most intuitive layout is the following three-gate approach:

[![](https://substackcdn.com/image/fetch/$s_!Zsfy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa98c8dbb-0c84-4d12-9974-2e89996f9e42_2000x700.jpeg)](https://substackcdn.com/image/fetch/$s_!Zsfy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa98c8dbb-0c84-4d12-9974-2e89996f9e42_2000x700.jpeg)_A three-gate S-R latch._

To analyze the circuit, let’s assume that the “set” signal (S) is high and the “reset” signal (R) is low. In this case, the output of the OR gate is a logical one regardless of the looped-back signal present on the gate’s other terminal; this produces a logical one on the first input of the downstream AND gate. The other input of that AND gate is also equal to one, because it’s just an inverted copy of R = 0. All in all, in the S = 1 and R = 0 scenario, both inputs of the AND gate are high; therefore, so is the signal on the circuit’s output leg (Q).

Next, let’s imagine that S transitions to a logical zero. This puts one of the OR inputs at zero volts, but the other is still high because it’s the looped-back output signal Q. The circuit is latched: it keeps outputting the same voltage as before, even though the original driving signal is gone.

The only thing that can break the cycle if the “reset” line is pulled high. This causes one of the AND input to go low, thus forcing the output signal to zero and breaking the loop that kept the OR gate latched. From now on, the output remains low even if R returns to zero volts.

This two-lever latch can be fashioned into a more practical data (D) latch, which stores an arbitrary input bit supplied on the data line whenever the enable signal (E) is high, and keeps it when E is low:

[![](https://substackcdn.com/image/fetch/$s_!67OG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc87bdb9a-f161-4b56-a766-0392be466f2b_1785x441.jpeg)](https://substackcdn.com/image/fetch/$s_!67OG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc87bdb9a-f161-4b56-a766-0392be466f2b_1785x441.jpeg)_A conceptual illustration of a D latch._

In this circuit, a pair of input-side AND gates ensures that when E is at zero volts, the underlying S and R lines remain low regardless of the value presented on the data line. Conversely, if enable is high, the gates pass through a logical one either to the S line (if D is high) or the R line (if D is low).

Going further down that path, we can turn a D latch into a clocked D flip-flop, which stores a bit of data on the rising edge of the clock signal:

[![](https://substackcdn.com/image/fetch/$s_!uWN2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01325f81-7dfc-4aab-8a2d-2844793910fb_2000x578.jpeg)](https://substackcdn.com/image/fetch/$s_!uWN2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01325f81-7dfc-4aab-8a2d-2844793910fb_2000x578.jpeg)_A clocked D flip-flop._

In this circuit, the latch on the left passes through the input data when the clock signal is low, or keeps the previous value if the clock is high. The latch on the right works the opposite way: it passes through the output from the first latch if the clock is high or holds the last value otherwise.

In effect, the value on the input line appears to propagate to the circuit’s output only during the 0 → 1 transition (rising edge) of the clock signal. More to the point, the propagation happens in two stages and there is never a direct signal path between D and Q, which prevents the cell from misbehaving if Q is looped back onto D.

### Phase error detector

Once we have a clocked D flip-flop — and make a trivial modification to furnish it with an additional reset input — we can build a digital phase error detector circuit. One type of such a detector is shown below:

[![](https://substackcdn.com/image/fetch/$s_!N6b_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F911b9921-98f1-470d-ae8d-c716e5282520_2000x1050.jpeg)](https://substackcdn.com/image/fetch/$s_!N6b_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F911b9921-98f1-470d-ae8d-c716e5282520_2000x1050.jpeg)_A simple phase error detector._

The purpose of the detector is to compare clock signal B to a reference clock provided on input A. If the positive edge on input A arrives before a positive edge on input B, the output of the upper flip-flop (_Q A_) goes high before the output of the bottom flip-flop (_Q B_); this signals that clock B is running too slow. Conversely, if the edge on B arrives before the edge on A, the circuit generates a complementary output indicating that B is running too fast. As soon as both flip-flops are latched high — i.e., after encountering a positive edge on whichever of the two clock signals is running slower — the circuit is reset.

The following plot shows the behavior of the circuit when the clock supplied on the B leg is running too slow (left) or too fast (right) in relation to the reference signal on leg A:

[![](https://substackcdn.com/image/fetch/$s_!Z-Zh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb626b761-7d03-48da-89c6-dc9a061decc0_2813x1875.jpeg)](https://substackcdn.com/image/fetch/$s_!Z-Zh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb626b761-7d03-48da-89c6-dc9a061decc0_2813x1875.jpeg)_The basic behavior of the phase error detector circuit._

In effect, the detector generates longer pulses on the output labeled P if the analyzed clock signal is lagging behind the reference; and longer pulses on the other output (R) if the signal is rushing ahead.

It’s worth noting that the frequencies in the plot are not cherry-picked; although a rigorous mathematical analysis of phase detectors is fairly involved and they have transient failure modes, the following simulation shows that happens if the frequency B is changing continuously:

[![](https://substackcdn.com/image/fetch/$s_!nqfK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ec45e92-4453-4adc-9873-ffd4ae9ed319_2813x1875.png)](https://substackcdn.com/image/fetch/$s_!nqfK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ec45e92-4453-4adc-9873-ffd4ae9ed319_2813x1875.png)_A continuously-variable-frequency variant of the simulation._

### PLL loop

The detector can serve as the fundamental building block of a circuit known as a phase-locked loop. Despite the name, the main forte of phase-locked loops is that they can generate output frequencies that match an input signal of some sort, even if that signal is noisy or faint:

[![](https://substackcdn.com/image/fetch/$s_!W2FF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8c679cc-be02-499e-b81d-5ecfa647f7cc_2000x650.jpeg)](https://substackcdn.com/image/fetch/$s_!W2FF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8c679cc-be02-499e-b81d-5ecfa647f7cc_2000x650.jpeg)_The basic architecture of a digital PLL._

The output stage of the PLL is a [voltage-controlled oscillator (VCO)](https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator). We’ve briefly covered VCOs before: they generate an output waveform with a frequency proportional to the supplied input voltage.

The voltage for the VCO is selected by a simple switched capacitor section in the middle; the section has two digital inputs, marked “+” and “-”. Supplying a digital signal on the “+” input turns on a high-side transistor that gradually charges the output capacitor to a higher voltage, thus increasing the output frequency of the VCO. Supplying a signal on the “-” leg turns on a low-side transistor, slowly discharges the capacitor, and achieves the opposite effect. 

The last part of the circuit is the now-familiar phase error detector; it compares the externally-supplied clock to the looped-back output from the VCO. The detector outputs long pulses on the P output if the VCO frequency is lower than the reference clock, or on the R output if the VCO is running too fast. In doing so, the circuit adjusts the capacitor voltage and nudges the VCO to match the frequency and phase of the input waveform.

### Toward the frequency multiplier

So far, we have a circuit that synchronizes the VCO with an external clock; that has some uses in communications, but doesn’t seem all that interesting on its own. To take it to the next level, we need to add a small but ingenious tweak:

[![](https://substackcdn.com/image/fetch/$s_!5hXD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92b34198-5799-4bab-abc8-67dbbb509450_2000x800.jpeg)](https://substackcdn.com/image/fetch/$s_!5hXD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92b34198-5799-4bab-abc8-67dbbb509450_2000x800.jpeg)_A PLL-based frequency multiplier._

In this new circuit, we incorporated a frequency divider in the feedback loop. A frequency divider is not a complicated concept; most simply, it can be a binary counter (e.g., 74HC393) that advances by one with every cycle of the input clock. For a three-bit counter, the outputs will be:

\\(\begin{array}{| c | c | c | c | c |} \hline \textbf{Clock cycle #} & \boldsymbol{Q_2} & \boldsymbol{Q_1} & \boldsymbol{Q_0} \\\ \hline 0 & 0 & 0 & 0 \\\ 1 & 0 & 0 & 1 \\\ 2 & 0 & 1 & 0 \\\ 3 & 0 & 1 & 1 \\\ 4 & 1 & 0 & 0 \\\ 5 & 1 & 0 & 1 \\\ 6 & 1 & 1 & 0 \\\ 7 & 1 & 1 & 1 \\\ \hline \end{array}\\)

Note that the counter produces a square wave with half the clock frequency on the LSB output (_Q 0_); with one-fourth the frequency on the second output (Q1); and with one-eighth on the MSB leg (Q2).

If we choose _Q 0_ for the divider, the phase error detector will be presented with a looped-back signal that’s equal to one half the running frequency of the VCO; it will then work to get the VCO frequency high enough so that the divided signal matches the reference clock. This will cause the VCO to run exactly twice as fast — and yet, precisely in lockstep with the input clock. 

_👉 Previous installments:[one](https://lcamtuf.substack.com/p/cursed-circuits-charge-pump-voltage), [two](https://lcamtuf.substack.com/p/cursed-circuits-2-switched-capacitor), [three](https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics). If you like the content, please subscribe. I’m not selling anything; it’s just a good way to stay in touch with the authors you like._

Subscribe

20

1

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![wubbles's avatar](https://substackcdn.com/image/fetch/$s_!g_Yo!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3b5640d-92b9-4ee3-9f9f-3f8dc7542a0c_400x400.jpeg)](https://substack.com/profile/4271208-wubbles?utm_source=comment)

[wubbles](https://substack.com/profile/4271208-wubbles?utm_source=substack-feed-item)

[Dec 26](https://lcamtuf.substack.com/p/cursed-circuits-4-pll-frequency-multiplier/comment/191937364 "Dec 26, 2025, 7:48 PM")

One of the really strange facts: if instead of a phase comparator we put in an xor gate and have the right filter, the PLL still works!

ReplyShare

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 lcamtuf · [Publisher Privacy](https://lcamtuf.substack.com/privacy)

Substack · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
