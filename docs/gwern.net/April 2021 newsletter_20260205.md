# April 2021 newsletter

**来源:** https://gwern.net
**链接:** https://gwern.substack.com/p/april-2021-newsletter
**日期:** Thu, 03 Jun 2021 15:45:24 GMT

---

[![Gwern.net Newsletter](https://substackcdn.com/image/fetch/$s_!rpC9!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5860611c-2de0-45a7-99a0-dc1b248b0199_1280x1280.png)](/)

# [Gwern.net Newsletter](/)

SubscribeSign in

# April 2021 newsletter

### with links on AI scaling, particular new East Asian record-breaking work & deep reinforcement learning.

[![gwern's avatar](https://substackcdn.com/image/fetch/$s_!jpKC!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3a41d1b8-0e3c-44d4-b99a-8f52362678eb_1592x1800.png)](https://substack.com/@gwern)

[gwern](https://substack.com/@gwern)

Jun 03, 2021

43

1

2

Share

April 2021’s [Gwern.net](https://www.gwern.net/newsletter/2021/04) [newsletter](https://gwern.substack.com) is now out; previous, [March 2021](https://www.gwern.net/newsletter/2021/03) ([archives](https://www.gwern.net/tags/newsletter)). This is a collation of links and summary of major changes, overlapping with my [Changelog](https://www.gwern.net/Changelog); brought to you by my donors on [Patreon](https://www.patreon.com/gwern).

# 1 Writings

  * [Better Greek Variable Suggestions](https://www.gwern.net/Variables) (use ϰ, ς, υ, ϖ, Υ, Ξ, ι, ϱ, ϑ, or Π instead)




# 2 Links

## 2.1 AI

  * [“Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks”](https://arxiv.org/abs/1810.00825), Lee et al 2018; [“Perceiver: General Perception with Iterative Attention”](https://arxiv.org/abs/2103.03206#deepmind), Jaegle et al 2021 (skinny Transformers applied recurrently; given reinvention, one might ask “is [attention](https://arxiv.org/abs/1706.03762#google "'Attention Is All You Need', Vaswani et al 2017"), getting too much attention?”, especially given how many Transformer tweaks [don’t pan out](https://arxiv.org/abs/2102.11972#google "'Do Transformer Modifications Transfer Across Implementations and Applications?', Narang et al 2021") or have antecedents, indicating a gold rush? Probably not: if the marginal return on this research direction had fallen below that of competitors, we would see those neglected directions invade Transformer topics—while we continue to see the reverse, and many applications as yet untouched by all the new approaches, suggesting that we _still_ don’t pay enough attention)

  * [“Z-IL: Predictive Coding Can Do Exact Backpropagation on Any Neural Network”](https://arxiv.org/abs/2103.04689), Salvatori et al 2021 (scaling local learning rules to ImageNet AlexNet/Resnet & ALE DRL at similar compute cost)

  * [“Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates”](https://arxiv.org/abs/1708.07120), Smith & Topin 2017 (the lingering mystery of super-convergence, saving 50–90% compute with LRs as high as 20 (!): what is it, why does it work only sometimes, is there any connection to [grokking](https://www.gwern.net/docs/ai/2021-power.pdf#openai "'Grokking: Generalization Beyond Overfitting On Small Algorithmic Data Sets', Powers et al 2021") & can it work for large models like GPT-3 given the [tunneling hypothesis](https://old.reddit.com/r/MachineLearning/comments/ba1wg5/d_thoughts_about_superconvergence_and/)?)

  * [“Rip van Winkle’s Razor, a Simple New Estimate for Adaptive Data Analysis”](http://www.offconvex.org/2021/04/07/ripvanwinkle/) (an unusual approach to estimating generalization—by quantifying the information-theoretic simplicity of all the powerful DL research discoveries since 2012, into ~1 kilobyte. And yet, _what_ a kilobyte…)

  * [“Ambigrammatic Figures”](https://github.com/golanlevin/AmbigrammaticFigures), Levin & Huang 2020 (making horrifying StyleGAN faces that can be [rotated 180°](https://en.wikipedia.org/wiki/Ambigram) by projection & then [gradient-ascent](https://www.gwern.net/Faces#reversing-stylegan-to-control-modify-images) towards an upside-down face)




[Matters Of Scale](https://old.reddit.com/r/mlscaling/):

  * **[Large Models](https://lair.lighton.ai/akronomicon/ "The Akronomicon: an Extreme-Scale Leaderboard")** :

    * Congratulations to OpenAI on 1 year of GPT-3 & OA API. Has it really only been a year?—it has truly exceeded expectations.

    * [Naver](https://en.wikipedia.org/wiki/Naver) announces 204b-parameter Korean-language NN, [“HyperCLOVA”](http://m.koreaherald.com/view.php?ud=20210525000824) (KO; unknown arch although apparently dense, or training-compute or benchmark/loss performance; 650b token training dataset. Who knew Naver was even trying? “And we are here as on a darkling plain / Swept with confused alarms of struggle and flight, / Where ignorant armies clash by night.”)

    * [“PanGu-α: Large-scale Autoregressive Pretrained Chinese Language Models with Auto-parallel Computation”](https://arxiv.org/abs/2104.12369#huawei), Zeng et al 2021 (Zh; Huawei’s GPT-3-200b prototype, trained on indigenous Chinese GPU+DL stack; a partial replication, due to incomplete training on ~43b tokens; the [13b-parameter](https://git.openi.org.cn/PCL-Platform.Intelligence/PanGu-Alpha#user-content-%E6%A8%A1%E5%9E%8B%E4%B8%8B%E8%BD%BD) model checkpoint has been released for download, and they are considering releasing the 200b-parameter model… [Ding commentary](https://chinai.substack.com/p/chinai-141-the-pangu-origin-story))

    * New 𝒪(100b)-parameter Transformer models announced at Google I/O ’2021: [LaMDA](https://blog.google/technology/ai/lamda/ "LaMDA: our breakthrough conversation technology") (EN; chatbot), [MUM](https://blog.google/products/search/introducing-mum/) (multimodal multilingual search/translation/Q&A)

    * [“PLUG”](https://www.infoq.cn/article/EFIHo75sQsVqLvFTruKE#alibaba) (Zh): a 27b parameter BERT-like Chinese language model, targeting 200b next (AliBaba followup to [StructBERT](https://arxiv.org/abs/1908.04577#alibaba "'StructBERT: Incorporating Language Structures into Pre-training for Deep Language Understanding', Wang et al 2019")/[PALM](https://arxiv.org/abs/2004.07159#alibaba "'PALM: Pre-training an Autoencoding&Autoregressive Language Model for Context-conditioned Generation', Bi et al 2020"))

    * [“CogView: Mastering Text-to-Image Generation via Transformers”](https://arxiv.org/abs/2105.13290), Ding et al 2021 (another Chinese [DALL·E](https://openai.com/blog/dall-e/) clone, post-[M6](https://arxiv.org/abs/2103.00823#alibaba "'M6: A Chinese Multimodal Pretrainer', Lin et al 2021"): _n_ = [30m text-image pairs](https://wudaoai.cn/data-detail/1 "WuDaoCorpus: the largest Chinese corpus data set, with about 2TB of text and 725 billion Chinese characters"), 4b-parameter GPT, models to be released)

    * [“VideoGPT: Video Generation using VQ-VAE and Transformers”](https://arxiv.org/abs/2104.10157), Yan et al 2021; [“GODIVA: ](https://arxiv.org/abs/2104.14806#microsoft)_[G](https://arxiv.org/abs/2104.14806#microsoft)_[enerating ](https://arxiv.org/abs/2104.14806#microsoft)_[O](https://arxiv.org/abs/2104.14806#microsoft)_[pen-](https://arxiv.org/abs/2104.14806#microsoft)_[D](https://arxiv.org/abs/2104.14806#microsoft)_[oma](https://arxiv.org/abs/2104.14806#microsoft) _[I](https://arxiv.org/abs/2104.14806#microsoft)_[n ](https://arxiv.org/abs/2104.14806#microsoft)_[V](https://arxiv.org/abs/2104.14806#microsoft)_[ideos from n](https://arxiv.org/abs/2104.14806#microsoft) _[A](https://arxiv.org/abs/2104.14806#microsoft)_[tural Descriptions”](https://arxiv.org/abs/2104.14806#microsoft), Wu et al 2021 (DALL·E for video on Howto100M: [VQ-VAE](https://arxiv.org/abs/1906.00446#deepmind "'Generating Diverse High-Fidelity Images with VQ-VAE-2', Razavi et al 2019") \+ sparse attention)

    * [“Efficient Large-Scale Language Model Training on GPU Clusters”](https://arxiv.org/abs/2104.04473#nvidia), Narayanan et al 2021 (Nvidia [‘Megatron-LM’ software](https://github.com/nvidia/megatron-lm) for scaling up to 3072 A100 GPUs; allows 1t-parameter models at 502 petaFLOP/s or 50% efficiency, cf TPU rival, [GSPMD](https://arxiv.org/abs/2105.04663#google "'GSPMD: General and Scalable Parallelization for ML Computation Graphs', Xu et al 2021: '50% to 62% compute utilization on 128 to 2048 Cloud TPUv3 cores for models with up to one trillion parameters'"), and note [Patterson et al 2021](file:///tmp/burlyHGiKo.html#patterson-et-al-2021) estimates GPT-3 at ~3.5m V100 GPU-hours, so OA got ~20% efficiency?); [“We expect to see multi-trillion-parameter models by next year, and 100 trillion+ parameter models by 2023”](https://www.youtube.com/watch?v=eAn_oiZwUXA&t=2998s "GTC 2021 Keynote with NVIDIA CEO Jensen Huang: NVIDIA CEO Jensen Huang delivers the #GTC21​ keynote, where he introduced amazing breakthroughs in building virtual worlds with NVIDIA Omniverse; in advancing enterprise computing with new NVIDIA DGX systems and software; in turning the data center into the new unit of computing with the new NVIDIA Grace CPU, BlueField-3 DPU, and DOCA 1.0 SDK; in broadening the reach of AI to all companies and industries with NVIDIA EGX and Aerial 5G; and in transforming transportation with NVIDIA DRIVE Orin and Atlan.") —Nvidia CEO [Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) ([subtitles](https://www.gwern.net/docs/ai/2021-04-12-jensenhuang-gtc2021keynote-eAn_oiZwUXA.en.vtt.txt))

    * Mixture-Of-Experts:

      * [BAAI’s “Wudao Wensu”: 1.75-trillion parameters & multimodal!](https://en.pingwest.com/a/8693) ([prologue](https://syncedreview.com/2021/03/23/chinas-gpt-3-baai-introduces-superscale-intelligence-model-wu-dao-1-0/))

      * [“Exploring Sparse Expert Models and Beyond”](https://arxiv.org/abs/2105.15082#alibaba), Yang et al 2021 (1t-parameter hierarchical Switch Transformer trained on 480 V100 GPUs)

  * **[MuZero](https://arxiv.org/abs/1911.08265#deepmind)** :

    * [“MuZero Unplugged: Online and Offline Reinforcement Learning by Planning with a Learned Model”](https://arxiv.org/abs/2104.06294#deepmind), Schrittwieser et al 2021 (Reanalyze+MuZero; [smooth log-scaling](https://www.gwern.net/images/ai/2021-schrittwieser-figure1-mspacmanmuzerologrewardscaling.png "Figure 1: Final scores in Ms. Pac-Man for different Reanalyse fractions. By scaling the Reanalyse fraction, MuZero can be trained at any desired data budget. All other parameters are held constant. Note the logarithmic x-axis: Linear improvements in score require exponentially more data, matching scaling laws such as described by Kaplan et al 2020 for language models.") of _Ms. Pacman_ reward with sample size, 107–1010, showing that DRL for arcade games parallels board games)

    * [“Decision Transformer: Reinforcement Learning via Sequence Modeling”](https://sites.google.com/berkeley.edu/decision-transformer), Chen et al 2021

    * [“Sampled MuZero: Learning and Planning in Complex Action Spaces”](https://arxiv.org/abs/2104.06303#deepmind), Hubert et al 2021 (MuZero for continuous domains: DM Control Suite/Real-World RL Suite); [“Continuous Control for Searching and Planning with a Learned Model”](https://arxiv.org/abs/2006.07430), Yang et al 2020

    * [“Muesli: Combining Improvements in Policy Optimization”](https://arxiv.org/abs/2104.06159), Hessel et al 2020 (catching up with original MuZero)

    * [“Visualizing MuZero Models”](https://arxiv.org/abs/2102.12924), de Vries et al 2021 (reimplementing & introspecting a MuZero)

  * [“Scaling Scaling Laws with Board Games”](https://arxiv.org/abs/2104.03113), [Jones](https://andyljones.com/) 2021 (AlphaZero/[Hex](https://en.wikipedia.org/wiki/Hex_\(board_game\)): [highly-optimized](https://www.gwern.net/notes/Faster) GPU implementation enables showing [smooth scaling](https://www.gwern.net/notes/Scaling) across 6 OOM of compute—2× FLOPS = 66% victory; amortization of training → runtime tree-search, where 10× training = 15× runtime)

  * [“Scaling Laws for Language Transfer Learning”](https://christina.kim/2021/04/11/scaling-laws-for-language-transfer-learning/#openai), Christina Kim ([Hernandez et al 2021](https://arxiv.org/abs/2102.01293#openai "Scaling Laws for Transfer") followup: smooth scaling for En → De/Es/Zh)

  * [“Carbon Emissions and Large Neural Network Training”](https://arxiv.org/abs/2104.10350#google), Patterson et al 2021 (“…choice of DNN/datacenter/processor can reduce the carbon footprint up to ~100–1000×. These large factors make retroactive estimates difficult.”)

  * [“How to Train BERT with an Academic Budget”](https://arxiv.org/abs/2104.07705), Izsak et al 2021 ([BERT](https://arxiv.org/abs/1810.04805#google "'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding', Devlin et al 2018") in 8 GPU-days—R&D iteration allows finding efficiency; there’s nothing so expensive as demanding research be cheap.^1^)




## 2.2 Genetics

Everything Is Heritable:

  * [“Precision exercise medicine: understanding exercise response variability”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6818669/), Ross et al 2019 (“large individual differences in CRF response (range: −33% to +118%) have been observed across the 8 exercise training studies independent of exercise duration”—nothing in psychology, or medicine, makes sense except in the light of individual differences…)




Recent Evolution:

  * [“Analysis of genomic DNA from medieval plague victims suggests long-term effect of ](https://academic.oup.com/mbe/advance-article/doi/10.1093/molbev/msab147/6277411)_[Yersinia pestis](https://academic.oup.com/mbe/advance-article/doi/10.1093/molbev/msab147/6277411)_[ on human immunity genes”](https://academic.oup.com/mbe/advance-article/doi/10.1093/molbev/msab147/6277411), Immel et al 2021




Engineering:

  * [“China officially bans CRISPR babies, human clones and animal-human hybrids”](https://biohackinfo.com/news-china-gene-editing-criminal-law-article-336-march-2021/)? (another blow to attempts to project fears & fantasies onto China)




## 2.3 Politics/Religion

  *  _[Reflecting Sunlight: Recommendations for Solar Geoengineering Research and Research Governance](https://www.nap.edu/catalog/25762/reflecting-sunlight-recommendations-for-solar-geoengineering-research-and-research-governance)_ , National Academies 2021 ([media](https://www.nytimes.com/2021/03/25/climate/geoengineering-sunlight.html))

  * [“Improving Public Sector Management at Scale? Experimental Evidence on School Governance India”](https://www.gwern.net/docs/sociology/2020-muralidharan.pdf), Muralidharan & Singh 2020

  * [“Jay-Z’s ](https://www.gwern.net/docs/fiction/2012-mason.pdf)_[99 Problems](https://www.gwern.net/docs/fiction/2012-mason.pdf)_[, Verse 2: A Close Reading with 4th Amendment Guidance for Cops and Perps”](https://www.gwern.net/docs/fiction/2012-mason.pdf), Mason 2012




## 2.4 Psychology/Biology

  * [“Oxylipin biosynthesis reinforces cellular senescence and allows detection of senolysis”](https://www.gwern.net/docs/longevity/2021-wiley.pdf), Wiley et al 2021

  * [“Inside the Secret Sting Operations to Expose Celebrity Psychics”](https://www.nytimes.com/2019/02/26/magazine/psychics-skeptics-facebook.html "Are some celebrity mediums fooling their audience members by reading social media pages in advance? A group of online vigilantes is out to prove it")

  * [“If I fits I sits: A citizen science investigation into illusory contour susceptibility in domestic cats (](https://www.gwern.net/docs/catnip/2021-smith.pdf)_[Felis silvestris catus](https://www.gwern.net/docs/catnip/2021-smith.pdf)_[)”](https://www.gwern.net/docs/catnip/2021-smith.pdf), Smith et al 2021

  * [“Cetaceans, sex and sea serpents: an analysis of the Egede accounts of a ‘most dreadful monster’ seen off the coast of Greenland in 1734”](https://www.gwern.net/docs/biology/2005-paxton.pdf), Paxton et al 2005 (is that a legendary cryptid in your pocket, or are you just happy to see me?)

  * [“Building the perfect curse word: A psycholinguistic investigation of the form and meaning of taboo words”](https://www.gwern.net/docs/psychology/writing/2020-reilly.pdf), Reilly et al 2020

  * [Tarrare](https://en.wikipedia.org/wiki/Tarrare)




## 2.5 Technology

  * [“How Developers Choose Names”](https://arxiv.org/abs/2103.07487), Feitelson et al 2021 (“Another example concerned the function ‘arrangeFilesByName(files)’. When asked the return value…one suggested the number of files reordered”)

  * [“Bringing GNU Emacs to Native Code”](https://arxiv.org/abs/2004.02504), Corallo et al 2020 (using libgccjit to make Emacs 2.3× to 42× faster; gccemacs has been merged into Emacs HEAD & will be available soon)

  * [“Hosting SQLite databases on Github Pages (or any static file hoster)”](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/) (a revolution in static website technology: eg running a query [need download only 54kb of a 670MB database](https://nitter.cc/simonw/status/1388933800445452290 "Check out this demo: I run the SQL query "select country_code, long_name from wdi_country order by rowid desc limit 100" and it fetches just 54.2KB of new data \(across 49 small HTTP requests\) to return 100 results---from a statically hosted database file that's 668.8MB!"); fulltext site search is just the beginning of the possibilities of this clever use of [range requests](https://en.wikipedia.org/wiki/Byte_serving))

  * [“](https://www.coderelay.io/fontemon.html) _[Fontemon](https://www.coderelay.io/fontemon.html)_[: World’s first video game in a font!”](https://www.coderelay.io/fontemon.html) (a _Pokemon_ -like CYOA [implemented as an OpenType font file](https://github.com/mmulet/code-relay/blob/main/markdown/HowIDidIt.md); play in browser or text editor—still not quite [Turing-complete](https://www.gwern.net/Turing-complete) but definitely the most impressive thing implemented in a font so far)

    * _Fontemon_ is by far the highlight of [SIGBOVIK 2021](http://sigbovik.org/2021/proceedings.pdf); but also worth noting: [“Back to Square One: Superhuman Performance in Chutes and Ladders Through Deep Neural Networks and Tree Search”](http://sigbovik.org/2021/proceedings.pdf#page=8) · [“Deep Deterministic Policy Gradient Boosted Decision Trees”](http://sigbovik.org/2021/proceedings.pdf#page=83) · [“Lowestcase and uppestcase letters: Advances in derp learning”](http://sigbovik.org/2021/proceedings.pdf#page=126) · [“openCHEAT: Computationally Helped Error bar Approximation Tool—Kick-starting Science 4.0”](http://sigbovik.org/2021/proceedings.pdf#page=167) · [“The Newcomb-Benford Law, Applied to Binary Data: An Empirical and Theoretic Analysis”](http://sigbovik.org/2021/proceedings.pdf#page=216) · [“Inverted Code Theory: Manipulating Program Entropy”](http://sigbovik.org/2021/proceedings.pdf#page=252) (_[Tenet](https://en.wikipedia.org/wiki/Tenet_\(film\))_ fans only—possibly inferior to [Moravec 1991](http://www.frc.ri.cmu.edu/~hpm/project.archive/general.articles/1991/TempComp.html "Time Travel and Computing")?) · [“Build your own 8-bit busy beaver on a breadboard!”](http://sigbovik.org/2021/proceedings.pdf#page=282)

Incidentally, it’s curious that while STEM fields have entire annual issues, journals, & conferences devoted to satire ([SIGBOVIK](http://sigbovik.org/); Arxiv April Fools papers like [Garfinkel et al 2017](https://arxiv.org/abs/1703.10987 "On the Impossibility of Supersized Machines"); [Special Topics](https://www108.lamp.le.ac.uk/ojs1/index.php/pst/issue/archive); the [BMJ Christmas issue](https://www.bmj.com/about-bmj/resources-authors/article-types/christmas-issue); the [Ig Nobel Prizes](https://en.wikipedia.org/wiki/Ig_Nobel_Prize) & [BAHFest](https://bahfest.com/)), after asking in several places, I have found no instances in the humanities. (I know of many entertaining _papers_ , like [Sinhababu 2008](https://www.gwern.net/docs/philo/2008-sinhababu.pdf "Possible Girls") on waifus, but no _regular organized_ publication, with the possible exception of the annual [“Latke-Hamantash Debate”](https://en.wikipedia.org/wiki/Latke%E2%80%93Hamantash_Debate).)




## 2.6 Economics

  * [“The Kelly Criterion in Blackjack Sports Betting, and the Stock Market”](https://www.gwern.net/docs/statistics/decision/2006-thorp.pdf), Thorp 2006

  * [“The Performance Pay Nobel”](https://marginalrevolution.com/marginalrevolution/2016/10/performance-pay-nobel.html) (CEO pay as [blackbox optimization problem](https://www.gwern.net/Backstop))

  * [“The Ocean’s Hot Dog: The Development of the Fish Stick”](https://www.gwern.net/docs/economics/2008-josephson.pdf), Kelly 2008 (out of nostalgia, I bought some fish sticks for the first time in decades; better than I remembered, even if I had no [tartar](https://en.wikipedia.org/wiki/Tartar_sauce) handy)




## 2.7 Philosophy

  * [“The Aesthetics of Smelly Art”](https://www.gwern.net/docs/culture/2007-shiner.pdf), Shiner & Kriskovets 2007; [“The Odor Value Concept in the Formal Analysis of Olfactory Art”](https://www.gwern.net/docs/culture/2019-kraft.pdf), Kraft 2019; [“Perfumery as an art form”](https://qualiacomputing.com/2020/02/21/perfumery-as-an-art-form/ "Hedonic Tone, memetics, scent, sex, spirituality")/[notes](https://qualiacomputing.com/2020/08/14/qualia-research-diary-scents/ "Qualia Research Diary: Scents \[consciousness research, Experiment, genetics, memetics, scent, valence\]"), Qualia Computing 2020 (more: manufacturing: [“The Scent of the Nile: Jean-Claude Ellena creates a new perfume”](https://www.newyorker.com/magazine/2005/03/14/scent-nile "Chandler Burr 2005"); human smell is better than you think: [“Mechanisms of Scent-tracking in Humans”](https://www.gwern.net/docs/psychology/2006-porter.pdf), Porter et al 2006 ([video](https://www.gwern.net/images/psychology/2006-porter-humanscenttracking-41593_2007_bfnn1819_moesm2_esm.mp4); see also [“Poor Human Olfaction is a 19th Century Myth”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5512720/), McGann 2017); [olfactory white](https://www.pnas.org/content/109/49/19959.full "'Perceptual convergence of multi-component mixtures in olfaction implies an olfactory white', Weiss et al 2012"); _[Kōdō](https://en.wikipedia.org/wiki/K%C5%8Dd%C5%8D)_ , which unexpectedly appears in [Knuth](https://www.gwern.net/docs/cs/2005-knuth-taocp-v4-prefascicle4b.pdf#page=22 "7.2.1.7: History of Combinatorial Generation: Set Partitions"). [C. Thi Nguyen](https://threadreaderapp.com/thread/1357071738731814912.html "https://twitter.com/add_hawk/status/1357071738731814912")’s description of the more bizarre & avant-garde perfumes made me curious enough to nose around & order 39 [LuckyScent](https://www.luckyscent.com/) samplers.)




## 2.8 Miscellaneous

  * [Bog butter](https://en.wikipedia.org/wiki/Bog_butter)

  * [Sarah Bernhardt](https://en.wikipedia.org/wiki/Sarah_Bernhardt) (Lions. Lots of lions.)




* * *

  1. Another thought, looking at [‘Employer Costs for Employee Compensation’](https://bls.gov/news.release/ecec.nr0.htm) ([PDF](https://bls.gov/news.release/archives/ecec_031986.pdf)):

     1. “Moore’s Law”: the cost of a transistor halves every ~19 months;

     2. “Anti-Moore’s Law”: the cost of a synapse doubles every ~119 years.




43

1

2

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[](https://substack.com/profile/41553795-c?utm_source=comment)

[C.](https://substack.com/profile/41553795-c?utm_source=substack-feed-item)

[Jul 9, 2021](https://gwern.substack.com/p/april-2021-newsletter/comment/2351057 "Jul 9, 2021, 9:45 PM")

 _User was indefinitely suspended for this comment.[Show](javascript:void\(0\))_

 __

Reply Share

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 Gwern Branwen · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
