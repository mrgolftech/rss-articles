# My Gripes with Prolog

**来源:** https://buttondown.com_hillelwayne
**链接:** https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/
**日期:** Wed, 14 Jan 2026 16:48:51 +0000

---

#  [ Computer Things ](https://buttondown.com/hillelwayne)

[ Archives ](/hillelwayne/archive/)

Search...

[ Subscribe ](https://buttondown.com/hillelwayne#subscribe-form)

January 14, 2026 

# My Gripes with Prolog

## It's not my favorite language

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
    

There's no way to get that behavior with cuts! I don't think `\+` uses cuts at all! And now I have to figure out why `foo(A, B)` doesn't returns results. Is it [floundering](https://github.com/dtonhofer/prolog_notes/blob/master/other_notes/about_negation/floundering.md)? Is it because `\+ P` only succeeds if `P` fails, and `A = B` always succeeds? A closed-world assumption? Something else?1

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

  1. A couple of people mentioned using [dif/2](https://eu.swi-prolog.org/pldoc/doc_for?object=dif/2) instead of `\+ A = B`. Dif is great but usually I hit the negation footgun with things like `\+ foo(A, B), bar(B, C), baz(A, C)`, where `dif/2` isn't applicable. ↩




_If you're reading this on the web, you can subscribe[here](/hillelwayne). Updates are once a week. My main website is [here](https://www.hillelwayne.com)._

_My new book,_ Logic for Programmers _, is now in early access! Get it[here](https://leanpub.com/logic/)._

Don't miss what's next. Subscribe to Computer Things: 

Email address (required)

Subscribe

Join the discussion: 

  1. A

Abil 

January 16, 2026, morning

A, good language it is shud become de facto standard for AI

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/52dd95a8-9363-4c32-adf1-d629512cc055) [Report](mailto:support@buttondown.com?subject=Improper+comment)

  2. C

cjunke 

January 16, 2026, morning

A lot of predicates have a last argument as the result and can thus be used as _evaluation predicates_ for `is/2`. For example: `O is (length([a,b,c]) + 1).`

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/ce81e1da-de4c-4ce4-8e27-90639c27ff64) [Report](mailto:support@buttondown.com?subject=Improper+comment)

C

[ Hillel Wayne ](https://buttondown.com/hillelwayne) Author

January 16, 2026, afternoon

See this is why Cunningham's law is great =)

(I don't think `length` _specifically_ can be used as an evaluation predicate. I tried `A is (length([a,b,c]) + 1)` in SWI-Prolog and Scryer and both threw errors. Do you have another example?)

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/08c2b658-9e4e-4e82-a960-7296165d7b01) [Report](mailto:support@buttondown.com?subject=Improper+comment) [Delete](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/08c2b658-9e4e-4e82-a960-7296165d7b01/delete)

C

cjunke 

January 16, 2026, afternoon

It must be an Eclipse specificity, looking at the code it is implemented with term rewriting. It's a bit unfortunate that there is no uniformity across implementations.

https://eclipseclp.org/doc/bips/kernel/arithmetic/is-2.html

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/f936660f-6bdd-45c0-ba3d-889552a5fe5b) [Report](mailto:support@buttondown.com?subject=Improper+comment)

  3. M

Michael Leuschel 

January 16, 2026, noon

Yes, the cut is confusing. \+ does use a cut, but the cut is executed within the definition of + and will prune away the second clause of +. It does not affect the clauses calling + : +(P) :- P,!,fail. +(_). % <\--- pruned away by cut

For your example member(A, [1,2,3]), + (A = 2), A = 3, this happens: 1) the first call to + will be +(1=2) and the cut is not executed, 1=3 fails, 2) we backtrack to member, then for +(2=2), the call 2=2 succeeds and the cut is called, meaning that +(2=2) fails and 3) we backtrack to member and then get the final candidate A=3 from member for which all calls succeed.

