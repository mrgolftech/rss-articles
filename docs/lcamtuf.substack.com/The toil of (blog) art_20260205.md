# The toil of (blog) art

**来源:** https://lcamtuf.substack.com
**链接:** https://lcamtuf.substack.com/p/the-toil-of-blog-art
**日期:** Sun, 18 Jan 2026 18:17:01 GMT

---

[![lcamtuf’s thing](https://substackcdn.com/image/fetch/$s_!WvGP!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F57b73d90-d717-4de9-bfb7-30a0f2913607_400x400.png)](/)

# [lcamtuf’s thing](/)

SubscribeSign in

# The toil of (blog) art

### An image is worth $19.95.

Jan 18, 2026

53

15

Share

When writing a technical blog, the first 90% of every article is a lot easier than the final 10%. Sometimes, the challenge is collecting your own thoughts; I remember walking through the forest and talking to myself about the articles about [Gödel’s beavers](https://lcamtuf.substack.com/p/monkeys-typewriters-and-busy-beavers) or [infinity](https://lcamtuf.substack.com/p/how-has-mathematics-gotten-so-abstract). Other times, the difficulty is the implementation of an idea. I sometimes spend days in the workshop or writing code to get, say, the throwaway image of a [square-wave spectrogram](https://lcamtuf.substack.com/p/is-the-frequency-domain-a-real-place) at the end of a whimsical post.

That said, by far the most consistent challenge is art. Illustrations are important, easy to half-ass, and fiendishly difficult to get right. I’m fortunate enough that photography has been my [lifelong hobby](https://lcamtuf.coredump.cx/photo_basics/), so I have little difficulty capturing good photos of the physical items I want to talk about:

[![](https://substackcdn.com/image/fetch/$s_!jRPu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F539af19d-55ff-45ef-a127-a4582e89ccc0_2000x1334.jpeg)](https://substackcdn.com/image/fetch/$s_!jRPu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F539af19d-55ff-45ef-a127-a4582e89ccc0_2000x1334.jpeg)_A macro photo of a photodiode sensor. By author._

Similarly, because I’ve been [interested in CAD and CAM](https://lcamtuf.coredump.cx/gcnc/full/) for nearly two decades, I know how to draw shapes in 3D and know enough about rendering tech to make the result look good:

[![](https://substackcdn.com/image/fetch/$s_!L4no!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd145833b-05b5-4f5d-ad13-7c1ee632058d_1600x900.jpeg)](https://substackcdn.com/image/fetch/$s_!L4no!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd145833b-05b5-4f5d-ad13-7c1ee632058d_1600x900.jpeg)_An explanation of resin casting, by author._

Alas, both approaches have their limits. Photography just doesn’t work for conceptual diagrams; 3D could, but it’s slow and makes little sense for two-dimensional diagrams, such as circuit schematics of most function plots.

Over the past three years, this forced me to step outside my comfort zone and develop a new toolkit for simple, technical visualizations. If you’re a long-time subscriber, you might have seen the changing art style of the posts. What you probably don’t know is that I often revise older articles to try out new visualizations and hone in my skills. So, let’s talk shop!

### Circuit schematics

Electronic circuits are a common theme of my posts; the lifeblood of this trade are circuit schematics. I’m old enough to remember the beautiful look of hand-drawn schematics in the era before the advent of electronic design automation (EDA) software:

[![](https://substackcdn.com/image/fetch/$s_!U8kd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7280e4e-b680-4915-9caf-0254cccb33de_1023x682.jpeg)](https://substackcdn.com/image/fetch/$s_!U8kd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7280e4e-b680-4915-9caf-0254cccb33de_1023x682.jpeg)_An old circuit schematic._

Unfortunately, the industry no longer takes pride in this craft; the output from modern schematic capture tools, such as KiCad, is uniformly hideous:

[![](https://substackcdn.com/image/fetch/$s_!PIx-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F586762cc-9ed2-472b-84c6-99862961d371_864x505.png)](https://substackcdn.com/image/fetch/$s_!PIx-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F586762cc-9ed2-472b-84c6-99862961d371_864x505.png)_An example of KiCad schematic capture._

I used this style for some of the electronics-related articles I published in the 2010s, but for this Substack, I wanted to do better. This meant ditching EDA for general-purpose drawing software. At first, I experimented with the same CAD software I use for 3D part design, [Rhino3D](https://www.rhino3d.com/):

[![](https://substackcdn.com/image/fetch/$s_!mFgg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6e13dc3-b62e-4dec-a522-4f12f8516774_5850x3600.png)](https://substackcdn.com/image/fetch/$s_!mFgg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6e13dc3-b62e-4dec-a522-4f12f8516774_5850x3600.png)_Chicken coop controller in Rhino3D. By author._

This approach had several advantages. First, I was already familiar with the software. Second, CAD tools are tailored for technical drawings: it’s a breeze to precisely align shapes, parametrically transform and duplicate objects, and so forth. At the same time, while the schematics looked more readable, they were nothing to write home about.

In a quest for software that would allow me to give the schematics a more organic look, I eventually came across [Excalidraw](https://excalidraw.com/). Excalidraw is an exceedingly simple, web-based vector drawing tool. It’s limited and clunky, but with time, I’ve gotten good at working around many of its flaws:

[![](https://substackcdn.com/image/fetch/$s_!QH2k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F951cc0a9-e0b3-4c57-bacc-47e663e36eae_3113x1500.jpeg)](https://substackcdn.com/image/fetch/$s_!QH2k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F951cc0a9-e0b3-4c57-bacc-47e663e36eae_3113x1500.jpeg)_A schematic of a microphone amplifier in Excalidraw, by author._

What I learned from these two tools is that consistency is key. There is a temptation to start every new diagram with a clean slate, but it’s almost always the wrong call. You need to develop a set of conventions you follow every time: scale, line thickness, font colors, a library of reusable design elements to copy-and-paste into new designs. This both makes the tool faster to use — rivaling any EDA package — and allows you to refine the style over time, discarding failed ideas and preserving the tricks that worked well.

This brings us to [Affinity](https://www.affinity.studio/). Affinity is a “grown-up” image editing suite that supports bitmap and vector files; I’ve been using it for photo editing ever since Adobe moved to a predatory subscription model for Photoshop. It took me longer to figure out the vector features, in part because of the overwhelming feature set. This is where the lessons from Rhino3D and Excalidraw paid off: on the latest attempt, I knew not to get distracted and to focus on a simple, reusable workflow first.

[![](https://substackcdn.com/image/fetch/$s_!FHmx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcbab8f9-b761-469b-bdde-297a4c48739b_2323x1372.png)](https://substackcdn.com/image/fetch/$s_!FHmx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcbab8f9-b761-469b-bdde-297a4c48739b_2323x1372.png)_My own library of electronic components in Affinity._

This allowed me to finally get in the groove and replicate the hand-drawn vibe I’ve been after. The new style hasn’t been featured in any recent articles yet, but I’ve gone ahead and updated some older posts. For example, the earlier microphone amplifier circuit now looks the following way:

[![](https://substackcdn.com/image/fetch/$s_!3m6t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0663c62d-e09a-4fdc-91d6-08f76d8de314_2500x1288.jpeg)](https://substackcdn.com/image/fetch/$s_!3m6t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0663c62d-e09a-4fdc-91d6-08f76d8de314_2500x1288.jpeg)_A decent microphone amplifier. By author._

### Explanatory illustrations

Electronic schematics are about the simplest case of technical illustrations. They’re just a map of connections between standard symbols, laid out according to simple rules. There’s no need to make use of depth, color, or motion.

Many other technical drawings aren’t as easy; the challenge isn’t putting lines on paper, it’s figuring out the most effective way to convey the information in the first place. You need to figure out which elements you want to draw the attention to, and how to provide visual hints of the dynamics you’re trying to illustrate.

I confess that I wasn’t putting much thought into it early on. For example, here’s the original 2024 illustration for an article on photodiodes:

[![](https://substackcdn.com/image/fetch/$s_!nn2l!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3baf384b-1003-47b5-818d-403ad91f4a51_2500x824.png)](https://substackcdn.com/image/fetch/$s_!nn2l!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3baf384b-1003-47b5-818d-403ad91f4a51_2500x824.png)_Photodiode structure._

It’s not unusable, but it’s also not good. It’s hard to read and doesn’t make a clear distinction between different materials (solid color) and an electrical region that forms at the junction (hatched overlay).

Here’s my more recent take:

[![](https://substackcdn.com/image/fetch/$s_!o-Bn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e5b3b32-d7c8-488e-8c6b-fbcebe1eb1c1_2000x1050.jpeg)](https://substackcdn.com/image/fetch/$s_!o-Bn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e5b3b32-d7c8-488e-8c6b-fbcebe1eb1c1_2000x1050.jpeg)_A better version of the same._

Once again, the trick isn’t pulling off a single illustration like this; it’s building a standardized workflow that lets you crank out dozens of them. You need to converge on backgrounds, line styles, shading, typefaces, arrows, and so on. With this done, you can take an old and janky illustration, such as the following visual from an [article on magnetism](https://lcamtuf.substack.com/p/whats-the-deal-with-magnetic-fields):

[![](https://substackcdn.com/image/fetch/$s_!a6Lr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4a52d1e-90e9-44f6-a799-963e3e7f9350_1446x810.png)](https://substackcdn.com/image/fetch/$s_!a6Lr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4a52d1e-90e9-44f6-a799-963e3e7f9350_1446x810.png)_A simple model of a conductor._

…and then turn it into the following:

[![](https://substackcdn.com/image/fetch/$s_!xgIU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65caec75-330b-4ba7-acb3-790e1195eb45_2011x983.jpeg)](https://substackcdn.com/image/fetch/$s_!xgIU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65caec75-330b-4ba7-acb3-790e1195eb45_2011x983.jpeg)_A prettier model of the same. By author._

As hinted earlier, in many 2D drawings, it’s a challenge to imply a specific three-dimensional order of objects or to suggest that some of them are in motion. Arrows and annotations don’t always cut it. After a fair amount of trial and error, I settled on subtle outlines, nonlinear shadows, and “afterimages”, as shown in this illustration of a simple rotary encoder:

[![](https://substackcdn.com/image/fetch/$s_!iJCy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5dc47df-9d33-44bd-a9b0-7b8538e42176_2000x1000.jpeg)](https://substackcdn.com/image/fetch/$s_!iJCy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5dc47df-9d33-44bd-a9b0-7b8538e42176_2000x1000.jpeg)_Explaining a rotary encoder._

The next time you see a blog illustration that doesn’t look like 💩 and wasn’t cranked out by AI, remember that more time might have gone into making that single picture than into writing all of the surrounding text.

Subscribe

53

15

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Silverdisc's avatar](https://substackcdn.com/image/fetch/$s_!ryS2!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fyellow.png)](https://substack.com/profile/110993776-silverdisc?utm_source=comment)

[Silverdisc](https://substack.com/profile/110993776-silverdisc?utm_source=substack-feed-item)

[Jan 18](https://lcamtuf.substack.com/p/the-toil-of-blog-art/comment/201624206 "Jan 18, 2026, 6:24 PM")

Liked by lcamtuf

We always tend to took for granted information and knowledge we come across without thinking about the hard labor that is “taking it out of your brain” into a human friendly format. I’m grateful that you share with us all your stuff as it has come to be one of my trusty sources of knowledge and insight. Thank you 

ReplyShare

[![Wojtek's avatar](https://substackcdn.com/image/fetch/$s_!CSnw!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb804fed6-85a8-4040-bde0-9abc8088aada_144x144.png)](https://substack.com/profile/399232257-wojtek?utm_source=comment)

[Wojtek](https://substack.com/profile/399232257-wojtek?utm_source=substack-feed-item)

[Jan 18](https://lcamtuf.substack.com/p/the-toil-of-blog-art/comment/201649504 "Jan 18, 2026, 7:23 PM")

Liked by lcamtuf

I simply admire your attention to detail and consistent struggle for perfection!

ReplyShare

[13 more comments...](https://lcamtuf.substack.com/p/the-toil-of-blog-art/comments)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 lcamtuf · [Publisher Privacy](https://lcamtuf.substack.com/privacy)

Substack · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
