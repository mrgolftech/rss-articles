# February 2021 Gwern.net Newsletter

**来源:** https://gwern.net
**链接:** https://gwern.substack.com/p/february-2021-gwernnet-newsletter
**日期:** Sat, 13 Mar 2021 15:18:44 GMT

---

[![Gwern.net Newsletter](https://substackcdn.com/image/fetch/$s_!rpC9!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5860611c-2de0-45a7-99a0-dc1b248b0199_1280x1280.png)](/)

# [Gwern.net Newsletter](/)

SubscribeSign in

# February 2021 Gwern.net Newsletter

### links on AI scaling, semaglutide, and ethicist ethics

[![gwern's avatar](https://substackcdn.com/image/fetch/$s_!jpKC!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3a41d1b8-0e3c-44d4-b99a-8f52362678eb_1592x1800.png)](https://substack.com/@gwern)

[gwern](https://substack.com/@gwern)

Mar 13, 2021

11

Share

February 2021’s [Gwern.net](https://www.gwern.net/newsletter/2021/02) [newsletter](https://gwern.substack.com) is now out; previous, [January 2021](https://www.gwern.net/newsletter/2021/01) ([archives](https://www.gwern.net/tags/newsletter)). This is a summary of the revision-history RSS feed, overlapping with my [Changelog](https://www.gwern.net/Changelog) & [/r/gwern](https://old.reddit.com/r/gwern/); brought to you by my donors on [Patreon](https://www.patreon.com/gwern).

# 1 Writings

  * **Gwern.net** : popups: can now be moved, stickied, and full-screened (another step towards our ambition of Windows-95-in-the-browser!)




# 2 Links

## 2.1 AI

  * [“Controllable Neural Text Generation”](https://lilianweng.github.io/lil-log/2021/01/02/controllable-neural-text-generation.html), Lilian Weng; [“Recent Advances in Language Model Fine-tuning”](https://ruder.io/recent-advances-lm-fine-tuning/ "This article provides an overview of recent methods to fine-tune large pre-trained language models"), Sebastian Ruder (review)

    * [“Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm”](https://arxiv.org/abs/2102.07350), Reynolds & McDonell 2021 (original 10-shot Fr → En translation can be beaten by the better 0-shot prompt: “French: XYZ / English:…”; this is “true of most worst-performing prompts…”); [“Calibrate Before Use: Improving Few-Shot Performance of Language Models”](https://arxiv.org/abs/2102.09690), Zhao et al 2021 (huge boost from calibrating unstable prompts; both demonstrate, [as always](https://www.gwern.net/GPT-3#prompts-as-programming), that “sampling can prove the presence of knowledge but not the absence.”)

  * [“TransGAN: Two Transformers Can Make One Strong GAN”](https://arxiv.org/abs/2102.07074), Jiang et al 2021 (Transformer-only GAN: attention is all you need)

  * [“PACT: Proof Artifact Co-training for Theorem Proving with Language Models”](https://arxiv.org/abs/2102.06203), Han et al 2021 ([GPT-f](https://arxiv.org/abs/2009.03393#openai "'GPT-f: Generative Language Modeling for Automated Theorem Proving', Polu & Sutskever 2020") for [Lean](https://en.wikipedia.org/wiki/Lean_\(proof_assistant\)))

  * [“Towards End-to-End In-Image Neural Machine Translation”](https://arxiv.org/abs/2010.10648#google), Mansimov et al 2020 (sure why not)

  * **Brains** :

    * [“Artificial Neural Nets Finally Yield Clues to How Brains Learn”](https://www.quantamagazine.org/artificial-neural-nets-finally-yield-clues-to-how-brains-learn-20210218/ "The learning algorithm that enables the runaway success of deep neural networks doesn’t work in biological brains, but researchers are finding alternatives that could") (short overview of biologically-plausible backprop: feedback alignment, target propagation, predictive coding, & attentional feedback; also of recent interest, [VS-ML](https://arxiv.org/abs/2012.14905 "'VS-ML: Meta Learning Backpropagation And Improving It', Kirsch & Schmidhuber 2021"); given their increasing success in training while respecting more biological constraints, the increasing power of backprop-trained ANNs and the neurological success of ANNs in predicting & imitating brain signals, it is increasingly clear that brains _really do_ do backprop in some sense)

    * [“NSD: A massive 7-tesla fMRI dataset to bridge cognitive and computational neuroscience”](https://www.biorxiv.org/content/10.1101/2021.02.22.432340v1), Jean et al 2021 (“…The availability of NSD thus opens the door to using brain activity to directly guide the optimization of deep neural networks.”)

    * [“Brain2Pix: Fully convolutional naturalistic video reconstruction from brain activity”](https://www.biorxiv.org/content/10.1101/2021.02.02.429430v1), Le et al 2021 (reconstructing _[Dr. Who](https://www.biorxiv.org/content/10.1101/687681v1.full "'A large single-participant fMRI dataset for probing brain responses to naturalistic stimuli in space and time', Seeliger et al 2019")_)

    * [“High-performance brain-to-text communication via imagined handwriting”](https://www.biorxiv.org/content/10.1101/2020.07.01.183384v1.full), Willett et al 2020

    * [“Brain-computer interface for generating personally attractive images”](https://www.gwern.net/docs/rl/2021-spape.pdf), Spape et al 2021 (many ways to improve this…)




[Matters Of Scale](https://old.reddit.com/r/mlscaling/):

  * [“Scaling Laws for Transfer”](https://arxiv.org/abs/2102.01293#openai), Hernandez et al 2021 (“We find that pre-training effectively multiplies the fine-tuning dataset size”; a shot across the bow of anyone floating on a proprietary-dataset moat: large models can drop data requirements by orders of magnitude overnight, even surpassing you)

  * [“ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision”](https://arxiv.org/abs/2102.05918#google), Jia et al 2021 (see also [CC-12M](https://arxiv.org/abs/2102.08981#google "'Conceptual 12M: Pushing Web-Scale Image-Text Pre-Training To Recognize Long-Tail Visual Concepts', Changpinyo et al 2021"); [CLIP](https://openai.com/blog/clip/)-like w/EfficientNet trained on 1.8 billion images on a TPUv3-1024—[DM](https://arxiv.org/abs/2102.00529#deepmind "'Decoupling the Role of Data, Attention, and Losses in Multimodal Transformers', Hendricks et al 2021") argues that fancier cross-modal Transformers are better, nevertheless, [‘TPUs go brrr’](http://www.incompleteideas.net/IncIdeas/BitterLesson.html). Given DALL·E, CLIP, ALIGN, [VDVAE](https://arxiv.org/abs/2011.10650#openai "'VDVAE: Very Deep VAEs Generalize Autoregressive Models and Can Outperform Them on Images', Child 2020"), [CW-VAE](https://arxiv.org/abs/2102.09532 "'Clockwork Variational Autoencoders', Saxena et al 2021"), [AIPO](https://arxiv.org/abs/2102.12037 "'AIPO: Image Completion via Inference in Deep Generative Models', Harvey et al 2021") et al, are GANs already dead, and just don’t realize it yet? Or at least soon to be relegated to only DRL-like uses as a final finetuning phase to sharpen up a self-supervised model?); [“WenLan: Bridging Vision and Language by Large-Scale Multi-Modal Pre-Training”](https://arxiv.org/abs/2103.06561), Huo et al 2021

  * [“DALL·E: Zero-Shot Text-to-Image Generation”](https://arxiv.org/abs/2102.12092#openai), Ramesh et al 2021 ([original blog](https://openai.com/blog/dall-e/)); [“M6: A Chinese Multimodal Pretrainer”](https://arxiv.org/abs/2103.00823#alibaba), Lin et al 2021 (Chinese DALL·E: 1.9TB images/0.29TB text for 10b-parameter dense/100b-parameter MoE Transformer; shockingly fast Chinese replication of DALL·E/CLIP)

  * [“Explaining Neural Scaling Laws”](https://arxiv.org/abs/2102.06701#google), Bahri et al 2021/[“Learning Curve Theory”](https://arxiv.org/abs/2102.04074#deepmind), Hutter 2021 ([Rohin Shah commentary](https://www.lesswrong.com/posts/Yt5wAXMc7D2zLpQqx/an-140-theoretical-models-that-predict-scaling-laws#HIGHLIGHTS); more on the manifold hypothesis)




## 2.2 Genetics

Everything Is Heritable:

  * [“Phenotypic covariance across the entire spectrum of relatedness for 86 billion pairs of individuals”](https://www.nature.com/articles/s41467-021-21283-4), Kemper et al 2021

  * [“Genetic variation, brain, and intelligence differences”](https://www.nature.com/articles/s41380-021-01027-y), Deary et al 2021

  * [“Pathfinder: A gamified measure to integrate general cognitive ability into the biological, medical and behavioural sciences”](https://www.biorxiv.org/content/10.1101/2021.02.10.430571v1), Malanchini et al 2021 (not the focus, but the IQ PGS is a slight improvement over [Allegrini et al 2018](https://www.biorxiv.org/content/early/2018/09/17/418210 "Genomic prediction of cognitive traits in childhood and adolescence") due to less phenotype measurement error?)

  * [“Polygenic burden has broader impact on health, cognition, and socioeconomic outcomes than most rare and high-risk copy number variants”](https://www.nature.com/articles/s41380-021-01026-z), Saarentaus et al 2021

  * [On candidate-genes & COMT](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1516-44462021005006201 "'Ditching candidate gene association studies: lessons from psychiatric genetics', Duarte et al 2021")




Recent Evolution:

  * [“Million-Year-Old DNA Rewrites the Mammoth Family Tree: Genomic data—the oldest ever recovered from a fossil—reveals the origin and evolution of the Columbian mammoth”](https://www.nytimes.com/2021/02/17/science/DNA-mammoth.html)

  * [“Kin selection explains the evolution of cooperation in the gut microbiota”](https://www.pnas.org/content/118/6/e2016046118), Simonet & McNally 2021




Engineering:

  * [First Black-Footed Ferret cloned](https://www.nytimes.com/2021/02/18/science/black-footed-ferret-clone.html ""Meet Elizabeth Ann, the First Cloned Black-Footed Ferret: Her birth represents the first cloning of an endangered species native to North America, and may bring needed genetic diversity to the species"")




## 2.3 Statistics/Meta-Science

  * [“Lessons from Gerolamo Cardano’s ](https://www.lesswrong.com/posts/9YDk52NPrfq7nqLvd/lessons-from-the-book-of-my-life)_[The Book of My Life](https://www.lesswrong.com/posts/9YDk52NPrfq7nqLvd/lessons-from-the-book-of-my-life)_[”](https://www.lesswrong.com/posts/9YDk52NPrfq7nqLvd/lessons-from-the-book-of-my-life) (progress studies; see also [Newton’s anthropic argument](https://www.gwern.net/Newton), [Bakewell & inventing progress](https://www.gwern.net/Bakewell), _[The Autobiography of Benvenuto Cellini](https://www.gwern.net/Book-reviews#the-autobiography-of-benvenuto-cellini-cellini-1999)_)

  * [“How Many Microcovids Would You Spend on a Burrito?”](https://www.wired.com/story/group-house-covid-risk-points/) (on the [microCOVID Project Calculator](https://www.microcovid.org/))

  * [“On the enfeeblement of mathematical skills by ‘Modern Mathematics’ and by similar soft intellectual trash in schools and universities”](https://www.gwern.net/docs/math/1968-hammersley.pdf), Hammersley 1968 ([Knuth](https://www.gwern.net/docs/math/1973-knuth.pdf "The Dangers of Computer--Science Theory") highlights as also amusing: [“A Note on Piffles”](https://www.gwern.net/docs/math/1967-austin.pdf), Smith 1967; [“A rebuke of A. B. Smith’s paper, ‘A Note on Piffles’”](https://www.gwern.net/docs/math/1980-farlow.pdf), Farlow 1980)

  * [“Artifact and Recording Concepts in EEG”](https://www.gwern.net/docs/statistics/bias/2011-tatum.pdf), Tatum et al 2011 (on the [EEG](https://en.wikipedia.org/wiki/Electroencephalography) signals of [Jell-O](https://en.wikipedia.org/wiki/Jell-O), or, the importance of [negative controls](https://en.wikipedia.org/wiki/Scientific_control#Negative))




## 2.4 Politics/Religion

  * [“The Logic of Fashion Cycles”](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0032541), Acerbi et al 2012; [“Fashion and art cycles are driven by counter-dominance signals of elite competition: quantitative evidence from music styles”](https://royalsocietypublishing.org/doi/10.1098/rsif.2018.0731), Klimek et al 2019; [“The hipster effect: When anti-conformists all look the same”](https://arxiv.org/abs/1410.8001), Touboul 2019; [“Right Is The New Left”](https://slatestarcodex.com/2014/04/22/right-is-the-new-left), Scott Alexander (see also [Han et al 2010](https://www.gwern.net/docs/culture/2010-han.pdf "Signaling Status with Luxury Goods: The Role of Brand Prominence"), [Downs 1972](https://www.gwern.net/docs/sociology/1972-downs.pdf "Up and down with ecology---the 'issue-attention cycle'")/[Gupta & Jenkins-Smith 2015](https://www.gwern.net/docs/sociology/2015-gupta.pdf "On Anthony Downs's 'Up and Down with Ecology: The "Issue-Attention" Cycle'"), [Lorenz-Spreen et al 2019](https://www.nature.com/articles/s41467-019-09311-w "Accelerating dynamics of collective attention")/[Candia et al 2019](https://www.gwern.net/docs/culture/2019-candia.pdf "The universal decay of collective memory and attention"), [Loury 1994](https://www.gwern.net/docs/sociology/1994-loury.pdf "Self-Censorship in Public Discourse: A Theory of 'Political Correctness' and Related Phenomena"))

  * [“What can we learn from the lunar pandemic that never was?”](https://aeon.co/essays/what-can-we-learn-from-the-lunar-pandemic-that-never-was) (NASA’s lunar quarantine was a sham intended to mollify the public as they covered up repeated major failures & lab leaks both before & after—had there been any dangerous lunar organisms, they would have escaped easily)

  * [MrBeast](https://en.wikipedia.org/wiki/MrBeast) (the new aristocracy of [prestige](https://meltingasphalt.com/social-status-down-the-rabbit-hole/)? Borrowed plumage, perhaps, but effective…)

  * [“Russia’s new Lysenkoism”](https://www.cell.com/current-biology/fulltext/S0960-9822\(17\)30949-1), Kolchinsky et al 2017




## 2.5 Psychology/Biology

  * **[Semaglutide](https://en.wikipedia.org/wiki/Semaglutide)** : [“Once-Weekly Semaglutide in Adults with Overweight or Obesity”](https://www.gwern.net/docs/longevity/2021-wilding.pdf), Wilding et al 2021; [“Effect of Subcutaneous Semaglutide vs Placebo as an Adjunct to Intensive Behavioral Therapy on Body Weight in Adults With Overweight or Obesity: The STEP 3 Randomized Clinical Trial”](https://www.gwern.net/docs/longevity/2021-wadden.pdf), Wadden et al 2021

A longer-acting version of the insulin/appetite peptide [liraglutide](https://en.wikipedia.org/wiki/Liraglutide), semaglutide greatly reduces weight, fat, blood sugar, cholesterol etc, with an [upcoming oral version](https://link.springer.com/article/10.1007/s40262-018-0728-4 "'Safety and pharmacokinetics of single and multiple ascending doses of the novel oral human GLP-1 analogue, oral semaglutide, in healthy subjects and subjects with type 2 diabetes', Granhall et al 2019"); background: [Kushner et al 2020](https://www.gwern.net/docs/longevity/2020-kushner.pdf "Semaglutide 2.4 mg for the Treatment of Obesity: Key Elements of the STEP Trials 1 to 5"), [Aroda et al 2019](https://www.gwern.net/docs/longevity/2019-aroda.pdf "Comparative efficacy, safety, and cardiovascular outcomes with once-weekly subcutaneous semaglutide in the treatment of type 2 diabetes: Insights from the SUSTAIN 1--7 trials"), [Nauck & Meier 2019](https://www.gwern.net/docs/longevity/2019-nauck.pdf "Management Of Endocrine Disease: Are all GLP-1 agonists equal in the treatment of type 2 diabetes?"), [O’Neil et al 2018](https://www.gwern.net/docs/longevity/2018-oneil.pdf "Efficacy and safety of semaglutide compared with liraglutide and placebo for weight loss in patients with obesity: a randomized, double-blind, placebo and active controlled, dose-ranging, phase 2 trial"), [Blundell et al 2017](https://www.gwern.net/docs/longevity/2017-blundell.pdf "Effects of once-weekly semaglutide on appetite, energy intake, control of eating, food preference and body weight in subjects with obesity"), [Nauck et al 2016](https://www.gwern.net/docs/longevity/2016-nauck.pdf "A Phase 2, Randomized, Dose-Finding Study of the Novel Once-Weekly Human GLP-1 Analog, Semaglutide, Compared With Placebo and Open-Label Liraglutide in Patients With Type 2 Diabetes"), [Lau et al 2015](https://www.gwern.net/docs/longevity/2015-lau.pdf "Discovery of the Once-Weekly Glucagon-Like Peptide-1 \(GLP-1\) Analogue Semaglutide").

  * [“Lessons from the host defences of bats, a unique viral reservoir”](https://www.gwern.net/docs/biology/2020-irving.pdf), Irving et al 2021 ([bat-borne viruses](https://en.wikipedia.org/wiki/Bat-borne_virus); previously, [Trevor Klee](https://get21stnight.com/2020/03/30/why-do-we-keep-getting-diseases-from-bats/))

  * [“Beneficial & Detrimental Effects of Reactive Oxygen Species on Lifespan: A Comprehensive Review of Comparative & Experimental Studies”](https://www.frontiersin.org/articles/10.3389/fcell.2021.628157/full), Shields et al 2021 (antioxidants still aren’t the fountain of youth, and may be harmful; animal studies still frequently inconsistent)

  * [“Positive expectations predict improved mental-health outcomes linked to psychedelic microdosing”](https://www.nature.com/articles/s41598-021-81446-7), Kaertner et al 2021 (placebo)

  * [“The Effects of Fluoride in Drinking Water”](https://www.gwern.net/docs/iq/2021-aggeborn.pdf), Aggeborn & Öhman 2021

  * [“Sleep & Sex: What Can Go Wrong? A Review of the Literature on Sleep Related Disorders and Abnormal Sexual Behaviors & Experiences”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1978350/), Schenck et al 2007




## 2.6 Technology

  * [New X-Prize: $100m in prizes for Carbon Removal](https://www.xprize.org/prizes/elonmusk)

  * [Wringing gauge blocks](https://en.wikipedia.org/wiki/Gauge_block) (“With their precisely-flat metal faces, gauge blocks can be stuck together non-magnetically via a process calling ‘wringing’, requiring substantial effort to separate. Scientists are still uncertain exactly how wringing works.”)

  * [Armored train](https://en.wikipedia.org/wiki/Armoured_train)




## 2.7 Economics

  * [“Why did renewables become so cheap so fast? And what can we do to use this global opportunity for green growth?”](https://ourworldindata.org/cheap-renewables-growth), Max Roser (specifically, why such an extreme [experience curve](https://en.wikipedia.org/wiki/Experience_curve_effects)?)

  * [“IQ, trading behavior, and performance”](https://www.gwern.net/docs/iq/2012-grinblatt.pdf), Grinblatt et al 2012; [“Genetic Endowments and Wealth Inequality”](https://www.gwern.net/docs/economics/2020-barth.pdf), Barth et al 2020 (why, despite notorious setbacks, did Isaac Newton & LTCM’s founders die wealthy? Why, in general, are more intelligent people so much better investors? ‘The indifference of the indicator’: it’s not one thing, it’s everything—more intelligent people have lower discount rates, save more for longer & are less risk-averse, more accurately predict future growth or inflation, are more likely to participate in +EV opportunities like the stock market, to use low-fee rather than high-fee (and thus, underperforming) mutual funds, succumb less to biases like herding as they trade better & at better times, trade less, and harvest losses more efficiently when trading poorly.)




## 2.8 Philosophy

  * Are **ethics experts more ethical**? [“The Behavior of Ethicists”](https://www.gwern.net/docs/philo/2016-schwitzgebel.pdf), Schwitzgebel & Rust 2016 (most recently: [“The moral behavior of ethics professors: A replication-extension in German-speaking countries”](https://www.gwern.net/docs/philo/2019-schonegger.pdf), Schönegger et al 2019; given moral licensing & activism, perhaps we should be surprised we don’t hear about more ethicists doing things like posting enemy lists or trying to dox reviewers. “Woe to you Pharisees!”)

  * [“Meta-analysis on belief in free will manipulations”](https://psyarxiv.com/quwgr), Genschow et al 2021 (another noble lie turns out to be ignoble)

  * [Gricean maxims of communication](https://en.wikipedia.org/wiki/Cooperative_principle)




## 2.9 Fiction

  *  _[Bunnies& Burrows](https://en.wikipedia.org/wiki/Bunnies_%26_Burrows)_




## 2.10 Miscellaneous

  * [“Caesar Lives”](https://www.gwern.net/docs/history/1995-pop.pdf), [Iggy Pop](https://en.wikipedia.org/wiki/Iggy_Pop) 1995 (on [Gibbon](https://en.wikipedia.org/wiki/The_History_of_the_Decline_and_Fall_of_the_Roman_Empire))

  * [Mad honey](https://en.wikipedia.org/wiki/Grayanotoxin#Mad_honey_intoxication)

  * [Imperial Court System](https://en.wikipedia.org/wiki/Imperial_Court_System)




11

Share

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 Gwern Branwen · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
