# In which I have Opinions about parsing and grammars

**来源:** https://chiark.greenend.org.uk/~sgtatham
**链接:** https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/parsing/
**日期:** 2025-06-05T00:00:00+00:00

---

# In which I have Opinions about parsing and grammars

[Simon Tatham, 2025-06-05]

  * Introduction
  * Context-free grammars are less declarative than youâd like
    * A simple grammatical concept becomes complicated when written as a CFG
    * CFGs must be tailored to the parser technology
  * You probably want to handwrite your production parser
  * Name a parser generation technology in your language spec
  * Use LR parser generators during language design
    * Because they can point out design errors
    * Because they can generate test cases
  * Stop doing LALR
  * Grammars should be synthetic as well as analytic
  * OK, what _should_ you do?
    * Compile a simpler form into an LR grammar?
    * LR with attributes?
  * Bodges to handle non-LR languages
  * Conclusion
  * Footnotes



## Introduction

Iâve been interested in parsing since I was a teenager. I first got into the subject by reading the [dragon book](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools) in the early 1990s. (Thatâs about compilers in general, but the parsing chapter is a major part of it.) Then I played around with parser generators; my first one was [TPLY](https://github.com/jmrcpn/tply/), since as a teenager I was a Turbo Pascal programmer.

In my time, Iâve designed and implemented entire (small, toy, personal-project) programming languages from scratch, which of course needed parsers along with all the other components of a compiler or interpreter. Iâve tried to write parsers for existing languages, and found some of the ways that can go wrong. Iâve put some effort into understanding the theory of parser generators (particularly LR). Iâve used automated parser generators, hand-written my own parsers, and even tried _writing_ an automated parser generator.

In all that activity, Iâve formed a lot of opinions. This article attempts to get all of them off my chest at once, in a series of not entirely connected rants.

## Context-free grammars are less declarative than youâd like

Context-free grammars â either written out directly as a list of rules (sometimes also known as âBackus-Naur Formâ or BNF), or converted into the slightly more graphical form of a [syntax diagram](https://en.wikipedia.org/wiki/Syntax_diagram) â are more or less the gold standard for specifying the syntax of a language.

One reason theyâre popular is that the specification doesnât itself look like a _program_. It looks as if you just specify the rules of the grammar in a more or less natural way, and donât have to confuse the reader with any of the difficult algorithms that actually figures out what the input means. The usual term for this is âdeclarative programmingâ: I just specify _what I want_ in a simple and direct way, and the language doesnât force me to engage with the details of _how to calculate it_.

When this works, itâs great. This (slightly simplified) list of statement types in a language like C, for example, could hardly be clearer:

statement â expression ;

statement â return expression ;

statement â { declarations-and-statements }

statement â if ( expression ) statement

statement â if ( expression ) statement else statement

statement â while ( expression ) statement

statement â do statement while ( expression ) ;

statement â for ( expression ; expression ; expression ) statement

statement â continue ;

statement â break ;

statement â switch ( expression ) statement

statement â case expression : statement

statement â default : statement

statement â goto label ;

statement â label : statement

(Iâll reuse this notation for grammars throughout this article. In case itâs not already obvious, Iâm using a bolded word or punctuation mark in a green box, like while or {, to represent an individual _token_ communicated from the lexer to the parser, otherwise known as a _terminal symbol_ of the grammar; and Iâm using an italic word in a rounded blue box, like statement, to represent a _nonterminal_ symbol â one representing a larger subsection of the input program, potentially consisting of a string of many tokens, or sometimes even none.)

This is a straightforward enough description that you can learn this aspect of the language directly from it. If I want to _write_ , say, a `do`-`while` statement in C, and I havenât learned what one looks like yet, I have only to find the right line of the above and work my way along it writing each token or grammatical subcomponent as I go. And at the same time it can also be handed to an automated parser generator. Ideal, right?

Unfortunately, not always. Iâve cherry-picked a particularly successful example here, but in other cases, CFGs _donât_ achieve the ideals of declarative programming1My other example of a thing advertised as âdeclarativeâ which doesnât deliver on its promise is functional programming. Iâm not saying FP has no virtues, but declarative it is not. For example, to write a sorting function in a language like Haskell, you must decide which actual sorting algorithm you want to use; you can write very different Haskell functions that look like quicksort or mergesort or some other sort, and the compiler will generate the algorithm you asked for. My litmus test for a language worth calling âdeclarativeâ would be that I can write a sorting function by simply specifying the _properties_ I want the output list to have, without saying anything about _how_ to achieve it: it should be a permutation of the input list, such that _a_[_i_] â¤ _a_[_i_ +1] for all _i_.1. When youâre writing a CFG, you _do_ have to think about implementation, in two separate senses, which Iâll discuss below.

### A simple grammatical concept becomes complicated when written as a CFG

The first part of the notion of âdeclarativeâ is that I should be able to say what I want, in a simple and direct way. Transferring the idea in my head to the source file should be easy, and reading the source code to recover the idea should be equally easy.

But itâs not, in every case.

Translating your mental notion of the languageâs grammar into CFG rules is itself an exercise in programming: you have to know the non-obvious pitfalls and the tricky rewordings needed to avoid them, and you have the usual tension between wanting to factor out commonly used idioms into explicit subthings, and wanting to keep each grammar rule self-contained and clear. Itâs entirely possible to write _bugs_ in grammars.

Even in the clear-looking C example above, the seeds of this problem are already sown. My example `for` statement was in the C89 style, where all three clauses are plain expressions. But C99 introduced the option to declare a new variable in the initialisation clause: â`for (**int i** = 0; â¦)`â. The grammar rule for _that_ version of `for`, in the C99 standard, is already less clear.

statement â for ( declaration expression ; expression ) statement

Whereâs the semicolon gone, in between the first two clauses? Itâs included in the nonterminal declaration: because of the way that symbol is used in other contexts, itâs defined so that it expands to a sequence of tokens that _includes_ the trailing semicolon, and so it would be a mistake for this rule to write a ; after the declaration, or youâd end up accidentally specifying a language in which _two_ semicolons were needed between the first two clauses. As a grammar author, you could easily make this mistake â and if you werenât _testing_ your grammar in some way, you might miss the error completely, and publish a nonsense specification. Meanwhile, as a grammar _reader_ , you see this and scratch your head, and then have to go and look up the definition of declaration elsewhere to figure out what you missed.

Similarly, some of the grammar rules above _end_ with a ;, and some donât â because some of the statement types end with another entire statement, which includes its own trailing ; and so another one isnât needed. When a beginner learns C (or any other language with even slightly similar syntax), one of the earliest rules they must internalise is that _every_ statement ends with a semicolon2Except that a braced block counts as a statement by this grammar, and doesnât have a semicolon after the closing brace. So even this âobviousâ fact about C syntax depends a bit on your point of view.2. And yet you have to look carefully, and think hard, to convince yourself from the list of rules above that this is true.

Another pitfall in the example above is the well-known if-else ambiguity, arising from these two rules:

statement â if ( expression ) statement

statement â if ( expression ) statement else statement

because the grammar doesnât explain which way to interpret an input sequence of symbols such as this:

if ( expression )

if ( expression )

statement else statement

Is that an outer if-without-else, whose then-clause contains an if-with-else? Or is it an outer if-_with_ -else, whose then-clause is an if-without-else? In other words, which of the two `if`s does the single `else` bind to? Thereâs a very standard answer to this question in practice: the `else` is always considered to bind to the the last unmatched `if`. But the grammar as written doesnât _say_ that thatâs the answer. That information is communicated separately. In the C standard itâs written in prose, alongside the list of grammar rules. If you feed the same set of rules to an automated parser generator, youâll have to look up how your parser generator resolves ambiguities, and whether in this case it will do the thing you want, and if not, how to tell it to do something different.

You _can_ write an unambiguous context-free grammar for a language containing both types of if-statement. But it requires some puzzle-solving ingenuity to come up with. And it _hugely_ impacts comprehension, to a reader whoâs trying to learn _what the language is_ from the written grammar.

The gory details: an unambiguous grammar for C statements

You do it by dividing the nonterminal statement into two subclasses: one representing a âbalancedâ statement, in which there are no ifs without else clauses, and one representing an âunbalancedâ statement. The idea is that an unbalanced statement is precisely a token sequence that you only chose to parse as a complete statement _because_ it wasnât followed by an else token; if it had been, youâd have parsed a longer token sequence as a different statement.

So you start with the top-level rules that say that the overall category statement can be whichever it likes:

statement â balanced-statement

statement â unbalanced-statement

Many statement types are automatically balanced. These include a braced block containing other statements, because any imbalance _inside_ the block is safely wrapped up by the braces â thereâs no way that an else _outside_ a pair of braces would ever be considered to bind to an if _inside_ them. Similarly, the do and while tokens have the same bracketing effect, so that a do-while statement is balanced no matter what kind of statement it contains.

balanced-statement â expression ;

balanced-statement â return expression ;

balanced-statement â { declarations-and-statements }

balanced-statement â do statement while ( expression ) ;

balanced-statement â continue ;

balanced-statement â break ;

balanced-statement â goto label ;

Thereâs just one statement type which is automatically _not_ balanced, no matter whether its final statement is balanced or not:

unbalanced-statement â if ( expression ) statement

The remaining statement types, like `while` and `for` loops, are balance-preserving: each one ends with a statement, and is balanced if and only if that sub-statement is. We could write out each rule twice, for balanced and unbalanced statements. But I think itâs more convenient to introduce a third nonterminal, describing a âstatement prefixâ: anything you can stick on the front of an existing statement to make a larger statement, in such a way that balance and imbalance are preserved.

So we can express _just once_ the idea that statement prefixes preserve balance:

balanced-statement â statement-prefix balanced-statement

unbalanced-statement â statement-prefix unbalanced-statement

And then we can write out each of the actual statement prefixes just once:

statement-prefix â if ( expression ) balanced-statement else

statement-prefix â while ( expression )

statement-prefix â for ( expression ; expression ; expression )

statement-prefix â switch ( expression )

statement-prefix â case expression :

statement-prefix â default :

statement-prefix â label :

The key detail in the above list is: in the if statement _with_ an else-clause, the then-clause has to be a balanced-statement. So itâs just not _legal_ to insert an elseless if in that slot, because that would be an unbalanced-statement, and wouldnât match the rule.

I hope you see what I mean about readability! This doesnât look like a simple description of the language syntax any more. It looks like a complicated computer program.

Perhaps it would have been more readable to a language learner if I hadnât done the statement-prefix business, and instead just written the duplications out longhand, e.g.

balanced-statement â while ( expression ) balanced-statement

unbalanced-statement â while ( expression ) unbalanced-statement

and the same for all the rest of the statement prefixes? But even if thatâs true, now weâre trading off good programming practice against readability. When the next version of the C standard adds another statement prefix, the DRY version of this grammar with a statement-prefix nonterminal offers less risk of mistakes when updating the grammar. But a reader trying to learn _this_ version of the language might well prefer the WET version which doesnât factor out the statement prefixes.

The other very common example of needing a complicated grammar for a simple syntax is the problem of operator precedence in infix expressions. If you just write something like this:

expression â variable-name

expression â literal-constant

expression â ( expression )

expression â expression + expression

expression â expression â expression

expression â expression Ã expression

expression â expression Ã· expression

then you have the usual problems. Is an expression like `1+2Ã3` interpreted as `1+(2Ã3)`, or as `(1+2)Ã3`? Does `1â2â3` mean `1â(2â3)` or `(1â2)â3`? Of course, we know which one we want in each case, but the above grammar certainly doesnât _say_ it. If you write the grammar as above, then you have to either communicate that information out of band, perhaps using a precedence table in a written specification, or magic directives to your automated parser generator, like `%prec` in Bison.

So, again, the context-free grammar _itself_ doesnât make it easy to âjust write what you meanâ. You _can_ write a CFG that makes operator precedence unambiguous, but itâs long and verbose and involves introducing a lot of extra nonterminal symbols.

Further details: an unambiguous grammar for infix expressions

The way to deal with this is to add a nonterminal symbol for each precedence level. The innermost one is an âatomicâ expression, describing a token sequence that _absolutely must_ form a self-contained subexpression: it canât possibly be split up and re-parsed differently, no matter what operator appears next to it on either side. This includes any single token thatâs a subexpression by itself, and anything in brackets:

atomic-expression â variable-name

atomic-expression â literal-constant

atomic-expression â ( expression )

Then we work down the precedence levels, highest to lowest. In our simple four-operator example, the highest precedence level is shared by the Ã and Ã· operators. So we define a symbol for a âmultiplicative expressionâ, which is an expression that takes one or more atomic expressions, and does multiplications and divisions to them:

multiplicative-expression â multiplicative-expression Ã atomic-expression

multiplicative-expression â multiplicative-expression Ã· atomic-expression

The right-hand side of each of those rules is asymmetric. On the left of the operator is another _multiplicative_ expression: one thatâs allowed to contain another unbracketed Ã or Ã· operator. But on the right is an _atomic_ expression, which canât contain any infix operators at all unless it safely wraps them up in brackets. This asymmetry expresses the fact that, at this precedence level, the operators âassociate to the leftâ: `aÃ·bÃc` is parsed as a multiplication whose left operand is a division, i.e. like `(aÃ·b)Ãc`. If Iâd written the rules the other way round, with the multiplicative-expression on the right instead of the left, then Iâd have made the operators âassociate to the rightâ.

Associating to the right is the normal choice for _some_ mathematical operators. In particular, the âraise to a powerâ operator: itâs better to interpret `2^3^4` as `2^(3^4)`, because if you interpret it as `(2^3)^4` then thatâs saying the same thing as `2^(3Ã4)`, which you already had a way to say. So there isnât one right way to write each of these rule sets: for each precedence level, you have to decide how the operators associate, and write the rules differently depending on your choice.

(There are other options! If Iâd put an atomic-expression on _both_ sides of each rule, Iâd have defined a syntax in which you just arenât _allowed_ to chain the same operator twice, without adding brackets to say which way you mean it to be interpreted. More subtly, by introducing yet more nonterminals, itâs possible to define a set of operators each of which can associate with _itself_ freely, but they canât associate with _each other_. In languages I design myself I like to use this trick for the `AND` and `OR` operators: you can write `a AND b AND c`, but if you write `a AND b OR c` you must add brackets to clarify.)

Iâve left out one rule. A multiplicative expression is _allowed_ to contain an unbracketed Ã or Ã· operator. But it doesnât _have_ to. We must also specify that a multiplicative-expression is allowed to do _zero_ multiplications and divisions to its input atomic expressions: it can contain just _one_ atomic-expression, and pass it through without doing anything to it.

multiplicative-expression â atomic-expression

Now weâre done with the multiplicative operators, and we move on to the additive ones, + and â. These work exactly the same way, except that the inputs to an additive expression donât have to be _atomic_ expressions: they can be multiplications or divisions, without the Ã or Ã· operators inside them having to be bracketed. In other words, they can be any multiplicative-expression:

additive-expression â additive-expression + multiplicative-expression

additive-expression â additive-expression â multiplicative-expression

additive-expression â multiplicative-expression

If there were more levels of operator precedence, weâd continue down the list, inventing yet another name at each stage, with each new nonterminal consuming instances of the previous nonterminal and chaining them together with operators of the next lower priority. In the full C expression grammar, there are a staggering _seventeen!_

Which of these nonterminals should have the honour of being called just plain expression? Generally the outermost one, dealing with the lowest-priority operators. Where the syntax of the rest of the language calls for an expression, thereâs normally no restriction on what operators you can use, so the grammar would specify the nonterminal that allows _any_ operator to appear without brackets. In particular, thatâs certainly the right nonterminal to use for the _contents_ of a pair of brackets, back up there in the rule that turns a bracketed expression into an atomic-expression: the whole point of brackets is that they should let you wrap up anything at all safely.

In C, in fact, this is only _mostly_ true. The outermost, lowest-priority nonterminal is used in _most_ contexts where the language as a whole calls for an expression. But thereâs an exception. The lowest-priority operator in C is the comma operator: the expression `x,y` means âevaluate `x`, performing any side effects like output or modifying a variable, and then return the value of `y`â. But commas are also used to separate the arguments of a function call. So in the argument list of a function call, the reference C grammar says that each argument must be the expression nonterminal for the _second_ -lowest precedence level: the nonterminal thatâs allowed to contain any operator unbracketed _except_ a comma. (Which doesnât mean you _canât_ use the comma operator in a C function argument â it just means you have to put brackets around it, to prevent the language from seeing it as an argument separator.)

So, despite the initial promise, writing a context-free grammar in a way that is unambiguous is just like using a programming language. You _canât_ just âwrite what you meanâ. You have to know all the tricks for how to translate the simple ideas in your head into the details that will actually work. And those tricks involve introducing extra complexity, which trades off readability in return for ease of maintenance and reducing the probability of making mistakes: refactoring, reorganising, adding internal identifiers that arenât particularly meaningful to an end user.

### CFGs must be tailored to the parser technology

The second element of âdeclarativeâ is that I shouldnât have to worry about the algorithm used to compute what I asked for. Itâs my job to say what it is, and the softwareâs job to find a way to get it for me.

CFGs donât reliably satisfy that aspect either!

You also have to consider the implementation of the parser generator your grammar will be fed to, and depending which one it is, extra constraints arise.

Some parser generation strategies allow you to write each individual rule in a way thatâs more expressive than a plain list of symbols. You can use some regular-expression-like operators, tagging a symbol as optional, or allowed to be repeated any number of times. This tends to be a feature supported by LL parsing tools, because in the LL strategy, you know early which production for a symbol youâre looking at, and can concentrate on just that one production. LR finds this harder because it tries to keep multiple possibilities in mind until the last moment.

For example, in my example list of C statement types above, I simplified the real syntax by leaving out some of those âoptionalâ markers. For example, the `for` statement ought to have all three of its expressions optional:

statement â for ( expressionopt ; expressionopt ; expressionopt ) statement

(Iâve used the notation of the C standard here: a subscript âoptâ to indicate that a symbol is optional. Some parser generators will use a suffix `?`, like a regular expression.)

Not all parser generators support this extended syntax. If one doesnât, you have to make an extra symbol to use instead:

statement â for ( expression-opt ; expression-opt ; expression-opt ) statement

expression-opt â expression

expression-opt â Îµ

(The Îµ on the right-hand side is mathematical notation for the empty string. It doesnât represent a true symbol of the grammar: you wonât ever find one pushed on the LR parse stack, for example. In code, youâd just have a zero-length list of symbols on the right-hand side of that production. The Îµ is just a marker in the written notation, indicating that this grammar production _intentionally_ has an empty right-hand side, and I didnât accidentally leave it half-written!)

Similarly, if your parser generator wonât let you write a `*` or `+` suffix to indicate that a RHS symbol is repeatable, you have to make a special symbol for a list of them. For example, in the C statement list, I used the symbol declarations-and-statements inside the braced block statement (expecting that it would be obvious what it meant). If you were encoding this properly in an LR system like Bison, youâd have to expand it like this:

declarations-and-statements â declarations-and-statements declaration

declarations-and-statements â declarations-and-statements statement

declarations-and-statements â Îµ

which says that a declarations-and-statements can be empty, or else it can consist of another instance of itself followed by a declaration or a statement. In other words, you end up with a list of zero or more declarations and statements, intermixed in any order.

But this brings me to the next point: for different parser generation technologies, you donât even write _that_ the same way.

You could equally well have chosen to write this list symbol with the recursion on the right-hand side rather than the left:

declarations-and-statements â declaration declarations-and-statements

declarations-and-statements â statement declarations-and-statements

declarations-and-statements â Îµ

This has exactly the same meaning in terms of what sequences of tokens are allowed. But if youâre using an LL parser generator (and it doesnât have a repetition operator you can use instead), you need to write it this way round, because LL grammars fundamentally arenât allowed to _left-recurse_ : a production for a symbol foo may not start with another foo, or even with another symbol capable of becoming a foo again after further expansions.

So maybe you should write this kind of list symbol with the recursion on the right _always_ , so that LL and LR parser generators can both cope with it? Not a good idea, unfortunately. Itâs true that LR _can_ handle the right-recursive form, but itâs less efficient, because a long list of statements would all have to be pushed on the parse stack in sequence before the parser could start combining them into larger and larger declarations-and-statements instances. Using the left-recursive form, the parser immediately makes an empty declarations-and-statements on the stack, and then folds each incoming declaration or statement into it, so the stack size stays bounded.

In this case, efficiency is the only consideration when deciding whether to write a thing one way round or the other, because these statements are just being combined into a plain list, and _after_ youâve constructed the whole list, it doesnât matter whether you built it up from the right-hand end or the left. But in some cases it makes a semantic difference which way round you write one of these constructions. For example, consider this simplified grammar for infix subtraction:

expression â NUMBER

expression â expression â NUMBER

If Iâd written _that_ rule the other way round, as NUMBER â expression, it would make a difference to the meaning. An expression like â`123â234â345`â would have to be parsed as 123 â (234 â 345), whereas the original rule parses it as (123 â 234) â 345, the way we wanted it.

So this subtraction grammar _must_ left-recurse in order to mean what we want it to mean. But then how do you express it at all in an LL system, under the constraint that you _mustnât_ ever left-recurse?

You have to introduce a âtailâ symbol, something like this:

expression â NUMBER expr-tail

expr-tail â â NUMBER expr-tail

expr-tail â Îµ

This avoids left-recursion, and matches the right set of strings of tokens. But converting it into an abstract syntax tree has to be done by more awkward methods than usual: you canât just associate each nonterminal symbol with an AST node in the usual way, because expr-tail by itself _doesnât_ represent an AST node for a subexpression! Instead, it represents some kind of _function_ , transforming one AST node into another.

So a lot of common constructions in language syntax have to be expressed using quite different context-free grammars, depending on the parser technology you plan to feed the grammar to. And some of those grammars look very confusing and unintuitive, compared to the simple idea of the languageâs syntax that you had in your head before you sat down to write a formal grammar.

Hereâs another annoying case. Going back a bit to the âoptionalâ thing I mentioned at the start of this section, supposing I wanted to write a syntax for specifying a range of numbers, with one or other end of the range allowed to be omitted, but not both. That is, I could write `[50,100]`, or `[50,]`, or `[,100]`, but not `[,]` with both endpoints missing.

If youâre allowed the âoptionalâ suffix, you might try writing something like this:

interval â [ endpointopt , endpoint ]

interval â [ endpoint , endpointopt ]

But this is ambiguous â if _both_ endpoints are provided, then the parser generator will report that it doesnât know which of the two productions to use, because both match! This is a phenomenon I think of as a âbenign ambiguityâ: the grammar is formally ambiguous, but both parses translate into the same AST, so it doesnât really matter. Even so, one normally wants to avoid even _formal_ ambiguities, to keep the parser generator happy, so perhaps we write this instead:

interval â [ endpointopt , endpoint ]

interval â [ endpoint , ]

This is formally unambiguous, because the rules clearly canât both match: the first rule only matches intervals where the right endpoint is present, and the second only matches where the right endpoint is absent.

But now try translating this into pure LR, where youâre not allowed the âoptionalâ suffix. You get this:

interval â [ endpoint-opt , endpoint ]

interval â [ endpoint , ]

endpoint-opt â endpoint

endpoint-opt â Îµ

This grammar is unambiguous, and avoids using any extensions of the CFG concept. But, annoyingly, itâs not LR(1)!

An LR parser for this grammar, if itâs given an input in which the first interval endpoint is present, will reach a state in which it has [ endpoint on its parse stack, and is looking at the , that follows it. Now it must make a decision: shift the , immediately, or reduce the endpoint into an endpoint-opt first?

Whichever way it decides, it might regret it when it sees the next symbol. If thereâs another endpoint, then it will need to have reduced the first one into an endpoint-opt; if there isnât, it will need _not_ to have done that. And it canât go back and change its mind once it finds out which: the LR parsing system only permits reductions at the top of the parse stack. Once youâve shifted the , on top, itâs too late to go back and do a reduction lower down.

In this case, the grammar isnât LR(1), but it _is_ LR(2): with _two_ tokens of lookahead, the parser could see whether the token following the , is a ] or not, and make its decision based on that. But in a more complicated case where the separating , token is replaced by some other nonterminal that can expand to arbitrarily many tokens, a grammar of this kind wouldnât be LR(_anything_).

If you get into this kind of situation when designing your grammar, there are a couple of ways to fix it. One is to avoid using an intermediate nonterminal, by instead expanding out the two possibilities in full as parallel productions for interval:

interval â [ endpoint , endpoint ]

interval â [ , endpoint ]

interval â [ endpoint , ]

That avoids the indecision between endpoint and endpoint-opt, because there _is_ no endpoint-opt any more. But itâs more verbose, and makes the grammar harder to maintain or read. (Imagine if you had to do this to more than two optional things â say, the three clauses of a C `for` statement. Youâd expand into 8 separate productions, or whatever subset of them you wanted.)

Perhaps a _better_ approach is to make the grammar deliberately match _too much_ , by not forbidding the case where both endpoints are missing! Then you only need one production for interval (plus the definition of endpoint-opt as above):

interval â [ endpoint-opt , endpoint-opt ]

Of course, now your parser will accept some token sequences that you didnât intend to be legal. But you can detect them afterwards, when you examine the finished parse tree (or eagerly in a Bison action at the moment of the reduction, if you prefer), and give a custom error message of your own instead of relying on the parser generatorâs general method of reporting syntax errors. That seems inelegant because now you need an extra error-checking pass on top of your autogenerated parser â but donât forget that in any nontrivial language youâre likely to follow up the parsing phase with a lot of semantic analysis and error checking anyway: matching up variable references to definitions, figuring out the type of everything, and reporting errors if anything doesnât match. So this is just another check that goes into the semantic analysis phase. Plus, writing the message yourself allows you to make it clearer to a reader: you can explain âan interval must specify at least one of its endpointsâ instead of just âparse error, expected [some token]â.

There is one parsing strategy that will _never_ require you to contort your grammar in the ways described in this section (although you still have to worry about the things in the _previous_ section, where you have to contort the grammar just to make it unambiguous in the first place). Thatâs the [Earley parser](https://en.wikipedia.org/wiki/Earley_parser), which can handle any context-free grammar at all, without insisting that you convert it into any particular restricted form. But you pay for it in speed: an Earley parser can take quadratic time to run (or cubic if the grammar is ambiguous). I donât know of anyone whoâs actually taken this option in a production compiler.

## You probably want to handwrite your production parser

Automated parser generators sound like a great way to write parsers. They have the same advantages as automating anything else: faster, easier, and less chance of human error.

But generally, if youâre writing a _serious_ tool that involves a parser â one that you hope will be used by many users, because you aim for it to become a widely used free software project, or are going to sell it to paying customers â it isnât a good idea to use an autogenerated parser.

For example, GCC â the very widely used GNU C compiler â started off using autogenerated parsers, but switched to handwritten ones (in [GCC 3.4](https://gcc.gnu.org/gcc-3.4/changes.html#cplusplus) for C++, and in [GCC 4.1](https://gcc.gnu.org/gcc-4.1/changes.html) for C).

There are a couple of reasons why you might do this. One is that it gives you greater flexibility to keep the parser working if the language spec does something weird: if the next version of C decides to have a grammar that doesnât go through `yacc` successfully any more, youâll be glad you didnât commit 100% to `yacc` as your parsing strategy. (I expect that was why GCC had to rewrite their C++ parser more urgently than C.)

But the really big reason is that autogenerated parsers just donât write good error messages.

Automated parser generators are usually very good at reliable error _detection_. For example, the LR algorithm will report an error on precisely the first input symbol which rules out the possibility that the input can be continued in any way that completes a syntactically legal program. But when it comes to explaining to the user what the error _is_ , theyâre not so great.

Traditional Yacc would just report something content-free like âparse errorâ: it would cite a specific location in the input, but beyond that, it was up to you to work out what the problem was. More up-to-date Bison can manage âI expected one of [these] tokens, but saw [this] one insteadâ, which is at least a bit more information than the content-free âparse errorâ, but it can still be difficult for a user to understand _why_ the parser was expecting a different set of tokens, because it canât say anything about what context it thought those tokens were in.

Hereâs a concrete example. Suppose youâre writing a parser for C. In C, function definitions canât be nested. Now suppose a user has written some code like this, which accidentally leaves out the closing brace of a `for` statement:
    
    
    int first_function(int *array, size_t size) {
        int result = 0;
        for (size_t i = 0; i < size; i++) {
            result *= 37;
            result += array[i];
        // here the user should have written } but accidentally didnât
    }
    
    int second_function(void) {
        return 42;
    }

Any parser that consumes the source file from start to end will be happy as far as the opening brace of `second_function`. But that brace is syntactically invalid, because according to the actual source file, weâre still inside `first_function` at this point (we need to see another `}` to finish it), and you canât start defining a function inside another function.

The _ideal_ compiler error message in this situation would point at the location at the end of the `for` statement in `first_function`, where the missing brace should be. But it would take a truly mind-reading C compiler to reliably give _that_ error message! It might be possible to suggest a likely error location based on the indentation, but not with 100% certainty.

If youâre not imagining a mind-reading compiler, then youâre probably constrained to give an error message pointing at the place where the parser stopped being able to make sense of the code: the opening brace of `second_function`. What should the message say?

I think a reasonable error message is something like âyou canât define a function inside another functionâ. The location we point at is not where the actual mistake is, but the user will see this message and think âWait, why do you think this is inside another function? Itâs supposed to be at the top level. Perhaps I havenât closed all the braces?â They may not instantly know where to look for the missing `}`, but the hint that the parser _thinks_ itâs still inside a function is enough to make them go and look for one _somewhere._

But an automated parser generator, with automated error messages, would only be able to point at the brace and report something like âParse error, expected `;` or `,` insteadâ. (A semicolon in place of the brace would make `int second_function(void);` a _declaration_ â stating that a function exists and what its type is, but not providing its body â and function declarations _are_ legal inside a function. A comma would be fine too, because a declaration can contain a comma-separated list of things to declare.)

So, given _that_ error message, the user has to solve a puzzle game: given _that_ list of acceptable next tokens, what context does the parser imagine itâs in?

To some extent this difficulty is inherent in the LR parsing techniques, because part of the point of the LR automaton is to keep an open mind until the last minute about _what_ context itâs in. In terms of being able to parse a larger set of grammars, this is precisely LRâs _advantage_ over LL: LL needs to be able to tell near the start of a statement what kind of statement it is, but in many cases LR can deal with not knowing the answer until the end, or even one symbol _after_ the end. So even if a user was happy to receive a description of context in terms of the grammar symbols rather than natural language, LR would still have trouble, because it canât always narrow down to just one.

LL techniques narrow down to a single context earlier, so it would be easier to give a message describing that context. Indeed, handwritten recursive-descent parsers are often _structured_ in the LL style, allowing the author to know enough about the context to think of a good wording for each error message. But itâs still hard for an automated parser to produce a _human-readable_ description of the context. (Perhaps you could annotate a formal LL grammar with text descriptions of contexts which could be included in autogenerated error messages? But Iâve never seen this approach tried.)

So if weâre not going to use automated parser generators in our final production compilers, are they good for anything at all?

Yes, I think they still are. Theyâre good for rapid development â getting a parser up and running in the first place _before_ it reaches production quality, or one thatâs never going to need to reach production quality at all. But also, more importantly, theyâre good during language _design_ , when you havenât finalised the language syntax yet and keep changing your mind. Iâll discuss that in a [later section](design).

## Name a parser generation technology in your language spec

In a previous section Iâve described various ways in which a context-free grammar has to be written in a different style, depending on what parsing tool you intend to feed it to. In other words, not every context-free grammar is suitable for every parsing tool.

So, suppose Iâm reading the specification for a programming language, and it describes the language syntax using a context-free grammar. If Iâm planning to write an implementation, then probably one of the first things I might do is to feed that grammar to a parsing tool, to autogenerate a parser for it.

(As I said earlier, I might well not keep that parser for ever. But itâs useful to get _some_ kind of parser up and running quickly; I can polish it later, once all the more interesting parts of my implementation are working.)

OK â so _which_ parsing tool do I feed your language specâs grammar to? It probably wonât work with all of them, for all the reasons I mentioned earlier â left versus right recursion, extensions of the CFG notation, etc.

One particular annoyance in a language specification is if it provides a context-free grammar and _doesnât say_ what parsing technology the author thinks that grammar is compatible with. Now Iâve got to solve a puzzle game! Maybe Iâll study the grammar rules looking for left-recursion (which would mean the LL algorithm canât handle it), or notice whether there are any âoptionalâ or ârepeatedâ markers (LR systems usually donât provide those). Or maybe I just paste the grammar into every tool I can find and see which one doesnât give an error message.

Thereâs no purpose to making every implementor solve this puzzle game. The author of the grammar surely _knew_ of a specific parsing tool that itâs compatible with. All they had to do was _write that down!_

So my ranty opinion is: **if you include a BNF grammar in your language spec, state what technology you expect it to be compatible with.**

As Iâll discuss in the next section, _I_ think that the best choice is LR. But if you donât like LR for some reason â even if you prefer LL, or PEGs, or something I havenât even thought of â then say what you _did_ use.

Better still, provide the grammar **in a machine-readable form** 3Since Iâve used C as an example already in this article: the C standard scores one out of two points here. Annex A of the C standard provides a full context-free grammar, and states specifically that itâs acceptable to `yacc`, i.e. to the LALR algorithm. Or rather, itâs _nearly_ LALR; thereâs a parsing action conflict due to the if-else ambiguity, and a fundamental issue with `typedef` which requires the parser to feed back to the lexer â but the standard warns you about both of those things. Thatâs all fine; top marks. On the other hand, you do have to paste the grammar out of the PDF and fix up paste issues, because the C standard (unlike C++) isnât available in the form of the input markup, only the PDF standard.3. Donât make everyone copy-type the grammar out of the PDF, or copy-paste it and then have to fix up all the paste wreckage. Not every parsing tool accepts the same exact syntax for grammars, but if you provide _some_ machine-readable form of the grammar, it can easily be autoconverted into the syntax of a particular parser generator, with not much risk of introducing typos.

Another advantage of having your reference grammar in a machine-readable form is that _you_ can feed it to an actual parser generator. If your chosen parsing technology is one which proves the grammar is unambiguous (like LR or LL), then this gives you (the specification author) an extra assurance that _you_ didnât make a typo and write an unimplementable specification. You could also check your grammar against a set of reference inputs, to make sure it really says what you wanted it to say (and you didnât, for example, accidentally write a grammar that expects two ; in a row, as I discussed earlier in the C `for` statement).

(Even if your choice of parsing technology isnât self-checking, like a PEG, I think itâs still worth doing this. You still get _some_ checking â you at least check that the PEG parser tool doesnât report any more obvious kinds of error like a nonterminal you completely forgot to define. And you can still check your grammar against the test inputs.)

So ranty opinion #2 for language spec writers is: **test your reference grammar before writing it in the spec**. Ideally via a check that runs at typesetting time, to ensure you canât even build the specification PDF at all until the grammar in it is sensible.

## Use LR parser generators during language design

Iâve discussed the use of formal grammars and parser generators in language _specifications_ , when someone has already designed the language and youâre writing it down as precisely as you can. And Iâve discussed their use in _implementations_.

But thereâs another place I think parser generators are useful â perhaps even _more_ useful â and thatâs when youâre _designing_ a language in the first place, and coevolving the design, the initial test implementation, and the corpus of example input programs. If youâre changing your mind about the language syntax every day, or several times a day, the rapid-development advantages of an automated parser generator become overwhelming.

I think LR parser generators are a particularly good tool for this job â the best one I currently know of.

### Because they can point out design errors

When youâre designing a language syntax, itâs easy to introduce ambiguities by mistake.

For example (as I mentioned above in a fine-details section): in C, the comma is a valid binary operator in expressions. But arguments in a function call are also separated by commas. If you were designing a language with both of those properties, and youâd absentmindedly written your grammar to say that a function call contains a comma-separated list of expression inside the brackets, then youâd have written an ambiguity, perhaps without even noticing. You meant to say (and the real C grammar _does_ say) that if a comma operator occurs within a function argument, it must be protected by parentheses, to prevent it from being taken to be an argument separator.

Itâs helpful to catch things like this early, by running your draft grammar through a tool which can check that itâs unambiguous. Unfortunately, the general problem of checking a context-free grammar for ambiguity is formally undecidable. (Not even just âNP-completeâ â no algorithm, not _even_ a slow one, can do it reliably.) So your best bet is to restrict yourself to some subclass of grammars which _can_ be checked for ambiguity.

Some parser generation algorithms can detect and report ambiguity in their input grammar. LL and LR both can. Of those, LR can handle a strict superset of grammars; so my personal preference â and my advice to anyone else undecided â is to commit to making your languageâs grammar some form of LR, and verifying your draft grammars using an LR parser generator.

Another popular grammar formalism is a PEG. This has some superficially nice properties, like being able to fold lexing and parsing into one unified whole. But one thing I really dislike about it is that it completely lacks the much more important property of pointing out mistakes in the grammar design. _By definition_ , a PEG has no ambiguities, because any time a nonterminal has two or more productions, the grammar author must prioritise them, so that if both productions _could_ match a given input string, the grammar specifies which one _does_ match it.

As a result, thereâs no way for the grammar author to _find out_ that two of their productions are capable of matching the same input string. During the design of a language syntax, thatâs a thing you might very easily do _by mistake_ , and want to find out about, so that you can fix it!

For this same reason, I dislike parser-generator features that accept ambiguities in the grammar and specify how to resolve them, like `%prec`. Those arenât _so_ bad, because at least you wait to find out about each specific ambiguity, and decide whether to fix it or to use `%prec` to resolve it on purpose. But it seems to me that thereâs still some risk of accidentally missing a case.

Thereâs another reason I dislike leaving formal ambiguities in your LR grammar, which Iâll mention later.

### Because they can generate test cases

I mentioned earlier that production compilers often donât autogenerate their parsers from a grammar using an LR parser generator, because if you handwrite the parser, you can handwrite its error reporting too, and often do a better job.

But of course when you hand-write something, thereâs a risk of mistakes, compared to (traditional, formal, reliable forms of) computer generation. If youâre hand-writing a pile of code which you _could_ have used a generation tool for instead, you want to have some way of checking you didnât introduce bugs.

Well, another thing LR parsing automatons are good for is generating test cases. If you have a reference grammar for your language which is compatible with an LR generator, you can use the state machine output from the grammar as a test-case constructor, by finding a path from the start state to every possible state and to every possible transition. For each of those paths, you can automatically generate a full syntactically legal string of tokens and its expected formal parse tree. If your handwritten parser can parse all of those in the expected way, that should give you pretty good confidence.

Not only that, but in a similar way, you can also generate a path from the start state to every possible _illegal_ state transition, creating a similarly exhaustive set of error tests, to check that your handwritten parser _rejects_ all the things it ought to reject, as well as accepting the things it ought to accept.

However, this technique doesnât play nicely with `%prec` â see  later.

## Stop doing LALR

LR parsers were not supposed to have mysterious conflicts!

Perhaps the most famous book about compilers is the âdragon bookâ, which I mentioned in the introduction as my own first reading on the subject. (Itâs properly known as Compilers: Principles, Techniques and Tools; the colloquial name is because itâs traditionally had a picture of a dragon on the cover.) The parsing chapter ends in a presentation of LR-based techniques, and gives a choice of two4OK, three: they also present SLR, which is a _particularly_ horrible bodge and doesnât really deserve mentioning.4: CLR (or âcanonical LRâ), and LALR (âlookahead LRâ). The tradeoff is that LALR produces a much smaller state machine, but fails on a small class of languages, by introducing âmysterious conflictsâ which are a consequence of a bug in the generation algorithm and not a genuine problem with the grammar. CLR avoids those mysterious conflicts, but you pay for it by increasing the size of the parsing tables by a large factor.

The dragon book was published in 1986, and has a second edition dated 2007. But its presentation of LR parsing was out of date even the first time round. In 1977, David Pager published the paper âA Practical General Method for Constructing LR(_k_) Parsersâ, which presents a technique for avoiding the dilemma: it lets you construct parsing tables almost as small as LALRâs, without the bug that introduces spurious conflicts.

This ought to be the LR algorithm _everyone_ is using (or descendants of it that share those good properties). But well known books ignore it, and widely used parser generators are _still_ using LALR instead of Pagerâs PGM! At least, by default. For example, in GNU Bison, you can write â`%define lr.type ielr`â to avoid LALRâs bug (IELR is a later algorithm descended from PGM), but you have to ask for it â if you donât ask, you can still get error messages about reduce/reduce conflicts in situations where it wasnât actually your fault.

Fair enough, the dragon book is not the last word in books _about parsing_. If youâre a parsing specialist, or want to become one, then I expect you look at a book _all_ about parsing, instead of a general compilers work like the dragon book in which parsing is just one chapter. Iâm sure that specialist parsing books havenât overlooked PGM and its descendants. But non-specialists will probably go for the more general overview, and it seems wrong to mislead them all into thinking this is still a problem!

Gory details: a non-LALR grammar, and brief discussion of Pagerâs PGM

Hereâs a concrete example of a small non-LALR grammar, describing English-language commands to read and write a file, given one variable containing the file name and another containing (or receiving) the fileâs contents. Anticipating that users might not all agree on the natural order to write one of these commands, the syntax allows you to put the two inputs either way round, with a preposition in the middle indicating which way they are:

command â write data to file

command â write file from data

command â read data from file

command â read file to data

file â IDENTIFIER

data â IDENTIFIER

When the parser receives any of these four types of commands as input, it will reach a point where itâs seen the initial verb (write or read), and then an IDENTIFIER, and it must decide whether to reduce the identifier to a data nonterminal or to a file. It must do this based on the _next_ token of lookahead (which is either to or from), but it must also remember which verb itâs parsing, because those two tokens work the opposite way round in the two commands: the lookahead to indicates that the thing before it is data if the verb was write, but file if the verb was read, and similarly for from.

CLR has no trouble with this. Its parsing state machine has separate states depending on the verb, and in each state, the parser generator can write the appropriate reduction for the lookaheads to and from. But LALR merges those two states into one, so that â intuitively â the parser has temporarily âforgottenâ which verb started the command. (Itâs still somewhere on the parse stack, but reduction decisions are made entirely based on the current automaton state.) So a LALR parser generator throws up its hands and says it canât decide which reduction to perform if it sees to, or if it sees from.

But this is LALRâs own fault, for merging the states! All it had to do was _not do that_ , and it would have been fine.

(In this case, a workaround would be to change the grammar so that it doesnât have separate nonterminals for data and file. Instead, just write all four top-level productions for command so that each one has two explicit IDENTIFIERs. Once the parser has found out which of the four commands itâs dealing with, _then_ it knows which identifier is the data and which is the file name. But this is a workaround for a parser generation bug that shouldnât have existed in the first place: itâs not _wrong_ to write the grammar as Iâve shown it above â and it might be necessary, if each of file and data had some _extra_ productions that allowed them to be specified in syntactically different ways from each other. Better is to fix the generator so that the grammar author doesnât have to work around the bug in the first place.)

OK, what _is_ Pagerâs PGM?

One way to understand LALR (though not the only way) is that it effectively generates all the states of the larger CLR automaton, but as it generates each one, it merges it into a previous state if it can. Thereâs a basic compatibility constraint that says when two states are _candidates_ for potential merging, which Iâll describe below. LALR simply merges _all_ pairs of states which meet that basic constraint, without checking to see if that introduces a more subtle bug. On the other hand, CLR _never_ merges states of its automaton, so it avoids introducing any bugs of that kind, but you end up with a _much_ larger number of states, hence a huge lookup table.

What you want is to merge states _whenever itâs safe_ , but detect and avoid the rare cases like this where it isnât safe. Then you get the same space saving as LALR (or very nearly), but your parser still _works properly_.

Pagerâs paper presents two different techniques for detecting when itâs safe to merge states, described as âweakâ and âstrongâ. The strong one is more precise: it will only detect genuine unsafety. So youâll end up with the same minimal-sized parsing table as LALR, in any case where LALR _doesnât_ introduce a bogus conflict; it only adds extra states to the state machine when theyâre absolutely necessary to prevent a bug. But the strong algorithm is fairly complicated, and tricky to get right.

Pagerâs weak algorithm is a conservative approximation, _much_ simpler to calculate. It will sometimes err on the side of caution, and refuse to merge two states when it would actually have been perfectly safe. But this happens rarely: a weak-PGM automaton might have 2 states more than the smallest possible LALR one, when the CLR automaton might have five _times_ more. So this is absolutely fine in practice.

The weak algorithm can be _described_ quite quickly, at least for LR(1), though I donât have space here to go into the details of _why_ it works. Two CLR states are candidates for merging if they contain exactly the same set of âmarked productionsâ. (Thatâs a production of the grammar, with a mark indicating how far through it the parser currently is, either between two symbols or at the start or end. In textbooks itâs usually written with a â¢ showing the mark, like foo â bar â¢ baz; in an implementation the mark is more likely to be a numeric index into the array representing the productionâs right-hand side.) A CLR state augments each marked production with a collection of possible _contexts_ â possible tokens that could come after the end of the grammar symbol described by the production. The weak PGM condition is: itâs safe to merge states if, after the merge, no two marked productions have a context token in common _unless_ they had that context in common already in one of the two original states before merging them.

In the example above, the two CLR states that are dangerous to merge are the ones containing the marked productions file â IDENTIFIER â¢ and data â IDENTIFIER â¢. In each case the â¢ is at the end, indicating that in this state weâve already seen all the tokens making up the file or the data, and our next action will be a reduction. Each of these two CLR states assigns the context token to to one of those marked productions and from to the other â but opposite ways round. So if you merge them, then you end up with to being a valid context token for _both_ productions, and similarly from. If each context had appeared on both productions in one of the _original_ states, then it would still be OK to merge them, because either the shared context wasnât a problem at all, or it was going to be a problem even in CLR. But here, _neither_ context token is shared between the two productions in the original states, and itâs only the merging that introduces the clash. Therefore, itâs dangerous â donât merge those states!

## Grammars should be synthetic as well as analytic

Context-free grammar terminology is full of words like âstart symbolâ, âproductionâ, ânonterminal symbolâ and âterminal symbolâ. All of these words suggest that youâre _starting_ from a single most-generic symbol representing âa whole programâ, and expanding it gradually â by _producing_ extra symbols â into a more and more detailed description of some specific program. A _non-terminal_ symbol is one that indicates that you havenât finished yet. When everything in the string is a _terminal_ symbol, the _production_ of code has terminated.

Itâs odd that the terminology should be that way round, because of course _most_ uses of a grammar formalism are exactly the other way round! You use a grammar to generate a parser, and a parser doesnât _create_ a program: it _receives_ one as input, and tries to make sense of it, by breaking it up into its component parts and mapping the hierarchy of parts and sub-parts and sub-sub-parts. The normal use of a grammar for parsing is _analytic_ , even though the terminology all suggests grammars are supposed to be _synthetic_.

But the synthetic use of grammars is actually useful. The ability to start from a parse tree and transform it into a program has two uses I can think of, and there are very likely more.

Firstly, the test-case generator I mentioned [in a previous section](test-generator): if you have an LR grammar, then by an easy search through its parsing automaton, you can autogenerate a set of complete input sequences that between them exercise every shift and reduction, and every illegal token in every automaton state. Then you can use those as test cases for another parser (say, a handwritten one with nicer error messages) thatâs supposed to accept exactly the same grammar.

But this only works if _every_ formal parse tree that you can make out of the grammar productions, translated into a token sequence in the obvious way, is a legal string of the language and parses back into the same parse tree. If thatâs not true, then your corpus of autogenerated test cases will contain some invalid ones, and now you have to go through and figure out which ones they are!

So thatâs the other reason I mentioned earlier why Iâm not a fan of the common pattern of having an ambiguous grammar plus hints to the parser generator about which way to resolve the ambiguities. The use of `%prec` in Bison to specify your operator precedences, or the entirely implicit resolution of the if-else ambiguity by relying on Bisonâs default of taking the shift action if thereâs a shift/reduce conflict, have exactly this effect: it makes the grammar _only_ good for parsing an input token sequence, and no longer reliable for generating an output one. It makes your grammar only analytic, where it should be both analytic _and_ synthetic.

You could âsolveâ this by a round-trip test: after you autogenerate your test cases by exploring the parsing automaton, run all of them back through the reference LR parser, and filter out the ones which donât deliver an output parse tree identical to the input one. But now you have some edge cases of the LR automaton that you donât have tests for any more. If the grammar had been formally unambiguous in the first place, then your collection of test cases would be complete.

(On the other hand, perhaps the _misleading_ test cases â where one formal parse tree round-trips to a different one â might be worthwhile in their own right, because they precisely test that some other parser _does_ resolve the ambiguities correctly? But I donât think you can _rely_ on this generation technique finding all the cases that are difficult in that sense. You probably do better by thinking those up yourself.)

A second application for generative use of grammars starts from an _abstract_ syntax tree, rather than a formal parse tree. The difference is that a formal parse tree is tightly tied to the details of the grammar, with each node naming a specific grammar production and having one child node for each nonterminal on its RHS, whereas an AST simplifies away as many details as possible of the syntax and reduces to _just_ enough information to convey the semantics. For example, parentheses around a subexpression would show up as a node in the formal parse tree, naming some production like atomic-expression â ( expression ); but the AST representation of an expression has no node at all for the parentheses, because theyâre not needed to determine the semantics of the expression. Both `1+2*3` and `1+(2*3)` would be represented as the same AST, consisting of an addition node with one of its children being a multiplication.

The usefulness of _abstracting_ away the details of syntax to make a cut-down AST is that you might have _two_ grammars for different language syntaxes, both mapping to the same AST â and then you could automatically translate from one syntax into the other, by parsing an input file into an AST via one grammar, and âunparsingâ again via the other grammar. (You couldnât really have two different grammars deliver the same _formal_ parse tree, because the formal parse tree includes so many details of the grammar.)

Itâs probably not useful to use this to translate between two completely different programming languages, because the semantics too would differ too much. But I could see it being useful during language design. Suppose Iâve got a draft language grammar, and a bunch of test programs written in that language. Now I change my mind about the grammar, because it was only a draft. Iâve got to rewrite all my test programs, probably by hand! But if both the old and new grammars provided a mapping to the same AST representation, then I could do the rewriting automatically, by parsing each input program to the common AST using the old grammar, and then unparsing again using the new grammar.

In this application you probably have to augment your grammar with some hints about how to wrap up a thing safely, because it might be too much to expect the automation to figure it out in every case. If your production for wrapping a subexpression in parentheses indicates that the parenthesised expression has the same semantics as the expression inside the parens, then maybe the parser can figure that one out by itself; but itâs harder to figure out that (for example) the way to protect an if-without-else statement inside another if is to wrap it in braces, because the production for wrapping a thing in braces accepts _multiple_ statements.

But, again, this entire technique only works if the grammar guarantees that any token sequence you can make by following productions from the start symbol _is_ valid and parses as you expect. So this too only works if youâve avoided the use of `%prec` or implicit conflict resolutions.

## OK, what _should_ you do?

Iâve painted myself into a bit of a corner by now.

On the one hand, I think you should write your languageâs reference grammar in the form of an _unambiguous_ CFG, without using ambiguity-resolving features like `%prec`. On the other hand, I donât like the way that, if you do that, your grammar looks like a complicated computer program rather than a natural and declarative description of the underlying ideas in the syntax, so that you risk introducing bugs while writing your spec, and itâs difficult to learn the language by reading it.

Sounds as if Iâve found a reason not to like _anything!_

And itâs true â every well-known way of dealing with grammars is a bit unsatisfactory. If this collection of thoughts has an overall point, itâs not so much that people use CFGs wrongly, but that thereâs no _really good_ way to use them at all. Everything has downsides.

Well, in computing, if you think somethingâs hard to use, you can always try to redesign it better. You may not succeed, but at least you can try. So, if I were designing a language, what alternatives might I consider trying?

I have a couple of thoughts about this, but Iâve never tried out either for real, so they might turn out not to work. (Also either or both of them might very well have been done by someone else â I donât have a deep knowledge of the current state of the art.)

### Compile a simpler form into an LR grammar?

One option Iâve considered is to decouple the grammar you actually _write_ from the formally unambiguous grammar you use for all the automation purposes â test case generation, unparsing from an AST, making a reference parser for implementors to compare against.

I mentioned in an earlier section some standard things you often want to write in a language spec, which are complicated to represent as an unambiguous CFG. So one possibility is to have some kind of macro library that automatically generates the tedious parts of the grammar. For example, you might write down your table of infix operators with their precedence levels and associativity, and then pass that table as input to a macro that autogenerates a nonterminal for each precedence level, saving any human from having to write all that boilerplate.

Macros are ugly, though. Perhaps a more interesting idea is to have a kind of grammar compiler which takes a CFG augmented with ambiguity-resolution rules as input, and outputs a plain unambiguous one? Then you could write your `%prec` directives, or something quite similar, and still get all the advantages of a pure, unambiguous, synthetic CFG, because the compiler output _would_ be one of those.

I havenât worked out the details of what such a compiler would look like, though! I think the starting point would be to _try_ making an LR automaton out of the input grammar, and see where the ambiguities arise. Then youâd make local tweaks to the grammar to fix each one in accordance with the userâs directives.

In both of my example cases â operator precedence and the if-else ambiguity â the usual solution is to clone nonterminals. The ambiguous grammar has just one nonterminal for statement or expression, and the unambiguous version has multiple ones, for a balanced or unbalanced statement, or for an expression at a particular level of the precedence hierarchy. So I think the basic idea would be that any time you see a conflict between two productions, you find a nonterminal involved with the conflict, split it into two clones, and assign one of the conflicting actions to each clone. Then you try â¦ errrr, _somehow_ â¦ to decide which clone to use where, in the rest of the grammar, in such a way that the choice of parses ends up corresponding to the userâs intended resolution of the ambiguity.

But, as you can tell, I havenât thought this out in full!

Another possible approach, which I also havenât thought out fully, might be to start by processing the input grammar into the same LR automaton that Bison would output, with all the conflicts resolved according to the precedence directives, and then try to reconstruct a completely different unambiguous CFG that matches the language _really_ recognised by that automaton. My intuitive sense is that thatâs probably either fairly easy, or formally undecidable, but I canât quite work out which. If it could be done, though, it would allow any analytic-only grammar to be turned back into a synthetic one, which would be very nice.

### LR with attributes?

Hereâs a different thought Iâve had about this, which requires extending the concept of what a grammar _is_. I havenât got an implementation of this working either, but if I had a spare year to work on stuff like this, Iâd like to give it a try.

Iâll start by showing an example of a completely naÃ¯ve context-free grammar, representing a simple syntax for infix expressions, involving only binary operators and some kind of atomic subexpression like a variable or a constant. (A real grammar would probably have some unary operators too, and also support parenthesised subexpressions, but this is enough to show the idea I have in mind.)

expr â ATOM

expr â expr BINOP expr

This grammar is _of course_ ambiguous. If you feed it to Bison, it will report a shift/reduce conflict, in the obvious location: if you have expr BINOP expr on the parse stack already, and you see another BINOP next, do you reduce the existing three symbols into a higher-order expr, or do you shift the second BINOP in order to reduce that one first?

Of course, thereâs no fixed answer that works for all operators: it depends on the relative precedence of the two binary operators, or if those are the same, it tie-breaks on whether the operator is left- or right-associative.

Normally, youâd fix that by replacing BINOP with a whole set of more specific tokens, each representing a specific operator with a known precedence. Then, as Iâve discussed earlier, youâd either leave the conflicts in the theoretical grammar and use `%prec` to tell the parser generator which way you want them resolved during parsing, or else, youâd also replace expr with a set of more specific _nonterminals_ , one for each precedence level.

What if you _didnât_ split BINOP into lots of different token types?

Instead, annotate each BINOP with information about the operatorâs precedence, and also annotate each expr with similar information, based on the outermost (non-bracketed) operator in it. Then you have an augmented grammar that looks something like this:

exprâ¤ â ATOM

expr _Î²_ â expr _Î±_ BINOP _Î²_ expr _Î³_ provided that _Î±_ â¥ _Î²_ and _Î³_ > _Î²_

where the Greek letters _Î±_ , _Î²_ , _Î³_ represent elements of some ordered set of operator precedences, and â¤ represents an element that compares greater than the precedence of any actual operator. The constraints _Î±_ â¥ _Î²_ and _Î³_ > _Î²_ on the second production enforce that higher-precedence operators are evaluated first. They also enforce that (in this example) all types of BINOP associate to the left, because the _left_ operand to BINOP _Î²_ is allowed to reuse the same precedence level _Î²_ , whereas the right operand must have a strictly higher one. In a more complete example Iâd want to extend the annotations so that they also allowed each precedence level to be independently specified as left-, right- or non-associative, but this is enough for now.

My idea is that it should be possible to extend the LR(1) parser construction algorithm to operate on this kind of augmented grammar, in such a way that each automaton state carries some extra parameter variables and some required relationships between them, and annotates the stateâs marked productions and their contexts with those parameters. At some point in the automaton there will be a state that has to make the key decision: it contains the marked productions expr â expr â¢ BINOP expr and expr â expr BINOP expr â¢, and has to decide whether to shift or reduce if it sees BINOP next. Propagating the annotations through the automaton _ought_ to arrange that each of those parsing actions is only valid according to some relationship between the annotation on the next BINOP and the annotations in the state parameters, and thus, resolve the conflict.

This relies on the parser generator being able to recognise that the conditions on the various actions are mutually exclusive. In this case, it has to _know_ that precedence annotations on expr and BINOP are partially ordered, and therefore, that if it finds a shift action conditional on _Î²_ â¥ _Î³_ and a reduce action conditional on _Î²_ < _Î³_ , it can be sure that thereâs no way both can be valid at once. That way it can still prove that the augmented grammar is unambiguous, even if it doesnât know anything else about what the annotations actually _are_.

This is a much more ambitious idea than the previous one, requiring a rethink of the whole concept of a context-free grammar. But if it can be done, it would deliver extra advantages.

To begin with, it restores the ability to write an infix grammar declaratively. You really _could_ write down a childishly simple grammar for the actual expressions, and separately, write down a set of rules specifying the precedence and associativity of each operator â just like `%prec`, but in a way that still keeps the grammar synthetic as well as analytic. Perhaps youâd do that by turning BINOP into a nonterminal binop, and having a set of productions such as binop _Î±_ â +, each one specifying an appropriate annotation _Î±_ for that operator.

Similarly, you could sort out the if-else ambiguity without having to do any duplication or refactoring: you wouldnât have to separate statement into two nonterminals. Instead you could keep it as just one, with a boolean attribute âbalanced?â, and propagate balance through things like `while` loops by simply setting the flag to the same value on left and right:

statement _Î²_ â while ( expression ) statement _Î²_

But this system of annotations _also_ opens up the possibility of augmenting the parser with code that figures out the annotations _at run time_. What if you wanted a programming language that would let you _reconfigure_ the set of infix operators within a particular lexical scope, by adding new ones, or changing the priorities (because in some particular context the same symbols meant something different)? In this system, you could annotate each open scope (corresponding to some state on the parse stack) with configuration indicating how its operators had been reconfigured, and use the topmost stack state of that kind to choose the priority of each binary operator token. Because the parser automaton itself doesnât have to change at all to accommodate a different set of operators and different precedences, you can reconfigure them without having to regenerate the parser, even dynamically.

Similarly, a system of this kind would be able to solve the C `typedef` problem in a more principled way than the usual pragmatic approach. In the usual approach, the lexer keeps track of a list of tokens that are currently typedef names, and emits those to the parser as a separate token type, say TYPENAME in place of IDENTIFIER; the parser, when it processes the reduction that completes a typedef declaration, feeds the new name to the lexer to add to its set, and when it closes a scope, tells the lexer to discard new typedefs opened since the start of the scope. That setup relies on the precise flow of control between parser and lexer â if the parser notified the lexer _too late_ about a new typedef or a scope closure, a token that should have been recognised as one thing would be misidentified as the other.

But in _this_ setup, the lexer is kept simple. Identifiers and typedef names come from the lexer as a single token type. That token type has a boolean annotation, âis this a typedef name?â And the answer is determined only when the parser needs to know it, by searching up the _parse stack_ for states annotated with an attribute saying theyâve brought a typedef name into scope. This automatically takes care of descoping typedefs when a scope closes, because those states are popped off the parse stack. And it no longer relies on the lexer and parser being tightly interleaved: you could lex the C program in whatever size block you happened to read from the source file, or even lex the _whole_ translation unit in advance before even starting to parse the resulting list of tokens, and it would still work exactly the same.

## Bodges to handle non-LR languages

Thereâs a big problem with my recommendation that people should use a LR parser generator as a tool for language design: a lot of widely used modern languages _canât_ be parsed by the orthodox strategy of a regex-based lexer followed by a pure LR grammar. In fact, when I tried to find an example of a well-known language which _can_ be parsed using that strategy without any hacks, it was hard to find one! (Discussion among my friends eventually decided OCaml might qualify, although I donât know it well myself.)

There are lots of common reasons why not. Here are a few examples.

Type name ambiguity
    I mentioned this in the previous section: Câs grammar depends on the lexer knowing what typedefs are currently in scope, so that it can distinguish type names from variable names reliably. C and C++ arenât the only languages with this feature; some Pascal flavours have it too (at least the Borland-derived dialects â 1990s Turbo Pascal, Delphi, Free Pascal). Iâve even managed to _accidentally_ design a language myself with a similar property: itâs a surprisingly easy mistake to make! (The expression language in [spigot](https://www.chiark.greenend.org.uk/~sgtatham/spigot/) requires the lexer to tell variable and function names apart, which initially didnât seem worrying because the set of functions was fixed, but later I added the ability to define your own functions, oops).
Angle brackets vs shift operators
    In all of C++, Java and Rust, you write a parametric type by writing its parameters in angle brackets after it, like `std::vector<int>` or `Vec<i32>`. If the parameter type is parametrised in turn, you have to write two consecutive closing angle brackets, e.g. `Vec<Option<i32>>`. In this situation `>>` wants to be treated as two separate âclosing angle bracketâ tokens â but in a different context, `>>` is the right-shift operator, which is a single token. So the lexer needs to know something about the parsing context, to decide how it should treat `>>`.
Significant whitespace
    If your language assigns semantic meaning to indentation, like Python or Haskell, itâs very hard to even represent that within the model of a _sequence of tokens_ at all, let alone teach an LR parser to understand the result!
_Sometimes_ significant newlines
    If newlines were _always_ syntactically significant, then thereâs no reason an orthodox parser would have trouble with it: the lexer simply emits newlines as a token, and the grammar says where one is acceptable, just like the way semicolons work in C or Java or Rust or whatever. But many languages take the view that newlines count as a vital syntactic token in _some_ locations, but are completely ignored in others. For example, Python will ignore newlines as long as they appear within some pair of matched delimiters like `()` or `[]` or `{}`, so that you can break a long array declaration or list of function call parameters across lines without needing an ugly `\` at the end of each line â but _outside_ any delimiters of those kind, a newline ends the current statement. I donât know if itâs actually _impossible_ to write an LR grammar in such a way that it consistently ignores newlines in some contexts, but itâs certainly at least very difficult and unergonomic.

What can be done about these, if you also want to stick as close as possible to LR, for all the advantages Iâve mentioned (rapid development, grammar validation, test case generation)?

Iâve discussed the type-name ambiguity already, in the previous section. If my âLR with attributesâ idea can be made to work, then it can give a formal account of how you know whatâs a type name and whatâs not, and a way of determining it at run time.

I understand that significant whitespace is often handled by some kind of preprocessing step, which takes in (say) a Python program with significant indentation, and re-emits it in a modified internal form that has explicit block delimiters, which _can_ be handled by an LR parser. In Haskell this is surely even easier, because the language itself defines explicit block delimiters, which you can use in place of significant whitespace if you prefer â so the preprocessor doesnât even need to emit a _different_ internal syntax. But I wonder if the âLR with attributesâ approach might be able to do better: if nonterminals such as block were annotated with an integer parameter giving their indentation, and the lexer emitted start-of-line whitespace as a token with the same integer parameter, perhaps you _could_ get an augmented-LR parser to directly handle block scope specified by indentation? Something like:

  * every production for statement _n_ starts with an INITIAL-WHITESPACE _n_ token (and ends with a NEWLINE)
  * a block _n_ is a list of statement _n_ (so that every statement in the block is indented the same)
  * productions for statement _n_ which include one or more block _k_ have the constraint _k_ > _n_ (so that the sub-statements are indented to some deeper level). If your language were more prescriptive you might even require _k_ = _n_ \+ 4 or something.



For the other two cases â conditionally significant newlines, and conditionally lexing `>>` as either a single token or two separate `>` tokens â my best thought is to interpose a âfilterâ layer _between_ the lexer and parser, which is aware of the current state of the LR automaton itâs talking to, and can query its transition tables.

For example, you could handle conditionally significant newlines by making the filter do something really simple: **if the current state of the LR automaton would be able to shift a newline token, emit the newline, otherwise discard it**. So a newline appearing in the source _in a location where the grammar permits one_ would be treated as syntactically significant, but a newline _anywhere else at all_ would be treated as mere line-splitting for readability, and quietly ignored.

(The automaton might have to reduce one or more times before shifting a newline, and the filter would have to take that into account. The question is, if it were given a newline token, then _after_ it finishes doing reductions, will it shift the newline, or give an error? Or if you used the extra-big tables of a CLR parser you wouldnât have to imagine the in-between reductions.)

Similarly, if the lexer sees `>>` coming up, it could query the LR automaton to ask whether thereâs a legal transition on a `>>` token right now, and also whether there would be legal transitions for two `>` in sequence. Then it could decide what to do based on the answers. Easy, right?

Well, not quite. If only _one_ of those two options is legal, then sure, no problem. But if _both_ token sequences would be legal, there _is_ a problem. What if the user has a type parametrised by an integer expression? What if the user writes an integer expression like `i >> 3` inside the angle brackets?

If you want `>>` to win, then the filter between the lexer and the parser has an easy choice: **if thereâs a shift transition available for`>>`, emit `>>`, else emit two `>` instead**.

But I think more normally languages of this kind want `>>` to _lose_. Itâs considered too confusing to let users write anything like `Vec<MyType<i >> 3>>` at all: instead, theyâre supposed to protect the shift operator with parentheses, to make it clear that itâs not a template bracket. You write `Vec<MyType<(i >> 3)>>` instead.

But this is harder for the filter to cope with. You could certainly ask whether the LR automaton would be able to (eventually, ignoring intermediate reductions) shift _two_ `>` tokens, and if so, split up the `>>`. But then youâre in the extra confusing situation where you _do_ permit an unguarded right shift operator in _one_ layer of template brackets: that filter would allow `MyType<i >> 3>` without complaint, but if you tried to put that text inside a second pair of template brackets to get `Vec<MyType<i >> 3>>`, _then_ itâs an error. I donât think that was what we wanted!

So, in this case, perhaps a more sensible idea is to rewrite the actual grammar to resolve the ambiguity. Introduce some extra nonterminals for expressions, which behave like the existing ones except that they enforce that no right-shift operator appears outside parentheses. (The nonterminals for precedence levels _higher_ than the right shift token already have this property; each nonterm at or below the right-shift priority level would have to be duplicated.)

After you modify the grammar like that, the aim is that there should _never_ be a situation in which _both_ of `>>` (one token) and `> >` are acceptable in the same location. You could _prove_ that statically â for example, by running the CLR(2) algorithm, and then checking no state of the output automaton has a valid parsing action on the lookahead pair > > _and_ a valid action on any lookahead pair whose first token is >>. And then the filter between lexer and parser will have no trouble making its decision, because thereâs always (at most) one right decision.

(What about the âsynthetic, not just analyticâ property Iâve been making such a fuss about? With the filters Iâve described here, thereâs always _some_ way to emit an output program which will be re-parsed the same way. You could never emit a newline _unless_ itâs significant; you could never emit `>>` without a space in between unless you mean it as a right-shift operator. So _technically_ the property I wanted is still available. But maybe you donât think thatâs high-quality unparsing? In that case perhaps an output filter could re-parse the emitted text and figure out when it was safe to cut cornersâ¦)

## Conclusion

Context-free grammars and automated parser generation give me a strong sense of âso near, and yet so farâ. They seem like such a clean, nice idea, with so many advantages â and yet they fall short of being a sensible way to write your real-world production parsers, _or_ to write your clear language specification.

With normal programming languages itâs common to blame the language designers. (Not necessarily with justification â itâs easy to find something you donât like and shout about it, and much harder to find a design that fixes it without breaking something else. But this doesnât generally stop people.)

But context-free grammars are _barely_ a language at all. There were almost no choices made in the design. So itâs much harder to say that someone should have made this or that small detailed decision differently â there _werenât_ any small detailed decisions to make differently. Itâs as if _mathematics itself_ did a not-quite-good-enough job of giving us an ideal way to specify languages!

## Footnotes

With any luck, you should be able to read the footnotes of this article in place, by clicking on the superscript footnote number or the corresponding numbered tab on the right side of the page.

But just in case the CSS didnât do the right thing, hereâs the text of all the footnotes again:

1. My other example of a thing advertised as âdeclarativeâ which doesnât deliver on its promise is functional programming. Iâm not saying FP has no virtues, but declarative it is not. For example, to write a sorting function in a language like Haskell, you must decide which actual sorting algorithm you want to use; you can write very different Haskell functions that look like quicksort or mergesort or some other sort, and the compiler will generate the algorithm you asked for. My litmus test for a language worth calling âdeclarativeâ would be that I can write a sorting function by simply specifying the _properties_ I want the output list to have, without saying anything about _how_ to achieve it: it should be a permutation of the input list, such that _a_[_i_] â¤ _a_[_i_ +1] for all _i_.

2. Except that a braced block counts as a statement by this grammar, and doesnât have a semicolon after the closing brace. So even this âobviousâ fact about C syntax depends a bit on your point of view.

3. Since Iâve used C as an example already in this article: the C standard scores one out of two points here. Annex A of the C standard provides a full context-free grammar, and states specifically that itâs acceptable to `yacc`, i.e. to the LALR algorithm. Or rather, itâs _nearly_ LALR; thereâs a parsing action conflict due to the if-else ambiguity, and a fundamental issue with `typedef` which requires the parser to feed back to the lexer â but the standard warns you about both of those things. Thatâs all fine; top marks. On the other hand, you do have to paste the grammar out of the PDF and fix up paste issues, because the C standard (unlike C++) isnât available in the form of the input markup, only the PDF standard.

4. OK, three: they also present SLR, which is a _particularly_ horrible bodge and doesnât really deserve mentioning.