Note, If in foo you use the dif/2 predicate instead of + you will get more natural behaviour. E.g., with foo(A,B) :- dif(A,B), A=1, B=2. you will get the solution you expected. Indeed, in contrast to + or \=, dif is declarative and not binding sensitive (i.e., dif(X,a), X=b is equivalent to X=b, dif(X,a)).

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/69aaba0b-9189-4761-a703-51b0d08f50c9) [Report](mailto:support@buttondown.com?subject=Improper+comment)

C

[ Hillel Wayne ](https://buttondown.com/hillelwayne) Author

January 16, 2026, afternoon

Ah knowing that the "cut" is only within the definition of `\+` is what clears it all up for me, thank you!

Also `dif/2` is great, I don't know why `A \= B` desugars to `\+ (A = B)` and not `\+ (A = B)`

(I know why, it's legacy reasons)

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/5617b23b-adcd-41b9-b129-e5b461304543) [Report](mailto:support@buttondown.com?subject=Improper+comment) [Delete](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/5617b23b-adcd-41b9-b129-e5b461304543/delete)

  4. I

Ivan 

January 16, 2026, evening

Good post, thanks. I (@prologinfo) shared on the old hillside.

You have a robot fan. I don't think they link back here:

https://news.lavx.hu/article/prolog-s-design-quirks-spark-alternative-approaches-in-logic-programming-education

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/88d95ae0-7dd7-4108-9e31-5c41b156d1ae) [Report](mailto:support@buttondown.com?subject=Improper+comment)

C

[ Hillel Wayne ](https://buttondown.com/hillelwayne) Author

January 21, 2026, morning

Wow, they even have the GPT-purple color scheme :D

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/3c0ec66b-9988-4374-bd7e-c8cd01e86abc) [Report](mailto:support@buttondown.com?subject=Improper+comment) [Delete](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/3c0ec66b-9988-4374-bd7e-c8cd01e86abc/delete)

  5. P

Paul Bredbury 

January 17, 2026, morning

To get length of a list, plus 1:

?- List = [a,b,c], length([_|List], Len1). Len1 = 4.

Can use true and false as data values ("terms"), same as yes and no.

Prolog is awesome because it is logical and relational.

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/2e9c354b-5585-45ff-9a9a-ce3d6dedc8fe) [Report](mailto:support@buttondown.com?subject=Improper+comment)

C

[ Hillel Wayne ](https://buttondown.com/hillelwayne) Author

January 21, 2026, morning

I'm generally not a fan of overly clever-but-fragile solutions like, which cleverly solve the specific problem but can't generalize to problem variants. Like what happened if I asked you to get `floor(sqrt(2*length(l)))+1`? In most languages it's an easy one-liner (that probably looks like the pseudocode there), but I don't see an easy way to adapt the Prolog you gave me to get the new equation.

I've written about my discomfort with fragile solutions a couple of times before:

     * [The Problem With APLs](https://www.hillelwayne.com/post/the-problem-with-apls/)
     * [Clever vs Insightful Code](https://www.hillelwayne.com/post/cleverness/)

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/c5c71546-c553-4da0-ae75-0372dda46bfa) [Report](mailto:support@buttondown.com?subject=Improper+comment) [Delete](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/c5c71546-c553-4da0-ae75-0372dda46bfa/delete)

  6. S

Srin nedunuri 

January 20, 2026, afternoon

Its been over a decade sinxe i used Prolog but it seems to me that + (A,B) fails for uninstantiated A and B b/c Prolog isnt lazy so it cannot generate an infinite stream of pairs of numbers that arent equal. Which is what you'd need to move onto the next literal

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/19456f15-e1b2-430f-8ef8-797a7c7fc69f) [Report](mailto:support@buttondown.com?subject=Improper+comment)

  7. P

Peter Ludemann 

January 20, 2026, evening

I've posted a link to your post here: https://swi-prolog.discourse.group/t/hillel-wayne-my-gripes-with-prolog/9484 where it might generate some discussion.

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/aca72618-305f-4446-9a39-500713e37c9d) [Report](mailto:support@buttondown.com?subject=Improper+comment)

