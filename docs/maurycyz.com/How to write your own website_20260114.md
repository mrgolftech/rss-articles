# How to write your own website

**来源:** [maurycyz.com](https://maurycyz.com)
**发布时间:** Wed, 14 Jan 2026 00:00:00 +0000
**链接:** https://maurycyz.com/tutorials/website/

---

<!-- mksite: start of content -->
<p class="dropcap">

I recently wrote <a href="https://maurycyz.com/misc/starting_a_blog/">an essay</a> on why you should set up a personal website rather then using social media. 
Doing so lets you own your space on the internet, customize it and free your readers from constant advertising and algorithmic feeds designed to keep you stuck doomscrolling all day.
</p><p>
<em>Despite how much time we spend using it</em>, creating something for the intenet is seen as arcane wizardy by most people.
This is a fairly accessable guide to getting started.
</p><p>
You'll need a text editor (any will do) and a browser (you already have one).
</p><p>
<!-- snip -->
</p>
<p>


</p><p>
<em>All sites are written in HTML</em>, which is a simple text-based format.
To start with, this is a perfectly valid HTML document:
</p><p>
<pre>
Check out my epic site!
</pre>
</p><p>
To try this, just create a text file with a ".html" extension, and open it in your favorite browser. 
Do this now: experimenting is the best way to learn how everything works.
</p><p>
This is what it should look like:
</p><p>

Check out my epic site!

</p><p>
<em>Plain text is boring</em>, so let's add some formatting:
</p><p>
<pre>
Check out my &lt;b&gt;epic&lt;/b&gt; site!
</pre>
</p><p>

Check out my <b>epic</b> site!

</p><p>

</p><p>

If your browser shows angle brackets on the page, it's likely you accidentally created a file with double extentions.
You can check for this by looking at the URL bar: It should look something like this "file://.../site.html"
If it doesn't end with ".html" but instead ".html.txt" or similar, will will need to fix the file name. 
<br />
<br />
Windows will hide the real file extention by default:
If you are using it, ensure that "Show file extentions" is enabled in the file explorer settings. 

</p><p>
The angle bracket things are tags: "&lt;b&gt;" is an opening tag, and "&lt;/b&gt;" is the matching closing tag.
The word surrounded by brackets ("b") is the tag name, which tells the browser what to do:
In this case, <b>b</b>olding the enclosed text. 
</p><p>
The other formatting tags are &lt;em&gt; <b>em</b><i>phasis</i>,
&lt;u&gt; <u><b>u</b>nderline</u>,
&lt;sub&gt; <sub><b>sub</b>scipt</sub>,
&lt;sup&gt; <sup><b>sup</b>erscript</sup>,
&lt;small&gt; <small><b>small</b> text</small>, 
&lt;mark&gt; highlight and &lt;del&gt;
<del><b>del</b>eted</del>. 
</p><p>
You don't have to memorize this list, but go and try a few out.
</p><p>
There's also &lt;br/&gt; (<b>br</b>eak), which adds a line break. 
It's special because there's no closing tag: It's always closes immediatly and can't contain any text.
I like to add a slash after the tag name to indicate this
</p><p>
<em>A big wall of text can get quite ugly</em>, so it's good to break it up with &lt;p&gt; (<b>p</b>aragraph) tags.
Each paragraph will be visually separated from other content on the page:
</p><p>
<pre>
&lt;p&gt;
Check out my &lt;em&gt;new&lt;/em&gt; site
&lt;/p&gt;
&lt;p&gt;
I have many &lt;b&gt;epic&lt;/b&gt; things here.
&lt;/p&gt;
</pre>
</p>

<p>
Check out my <i>new</i> site:
</p>
<p>
I have many <b>epic</b> things here.
</p>

<p>
Together, the maching tags and their contents form an an <b>element</b>.
Elements can contain other elements, but it's important that they are closed in the correct order:
</p><p>
<em>This is wrong</em>:
</p><p>
<pre>
&lt;em&gt;Some &lt;b&gt;random&lt;/em&gt; text&lt;b&gt;
&lt;!-- &lt;em&gt; (parent) is closed *before* &lt;b&gt; (child) --&gt;
&lt;!-- Don't do this! --&gt;
</pre>
</p><p>
... but this is fine:
</p><p>
<pre>
&lt;em&gt;Some &lt;b&gt;random&lt;/b&gt; text&lt;em&gt;
&lt;!-- &lt;em&gt; (parent) is closed *after* &lt;b&gt; (child) --&gt;
&lt;!-- Perfectly fine. --&gt;
</pre>
</p><p>
Browsers will attempt to render invalid HTML, but the results may not be what you intended:
It's best to make it easy for them.
</p><p>
<em>On that topic, it's good practice</em> to put all your content inside a &lt;body&gt; element which is itself inside a &lt;html&gt; element:
</p><p>
<pre>
&lt;html&gt;
	&lt;body&gt;
		&lt;p&gt;Check out my new site:&lt;/p&gt;
		&lt;p&gt;I have many &lt;b&gt;epic&lt;/b&gt; things here.&lt;/p&gt;
	&lt;/body&gt;
&lt;/html&gt;
</pre>
</p>

<p>Check out my new site:</p>
<p>I have many <b>epic</b> things here.</p>

<p>
This isn't mandatory, but helps browsers render your page correctly:
In the case of an old browser, you don't want metadata (we'll add some later) getting confused for page content. 
</p><p>
<em>Back to text-wall-avoidance:</em>
the &lt;ul&gt; and &lt;ol&gt; (<b>u</b>nordered/<b>o</b>rdered <b>l</b>ist) tags create, well, lists.
Each item should be wraped in &lt;li&gt; tags (<b>l</b>ist <b>i</b>tem)
</p>
<pre>
&lt;html&gt;&lt;body&gt;

