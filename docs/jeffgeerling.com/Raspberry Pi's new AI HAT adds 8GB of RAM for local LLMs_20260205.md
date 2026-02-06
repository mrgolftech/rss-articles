# Raspberry Pi's new AI HAT adds 8GB of RAM for local LLMs

**来源:** https://jeffgeerling.com
**链接:** https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/
**日期:** Thu, 15 Jan 2026 02:00:00 -0600

---

[](https://www.jeffgeerling.com/cdn-cgi/content?id=HokC1qu6fWPKYBAqsfc1BeGeAyJf1lyPq5UNgkRwEqI-1770287279.8751159-1.0.1.1-mTSHHSqJVRe8IesnNR5VjqtJ6wyYaz3B3E3QgywLqco)

[Jeff Geerling](https://www.jeffgeerling.com/)

[YouTube](https://www.youtube.com/c/JeffGeerling) [Merch](https://www.redshirtjeff.com/) [Blog](/) [About](/about/) [RSS](/blog.xml)

# Raspberry Pi's new AI HAT adds 8GB of RAM for local LLMs

Jan 15, 2026

![Raspberry Pi AI HAT+ 2](/blog/2026/raspberry-pi-ai-hat-2/raspberry-pi-ai-hat-2.jpg)

Today Raspberry Pi launched their new [$130 AI HAT+ 2](https://www.raspberrypi.com/products/ai-hat-plus-2/) which includes a Hailo 10H and 8 GB of [LPDDR4X RAM](https://www.micron.com/products/memory/dram-components/lpddr4/part-catalog/part-detail/mt53e2g32d4de-046-wt-c).

With that, the Hailo 10H is capable of running LLMs entirely standalone, freeing the Pi's CPU and system RAM for other tasks. The chip runs at a maximum of 3W, with 40 TOPS of INT8 NPU inference performance in addition to the equivalent 26 TOPS INT4 machine vision performance on the earlier AI HAT with Hailo 8.

In practice, it's not as amazing as it sounds.

You still can't upgrade the RAM on the Pi, but at least this way if you _do_ have a need for an AI coprocessor, you don't have to eat up the Pi's memory to run things on it.

And it's a lot cheaper and more compact than [running an eGPU on a Pi](/blog/2025/big-gpus-dont-need-big-pcs/). In that sense, it's more useful than the silly NPUs Microsoft forces into their 'AI PCs'.

But it's still a solution in search of a problem, in all but the most niche of use cases.

Besides feeling like I'm living in the world of the [Turbo Encabulator](https://www.youtube.com/watch?v=Ac7G7xOG2Ag) every time I'm testing AI hardware, I find the marketing of these things to be very vague, and the applications not very broad.

For example, the Hailo 10H is advertised as being used for a [Fujitsu demo of automatic shrink detection for a self-checkout](https://www.youtube.com/watch?v=flD-WfJ4pUg).

That's certainly not a worthless use case, but it's not something I've ever needed to do. I have a feeling this board is meant more for development, for people who want to deploy the 10H in other devices, rather than as a total solution to problems individual Pi owners need to solve.

Especially when it comes to the headline feature: running inference, like with LLMs.

## Video

I also published a video with all the information in this blog post, but if you enjoy text more than video, scroll on pastâit doesn't offend me!

## LLM performance on the AI HAT+ 2

I ran everything on an 8 gig Pi 5, so I could get an apples-to-apples comparison, running the same models on the Pi's CPU as I did on the AI HAT's NPU.

They both have the same 8GB LPDDR4X RAM configuration, so _ideally_ , they'd have similar performance.

I tested every model Hailo put out so far, and compared them, Pi 5 versus Hailo 10H:

![Raspberry Pi AI HAT+ 2 - Inference performance NPU vs CPU](/blog/2026/raspberry-pi-ai-hat-2/pi-ai-hat-2-llm-compare-inference.jpg)

The Pi's built-in CPU trounces the Hailo 10H.

The Hailo is only close, really, on Qwen2.5 Coder 1.5B.

It _is_ slightly more efficient in most cases:

![Raspberry Pi AI HAT+ 2 - Inference efficiency NPU vs CPU](/blog/2026/raspberry-pi-ai-hat-2/pi-ai-hat-2-llm-compare-efficiency.jpg)

But looking more closely at power draw, we can see why the Hailo doesn't keep up:

![Raspberry Pi AI HAT+ 2 - Power draw NPU vs CPU](/blog/2026/raspberry-pi-ai-hat-2/pi-ai-hat-2-power-draw-compare-llm.jpg)

The Pi's CPU is allowed to max out it's power limits (10W on the SoC), which are a lot higher than the Hailo's (3W).

## Qwen 30B on a Pi

So power holds it back, but the 8 gigs of RAM holds back the LLM use case (vs just running on the Pi's CPU) the most. The Pi 5 can be bought in up to a _16 GB_ configuration. That's as much as you get in decent consumer graphics cards1.

Because of that, many quantized medium-size models target 10-12 GB of RAM usage (leaving space for context, which eats up another 2+ GB of RAM).

A couple weeks ago, [ByteShape got Qwen3 30B A3B Instruct to fit on a 16GB Pi 5](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/). Now this post isn't about LLMs, but the short of it is they found a novel way to compress the model to fit in 10 GB of RAM.

A little bit of quality is lost, but like a JPEG, it's still good enough to ace all the contrived tests (like building a TODO list app, or sorting a complex list) that the tiny models I ran on the Hailo 10H didn't complete well (see the video earlier in this post for details).

![Raspberry Pi 16GB running Qwen3 30B model](/blog/2026/raspberry-pi-ai-hat-2/llama-cpp-pi-5-qwen3-30b-a3b-instruct.jpg)

To test the 30B model, I [installed llama.cpp following this guide from my blog](https://www.jeffgeerling.com/blog/2024/llms-accelerated-egpu-on-raspberry-pi-5/), and [downloaded the compressed model](https://huggingface.co/byteshape/Qwen3-30B-A3B-Instruct-2507-GGUF/).

I asked it to generate a single page TODO list app, and it's still not a speed demon (this is a Pi CPU with LPDDR4x RAM we're talking about), but after a little while, it gave me this:

![Raspberry Pi 16GB Qwen3 Generated TODO list app](/blog/2026/raspberry-pi-ai-hat-2/pi-ai-16gb-qwen3-30b-todo-list-app.jpg)

It met all my requirements:

  * I can type in as many items as I want
  * I can drag them around to rearrange them
  * I can check off items and they go to the bottom of the list...



It's honestly crazy how many small tasks you can do even with free local models... even on a Pi. [Natural Language Programming](https://en.wikipedia.org/wiki/Natural_language_programming) was just a dream back when I started my career.

Besides being angry Google, OpenAI, Anthropic and all these other companies are [consuming all the world's money and resources](https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/is-ai-already-driving-us-growth/) doing this stuffânot to mention [destroying the careers of thousands of junior developers](https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html)âit is kinda neat to see NLP work for very tightly defined examples.

## Benchmarking computer vision

But I don't think this HAT is the best choice to run local, private LLMs (at least not as a primary goal).

What it _is_ good for, is vision processing. But the original AI HAT was good for that too!

In my testing, Hailo's [hailo-rpi5-examples](https://github.com/hailo-ai/hailo-rpi5-examples) were not yet updated for this new HAT, and even if I specified the Hailo 10H manually, model files would not load, or I ran into errors once the board was detected.

But Raspberry Pi's models ran, so I tested them with a Camera Module 3:

![Raspberry Pi AI HAT+ 2 running YOLO vision model at 30fps](/blog/2026/raspberry-pi-ai-hat-2/pi-ai-hat-vision-30fps-yolo.jpg)

I pointed it over at my desk, and it was able to pick out things like my keyboard, my monitor (which it thought was a TV), my phone, and even the mouse tucked away in the back.

It all ran quite fastâand 10x faster than on the Pi's CPUâbut the problem is I can do the same thing with the _original_ AI HAT ($110)âor the [AI Camera](https://www.raspberrypi.com/products/ai-camera/) ($70).

If you _just_ need vision processing, I would stick with one of those.

The headline feature of the AI HAT+ 2 is the ability to run in a 'mixed' mode, where it can process machine vision (frames from a camera or video feed), while also running inference (like an LLM or text-to-speech).

![Raspberry Pi AI HAT+ 2 mixed inference and vision not working](/blog/2026/raspberry-pi-ai-hat-2/pi-ai-hat-mixed-vision-llm-no-work.jpg)

Unfortunately, when I tried running two models simultaneously, I ran into segmentation faults or 'device not ready', and lacking any working examples from Hailo, I had to give up on getting that working in time for this post.

Just like the original AI HAT, there's some growing pains.

It seems like with most hardware with "AI" in the name, it's hardware-first, then software comes laterâif it comes at all. At least with Raspberry Pi's track record, the software _does_ come, it's just... often the solutions are only useful in tiny niche use cases.

## Conclusion

8 GB of RAM is useful, but it's not quite enough to give this HAT an advantage over just paying for the bigger 16GB Pi with more RAM, which will be more flexible and run models faster.

The main use case for this HAT might be in power-constrained applications where you need both vision processing _and_ inferencing. But even there... it's hard to say "yes, buy this thing", because for just a few more watts, the Pi could achieve better performance for inference in tandem with the $70 [AI Camera](https://www.raspberrypi.com/products/ai-camera/) or the $110 [AI HAT+](https://www.microcenter.com/product/687346/product?src=raspberrypi) for the vision processing.

Outside of running tiny LLMs in less than 10 watts, maybe the idea is you use the AI HAT+ 2 as a development kit for designing devices using the 10H like self-checkout scanners (which might not even run on a Pi)? I'm not sure.

* * *

  1. With the obvious caveat that the VRAM on GPUs runs a lot faster than equivalent LPDDR4 RAM on a Pi! ↩︎




## Further reading:

  * [55 TOPS Raspberry Pi AI PC - 4 TPUs, 2 NPUs](/blog/2024/55-tops-raspberry-pi-ai-pc-4-tpus-2-npus/)
  * [Testing Raspberry Pi's AI Kit - 13 TOPS for $70](/blog/2024/testing-raspberry-pis-ai-kit-13-tops-70/)
  * [Dell's version of the DGX Spark fixes pain points](/blog/2025/dells-version-dgx-spark-fixes-pain-points/)



  * [raspberry pi](/tags/raspberry-pi/)
  * [hat](/tags/hat/)
  * [ai](/tags/ai/)
  * [hailo](/tags/hailo/)
  * [video](/tags/video/)
  * [youtube](/tags/youtube/)
  * [llm](/tags/llm/)
  * [pcie](/tags/pcie/)
  * [pci express](/tags/pci-express/)
  * [review](/tags/review/)



## Comments

[](https://www.youtube.com/c/JeffGeerling "YouTube")[](https://github.com/geerlingguy "GitHub")[](/sponsor/ "Sponsor")[](https://twitter.com/geerlingguy/ "Twitter")[](https://www.instagram.com/geerlingguy "Instagram")

Â© 2026 Jeff Geerling | _As an Amazon Associate I earn from qualifying purchases._
