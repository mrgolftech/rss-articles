# Rust RPN Calculator

**来源:** https://beej.us
**链接:** http://beej.us/blog/data/rust-rpn-calc/
**日期:** Fri, 24 Oct 2025 00:00:00 +0000

---

# [Beej's Bit Bucket  â¡ Tech and Programming Fun ](../..)

2025-10-24

# Implementing an RPN Calculator in Rust

![HP-48G calculator](images/hp48g.jpg) The classic [HP-48G](https://en.wikipedia.org/wiki/HP_48_series) RPN calculator. This is what I used in college back in 1872.

Welcome back to another edition of _Rust Rabbit Holes_ wherein I attempt to learn a thing or two about Rust by implementing something and poking around. As usual, since I'm far from a Rust expert, I highly value learned feedback if you have it.

The intention is that you just read this through. It's not focused on how to do any one particular thing. It's just train-of-thought exploration.

Today we're going to implement a [postfix](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (AKA _Reverse Polish Notation_ , AKA RPN) calculator.

This is inextricably tied to the concept of the [_stack_ abstract data type](https://en.wikipedia.org/wiki/Stack_\(abstract_data_type\)) so read up on that if you have to. We're gonna push and pop!

## Quick Background

You're going to be given a list of numbers and operators that look like this:
    
    
    4 3 +
    

Reading from left to right, if the item is a number, push it on the stack.

If the item is an operator (we'll stick with `+` and `-`), pop the two previous numbers off the stack, perform the operation on them to get a result, and push the result on the stack.

So reading the above, we get:
    
    
    4: push 4 on the stack
    
    3: push 3 on the stack
    
    +: pop 3 off the stack,
       pop 4 off the stack,
       add 3 + 4 to get 7,
       push 7 on the stack
    

When we're done with the input, we do this:
    
    
    pop the stack
    print that value out
    

Which in our example would print `7`. Which, happily, is `4+3`.

In regular algebraic notation, we might have an expression that looks like this:

$$(3+10)-(1+7)$$

But with RPN we don't have parentheses; you just have to put stuff on the stack in the correct order.

We definitely want at least this for the above expression:
    
    
    3 10 +
    

And when we do that, we'll have `[13]` on the stack. We can just leave that there for later, though, and do more math.
    
    
    3 10 + 1 7 +
    

After that, we'll have `[13, 8]` on the stack. Which, if you'll notice, are the numbers we want to get the difference between in the original expression. So let's just take the difference:
    
    
    3 10 + 1 7 + -
    

Again read it from left to right. If it's a number: push. If it's an operator: pop, pop, do math, push result.
    
    
    3:  push 3, stack is [3]
    
    10: push 10, stack is [3, 10]
    
    +:  pop 10, stack is [3]
        pop 3, stack is []
        add 3 + 10 to get 13
        push 13, stack is [13]
    
    1:  push 1, stack is [13, 1]
    
    7:  push 7, stack is [13, 1, 7]
    
    +:  pop 7, stack is [13, 1]
        pop 1, stack is [13]
        add 1 + 7 to get 8
        push 8, stack is [13, 8]
    
    -:  pop 8, stack is [13]
        pop 13, stack is []
        subtract 13 - 8 to get 5
        push 5, stack is [5]
    

And after that we'll have `[5]` on the stack. And if that's the last operation, we'll pop the `5` and print it out for the answer.

## The First Stab

This one works. We'll break it down a bit, below, and try to improve it.
    
    
    fn main() {
        let args: Vec<String> = std::env::args().collect();
        let mut stack: Vec<i64> = Vec::new();
    
        for a in &args[1..] {
            match a.parse::<i64>() {
                Ok(n) => stack.push(n),
                Err(_) => match a.as_str() {
                    "+" => {
                        let o2 = stack.pop().unwrap();
                        let o1 = stack.pop().unwrap();
                        stack.push(o1 + o2);
                    }
                    "-" => {
                        let o2 = stack.pop().unwrap();
                        let o1 = stack.pop().unwrap();
                        stack.push(o1 - o2);
                    }
                    _ => {
                        println!("unknown operator {}", a);
                        std::process::exit(1);
                    }
                },
            }
        }
    
        let result = stack.pop().unwrap();
        println!("{}", result);
    }
    

An example run:
    
    
    $ cargo run 3 10 + 1 7 + -
       Compiling rpncalc v0.1.0 (/home/beej/src/rust/rpncalc)
        Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.09s
         Running `/home/beej/src/rust/rpncalc/target/debug/rpncalc 3 10 + 1 7 + -`
    5
    

And there's my `5` at the end!

[Clippy](https://doc.rust-lang.org/clippy/usage.html) gives its seal of approval. But I'm not completely happy.

## Command Line Arguments

As we see, the command line arguments accessed with the [`std::env::args()`](https://doc.rust-lang.org/beta/std/env/fn.args.html) function.

This returns an [`Args` struct](https://doc.rust-lang.org/beta/std/env/struct.Args.html) that implements [`Iterator`](https://doc.rust-lang.org/beta/std/iter/trait.Iterator.html), so we can do all kinds of iterator-y stuff with it, including `collect()`ing it into a vector. Which I've done:
    
    
    let args: Vec<String> = std::env::args().collect();
    

What that does is take the `Args` iterator and turn it into a `Vec` so I can more easily index it.

Notably, I don't want the element at index 0 because that's the name of the executable (typically). But I do want the items at indexes 1-to-the-end. And I do that by getting a slice, like so:
    
    
    fn main() {
        let args: Vec<String> = std::env::args().collect();
    
        for a in &args[1..] {
    

But I'm not super happy with that. I just want to iterate once over the command line arguments, and I'm doing it twice. (Once for the `collect()` and one for the `for`-loop.)

We'll steal something from the [previous blog entry](https://beej.us/blog/data/rust-trait-impl/) and manually run through the iterator.

And we'll discard the command name (the zero-th argument) before we start the loop.

This also works:
    
    
    fn main() {
        let mut args = std::env::args();
    
        let _ = args.next();  // strip off the command name
    
        while let Some(a) = args.next() {
    

And that's only one iteration through the arguments.

But it's really just longhand for using an `for`-`in` loop:
    
    
    fn main() {
        let mut args = std::env::args();
    
        let _ = args.next();  // strip off the command name
    
        for a in args {
    

Happier, still!

## Calling The Rabbit Hole Collect

Before the above refactor, we were doing this, and recall that `args()` returns an `Args` structure that implements `Iterator`:
    
    
    let args: Vec<String> = std::env::args().collect();
    

Question: why do I have to specify the type of the `args` variable? Why can't Rust figure it out? Let's dig in.

The `collect()` method is interesting in that it has no idea what type of thing to collect into. It's a generic method.
    
    
    fn collect<B>(self) -> B
    where
        B: FromIterator<Self::Item>,
        Self: Sized,
    

`Self: Sized` means the thing being collected, `Args`, needs to be [`Sized`](https://doc.rust-lang.org/std/marker/trait.Sized.html), meaning that it has a compile-time known size. So here `Self` refers to `Args`, the thing on which `.collect()` is being called. And from what I can tell it's important to be `Sized` when moving ownership for generating code for which the size needs to be known, e.g. stack space.

The important bit is `B: FromIterator<Self::Item>`. This means whatever we're collecting into, `B`, needs to implement `FromIterator<Self::Item>`. Hmm!

Okay, `B` in this case is `Vec<String>` because that's the type we used. Does it implement `FromIterator<Self::Item>`?

Well, [`Vec` implements `FromIterator<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#impl-FromIterator%3CT%3E-for-Vec%3CT%3E) according to the documentation. So that's good. This is the trait that allows it to be collectedâanything implementing this trait is eligible (as long as it's `Sized`).

What's `Self::Item`? We saw `Self` referred to the `Args` type. Where is `Item` and what is it?

If we look at the source for [`Iterator`](https://doc.rust-lang.org/beta/std/iter/trait.Iterator.html), we see this at the top:
    
    
    pub trait Iterator {
        type Item;         // â There it is!
    
        // Required method
        fn next(&mut self) -> Option<Self::Item>;
    

What is this `type Item` stuff in the trait? Turns out that's an [_associated type_](https://doc.rust-lang.org/book/ch20-02-advanced-traits.html#specifying-placeholder-types-in-trait-definitions-with-associated-types), a way of bundling some additional type information along with an implementation of the trait. For example, I might be making my own iterator that implements `Iterator` over the type I happen to be using, say `u64`. In that case, I could do this:
    
    
    impl Iterator for MyStruct {
        type Item = u64;
    
        //...
    }
    

Now if someone uses a `MyStruct` as an iterator, the type held within (`u64`) is automatically bundled along with the iterator. If we didn't have this, we'd have to add it as another generic type. That's a lot less ergonomic, among other things.

> More reading:
> 
>   * [The Rust Book, _Associated Types_](https://doc.rust-lang.org/book/ch20-02-advanced-traits.html#specifying-placeholder-types-in-trait-definitions-with-associated-types)
>   * [Rust by Example, _Associated Types_](https://doc.rust-lang.org/rust-by-example/generics/assoc_items/types.html)
>   * [RFC 195, _Associated Items_](https://github.com/rust-lang/rfcs/blob/master/text/0195-associated-items.md)
>   * [Reddit, _Why do you need associated types?_](https://www.reddit.com/r/rust/comments/14twron/why_do_you_need_associated_types_in_rust_why_not/)
> 


Sure enough, if we [look at the `Args` source](https://doc.rust-lang.org/beta/src/std/env.rs.html#867-889), we see:
    
    
    impl Iterator for Args {
        type Item = String;
    

There we go.

So, to answer my question, I have to specify the type as `Vec<String>` and then Rust can figure out `Item` from the type we're assigning into. If we left the type off, it would be an error because... Rust doesn't know what the type of `Item` is?

No, wait. Rust has that information. `args()` returns an `Args`, which implements `Iterator` with `type Item = String`. It knows it's getting `String`s out of it.

What it doesn't know is that I want this in a `Vec`! All `collect()` knows, in this case, is that it's collecting into something that implements `FromIterator<String>`. That could be a `Vec` or it could be an `Antelope`. So we have to say:
    
    
    let args: Vec<String> = std::env::args().collect();
    

Actually, since it knows the `String` part, we can just let the compiler fill that in, too. We only need `Vec`. Here's how:
    
    
    let args: Vec<_> = std::env::args().collect();
    

All that said, we could also do it the other way and tell `collect()` exactly what type to use. That uses [_turbo fish_](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect) notation (`::<>`):
    
    
    let args = std::env::args().collect::<Vec<String>>();
    let args = std::env::args().collect::<Vec<_>>();      // Or this
    

I didn't have to give `args` a type; the compiler infers it from the right hand side. Let's look at `collect()` again:
    
    
    fn collect<B>(self) -> B
    

What the turbo fish does is it sets type that `B` is. Earlier, with the type `Vec<String>` attached to `args`, the compiler could fill `B` in itself, inferring it from the type of `args`. Now, with `Vec<String>` attached to the `collect()`, the compiler can infer the type of `args` in that direction.

Same thing, different way. Personally I prefer the type attached to the variable for readability, but that's just me.

We could do both:
    
    
    let args: Vec<String> = std::env::args().collect::<Vec<String>>();
    

but that's just redundantly redundant.

## Parsing Tokens

There are two kinds of tokens in our RPN calculator: numbers and operators. We'll differentiate by trying to parse it as a number, then, if that fails, trying to see if it's a valid token.

Here's how to parse a string into a type like we did with `.parse()` in the original code at the top of the page. Keep in mind that `a` is a `String`, so `.parse<F>()` must be a method on `String`, and it is.
    
    
    match a.parse::<i64>() {
    

And there's the turbo fish again. In this case we're not doing an assignment so we can't specify a type on the left, and we're forced to use it. Let's dig a bit into these traits.

This is what we have for `parse()`:
    
    
    pub fn parse<F>(&self) -> Result<F, <F as FromStr>::Err>
    where
        F: FromStr,
    

So the type we specify in the turbo fish has to implement `FromStr`. Does `i64` do that? [Yes, it does](https://doc.rust-lang.org/std/primitive.i64.html#impl-FromStr-for-i64). Lots of things do.

This is interesting to me because it means that all the individual types that implement `FromStr` handle their own parsing. Floats will do their parsing independent of the integers that do theirs.

This actually makes the `parse()` code in `String` dirt-simple:
    
    
    pub fn parse<F: FromStr>(&self) -> Result<F, F::Err> {
        FromStr::from_str(self)
    }
    

That's it. All we need to do is somehow specify what `<F>` is and the appropriate `from_str()` method is called.

## Using the Stack and Errors

So we try to parse the number, and if that works, we push it on the stack, otherwise we start checking to see if the argument is an operator. If it is an operator, we pop the operands, do the operation, and push the result on the stack.
    
    
    Ok(n) => stack.push(n),          // parse() succeded
    Err(_) => match a.as_str() {     // parse() failed
        "+" => {
            let o2 = stack.pop().unwrap();
            let o1 = stack.pop().unwrap();
            stack.push(o1 + o2);
        }
    

We have those pesky `unwrap()` calls in there. These operate on `Option`s or `Result`s and try to get to the `Ok()` or `Some()` that's embedded within them. If it's `Err()` or `None`, `unwrap()` will crash the program. It's pretty heavy-handed and crashes are typically not a desirable quality in any given piece of software.

I can force this to happen by computing `1 +`. (That'll try to pop two things off the stack, but there's only one, so the second `pop()` will return `None` and `unwrap()` will bomb out at that point.)
    
    
    $ cargo run 1 +
        Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.01s
         Running `/home/beej/src/rust/rpncalc/target/debug/rpncalc 1 +`
    
    thread 'main' panicked at src/main.rs:14:42:
    called `Option::unwrap()` on a `None` value
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    

So it's not super-robust.

We could nest more `match`es, or push these into functions (would certainly be better than nesting). We could also use `if let`, but this is positively obnoxious:
    
    
    let mut o1 = 0i64;
    let mut o2 = 0i64;
    
    if let Some(t) = stack.pop() {
        o2 = t;
    } else {
        println!("missing argument");
    }
    if let Some(t) = stack.pop() {
        o1 = t;
    } else {
        println!("missing argument");
    }
    
    stack.push(o1 + o2);
    

We can actually clean that up with a tuple assignment like so:
    
    
    if let (Some(o2), Some(o1)) = (stack.pop(), stack.pop()) {
        stack.push(o1 + o2);
    } else {
        println!("missing argument");
    }
    

Those `stack.pop()` calls definitely have side-effects, so they'd better be in the right order! Rust guarantees left-to-right evaluation in the tuple, so that should be fine.

That's cleaner for sure, and we got rid of some of our `unwrap()`s and put in some rudimentary error handling.

But can we do better? Maybe it's best to restructure this to flatten it out a bit.

We could check to see if we got a number, and if we did, push it and continue.

Otherwise, we could do our match.
    
    
    for a in args {
    
        if let Ok(n) = a.parse::<i64>() {
            stack.push(n);
            continue;  // next iteration
        }
    
        match a.as_str() {
            "+" => {
                if let (Some(o2), Some(o1)) = (stack.pop(), stack.pop()) {
                    stack.push(o1 + o2);
                } else {
                    println!("missing argument");
                }
            }
    

That gets rid of the `match`-in-`match` nesting. Nothing particularly Rusty, hereâjust some run-of-the-mill restructuring.

But I have some repeated code in that `match`.
    
    
    match a.as_str() {
        "+" => {
            if let (Some(o2), Some(o1)) = (stack.pop(), stack.pop()) {
                stack.push(o1 + o2);
            } else {
                println!("missing argument");
            }
        }
        "-" => {
            if let (Some(o2), Some(o1)) = (stack.pop(), stack.pop()) {
                stack.push(o1 - o2);
            } else {
                println!("missing argument");
            }
        }
    

And if we add more operators, it's just going to get worse. I want some general code to pop two things, perform some operation, and then push them. One way to do this is with an anonymous function, which is called a _closure_ in Rust and some other languages.

Here's how this might work:
    
    
    match a.as_str() {
        "+" => math_op(&mut stack, |x, y| x + y),
        "-" => math_op(&mut stack, |x, y| x - y),
        _ => {
            println!("unknown operator {}", a);
            std::process::exit(1);
        }
    

Oooo... so much cleaner! But what is this?
    
    
    math_op(&mut stack, |x, y| x + y)
    

`math_op()` is (will be) a function that takes two arguments. The first is a mutable reference to the stack. The second is a closureâit's a function that accepts two arguments (in parameters `x` and `y`) and returns the result of the expression after it. (Nothing magical about the return; `x+y` is the last line in the closure, so it takes on the return value.)

All that's left is to code up the `math_op()` function. Great. We'll use parameter `f` to represent the closure function.
    
    
    fn math_op(stack: &mut Vec, f ...
    

What type is that? Well, we could rabbit hole on this one, but I don't want to get too far off track. Here's my understanding, which is somewhat incomplete.

Rust has a trait, `FnOnce`, that represents a function (meant to be called once). Closures implement this trait.

In this case, we know we know our closure implements this in particular:
    
    
    FnOnce(i64, i64) -> i64
    

Our closures take two `i64`s as arguments and return an `i64`.

We might be tempted to:
    
    
    fn math_op(stack: &mut Vec, f: FnOnce(i64, i64) -> i64) // NOPE
    

But that won't compile. `FnOnce` is a _trait_ , not a type. But we can certainly use generics to enforce it!
    
    
    fn math_op<A>(stack: &mut Vec, f: A)
    where
        A: FnOnce(i64, i64) -> i64,
    

Which says the second argument `f` is of generic type `A` where `A` is required to implement `FnOnce(i64, i64) -> i64`. Which our closures do.

So the `math_op()` function will look like this:
    
    
    fn math_op<A>(stack: &mut Vec<i64>, f:A)
    where
        A: FnOnce(i64, i64) -> i64,
    {
        if let (Some(o2), Some(o1)) = (stack.pop(), stack.pop()) {
            let result = f(o1, o2);
            stack.push(result);
        } else {
            println!("missing argument");
        }
    }
    

And we can call it like we planned:
    
    
    match a.as_str() {
        "+" => math_op(&mut stack, |x, y| x + y),
        "-" => math_op(&mut stack, |x, y| x - y),
    

Slick!

One final rabbit hole fun fact for the section is that all functions actually implement `FnOnce`. So I could have a completely separate function like this:
    
    
    fn subtract(x: i64, y: i64) -> i64 {
        x - y
    }
    

and then use it in my `match`:
    
    
    match a.as_str() {
        "+" => math_op(&mut stack, |x, y| x + y),
        "-" => math_op(&mut stack, subtract),     // Works!
    

All kinds of fun with function pointers! Woot! This goes down a path to visit on another day.

## Get Some Results

I'm almost happy with that, but really `math_op()` should be returning some kind of `Result` instead of printing the error message. But then don't we have to handle that in the caller and mess up all our clean code?

Yes... But maybe there's a way. Right now it's all in one big main, but we could break out the main code into another function, and _that_ function could just propagate the error back to `main()` which could handle it. That makes sense in this case since invalid operands should be completely fatal to the run.

But can we get our hands on that `Result` and check it another way?

Coming from other languages, I forget that in Rust `match` (and other) statements can act as expressions and we can "return" things from them.

Let's change the `math_op()` to return a `Result`:
    
    
    fn math_op<A>(stack: &mut Vec<i64>, f: A) -> Result<(), &'static str>
    where
        A: FnOnce(i64, i64) -> i64,
    {
        if let (Some(o2), Some(o1)) = (stack.pop(), stack.pop()) {
            let result = f(o1, o2);
            stack.push(result);
            Ok(())
        } else {
            Err("missing argument")
        }
    }
    

And now when we use it in the `match` and then see if the `Result` holds an `Err` after that:
    
    
    let result = match a.as_str() {
        "+" => math_op5(&mut stack, |x, y| x + y),
        "-" => math_op5(&mut stack, |x, y| x - y),
        _ => Err("unknown operator"),
    };
    
    if let Err(e) = result {
        eprintln!("Error: {} at token {}", e, a);
        std::process::exit(1);
    }
    

Now it's a little beefier.

## The Final Code

I'd throw this in the [Rust Playground](https://play.rust-lang.org/), but it apparently doesn't support command line arguments. So here it is.
    
    
    fn math_op<A>(stack: &mut Vec<i64>, f: A) -> Result<(), &'static str>
    where
        A: FnOnce(i64, i64) -> i64,
    {
        if let (Some(o2), Some(o1)) = (stack.pop(), stack.pop()) {
            let result = f(o1, o2);
            stack.push(result);
            Ok(())
        } else {
            Err("missing argument")
        }
    }
    
    fn main() {
        let mut args = std::env::args();
        let mut stack: Vec<i64> = Vec::new();
    
        let _ = args.next();
    
        for a in args {
            if let Ok(n) = a.parse::<i64>() {
                stack.push(n);
                continue; // next iteration
            }
    
            let result = match a.as_str() {
                "+" => math_op(&mut stack, |x, y| x + y),
                "-" => math_op(&mut stack, |x, y| x - y),
                _ => Err("unknown operator"),
            };
    
            if let Err(e) = result {
                eprintln!("Error: {} at token {}", e, a);
                std::process::exit(1);
            }
        }
    
        if let Some(result) = stack.pop() {
            println!("{}", result);
        } else {
            eprintln!("Error: empty stack");
            std::process::exit(2);
        }
    }
    

Good rabbit holes in this one.

## Further Reading

If you really want to learn more fun things about RPN math, read up on [The Shunting Yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) which takes a "regular" algebraic expression in _infix_ notation and converts it to the postfix notation we used in this blog.

## Comments

[View Comments](https://mastodon.sdf.org/@beejjorgensen/115432898842626559) [Reply](https://mastodon.sdf.org/@beejjorgensen/115432898842626559)

Click on "View Comments" to see the comments.

[**Blog**](http://beej.us/blog/)  â¡  [**beej@beej.us**](mailto:beej@beej.us)  â¡  [**Home page**](http://beej.us/)