&lt;p&gt;About this site (unordered):
	&lt;ul&gt;
		&lt;li&gt;This site has &lt;b&gt;epic&lt;/b&gt; things&lt;/li&gt;
		&lt;li&gt;... and I wrote it myself&lt;/li&gt;
	&lt;/ul&gt;
&lt;/p&gt;

&lt;p&gt;
	It uses these tags: (ordered)
	&lt;ol&gt;
		&lt;li&gt;&amp;lt;html&amp;gt;&lt;/li&gt;
		&lt;li&gt;&amp;lt;body&amp;gt;&lt;/li&gt;
		&lt;li&gt;&amp;lt;p&amp;gt;&lt;/li&gt;
		&lt;li&gt;&amp;lt;ul&amp;gt; and &amp;lt;ol&amp;gt;&lt;/li&gt;
		&lt;li&gt;&amp;lt;li&amp;gt;&lt;/li&gt;
	&lt;/ol&gt;
&lt;/p&gt;

&lt;/body&gt;&lt;/html&gt;
</pre>

<p>About this site (unordered):
	<ul>
		<li>It has <b>epic</b> things</li>
		<li>... and is handwritten HTML</li>
	</ul>
</p>

<p>
	It uses these tags: (ordered)
	<ol>
		<li>&lt;html&gt;</li>
		<li>&lt;body&gt;</li>
		<li>&lt;p&gt;</li>
		<li>&lt;ul&gt; and &lt;ol&gt;</li>
		<li>&lt;li&gt;</li>
	</ol>
</p>

<p>

<em>You can add angle brackets</em> to a page with &amp;gt; (&gt;), &amp;lt; (&lt;) and &amp;amp; (&amp;).
These entities will render as the corresponding charater, but won't form tags.
</p><p>
<em>Headings use</em> &lt;h1&gt; (<b>h</b>eading <b>1</b>) through &lt;h5&gt; (<b>h</b>eading <b>5</b>), with larger numbers using smaller font sizes:

</p>
<pre>
&lt;html&gt;&lt;body&gt;

&lt;h1&gt;My cool site:&lt;/h1&gt;

&lt;p&gt;This site has &lt;b&gt;epic&lt;/b&gt; things and I wrote it myself.&lt;/p&gt;

&lt;h3&gt;Other cool places:&lt;/h3&gt;

