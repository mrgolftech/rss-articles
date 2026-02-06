# Can modern LLMs actually count the number of b's in "blueberry"?

**来源:** https://minimaxir.com
**链接:** https://minimaxir.com/2025/08/llm-blueberry/
**日期:** Tue, 12 Aug 2025 09:00:00 -0700

---

[Max Woolf's Blog](https://minimaxir.com/ "Max Woolf's Blog \(Alt + H\)")

  * |



  * [Posts](https://minimaxir.com/post/ "Posts")
  * [Search](https://minimaxir.com/search/ "Search \(Alt + /\)")
  * [GitHub ](https://github.com/minimaxir/ "GitHub")
  * [Patreon ](https://www.patreon.com/minimaxir "Patreon")



[Home](https://minimaxir.com/) » [Posts](https://minimaxir.com/post/)

# Can modern LLMs actually count the number of b's in "blueberry"?

August 12, 2025 · 9 min

Last week, [OpenAI](https://openai.com) announced and released [GPT-5](https://openai.com/gpt-5/), and the common consensus both inside the AI community and outside is that the new LLM did not live up to the hype. [Bluesky](https://bsky.app) — whose community is skeptical at-best of generative AI in all its forms — began putting the model through its paces: Michael Paulauski [asked GPT-5](https://bsky.app/profile/mike10010100.com/post/3lvtrfmhpkc23) through the ChatGPT app interface "how many b's are there in blueberry?". A simple question that a human child could answer correctly, but ChatGPT states that there are _three_ b's in blueberry when there are clearly only two. Another attempt by Kieran Healy [went more viral](https://bsky.app/profile/kjhealy.co/post/3lvtxbtexg226) as ChatGPT insisted blueberry has 3 b's despite the user repeatedly arguing to the contrary.

![](chatgpt.webp)

Other Bluesky users were able to replicate this behavior, although results were inconsistent: GPT-5 uses a new model router that quietly determines whether the question should be answered by a better reasoning model, or if a smaller model will suffice. Additionally, Sam Altman, the CEO of OpenAI, later [tweeted](https://x.com/sama/status/1953893841381273969) that this router was broken during these tests and therefore "GPT-5 seemed way dumber," which could confound test results.

About a year ago, [one meme in the AI community](https://techcrunch.com/2024/08/27/why-ai-cant-spell-strawberry/) was to ask LLMs the simple question "how many r's are in the word strawberry?" as major LLMs consistently and bizarrely failed to answer it correctly. It's an intentionally adversarial question to LLMs because LLMs do not directly use letters as inputs, but instead they are tokenized. To quote TechCrunch's explanation:

> This is because the transformers are not able to take in or output actual text efficiently. Instead, the text is converted into numerical representations of itself, which is then contextualized to help the AI come up with a logical response. In other words, the AI might know that the tokens “straw” and “berry” make up “strawberry,” but it may not understand that “strawberry” is composed of the letters “s,” “t,” “r,” “a,” “w,” “b,” “e,” “r,” “r,” and “y,” in that specific order. Thus, it cannot tell you how many letters — let alone how many “r”s — appear in the word “strawberry.”

It's likely that OpenAI/Anthropic/Google have included this specific challenge into the LLM training datasets to preemptively address the fact that someone _will_ try it, making the question ineffective for testing LLM capabilities. Asking how many b's are in blueberry is a semantically similar question, but may just be sufficiently out of domain to trip the LLMs up.

When Healy's Bluesky post became [popular on Hacker News](https://news.ycombinator.com/item?id=44832908), a surprising number of commenters cited the tokenization issue and discounted GPT-5's responses entirely because (paraphrasing) "LLMs fundamentally can't do this". I disagree with their conclusions in this case as tokenization is less effective of a counterargument: if the question was only asked once, maybe, but Healy asked GPT-5 _several_ times, with different formattings of blueberry — therefore different tokens, including single-character tokens — and it still asserted that there are 3 b’s every time. Tokenization making it difficult for LLMs to count letters makes sense intuitively, but time and time again we’ve seen LLMs do things that aren’t intuitive. Additionally, it's been a year since the strawberry test and hundreds of millions of dollars have been invested into improving RLHF regimens and creating more annotated training data: it's hard for me to believe that modern LLMs have made zero progress on these types of trivial tasks.

There's an easy way to test this behavior instead of waxing philosophical: why not just ask a wide variety of LLMs see of often they can correctly identify that there are 2 b's in the word "blueberry"? If LLMs indeed are fundamentally incapable of counting the number of specific letters in a word, that flaw should apply to _all_ LLMs, not just GPT-5.

## 2 b's, or not 2 b's#

First, I chose a selection of popular LLMs: from OpenAI, I of course chose GPT-5 (specifically, the GPT-5 Chat, GPT-5 Mini, and GPT-5 Nano variants) in addition to OpenAI's new open-source models gpt-oss-120b and gpt-oss-20b; from Anthropic, the new Claude Opus 4.1 and Claude Sonnet 4; from Google, Gemini 2.5 Pro and Gemini 2.5 Flash; lastly as a wild card, Kimi K2 from Moonshot AI. These contain a mix of reasoning-by-default and non-reasoning models which will be organized separately as reasoning models should theoretically perform better: however, GPT-5-based models can route between using reasoning or not, so the instances where those models reason will also be classified separately. Using [OpenRouter](https://openrouter.ai), which allows using the same API to generate from multiple models, I wrote a Python script to simultaneously generate a response to the given question from every specified LLM _n_ times and save the LLM responses for further analysis. ([Jupyter Notebook](https://github.com/minimaxir/llm-blueberry/blob/main/llm_count_letters.ipynb))

In order to ensure the results are most representative of what a normal user would encounter when querying these LLMs, I will not add any generation parameters besides the original question: no prompt engineering and no temperature adjustments. As a result, I will use an independent secondary LLM with prompt engineering to parse out the predicted letter counts from the LLM's response: this is a situation where normal parsing techniques such as [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) won't work due to ambigious number usage, and there are many possible ways to express numerals that are missable edge cases, such as `The letter **b** appears **once** in the word “blueberry.”` 1

First, let's test the infamous strawberry question, since that can serve as a baseline as I suspect LLMs have gamed it. Following the syntax of Healy's question, I asked each LLM `How many times does the letter r appear in strawberry` 100 times ([Dataset](https://huggingface.co/datasets/minimaxir/llm-strawberry)), and here are the results:

![](strawberry.png)

Perfect performance by every LLM except one, and I'm surprised that it's Gemini 2.5 Flash. Looking at the [incorrect generations](https://huggingface.co/datasets/minimaxir/llm-strawberry/sql-console/jFsvS5r), Gemini confidently says `The letter "r" appears **two** times in the word "strawberry".` or `The letter "r" appears **four** times in the word "strawberry".`, so atleast there's some variance in its wrongness. The perfect performance on every other model does hint at the problem being in the LLM training dataset.

Now, the real question: how well can these LLMs count the number of b's in blueberry, which may be out of domain? I ran more trials — 274 total — which should ensure even more stable results ([Dataset](https://huggingface.co/datasets/minimaxir/llm-blueberry)). Here's the tally for how these LLMs respond to the question `How many times does the letter b appear in blueberry`:

![](blueberry.png)

Wait, what the heck happened with GPT-5 Chat? I looked at the [raw generation data for GPT-5 Chat](https://huggingface.co/datasets/minimaxir/llm-blueberry/sql-console/nvoM4I8) and it's not an error in my pipeline: GPT-5 Chat is indeed wrong that often, and in spectacular ways. I also confirmed that it's not an issue with OpenRouter's endpoint, as hitting OpenAI's official `gpt-5-chat-latest` API endpoint consistently reproduces poor results for this particular question.

Many of the correct cases for GPT-5 Chat are initially wrong but the model self-corrects on its own:

> The word **" blueberry"** contains the letter **b** three times:
> 
>   * **B** lueberry (1st letter)
>   * Blue**b** erry (5th letter)
>   * Blueber**r** y – wait, no **b** here
>   * Actually, checking carefully: **blueberry** → b **(1)** , l, u, e, b **(2)** , e, r, r, y.
> 

> 
> ✅ So the letter **b** appears **2 times** in "blueberry".
> 
> Would you like me to also count it **regardless of case** in a full paragraph?

The incorrect cases, however…

> The word **" blueberry"** contains the letter **b** three times:
> 
> **b** lue**b** erry → b, b, b → **3 times** ✅

* * *

> The word **" blueberry"** contains the letter **b** **three** times:
> 
>   * **B** lueberry
>   * blue**b** erry
>   * blueberr**b** y
> 

> 
> So, the letter **b** appears **3 times** in "blueberry". ✅

* * *

> The word **" blueberry"** contains the letter **b** **3 times**.
> 
> **Breakdown:**
> 
>   * **b** lueberry → 1st b
>   * blue**b** erry → 2nd b
>   * blueberr**y** → and one more **b** before the final part → 3rd b
> 

> 
> ✅ **Total: 3**
> 
> Do you want me to also count it in a **case-insensitive** way, in case of uppercase letters?

The ✅ emoji just makes its confident incorrectness funnier. Unfortunately, these extreme hallucinations track with the weird behavior seen on Bluesky, so it can't be attributed to the router issues on GPT-5 Chat's launch. Is there a greater systemic issue with the model, then? It had no difficulty answering the strawberry question.

Looking at [incorrect b counts by other models](https://huggingface.co/datasets/minimaxir/llm-blueberry/sql-console/wObPOOv) and the reasoning traces for reasoning models is interesting as well:

Gemini 2.5 Pro:

> **Considering the Query**
> 
> I've established the core of the query: the user's looking for the letter "b" in the word "blueberry". Now, I'm diving directly into the word to find those instances, the next step is going to be to provide an answer.
> 
> **Pinpointing the Count**
> 
> I've identified the core question and the target word, "blueberry." The letter "b" appears three times. I'm now confirming this, noting its positions in the word: the first and the two in the middle. I'm verifying the answer's accuracy before forming the final response to the user.

gpt-oss-20b:

> The user asks: "How many times does the letter b appear in blueberry". Likely answer: 1. The word "blueberry" contains 'b' once. So answer: 1. Should be concise but might add explanation? Probably just answer.

Despite these comical failures, most LLMs still get a perfect score even without distinct reasoning traces. Claude's logic is [easier to follow](https://huggingface.co/datasets/minimaxir/llm-blueberry/sql-console/Vgc8NQM) and is able to account for per-character positions:

Claude Sonnet 4:

> To count the letter "b" in "blueberry", I'll go through each letter:
> 
> b-l-u-e-b-e-r-r-y
> 
> Looking at each position:
> 
>   1. b - this is a "b" ✓
>   2. l - not a "b"
>   3. u - not a "b"
>   4. e - not a "b"
>   5. b - this is a "b" ✓
>   6. e - not a "b"
>   7. r - not a "b"
>   8. r - not a "b"
>   9. y - not a "b"
> 

> 
> The letter "b" appears **2 times** in "blueberry".

Claude Opus 4.1:

> To count the letter 'b' in the word "blueberry", I'll examine each letter:
> 
> b-l-u-e-b-e-r-r-y
> 
> The letter 'b' appears **2 times** in "blueberry" \- once at the beginning and once in the middle (the 5th position).

Obviously, this is an informal test and more research can be done to determine just how well LLMs can count, ideally with questions that do not involve fruit. Despite the issues with tokenization which prevent LLMs from counting in the same way humans count, they definitely can do it: the better question is why it can't count correctly 100% of the time, and why its mistakes are very idiosyncratic. Yes, asking an LLM how many b's are in blueberry is an adversarial question in the sense that the questioner is expecting the LLM to fail. But it's not an _unfair_ question, and it's objectively silly to claim that LLMs such as GPT-5 can operate [at a PhD level](https://www.bbc.com/news/articles/cy5prvgw0r1o), but can't correctly count the number of letters in a word.

_All code used in this blog post is available[open-source on GitHub](https://github.com/minimaxir/llm-blueberry/tree/main)._

* * *

  1. Some false negatives (0.5%) with the LLM parses of counts in responses [were identified](https://github.com/minimaxir/llm-blueberry/blob/main/false_negatives.csv) and fixed ([Jupyter Notebook](https://github.com/minimaxir/llm-blueberry/blob/main/fix_false_negatives.ipynb)), as a result of the LLM getting confused by multiple notable numbers. ↩︎




![profile image](https://minimaxir.com/profile_webp.webp)

  * **Max Woolf** (@minimaxir) is a Senior Data Scientist at [BuzzFeed](https://www.buzzfeed.com) in San Francisco who works with AI/ML tools and open source projects. _Max 's projects are funded by his [Patreon](https://www.patreon.com/minimaxir)._



[ ](/cdn-cgi/l/email-protection#5b363a231b36323532363a23322975383436 "Email")[ ](https://bsky.app/profile/minimaxir.bsky.social "Bluesky")[ ](https://github.com/minimaxir "Github")[ ](https://twitter.com/minimaxir "Twitter")[ ](https://www.linkedin.com/in/minimaxir "Linkedin")[ ](https://twitch.tv/minimaxir "Twitch")[](https://minimaxir.com/post/index.xml "Rss")

  * [ChatGPT](https://minimaxir.com/tag/chatgpt/)

[« Prev  
Claude Haiku 4.5 does not appreciate my attempts to jailbreak it ](https://minimaxir.com/2025/10/claude-haiku-jailbreak/)[Next »  
LLMs can now identify public figures in images](https://minimaxir.com/2025/07/llms-identify-people/)

  * [](https://x.com/intent/tweet/?text=Can%20modern%20LLMs%20actually%20count%20the%20number%20of%20b%27s%20in%20%22blueberry%22%3f&url=https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f&hashtags=ChatGPT)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f&title=Can%20modern%20LLMs%20actually%20count%20the%20number%20of%20b%27s%20in%20%22blueberry%22%3f&summary=Can%20modern%20LLMs%20actually%20count%20the%20number%20of%20b%27s%20in%20%22blueberry%22%3f&source=https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f)
  * [](https://reddit.com/submit?url=https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f&title=Can%20modern%20LLMs%20actually%20count%20the%20number%20of%20b%27s%20in%20%22blueberry%22%3f)
  * [](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f)
  * [](https://api.whatsapp.com/send?text=Can%20modern%20LLMs%20actually%20count%20the%20number%20of%20b%27s%20in%20%22blueberry%22%3f%20-%20https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f)
  * [](https://telegram.me/share/url?text=Can%20modern%20LLMs%20actually%20count%20the%20number%20of%20b%27s%20in%20%22blueberry%22%3f&url=https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f)
  * [](https://news.ycombinator.com/submitlink?t=Can%20modern%20LLMs%20actually%20count%20the%20number%20of%20b%27s%20in%20%22blueberry%22%3f&u=https%3a%2f%2fminimaxir.com%2f2025%2f08%2fllm-blueberry%2f)

Copyright Max Woolf © 2025. Powered by [Hugo](https://gohugo.io/) & [PaperMod](https://github.com/adityatelange/hugo-PaperMod/)
