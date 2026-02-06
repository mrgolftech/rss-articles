# Writing an LLM from scratch, part 29 -- using DistributedDataParallel to train a base model from scratch in the cloud

**来源:** https://gilesthomas.com
**链接:** https://www.gilesthomas.com/2026/01/llm-from-scratch-29-ddp-training-a-base-model-in-the-cloud
**日期:** Wed, 07 Jan 2026 20:40:00 +0000

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



## Writing an LLM from scratch, part 29 -- using DistributedDataParallel to train a base model from scratch in the cloud

Posted on 7 [January 2026](/2026/01/) in [AI](/ai), [LLM from scratch](/llm-from-scratch), [TIL deep dives](/til-deep-dives), [Python](/python)

I'm carrying on with my ["extra credit" projects](/2025/11/llm-from-scratch-27-whats-left-and-whats-next) after finishing the main body of [Sebastian Raschka](https://sebastianraschka.com/)'s book "[Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)". Having proven that I could [train a GPT-2 small scale base model from scratch on my RTX 3090](/2025/12/llm-from-scratch-28-training-a-base-model-from-scratch) in 48 hours, I wanted to try training it on a multi-GPU machine on Lambda Labs. There are two benefits I see in doing that:

  1. I can learn what you need to change in a simple single-GPU training loop to make it multi-GPU.
  2. If I can get the training time for a full base model down from 48 hours to something more manageable (and hopefully not too expensive) -- then I can try a few experiments to see how I can improve the quality of the trained model. I have [a bunch of ideas](/2025/12/llm-from-scratch-28-training-a-base-model-from-scratch#but-why-is-our-model-worse-than-openais) about why my own base model wasn't as good as the original OpenAI one, and it would be good to know which (if any) of them are right.



In addition, I wanted to see if anything unexpected dropped out of it; after all, there were four different sizes of machines that I wanted to try, so I'd be doing four from-scratch trains on the same dataset. Does the machine size affect the quality of the model in some way?

Here's what happened. As with the last post, this is a set of tidied-up lab notes, so you can see the full journey. There's a lot to it! I was considering splitting it into multiple posts -- "writing the code", "building the datasets", "running the trains" -- but they're interleaved. Each train taught me something about how to structure the code to make it easier to use, so the code kept changing.

So I think it's worth documenting the process as it really was. If at some point I want to write a how-to document on porting single-GPU code to multi-GPU, I'll be able to mine this for resources, and in the meantime, hopefully this will be of use to readers -- even if it's just at the level of "I got this error message, how do I fix it?"

Anyway, once again I don't want to bury the lede, so: after spending US$215.16 on various trains on various servers, I was able to find that a reasonably cheap instance on Lambda Labs, with 8x A100 GPUs, each of which has 40 GiB of VRAM, is the sweet spot for this particular 163M-parameter, ~Chinchilla-optimal single-epoch run. They can train the model in less than four hours, they happen to be the right size for batches that minimise loss (more on that later), and can do that train for about US$35, excluding validation.

If you'd like to read the gory details of what I did, then read on -- but if you prefer, you can jump straight to the results.

### Which multi-GPU technique?

Back when I was [messing around with fine-tuning LLMs](/fine-tuning) using the Hugging Face ecosystem \-- [their "Transformers" library](https://huggingface.co/docs/transformers/en/index) and so on -- one of the experiments I did was to [fine-tune a 0.5B Qwen model on an 8x GPU machine](/2024/05/fine-tuning-3). As part of that, I came across [this excellent HF page summarising different kinds of multi-GPU training techniques](https://huggingface.co/docs/transformers/en/perf_train_gpu_many). The three that are relevant are:

  1. DataParallel (DP). With this: 
     * The default GPU (normally `gpu0`) is in charge of the process. It gets a batch of data, divides it up into per-GPU "micro-batches", and sends each of those to a thread for each of the other GPUs.
     * It then sends an up-to-date version of the model to each GPU.
     * Next, all of the per-GPU threads do a forward pass on their replica using their specific micro-batch, and send their outputs to the thread for the default GPU.
     * The default GPU thread aggregates all of those outputs (similarly to how the losses across all of our batches and the prefix sequences [are aggregated in the normal single-GPU case](/2025/10/llm-from-scratch-20-starting-training-cross-entropy-loss)) to work out an overall loss.
     * It then does a backward pass. This will start on the default GPU, as the aggregation step is the first thing that it will come to when going backwards through the steps that came up with that overall loss. However, it will then come to operations that happened on the other GPUs and those are (somehow) parallelised.
     * Once that is done, each GPU has gradients that represent how their copies of the model contributed to the overall loss.
     * Finally, they send those gradients back to the default GPU, which combines them (I think of this as just being an average, though I gather it's more complex) and applies them, producing an updated model.
     * Then the process repeats; the updated model on the default GPU will be sent to the other GPUs in the second step of the next iteration.
  2. DistributedDataParallel (DDP). This does less work on the default GPU and does less copying around. Each GPU has its own process (rather than thread), and is essentially responsible for its own training loop. Right at the very start, the default GPU's process sends the model to all of the others. Then all processes go into their training loop: 
     * Firstly, each one works out its own micro-batch (which means you need to have code to make sure that the datasets are properly split across the GPUs)
     * Each model does its own forward pass, then its own backward pass, working out its own independent gradients.
     * As it comes up with those gradients, it broadcasts them to a "reducer", which handles the aggregation. This is done in a distributed way -- there's not just one reducer handling everything.
     * When all models have completed the backward pass, the reducer has a set of combined gradients, which is visible from the per-GPU processes.
     * Each GPU process does its own optimizer step using those combined gradients.
     * That means that there's no model copy required -- each GPU has applied the same gradient update, so they already have in-sync models, assuming everything went well.
  3. ZeRO. This is a much more complex system, and I went into how it works [in this blog post](/2024/05/fine-tuning-4).



Now, from what I understand, due to all of the copying around of models, plus the issues inherent with the GIL in Python, DDP is actually better than DP despite being more complicated -- and more flexible! Per Hugging Face:

> DDP is recommended because it reduces communication overhead between GPUs, efficiently utilizes each GPU, and scales to more than one machine.

It might be a while before I want to try multi-machine training, but it would be awesome to have code that's ready to do that without needing any extra work.

Now, how to implement it?

### Implementing DDP for our model.

Hugging Face have a library called [Accelerate](https://huggingface.co/docs/accelerate/index), which does everything for you:

> Accelerate is a library that enables the same PyTorch code to be run across any distributed configuration by adding just four lines of code!

That does sound very useful, but I worry that by using it I won't learn as much. It also rather ties you in to the HF ecosystem. That's not necessarily a bad thing -- I enjoyed using their stuff in my fine-tuning project -- but I'm trying for a somewhat lower-level view in this series.

So, let's use the PyTorch-native stuff. There's a ["getting started" tutorial](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html), so we can follow that.

It has two options for running using DDP, one with a bit of extra setup code -- the first example, under "Basic Use Case" -- and one that uses `torchrun` to make things easier. The second sounds best.

The code changes actually look really simple; given a normal single-GPU training script, you need to do some setup at the start:
    
    
    import torch.distributed as dist
    from torch.nn.parallel import DistributedDataParallel as DDP
    
    # ...
    
        torch.accelerator.set_device_index(int(os.environ["LOCAL_RANK"]))
        acc = torch.accelerator.current_accelerator()
        backend = torch.distributed.get_default_backend_for_device(acc)
        dist.init_process_group(backend)
        rank = dist.get_rank()
        print(f"Start running basic DDP example on rank {rank}.")
        # create model and move it to GPU with id rank
        device_id = rank % torch.accelerator.device_count()
    

...then wrap the model itself in a `DDP` object, which is what you actually do the train on:
    
    
        model = ToyModel().to(device_id)
        ddp_model = DDP(model, device_ids=[device_id])
    

...and a bit of teardown at the end:
    
    
        dist.destroy_process_group()
    

The way to look at this is that `torchrun` will spin off one process per GPU, each running exactly the same code. They have a "rank", which is an integer saying which of the per-GPU processes they are -- 0 for GPU 0, 1 for GPU 1, and so on. There's a bit of a gotcha here, though -- you can see that we're looking at an environment variable called `LOCAL_RANK` at the start, but we then get a (non-"local") `rank` variable from `torch.distributed` a bit later on. This is due to the multi-machine possibilities with DDP -- if you have multiple machines, then the local rank will be "which GPU on the machine does this process relate to", but there will also be a "global" rank, which is unique across all machines. This distinction won't matter that much during this one-machine test, but it's worth keeping in mind if we want to keep the code in a shape where it could potentially scale to multiple machines.

Anyway, after the processes are spun up, they will do their training, and the synchronisation and passing around of gradients during the backward pass will all happen invisibly in the background, so when we do our `optimizer.step()`, it will have the full set of gradients.

Now that means that we'll presumably also need to use the rank -- that is, which of the _n_ per-GPU processes the current code is running in -- when selecting which dataset items to train on. More about that later.

Let's start writing some code! I'll use a [new repo](https://github.com/gpjt/ddp-base-model-from-scratch), into which I can put just the code needed for this train. I'll also structure it a little better than last time, with separate "runs", each of which has a model config and training parameters, and will later on have its own checkpoints. You can think of these as being one per machine size that I'm trying out -- I'll create a run directory for each one.

[Here's a first cut](https://github.com/gpjt/ddp-base-model-from-scratch/blob/0c3462c71874d83511eaabdf18fe8a91a7c31c2b/ddp_train.py), simply loading up a model config from a run's directory, using it to create the model, and then doing the wrapping above -- no training at all. Running it with `torchrun` (and `uv`, as I'm using that for all new projects):
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run torchrun ddp_train.py original
    On rank 0.
    

Promising. Now, unfortunately we only have one GPU locally, and the code assumes that it's one process per GPU (I believe that's a hard limitation for PyTorch's DDP), so running with `--nproc_per_node=2` blows up. So we can't do an in-depth test locally.

But at least we know that the basic infra is there and working.

Now let's move the other training code from the single-GPU script into that file, pretty much blindly. [This is the result](https://github.com/gpjt/ddp-base-model-from-scratch/blob/2e781226034bbd2a7f0a9204f8f9c0bd55bac261/ddp_train.py) \-- it's doing almost nothing beyond what the last train did, apart from wrapping the model in a `DDP` object -- the only other changes are to use this "runs" directory that we've introduced.

As a quick hack, we should try running it. It does a validation and checkpoint before it starts, and we can make that happen quickly by hacking the validation loop to only do a couple of iterations:
    
    
    for val_inputs, val_targets in tqdm(val_ds[:2]):
    

(Foreshadowing: that hack will come back to haunt us later!)

Running that, then hitting control-C after the validation completes, and it looks OK:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run torchrun ddp_train.py original
    On rank 0.
    Starting training at dataset offset 0
      0%|                                                                                                                                          | 0/530630 [00:00<?, ?it/s]Validation/checkpoint
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 2/2 [00:00<00:00, 10.95it/s]
    Continuing trainingâââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 2/2 [00:00<00:00, 10.96it/s]
      0%|                                                                                                                              | 18/530630 [00:06<45:20:54,  3.25it/s]^CW1203 18:34:11.363000 471545 torch/distributed/elastic/agent/server/api.py:725] Received 2 death signal, shutting down workers
    W1203 18:34:11.364000 471545 torch/distributed/elastic/multiprocessing/api.py:908] Sending process 471607 closing signal SIGINT
      0%|                                                                                                                              | 18/530630 [00:07<57:44:53,  2.55it/s]
    
    Aborted!
    

...and we have what look like solid checkpoints:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ ls -lrt runs/original/checkpoints/
    total 4
    lrwxrwxrwx 1 giles giles   27 Dec  3 18:34 latest -> 20251203Z183404-iteration-0
    lrwxrwxrwx 1 giles giles   27 Dec  3 18:34 best -> 20251203Z183404-iteration-0
    drwxr-xr-x 2 giles giles 4096 Dec  3 18:34 20251203Z183404-iteration-0
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ ls -lrth runs/original/checkpoints/20251203Z183404-iteration-0/
    total 1.9G
    -rw-r--r-- 1 giles giles 670M Dec  3 18:34 model.safetensors
    -rw-r--r-- 1 giles giles 1.4K Dec  3 18:34 scaler.pt
    -rw-r--r-- 1 giles giles 1.3G Dec  3 18:34 optimizer.pt
    -rw-r--r-- 1 giles giles  105 Dec  3 18:34 meta.json
    

However, loading one of those checkpoints fails:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run torchrun ddp_train.py original best
    On rank 0.
    [rank0]: Traceback (most recent call last):
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/ddp_train.py", line 229, in <module>
    [rank0]:     main()
    [rank0]:     ~~~~^^
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/.venv/lib/python3.13/site-packages/click/core.py", line 1485, in __call__
    [rank0]:     return self.main(*args, **kwargs)
    [rank0]:            ~~~~~~~~~^^^^^^^^^^^^^^^^^
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/.venv/lib/python3.13/site-packages/click/core.py", line 1406, in main
    [rank0]:     rv = self.invoke(ctx)
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/.venv/lib/python3.13/site-packages/click/core.py", line 1269, in invoke
    [rank0]:     return ctx.invoke(self.callback, **ctx.params)
    [rank0]:            ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/.venv/lib/python3.13/site-packages/click/core.py", line 824, in invoke
    [rank0]:     return callback(*args, **kwargs)
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/ddp_train.py", line 211, in main
    [rank0]:     train_ds_offset, best_loss = load_checkpoint(
    [rank0]:                                  ~~~~~~~~~~~~~~~^
    [rank0]:         run_dir, checkpoint, model, optimizer, scaler
    [rank0]:         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    [rank0]:     )
    [rank0]:     ^
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/checkpointing.py", line 16, in load_checkpoint
    [rank0]:     model.load_state_dict(load_file(checkpoint_dir / "model.safetensors"))
    [rank0]:     ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    [rank0]:   File "/home/giles/Dev/ddp-base-model-from-scratch/.venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 2629, in load_state_dict
    [rank0]:     raise RuntimeError(
    [rank0]:     ...<3 lines>...
    [rank0]:     )
    [rank0]: RuntimeError: Error(s) in loading state_dict for GPTModel:
    [rank0]:    Missing key(s) in state_dict: "tok_emb.weight", "pos_emb.weight", "trf_blocks.0.att.mask", "trf_blocks.0.att.W_query.weight",
    ...
    [rank0]:    Unexpected key(s) in state_dict: "module.final_norm.scale", "module.final_norm.shift", "module.out_head.weight", "module.pos_emb.weight", "module.tok_emb.weight"
    ...
    

It turns out that the problem is this code when we save it:
    
    
                save_checkpoint(
                    run_dir,
                    f"iteration-{ix}",
                    model, optimizer, scaler,
                    avg_train_loss, val_loss,
                    ix,
                    is_best
                )
    

The `model` that we're saving is the `DDP` wrapper around our model; my guess is that it does actually include all of the weights for the model, hence the correct-looking size for the checkpoint file, but they're renamed -- the `DDP` wrapper sees the underlying model as something called `module`, so (for example) `tok_emb.weight` would be called `module.tok_emb.weight`.

Fixing that, with this diff:
    
    
    diff --git a/ddp_train.py b/ddp_train.py
    index 7418851..963fbf7 100644
    --- a/ddp_train.py
    +++ b/ddp_train.py
    @@ -137,12 +137,13 @@ def train(
             if (ix % VAL_AND_CHECKPOINT_INTERVAL == 0) or (ix == len(train_ds) - 1):
                 print("Validation/checkpoint")
                 model.eval()
    +            base_model = model.module
                 with torch.inference_mode(), torch.amp.autocast(device_type=device.type, dtype=torch.float16):
                     val_losses = []
                     for val_inputs, val_targets in tqdm(val_ds):
                         val_inputs = val_inputs.to(device).to(torch.long)
                         val_targets = val_targets.to(device).to(torch.long)
    -                    val_logits = model(val_inputs)
    +                    val_logits = base_model(val_inputs)
                         val_losses.append(
                             calculate_loss(val_logits, val_targets).item()
                         )
    @@ -160,7 +161,7 @@ def train(
                 save_checkpoint(
                     run_dir,
                     f"iteration-{ix}",
    -                model, optimizer, scaler,
    +                base_model, optimizer, scaler,
                     avg_train_loss, val_loss,
                     ix,
                     is_best
    

...sorts it out -- we can load our checkpoints again. Here's [the updated file](https://github.com/gpjt/ddp-base-model-from-scratch/blob/7d1f189a0174e1a88d6f21ce2d4b0b88ab2965f7/ddp_train.py).

I think we're going to have to revisit checkpointing and validation again; we don't want to do it in all of our processes, probably only on global rank 0, and we'll need to somehow synchronise everything so that the other processes don't carry on training while we're doing it.

But before we get on to that, there are a couple of other things to change. At the top of the file we're defining some constants that look wrong:
    
    
    BATCH_SIZE = 6
    SEQ_LENGTH = 1024
    VAL_AND_CHECKPOINT_INTERVAL = 2000
    

### Sequence length

We'll handle the dumbest of these first; it was actually silly that in the old code we had a constant for sequence length. We're using the context length of the model for that, so it's duplicated information. Let's get it from the `model_conf`:
    
    
    diff --git a/ddp_train.py b/ddp_train.py
    index 963fbf7..77a62ae 100644
    --- a/ddp_train.py
    +++ b/ddp_train.py
    @@ -20,15 +20,14 @@ from gpt import GPTModel
    
    
     BATCH_SIZE = 6
    -SEQ_LENGTH = 1024
     VAL_AND_CHECKPOINT_INTERVAL = 2000
    
    
     class BigTrainDataset(Dataset):
    
    -    def __init__(self, all_tokens):
    -        self.xs = all_tokens[:-1].reshape(-1, BATCH_SIZE, SEQ_LENGTH)
    -        self.ys = all_tokens[1:].reshape(-1, BATCH_SIZE, SEQ_LENGTH)
    +    def __init__(self, all_tokens, seq_length):
    +        self.xs = all_tokens[:-1].reshape(-1, BATCH_SIZE, seq_length)
    +        self.ys = all_tokens[1:].reshape(-1, BATCH_SIZE, seq_length)
    
         def __getitem__(self, ix):
             return (self.xs[ix], self.ys[ix])
    @@ -37,9 +36,10 @@ class BigTrainDataset(Dataset):
             return self.xs.shape[0]
    
    
    -def load_dataset(run_dir, split):
    +def load_dataset(run_dir, split, seq_length):
         return BigTrainDataset(
    -        load_file(run_dir / "datasets" / f"{split}.safetensors")["tokens"]
    +        load_file(run_dir / "datasets" / f"{split}.safetensors")["tokens"],
    +        seq_length,
         )
    
    
    @@ -205,8 +205,8 @@ def main(run, checkpoint):
    
         scaler = torch.amp.GradScaler()
    
    -    train_ds = load_dataset(run_dir, "train")
    -    val_ds = load_dataset(run_dir, "validation")
    +    train_ds = load_dataset(run_dir, "train", model_conf["context_length"])
    +    val_ds = load_dataset(run_dir, "validation", model_conf["context_length"])
    
         if checkpoint:
             train_ds_offset, best_loss = load_checkpoint(
    

...and [here's the updated file](https://github.com/gpjt/ddp-base-model-from-scratch/blob/017dd79a4a3c05c7a2dc31189c9ff71cf164fa64/ddp_train.py). That was nice and simple.

### Batch size

The code that we have specifies the batch size for each GPU -- that is, with `6`, we'll have six sequences in each batch on each one. Like I mentioned earlier, that's called a "micro-batch" in distributed training like this 1 \-- a per-GPU batch, as opposed to the overall global size across all GPUs -- so we could just rename it, and then we'd have 6×ngpus as a global batch size.

However, it feels to me like this is a useful metaparameter to be able to tweak from outside the code. I can see machines with per-GPU VRAM varying from 40 GiB to 160 GiB on Lambda Labs, and pretty clearly that will mean there will be a varying largest micro-batch size on each type. So this is something we'll want to configure on a per-run basis, so let's add a new `train.json` file to our run config, load that up, and pass it through.

That's a simple enough fix; no need to note the diff, but [here's the code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/3e1879a8eadade783c1a6dd9f621b8cf2ae76be7/ddp_train.py).

### Validation/checkpoint interval

This one we'll need to think about. The size of our validation set is based on what one process running on my local RTX 3090 can validate in five minutes, and the interval (for which I fairly arbitrarily put 2000 in the code when copying it across) was calibrated for roughly every half-hour. Those numbers in turn were aimed at the 44 hours of training time I expected locally.

For this train, we'll (hopefully!) be taking significantly less time. We'll have eight GPUs, so naively that's 5.5 hours of train time, and each will have more VRAM, so we should be able to bump up the batch size and potentially get even faster than that. Depending on which kind of cards we're using, they may be faster, too -- I found that an A100 is slower (with the same batch size) than the RTX 3090 in my fine-tuning experiments, but the H100 and B200 are likely faster.

I think this is another thing for the train config; we should have the validation interval (in terms of iterations) and the number of batches to do for validation.

[Here's the updated code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/fec0f54e4f0061f5ce93c85c4649b11f6ed7b77d/ddp_train.py).

### Datasets

Now, let's move on to the dataset. With the code as it is right now, all of our per-GPU processes are using this code to iterate over the same dataset:
    
    
    for ix in tqdm(range(train_ds_offset, len(train_ds))):
    

That means that they'll all be training on the same data; the synchronisation that is happening "magically" in the background means that they'll all train on the first item, work out gradients, and step their optimiser -- so they'll essentially (modulo randomness) have the same updates. Pretty pointless! What we want is for each of the n per-GPU processes to train on 1/n of the data.

We have two useful helpers in [`torch.distributed`](https://docs.pytorch.org/docs/stable/distributed.html):

  * `get_rank`, which gets the global rank of this process. In our one-machine case, it returns 0 for the process on `gpu0`, 1 for the one on `gpu1`, and so on. We're already using it in that setup code we looked at earlier:
        
        rank = dist.get_rank()
        print(f"Start running basic DDP example on rank {rank}.")
        # create model and move it to GPU with id rank
        device_id = rank % torch.accelerator.device_count()
        

  * `get_world_size`, which tells us how many GPU processes there are (globally -- it would be across all machines if we had more than one)




So, the simplest thing to do is to use the world size as a step, and the rank as an offset:
    
    
    rank = dist.get_rank()
    world_size = dist.get_world_size()
    for ix in tqdm(range(train_ds_offset + rank, len(train_ds), world_size)):
    

[Here's the code with that](https://github.com/gpjt/ddp-base-model-from-scratch/blob/86ea49d0e576e4dec3b5ca9b4fcd8ce8ad176a3f/ddp_train.py).

### Validation and checkpointing only on rank 0

Now, remember that the same code is running for every one of our per-GPU processes. That means that all of them will do the training with forward and backward passes, and their own optimiser steps, all synchronised by PyTorch DDP magic. But they will also do their own validations -- which is kind of pointless -- and they'll also try to save their own checkpoints, which would be messy because they could quite easily interfere with each other; after all, all of the processes are running on the same machine and would be writing to the same filesystem.

So, as a first cut, let's just wrap an `if rank == 0` around the eval and checkpointing stuff -- we change this:
    
    
    if (ix % validation_interval == 0) or (ix == len(train_ds) - 1):
    

...to this:
    
    
    if rank == 0 and ((ix % validation_interval == 0) or (ix == len(train_ds) - 1)):
    

That line is getting bit long, so let's break it apart a bit:
    
    
    is_eval_iter = (
        (ix % validation_interval == 0)
        or (ix == len(train_ds) - 1)
    )
    if rank == 0 and is_eval_iter:
    

That looks OK, but there's an extra wrinkle: all of the processes are running the same code, so while the rank zero one will do the eval, the others will continue through the script, so they will go right back around our loop and start training on the next batches -- which is bad. We want our processes to be proceeding in lockstep, iteration-by-iteration.

Luckily, the solution is simple: the `barrier` function in `torch.distributed` basically says "stop here until all of our processes have reached this point".

So we can use two of those -- one before the eval loop, to make sure that all of the processes have finished their training part of the iteration before we do the eval on rank zero, and one after the eval, so that the non-rank-zero processes will wait.

One bit of complexity -- we want to do those barriers only if it's a eval iteration, but we want to do them for all processes. So we have to break up the `if` statement, and we wind up with this:
    
    
           is_eval_iter = (
                (ix % validation_interval == 0)
                or (ix == len(train_ds) - 1)
            )
            if is_eval_iter:
                dist.barrier()
    
                if rank == 0:
                    print("Validation/checkpoint")
                    model.eval()
    
                    base_model = model.module
                    with torch.inference_mode(), torch.amp.autocast(device_type=device.type, dtype=torch.float16):
                        val_losses = []
                        for val_inputs, val_targets in tqdm(val_ds[:validation_batches]):
                            val_inputs = val_inputs.to(device).to(torch.long)
                            val_targets = val_targets.to(device).to(torch.long)
                            val_logits = base_model(val_inputs)
                            val_losses.append(
                                calculate_loss(val_logits, val_targets).item()
                            )
                        val_loss = sum(val_losses) / len(val_losses)
    
                    if best_loss is None or val_loss < best_loss:
                        is_best = True
                        best_loss = val_loss
                    else:
                        is_best = False
    
                    avg_train_loss = sum(train_losses) / len(train_losses)
                    train_losses = []
    
                    save_checkpoint(
                        run_dir,
                        f"iteration-{ix}",
                        base_model, optimizer, scaler,
                        avg_train_loss, val_loss,
                        ix,
                        is_best
                    )
                    generate_training_chart(run_dir)
    
                    model.train()
                    print("Continuing training")
    
                dist.barrier()
    

That seems to work OK ([code here](https://github.com/gpjt/ddp-base-model-from-scratch/blob/a44b90088ca6373be6749cb512e4221ebb9c67b6/ddp_train.py)), but it does give a warning:
    
    
    UserWarning: barrier(): using the device under current context. You can specify ``device_id`` in ``init_process_group`` to mute this warning.
    

So, we want to pass the device ID in when we call `init_process_group`. Let's dig into that a bit.

### Revisiting the init code

Here's the copypasta that I took from the PyTorch tutorial earlier in this post:
    
    
        torch.accelerator.set_device_index(int(os.environ["LOCAL_RANK"]))
        acc = torch.accelerator.current_accelerator()
        backend = torch.distributed.get_default_backend_for_device(acc)
        dist.init_process_group(backend)
        rank = dist.get_rank()
        print(f"On rank {rank}.")
        device_id = rank % torch.accelerator.device_count()
    

Let's dig into what that is doing.

The `LOCAL_RANK` environment variable is being set by `torchrun` to 0, 1, 2, etc as appropriate to tell us which process we are on this machine. So the first line is telling PyTorch to [use the device with that index for this process](https://docs.pytorch.org/docs/stable/generated/torch.accelerator.device_index.html).

The next line is [getting the current accelerator](https://docs.pytorch.org/docs/stable/generated/torch.accelerator.current_accelerator.html) \-- that is, an object that represents which acceleration hardware we're using in this process.

I think that the best way to see the combination of these two lines is that the first says "use `gpu0`" (or 1, or 2, or...), and then the second says "get the object describing the GPU you're using right now". So it's a slightly indirect way of getting the object containing the details of the GPU in question.

Next, we call [`torch.distributed.get_default_backend_for_device`](https://docs.pytorch.org/docs/stable/distributed.html#torch.distributed.get_default_backend_for_device). A backend in this context is an abstraction of whatever system the device in question is programmed using -- in the case of an Nvidia GPU, it would be some kind of thing that encapsulates CUDA.

Once that's done, we call [`torch.distributed.init_process_group`](https://docs.pytorch.org/docs/2.9/distributed.html#torch.distributed.init_process_group), passing in the backend that we're using. We're saying "initialise the internal data structures for `torch.distributed` so that they're all set up properly to work with the backend we specified".

After that, we can do stuff like getting the global rank with `dist.get_rank` and so on, because `torch.distributed` has been properly initialized. Presumably at this point we're talking to any other machines in a multi-machine cluster, so we can find out what our world size is and that kind of thing.

That extra line at the end, to get the `device_id`:
    
    
        device_id = rank % torch.accelerator.device_count()
    

...actually looks erroneous to me. All of our code is assuming one process per GPU. So I think we can just use the `LOCAL_RANK` there as well.

Let's rewrite it like this (with some useful comments):
    
    
        # Which of the one-per-GPU processes are we?
        rank = int(os.environ["LOCAL_RANK"])
    
        # Set ourselves up to use the GPU with ID ``rank``
        torch.accelerator.set_device_index(rank)
    
        # Get the accelerator object associated with that GPU,
        # and the associated backend object (eg. ``nccl`` for CUDA):
        acc = torch.accelerator.current_accelerator()
        backend = torch.distributed.get_default_backend_for_device(acc)
    
        # Initialize torch.distributed; set the device ID explicitly
        # to avoid warnings in ``dist.barrier``
        dist.init_process_group(backend, device_id=rank)
    
        print(f"On rank {rank}.")
        model = GPTModel(model_conf).to(rank)
    

That seems to work well! [Here's the code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/0f17f4fc455031020400ac3ccc7d41e3dc8d44dc/ddp_train.py). However, I ran it past ChatGPT (largely to validate my understanding of what was going on), and it highlighted something slightly misleading about it.

Right now, we're training on a single node, with one process per GPU. But again, one of the neat-o things about this DDP stuff is that it should be able to scale to multiple nodes.

Now, remember that `LOCAL_RANK` is just the rank of the current process on the specific node that it's running on -- hence the name. If we had two machines, each with 8 GPUs, then there would be a process with rank zero on each of them.

The "real" rank -- that is, across all machines -- is the one that you can get from `dist.get_rank` once it has been initialised. One of the things it does during that initialisation is to talk to all of the other nodes and work that kind of thing out \-- which of the local rank zero processes across all of the machines is the global rank zero process.

So we need to use the local rank when working out which GPU we should be running on and so on, but we should not treat it as a global rank.

That's actually quite fine in this case, as we're calling `dist.get_rank` inside the training loop when we actually need to use the global one (when indexing into the dataset, or when deciding if we're the process that should be doing evals and checkpoints). The only place where we might be confusing matters is in that print, which is not important anyway, as the training loop also prints out its rank.

So, let's tweak it a little more for clarity:
    
    
        # Which of the one-per-GPU processes are we on this machine?
        local_rank = int(os.environ["LOCAL_RANK"])
    
        # Set ourselves up to use the GPU with the ID that matches our local rank
        torch.accelerator.set_device_index(local_rank)
    
        # Get the accelerator object associated with that GPU,
        # and the associated backend object (eg. ``nccl`` for CUDA):
        acc = torch.accelerator.current_accelerator()
        backend = torch.distributed.get_default_backend_for_device(acc)
    
        # Initialize torch.distributed; set the device ID explicitly
        # to avoid warnings in ``dist.barrier``
        dist.init_process_group(backend, device_id=local_rank)
    
        model = GPTModel(model_conf).to(local_rank)
    

That seems to work well! [Here's the code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/5ae5ea2aa38cd5f62b609e2bf33c8a45d5b642d4/ddp_train.py).

Time to run it past ChatGPT to see if I've made any dumb errors. Turns out that (unsurprisingly) I have...

### Checkpointing, revisited

Let's go back to our code that decides whether or not it's an iteration where we need to do a validation run and a checkpoint:
    
    
            is_eval_iter = (
                (ix % validation_interval == 0)
                or (ix == len(train_ds) - 1)
            )
    

The problem is that our index `ix` is different in the different processes! Remember, we have this in order to pick out the correct training items:
    
    
        for ix in tqdm(range(train_ds_offset + rank, len(train_ds), world_size)):
    

So let's think about it; in the first run through the loop, with 8 GPUs, we would have

  * `ix` = 0 for the process with rank 0
  * `ix` = 1 for the process with rank 1
  * ...
  * `ix` = 7 for the process with rank 7



In the next run through the loop, we'd have:

  * `ix` = 8 for the process with rank 0
  * `ix` = 9 for the process with rank 1
  * ...
  * `ix` = 15 for the process with rank 7



So `is_eval_iter` will give different results for each process. That might not sound like the end of the world -- `ix % validation_interval` will only be zero for one of them, so long as `validation_interval` is larger than the number of GPUs -- but remember that our validation code looks like this:
    
    
            if is_eval_iter:
                dist.barrier()
    
                if rank == 0:
                    # do the validation and checkpointing
    
                dist.barrier()
    

Now, if different processes have different values for `is_eval_iter`, then `dist.barrier()` will only be called in the one(s) for which it is `True`. But `dist.barrier()` means "wait until all processes have reached this barrier". So the ones that call it will lock up completely until other processes get there, and everything will at best get out-of-sync, and at worst will lock up completely.

I think that the problem here is that I'm conflating two things: the index of the global step -- that is, one iteration across all GPUs -- and the dataset element that we want to use. In the original one-GPU case that made, sense; iteration 0 was on dataset element 0, iteration 1 was on element 1, and so on. But now the offset into the dataset, and the global step, are quite different things.

This is quite deeply embedded in the code, but we can fix it!

Let's start off by changing our checkpoint code, just to rename things. It keeps track of a variable called `train_ds_offset`, our offset into the training dataset, and uses that both to index into the dataset, and to work out how far through the train we are. The latter is a much better thing to store in a checkpoint, so instead of saving `train_ds_offset`, we'll store (and restore) `global_step`. Basically, just a rename so that the variables and stored JSON match the new reality. [Here's the updated code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/c8702169afb44082a4571b0179e1ad4a2c43fb3d/checkpointing.py).

Now we need to make a number of minor changes to the training loop just to match that rename of the value that we're checkpointing (eg. for the code to generate the training chart) but the most important change is to our loop. Instead of iterating over our dataset with a step and and offset so that we can index into it, we firstly work out how many global steps there will be:
    
    
    total_global_steps = len(train_ds) // world_size
    

...then we iterate from our initial global step -- zero if we're starting a fresh train, or whatever global step we were on in a loaded checkpoint plus one if we're doing a continued train from a checkpoint -- up to the `total_global_steps`:
    
    
    for global_step in tqdm(range(start_global_step, total_global_steps)):
    

That means that we need to use the global step, the world size, and our current rank to work out which dataset item we should be training on for this process at this global step. Let's say that we have eight processes; on the 0th global step, we should have rank 0 training on dataset item 0, rank 1 on item 1, and so on. On the next global step, rank 0 should train on item 8, rank 1 on 9, and so on. So:
    
    
    inputs, targets = train_ds[global_step * world_size + rank]
    

That's actually much more elegant than the earlier code, and seems to work fine. [Here it is](https://github.com/gpjt/ddp-base-model-from-scratch/blob/c8702169afb44082a4571b0179e1ad4a2c43fb3d/ddp_train.py).

Phew, glad to have caught that before I started spending money on machines -- it would have been confusing if everything locked up. Thanks, ChatGPT!

### Slicing the validation dataset

Another thing that raised by ChatGPT is about the validation. We don't want to validate across all of the validation dataset -- we're using a number from the `train.json`. I have this code:
    
    
        for val_inputs, val_targets in tqdm(val_ds[:validation_batches]):
    

This looked like a nice, quick way to get the first `validation_batches` elements of the validation dataset. But ChatGPT told me it would raise. It didn't, though -- why?

The problem is that I had `validation_batches` set to `2` in my training config for testing. Stepping through what that slice does, when we run `val_ds[:validation_batches]`:

  * Python calls the `__getitem__` on the dataset, passing in a `slice` object as `ix`, so this code is called with it:
        
        def __getitem__(self, ix):
            return (self.xs[ix], self.ys[ix])
        

  * Now, because that code doesn't do anything clever with `slice`s, they're passed straight down to the tensors that make up `self.xs` and `self.ys`. So it's actually equivalent to this:
        
        return self.xs[:validation_batches], self.ys[:validation_batches]
        

  * Or, to rewrite the whole loop (omitting the `tqdm` for clarity):
        
        for val_inputs, val_targets in (self.xs[:validation_batches], self.ys[:validation_batches]):
            ...
        

  * So, the first time through the loop, we try to bind our loop variables like this:
        
        val_inputs, val_targets = self.xs[:validation_batches]
        

That is clearly wrong! It's equivalent to this:
        
        val_inputs = self.xs[:validation_batches][0]
        val_targets = self.xs[:validation_batches][1]
        

...with code to blow up if `self.xs[:validation_batches]` has more than two elements -- the normal Python "ValueError: too many values to unpack"

  * But if `validation_batches` is set to 2, which it happened to be in my case, then it will silently fail -- our first eval loop will get the first X from the validation set as `val_inputs`, and the second X as `val_targets`.



Nasty! AI code review certainly helped me dodge a bullet on that one.

Let's fix it, it's not a big change: we can just do this:
    
    
        for val_ix in tqdm(range(validation_batches)):
            val_inputs, val_targets = val_ds[val_ix]
    

...and that works! So [here's the code now](https://github.com/gpjt/ddp-base-model-from-scratch/blob/87d15bfc4ff9187077b09293922df525fa42f425/ddp_train.py).

### Back to the datasets

So, I think we have one final issue, which is the training and validation datasets. In our single-GPU train, we worked out ahead of time how much of FineWeb (or FineWeb-Edu) to train on -- the Chinchilla-optimal number -- and generated a dataset that contained a round number of 6-sequence, 1024-token batches that was the smallest such round number that was larger than our target. We also worked out exactly how large (in terms of batches) our validation dataset needed to be so that each validation run would take five minutes.

There was one big issue with that system; when I decided to do an "extended" train on more of the FineWeb-Edu dataset, in order to see whether I could get the loss down further, I had to do some nasty hackery in order to generate a new one. So it would be nice to not have that problem this time around.

Additionally, we're likely to be tweaking the batch size quite a lot in this experiment while we find what the appropriate level is to fit onto the cloud GPUs, and also varying how much validation we do -- and additionally, we have the world size to worry about.

I think that the best way to give us the flexibility we need will be to pre-convert the complete FineWeb and FineWeb-Edu datasets into the format we need -- each sequence in the dataset converted to GPT-2 tokens, and then those sequences concatenated together, with the `<|endoftext|>` token 50257 separating them.

It would be good to properly nail down the validation dataset at the same time. So we can have a script that loads up the original dataset as downloaded from Hugging Face, splits it into 99% train, 1% validation, does the conversion, and then saves them as safetensors files.

If we use `uint16` for those (which is just large enough for our 50,257-token vocab), we can fit the ~10B tokens in each dataset's train split into 20 GiB of disk. Not too bad.

But there will still be the issue of getting them onto our cloud machines. Let's generate the data, and then work out how to handle that.

I tried initially with [the code I used last time, adapted to run through the entire dataset](https://github.com/gpjt/ddp-base-model-from-scratch/blob/aede6fbca2bf5ca518995ef39e58103e4c2dae15/prepare_datasets.py). It does the 99%/1% train/validation split, and then for each of those generates a single massive tensor of tokens like this:

  * Zoom through the records in the dataset in batches of 1,000.
  * For each batch: 
    * Tokenising each batch, so we get a list of lists of tokens.
    * Convert that list of lists into a single list `<|endoftext|>` tokens separating each item.
    * Convert that list into a PyTorch `uint16` tensor.
    * Add the tensor to a `results` list.
  * After that's all done, use `torch.cat` to convert the `results` list into a single tensor, and then save that with `safetensors`.



It _almost_ worked! To my surprise, it got all the way to the end, and only blew up with an out-of-memory error when it was trying to save the result -- and it did that completely silently, so I thought it had worked right up until I tried to check the file on disk to see how large it was, and it wasn't there.

The obvious tweak: set the `results` list to `None` just after the `torch.cat`, to free up the memory it's using. Given that it was the save that triggered the OOM, you'd think that that would be enough -- but it turned out not to be so.

Rather than mess around with this for much longer, I just decided to add on 128 GiB of swap to my machine temporarily:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ sudo dd if=/dev/zero of=./swap bs=1G count=128
    [sudo] password for giles:
    128+0 records in
    128+0 records out
    137438953472 bytes (137 GB, 128 GiB) copied, 63.1124 s, 2.2 GB/s
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ sudo chmod 0600 ./swap
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ sudo mkswap ./swap
    Setting up swapspace version 1, size = 128 GiB (137438949376 bytes)
    no label, UUID=693d72a1-871d-4ab8-b0c8-b383b435ca8f
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ sudo swapon ./swap
    

...and that was enough to make it run. So I've now generated pre-tokenised, pre-concatenated train and validation sets for both FineWeb and FineWeb-Edu:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ ls -lrth fineweb-prepared/
    total 20G
    -rw-r--r-- 1 giles giles 196M Dec  4 21:02 validation.safetensors
    -rw-r--r-- 1 giles giles  20G Dec  4 21:20 train.safetensors
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ ls -lrth fineweb-edu-prepared/
    total 19G
    -rw-r--r-- 1 giles giles 192M Dec  4 22:43 validation.safetensors
    -rw-r--r-- 1 giles giles  19G Dec  4 22:59 train.safetensors
    

Now, thinking about how to get it up to the Lambda Labs machines. I have normal 1 Gb residential broadband, so conceivably I could upload 20 GiB in about 200 seconds. But that's assuming that there's no network congestion, so I would expect it to take longer. The LL machines are quite expensive, and I don't want to waste money keeping them up while I'm just uploading data.

There are possibilities here:

  1. I can upload the datasets to Hugging Face; their network connection will be better than mine, so I can just pay the price in time of uploading everything from home once, and then I can download them faster from HF to LL. That also has the benefit of meaning that after this experiment I can safely delete the local files, but then download them again if I need them. And if anyone else wants to repro this experiment, the data will be easily available to them.
  2. Lambda Labs have persistent filesystems that you can use. They cost $0.20/GB/month, so that would be about $5/month for all of my datasets. So I could upload the data to a cheap instance with a persistent filesystem mounted, shut down that instance but keep the filesystem, and then mount it on each machine I use to run tests. .



I think the best option is to use option (1), but with the option of also doing (2). The HF dataset will still take time to download to LL, even over the faster network connection. That might not be a problem -- but if it is, I download it once on a cheap instance and use a persistent disk too. Essentially I'd be using the persistent disk as a "cache", and still get the benefits of the easily-shareable datasets on Hugging Face.

So, that decided, let's find out how we can upload a whacking great 20 GiB safetensors file as a dataset on Hugging Face.

### Putting the datasets on Hugging Face.

It turns out that resources like datasets on HF are just Git repositories using the LFS (Large File System) plugin to be able to handle, well, large files. Conveniently, given that I'm using `uv` to manage my project, there's a [plugin](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#using-uv) that allows me to use their CLI tools with minimal effort, so:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uvx hf auth login
    
        _|    _|  _|    _|    _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|_|_|_|    _|_|      _|_|_|  _|_|_|_|
        _|    _|  _|    _|  _|        _|          _|    _|_|    _|  _|            _|        _|    _|  _|        _|
        _|_|_|_|  _|    _|  _|  _|_|  _|  _|_|    _|    _|  _|  _|  _|  _|_|      _|_|_|    _|_|_|_|  _|        _|_|_|
        _|    _|  _|    _|  _|    _|  _|    _|    _|    _|    _|_|  _|    _|      _|        _|    _|  _|        _|
        _|    _|    _|_|      _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|        _|    _|    _|_|_|  _|_|_|_|
    
        To log in, ``huggingface_hub`` requires a token generated from https://huggingface.co/settings/tokens .
    Enter your token (input will not be visible):
    Add token as git credential? [y/N]: n
    Token is valid (permission: write).
    The token ``[REDACTED]`` has been saved to /home/giles/.cache/huggingface/stored_tokens
    Your token has been saved to /home/giles/.cache/huggingface/token
    Login successful.
    The current active token is: ``[REDACTED]``
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uvx hf repo create fineweb-gpt2-tokens --repo-type dataset
    Successfully created gpjt/fineweb-gpt2-tokens on the Hub.
    Your repo is now available at https://huggingface.co/datasets/gpjt/fineweb-gpt2-tokens
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uvx hf repo create fineweb-edu-gpt2-tokens --repo-type dataset
    Successfully created gpjt/fineweb-edu-gpt2-tokens on the Hub.
    Your repo is now available at https://huggingface.co/datasets/gpjt/fineweb-edu-gpt2-tokens
    

Both datasets show up on my profile page on Hugging Face, so that's looking good. Now it's time to try to upload the data. We'll need to install Git's LFS support first:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ git lfs install
    Updated Git hooks.
    Git LFS initialized.
    

Now let's try the FineWeb one first:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ git clone https://huggingface.co/datasets/gpjt/fineweb-gpt2-tokens
    Cloning into 'fineweb-gpt2-tokens'...
    remote: Enumerating objects: 3, done.
    remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 3 (from 1)
    Unpacking objects: 100% (3/3), 1.17 KiB | 1.17 MiB/s, done.
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ cd fineweb-gpt2-tokens
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ cp ../fineweb-prepared/train.safetensors .
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ cp ../fineweb-prepared/validation.safetensors .
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ cat > meta.json << 'EOF'
    {
      "description": "FineWeb 10BT tokenized with GPT-2 BPE (tiktoken). uint16 safetensors, single long sequence with ``<|endoftext|>`` separators.",
      "token_dtype": "uint16",
      "files": {
        "train": "train.safetensors",
        "validation": "validation.safetensors"
      }
    }
    EOF
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ git add .
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ git commit -am"First cut, added GPT-2 tokens"
    [main 3af6ef2] First cut, added GPT-2 tokens
     3 files changed, 14 insertions(+)
     create mode 100644 meta.json
     create mode 100644 train.safetensors
     create mode 100644 validation.safetensors
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ git push
    Username for 'https://huggingface.co': gpjt
    Password for 'https://gpjt@huggingface.co':
    Username for 'https://huggingface.co': gpjtB/s
    Password for 'https://gpjt@huggingface.co':
    batch response:
    You need to configure your repository to enable upload of files > 5GB.
    Run "hf lfs-enable-largefiles ./path/to/your/repo" and try again.
    
    error: failed to push some refs to 'https://huggingface.co/datasets/gpjt/fineweb-gpt2-tokens'
    

OK, so we need some kind of extra thing to tell it we can use large files on top of the LFS stuff:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ uvx hf lfs-enable-largefiles .
    Local repo set up for largefiles
    

Right, now let's try again:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ git push
    Username for 'https://huggingface.co': gpjt
    Password for 'https://gpjt@huggingface.co':
    Username for 'https://huggingface.co': gpjtB/s
    Password for 'https://gpjt@huggingface.co':
    EOFoading LFS objects: 100% (2/2), 21 GB | 0 B/s
    error: failed to push some refs to 'https://huggingface.co/datasets/gpjt/fineweb-gpt2-tokens'
    

Weird that it prompted for the credentials twice, but it did appear to try to do something there -- but obviously it didn't work.

Let's see if Git over SSH is any better.
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ cd ..
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ rm -rf fineweb-gpt2-tokens/
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ git clone git@hf.co:datasets/gpjt/fineweb-gpt2-tokens
    Cloning into 'fineweb-gpt2-tokens'...
    ** WARNING: connection is not using a post-quantum key exchange algorithm.
    ** This session may be vulnerable to "store now, decrypt later" attacks.
    ** The server may need to be upgraded. See https://openssh.com/pq.html
    remote: Enumerating objects: 3, done.
    remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 3 (from 1)
    Receiving objects: 100% (3/3), done.
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ cd fineweb-gpt2-tokens
    

...then the same stuff to copy in the files and create the metadata file, then:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ uvx hf lfs-enable-largefiles .
    Local repo set up for largefiles
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ git add .
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ git commit -am"First cut of code to prepare datasets"
    [main 44df15c] First cut of code to prepare datasets
     3 files changed, 14 insertions(+)
     create mode 100644 meta.json
     create mode 100644 train.safetensors
     create mode 100644 validation.safetensors
    giles@perry:~/Dev/ddp-base-model-from-scratch/fineweb-gpt2-tokens (main)$ git push
    ** WARNING: connection is not using a post-quantum key exchange algorithm.
    ** This session may be vulnerable to "store now, decrypt later" attacks.
    ** The server may need to be upgraded. See https://openssh.com/pq.html
    EOFoading LFS objects: 100% (2/2), 21 GB | 0 B/s
    error: failed to push some refs to 'hf.co:datasets/gpjt/fineweb-gpt2-tokens'
    

Looks like the same error. Odd.

Let's try using HF's upload tools rather than Git -- feels like a bit of a cop-out, but maybe it'll work better.
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uvx hf upload gpjt/fineweb-gpt2-tokens ./fineweb-prepared/train.safetensors train.safetensors --repo-type dataset
    Processing Files (1 / 1)      : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 20.5GB / 20.5GB, 2.76MB/s
    New Data Upload               : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 2.95GB / 2.95GB, 2.76MB/s
      ...repared/train.safetensors: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 20.5GB / 20.5GB
    https://huggingface.co/datasets/gpjt/fineweb-gpt2-tokens/commit/69085f941ba3e8f0750929a1f8cd451fba761bff
    

That did indeed take about 200 seconds to run, but the upload speed was only about 10 MiB/s -- from the output, I think it must have been compressing it. Anyway, it looks like it succeeded, so let's upload the others!
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uvx hf upload gpjt/fineweb-gpt2-tokens ./fineweb-prepared/validation.safetensors validation.safetensors --repo-type dataset
    Processing Files (1 / 1)      : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ|  205MB /  205MB, 78.7MB/s
    New Data Upload               : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ|  235kB /  235kB, 90.6kB/s
      ...ed/validation.safetensors: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ|  205MB /  205MB
    https://huggingface.co/datasets/gpjt/fineweb-gpt2-tokens/commit/885777d5211383cc7990004f99a8823fad53be66
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uvx hf upload gpjt/fineweb-edu-gpt2-tokens ./fineweb-edu-prepared/train.safetensors train.safetensors --repo-type dataset
    Processing Files (1 / 1)      : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 19.7GB / 19.7GB, 4.53MB/s
    New Data Upload               : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3.09GB / 3.09GB, 4.53MB/s
      ...repared/train.safetensors: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 19.7GB / 19.7GB
    https://huggingface.co/datasets/gpjt/fineweb-edu-gpt2-tokens/commit/55baacd6812ac085df0c91ea573c8ccd89015341
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uvx hf upload gpjt/fineweb-edu-gpt2-tokens ./fineweb-edu-prepared/validation.safetensors validation.safetensors --repo-type dataset
    Processing Files (1 / 1)      : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ|  201MB /  201MB, 62.8MB/s
    New Data Upload               : 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ|  104kB /  104kB, 32.5kB/s
      ...ed/validation.safetensors: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ|  201MB /  201MB
    https://huggingface.co/datasets/gpjt/fineweb-edu-gpt2-tokens/commit/8bc548d681476ecc79444779746d6dc1a852cca2
    

...and that's done :-)

Next, a bit of manual editing of the dataset cards on the Hugging Face website, and we have our two new public datasets:

  * [`gpjt/fineweb-gpt2-tokens`](https://huggingface.co/datasets/gpjt/fineweb-gpt2-tokens)
  * [`gpjt/fineweb-edu-gpt2-tokens`](https://huggingface.co/datasets/gpjt/fineweb-edu-gpt2-tokens)



That looks solid. So, the next thing: change our codebase so that we have some quick and easy way to download them (I'm feeling a little wary of using Git for that after the upload issue), and then to use the downloaded files in our training code.

### Downloading the datasets from Hugging Face

We already have the code to download a dataset; the stuff that I wrote to [download FineWeb and FineWeb-Edu](https://github.com/gpjt/ddp-base-model-from-scratch/blob/aede6fbca2bf5ca518995ef39e58103e4c2dae15/download-fineweb-10b.py) originally. Here's the important bit:
    
    
    from huggingface_hub import snapshot_download
    
    ...
    
        folder = snapshot_download(
            f"HuggingFaceFW/{name}",
            repo_type="dataset",
            local_dir=f"./{name}/",
            allow_patterns="sample/10BT/*"
        )
    

...so we can adapt that to download all files in an arbitrary dataset:
    
    
    def download_dataset(datasets_dir, dataset_name):
        download_path = snapshot_download(
            f"{dataset_name}",
            repo_type="dataset",
            local_dir=datasets_dir / dataset_name,
            allow_patterns="*"
        )
        return Path(download_path)
    

...and call that from our `main`, using a new command-line argument `datasets_dir_path`, and a new `dataset` element in our train config JSON file:
    
    
        datasets_dir = Path(datasets_dir_path)
        if not datasets_dir.is_dir():
            raise Exception(f"{datasets_dir_path} is not a directory")
        dataset_dir = download_dataset(datasets_dir, train_conf["dataset"])
    

I was thinking that we'd need extra guard code to not download the dataset again if it's already there, but it looks like `snapshot_download` handles that all nicely for us.

So we have a way to specify which dataset we should use for a training run, and code to download it. Now we just need to adjust the code that loads our datasets so that instead of looking in the `run_dir`, it looks in the directory returned by `download_dataset`:
    
    
        train_ds = load_dataset(
            dataset_dir, "train",
            model_conf["context_length"], train_conf["microbatch_size"]
        )
        val_ds = load_dataset(
            dataset_dir, "validation",
            model_conf["context_length"], train_conf["microbatch_size"]
        )
    

...and update the `load_dataset` directory so that if just blindly uses the directory provided rather than trying to look in a `datasets` subdirectory:
    
    
    def load_dataset(dataset_dir, split, seq_length, microbatch_size):
        return BigTrainDataset(
            load_file(dataset_dir / f"{split}.safetensors")["tokens"],
            seq_length, microbatch_size,
        )
    

That all works! We successfully download the datasets and try to use them. [Here's the code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/441e3564e2dabc9e06dbc7d1783d086312a11960/ddp_train.py).

But now we have a problem; when the `BigTrainDataset` tries to reshape the huge tensor that we have as our inputs:
    
    
            self.xs = all_tokens[:-1].reshape(-1, microbatch_size, seq_length)
    

...it craps out:
    
    
    RuntimeError: shape '[-1, 6, 1024]' is invalid for input of size 10248871836
    

That makes perfect sense. Our original `safetensors` files were carefully sized for a batch size of six, and 1024-token sequences. We need some way to work out an appropriate slice of both the training and the validation data.

### Slicing the datasets

Most of the trains are likely to be Chinchilla-optimal, or at least use a Chinchilla-optimal number of tokens -- rounded up appropriately to match our micro-batch size, sequence length, and world size.

But I'd like it to be more configurable. What I'll do is add a `min_train_tokens` key to the training config dictionary, along with a `start_train_token` so that we can (for example) train on the first Chinchilla-optimal tokens, then do an extended train continuing on from there. The idea is that we can use `min_train_tokens` as a base, and train on the smallest number of full batches that contains at least that many tokens.

For validation, I think that the `validation_batches` key that we already have is actually quite nice. Validation is time-bound, and the number of batches is the easiest lever to pull to handle that. However, a `start_val_token` would be nice for symmetry.

So, here are some numbers for debugging:
    
    
    {
        "microbatch_size": 6,
        "validation_interval": 10,
        "dataset": "gpjt/fineweb-gpt2-tokens",
        "min_train_tokens": 3260190720,
        "start_train_token": 0,
        "validation_batches": 3,
        "start_val_token": 0
    }
    

Now let's use them. Initially, we have this to load the train dataset:
    
    
        train_ds = load_dataset(
            dataset_dir, "train",
            model_conf["context_length"], train_conf["microbatch_size"]
        )
    

Let's work through that one first then make appropriate changes to the validation one. The pieces of information we need to work out which tokens to use are:

  * The `min_train_tokens`
  * The `start_train_token`
  * The world size -- that is, how many per-GPU processes are we running?
  * The micro-batch size
  * The sequence length



Let's update our `load_dataset` function so that it takes those parameters in that order:
    
    
        train_ds = load_dataset(
            dataset_dir, "train",
            train_conf["min_train_tokens"], train_conf["start_train_token"],
            dist.get_world_size(), train_conf["microbatch_size"],
            model_conf["context_length"]
        )
    

...and now we can write an updated `load_dataset` that uses those numbers to get the right number of tokens:
    
    
    def load_dataset(
        dataset_dir, split,
        min_tokens, start_token,
        world_size, microbatch_size,
        seq_length
    ):
        full_dataset = load_file(dataset_dir / f"{split}.safetensors")["tokens"]
    
        one_full_batch_tokens = world_size * microbatch_size * seq_length
        batches_for_just_over_min = (min_tokens // one_full_batch_tokens) + 1
    
        # Note that we need one extra token for our Ys.
        tokens_needed = (batches_for_just_over_min * one_full_batch_tokens) + 1
    
        if len(full_dataset) < start_token + tokens_needed:
            raise Exception(f"Not enough tokens (wanted {start_token + tokens_needed}, got {len(full_dataset)})")
    
        return BigTrainDataset(
            full_dataset[start_token:start_token + tokens_needed],
            seq_length, microbatch_size,
        )
    

Validation is less obvious; I think that the best way to do this (given that the validation dataset is small) is just to have a "magic" `-1` value for `min_tokens`, which means "just get a round number of full batches starting at `start_val_token`. It's also worth remembering that we only do evals on the rank 0 process, so we could in theory pass in a world size of 1 -- but I think that passing in the real world size might be a good idea, because it gives us one fewer thing to change if, in the future, we move towards distributed evals.

So:
    
    
        val_ds = load_dataset(
            dataset_dir, "validation",
            -1, train_conf["start_val_token"],
            dist.get_world_size(), train_conf["microbatch_size"],
            model_conf["context_length"]
        )
    

...and we change `load_dataset` to be able to handle the magic `-1`:
    
    
    def load_dataset(
        dataset_dir, split,
        min_tokens, start_token,
        world_size, microbatch_size,
        seq_length
    ):
        full_dataset = load_file(dataset_dir / f"{split}.safetensors")["tokens"]
        if start_token > len(full_dataset):
            raise Exception(f"start_token {start_token} is past the end of the dataset")
    
        one_full_batch_tokens = world_size * microbatch_size * seq_length
    
        if min_tokens == -1:
            available_tokens = len(full_dataset) - start_token
            available_batches = (available_tokens // one_full_batch_tokens)
            tokens_needed = available_batches * one_full_batch_tokens
        else:
            batches_for_just_over_min = (min_tokens // one_full_batch_tokens) + 1
            tokens_needed = batches_for_just_over_min * one_full_batch_tokens
    
        # Note that we need one extra token for our Ys.
        tokens_needed += 1
    
        if len(full_dataset) < start_token + tokens_needed:
            raise Exception(f"Not enough tokens (wanted {start_token + tokens_needed}, got {len(full_dataset)})")
    
        return BigTrainDataset(
            full_dataset[start_token:start_token + tokens_needed],
            seq_length, microbatch_size,
        )
    

I also added in a quick sanity check to make sure that we don't get weird behaviour if the `start_token` is past the end of the original dataset.

That all looks good! Running it kicks off training, and validation is running happily every ten global steps, but just with three samples, as configured in the JSON file. [Here's the code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/36e475bcae5ef36757ddd3cff4da8692d2434213/ddp_train.py).

### QoL features

One thing that hasn't shown up while running this code locally is that our training loop has this:
    
    
        for global_step in tqdm(range(start_global_step, total_global_steps)):
    

With one GPU, that's fine, but on a multi-GPU machine, that `tqdm` is going to happen in all of our per-GPU processes \-- so they'll all be spamming out progress bars, which will be ugly. So, as a first cut:
    
    
        for global_step in tqdm(range(start_global_step, total_global_steps), disable=(rank != 0)):
    

Now, in order to compare different machines (say, an 8x H100 vs an 8x A100) it would be nice to get tokens-per-second numbers while training. We can do that in the `tqdm` progress bar too! It has a `set_postfix` method that adds stuff to the end of the bar, just after the elapsed time and iterations/second numbers. For that, we'll need to have the `tqdm` object available in a variable:
    
    
        progress_bar = tqdm(
            range(start_global_step, total_global_steps),
            disable=(rank != 0)
        )
        for global_step in progress_bar:
    

...and now we can count the total tokens seen in the training run, plus keep track of the start time -- just before the start of the training loop:
    
    
        start_time = time.time()
        tokens_seen_this_rank = 0
    

...then inside, after the training step:
    
    
            microbatch_size, sequence_length = inputs.shape
            tokens_seen_this_rank += microbatch_size * sequence_length
    
            if rank == 0:
                elapsed_time = time.time() - start_time
                tokens_per_sec = (tokens_seen_this_rank * world_size) / elapsed_time
                progress_bar.set_postfix(
                    loss=f"{train_loss.item():.3f}",
                    tps=f"{tokens_per_sec:,.0f}"
                )
    

That will give us a running average of tokens per second over the train as a whole since the start.

Running that, we get a nice progress bar like this (you'll need to scroll to the right):
    
    
      0%|                                                                                                      | 10/530631 [00:04<47:31:23,  3.10it/s, loss=8.094, tps=14,362]
    

Note that the tokens per second is worse than the just less than 20k that we got when running the single-GPU test previously, but that's due to the testing setup I have -- I'm doing an eval every 10 global steps. Changing that to 1,000,000 so that we just get a single eval when we start, then letting it run for a while to settle down from the initial eval, we get this:
    
    
      0%|                                                                                                     | 631/530631 [03:17<46:02:23,  3.20it/s, loss=6.890, tps=19,678]
    

...which is close enough to what we had before.

Finally, let's print out some summary information at the end:
    
    
        end_time = time.time()
        elapsed_time = end_time - start_time
    
        if rank == 0:
            print(f"\n\n\nTraining complete in {elapsed_time:,.3f} seconds")
            total_tokens_seen = tokens_seen_this_rank * world_size
            print(f"Tokens seen: {total_tokens_seen:,.0f}")
            print(f"Throughput: {total_tokens_seen / elapsed_time:,.0f} tokens/second")
            print(f"Final train loss: {avg_train_loss:.3f}")
            print(f"Final val loss: {val_loss:.3f}")
    

Ran that on a super-short train with about 50 iterations-worth of tokens, and:
    
    
    Training complete in 26.520 seconds
    Tokens seen: 331,776
    Throughput: 12,510 tokens/second
    Final train loss: 7.817
    Final val loss: 8.093
    

Looking good. [Here's the code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/d6c0baaf7081828614beda68d47620084d99b805/ddp_train.py).

I think we now have something where it's worth spinning up a Lambda Labs machine to run it.

### A first run on Lambda Labs

Let's kick off a training run on the cheapest two-GPU machine that they have available right now. That's actually not all that cheap, it's a $6.38/hour 2x H100 80 GiB SXM5. But I'm not planning to do a full train on it yet, this is just a sanity test.

I won't attach a filesystem this time, either -- let's see how things go without the caching of the datasets that I was considering.

First thing: do we have `uv`?
    
    
    ubuntu@192-222-53-181:~$ uv
    uv: command not found
    

Nope. OK, let's install it:
    
    
    ubuntu@192-222-53-181:~$ curl -LsSf https://astral.sh/uv/install.sh | sh
    downloading uv 0.9.15 x86_64-unknown-linux-gnu
    no checksums to verify
    installing to /home/ubuntu/.local/bin
      uv
      uvx
    everything's installed!
    

Right, now let's clone our repo and set up our environment:
    
    
    ubuntu@192-222-53-181:~$ git clone https://github.com/gpjt/ddp-base-model-from-scratch.git
    Cloning into 'ddp-base-model-from-scratch'...
    remote: Enumerating objects: 123, done.
    remote: Counting objects: 100% (123/123), done.
    remote: Compressing objects: 100% (82/82), done.
    remote: Total 123 (delta 66), reused 88 (delta 34), pack-reused 0 (from 0)
    Receiving objects: 100% (123/123), 124.76 KiB | 3.46 MiB/s, done.
    Resolving deltas: 100% (66/66), done.
    ubuntu@192-222-53-181:~$ cd ddp-base-model-from-scratch/
    ubuntu@192-222-53-181:~/ddp-base-model-from-scratch$ uv sync
    Using CPython 3.13.10
    Creating virtual environment at: .venv
    Resolved 90 packages in 0.58ms
    Prepared 88 packages in 34.05s
    Installed 88 packages in 133ms
    ...
    

And now I think we can just try running it!
    
    
    ubuntu@192-222-53-181:~/ddp-base-model-from-scratch$ uv run torchrun ddp_train.py original datasets
    Fetching 4 files: 100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:18<00:00,  4.51s/it]
    Download complete: : 20.7GB [00:18, 724MB/s]                                                                                                                              Starting rank 0 training at global step 0
    
      0%|                                                                                                                 | 0/530631 [00:00<?, ?it/s, loss=10.972, tps=12,439]
    
    Validation/checkpoint
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 2/2 [00:00<00:00, 33.12it/s]
    Download complete: : 20.7GB [00:19, 1.06GB/s]
    findfont: Font family 'xkcd' not found.                                                                                                             | 0/2 [00:00<?, ?it/s]
    findfont: Font family 'xkcd' not found.
    findfont: Font family 'xkcd' not found.
    

It took 18 seconds to download the dataset! I don't think we need to worry about the caching thing with persistent disks, at least at this point.

But there are a couple of issues here. I didn't put the number of processes in the command line \-- I should be using
    
    
    uv run torchrun --nproc_per_node=2 ddp_train.py original datasets
    

Also, we don't have the XKCD font family. I'll ignore that for now.
    
    
    ubuntu@192-222-53-181:~/ddp-base-model-from-scratch$ uv run torchrun --nproc_per_node=2 ddp_train.py original datasets
    W1205 20:16:58.548000 6491 torch/distributed/run.py:803]
    W1205 20:16:58.548000 6491 torch/distributed/run.py:803] *****************************************
    W1205 20:16:58.548000 6491 torch/distributed/run.py:803] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed.
    W1205 20:16:58.548000 6491 torch/distributed/run.py:803] *****************************************
    Fetching 4 files: 100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 8260.57it/s]
    Fetching 4 files: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 19418.07it/s]
    Download complete: : 0.00B [00:00, ?B/s]              Starting rank 0 training at global step 0                                                     | 0/4 [00:00<?, ?it/s]
    Starting rank 1 training at global step 0
    
      0%|                                                                                                                 | 0/265316 [00:00<?, ?it/s, loss=10.982, tps=26,590]
    
    Validation/checkpoint
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 2/2 [00:00<00:00, 33.23it/s]
    findfont: Font family 'xkcd' not found.
    ...
    
    Continuing training
    
      0%|                                                                                                      | 10/265316 [00:03<13:29:38,  5.46it/s, loss=8.391, tps=35,279]
    

OK, that's looking good! Let's make our validations happen less often, and see how high we can get the micro-batches with the 80 GiB VRAM we have on each of our two GPUs.

Doing a binary chop, I set the micro-batch size to 100 (OOM), then to 50 (OOM), then to 25 (worked), then to 37 (OOM), then 31 (OOM), then 28 (worked), and finally 29 (OOM).

So we have a batch size of 28 for our 80 GiB machines. Leaving it for a little while to settle down, and we get to about 142,000 tokens/second.

Now, on the 3090, we were training at 20,000 tokens/second. That means that this machine is running at about 7 times the speed. Given that our original train finished in 48 hours, we'd expect the train to finish in about 6, which indeed is the estimated time on the tqdm progress bar.

At $6.38 per hour, that comes to $38.28. Not bad! And this instance is actually quite pricey on a per-GPU basis -- it's $3.19 per GPU/hour, whereas there is an 8x H100 that costs $2.99 per GPU/hour.

I'm almost tempted to let it run. But the purpose of this run was to work out the bugs.

We're going to want to track the training chart -- remember that after every validation run, our training code generates a chart showing the training and validation loss so far, [like this one](/post-assets/llm-from-scratch-28-training-a-base-model-from-scratch/big-training-run-chart-fineweb.png). I ran the normal quick-and-dirty Python webserver command on the instance, inside the directory containing the training chart:
    
    
    ubuntu@192-222-53-181:~/ddp-base-model-from-scratch/runs/original$ python -m http.server 8000
    

My browser didn't connect to it, but looking at the Lambda Labs interface, there's a new "Firewall" section, where you configure rules for allowing incoming connections to your instances. That's sensible, and the default rules are just "allow SSH from any IP" and "allow ping from any IP". Adding one letting anyone access port 8000 fixed the problem, and I saw a directory listing; clicking on the chart showed exactly what I'd expect, but without the XKCD fonts. Nice.

Let's work out how to fix that XKCD font thing. Looking around, it seems like there are approximately twenty thousand ways to do it. Here's one that seems to work; firstly, install the font on the system:
    
    
    mkdir -p ~/.local/share/fonts
    curl -sL https://github.com/ipython/xkcd-font/raw/master/xkcd-script/font/xkcd-script.ttf -o ~/.local/share/fonts/xkcd-script.ttf
    fc-cache -f -v
    

Now, that installs a font that has the family name 'xkcd Script` (with that erratic capitalisation). So we need to change the code to pick up pretty much anything that looks like it's XKCD, so instead of this:
    
    
    plt.rcParams['font.family'] = "xkcd"
    

...we can do this:
    
    
    from matplotlib import font_manager
    
    ...
    
        font_family = None
        for f in font_manager.fontManager.ttflist:
            if "xkcd" in f.name.lower():
                font_family = f.name
                break
    
        if font_family is not None:
            plt.rcParams['font.family'] = font_family
    

That seems to work OK.

So, now, I think we have the beginnings of a script to set up a Lambda Labs machine so that we can use it. Let's write a [`setup_lambda.sh`](https://github.com/gpjt/ddp-base-model-from-scratch/blob/30a3fd75f1eab96cd598a6c0a0f14465ddee6ae4/setup_lambda.sh) with this:
    
    
    #!/bin/bash
    set -a
    curl -LsSf https://astral.sh/uv/install.sh | sh
    mkdir -p ~/.local/share/fonts
    curl -sL https://github.com/ipython/xkcd-font/raw/master/xkcd-script/font/xkcd-script.ttf -o ~/.local/share/fonts/xkcd-script.ttf
    fc-cache -f -v
    

...and give it another go on a fresh machine. Shut this one down -- total cost so far $7.28.

### A second run on Lambda Labs, as a sanity check

Now there are no 2-GPU instances available. There is a super-cheap 1x A10 (basically the datacenter version of a 3090), though, so let's use that -- we're as certain as we can be that the multi-GPU stuff works, and the proof of the pudding will be whether we can train a model that works.

After spinning up our 1x A10 machine:
    
    
    ubuntu@150-136-154-247:~$ git clone https://github.com/gpjt/ddp-base-model-from-scratch.git
    Cloning into 'ddp-base-model-from-scratch'...
    remote: Enumerating objects: 134, done.
    remote: Counting objects: 100% (134/134), done.
    remote: Compressing objects: 100% (89/89), done.
    remote: Total 134 (delta 70), reused 98 (delta 37), pack-reused 0 (from 0)
    Receiving objects: 100% (134/134), 127.03 KiB | 31.76 MiB/s, done.
    Resolving deltas: 100% (70/70), done.
    ubuntu@150-136-154-247:~$ cd ddp-base-model-from-scratch
    ubuntu@150-136-154-247:~/ddp-base-model-from-scratch$ ./setup_lambda.sh
    downloading uv 0.9.15 x86_64-unknown-linux-gnu
    no checksums to verify
    installing to /home/ubuntu/.local/bin
      uv
      uvx
    everything's installed!
    /usr/share/fonts: caching, new cache contents: 0 fonts, 2 dirs
    /usr/share/fonts/opentype: caching, new cache contents: 0 fonts, 1 dirs
    /usr/share/fonts/opentype/font-awesome: caching, new cache contents: 1 fonts, 0 dirs
    /usr/share/fonts/truetype: caching, new cache contents: 0 fonts, 4 dirs
    /usr/share/fonts/truetype/dejavu: caching, new cache contents: 6 fonts, 0 dirs
    /usr/share/fonts/truetype/font-awesome: caching, new cache contents: 1 fonts, 0 dirs
    /usr/share/fonts/truetype/lato: caching, new cache contents: 18 fonts, 0 dirs
    /usr/share/fonts/truetype/lyx: caching, new cache contents: 12 fonts, 0 dirs
    /usr/local/share/fonts: caching, new cache contents: 0 fonts, 0 dirs
    /home/ubuntu/.local/share/fonts: caching, new cache contents: 1 fonts, 0 dirs
    /home/ubuntu/.fonts: skipping, no such directory
    /usr/share/fonts/opentype: skipping, looped directory detected
    /usr/share/fonts/truetype: skipping, looped directory detected
    /usr/share/fonts/opentype/font-awesome: skipping, looped directory detected
    /usr/share/fonts/truetype/dejavu: skipping, looped directory detected
    /usr/share/fonts/truetype/font-awesome: skipping, looped directory detected
    /usr/share/fonts/truetype/lato: skipping, looped directory detected
    /usr/share/fonts/truetype/lyx: skipping, looped directory detected
    /var/cache/fontconfig: not cleaning unwritable cache directory
    /home/ubuntu/.cache/fontconfig: cleaning cache directory
    /home/ubuntu/.fontconfig: not cleaning non-existent cache directory
    fc-cache: succeeded
    ubuntu@150-136-154-247:~/ddp-base-model-from-scratch$ mkdir datasets
    ubuntu@150-136-154-247:~/ddp-base-model-from-scratch$ uv run torchrun --nproc_per_node=1 ddp_train.py original datasets
    Using CPython 3.13.10
    Creating virtual environment at: .venv
    Installed 88 packages in 1.30s
    Fetching 4 files: 100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:14<00:00,  3.60s/it]
    Download complete: : 20.7GB [00:14, 1.20GB/s]                                                                                                                             Starting rank 0 training at global step 0
    Download complete: : 20.7GB [00:15, 1.36GB/s]
      0%|                                                                                                                                          | 0/530631 [00:00<?, ?it/s]
      0%|                                                                                                                  | 0/530631 [00:00<?, ?it/s, loss=10.981, tps=6,533]
    
    Validation/checkpoint
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 2/2 [00:00<00:00,  7.27it/s]
    

Looking good! I think we have something that (in theory) should work. That cost $0.05.

I think it's time to do our first train on a big instance.

### First train on a big instance: 8x A100, 40 GiB/GPU, SXM4

There are four 8x instances available on Lambda Labs for me right now:

  * An 8x B200, with 160 GiB per GPU, at $39.92/hour
  * An 8x H100, with 80 GiB per GPU, at $23.92/hour
  * An 8x A100, with 80 GiB per GPU, at $14.32/hour
  * An 8x A100, with 40 GiB per GPU, at $10.32/hour



I think I'm going to want to train on all of those, to try to work out some kind of metric (dollars per megatoken?) to compare them. But let's start with something reasonably low-end -- in fact, let's try the cheapest, and see what happens.

Spin one up, and first thing; after the setup, we need to work out the micro-batch size. Last time we used 28, but this machine has GPUs with half as much VRAM. I did a binary chop again... it turns out to be 13.

Now let's think about validation frequency. Let's try to get a feel for how long it will take. We can set the eval batches to (say) 100, so that we can see how fast evals are, but also set the interval to 10,000,000 so that it never does one after the first.

It took 11 seconds to run 100 validation batches, and after a few minutes, it settles down at 254,000 tokens/second or so, and is estimating 3h15m to completion. Nice! The cards are an earlier generation to the H100s we used in the two-GPU test, so they're slower, and they have half the VRAM. So eight of them are, working together, about twice as fast as two H100s. Doesn't sound completely crazy.

So, in our local train, we spent 5 minutes evaluating every 30 minutes. So our eval time was 16% of our train time. Probably a bit high, but let's run with it.

If we're going to take 3 hours training time, then 16% of that is about 28 minutes. Previously we did about 88 evals (44 hours train time, with an eval after each half hour). That seems a bit too high. So let's say that we want to do 50 evals.

28 minutes eval time in total, with 50 of them, means about 30 seconds per eval. If 100 eval batches take 11 seconds, let's approximate it to 300 eval batches.

As to the interval between them -- if we want to do 50 over 3h15m, or 195 minutes, then that's one every (let's approximate) 4 minutes. We seem to have settled down to 2.57 iterations per second, so that's about every 617 iterations.

Let's bake those in and let it rip.
    
    
    ubuntu@129-213-131-52:~/ddp-base-model-from-scratch$ cat runs/8xa100m40/train.json
    {
        "microbatch_size": 13,
        "validation_interval": 617,
        "dataset": "gpjt/fineweb-gpt2-tokens",
        "min_train_tokens": 3260190720,
        "start_train_token": 0,
        "validation_batches": 300,
        "start_val_token": 0
    }
    

After the run:
    
    
    Training complete in 13,904.270 seconds
    Tokens seen: 3,260,268,544
    Throughput: 234,480 tokens/second
    Final train loss: 3.720
    Final val loss: 3.675
    

OK, let's download everything.
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch/first-cloud-train (main)$ scp ubuntu@129.213.131.52:/home/ubuntu/ddp-base-model-from-scratch/runs/8xa100m40/big-training-run-chart.png .
    big-training-run-chart.png
    

Looking at the checkpoints, the latest (that is, the last one at the end of the training) and best (the checkpoint that had the lowest validation loss) are the same one, meaning that validation loss kept falling consistently:
    
    
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec  6 01:49 20251206Z014912-iteration-29616
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec  6 01:53 20251206Z015351-iteration-30233
    lrwxrwxrwx 1 ubuntu ubuntu   31 Dec  6 01:57 latest -> 20251206Z015658-iteration-30613
    lrwxrwxrwx 1 ubuntu ubuntu   31 Dec  6 01:57 best -> 20251206Z015658-iteration-30613
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec  6 01:57 20251206Z015658-iteration-30613
    

So let's just download using the "best" symlink to get the weights for that checkpoint:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xa100m40 (main)$ scp -r ubuntu@129.213.131.52:/home/ubuntu/ddp-base-model-from-scratch/runs/8xa100m40/big-training-run-chart.png .
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xa100m40 (main)$ mkdir checkpoints; cd checkpoints
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xa100m40/checkpoints (main)$ scp -r ubuntu@129.213.131.52:/home/ubuntu/ddp-base-model-from-scratch/runs/8xa100m40/checkpoints/best/ .
    scaler.pt                                                                                                                               100% 1383     6.8KB/s   00:00
    optimizer.pt                                                                                                                            100% 1244MB   7.7MB/s   02:41
    model.safetensors                                                                                                                       100%  670MB   7.4MB/s   01:29
    meta.json                                                                                                                               100%  104     0.5KB/s   00:00
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xa100m40/checkpoints (main)$ ls -lrt
    total 84
    drwxr-xr-x 2 giles giles  4096 Dec  6 02:05 best
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xa100m40/checkpoints (main)$ ls best
    meta.json  model.safetensors  optimizer.pt  scaler.pt
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xa100m40/checkpoints (main)$ ls -h best
    meta.json  model.safetensors  optimizer.pt  scaler.pt
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xa100m40/checkpoints (main)$ ls -lh best
    total 1.9G
    -rw-r--r-- 1 giles giles  104 Dec  6 02:05 meta.json
    -rw-r--r-- 1 giles giles 670M Dec  6 02:05 model.safetensors
    -rw-r--r-- 1 giles giles 1.3G Dec  6 02:04 optimizer.pt
    -rw-r--r-- 1 giles giles 1.4K Dec  6 02:01 scaler.pt
    

And now we can shut the cloud machine down.

Now that the clock is no longer ticking and we aren't spending money on an unused machine, here's the training chart:

![Training run on an 8x A100 with 40 GiB/GPU](/post-assets/llm-from-scratch-29-ddp-training-a-base-model-in-the-cloud/training-run-8xa100m40.png)

It looks like we had a couple of gradient spikes there. I'm going to add some gradient clipping code at some point, but I think I'll hold off for a little bit -- I want to do a few cloud trains first to work out the best instance sizes to use, and only then start exploring the possibilities for making the models better.

Apart from that, it looks pretty normal.

Looking at the billing page on Lambda Labs, that machine was up for about 4 hours and 35 minutes, costing US$10.32 per hour, for a total cost of US$47.35.

Of that 4h35m, 13,904 seconds, or 3h52 was the actual training run -- somewhat more than the 3h15m that was predicted at the start of the run. The validation will have accounted for most of that -- we did 50 evals, at 30 seconds each, so that's 25 minutes. That means that 3h40m is accounted for, and the remainder can just be chalked up to noise, I guess.

That leads to one question: do we actually need to be doing validation for these trains?

### To validate or not to validate?

I've been doing validation loops in these trains largely out of habit -- when you're training an ML model, it's just "what you do".

The reason you'd normally hold out a validation set is simple: if you're training over multiple epochs, then eventually your model is going to start overfitting to the training data 2. You validate as you go along so that you can spot any points where, while the training loss continues to drop, the validation loss -- which is loss on data that the model hasn't been trained on -- starts rising. That's the classic indicator of overfitting.

But for these models we're not doing multiple epochs -- we're just training through a stream of constantly new tokens. So, in fact, there's no real difference between the training data and the validation data, apart from the fact that the validation data is constant. From the model's perspective, it's all new stuff (modulo any repetitions in the dataset, which is possible but I think not likely to be super-common in something as curated as FineWeb).

Now, in this post I'm aiming to identify the best options for training in the cloud -- cost in terms of dollars and time. I don't want to change the model itself or the training strategy because I want whatever I come up with to be roughly equivalent to the models I trained on my own machine. Exploring enhancements is for the next post. (Of course, given that the batch size is one of the levers I want to experiment with, and training on larger machines is already meaning that I'm doing micro-batches larger than the batch size of 6 that I used locally, and then the overall batches are 8 times larger, that's not quite true.)

Validation, however, doesn't actually affect the training runs in any direct way. I could in theory remove it.

However, that is a relatively large change to the code, as I've kind of linked it in with my checkpointing code.

I think that what I'll do for now is leave it in. Validation will scale at the same rate as training (so long as I leave the eval batches constant) so it leaving it there will give me a clean comparison between machine types. And I can keep notes on how much time was spent on validation for each train so that I can subtract it from the total time if that proves useful.

However, when I start tweaking the training code with changes beyond the batch size, I should probably try removing validation first.

Anyway, while validation during the training run might not be important, evaluating the model at the end and seeing how it compares to others is! Let's do that next.

### Testing the first model

There were two important post-train evals that I did on the models that I trained locally:

  1. The loss they got on the validation set from the first train. Strictly speaking, I was kind of cheating and using that as a test set.
  2. The score given by the OpenAI GPT 5.1 model for an instruction-following dataset. This was the one provided in the book -- an Alpaca-style Q&A dataset, with a well-defined train and test set. Each model was fine-tuned on a training set of 85% of the data until loss on a validation set of 5% of the data started rising, and then tested on the remaining 10%. Sebastian Raschka, being a pro, was splitting up the data properly :-)



There was also a simple smoke test -- how does the model predict that the phrase
    
    
    Every effort moves you
    

...should continue?

I should do the same three tests here.

#### Smoke test

[A simple autoregressive generation script](https://github.com/gpjt/ddp-base-model-from-scratch/blob/a9167188d4a64762bfb3d45624f6677cabff9efd/test_smoke.py) is easy enough to knock together, and:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_smoke.py runs/8xa100m40/model.json runs/8xa100m40/checkpoints/best/model.safetensors
    Every effort moves you toward finding more fun stuff,â Geller explains.
    âWe love the music because
    

All we're looking for here is basic coherency, and I think this is good enough to pass that filter.

#### Loss tests

Next, the loss-style testing. What I think I want to be able to do here is just take a `model.safetensors` file and run an eval against a standard dataset.

I did not generate my own test set, but I did generate a much-larger-than-necessary eval set, 1% of both FineWeb and FineWeb-Edu -- that's 100 million tokens or so in both cases.

In the validation that I was doing during the train just now, I did 300 batches of 1,024 tokens with a micro-batch size of 13. That only ran on the rank 0 process, so that's

300×13×1,024=3,993,600tokens

Not even 4% of the validation data.

Now, for the local eval, I think it makes sense to make it run for about five minutes \-- that's just for my own convenience, I don't want to spend very long -- and I know from the previous local train that I can do 3,200 batches of six 1,024-token sequences in that time:

3,200×6×1,024=19,660,800tokens

So, somewhat arbitrarily, let's use the 19,660,800 tokens starting at position 50,000,000 in the FineWeb validation dataset for our tests -- they'll never be used for training or validation during the training loop. It's kind of a hack, but it'll do for now.

[Here's the code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/80fb517ef91785644264b5eddb14d88455fa29da/test_loss.py). It should be easy enough to understand; it did require one tweak to our existing `load_dataset` function, though:

Originally, that function worked out out the actual number of tokens to use by working out the size of each global batch, dividing our requested minimum number of tokens by that size and taking the floor, adding on one, then multiplying that by the global batch size.

That works fine in cases where the `min_tokens` is not a multiple of the global batch size -- it gives us a round number of batches that contains at least `min_tokens`. But if `min_tokens` is already a multiple of the global batch size, it gives us an extra batch at the end. So I added that as a special case in `load_dataset` to avoid that.

Anyway, running that gives us a loss:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets runs/8xa100m40/model.json runs/8xa100m40/checkpoints/best/model.safetensors
    Fetching 4 files: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 588.84it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [05:05<00:00, 10.49it/s]
    Loss against our test dataset: 3.674
    

That's actually quite a lot lower than we were seeing with the locally-trained models on the test dataset I was using then -- but, of course, it's a different dataset so it's not strictly comparable.

Let's run the same test against them:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets ~/Dev/llm-from-scratch/big-train-model-conf.json ~/Dev/llm-from-scratch/big-train-checkpoints-fw/best/model.safetensors
    Fetching 4 files: 100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 3069.94it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [04:56<00:00, 10.79it/s]
    Loss against our test dataset: 3.944
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets ~/Dev/llm-from-scratch/big-train-model-conf.json ~/Dev/llm-from-scratch/big-train-checkpoints-fw-edu/best/model.safetensors
    Fetching 4 files: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 979.35it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [04:55<00:00, 10.83it/s]
    Loss against our test dataset: 4.167
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets ~/Dev/llm-from-scratch/big-train-model-conf.json ~/Dev/llm-from-scratch/big-train-checkpoints-fw-edu-2x/best/model.safetensors
    Fetching 4 files: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 832.12it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [04:54<00:00, 10.87it/s]
    Loss against our test dataset: 4.135
    

That's really interesting! Those numbers are really close to the numbers I got in the last post. That does make some kind of sense, though -- while the numbers aren't strictly comparable, as I said, both the dataset that I was using then and the one I'm using now are essentially random stuff from FineWeb, so I guess they must be more similar than I thought.

But, importantly, the loss on the newly-trained model is much lower -- 3.674 rather than > 3.9 for all three of the older locally-trained models.

Now, the only big difference between this training run and the ones that I did locally is the batch size. As I said in the last post, while I felt that the difference between my batch size of six and the (reported) batch size of 512 for the original GPT-2 was the least-likely cause of the differences in the results, Gemini told me that it thought it was the most likely cause.

It looks like Gemini (and, I should note, [`spi` on Hacker News](https://news.ycombinator.com/item?id=46205589)) might have been right! Batch size is super-important.

Let's do the same eval with the OpenAI weights. I wrote a quick script (in my old 'LLM from scratch' repo, which has the code used in the book) to [load up the GPT-2 weights and save them as a safetensors file](https://github.com/gpjt/llm-from-scratch/blob/c939774754f3b8ee42c1490f53ade2b77433e548/convert_openai_weights_to_safetensors.py).

When I ran that, I got an interesting error:
    
    
    ValueError: You are trying to save a non contiguous tensor:
    ``trf_blocks.0.att.W_query.weight`` which is not allowed. It either means you are
    trying to save tensors which are reference of each other in which case it's
    recommended to save only the full tensors, and reslice at load time, or simply
    call ``.contiguous()`` on your tensor to pack it before saving.
    

That was easy enough to fix; in the book's code we assign the weights that have been loaded from the OpenAI TensorFlow checkpoint files with a function called `assign` that looks like this:
    
    
    def assign(left, right):
        if left.shape != right.shape:
            raise ValueError(
                f"Shape mismatch.  Left: {left.shape}, Right: {right.shape}"
            )
        return torch.nn.Parameter(torch.tensor(right))
    

Just adding a call to `contiguous` to the last line fixed the error:
    
    
        return torch.nn.Parameter(torch.tensor(right).contiguous())
    

...and as a result, I had safetensors files for the original OpenAI models:
    
    
    (llm-from-scratch) giles@perry:~/Dev/llm-from-scratch (main)$ ls -lrt
    ...
    -rw-r--r--  1 giles giles        731 Dec  9 18:57 convert_openai_weights_to_safetensors.py
    -rw-r--r--  1 giles giles        160 Dec  9 19:00 openai-weights-gpt-medium.json
    -rw-r--r--  1 giles giles        159 Dec  9 19:01 openai-weights-gpt-small.json
    -rw-r--r--  1 giles giles       4452 Dec  9 19:10 download_and_use_gpt2.py
    drwxr-xr-x  2 giles giles       4096 Dec  9 19:10 __pycache__
    -rw-r--r--  1 giles giles 1725850968 Dec  9 19:10 gpt-2-medium.safetensors
    -rw-r--r--  1 giles giles  702501224 Dec  9 19:14 gpt-2-small.safetensors
    

So now we can run our test against them:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets ~/Dev/llm-from-scratch/openai-weights-gpt-medium.json ~/Dev/llm-from-scratch/gpt-2-medium.safetensors
    Fetching 4 files: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 804.24it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [12:41<00:00,  4.20it/s]
    Loss against our test dataset: 3.231
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets ~/Dev/llm-from-scratch/openai-weights-gpt-small.json ~/Dev/llm-from-scratch/gpt-2-small.safetensors
    Fetching 4 files: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 687.84it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [04:53<00:00, 10.89it/s]
    Loss against our test dataset: 3.500
    

Excellent. Let's start putting together a table of these results:

| Test loss  
---|---  
OpenAI weights: medium | 3.231  
OpenAI weights: small | 3.500  
Cloud FineWeb, 8x A100 40 GiB | 3.674  
Local FineWeb train | 3.944  
Local FineWeb-Edu extended train | 4.135  
Local FineWeb-Edu train | 4.167  
  
That's pretty amazing. Having a batch size of 13 micro-batches over eight GPUs, or 104 in total, seems to have massively improved the model -- it's much closer to the original weights. It will be interesting to see whether I get further improvements when I move to the larger machines, which (due to having more VRAM) will have larger possible micro-batches, so we'll get larger global batch sizes.

It certainly makes me think that I could have got much better results locally by using gradient accumulation, which would mimic the effects of a larger batch size by running multiple smaller batches through, without doing an optimiser step each time, then doing one big update once enough has gone through.

But all of that is for another day. Let's try the instruction fine-tuning test now.

#### Instruction fine-tuning

I decided to pretty much re-use my adapted version of the code from the book; that meant that I was borrowing quite a lot of Raschka's code, which he has [released under the Apache 2 license](https://github.com/rasbt/LLMs-from-scratch/blob/main/LICENSE.txt). I normally use the MIT license for my code, but I'm not married to it, so I relicensed the whole repo as Apache 2 with some specific headers to say which parts came from "Build a Large Language Model (from Scratch)", and added [this code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/77ab971c5830a8f4827c1e485267915690871b0f/test_ift.py).

It downloads the Alpaca dataset from the site for the book, splits it into train/validation/test splits, trains on the training set, evaluating each epoch and bailing out (and restoring the previous epoch's weights) when validation loss starts rising, and then runs through the test set generating responses, and then sends them all off to the OpenAI API for GPT-5.1 to judge them.

Running it against our new model gets a score of 17.09. Let's try the various other models and build out our table:

| Test loss | Instruction fine-tune score  
---|---|---  
OpenAI weights: medium | 3.231 | 38.53  
OpenAI weights: small | 3.500 | 22.98  
Cloud FineWeb, 8x A100 40 GiB | 3.674 | 17.09  
Local FineWeb train | 3.944 | 16.01  
Local FineWeb-Edu extended train | 4.135 | 14.55  
Local FineWeb-Edu train | 4.167 | 16.86  
  
Interesting! In the last run, [I found](/2025/12/llm-from-scratch-28-training-a-base-model-from-scratch#but-why-is-our-model-worse-than-openais) the instruction fine-tune numbers came out as FineWeb-Edu extended > FineWeb > FineWeb-Edu, but here we have FineWeb-Edu > FineWeb > FineWeb-Edu extended -- exactly the opposite!

I do have to wonder, though, how precise a measure this is. While the training should be fairly consistent (though I don't have a random seed in there to enforce it), the fact that we're using an LLM as a judge means that there is an element of randomness coming in here. Indeed, I re-ran the FineWeb-Edu extended train test again, just to see what I got, and it came up with an even-worse 12.12.

So I don't think we can read a huge amount into these numbers -- well, unless we can get the numbers significantly up. While it looks like a 2.5-point difference might just be randomness, I doubt that a 10-point difference could be.

I think we've done the tests that we need for this model now, and we have a testing procedure in place. So let's train some further models on different instance sizes, and gather numbers.

### Training on an 8x B200 with 160 GiB per GPU, using SXM6

This is the biggest machine available on Lambda Labs right now, and is only sporadically available; one happens to be there now, so let's to give it a go. First, we need to create the [runs/8xb200m160](https://github.com/gpjt/ddp-base-model-from-scratch/tree/main/runs/8xb200m160) directory, initially with a `train.json` that is a clone of the one I did for the last train, `8xa100m40`, then spin up the machine.

#### The train

As before, we need to log in, clone the repo, then in it run the [`setup_lambda.sh`](https://github.com/gpjt/ddp-base-model-from-scratch/blob/30a3fd75f1eab96cd598a6c0a0f14465ddee6ae4/setup_lambda.sh) script, run `uv sync`, and try to run the script:
    
    
    uv run torchrun --nproc_per_node=8 ddp_train.py 8xb200m160 datasets
    

It crapped out because there was no datasets directory, which is an annoyance. We should create it if it doesn't exist.

Create the directory, and run it again. It took a while to download the dataset, because every per-GPU process downloads it separately. That only took a minute or two, but it was a waste of time; I think we should only download it from the rank 0 process with some barriers to make the other processes pause.

Next, we need to do a binary chop on the micro-batch size, starting with a low of 13 (which I know will be fine because it worked on the 40 GiB GPUs that we used last time), and a high of 100 (fairly random, just something I'm pretty sure will fail).

While doing that, a few things are standing out, both to do with validation. When the script starts, it does one training iteration, then goes straight into validation. Then it starts the training run proper. However:

  * If we're going to do validation then it does make some sense to do one at the start -- but doing one training iteration first seems kind of arbitrary (though it's clear how that drops out of the existing code).
  * The validation runs on this machine are taking longer than they were on the less-powerful A100 GPUs! That confused me for a bit, until I realised that I didn't notice that it was slower with the batch-size 13 test, only with the larger ones later in in the binary chop. If we're using larger batches, then there's more work to do for the validation.
  * Doing this binary chop by hand is annoying and error-prone, and worse, we have to wait for one of those (long) validation runs before we get into proper training. The initial training iteration can succeed, while later ones hit memory limits -- it seems like we need to wait for three or four training iterations before we can be sure that we have a workable batch size. Not quite sure why that is, perhaps it's something in the optimiser or the scaler?



We're going to need to work out some kind of fix for that, because it's taken me 17 minutes from spinning up the machine to getting a size for our micro-batches -- which happens to be 64. On a machine that costs US$39.92/hour, that's an expensive test! We'll look into that later.

Anyway, a batch size of 64 is pretty neat, as with 8 GPUs, that means we have a global batch size of 512 -- exactly the same as in the original GPT-2 paper!

So, let's kick off the train. It takes about 7 minutes to get to the first checkpoint, at which point it's averaging 801,221 tokens/second. That pattern repeats, and with about one minute to do the validation, we're spending about 12.5% of the time on this machine validating. Hmm. A further indication that we might want to remove the validation stuff if it's not adding on any value.

Eventually, it finishes:
    
    
    Training complete in 4,190.357 seconds
    Tokens seen: 3,260,547,072
    Throughput: 778,107 tokens/second
    Final train loss: 3.865
    Final val loss: 3.770
    

So, that's 1h9m50s. The final validation loss is not as good as the previous run on the 8x A100 40 GiB machine, where we got down to 3.675. Given that we're using the same validation dataset as the previous, that's meaningful: this is not as good a model, it seems.

Again, latest and best checkpoints are the same one:
    
    
    ubuntu@129-213-85-212:~/ddp-base-model-from-scratch$ ls -lrt runs/8xb200m160/checkpoints/
    total 64
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:05 20251210Z170527-iteration-0
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:07 20251210Z170712-iteration-0
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:08 20251210Z170848-iteration-0
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:10 20251210Z171043-iteration-0
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:12 20251210Z171231-iteration-0
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:19 20251210Z171914-iteration-617
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:26 20251210Z172557-iteration-1234
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:32 20251210Z173241-iteration-1851
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:39 20251210Z173924-iteration-2468
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:46 20251210Z174608-iteration-3085
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:52 20251210Z175251-iteration-3702
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 17:59 20251210Z175935-iteration-4319
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 18:06 20251210Z180619-iteration-4936
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 18:13 20251210Z181302-iteration-5553
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 18:19 20251210Z181945-iteration-6170
    lrwxrwxrwx 1 ubuntu ubuntu   30 Dec 10 18:21 latest -> 20251210Z182116-iteration-6218
    lrwxrwxrwx 1 ubuntu ubuntu   30 Dec 10 18:21 best -> 20251210Z182116-iteration-6218
    drwxrwxr-x 2 ubuntu ubuntu 4096 Dec 10 18:21 20251210Z182116-iteration-6218
    

So we can download everything:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xb200m160 (main)$ scp ubuntu@129.213.85.212:/home/ubuntu/ddp-base-model-from-scratch/runs/8xb200m160/big-training-run-chart.png .
    big-training-run-chart.png                                                                                                              100%   75KB 149.0KB/s   00:00
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xb200m160 (main)$ scp -r ubuntu@129.213.85.212:/home/ubuntu/ddp-base-model-from-scratch/runs/8xb200m160/checkpoints/best ./
    big-training-run-chart.html  big-training-run-chart.png   model.json                   train.json
    giles@perry:~/Dev/ddp-base-model-from-scratch/runs/8xb200m160 (main)$ scp -r ubuntu@129.213.85.212:/home/ubuntu/ddp-base-model-from-scratch/runs/8xb200m160/checkpoints/best ./
    meta.json                                                                                                                               100%  100     0.5KB/s   00:00
    optimizer.pt                                                                                                                            100% 1244MB  12.2MB/s   01:42
    scaler.pt                                                                                                                               100% 1383     4.9KB/s   00:00
    model.safetensors                                                                                                                       100%  670MB  12.7MB/s   00:52
    

...and here's the training chart:

![Training run on an 8x B200 with 160 GiB/GPU](/post-assets/llm-from-scratch-29-ddp-training-a-base-model-in-the-cloud/training-run-8xb200m160.png)

OK, so that's smoother than the last one -- no loss spikes. Maybe the larger batch size smoothed them?

Let's think a bit about the cost of this train.

#### Cost

From Lambda Labs, we had that machine running for a little over 1h30m. At US$39.92/hour, the total cost was US$60.25.

Yikes. So, knocking off the 1h10 or so for the train, we have 20m to allow for -- which matches up quite well to the 17 minutes of fiddling with batch sizes, and then 3 minutes to download all of the files.

If this blog post isn't going to cost significantly more than it needs to, we need to get that down. Of the US$60.25, just over US$13 was spent on identifying the batch size. Only US$46.57 was spent on the train itself.

We also did 11 validation runs as part of that; at a minute each, those cost US$7.32. So, excluding validation, we're below US$40 for the train.

#### Evals

Now, let's run our tests. First, the smoke test: we get this:
    
    
    Every effort moves you to give something back. You will only make sure to check what you find on all other website for
    

"...on all other website for..." is a bit rubbish. Still, on to the loss:
    
    
    Loss against our test dataset: 3.771
    

That's in line with the training loss -- worse than the loss I got with the one trained on the smaller machine, with its corresponding smaller batch size, but still better than any of our local trains. Still interesting, though -- larger batches are not guaranteed to get bigger results. More investigation needed there!

On to the instruction fine-tuning test. That gives us a score of 13.89 -- the worst that we've seen yet!

I think I'll put together a full table including these results later; I want to try training on some other, differently sized machines first, and we can aggregate the results at the end.

But before we do that, let's make some changes to the scripts to fix some of those QoL issues we encountered in that last train.

### QoL fixes to the script

The first irritation was that it errored out saying that `datasets` was not a directory when it didn't exist. The script takes a datasets directory as one of its command-line options, and it's reasonable that it checks that it really is a directory (rather than, say, a file or a symlink):
    
    
        datasets_dir = Path(datasets_dir_path)
        if not datasets_dir.is_dir():
            raise Exception(f"{datasets_dir_path} is not a directory")
    

...but if it doesn't exist, it might as well create it first. Now, I could just put this before the `is_dir` check:
    
    
        if not datasets_dir.exists():
            datasets_dir.mkdir()
    

...but remember, this code is run by multiple processes -- so they could easily trip over a race condition here.

What I want is to have just one of them do this; I've deemed the rank 0 process the "special" one for validation, printing the progress bar, and so on, so we may as well treat it that way here.

But -- there's a difference! Rank zero is the one that should be printing stuff out, it's true. And right now, we only have one node participating in this train. But I do want to avoid simple errors that would make it hard to run multi-node in the future.

Now, if we have multiple nodes, then each one will have its own filesytem (unless we're using NFS or something like that), so we'll need a separate "datasets" directory for all of them. What we want is to do these checks on one process on each node.

Usefully, we have the `local_rank` variable that is defined earlier in `main`, which is per-node. Again, let's imagine we have two nodes with two GPUs each. Node 0 might be runnning the processes with global rank 0 and 1, and node 1 might have global ranks 2 and 3. On node 0, the processes would have local ranks 0 and 1 respectively, but on node 1, they'd also be local ranks 0 and 1.

So, the full code becomes this:
    
    
        datasets_dir = Path(datasets_dir_path)
        if local_rank == 0:
            if not datasets_dir.exists():
                datasets_dir.mkdir()
        dist.barrier()
        if not datasets_dir.is_dir():
            raise Exception(f"{datasets_dir_path} is not a directory")
    

Note the barrier; we don't want the other processes to check whether `datasets_dir` is a directory until the local rank 0 process has had a chance to create it.

(Of course, if we were running this on a setup where all of the nodes shared a filesystem, it wouldn't work -- in that case we'd want to use the global rank that we can get from `dist.get_rank()` instead. But we can burn that bridge if we ever come to it ;-)

Phew, that was a bit more work than I expected! But it sets us up nicely for the next QoL fix on my to-do list.

I don't like the fact that every process downloaded the whole dataset. The `huggingface_hub.snapshot_download` actually handled it pretty gracefully -- none of the processes tripped over any of the others. Indeed, it looks like there was some kind of global queueing going on, so they downloaded it one after the other.

But it did take time -- maybe a minute or two in total, and with the clock ticking on that ~US$40/hour machine, that felt a bit stress-inducing.

So: I think it would be best to only do that from the rank 0 process as well.

The code that downloads the dataset is just after the bit we've been looking at:
    
    
        dataset_dir = download_dataset(datasets_dir, train_conf["dataset"])
    

...and `download_dataset` looks like this:
    
    
    def download_dataset(datasets_dir, dataset_name):
        download_path = snapshot_download(
            f"{dataset_name}",
            repo_type="dataset",
            local_dir=datasets_dir / dataset_name,
            allow_patterns="*"
        )
        return Path(download_path)
    

Now, the docs for [`huggingface_hub.snapshot_download`](https://huggingface.co/docs/huggingface_hub/v1.2.2/en/package_reference/file_download#huggingface_hub.snapshot_download) say that the `local_dir` parameter is:

> If provided, the downloaded files will be placed under this directory.

...and the return value is this:

> Returns
> 
> `str` or list of `DryRunFileInfo`
> 
>   * If `dry_run=False`: Local snapshot path.
>   * If `dry_run=True`: A list of DryRunFileInfo objects containing download information.
> 


We happen to be passing in a `Path` object for `local_dir`, and we're not in `dry_run` mode -- it defaults to `False`. So all we're doing by returning that `download_path` wrapped in a `Path` object is a slightly indirect way of returning the path `datasets_dir / dataset_name` that we're passing in as `local_dir`.

For tidiness, I really want to gate the call to `download_dataset` in `main` with the same rank stuff as we did for the directory creation. So, let's change the setup so that `download_dataset` takes the path to the directory where we want this specific dataset to be, not the generic "all datasets" directory. And given that we're now passing this specific path into the function, we don't need to return it:
    
    
    def download_dataset(dataset_dir, dataset_name):
        snapshot_download(
            f"{dataset_name}",
            repo_type="dataset",
            local_dir=dataset_dir,
            allow_patterns="*"
        )
    

Now it's just a wrapper around a single call to `snapshot_download`, which I'm not entirely sure about (it's a code smell that I'm probably creating an unnecessary level of abstraction) but I think I'm happiest leaving it that way for now, as it does hide away a bit of messiness in the HF hub API. 3

That means that we can now combine the directory-checking logic that we fixed above with download-on-local-rank-zero-only code like this:
    
    
        datasets_dir = Path(datasets_dir_path)
        dataset_name = train_conf["dataset"]
        dataset_dir = datasets_dir / dataset_name
        if local_rank == 0:
            if not datasets_dir.exists():
                datasets_dir.mkdir()
            if not datasets_dir.is_dir():
                raise Exception(f"{datasets_dir_path} is not a directory")
            download_dataset(dataset_dir, dataset_name)
        dist.barrier()
    

[Here's the updated code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/6851ce9b403204477758faa2e14f99061fc25504/ddp_train.py) with those fixes.

Now, let's move on to validation. I'm increasingly of the opinion that the validation steps are just adding on to the cost without much in the way of benefit.

Additionally, the validation is taking a different amount of time for each batch size, and happen a different number of times in each train -- remember, it's `validation_batches` batches every `validation_interval` global steps, and the batch size varies based on the micro-batch size, which is different for different amounts of GPU VRAM, and the total number of global steps in a train _also_ varies based on the size of each batch.

So that means that if we want to compare apples to apples in any final comparison of the time and money cost of training models on different kinds of Lambda Labs machines, we'll want to exclude the validation cost -- once we've settled on a machine type, we're going to want to fine-tune the validation size for that in much more detail than I have to date, assuming we don't drop it entirely.

However: I'm loath to make such a fundamental change halfway through this comparison. It's tightly coupled to the checkpointing code, and the charting code, and so on. So I think that for this post, I'm just going to keep it there, and keep track of how much time (roughly) we're spending on each validation step for each train, so that we can remove it and get a "pure" train-time only comparison between the different kinds of machines.

It's not pretty, but I think it's better than changing horses mid-stream.

On the other hand, the validation is a real pain when doing the binary chop to find out the maximum micro-batch size for our VRAM before we start the training run. That's because we have to wait for one validation to run before we get into the full training loop, which makes it slower. On top of that, having to do a manual binary chop is a PITA.

What I think would be a true QoL improvement for the future trains is something that does the binary chop for us, using a dummy training loop. We run it once on each new machine type, get a micro-batch size to plug into our training parameters, and then let it rip,

This will re-use so much of the code from the training script `ddp_train` that I think it actually is just an alternative way of running it.

After a bit of hacking, I came up with [this updated code](https://github.com/gpjt/ddp-base-model-from-scratch/blob/d2a7b694ff217a4ca0ade8267776a87816c58825/ddp_train.py) \-- the [diff](https://github.com/gpjt/ddp-base-model-from-scratch/commit/d2a7b694ff217a4ca0ade8267776a87816c58825) is a bit hairy, but essentially:

  * I updated the `train` function so that it takes flags to tell it whether or not to do validation (default true) and an optional maximum number of steps, which is `None` by default. With those default values, it does exactly the same as before, of course.
  * I created a `load_datasets_and_train` function, which does all of the dataset-loading stuff that the original `main` function did, and then calls `train` with a `DDP`-wrapped model. So that maintains the current flow.
  * Next, I added a `--find-max-microbatch-size` flag to the script; if that's not set, it just calls `load_datasets_and_train`.
  * However, if it is set, it instead calls a new `binary_chop_batch_sizes` function, which determines the largest batch size we can fit onto the current hardware for the current run, and (on the rank 0 process only, to avoid log spam), prints it out.
  * `binary_chop_batch_sizes` does what it says on the tin; it confirms that we can train with batch size of 1, and that we can't with batch size 70 (chosen because the limit was 64 on that massive B200 machine), then chops between them to find the largest batch size that doesn't OOM.
  * It uses `check_batch_size_works` for that -- that just constructs a dataset with the appropriate batch size, then runs a three-step train with no validation to see if it raises an OOM. PyTorch rather messily just raises a generic `RuntimeError` for those, but we can look inside the exception's message to see if it is an OOM.



That takes just over six seconds to find the correct batch size on my local machine; with multiple GPUs, I expect it will be slower (there's a spinup overhead to start all of the per-GPU processes), but I'm sure it won't be as bad as the manual binary chops with validation that I was doing, and will be less error-prone.

Right! We've done some QoL stuff, let's try another machine size on Lambda Labs :-)

### Training on an 8x H100 with 80 GiB per GPU, using SXM5

These are the machines that Andrej Karpathy is recommending for training nanochat, so let's see how we do with them. They cost US$23.92/hour; let's see how it works out.

#### The train

Here are the steps:

  1. Create the `8xh100m80` run file, commit and push.
  2. Spin up the machine. On it:
  3. Clone the repo
  4. `setup_lambda.sh`
  5. `uv sync`



Now let's download our dataset and find our micro-batch size:
    
    
    ubuntu@192-222-52-220:~/ddp-base-model-from-scratch$ uv run torchrun --nproc_per_node=8 ddp_train.py 8xh100m80 datasets -f
    ...
    Max microbatch size was 27
    

That took less than a minute to run -- nice! Now we can put that micro-batch size in `train.json`. It does seem a little small -- after all, we could fit a batch of 64 into 160 GiB -- but I'll do some analysis later.

Actually, before we kick off the train, let's see how long all of the preparatory steps took to run before we can do that -- not just the micro-batch-size script, but also the installation of the dependencies, the clone, and any overhead from boot time etc:
    
    
    ubuntu@192-222-52-220:~/ddp-base-model-from-scratch$ uptime
     22:37:19 up 5 min,  2 users,  load average: 1.38, 1.51, 0.69
    

Five minutes total. Not bad.

Let's start the train:
    
    
    ubuntu@192-222-52-220:~/ddp-base-model-from-scratch$ uv run torchrun --nproc_per_node=8 ddp_train.py 8xh100m80 datasets
    

The initial validation run took 38 seconds, and then we started off. At 4m37s in, we get the first real validation run; at that point, it's running at 493k tokens/second.

Eventually, it finishes, having taken about 1h50 including all of the validations.
    
    
    Training complete in 6,650.197 seconds
    Tokens seen: 3,260,252,160
    Throughput: 490,249 tokens/second
    Final train loss: 4.091
    Final val loss: 3.729
    

Here's the training chart:

![Training run on an 8x H100 with 80 GiB/GPU](/post-assets/llm-from-scratch-29-ddp-training-a-base-model-in-the-cloud/training-run-8xh100m80.png)

Two things stand out here:

  1. We had two nasty loss spikes.
  2. As a result of the second of those, the best iteration as per validation loss is not the last one.



Further evidence that gradient clipping is likely to be an excellent addition to our training loop! It's also worth noting that the train loss spikes at the same time as the validation loss, so getting rid of the latter would still allow us to get a "best" checkpoint to compare with the latest at the end of the train.

#### Cost

The machine was up and running for 2h9m, costing US$23.92/hour, for a total cost of US$51.47.

The train took 6,650.197 seconds, so about 1h50m. Allowing for five minutes setup time, that's 1h55m accounted for. There's an extra 14m there -- that was because downloading those two checkpoints to my machine took quite a long time due to local network issues. Might want to look into ways to avoid that later.

And for later cost-accounting purposes, we should note that it took 38 seconds or so for each validation run, and we can see on the chart that there were 24 of them.

#### Evals

So, firstly, let's give our two models -- the best one and the latest one -- a smoke test:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_smoke.py runs/8xh100m80/model.json runs/8xh100m80/checkpoints/best/model.safetensors
    Every effort moves you forward, and you will not regret it.
    But if something comes in, you may ask the
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_smoke.py runs/8xh100m80/model.json runs/8xh100m80/checkpoints/latest/model.safetensors
    Every effort moves you in the future; in many cases you can't afford the most costly replacement.<|endoftext|>The following list
    

Both of those look OK! Now let's try the loss test. I started running it, but when it started downloading the dataset, I realised that it needed [updating to allow for the changes I made to `download_dataset`](https://github.com/gpjt/ddp-base-model-from-scratch/commit/bd4f14cd1e323434561b35edebe4bce71c5e4b37) \-- ooops! That done, let's give it a run for both of our models:
    
    
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets runs/8xh100m80/model.json runs/8xh100m80/checkpoints/best/model.safetensors
    Fetching 4 files: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 810.61it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [04:54<00:00, 10.88it/s]
    Loss against our test dataset: 3.725
    giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ uv run test_loss.py datasets runs/8xh100m80/model.json runs/8xh100m80/checkpoints/latest/model.safetensors
    Fetching 4 files: 100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 4/4 [00:00<00:00, 1719.15it/s]
    Download complete: : 0.00B [00:00, ?B/s]                                                                                                            | 0/4 [00:00<?, ?it/s]
    100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 3200/3200 [04:53<00:00, 10.89it/s]
    Loss against our test dataset: 3.734
    

As you'd expect, the best checkpoint has somewhat better loss, at 3.725, than the last one, with 3.734. Once again, better than our local trains, but not quite as good as the result with the first cloud train on that 8x A100 40 GiB machine, which was 3.674. Again, I'll put together a table comparing all of these results at the end.

Does that make any real difference with the instruction fine-tune test? The test prints a lot out, but the headline numbers:

  * Best checkpoint: 4 epochs of fine-tuning, and a score of 11.98 -- another record low! Amusingly, it confidently said "The author of 'Pride and Prejudice' is Sarah Palin".
  * Latest checkpoint: 5 epochs of fine-tuning, and a rather good score of 17.91.



So that was interesting! However, I am getting ever less convinced that the IFT test is a useful one; the randomness of the LLM-as-a-judge responses means that I don't think it can be consistent.

Perhaps a better way to do this would be to batch up all of the models, and then give GPT5.1 answers from "model A", "model B", and so on all in one query, and then to ask it to give them scores all at the same time. That would hopefully make things at least a bit more consistent. Something to ponder later, I think.

In the meantime, one extra thing I wanted to dig into before going on to the last train for this post:

### Batch size scaling

I mentioned that I thought that the batch size for that last run, 27, was a bit small considering that we'd managed to fit a size of 64 into the 160 GiB/GPU machine. But after thinking about it for a bit, it occurs to me that during my experiments doing fine-tuning, I came to the conclusion that [memory use scaled linearly with batch size](/2024/08/fine-tuning-8), with a fixed amount per element in the batch (the activations for the model for that batch element), plus an overhead (the model itself, the optimiser, and perhaps other stuff).

We have batch sizes for:

  * 24 GiB locally, which was 6
  * 40 GiB in the first train in this series, which was 13
  * 80 GiB in the last one, giving us 27
  * 160 GiB in the one on the huge machine, giving us 64



Now, that is slightly messy data because each memory "measurement" is the size of the card's VRAM, not the amount of VRAM we actually used -- there might have been anything from zero to just less than one extra batch element's worth of "spare" space -- but we can see what we get with a simple linear regression:
    
    
    >>> import numpy as np
    >>> xs = np.array([6, 13, 27, 64])
    >>> ys = np.array([24, 40, 80, 160])
    >>> a, b = np.polyfit(xs, ys, 1)
    >>> print(a, b)
    2.3461346633416458 11.481296758104722
    

And if we plot that, we get this:

![Batch size vs GPU VRAM linear regression](/post-assets/llm-from-scratch-29-ddp-training-a-base-model-in-the-cloud/micro-batch-size-scaling-chart.png)

Nice! That fits really well. So we have an overhead of about 11.5 GiB, then about 2.35 GiB per batch element on top of that.

That is, of course, somewhat sad news for anyone trying to repro this on a GPU with 12 GiB -- looks like it would be _just_ too small to even fit in a single-element batch after the overhead :-(

Anyway, that's been a bit of a side quest. Let's try our last machine size for what has (once again) turned into a bit of a monster of a blog post...

### Training on an 8x A100 with 80 GiB per GPU, using SXM4

This is the same kind of instance as the first train in this post, except that it has double the VRAM per GPU. Let's see what we can do with it.

#### The train

Once again, we create the `8xa100m80` run file, commit and push, then spin up the machine. On it, we clone the repo, run `setup_lambda.sh` then `uv sync`.

Next, we can find our micro-batch size:
    
    
    ubuntu@192-222-52-220:~/ddp-base-model-from-scratch$ uv run torchrun --nproc_per_node=8 ddp_train.py 8xa100m80 datasets -f
    ...
    Max microbatch size was 28
    

Interesting, we managed to squeeze an extra one in compared to the H100's batch size of 27, despite having exactly the same amount of VRAM! Not sure what might have caused that.

It took 4 minutes to get to this point, so let's get that batch size into the config and kick off the run. The initial validation takes 1m06s, which is consistent throughout the train. The first real val run at 8m15s in, and the estimated train time is 2h35m, with a tokens-per-second of 286,188.

At the end:
    
    
    Training complete in 11,532.620 seconds
    Tokens seen: 3,260,350,464
    Throughput: 282,707 tokens/second
    Final train loss: 3.771
    Final val loss: 3.723
    

Again, the latest and the best global steps are the same (despite some loss spikes):

![Training run on an 8x A100 with 80 GiB/GPU](/post-assets/llm-from-scratch-29-ddp-training-a-base-model-in-the-cloud/training-run-8xa100m80.png)

...so we just need to download that and shut down the machine.

How much did that cost us?

#### Cost

The machine was running for 3h25m, costing US$14.32 / hour, for a total of US$48.76.

Our train took 11,532 seconds, which is 3h12m, and our setup took about 4 minutes -- maybe five including the time required to update the train config with the micro-batch size, so we have 7 minutes on top of that, which is about the amount of time it took to download the model.

Let's run some evals!

#### Evals

Our smoke test gives us this:
    
    
    Every effort moves you up the hill for a full day.
    âWe donât know anyone who looks
    

Coherent enough, I think! Now the loss on our test dataset; it comes out as 3.730, so pretty similar to our other cloud trains, apart from the oddly-low one on the 40 GiB GPUs.

Now let's see what GPT-5.1 thinks of the instruction fine-tuned version. It only needs two epochs of fine-tuning, and believes that "The author of 'Pride and Prejudice' is 'Pride and Prejudice'", which is not promising, and gets a score in the same kind of range as the other models, 11.71.

So: we've trained four models on four different machine sizes. Let's see how they stack up against each other, against our locally-trained models, and the original OpenAI GPT-2 weights.

### The results

So, I've trained four of my 163M-parameter GPT-2 models, using almost exactly the same dataset \-- the Chinchilla-optimal number of tokens, rounded up to make an even number of batches. I did this on four different multi-GPU machines on Lambda Labs:

  * An 8x A100 40 GiB
  * An 8x A100 80 GiB
  * An 8x H100 80 GiB
  * An 8x B200 160 GiB



#### Evals

I've done some evals on each of the models, so let's put those results together in one table -- results for the trains in this blog post, alongside those for the original OpenAI GPT-2 weights, both small and medium, and for the models I got when training locally.

For all models, I've provided:

  * The loss on my test set.
  * The results it got on an instruction fine-tune test based on Sebastian Raschka's.
  * The global batch size (that is, for single GPU runs, just the batch size, but for the multi-GPU ones, where each batch is made up of per-GPU micro-batches, the per-GPU batch size times the number of GPUs). 4



I've sorted the models in order of increasing loss on the test set -- so, the best model by that measure is first.

| Test loss | IFT score | Batch size  
---|---|---|---  
OpenAI weights: medium | 3.231 | 38.52 | 512  
OpenAI weights: small | 3.500 | 22.98 | 512  
Cloud FineWeb, 8x A100 40 GiB | 3.674 | 17.09 | 104  
Cloud FineWeb, 8x H100 80 GiB | 3.725 | 11.98 | 216  
Cloud FineWeb, 8x A100 80 GiB | 3.734 | 11.71 | 224  
Cloud FineWeb, 8x B200 160 GiB | 3.771 | 13.89 | 512  
Local FineWeb train | 3.944 | 16.01 | 6  
Local FineWeb-Edu extended train | 4.135 | 14.44 | 6  
Local FineWeb-Edu train | 4.167 | 16.86 | 6  
  
The instruction fine-tune results are kind of all over the place, and I'll look into that later 5. For now, let's focus on the test loss. We have a pretty clear pattern, where the local trains are grouped together at around 4.0, and the cloud trains at around 3.7. For the local trains, as I noticed last time around, FineWeb is counter-intuitively _better_ than FineWeb-Edu.

There are two interesting things about the cloud trains:

  1. They're all consistently better than the local ones.
  2. The one on the _smaller_ machine is better than the ones on the larger ones; indeed, it looks like the larger the machine, the worse.



I think that what we're seeing here is that larger batches are better, but only up to a point. It's as if there's some kind of curve like this:

![Log batch size vs loss quadratic polynomial regression](/post-assets/llm-from-scratch-29-ddp-training-a-base-model-in-the-cloud/batch-size-fit.png)

I got that by taking the log of the batch size, then asking NumPy to do a polynomial regression -- that is, work out a, b and c so that the formula

y=ax2+bx+c

...fits it as well as possible:
    
    
    >>> import numpy as np
    >>> xs = np.array([104, 216, 224, 512, 6])
    >>> ys = np.array([3.674, 3.725, 3.73, 3.771, 3.944])
    >>> log_xs = np.log(xs)
    >>> a, b, c = np.polyfit(log_xs, ys, 2)
    >>> a, b, c
    (np.float64(0.03231264430524897),
     np.float64(-0.2957154034594081),
     np.float64(4.368745850428664))
    

It's kind of interesting that it's such a good fit with such an ad-hoc formula! We have a nice smooth curve hitting almost all of the points, and our optimal batch size looks like it's just a little below that 104 we managed with the smaller cloud machine, at about 97. But it's certainly not something that I'd like to read too much into. Best to treat it as purely illustrative: "it _might_ be something like this".

I think digging into that might be an interesting experiment at some later point. A bit of checking around the Internet (and a chat with ChatGPT) suggests that it's something people have looked into in some detail, unsurprisingly. An interesting point ChatGPT raised is that with our pretty much fixed "budget" of tokens -- we're always training on something close to the Chinchilla-optimal number -- then a larger batch size means that we're doing fewer optimiser steps.

Intuitively, that sounds like a problem. The larger batches mean that each move across the loss landscape is "better", or at least more stable. But we're doing fewer of those moves over the course of the train. There's obviously a tension between those two. You can imagine a degenerate case where the batch is so large you can fit the entire run into one iteration, so you do just one update of the parameters; that obviously wouldnât work very well.

Anyway, for the purposes of this post, let's flag it as interesting and move on. Let's take a look at costs.

#### Costs of training in the cloud

Here's another table for those -- for each cloud model, I've listed:

  * How long the training run took.
  * How much the machine cost per hour.
  * How much the training run cost.
  * How much of that was doing validation (which I'm now thinking is pointless on single-epoch trains like this).
  * How much it would have cost, and how long it would have taken if it had been run without validation.

| Train time (s) | Cost/hour (USD) | Train cost (USD) | Val runs | Per-val time (s) | Total val time (s) | Val cost (USD) | Cost ex val (USD) | Time ex val (s)  
---|---|---|---|---|---|---|---|---|---  
Cloud FineWeb, 8x A100 40 GiB | 13,904 | 10.32 | 39.86 | 50 | 30 | 1,500 | 4.30 | 35.56 | 12,404  
Cloud FineWeb, 8x H100 80 GiB | 6,650 | 23.92 | 44.19 | 24 | 38 | 912 | 6.06 | 38.13 | 5,738  
Cloud FineWeb, 8x A100 80 GiB | 11,532 | 14.32 | 45.87 | 24 | 66 | 1,584 | 6.30 | 39.57 | 9,948  
Cloud FineWeb, 8x B200 160 GiB | 4,190 | 39.92 | 46.46 | 11 | 60 | 660 | 7.32 | 39.14 | 3,530  
  
What do these numbers tell us, given what we were trying to do here?

### Conclusion

Like I said at the start, this was a pretty expensive learning experience: I wound up spending US$215.16 on Lambda Labs instances over the course of putting this all together. But it was worth it!

At the start of this post (if you can remember so far back), I said I wanted to achieve two things:

  1. I wanted to learn how to change a simple single-GPU training loop to make it multi-GPU.



Success!

  2. Could I get the training time for a full base model down from 48 hours to something more manageable -- and, hopefully, not too expensive?



Yes, absolutely. The trains I did, if we exclude the validation time, each cost between US$35.56 and US$39.14. In time, also excluding validation, the slowest ran for about 3h25m, and the fastest just less than an hour.

Now, in a future post I want to try making the changes that I listed [at the end of my last post](/2025/12/llm-from-scratch-28-training-a-base-model-from-scratch#but-why-is-our-model-worse-than-openais) to see if I can get the loss lower:

  * Removing dropout
  * Tweaking the learning rate (and maybe adding the warmup and cosine learning-rate decay stuff I've read about).
  * Reverting the architectural differences between our model and the original GPT-2: reintroducing weight tying between the token embeddings and the final linear layer, and also bias in the attention weights.
  * Trying full-fat 32-bit precision.
  * Fixing the exploding gradients issue with gradient clipping.



If I'm to do those, what I'll need to do is start with a baseline train on one particular size of machine, and then try introducing each change separately to see what happens to loss. I'll want to use a fixed seed for random number generation, so that I start with the same initial weights each time.

Given what these experiments have already shown about loss -- that the smallest, cheapest machine has better loss than the other more expensive ones due to what I assume is the batch size -- then that actually feels like exactly the right machine to choose for this. It does take a while to train anything, but three and a half hours is pretty acceptable, I think \-- I can do a train or two per day. An 8x A100 with 40 GiB VRAM per GPU is the way forward.

So: next steps. I want to:

  * Dig in to the instruction fine-tuning tests a little more -- as I've said above, I'm not 100% happy with how comparable it really is between models, at least given how I've been running it so far.
  * Upload the models we have to Hugging Face. I have a new motherboard ready for my PC, and replacing the old one has a risk that I might mess up and break the NVMe drive I have them stored on. I was holding off on this because it would mean sharing Raschka's GPT code, but having noticed that he's already licensed it all under the Apache license, I can release them under the same one.
  * Strip out the validation stuff. We can use training loss to track our progress, and losing evals during the train will help keep the cost down.
  * Finally, do the trains to see how each of the levers above affects loss.



This is going to be fun. Stay tuned!

[Here's a link to the next post in this series](/2026/01/llm-from-scratch-30-digging-into-llm-as-a-judge).

* * *

  1. I erroneously called this a "mini-batch" in earlier versions of this post and in the code -- fixed in [this commit](https://github.com/gpjt/ddp-base-model-from-scratch/commit/7f50aa4d86ff81699bbf4bb7fbb1931e0461cc8a). The code in this post reflects the correct terminology, but if you follow the links to the earlier versions you will, of course, see the mistaken name. ↩

  2. Disregarding the "grokking" phenomenon where continued training after overfitting, in some cases, can apparently make it start generalising again. ↩

  3. Of course, people _always_ say that when they add on unnecessary levels of abstraction... ↩

  4. The [GPT-2 paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) is annoyingly short on concrete numbers, but they do at least explicitly state that they used a batch size of 512. ↩

  5. To be strictly honest here, I've already dug into it, but adding a writeup of that to this already absurdly long blog post felt like something adjacent to sadism. Update shortly. ↩




[« Writing an LLM from scratch, part 28 -- training a base model from scratch on an RTX 3090](/2025/12/llm-from-scratch-28-training-a-base-model-from-scratch) [Writing an LLM from scratch, part 30 -- digging into the LLM-as-a-judge results »](/2026/01/llm-from-scratch-30-digging-into-llm-as-a-judge)

Copyright (c) 2006-2026 by Giles Thomas. This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). 
