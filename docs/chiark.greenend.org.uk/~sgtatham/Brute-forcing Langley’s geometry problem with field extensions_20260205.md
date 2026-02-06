# Brute-forcing Langley’s geometry problem with field extensions

**来源:** https://chiark.greenend.org.uk/~sgtatham
**链接:** https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/adventitious/
**日期:** 2025-07-18T00:00:00+00:00

---

# Brute-forcing Langleyâs geometry problem with field extensions

[Simon Tatham, 2025-07-18]

  * Introduction
  * Set the problem in the complex plane
    * How to make a triangle with three known angles
    * Make three of them and put them side by side
    * Divide two numbers to get the angle you want
    * Divide by the complex conjugate to normalise to unit length
    * Putting it all together
  * Now do it all by algebra
    * Find the minimal polynomial of _t_
    * Addition and multiplication
    * Division
    * Complex conjugate of a polynomial
    * Now do the actual calculation
  * Afterthoughts
    * What if the answer isnât nice?
    * I did twice as much work as I really needed to
    * Have I cheated?
  * Footnotes



## Introduction

[Langleyâs Adventitious Angles](https://en.wikipedia.org/wiki/Langley%27s_Adventitious_Angles) is a notoriously difficult problem in elementary geometry. The challenge is to determine the angle _Î¸_ in this diagram:

![\[start.svg\]](start.svg) Langleyâs geometry problem

Itâs relatively easy to chase angles around the diagram and get this far:

![\[more.svg\]](more.svg) All the easy bits filled in

But after this, it suddenly becomes difficult to make any more progress. Weâve filled in an expression for every angle weâve got, and everything seems to make sense: the angles in each triangle and on each straight line add up to 180Â°. But in all the angle sums involving _Î¸_ , the instances of _Î¸_ appear with opposite signs and cancel out. So each of those sums will add up to 180Â° no matter _what_ the value of _Î¸_ is â and so none of them helps us to narrow down to a single answer.

Once you reach this point, you might be tempted to wonder if there even _is_ a single answer. When a problem _doesnât_ have a unique solution, this is often what it looks like: you eliminate all but one variable, expressing everything else in terms of the remaining variable, and all your constraints seem to stay true regardless of the value of that variable. This is often the signature of a situation in which you can make an arbitrary choice of the variable, leading to a whole space of equally valid solutions.

But that canât be true here, because the locations of all the points in the plane are completely determined, at least provided you choose an initial location and size for the overall 80Â°â80Â°â20Â° isosceles triangle. Each of the two lines from a base vertex to the opposite edge is at a known angle, so thereâs only one possible place it can intersect the opposite edge. And once every point in the diagram has a unique location, thereâs no way the desired angle can have more than one value.

So one way you could âsolveâ the problem would be to construct the diagram on paper, using a protractor, as accurately as possible, and then _measure_ the target angle. Another approach would be to do the same thing in a computer, using trigonometry to calculate the _x_ and _y_ coordinates of every point â or to get a tool like GeoGebra to do the heavy lifting.

If you try that, it turns out that the angle looks like a nice round number of degrees. But you havenât _proved_ that it has that exact value: the âdraw it on paperâ method only gives you an approximate answer, up to the limits of your own ability to draw and measure precisely. And even the computer approach using trigonometry will be limited by floating-point accuracy. So all you can say after doing it this way is that it _looks as if_ the angle is exactly [this many] degrees.

In fact the problem is sometimes set with a specific rule that says âdonât use trigonometryâ, because there _is_ a solution using elementary geometry, involving a clever choice of extra construction lines to add to the figure. The Wikipedia link above shows the answer (at the time of writing) â but beware that the choice of extra construction lines depends crucially on what the starting angles are. There are variants of this problem in which the two internal lines make different angles with the base of the triangle, and for each of those variants, you might need a _different_ clever insight.

My aim in this article is to show how you can solve this problem _without_ a clever insight1Perhaps youâre wondering _why_ I might happen to be concerned with this problem and how to solve it without cleverness. Might it be because someone gave me the problem recently and I didnât manage to find the clever answer? No comment.1. The method Iâll show is hard work â hard enough that youâd surely want a computer to do the boring parts for you â but itâs systematic enough that it can handle different variants of the problem by exactly the same method, without needing a different clever construction in each case. And unlike the trigonometry approach, it _is_ able to calculate the answer in an exact manner.

## Set the problem in the complex plane

Iâll start by describing a method for solving the problem by using complex numbers to represent the locations of all the points.

In this section, I wonât worry about whether calculations are approximate or exact. You _can_ follow this procedure in an approximate way, using any programming language that has complex numbers as a built-in type; Iâll show an example in Python at the end of the section. Then, in the next section, Iâll show a technique that lets you follow the same procedure in a way that gives an exact answer.

### How to make a triangle with three known angles

Weâre going to need to construct several triangles with particular angles, so our first job is to find a way of doing that easily with complex numbers.

The simplest way I know of is to make use of the geometric result that the angle at the centre is twice the angle on a chord. That is, given any two points _A_ ,_B_ on the circumference of a circle, the angle _AOB_ (where _O_ is the centre of the circle) is twice _ACB_ , where _C_ is _any_ third point on the circleâs circumference2What if _C_ is on the opposite side of the line from _O_? In that case, you have to switch to measuring the angle at _O_ on the other side of the line, so that itâs 360Â° minus the angle shown here.2.

![\[chordangle.svg\]](chordangle.svg) Angles on a chord and at the centre

So, suppose we want to make a triangle with angles _Î±_ ,Â  _Î²_ ,Â  _Î³_. Imagine drawing the circumcircle of that triangle, so that all three of the vertices are points on the circumference. Then each of the angles of the triangle _is_ an angle on a chord, and therefore, the corresponding angle at the centre is twice that.

![\[triangle-corners.svg\]](triangle-corners.svg)

![\[triangle-centre.svg\]](triangle-centre.svg)

Angles at the centre of a triangleâs circumcircle

But this means weâve reduced the problem to finding three points at the same distance from the centre of a circle, with angles 2 _Î±_ ,Â 2 _Î²_ ,Â 2 _Î³_ at the centre between them. The simplest way to do that in the complex numbers is just to take numbers of unit magnitude, so that theyâre all on the unit circle. Itâs easiest to make one of them 1, say _A_ Â =Â 1, and then choose the other two to be the right distances away from it round the circle, in opposite directions, so youâd have _B_ Â =Â  _e_ 2 _Î³i_ and _C_ Â =Â  _e_ â2 _Î²i_ , for example (with the angles _Î²_ ,Â  _Î³_ written in radians).

### Make three of them and put them side by side

Now we know how to make triangles, letâs put some of them together to construct the points we need for the actual problem.

We donât really need the point _C_ , at the very apex of the whole triangle. All we really need is the lower quadrilateral _ABED_ , which is divided into four triangles by lines to the extra point _X_ in the middle. Three of those triangles have all known angles, so we can start by making those, and fitting them together. Then weâll have all the points of the top triangle, whose angles weâre trying to measure.

![\[quadrilateral.svg\]](quadrilateral.svg) The figure we want to construct

We begin by making the bottom triangle _ABX_. Letâs choose _X_ to be the complex number 1. Using the idea from the previous section, the angle _XBA_ is 50Â°, so we want the angle _XOA_ at the origin to be twice that. That is, we want _A_ to be a point on the unit circle, 100Â° anticlockwise from 1.

Here Iâm going to introduce a shorthand for a complex number weâre going to use a lot. All the angles in this problem are multiples of 10Â°, so instead of talking about _e_ to the power of fiddly imaginary numbers in radians, Iâm going to define _t_ to be the complex number that represents a 10Â° rotation anticlockwise. 10Â° is one 36th of a turn, so _t_ Â =Â  _e_ 2 _Ïi_ /36.

Then any angle thatâs an integer multiple of 10Â° corresponds to the corresponding integer power of _t_. For example, we want _A_ to be 100Â° around the circle from the starting point _X_ , so we just set _A_ Â =Â  _t_ 10.

Similarly, _B_ wants to be 120Â° round the circle in the _opposite_ direction from _A_ , because if the angle _XOB_ Â =Â 120Â°, then that will make the angle _XAB_ half that, which is 60Â°, which is the angle we want at _A_. So we also have _B_ Â =Â  _t_ â12.

(This arrangement of points wonât put the triangle _XAB_ with the _AB_ edge horizontal, as it is in the diagram above. But we donât care. If the whole diagram is rotated by some arbitrary angle, the angles _within_ the figure donât change, so thereâs no point going to the extra effort to put it any particular way up.)

OK, thatâs one triangle. Now we need to make a second one â letâs do the triangle _XDA_ next â and then put it in the right place relative to the first one.

Making the triangle is easy enough if we donât mind it being in the wrong place and the wrong size. We just do the same trick again: letâs invent points _x_ Â =Â 1, _d_ Â =Â  _t_ 4, _a_ Â =Â  _t_ â10. (Then the angles _xOd_ and _xOa_ are 40Â° and 100Â° respectively, which makes the angles _xad_ and _xda_ half those, 20Â° and 50Â°.)

Now we need to scale and rotate the second triangle _xad_ to fit it alongside the first one. In other words, we need to find a new point _D_ , which goes with our original _X_ and _A_ to form a triangle _XAD_ similar to the _xad_ we just constructed.

We do this by ensuring that the _ratio_ (_d_ Â âÂ  _x_)Â /Â (_a_ Â âÂ  _x_) is equal to the ratio (_D_ Â âÂ  _X_)Â /Â (_A_ Â âÂ  _X_). (A ratio of two complex numbers tells you how much you need to scale and rotate one to turn it into the other, which means itâs exactly what you need to know to check that two triangles are similar.)

So if we know all of _X_ , _A_ , _x_ , _a_ , and _d_ , and we also want (_d_ Â âÂ  _x_)Â /Â (_a_ Â âÂ  _x_)Â =Â (_D_ Â âÂ  _X_)Â /Â (_A_ Â âÂ  _X_), then we can just solve that equation for _D_ , to get

_D_ = _X_ \+ (_d_ â _x_) (_A_ â _X_) / (_a_ â _x_)

Substituting in the values _x_ Â =Â 1, _d_ Â =Â  _t_ 4, _a_ Â =Â  _t_ â10, this gives us

_D_ = _X_ \+ (_t_ 4 â 1) (_A_ â _X_) / (_t_ â10 â 1)

Similarly, we can construct the point _E_ by doing the same thing again: make a triangle inscribed in the unit circle with angles 30Â°, 40Â° and 110Â°, and place it so that two of its vertices coincide with _X_ and _B_. Omitting the boring bits, this gives us

_E_ = _X_ \+ (_t_ â6 â 1) (_B_ â _X_) / (_t_ 8 â 1)

### Divide two numbers to get the angle you want

Now we have all the points _D_ ,Â  _E_ ,Â  _X_ involved in the topmost triangle of the diagram. So we can construct a complex number representing the ratio between two sides of that triangle:

_z_ = (_X_ â _E_) / (_D_ â _E_)

The modulus of _z_ is uninteresting to us: it tells us the ratio between the lengths _EX_ and _ED_ , and nobodyâs asking us to find those lengths or their ratio. But the _argument_ of _z_ is exactly the angle we want!

### Divide by the complex conjugate to normalise to unit length

At this point, if we were happy to get an approximate solution, we could just stop there, and measure the argument of _z_. But Iâm working towards an _exact_ solution in the next section, and so I want to do one more thing: I want to modify the number _z_ so that it has unit length. When we get to the end of the exact solution, youâll see why that was useful!

We can do this by making the complex conjugate of _z_ , which Iâll write _z_ *. This has the same modulus as _z_ , but rotates the opposite way around the origin. So if we _divide_ them, to make the quotient _q_ Â =Â  _z_ Â /Â  _z_ *, then _q_ is guaranteed to have modulus 1.

This operation also doubled the argument, because _z_ and 1Â /Â  _z_ * _both_ have the same argument (namely the angle we want). So _q_ is a complex number with unit modulus, and whose argument is exactly _twice_ the angle weâre after.

### Putting it all together

Letâs recap. Here are all the variables we defined, in order, with the later definitions depending on earlier ones:

_t_ Â =Â  _e_ 2 _Ïi_ /36  
 _X_ = 1  
 _A_ Â =Â  _t_ 10  
 _B_ Â =Â  _t_ â12  
 _D_ = _X_ \+ (_t_ 4 â 1) (_A_ â _X_) / (_t_ â10 â 1)  
_E_ = _X_ \+ (_t_ â6 â 1) (_B_ â _X_) / (_t_ 8 â 1)  
_z_ = (_X_ â _E_) / (_D_ â _E_)  
_q_ Â =Â  _z_ Â /Â  _z_ *

If we could calculate all those complex numbers _exactly_ , then weâd find that _q_ was a unit-modulus number whose argument was twice the angle we want.

Just to demonstrate it works, hereâs a transcription of that calculation directly into Python, without worrying about the rounding errors. So you can at least find out what the answer _is_ :
    
    
    import cmath
    import math
    t = cmath.exp(math.pi * 2j / 36)
    X = 1
    A = t**10
    B = t**-12
    D = X + (t**4 - 1) * (A - X) / (t**-10 - 1)
    E = X + (t**-6 - 1) * (B - X) / (t**8 - 1)
    z = (X - E) / (D - E)
    q = z / z.conjugate()
    arg = cmath.phase(q) * 180 / math.pi
    print(f"Argument of q = {arg}Â°")
    print(f"So Î¸ = {arg/2}Â°")
    

If you run this in Python, it prints:
    
    
    Argument of q = 59.99999999999992Â°
    So Î¸ = 29.99999999999996Â°
    

See what I mean about the solution being approximate? It looks very much as if this ought to be exactly 30Â° but has suffered some rounding errors. So surely the final answer to the problem is that _Î¸_ Â =Â 30Â° exactly. But if we want to impress a mathematician, we have to do better than âwell, it looks right to about 13 decimal placesâ.

## Now do it all by algebra

Now we need to find a way to do the same calculation, but without any approximation. We canât use floating-point numbers: weâll have to use integers, and rational numbers, which can be represented exactly.

This is a problem, because the coordinates of all the points in this problem _arenât_ rational numbers. But looking back at the calculation, theyâre all derived from just _one_ complex number with irrational components, which we used as our starting point: the number _t_ Â =Â  _e_ 2 _Ïi_ /36. Everything we did after that looked like pretty simple arithmetic, without any irrational constants.

So the trick is going to be: carry through the calculation in such a way that we express all our intermediate results as algebraic expressions in terms of _t_. Then we can arrange that everything _else_ in those expressions is a rational, and we can keep things exact.

In fact, weâre going to arrange that every intermediate result is a _polynomial_ in _t_ , and moreover, limit the degree of those polynomials.

### Find the minimal polynomial of _t_

The number _t_ represents a 10Â° rotation about the origin. If you raise it to the power _n_ , it represents a 10 _n_ Â° rotation about the origin. So, in particular, if you raise it to the power 36, it represents a 360Â° rotation, which is the same as no rotation at all. That is: _t_ 36Â =Â 1.

I said we were going to limit the degree of our polynomials. This is how: now that we know _t_ 36Â =Â 1, it follows that if we have a _really big_ polynomial, involving very large powers of _t_ , we can reduce the larger powers to smaller ones, by replacing _t_ 36 with 1 wherever it appears, and more generally, replacing _t_ 36Â +Â  _n_ with _t_ _n_. This allows us to ensure that when our calculations start generating polynomials in _t_ , we can keep their degree less than 36.

But in fact we can do better than that. Another way to say that _t_ 36Â =Â 1 is to say that _t_ is a root of the polynomial _t_ 36Â âÂ 1. But that polynomial factorises:

_t_ 36Â âÂ 1 = (_t_ Â âÂ 1) (_t_ Â +Â 1) (_t_ 2Â +Â 1) (_t_ 2Â âÂ  _t_ Â +Â 1) (_t_ 2Â +Â  _t_ Â +Â 1) (_t_ 4Â âÂ  _t_ 2Â +Â 1) (_t_ 6Â âÂ  _t_ 3Â +Â 1) (_t_ 6Â +Â  _t_ 3Â +Â 1) (_t_ 12Â âÂ  _t_ 6Â +Â 1)

Any given root of the left-hand side _t_ 36Â âÂ 1 must be a root of _one_ of the factors on the right-hand side. But nothing will be a root of _more than one_ of those factors, or else theyâd split further. So we can find out which factor the _t_ we want is a root of, and then just use that one.

It turns out that our original _t_ is a root of the final, largest factor: _t_ 12Â âÂ  _t_ 6Â +Â 1. In other words, _t_ has the property that _t_ 12Â =Â  _t_ 6Â âÂ 1.

So we can keep all our polynomialsâ degrees less than 12, instead of the 36 I suggested earlier. Whenever we generate a new polynomial, we can reduce it by replacing _t_ 12 with _t_ 6Â âÂ 1 wherever it appears, or more generally, replacing _t_ 12Â +Â  _n_ with _t_ 6Â +Â  _n_ Â âÂ  _t_ _n_ , and keep doing that until there arenât any terms bigger than _t_ 11 any more.

This is called the _minimal polynomial_ of the number _t_ : itâs the smallest-degree polynomial with rational coefficients that _t_ is a root of. Any other polynomial which has _t_ as a root must therefore be a multiple of it. (So if there were a smaller one, then _t_ 12Â âÂ  _t_ 6Â +Â 1 would have to be a multiple of _that_ , and it isnât, because we already factorised it as far as it would go in rationals.)

This minimality means that we can reliably test our numbers for equality. If we have two polynomials in _t_ , and the complex numbers they represent are _exactly equal_ , then their difference is a polynomial in _t_ which evaluates to zero, i.e. which has _t_ as a root. Therefore it must be a multiple of _t_ 12Â âÂ  _t_ 6Â +Â 1. But if we reduced both polynomials to degree less than 12, then their difference canât be a multiple of _t_ 12Â âÂ  _t_ 6Â +Â 1 unless itâs zero.

So, as long as we keep our polynomials fully reduced, we can easily tell when two polynomials represent the same complex number, because it only happens if theyâre exactly the same polynomial. This is how weâre going to end up being sure that our answer is exactly right.

### Addition and multiplication

All right, so weâre representing our numbers as polynomials in _t_ , reduced mod _t_ 12Â âÂ  _t_ 6Â +Â 1. Now we have to work out how to do arithmetic on numbers in that form.

Addition is easy. If you have two polynomials in _t_ , then you add them by just adding together corresponding coefficients. No higher-order terms are ever generated, so if the two input polynomials had degree <Â 12, so does the sum. For example:

(_t_ 11 \+ 3 _t_ 9 \+ _t_) + (_t_ 9 â _t_ \+ 42) = (_t_ 11 \+ 4 _t_ 9 \+ 42)

Multiplying two polynomials _can_ generate terms of higher degree. But we already know what to do about that: reduce the product polynomial until it has degree <Â 12, by repeatedly reducing a large term using _t_ 12Â +Â  _n_ Â =Â  _t_ 6Â +Â  _n_ Â âÂ  _t_ _n_. For example:

(2 _t_ 7 \+ 3 _t_) Ã (4 _t_ 8 \+ 1) = 8 _t_ 15 \+ 12 _t_ 8 \+ 2 _t_ 7 \+ 3 _t_ = (8 _t_ 9 â 8 _t_ 3) + 12 _t_ 8 \+ 2 _t_ 7 \+ 3 _t_

in which the multiplication generated a single oversized term, namely 8 _t_ 15, and then we reduced it by replacing that term with 8 _t_ 9 â 8 _t_ 3. So the final answer has no term larger than _t_ 11.

### Division

But addition and multiplication arenât enough by themselves. The calculations shown in the previous section also involve division. And if you divide two polynomials, itâs not obvious that you can make the result back into a polynomial at all.

The first division that comes up in that calculation is an easy one: we set _B_ Â =Â  _t_ â12, i.e. _B_ Â =Â 1Â /Â  _t_ 12. But that one can be eliminated almost trivially: we know _t_ 36Â =Â 1, so _t_ â12Â =Â  _t_ 36â12Â =Â  _t_ 24. And now that _is_ a polynomial again (although its degree is too high, so weâll have to reduce it).

But the next division, where we make _D_ by dividing something by (_t_ â10 â 1), isnât nearly as easy to handle. We can turn the _t_ â10 into _t_ 26 easily enough, but even so, how do we make something like 1Â /Â (_t_ 26 â 1) back into a polynomial?

Suppose that we have some value _x_ , expressed as a polynomial in _t_ , and we want to find 1Â /Â  _x_.

That value _x_ will have a _minimal polynomial_ , just like _t_ does. Letâs call it _P_ _x_. By definition, this is the lowest-degree polynomial (with rational coefficients) that has _x_ as a root. (There must be one, because anything you can write as a polynomial in _t_ is an algebraic number, and therefore a root of _some_ polynomial â and then itâs just a matter of finding the smallest one.)

In general, _x_ isnât the only root of _P_ _x_. If _P_ _x_ has degree greater than 1, then it will have other roots too, say _a_ , _b_ , â¦, _n_. If we could find _all_ the roots of _P_ _x_ (including _x_ itself), then we could write the polynomial _P_ _x_ as a product of linear terms, each one having one of the roots of _P_ _x_ (negated) as its constant term. And if you imagine multiplying out that product, then the constant term of the whole thing is therefore the product of all the roots (up to maybe a sign flip). But itâs also equal to the constant term of _P_ _x_ itself, i.e. a rational number.

But in that case, let _w_ be the product of all the roots of _P_ _x_ _apart_ from _x_ itself. Then _wx_ is a rational. But then _w_ Â /Â  _wx_ is a polynomial divided by a rational, i.e. still a polynomial â and itâs clearly also equal to 1Â /Â  _x_. So this _is_ a way to write 1Â /Â  _x_ as a polynomial.

Thatâs all very well, but _how_ do you find the other roots of _P_ _x_? You _could_ do it by directly calculating _P_ _x_ and then trying to find its roots, but thatâs a huge amount of effort. Thereâs a shortcut.

All you need is to know the other 11 roots of _P_ _t_ Â =Â  _t_ 12Â âÂ  _t_ 6Â +Â 1, the minimal polynomial of _t_. Suppose that _u_ is a root of _P_ _t_ , but isnât _t_ itself. Then any equation between polynomials in _t_ (saying that two of them work out to the same thing mod _P_ _t_) must also be true if you replace every occurrence of _t_ with _u_ , because the only _property_ of _t_ that the equation depends on is that itâs a root of _P_ _t_ , and since _u_ also has that property, the statement must still be true.

So you can make all the roots3Iâve glossed over a subtlety here: this procedure will always give 12 values in total, including the original _x_ , but _some_ numbers represented as polynomials in _t_ have a minimal polynomial of lower degree than 12. In that situation our 12 values will consist of multiple copies of each root of _P_ _x_ , including multiple copies of _x_ itself. But what we do with them next still works, because the product of all of them is still a rational â itâs just a _power_ of _P_ _x_ âs constant term, instead of the constant term itself.3 of _P_ _x_ by taking the polynomial _x_ , and _evaluating_ it at each root _u_ of _P_ _t_ in turn.

That is: weâve been thinking of _x_ as a _complex number_ which just happens to be written as a polynomial in _t_. But we now switch to regarding it as a _function_ given by the same polynomial, which can be given _any_ complex number as input, and returns a weighted sum of powers of its input number. So evaluating the polynomial _x_ at _t_ gives us the value we had to start with â but we can also evaluate the same polynomial at some other number, such as _u_.

OK, but in order to evaluate _x_ at all the other roots of _P_ _t_ , we need to _know_ the other roots of _P_ _t_. What are they?

Well, _P_ _t_ was a factor of _t_ 36Â âÂ 1. So the roots of _P_ _t_ must all be roots of _t_ 36Â âÂ 1, which means theyâre complex numbers whose 36th power is 1 â and all such numbers are powers of _t_. And the powers weâre looking for are the ones which have no common factor with 36: the roots of _P_ _t_ are

_t_ , _t_ 5, _t_ 7, _t_ 11, _t_ 13, _t_ 17, _t_ 19, _t_ 23, _t_ 25, _t_ 29, _t_ 31, _t_ 35

because when we factorised _t_ 36Â âÂ 1, the _other_ factors are the ones that represent numbers which become 1 when raised to a _smaller_ power than 36. The polynomial _t_ 12Â âÂ  _t_ 6Â +Â 1 is the one whose roots are the numbers whose 36th power is 1 _and no smaller power is_.

That was a lot of faff, so letâs bring it back down to earth. If you have a value _x_ represented as a polynomial in _t_ , then you can find the reciprocal 1Â /Â  _x_ as a polynomial in _t_ as follows:

  * Evaluate _x_ at each of those powers of _t_ (other than _t_ itself) to make _x_(_t_ 5), _x_(_t_ 7), ..., _x_(_t_ 35), each as a polynomial in _t_.
  * Multiply those 11 polynomials together to make a product _w_.
  * Then the product _wx_ , reduced mod _t_ 12Â âÂ  _t_ 6Â +Â 1, will work out to a rational number.
  * So _w_ divided by the rational _wx_ is a polynomial in _t_ , and is also equal to 1Â /Â  _x_.



Iâve just about got room to show an example. Suppose _x_ Â =Â  _t_ 3Â +Â  _2t_ Â +Â 1. Then _x_(_t_ 5)Â =Â  _t_ 15Â +Â  _2t_ 5Â +Â 1 (you replace each power of _t_ in the original expression with the corresponding power of _t_ 5). Similarly, _x_(_t_ 7)Â =Â  _t_ 21Â +Â  _2t_ 7Â +Â 1, and so on until _x_(_t_ 35)Â =Â  _t_ 105Â +Â  _2t_ 35Â +Â 1.

Multiplying out the product _w_ of all of those 11 polynomials gives a _huge_ polynomial, with coefficients going up to _t_ 645. But youâd reduce it mod _t_ 12Â âÂ  _t_ 6Â +Â 1 as you went along, to keep the intermediate values small.

The product _w_ , fully reduced, works out to

â5692 _t_ 11 \+ 2500 _t_ 10 â 1129 _t_ 9 \+ 692 _t_ 8 â 242 _t_ 7 â 255 _t_ 6 \+ 5484 _t_ 5 â 1748 _t_ 4 \+ 1800 _t_ 3 â 1988 _t_ 2 â 1852 _t_ \+ 2176

Even reduced, that still looks like a horrible mess. But if you multiply that by the original _x_ Â =Â  _t_ 3Â +Â  _2t_ Â +Â 1 and reduce again, then just like magic4In fact, this is a generalised form of the same technique you use to divide by a complex number _a_ Â +Â  _bi_ , by multiplying top and bottom by its complex conjugate _a_ Â âÂ  _bi_ so that the denominator turns into a real number. The principle is identical: _a_ Â +Â  _bi_ is a polynomial in _i_ ; the minimal polynomial of _i_ over â is _x_ 2Â +Â 1, and the only other root of that polynomial is â _i_ ; so we evaluate _a_ Â +Â  _bi_ at that other root to make _a_ Â âÂ  _bi_ , and then the product of that with the original number â reducing _i_ 2 wherever it appears â turns into a polynomial with only a constant term, which itâs easy to divide by. It all looks more complicated when you have 11 other roots rather than just one, but itâs exactly the same trick, just bigger!4, the result comes out to just

14689

And therefore, _w_ Â /Â 14689 is a degree-11 polynomial in _t_ , with rational coefficients, which is equal to 1Â /Â  _x_. It can be done5Another completely different approach to dividing by a polynomial _x_ when working mod _P_ _t_ is to use Euclidâs algorithm, the same as you would for modular arithmetic in integers. Find the greatest common divisor of the polynomials _x_ and _P_ _t_ ; you expect this to be 1, because _P_ _t_ is irreducible. As a by-product the algorithm will produce two more polynomials _Î»_ , _Î¼_ such that _Î»x_ Â +Â  _Î¼P_ _t_ Â =Â 1. Another way of writing that is _Î»x_ Â â¡Â 1 mod _P_ _t_ , so _Î»_ is precisely the inverse we wanted. Iâve chosen to do it this way instead for several reasons. First, because the idea of evaluating _x_ at a different value will be reused in the next section; second, because Euclidâs algorithm requires dividing polynomials (in the more usual sense of delivering a quotient and a remainder), which is a more complicated primitive operation than evaluating them and multiplying them â especially since Iâm going to show example code later. And thirdly, you can make this approach give you a _single_ algebraic formula for calculating the reciprocal of any number mod _P_ _t_ , which is more elegant than the way Euclid takes a variable number of steps depending on the inputs. But you _could_ do it by Euclid if you preferred, and it would still work.5!

### Complex conjugate of a polynomial

One last awkwardness: in solving this problem, we also wanted to take a complex conjugate, to calculate _q_ Â =Â  _z_ Â /Â  _z_ *. How will we do _that_ when _z_ is one of these polynomials?

Thatâs not too hard. The complex conjugate of a single power of _t_ is just the same power negated, because powers of _t_ all have modulus 1: (_t_ _n_)*Â =Â  _t_ â _n_. So if you have some number _x_ represented as a polynomial in _t_ , you can take its conjugate by evaluating it at _t_ â1. For example, take _x_ Â =Â  _t_ 3Â +Â  _2t_ Â +Â 1 (the same example we just used for division). Then

_x_ * = _x_(_t_ â1) = _t_ â3Â +Â  _2t_ â1Â +Â 1 = _t_ 33Â +Â  _2t_ 35Â +Â 1

because, again, _t_ â _n_ is the same thing as _t_ 36Â âÂ  _n_. Now we just reduce that mod _t_ 12Â âÂ  _t_ 6Â +Â 1 as usual, and thatâs the complex conjugate of _x_.

### Now do the actual calculation

Now we know how to do every arithmetic operation involved in our calculation, on numbers expressed as polynomials in _t_. Itâs time to actually _do_ the calculation!

As I said at the start, the amount of sheer polynomial-juggling in this procedure is large enough that you do want a computer to do the work for you. There are plenty of computer algebra systems that already have built-in libraries to work in polynomial quotient fields of this kind: I could show a piece of code in SageMath, for example, that isnât much longer than the earlier approximate version in Python. Or an interactive session in Maxima. Or probably half a dozen other systems of that kind.

But just to show that you donât _need_ a million lines of Serious Computer Algebra to do a job like this, hereâs an implementation in Python ([download the source](exact.py)) that does all the polynomial arithmetic all by itself and still just about fits on a (large) monitor. The actual calculation is shown at the bottom, very like the previous representation except that all the starting values are instances of the `Value` class, instead of Pythonâs native complex number type:
    
    
    import fractions
    
    class Value:
        "Class representing a polynomial in t, mod t^12 - t^6 + 1"
    
        def __init__(self, coeffs):
            # coeffs is an array with coeffs[i] giving the coefficient of t^i.
            # The input to this constructor can be any length; we'll reduce it.
            while len(coeffs) > 12:
                # Remove the highest-order coefficient
                coeff = coeffs.pop()
                n = len(coeffs)
                # Popping that coefficient subtracted coeff * t^n.
                # Add coeff * (t^(n-6) - t^(n-12)) to compensate.
                coeffs[n-6] += coeff
                coeffs[n-12] -= coeff
            # Pad with zeroes so that len(self.coeffs) is always exactly 12
            self.coeffs = coeffs + [0] * (12 - len(coeffs))
    
        def __add__(self, other):
            # Add corresponding coefficients
            return Value([u+v for u,v in zip(self.coeffs, other.coeffs)])
    
        def scale(self, scalar):
            # Multiply every coefficient by the scale
            return Value([scalar*u for u in self.coeffs])
    
        def __sub__(self, other):
            # Negate the RHS, then add
            return self + other.scale(-1)
    
        def mul_by_t(self):
            # Multiply by t by shifting all the coefficients upward by one
            return Value([0] + self.coeffs)
    
        def __mul__(self, other):
            total = Value([]) # zero
            other_times_power_of_t = other # other * t^0
            for coeff in self.coeffs:
                # Add coeff * other * t^i to the total
                total += other_times_power_of_t.scale(coeff)
                # Multiply by t to make the next (other * t^i)
                other_times_power_of_t = other_times_power_of_t.mul_by_t()
            return total
    
        def evaluate_at(self, x):
            total = Value([]) # zero
            power_of_x = Value([1]) # x^0
            for coeff in self.coeffs:
                # Add coeff * x^i to the total
                total += power_of_x.scale(coeff)
                # Multiply by x to make the next x^i
                power_of_x *= x
            return total
    
        @staticmethod
        def power_of_t(n):
            # t^36 = 1, so reduce mod 36, which also makes negative n positive
            n %= 36
            # Make the literal polynomial t^n and let the constructor reduce it
            return Value([0]*n + [1])
    
        def complex_conjugate(self):
            # Evaluate at t^-1
            return self.evaluate_at(self.power_of_t(-1))
    
        def reciprocal(self):
            # Evaluate at t^5, t^7, t^11, ..., t^35 and multiply them all together
            w = Value([1])
            for index in [5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35]:
                w *= self.evaluate_at(self.power_of_t(index))
            # Check that w * x is a constant (all coeffs after the 0th are zero)
            wx = self * w
            assert all(coeff == 0 for coeff in wx.coeffs[1:])
            # And divide by that constant, using fractions.Fraction for exactness
            return w.scale(fractions.Fraction(1, wx.coeffs[0]))
    
        def __truediv__(self, other):
            return self * other.reciprocal()
    
        def __str__(self):
            # Format as a mathematical expression in Python syntax
            return " + ".join(
                f"{u}" if i==0 else f"{u}*t" if i==1 else f"{u}*t**{i}"
                for i, u in enumerate(self.coeffs)
                if u != 0
            )
    
    one = Value([1])
    X = one
    A = Value.power_of_t(10)
    B = Value.power_of_t(-12)
    D = X + (Value.power_of_t(4) - one) * (A - X) / (Value.power_of_t(-10) - one)
    E = X + (Value.power_of_t(-6) - one) * (B - X) / (Value.power_of_t(8) - one)
    z = (X - E) / (D - E)
    q = z / z.complex_conjugate()
    
    print("X =", X)
    print("A =", A)
    print("B =", B)
    print("D =", D)
    print("E =", E)
    print("z =", z)
    print("q =", q)
    

When this is run, it prints:
    
    
    X = 1
    A = 1*t**10
    B = -1*t**6
    D = 1 + 1*t**2 + -1*t**8 + 1*t**10
    E = 1 + 1*t**2 + 1*t**4 + -1*t**6 + -1*t**8
    z = 1 + -1*t**2 + 1*t**6 + 1*t**8 + -1*t**10
    q = 1*t**6
    

The first five lines of this output give the locations of the five points in our geometric diagram, as polynomials in _t_. To show that this really works and isnât abstract nonsense, hereâs a diagram showing _how_ those points are derived from those polynomials:

![\[polynomials.svg\]](polynomials.svg) The points in our calculation, represented as polynomials

This diagram happens to be nice and simple, because all the coefficients in those polynomials worked out to Â±1, for some reason. You can confirm for yourself that each arrow looks as if itâs at about the right angle (e.g. the arrow marked 1 points directly to the right, the _t_ 2 arrow is 20Â° anticlockwise from that, and if the â _t_ 6 arrow were reversed then it would be 60Â° anticlockwise from 1). And if you start from the black circle at the origin, you can follow a path of grey arrows to get to each of the points _X_ , _A_ , _B_ , _D_ , _E_ , and if you add up the powers of _t_ written on each arrow, you get the same polynomials shown above.

I showed those values purely for interest. But the key point is the final value: _q_ Â =Â  _t_ 6.

Thatâs saying that _q_ is _exactly_ the complex number that represents a 60Â° rotation about the origin. And remember that in the previous section I said that _q_ was _twice_ the angle we were actually after.

So the final answer is that the angle _Î¸_ , in the original diagram at the start of this article, is _exactly_ 30Â°. No surprises there: thatâs the same value it _looked_ as if it was going to be, after we ran the approximate version earlier. But this time weâre sure of it: the calculations have no approximation error, because we didnât do anything approximate at all.

## Afterthoughts

### What if the answer isnât nice?

I hope itâs now clear why I wanted to do that final step of calculating _q_ Â =Â  _z_ Â /Â  _z_ *. The _previous_ value in the programâs output was

_z_ = 1 â _t_ 2 \+ _t_ 6 \+ _t_ 8 â _t_ 10

This represents a complex number whose argument is the desired angle 30Â°. But you wouldnât know it just by looking at that polynomial! That nice simple argument is combined with a _magnitude_ of something complicated which has to be represented as a sum of lots of powers of _t_ pointing in other random directions, and therefore, you canât _see_ by eye what its argument is. But _q_ , because itâs been reduced back to unit magnitude, is very simple by comparison, and itâs easy to check by eye that the answer is what you expect it to be.

But one caveat: this entire procedure only works out neatly, with _q_ coming out as a really simple monomial, _because_ the angle in question is a nice round number â a multiple of the same 10Â° unit that all the input angles are.

Langleyâs problem is called âadventitiousâ because of the nice coincidence that using _those_ particular input angles makes the output angle _Î¸_ a nice exact value. With most other choices of the angles, that wouldnât have worked, and the way youâd find out it hadnât worked would be that the output value of _q_ would look like some disgusting complicated polynomial, with many nonzero terms instead of a single one, probably with fractional coefficients as well. If you saw _that_ output (and hadnât made a mistake setting up the problem), then it would tell you the output wasnât a nice round number, and the only thing to do was to calculate it numerically using trigonometry after all.

For example, hereâs a variant version of the problem in which the angles donât work out nicely:

![\[nastyversion.svg\]](nastyversion.svg) A version that would make Langley wince

In this version, Iâve made the overall triangle _ABC_ into a 70Â°â70Â°â40Â° triangle instead of its original 80Â°â80Â°â20Â°, and left the base triangle _ABX_ the same.

If you run my polynomial-based calculation for _this_ triangle, the answer you get as the final value _q_ looks much nastier, and so do a lot of the intermediate values:
    
    
    X = 1
    A = 1*t**10
    B = -1*t**6
    D = 2/3 + 2/3*t**2 + 1/3*t**4 + -1/3*t**6 + -1/3*t**8 + 1/3*t**10
    E = 3*t**2 + -2*t**4 + 2*t**6 + -3*t**8 + 1*t**10
    z = 45/73 + -132/73*t**2 + 66/73*t**4 + 141/73*t**6 + 39/73*t**8 + -129/73*t**10
    q = 6/73 + -3/73*t**2 + 38/73*t**4 + 48/73*t**6 + -24/73*t**8 + 12/73*t**10
    

But the answer isnât _wrong!_ Itâs not presented in a helpful form, but itâs still _right_. If we did want to calculate the angle _Î¸_ in this version of the problem, then one way would be to go back to the Python code shown above which did the whole job using floating point. But we can take a short cut by using the value of _q_ that the polynomial code has computed, and just converting that back into a complex number using Python. If you do that, you find that it really does have unit magnitude (up to Pythonâs rounding errors), and that its argument is twice the angle _Î¸_ in my modified diagram:
    
    
    import cmath
    import math
    t = cmath.exp(math.pi * 2j / 36)
    q = 6/73 + -3/73*t**2 + 38/73*t**4 + 48/73*t**6 + -24/73*t**8 + 12/73*t**10
    print(f"Modulus of q = {abs(q)}")
    arg = cmath.phase(q) * 180 / math.pi
    print(f"Argument of q = {arg}Â°")
    print(f"So Î¸ = {arg/2}Â°")
    
    
    
    Modulus of q = 0.9999999999999998
    Argument of q = 46.727454823246Â°
    So Î¸ = 23.363727411623Â°
    

So this time we _had_ to do some trigonometry at the end to get the angle â because itâs a horrible irrational, and we werenât going to get it out of any amount of nice clean rational-number work. But the method was still _accurate_ â the polynomial representation of that _q_ is exactly correct, without any rounding error. The rounding errors only appear in the very last stage when you convert back into a real angle.

### I did twice as much work as I really needed to

Looking at the intermediate values from the final calculation, you might notice that they all consist entirely of _even_ powers of _t_. Nothing is ever an odd power. Not even in the disgusting modified version where the angle doesnât work out neatly.

With hindsight, I should have been able to predict that, because all the angles we ever encounter are doubled! We construct a triangle with angles _Î±_ , _Î²_ , _Î³_ by doubling those angles and then making angles at the origin of 2 _Î±_ , 2 _Î²_ , 2 _Î³_. And the final trick of multiplying _z_ by its complex conjugate has the effect of doubling the output angle weâre trying to find. So nothing in the input or output of the calculation ever has to work with an angle _not_ doubled.

Therefore, since all the angles in the problem are multiples of 10Â°, all the angles the calculation ever has to work with are multiples of 20Â°. So I could have saved myself some time by starting from a different complex number, _T_ Â =Â  _t_ 2 representing a 20Â° instead of 10Â° rotation. The minimal polynomial of _that_ is _t_ 6Â âÂ  _t_ 3Â +Â 1 (also one of the factors of _t_ 36Â âÂ 1). So that would have let me limit all the polynomials in the calculation to degree less than 6, instead of less than 12.

But I didnât think of that until I saw all the intermediate values at the end of the procedure, noticed all the exponents were even, and felt silly!

### Have I cheated?

I mentioned in the introduction that thereâs often a âno trigonometryâ rule when this problem is set. Have I broken it?

Certainly Iâve obeyed the _letter_ of the rule: I havenât calculated a sine, cosine or tangent anywhere in this entire derivation6All right, the Python code at the end of the first section _did_ do trigonometry, in the form of complex exponentials and the Python `cmath.phase` function. So did the modified example where the angle didnât work out nicely. But those arenât part of the proper solution. The full solution to the original problem, delivering the answer of 30Â° exactly using nothing but polynomials, didnât use either of those pieces of floating-point code.6. But whether you think Iâve kept to the _spirit_ of the rule is another matter, and in my opinion, the answer depends on what exactly you think the spirit of the rule _is_.

_Why_ did someone forbid trigonometric solutions to this problem? I can see two reasonable possibilities.

One answer is that the trigonometry approach is only approximate: you get an answer to some number of significant figures, but you canât easily prove that itâs _exactly_ the number of degrees it looks like. So you might have forbidden trigonometry because you wanted the answer calculated exactly, not just approximated. In that case, I havenât violated the spirit of the rule: this method _does_ calculate the exact answer.

But the other answer is that the aim of forbidding trigonometry was to force the puzzle solver to find the _clever_ solution involving extra construction lines. If thatâs what you think the point was, then I _have_ violated the spirit of the rule: the method Iâve shown here is brute-force plodding, designed to avoid needing an insight of any kind. (Or, at least, an insight specific to the individual numbers; the trick for dividing by a polynomial in _t_ certainly is clever, but itâs well known, and you only have to learn it once, and then itâs reusable in any situation of this kind.)

But hereâs a third thought. One purpose of setting a student a problem in the first place is that they should learn something worthwhile from it. And what you learn from this algebraic method is indeed worthwhile. The whole technique can be reused unchanged in other computational contexts ([hereâs an example!](../aperiodic-tilings/#exact-coords)), and also all of the ideas here are important to ârealâ mathematics: this kind of algebraic extension of the field of rational numbers leads directly to Galois theory. If I had a student, and set them this problem, and they chose to learn about field extensions instead of constructing extra triangles in a diagram, I would think theyâd made good use of their time!

## Footnotes

With any luck, you should be able to read the footnotes of this article in place, by clicking on the superscript footnote number or the corresponding numbered tab on the right side of the page.

But just in case the CSS didnât do the right thing, hereâs the text of all the footnotes again:

1. Perhaps youâre wondering _why_ I might happen to be concerned with this problem and how to solve it without cleverness. Might it be because someone gave me the problem recently and I didnât manage to find the clever answer? No comment.

2. What if _C_ is on the opposite side of the line from _O_? In that case, you have to switch to measuring the angle at _O_ on the other side of the line, so that itâs 360Â° minus the angle shown here.

3. Iâve glossed over a subtlety here: this procedure will always give 12 values in total, including the original _x_ , but _some_ numbers represented as polynomials in _t_ have a minimal polynomial of lower degree than 12. In that situation our 12 values will consist of multiple copies of each root of _P_ _x_ , including multiple copies of _x_ itself. But what we do with them next still works, because the product of all of them is still a rational â itâs just a _power_ of _P_ _x_ âs constant term, instead of the constant term itself.

4. In fact, this is a generalised form of the same technique you use to divide by a complex number _a_ Â +Â  _bi_ , by multiplying top and bottom by its complex conjugate _a_ Â âÂ  _bi_ so that the denominator turns into a real number. The principle is identical: _a_ Â +Â  _bi_ is a polynomial in _i_ ; the minimal polynomial of _i_ over â is _x_ 2Â +Â 1, and the only other root of that polynomial is â _i_ ; so we evaluate _a_ Â +Â  _bi_ at that other root to make _a_ Â âÂ  _bi_ , and then the product of that with the original number â reducing _i_ 2 wherever it appears â turns into a polynomial with only a constant term, which itâs easy to divide by. It all looks more complicated when you have 11 other roots rather than just one, but itâs exactly the same trick, just bigger!

5. Another completely different approach to dividing by a polynomial _x_ when working mod _P_ _t_ is to use Euclidâs algorithm, the same as you would for modular arithmetic in integers. Find the greatest common divisor of the polynomials _x_ and _P_ _t_ ; you expect this to be 1, because _P_ _t_ is irreducible. As a by-product the algorithm will produce two more polynomials _Î»_ , _Î¼_ such that _Î»x_ Â +Â  _Î¼P_ _t_ Â =Â 1. Another way of writing that is _Î»x_ Â â¡Â 1 mod _P_ _t_ , so _Î»_ is precisely the inverse we wanted. Iâve chosen to do it this way instead for several reasons. First, because the idea of evaluating _x_ at a different value will be reused in the next section; second, because Euclidâs algorithm requires dividing polynomials (in the more usual sense of delivering a quotient and a remainder), which is a more complicated primitive operation than evaluating them and multiplying them â especially since Iâm going to show example code later. And thirdly, you can make this approach give you a _single_ algebraic formula for calculating the reciprocal of any number mod _P_ _t_ , which is more elegant than the way Euclid takes a variable number of steps depending on the inputs. But you _could_ do it by Euclid if you preferred, and it would still work.

6. All right, the Python code at the end of the first section _did_ do trigonometry, in the form of complex exponentials and the Python `cmath.phase` function. So did the modified example where the angle didnât work out nicely. But those arenât part of the proper solution. The full solution to the original problem, delivering the answer of 30Â° exactly using nothing but polynomials, didnât use either of those pieces of floating-point code.