C

[ Hillel Wayne ](https://buttondown.com/hillelwayne) Author

January 21, 2026, morning

We'll see what comes of it! I've gotten a bit of flack over the weekend and don't have a discourse account for that group, would you mind posting a couple of clarifying notes? Thanks:

     1. I've been trying to make my newsletter more off-the-cuff and scope each post to much less time, so I ended up being pretty sloppy with the technical aspects! For example, saying rules "return true or false" or that cuts "can lead to invalid programs" (when I meant it could fail to find all valid solutions). I'm being a lot more careful in the book.
     2. Logic Programming is only about 6% of _Logic for Programmers_. Most of the book is about more mundane topics like property testing and database constraints and such.
     3. For every gripe I have about Prolog I have six gripes about TLA+ and Alloy. [Hate Your Tools](https://buttondown.com/hillelwayne/archive/on-hating-your-tools/)!

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/be9dd23e-af4a-406e-9850-235bf2961720) [Report](mailto:support@buttondown.com?subject=Improper+comment) [Delete](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/be9dd23e-af4a-406e-9850-235bf2961720/delete)

  8. D

D 

January 21, 2026, midnight

I think Prolog suffers from the Lisp-curse (Prolog-curse?): any perceived imperfection isn't seen as one, because the gurus can just hack a meta-interpreter in no time (and they are right, I have never come across a more meta-programmable language).

This has led to a zillion libraries doing things that instead should have been standardized at the language level. There are prolog variants with function calls and many modernizations (e.g. Ciao prolog), but they are not widely agreed upon.

In the same vein, Prolog can be typed very easily, but this has been done through libraries (meta-interpreters again), that are fragile and not well-documented. The same goes for typing of the modes of predicates. Here the curse of the symbolic terms (which I think are great, btw.) hits again, because there is no standard as to how to specify types.

Picat is a wonderful language, but, alas, it lacks the metaprogrammability that makes Prolog to interesting. I don't think without metaprogrammability it will ever be able to take Prolog's place.

Another "curse" of Prolog is that SLD resolution over Horn clauses is just on the threshold of what is still computable in linear time. 

Even small changes, such as interpretation of the clauses under stable model semantics, lead to an NP-complete problem. So, while Answer Set Programming is very appealing for many applications, it can't form the basis of a general-purpose programming language. And I am not even speaking about λProlog.

From a complexity point of view, we will never get a more powerful Prolog2 that could realistically solve what Prolog can't.

I love Prolog, I think it is an awesome language, but I also share your gripes. One of the main issues is that, because I need to leave my regular programming environment, I very rarely think about problems the way I would think about programming in Prolog.

In my opinion, we need:

     * a stronger integration of Prolog into other languages. Janus Prolog is a good start. Ultimately, I would love to see a tight integration, like what LINQ did. I know that the Prolog gurus will strongly disagree, but I don't think using Prolog as the main language is the right approach.

     * de-crufting of Prolog, and moving towards a more declarative approach. Markus Triska's approach is refreshing. 

     * integration of specific solvers for higher order logic, ASP etc. s(CASP) is already tightly integrated with Prolog. Similarly, using other solvers, SMB, SMT, need to be a bit smoother, and well-documented.

     * it irks me a bit that we have a split between logic programming, and solvers for logic programming problems (such as OR or SMT), the latter which are typically written in C++. I would love to better understand what logic programming is lacking to be considered here.

     * similarly, a Prolog engine would be a perfect addition to anything where backtracking is needed. Attributed variables, https://www.metalevel.at/prolog/attributedvariables , are incredibly powerful as the attributes are automatically sync'ed with the search state. Building such a system by hand is extremely error prone. This integration is what makes it possible to seamlessly integrate constraints into Prolog. 

Unfortunately, there is disagreement in the community as to which solution is best, this has ultimately led to the creation of Scryer Prolog. Details are here: https://github.com/SWI-Prolog/roadmap/issues/14

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/55dd85a0-9ee5-46ce-a8a3-92b95f9ebc8e) [Report](mailto:support@buttondown.com?subject=Improper+comment)

  9. P

