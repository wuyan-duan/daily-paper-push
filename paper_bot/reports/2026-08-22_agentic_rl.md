# RL / Post-Training / Agentic RL Reading Queue - 2026-08-22

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 267. Minimum score: 8.

## Top Picks

### 101 - SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning

- arXiv: [2608.19842](https://arxiv.org/abs/2608.19842) | [PDF](https://arxiv.org/pdf/2608.19842) | [papers.cool](https://papers.cool/arxiv/2608.19842)
- Authors: Dayang Liang, Lang Feng, Bo An, Yunlong Liu
- Published: 2026-08-20 09:43 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; planning_and_action: trajectory, rollout; memory_and_benchmarks: memory, alfworld
- Abstract skim: Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative methods estimate policy advantages from multiple rollouts, avoiding the substantial memory overhead of conventional proximal policy optimization (PPO) and achieving...

### 61 - Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design

- arXiv: [2608.20099](https://arxiv.org/abs/2608.20099) | [PDF](https://arxiv.org/pdf/2608.20099) | [papers.cool](https://papers.cool/arxiv/2608.20099)
- Authors: Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu, Pascal Bouvry
- Published: 2026-08-20 14:32 UTC | Categories: cs.CL, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, reward model; reasoning: reasoning
- Abstract skim: LLM-based Multi-Agent Systems (MAS) achieve strong performance on complex reasoning tasks by coordinating multiple agents, but at the cost of substantial token consumption. Recent work on automatic topology design, ARG-Designer, has reframed this problem as autoregressive graph generation. However, its training...

### 53 - MidTool: Mid-training Data Synthesis for Agentic Tool Use

- arXiv: [2608.20314](https://arxiv.org/abs/2608.20314) | [PDF](https://arxiv.org/pdf/2608.20314) | [papers.cool](https://papers.cool/arxiv/2608.20314)
- Authors: Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao, et al. (8 authors)
- Published: 2026-08-20 17:53 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Mid-training is increasingly recognized as a critical stage for shaping the capabilities of large language models. Recent work has shown that targeted mid-training can strengthen reasoning-intensive abilities such as math and science, and can also improve agentic capabilities in software-engineering settings. In...

### 52 - Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving

- arXiv: [2608.20129](https://arxiv.org/abs/2608.20129) | [PDF](https://arxiv.org/pdf/2608.20129) | [papers.cool](https://papers.cool/arxiv/2608.20129)
- Authors: Mehdi Azarafza, Faezeh Pasandideh, Ali Ehteshami Bejnordi, Stefan Henkler, Achim Rettberg
- Published: 2026-08-20 14:56 UTC | Categories: cs.CL, cs.MA
- Why it matched: agentic_rl: multi-agent, agent orchestration; rl_post_training: reinforcement learning, ppo; reasoning: reasoning; planning_and_action: decision making; downranked: traffic, driving, autonomous driving
- Abstract skim: Autonomous vehicles require robust perception and decision-making capabilities to operate in diverse and unseen scenarios. While reinforcement learning and rule-based methods can provide effective control and safety mechanisms, their performance may degrade in situations requiring contextual reasoning. Large...

### 47 - MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents

- arXiv: [2608.19803](https://arxiv.org/abs/2608.19803) | [PDF](https://arxiv.org/pdf/2608.19803) | [papers.cool](https://papers.cool/arxiv/2608.19803)
- Authors: Bo Qian, Yuting Wu, Shuang Zeng, Huaiyu Wan, Dalin Zhang, Jiqiang Liu
- Published: 2026-08-20 08:58 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Credit assignment is challenging in long-horizon agentic reinforcement learning, where supervision often comes only from final rewards. Existing methods refine trajectory-level signals into step-level credits through step grouping or graph-based advantage estimation, but can overlook meaningful intermediate...

### 45 - Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation

- arXiv: [2608.20256](https://arxiv.org/abs/2608.20256) | [PDF](https://arxiv.org/pdf/2608.20256) | [papers.cool](https://papers.cool/arxiv/2608.20256)
- Authors: Gijs Kassenaar, Zhao Yang, Vincent François-Lavet
- Published: 2026-08-20 16:54 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which can lead to over-computation on easy problems and insufficient computation on difficult ones. We study whether a model can learn to allocate its own reasoning...

### 40 - Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration

- arXiv: [2608.19701](https://arxiv.org/abs/2608.19701) | [PDF](https://arxiv.org/pdf/2608.19701) | [papers.cool](https://papers.cool/arxiv/2608.19701)
- Authors: Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai
- Published: 2026-08-20 06:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent memory; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings: memories written...

### 40 - Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress

- arXiv: [2608.19408](https://arxiv.org/abs/2608.19408) | [PDF](https://arxiv.org/pdf/2608.19408) | [papers.cool](https://papers.cool/arxiv/2608.19408)
- Authors: Chen Yang, Haiyuan Wan, Rengrong Xiong, Yize Chen, Danny H. K. Tsang
- Published: 2026-08-19 19:45 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: On-policy distillation (OPD) has emerged as an effective framework for post-training language models by pairing student-generated trajectories with dense token-level supervision from a teacher. However, OPD implicitly assumes that teacher-derived rewards are an appropriate proxy for reasoning progress, and therefore...

### 34 - FAR-DPO: Feasibility-Aware and Robust Direct Preference Optimization for Cyclic Peptide Design

- arXiv: [2608.19808](https://arxiv.org/abs/2608.19808) | [PDF](https://arxiv.org/pdf/2608.19808) | [papers.cool](https://papers.cool/arxiv/2608.19808)
- Authors: Guofeng Zhang, Rong Han, Xiaoyu Wang, Zhiyun Li, Zongbo Han, Xiaohong Liu, et al. (7 authors)
- Published: 2026-08-20 09:00 UTC | Categories: cs.LG
- Why it matched: rl_post_training: preference optimization, dpo; memory_and_benchmarks: benchmark
- Abstract skim: Cyclic peptides are emerging as promising molecular scaffolds in drug discovery due to their high binding affinity and structural stability. However, extending generative models from linear to cyclic peptide design remains challenging, as cyclization sharply restricts the feasible design space through coupled...

### 32 - DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing

- arXiv: [2608.20161](https://arxiv.org/abs/2608.20161) | [PDF](https://arxiv.org/pdf/2608.20161) | [papers.cool](https://papers.cool/arxiv/2608.20161)
- Authors: Haoxiang Cao, Jiajiong Cao, Xuanpu Zhang, Changqian Yu, Chaoqun Wang
- Published: 2026-08-20 15:16 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, reward model; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Instruction-based image editing uses a planner-renderer pipeline: a vision-language model (VLM) first converts the instruction into an edit plan, and a diffusion model then executes that plan. Training such systems with only final-image rewards is inefficient because a poor edit does not reveal whether additional...

### 32 - Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning

- arXiv: [2608.19669](https://arxiv.org/abs/2608.19669) | [PDF](https://arxiv.org/pdf/2608.19669) | [papers.cool](https://papers.cool/arxiv/2608.19669)
- Authors: Haoqiang Kang, Yinpeng Chen, Luyang Liu, Jesper Sparre Andersen, Abhijit Ogale, Baochen Sun, et al. (8 authors)
- Published: 2026-08-20 06:04 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: planning
- Abstract skim: Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visual chain-of-thought during a supervised fine-tuning (SFT) stage, and (2) these latent tokens are further refined with reward feedback during a reinforcement learning...

### 32 - PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for MLLMs Alignment

- arXiv: [2608.19598](https://arxiv.org/abs/2608.19598) | [PDF](https://arxiv.org/pdf/2608.19598) | [papers.cool](https://papers.cool/arxiv/2608.19598)
- Authors: Jiawei Feng, Jiancan Wu, Xingyu Zhu, Junkang Wu, Xiang Wang, Xiangnan He
- Published: 2026-08-20 03:35 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: preference optimization, dpo
- Abstract skim: Direct Preference Optimization (DPO) has emerged as an effective approach for aligning large language models (LLMs) with human preferences. However, its adaptation to multimodal settings remains unexplored. Through representational analysis, we identify a key limitation in multimodal preference optimization, which...

### 28 - G-CARL: Grounded Checklist-Aligned Reward Learning for Patient-Oriented Medical Report Interpretation

- arXiv: [2608.20331](https://arxiv.org/abs/2608.20331) | [PDF](https://arxiv.org/pdf/2608.20331) | [papers.cool](https://papers.cool/arxiv/2608.20331)
- Authors: Shiao Xie, Siyu Chen, Jianwei Lv, Bo Yuan, Yujin Wang, Xiandong Li
- Published: 2026-08-20 17:59 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Personalized interpretation of medical reports has emerged as an increasingly important need among patients. Addressing this need requires both evidence-grounded medical factuality and context-dependent patient communication, yet existing medical vision-language tasks do not adequately capture these dual...

### 24 - Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization

- arXiv: [2608.20281](https://arxiv.org/abs/2608.20281) | [PDF](https://arxiv.org/pdf/2608.20281) | [papers.cool](https://papers.cool/arxiv/2608.20281)
- Authors: Qian Kou, Xiaofeng Shi, Xiaosong Qiu, Hua Zhou
- Published: 2026-08-20 17:14 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training
- Abstract skim: Large language models often fail to answer questions about a bounded document collection when the source documents are not retrieved at inference time. We study this setting as document knowledge internalization: converting a fixed corpus into usable parametric knowledge for retrieval-free question answering. We...

### 24 - ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

- arXiv: [2608.19974](https://arxiv.org/abs/2608.19974) | [PDF](https://arxiv.org/pdf/2608.19974) | [papers.cool](https://papers.cool/arxiv/2608.19974)
- Authors: Yiyang Luo, Yihang Jiang, Qijun Xie, Liang Lan, Lin Willian Cong, Anyi Rao, et al. (7 authors)
- Published: 2026-08-20 12:49 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: LLM agents in financial markets may cite rules yet still submit orders that violate executable constraints or misread surveillance evidence. We introduce ReguSim, a controlled financial-compliance environment, and ReguBench, a target-marked monitoring benchmark, to separate four artifacts: stated reasoning,...

### 24 - Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents

- arXiv: [2608.19564](https://arxiv.org/abs/2608.19564) | [PDF](https://arxiv.org/pdf/2608.19564) | [papers.cool](https://papers.cool/arxiv/2608.19564)
- Authors: Baichuan Li, Junyi Yao, Zihao Zheng
- Published: 2026-08-20 02:11 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent; memory_and_benchmarks: memory, evaluation
- Abstract skim: Persistent memory can personalize an LLM agent, but an incorrect durable update can silently distort future behavior. We study the memory-clarification boundary: whether interaction-derived information should be persisted, used only in the current context, re-verified, or clarified with the user. MCB contains 140...

### 23 - EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models

- arXiv: [2608.20055](https://arxiv.org/abs/2608.20055) | [PDF](https://arxiv.org/pdf/2608.20055) | [papers.cool](https://papers.cool/arxiv/2608.20055)
- Authors: Yiting Qu, Ziqing Yang, Chi Cui, Ye Leng, Junjie Chu, Yang Zhang
- Published: 2026-08-20 13:52 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory
- Abstract skim: Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be...

### 22 - Can Agent Memory Systems Track Evolving State?

- arXiv: [2608.19652](https://arxiv.org/abs/2608.19652) | [PDF](https://arxiv.org/pdf/2608.19652) | [papers.cool](https://papers.cool/arxiv/2608.19652)
- Authors: Xinyi Fan, Miri Liu, Ruozhen Yang, Siru Ouyang, Jiawei Han
- Published: 2026-08-20 05:41 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory, benchmark
- Abstract skim: As LLM-based agents are deployed for longer and higher-stakes tasks, their memory systems continue to have crucial gaps. While existing memory benchmarks focus largely on recall-shaped tasks, we argue an effective memory system must track the evolving state of the world; as facts, constraints, and decisions are...

### 20 - AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement

- arXiv: [2608.20318](https://arxiv.org/abs/2608.20318) | [PDF](https://arxiv.org/pdf/2608.20318) | [papers.cool](https://papers.cool/arxiv/2608.20318)
- Authors: Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, et al. (10 authors)
- Published: 2026-08-20 17:56 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: benchmark
- Abstract skim: Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subsequent run,...

### 20 - An Evidence-Grounded Multi-Agent System for High-Level Bio-Robot Design

- arXiv: [2608.19699](https://arxiv.org/abs/2608.19699) | [PDF](https://arxiv.org/pdf/2608.19699) | [papers.cool](https://papers.cool/arxiv/2608.19699)
- Authors: Yujun Chen, Tianle Li, Jiayu Chen, Zhen Yin
- Published: 2026-08-20 06:44 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: memory, evaluation
- Abstract skim: In this paper, a bio-robot is an engineered living or biohybrid system in which living cells perform one or more core functions, such as sensing, information processing, actuation or output. We focus on systems whose cell-based functions are programmed by genetic circuits; physical movement is optional. Designing...

### 19 - Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning

- arXiv: [2608.19836](https://arxiv.org/abs/2608.19836) | [PDF](https://arxiv.org/pdf/2608.19836) | [papers.cool](https://papers.cool/arxiv/2608.19836)
- Authors: Astrid Horn Brorholt, Maris F. L. Galesloot, Nils Jansen, Kim Guldstrand Larsen, Christian Schilling
- Published: 2026-08-20 09:37 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: acting
- Abstract skim: Probabilistic shielding is a technique for safe reinforcement learning (RL). Typically, a static observer -- called the shield -- constrains the learning agent's actions to those for which acting safely remains feasible. Traditionally, the shield is computed from the transition probabilities of the underlying Markov...

### 19 - Stopping and Routing LLM Judge Panels

- arXiv: [2608.19802](https://arxiv.org/abs/2608.19802) | [PDF](https://arxiv.org/pdf/2608.19802) | [papers.cool](https://papers.cool/arxiv/2608.19802)
- Authors: Bin Zhu, Yi Xie, Yanghui Rao
- Published: 2026-08-20 08:58 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reward model; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: LLM evaluation pipelines often have many candidate judges: general LLM-as-a-judge prompts, reward models, safety classifiers, confidence variants, and task-specific verifiers. The deployment question is not only which judge is best, but which judges should be called, on which examples, and when panel construction...

### 19 - Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning

- arXiv: [2608.19684](https://arxiv.org/abs/2608.19684) | [PDF](https://arxiv.org/pdf/2608.19684) | [papers.cool](https://papers.cool/arxiv/2608.19684)
- Authors: Tanachai Anakewat, Takayuki Osa, Tatsuya Harada
- Published: 2026-08-20 06:20 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: trajectory
- Abstract skim: Recent studies investigate how to leverage pre-collected datasets to improve the policy performance and sample efficiency of RL. One promising approach to achieve this goal is to employ a two-stage strategy: In the first stage, diverse skills are extracted as a low-level policy from a given dataset, and a high-level...

### 18 - Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection

- arXiv: [2608.20169](https://arxiv.org/abs/2608.20169) | [PDF](https://arxiv.org/pdf/2608.20169) | [papers.cool](https://papers.cool/arxiv/2608.20169)
- Authors: Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki
- Published: 2026-08-20 15:24 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: llm agent, agent harness; memory_and_benchmarks: evaluation
- Abstract skim: We present a novel approach to efficient LLM agent harness optimization through adaptive validation task selection. Harness optimization iteratively rewrites the harness code based on validation performance, enabling substantial performance gains without updating the underlying model weights. Existing approaches,...

### 18 - Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking

- arXiv: [2608.20011](https://arxiv.org/abs/2608.20011) | [PDF](https://arxiv.org/pdf/2608.20011) | [papers.cool](https://papers.cool/arxiv/2608.20011)
- Authors: Yansen Han, Shengyi Liao, Yuanxing Zhang, Pengfei Wan, Tao Lin
- Published: 2026-08-20 13:25 UTC | Categories: cs.AI
- Why it matched: rl_post_training: preference optimization; memory_and_benchmarks: benchmark
- Abstract skim: Preference optimization is a standard alignment method for generative models, yet extending it to continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify transport trajectories without an inherent constraint to the pretrained data manifold and can move terminal samples off the...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
