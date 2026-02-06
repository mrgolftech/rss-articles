# Introducing Deno Sandbox

**来源:** https://simonwillison.net
**链接:** https://simonwillison.net/2026/Feb/3/introducing-deno-sandbox/#atom-everything
**日期:** 2026-02-03T22:44:50+00:00

---

# [Simon Willison’s Weblog](/)

[Subscribe](/about/#subscribe)

**[Introducing Deno Sandbox](https://deno.com/blog/introducing-deno-sandbox)** ([via](https://news.ycombinator.com/item?id=46874097 "Hacker News")) Here's a new hosted sandbox product from the Deno team. It's actually unrelated to Deno itself - this is part of their Deno Deploy SaaS platform. As such, you don't even need to use JavaScript to access it - you can create and execute code in a hosted sandbox using their [deno-sandbox](https://pypi.org/project/deno-sandbox/) Python library like this:
    
    
    export DENO_DEPLOY_TOKEN="... API token ..."
    uv run --with deno-sandbox python

Then:
    
    
    from deno_sandbox import DenoDeploy
    
    sdk = DenoDeploy()
    
    with sdk.sandbox.create() as sb:
        # Run a shell command
        process = sb.spawn(
            "echo", args=["Hello from the sandbox!"]
        )
        process.wait()
        # Write and read files
        sb.fs.write_text_file(
            "/tmp/example.txt", "Hello, World!"
        )
        print(sb.fs.read_text_file(
            "/tmp/example.txt"
        ))

There’s a JavaScript client library as well. The underlying API isn’t documented yet but appears [to use WebSockets](https://tools.simonwillison.net/zip-wheel-explorer?package=deno-sandbox#deno_sandbox/sandbox.py--L187).

There’s a lot to like about this system. Sandboxe instances can have up to 4GB of RAM, get 2 vCPUs, 10GB of ephemeral storage, can mount persistent volumes and can use snapshots to boot pre-configured custom images quickly. Sessions can last up to 30 minutes and are billed by CPU time, GB-h of memory and volume storage usage.

When you create a sandbox you can configure network domains it’s allowed to access.

My favorite feature is the way it handles API secrets.
    
    
    with sdk.sandboxes.create(
        allowNet=["api.openai.com"],
        secrets={
            "OPENAI_API_KEY": {
                "hosts": ["api.openai.com"],
                "value": os.environ.get("OPENAI_API_KEY"),
            }
        },
    ) as sandbox:
        # ... $OPENAI_API_KEY is available

Within the container that `$OPENAI_API_KEY` value is set to something like this:
    
    
    DENO_SECRET_PLACEHOLDER_b14043a2f578cba...
    

Outbound API calls to `api.openai.com` run through a proxy which is aware of those placeholders and replaces them with the original secret.

In this way the secret itself is not available to code within the sandbox, which limits the ability for malicious code (e.g. from a prompt injection) to exfiltrate those secrets.

From [a comment on Hacker News](https://news.ycombinator.com/item?id=46874097#46874959) I learned that Fly have a project called [tokenizer](https://github.com/superfly/tokenizer) that implements the same pattern. Adding this to my list of tricks to use with sandoxed environments!

Posted [3rd February 2026](/2026/Feb/3/) at 10:44 pm

## Recent articles

  * [Distributing Go binaries like sqlite-scanner through PyPI using go-to-wheel](/2026/Feb/4/distributing-go-binaries/) \- 4th February 2026
  * [Moltbook is the most interesting place on the internet right now](/2026/Jan/30/moltbook/) \- 30th January 2026
  * [Adding dynamic features to an aggressively cached website](/2026/Jan/28/dynamic-features-static-site/) \- 28th January 2026



[ python 1225 ](/tags/python/) [ sandboxing 33 ](/tags/sandboxing/) [ security 574 ](/tags/security/) [ deno 26 ](/tags/deno/) [ fly 37 ](/tags/fly/)

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

