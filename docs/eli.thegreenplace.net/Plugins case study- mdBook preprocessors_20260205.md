# Plugins case study: mdBook preprocessors

**来源:** https://eli.thegreenplace.net
**链接:** https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/
**日期:** 2025-12-17T18:11:00-08:00

---

Toggle navigation [ ![](https://eli.thegreenplace.net/images/logosmall.png) Eli Bendersky's website ](https://eli.thegreenplace.net/)

  * [ __ About ](https://eli.thegreenplace.net/pages/about)
  * [ __ Projects ](https://eli.thegreenplace.net/pages/projects)
  * [ __ Archives ](https://eli.thegreenplace.net/archives/all)



#  [ Plugins case study: mdBook preprocessors ](https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/ "Permalink to Plugins case study: mdBook preprocessors")

__ December 17, 2025 at 18:11 Tags [Plugins](https://eli.thegreenplace.net/tag/plugins) , [Python](https://eli.thegreenplace.net/tag/python) , [Rust](https://eli.thegreenplace.net/tag/rust)

[mdBook](https://rust-lang.github.io/mdBook/index.html) is a tool for easily creating books out of Markdown files. It's very popular in the Rust ecosystem, where it's used (among other things) to publish [the official Rust book](https://doc.rust-lang.org/book/).

mdBook has a simple yet effective plugin mechanism that can be used to modify the book output in arbitrary ways, using any programming language or tool. This post describes the mechanism and how it aligns with the [fundamental concepts of plugin infrastructures](https://eli.thegreenplace.net/2012/08/07/fundamental-concepts-of-plugin-infrastructures).

## mdBook preprocessors

mdBook's architecture is pretty simple: your contents go into a directory tree of Markdown files. mdBook then renders these into a book, with one file per chapter. The book's output is HTML by default, but mdBook supports other outputs like PDF.

The [preprocessor mechanism](https://rust-lang.github.io/mdBook/for_developers/preprocessors.html) lets us register an arbitrary program that runs on the book's source after it's loaded from Markdown files; this program can modify the book's contents in any way it wishes before it all gets sent to the renderer for generating output.

![Preprocessor flow for mdbook](https://eli.thegreenplace.net/images/2025/mdbook-preprocessor.png)

The official documentation [explains this process very well](https://rust-lang.github.io/mdBook/for_developers/preprocessors.html#hooking-into-mdbook).

## Sample plugin

I rewrote [my classical "nacrissist" plugin](https://eli.thegreenplace.net/2012/08/07/fundamental-concepts-of-plugin-infrastructures) for mdBook; the code is [available here](https://github.com/eliben/code-for-blog/tree/main/2025/plugin-mdbook).

In fact, there are two renditions of the same plugin there:

  1. One in Python, to demonstrate how mdBook can invoke preprocessors written in any programming language.
  2. One in Rust, to demonstrate how mdBook exposes an application API to plugins written in Rust (since mdBook is itself written in Rust).



## Fundamental plugin concepts in this case study

Let's see how this case study of mdBook preprocessors measures against the [Fundamental plugin concepts](https://eli.thegreenplace.net/2012/08/07/fundamental-concepts-of-plugin-infrastructures) that were covered [several times on this blog](https://eli.thegreenplace.net/tag/plugins).

### Discovery

Discovery in mdBook is very explicit. For every plugin we want mdBook to use, it has to be listed in the project's `book.toml` configuration file. For example, in [the code sample for this post](https://github.com/eliben/code-for-blog/tree/main/2025/plugin-mdbook), the Python narcissist plugin is noted in `book.toml` as follows:
    
    
    [preprocessor.narcissistpy]
    command = "python3 ../preprocessor-python-narcissist/narcissist.py"
    

Each preprocessor is a command for `mdBook` to execute in a sub-process. Here it uses Python, but it can be anything else that can be validly executed.

### Registration

For the purpose of registration, `mdBook` actually invokes the plugin command _twice_. The first time, it passes the arguments `supports <renderer>` where `<renderer>` is the name of the renderer (e.g. `html`). If the command returns 0, it means the preprocessor supports this renderer; otherwise, it doesn't.

In the second invocation, `mdBook` passes some metadata plus the entire book in JSON format to the preprocessor through stdin, and expects the preprocessor to return the modified book as JSON to stdout (using the same schema).

### Hooks

In terms of hooks, `mdBook` takes a very coarse-grained approach. The preprocessor gets the _entire book_ in a single JSON object (along with a context object that contains metadata), and is expected to emit the entire modified book in a single JSON object. It's up to the preprocessor to figure out which parts of the book to read and which parts to modify.

Given that books and other documentation typically have limited sizes, this is a reasonable design choice. Even tens of MiB of JSON-encoded data are very quick to pass between sub-processes via stdout and marshal/unmarshal. But we wouldn't be able to implement Wikipedia using this design.

### Exposing an application API to plugins

This is tricky, given that the preprocessor mechanism is language-agnostic. Here, `mdBook` offers some additional utilities to preprocessors implemented in Rust, however. These get access to `mdBook`'s API to unmarshal the JSON representing the context metadata and book's contents. `mdBook` offers the [Preprocessor trait](https://docs.rs/mdbook-preprocessor/latest/mdbook_preprocessor/trait.Preprocessor.html) Rust preprocessors can implement, which makes it easier to wrangle the book's contents. See [my Rust version of the narcissist preprocessor](https://github.com/eliben/code-for-blog/tree/main/2025/plugin-mdbook/preprocessor-rust-narcissist) for a basic example of this.

## Renderers / backends

Actually, `mdBook` has _another_ plugin mechanism, but it's very similar conceptually to preprocessors. A _renderer_ (also called a _backend_ in some of `mdBook`'s own doc pages) takes the same input as a preprocessor, but is free to do whatever it wants with it. The default renderer emits the HTML for the book; [other renderers](https://github.com/rust-lang/mdBook/wiki/Third-party-plugins#backends) can do other things.

The idea is that the book can go through multiple preprocessors, but at the end a _single_ renderer.

The data a renderer receives is exactly the same as a preprocessor - JSON encoded book contents. Due to this similarity, there's no real point getting deeper into renderers in this post.

* * *

For comments, please send me [__an email](mailto:eliben@gmail.com). 

* * *

(C) 2003-2025 Eli Bendersky 

__Back to top
