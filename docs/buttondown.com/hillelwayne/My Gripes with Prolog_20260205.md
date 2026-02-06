# My Gripes with Prolog

**来源:** https://buttondown.com/hillelwayne
**链接:** https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/
**日期:** Wed, 14 Jan 2026 16:48:51 +0000

---

For the next release of [Logic for Programmers](https://leanpub.com/logic/), I'm finally adding the sections on Answer Set Programming and Constraint Logic Programming that I TODOd back in version 0.9. And this is making me re-experience some of my pain points with Prolog, which I will gripe about now. If you want to know more about why Prolog is cool instead, go [here](https://buttondown.com/hillelwayne/archive/a48fce5b-8a05-4302-b620-9b26f057f145/) or [here](https://www.metalevel.at/prolog) or [here](https://ianthehenry.com/posts/drinking-with-datalog/) or [here](https://logicprogramming.org/). 

### No standardized strings

ISO "strings" are just atoms or lists of single-character atoms (or lists of integer character codes). The various implementations of Prolog add custom string operators but they are not cross compatible, so code written with strings in SWI-Prolog will not work in Scryer Prolog. 

### No functions

Code logic is expressed entirely in _rules_ , predicates which return true or false for certain values. For example if you wanted to get the length of a Prolog list, you write this:
    
    
    ?- length([a, b, c], Len).
    
       Len = 3.
    

Now this is pretty cool in that it allows bidirectionality, or running predicates "in reverse". To generate lists of length 3, you can write `length(L, 3)`. But it also means that if you want to get the length a list _plus one_ , you can't do that in one expression, you have to write `length(List, Out), X is Out+1`.

For a while I thought no functions was necessary evil for bidirectionality, but then I discovered [Picat](https://picat-lang.org/) has functions and works just fine. That by itself is a reason for me to prefer Picat for my LP needs.

(Bidirectionality is a killer feature of Prolog, so it's a shame I so rarely run into situations that use it.)

### No standardized collection types besides lists

Aside from atoms (`abc`) and numbers, there are two data types:

  * Linked lists like `[a,b,c,d]`.
  * Compound terms like `dog(rex, poodle)`, which _seem_ like record types but are actually tuples. You can even convert compound terms to linked lists with `=..`:


    
    
    ?- L =.. [a, b, c].
       L = a(b, c).
    ?- a(b, c(c)) =.. L.
       L = [a, b, c(c)].
    

There's no proper key-value maps or even struct types. Again, this is something that individual distributions can fix (without cross compatibility), but these never feel integrated with the rest of the language. 

### No boolean values

`true` and `false` aren't values, they're control flow statements. `true` is a noop and `false` says that the current search path is a dead end, so backtrack and start again. You can't explicitly store true and false as values, you have to implicitly have them in facts (`passed(test)` instead of `test.passed? == true`).

This hasn't made any tasks impossible, and I can usually find a workaround to whatever I want to do. But I do think it makes things more inconvenient! Sometimes I want to do something dumb like "get all atoms that don't pass at least three of these rules", and that'd be a lot easier if I could shove intermediate results into a sack of booleans. 

(This is called "[Negation as Failure](https://en.wikipedia.org/wiki/Negation_as_failure)". I think this might be necessary to make Prolog a Turing complete general programming language. Picat fixes a lot of Prolog's gripes and still has negation as failure. ASP has regular negation but it's not Turing complete.) 

### Cuts are confusing

Prolog finds solutions through depth first search, and a "cut" (`!`) symbol prevents backtracking past a certain point. This is necessary for optimization but can lead to invalid programs. 

You're not supposed to use cuts if you can avoid it, so I pretended cuts didn't exist. Which is why I was surprised to find that [conditionals](https://eu.swi-prolog.org/pldoc/doc_for?object=\(-%3E\)/2) are implemented with cuts. Because cuts are spooky dark magic conditionals _sometimes_ conditionals work as I expect them to and sometimes leave out valid solutions and I have no idea how to tell which it'll be. Usually I find it safer to just avoid conditionals entirely, which means my code gets a lot longer and messier. 

### Non-cuts are confusing

The original example in the last section was this: 
    
    
    foo(A, B) :-
        \+ (A = B),
        A = 1,
        B = 2.
    

`foo(1, 2)` returns true, so you'd expect `f(A, B)` to return `A=1, B=2`. But it returns `false`. Whereas this works as expected.
    
    
    bar(A, B) :-
        A = 1,
        B = 2,
        \+ (A = B).
    

I _thought_ this was because `\+` was implemented with cuts, and the [Clocksin book](https://www.amazon.com/Programming-Prolog-Using-ISO-Standard/dp/3540006788) suggests it's `call(P), !, fail`, so this was my prime example about how cuts are confusing. But then I tried this:
    
    
    ?- member(A, [1,2,3]), \+ (A = 2), A = 3.
    A = 3. % wtf?
    

There's no way to get that behavior with cuts! I don't think `\+` uses cuts at all! And now I have to figure out why `foo(A, B)` doesn't returns results. Is it [floundering](https://github.com/dtonhofer/prolog_notes/blob/master/other_notes/about_negation/floundering.md)? Is it because `\+ P` only succeeds if `P` fails, and `A = B` always succeeds? A closed-world assumption? Something else?[1](https://buttondown.com/hillelwayne/rss#fn:dif)

### Straying outside of default queries is confusing

Say I have a program like this:
    
    
    tree(n, n1).
    tree(n, n2).
    tree(n1, n11).
    tree(n2, n21).
    tree(n2, n22).
    tree(n11, n111).
    tree(n11, n112).
    
    branch(N) :- % two children
        tree(N, C1),
        tree(N, C2),
        C1 @< C2. % ordering
    

And I want to know all of the nodes that are parents of branches. The normal way to do this is with a query:
    
    
    ?- tree(A, N), branch(N).
    A = n, N = n2; % show more...
    A = n1, N = n11.
    

This is interactively making me query for every result. That's usually not what I want, I know the result of my query is finite and I want all of the results at once, so I can count or farble or whatever them. It took a while to figure out that the proper solution is [`bagof(Template, Goal, Bag)`](https://www.swi-prolog.org/pldoc/man?predicate=bagof/3), which will "Unify Bag with the alternatives of Template":
    
    
    ?- bagof(A, (tree(A, N), branch(N)), As).
    
    As = [n1], N = n11;
    As = [n], N = n2.
    

Wait crap that's still giving one result at a time, because `N` is a free variable in `bagof` so it backtracks over that. It surprises me but I guess it's good to have as an option. So how do I get all of the results at once?
    
    
    ?- bagof(A, N^(tree(A, N), branch(N)), As).
    
    As = [n, n1]
    

The only difference is the `N^Goal`, which tells `bagof` to ignore and group the results of `N`. As far as I can tell, this is the _only_ place the ISO standard uses `^` to mean anything besides exponentiation. Supposedly it's the [existential quantifier](https://sicstus.sics.se/sicstus/docs/latest4/html/sicstus.html/ref_002dall_002dsum.html)? In general whenever I try to stray outside simpler use-cases, especially if I try to do things non-interactively, I run into trouble.

### I have mixed feelings about symbol terms

It took me a long time to realize the reason `bagof` "works" is because infix symbols are mapped to prefix compound terms, so that `a^b` is `^(a, b)`, and then different predicates can decide to do different things with `^(a, b)`.

This is also why you can't just write `A = B+1`: that unifies `A` with the _compound term_ `+(B, 1)`. `A+1 = B+2` is _false_ , as `1 \= 2`. You have to write `A+1 is B+2`, as `is` is the operator that converts `+(B, 1)` to a mathematical term.

(And _that_ fails because `is` isn't fully bidirectional. The lhs _must_ be a single variable. You have to import `clpfd` and write `A + 1 #= B + 2`.)

I don't like this, but I'm a hypocrite for saying that because I appreciate the idea and don't mind custom symbols in other languages. I guess what annoys me is there's no official definition of what `^(a, b)` is, it's purely a convention. ISO Prolog uses `-(a, b)` (aka `a-b`) as a convention to mean "pairs", and the only way to realize that is to see that an awful lot of standard modules use that convention. But you can use `-(a, b)` to mean something else in your own code and nothing will warn you of the inconsistency.

Anyway I griped about pairs so I can gripe about `sort`.

### go home sort, ur drunk

This one's just a blunder:
    
    
    ?- sort([3,1,2,1,3], Out).
       Out = [1, 2, 3]. % wat
    

According to an expert online this is because sort is supposed to return a sorted _set_ , not a sorted list. If you want to preserve duplicates you're supposed to lift all of the values into `-($key, $value)` compound terms, then use [keysort](https://eu.swi-prolog.org/pldoc/doc_for?object=keysort/2), then extract the values. And, since there's no functions, this process takes at least three lines. This is also how you're supposed to sort by a custom predicate, like "the second value of a compound term". 

(Most (but not all) distributions have a duplicate merge like [msort](https://eu.swi-prolog.org/pldoc/doc_for?object=msort/2). SWI-Prolog also has a [sort by key](https://eu.swi-prolog.org/pldoc/doc_for?object=predsort/3) but it removes duplicates.)

### Please just let me end rules with a trailing comma instead of a period, I'm begging you

I don't care if it makes fact parsing ambiguous, I just don't want "reorder two lines" to be a syntax error anymore

* * *

I expect by this time tomorrow I'll have been Cunningham'd and there will be a 2000 word essay about how all of my gripes are either easily fixable by doing XYZ or how they are the best possible choice that Prolog could have made. I mean, even in writing this I found out some fixes to problems I had. Like I was going to gripe about how I can't run SWI-Prolog queries from the command line but, in doing do diligence finally _finally_ figured it out:
    
    
    swipl -t halt -g "bagof(X, Goal, Xs), print(Xs)" ./file.pl
    

It's pretty clunky but still better than the old process of having to enter an interactive session every time I wanted to validate a script change.

(Also, answer set programming is pretty darn cool. Excited to write about it in the book!)

* * *

  1. A couple of people mentioned using [dif/2](https://eu.swi-prolog.org/pldoc/doc_for?object=dif/2) instead of `\+ A = B`. Dif is great but usually I hit the negation footgun with things like `\+ foo(A, B), bar(B, C), baz(A, C)`, where `dif/2` isn't applicable. [↩](https://buttondown.com/hillelwayne/rss#fnref:dif "Jump back to footnote 1 in the text")



