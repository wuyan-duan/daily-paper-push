# RL / Post-Training / Agentic RL Reading Queue - 2026-11-17

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 869. Minimum score: 8.

## Top Picks

### 59 - GEM-MM: Reducing VLM Hallucination with Entropy-Guided Preference Alignment

- arXiv: [2611.20016](https://arxiv.org/abs/2611.20016) | [PDF](https://arxiv.org/pdf/2611.20016) | [papers.cool](https://papers.cool/arxiv/2611.20016)
- Authors: Yuanshan Chua, Xuejiao Zhao
- Published: 2026-11-15 13:55 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: rlhf, preference optimization, reward model, dpo; reasoning: reasoning, chain-of-thought, chain of thought, self-improvement, +1 more; memory_and_benchmarks: evaluation
- Abstract skim: Vision-language models (VLMs) are routinely aligned with offline pairwise RLHF objectives, but multimodal preference data is scarce and treats every response token as equally informative. Under a small preference budget, pair construction becomes nearly irrelevant: standard DPO-style, image-conditional, and self-...

### 54 - TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration

- arXiv: [2611.20430](https://arxiv.org/abs/2611.20430) | [PDF](https://arxiv.org/pdf/2611.20430) | [papers.cool](https://papers.cool/arxiv/2611.20430)
- Authors: Xuannan Liu, Tian Lan, Zekun Li, Xing Cui, Zhengfeng Yu, Feihu Jiang, et al. (12 authors)
- Published: 2026-11-16 02:46 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training; reasoning: self-improvement, self improvement; planning_and_action: planning
- Abstract skim: LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and (2) coupled execution that obscures...

### 53 - Stochastic Self-Distillation for Flow-Based Vision-Language-Action Models

- arXiv: [2611.20460](https://arxiv.org/abs/2611.20460) | [PDF](https://arxiv.org/pdf/2611.20460) | [papers.cool](https://papers.cool/arxiv/2611.20460)
- Authors: Jingru Guo, Alessandra Russo, Joey Bose, Christos Ziakas
- Published: 2026-11-16 03:28 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: Flow-based vision-language-action (VLA) models achieve strong performance in robotics through imitation learning, yet fine-tuning them with on-policy reinforcement learning (RL) is limited. In group-based RL methods like Group Relative Policy Optimization (GRPO), every rollout step requires multi-step ODE...

### 51 - GPRM: Global Perspective Process Reward Model

- arXiv: [2611.20755](https://arxiv.org/abs/2611.20755) | [PDF](https://arxiv.org/pdf/2611.20755) | [papers.cool](https://papers.cool/arxiv/2611.20755)
- Authors: Zifan Zhang, Zhengbo Jiao, Shaobo Wang, Jing Zhou, Guoyi Li, Jiayi Chen, et al. (13 authors)
- Published: 2026-11-16 09:03 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, reward model, grpo; reasoning: reasoning, process reward; memory_and_benchmarks: evaluation
- Abstract skim: Process Reward Models (PRMs) are widely used for step-level evaluation of multi-step reasoning in large language models, but existing methods are often limited by weak historical dependency modeling and insufficient global awareness. They typically fail to leverage prior step evaluations for coherent judgment and...

### 51 - Interactive Structured Environment Scaling for Large Language Model Agentic Reasoning

- arXiv: [2611.19871](https://arxiv.org/abs/2611.19871) | [PDF](https://arxiv.org/pdf/2611.19871) | [papers.cool](https://papers.cool/arxiv/2611.19871)
- Authors: Peng Yu, Luoyi Fu, Xinbing Wang, Ying Wen
- Published: 2026-11-15 08:20 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Reinforcement learning via environmental interaction is a cornerstone post-training paradigm for evolving large language models into autonomous agents capable of multi-turn tool use and exploration. Because the environment defines what the policy observes and how actions are verified, its structure directly bounds...

### 49 - Policy Optimization With Multiple Verifiers via Pareto Rankings

- arXiv: [2611.19064](https://arxiv.org/abs/2611.19064) | [PDF](https://arxiv.org/pdf/2611.19064) | [papers.cool](https://papers.cool/arxiv/2611.19064)
- Authors: Kai Yamashita, Shohei Taniguchi, Hiroki Furuta, Masahiro Suzuki, Yutaka Matsuo
- Published: 2026-11-14 01:15 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, preference optimization, policy optimization; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has become an important approach to improving the reasoning capabilities of large language models. In tasks such as code generation and instruction following, multiple verifiers evaluate whether a response satisfies different requirements. Their outcomes provide...

### 48 - Attacker Diversity Reduction in Adaptive LLM Red Teaming

- arXiv: [2611.19680](https://arxiv.org/abs/2611.19680) | [PDF](https://arxiv.org/pdf/2611.19680) | [papers.cool](https://papers.cool/arxiv/2611.19680)
- Authors: Chris Tava
- Published: 2026-11-15 00:15 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, preference optimization, policy optimization, group relative policy optimization, +2 more
- Abstract skim: Reinforcement learning can make automated red-teaming more successful while narrowing the attacks it produces. Co-training an attacker and a defender with group-relative policy optimization (GRPO) has been reported to reduce attacker diversity. This experiment reproduces attack diversity reduction using three runs...

### 47 - WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection

- arXiv: [2611.21373](https://arxiv.org/abs/2611.21373) | [PDF](https://arxiv.org/pdf/2611.21373) | [papers.cool](https://papers.cool/arxiv/2611.21373)
- Authors: Yipeng Du, Yuxi Li, Ying Zhang, Chong Sun, Chen Li, Jing Lyu, et al. (7 authors)
- Published: 2026-11-16 16:36 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting...

### 43 - ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization

- arXiv: [2611.21605](https://arxiv.org/abs/2611.21605) | [PDF](https://arxiv.org/pdf/2611.21605) | [papers.cool](https://papers.cool/arxiv/2611.21605)
- Authors: Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi, Zhichao Xu, et al. (12 authors)
- Published: 2026-11-16 18:59 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinforcement learning (RL) on the final answer cannot correct this, because a guess earns the same reward as reading. We...

### 42 - Assume/Guarantee Contracts for the Compositional Multi-Agent Reinforcement Learning of Heterogeneous Teams

- arXiv: [2611.19078](https://arxiv.org/abs/2611.19078) | [PDF](https://arxiv.org/pdf/2611.19078) | [papers.cool](https://papers.cool/arxiv/2611.19078)
- Authors: Dominic Klukas, Cyrus Neary
- Published: 2026-11-14 01:27 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: evaluation
- Abstract skim: Multi-agent reinforcement learning (MARL) problems for heterogeneous teams require agents to collaborate to complete team tasks while making the best use of diverse agent capabilities. We introduce assume/guarantee contracts for heterogeneous multi-agent systems (AGC-MAS) and Iterative Heterogeneous Assignment for...

### 40 - Exploration of Reinforcement Learning in Generative Recommendation Models

- arXiv: [2611.19742](https://arxiv.org/abs/2611.19742) | [PDF](https://arxiv.org/pdf/2611.19742) | [papers.cool](https://papers.cool/arxiv/2611.19742)
- Authors: Pengfei Zheng, Wuchao Li, Shiyao Wang, Honghui Bao, Hongyi Xie, Jiaxin Deng, et al. (14 authors)
- Published: 2026-11-15 03:01 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: Traditional cascaded recommender systems balance accuracy and efficiency over large item spaces, but misaligned stage-wise objectives hinder end-to-end optimization. Generative recommendation unifies these stages in an autoregressive framework, providing a natural interface for reinforcement learning (RL) to...

### 38 - Contrastive Activation-Guided Zeroth-Order Preference Optimisation for Memory-Efficient LLM Alignment

- arXiv: [2611.20635](https://arxiv.org/abs/2611.20635) | [PDF](https://arxiv.org/pdf/2611.20635) | [papers.cool](https://papers.cool/arxiv/2611.20635)
- Authors: Weiyun Huang, Alessio Galatolo
- Published: 2026-11-16 06:55 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, dpo; memory_and_benchmarks: memory, evaluation
- Abstract skim: Direct Preference Optimisation (DPO) simplifies reinforcement learning from human feedback, but still relies on traditional backpropagation and its associated activation-memory cost. Zeroth-order (ZO) optimisation avoids backpropagation, yet isotropic perturbations can produce noisy updates for preference objectives...

### 38 - Wireless Edge-Assisted Adaptive Latent Reasoning for Vision-Language-Action Models in Physical AI

- arXiv: [2611.19131](https://arxiv.org/abs/2611.19131) | [PDF](https://arxiv.org/pdf/2611.19131) | [papers.cool](https://papers.cool/arxiv/2611.19131)
- Authors: Fatih Temiz, Melike Erol-Kantarci
- Published: 2026-11-14 03:40 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: decision making; memory_and_benchmarks: benchmark; downranked: wireless
- Abstract skim: Vision-language-action (VLA) models enable embodied artificial intelligence (AI) by translating visual observations and language instructions into robotic actions. Emerging use cases in physical AI are expected to drive the need for efficient inference and communication, as the computational demands of the VLA...

### 37 - Deep Learning for Physicists: From Linear Regression to Reasoning Models

- arXiv: [2611.21295](https://arxiv.org/abs/2611.21295) | [PDF](https://arxiv.org/pdf/2611.21295) | [papers.cool](https://papers.cool/arxiv/2611.21295)
- Authors: Masanori Hanada
- Published: 2026-11-16 15:56 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: These lecture notes are based on an introductory course on neural networks and deep learning that the author taught in the School of Mathematical Sciences at Queen Mary University of London in 2023/24 and 2024/25. The author, however, is a physicist, and it shows: wherever possible, ideas are explained with physical...

### 37 - Foundation Pareto Flow Policy for Multi-Objective Reinforcement Learning

- arXiv: [2611.19825](https://arxiv.org/abs/2611.19825) | [PDF](https://arxiv.org/pdf/2611.19825) | [papers.cool](https://papers.cool/arxiv/2611.19825)
- Authors: Zhanjiang Yang, Lijun Sun, Yueming Li, Meng Li, Yijun Yang
- Published: 2026-11-15 06:14 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: The overarching goal of reinforcement learning (RL) is to efficiently optimize the agent's policy for various environments, tasks, dynamics, and even user preferences, which often consist of multiple and potentially conflicting rewards/objectives. This necessitates the learning of Pareto-optimal policies that can...

### 37 - LogT: Logically Think with Images for Visual Search

- arXiv: [2611.19200](https://arxiv.org/abs/2611.19200) | [PDF](https://arxiv.org/pdf/2611.19200) | [papers.cool](https://papers.cool/arxiv/2611.19200)
- Authors: Yanjun Fu, Quanzeng You, Jiadong Guo, Yujie Lu, Sai Charitha Akula, Haiping Wu, et al. (9 authors)
- Published: 2026-11-14 06:47 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Thinking with images empowers vision-language models (VLMs) to use an external Zoom-in tool for fine-grained visual search. Recent works employ supervised fine-tuning (SFT) and reinforcement learning (RL) with tool-specific designs to enable such capabilities. However, achieving logical reasoning alongside accurate...

### 36 - SpeCal: Spectral Calibration for Unsupervised RLVR

- arXiv: [2611.20691](https://arxiv.org/abs/2611.20691) | [PDF](https://arxiv.org/pdf/2611.20691) | [papers.cool](https://papers.cool/arxiv/2611.20691)
- Authors: Kai Tang, Xing Zheng, Haobo Wang, Guangcheng Zhu, Shenzhi Yang, Zhengqing Zang, et al. (10 authors)
- Published: 2026-11-16 07:56 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning abilities of large language models, but its dependence on ground-truth answers or external verifiers limits its ability to exploit abundant unlabeled reasoning data. Unsupervised RLVR alleviates this bottleneck by deriving...

### 36 - Learning Design Taste through Verifiable Synthetic Environments and Agentic Reinforcement Learning

- arXiv: [2611.20612](https://arxiv.org/abs/2611.20612) | [PDF](https://arxiv.org/pdf/2611.20612) | [papers.cool](https://papers.cool/arxiv/2611.20612)
- Authors: Sujay choubey, Siddhant Saxena, Sarthak Kapil, Suhas Motwani
- Published: 2026-11-16 06:37 UTC | Categories: cs.MA
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning
- Abstract skim: Code-generating language models produce user interfaces that build and run, but the pages are often weak in hierarchy, spacing, typography and composition. We study whether a small code model can learn design taste through reinforcement learning in verifiable synthetic environments. The method has three components....

### 35 - Towards Probabilistically Safe Reinforcement Learning: Theory and Deployment on Humanoid and Aerial Robots

- arXiv: [2611.19616](https://arxiv.org/abs/2611.19616) | [PDF](https://arxiv.org/pdf/2611.19616) | [papers.cool](https://papers.cool/arxiv/2611.19616)
- Authors: Pol Mestres, Varun Gabbita, Jason H. K. Siu, Sergio A. Esteban, Hampus Serneke, Joel W. Burdick, et al. (7 authors)
- Published: 2026-11-14 20:57 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; planning_and_action: trajectory
- Abstract skim: Reinforcement learning (RL) enables robots to acquire complex skills, but standard RL formulations do not guarantee that learned policies satisfy safety constraints, which limits their use in safety-critical settings. Existing safe RL methods with provable guarantees typically support only restricted classes of...

### 33 - Learning to Reason with Predictive Gains for Generative Recommendation

- arXiv: [2611.21441](https://arxiv.org/abs/2611.21441) | [PDF](https://arxiv.org/pdf/2611.21441) | [papers.cool](https://papers.cool/arxiv/2611.21441)
- Authors: Zhuoyang Li, Teng Shi, Jiakai Tang, Weijie Yu, Guofu Xie, Xiao Zhang, et al. (13 authors)
- Published: 2026-11-16 17:28 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: Reasoning-enhanced generative recommendation (GR) has attracted increasing attention for leveraging the reasoning capabilities of large language models (LLMs) to improve next-item prediction. However, existing methods primarily optimize reasoning through Group Relative Policy Optimization (GRPO) with rule-based...

### 32 - Infrastructure-Based Multi-Agent Reinforcement Learning with Attention for Highway Ramp Merging

- arXiv: [2611.20078](https://arxiv.org/abs/2611.20078) | [PDF](https://arxiv.org/pdf/2611.20078) | [papers.cool](https://papers.cool/arxiv/2611.20078)
- Authors: Chenhao Tong, Steffen Müller
- Published: 2026-11-15 15:44 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: traffic
- Abstract skim: On-ramp merging is a typical safety and throughput problem on highways. Without proper coordination, human drivers and self-interested autonomous vehicles may make risky manoeuvres and cause accidents or congestion. With recent advances in connected autonomous vehicles (CAVs) and multi-agent reinforcement learning...

### 31 - Distilling Safety Filters for Filter-free Multi-agent RL

- arXiv: [2611.19190](https://arxiv.org/abs/2611.19190) | [PDF](https://arxiv.org/pdf/2611.19190) | [papers.cool](https://papers.cool/arxiv/2611.19190)
- Authors: Srikar Babu Gadipudi, Somayeh Sojoudi, Claire J. Tomlin
- Published: 2026-11-14 06:11 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: acting
- Abstract skim: Reinforcement learning (RL) can teach robot teams to navigate shared spaces, but trial and error causes collisions that real robots cannot afford. Control barrier function (CBF) safety filters prevent these collisions by correcting unsafe actions, yet in a team the filter becomes a centralized optimization whose...

### 28 - Benchleaking Is Accelerating: Benchmark contamination has worsened sharply in the past month -- from post-training down to pre-training base models

- arXiv: [2611.21315](https://arxiv.org/abs/2611.21315) | [PDF](https://arxiv.org/pdf/2611.21315) | [papers.cool](https://papers.cool/arxiv/2611.21315)
- Authors: Yiwei Qin, Muhang Xie, Xuefeng Li, Mohan Jiang, Dayuan Fu, Tiantian Mi, et al. (8 authors)
- Published: 2026-11-16 16:10 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: benchmark
- Abstract skim: Benchmark contamination is not new, but recent model releases show it in a sharper form. We use the term benchleaking for the case in which a benchmark's own test examples enter training data, so that a score reflects recall rather than capability. This differs from benchmaxxing, which optimizes toward a benchmark...

### 27 - GNN-Based Deep Reinforcement Learning for Coastal Emergency Response under Extreme Water Levels

- arXiv: [2611.20268](https://arxiv.org/abs/2611.20268) | [PDF](https://arxiv.org/pdf/2611.20268) | [papers.cool](https://papers.cool/arxiv/2611.20268)
- Authors: Marcello Sano, Samuele Casagrande, Davide Ferrario, Sebastiano Vascon, Silvia Torresan, Andrea Critto
- Published: 2026-11-15 21:52 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, ppo; planning_and_action: planning
- Abstract skim: When a storm surge approaches a coastal town, the emergency plan must be put into action quickly using water-level forecasts, flood extent, road access, vulnerable residents and shelters. Bringing this information together under time pressure is slow and depends on the duty officer's expertise. This paper is one...

### 26 - HEAMS: Holistic Evaluation of Agent Memory Systems

- arXiv: [2611.20144](https://arxiv.org/abs/2611.20144) | [PDF](https://arxiv.org/pdf/2611.20144) | [papers.cool](https://papers.cool/arxiv/2611.20144)
- Authors: Chirag Goel, Jacob Lavoie, Amirhossein Naghshzan, Jordan Bannister, Marzia Nouri, Mehar Bhatia, et al. (10 authors)
- Published: 2026-11-15 17:26 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: Memory systems allow AI agents to persist information across interactions, making them more personalized and more capable on long-horizon tasks. This persistence introduces new risks: stored information can be disclosed in inappropriate contexts, resist correction or deletion, be retained beyond what users desire,...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
