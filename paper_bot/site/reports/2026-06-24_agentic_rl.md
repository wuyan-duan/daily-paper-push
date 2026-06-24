# RL / Post-Training / Agentic RL Reading Queue - 2026-06-24

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 323. Minimum score: 8.

## Top Picks

### 42 - ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning

- arXiv: [2606.24601](https://arxiv.org/abs/2606.24601) | [PDF](https://arxiv.org/pdf/2606.24601) | [papers.cool](https://papers.cool/arxiv/2606.24601)
- Authors: Anurag Akula, Satheesh K. Perepu, Abhishek Sarkar, Kaushik Dey
- Published: 2026-06-23 14:03 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark
- Abstract skim: Multi-agent reinforcement learning (MARL) addresses the problem of training multiple agents that pursue collaborative, competitive, or mixed objectives. Prior work has investigated transfer learning between source and target domains in MARL; however, the majority of existing approaches impose the constraint that the...

### 40 - LaGO: Latent Action Guidance for Online Reinforcement Learning

- arXiv: [2606.24669](https://arxiv.org/abs/2606.24669) | [PDF](https://arxiv.org/pdf/2606.24669) | [papers.cool](https://papers.cool/arxiv/2606.24669)
- Authors: Kuan-Yen Liu, Ren-Jyun Huang, Ti-Rong Wu
- Published: 2026-06-23 15:03 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; planning_and_action: planning, decision making; memory_and_benchmarks: benchmark
- Abstract skim: Large language models (LLMs) have shown strong potential for planning and sequential decision-making, but prior work often relies on using them as direct controllers, which requires precise action generation and can be unreliable in practice. This paper proposes Latent Action Guidance for Online Reinforcement...

### 37 - Weight-Space Geometry of Offline Reasoning Training

- arXiv: [2606.23740](https://arxiv.org/abs/2606.23740) | [PDF](https://arxiv.org/pdf/2606.23740) | [papers.cool](https://papers.cool/arxiv/2606.23740)
- Authors: Aleksandr Nikolich, Igor Kiselev, Vladimir Platonov, Karina Romanova
- Published: 2026-06-21 15:34 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo, dpo; reasoning: reasoning
- Abstract skim: Offline reinforcement-learning losses (RFT, RIFT, DFT, Offline GRPO, DPO) are widely used to distill reasoning from large teachers into smaller students, and are typically compared on downstream accuracy alone. We ask whether they are mechanistically distinct or converge to a similar weight update. Training six...

### 36 - AsyncOPD: How Stale Can On-Policy Distillation Be?

- arXiv: [2606.24143](https://arxiv.org/abs/2606.24143) | [PDF](https://arxiv.org/pdf/2606.24143) | [papers.cool](https://papers.cool/arxiv/2606.24143)
- Authors: Wonjun Kang, Kevin Galim, Seunghyuk Oh, Minjun Kang, Sanghyun Park, Donghoon Kim, et al. (12 authors)
- Published: 2026-06-23 04:50 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: On-policy distillation (OPD) trains a student on its own rollouts guided by teacher feedback and is becoming increasingly important for large language model (LLM) post-training. Like reinforcement learning (RL), however, OPD faces an on-policy systems bottleneck, as rollouts can dominate training time for reasoning...

### 35 - Beyond Trajectory Imitation: Strategy-Guided Policy Optimization for LLM Reasoning

- arXiv: [2606.24064](https://arxiv.org/abs/2606.24064) | [PDF](https://arxiv.org/pdf/2606.24064) | [papers.cool](https://papers.cool/arxiv/2606.24064)
- Authors: Tianyuan Shi, Canbin Huang, Bei Li, Xin Chen, Xiaojun Quan, Jingang Wang, et al. (7 authors)
- Published: 2026-06-23 02:14 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Distilling reasoning capabilities from strong to weak language models typically involves imitating specific solution trajectories, effectively transferring what to answer rather than how to reason. This trajectory-level imitation encourages memorization of instance-specific steps rather than acquisition of...

### 33 - Qwen-AgentWorld: Language World Models for General Agents

- arXiv: [2606.24597](https://arxiv.org/abs/2606.24597) | [PDF](https://arxiv.org/pdf/2606.24597) | [papers.cool](https://papers.cool/arxiv/2606.24597)
- Authors: Yuxin Zuo, Zikai Xiao, Li Sheng, Fei Huang, Jianhong Tu, Yuxuan Liu, et al. (33 authors)
- Published: 2026-06-23 13:53 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic rl; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: planning, world model; memory_and_benchmarks: benchmark
- Abstract skim: A world model predicts environment dynamics based on current observations and actions, serving as a core cognitive mechanism for reasoning and planning. In this work, we investigate how world modeling based on language models can further push the boundaries of general agents. (i) We first focus on building...

### 32 - Accelerating Disaggregated RL for Visual Generative LLMs with Diffusion-Based Parallelism and Trainer-Assisted Generation

- arXiv: [2606.24369](https://arxiv.org/abs/2606.24369) | [PDF](https://arxiv.org/pdf/2606.24369) | [papers.cool](https://papers.cool/arxiv/2606.24369)
- Authors: Sijie Wang, Zhengyu Qing, Zhiqiang Tan, Yiming Yin, Yeqing Zhang, Yaoyuan Wang, et al. (9 authors)
- Published: 2026-06-23 09:59 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: rollout; downranked: driving
- Abstract skim: Reinforcement learning (RL) has become a dominant post-training paradigm, driving the emergence of high-performance RL systems such as veRL for autoregressive large language models (LLMs). In parallel, diffusion-oriented RL algorithms, e.g., DanceGRPO and FlowGRPO, have rapidly expanded the scope of RL from language...

### 32 - KLip-PPO: A per-sample KL perspective on PPO-Clip

- arXiv: [2606.23932](https://arxiv.org/abs/2606.23932) | [PDF](https://arxiv.org/pdf/2606.23932) | [papers.cool](https://papers.cool/arxiv/2606.23932)
- Authors: Riccardo Colletti, Robin Holzinger
- Published: 2026-06-22 20:52 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Proximal Policy Optimization (PPO) is the standard policy-gradient algorithm for on-policy reinforcement learning. The literature presents it in two forms, a clipped surrogate that bounds the importance ratio between successive policies and a Kullback-Leibler penalty between them. These forms are treated as separate...

### 31 - Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation

- arXiv: [2606.24515](https://arxiv.org/abs/2606.24515) | [PDF](https://arxiv.org/pdf/2606.24515) | [papers.cool](https://papers.cool/arxiv/2606.24515)
- Authors: Marta Sumyk, Oleksandr Kosovan
- Published: 2026-06-23 12:46 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: acting; memory_and_benchmarks: evaluation
- Abstract skim: Computer-Use Agents (CUAs) execute high-level user goals by perceiving and acting directly within graphical user interfaces. However, reinforcement learning for CUAs remains difficult because open-ended desktop environments rarely provide scalable, machine-readable reward signals: task success is often visually...

### 30 - DramaDirector: Geometry-Guided Short Drama Generation

- arXiv: [2606.24107](https://arxiv.org/abs/2606.24107) | [PDF](https://arxiv.org/pdf/2606.24107) | [papers.cool](https://papers.cool/arxiv/2606.24107)
- Authors: Hengji Zhou, Sijie Liu, Jianrun Chen, Xingchen Zou, Lianghao Xia, Liqiang Nie
- Published: 2026-06-23 03:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: grpo; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Short dramas, with their rapid shot rhythms, dialogue-driven focus shifts, and demanding cinematographic grounding, pose challenges that prompt-level or text-only video generation pipelines struggle to meet. We study plot-to-short-drama generation, where a global plot and local context are transformed into visually...

### 29 - Learning to Trigger: Reinforcement Learning at the Large Hadron Collider

- arXiv: [2606.23993](https://arxiv.org/abs/2606.23993) | [PDF](https://arxiv.org/pdf/2606.23993) | [papers.cool](https://papers.cool/arxiv/2606.23993)
- Authors: Zixin Ding, Shaghayegh Emam, Giovanna Salvi, Cecilia Tosciri, Abhijith Gandrakota, Jennifer Ngadiuba, et al. (10 authors)
- Published: 2026-06-22 22:56 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: decision making; memory_and_benchmarks: benchmark
- Abstract skim: High-throughput scientific facilities such as the Large Hadron Collider depend on real-time event filtering (\textit{triggering}) under tight constraints on bandwidth, latency, and storage. In practice, trigger menus are largely static and hand-tuned and can become suboptimal as detector conditions, pileup, and...

### 28 - Governed Shared Memory for Multi-Agent LLM Systems

- arXiv: [2606.24535](https://arxiv.org/abs/2606.24535) | [PDF](https://arxiv.org/pdf/2606.24535) | [papers.cool](https://papers.cool/arxiv/2606.24535)
- Authors: Yanki Margalit, Nurit Cohen-Inger, Erni Avram, Ran Taig, Oded Margalit
- Published: 2026-06-23 13:04 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent memory; memory_and_benchmarks: memory, evaluation
- Abstract skim: Multi-agent LLM environments require robust mechanisms for shared knowledge management. This paper formalizes the fleet-memory problem and identifies four foundational failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse. To address these, we define explicit...

### 28 - Safe and Generalizable Hierarchical Multi-Agent RL via Constraint Manifold Control

- arXiv: [2606.24010](https://arxiv.org/abs/2606.24010) | [PDF](https://arxiv.org/pdf/2606.24010) | [papers.cool](https://papers.cool/arxiv/2606.24010)
- Authors: Zihao Guo, Jianing Zhao, Ling Li, Hao Liang, Giuseppe Loianno, Yali Du
- Published: 2026-06-22 23:32 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Multi-agent systems are widely used in safety-critical applications that require coordinated behavior under strict safety constraints. Existing approaches face a fundamental trade-off: learning-based methods achieve strong empirical performance but lack theoretical safety guarantees, while control-theoretic methods...

### 27 - MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery

- arXiv: [2606.24595](https://arxiv.org/abs/2606.24595) | [PDF](https://arxiv.org/pdf/2606.24595) | [papers.cool](https://papers.cool/arxiv/2606.24595)
- Authors: Enze Ma, Yufan Zhou, Wei-Chieh Huang, Jie Yang, Huanhuan Ma, Zixuan Wang, et al. (10 authors)
- Published: 2026-06-23 13:52 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agent memory; planning_and_action: trajectory; memory_and_benchmarks: memory, long-term memory, benchmark
- Abstract skim: Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which...

### 27 - video-SALMONN-R$^3$: Learning to ReWatch, ReAsk, and ReAnswer for Efficient Video Understanding

- arXiv: [2606.24477](https://arxiv.org/abs/2606.24477) | [PDF](https://arxiv.org/pdf/2606.24477) | [papers.cool](https://papers.cool/arxiv/2606.24477)
- Authors: Yixuan Li, Guangzhi Sun, Yudong Yang, Wei Li, Zejun MA, Chao Zhang
- Published: 2026-06-23 12:13 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: memory
- Abstract skim: Video large language models (LLMs) are often constrained by computation and memory budgets, leading them to use reduced frame rates and spatial resolutions, which may cause them to miss critical information for question answering (QA). A practical and efficient solution is a two-stage paradigm: first perform coarse...

### 26 - Themis: An explainable AI-enabled framework for Reinforcement Learning with Human Feedback

- arXiv: [2606.24622](https://arxiv.org/abs/2606.24622) | [PDF](https://arxiv.org/pdf/2606.24622) | [papers.cool](https://papers.cool/arxiv/2606.24622)
- Authors: Andreas Chouliaras, Luke Connolly, Dimitris Chatzpoulos
- Published: 2026-06-23 14:20 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback; memory_and_benchmarks: evaluation
- Abstract skim: Training safe Reinforcement Learning (RL) systems is inherently challenging, with no guarantee of avoiding unwanted behaviors. The most effective defenses against this are (i) transparency through explainability and (ii) alignment via human feedback. While both show promising results, no publicly available framework...

### 25 - CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic Video Captioning

- arXiv: [2606.24636](https://arxiv.org/abs/2606.24636) | [PDF](https://arxiv.org/pdf/2606.24636) | [papers.cool](https://papers.cool/arxiv/2606.24636)
- Authors: Xinyu Mao, Yuhui Zeng, Xiaokun Liu, Wenyu Qin, Meng Wang, Xin Tao, et al. (9 authors)
- Published: 2026-06-23 14:29 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Cinematographic captioning aims to describe how a video is filmed using professional film-language concepts such as camera movement, shot size, depth of field, composition, and shooting angle. This capability is important for fine-grained video understanding and controllable movie-quality video generation, yet...

### 25 - E-MRL: Cross-view Aligned Evidence-driven Multimodal Reinforcement Learning for Reliable 3D Tumor Analysis

- arXiv: [2606.23888](https://arxiv.org/abs/2606.23888) | [PDF](https://arxiv.org/pdf/2606.23888) | [papers.cool](https://papers.cool/arxiv/2606.23888)
- Authors: Sijing Li, Zhongwei Qiu, Zhuoya Wang, Boxiang Yun, Zhenyu Yi, Jianwei Xu, et al. (9 authors)
- Published: 2026-06-22 19:34 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: While Vision-Language Models (VLMs) show great promise in volumetric medical report generation, they frequently suffer from visual hallucinations and a lack of grounding in 3D CT data. Current Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) strategies typically optimize text fidelity alone, essentially...

### 22 - SHERLOC: Structured Diagnostic Localization for Code Repair Agents

- arXiv: [2606.24820](https://arxiv.org/abs/2606.24820) | [PDF](https://arxiv.org/pdf/2606.24820) | [papers.cool](https://papers.cool/arxiv/2606.24820)
- Authors: Hovhannes Tamoyan, Sean Narenthiran, Erik Arakelyan, Mira Mezini, Boris Ginsburg
- Published: 2026-06-23 17:05 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent, tool use, agent orchestration; reasoning: reasoning
- Abstract skim: LLM agents solve repository-level coding tasks through multi-turn tool use, but utilize half their budget on locating faults before editing. Dedicated localization frameworks have emerged, yet are still evaluated as file retrieval rather than actionable diagnosis, producing locations without the diagnostic context a...

### 22 - ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling

- arXiv: [2606.24437](https://arxiv.org/abs/2606.24437) | [PDF](https://arxiv.org/pdf/2606.24437) | [papers.cool](https://papers.cool/arxiv/2606.24437)
- Authors: Heng Ping, Arijit Bhattacharjee, Peiyu Zhang, Shixuan Li, Wei Yang, Ali Jannesari, et al. (8 authors)
- Published: 2026-06-23 11:14 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines. However, existing MoA variants fail to sustain gains as depth increases, exhibiting degradation, early plateauing, or saturation. We propose ReM-MoA, a memory-augmented MoA...

### 22 - NavWM: A Unified Navigation World Model for Foresight-Driven Planning

- arXiv: [2606.24101](https://arxiv.org/abs/2606.24101) | [PDF](https://arxiv.org/pdf/2606.24101) | [papers.cool](https://papers.cool/arxiv/2606.24101)
- Authors: Yanghong Mei, Longteng Guo, Ming-Ming Yu, Guiyu Zhao, Xingjian He, Jing Liu
- Published: 2026-06-23 03:30 UTC | Categories: cs.RO
- Why it matched: reasoning: reasoning; planning_and_action: planning, trajectory, decision making, world model
- Abstract skim: Conventional visual navigation policies often struggle with myopic decision-making and mode collapse in complex environments. While world models offer a promising alternative, existing paradigms typically isolate perception, generation, and control, failing to capture their shared spatio-temporal dynamics. In this...

### 22 - Neuro-Symbolic Drive: Rule-Grounded Faithful Reasoning for Driving VLAs

- arXiv: [2606.23938](https://arxiv.org/abs/2606.23938) | [PDF](https://arxiv.org/pdf/2606.23938) | [papers.cool](https://papers.cool/arxiv/2606.23938)
- Authors: Xiangbo Gao, Xiukun Huang, Boyu Lu, Junge Zhang, Mengjie Mao, Jiachen Li, et al. (8 authors)
- Published: 2026-06-22 20:57 UTC | Categories: cs.AI, cs.CL
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: planning, trajectory; memory_and_benchmarks: benchmark, evaluation; downranked: driving
- Abstract skim: Driving VLA models incorporating Chain-of-Thought (CoT) reasoning are attractive because they leverage pretrained VLM representations and expose intermediate decisions in natural language, yet current rationales often lack the step-by-step decision semantics needed to keep the rationale causally connected to the...

### 21 - SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation

- arXiv: [2606.24626](https://arxiv.org/abs/2606.24626) | [PDF](https://arxiv.org/pdf/2606.24626) | [papers.cool](https://papers.cool/arxiv/2606.24626)
- Authors: Chenyang Zhu, Jiayu Yao, Kushal Chawla, Youbing Yin, Nathan Wolfe, Pengshan Cai, et al. (13 authors)
- Published: 2026-06-23 14:23 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: memory, gaia
- Abstract skim: As autonomous agents tackle increasingly complex multi-step, multi-agent tasks, their execution trajectories have scaled beyond the constraints of even the largest context windows. Current methods for effectively diagnosing agent failures load the full trajectory into an LLM's context window, which suffers from...

### 21 - ScaleToT: Generalizing Structured LLM Reasoning for Billion-Scale Low-Activity User Modeling

- arXiv: [2606.24605](https://arxiv.org/abs/2606.24605) | [PDF](https://arxiv.org/pdf/2606.24605) | [papers.cool](https://papers.cool/arxiv/2606.24605)
- Authors: Tianbao Ma, Chang Xi, Yichuan Zou, Chengen Li, Linxun Chen, Zilong Lu, et al. (10 authors)
- Published: 2026-06-23 14:05 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization; reasoning: reasoning
- Abstract skim: Accurate user modeling often depends on rich interaction histories, which are unavailable for billions of low-activity users. Large Language Models (LLMs) can infer latent user states from static profiles, but this reasoning becomes unreliable when profiles are sparse, and applying an LLM to billions of users is...

### 21 - EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games

- arXiv: [2606.23995](https://arxiv.org/abs/2606.23995) | [PDF](https://arxiv.org/pdf/2606.23995) | [papers.cool](https://papers.cool/arxiv/2606.23995)
- Authors: Tristan Maidment, JB Lanier, Chase McDonald, Nathan Tsang, Eugene Vinitsky, Roy Fox, et al. (8 authors)
- Published: 2026-06-22 23:05 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: rl_post_training: ppo; reasoning: self-play
- Abstract skim: Recent work has established that regularized policy gradient methods such as PPO, when used in self-play, can match or exceed specialized game-theoretic algorithms for solving two-player zero-sum imperfect-information games. The uniform distribution has emerged as a strong policy regularization target for this...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
