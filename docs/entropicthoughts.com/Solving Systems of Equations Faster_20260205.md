# Solving Systems of Equations Faster

**来源:** https://entropicthoughts.com
**链接:** https://entropicthoughts.com/solving-systems-of-equations-faster
**日期:** Thu, 29 Jan 2026 00:00:00 +0100

---

# [Entropic Thoughts](/)

## Solving Systems of Equations Faster

  * [Home](/)
  * [Archive](/archive)
  * [Tags](/tags)
  * [About](/about)
  * [xkqr.org](https://xkqr.org/)



# Solving Systems of Equations Faster

by kqr, published 2026-01-29

Tags: 

  * [maths](tags.html#maths)



![solving-systems-of-equations-faster.jpg](../image/banner/solving-systems-of-equations-faster.jpg)

Here's an example of a system of equations I came across. 

\\[\left\\{\begin{array}{l} & 4x & \- & 3y & = & -17 \\\ - & 2x & \+ & y & = & 7 \end{array} \right.\\] 

There's a fast way to solve this, which is to take two of the lower equation and add to the upper equation. This makes the \\(x\\)'s cancel out and removes some of the \\(y\\)'s, leaving us with 

\\[-y = - 17 + 2 \times 7\\] 

which is easy to mentally rearrange into 

\\[y = 3\\] 

and, looking at the lower equation, this must mean that 

\\[x = -2\\] 

We have solved the system of equations, and it was quite fast. Also, it was in our heads. 

* * *

In school, I was taught a different method. I was taught to rearrange one of the equations and substitute into the other. This leads to something like turning the lower equation into 

\\[y = 7 + 2x\\] 

and then plopping it into the upper equation, which yields 

\\[4x - 3\left(7 + 2x\right) = -17\\] 

and it gets kind of messy and is not trivial to keep straight in the head. 

* * *

It is very satisfying to take an entire equation, add it a few times to one of the others, and get something simpler fall out. When it works out, it looks magical to an audience! But you have to pick the right scaling factor. we could have aimed for canceling out the \\(y\\)'s instead, by adding the lower equation three times to the upper. But that would have ended us up with 

\\[-2x = -17 + 21\\] 

which, when we see it on paper like this, we can tell is 

\\[x=-2\\] 

but it's not quite as clear to do in the head because it results in bigger numbers to subtract and add. 

# Comments

## 2026-01-29: Julian Ferrone

You might want to mention that the term for this technique is Gaussian elimination—then in case any of your readers are unfamiliar, they can search for more examples on larger systems of linear equations. 

It's a handy technique, especially on paper—not rewriting the coefficients over and over is a nice time saver—but it's useful in code too. For example, last year's Advent of Code had a puzzle that involved solving systems of linear equations, so I had to write a Gaussian eliminator (and roll my own implementation of rational numbers as floats caused issues) in Elixir, as I rather stubbornly refused to just shell out to an already-written solver—since where's the fun in that? 

([Julian has a blog on his website](https://www.julianferrone.com/). I particularly enjoyed the article on adding metadata to the otherwise human-only markup format Subtext.) 

## 2026-01-30: Andrew Rodland

And of course, if you put everything in columns and then take away the symbols leaving just the coefficients, the method still works, and it's called Gaussian elimination on matrices. 

But for some reason, many schools teach the "rearrange and substitute" method, and then they teach the matrix method, without ever even mentioning the symbolic method "behind" the matrix method, or the identities that make those transformations valid. So you learn one way that's cumbersome, and one that's mysterious wizardry! 

If you liked this and want more you should [buy me a coffee](https://buymeacoff.ee/kqr). That helps me turn my 170+ ideas backlog into articles. 

Shoutout to my amazing wife    without whose support I would never make it past the first sentence. ♥ 

S = k log W.  
   
Comments? [Send me an email](/about).  
You can also [subscribe for new articles](https://buttondown.email/entropicthoughts). 
