# The Liskov Substitution Principle does more than you think

**来源:** https://buttondown.com_hillelwayne
**链接:** https://buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/
**日期:** Tue, 06 Jan 2026 16:51:26 +0000

---

#  [ Computer Things ](https://buttondown.com/hillelwayne)

[ Archives ](/hillelwayne/archive/)

Search...

[ Subscribe ](https://buttondown.com/hillelwayne#subscribe-form)

January 6, 2026 

# The Liskov Substitution Principle does more than you think

## It's more than just the L in SOLID!

Happy New Year! I'm done with the newsletter hiatus and am going to try updating weekly again. To ease into things a bit, I'll try to keep posts a little more off the cuff and casual for a while, at least until [_Logic for Programmers_](https://leanpub.com/logic/) is done. Speaking of which, v0.13 should be out by the end of this month.

So for this newsletter I want to talk about the [Liskov Substitution Principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle) (LSP). Last week I read [A SOLID Load of Bull](https://loup-vaillant.fr/articles/solid-bull) by cryptographer Loupe Vaillant, where he argues the [SOLID](https://en.wikipedia.org/wiki/SOLID) principles of OOP are not worth following. He makes an exception for LSP, but also claims that it's "just subtyping" and further:

> If I were trying really hard to be negative about the Liskov substitution principle, I would stress that **it only applies when inheritance is involved** , and inheritance is strongly discouraged anyway.

LSP is more interesting than that! In the original paper, [A Behavioral Notion of Subtyping](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf), Barbara Liskov and Jeannette Wing start by defining a "correct" subtyping as follows:

> Subtype Requirement: Let ϕ(x) be a property provable about objects x of type T. Then ϕ(y) should be true for objects y of type S where S is a subtype of T.

From then on, the paper determine what _guarantees_ that a subtype is correct.1 They identify three conditions: 

  1. Each of the subtype's methods has the same or weaker preconditions and the same or stronger postconditions as the corresponding supertype method.2
  2. The subtype satisfies all state invariants of the supertype. 
  3. The subtype satisfies all "history properties" of the supertype. 3 e.g. if a supertype has an immutable field, the subtype cannot make it mutable. 



(Later, Elisa Baniassad and Alexander Summers [would realize](https://www.cs.ubc.ca/~alexsumm/papers/BaniassadSummers21.pdf) these are equivalent to "the subtype passes all black-box tests designed for the supertype", which I wrote a little bit more about [here](https://www.hillelwayne.com/post/lsp/).)

I want to focus on the first rule about preconditions and postconditions. This refers to the method's **contract**. For a function `f`, `f.Pre` is what must be true going into the function, and `f.Post` is what the function guarantees on execution. A canonical example is square root: 
    
    
    sqrt.Pre(x) = x >= 0
    sqrt.Post(x, out) = out >= 0 && out*out == x
    

Mathematically we would write this as `all x: f.Pre(x) => f.Post(x)` (where `=>` is the [implication operator](https://en.wikipedia.org/wiki/Material_conditional)). If that relation holds for all `x`, we say the function is "correct". With this definition we can actually formally deduce the first subtyping requirement. Let `caller` be some code that uses a method, which we will call `super`, and let both `caller` and `super` be correct. Then we know the following statements are true:
    
    
      1. caller.Pre && stuff => super.Pre
      2. super.Pre => super.Post
      3. super.Post && more_stuff => caller.Post
    

Now let's say we substitute `super` with `sub`, which is also correct. Here is what we now know is true: 
    
    
      1. caller.Pre => super.Pre
    - 2. super.Pre => super.Post
    + 2. sub.Pre => sub.Post
      3. super.Post => caller.Post
    

When is `caller` still correct? When we can fill in the "gaps" in the chain, aka if `super.Pre => sub.Pre` and `sub.Post => super.Post`. In other words, if `sub`'s preconditions are weaker than (or equivalent to) `super`'s preconditions and if `sub`'s postconditions are stronger than (or equivalent to) `super`'s postconditions.

Notice that I never actually said `sub` was from a subtype of `super`! The LSP conditions (at least, the contract rule of LSP) doesn't just apply to _subtypes_ but can be applied in any situation where we substitute a function or block of code for another. Subtyping is a common place where this happens, but by no means the only! We can also substitute across time.Any time we modify some code's behavior, we are effectively substituting the new version in for the old version, and so the new version's contract must be compatible with the old version's to guarantee no existing code is broken.

For example, say we maintain an API or function with two required inputs, `X` and `Y`, and one optional input, `Z`. Making `Z` required strengthens the precondition ("input must have Z" is stronger than "input may have Z"), so potentially breaks existing users of our API. Making `Y` optional weakens the precondition ("input may have Y" is weaker than "input must have Y"), so is guaranteed to be compatible.

(This also underpins [The robustness principle](https://en.wikipedia.org/wiki/Robustness_principle): "be conservative in what you send, be liberal in what you accept".)

Now the dark side of all this is [Hyrum's Law](https://www.hyrumslaw.com/). In the below code, are `new`'s postconditions stronger than `old`'s postconditions? 
    
    
    def old():
        return {"a": "foo", "b": "bar"}
    
    def new():
        return {"a": "foo", "b": "bar", "c": "baz"}
    

On a first appearance, this is a strengthened postcondition: `out.contains_keys([a, b, c]) => out.contains_keys([a, b])`. But now someone does this:
    
    
    my_dict = {"c": "blat"} 
    my_dict |= new()
    assert my_dict[c] == "blat"
    

Oh no, their code now breaks! They saw `old` had the postcondition "`out` does NOT contain "c" as a key", and then wrote their code expecting that postcondition. In a sense, _any_ change the postcondition can potentially break _someone_. "All observable behaviors of your system will be depended on by somebody", as [Hyrum's Law](https://www.hyrumslaw.com/) puts it.

So we need to be explicit in what our postconditions actually are, and properties of the output that are not part of our explicit postconditions are subject to be violated on the next version. You'll break people's workflows but you also have grounds to say "I warned you".

Overall, Liskov and Wing did their work in the context of subtyping, but the principles are more widely applicable, certainly to more than just the use of inheritance.

* * *

  1. Though they restrict it to just [safety properties](https://www.hillelwayne.com/post/safety-and-liveness/). ↩

  2. The paper lists a couple of other authors as introduce the idea of "contra/covariance rules", but part of being "off-the-cuff and casual" means not diving into every referenced paper. So they might have gotten the pre/postconditions thing from an earlier author, dunno for sure! ↩

  3. I _believe_ that this is equivalent to the formal methods notion of a [refinement](https://www.hillelwayne.com/post/refinement/). ↩




_If you're reading this on the web, you can subscribe[here](/hillelwayne). Updates are once a week. My main website is [here](https://www.hillelwayne.com)._

_My new book,_ Logic for Programmers _, is now in early access! Get it[here](https://leanpub.com/logic/)._

Don't miss what's next. Subscribe to Computer Things: 

Email address (required)

Subscribe

Join the discussion: 

  1. A

anon 

January 8, 2026, midnight

> Mathematically we would write this as all x: f.Pre(x) => f.Post(x)

Shouldn't it be `all x: f.Pre(x) => f.Post(x, f(x))`?

[Reply](https://buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/comment/5fbec809-db77-4deb-9ee4-b4a2d8a2f8df) [Report](mailto:support@buttondown.com?subject=Improper+comment)

A

anon 

January 8, 2026, morning

Further, in your examples with `old` and `new` functions - they don't have any postconditions, because you don't state any. For example, in Dafny, you have to be explicit about them, and you may want to omit certain pre/postconditions (to not overload the spec, or simply because they are implementation details). If the spec for `old` said `!out.contains_keys('c')`, and the spec for `new` removed this clause, then it would have a weaker postcondition. Likewise, if `old` didn't mention it and `new` guaranteed the presence of `'c'` in keys, then `new` would have stronger postconditions. You really must be explicit about what you promise, not just what you return. Though, if you want to guarantee that both functions return the same value for all inputs, that can often be done as well.

[Reply](https://buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/comment/577aec5d-3ae4-4646-8726-cf995bf8969b) [Report](mailto:support@buttondown.com?subject=Improper+comment)

C

[ Hillel Wayne ](https://buttondown.com/hillelwayne) Author

January 8, 2026, morning

That's the point I was trying to make: without explicitly listing your postconditions, users are free to infer whatever postconditions they want, making any kind of non-breaking change to the postconditions impossible. Every emacs update breaks someone's workflow, as they say!

[Reply](https://buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/comment/cb23a61f-eaca-47a7-a525-0986d2fba300) [Report](mailto:support@buttondown.com?subject=Improper+comment) [Delete](https://buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/comment/cb23a61f-eaca-47a7-a525-0986d2fba300/delete)




#### Add a comment:

Comment and Subscribe 

Share this email:

[ Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A//buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/&title=The%20Liskov%20Substitution%20Principle%20does%20more%20than%20you%20think) [ Share on LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A//buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/) [ Share on Hacker News ](https://share.bingo/hn?url=https%3A//buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/) [ Share on Bluesky ](https://share.bingo/bluesky?url=https%3A//buttondown.com/hillelwayne/archive/the-liskov-substitution-principle-does-more-than/)

Powered by [Buttondown](https://buttondown.com/refer/hillelwayne), the easiest way to start and grow your newsletter.
