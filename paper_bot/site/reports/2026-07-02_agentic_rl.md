# RL / Post-Training / Agentic RL Reading Queue - 2026-07-02

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 337. Minimum score: 8.

## Top Picks

### 71 - Active-GRPO: Adaptive Imitation and Self-Improving Reasoning for Molecular Optimization

- arXiv: [2607.00531](https://arxiv.org/abs/2607.00531) | [PDF](https://arxiv.org/pdf/2607.00531) | [papers.cool](https://papers.cool/arxiv/2607.00531)
- Authors: Xuefeng Liu, Mingxuan Cao, Qinan Huang, Thomas Brettin, Rick Stevens, Le Cong
- Published: 2026-07-01 07:22 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: evaluation
- Abstract skim: Scientific reasoning is an increasingly important capability of large language models, yet improving the robustness and efficiency of training such reasoning remains a key open challenge. We study this problem in instruction-based molecular optimization, where answer-only supervised fine-tuning (SFT) collapses...

### 50 - Flow-Map GRPO: Reinforcement Learning for Few-Step Flow-Map Generators via Anchored Stochastic Composition

- arXiv: [2607.00535](https://arxiv.org/abs/2607.00535) | [PDF](https://arxiv.org/pdf/2607.00535) | [papers.cool](https://papers.cool/arxiv/2607.00535)
- Authors: Zhiqi Li, Wen Zhang, Bo Zhu
- Published: 2026-07-01 07:25 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; memory_and_benchmarks: evaluation
- Abstract skim: Few-step flow-map generators, such as consistency models and MeanFlow, accelerate sampling by directly learning long-range transport maps between noise and data. However, these models are typically deterministic, which makes them difficult to optimize with reinforcement learning (RL) post-training methods that...

### 49 - Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination

- arXiv: [2607.00924](https://arxiv.org/abs/2607.00924) | [PDF](https://arxiv.org/pdf/2607.00924) | [papers.cool](https://papers.cool/arxiv/2607.00924)
- Authors: Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal, Markus J. Buehler
- Published: 2026-07-01 13:26 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether...

### 44 - Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training

- arXiv: [2607.01232](https://arxiv.org/abs/2607.01232) | [PDF](https://arxiv.org/pdf/2607.01232) | [papers.cool](https://papers.cool/arxiv/2607.01232)
- Authors: Zijian Zhang, Rizhen Hu, Athanasios Glentis, Dawei Li, Chung-Yiu Yau, Hongzhou Lin, et al. (7 authors)
- Published: 2026-07-01 17:59 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; planning_and_action: decision making
- Abstract skim: Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes...

### 37 - Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use

- arXiv: [2607.01084](https://arxiv.org/abs/2607.01084) | [PDF](https://arxiv.org/pdf/2607.01084) | [papers.cool](https://papers.cool/arxiv/2607.01084)
- Authors: Song-Lin Lv, Weiming Wu, Rui Zhu, Zi-Jian Cheng, Lan-Zhe Guo
- Published: 2026-07-01 15:40 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets, and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use Agent in Open-World), a problem...

### 37 - VideoSearch-R1: Iterative Video Retrieval and Reasoning via Soft Query Refinement

- arXiv: [2607.00446](https://arxiv.org/abs/2607.00446) | [PDF](https://arxiv.org/pdf/2607.00446) | [papers.cool](https://papers.cool/arxiv/2607.00446)
- Authors: Seohyun Lee, Seoung Choi, Dohwan Ko, Jongha Kim, Hyunwoo J. Kim
- Published: 2026-07-01 04:59 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: As video corpora continue to expand in both scale and task complexity, there is increasing demand for approaches that retrieve relevant videos from large-scale corpora (inter-video reasoning) and subsequently perform fine-grained, query-conditioned tasks (intra-video reasoning) within the retrieved content, such as...

### 35 - Staleness-Learning Rate Scaling Laws for Asynchronous RLHF

- arXiv: [2607.01083](https://arxiv.org/abs/2607.01083) | [PDF](https://arxiv.org/pdf/2607.01083) | [papers.cool](https://papers.cool/arxiv/2607.01083)
- Authors: Jingwei Song, Haofeng Xu, Jie Xiao, Chengke Bao, Jingwei Shi, Pengbin Feng, et al. (11 authors)
- Published: 2026-07-01 15:40 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: rlhf, policy optimization, grpo; planning_and_action: rollout
- Abstract skim: High-throughput RLHF systems often decouple rollout generation from policy optimization, leading to the use of stale rollouts during learner updates. In this work, we study the effect of such staleness in asynchronous GRPO. We make the behavior policy explicit in the GRPO surrogate objective and distinguish between...

### 32 - GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity

- arXiv: [2607.00152](https://arxiv.org/abs/2607.00152) | [PDF](https://arxiv.org/pdf/2607.00152) | [papers.cool](https://papers.cool/arxiv/2607.00152)
- Authors: Yong Yi Bay, Kathleen A. Yearick
- Published: 2026-06-30 20:28 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo
- Abstract skim: Three of the most popular methods for training language models to reason look like three different tricks. They are not. All three adjust a single number: standard deviation, reflecting how much a prompt's sampled answers disagree. When such a model is trained, it answers each problem many times, and an automatic...

### 31 - MemSyco-Bench: Benchmarking Sycophancy in Agent Memory

- arXiv: [2607.01071](https://arxiv.org/abs/2607.01071) | [PDF](https://arxiv.org/pdf/2607.01071) | [papers.cool](https://papers.cool/arxiv/2607.01071)
- Authors: Zhishang Xiang, Zerui Chen, Yunbo Tang, Zhimin Wei, Ruqin Ning, Yujie Lin, et al. (8 authors)
- Published: 2026-07-01 15:30 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; reasoning: reasoning; planning_and_action: decision making; memory_and_benchmarks: memory, benchmark
- Abstract skim: Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of...

### 29 - Diffusion-GR2: Diffusion Generative Reasoning Re-ranker

- arXiv: [2607.01170](https://arxiv.org/abs/2607.01170) | [PDF](https://arxiv.org/pdf/2607.01170) | [papers.cool](https://papers.cool/arxiv/2607.01170)
- Authors: Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, Mingfu Liang, Xiaohan Wei, Yunchen Pu, et al. (15 authors)
- Published: 2026-07-01 17:02 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Generative reasoning re-rankers achieve strong recommendation accuracy by emitting a chain-of-thought before re-ordering a candidate list, but they are slow at inference: an autoregressive (AR) decoder spends one sequential forward pass per reasoning token, and the reasoning trace far exceeds the ranking it...

### 29 - CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models

- arXiv: [2607.00862](https://arxiv.org/abs/2607.00862) | [PDF](https://arxiv.org/pdf/2607.00862) | [papers.cool](https://papers.cool/arxiv/2607.00862)
- Authors: Qizhi Jiang, Shuo Wang, Pei Ke, Yuhang Song, Ke Qin
- Published: 2026-07-01 12:27 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: preference optimization; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by leveraging long chain-of-thought (CoT) trajectories, yet they frequently exhibit overthinking on simple queries, resulting in significant token overhead and reduced inference efficiency. However, existing compression methods...

### 29 - VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning

- arXiv: [2607.00483](https://arxiv.org/abs/2607.00483) | [PDF](https://arxiv.org/pdf/2607.00483) | [papers.cool](https://papers.cool/arxiv/2607.00483)
- Authors: Kuan-Chen Chen, Winston Chen, Wei-Fang Sun, Min-Chun Hu
- Published: 2026-07-01 06:11 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, reward model; planning_and_action: decision making; memory_and_benchmarks: evaluation
- Abstract skim: Designing effective reward functions remains a major challenge in reinforcement learning (RL), particularly in open-ended environments where task goals are abstract and difficult to quantify. In this work, we present VLM-AR3L, a framework that leverages Vision-Language Models (VLMs) to provide both absolute and...

### 28 - Personalization as Inverse Planning: Learning Latent Design Intents for Agentic Slide Generation via Structural Denoising

- arXiv: [2607.00407](https://arxiv.org/abs/2607.00407) | [PDF](https://arxiv.org/pdf/2607.00407) | [papers.cool](https://papers.cool/arxiv/2607.00407)
- Authors: Tianci Liu, Zihan Dong, Linjun Zhang, Haoyu Wang, jing Gao, Emre Kiciman, et al. (8 authors)
- Published: 2026-07-01 04:05 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: planning
- Abstract skim: Slide design requires personalizing both deck themes and page layouts. Yet, current AI agent-based methods struggle with fine-grained, page-level design. Solely relying on prespecified templates or user verbose instructions, they fail to capture latent design intents, leaving Page-level Slide Personalization (PSP)...

### 28 - RareDxR1: Autonomous Medical Reasoning for Rare Disease Diagnosis Beyond Human Annotation

- arXiv: [2607.00147](https://arxiv.org/abs/2607.00147) | [PDF](https://arxiv.org/pdf/2607.00147) | [papers.cool](https://papers.cool/arxiv/2607.00147)
- Authors: Deyang Jiang, Haoran Wu, Ziyi Wang, Yiming Rong, Yunlong Zhao, Ye Jin, et al. (7 authors)
- Published: 2026-06-30 20:25 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, reflection; planning_and_action: decision making
- Abstract skim: Rare disease differential diagnosis is a critical yet arduous clinical task, requiring physicians to identify precise phenotypes from complex, unstructured patient symptoms and execute intricate reasoning within a vast search space. However, existing AI approaches typically rely on pipeline-based phenotype...

### 27 - M2Note: Continual Evolution of Vision Language Models via Mistake Notebook Learning

- arXiv: [2607.00685](https://arxiv.org/abs/2607.00685) | [PDF](https://arxiv.org/pdf/2607.00685) | [papers.cool](https://papers.cool/arxiv/2607.00685)
- Authors: Haiwen Li, Jing Tang, Rui Chen, Lei Sun, Xiangxiang Chu
- Published: 2026-07-01 09:30 UTC | Categories: cs.MA
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: memory
- Abstract skim: Vision Language Models (VLMs) have demonstrated remarkable capabilities in multimodal reasoning tasks, yet they still suffer from recurring failures, such as skipping key visual checks, misapplying domain rules, and hallucinating unsupported concepts. Most existing solutions rely on supervised fine-tuning (SFT) and...

### 26 - The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology

- arXiv: [2607.01033](https://arxiv.org/abs/2607.01033) | [PDF](https://arxiv.org/pdf/2607.01033) | [papers.cool](https://papers.cool/arxiv/2607.01033)
- Authors: Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere, Nikita Menon, Stefan Heimersheim
- Published: 2026-07-01 15:01 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, dpo; memory_and_benchmarks: benchmark
- Abstract skim: Model organisms (MOs) - language models trained to exhibit undesired or unnatural behaviours - are frequently used as testbeds for evaluating white-box interpretability techniques. Current MOs are typically constructed via post-hoc supervised fine-tuning (SFT) on behavioural transcripts or synthetic documents. Prior...

### 25 - QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling

- arXiv: [2607.01179](https://arxiv.org/abs/2607.01179) | [PDF](https://arxiv.org/pdf/2607.01179) | [papers.cool](https://papers.cool/arxiv/2607.01179)
- Authors: Michael Y. Li, Anthony Zhan, Kanishk Gandhi, Noah D. Goodman, Emily B. Fox
- Published: 2026-07-01 17:10 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Scaling inference compute, by generating many parallel attempts per problem, is a costly but reliable lever for improving language model capabilities. By default these attempts are generated independently, wasting inference compute on redundant solutions. This waste seems unavoidable. After all, independence is what...

### 25 - Verifiable Rewards for Calibrated Probabilistic Forecasting

- arXiv: [2607.00164](https://arxiv.org/abs/2607.00164) | [PDF](https://arxiv.org/pdf/2607.00164) | [papers.cool](https://papers.cool/arxiv/2607.00164)
- Authors: Sadanand Singh, Allam Reddy, Manan Chopra
- Published: 2026-06-30 20:42 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Reinforcement learning with verifiable rewards can in principle train calibrated probabilistic forecasters, since a proper scoring rule such as the Brier score is computed from outcomes alone and is minimized in expectation by the true probability. In practice it degrades calibration, and existing remedies address...

### 24 - Autonomous Scientific Discovery via Iterative Meta-Reflection

- arXiv: [2607.01131](https://arxiv.org/abs/2607.01131) | [PDF](https://arxiv.org/pdf/2607.01131) | [papers.cool](https://papers.cool/arxiv/2607.01131)
- Authors: Bingchen Zhao, Sara Beery, Oisin Mac Aodha
- Published: 2026-07-01 16:16 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; reasoning: reasoning, reflection; memory_and_benchmarks: benchmark
- Abstract skim: Autonomous scientific discovery systems offer the potential to accelerate research by automating the process of hypothesis generation and validation. However, current systems operate within constrained search spaces or require predefined research questions, limiting their capacity for true open-ended inquiry....

### 24 - Post-Training Pruning for Diffusion Transformers

- arXiv: [2607.00927](https://arxiv.org/abs/2607.00927) | [PDF](https://arxiv.org/pdf/2607.00927) | [papers.cool](https://papers.cool/arxiv/2607.00927)
- Authors: Chengzhi Hu, Xuewen Liu, Jing Zhang, Mengjuan Chen, Zhikai Li, Qingyi Gu
- Published: 2026-07-01 13:30 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training
- Abstract skim: Diffusion Transformers (DiTs) have demonstrated impressive performance in image generation but suffer from substantial computational overhead and resource consumption. Post-training pruning offers a promising solution; however, due to DiTs' unique architectural design and parameter distribution, traditional pruning...

### 24 - Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware Agricultural Advisory Generation

- arXiv: [2607.00454](https://arxiv.org/abs/2607.00454) | [PDF](https://arxiv.org/pdf/2607.00454) | [papers.cool](https://papers.cool/arxiv/2607.00454)
- Authors: Vedant Balasubramaniam, Geetha Charan, Manojkumar Patil, Rohit P Suresh, V Priyanka, Kodur Sai Vinay Sathvik, et al. (7 authors)
- Published: 2026-07-01 05:18 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: memory, episodic memory
- Abstract skim: Agricultural advisory systems face a fundamental tension: static agronomic guidelines offer consistent, evidence-based recommendations, yet remain blind to in-season variability and dynamic uncertainties. Recent advisory systems powered by LLMs are liable for a different risk of generating recommendations that are...

### 24 - Gauging, Measuring, and Controlling Critic Complexity in Actor-Critic Reinforcement Learning

- arXiv: [2607.00452](https://arxiv.org/abs/2607.00452) | [PDF](https://arxiv.org/pdf/2607.00452) | [papers.cool](https://papers.cool/arxiv/2607.00452)
- Authors: Konstantin Garbers
- Published: 2026-07-01 05:10 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, ppo
- Abstract skim: Actor-critic methods depend on learned critics, but critic quality is often evaluated only indirectly through return, temporal-difference error, or value loss. Critic complexity is introduced as an additional diagnostic and intervention dimension for actor-critic reinforcement learning. The analysis uses spectral...

### 24 - Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications

- arXiv: [2607.00442](https://arxiv.org/abs/2607.00442) | [PDF](https://arxiv.org/pdf/2607.00442) | [papers.cool](https://papers.cool/arxiv/2607.00442)
- Authors: Merve Atasever, Cagan Bakirci, Alfredo Reina Corona, Keyan Azbijari, Jyotirmoy V. Deshmukh
- Published: 2026-07-01 04:57 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints...

### 23 - A Role-Based Multi-Agent Model for Climate Adaptation Deliberation Across Living Labs

- arXiv: [2607.00046](https://arxiv.org/abs/2607.00046) | [PDF](https://arxiv.org/pdf/2607.00046) | [papers.cool](https://papers.cool/arxiv/2607.00046)
- Authors: Önder Gürcan, David Eric John Herbert, F. LeRon Shultz, Christopher Frantz, Ivan Puga-Gonzalez
- Published: 2026-06-29 19:56 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: deliberation; planning_and_action: decision making
- Abstract skim: Climate governance processes involve complex interactions between heterogeneous citizens, advocacy groups, media actors, and political decision-makers. While agent-based models (ABMs) have been widely used to study environmental policy and socio-ecological systems, many existing approaches focus either on...

### 23 - ATM: CID-Brokered Pre-Write Admission for Multi-Agent Code Co-Synthesis

- arXiv: [2607.00041](https://arxiv.org/abs/2607.00041) | [PDF](https://arxiv.org/pdf/2607.00041) | [papers.cool](https://papers.cool/arxiv/2607.00041)
- Authors: Eagl Huang
- Published: 2026-06-29 16:02 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; planning_and_action: planning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Multi-agent LLM systems can decompose software-engineering work into planning, generation, validation, and repair, but a narrower systems problem remains: before any governed shared mutation is applied, a system must decide which concurrently formed write intents may proceed in parallel, which require deterministic...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
