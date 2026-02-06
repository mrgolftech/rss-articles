# Nested Code Fences in Markdown

**来源:** https://susam.net
**链接:** https://susam.net/nested-code-fences.html
**日期:** Mon, 19 Jan 2026 00:00:00 +0000

---

# Nested Code Fences in Markdown

By **Susam Pal** on 19 Jan 2026

Today, we will meet a spiky-haired nerd named Corey Dumm, who normally lives within Markdown code fences. We will get to know him a bit, smile with him when his fences hold and weep quietly when misfortune strikes. 

One of the caveats of the Markdown universe is the wide variety of Markdown implementations available. In these parallel universes, the rules of Markdown rendering differ subtly. In this post, we will focus only on the CommonMark specification. Since GitHub Flavoured Markdown (GFM) is a strict superset of CommonMark, whatever we discuss here applies equally well to both CommonMark and GFM. 

## Contents

  * Basic Code Fences
  * Fancy Code Fences
  * Basic Code Spans
  * Fancy Code Spans
  * Specification



## Basic Code Fences

Corey had a knack for working with computers ever since he was a kid. 
    
    
    Corey at his computer:
    
    ```
    (o_o)--.|[_]|
    ```

Everything was perfect in Corey's world. The CommonMark renderer would convert the Markdown above to the following HTML: 

Corey at his computer:
    
    
    (o_o)--.|[_]|
    

View HTML
    
    
    <p>Corey at his computer:</p>
    <pre><code>(o_o)--.|[_]|
    </code></pre>

At this point, all was well. Corey grew quickly. Before long, he had a head full of spiky hair. Then the fences began to matter. 
    
    
    Corey, all grown up:
    
    ```
     ```
    (o_o)--.|[_]|
    ```

Let us see how this renders. I must warn you that during the Markdown-to-HTML translation, Corey loses his hair. Some viewers may find the following scene disturbing. Viewer discretion is advised. Here is the rendered HTML: 

Corey, all grown up:


(o_o)--.|[_]|


View HTML
    
    
    <p>Corey, all grown up:</p>
    <pre><code></code></pre>
    <p>(o_o)--.|[_]|</p>
    <pre><code></code></pre>

Corey's hair is gone! What a catastrophic accident! Corey is alright, though. He is still quite afraid of Markdown fences, but otherwise well and bouncing back. Why did this happen? The second set of triple backticks immediately ends the fenced code block started by the first set of triple backticks. As a result, Corey's smiley face ends up outside the fenced code block. The triple backticks that were once Corey's hair are now woven into the fabric of the surrounding HTML. Fortunately, CommonMark offers a few ways to avoid such accidents. 

## Fancy Code Fences

In CommonMark, there are two main ways to include triple backticks within fenced code blocks. First, we can use tildes as the code fence: 
    
    
    Corey, all grown up:
    
    ~~~
     ```
    (o_o)--.|[_]|
    ~~~

In fact, a code fence need not consist of exactly three backticks or tildes. Any number of backticks or tildes is allowed, as long as that number is at least three. The following is therefore equivalent: 
    
    
    Corey, all grown up:
    
    ~~~~~
     ```
    (o_o)--.|[_]|
    ~~~~~

And so is this: 
    
    
    Corey, all grown up:
    
    `````
     ```
    (o_o)--.|[_]|
    `````

All three examples render like this: 

Corey, all grown up:
    
    
     ```
    (o_o)--.|[_]|
    

View HTML
    
    
    <p>Corey, all grown up:</p>
    <pre><code> ```
    (o_o)--.|[_]|
    </code></pre>

No hair is lost in translation. 

## Basic Code Spans

A similar problem arises with inline code spans. Most Markdown users know to use backticks to delimit inline code spans. For example: 
    
    
    An old picture of Corey at his computer: `(o_o)--.|[_]|`

This produces the following output: 

An old picture of Corey at his computer: `(o_o)--.|[_]|`

View HTML
    
    
    <p>An old picture of Corey at his computer: <code>(o_o)--.|[_]|</code></p>

However, what do we do when we need to put Corey's dear friend Becky Trace within an inline code span? Becky has short, straight hair tucked neatly on either side of her face. Here's a picture of her: 

``(o_o)``

I believe you can already see the difficulty here. Inline code spans use backticks as delimiters. So when we put Becky within a code span, the first backtick in Becky's face would terminate the code span immediately and then the rest of Becky would lie outside it. CommonMark offers solutions for this kind of situation as well. 

## Fancy Code Spans

An inline code span delimiter need not consist of exactly one backtick. It can consist of any number of backticks. So ``foo`` and ```foo``` produce identical HTML. There is another important but less well-known detail. When the text inside an inline code span begins and ends with spaces, one space is removed from each end before rendering. So ``foo`` and `` foo `` are equivalent. Therefore, when we need to put backticks within an inline code span, we can start the code span using multiple backticks and a space. For example: 
    
    
    Meet Corey's friend Becky Trace: `` `(o_o)` ``

Here is the rendered output: 

Meet Corey's friend Becky Trace: ``(o_o)``

View HTML
    
    
    <p>Meet Corey's friend Becky Trace: <code>`(o_o)`</code></p>

Becky has her hair intact too. We have avoided the mishap that once caused great distress to Corey. That, my friends, is how backticks survive nesting in Markdown. 

## Specification

Before I finish this post, let us take a look at the CommonMark specification to see where these details are defined. The excerpts quoted below are taken from [CommonMark Spec Version 0.30](https://spec.commonmark.org/0.30/), which is by now over four years old. 

From section [4.5 Fenced Code Blocks](https://spec.commonmark.org/0.30/#fenced-code-blocks): 

> A [code fence](https://spec.commonmark.org/0.30/#code-fence) is a sequence of at least three consecutive backtick characters (```) or tildes (`~`). (Tildes and backticks cannot be mixed.) 

> The content of the code block consists of all subsequent lines, until a closing [code fence](https://spec.commonmark.org/0.30/#code-fence) of the same type as the code block began with (backticks or tildes), and with at least as many backticks or tildes as the opening code fence. 

From section [6.1 Code Spans](https://spec.commonmark.org/0.30/#code-spans): 

> A [backtick string](https://spec.commonmark.org/0.30/#backtick-string) is a string of one or more backtick characters (```) that is neither preceded nor followed by a backtick. 
> 
> A [code span](https://spec.commonmark.org/0.30/#code-span) begins with a backtick string and ends with a backtick string of equal length. The contents of the code span are the characters between these two backtick strings, normalized in the following ways: 
> 
>   * First, [line endings](https://spec.commonmark.org/0.30/#line-ending) are converted to [spaces](https://spec.commonmark.org/0.30/#space). 
>   * If the resulting string both begins _and_ ends with a [space](https://spec.commonmark.org/0.30/#space) character, but does not consist entirely of [space](https://spec.commonmark.org/0.30/#space) characters, a single [space](https://spec.commonmark.org/0.30/#space) character is removed from the front and back. This allows you to include code that begins or ends with backtick characters, which must be separated by whitespace from the opening or closing backtick strings. 
> 


I hope these little nuggets of Markdown trivialities will one day prove useful in your own Markdown misfortunes. 

[Comments](./comments/nested-code-fences.html) | [#web](./tag/web.html) | [#technology](./tag/technology.html)

* * *

[Home](./) [Links](./links.html) [Feed](./feed.xml) [Subscribe](./form/subscribe/) [About](./about.html) [GitHub](https://github.com/susam) [Mastodon](https://mastodon.social/@susam)

(C) 2001-2026 Susam Pal
