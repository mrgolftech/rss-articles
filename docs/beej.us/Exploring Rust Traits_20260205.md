# Exploring Rust Traits

**来源:** https://beej.us
**链接:** http://beej.us/blog/data/rust-trait-impl/
**日期:** Fri, 17 Oct 2025 00:00:00 +0000

---

# [Beej's Bit Bucket  â¡ Tech and Programming Fun ](../..)

2025-10-17, 2025-10-20

# Exploring Rust Traits

![Ferris the Crab](images/ferris.png) Ferris the mascot crab is here to help, hopefully, 'cause I'm gonna need it.

Welcome to my first blog in my _Rust Rabbit Holes_ series! In these I'll just try implementing something relatively simple and then pull on the various threads to see where they lead.

I'm a Rust noob. I've dabbled for a few years and written a [small-but-non-trivial project](https://github.com/beejjorgensen/Wizards-Castle-Rust), but I'm far, far from expert.

So I'm going to just mess around with the language a bit and see what it takes to do what. And see what I learn along the way. And if anything is wrong in this blog, it's because [I'm _human_](https://www.pcgamer.com/software/ai/ai-content-now-outnumbers-human-written-articles-on-the-internet-but-the-good-news-is-that-the-slop-seems-to-have-plateaued-for-now/). ð Corrections and additional comments welcome, of course.

For this exploration, I had in mind to just compare buffered and unbuffered file I/O. But then it got into [traits](https://doc.rust-lang.org/book/ch10-02-traits.html) a bit. And I ran with that.

Reader skill level: beginner, like me.

## Traits

If you aren't familiar with the concept of Rust traits, you can very loosely think of them as "interfaces" or "abstract classes" in other languages. They're a description of methods you must have in order to implement a particular trait.

For example, to implement the [`Read` trait](https://doc.rust-lang.org/std/io/trait.Read.html) in Rust, your `struct` must implement a `read()` function with the proper signature.

There are plenty more details in [the Rust Book](https://doc.rust-lang.org/book/ch10-02-traits.html).

## Buffered and Unbuffered Reads

At a low level, the OS typically exposes an interface that just lets you synchronously read a chunk of bytes into memory. On Unix-likes, this is the [`read()` syscall](https://man7.org/linux/man-pages/man2/read.2.html).

This is inconvenient for a number of reasons, two of which are:

  * Each syscall is expensive, and if you do a lot of tiny reads, that's overhead. It's better to do one big actual OS read, and then all your smaller reads can take place in [user space](https://en.wikipedia.org/wiki/User_space_and_kernel_space) without that overhead.

  * The OS doesn't allow you to do fun things like "read a single line of data" because its interface is so simplistic. You'd have to micromanage that yourself. A buffered I/O system, since it already grabbed a big chunk of input, can scan ahead for newlines and return single lines.




In C, the `stdio.h` I/O functions are all typically buffered. If you want unbuffered, you either tell the C I/O subsystem to go unbuffered, or you can call the OS directly.

In Rust, both modes are present in the standard library. In the modern style, you first open a file in unbuffered mode, and then you wrap that up in some buffering functionality if you want that.

## Unbuffered Reads in Rust

Rust does unbuffered I/O with its [`struct File`](https://doc.rust-lang.org/std/fs/struct.File.html) type. It implements the [`Read`](https://doc.rust-lang.org/std/io/trait.Read.html) trait which gives us this method, among others:
    
    
    fn read(&mut self, buf: &mut [u8]) -> Result<usize>;
    

That's a hard parse if you're new to Rust, but the gist is that you're going to pass in a mutable reference to an array of bytes in `buf` (mutable so that `read()` can put bytes in it!) and it returns a `Result` object telling you the number of bytes that have been read. (Incidentally, this is exactly how Unix `read()` syscall works.)

So after you call `read()` on your file object, hopefully that `buf` parameter gets filled up with some bytes and the returned `Result` holds the number of bytes that we read.

Here's a bit of a demo that does this:
    
    
    use std::fs::File;
    use std::error::Error;
    use std::io::Read;
    
    fn unbuffered_demo() -> Result<(), Box<dyn Error>> {
        const BUFSIZE: usize = 128;
    
        // Open the file
        let mut file = File::open("input.txt")?;
    
        // Buffer to read bytes into
        let mut buf = [0u8; BUFSIZE];
    
        // Call file.read repeatedly, trying to get BUFSIZE bytes
        loop {
            let bytes_read = file.read(&mut buf)?;
    
            // Check for end-of-file
            if bytes_read == 0 {
                break;
            }
    
            // Otherwise, convert bytes to a string
            let str_val = std::str::from_utf8(&buf[..bytes_read])?;
            print!("{}", str_val);
        }
    
        Ok(())
    }
    

Interesting that we had to bring in the `std::io::Read` trait even though it doesn't appear in our code. It's because `File` implements it that we have to do that, apparently.

Also check out that `std::str::from_utf8()` call. I'm assuming the bytes in that files are [UTF-8 encoded](https://en.wikipedia.org/wiki/UTF-8) (they are in my `input.txt`). I pass in `&buf[..bytes_read]` which is a slice of the buffer just composed of how ever many bytes I read. Hopefully the number of bytes is `BUFSIZE`, but the file is unlikely to be an exact multiple of that so the last read is short.

When there is a short read, values in the `[u8]` array past the end of the read just have whatever was in there from the _previous_ read. So we slice those off.

Finally, the function return type is interesting:
    
    
    fn unbuffered_demo() -> Result<(), Box<dyn Error>> {
    

That's the classic `Result`, but what's the rest of it? My function returns `Ok(())` in the good case. But we have all those `?` operators all over the place. Those basically say, "Unwrap the return value from this function. If it's good, assign it to the variable on the left. If it's bad, return with the error."

But all those functions with `?` after technically return different types, so how do we handle them all?

Well, all of those error types implement the `std::error::Error` trait. So we can treat them all like `Error`. Except that they aren't the same types, and we won't know which exact type was returned until runtime, so we have to use [dynamic dispatch](https://en.wikipedia.org/wiki/Dynamic_dispatch) when returning itâthat's the `dyn` keyword you see.

Not only that, but we don't know how big the particular runtime error object will be, so it has to be `Box`ed. Rust needs to know the size of everything at compile time, and a `Box` is basically just a pointer to something on the [heap](https://en.wikipedia.org/wiki/Memory_management#HEAP), and pointers are fixed size.

I was also wondering how the called functions know to `Box` their errors for our function because it seems like normally they wouldn't. Apparently this happens through the magic of the [`From`](https://doc.rust-lang.org/std/convert/trait.From.html) trait, but I didn't pursue that rabbit hole this time.

Boxing errors like this is not the only way to handle multiple error types, and arguably isn't the _best_ way (whatever that means). [Rust by Example](https://doc.rust-lang.org/rust-by-example/error/multiple_error_types.html) has more information.

OK, so that's unbuffered. How do we get buffered I/O?

## Buffered Reads in Rust

In order to get buffered reads, we need to wrap our `File` up in a [`BufReader`](https://doc.rust-lang.org/std/io/struct.BufReader.html).

The short of it looks like this:
    
    
    // Open the file
    let file = File::open("input.txt")?;
    
    // Make a new buffered reader on the file
    let mut reader = BufReader::new(file);
    

And now we have a `reader` object that has all kinds of higher-level [`BufReader` methods](https://doc.rust-lang.org/std/io/struct.BufReader.html#implementations) on it. We can now use _these_ to read the data instead of that lower-level `read()` method. In particular, it implements the [`BufRead` trait](https://doc.rust-lang.org/std/io/trait.BufRead.html) that gives you more (and easier) control over what you read.

Notably, it has this method:
    
    
    fn read_line(&mut self, buf: &mut String) -> Result<usize> { ... }
    

That will read a line at a time! That's fun! Let's write some code that does it. I'll just copy the unbuffered code and modify it to use the `BufReader` for reading, instead:
    
    
    use std::fs::File;
    use std::error::Error;
    use std::io::{BufRead, BufReader, Read};
    
    fn buffered_demo() -> Result<(), Box<dyn Error>> {
        // Open the file
        let file = File::open("input.txt")?;
    
        // Make a new buffered reader on the file
        let mut reader = BufReader::new(file);
    
        // Storage for the line we'll read
        let mut line = String::new();
    
        loop {
            // Read a line!
            let bytes_read = reader.read_line(&mut line)?;
    
            // Check for end-of-file
            if bytes_read == 0 {
                break;
            }
    
            print!("{}", line);
            line.clear();
        }
    
        Ok(())
    }
    

Looks awfully similar to what we had before. There are a couple interesting things in this buffered version, though.

We're not reading into a byte array, but instead into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html). This is nice because `String`s are basically [`Vec`s](https://doc.rust-lang.org/std/vec/struct.Vec.html) under the hood so they grow and shrink as needed. No more fixed-size buffer to manage!

In the unbuffered version, the `File` variable had to be `mut`, and here it doesn't. That's because in the unbuffered version we were calling `file.read()`, which does a mutable borrow `&mut self` as we see in [its signature](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read). In this version, we simply pass ownership of the file to the `BufReader`, and it presumably tucks it away in its `struct` somewhere. And then when we call `reader.read_line()` is does its own `&mut self` borrow and then then calls its `file.read()` internally. I _think_.

We do have that `line.clear()` bit at the end. Turns out `read_line()` _appends_ data on the end of the `line` variable. So if we want to print them one at a time, we actually have to clear the string so it's empty for the next line.

I found myself wondering if that end-of-file check could be rolled into a `while let` similar to the idiomatic C while loop:
    
    
    // C code
    while ((bytes_read = read_line(line)) > 0) {
        puts(line);
    }
    

So in Rust that would be something like:
    
    
    // INVALID Rust code
    while (let bytes_read = reader.read_line(&mut line)?) > 0 {
        print!("{}", line);
        line.clear();
    }
    

But that won't build due to the way `let` in this instance is actually doing pattern matching to look for an `Ok()`. I speculate.

So are we stuck in terms of making our buffered reader prettier? Not quite!

> ![Update!](../../common/images/update50.png) There are a few ways to do this beyond what I thought of. You can `while` loop on a block (which I didn't realize was possible):
>     
>     
>     while {
>         let bytes_read = reader.read_line(&mut line)?;
>         bytes_read > 0
>     } {
>         print!("{line}");
>         line.clear();
>     }
>     
> 
> [HT Joe at [OSU-Cascades](https://osucascades.edu/)]

Digging around the `BufRead` trait, we find a method called [`lines()`](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines). This method returns an iterator that we can use to loop over the lines of the file, and it'll quit when done!
    
    
    fn buffered_demo_iter() -> Result<(), Box<dyn Error>> {
        // Open the file
        let file = File::open("input.txt")?;
    
        // Make a new buffered reader on the file
        let reader = BufReader::new(file);
    
        for line_result in reader.lines() {
            println!("{}", line_result?);
        }
    
        Ok(())
    }
    

Much cleaner!

One difference is that we're getting a `Result` type back in `line_result` from the `for` loop. So we have to unwrap that, which I do in the `println!()`.

And it's `println!()` this time, instead of `print!()`. Apparently the trailing newline is stripped off when using the `lines()` iterator.

> ![Update!](../../common/images/update50.png) Here's another option, since `reader.lines()` is an iterator. We can just repeatedly call `.next()` to extract lines:
>     
>     
>     let mut lines = reader.lines();
>     
>     while let Some(line) = lines.next() {
>         println!("{}", line?);
>     }
>     
> 
> [HT Joe at [OSU-Cascades](https://osucascades.edu/)]

Nowâwait a momentânothing is `mut` in our `for`-loop variant! But clearly at some deep level the `file` has to be `mut` to `read()` out of it. Let's dig. What's `reader.lines()` do?
    
    
    fn lines(self) -> Lines<Self>
    

Since it's just `self`, it's actually taking ownership of the `reader` `BufReader`. Which means we can't use the `reader` after the loop. In this case that's fine.

But if we wanted to use `reader` after the loop, we'd have to change the call to `.lines()` to be against a mutable borrow of `reader` (and it would have to be `mut`.
    
    
        let mut reader = BufReader::new(file);
    
        for line_result in (&mut reader).lines() {
    

That works and we can then use `reader` after the loop is complete if we want.

`lines()` is still taking ownership, but it's taking ownership of a mutable reference to the `reader`. So we could still use `reader` later. (_Am I saying this correctly?_)

However, this does _not_ work:
    
    
        let reader = BufReader::new(file);
    
        for line_result in (&reader).lines() {
    

Why not?

I made the following toy program to mess with it where I implemented traits for various borrows:
    
    
    struct Bar {
        x: usize,
    }
    
    impl Foo for Bar {   // Ownership
        fn foo(self) {
            println!("{}", self.x)
        }
    }
    
    impl Foo for &Bar {  // Borrow
        fn foo(self) {
            println!("{}", self.x)
        }
    }
    
    impl Foo for &mut Bar { // Mutable borrow
        fn foo(self) {
            println!("{}", self.x)
        }
    }
    
    trait Foo {
        fn foo(self);  // Ownership of self
    }
    
    fn main() {
        let mut b = Bar { x: 12 };
        (&mut b).foo(); // works
        (&b).foo();     // works
        b.foo();        // works
        //b.foo();      // error (b is moved by the previous call)
    }
    

And that works as long as I have `impl Foo` for the various forms of `Bar`. So that means we need to have an `impl BufRead` for all the supported types, and apparently `&BufReader` isn't one of them...?

> ![Update!](../../common/images/update50.png) Looking in the [`BufRead` implementors](https://doc.rust-lang.org/std/io/trait.BufRead.html#implementors) section of the docs, we see the following (among others that aren't pertinent):
>     
>     
>     impl<R: ?Sized + Read> BufRead for BufReader<R>  // 1
>     impl<B: BufRead + ?Sized> BufRead for &mut B     // 2
>     
> 
> So it's defined for:
> 
>   1. Any `BufReader` that implements `Read`. That's my `reader.lines()`.
>   2. Any `&mut` to a thing that implements `BufRead`. That's my `(&mut reader).lines()`.
> 

> 
> But that's it. Nothing in there that implements it for a `&BufReader`. So `(&reader).lines()` doesn't work.
> 
> [HT [Brian May](https://mastodon.sdf.org/@penguin_brian@hachyderm.io/115394532632498410)]

There might be more to it than this, but that's my new mental model so far.

## Implementing the `Read` Trait

If we look at what `BufReader::new()` takes, we see this:
    
    
    impl<R: Read> BufReader<R>
    
    pub fn new(inner: R) -> BufReader<R>
    

So that first line is saying "In the implementation of `BufReader` for any type `R` as long as `R` implements the `Read` trait..."

And the second is saying "We'll have a function `new` that takes an argument of type `R` (again `R` must implement the `Read` trait) and returns a new `BufReader` of that type."

It's generic! We can use any type to create our `BufReader` _as long as it implements the`Read` trait_.

And I have one! For this, we'll have a `DataProvider` object that has an array of bytes and implements the `Read` trait. If it implements that, it will be good to use with `BufReader`.
    
    
    struct DataProvider {
        data: &'static [u8],
        offset: usize,
    }
    
    impl DataProvider {
        fn new(data: &'static [u8]) -> DataProvider {
            DataProvider {
                data,
                offset: 0,
            }
        }
    }
    

All it's going to do it keep track of the current offset and copy bytes out when its `read()` method is called. We just have to make sure we match the function signature in the [`Read` trait](https://doc.rust-lang.org/std/io/trait.Read.html).
    
    
    impl Read for DataProvider {
        fn read(&mut self, buf: &mut [u8]) -> std::io::Result<usize> {
            let start = self.offset;
            let mut end = self.offset + buf.len();
            let maximum = self.data.len();
    
            if end > maximum {
                end = maximum;
            }
    
            let bytes_copied = end - start;
            self.offset += bytes_copied;
    
            let src_bytes = &self.data[start..start + bytes_copied];
            buf[..bytes_copied].copy_from_slice(src_bytes);
    
            Ok(bytes_copied)
        }
    }
    

A couple fun things there. We let `src_bytes` be a slice of our array from the starting point (which was the old `offset` to the ending (which might be the end of the data, or might be the end of the destination buffer).

And then we use the `copy_from_slice()` method to copy those bytes from the source into the destination buffer. And notably, we might only want to copy over _some_ of `buf` (in case we have fewer bytes remaining than `buf` is big). And that's why the receiver is the slice `buf[..bytes_copied]`.

And then we return `Ok(bytes_copied)`, and `bytes_copied` will be `0` once we reach the end of our data, indicating the equivalent of "end-of-file".

We can use it just like this:
    
    
    fn provider_demo() -> std::io::Result<()> {
        let dp = DataProvider::new(b"line 0\nline 1\nline 2\nline 3\n");
    
        let reader = BufReader::new(dp);
    
        for line_result in reader.lines() {
            println!("{}", line_result?);
        }
    
        Ok(())
    }
    

Works!

> ![Update!](../../common/images/update50.png) Adding my two `usize`s for `end` can overflow. This will either panic in a debug build or wrap around in a release build. Clamping it breaks the logic, so the best thing to do would be a `checked_add()` that returns an `Option` and return an `Error` if overflow happened.
>
>> Further, to avoid the overflow entirely, we should reverse the logic from an addition to a subtraction. I think somewhere in the depths of my brain I knew this, but had forgotten. This also simplifies the code a bit, especially if we use `min` for the clamping.
>>     
>>     
>>     impl Read for DataProvider {
>>         fn read(&mut self, buf: &mut [u8]) -> std::io::Result<usize> {
>>             let start = self.offset;
>>             let remaining = self.data.len() - self.offset;
>>             let bytes_copied = std::cmp::min(remaining, buf.len());
>>     
>>             let src_bytes = &self.data[start..start + bytes_copied];
>>             buf[..bytes_copied].copy_from_slice(src_bytes);
>>     
>>             self.offset += bytes_copied;
>>     
>>             Ok(bytes_copied)
>>         }
>>     }
>>     
> 
> [HT Jonathan from [Deschutes Tech Guild](https://www.deschutestechguild.com/) for both]

Technically `line_result` is `std::io::Result<String>`. But I didn't want to return some `Ok(String::from(""))` nastiness. So I changed it to `Result<()>` which is fine.

> However I was still confused over why I'm allowed to do this when that's not the `Result` that we get from `line_result`. Apparently it's due to the fact that the `?` really only has anything to do with the error portion of the result, and those are all compatible.
> 
> [HT Jonathan from [Deschutes Tech Guild](https://www.deschutestechguild.com/)]

## To-Do List

  * How the `From` trait works.
  * How to implement iterators.
  * Everything else.



## Comments

[View Comments](https://mastodon.sdf.org/@beejjorgensen/115391410243105919) [Reply](https://mastodon.sdf.org/@beejjorgensen/115391410243105919)

Click on "View Comments" to see the comments.

[**Blog**](http://beej.us/blog/)  â¡  [**beej@beej.us**](mailto:beej@beej.us)  â¡  [**Home page**](http://beej.us/)
