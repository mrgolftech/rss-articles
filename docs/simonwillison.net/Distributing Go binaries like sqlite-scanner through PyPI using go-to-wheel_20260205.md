# Distributing Go binaries like sqlite-scanner through PyPI using go-to-wheel

**来源:** https://simonwillison.net
**链接:** https://simonwillison.net/2026/Feb/4/distributing-go-binaries/#atom-everything
**日期:** 2026-02-04T14:59:47+00:00

---

# [Simon Willison’s Weblog](/)

[Subscribe](/about/#subscribe)

## Distributing Go binaries like sqlite-scanner through PyPI using go-to-wheel

4th February 2026

I’ve been exploring Go for building small, fast and self-contained binary applications recently. I’m enjoying how there’s generally one obvious way to do things and the resulting code is boring and readable—and something that LLMs are very competent at writing. The one catch is distribution, but it turns out publishing Go binaries to PyPI means any Go binary can be just a `uvx package-name` call away.

#### sqlite-scanner

[sqlite-scanner](https://github.com/simonw/sqlite-scanner) is my new Go CLI tool for scanning a filesystem for SQLite database files.

It works by checking if the first 16 bytes of the file exactly match the SQLite magic number sequence `SQLite format 3\x00`. It can search one or more folders recursively, spinning up concurrent goroutines to accelerate the scan. It streams out results as it finds them in plain text, JSON or newline-delimited JSON. It can optionally display the file sizes as well.

To try it out you can download a release from the [GitHub releases](https://github.com/simonw/sqlite-scanner/releases)—and then [jump through macOS hoops](https://support.apple.com/en-us/102445) to execute an “unsafe” binary. Or you can clone the repo and compile it with Go. Or... you can run the binary like this:
    
    
    uvx sqlite-scanner
    

By default this will search your current directory for SQLite databases. You can pass one or more directories as arguments:
    
    
    uvx sqlite-scanner ~ /tmp
    

Add `--json` for JSON output, `--size` to include file sizes or `--jsonl` for newline-delimited JSON. Here’s a demo:
    
    
    uvx sqlite-scanner ~ --jsonl --size
    

![running that command produces a sequence of JSON objects, each with a path and a size key](https://static.simonwillison.net/static/2025/sqlite-scanner-demo.gif)

If you haven’t been uv-pilled yet you can instead install `sqlite-scanner` using `pip install sqlite-scanner` and then run `sqlite-scanner`.

To get a permanent copy with `uv` use `uv tool install sqlite-scanner`.

#### How the Python package works

The reason this is worth doing is that `pip`, `uv` and [PyPI](https://pypi.org/) will work together to identify the correct compiled binary for your operating system and architecture.

This is driven by file names. If you visit [the PyPI downloads for sqlite-scanner](https://pypi.org/project/sqlite-scanner/#files) you’ll see the following files:

  * `sqlite_scanner-0.1.1-py3-none-win_arm64.whl`
  * `sqlite_scanner-0.1.1-py3-none-win_amd64.whl`
  * `sqlite_scanner-0.1.1-py3-none-musllinux_1_2_x86_64.whl`
  * `sqlite_scanner-0.1.1-py3-none-musllinux_1_2_aarch64.whl`
  * `sqlite_scanner-0.1.1-py3-none-manylinux_2_17_x86_64.whl`
  * `sqlite_scanner-0.1.1-py3-none-manylinux_2_17_aarch64.whl`
  * `sqlite_scanner-0.1.1-py3-none-macosx_11_0_arm64.whl`
  * `sqlite_scanner-0.1.1-py3-none-macosx_10_9_x86_64.whl`



When I run `pip install sqlite-scanner` or `uvx sqlite-scanner` on my Apple Silicon Mac laptop Python’s packaging magic ensures I get that `macosx_11_0_arm64.whl` variant.

Here’s [what’s in the wheel](https://tools.simonwillison.net/zip-wheel-explorer?url=https%3A%2F%2Ffiles.pythonhosted.org%2Fpackages%2F88%2Fb1%2F17a716635d2733fec53ba0a8267f85bd6b6cf882c6b29301bc711fba212c%2Fsqlite_scanner-0.1.1-py3-none-macosx_11_0_arm64.whl#sqlite_scanner/__init__.py), which is a zip file with a `.whl` extension.

In addition to the `bin/sqlite-scanner` the most important file is `sqlite_scanner/__init__.py` which includes the following:
    
    
    def get_binary_path():
        """Return the path to the bundled binary."""
        binary = os.path.join(os.path.dirname(__file__), "bin", "sqlite-scanner")
     
        # Ensure binary is executable on Unix
        if sys.platform != "win32":
            current_mode = os.stat(binary).st_mode
            if not (current_mode & stat.S_IXUSR):
                os.chmod(binary, current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
     
        return binary
     
     
    def main():
        """Execute the bundled binary."""
        binary = get_binary_path()
     
        if sys.platform == "win32":
            # On Windows, use subprocess to properly handle signals
            sys.exit(subprocess.call([binary] + sys.argv[1:]))
        else:
            # On Unix, exec replaces the process
            os.execvp(binary, [binary] + sys.argv[1:])

That `main()` method—also called from `sqlite_scanner/__main__.py`—locates the binary and executes it when the Python package itself is executed, using the `sqlite-scanner = sqlite_scanner:main` entry point defined in the wheel.

#### Which means we can use it as a dependency

Using PyPI as a distribution platform for Go binaries feels a tiny bit abusive, albeit [there is plenty of precedent](https://simonwillison.net/2022/May/23/bundling-binary-tools-in-python-wheels/).

I’ll justify it by pointing out that this means **we can use Go binaries as dependencies** for other Python packages now.

That’s genuinely useful! It means that any functionality which is available in a cross-platform Go binary can now be subsumed into a Python package. Python is really good at running subprocesses so this opens up a whole world of useful tricks that we can bake into our Python tools.

To demonstrate this, I built [datasette-scan](https://github.com/simonw/datasette-scan)—a new Datasette plugin which depends on `sqlite-scanner` and then uses that Go binary to scan a folder for SQLite databases and attach them to a Datasette instance.

Here’s how to use that (without even installing anything first, thanks `uv`) to explore any SQLite databases in your Downloads folder:
    
    
    uv run --with datasette-scan datasette scan ~/Downloads

If you peek at the code you’ll see it [depends on sqlite-scanner](https://github.com/simonw/datasette-scan/blob/1a2b6d1e6b04c8cd05f5676ff7daa877efd99f08/pyproject.toml#L14) in `pyproject.toml` and calls it using `subprocess.run()` against `sqlite_scanner.get_binary_path()` in its own [scan_directories() function](https://github.com/simonw/datasette-scan/blob/1a2b6d1e6b04c8cd05f5676ff7daa877efd99f08/datasette_scan/__init__.py#L38-L58).

I’ve been exploring this pattern for other, non-Go binaries recently—here’s [a recent script](https://github.com/simonw/tools/blob/main/python/livestream-gif.py) that depends on [static-ffmpeg](https://pypi.org/project/static-ffmpeg/) to ensure that `ffmpeg` is available for the script to use.

#### Building Python wheels from Go packages with go-to-wheel

After trying this pattern myself a couple of times I realized it would be useful to have a tool to automate the process.

I first [brainstormed with Claude](https://claude.ai/share/2d9ced56-b3e8-4651-83cc-860b9b419187) to check that there was no existing tool to do this. It pointed me to [maturin bin](https://www.maturin.rs/bindings.html#bin) which helps distribute Rust projects using Python wheels, and [pip-binary-factory](https://github.com/Bing-su/pip-binary-factory) which bundles all sorts of other projects, but did not identify anything that addressed the exact problem I was looking to solve.

So I [had Claude Code for web build the first version](https://gisthost.github.io/?41f04e4eb823b1ceb888d9a28c2280dd/index.html), then refined the code locally on my laptop with the help of more Claude Code and a little bit of OpenAI Codex too, just to mix things up.

The full documentation is in the [simonw/go-to-wheel](https://github.com/simonw/go-to-wheel) repository. I’ve published that tool to PyPI so now you can run it using:
    
    
    uvx go-to-wheel --help

The `sqlite-scanner` package you can [see on PyPI](https://pypi.org/project/sqlite-scanner/) was built using `go-to-wheel` like this:
    
    
    uvx go-to-wheel ~/dev/sqlite-scanner \
      --set-version-var main.version \
      --version 0.1.1 \
      --readme README.md \
      --author 'Simon Willison' \
      --url https://github.com/simonw/sqlite-scanner \
      --description 'Scan directories for SQLite databases'

This created a set of wheels in the `dist/` folder. I tested one of them like this:
    
    
    uv run --with dist/sqlite_scanner-0.1.1-py3-none-macosx_11_0_arm64.whl \
      sqlite-scanner --version

When that spat out the correct version number I was confident everything had worked as planned, so I pushed the whole set of wheels to PyPI using `twine upload` like this:
    
    
    uvx twine upload dist/*

I had to paste in a PyPI API token I had saved previously and that was all it took.

#### I expect to use this pattern a lot

`sqlite-scanner` is very clearly meant as a proof-of-concept for this wider pattern—Python is very much capable of recursively crawling a directory structure looking for files that start with a specific byte prefix on its own!

That said, I think there’s a _lot_ to be said for this pattern. Go is a great complement to Python—it’s fast, compiles to small self-contained binaries, has excellent concurrency support and a rich ecosystem of libraries.

Go is similar to Python in that it has a strong standard library. Go is particularly good for HTTP tooling—I’ve built several HTTP proxies in the past using Go’s excellent `net/http/httputil.ReverseProxy` handler.

I’ve also been experimenting with [wazero](https://github.com/wazero/wazero), Go’s robust and mature zero dependency WebAssembly runtime as part of my ongoing quest for the ideal sandbox for running untrusted code. [Here’s my latest experiment](https://github.com/simonw/research/tree/main/wasm-repl-cli) with that library.

Being able to seamlessly integrate Go binaries into Python projects without the end user having to think about Go at all—they `pip install` and everything Just Works—feels like a valuable addition to my toolbox.

Posted [4th February 2026](/2026/Feb/4/) at 2:59 pm * Follow me on [Mastodon](https://fedi.simonwillison.net/@simon), [Bluesky](https://bsky.app/profile/simonwillison.net), [Twitter](https://twitter.com/simonw) or [subscribe to my newsletter](https://simonwillison.net/about/#subscribe)

## More recent articles

  * [Moltbook is the most interesting place on the internet right now](/2026/Jan/30/moltbook/) \- 30th January 2026
  * [Adding dynamic features to an aggressively cached website](/2026/Jan/28/dynamic-features-static-site/) \- 28th January 2026



This is **Distributing Go binaries like sqlite-scanner through PyPI using go-to-wheel** by Simon Willison, posted on [4th February 2026](/2026/Feb/4/).

[ go 48 ](/tags/go/) [ packaging 44 ](/tags/packaging/) [ projects 517 ](/tags/projects/) [ pypi 42 ](/tags/pypi/) [ python 1225 ](/tags/python/) [ sqlite 312 ](/tags/sqlite/) [ datasette 454 ](/tags/datasette/) [ ai-assisted-programming 317 ](/tags/ai-assisted-programming/) [ uv 88 ](/tags/uv/)

**Previous:** [Moltbook is the most interesting place on the internet right now](/2026/Jan/30/moltbook/)

###  Monthly briefing 

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments. 

Pay me to send you less! 

[ Sponsor & subscribe ](https://github.com/sponsors/simonw/)

  * [Colophon](/about/#about-site)
  * (C)
  * [2002](/2002/)
  * [2003](/2003/)
  * [2004](/2004/)
  * [2005](/2005/)
  * [2006](/2006/)
  * [2007](/2007/)
  * [2008](/2008/)
  * [2009](/2009/)
  * [2010](/2010/)
  * [2011](/2011/)
  * [2012](/2012/)
  * [2013](/2013/)
  * [2014](/2014/)
  * [2015](/2015/)
  * [2016](/2016/)
  * [2017](/2017/)
  * [2018](/2018/)
  * [2019](/2019/)
  * [2020](/2020/)
  * [2021](/2021/)
  * [2022](/2022/)
  * [2023](/2023/)
  * [2024](/2024/)
  * [2025](/2025/)
  * [2026](/2026/)
  * 

