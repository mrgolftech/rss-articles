# March 2021 Gwern.net Newsletter

**来源:** https://gwern.net
**链接:** https://gwern.substack.com/p/march-2021-gwernnet-newsletter
**日期:** Tue, 06 Apr 2021 15:31:01 GMT

---

[![Gwern.net Newsletter](https://substackcdn.com/image/fetch/$s_!rpC9!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5860611c-2de0-45a7-99a0-dc1b248b0199_1280x1280.png)](/)

# [Gwern.net Newsletter](/)

SubscribeSign in

# March 2021 Gwern.net Newsletter

### 2 major new site features: 'popins' and recursive Wikipedia popups

[![gwern's avatar](https://substackcdn.com/image/fetch/$s_!jpKC!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3a41d1b8-0e3c-44d4-b99a-8f52362678eb_1592x1800.png)](https://substack.com/@gwern)

[gwern](https://substack.com/@gwern)

Apr 06, 2021

10

3

Share

[March 2021’s Gwern.net](https://www.gwern.net/newsletter/2021/03) [newsletter](https://gwern.substack.com) is now out; previous, [February 2021](https://www.gwern.net/newsletter/2021/02) ([archives](https://www.gwern.net/tags/newsletter)). This is a summary of the revision-history RSS feed, overlapping with my [Changelog](https://www.gwern.net/Changelog) & [/r/gwern](https://old.reddit.com/r/gwern/); brought to you by my donors on [Patreon](https://www.patreon.com/gwern).

# 1 Writings

  * **Gwern.net** : mobile “popins” are finally enabled! ([example](https://www.gwern.net/images/design/2021-03-28-gwern.net-annotations-mobilepopins-darkmode.png)); new Wikipedia popups (this 7th implementation enables _[recursive](https://www.gwern.net/images/design/2021-04-01-gwern.net-annotations-popups-recursivewikipediapopups.png)_[ WP popups](https://www.gwern.net/images/design/2021-04-01-gwern.net-annotations-popups-recursivewikipediapopups.png))




# 2 Links

## 2.1 AI

  * [“Multimodal Neurons in Artificial Neural Networks”](https://distill.pub/2021/multimodal-neurons/#openai), Goh et al 2021 (dissecting [CLIP](https://openai.com/blog/clip/ "CLIP \(Contrastive Language-Image Pre-training\): Connecting Text and Images") concepts, discovering typographical classification ‘attacks’^1^ and a [Stroop effect](https://en.wikipedia.org/wiki/Stroop_effect)! Is there anything CLIP can’t do?)

  * [“Evolving Reinforcement Learning Algorithms”](https://arxiv.org/abs/2101.03958#google), Co-Reyes et al 2021 (evolving eg [TD-learning](https://en.wikipedia.org/wiki/Temporal_difference_learning))

  * [“Waymo Simulated Driving Behavior in Reconstructed Fatal Crashes within an Autonomous Vehicle Operating Domain”](https://www.gwern.net/docs/rl/2021-scanlon.pdf), Scanlon et al 2021 ([blog](https://blog.waymo.com/2021/03/replaying-real-life.html); hard negative mining—self-driving cars, being inhuman, can learn not just from their mistakes but humans’ mistakes too)

  * [“Debugging Reinforcement Learning Systems Without The Agonizing Pain”](https://andyljones.com/posts/rl-debugging.html), Andy L. Jones; [“My Reinforcement Learning Learnings”](https://clemenswinter.com/2021/03/24/my-reinforcement-learning-learnings/), Clemens Winter




[Matters Of Scale](https://old.reddit.com/r/mlscaling/):

  * [“SEER: Self-supervised Pretraining of Visual Features in the Wild”](https://arxiv.org/abs/2103.01988#facebook), Goyal et al 2021 ([blog](https://ai.facebook.com/blog/self-supervised-learning-the-dark-matter-of-intelligence "Self-supervised learning: The dark matter of intelligence"); near-SOTA by training 1b-param CNN on 1b unfiltered unlabeled Internet images—another reminder that unsupervised learning is really working!); [“‘Learning From Videos’ to understand the world”](https://ai.facebook.com/blog/learning-from-videos-to-understand-the-world) (rapid FB expansion of self-supervised training to millions of photos/videos/hours-of-speech); [“Contrasting Contrastive Self-Supervised Representation Learning Models”](https://arxiv.org/abs/2103.14005), Kotar et al 2021 (Supervised learning from ImageNet is now obsolete for transfer learning, and ImageNet just a contaminated validation set)

  * [“Understanding Robustness of Transformers for Image Classification”](https://arxiv.org/abs/2103.14586#google), Bhojanapalli et al 2021 ([Vision Transformers](https://openreview.net/forum?id=YicbFdNTTy#google) gain robustness faster than CNNs as dataset size increases)

  * [“Artificial Intelligence Index Report 2021”](https://aiindex.stanford.edu/wp-content/uploads/2021/03/2021-AI-Index-Report_Master.pdf#page=41): technical performance and cost ([Ding questions](https://chinai.substack.com/p/chinai-137-year-3-of-chinai "ChinAI #137: Year 3 of ChinAI: Reflections on the newsworthiness of machine translation") whether this shows China catching up on AI at all, as we are incessantly told it is doing; one question to ask: ignoring fast-following, what, out of the thousands upon thousands of publications flooding out these days, are the last 3 _major novel_ AI breakthroughs coming out of all pure-Chinese labs combined which could be plausibly equated in importance with, say, just OpenAI’s recent output of [GPT-3](https://arxiv.org/abs/2005.14165#openai)/[DALL·E](https://openai.com/blog/dall-e/)/CLIP?)

  * [OA GPT-3 API: >300 apps, >10k developers, >4.5b words per day](https://openai.com/blog/gpt-3-apps/)

  * [“A mathematical theory of semantic development in deep neural networks”](https://www.pnas.org/content/116/23/11537), Saxe et al 2019 (are jumps in NN capabilities to be expected when scaling? see also [Viering & Loog 2021](https://arxiv.org/pdf/2103.10948.pdf#page=22 "The Shape of Learning Curves: a Review: 6. Ill-behaved learning curves: 6.1. Phase transitions")’s discussion of phase transitions & averaging of exponentials giving power-laws)

  * [“An early cell shape transition drives evolutionary expansion of the human forebrain”](https://www.cell.com/cell/fulltext/S0092-8674\(21\)00239-7), Benito-Kwiecinski et al 2021 ([media](https://www.theguardian.com/science/2021/mar/24/scientists-discover-why-the-human-brain-is-so-big "Scientists discover why the human brain is so big: Molecular switch makes human organ three times larger than great apes’, study finds"); a simple switch for the [scaling up](https://www.gwern.net/docs/psychology/2012-herculanohouzel.pdf "'The remarkable, yet not extraordinary, human brain as a scaled-up primate brain and its associated cost', Herculano-Houzel 2012") of the primate brain)

    * [“Crows possess higher intelligence long thought primarily human”](https://www.statnews.com/2020/09/24/crows-possess-higher-intelligence-long-thought-primarily-human/) (the remarkable, yet not extraordinary, crow/raven brain as scaled-up [bird brain](https://en.wikipedia.org/wiki/Bird_intelligence))




## 2.2 Genetics

Everything Is Heritable:

  * [“GWAS in almost 195,000 individuals identifies 50 previously unidentified genetic loci for eye color”](https://advances.sciencemag.org/content/7/11/eabd1239), Simcoe et al 2021

  * [“Why Do Wealthy Parents Have Wealthy Children?”](https://www.gwern.net/docs/genetics/heritable/2021-fagereng.pdf), Fagereng et al 2021 (I’m always impressed just how difficult it is for rich people to pass on wealth—“shirtsleeves to shirtsleeves in 3 generations” etc)




Evolution:

  * [“Nothing in evolution makes sense except in the light of parasites”](https://www.biorxiv.org/content/10.1101/2021.02.25.432891v1), Hickinbotham et al 2021




Engineering:

  * [“The Demise and Potential Revival of the American Chestnut”](https://www.sierraclub.org/sierra/2021-2-march-april/feature/demise-and-potential-revival-american-chestnut "Before a disastrous blight, the American chestnut was a keystone species in eastern forests. Could genetic engineering help bring it back?")




## 2.3 Statistics/Meta-Science

  * [“Broad cross-national public support for accelerated COVID-19 vaccine trial designs”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7831807/), Broockman et al 2021 (“we can’t do challenge trials with volunteers in February 2020 to save countless thousands of lives because ordinary people might think it unethical”—have you tried _asking_ them, or was that irrelevant because it was just another noble lie?)

  * [“This is the story of how I found what I believe to be scientific misconduct and what happened when I reported it”](https://crystalprisonzone.blogspot.com/2021/01/i-tried-to-report-scientific-misconduct.html), Joe Hilgard

  * [“The Revolution in Classic Tetris: How a younger generation used the Internet to master the falling blocks”](https://www.newyorker.com/culture/cultural-comment/the-revolution-in-classic-tetris) (how achieving classic Tetris maximum-scores, first done in 2010, became routine thanks to YouTube & [online competition for excellence](https://www.gwern.net/Bakewell#external-links))




## 2.4 Politics/Religion

  * [“Magic, Explanations, and Evil: The Origins and Design of Witches and Sorcerers”](https://www.gwern.net/docs/sociology/2021-singh.pdf), Singh 2021 (doubtless even cavemen were all “Og: sus.”)

  * [“Self-blinding citizen science to explore psychedelic microdosing”](https://elifesciences.org/articles/62878), Szigeti et al 2021 (related to [Kaertner et al 2021](https://www.nature.com/articles/s41598-021-81446-7 "Positive expectations predict improved mental-health outcomes linked to psychedelic microdosing"); a self-blinding study, similar to my old self-blinding protocols, confirms that microdosing is just placebo effect, as [I said in 2012](https://www.gwern.net/LSD-microdosing), and I’m reminded of DNB studies like [Foroughi et al 2016](https://www.gwern.net/docs/dnb/2016-foroughi.pdf "Placebo effects in cognitive training"))

  * [The 2019–2020 vaping moral panic](https://en.wikipedia.org/wiki/2019%E2%80%932020_vaping_lung_illness_outbreak) over adulterated black-market THC products (depressing to see how irresponsibly reported & alarmist this was, and how everyone attempted to frame nicotine for it[2](file:///tmp/burlVELRZZ.html#fn2). Naturally, no one involved has apologized or admitted fault—after all, their _[intentions](https://en.wikipedia.org/wiki/Noble_lie)_[ were good](https://en.wikipedia.org/wiki/Noble_lie), “won’t someone think of the children”‽ The incompetence and/or dishonesty here emphasizes how 2020–2021 was business as usual, and the only unusual part is that reality happened so fast we saw some of [the unseen](https://en.wikipedia.org/wiki/Parable_of_the_broken_window).)

  * [Mark Hofmann](https://en.wikipedia.org/wiki/Mark_Hofmann)

  * [Alexandra David-Néel](https://en.wikipedia.org/wiki/Alexandra_David-N%C3%A9el) (one of _those_ 1800–1900s biographies)

  * [John Harvey Kellogg](https://en.wikipedia.org/wiki/John_Harvey_Kellogg)




## 2.5 Psychology/Biology

  * [“Can You Ever Be Too Smart for Your Own Good? Comparing Linear and Nonlinear Effects of Cognitive Ability on Life Outcomes”](https://www.gwern.net/docs/iq/2021-brown.pdf), Brown et al 2021

  * [“The pandemic fallacy: Inaccuracy of social scientists’ and lay judgments about COVID-19’s societal consequences in America”](https://psyarxiv.com/g8f9s/), Hutcherson et al 2021 (highly-inaccurate even retrospectively, typically grossly overestimating)

  * [“Training Working Memory for Two Years—No Evidence of Latent Transfer to Intelligence”](https://psyarxiv.com/hc8je/), Watrin et al 2021 (fade-out of expectancy/placebo effects)

  * [“Real-time dialogue between experimenters and dreamers during REM sleep”](https://www.cell.com/current-biology/fulltext/S0960-9822\(21\)00059-2), Konkoly et al 2021

  * [“Leroy’s elusive little people: A systematic review on lilliputian hallucinations”](https://www.sciencedirect.com/science/article/pii/S0149763421001068), Blom 2021 ([Alice in Wonderland syndrome](https://en.wikipedia.org/wiki/Alice_in_Wonderland_syndrome))

  * [“A Group of Orca Outcasts Is Now Dominating an Entire Sea: ‘Transient’ killer whales that feast on seals and hunt in small packs are thriving while their widely beloved ‘Resident’ siblings are dying out”](https://www.theatlantic.com/science/archive/2021/01/orcas-killer-whale-resident-transient/617862/) (I wonder how the third [orca](https://en.wikipedia.org/wiki/Killer_whale) type, [‘offshore’](https://en.wikipedia.org/wiki/Killer_whale#Types), are doing?)

  * [“Estimation of the total saliva volume produced per day in 5-year-old children”](https://www.gwern.net/docs/biology/1995-watanabe.pdf), Watanabe et al 1995




## 2.6 Technology

  * [“The Aesthetic-Usability Effect”](https://www.nngroup.com/articles/aesthetic-usability-effect/), Moran 2017 ([“They Might Never Tell You It’s Broken”](https://pointersgonewild.com/2019/11/02/they-might-never-tell-you-its-broken/) if it’s pretty enough; see also [“The Third User”](https://asktog.com/atc/the-third-user/ "'The Third User, or, Exactly Why Apple Keeps Doing Foolish Things"))

  * [“Cameras and Lenses”](https://ciechanow.ski/cameras-and-lenses/), Bartosz Ciechanowski (explorable; followup to [“Lights and Shadows”](https://ciechanow.ski/lights-and-shadows/))

  * [“Large Batch Simulation for Deep Reinforcement Learning”](https://arxiv.org/abs/2103.07013), Shacklett et al 2021 (your computer is faster than you think)

  * [“The incredible boxes of Hock Wah Yeo”](https://obscuritory.com/essay/incredible-boxes-of-hock-wah-yeo/) (unusual video game packaging design)

  * [“Stone Walls That Stay Built: A master waller shares how to dry-lay stone walls that hold their ground for centuries”](https://www.gwern.net/docs/technology/2017-post.pdf), Post 2017

  * [Automated storage and retrieval system](https://en.wikipedia.org/wiki/Automated_storage_and_retrieval_system)

  * [Visual cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)




## 2.7 Economics

  * [“The Use and Misuse of Income Data and Extreme Poverty in the United States”](https://www.gwern.net/docs/economics/2021-meyer.pdf), Meyer et al 2021 (measurement error in non-registry surveys of population extremes—not quite [“lizardman”](https://www.gwern.net/GPT-3#lizardman-constant) but similar problem)

  * [“Is economics performative? Option theory and the construction of derivatives markets”](https://www.gwern.net/docs/economics/2006-mackenzie.pdf), Mackenzie 2006 (the mechanics of how the [Black-Scholes model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) changed markets: [Black](https://en.wikipedia.org/wiki/Fischer_Black) ran a service printing “paper” estimating optimal prices for all options which traders could consult & use with simple heuristics to try to arbitrage the market)

  * [“Whitewood under Siege: On the front lines of the pallet wars”](https://www.cabinetmagazine.org/issues/52/hodes.php) (the competition between the two ecosystems of shipping [pallets](https://en.wikipedia.org/wiki/Pallet): ‘whitewood’ & ‘blue pallet’)

  * _[Mautam](https://en.wikipedia.org/wiki/Mautam)_




## 2.8 Philosophy

  * [“Coping with mortality: responses of monkeys and great apes to collapsed, inanimate and dead conspecifics”](https://www.tandfonline.com/doi/full/10.1080/03949370.2021.1893826), De Marco et al 2021

  * [Braitenberg vehicle](https://en.wikipedia.org/wiki/Braitenberg_vehicle)




## 2.9 Fiction

  * [“Reply of the Zaporozhian Cossacks”](https://en.wikipedia.org/wiki/Reply_of_the_Zaporozhian_Cossacks)




## 2.10 Miscellaneous

  * America’s top ace, [Major Dick Bong](https://en.wikipedia.org/wiki/Dick_Bong)




# 3 Film/TV

**Live-action:**

  * _[North by Northwest](https://en.wikipedia.org/wiki/North_by_Northwest)_ ([Hitchcock](https://en.wikipedia.org/wiki/Alfred_Hitchcock) 1959; for such a extremely respected movie, it felt oddly formless and like it was bouncing through genres as more of a comedic B-movie romp than a serious auteur’s effort—since James Bond started in 1953, with a TV adaptation in 1954, NbN comes off as almost a satire. I mean, really, monkeying around in Presidential noses!)




* * *

  1. While interesting, these are ‘attacks’ only in the most generous interpretation possible (since it [does know](https://nitter.cc/NoaNabeshima/status/1368662246885265409 "The new CLIP adversarial examples are partially from the use-mention distinction. CLIP was trained to predict which caption from a list matches an image. It makes sense that a picture of an apple with a large 'iPod' label would be captioned with 'iPod', not 'Granny Smith'! This can be somewhat fixed with a list of labels that are more explicit about this, at least for a small set of pictures I've tried. After some experimentation, I found this prompt that seems to work with CLIP ViT-B-32: ...") [the difference](https://www.youtube.com/watch?v=Rk3MBx20z24&t=35s "'Apple or iPod? Easy Fix for Adversarial Textual Attacks on OpenAI's CLIP Model!', Yannic Kilcher")), and the fact that CLIP can read text in images to note the semantic similarity, is to considerable credit. As the CLIP authors [note](https://www.gwern.net/images/ai/2021-radford-clip-figure4-promptengineering.png "Radford et al 2021 \(CLIP\): **Figure 4**. _Prompt engineering and ensembling improve zero-shot performance_. Compared to the baseline of using contextless class names, prompt engineering and ensembling boost zero-shot classification performance by almost 5 points on average across 36 datasets. This improvement is similar to the gain from using 4× more compute with the baseline zero-shot method but is “free” when amortized over many predictions."), some queries benefit from ensembling, more context than a single word class name such as prefixing “A photograph of a”, and class names can be highly ambiguous: in ImageNet, the class name “crane” could refer to the bird or construction equipment; and the Oxford-IIIT Pet dataset labels one class “boxer”. (CLIP is still [vulnerable to regular adversarial examples](https://stanislavfort.github.io/2021/03/05/OpenAI_CLIP_stickers_and_adversarial_examples.html "Pixels still beat text: Attacking the OpenAI CLIP model with text patches and adversarial pixel perturbations"), of course.)↩

  2. It _couldn’t’ve_ been nicotine because people had been vaping for a decade and a half without widespread near-instantaneous lung-related fatalities! It _had_ to be a new adulterant, and as soon as the first few black-market THC links surfaced, that meant the problem had to be THC-products-only because how would the same adulterant simultaneously get into the different supply chains? And yet, every article, health official, and activist did their paternalist best to suggest otherwise to pin the blame on regular vaping, no matter how many tests turned up clean, and it was the nicotine vaping products which got summarily banned…. One must assume many of those laws are still on the books, inasmuch as [the shipping bans keep expanding](https://old.reddit.com/r/electronic_cigarette/comments/lkhewr/usa_vape_mail_ban_newssales_megathread/).↩




10

3

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![l̴o̴o̴p̴u̴l̴e̴a̴s̴a̴'s avatar](https://substackcdn.com/image/fetch/$s_!lqhe!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F83a07a14-f87b-40ba-ae82-6ce34b65e69f_230x230.jpeg)](https://substack.com/profile/2165244-loopuleasa?utm_source=comment)

[l̴o̴o̴p̴u̴l̴e̴a̴s̴a̴](https://substack.com/profile/2165244-loopuleasa?utm_source=substack-feed-item)

[Apr 14, 2021](https://gwern.substack.com/p/march-2021-gwernnet-newsletter/comment/1731894 "Apr 14, 2021, 11:09 AM")

hi gwern,

is the wordpress popup plugin available for others to use?

I am slowly falling in love with it on your website [gwern.net](http://gwern.net)

ReplyShare

[1 reply by gwern](https://gwern.substack.com/p/march-2021-gwernnet-newsletter/comment/1731894)

[![Lapsed Pacifist's avatar](https://substackcdn.com/image/fetch/$s_!6f-o!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F707c373e-3857-4789-9347-864b8b700405_1575x2044.jpeg)](https://substack.com/profile/34440219-lapsed-pacifist?utm_source=comment)

[Lapsed Pacifist](https://substack.com/profile/34440219-lapsed-pacifist?utm_source=substack-feed-item)

[Sep 30, 2023](https://gwern.substack.com/p/march-2021-gwernnet-newsletter/comment/41033464 "Sep 30, 2023, 4:40 PM")

I build dry stone walls as part of my work, and Brian Post is an outstanding waller and teacher. The Stone Trust in VT, USA, is a great institution and I encourage professionals and amateurs alike to consider taking a class with them. Also, search for 'Moon Gate Vermont' to see an amazing work of art from the founder of the Stone Trust.

ReplyShare

[1 more comment...](https://gwern.substack.com/p/march-2021-gwernnet-newsletter/comments)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 Gwern Branwen · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
