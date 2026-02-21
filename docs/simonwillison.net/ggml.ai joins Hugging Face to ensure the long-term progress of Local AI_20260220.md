# ggml.ai joins Hugging Face to ensure the long-term progress of Local AI

**来源:** [simonwillison.net](https://simonwillison.net)
**发布时间:** 2026-02-20T17:12:55+00:00
**链接:** https://simonwillison.net/2026/Feb/20/ggmlai-joins-hugging-face/#atom-everything

---

<p><strong><a href="https://github.com/ggml-org/llama.cpp/discussions/19759">ggml.ai joins Hugging Face to ensure the long-term progress of Local AI</a></strong></p>
I don't normally cover acquisition news like this, but I have some thoughts.</p>
<p>It's hard to overstate the impact Georgi Gerganov has had on the local model space. Back in March 2023 his release of <a href="https://github.com/ggml-org/llama.cpp">llama.cpp</a> made it possible to run a local LLM on consumer hardware. The <a href="https://github.com/ggml-org/llama.cpp/blob/775328064e69db1ebd7e19ccb59d2a7fa6142470/README.md?plain=1#L7">original README</a> said:</p>
<blockquote>
<p>The main goal is to run the model using 4-bit quantization on a MacBook. [...] This was hacked in an evening - I have no idea if it works correctly.</p>
</blockquote>
<p>I wrote about trying llama.cpp out at the time in <a href="https://simonwillison.net/2023/Mar/11/llama/#llama-cpp">Large language models are having their Stable Diffusion moment</a>:</p>
<blockquote>
<p>I used it to run the 7B LLaMA model on my laptop last night, and then this morning upgraded to the 13B model—the one that Facebook claim is competitive with GPT-3.</p>
</blockquote>
<p>Meta's <a href="https://github.com/meta-llama/llama/tree/llama_v1">original LLaMA release</a> depended on PyTorch and their <a href="https://github.com/facebookresearch/fairscale">FairScale</a> PyTorch extension for running on multiple GPUs, and required CUDA and NVIDIA hardware. Georgi's work opened that up to a much wider range of hardware and kicked off the local model movement that has continued to grow since then.</p>
<p>Hugging Face are already responsible for the incredibly influential <a href="https://github.com/huggingface/transformers">Transformers</a> library used by the majority of LLM releases today. They've proven themselves a good steward for that open source project, which makes me optimistic for the future of llama.cpp and related projects.</p>
<p>This section from the announcement looks particularly promising:</p>
<blockquote>
<p>Going forward, our joint efforts will be geared towards the following objectives:</p>
<ul>
<li>Towards seamless "single-click" integration with the <a href="https://github.com/huggingface/transformers">transformers</a> library. The <code>transformers</code> framework has established itself as the 'source of truth' for AI model definitions. Improving the compatibility between the transformers and the ggml ecosystems is essential for wider model support and quality control.</li>
<li>Better packaging and user experience of ggml-based software. As we enter the phase in which local inference becomes a meaningful and competitive alternative to cloud inference, it is crucial to improve and simplify the way in which casual users deploy and access local models. We will work towards making llama.cpp ubiquitous and readily available everywhere, and continue partnering with great downstream projects.</li>
</ul>
</blockquote>
<p>Given the influence of Transformers, this closer integration could lead to model releases that are compatible with the GGML ecosystem out of the box. That would be a big win for the local model ecosystem.</p>
<p>I'm also excited to see investment in "packaging and user experience of ggml-based software". This has mostly been left to tools like <a href="https://ollama.com">Ollama</a> and <a href="https://lmstudio.ai">LM Studio</a>. ggml-org released <a href="https://github.com/ggml-org/LlamaBarn">LlamaBarn</a> last year - "a macOS menu bar app for running local LLMs" - and I'm hopeful that further investment in this area will result in more high quality open source tools for running local models from the team best placed to deliver them.

    <p><small></small>Via <a href="https://twitter.com/ggerganov/status/2024839991482777976">@ggerganov</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/open-source">open-source</a>, <a href="https://simonwillison.net/tags/transformers">transformers</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llama">llama</a>, <a href="https://simonwillison.net/tags/local-llms">local-llms</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/hugging-face">hugging-face</a>, <a href="https://simonwillison.net/tags/llama-cpp">llama-cpp</a></p>

---

*抓取时间: 2026-02-22 00:02:38*
