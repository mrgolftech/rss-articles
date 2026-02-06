# Cursed circuits #3: true mathematics

**来源:** https://lcamtuf.substack.com
**链接:** https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics
**日期:** Mon, 22 Dec 2025 02:38:09 GMT

---

[![lcamtuf’s thing](https://substackcdn.com/image/fetch/$s_!WvGP!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F57b73d90-d717-4de9-bfb7-30a0f2913607_400x400.png)](/)

# [lcamtuf’s thing](/)

SubscribeSign in

# Cursed circuits #3: true mathematics

### Op-amp arithmetics -explained in a more accessible way

Dec 22, 2025

20

15

1

Share

In the previous installments of _Cursed Circuits_ , we looked at two switched capacitor circuits: the [voltage halver](https://lcamtuf.substack.com/p/cursed-circuits-charge-pump-voltage) and the [capacitor lowpass filter](https://lcamtuf.substack.com/p/cursed-circuits-2-switched-capacitor).

In today’s episode, I’d like to talk about the use of operational amplifiers to do something other than amplification: to solve analog math. Analog computing at a scale is wildly impractical because errors tend to accumulate every step along the way; nevertheless, individual techniques find a number of specialized uses, perhaps most prominently in [analog-to-digital converters](https://lcamtuf.substack.com/p/dacs-and-adcs-or-there-and-back-again). Let’s have a look at how it’s done.

_The following assumes familiarity with[core concepts in electronic circuits](https://lcamtuf.substack.com/p/primer-core-concepts-in-electronic) and with the [fundamentals of signal amplification](https://lcamtuf.substack.com/p/the-basics-of-signal-amplification). If you need a refresher, start with the two linked articles first._

### Op-amps at a glance

Before we get to less obvious circuits, let’s start with a brief recap: operational amplifiers are to analog electronics what logic gates are to digital logic. They are simple but remarkably versatile building blocks that let you accomplish far more than appears possible at first blush.

Unfortunately, in introductory texts, their operation is often explained in confusing ways. All that an op-amp does is taking two input voltages — _V in-_ (“inverting input”) and _V in+_ (“non-inverting input”) — and then outputting a voltage that’s equal to the difference between the two, amplified by a huge factor (_A OL_, often 100,000 or more) and then referenced to the midpoint of the supply (_V mid_). You can write it the following way:

\\(V_{out} = V_{mid} + (V_{in+} - V_{in-}) \cdot A_{OL}\\)

That’s all the chip does. Because the gain is massive, there is a very narrow linear region near _V in-_ = _V in+_; a difference greater than a couple of microvolts will send the output toward one of the supply rails. The chip doesn’t care about the absolute value of _V in-_ or _V in+_ it can’t “see” any external components you connect to it, and its internal gain can’t be changed.

To show the versatility of the component, we can have a quick look at the following circuit that you might be already familiar with — a non-inverting amplifier:

[![](https://substackcdn.com/image/fetch/$s_!ELK3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbac0ada9-3028-4bf9-a258-c0a11688efde_2000x1177.jpeg)](https://substackcdn.com/image/fetch/$s_!ELK3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbac0ada9-3028-4bf9-a258-c0a11688efde_2000x1177.jpeg)_The basic non-inverting voltage amplifier._

One input of the op-amp is connected to the external signal source: _V in+ _= _V signal_. The other input is hooked up to a two-resistor voltage divider that straddles the ground and the output leg; the divider’s midpoint voltage is:

\\(V_{in-} = {R_g \over R_g + R_f} \cdot V_{out} \\)

As discussed earlier, the only way for the op-amp to output voltages other than 0 V or _V supply _is for _V in+ _to be very close to _V in-_. We can assume that we’re operating near that equilibrium point, combine the equations for the voltages on the two input legs, and write:

\\(V_{signal} \approx {R_g \over R_g + R_f } \cdot V_{out}\\)

Solving this for _V out_, we get:

\\(V_{out} \approx V_{signal} \cdot {R_g + R_f \over R_g} \approx V_{signal} \cdot (1 + {R_f \over R_g})\\)

In other words, the output voltage is the input signal amplified by a factor of _1 + R f/Rg_. We have a near-ideal single-ended voltage amplifier with a configurable gain. Again, the circuit is probably familiar to most folks dabbling in analog electronics, but it’s worth pondering that we implemented it by adding a couple of resistors to a chip that does something conceptually quite different.

_Note: there’s a bit more to op-amp lore when dealing with high-frequency signals; a more rigorous analysis of their frequency characteristics can be found in[this article](https://lcamtuf.substack.com/p/deep-dive-the-instability-of-op-amps)._

### Addition

Now that we have the basics covered, we can show that op-amps can do more than just amplify signals. The first contender is the following summing layout that differs from what’s usually covered in textbooks, but that’s well-suited for single-supply use:

[![](https://substackcdn.com/image/fetch/$s_!N-qA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa8e2a97-1a44-44fc-8724-4b6615b3a19b_2000x1225.jpeg)](https://substackcdn.com/image/fetch/$s_!N-qA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa8e2a97-1a44-44fc-8724-4b6615b3a19b_2000x1225.jpeg)_A three-way non-inverting summing amplifier._

Assuming well-behaved signal sources that can supply and sink currents, it should be pretty intuitive that the voltage on the _V in+_ leg is just an average of three input signals:

\\(V_{in+} = {V_A + V_B + V_C \over 3}\\)

For readers who are unpersuaded, we can show this from Kirchoff’s current law (KCL); the law essentially just says “what comes in must come out” — i.e., the currents flowing into and out of the three-resistor junction must balance out. If we use _V jct _to denote the voltage at the junction, then from Ohm’s law, we can write the following current equations for each resistor branch:

\\(\begin{array}{c} I_1 = {V_A - V_{jct} \over R} \\\ I_2 = {V_B - V_{jct} \over R} \\\ I_3 = {V_C - V_{jct} \over R} \\\ \end{array}\\)

Further, from KCL, we can assert that the currents must balance out: _I 1 _\+ _I 2 _\+ _I 3 _= 0 A. Combining all these equations and multiplying both sides by R, we get:

\\(V_A + V_B + V_C - 3 \cdot V_{jct} = 0 \textrm{ V}\\)

Solving for _V jct_, we get (_V A _\+ _V B_ \+ _V C_) / 3. We have a confirmation that the input-side resistor section averages the input voltages.

To be fair, the averaging portion of the circuit has a minor weakness: it depends some inputs sinking current while others source it. Some signal sources might not have that ability. That said, compared to the alternative design, it has the benefit of being more useful in single-supply circuits, so let’s stick with that.

Moving on to the op-amp section: this is just another sighting of the non-inverting amplifier. The gain of the amplifier circuit is set by the _R f_ and _R g_ resistors, and in this instance, works out to A = 1 + _R f/Rg_ = 3. In other words, the signal on the output leg is:

\\(V_{out} \approx 3 \cdot V_{in+} \approx { \cancel{3} \cdot (V_A + V_B + V_C) \over \cancel{3}} \approx V_A + V_B + V_C\\)

That looks like a sum! But it also feels like we cheated in some way: it just so happens that we could implement averaging using passive components, and then tack on an amplifier for some gain. Surely, resistor magic can’t get us much further than that?

### Subtraction

It can! The next stop is subtraction, which can be achieved with the following circuit topology:

[![](https://substackcdn.com/image/fetch/$s_!QnTs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f412f17-8062-4912-9146-8f5522be8e49_2000x1100.jpeg)](https://substackcdn.com/image/fetch/$s_!QnTs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f412f17-8062-4912-9146-8f5522be8e49_2000x1100.jpeg)_A simple difference amplifier (A - B)._

We can start the analysis with the non-inverting input of the amplifier. The signal on this leg is generated by a voltage divider consisting of two identical resistances connected in series between VA and the ground. In other words, the voltage here is _V in+ = ½ · VA._

The inverting input is a voltage divider too, except it produces a voltage that’s halfway between _V B_ and _V out_: _V in-_ = ½ · (_V_ B \+ _V out_). 

As with any op-amp topology, linear operation can happen only when _V in- ≈ Vin+_. In other words, we can assert that for the circuit to function, the following must be true:

\\(½ \cdot V_A \approx ½ \cdot (V_B + V_{out})\\)

We can cancel out the repeated ½ term on both sides, and then reorder the equation to:

\\(V_{out} \approx V_A - V_B\\)

Neat: that’s precisely what we’ve been trying to do.

To be fair, not all is roses: in a single-supply circuit, an op-amp can’t output negative voltages, so the topology we’ve just analyzed works only if _V A > VB_; otherwise, _V out _just hits the lower rail and stays there until the input voltages change.

To accommodate use cases where _V A < VB_, we’d need to use a higher output voltage as the “zero” point (_V zero_). For example, if _V zero _= 2.5 V, then a computed difference of -1 V could be represented by _V out _= _V zero _\- 1 V = 1.5 V; in the same vein, a difference of +2 V could correspond to _V out _= 4.5 V.

To do this, we just need to disconnect the bottom voltage divider from the ground and replace 0 V with a fixed “zero” voltage of our choice. This changes the equation for the positive leg to _V in+_ = ½ · (_V_ A \+ _V zero_). The overall equilibrium condition becomes:

\\(½ \cdot ( V_A + V_{zero}) \approx ½ \cdot (V_B + V_{out})\\)

After tidying up and solving for the output signal, we get:

\\(V_{out} \approx V_{zero} + (V_A - V_B)\\)

A common choice of a reference point would be the midpoint of the supply (_V mid_ = ½ · _V supply_).

### Multiplication and division

The concept of analog computation can be also extended to multiplication and division. The most common and mildly mind-bending approach hinges on the fact that any positive number can be rewritten as a constant base _n_ raised to some power; for example, 8 can be written as 23, while 42 is approximately 25.3924. 

From the basic properties of exponentiation, it’s easy to show that _n a · nb _is the same as _n a+b_; it follows that if we have two numbers represented as exponents of a common base, we can reduce the problem of multiplication to the addition of these exponents.

We already know how to build a summing circuit, so all we’re missing is a way to convert a number to an exponent. We don’t really care what base we’re using, as long as the base remains constant over time.

This brings us to the following design:

[![](https://substackcdn.com/image/fetch/$s_!v48I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2dfc829-5c95-4bdd-9136-13cae83e63f8_2000x682.jpeg)](https://substackcdn.com/image/fetch/$s_!v48I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2dfc829-5c95-4bdd-9136-13cae83e63f8_2000x682.jpeg)_A logarithmic amplifier._

As before, the linear equilibrium condition requires _V in- ≈ Vin+. _Let’s assume that the initial input voltage is about equal to _V zero_; in this case, the output settles in the same vicinity.

Next, let’s analyze what would happen if the input voltage increased by _v s_ _=_ 100 mV. In such a scenario, for the op-amp to stay at an equilibrium of _V in- ≈ Vin+_, we would need a sufficient current to flow through the resistor to create a 100 mV voltage drop:

\\(I_R = {v_{s} \over R}\\)

The op-amp has a very high input impedance, so the current must flow through the diode; if it doesn’t, that’d move the circuit toward a condition of _V_ in- ≫ _V_ in+, which would cause _V out_ to move toward the negative supply rail. That would forward-bias the diode and thus motivate it to conduct better. In other words, the circuit has an automatic mechanism that coerces the diode to admit the current matching _I_ R, and the amount of convincing is reflected in how much the output voltage has been reduced from the midpoint. We can denote this relative shift as _v o_.

From an [earlier feature about diodes](https://lcamtuf.substack.com/p/things-you-can-do-with-diodes), you might recall that although the relationship between the applied diode voltage and the resulting current is complicated, there is an initial region where the component’s V-I curve is exponential. In the following plot for a 1N4148 diode, this property holds up for currents up to about 1 mA:

[![](https://substackcdn.com/image/fetch/$s_!1YT_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc911561-42ea-431b-b5c9-a1bdd10c2eaa_2969x1250.jpeg)](https://substackcdn.com/image/fetch/$s_!1YT_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc911561-42ea-431b-b5c9-a1bdd10c2eaa_2969x1250.jpeg)_V-I curve for 1N4148, normal (left) and log scale current (right). By author._

In other words, if the input resistor is large enough (10 kΩ or so), we can say that _v o_ will be dictated by the magnitude of an exponent of some constant base _n_ that yields the correct diode current _: I D = nvₒ_.

We also know that the current that must flow through the diode is proportional to the shift in the input signal (_v s_) divided by _R._ This means that we’ve accomplished the number-to-exponent conversion between _v s _and _v o_. Or, in the mathematical parlance, we’ve calculated a logarithm.

To implement multiplication, we need two logarithmic converters on the input side, a summing amplifier to add the exponents, and then an exponential converter that goes from the summed exponent back to a normal value. That last part can be accomplished by switching the location of the diode and the resistor in the log converter circuit we already have.

### Integration

Integration is just a fancy word for summing values over time; if you want to sound posh, you can say that a bucket in your backyard “integrates” rainfall over the duration of a storm.

Although integration is important in calculus, analog integrators have down-to-earth uses too. For example, the circuits can convert square waves into triangular shapes that are useful in electronic musical instruments. The circuit’s ability to produce very linear up and down slopes also comes in handy in [slope-based and delta-sigma ADCs](https://lcamtuf.substack.com/p/dacs-and-adcs-or-there-and-back-again).

The simplest, textbook integrator is shown below:

[![](https://substackcdn.com/image/fetch/$s_!-t1B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95fd2219-a871-4cf7-a1ac-0fc9a54f2912_2000x682.jpeg)](https://substackcdn.com/image/fetch/$s_!-t1B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95fd2219-a871-4cf7-a1ac-0fc9a54f2912_2000x682.jpeg)_Basic integrator._

Once again, we can note that the linear operation condition is _V in- ≈ Vin+. _Further, let’s assume that the input signal is equal to _V zero _and the capacitor is discharged, so both op-amp inputs and the output are at about the midpoint.

Next, similarly to the analysis we’ve done for the log amplifier, let’s assume that the input signal shifts up by _v s =_ 100 mV. For the op-amp to stay at an equilibrium, we would need a sufficient current to flow through the resistor to create a 100 mV voltage drop: _I R = vs/R._

The only possible path for this current is the capacitor; a capacitor doesn’t admit steady currents, but it will allow the movement of charges during the charging process, which will kick off when the op-amp’s output voltage begins to drop; this drop causes a voltage differential appears across the capacitor’s terminals.

From the fundamental capacitor equation, charging the capacitor with a constant current _I R_ for a time _t_ will produce the following voltage across its terminals:

\\(V_{cap} = {I_R \cdot t \over C} = {v_s \cdot t \over RC}\\)

To keep _V in-_ steady, the voltage to which the capacitor gets charged must be accounted for by a directionally opposite shift of the output voltage (_v o_). The shift will persist after _V signal _returns to the midpoint, because with no charging or discharging current, the capacitor just retains charge. The shift can be undone if _v s _swings the other way around. 

From the earlier formula for the capacitor voltage, it should be clear that the circuit keeps a sum of (midpoint-relative) input voltages summed over time.

The textbook integrator we’ve been working with has an inverted output: _V out _moves down whenever _V signal _moves up; this makes it somewhat clunky to use in single-supply applications. The problem can be addressed in a couple of intuitive ways, but a particularly efficient — if positively cursed — solution is shown below:

[![](https://substackcdn.com/image/fetch/$s_!eTfw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d8d61dd-aabb-4a58-a723-420459983405_2000x1193.jpeg)](https://substackcdn.com/image/fetch/$s_!eTfw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d8d61dd-aabb-4a58-a723-420459983405_2000x1193.jpeg)_The single-supply, non-inverting integrator._

As in all other cases, the prerequisite for linear operation is _V in-_ ≈ _V in+_. 

We can start the analysis with the two-resistor divider on the top: it simply ensures that _V in- _is equal to ½ · _V out_. As the bottom portion of the circuit, the instantaneous voltage on the non-inverting input is decided by the capacitor’s charge state (_V cap_). The bottom resistors will influence the charge of the capacitor over time, but if we’re living in the moment, we can combine the equations and write the following equilibrium rule:

\\(V_{cap} \approx ½ \cdot V_{out}\\)

Equivalently, we can say that _V out ≈ _2 · _V cap_.

We have established that _V out_ is equal to twice the value of _V cap_, but if so, the resistor on the bottom right is subjected to a voltage differential between these two points (always equal to _V cap_). From Ohm’s law, the resistor will admit the following current:

\\(I_1 = {V_{cap} \over R}\\)

If the input voltage is zero, the neighboring resistor to the left is subjected to the same voltage differential, so the current flowing into the junction (_I 1_) is the same as the current flowing out (_I 2_). With the currents in balance, the capacitor holds its previous charge and the output voltage doesn’t change.

That said, if the input voltage (_V signal_) is non-zero, the voltage differential across the terminals of the resistor on the left is different, and the formula for _I 2_ becomes:

\\(I_2 = {V_{cap} -V_{signal} \over R}\\)

In this case, there is a non-zero balance of the currents flowing in and out via the resistors:

\\(I_{net} = I_1 - I_2 = {\cancel{V_{cap}} -\cancel{V_{cap}} + V_{signal} \over R} = {V_{signal} \over R}\\)

This current is flowing in via the resistor on the right but not flowing out via the resistor on the left, so it necessarily charges the capacitor. Note that the capacitor charging current is independent of _V cap_; it remains constant as long as the input voltage is constant too.

As before, from the fundamental capacitor equation (V = I·t/C), we can tell that a constant charging current will cause the voltage on the output leg to ramp up in a straight line. Of course, this will come to an end once we hit the output voltage limit of the amplifier. To reset the circuit, we’d need to short the terminals of the capacitor.

_👉 For another installment of the series,[click here](https://lcamtuf.substack.com/p/cursed-circuits-4-pll-frequency-multiplier)._

Subscribe

 _If you enjoy the content, please subscribe. I don’t sell anything; it’s just a good way to stay in touch with the authors you like._

20

15

1

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![lcamtuf's avatar](https://substackcdn.com/image/fetch/$s_!koIn!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F160026b1-f333-4244-b8dc-5ca8c437a0b4_400x400.jpeg)](https://substack.com/profile/92541588-lcamtuf?utm_source=comment)

[lcamtuf](https://substack.com/profile/92541588-lcamtuf?utm_source=substack-feed-item)

[Dec 23](https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics/comment/190836101 "Dec 23, 2025, 7:39 AM")Edited

Pinned

Just some meta commentary for what follows here: I make mistakes every now and then and I always welcome corrections, questions, and friendly banter from subscribers. That said, in this instance, after a spirited exchange in the comments section below, I do stand by the article :-)

The TL;DR is that a subscriber expressed concern that the non-inverting summing amplifier presented in the circuit may not work correctly. I think that in the general case, it should. If you're looking for independent references to the circuit, see the relevant section in <https://www.ti.com/lit/an/snla140d/snla140d.pdf>

Now, there is an important distinction between the non-inverting architecture presented in the article and the "textbook" inverting summing amplifier that you will, for example, find in "The Art of Electronics". The distinction is that in the non-inverting design, the current is necessarily flowing in through some of the input legs and flowing out through others. This can cause problems if one of the sources can only source currents, but not sink any (e.g., if it includes a series diode). The inverting variant, on the other hand, keeps the junction point near 0 V. Because of this, for positive input voltages, all the currents are flowing in the same direction and the drive constraint is eased. 

In other words: I agree that in some situations, the inverting architecture may be preferred. That said, I believe the circuit presented in the article is reasonable. I did not use the inverting layout because it works as advertised only in a dual-supply circuit. The inverting summing amplifier *can* be converted to to single-supply operation, but that necessarily involves putting the summing point at a higher voltage and breaks the symmetry with the difference amplifier.

ReplyShare

[![Noah Fect's avatar](https://substackcdn.com/image/fetch/$s_!wdf9!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b134dc9-6cdf-4de1-8bd9-42efabd79095_144x144.png)](https://substack.com/profile/25598810-noah-fect?utm_source=comment)

[Noah Fect](https://substack.com/profile/25598810-noah-fect?utm_source=substack-feed-item)

[Dec 22](https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics/comment/190432053 "Dec 22, 2025, 3:10 AM")

Your adder might not work the way you expect. Those three input resistors normally drive the virtual ground at the - input. 

ReplyShare

[7 replies by lcamtuf and others](https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics/comment/190432053)

[13 more comments...](https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics/comments)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 lcamtuf · [Publisher Privacy](https://lcamtuf.substack.com/privacy)

Substack · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
