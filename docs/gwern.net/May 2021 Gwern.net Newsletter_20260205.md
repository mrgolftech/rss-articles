# May 2021 Gwern.net Newsletter

**来源:** https://gwern.net
**链接:** https://gwern.substack.com/p/may-2021-gwernnet-newsletter
**日期:** Fri, 11 Jun 2021 14:16:22 GMT

---

[![Gwern.net Newsletter](https://substackcdn.com/image/fetch/$s_!rpC9!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5860611c-2de0-45a7-99a0-dc1b248b0199_1280x1280.png)](/)

# [Gwern.net Newsletter](/)

SubscribeSign in

# May 2021 Gwern.net Newsletter

### links on AI hardware, diffusion models, optogenetics, brain scanning.

[![gwern's avatar](https://substackcdn.com/image/fetch/$s_!jpKC!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3a41d1b8-0e3c-44d4-b99a-8f52362678eb_1592x1800.png)](https://substack.com/@gwern)

[gwern](https://substack.com/@gwern)

Jun 11, 2021

21

14

1

Share

May 2021’s [Gwern.net](https://www.gwern.net/newsletter/2021/05) [newsletter](https://gwern.substack.com) is now out; previous, [April 2021](https://www.gwern.net/newsletter/2021/04) ([archives](https://www.gwern.net/tags/newsletter)). This is a collation of links and summary of major changes, overlapping with my [Changelog](https://www.gwern.net/Changelog); brought to you by my donors on [Patreon](https://www.patreon.com/gwern).

Note: I will be in Denver 12–13 June 2021 for a conference.

# 1 Writings

  * **Proposal** : [“Choose Your Own Adventure AI Dungeon”](https://www.gwern.net/CYOA); [“Decision Transformers: Preference Learning As Simple As Possible”](https://www.gwern.net/GPT-2-preference-learning#decision-transformers-preference-learning-as-simple-as-possible)




# 2 Links

## 2.1 AI

[Matters Of Scale](https://old.reddit.com/r/mlscaling/):

  * **Hardware** :

    * [“Podracer architectures for scalable Reinforcement Learning”](https://arxiv.org/abs/2104.06272#deepmind), Hessel et al 2021 (highly-efficient TPU pod use: eg solving Pong in <1min at 43 million FPS on a TPUv3-2048); [“Google details new TPUv4 AI accelerator chips”](https://venturebeat.com/2021/05/18/google-details-new-ai-accelerator-chips/) (2.7× TPUv3 chips; up to TPUv4-4096 pods, yielding >1 ExaFLOPS; public access later in 2021)x

    * [“ZeRO-Infinity: Breaking the GPU Memory Wall for Extreme Scale Deep Learning”](https://arxiv.org/abs/2104.07857#microsoft), Rajbhandari et al 2021 (~1 trillion parameters per 16 GPUs/DGX-2-node, scaling to >512 GPUs ~40% efficiency)

    * [“GSPMD: General and Scalable Parallelization for ML Computation Graphs”](https://arxiv.org/abs/2105.04663#google), Xu et al 2021 (Google upgrade of [GPipe](https://arxiv.org/abs/1811.06965#google "'GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism', Huang et al 2018")/[GShard](https://arxiv.org/abs/2006.16668#google "'GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding', Lepikhin et al 2020") arch to match [MS DeepSpeed](https://www.microsoft.com/en-us/research/blog/deepspeed-extreme-scale-model-training-for-everyone/ "DeepSpeed: Extreme-scale model training for everyone"): “…50%–62% compute utilization on 128–2048 Cloud TPUv3 cores for models with up to one trillion parameters”)

    * [“DLRM: High-performance, Distributed Training of Large-scale Deep Learning Recommendation Models”](https://arxiv.org/abs/2104.05158#facebook), Mudigere et al 2021 (ZionEX software/hardware platform for training extremely large embeddings—while embeddings aren’t ‘real’ parameters & things like [DynamicEmbedding](https://arxiv.org/abs/2004.08366#google "'DynamicEmbedding: Extending TensorFlow for Colossal-Scale Applications', Zeng et al 2020") will never learn tricks like GPT-3 no matter how big, they present similar challenges); [“RecPipe: Co-designing Models and Hardware to Jointly Optimize Recommendation Quality and Performance”](https://arxiv.org/abs/2105.08820#facebook), Gupta et al 2021

  * [“From Motor Control to Team Play in Simulated Humanoid Football”](https://arxiv.org/abs/2105.12196#deepmind), Liu et al 2021 (curriculum training of a single NN from raw humanoid control to coordinated team-wide soccer strategy; neat to compare with [Hill et al 2020](https://arxiv.org/abs/2009.01719#deepmind "Grounded Language Learning Fast and Slow") in terms of agent abilities)

  * [“Wav2vec-U: Unsupervised Speech Recognition”](https://arxiv.org/abs/2105.11084#facebook), Baevski et al 2021

  * [“Anthropic” public-benefit-corp/startup launched](https://www.anthropic.com/news/announcement) (founded by the Amodeis; $124M investment for scaling “reliable and steerable AI systems”); [“Cooperative AI Foundation” (CAIF)](https://www.cooperativeai.com/foundation) launched

  * [“MLP-Mixer: An all-MLP Architecture for Vision”](https://arxiv.org/abs/2105.01601#google), Tolstikhin et al 2021 (another [FC paper](https://www.gwern.net/notes/FC) removing even more inductive biases—ponies are all you need: “Mixer [improves more rapidly with data](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) than ResNets, or even ViT, and the gap between large scale Mixer and ViT models shrinks until the performance is matched on the entire dataset…” The Bitter Lesson truly is the single bitterest lesson in ML, isn’t it? The more people tweet about how MLP-Mixer is overhyped because is −X% worse than the ultra-hand-optimized baseline or requires Y× more FLOPS, the more they demonstrate _precisely why_ this sort of research is so important! And showing, incidentally, that Transformers are still under-researched if such a fundamental fact could have been missed for so long.)

  * [“Data-Efficient Language-Supervised Zero-Shot Learning with Self-Distillation”](https://arxiv.org/abs/2104.08945#facebook), Cheng et al 2021 ([CLIP](https://openai.com/blog/clip/)-like performance scaled down to _n_ = 3m using [soft labels](https://arxiv.org/abs/1503.02531#google "'Distilling the knowledge in a neural network', Hinton et al 2015") generated by a [Conceptual Captions](https://www.gwern.net/docs/ai/2018-sharma.pdf#google "Conceptual Captions: A Cleaned, Hypernymed, Image Alt-text Dataset For Automatic Image Captioning")-pretrained model)

  * [“SR3: Image Super-Resolution via Iterative Refinement”](https://arxiv.org/abs/2104.07636#google), Saharia et al 2021; [“Diffusion Models Beat GANs on Image Synthesis”](https://arxiv.org/abs/2105.05233#openai), Dhariwal & Nichol 2021 ([DDPM](https://arxiv.org/abs/2006.11239 "'Denoising Diffusion Probabilistic Models', Ho et al 2020")^[1](file:///tmp/burlbC6ws6.html#fn1)^ finally surpass [BigGAN-deep](https://arxiv.org/abs/1809.11096#deepmind "'BigGAN: Large Scale GAN Training for High Fidelity Natural Image Synthesis', Brock et al 2018") on ImageNet 512px images at similar compute-cost, as [expected from their](https://arxiv.org/abs/2102.09672 "'Improved Denoising Diffusion Probabilistic Models', Nichol & Dhariwal 2021")[good scaling](https://www.gwern.net/notes/Scaling)); [“Cascaded Diffusion Models for High Fidelity Image Generation”](https://cascaded-diffusion.github.io/), Ho et al 2021

  * [“Learning to summarize from human feedback”](https://arxiv.org/abs/2009.01325#openai), Stiennon et al 2020

  * [“Grokking: Generalization Beyond Overfitting On Small Algorithmic Data Sets”](https://www.gwern.net/docs/ai/2021-power.pdf#openai), Power et al 2021 ([discussion](https://old.reddit.com/r/mlscaling/comments/n78584/grokking_generalization_beyond_overfitting_on/); new scaling effect, ‘grokking’: sudden perfect generalization emerging many epochs after training-set overfitting on algorithmic tasks when training in [flat shallow loss landscapes](https://www.gwern.net/docs/ai/2021-power-poster.png#openai)); [“Knowledge distillation: A good teacher is patient and consistent”](https://arxiv.org/abs/2106.05237#google), Beyer et al 2021 (training much smaller models merely requires hundreds of thousands or millions of epochs)

  * [“Scaling End-to-End Models for Large-Scale Multilingual ASR”](https://arxiv.org/abs/2104.14830#google), Li et al 2021

  * [“The Shape of Learning Curves: a Review”](https://arxiv.org/abs/2103.10948), Viering & Loog 2021

  * [“Reward is enough”](https://www.sciencedirect.com/science/article/pii/S0004370221000862#deepmind), Silver et al 2021 (a DRL manifesto: reward losses enough at scale of compute/parameters/tasks to induce all important capabilities like memory/exploration/generalization/imitation/reasoning)

  * **Scaling Down** : [`lazy`: a tool for running processes in idle time](https://github.com/nshepperd/lazy) (how to train on a GPU without destroying your GUI’s usability! `lazy` pauses runs briefly while you interact with your desktop, letting you do months-long runs without going crazy or resorting to Colab etc. This enables hobbyists to go after previously-infeasible model sizes); EleutherAI releases [a 6b-parameter GPT-3 model, GPT-J](https://arankomatsuzaki.wordpress.com/2021/06/04/gpt-j/) (are you still using GPT-2/GPT-Neo? upgrade!); [“Aggregating Nested Transformers”](https://arxiv.org/abs/2105.12723), Zhang et al 2021/[“Less is More: Pay Less Attention in Vision Transformers”](https://arxiv.org/abs/2105.14217), Pan et al 2021



  * [“ByT5: Towards a token-free future with pre-trained byte-to-byte models”](https://arxiv.org/abs/2105.13626#google), Xue et al 2021 (character models—not just feasible but desirable; we’ll get our rhyming & pun-making language models yet!)

  * [“Machine Learning Attacks Against the Asirra CAPTCHA”](https://www.gwern.net/docs/ai/2008-golle.pdf), Golle 2008 (a look back on a decade of CV progress: months of work for 80% cat vs dog with SVM ensembles in 2008; 5min in Fast.ai for 99% accuracy in 2018; for even more perspective, [Cireşan 2012](https://www.gwern.net/docs/ai/2012-ciresan.pdf "Deep big multilayer perceptrons for digit recognition"))




## 2.2 Genetics

Everything Is Heritable:

  * [“Bi-ancestral depression GWAS in the Million Veteran Program and meta-analysis in >1.2 million individuals highlight new therapeutic directions”](https://www.gwern.net/docs/genetics/heritable/2021-levey.pdf), Levey et al 2021

  * [“The complete sequence of a human genome”](https://www.biorxiv.org/content/10.1101/2021.05.26.445798v1), Nurk et al 2021 ([media](https://www.nature.com/articles/d41586-021-01506-w "A complete human genome sequence is close: how scientists filled in the gaps; researchers added 200 million DNA base pairs and 115 protein-coding genes — but they’ve yet to entirely sequence the Y chromosome"))

  * [“Using DNA to predict intelligence”](https://www.gwern.net/docs/iq/2021-vonstumm.pdf), von Stumm & Plomin 2021 (review)

  * [“Long read sequencing of 3,622 Icelanders provides insight into the role of structural variants in human diseases and other traits”](https://www.biorxiv.org/content/10.1101/848366v2.full), Beyter et al 2021

  * [“Rapid Sequencing–Based Diagnosis of Thiamine Metabolism Dysfunction Syndrome”](https://www.gwern.net/docs/genetics/heritable/2021-owen.pdf) (sequence everyone!)




Engineering:

  * [“Sense codon reassignment enables viral resistance and encoded polymer synthesis”](https://www.gwern.net/docs/genetics/editing/2021-robertson.pdf), Robertson et al 2021 (“ultra-safe cells”: synthesizing an entire E. coli genome with swapped codons for complete viral immunity)

  * [“In vivo CRISPR base editing of ](https://www.gwern.net/docs/genetics/editing/2021-musunuru.pdf)_[PCSK9](https://www.gwern.net/docs/genetics/editing/2021-musunuru.pdf)_[ durably lowers cholesterol in primates”](https://www.gwern.net/docs/genetics/editing/2021-musunuru.pdf), Musunuru et al 2021

  * **[Optogenetics](https://en.wikipedia.org/wiki/Optogenetics)** : [“Partial recovery of visual function in a blind patient after optogenetic therapy”](https://www.gwern.net/docs/genetics/editing/2021-sahel.pdf), Sahel et al 2021 ([media](https://www.statnews.com/2021/05/24/scientists-use-optogenetics-for-first-time-to-help-blind-patient-see/ "With engineered proteins, scientists use optogenetics for the first time to help a blind patient see again")); [“Wireless multilateral devices for optogenetic studies of individual and social behaviors”](https://www.gwern.net/docs/biology/2021-yang.pdf), Yang et al 2021 ([media](https://www.nytimes.com/2021/05/25/science/optogenetics-brain-social-behavior.html "Scientists Drove Mice to Bond by Zapping Their Brains With Light: The study, a tour de force in bioengineering, comes after 2 decades of research on brain-to-brain synchrony in people"))

  * [“Retron Library Recombineering (RLR): High-throughput functional variant screens via in vivo production of single-stranded DNA”](https://www.pnas.org/content/118/18/e2018181118), Schubert et al 2021

  * [“First genetically modified Oxitec mosquitoes released in the United States”](https://www.nature.com/articles/d41586-021-01186-6)

  * [“Genomic characterization of world’s longest selection experiment in mouse reveals the complexity of polygenic traits”](https://www.biorxiv.org/content/10.1101/2021.05.28.446207v1), Palma-Vera et al 2021

  * [“Surrogate broodstock to enhance biotechnology research and applications in aquaculture”](https://www.sciencedirect.com/science/article/pii/S0734975021000628), Jin et al 2021

  * [“Utility of polygenic embryo screening for disease depends on the selection strategy”](https://www.biorxiv.org/content/10.1101/2020.11.05.370478v3), Lencz et al 2021

  * [“Limit on lab-grown human embryos dropped by stem-cell body: The International Society for Stem Cell Research relaxed the famous 14-day rule on culturing human embryos in its latest research guidelines”](https://www.nature.com/articles/d41586-021-01423-y)

  * [“Useful Mutants, Bred With Radiation”](https://www.nytimes.com/2007/08/28/science/28crop.html) (on [atomic gardening](https://en.wikipedia.org/wiki/Atomic_gardening))




## 2.3 Statistics/Meta-Science

  * [“Correlated Failures” in HDDs/SSDs](https://blog.dshr.org/2021/03/correlated-failures.html)

  * [“How a Publicity Blitz Created The Myth of Subliminal Advertising”](https://www.gwern.net/docs/statistics/bias/1992-rogers.pdf), Rogers 1992 (the famous movie-theater/popcorn-sales experiment never happened)




## 2.4 Politics/Religion

  * [“Clarifying the Structure and Nature of Left-Wing Authoritarianism (LWA)”](https://www.gwern.net/docs/sociology/2021-costello.pdf), Costello et al 2021

  * [“Book Review: ](https://fantasticanachronism.com/2021/04/28/book-review-the-decline-and-fall-of-the-roman-empire/)_[The Decline and Fall of the Roman Empire](https://fantasticanachronism.com/2021/04/28/book-review-the-decline-and-fall-of-the-roman-empire/)_[”](https://fantasticanachronism.com/2021/04/28/book-review-the-decline-and-fall-of-the-roman-empire/) ([excerpts](https://fantasticanachronism.com/2021/05/03/highlights-from-the-decline-and-fall-of-the-roman-empire/))




## 2.5 Psychology/Biology

  * [“A connectomic study of a petascale fragment of human cerebral cortex”](https://www.biorxiv.org/content/10.1101/2021.05.29.446289v1), Shapson-Coe et al 2021 (“…This “digital tissue” is a ~660,000× scale up of an earlier saturated reconstruction from a small region of mouse cortex, published in 2015 ([Kasthuri et al 2015](https://www.sciencedirect.com/science/article/pii/S0092867415008247 "Saturated Reconstruction of a Volume of Neocortex")). Although this scaleup was difficult, it was not hundreds of thousands of times more difficult and took about the same amount of time as the previous data set (~4 years)…The rapid improvements over the past few years…argues that analyzing volumes that are even 3 orders of magnitude larger, such as an exascale whole mouse brain connectome, will likely be in reach within a decade." See also [“Accelerating progress in brain recording tech”](https://xcorr.net/2021/04/27/accelerating-progress-in-brain-recording-tech/).)

  * [“Neuroimaging evidence for a network sampling theory of individual differences in human intelligence test performance”](https://www.nature.com/articles/s41467-021-22199-9), Soreq et al 2021; [“The neural basis of intelligence in fine-grained cortical topographies”](https://elifesciences.org/articles/64058), Feilong et al 2021; [“Predicting intelligence from brain gray matter volume”](https://link.springer.com/article/10.1007/s00429-020-02113-7), Hilger et al 2020 (towards the mechanistic reification of _g_ : per [P-FIT](https://www.gwern.net/docs/iq/2007-jung.pdf "'The Parieto-Frontal Integration Theory \(P-FIT\) of intelligence: Converging neuroimaging evidence', Jung & Haier 2007"), it is global efficiency/total cognitive resources which can be spent on learning & orchestrating specialized capabilities); if we consider recent human brain imaging studies, cross-species comparisons, and deep learning as converging, I would offer as a speculation the following:

The Master Synthesis: intelligence is execution of small simplicity-weighted programs, best discovered by search over smooth loss landscapes like that of [highly-overparameterized](https://www.gwern.net/notes/Sparsity) differentiable networks containing lottery-ticket subnetworks which are ensembled/averaged over, [approaching Bayes-optimal](https://www.gwern.net/Backstop#deep-bayes) reasoning in the limit (as nearest-neighbors-like high dimensional interpolation / memorization gives way to algorithmic generalization / interpolation on a more abstract level); this can be implemented by large numbers of similar neurons trained using any of the many approximations to backprop; human intelligence’s _g_ is real but is the overall ‘pool’ of neural resources which derives from overall body integrity because the number of neurons, their density, their myelination, resistance to damage and infection etc, is causally downstream of all body and developmental systems, creating a huge mutational target; the brain regions specialize and differentiate, and their orchestration (or lack thereof) contributes to observed performance on tasks tapping into multiple specialized regions; as tasks rely on fewer regions or approach intrinsic ceiling, _g_ ceases to be observable and task-specific influences matter most.

  * [“MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 study”](https://www.nature.com/articles/s41591-021-01336-3), Mitchell et al 2021 (_d_ = 0.9 over therapy); [“Effects of Psilocybin-Assisted Therapy on Major Depressive Disorder”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7643046/), Davis et al 2021

  * [“Why Animals Don’t Get Lost: Birds do it. Bees do it. Learning about the astounding navigational feats of wild creatures can teach us a lot about where we’re going”](https://www.newyorker.com/magazine/2021/04/05/why-animals-dont-get-lost) (on spectacular but still mysterious feats of [animal navigation](https://en.wikipedia.org/wiki/Animal_navigation))

  * [“In The Future Of Collecting, Is Anyone Having Fun?”](https://defector.com/in-the-future-of-collecting-is-anyone-having-fun/) (on [Bobblehead](https://en.wikipedia.org/wiki/Bobblehead) collectors)

  * [“Linking Brain Biology to Intellectual Endowment: A Review on the Associations of Human Intelligence With Neuroimaging Data”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8114859/), Dizaji et al 2021

  * [“The Best And The Rest: Revisiting The Norm Of Normality Of Individual Performance”](https://www.gwern.net/docs/economics/2012-oboyle.pdf), O’Boyle & Aguinis 2012 (performance is [log-normal](https://www.gwern.net/notes/Pipeline))

  * [“A conserved strategy for inducing appendage regeneration”](https://www.biorxiv.org/content/10.1101/2020.11.21.392720v1), Abrams et al 2021 (slight regrowth of damaged mouse limbs by drinking sugar+amino-acid-supplemented water)

  * [“Know Your Amphetamines”](https://astralcodexten.substack.com/p/know-your-amphetamines), Scott Alexander

  * [“Feeling Small: Exploring the Tactile Perception Limits [of Humans]”](https://www.nature.com/articles/srep02617), Skedung et al 2013

  * [“The Board Game of the Alpha Nerds: Before ](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[Risk](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[, before ](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[Dungeons& Dragons](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[, before ](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[Magic: The Gathering](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[, there was ](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[Diplomacy](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)")_[”](http://grantland.com/features/diplomacy-the-board-game-of-the-alpha-nerds/ "One writer enters international competition to play the world-conquering game that redefines what it means to be a geek \(and a person\)") ([WP](https://en.wikipedia.org/wiki/Diplomacy_\(game\)); “I still don’t know whom I should have trusted, if anyone. All I know is that I felt stupid, stressed out, humiliated, and sad.”)




## 2.6 Technology

  * [“I walk the (beta-stability) line: How counting neutrons explains nuclear waste”](https://rootsofprogress.org/nuclear-physics)

  * [“Making is Show Business now”](https://alexdanco.com/2020/10/08/making-is-show-business-now/), Alex Danco

  * [“Shop Class as Soulcraft: The case for the manual trades”](https://www.thenewatlantis.com/publications/shop-class-as-soulcraft), Crawford 2006

  * [“Spintronics: Build mechanical circuits”](https://www.kickstarter.com/projects/upperstory/spintronics-build-mechanical-circuits), Kickstarter (followup to [Turing Tumble](https://en.wikipedia.org/wiki/Turing_Tumble))




## 2.7 Economics

  * [“RCTs to Scale: Comprehensive Evidence from 2 Nudge Units”](https://www.gwern.net/docs/sociology/2020-dellavigna.pdf), DellaVigna & Linos 2020 (nudge effects overestimated by 6.2× due to publication bias)

  * [“No causal associations between childhood family income and subsequent psychiatric disorders, substance misuse and violent crime arrests: a nationwide Finnish study of >650,000 individuals and their siblings”](https://academic.oup.com/ije/advance-article/doi/10.1093/ije/dyab099/6288123), Sariaslan et al 2021; [“Parental income and mental disorders in children and adolescents: prospective register-based study”](https://academic.oup.com/ije/advance-article/doi/10.1093/ije/dyab066/6274255), Kinge et al 2021

  * [“Everything You Might Want to Know about Whaling”](https://mattlakeman.org/2021/06/01/everything-you-might-want-to-know-about-whaling/), Matt Lakeman

  * [Exploding Nash Equilibrium For Trustless Trade](https://www.gwern.net/notes/Nash)




## 2.8 Fiction

  * [“Love Is the Plan the Plan Is Death”](https://www.lightspeedmagazine.com/fiction/love-is-the-plan-the-plan-is-death/), [James Tiptree, Jr.](https://en.wikipedia.org/wiki/James_Tiptree_Jr.) ([WP](https://en.wikipedia.org/wiki/Love_Is_the_Plan_the_Plan_Is_Death))




## 2.9 Miscellaneous

  * [“The Strange Story of Dagobert, the ](https://www.newyorker.com/news/dispatch/the-strange-story-of-dagobert-the-ducktales-bandit)_[Duck Tales](https://www.newyorker.com/news/dispatch/the-strange-story-of-dagobert-the-ducktales-bandit)_[ Bandit: In the ’90s, a frustrated artist in Berlin went on a crime spree—building bombs, extorting high-end stores, and styling his persona after Scrooge McDuck. He soon became a German folk hero.”](https://www.newyorker.com/news/dispatch/the-strange-story-of-dagobert-the-ducktales-bandit) ([WP](https://en.wikipedia.org/wiki/Arno_Funke); another reminder for Americans—odd as it may seem, Donald Duck is _extremely_ popular overseas; see also the unknown-in-the-USA character [John D. Rockerduck](https://en.wikipedia.org/wiki/John_D._Rockerduck) or [beloved Scandinavian tradition](https://slate.com/culture/2009/12/sweden-s-bizarre-tradition-of-watching-donald-duck-kalle-anka-cartoons-on-christmas-eve.html) _[From All of Us to All of You](https://en.wikipedia.org/wiki/From_All_of_Us_to_All_of_You)_ who 2020 airing set an all-time record of >4.5m viewers)

  * [List of atmospheric optical phenomena](https://en.wikipedia.org/wiki/Atmospheric_optics#List) (How many would you recognize from a distance or plane? How many have you even heard of?)

  * [Baron Franz Nopcsa von Felső-Szilvás](https://en.wikipedia.org/wiki/Franz_Nopcsa_von_Fels%C5%91-Szilv%C3%A1s) (noted geologist, paleontologist, anthropologist, homosexual, & skyjacker)

  * [Krishnacore](https://en.wikipedia.org/wiki/Krishnacore)




* * *

  1. What is a diffusion model like DDPM? To try to explain it as simply as possible [without the math](https://yang-song.github.io/blog/2021/score/ "Generative Modeling by Estimating Gradients of the Data Distribution"):

DDPM is a neural net which is trained to fix noise in an image: it takes a noisy image and ‘sharpens’ it to produce a new image. You train it by adding dirt to a normal image, and teaching it to turn the dirty version into the original. As it gets better, it learns what the images all tend to look like so it can ‘see through’ ever more noise, to turn smudged hints of the original image into its best guess. Once it’s done training, what happens if you give it a completely dirty photo, which is pure static noise? Well, it produces a slightly less dirty ‘photo’. And if you do it again? it’s a little cleaner still. Now, what if you do this many times? It has to get cleaner each time. The end result: the static noise goes in, and a face pops out! The DDPM has hallucinated a face out of the noise. One little blob of static here turned into a nose, and another blob turned into an ear, and it went from there.




21

14

1

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Jetbat's avatar](https://substackcdn.com/image/fetch/$s_!-1i6!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4f2bae36-9707-446a-9c17-046f81f4f95e_144x144.png)](https://substack.com/profile/42260476-jetbat?utm_source=comment)

[Jetbat](https://substack.com/profile/42260476-jetbat?utm_source=substack-feed-item)

[Jul 20, 2022](https://gwern.substack.com/p/may-2021-gwernnet-newsletter/comment/7863789 "Jul 20, 2022, 6:06 PM")

I miss these

ReplyShare

[![Josh F's avatar](https://substackcdn.com/image/fetch/$s_!bXMT!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F46ab5038-0d40-4ce0-875e-0797dc001b6d_400x400.jpeg)](https://substack.com/profile/3428556-josh-f?utm_source=comment)

[Josh F](https://substack.com/profile/3428556-josh-f?utm_source=substack-feed-item)

[Sep 22, 2021](https://gwern.substack.com/p/may-2021-gwernnet-newsletter/comment/2995126 "Sep 22, 2021, 3:58 AM")

hey, are the newsletters not going out on substack these days? didn't get june / july / august

ReplyShare

[3 replies](https://gwern.substack.com/p/may-2021-gwernnet-newsletter/comment/2995126)

[12 more comments...](https://gwern.substack.com/p/may-2021-gwernnet-newsletter/comments)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 Gwern Branwen · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture




This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts 
