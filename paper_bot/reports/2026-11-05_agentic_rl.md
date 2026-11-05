# RL / Post-Training / Agentic RL Reading Queue - 2026-11-05

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 441. Minimum score: 8.

## Top Picks

### 60 - Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man

- arXiv: [2611.06704](https://arxiv.org/abs/2611.06704) | [PDF](https://arxiv.org/pdf/2611.06704) | [papers.cool](https://papers.cool/arxiv/2611.06704)
- Authors: Xinglu Wang, Edward Wang, Yong Zhang, Zhenan Fan
- Published: 2026-11-04 16:04 UTC | Categories: cs.LG
- Why it matched: agentic_rl: language agent, agent training; rl_post_training: post-training, post training, reinforcement learning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Training an agent to play Pac-Man with only up, down, left and right actions raises a basic question: when performance is poor, what should be improved? Difficulty can arise from reading the screen or from choosing actions over a long sequence. We examine these problems in a Qwen3.5-9B-based agent through separate...

### 60 - C-GRPO: Conformal Group Relative Policy Optimization

- arXiv: [2611.05591](https://arxiv.org/abs/2611.05591) | [PDF](https://arxiv.org/pdf/2611.05591) | [papers.cool](https://papers.cool/arxiv/2611.05591)
- Authors: Arya Fayyazi, Seyedarmin Azizi, Mehdi Kamal, Massoud Pedram
- Published: 2026-11-03 20:23 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reasoning-oriented language model training increasingly relies on multiple on-policy rollouts, but standard Group Relative Policy Optimization (GRPO) uses a fixed group size, wasting compute on easy prompts and under-exploring hard ones. Existing adaptive-budget methods alleviate this inefficiency, yet their...

### 53 - EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL

- arXiv: [2611.06518](https://arxiv.org/abs/2611.06518) | [PDF](https://arxiv.org/pdf/2611.06518) | [papers.cool](https://papers.cool/arxiv/2611.06518)
- Authors: Mingzhe Zheng, Yue Wu, Jing Tan, Chang Zou, Dengyang Jiang, Zeyue Tian, et al. (22 authors)
- Published: 2026-11-04 13:43 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, rlhf, policy optimization, +2 more; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has no uniquely correct target. Existing approaches typically rely on...

### 44 - RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management

- arXiv: [2611.06554](https://arxiv.org/abs/2611.06554) | [PDF](https://arxiv.org/pdf/2611.06554) | [papers.cool](https://papers.cool/arxiv/2611.06554)
- Authors: Shreya K. Chari, John S. Vardakas, Kostas Ramantas, Christos Verikoukis
- Published: 2026-11-04 14:18 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, reward model; memory_and_benchmarks: memory
- Abstract skim: Resource management for distributed edge networks hosting different services has been handled efficiently using Reinforcement learning (RL). Reward generalization in complex workflows is still an open issue within the RL realm. Therefore, this work proposes RAGAM-AI, a hybrid framework that combines the capabilities...

### 41 - SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory

- arXiv: [2611.06445](https://arxiv.org/abs/2611.06445) | [PDF](https://arxiv.org/pdf/2611.06445) | [papers.cool](https://papers.cool/arxiv/2611.06445)
- Authors: Jizhe Zhang, Ang Li, Chenheng Zhang, Yisen Wang
- Published: 2026-11-04 12:49 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; rl_post_training: grpo; planning_and_action: trajectory; memory_and_benchmarks: memory, evaluation
- Abstract skim: Long-horizon language-model agents accumulate increasingly large interaction histories, making context compaction essential for efficient execution. Existing learned compaction methods often rely on downstream task outcomes or solver behavior, coupling training to specific tasks or agents. We introduce SumOne, a...

### 40 - Vision Paper: Why Distributed LLM Post-Training and Decentralized Alignment Are Now Essential

- arXiv: [2611.05841](https://arxiv.org/abs/2611.05841) | [PDF](https://arxiv.org/pdf/2611.05841) | [papers.cool](https://papers.cool/arxiv/2611.05841)
- Authors: Zhanhong Jiang, Qisai Liu, Soumik Sarkar
- Published: 2026-11-04 02:30 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, rlhf, dpo
- Abstract skim: This vision paper argues that distributed learning, including federated and decentralized, should become a first-class paradigm in LLM post-training, not merely a privacy add-on. Current methods like RLHF and DPO rest on an invisible assumption: preference data should be centralized. We contend this assumption is...

### 39 - H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control

- arXiv: [2611.06523](https://arxiv.org/abs/2611.06523) | [PDF](https://arxiv.org/pdf/2611.06523) | [papers.cool](https://papers.cool/arxiv/2611.06523)
- Authors: Xuemin Hu, Kaixin Li, Qingqing Xia, Yuxin Wang, Wei Xie, Bo Tang, et al. (7 authors)
- Published: 2026-11-04 13:48 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: planning
- Abstract skim: Coordinated whole-body control of humanoid robots remains challenging due to high-dimensional coupled dynamics and substantial physical heterogeneity across joint degrees of freedom (JDoFs). Existing multi-agent reinforcement learning methods either employ coarse agent partitions or directly apply generic...

### 39 - What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?

- arXiv: [2611.06483](https://arxiv.org/abs/2611.06483) | [PDF](https://arxiv.org/pdf/2611.06483) | [papers.cool](https://papers.cool/arxiv/2611.06483)
- Authors: Kejian Zhu, Zhuoran Jin, Shangqing Tu, Tianyi Men, Yupu Hao, Jiachun Li, et al. (8 authors)
- Published: 2026-11-04 13:24 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; planning_and_action: trajectory
- Abstract skim: While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advantages depend on sufficient turn...

### 38 - MA-Mesh: Resilient Multi-Agent Collaboration via Role-based Self-Healing

- arXiv: [2611.06389](https://arxiv.org/abs/2611.06389) | [PDF](https://arxiv.org/pdf/2611.06389) | [papers.cool](https://papers.cool/arxiv/2611.06389)
- Authors: JunYong Lee, Woo Kyung Kim, Honguk Woo
- Published: 2026-11-04 11:54 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, tool use, agent collaboration; reasoning: reasoning, reflection
- Abstract skim: Effective collaboration in multi-agent systems requires mechanisms for coordination and adaptability in dynamic and uncertain environments. However, existing multi-agent systems rarely model resilience explicitly, instead relying on ad-hoc output correction that limits systematic, runtime management of robustness....

### 34 - TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration

- arXiv: [2611.05827](https://arxiv.org/abs/2611.05827) | [PDF](https://arxiv.org/pdf/2611.05827) | [papers.cool](https://papers.cool/arxiv/2611.05827)
- Authors: Baohang Li, Xiaocheng Feng, Bing Qin
- Published: 2026-11-04 02:08 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent, agent collaboration; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Decision models choose among predefined options in tasks such as routing and action selection. In multi-agent collaboration, a decision determines how members divide work, exchange resources, and act in parallel. We introduce TandemBench, a benchmark of 1,200 questions in multi-agent cooking scenarios where...

### 32 - From Handcrafted to Generative: RLVR-Optimized Icon Generation for Alexa+

- arXiv: [2611.06123](https://arxiv.org/abs/2611.06123) | [PDF](https://arxiv.org/pdf/2611.06123) | [papers.cool](https://papers.cool/arxiv/2611.06123)
- Authors: Rohan Sequeira, Matthew Rosenberg, Amin Mahmoudabadbozchelou, Oleg Poliannikov, Jonathan Rubin
- Published: 2026-11-04 08:08 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, reward model
- Abstract skim: Alexa+ devices with screens display animated icons during conversations to visually reinforce what is being said. The original set of these icons was hand-drawn by designers one at a time, a process that produces polished results but is time-consuming and cannot scale to the range of topics encountered in open-ended...

### 32 - FlyHash for LLM Agent Memory: An Empirical Validation and a New Application

- arXiv: [2611.05791](https://arxiv.org/abs/2611.05791) | [PDF](https://arxiv.org/pdf/2611.05791) | [papers.cool](https://papers.cool/arxiv/2611.05791)
- Authors: Mohan Bheemadolu, Chrisogonas O. Odhiambo
- Published: 2026-11-04 00:57 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: llm agent, agent memory; memory_and_benchmarks: memory
- Abstract skim: Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash of sensory input using a strikingly...

### 31 - TSFM Meets LLM: Context as Covariates

- arXiv: [2611.05515](https://arxiv.org/abs/2611.05515) | [PDF](https://arxiv.org/pdf/2611.05515) | [papers.cool](https://papers.cool/arxiv/2611.05515)
- Authors: Hemanth Ram, Sai Shankar Narasimhan, Shubhankar Agarwal, Sandeep Chinchali
- Published: 2026-11-03 19:13 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: evaluation; downranked: traffic
- Abstract skim: Textual information is ubiquitous in real-world time series datasets, appearing as news, reports, and annotations that hold key predictive signals not deducible from numerical history alone. Large Language Models (LLMs) interpret text but lack numerical precision, while Time Series Foundation Models (TSFMs) are...

### 29 - Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement

- arXiv: [2611.06905](https://arxiv.org/abs/2611.06905) | [PDF](https://arxiv.org/pdf/2611.06905) | [papers.cool](https://papers.cool/arxiv/2611.06905)
- Authors: Michal Korniak, Marco Bagatella, Ralf Römer, Michal Nauman, Yarden As, Pranav Vignesh, et al. (24 authors)
- Published: 2026-11-04 18:52 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: self-improvement, self improvement
- Abstract skim: The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-shot generalization capabilities, they typically require an adaptation phase to achieve sufficient performance in...

### 29 - Learning When to Think Aloud in Latent Reasoning

- arXiv: [2611.06108](https://arxiv.org/abs/2611.06108) | [PDF](https://arxiv.org/pdf/2611.06108) | [papers.cool](https://papers.cool/arxiv/2611.06108)
- Authors: Zhehao Zhou, Tongrui Su, Shengyu Zhu, Da Li, Zeyu Liu, Jun Zhu, et al. (7 authors)
- Published: 2026-11-04 07:51 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Latent Chain-of-Thought (CoT) reasoning improves efficiency by shifting intermediate computation into continuous hidden states. However, fully latent methods often struggle on precision-critical tasks such as mathematical reasoning, while existing hybrid approaches retain substantial token-generation overhead. We...

### 29 - Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning

- arXiv: [2611.05942](https://arxiv.org/abs/2611.05942) | [PDF](https://arxiv.org/pdf/2611.05942) | [papers.cool](https://papers.cool/arxiv/2611.05942)
- Authors: Mengni Jia, Mengyu Zhou, Xiaoxi Jiang, Guanjun Jiang
- Published: 2026-11-04 04:32 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: RL for LLM reasoning often reaches an early performance plateau as the policy distribution becomes increasingly sharp. Recent work has studied policy entropy as both a diagnostic and a control signal for this behavior. In our experiments, however, increasing entropy alone does not reliably change the eventual...

### 27 - Turns Matter: Advancing Streaming Video RL via Turn-Level Credit

- arXiv: [2611.06728](https://arxiv.org/abs/2611.06728) | [PDF](https://arxiv.org/pdf/2611.06728) | [papers.cool](https://papers.cool/arxiv/2611.06728)
- Authors: Shuai Dong, Kanghui Tian, Linghan Chen, Wenqi Shao, Hongrui Wu, Haowen Hou, et al. (23 authors)
- Published: 2026-11-04 16:16 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; planning_and_action: trajectory
- Abstract skim: Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design while retaining a single trajectory-level advantage across turns. Such...

### 24 - AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents

- arXiv: [2611.06674](https://arxiv.org/abs/2611.06674) | [PDF](https://arxiv.org/pdf/2611.06674) | [papers.cool](https://papers.cool/arxiv/2611.06674)
- Authors: Sachin Gupta
- Published: 2026-11-04 15:46 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Infrastructure security does not establish whether an LLM agent selected an allowed tool, grounded its answer in tool output, or followed a required workflow. AgentTrustCI is a Java/JUnit 5 framework that expresses these application-layer expectations as policy, grounding, and trajectory checks over recorded traces....

### 24 - TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics

- arXiv: [2611.06442](https://arxiv.org/abs/2611.06442) | [PDF](https://arxiv.org/pdf/2611.06442) | [papers.cool](https://papers.cool/arxiv/2611.06442)
- Authors: Shu'ang Sun, Yibo Qiu, Haoliang Ye, Zan Huang, Ao Tian, Kan Ding, et al. (8 authors)
- Published: 2026-11-04 12:44 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, reward model
- Abstract skim: Online reinforcement learning offers an effective approach to precise laboratory manipulation, yet costly real-world demonstrations and limited access to dense process rewards hinder its practical application. We present TwinBridge, a digital twin-driven framework that supplies policy initialization and dense visual...

### 24 - GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR

- arXiv: [2611.06395](https://arxiv.org/abs/2611.06395) | [PDF](https://arxiv.org/pdf/2611.06395) | [papers.cool](https://papers.cool/arxiv/2611.06395)
- Authors: Xuliang Huang, Tianxiang Zhao, Chengwei Qin, Yao Shu
- Published: 2026-11-04 12:01 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr
- Abstract skim: Offline reinforcement learning with verifiable rewards (RLVR) trains on a fixed pool of sampled responses and typically supervises every token of every response, although responses and tokens are not equally informative. We study which ones to supervise through the Gibbs-optimal policy of KL-regularized RLVR, which...

### 24 - Mass Producing Training Data with Surprising Side Effects

- arXiv: [2611.06324](https://arxiv.org/abs/2611.06324) | [PDF](https://arxiv.org/pdf/2611.06324) | [papers.cool](https://papers.cool/arxiv/2611.06324)
- Authors: Yaowen Ye, Jacob Steinhardt, Sarah Schwettmann, Cassidy Laidlaw
- Published: 2026-11-04 10:57 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Training data can have unexpected side effects on language model behavior outside the training domain: insecure code data can induce broad misalignment, and outdated bird names can induce a 19th-century persona. Understanding such generalization is hard because only dozens of isolated examples exist, each...

### 24 - When to Ask, When to Answer: Strategic Clarification for Ambiguous Reference Resolution in Dialogue

- arXiv: [2611.05517](https://arxiv.org/abs/2611.05517) | [PDF](https://arxiv.org/pdf/2611.05517) | [papers.cool](https://papers.cool/arxiv/2611.05517)
- Authors: Ibrahim Khebour, Nikhil Krishnaswamy
- Published: 2026-11-03 19:14 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, grpo
- Abstract skim: For humans, referential disambiguation is a collaborative process involving clarification questions asked when they will meaningfully change the outcome. However, large language models (LLMs) have been shown to be biased toward premature answering, preferring definite single-turn responses over more clarification...

### 23 - Compounding Physical RSI: Turning Execution Failure into Inherited Capability

- arXiv: [2611.06654](https://arxiv.org/abs/2611.06654) | [PDF](https://arxiv.org/pdf/2611.06654) | [papers.cool](https://papers.cool/arxiv/2611.06654)
- Authors: Yixuan Yang, Qiang Chen, Run Shao, Shuwei Dong, Wenhao Li, Yunpeng Wang, et al. (34 authors)
- Published: 2026-11-04 15:31 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: self-improvement, self improvement; memory_and_benchmarks: benchmark
- Abstract skim: Generalist robot policies are trained on static offline datasets, yet physical manipulation unfolds sequentially across stages. Because a weakness in a downstream stage remains unobservable until the policy passes earlier ones, each resolved bottleneck exposes the next hidden failure mode. This staged structure...

### 22 - Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination

- arXiv: [2611.05953](https://arxiv.org/abs/2611.05953) | [PDF](https://arxiv.org/pdf/2611.05953) | [papers.cool](https://papers.cool/arxiv/2611.05953)
- Authors: Haihui Liu, Yang Chen, Zice Qiu, Yun Zhang, Jialun Zhong, Wenhua Wang, et al. (8 authors)
- Published: 2026-11-04 04:47 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Graphs play an increasingly important role in large language model (LLM) systems, supporting structural reasoning, knowledge grounding, retrieval, and memory. As these systems evolve toward the agentic era, graphs also organize execution dependencies and multi-agent communication, linking intermediate observations...

### 21 - PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World

- arXiv: [2611.06768](https://arxiv.org/abs/2611.06768) | [PDF](https://arxiv.org/pdf/2611.06768) | [papers.cool](https://papers.cool/arxiv/2611.06768)
- Authors: Qiang Wang, Jianxin Bi, Shulong Jiang, Ruiyang Si, Wenbo Huang, Kaiqi Chen, et al. (10 authors)
- Published: 2026-11-04 16:46 UTC | Categories: cs.RO
- Why it matched: reasoning: reasoning, self-improvement, self improvement; planning_and_action: decision making; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: Coding agents powered by models such as GPT-6-Astra connect spatial reasoning with executable robot behavior, raising the question of how such agents can produce lasting improvements in robot capabilities from physical interaction. In this work, we study embodied recursive self-improvement (RSI) through real-world...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