&lt;p&gt;To do: Figure out how to add links.&lt;/p&gt;

&lt;/body&gt;&lt;/html&gt;
</pre>

<h1>My cool site:</h1>

<p>This site has <b>epic</b> things and I wrote it myself.</p>

<h3>Other cool places:</h3>

<p>To do: Figure out how to add links.</p>


<p>
<em>About that. Links are just &lt;a&gt; (<b>a</b>nchor) tags</em>, but they have something new:
an attribute after the tag name but before the bracket.
</p>

<pre>
I found this &lt;a href=https://www.righto.com/&gt;cool blog&lt;/a&gt; about electronics. 
</pre>


I found this <a class="default" href="https://www.righto.com/">cool blog</a> about electronics.


<p>
The "href= " attribute sets where the link points to.
A lot of other tags can also have attributes: For example, ordered lists with "reverse=true" count backwards.
</p><p>
The URL in "href=" can be relative:
If linking up multiple pages on the same site, instead of this:
</p>

<pre>
&lt;a href=https://example.com/some/page&gt;Some page&lt;/a&gt;
</pre>

<p>
... just write this: 
</p>

<pre>
&lt;a href=https://example.com/some/page&gt;Some page&lt;/a&gt;
</pre>

<p>
<em>Images work similarly to links</em>, except that they are self-closing elements like &lt;br/&gt;:
</p>



<pre>
&lt;p&gt;Check out this &lt;a href=/astro/m27&gt;picture&lt;/a&gt; of a nebula I took!&lt;/p&gt;

&lt;img src=/astro/m27/small.jpg /&gt;
</pre>
</p>

<p>
Check out this <a class="default" href="https://maurycyz.com/astro/m27">picture</a> of a nebula I took!
</p>
<img class="narrow" src="https://maurycyz.com/astro/m27/small.jpg" />