Peter Ludemann 

January 23, 2026, afternoon

I can recall the problems with "cut" and "not" being discussed in the 1980s ... there are now a number of solutions: \- if-then-else (note that *-> does backtrack over the condition) \- Picat/Haskell style single-sided-unification \- freeze/2 for delaying the computation of a "not" until the arguments are sufficiently instantiated \- attributed variables (a generalization of freeze/2)

Yes, setof/3, bagof/3, find all/3 are confusing (see also library(aggregate)). These have to do with the implicit "for all" qualification which requires being explicit about "there exists" -- one solution is to write auxiliary predicates rather than trying to be clever for complex goals ... this also gets into problems with free variables, which have never been satisfactorily resolved (e.g., library(yall) allows something like lambda expressions; but can lead to surprises similar to the "exists" surprise in set of/3).

AST is a nicer approach than setof/3 and friends; but it also comes at a computational cost. Similarly, Constraint Logic Programming (https://www.swi-prolog.org/pldoc/man?section=clp) generalizes the handling of "not", but also at a computational cost.

Picat takes a different approach (e.g., it doesn't allow treating code as data) and has some much more powerful features -- it's great for solving "Advent of Code" problems -- but if you read its forum, you'll see subtle difficulties with using its various solvers.

None of these solution are fully satisfying, but many are related to how to handle the undecidability parts of first-order logic, and how to handle competing design goals (e.g., better handling of variable scope would cause problems with manipulating programs as data)

(I could a long list of other issues in Prolog: scope of names, macros, modules, foreign-language interfaces, compatibility with (relational) databases, etc., etc.)

Such conundrums aren't unique to Prolog -- look at all the variants of Lisp where what seem like minor changes to semantics in edge cases result in new languages (e.g., Scheme). 

I suspect that one sign of a language being useful is that some of its features are controversial.

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/69d6c74f-c9bd-411a-a252-b9833ba2f0cf) [Report](mailto:support@buttondown.com?subject=Improper+comment)

  10. D

D 

January 27, 2026, morning

@Peter, very interesting comments!

To me, the appeal of prolog stems from its metaprogramming capabilities, continuations, coroutines, attributes, cut, call, etc. That's why Picat has less appeal, despite the fact that it fixes many of Prolog's warts.

Without control of the execution strategy, why not just use SQL for data-heavy applications, and an SMT or OR-specific solver for logic problems?

At least, SWI has adapted =>/2 for single-sided unification, https://www.swi-prolog.org/pldoc/man?section=ssu.

An interesting paper on the if-then-else issue is "indexing dif/2" https://arxiv.org/pdf/1607.01590

You've been around during the heyday of Prolog, do you happen know why it was never able to get a foothold in the OR or logic solver worlds? 

[Reply](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/comment/ce8c65c6-2291-4c8d-8e3e-d2bf678c474b) [Report](mailto:support@buttondown.com?subject=Improper+comment)




#### Add a comment:

Comment and Subscribe 

Share this email:

[ Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A//buttondown.com/hillelwayne/archive/my-gripes-with-prolog/&title=My%20Gripes%20with%20Prolog) [ Share on LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//buttondown.com/hillelwayne/archive/my-gripes-with-prolog/) [ Share on Hacker News ](https://share.bingo/hn?url=https%3A//buttondown.com/hillelwayne/archive/my-gripes-with-prolog/) [ Share on Bluesky ](https://share.bingo/bluesky?url=https%3A//buttondown.com/hillelwayne/archive/my-gripes-with-prolog/)

Powered by [Buttondown](https://buttondown.com/refer/hillelwayne), the easiest way to start and grow your newsletter.
