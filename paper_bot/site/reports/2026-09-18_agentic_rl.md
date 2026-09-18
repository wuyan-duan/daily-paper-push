# RL / Post-Training / Agentic RL Reading Queue - 2026-09-18

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 449. Minimum score: 8.

## Top Picks

### 69 - UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning

- arXiv: [2609.20089](https://arxiv.org/abs/2609.20089) | [PDF](https://arxiv.org/pdf/2609.20089) | [papers.cool](https://papers.cool/arxiv/2609.20089)
- Authors: Wenjie Liao, Liangjie Zhao, Zehong Cao
- Published: 2026-09-17 11:49 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: planning, trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Self-evolving methods reduce the need for human-annotated trajectories by allowing tool-using agents to generate their own training data. Yet existing methods typically separate trajectory generation from evaluation, relying on static verifiers that cannot adapt to emerging failure modes or self-consistency signals...

### 53 - Compositional Reasoning in Language Models under Reinforcement Learning Post-Training

- arXiv: [2609.19465](https://arxiv.org/abs/2609.19465) | [PDF](https://arxiv.org/pdf/2609.19465) | [papers.cool](https://papers.cool/arxiv/2609.19465)
- Authors: Yu He, Yingxi Li, Yifei Wang, Ellen Vitercik
- Published: 2026-09-16 22:11 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Compositional reasoning is critical for real-world problem solving: since training data is necessarily limited, models must generalize by composing learned skills in new ways. While post-training methods such as reinforcement learning (RL) have substantially improved the reasoning abilities of language models (LMs),...

### 46 - EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning

- arXiv: [2609.20004](https://arxiv.org/abs/2609.20004) | [PDF](https://arxiv.org/pdf/2609.20004) | [papers.cool](https://papers.cool/arxiv/2609.20004)
- Authors: Nikita Khomich, Leopold Hermansson, Ido Hakimi
- Published: 2026-09-17 10:08 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; planning_and_action: trajectory, rollout
- Abstract skim: Reward-based reinforcement learning for language models, exemplified by Group Relative Policy Optimization (GRPO), collapses an entire stochastic trajectory into a single scalar reward. This is clean and scalable, but it explores and allocates reward inefficiently: a trajectory may contain many causal decisions,...

### 46 - Towards High-DoF Dexterous Manipulation through VLA Post-Training

- arXiv: [2609.19666](https://arxiv.org/abs/2609.19666) | [PDF](https://arxiv.org/pdf/2609.19666) | [papers.cool](https://papers.cool/arxiv/2609.19666)
- Authors: Junlei Zhu, Shenzhe Yao, Chaogui Huang, Wenkai Zhu, Jingwei Peng, Guanqi He, et al. (9 authors)
- Published: 2026-09-17 04:12 UTC | Categories: cs.RO
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Imitation-learned vision--language--action (VLA) foundation models acquire broad manipulation capabilities by scaling robot data across tasks and embodiments, but reliable deployment on a specific downstream task and hardware platform still requires post-training. Dexterous hands make this adaptation particularly...

### 45 - RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning

- arXiv: [2609.20784](https://arxiv.org/abs/2609.20784) | [PDF](https://arxiv.org/pdf/2609.20784) | [papers.cool](https://papers.cool/arxiv/2609.20784)
- Authors: Yan Yu, Zhengxi Lu, Yizhou Liu, Yichen Pan, Aozhe Wang, Qipeng Chen, et al. (11 authors)
- Published: 2026-09-17 17:52 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Multi-turn agents trained with reinforcement learning (RL) receive a single scalar reward per trajectory, which motivates self on-policy distillation (OPD) to supply dense token-level supervision from a self-teacher with privileged task skills, letting a skill-free student internalize them. This recipe, however, is...

### 44 - MATCH: Model-Aware Tool Learning with Curriculum Scheduling and Hierarchically Gated Rewards

- arXiv: [2609.20082](https://arxiv.org/abs/2609.20082) | [PDF](https://arxiv.org/pdf/2609.20082) | [papers.cool](https://papers.cool/arxiv/2609.20082)
- Authors: Shihao Liu, Hao Yin, Lijun Liu, Zhengzong Chen, Yuanyuan Zhao, Fei Huang
- Published: 2026-09-17 11:40 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: tool learning; rl_post_training: reinforcement learning, policy optimization, grpo
- Abstract skim: Tool learning enables large language models (LLMs) to use external tools for tasks beyond parametric knowledge. Reinforcement learning can optimize tool-call behavior from feedback, but current methods still face two problems: fixed-threshold curricula can become misaligned with the policy's evolving capability...

### 43 - Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization

- arXiv: [2609.19830](https://arxiv.org/abs/2609.19830) | [PDF](https://arxiv.org/pdf/2609.19830) | [papers.cool](https://papers.cool/arxiv/2609.19830)
- Authors: Yingxuan Zhuang, Binhe Yu, Jingxiao Yang, Ruopei Sun, Ziting Li, Cheng Tan, et al. (9 authors)
- Published: 2026-09-17 07:35 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; planning_and_action: trajectory, environment feedback; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning for LLM agents involves two distinct optimization di- mensions: how environment feedback is exploited within a trajectory, and how complete trajectories are aggregated across a batch. We formulate these dimen- sions as Intra-Trajectory Feedback Attribution and Inter-Trajectory Objec- tive...

### 39 - Reach or Solve? Attributing Agentic RL Gains with Checkpoint Handoffs

- arXiv: [2609.19636](https://arxiv.org/abs/2609.19636) | [PDF](https://arxiv.org/pdf/2609.19636) | [papers.cool](https://papers.cool/arxiv/2609.19636)
- Authors: Xuan Liu, Jingbin Qian
- Published: 2026-09-17 03:27 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl; rl_post_training: reinforcement learning; planning_and_action: decision making; memory_and_benchmarks: evaluation, alfworld
- Abstract skim: Reinforcement learning now trains language-model agents that act over dozens of steps in live environments. The gains are large, and they are read as better decision-making. An agent in a closed loop writes its own inputs. Each observation follows from its own earlier actions, so the states it meets late in an...

### 38 - EmbodiedMind: Adaptive Data Curation and Prefix-Tree Reinforcement Learning for Efficient Embodied Intelligence

- arXiv: [2609.19659](https://arxiv.org/abs/2609.19659) | [PDF](https://arxiv.org/pdf/2609.19659) | [papers.cool](https://papers.cool/arxiv/2609.19659)
- Authors: Feifan Wang, Zongbing Zhang, Yu Zhang, Lingfeng Wang, Yurui Zhu, Jin Deng, et al. (11 authors)
- Published: 2026-09-17 03:59 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; planning_and_action: planning, trajectory
- Abstract skim: Training embodied foundation models typically requires massive-scale datasets and extensive computational resources, yet often suffers from three critical limitations: (1) inefficient sample utilization due to low-informative samples; (2) imbalanced gradient contributions across heterogeneous tasks; and (3) severe...

### 37 - GR2PO: Group Relative Return Policy Optimization for Continuous Robot Control

- arXiv: [2609.19850](https://arxiv.org/abs/2609.19850) | [PDF](https://arxiv.org/pdf/2609.19850) | [papers.cool](https://papers.cool/arxiv/2609.19850)
- Authors: Pengqin Wang, Qiming Zhang, Shaojie Shen, Jun Ma
- Published: 2026-09-17 08:03 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Actor-critic architecture has been widely used in continuous robot control. However, they rely on learning a value network, introducing additional computational overhead during training. Moreover, policy learning may also be affected by the approximation error of value estimation. Critic-free group relative policy...

### 33 - AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models

- arXiv: [2609.19991](https://arxiv.org/abs/2609.19991) | [PDF](https://arxiv.org/pdf/2609.19991) | [papers.cool](https://papers.cool/arxiv/2609.19991)
- Authors: Longyin Zhang, Parth Sakhare Mahendra, Chengwei Wei, Ning Zhang, Lim Ming Chong, Sirui He, et al. (7 authors)
- Published: 2026-09-17 09:58 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Omni models can describe video content, but can they locate events in time, preserve event order, and judge audio-visual synchronization? We introduce AVTrace (Audio-Visual Temporal Reasoning Assessment and Capability Evaluation), a silver-standard diagnostic suite spanning onset and span grounding, synchronization,...

### 33 - CovR: Coverage-Aware Hardware Verification via Reasoning-Guided Reinforcement Learning

- arXiv: [2609.19189](https://arxiv.org/abs/2609.19189) | [PDF](https://arxiv.org/pdf/2609.19189) | [papers.cool](https://papers.cool/arxiv/2609.19189)
- Authors: Manar Abdelatty, Maryam Nouh, Sherief Reda
- Published: 2026-09-15 17:26 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, reflection
- Abstract skim: Design verification remains one of the most resource-intensive stages of hardware development, often consuming up to 70% of the total design effort. While recent work has explored using Large Language Models (LLMs) to automate testbench generation, most existing approaches focus narrowly on functional correctness,...

### 32 - RTK-Vision PPO for Autonomous Micro UAV Recovery on an Airborne Carrier

- arXiv: [2609.20629](https://arxiv.org/abs/2609.20629) | [PDF](https://arxiv.org/pdf/2609.20629) | [papers.cool](https://papers.cool/arxiv/2609.20629)
- Authors: Aashish Sahu, R Prasanth Kumar
- Published: 2026-09-17 16:16 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Autonomous recovery of a micro unmanned aerial vehicle (UAV) onto a moving airborne carrier enables reusable deploy-mission-recover operation, but couples long-range rendezvous, close-range perception, carrier motion, aerodynamic interaction, and a discontinuous contact event. This paper presents an RTK-vision-...

### 32 - SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

- arXiv: [2609.20519](https://arxiv.org/abs/2609.20519) | [PDF](https://arxiv.org/pdf/2609.20519) | [papers.cool](https://papers.cool/arxiv/2609.20519)
- Authors: Haozhe Liu, Tian Ye, Sensen Gao, Qihang Cao, Yitong Li, Mingchen Zhuge, et al. (14 authors)
- Published: 2026-09-17 14:58 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use, agent harness; reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: evaluation; downranked: traffic
- Abstract skim: As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired...

### 29 - When2Think: Learning Difficulty-Aware Length Control for Efficient Hybrid Reasoning Models

- arXiv: [2609.19671](https://arxiv.org/abs/2609.19671) | [PDF](https://arxiv.org/pdf/2609.19671) | [papers.cool](https://papers.cool/arxiv/2609.19671)
- Authors: Jaejun Shim, HyunJin Kim, Young Jin Kim, JinYeong Bak
- Published: 2026-09-17 04:15 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Large Reasoning Models (LRMs) achieve strong performance on complex tasks but exhibit systematic inefficiency: they often overthink easy problems and underthink hard ones. Existing approaches based on uniform length penalties or rigid routing incur an efficiency tax, trading reduced computation on easy instances for...

### 28 - An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence

- arXiv: [2609.19519](https://arxiv.org/abs/2609.19519) | [PDF](https://arxiv.org/pdf/2609.19519) | [papers.cool](https://papers.cool/arxiv/2609.19519)
- Authors: Erik Nijkamp, Anurag Koul, Egor Pakhomov, Bo Pang
- Published: 2026-09-17 00:15 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: long-horizon agent; rl_post_training: reinforcement learning
- Abstract skim: Language-model agents are increasingly asked to carry out work spanning days or weeks, such as an operations remediation or a research programme. Such a task outlives any context window, any process and any interval at which a person can attend. In this paper, we argue that a long-horizon agent must run continually...

### 27 - HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface

- arXiv: [2609.20659](https://arxiv.org/abs/2609.20659) | [PDF](https://arxiv.org/pdf/2609.20659) | [papers.cool](https://papers.cool/arxiv/2609.20659)
- Authors: Zimu Han, Yiming Zeng, Jiyao Zhang, Zihao Zhao, Yuanfei Wang, Yixiang Jin, et al. (12 authors)
- Published: 2026-09-17 16:38 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training; planning_and_action: trajectory
- Abstract skim: Large-scale vision-language-action (VLA) models provide powerful priors for robot manipulation, yet adapting them to a specific deployment remains challenging. Supervised fine-tuning (SFT) on task-specific demonstrations provides a step toward deployment, but faces two persistent limitations: static data provide...

### 26 - Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement Learning

- arXiv: [2609.20389](https://arxiv.org/abs/2609.20389) | [PDF](https://arxiv.org/pdf/2609.20389) | [papers.cool](https://papers.cool/arxiv/2609.20389)
- Authors: Weiwei Wang, Yuqiang Li, Xianyi Wu, Bingyi Jing
- Published: 2026-09-17 13:41 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: trajectory, decision making; memory_and_benchmarks: evaluation
- Abstract skim: Offline policy evaluation (OPE) is crucial in high-stakes reinforcement learning applications, where new policies must be assessed reliably before deployment. In such settings, point estimates alone are insufficient; principled uncertainty quantification, such as confidence intervals and variance estimates, is...

### 26 - Multi-Dimensional Prosody Judgment For Live Streaming Speech Synthesis

- arXiv: [2609.20124](https://arxiv.org/abs/2609.20124) | [PDF](https://arxiv.org/pdf/2609.20124) | [papers.cool](https://papers.cool/arxiv/2609.20124)
- Authors: Zifan Guan, Longyu Lu, Junan Zhang, Zhizheng Wu, Meiguang Jin, Junfeng Ma
- Published: 2026-09-17 12:20 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, preference optimization, grpo; memory_and_benchmarks: evaluation
- Abstract skim: Evaluating live streaming speech synthesis (TTS) requires assessing fine-grained, highly expressive prosody such as emotion, intonation, and energy which traditional MOS predictors fail to capture. While proprietary Large Language Models (LLMs) like Gemini can evaluate these aspects, they are too costly for massive...

### 26 - Hybrid Residual Reinforcement Learning for Contact-Rich Robotic Book Insertion

- arXiv: [2609.19962](https://arxiv.org/abs/2609.19962) | [PDF](https://arxiv.org/pdf/2609.19962) | [papers.cool](https://papers.cool/arxiv/2609.19962)
- Authors: Tianyuan Liu, Rutherford Agbeshi Patamia, Benjamin Champion, Akansel Cosgun, Richard Dazeley
- Published: 2026-09-17 09:34 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Placing a grasped book into a tight shelf is a compact but difficult contact-rich control problem: millimetre-scale pose error can turn a geometrically valid approach into jamming, failed release, or incomplete seating. We study this final phase after grasp acquisition and global approach, and ask how control...

### 26 - FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA

- arXiv: [2609.19680](https://arxiv.org/abs/2609.19680) | [PDF](https://arxiv.org/pdf/2609.19680) | [papers.cool](https://papers.cool/arxiv/2609.19680)
- Authors: Yanzhang Ma, Zhenghan Tai, Hanwei Wu, Sizhe Guan, Jianliang Lei, Hailin He, et al. (28 authors)
- Published: 2026-09-17 04:25 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: self-improvement, self improvement; memory_and_benchmarks: benchmark
- Abstract skim: Financial QA systems are typically improved before deployment through better retrieval, prompting, or agent coordination, leaving their reliability behavior fixed thereafter. In practice, new SEC-filing questions repeatedly expose heterogeneous errors in period, entity, evidence use, and calculation. Existing self-...

### 24 - Think Thrice Before Reranking: Multi-perspective Evidence and Reasoning Integration for Text Reranking

- arXiv: [2609.20131](https://arxiv.org/abs/2609.20131) | [PDF](https://arxiv.org/pdf/2609.20131) | [papers.cool](https://papers.cool/arxiv/2609.20131)
- Authors: Lijun Liu, Zhengzong Chen, Wenyan Li, Yuanyuan Zhao, Fei Huang
- Published: 2026-09-17 12:24 UTC | Categories: cs.CL
- Why it matched: rl_post_training: policy optimization; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reasoning-based reranking with Large Language Models (LLMs) has shown promising improvements in text ranking. However, current methods predominantly rely on a single reasoning trajectory, resulting in rankings that are susceptible to reasoning errors and inherently constrained in modeling the multifaceted signals...

### 24 - Rethinking Multi-Agent Collaboration: When More Is Less

- arXiv: [2609.19759](https://arxiv.org/abs/2609.19759) | [PDF](https://arxiv.org/pdf/2609.19759) | [papers.cool](https://papers.cool/arxiv/2609.19759)
- Authors: Yishuo Yuan, Yibo Wu, Yihan Zhang, Minyuan Sun, Shenliang Li, Xinkai Ma, et al. (8 authors)
- Published: 2026-09-17 06:29 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent collaboration
- Abstract skim: The rapid advancement of large language models and single-agent harnesses has reshaped the landscape of autonomous systems, raising a critical question of when multi-agent collaboration offers genuine value. As individual agent capabilities continue to scale, multi-agent collaboration faces diminishing returns while...

### 22 - CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding

- arXiv: [2609.20586](https://arxiv.org/abs/2609.20586) | [PDF](https://arxiv.org/pdf/2609.20586) | [papers.cool](https://papers.cool/arxiv/2609.20586)
- Authors: Zhikun Zhou, Kunyu Peng, Runyi Yang, Junhao Cai, Di Wen, Ruiping Liu, et al. (10 authors)
- Published: 2026-09-17 15:39 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Referring scene understanding for embodied robots requires grounding object- and relation-centric language queries from a designated viewpoint. While a local semantic Gaussian map can support such grounding within one agent's observations, cooperative settings require this ability to remain effective after...

### 22 - DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum

- arXiv: [2609.19801](https://arxiv.org/abs/2609.19801) | [PDF](https://arxiv.org/pdf/2609.19801) | [papers.cool](https://papers.cool/arxiv/2609.19801)
- Authors: Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, et al. (8 authors)
- Published: 2026-09-17 07:13 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, trajectory, rollout; memory_and_benchmarks: evaluation
- Abstract skim: Executable environments enable LLM agents to learn from the consequences of their actions. For embodied agents, those consequences extend beyond whether the current task succeeds: completing a delivery can consume the time, energy, or money needed for later work. Learning to plan therefore requires environments that...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
