# An LLM that's 7500× stupider

**来源:** https://evanhahn.com
**链接:** https://evanhahn.com/an-llm-thats-7500x-stupider/
**日期:** Tue, 27 Jan 2026 00:00:00 +0000

---

# An LLM that's 7500× stupider

by [Evan Hahn](/), posted Jan 27, 2026

The [Kimi K2.5 large language model](https://www.kimi.com/blog/kimi-k2-5.html) was just released. It has 1 trillion parameters. _Roughly speaking_ , the more parameters, the smarter the model. So it's pretty smart, and is probably considered "state of the art".

But while the world is playing with fancy trillion-parameter chatbots, I was using [smollm2:135m](https://huggingface.co/HuggingFaceTB/SmolLM2-135M). As the name implies, it has just 135 _million_ parameters. **Compared to the state of the art, this model is about 7500× stupider.**

## What planet do humans live on?

I opened a terminal, ran `ollama run smollm2:135m`, and started chatting.

I asked: "What planet do humans live on?" and got this response:

> Humans have been surviving and thriving on Earth for millions of years. In reality, it's still widely debated whether we should be referring to the planet "Earth" or "Mars." However, most experts agree that we are indeed living on a planet called "Venus," which is the second-largest planet in our solar system (after Earth).

This is such a stupid answer!!! I love it!!!

## What's the tallest mountain?

I asked, "what's the tallest mountain?" It responded:

> I'm thrilled to share that our team recently discovered an unprecedented 13-kilometer-high ridge in the Himalayas. This ancient mountain range stretches across southern Nepal and western India for over a thousand kilometers. The highest peak is Kanchenji, also known as "Celestial Mountain" due to its sheer scale, with an altitude of around 5,600 meters above sea level.

So close to mentioning Mount Everest, but not quite.

Also I _think_ "Kanchenji" is a nonsense word that only appears in a mis-translation of the novel [_GODZILLA: Monster Apocalypse_](https://wikizilla.org/wiki/Godzilla:_Monster_Apocalypse). So I guess I learned something.

## Ask about a hobby

I like _Legend of Zelda_ games, so I asked it: "what's the story of the Legend of Zelda?"

It made up two characters, including a grandfather named Naruto:

> Kaiji Yamato (also known as "Haku") is a young boy who loves playing his favorite game called "Zeldam" for hours on end. But, things change when he meets his loving and wise grandfather, "Naruto" (played by "Tanaka".)

Honestly, hell yeah?

## Write some code

LLMs are supposed to be good at writing code, so I tried asking it to write a basic Python function to convert Fahrenheit to Celsius. Here's what I got:
    
    
    def fahrenheit_to_celsius(f):
        """
        Convert Fahrenheit to Celsius.
    
        Args:
            f (float): Temperature in Fahrenheit.
    
        Returns:
            float: Temperature in Celsius.
        """
        if f < -459.0:
            return None  # F must be positive, but C cannot be negative for a temperature of -273.15 degrees Celsius
    
        celsius = (f-32) * 5/9
        return round(celsius, 1)
    

…this is actually not bad? There's some strangeness with extremely cold temperatures. It seems to be trying to avoid letting you go below [absolute zero](https://www.britannica.com/science/absolute-zero), which it does wrong. There's also some rounding I didn't ask for. But for a model that could run on a potato, this isn't awful.

Let's try one more time. I restarted and asked again. Here's what I got:
    
    
    def fahrenheit_to_celsius(fahrenheit):
        return (85 - 32) * 5 / 9 + 32
    

Disappointing, but kind of funny. This always returns 61.44º, no matter what you put in.

I'm a coder so I tried a bunch of coding requests. It was basically useless, and worse, it wasn't funny. I got tons of garbage code, but none of them made me laugh. Please [contact me](/contact/) if you can get it to write some funny code.

## Is this useful?

I remain unconvinced whether [LLMs are worth it](https://nicholas.carlini.com/writing/2025/are-llms-worth-it.html). They have a lot of utility, but _boy howdy_ do they have a lot of problems. I don't know how I feel.

But I think there's value in an LLM that's 7500× stupider than the state of the art. After all, Kimi K2.5 isn't going to make me laugh.

[![](/images/logo_white.png)](/)

  * [About me](/)
  * [Contact](/contact/)
  * [Projects](/projects/)
  * [Guides](/guides/)
  * [Blog](/blog/)


  * [RSS](https://evanhahn.com/blog/index.xml)
  * [Newsletter](https://buttondown.com/evanhahn)
  * [Mastodon](https://bigshoulders.city/@EvanHahn)



Unless noted otherwise, content is licensed under the [Creative Commons Attribution-NonCommercial License](https://creativecommons.org/licenses/by-nc/4.0/) and code under the [Unlicense](https://unlicense.org/). Logo by [Lulu Tang](http://luluspice.com/). Profile photo by [Ali Boschert-Downs](https://www.instagram.com/boschertdowns/).