<p>
</p><p>
(If you don't have a URL for your image, skip to the <a href="https://maurycyz.com/index.xml#hosting">hosting</a> section to set one up)
</p><p>
That's all the essentials, but there's a lot of other useful tags.
For example &lt;details&gt; creates a dropdown that works with ctrl-f:
</p>

<details>
Awsome dropdown (click me!)
<p>
This is a dropdown with just HTML. It works well with browser features (ctrl-f, fragment identifiers, screen readers, etc) by default.
</p>
<p>
(better usability than 99% of commercial sites!)
</details>

<p>
...but I can't cover everything without writing a whole book. 
(The <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements">Mozilla Docs</a> are a fantastic reference)
</p><p>
<h1>Making it look nice:</h1>
</p><p>
<em>At this point</em>, you should have something like this:
</p>

<pre>
&lt;html&gt;
&lt;body&gt;
	&lt;h1&gt;Check out my cool site:&lt;/h1&gt;
	&lt;p&gt;
		I made this site to write about things I do.
		More updates &lt;em&gt;soon™&lt;/em&gt;.
	&lt;/p&gt;

	&lt;h2&gt;Other cool places:&lt;/h2&gt;
	&lt;ul&gt;
		&lt;li&gt;&lt;a href=https://www.righto.com/&gt;Ken Shirriff's blog&lt;/a&gt;&lt;/li&gt;
	&lt;/ul&gt;

	&lt;h2&gt;Photography:&lt;/h2&gt;
	&lt;p&gt;Here's my &lt;a href=/astro/m27&gt;picture&lt;/a&gt; of the Dumbbell Nebula:&lt;/p&gt;
	&lt;img src=/astro/m27/small.jpg /&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>


<h1>Check out my cool site:</h1>
<p>
I made this site to write about things I do.
More updates <i>soon™</i>.
</p>
<h2>Other cool places:</h2>
<ul>
	<li><a class="default" href="https://www.righto.com/">Ken Shirriff's blog</a></li>
</ul>
<h2>Photography:</h2>
<p>Here's my <a class="default" href="https://maurycyz.com/astro/m27">picture</a> of the Dumbbell Nebula:</p>
<img class="narrow" src="https://maurycyz.com/astro/m27/small.jpg" />

<p>

<p>
Let's start by giving the page a machine-readable title:
</p><p>
<pre>
&lt;html&gt;
&lt;head&gt;
	&lt;title&gt;My epic site&lt;/title&gt;
&lt;/head&gt;
&lt;!-- snip --&gt;
</pre>
</p><p>
Like with &lt;body&gt;, the &lt;head&gt; tag isn't required, but it is good to include it:
Otherwise, any metadata that the browser doesn't understand might be mistaken for content.
</p><p>
<em>The page still looks kinda bad</em>: 
Text extending the edges of the page isn't exactly easy to read.
It's not too bad when crammed into my blog, but longer paragraphs will look terrible on large monitors. 
(You might have to switch to landscape to see this problem on mobile)
</p><p>
To fix this, we need to add some style and layout information using the &lt;style&gt; tag:
</p><p>
<pre>
&lt;!-- snip --&gt;
	&lt;style&gt;
		body {
			max-width: 30em;
		}

		img {
			width: 100%;
		}
	&lt;/style&gt;
&lt;/head&gt;
&lt;!-- snip --&gt;
</pre>
</p><p>
<em>Unlike other tags, the contents of &lt;style&gt; isn't HTML</em>, its CSS: a whole other langauge embedded within the file.
CSS is compoosed of blocks, each begining with a selector to control what gets effected.
Here, these are just tag names: "head" and "img"
</p><p>
The selector is followed by a series of declarations wraped in curly braces.
The first block only has one: "max-width: 30em;"
This limits the width of the &lt;body&gt; element to 30 times the font size ("em" unit):
</p>





<h1>Check out my cool site:</h1>
<p>
I made this site to write about things I do.
More updates <i>soon™</i>.
</p>
<h2>Other cool places:</h2>
<ul>
	<li><a class="default" href="https://www.righto.com/">Ken Shirriff's blog</a></li>
</ul>
<h2>Photography:</h2>
<p>Here's my <a class="default" href="https://maurycyz.com/astro/m27">picture</a> of the Dumbbell Nebula:</p>
<img class="narrow" src="https://maurycyz.com/astro/m27/small.jpg" />



<p>
The second block...
</p>
<pre>
img {
	width: 100%;
}
</pre>
<p>
... sets the width of images to (100%) the size of their container.
This ensures that they are properly sized for the column regardless of resolution:
Otherwise, particularly big images can overflow the column, and low-res ones will be tiny.
</p>

<p>
<em>The page is looking rather asymetrical</em>, so lets center the column.
For fixed-width elements, this can be done using the "margin" property:
</p>

<pre>
&lt;!-- snip --&gt;
	&lt;style&gt;
		body {
			max-width: 30em;
			margin: auto;
		}

		img {
			width: 100%;
		}
	&lt;/style&gt;
&lt;!-- snip --&gt;
</pre>


</p>


<h1>Check out my cool site:</h1>
<p>
I made this site to write about things I do.
More updates <i>soon™</i>.
</p>
<h2>Other cool places:</h2>
<ul>
	<li><a class="default" href="https://www.righto.com/">Ken Shirriff's blog</a></li>
</ul>
<h2>Photography:</h2>
<p>Here's my <a class="default" href="https://maurycyz.com/astro/m27">picture</a> of the Dumbbell Nebula:</p>
<img class="narrow" src="https://maurycyz.com/astro/m27/small.jpg" />



<p>
(For varable width elements, use flexbox for centering and other fancy layouts.
A single line of text can be centered with "text-align=center")
</p><p>
<em>Personally, I like dark themed sites</em>, so lets change some of the colors:
</p>

<pre>
&lt;!-- snip --&gt;
	&lt;style&gt;
		html {
			background-color: black;
		}

		html {
			max-width: 30em;
			margin: auto;
			color: white;
		}

		img {
			width: 100%;
		}

		/* Fancy selectors to make visited and unvisited links different colors */
		a:link {color: #4ee;}
		a:visited {color: #399;}
	&lt;/style&gt;
&lt;/head&gt;
&lt;!-- snip --&gt;
</pre>





<h1>Check out my cool site:</h1>
<p>
I made this site to write about things I do.
More updates <i>soon™</i>.
</p>
<h2>Other cool places:</h2>
<ul>
	<li><a class="darklink" href="https://www.righto.com/">Ken Shirriff's blog</a></li>
</ul>
<h2>Photography:</h2>
<p>Here's my <a class="darklink" href="https://maurycyz.com/astro/m27">picture</a> of the Dumbbell Nebula:</p>
<img class="narrow" src="https://maurycyz.com/astro/m27/small.jpg" />



<p>
The "color" style will carry over to every element inside of the styled tag, so there's no need to individually change the text-color of every element.
However, the links do need to be changed because they override the color by default.
</p><p>
<em>That's it:</em>
Everything needed to replicate my blog, minus a few small bits like the sans-serif font, nagivation box, etc.
Of course, your website can and should be different: It's yours.
</p><p>
<em>I highly recomend you read <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">some documentation</a></em> and play around with CSS.
There's also way more to it then I can possbly cover here.
Every website you see was created with it, and it even supports animations and <a href="https://lyra.horse/blog/2025/08/you-dont-need-js/">some interactivity</a>
</p><p>
... also, check out your browser's devtools (ctrl-shift-i):
It will have a nice GUI for editing which shows you the result in real time and shows you what's going on under the hood.
</p><p>
<em>If you ever run out of tags</em>, you can just <a href="https://maurycyz.com/misc/make-up-tags/">make up your own</a> and style them as needed.
As long as the name includes a hypen, it's guaranteed not to be included in any future version of HTML.
The specification even lists &lt;math-α&gt; and &lt;emotion-😍&gt; as allowed custom elements names. 
</p><p>
I've used this heavily on this page: 
All the example websites aren't screenshots, they are &lt;fake-frame&gt; elements styled up to look like a browser window.
Custom tags are also very handy for styling text:
</p>

<pre>
&lt;html&gt;
	&lt;style&gt;
		html {
			color: white;
			background-color: black;
		}
		green-text {
			color: green;
		}
	&lt;/style&gt;

	It &lt;green-text&gt;works&lt;/green-text&gt;!
&lt;/html&gt;
</pre>





It works!



<p>
<h1 id="hosting">Sharing it:</h1>
</p><p>
<em>You should now have a reasonably nice page</em> ready to put up on the internet. 
The easiest way to do this is to use a static file hosting service like <a href="https://docs.github.com/en/pages">Github pages</a> or <a href="https://pages.cloudflare.com/">Cloudflare pages</a>. 
Both of these have generous free tiers that should last a very long time. 
</p><p>
If you don't like big companies, there are plenty of similar, smaller services. 
These can be more limited: The popular <a href="https://neocities.org/">Neocities</a> charges $5/mo to use a custom domain. 
</p><p>
Another option is to rent a server ($3-$5/mo) or, if you have good internet, run one yourself. 
This is by far the most fiddly option: I would not recommend it unless you like playing with computers. 
</p><p>
All off these (except a server) will give you a subdomain by default.
For example, Github Pages will give you <b>your-username</b>.github.io 
However, I do recommend setting up a custom domain:
This will let you switch providers seamlessly should anything happen.
</p><p>
<em>They all work in a similar way:</em>
Upload a file with some name, and it will given a URL with that same name.
The one exception is that files called "index.html" will be viewable at the root of the folder they are in.
</p>
<pre>
Filename          URL

root/
+- my_cats.html   https://example.com/my_cats.html
+- cat_photos/    
|   +- cat1.jpg   https://example.com/cat_photos/cat1.jpg
|   +- cat2.jpg   https://example.com/cat_photos/cat2.jpg
|   +- index.html https://example.com/cat_photos/
|
+- index.html     https://example.com/ 
</pre>
<p>
You should put an index.html in the root of your site to serve as the homepage, but apart from that, the organization is up to you.
</p>
<!-- mksite: end of content -->

---

*抓取时间: 2026-02-26 06:10:02*
