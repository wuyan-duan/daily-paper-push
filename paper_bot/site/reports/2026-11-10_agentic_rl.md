# RL / Post-Training / Agentic RL Reading Queue - 2026-11-10

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 989. Minimum score: 8.

## Top Picks

### 78 - Spectral Rank and Step-Direction Dynamics in Language-Model Post-Training

- arXiv: [2611.11752](https://arxiv.org/abs/2611.11752) | [PDF](https://arxiv.org/pdf/2611.11752) | [papers.cool](https://papers.cool/arxiv/2611.11752)
- Authors: Khurram Khalil, Khaza Anuarul Hoque
- Published: 2026-11-09 01:43 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +4 more; planning_and_action: trajectory, rollout
- Abstract skim: Language-model post-training modifies weights through cumulative updates and successive displacements, yet existing studies report seemingly conflicting spectral properties: nearly full-rank updates and low stable-rank changes. We show these observations are compatible and characterize update directions during...

### 70 - What Broke & Why: Practical Lessons from Reinforcement Learning Post-Training

- arXiv: [2611.10844](https://arxiv.org/abs/2611.10844) | [PDF](https://arxiv.org/pdf/2611.10844) | [papers.cool](https://papers.cool/arxiv/2611.10844)
- Authors: Luv Verma
- Published: 2026-11-07 16:43 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has become an important way to improve how language models reason, solve problems, and use tools. But getting it to work in practice is not always straightforward. Training can fail because a model receives no useful reward, learns to exploit the reward system,...

### 59 - When Credit Turns Against Tools: Transition-Aware Credit Assignment in Agentic Reinforcement Learning

- arXiv: [2611.11330](https://arxiv.org/abs/2611.11330) | [PDF](https://arxiv.org/pdf/2611.11330) | [papers.cool](https://papers.cool/arxiv/2611.11330)
- Authors: Xiangyu Lu, Zhanke Zhou, Jiazhe Ning, Chentao Cao, Jiangchao Yao, Bo Han
- Published: 2026-11-08 12:11 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, tool use; rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Agentic reinforcement learning with verifiable rewards trains language models through multi-turn tool interactions, yet their reasoning performance and tool-calling ability can decline during training. We trace this degradation to three coupled mechanisms: (1) tool-token imbalance produces negative overall tool...

### 59 - Plug-and-Play Verifier for Decoupling Process Reward in Stabilizing Long-Horizon Agentic Reasoning

- arXiv: [2611.10305](https://arxiv.org/abs/2611.10305) | [PDF](https://arxiv.org/pdf/2611.10305) | [papers.cool](https://papers.cool/arxiv/2611.10305)
- Authors: Mingwei Xu, Jieyuan Pei, Binghao Tu, Hao Fang
- Published: 2026-11-06 23:06 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning, process reward, reflection; memory_and_benchmarks: evaluation
- Abstract skim: Stabilizing long-horizon reasoning requires intelligent agents to sustain useful progress across successive reasoning steps and tool interactions. Such agents are typically trained with reinforcement learning (RL), where actor-critic RL uses a learnable critic network to estimate step advantages, while critic-free...

### 56 - CARE-PO: Controllable Tool-Call Efficiency for LLM Agents

- arXiv: [2611.12125](https://arxiv.org/abs/2611.12125) | [PDF](https://arxiv.org/pdf/2611.12125) | [papers.cool](https://papers.cool/arxiv/2611.12125)
- Authors: Xiaoyang Ye, Xiao Yao, Hairui Zhu, Yiying Yang, Bei Gan, Jinliang Lu, et al. (9 authors)
- Published: 2026-11-09 09:41 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: llm agent, tool use; rl_post_training: policy optimization, grpo; planning_and_action: trajectory, rollout; memory_and_benchmarks: benchmark, gaia
- Abstract skim: External tool calls are a major running cost of an LLM agent, while its training objectives align almost exclusively with task completion. In a step-level diagnosis of Qwen3.5 trajectories at two model sizes on GAIA, a long-horizon tool-use benchmark, we find that most contain removable calls, at a similar rate at...

### 54 - BunshinRL: Splitting Live Agent Workspaces for Memory-Efficient Agentic RL

- arXiv: [2611.10453](https://arxiv.org/abs/2611.10453) | [PDF](https://arxiv.org/pdf/2611.10453) | [papers.cool](https://papers.cool/arxiv/2611.10453)
- Authors: Yutong Huang, Vikranth Srivatsa, Alex Asch, Yiying Zhang
- Published: 2026-11-07 04:05 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Agentic reinforcement learning (RL) rollouts interleave model reasoning with tool calls in persistent workspaces. Scaling these rollouts incurs substantial memory costs for concurrent environments, while slow tool calls delay entire rollout batches. We present BunshinRL, an agentic RL rollout system that exploits...

### 53 - Seeing Isn't Enough: Unlocking Visual Reasoning by Bridging the Reasoning-Access Gap with TIGER

- arXiv: [2611.10552](https://arxiv.org/abs/2611.10552) | [PDF](https://arxiv.org/pdf/2611.10552) | [papers.cool](https://papers.cool/arxiv/2611.10552)
- Authors: Gregory Kang Ruey Lau, Minh Huynh Nguyen, Bryan Kian Hsiang Low
- Published: 2026-11-07 07:41 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: rlvr, policy optimization, group relative policy optimization, grpo, +1 more; reasoning: reasoning
- Abstract skim: Multimodal Large Language Models (MLLMs) inherit strong textual reasoning capabilities from their language backbones and text pretraining, but often fail to apply the same level of competency to visual inputs. We show that this degradation cannot be attributed to only perception failures, by evaluating models on...

### 52 - DISCOVER: Online Variance-Guided Data Discovery for Budgeted Multimodal GRPO

- arXiv: [2611.11145](https://arxiv.org/abs/2611.11145) | [PDF](https://arxiv.org/pdf/2611.11145) | [papers.cool](https://papers.cool/arxiv/2611.11145)
- Authors: Peyman Gholami, Shivam Chandhok, Saber Malekmohammadi, Shayan Shams, Robert Xiao, Leonid Sigal
- Published: 2026-11-08 05:27 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Recent advances in reinforcement learning have made verifiable rewards a central post-training paradigm for improving multimodal reasoning. However, methods such as GRPO remain data- and compute-inefficient, spending rollout and annotation budget on prompts that provide little learning signal. We propose DISCOVER,...

### 51 - Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading

- arXiv: [2611.12269](https://arxiv.org/abs/2611.12269) | [PDF](https://arxiv.org/pdf/2611.12269) | [papers.cool](https://papers.cool/arxiv/2611.12269)
- Authors: Guangyan Gan, Jiahao Li, Jiashun Wang, Lin William Cong
- Published: 2026-11-09 11:57 UTC | Categories: cs.CL, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, ppo; reasoning: reflection; memory_and_benchmarks: memory
- Abstract skim: Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In this paper, we propose Agent4Crypto, a...

### 48 - Proximal Preference Optimization: A Unified Framework for Stable and Reward-Free Alignment

- arXiv: [2611.10785](https://arxiv.org/abs/2611.10785) | [PDF](https://arxiv.org/pdf/2611.10785) | [papers.cool](https://papers.cool/arxiv/2611.10785)
- Authors: Qisai Liu, Zhanhong Jiang, Zahid Hasan, Soumik Sarkar
- Published: 2026-11-07 15:10 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: preference optimization, policy optimization, reward model, ppo, +1 more
- Abstract skim: We introduce a proximal preference optimization framework that unifies the implicit reward formulation of Direct Preference Optimization (DPO) with the trust-region stability of Proximal Policy Optimization (PPO). Our framework yields two complementary algorithms. P$^2$O (Proximal Preference Optimization) introduces...

### 48 - AERO: Adaptive Ensemble-Disagreement Routing for Oracle Feedback in Sample-Efficient Online RLHF

- arXiv: [2611.10750](https://arxiv.org/abs/2611.10750) | [PDF](https://arxiv.org/pdf/2611.10750) | [papers.cool](https://papers.cool/arxiv/2611.10750)
- Authors: Shrey Singhal, Nannan Huang, Haytham M. Fayek
- Published: 2026-11-07 14:12 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, reward model, +1 more
- Abstract skim: Aligning Large Language Models (LLMs) with human preferences via Reinforcement Learning from Human Feedback (RLHF) has driven substantial improvements across a wide range of tasks, but the cost of acquiring preference labels remains the dominant bottleneck in the alignment pipeline. While many recent alignment...

### 46 - A Gamified Framework for Conflict-Driven Design: Discovering Strategies for Collaborative Resilience with Multi-Agent Learning

- arXiv: [2611.10841](https://arxiv.org/abs/2611.10841) | [PDF](https://arxiv.org/pdf/2611.10841) | [papers.cool](https://papers.cool/arxiv/2611.10841)
- Authors: Jin Gao
- Published: 2026-11-07 16:37 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: self-play; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Conflicting stakeholder objectives make it difficult to coordinate investments in urban resilience. We model conflict-driven urban design as a non-zero-sum digital board game in which stakeholder agents allocate scarce resources and balance individual payoffs against shared urban development and resilience...

### 45 - Learning Evidence-Grounded Reasoning for Context-Aware Time Series Forecasting

- arXiv: [2611.12285](https://arxiv.org/abs/2611.12285) | [PDF](https://arxiv.org/pdf/2611.12285) | [papers.cool](https://papers.cool/arxiv/2611.12285)
- Authors: Xingpeng Gao, Mingyue Cheng, Daoyu Wang, Huajian Zhang, Xiaoyu Tao
- Published: 2026-11-09 12:12 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: LLM-driven time series forecasting has become increasingly promising by leveraging contextual features to generate future values directly or refine forecast priors. However, incorporating contextual features alone does not ensure that models can identify which features matter for forecasting and understand what they...

### 45 - Tail-risk-aware Agent Safety: Constraining Tail Risks Across Multi-step LLM Agent Workflows

- arXiv: [2611.10411](https://arxiv.org/abs/2611.10411) | [PDF](https://arxiv.org/pdf/2611.10411) | [papers.cool](https://papers.cool/arxiv/2611.10411)
- Authors: Shilong Pan, Zhiliang Tian, Zihan Chen, Wentao Zou, Weiguo Chen, DongSheng Li
- Published: 2026-11-07 02:45 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; rl_post_training: post-training, post training; planning_and_action: planning; memory_and_benchmarks: memory
- Abstract skim: LLM-based agents extend LLMs with tool calls, memory, planning, and retrieval to act in external environments, but they are vulnerable to attacks at different workflow steps. Existing defenses, including prompt engineering and post-training alignment, primarily improve LLM-only safety and often overlook risks that...

### 43 - Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards

- arXiv: [2611.12728](https://arxiv.org/abs/2611.12728) | [PDF](https://arxiv.org/pdf/2611.12728) | [papers.cool](https://papers.cool/arxiv/2611.12728)
- Authors: Brendan P. Murphy, Agustina Saenz
- Published: 2026-11-09 17:14 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood. We study this problem in clinical multi-turn agents that must decide what information to request, when to stop gathering evidence, and...

### 43 - Watching Itself Watch: Self-Auditing Visual Reliance for Video Reasoning

- arXiv: [2611.11949](https://arxiv.org/abs/2611.11949) | [PDF](https://arxiv.org/pdf/2611.11949) | [papers.cool](https://papers.cool/arxiv/2611.11949)
- Authors: Rohan Dugad, Mi Luo, Kristen Grauman
- Published: 2026-11-09 06:15 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Video reasoning hinges on a small number of visually decisive tokens embedded in otherwise largely language-driven chains of thought. Yet prevailing post-training methods such as GRPO overlook this structure, assigning coarse trajectory-level rewards while requiring multiple rollouts and often costly external...

### 43 - BRAT: Bounded Residual-Aligned Training for Stable Multi-Pass LLM Post-Training

- arXiv: [2611.10873](https://arxiv.org/abs/2611.10873) | [PDF](https://arxiv.org/pdf/2611.10873) | [papers.cool](https://papers.cool/arxiv/2611.10873)
- Authors: Xunlan Zhou, Yuzhe Zhao, Xuhong Huang, Feng Chen, Xuanlin Chen, Lang Feng, et al. (7 authors)
- Published: 2026-11-07 17:51 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, ppo; planning_and_action: rollout
- Abstract skim: Reinforcement learning for large language model post-training often reuses each batch of sampled rollouts for several gradient passes to amortize the cost of generation. Under such multi-pass reuse, existing objectives fail in different ways: unclipped updates collapse as the policy drifts away from the sampling...

### 40 - TLRS-DPO: Token-Level Risk Scoring for Better Direct Preference Optimization

- arXiv: [2611.11232](https://arxiv.org/abs/2611.11232) | [PDF](https://arxiv.org/pdf/2611.11232) | [papers.cool](https://papers.cool/arxiv/2611.11232)
- Authors: Suxin Ji, Hungtao Wan
- Published: 2026-11-08 08:37 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: rlhf, preference optimization, dpo
- Abstract skim: Direct Preference Optimization (DPO) is a simple and widely used alternative to RLHF for aligning large language models (LLMs), but its sequence-level objective cannot precisely locate or suppress the local patterns that make an otherwise acceptable response unsafe or undesirable. We propose TLRS-DPO (Token-Level...

### 39 - Viscot-steer: Disentangling and Transferring Visual Chain-of-Thought via Activation Steering

- arXiv: [2611.11209](https://arxiv.org/abs/2611.11209) | [PDF](https://arxiv.org/pdf/2611.11209) | [papers.cool](https://papers.cool/arxiv/2611.11209)
- Authors: Ningning Wang, Beier Zhu, Xingyu Zhu, Kaiyun Yang, Xun Yang
- Published: 2026-11-08 07:57 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: evaluation
- Abstract skim: Visual chain-of-thought (visual-CoT), also known as "thinking with images", equips LVLMs with the ability to locate and use key visual evidence for reasoning. However, acquiring such visual-CoT capabilities requires costly post-training and tightly couples them to a specific backbone, making transfer to other LVLMs...

### 37 - REINS: A Self-Evolving Agent Harness for Real-Time Trajectory Planning

- arXiv: [2611.10748](https://arxiv.org/abs/2611.10748) | [PDF](https://arxiv.org/pdf/2611.10748) | [papers.cool](https://papers.cool/arxiv/2611.10748)
- Authors: Zhihong Cui, Hengyu Liu, Haoran Tang, Shijun Liu, Amir Taherkordi, Tor Skeie
- Published: 2026-11-07 14:11 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: agent harness; reasoning: reasoning; planning_and_action: planning, trajectory, rollout; memory_and_benchmarks: memory
- Abstract skim: Agent harnesses -- runtime scaffolds that wrap an LLM's reasoning loop with tool dispatch, verification, and persistent memory -- have become the standard substrate for deploying LLMs as autonomous agents, as demonstrated by Claude Code and Codex in software engineering. In trajectory planning, however, this...

### 37 - LongCapHarness: Capability-Guided Auto-Harnessing for Long-Context Reasoning

- arXiv: [2611.10463](https://arxiv.org/abs/2611.10463) | [PDF](https://arxiv.org/pdf/2611.10463) | [papers.cool](https://papers.cool/arxiv/2611.10463)
- Authors: Tao Zhang, Yuhang He
- Published: 2026-11-07 04:26 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, self-improvement, self improvement
- Abstract skim: Existing methods enhancing an LLM's long-context reasoning capability often rely on data synthesis and follow-up LLM post-training. However, the data synthesis strategy and the post-training recipes are empirically driven and computationally intensive. In this work, we propose a new framework, dubbed LongCapHarness,...

### 36 - MIRIX-2.0: Multi-Agent Memory System

- arXiv: [2611.12068](https://arxiv.org/abs/2611.12068) | [PDF](https://arxiv.org/pdf/2611.12068) | [papers.cool](https://papers.cool/arxiv/2611.12068)
- Authors: Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan, Peng Xia, Yu Wang
- Published: 2026-11-09 08:43 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent, agent memory; memory_and_benchmarks: memory, long-term memory, alfworld
- Abstract skim: Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system designed to be practical, accurate, and...

### 35 - Jais 3: Introducing Arabic-centric Agentic AI

- arXiv: [2611.10224](https://arxiv.org/abs/2611.10224) | [PDF](https://arxiv.org/pdf/2611.10224) | [papers.cool](https://papers.cool/arxiv/2611.10224)
- Authors: Team IFM, Haonan Li, Hadi Abdine, Nikhil Ranjan, Mohamed Anwar, Ahmad Chamma, et al. (55 authors)
- Published: 2026-11-06 21:11 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr, preference optimization; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: We present Jais 3, a fleet of six open, Arabic-centric agentic language models ranging from 0.9B to 375B parameters. Jais 3 is built to complete tasks for Arabic speakers, not only to answer questions in plain text: it is trained to plan multi-step tasks, call tools and Model Context Protocol (MCP) servers, operate...

### 34 - ECOS: Environment-Calibrated On-Policy Self-Distillation for Language Agents

- arXiv: [2611.12232](https://arxiv.org/abs/2611.12232) | [PDF](https://arxiv.org/pdf/2611.12232) | [papers.cool](https://papers.cool/arxiv/2611.12232)
- Authors: Chenhao Zhang, Zhongan Wang, Mingxuan Li, Hehe Fan, Zheng Zhu, Ming Li
- Published: 2026-11-09 11:25 UTC | Categories: cs.AI
- Why it matched: agentic_rl: language agent; rl_post_training: grpo; memory_and_benchmarks: alfworld
- Abstract skim: On-policy self-distillation lets a language agent act as its own Teacher by conditioning on privileged context such as skills written from its own trajectories. Its guidance, however, is weighted by how much this context shifts token likelihoods rather than by whether it improves behavior, so errors in self-written...

### 34 - AutoC2V: Synthesis-Guided LLM Training for QoR-Optimized C++-to-Verilog Generation

- arXiv: [2611.10824](https://arxiv.org/abs/2611.10824) | [PDF](https://arxiv.org/pdf/2611.10824) | [papers.cool](https://papers.cool/arxiv/2611.10824)
- Authors: Guanqi Lyu, Fei Zhao, Zhaojun Lu, Jiaji He, Yongqiang Lyu
- Published: 2026-11-07 16:05 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, reward model, group relative policy optimization, grpo; memory_and_benchmarks: evaluation
- Abstract skim: High-level synthesis (HLS) can translate C/C++ kernels into register-transfer level (RTL) designs, yet generating high-quality hardware still relies heavily on manual pragma tuning and repeated synthesis evaluation. We propose AutoC2V, a C++-to-Verilog generation framework driven by real synthesis feedback that...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
