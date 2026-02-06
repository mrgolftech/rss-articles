# Voxtral transcribes at the speed of sound

**来源:** https://simonwillison.net
**链接:** https://simonwillison.net/2026/Feb/4/voxtral-2/#atom-everything
**日期:** 2026-02-04T22:42:34+00:00

---

# [Simon Willison’s Weblog](/)

[Subscribe](/about/#subscribe)

**[Voxtral transcribes at the speed of sound](https://mistral.ai/news/voxtral-transcribe-2)** ([via](https://news.ycombinator.com/item?id=46886735 "Hacker News")) Mistral just released Voxtral Transcribe 2 - a family of two new models, one open weights, for transcribing audio to text. This is the latest in their Whisper-like model family, and a sequel to the original Voxtral which they released [in July 2025](https://simonwillison.net/2025/Jul/16/voxtral/).

Voxtral Realtime - official name `Voxtral-Mini-4B-Realtime-2602` \- is the open weights (Apache-2.0) model, available as a [8.87GB download from Hugging Face](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602).

You can try it out in this [live demo](https://huggingface.co/spaces/mistralai/Voxtral-Mini-Realtime) \- don't be put off by the "No microphone found" message, clicking "Record" should have your browser request permission and then start the demo working. I was very impressed by the demo - I talked quickly and used jargon like Django and WebAssembly and it correctly transcribed my text within moments of me uttering each sound. 

The closed weight model is called `voxtral-mini-latest` and can be accessed via the Mistral API, using calls that look something like this:
    
    
    curl -X POST "https://api.mistral.ai/v1/audio/transcriptions" \
      -H "Authorization: Bearer $MISTRAL_API_KEY" \
      -F model="voxtral-mini-latest" \
      -F file=@"Pelican talk at the library.m4a" \
      -F diarize=true \
      -F context_bias="Datasette" \
      -F timestamp_granularities="segment"

It's priced at $0.003/minute, which is $0.18/hour.

The Mistral API console now has a [speech-to-text playground](https://console.mistral.ai/build/audio/speech-to-text) for exercising the new model and it is _excellent_. You can upload an audio file and promptly get a diarized transcript in a pleasant interface, with options to download the result in text, SRT or JSON format.

![Screenshot of a speech-to-text transcription interface for a file named "Pelican talk at the library.m4a". The toolbar shows "Speech to text" with Code, Transcribe, and Download buttons. The transcript shows timestamped segments from 5:53 to 6:53 with a speaker icon, reading: "5:53 – 6:01 So pelicans love to, they're very good at getting the most they can out of the topography when they're flying. 6:01 – 6:06 And our winds come in from the northwest and they hit those bluffs and they're deflected up. 6:07 – 6:18 And they will sit right, they'll fly north into a wind like five feet off those bluffs, but just five or ten feet off the surface because the winds dissipate. 6:19 – 6:22 And they will surf that bluff all the way north. 6:23 – 6:30 So you'll see a wind from the north at 15 miles an hour, and the pelicans are flying north into that wind and not flapping their wings. 6:31 – 6:33 And it's one of the coolest things. 6:33 – 6:35 You can only find it on San Francisco Coast. 6:36 – 6:39 Where right where the bluffs are steep. 6:41 – 6:43 Pacifica, you can find them there. 6:43 – 6:51 They like their, what we call pier bums, which are typically pelicans that have, are in some sort of trouble. 6:51 – 6:53 They're unable to catch food." The segment at 6:41–6:43 is highlighted in yellow. An audio waveform is shown at the bottom with a playhead near 6:40. Stats in the lower right show 53.90s, 7946.00s, and #45833.](https://static.simonwillison.net/static/2025/mistral-transcript-ui.jpg)

Posted [4th February 2026](/2026/Feb/4/) at 10:42 pm

## Recent articles

  * [Distributing Go binaries like sqlite-scanner through PyPI using go-to-wheel](/2026/Feb/4/distributing-go-binaries/) \- 4th February 2026
  * [Moltbook is the most interesting place on the internet right now](/2026/Jan/30/moltbook/) \- 30th January 2026
  * [Adding dynamic features to an aggressively cached website](/2026/Jan/28/dynamic-features-static-site/) \- 28th January 2026



[ ai 1814 ](/tags/ai/) [ generative-ai 1606 ](/tags/generative-ai/) [ llms 1572 ](/tags/llms/) [ hugging-face 20 ](/tags/hugging-face/) [ mistral 47 ](/tags/mistral/) [ speech-to-text 16 ](/tags/speech-to-text/)

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

