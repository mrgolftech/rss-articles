# Writing an LLM from scratch, part 26 -- evaluating the fine-tuned model

**来源:** https://gilesthomas.com
**链接:** https://www.gilesthomas.com/2025/11/llm-from-scratch-26-evaluating-the-fine-tuned-model
**日期:** Mon, 03 Nov 2025 19:40:00 +0000

---

[Giles' blog](/)

[![Me on X/Twitter](/images/x-icon.png)](https://x.com/gpjt) [![Me on Bluesky](/images/bluesky-icon.png)](https://bsky.app/profile/gilesthomas.com) [![My GitHub profile](/images/github-icon.png)](https://github.com/gpjt) [![My Hugging Face profile](/images/hf-icon.png)](https://huggingface.co/gpjt) [![RSS feed for this blog](/images/rss-icon.png)](/feed/rss.xml)

[About](/about)

[Contact](/contact)

Archives 

Categories 

Blogroll 

  * [ February 2026 (2) ](/2026/02)
  * [ January 2026 (4) ](/2026/01)
  * [ December 2025 (1) ](/2025/12)
  * [ November 2025 (3) ](/2025/11)
  * [ October 2025 (9) ](/2025/10)
  * [ September 2025 (3) ](/2025/09)
  * [ August 2025 (5) ](/2025/08)
  * [ July 2025 (1) ](/2025/07)
  * [ June 2025 (2) ](/2025/06)
  * [ May 2025 (3) ](/2025/05)
  * [ April 2025 (2) ](/2025/04)
  * [ March 2025 (7) ](/2025/03)
  * [ February 2025 (10) ](/2025/02)
  * [ January 2025 (6) ](/2025/01)
  * [ December 2024 (7) ](/2024/12)
  * [ September 2024 (1) ](/2024/09)
  * [ August 2024 (2) ](/2024/08)
  * [ July 2024 (2) ](/2024/07)
  * [ May 2024 (2) ](/2024/05)
  * [ April 2024 (2) ](/2024/04)
  * [ February 2024 (2) ](/2024/02)
  * [ April 2023 (1) ](/2023/04)
  * [ March 2023 (2) ](/2023/03)
  * [ September 2022 (1) ](/2022/09)
  * [ February 2022 (1) ](/2022/02)
  * [ November 2021 (1) ](/2021/11)
  * [ March 2021 (1) ](/2021/03)
  * [ February 2021 (2) ](/2021/02)
  * [ August 2019 (1) ](/2019/08)
  * [ November 2018 (1) ](/2018/11)
  * [ May 2017 (1) ](/2017/05)
  * [ December 2016 (1) ](/2016/12)
  * [ April 2016 (1) ](/2016/04)
  * [ August 2015 (1) ](/2015/08)
  * [ December 2014 (1) ](/2014/12)
  * [ August 2014 (1) ](/2014/08)
  * [ March 2014 (1) ](/2014/03)
  * [ December 2013 (1) ](/2013/12)
  * [ October 2013 (3) ](/2013/10)
  * [ September 2013 (4) ](/2013/09)
  * [ August 2013 (2) ](/2013/08)
  * [ July 2013 (1) ](/2013/07)
  * [ June 2013 (1) ](/2013/06)
  * [ February 2013 (1) ](/2013/02)
  * [ October 2012 (1) ](/2012/10)
  * [ June 2012 (1) ](/2012/06)
  * [ May 2012 (1) ](/2012/05)
  * [ April 2012 (1) ](/2012/04)
  * [ February 2012 (1) ](/2012/02)
  * [ October 2011 (1) ](/2011/10)
  * [ June 2011 (1) ](/2011/06)
  * [ May 2011 (1) ](/2011/05)
  * [ April 2011 (1) ](/2011/04)
  * [ March 2011 (1) ](/2011/03)
  * [ February 2011 (1) ](/2011/02)
  * [ January 2011 (1) ](/2011/01)
  * [ December 2010 (3) ](/2010/12)
  * [ November 2010 (1) ](/2010/11)
  * [ October 2010 (1) ](/2010/10)
  * [ September 2010 (1) ](/2010/09)
  * [ August 2010 (1) ](/2010/08)
  * [ July 2010 (1) ](/2010/07)
  * [ May 2010 (3) ](/2010/05)
  * [ April 2010 (1) ](/2010/04)
  * [ March 2010 (2) ](/2010/03)
  * [ February 2010 (3) ](/2010/02)
  * [ January 2010 (4) ](/2010/01)
  * [ December 2009 (2) ](/2009/12)
  * [ November 2009 (5) ](/2009/11)
  * [ October 2009 (2) ](/2009/10)
  * [ September 2009 (2) ](/2009/09)
  * [ August 2009 (3) ](/2009/08)
  * [ July 2009 (1) ](/2009/07)
  * [ May 2009 (1) ](/2009/05)
  * [ April 2009 (1) ](/2009/04)
  * [ March 2009 (5) ](/2009/03)
  * [ February 2009 (5) ](/2009/02)
  * [ January 2009 (5) ](/2009/01)
  * [ December 2008 (3) ](/2008/12)
  * [ November 2008 (7) ](/2008/11)
  * [ October 2008 (4) ](/2008/10)
  * [ September 2008 (2) ](/2008/09)
  * [ August 2008 (1) ](/2008/08)
  * [ July 2008 (1) ](/2008/07)
  * [ June 2008 (1) ](/2008/06)
  * [ May 2008 (1) ](/2008/05)
  * [ April 2008 (1) ](/2008/04)
  * [ January 2008 (4) ](/2008/01)
  * [ December 2007 (3) ](/2007/12)
  * [ March 2007 (3) ](/2007/03)
  * [ February 2007 (1) ](/2007/02)
  * [ January 2007 (2) ](/2007/01)
  * [ December 2006 (4) ](/2006/12)
  * [ November 2006 (18) ](/2006/11)



  * [ AI (68) ](/ai)
  * [ TIL deep dives (63) ](/til-deep-dives)
  * [ Python (62) ](/python)
  * [ LLM from scratch (34) ](/llm-from-scratch)
  * [ Resolver One (34) ](/resolver-one)
  * [ Blogkeeping (18) ](/blogkeeping)
  * [ PythonAnywhere (17) ](/pythonanywhere)
  * [ Linux (16) ](/linux)
  * [ Startups (15) ](/startups)
  * [ NSLU2 offsite backup project (13) ](/nslu2-offsite-backup-project)
  * [ TIL (13) ](/til)
  * [ Hugging Face (12) ](/hugging-face)
  * [ Funny (11) ](/funny)
  * [ Finance (10) ](/finance)
  * [ Fine-tuning LLMs (10) ](/fine-tuning)
  * [ Musings (10) ](/musings)
  * [ C (9) ](/c)
  * [ Gadgets (8) ](/gadgets)
  * [ Personal (8) ](/personal)
  * [ Robotics (8) ](/robotics)
  * [ Website design (8) ](/website-design)
  * [ 3D (5) ](/3d)
  * [ Rants (5) ](/rants)
  * [ Cryptography (4) ](/cryptography)
  * [ JavaScript (4) ](/javascript)
  * [ Music (4) ](/music)
  * [ Oddities (4) ](/oddities)
  * [ Quick links (4) ](/quick-links)
  * [ Talks (4) ](/talks)
  * [ Dirigible (3) ](/dirigible)
  * [ Eee (3) ](/eee)
  * [ Memes (3) ](/memes)
  * [ Politics (3) ](/politics)
  * [ Django (2) ](/django)
  * [ GPU Computing (2) ](/gpu-computing)
  * [ LaTeX (2) ](/latex)
  * [ MathML (2) ](/mathml)
  * [ OLPC XO (2) ](/olpc-xo)
  * [ Retro Language Models (2) ](/retro-language-models)
  * [ Space (2) ](/space)
  * [ VoIP (2) ](/voip)
  * [ Copyright (1) ](/copyright)
  * [ Golang (1) ](/golang)
  * [ Raspberry Pi (1) ](/raspberry-pi)
  * [ Software development tools (1) ](/software-dev-tools)



  * [Agile Abstractions](https://agileabstractions.com/)
  * [Astral Codex Ten](https://www.astralcodexten.com/)
  * [:: (Bloggable a) => a -> IO ()](https://blog.omega-prime.co.uk/)
  * [David Friedman's Substack](https://daviddfriedman.substack.com/)
  * [Econ & Energy](https://robertsmithson1.substack.com/)
  * [Entrepreneurial Geekiness](https://ianozsvald.com/)
  * [For some value of "Magic"](https://holdenweb.blogspot.com/)
  * [Hackaday](https://hackaday.com/)
  * [kaleidic.ai newsletter](https://kaleidic.substack.com/)
  * [Knowing.NET](https://knowing.net/)
  * [Language Log](https://languagelog.ldc.upenn.edu/nll/)
  * [Millennium Hand](http://blog.millenniumhand.co.uk/)
  * [ntoll.org](https://ntoll.org/)
  * [Obey the Testing Goat!](https://www.obeythetestinggoat.com/)
  * [PK](https://pkaznowski.gitlab.io/projects/)
  * [PythonAnywhere News](https://blog.pythonanywhere.com/)
  * [Simon Willison's Weblog](https://simonwillison.net/)
  * [Societive](https://medium.com/@societive)
  * [Software Deviser](https://orestis.gr/)
  * [Some opinions, held with varying degrees of certainty](https://filip.lajszczak.dev/)
  * [tartley.com](https://www.tartley.com/)



## Writing an LLM from scratch, part 26 -- evaluating the fine-tuned model

Posted on 3 [November 2025](/2025/11/) in [AI](/ai), [LLM from scratch](/llm-from-scratch), [TIL deep dives](/til-deep-dives)

This post is on the second half of chapter 7 of [Sebastian Raschka](https://sebastianraschka.com/)'s book "[Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)". In the [last post](/2025/10/llm-from-scratch-25-instruction-fine-tuning) I covered the part of the chapter that covers instruction fine-tuning; this time round, we evaluate our model -- particularly interestingly, we try using another, smarter, model to judge how good its responses are.

Once again, Raschka's explanation in this section is very clear, and there's not that much that was conceptually new to me, so I don't have that many notes -- in fact, this post is probably the shortest one in my series so far!

### Generating the test set responses

Unusually, when at the start of section 7.7 we generate some sample responses for the instructions in our test set, I got exactly the same results as in the book. For once, I guess, everything that uses randomness was happening in the same order as it did when Raschka ran it on his machine.

The next step was to generate a file with all of the responses to all of the test instructions, which took 18.9 seconds on my RTX 3090 (compared to a minute on an A100, per the book -- that's quite surprising!)

Once that was done, it was time to install Ollama so that I could use the Llama 3 model to evaluate my own.

### Ollama

I've never used Ollama before -- when playing with other people's models, I've always used [Hugging Face's Transformers](https://huggingface.co/docs/transformers/en/index) library.

It's a neat package, though. It wraps `llama.cpp`, which is a pure C/C++ inference framework (with CUDA support), and makes it easy to download and run models that have been packaged for it. Being written in C, I would imagine that it's faster than PyTorch/Transformers -- though, being inference-only, it's less useful if you're planning to do things like training or fine-tuning the models.

My desktop is running a fairly customised install of Arch Linux, and I didn't want to use the default install procedure (which puts it into your system-wide `/bin` and `/lib` directories). But it turns out that it's a very well-packaged app, and you don't need to do that.

Using the manual [install instructions for Linux](https://docs.ollama.com/linux), I just created a new directory `~/Dev/ollama`, and then `cd`ed there and downloaded it:
    
    
    wget https://ollama.com/download/ollama-linux-amd64.tgz
    

It was about 1.75 GiB. I then untarred it:
    
    
    tar xf ollama-linux-amd64.tgz
    

...and then I could run commands with full paths, for example:
    
    
    ~/Dev/ollama/bin/ollama serve
    

...to start up the server, or
    
    
    ~/Dev/ollama/bin/ollama run llama3
    

...to start a session.

Neat! It's always good to see pre-built binary packages that have no issues with their install location.

### Actually running the evaluation

The next step was to throw all of the generated test responses (and their associated targets) at Llama 3 and see what it thought about how close they were.

Again, this all worked without trouble. I noted that the responses I was getting from Llama 3 were not the same as the ones in the book -- Raschka notes that Ollama is non-deterministic, so there's no surprise there (though it does make me wonder why it accepts a `seed` parameter in the API call).

When I got on to the final eval, where you run the test results through Llama 3 and ask it to rate them compared to the target outputs, it took 11 seconds to run, and I got an average score of 48.95 / 100, which is close enough to the 50.32 that appears in the book. 1 I'd run an eval on my model, using a smarter model to judge its responses!

Somewhat surprisingly, that number was stable over multiple runs. So perhaps there is some level of determinism in Ollama now that wasn't present when the book was written, and the seed (eg. `123`) is of value. Or perhaps Raschka's comment about it being non-deterministic was more of a "between machines" thing rather than for multiple runs on the same machine \-- though then I'm not sure why he suggests re-running it for multiple results.

Anyway -- that was it! Eval done. And, to my amazement, that was the end of the chapter -- and almost the end of the book. We've built an LLM from scratch, fine-tuned it, and evaluated it by using a smarter model to judge how well it was following instructions.

### This is the end...

...or at least the end of the beginning.

Having run the evaluation, I've reached the end of the main part of "[Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)". But I don't think I've reached the end of this project, there's still more to do (not least working through the appendices).

So, coming up next: a post summarising what I've got through so far in this series, and what the next steps are to wrap it up.

[Here's a link to the next post in this series](/2025/11/llm-from-scratch-27-whats-left-and-whats-next).

* * *

  1. I also got 110 out of 110 scores -- that is, every response from Llama 3 was parseable as an integer. That actually kind of surprised me! Models like to be chatty and helpful. But looking into it, [the famous X post by Riley Goodside](https://x.com/goodside/status/1657396491676164096) where he had to "threaten" Bard to stop it from saying "Sure, no problem! Here's your JSON" was almost two years ago. ↩




[« Writing an LLM from scratch, part 25 -- instruction fine-tuning](/2025/10/llm-from-scratch-25-instruction-fine-tuning) [Writing an LLM from scratch, part 27 -- what's left, and what's next? »](/2025/11/llm-from-scratch-27-whats-left-and-whats-next)

Copyright (c) 2006-2026 by Giles Thomas. This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). 
