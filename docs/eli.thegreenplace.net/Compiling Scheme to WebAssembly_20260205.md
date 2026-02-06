# Compiling Scheme to WebAssembly

**来源:** https://eli.thegreenplace.net
**链接:** https://eli.thegreenplace.net/2026/compiling-scheme-to-webassembly/
**日期:** 2026-01-17T14:37:00-08:00

---

Toggle navigation [ ![](https://eli.thegreenplace.net/images/logosmall.png) Eli Bendersky's website ](https://eli.thegreenplace.net/)

  * [ __ About ](https://eli.thegreenplace.net/pages/about)
  * [ __ Projects ](https://eli.thegreenplace.net/pages/projects)
  * [ __ Archives ](https://eli.thegreenplace.net/archives/all)



#  [ Compiling Scheme to WebAssembly ](https://eli.thegreenplace.net/2026/compiling-scheme-to-webassembly/ "Permalink to Compiling Scheme to WebAssembly")

__ January 17, 2026 at 14:37 Tags [Lisp](https://eli.thegreenplace.net/tag/lisp) , [Python](https://eli.thegreenplace.net/tag/python) , [WebAssembly](https://eli.thegreenplace.net/tag/webassembly)

One of my oldest open-source projects - [Bob](https://github.com/eliben/bobscheme) \- has [celebrated 15 a couple of months ago](https://eli.thegreenplace.net/2010/11/06/bob-a-scheme-interpreter-compiler-and-vm-in-python). Bob is a suite of implementations of the Scheme programming language in Python, including an interpreter, a compiler and a VM. Back then I was doing some hacking on CPython internals and was very curious about how CPython-like bytecode VMs work; Bob was an experiment to find out, by implementing one from scratch for R5RS Scheme.

Several months later I [added a C++ VM to Bob](https://eli.thegreenplace.net/2011/04/09/a-c-vm-added-to-bob), as an exercise to learn how such VMs are implemented in a low-level language without all the runtime support Python provides; most importantly, without the built-in GC. The C++ VM in Bob implements its own mark-and-sweep GC.

After many quiet years (with just a sprinkling of cosmetic changes, porting to GitHub, updates to Python 3, etc), I felt the itch to work on Bob again just before the holidays. Specifically, I decided to add another compiler to the suite - this one from Scheme directly to WebAssembly.

The goals of this effort were two-fold:

  1. Experiment with lowering a real, high-level language like Scheme to WebAssembly. Experiments like the recent [Let's Build a Compiler](https://eli.thegreenplace.net/2025/revisiting-lets-build-a-compiler/) compile toy languages that are at the C level (no runtime). Scheme has built-in data structures, lexical closures, garbage collection, etc. It's much more challenging.
  2. Get some hands-on experience with the WASM GC extension [1]. I have several samples of using WASM GC in the [wasm-wat-samples repository](https://github.com/eliben/wasm-wat-samples), but I really wanted to try it for something "real".



Well, it's done now; here's an updated schematic of the Bob project:

![Bob project diagram with all the components it includes](https://eli.thegreenplace.net/images/2026/bob_toplevel.png)

The new part is the rightmost vertical path. A [WasmCompiler](https://github.com/eliben/bobscheme/blob/main/bob/wasmcompiler.py) class lowers parsed Scheme expressions all the way down to WebAssembly text, which can then be compiled to a binary and executed using standard WASM tools [2].

## Highlights

The most interesting aspect of this project was working with WASM GC to represent Scheme objects. As long as we properly box/wrap all values in `ref`s, the underlying WASM execution environment will take care of the memory management.

For Bob, here's how some key Scheme objects are represented:
    
    
    ;; PAIR holds the car and cdr of a cons cell.
    (type $PAIR (struct (field (mut (ref null eq))) (field (mut (ref null eq)))))
    
    ;; BOOL represents a Scheme boolean. zero -> false, nonzero -> true.
    (type $BOOL (struct (field i32)))
    
    ;; SYMBOL represents a Scheme symbol. It holds an offset in linear memory
    ;; and the length of the symbol name.
    (type $SYMBOL (struct (field i32) (field i32)))
    

`$PAIR` is of particular interest, as it may contain arbitrary objects in its fields; `(ref null eq)` means "a nullable reference to something that has identity". `ref.test` can be used to check - for a given reference - the run-time type of the value it refers to.

You may wonder - what about numeric values? Here WASM has a trick - the `i31` type can be used to represent a reference to an integer, but without actually boxing it (one bit is used to distinguish such an object from a real reference). So we don't need a separate type to hold references to numbers.

Also, the `$SYMBOL` type looks unusual - how is it represented with two numbers? The key to the mystery is that WASM has no built-in support for strings; they should be implemented manually using offsets to linear memory. The Bob WASM compiler emits the string values of all symbols encountered into linear memory, keeping track of the offset and length of each one; these are the two numbers placed in `$SYMBOL`. This also allows to fairly easily implement the string interning feature of Scheme; multiple instances of the same symbol will only be allocated once.

Consider this trivial Scheme snippet:
    
    
    (write '(10 20 foo bar))
    

The compiler emits the symbols "foo" and "bar" into linear memory as follows [3]:
    
    
    (data (i32.const 2048) "foo")
    (data (i32.const 2051) "bar")
    

And looking for one of these addresses in the rest of the emitted code, we'll find:
    
    
    (struct.new $SYMBOL (i32.const 2051) (i32.const 3))
    

As part of the code for constructing the constant `cons` list representing the argument to `write`; address 2051 and length 3: this is the symbol `bar`.

Speaking of `write`, implementing this builtin was quite interesting. For compatibility with the other Bob implementations in my repository, `write` needs to be able to print recursive representations of arbitrary Scheme values, including lists, symbols, etc.

Initially I was reluctant to implement all of this functionality by hand in WASM text, but all alternatives ran into challenges:

  1. Deferring this to the host is difficult because the host environment has no access to WASM GC references - they are completely opaque.
  2. Implementing it in another language (maybe C?) and lowering to WASM is also challenging for a similar reason - the other language is unlikely to have a good representation of WASM GC objects.



So I bit the bullet and - with some AI help for the tedious parts - just wrote an implementation of `write` directly in WASM text; it wasn't really that bad. I import only two functions from the host:
    
    
    (import "env" "write_char" (func $write_char (param i32)))
    (import "env" "write_i32" (func $write_i32 (param i32)))
    

Though emitting integers [directly from WASM isn't hard](https://eli.thegreenplace.net/2023/itoa-integer-to-string-in-webassembly/), I figured this project already has enough code and some host help here would be welcome. For all the rest, only the lowest level `write_char` is used. For example, here's how booleans are emitted in the canonical Scheme notation (`#t` and `#f`):
    
    
    (func $emit_bool (param $b (ref $BOOL))
        (call $emit (i32.const 35)) ;; '#'
        (if (i32.eqz (struct.get $BOOL 0 (local.get $b)))
            (then (call $emit (i32.const 102))) ;; 'f'
            (else (call $emit (i32.const 116))) ;; 't'
        )
    )
    

## Conclusion

This was a really fun project, and I learned quite a bit about realistic code emission to WASM. Feel free to check out the source code of [WasmCompiler](https://github.com/eliben/bobscheme/blob/main/bob/wasmcompiler.py) \- it's very well documented. While it's a bit over 1000 LOC in total [4], more than half of that is actually WASM text snippets that implement the builtin types and functions needed by a basic Scheme implementation.

* * *

[1]| The GC proposal [is documented here](https://github.com/WebAssembly/gc). It was officially added to the WASM spec in Oct 2023.  
---|---  
[2]| In Bob this is currently done with `bytecodealliance/wasm-tools` for the text-to-binary conversion and Node.js for the execution environment, but this can change in the future. I actually wanted to use Python bindings to wasmtime, but these don't appear to support WASM GC yet.  
---|---  
[3]| 2048 is just an arbitrary offset the compiler uses as the beginning of the section for symbols in memory. We could also use the multiple memories feature of WASM and dedicate a separate linear memory just for symbols.  
---|---  
[4]| To be clear, this is just the WASM compiler class; it uses the `Expr` representation of Scheme that is created by Bob's parser (and lexer); the code of these other components is shared among all Bob implementations and isn't counted here.  
---|---  
  
* * *

For comments, please send me [__an email](mailto:eliben@gmail.com). 

* * *

(C) 2003-2025 Eli Bendersky 

__Back to top
