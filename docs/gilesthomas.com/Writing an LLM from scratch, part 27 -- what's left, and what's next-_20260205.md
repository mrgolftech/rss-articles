# Writing an LLM from scratch, part 27 -- what's left, and what's next?

**来源:** https://gilesthomas.com
**链接:** https://www.gilesthomas.com/2025/11/llm-from-scratch-27-whats-left-and-whats-next
**日期:** Tue, 04 Nov 2025 00:40:00 +0000

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



## Writing an LLM from scratch, part 27 -- what's left, and what's next?

Posted on 4 [November 2025](/2025/11/) in [AI](/ai), [LLM from scratch](/llm-from-scratch), [TIL deep dives](/til-deep-dives)

On 22 December 2024, [I wrote](/2024/12/llm-from-scratch-1):

> Over the Christmas break (and probably beyond) I'm planning to work through [Sebastian Raschka](https://sebastianraschka.com/)'s book "[Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)". I'm expecting to get through a chapter or less a day, in order to give things time to percolate properly. Each day, or perhaps each chapter, I'll post here about anything I find particularly interesting.

More than ten months and 26 blog posts later, I've reached the end of the main body of the book -- there's just the appendices to go. Even allowing for the hedging, my optimism was adorable.

I don't want to put anyone else off the book by saying that, though! I expect most people will get through it much faster. I made a deliberate decision at the start to write up everything I learned as I worked through it, and that, I think, has helped me solidify things in my mind much better than I would have done if I'd only been reading it and doing the exercises. But on the other hand, writing things up does take a _lot_ of time, much more than the actual learning does. It's worth it for me, but probably isn't for everyone.

So, what next? I've finished the main body of the book, and built up a decent backlog as I did so. What do I need to do before I can treat my "LLM from scratch" journey as done? And what other ideas have come up while I worked through it that might be good bases for future, similar series?

There are a few sources of ideas for this -- from the book itself and its supplementary material, from notes I've made as I went along, and from other things that I've kept on a mental checklist.

### The appendices and supplementary material

There are five appendices:

  * A: An introduction to PyTorch
  * B: References and further reading
  * C: Exercise solutions
  * D: Adding bells and whistles to the training loop
  * E: Parameter-efficient fine-tuning with LoRA



Raschka also gives a link at the end of chapter 7 to a notebook showing how to do further fine tuning using [Direct Preference Optimization](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch07/04_preference-tuning-with-dpo), which also looks fascinating, and he's working on a new project, "[Build a reasoning model (from scratch)](https://github.com/rasbt/reasoning-from-scratch)".

### Things I've deferred myself

While working through the book, I've deliberately deferred various things. I'd kind of lost track of all of them, so I gave ChatGPT the source markdown for all of the posts in this series, and asked it to find where I'd done that. It did an amazing job! There were three categories: long context and attention efficiency, maths, and optimisers.

#### Long context and attention efficiency.

The model we've built in the book has a context length of 1,024 tokens, and is O(n2) in both space and time with respect to the number of tokens you feed it. There are lots of things that people do to work around that. Things I need to learn:

  * **The KV cache**. This is basic stuff and I feel I sorta-kinda understand it, but I haven't written about it so I can't be sure. It's a pretty obvious enhancement to avoid repeating work when generating autoregressively -- that is, the normal setup where in order to generate n tokens, we give the model its input, sample our first token from its predictions, then feed the whole thing -- the input and that first token -- back in for the second token, and so on. Obviously, because attention is causal, we're doing exactly the same work every time for all of the tokens in each round apart from the last one, so it makes sense to cache things. The result is that generating the first token is still O(n2), but subsequent ones will be something more like O(n) each. That's why real-world modern models tend to take a while pondering before they generate the first token but then speed up -- they need to fill their cache.
  * **FlashAttention** and related things: there are lots of ways people have found to reduce the cost of attention generally, but this seems to be the most popular one, or at least the best to get started with.
  * **Better positional embeddings** : the context length of our GPT-2-style LLM is fixed in part because you need position embeddings for every possible input position. That means that we can never extend it. More modern LLMs use better ways to represent positions -- Rotary Position Embeddings (RoPE) look like they're very popular.



#### Maths

I really want to understand softmax at a better level than "it's a magic thing that turns logits into probabilities". I'd also like to learn more about higher-order tensor operations -- the ones that we use in the book are essentially treating the extra dimensions as the batch, but I believe that there's more to it than that.

#### Optimisers

I really want to understand in reasonable depth what optimisers do. I know that they make gradient updates work better than they do with simple gradient descent. But how?

* * *

That was the set of things I noted at the time I wrote the posts so far, but there are a few more that come to mind as I write this.

### Automatic differentiation and the backward pass

In some comments that he made on posts in this series, `Simon` said that it seems like this book isn't really "from scratch", given that we rely on PyTorch's magic to handle the backward pass.

