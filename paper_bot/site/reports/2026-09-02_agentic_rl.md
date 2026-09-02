# RL / Post-Training / Agentic RL Reading Queue - 2026-09-02

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 523. Minimum score: 8.

## Top Picks

### 68 - Group Adaptive Clipping Policy Optimization

- arXiv: [2609.00444](https://arxiv.org/abs/2609.00444) | [PDF](https://arxiv.org/pdf/2609.00444) | [papers.cool](https://papers.cool/arxiv/2609.00444)
- Authors: Sheng Jia, Xiao Wang, Shiva Prasad Kasiviswanathan, Rein Houthooft
- Published: 2026-08-31 22:32 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +2 more; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Group relative policy optimization for reinforcement learning with verifiable rewards (RLVR) typically uses a fixed importance-sampling (IS) ratio clipping boundary across all rollouts. We identify a key limitation: rare correct rollouts on harder problems and abundant correct rollouts on easier problems are clipped...

### 55 - ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning

- arXiv: [2609.01058](https://arxiv.org/abs/2609.01058) | [PDF](https://arxiv.org/pdf/2609.01058) | [papers.cool](https://papers.cool/arxiv/2609.01058)
- Authors: Fanrui Zhang, Ruixue Ding, Qiang Zhang, Xi Chen, Boli Chen, Shihang Wang, et al. (16 authors)
- Published: 2026-09-01 10:54 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning, rollout; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics. Moreover, even near the model's capability boundary, long-horizon open-ended agentic tasks often yield brittle and unstable rewards, resulting in weak or noisy rollout contrast that...

### 53 - Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents

- arXiv: [2609.01245](https://arxiv.org/abs/2609.01245) | [PDF](https://arxiv.org/pdf/2609.01245) | [papers.cool](https://papers.cool/arxiv/2609.01245)
- Authors: Liming Pu, Xiaoxia Li, Yifu Liu, Teng Cao, Bin Yang
- Published: 2026-09-01 13:44 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic rl, multi-agent, agent orchestration; rl_post_training: reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: memory, benchmark
- Abstract skim: Reinforcement learning is a natural way to post-train LLM agents for long-horizon interactive tasks judged only by end-of-task verification, yet a shared belief holds that outcome-only RL soon hits a ceiling on small open models. Recent work therefore compensates around the training with denser rewards, SFT priors,...

### 48 - Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO

- arXiv: [2609.00925](https://arxiv.org/abs/2609.00925) | [PDF](https://arxiv.org/pdf/2609.00925) | [papers.cool](https://papers.cool/arxiv/2609.00925)
- Authors: Prakhar Gupta, Vaibhav Gupta
- Published: 2026-09-01 08:49 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, grpo, dpo
- Abstract skim: Language models can ignore prompt evidence when it conflicts with memorized knowledge. Post-training can make models follow such evidence more reliably, but it is unclear whether these gains require new machinery or strengthen machinery already present. We compare nine post-training arms spanning GRPO, SFT, and DPO...

### 47 - From Rollouts to Recipes: Self-Contained Post-Training for LLMs

- arXiv: [2609.01422](https://arxiv.org/abs/2609.01422) | [PDF](https://arxiv.org/pdf/2609.01422) | [papers.cool](https://papers.cool/arxiv/2609.01422)
- Authors: Yifei Li, Lingling Zhang, Muye Huang, Zihan Ma, Jiashuai Liu, Jun Liu
- Published: 2026-09-01 15:36 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Post-training large language models usually applies a single training recipe to all samples, even though the model's own rollouts reveal different sample-level learning states. We propose Self-Routing, a behavior-conditioned post-training framework that uses rollout correctness and confidence to decide how each...

### 45 - Reinforcement Learning Enhanced LLM Agents for Complex Vehicle Routing Problems

- arXiv: [2609.00859](https://arxiv.org/abs/2609.00859) | [PDF](https://arxiv.org/pdf/2609.00859) | [papers.cool](https://papers.cool/arxiv/2609.00859)
- Authors: Yi Chen, Zikang Yu, Jiahai Wang, Jinbiao Chen, Jianpeng Zhou, Zizhen Zhang
- Published: 2026-09-01 07:56 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Vehicle Routing Problems (VRPs) are fundamental combinatorial optimization problems with widespread applications in various scenarios. The advanced optimization solvers can effectively solve such problems. However, modeling complex VRP variants for solvers often requires substantial domain expertise, which limits...

### 43 - Instella-MoE Technical Report

- arXiv: [2609.00791](https://arxiv.org/abs/2609.00791) | [PDF](https://arxiv.org/pdf/2609.00791) | [papers.cool](https://papers.cool/arxiv/2609.00791)
- Authors: Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra, Yonatan Dukler, Gowtham Ramesh, Jialian Wu, et al. (13 authors)
- Published: 2026-09-01 06:38 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, preference optimization; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: In this work, we introduce Instella-MoE, a fully open Mixture-of-Experts (MoE) language model with 16 billion total parameters and 2.8 billion active parameters per token, trained entirely from scratch on AMD Instinct MI300X and MI325X GPUs. Instella-MoE combines a sparsely activated MoE design with architectural...

### 41 - Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning

- arXiv: [2609.00213](https://arxiv.org/abs/2609.00213) | [PDF](https://arxiv.org/pdf/2609.00213) | [papers.cool](https://papers.cool/arxiv/2609.00213)
- Authors: Yu Yuan, Yaoyou Fan, Lili Zhao, Guangting Zheng, Kai Zhang, Lu Pan, et al. (8 authors)
- Published: 2026-08-31 18:24 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo, ppo; reasoning: reasoning
- Abstract skim: Reinforcement learning fine-tuning of large language models increasingly adopts multiple reward dimensions, including verifiable rules, task-specific evaluators, and learned reward models, to provide richer supervision across diverse capabilities. These dimensions are commonly scalarized with fixed aggregation...

### 39 - Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning

- arXiv: [2609.00879](https://arxiv.org/abs/2609.00879) | [PDF](https://arxiv.org/pdf/2609.00879) | [papers.cool](https://papers.cool/arxiv/2609.00879)
- Authors: Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee, Fahad Khalid, Mourad Oussalah
- Published: 2026-09-01 08:11 UTC | Categories: cs.AI
- Why it matched: rl_post_training: preference optimization, dpo; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Reliable disaster damage assessment requires models that provide both accurate predictions and transparent explanations. However, existing multimodal approaches are limited by scarce annotated data and insufficient evaluation of reasoning quality. This study proposes a two-stage training framework that integrates...

### 37 - From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers the Corporate Request Mix

- arXiv: [2609.01572](https://arxiv.org/abs/2609.01572) | [PDF](https://arxiv.org/pdf/2609.01572) | [papers.cool](https://papers.cool/arxiv/2609.01572)
- Authors: Olga Tsymboi, Dmitrii Stoianov, Ramil Latypov, Danil Taranets, Daniil Dryabin, Mikhail Gashkov, et al. (14 authors)
- Published: 2026-09-01 17:39 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning; downranked: traffic
- Abstract skim: Data-residency constraints force enterprises to self-host LLMs, but continuous adoption of newer models without decommissioning their predecessors expands the serving fleet, fragmenting a finite GPU pool. We consolidate traffic from over 200 internal applications onto a single model by closing quality gaps...

### 37 - From Base Rollouts to RL Reasoning: A Budgeted Search Perspective

- arXiv: [2609.01274](https://arxiv.org/abs/2609.01274) | [PDF](https://arxiv.org/pdf/2609.01274) | [papers.cool](https://papers.cool/arxiv/2609.01274)
- Authors: Wenhe Sun, Cunxiang Wang, Zijun Yao, Yixin Cao
- Published: 2026-09-01 14:08 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning, but how these gains relate to inference-time decoding and search remains unclear. Does RL create reasoning the base model lacks, or shift the rollout distribution toward trajectories it can already reach but rarely samples? We...

### 36 - NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games

- arXiv: [2609.01549](https://arxiv.org/abs/2609.01549) | [PDF](https://arxiv.org/pdf/2609.01549) | [papers.cool](https://papers.cool/arxiv/2609.01549)
- Authors: Tomáš Holeček, Viliam Lisý
- Published: 2026-09-01 17:15 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark
- Abstract skim: Model-based reinforcement learning (MBRL) has achieved remarkable results in single-agent domains, yet its extension to competitive imperfect information games (IIGs) remains underexplored. In multi-agent settings, opponent-induced non-stationarity complicates the learning process, and decentralized model learning...

### 35 - CARE: Contrastive Anchor-based Rubric Evolution for Large Language Model Post-Training

- arXiv: [2609.00892](https://arxiv.org/abs/2609.00892) | [PDF](https://arxiv.org/pdf/2609.00892) | [papers.cool](https://papers.cool/arxiv/2609.00892)
- Authors: Siyuan Li, Xinxin Song, Chen Ruinian, Jingjing Fan, Tingxiong Xiao, Yangen Hu, et al. (8 authors)
- Published: 2026-09-01 08:22 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: Rubric-based reinforcement learning decomposes open-ended instructions into prompt-specific, flexible rubrics, making it better suited than reinforcement learning with verifiable rewards for post-training LLMs on open-ended tasks. However, static rubrics are inevitably hacked as the policy evolves, and existing...

### 33 - CRAFT: Fine-Tuning Pre-hoc Explainability in AI-native 6G RAN

- arXiv: [2609.00590](https://arxiv.org/abs/2609.00590) | [PDF](https://arxiv.org/pdf/2609.00590) | [papers.cool](https://papers.cool/arxiv/2609.00590)
- Authors: Pranshav Gajjar, Vijay K Shah
- Published: 2026-09-01 02:30 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: The next generation of mobile networks is envisioned as fully AI-native, with AI-RAN architectures embedding small language models (SLMs) to perform reasoning over real-time telemetry. The state-of-the-art training paradigms for telecom LLMs, exemplified by RANSTRUCT-style supervised fine-tuning (SFT) on curated...

### 32 - VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models

- arXiv: [2609.01325](https://arxiv.org/abs/2609.01325) | [PDF](https://arxiv.org/pdf/2609.01325) | [papers.cool](https://papers.cool/arxiv/2609.01325)
- Authors: Zhiqi Huang, Vivek Datla, Zhichao Xu, Puxuan Yu, Vivek Srikumar, Alfy Samuel
- Published: 2026-09-01 14:43 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr, verifiable reward
- Abstract skim: Neural ranking models have become core components of modern information retrieval systems and important building blocks of AI systems such as retrieval-augmented generation (RAG) pipelines. However, their robustness remains insufficiently understood in the presence of large language models (LLMs), which can generate...

### 32 - Accelerating Reinforcement Learning via MPC Solver-Gradient Guidance for Weights-varying MPC

- arXiv: [2609.01061](https://arxiv.org/abs/2609.01061) | [PDF](https://arxiv.org/pdf/2609.01061) | [papers.cool](https://papers.cool/arxiv/2609.01061)
- Authors: Baha Zarrouki, Arslan Thobani, Jasper Hoffmann, Mattia Piccinini, Rudolf Reiter, Felix Jahncke, et al. (9 authors)
- Published: 2026-09-01 10:55 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: In Model Predictive Control (MPC), cost-function weights shape closed-loop behavior, yet changing conditions often make fixed parametrizations suboptimal and motivate context-dependent online adaptation. Learning such policies is difficult because behavior depends implicitly on numerical MPC solutions, producing...

### 32 - SFAD: Speculative Factuality-Aware Decoding

- arXiv: [2609.00796](https://arxiv.org/abs/2609.00796) | [PDF](https://arxiv.org/pdf/2609.00796) | [papers.cool](https://papers.cool/arxiv/2609.00796)
- Authors: Guanqiao Chen, Di Wang, Lijie Hu
- Published: 2026-09-01 06:46 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, preference optimization
- Abstract skim: As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive applications. This task is particularly challenging as it requires balancing factual consistency with generation efficiency. Contrastive decoding methods require dual...

### 31 - GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning

- arXiv: [2609.00577](https://arxiv.org/abs/2609.00577) | [PDF](https://arxiv.org/pdf/2609.00577) | [papers.cool](https://papers.cool/arxiv/2609.00577)
- Authors: Wenjian Wu, Zesheng Jia, Jiaying Tang, Benyuan Yang, Jin Wang
- Published: 2026-09-01 02:14 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: Multi-agent combinatorial optimization problems are notoriously challenging due to their NP-hard nature. Recent parallel autoregressive neural solvers improve inference efficiency by allowing agents to make decisions simultaneously, but their performance often degrades on large-scale instances. This is largely...

### 30 - Independent Reinforcement Learning in Discounted Markov Games

- arXiv: [2609.00504](https://arxiv.org/abs/2609.00504) | [PDF](https://arxiv.org/pdf/2609.00504) | [papers.cool](https://papers.cool/arxiv/2609.00504)
- Authors: Asrin Efe Yorulmaz, Ugur Aydin, Tamer Basar
- Published: 2026-09-01 00:07 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: In this work, we study radically uncoupled learning in discounted general-sum Markov games. Assuming ``$\mathsf{ETH}$ for $\mathsf{PPAD}$", we show that, for every fixed discount factor, there is no polynomial-time algorithm for computing inverse-polynomially accurate coarse correlated equilibria in discounted...

### 30 - Provably Efficient Federated Reinforcement Learning with Linear Function Approximation and Logarithmic Communication Cost

- arXiv: [2609.00193](https://arxiv.org/abs/2609.00193) | [PDF](https://arxiv.org/pdf/2609.00193) | [papers.cool](https://papers.cool/arxiv/2609.00193)
- Authors: Zihang Liang, Haochen Zhang, Lingzhou Xue
- Published: 2026-08-31 18:11 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: We study federated online reinforcement learning with linear function approximation. While recent multi-agent reinforcement learning algorithms achieve strong regret guarantees, they typically require sharing raw trajectories. This reliance incurs a communication cost that scales linearly with the number of episodes...

### 30 - AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes

- arXiv: [2609.00052](https://arxiv.org/abs/2609.00052) | [PDF](https://arxiv.org/pdf/2609.00052) | [papers.cool](https://papers.cool/arxiv/2609.00052)
- Authors: Xun Wang, Bihe Zhao, Michael Backes, Franziska Boenisch, Adam Dziedzic
- Published: 2026-08-30 08:22 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training
- Abstract skim: Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to save deployment costs. All existing audits decide backbone identity from the text-output channel, which is structurally fragile for agentic APIs because modern serving...

### 29 - Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall

- arXiv: [2609.01532](https://arxiv.org/abs/2609.01532) | [PDF](https://arxiv.org/pdf/2609.01532) | [papers.cool](https://papers.cool/arxiv/2609.01532)
- Authors: Jacqueline He, Howard Yen, Shuyue Stella Li, Margaret Li, Hanqing Zeng, Yinglong Xia, et al. (12 authors)
- Published: 2026-09-01 17:00 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD...

### 28 - Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR

- arXiv: [2609.01354](https://arxiv.org/abs/2609.01354) | [PDF](https://arxiv.org/pdf/2609.01354) | [papers.cool](https://papers.cool/arxiv/2609.01354)
- Authors: Esther Xin
- Published: 2026-09-01 14:57 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) and standard benchmark evaluation both rely on an automatic verifier that turns a free text answer into a binary reward. Prior work reports that one evaluation harness accepts only about 94% of its own ground truth answers, blaming LaTeX parsing. That is an...

### 26 - Post-Training Science for Supervised Fine-Tuning

- arXiv: [2609.01244](https://arxiv.org/abs/2609.01244) | [PDF](https://arxiv.org/pdf/2609.01244) | [papers.cool](https://papers.cool/arxiv/2609.01244)
- Authors: Charles O'Neill, Mudith Jayasekara, Harry Partridge
- Published: 2026-09-01 13:44 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: evaluation
- Abstract skim: Every supervised fine-tuning run forces the same chain of decisions, such as learning rate, batch size, LoRA or full fine-tuning, how many epochs, which optimiser, and what data to feed the model. Each of these is typically rediscovered from scratch for every new model and dataset. Here we measure them under one...

### 26 - It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning

- arXiv: [2609.00638](https://arxiv.org/abs/2609.00638) | [PDF](https://arxiv.org/pdf/2609.00638) | [papers.cool](https://papers.cool/arxiv/2609.00638)
- Authors: Runpeng Dai, Kaili Huang, Changsung Kang, Ciya Liao
- Published: 2026-09-01 03:17 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo; memory_and_benchmarks: benchmark
- Abstract skim: Retrieval is the first stage of modern search and advertising systems, selecting a candidate set from a large item universe for downstream ranking and auction. Recent work increasingly leverages LLMs to improve retrieval through query expansion, data synthesis, and retrieval-feedback training. However, the...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
