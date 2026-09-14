# RL / Post-Training / Agentic RL Reading Queue - 2026-09-14

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 336. Minimum score: 8.

## Top Picks

### 58 - Direct Preference Density Alignment for Conversational Audio Equalization

- arXiv: [2609.12607](https://arxiv.org/abs/2609.12607) | [PDF](https://arxiv.org/pdf/2609.12607) | [papers.cool](https://papers.cool/arxiv/2609.12607)
- Authors: Ioannis Stylianou, Sven Ewan Shepstone, Jon Francombe, Pablo Martinez Nuevo, Zheng-Hua Tan
- Published: 2026-09-11 09:05 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, preference optimization, policy optimization, reward model, +3 more; memory_and_benchmarks: memory
- Abstract skim: Large Language Model alignment typically relies on learned proxy reward models, which significantly increase the memory footprint during training and are notoriously prone to instability and reward hacking. While offline methods like Direct Preference Optimization (DPO) bypass the reward model, they lose the ability...

### 56 - Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent Reinforcement Learning

- arXiv: [2609.12424](https://arxiv.org/abs/2609.12424) | [PDF](https://arxiv.org/pdf/2609.12424) | [papers.cool](https://papers.cool/arxiv/2609.12424)
- Authors: Taoran Liang, Yang Liu, Shang Luo, Yingguang Yang, Rongrong Zhang, Yingzong Min, et al. (12 authors)
- Published: 2026-09-11 04:19 UTC | Categories: cs.LG
- Why it matched: agentic_rl: llm agent; rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning is now the standard way to train large language model agents on long-horizon tasks, where dozens of interdependent actions precede a single sparse reward. Critic-free, group-relative methods such as GRPO suit this regime, but they broadcast one trajectory-level scalar to every step and cannot...

### 54 - Hierarchical Belief Modeling for Zero-Shot Opponent Adaptation in Partially Observable Multi-Agent Navigation

- arXiv: [2609.12422](https://arxiv.org/abs/2609.12422) | [PDF](https://arxiv.org/pdf/2609.12422) | [papers.cool](https://papers.cool/arxiv/2609.12422)
- Authors: Kowei Shih, Lu Cheng, Zeyu Wang, Yeyun Xu, Kejian Tong
- Published: 2026-09-11 04:17 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: ppo; reasoning: reasoning; planning_and_action: world model; memory_and_benchmarks: memory
- Abstract skim: Lux AI Season 3 requires agents to act under partial observability, randomized episode level dynamics, and a best of five match structure that rewards both tactical execution and fast adaptation. We present HORIZON, a hierarchical agent that combines symmetry aware spatial perception, dual memory belief tracking,...

### 51 - Expert-Space Exploration in MoE Reinforcement Learning

- arXiv: [2609.13058](https://arxiv.org/abs/2609.13058) | [PDF](https://arxiv.org/pdf/2609.13058) | [papers.cool](https://papers.cool/arxiv/2609.13058)
- Authors: Hongyi He, Zhenghao Lin, Xiao Liu, Peng Cheng, Yan Lu, Yeyun Gong
- Published: 2026-09-11 16:58 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) has become central to post-training of large language models. Recent advances in RL for Mixture-of-Experts (MoE) models have primarily focused on improving optimization stability and training efficiency, while treating the expert selection as a fixed component. Since routing determines...

### 50 - CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models

- arXiv: [2609.13060](https://arxiv.org/abs/2609.13060) | [PDF](https://arxiv.org/pdf/2609.13060) | [papers.cool](https://papers.cool/arxiv/2609.13060)
- Authors: Blake Olson, Yuhang Song, Emmett McQuinn, Yuan Shangguan
- Published: 2026-09-11 16:59 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Diffusion Language Models (DLMs) offer promising parallel generation capabilities but lag behind autoregressive models in complex reasoning and tool-use tasks. While Reinforcement Learning (RL) has recently been applied to enhance DLMs, standard RL approaches suffer from an exploration bottleneck. To address this,...

### 41 - Earth-Agent-Pro: Towards Real-World Full-Chain Earth Observation with Agents

- arXiv: [2609.12533](https://arxiv.org/abs/2609.12533) | [PDF](https://arxiv.org/pdf/2609.12533) | [papers.cool](https://papers.cool/arxiv/2609.12533)
- Authors: Zhutao Lv, Chenhao Dang, Yi Feng, Yanpei Gong, Xiaolei Wang, Junyan Ye, et al. (8 authors)
- Published: 2026-09-11 07:41 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: policy optimization, group relative policy optimization; planning_and_action: planning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Real-world Earth observation (EO) agents must translate high-level scientific questions into executable workflows to acquire observations, prepare data, perform domain computations, and derive conclusions from runtime evidence. Existing EO agents typically start from supplied observations, while benchmarks typically...

### 36 - BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents

- arXiv: [2609.12394](https://arxiv.org/abs/2609.12394) | [PDF](https://arxiv.org/pdf/2609.12394) | [papers.cool](https://papers.cool/arxiv/2609.12394)
- Authors: Tong Ye, Kunyang Han, Guozhi Wang, Longqiang Luo, Zhifeng Ding, Yongxiang Zhang, et al. (43 authors)
- Published: 2026-09-11 03:36 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: trajectory, rollout; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Mobile GUI agents are shifting from multi-module frameworks to native models trained end-to-end, yet industrial deployment faces three persistent gaps. Sandbox training produces a distribution mismatch with production environments; expensive real-device failures remain underutilized; and fixed benchmarks saturate,...

### 34 - Sampling via Decision-Flow: Training-Free Extraction of Improved Latent Reasoning Paths in Large Language Models

- arXiv: [2609.12317](https://arxiv.org/abs/2609.12317) | [PDF](https://arxiv.org/pdf/2609.12317) | [papers.cool](https://papers.cool/arxiv/2609.12317)
- Authors: Zhendong Mi, Shaoyi Huang
- Published: 2026-09-11 00:48 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: A central question in LLM reasoning is whether reinforcement learning (RL) instills genuinely new capabilities or merely reshapes how existing knowledge is expressed during inference. Building on the distribution-sharpening hypothesis, which holds that RL reallocates probability mass toward high-reward trajectories...

### 32 - Distortion of AI Alignment Revisited: RLHF is a Decent Utilitarian Aligner

- arXiv: [2609.12651](https://arxiv.org/abs/2609.12651) | [PDF](https://arxiv.org/pdf/2609.12651) | [papers.cool](https://papers.cool/arxiv/2609.12651)
- Authors: Kazusato Oko, Annie Ulichney, Nika Haghtalab, Han Bao
- Published: 2026-09-11 09:55 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf
- Abstract skim: While Reinforcement Learning from Human Feedback (RLHF) is the standard paradigm for aligning large language models with human preferences, its effectiveness in pluralistic settings has been called into question. Notably, recent work by Gölz et al. (2025) demonstrated that the \textit{distortion} -- defined as the...

### 32 - Reinforcement Learning over Patient Trajectories for Clinical Reasoning in EHR Foundation Models

- arXiv: [2609.12277](https://arxiv.org/abs/2609.12277) | [PDF](https://arxiv.org/pdf/2609.12277) | [papers.cool](https://papers.cool/arxiv/2609.12277)
- Authors: Yuxin Xiao, Sheng Zhang, Chandan Singh, Tristan Naumann, Hoifung Poon, Jianfeng Gao, et al. (7 authors)
- Published: 2026-09-10 23:10 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Electronic health record (EHR) foundation models trained on longitudinal patient trajectories have demonstrated strong performance across diverse clinical prediction tasks. However, their clinical reasoning capabilities remain constrained by next-token prediction on limited and incomplete EHR data. To address this,...

### 32 - DIA: Denoising Intermediate Advantage for Diffusion Policy Optimization

- arXiv: [2609.12245](https://arxiv.org/abs/2609.12245) | [PDF](https://arxiv.org/pdf/2609.12245) | [papers.cool](https://papers.cool/arxiv/2609.12245)
- Authors: Arjun Sohal, Yuchi Zhao, Miroslav Bogdanovic, Alan Aspuru-Guzik
- Published: 2026-09-10 22:02 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Diffusion-based robot policies have become widely used in robotic manipulation, where they are typically trained with behavior cloning. However, policies trained purely from demonstrations are limited by the quality and coverage of the available data. Reinforcement learning can further improve the performance of...

### 28 - Curriculum-Based Adversarial Heterogeneous Agent Reinforcement Learning for Autonomous Quad-Copter Landing in Maritime Settings

- arXiv: [2609.12758](https://arxiv.org/abs/2609.12758) | [PDF](https://arxiv.org/pdf/2609.12758) | [papers.cool](https://papers.cool/arxiv/2609.12758)
- Authors: Allan Minh-Tam Nguyen, Sree Showrya Kotala, Stefan Banioi-Crijman, Kurt Driessens, Rico Möckel
- Published: 2026-09-11 12:09 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Recovering unmanned aerial vehicles (UAVs) in maritime environments is challenging due to wind turbulence and ship-deck motion, making it a valuable test case for alternative control and learning approaches as conventional landing approaches often become unreliable. We study simulated mid-air capture of quadrotor...

### 27 - SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking

- arXiv: [2609.13141](https://arxiv.org/abs/2609.13141) | [PDF](https://arxiv.org/pdf/2609.13141) | [papers.cool](https://papers.cool/arxiv/2609.13141)
- Authors: Zhiwei Li, Lei Zhu, Hao Gu, Xiang Hu, Yan Wang, Haitao Mi, et al. (9 authors)
- Published: 2026-09-11 17:58 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Post-training attention sparsification reduces the quadratic cumulative attention cost of pretrained Transformers by selecting a small set of context units (tokens or blocks) for each query. Existing trainable methods usually use a lightweight selector to score context units, followed by hard Top-K selection that...

### 26 - Robust Policy Optimization via Adversarial Importance Sampling

- arXiv: [2609.13044](https://arxiv.org/abs/2609.13044) | [PDF](https://arxiv.org/pdf/2609.13044) | [papers.cool](https://papers.cool/arxiv/2609.13044)
- Authors: Amine Andam, Jamal Bentahar, Mustapha Hedabou
- Published: 2026-09-11 16:40 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: evaluation
- Abstract skim: Significant progress has been made in safeguarding deep reinforcement learning (DRL) policies against input perturbations. Developing robust DRL involves three main stages: algorithm design, implementation, and evaluation. In this work, we identify and address a key limitation at each stage. First, we introduce...

### 26 - Offline Reinforcement Learning for Wind Farm Control: A Wind Tunnel Study under Dynamic Wind Directions

- arXiv: [2609.12905](https://arxiv.org/abs/2609.12905) | [PDF](https://arxiv.org/pdf/2609.12905) | [papers.cool](https://papers.cool/arxiv/2609.12905)
- Authors: Yuhan Su, Hongyang Dong, Simone Tamaro, Filippo Campagnolo, Carlo L. Bottasso, Xiaowei Zhao
- Published: 2026-09-11 14:31 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: benchmark
- Abstract skim: This paper addresses the wind farm power maximization problem in the presence of wind direction changes. Specifically, a model-free Modified Twin Delayed Deep Deterministic Policy Gradient with Behavior Cloning (MTD3-BC) algorithm is proposed to tackle this task through yaw control under varying wind direction...

### 25 - Chopthin-Consensus Power Sampling: A Diversity-Preserving Approach to LLM Decoding

- arXiv: [2609.12243](https://arxiv.org/abs/2609.12243) | [PDF](https://arxiv.org/pdf/2609.12243) | [papers.cool](https://papers.cool/arxiv/2609.12243)
- Authors: Minoo Ahmadi, Seyedarmin Azizi, Erfan Baghaei Potraghloo, Mehdi Kamal, Massoud Pedram
- Published: 2026-09-10 22:02 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Inference-time power sampling via Sequential Monte Carlo (SMC) can substantially improve large language model (LLM) reasoning without requiring post-training. However, many existing SMC approaches rely on equal-weight resampling, which can aggressively prune low-weight trajectories, discarding potentially correct...

### 23 - ParaRecover: A Process-Level Benchmark for Error Localization and Recovery in Parallel Tool-Use Agents

- arXiv: [2609.12345](https://arxiv.org/abs/2609.12345) | [PDF](https://arxiv.org/pdf/2609.12345) | [papers.cool](https://papers.cool/arxiv/2609.12345)
- Authors: Bowen Guan, Zhentao Yin, Yanming Shen
- Published: 2026-09-11 02:09 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Existing agent benchmarks mainly evaluate final task success or tool-call correctness, providing limited insight into whether agents can reliably diagnose and recover from intermediate execution failures. This limitation becomes particularly critical in multi-turn parallel tool-use scenarios, where errors may...

### 22 - AIM: A Privacy-Aware Interoperable Memory Framework for Multi-Agent Multi-User LLM Systems

- arXiv: [2609.12320](https://arxiv.org/abs/2609.12320) | [PDF](https://arxiv.org/pdf/2609.12320) | [papers.cool](https://papers.cool/arxiv/2609.12320)
- Authors: Zachary Johnson, Nigel Boachie Kumankumah, Somya Chatterjee, Tejas Sathyamurthi, Min Chen, Xinyi Alice Li, et al. (11 authors)
- Published: 2026-09-11 01:00 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: memory, benchmark
- Abstract skim: Traditional large language models (LLMs) are scoped to individual user sessions, limiting their knowledge to a single conversation and preventing them from learning user preferences that evolve over time. Existing agentic memory systems address this limitation but generally operate at the individual-user level,...

### 21 - Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model

- arXiv: [2609.13053](https://arxiv.org/abs/2609.13053) | [PDF](https://arxiv.org/pdf/2609.13053) | [papers.cool](https://papers.cool/arxiv/2609.13053)
- Authors: Hoeun Lee, Jaeik Kim, Jusang Oh, Jinhyeok Kim, Geon Choi, Hyeonggeun Kim, et al. (7 authors)
- Published: 2026-09-11 16:49 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: post-training, post training; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Visual goal and dynamics prediction can provide language-conditioned robot policies with both a target outcome and a representation of action-dependent scene changes. We bring these predictions into action generation and selection through a shared trajectory model. Dynin-Robotics implements this formulation on...

### 21 - Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving

- arXiv: [2609.12606](https://arxiv.org/abs/2609.12606) | [PDF](https://arxiv.org/pdf/2609.12606) | [papers.cool](https://papers.cool/arxiv/2609.12606)
- Authors: Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu
- Published: 2026-09-11 09:00 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: While multimodal reasoning has advanced rapidly, solving complex geometry problems critically hinges on active visual assistance, such as constructing auxiliary lines, spurring the rise of Visual Chain-of-Thought (VCoT). However, existing evaluations typically assess visual generation quality and final answer...

### 21 - SoK: Rethinking Jailbreaking in the Era of Agentic AI: Attacks, Defenses, and Practical Consideration

- arXiv: [2609.12413](https://arxiv.org/abs/2609.12413) | [PDF](https://arxiv.org/pdf/2609.12413) | [papers.cool](https://papers.cool/arxiv/2609.12413)
- Authors: Md Jueal Mia, Yanzhao Wu, Selcuk Uluagac, M. Hadi Amini
- Published: 2026-09-11 04:04 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Large language models (LLMs) are rapidly evolving from conversational assistants into agentic AI systems that reason, plan, invoke tools, maintain persistent memory, communicate with other agents, and execute multi-step tasks. At the same time, modern models exhibit substantially stronger native safety alignment...

### 21 - VRL-Bench: Benchmarking agents on computer control tasks under finite trial budgets

- arXiv: [2609.12404](https://arxiv.org/abs/2609.12404) | [PDF](https://arxiv.org/pdf/2609.12404) | [papers.cool](https://papers.cool/arxiv/2609.12404)
- Authors: Yu Bai, Yukai Miao, Dawei Wang, Li Chen, Yanyu Ren, Yuqian Shi, et al. (11 authors)
- Published: 2026-09-11 03:54 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reflection; memory_and_benchmarks: memory, evaluation
- Abstract skim: Learning from trial and error is a promising way to improve language agents on complex tasks such as computer control. Reflexion introduced verbal reinforcement learning, which turns failed trials into text that guides later attempts without updating model parameters. We introduce VRL-Bench, a harness for fair...

### 21 - Repair Before Reinforce: Context-Augmented Knowledge Graph Reasoning for Multi-Hop Question Answering

- arXiv: [2609.12230](https://arxiv.org/abs/2609.12230) | [PDF](https://arxiv.org/pdf/2609.12230) | [papers.cool](https://papers.cool/arxiv/2609.12230)
- Authors: Tharaka D. Fonseka, Niraj K. Jha
- Published: 2026-09-10 21:39 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Question-answering often requires reasoning across multiple connected facts rather than retrieving a single isolated relation. Knowledge graphs (KGs) provide a structured way to represent such facts, but training large language models (LLMs) only on isolated KG head-relation-tail triples may limit their ability to...

### 20 - Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural Reasoning for Language Models

- arXiv: [2609.13005](https://arxiv.org/abs/2609.13005) | [PDF](https://arxiv.org/pdf/2609.13005) | [papers.cool](https://papers.cool/arxiv/2609.13005)
- Authors: Utkarsh Soni, Syed Shariyar Murtaza, Yifan Nie, Sachin Chandrasekhar, Eugene Wen
- Published: 2026-09-11 16:04 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agent harness; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Large language models (LLMs) have achieved strong performance on a wide range of natural language tasks, and recent benchmarks suggest that they are increasingly adept at multi-hop reasoning. However, these benchmarks are typically short-horizon, requiring only a small number of retrieval or inference steps, and...

### 20 - From Collaboration to Capability: Internalizing Routed LLM Experts into Compact Reasoners

- arXiv: [2609.12578](https://arxiv.org/abs/2609.12578) | [PDF](https://arxiv.org/pdf/2609.12578) | [papers.cool](https://papers.cool/arxiv/2609.12578)
- Authors: Frank Nie, Shuyao Wang, Ethan B. Liu
- Published: 2026-09-11 08:31 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: A compact controller can coordinate stronger experts by selecting whom to consult, formulating requests, and integrating their responses. We study whether learning from both the controller's decisions and the experts' reasoning and code improves its generation after expert removal. We introduce \textsc{Rivet} for...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