He's 100% right! I think I understand why it is that way, though. There would be two different ways that I can see for the book to do it:

  * Manually code a backward pass to go with the forward pass on each of our modules. Simon did this, and was kind enough to share his code with me -- it looks like one of those things (like attention) that is pretty hard to get your head around initially, but once it clicks it's super-clear. Definitely kudos to him for getting it all to work! The problem with this is that I don't think any ML practitioners do this nowadays, because automatic differentiation is there in every popular framework. So it might be a good learning experience, but also might nudge people into an unprofitable direction.
  * Create our own automatic differentiation system. Andrej Karpathy pops up again when looking into this; he created [micrograd](https://github.com/karpathy/micrograd), which handles back-propagation for scalar functions. That's really clever -- but it would be hard, and a bit of a side quest from the point of the book. Also, the most interesting stuff (at least from what little I know) for automatic differentiation is how you do it with non-scalars -- the matrices and higher-order tensors that our LLM uses. From what Simon says, this is where you need to use the mysterious Jacobian matrices I've heard about in the context of back-propagation.



I think I'd definitely like to revisit that at some point.

### Tokenisers

Another one from Simon; while the book does explain how tokenisers work, even down to a high-level overview of byte-pair encoding, we don't write our own. Again, I can see why this is -- we load in the GPT-2 weights, so we need to use that model's tokeniser. And there's no point in writing our own if we're just going to throw it away.

But perhaps a bit of time playing with one would be useful?

#### Trying to train the LLM as a base model

The book, quite reasonably, shows you how to train your LLM, does a basic train on a small dataset, and then we switch to downloading the "pre-cooked" weights from OpenAI. That makes sense given that not every reader will have access to enough hardware to really train from scratch.

But given that I was getting a pretty good training speed on my own hardware, perhaps I could train a model really from scratch, perhaps using one of the smaller [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) datasets? Even if I can't do it locally, perhaps it might be doable on a rented cloud machine, like the Lambda Labs ones I used when [fine-tuning Llama 3](/fine-tuning)?

After all, Andrej Karpathy is training [a full model that you can chat with for $100](https://github.com/karpathy/nanochat/discussions/1).

### Building an LLM from scratch on my own.

I don't think I ever mentioned this on the blog, but one important plan for me is to try to build an LLM from scratch, only using my own blog posts and what I remember -- no looking at the book. If I can do that, then I can be reasonably sure that I really have learned it all.

I'm also thinking that I'll do that using a different library -- that is, not PyTorch. That would stop me from regurgitating code that I've learned. If you're reading this within a day or so of the post's publication, I'm [running a poll on X/Twitter about which framework to use](https://x.com/gpjt/status/1985434030880293004). If you have an opinion, please do stop by and vote :-)

### Mixture-of-experts

It feels like almost every new model these days is an MoE. I have read a lot around the subject and would love to build on it. Essentially, instead of having just one feed-forward network after your attention heads, you have several. In front of them you have a router -- a trainable network of some kind -- that tells you which of these "expert" FFNs the token should be forwarded to. You then send it to the top (or top k) experts, while leaving the others inactive. The result is that you have more space (in terms of parameters) for the LLM to know about things, but not all of those parameters are active during inference -- so your model is smarter but still fast.

There's a bunch of interesting stuff there, from how you build it in the first place, to how you handle the fact that you're processing lots of tokens at once -- multiple tokens in each sequence and multiple sequences in a batch.

It would be a pretty cool follow-on to the "my own LLM" series, thinking about it.

### So, what next?

I definitely don't think I need to do all of those things in order to wrap up this series. Here's the subset I'm planning on doing:

  * Training the full GPT-2 base model myself. I'm 100% going to try this.
  * From the appendices -- anything that surprises me from the one on PyTorch, and perhaps from the "bells and whistles" in the training loop. The others I either won't do, or will pick up later.
  * Building my own LLM from scratch in a different framework, without using the book. That is, I think, essential, and perhaps would be the crowning post of this series. It would be a nice way to end it, wouldn't it?



For the other things, I think there are some potential future series to write.

  * Improving context length -- RoPE and other tricks -- sounds like an excellent series to start on when I'm done with this. AIs tell me that other interesting things to look into would be ALiBi, NTK/YaRN scaling, and positional interpolation.
  * Improving performance: the KV cache, FlashAttention, and other performance enhancements likewise feel like they could make a good series.
  * I also want to do a separate series on LoRA. In that, I'll draw on appendix E from this book, but also on other tutorials.
  * Likewise DPO, along with other post-training that can be done to make models more useful as chatbots, like Reinforcement Learning. I'd really like to spend some time understanding that area. (And Raschka's upcoming reasoning model book might fit into that category too.)
  * Optimisers: Adam, AdamW, maybe Muon (though the latter scares me a bit).
  * The maths -- softmax and higher-order tensor calculations -- also seems to belong in another series, perhaps an extension of the various "maths for AI" posts I've done in the past.
  * Automatic differentiation and the backward pass; that would make a great series.
  * A mixture-of-experts model would be excellent fun, I think.
  * Tokenisers would be a great stand-alone post, at least at the level that I can see myself covering it. Perhaps that would develop into a series if I found myself getting sucked in.



I'm certainly not promising that I'll write up all (or even any) of that second list, but they all seem really tempting to me right now. If you're particularly interested in seeing my take on any of them, please do leave a comment below.

### Coming up...

I think the next post in this series -- maybe the next several posts -- will be on trying to train the model code provided in the book from scratch to produce my own base model. Stay tuned!

[Here's a link to the next post in this series](/2025/12/llm-from-scratch-28-training-a-base-model-from-scratch).

[« Writing an LLM from scratch, part 26 -- evaluating the fine-tuned model](/2025/11/llm-from-scratch-26-evaluating-the-fine-tuned-model) [Why smart instruction-following makes prompt injection easier »](/2025/11/smart-instruction-following-and-prompt-injection)

Copyright (c) 2006-2026 by Giles Thomas. This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). 
