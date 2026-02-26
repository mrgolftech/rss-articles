# Writing my own static site generator

**来源:** [maurycyz.com](https://maurycyz.com)
**发布时间:** Fri, 16 Jan 2026 00:00:00 +0000
**链接:** https://maurycyz.com/misc/new_ssg/

---

<!-- mksite: start of content -->
<p>

<em>In principle, a static site generator is a good idea:</em>
They automatically populate your homepage, index pages and RSS feeds.
</p><p>
Unlike software like Wordpress, they don't add runtime cost or security vulnerab&shy;ilities:
They run once and are never exposed to the internet.
</p><p>
However, they all put weird restrictions on how you structure your site:
<!-- snip -->
</p>
<p>
<em>Nearly all of them require you to write in Markdown</em>, which is common, but poorly specified and difficult to parse.
As soon as you do anything more complex then bolding a few words, it becomes a struggle to get the parser to do the right thing.
</p><p>
I recently spent way too much time trying to figure out how to stop it from link-ifying something that looked like a URL. 
</p><p>
In any case, the whole thing seems pointless:
I'm writing a <a href="https://maurycyz.com/tutorials/website">website</a>, something that will be published exclusively on the web... so...
</p><p>
<h1>Why not just use HTML?</h1>
</p><p>
<em>Converting from Markdown</em> would make sense if HTML was super ugly, but it's not.
Here's what bolding looks like in Markdown:
</p>

<pre>
This is an <b>**important point**</b>
</pre>
<p>
... and here's the same in HTML:
</p>
<pre>
This is an &lt;b&gt;<b>important point</b>&lt;/b&gt;
</pre>
<p>
That might be harder to type on a phone keyboard, but if you're writing on a phone, you're not having a good time anyway. 
</p><p>
There are some things that suck with plain HTML, like syntax highlighting, but doing that manually sucks in any language.
Adding a whole markdown parser just to improve code blocks is overkill.
</p><p>
<em>These translation layers are fragile</em>:
The <a href="https://info.cern.ch/hypertext/WWW/TheProject.html">original website</a> still renders fine in modern browsers,
but there's no shortage of Wordpress blogs where all the formatting broke after a server update...
and not just a <a href="https://madebynathan.com/posts/2021-12-05-how-docker-saved-my-blog/">Wordpress</a>.
</p><p>
<h1>Configuration:</h1>
</p><p>
The Markdown thing is somewhat justifiable:
A lot of people are more comfortable with markdown then HTML.
</p><p>
<em>... but they all use weird template formats</em>, which are entire programming languages shoved inside HTML:
complete with questionable design decisions and missing documentation.
As a result, it's very difficult to get these tools to do what you want.
</p><p>
I knew that something as simple as removing the publication date from pages that shouldn't have one 
(like the <a href="https://maurycyz.com/archive">archives</a>)
would result in hours of googling cryptic error messages.
</p><p>
<em>Using them doesn't feel like handcrafting a website.</em>
It feels like throwing arcane bullshit at the wall and seeing what sticks. 
</p><p>
<h1>I'll just do it myself:</h1>
</p><p>
<em>Each article on my site is an HTML file</em> prefixed with a metadata block:

</p><pre>
title Example page:
date 2021-02-11
edited 2025-01-21
tag electronics
tag radiation
---

Paragraph one.
.
Paragraph two 
&lt;!-- snip --&gt;
.
... the rest of the page
</pre><p>

My program copies all files from the source tree into the destination directory.
Everything except HTML is left unchanged.
</p><p>
When it sees an HTML file:
The metadata block is parsed and saved for later.
Everything else is added to a template with the navigation bar and <a href="https://maurycyz.com/misc/inline_css/">styles</a> before being written to the output directory.
</p><p>
To make writing easier, the generator supports using a dot on it's own line:
</p><p>
<pre>
.
</pre>
</p><p>
... as a shorthand for paragraph breaks:
</p><p>
<pre>
&lt;/p&gt;&lt;p&gt;
</pre>
</p><p>
During this process, the generator also saves everything before the <span title="the perks of HTML">&lt;!-- snip --&gt;</span> comment as an excerpt for the homepage.
This done manually because a good excerpt should be long enough get an idea of the topic,
but not any longer.
</p><p>
<em>Once done with the content</em>, all the posts are sorted by date in reverse order:
The first 5 are added to the <a href="https://maurycyz.com/">homepage</a> and <a href="https://maurycyz.com/index.xml">RSS feed</a>. 
All posts except photos are included in the <a href="https://maurycyz.com/archive/">archive</a> page. 
All <a href="https://maurycyz.com/tags/">12 tags</a> get their own index pages.
</p><p>
There's also my <a href="https://maurycyz.com/astro/catalog.html">catalog page</a> which is generated from objects tagged in photos I've taken:
The index page has a section for each astronomical catalog (i.e. NGC), with links sorted by their number in that catalog. (i.e. 5194)
Images of the same object are grouped together, and sorted by date.
Everything is on one page for easy searching and browsing. 
</p><p>
<em>This would be very difficult or even impossible to do in a template-ing language</em>, but is trivial with a custom site generator. 
</p><p>
<em><b>All of this is contained in a <a href="https://maurycyz.com/mksite.c">single C file</a></b></em>:
It has no configuration, no external assets and no weird domain-specific-language. 
The code is ~1000 lines, including template HTML.
It's something that one person can understand and maintain.
</p><p>
It's "🚀BLAZING FAST🔥": 
Building this site (100+ pages, 2000+ assets, ~1 GB total) takes 43 milliseconds. 
Because of this, there's no need for incremental builds or anything of that sort. 
</p><p>
<em>I highly recommend doing this</em>:
</p>
<ul>
<li>There will never be an update that <a href="https://www.ii.com/hugo-update-nope/">breaks your site</a>.
Sure, you could stay on an old version, but it's only a matter of time before you find an annoying bug.</li>
<li>You have complete control: Want to write pages in Emacs <a href="https://github.com/adityaathalye/shite">Org-mode</a>? LaTeX? AsciiDoc? Plain text? No problem.</li>
<li>Do you need something weird and very specific? Just add it.</li>
</ul>
<p>
It's not hard to write one:
It took only a few hours of work to get mine to the point it could replace <a href="https://gohugo.io/">Hugo</a> with it's 1000+ dependencies...
and mine is written in C: Not exactly the friendliest language. 
</p><p>
Sure, there will be some maintance work to fix bugs and add features, but it's not like the thing will break itself:
Lots of 40 year old C code <b>just works</b> on modern systems.
</p><p>
<h1>Switching:</h1>
</p><p>
<em>The longest step</em> was converting all my blog posts into the new format. 
This could have been automated, but I wanted the chance to freshen up the writing.
(... and it still took less time then configuring <a href="https://gohugo.io/">Hugo.</a>)
</p><p>
I started this blog to get better at writing:
All the posts from before 2023 need work.
</p><p>
Really, wanting to delete everything out of shame proves it's working.
But since this is <a href="https://maurycyz.com/misc/starting_a_blog/">a blog</a>, I don't have to delete the old stuff: I can just fix all the mistakes.
</p><p>
I made sure to keep all URLs and RSS &lt;guid&gt;-s the same as the old site, so most people shouldn't notice the change. 
If something broke, please send me an email:

</p><pre>
blog@maurycyz.com
</pre><p>
</p>
<!-- mksite: end of content -->

---

*抓取时间: 2026-02-26 06:10:02*
