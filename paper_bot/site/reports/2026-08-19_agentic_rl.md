# RL / Post-Training / Agentic RL Reading Queue - 2026-08-19

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 309. Minimum score: 8.

## Top Picks

### 67 - SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning

- arXiv: [2608.17301](https://arxiv.org/abs/2608.17301) | [PDF](https://arxiv.org/pdf/2608.17301) | [papers.cool](https://papers.cool/arxiv/2608.17301)
- Authors: Guozheng Sun
- Published: 2026-08-18 02:52 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark; downranked: wireless
- Abstract skim: Post-training with supervised chain-of-thought fine-tuning and reinforcement learning from verifiable rewards has substantially improved the mathematical reasoning capabilities of large language models (LLMs). However, their application to signal processing problems remains relatively under-explored. This report...

### 65 - GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models

- arXiv: [2608.17411](https://arxiv.org/abs/2608.17411) | [PDF](https://arxiv.org/pdf/2608.17411) | [papers.cool](https://papers.cool/arxiv/2608.17411)
- Authors: Peizheng Guo, Jianqi Zhang, Xingyu Zhang, Yun Fan, Jiahuan Zhou, Changwen Zheng, et al. (7 authors)
- Published: 2026-08-18 06:22 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning
- Abstract skim: Group Relative Policy Optimization (GRPO) has become a widely used approach for post-training Large Language Models (LLMs) for reasoning. In GRPO, the group gradients induced by different queries within the same mini-batch are directly averaged to form the policy update. However, these group gradients can point in...

### 63 - Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups

- arXiv: [2608.17423](https://arxiv.org/abs/2608.17423) | [PDF](https://arxiv.org/pdf/2608.17423) | [papers.cool](https://papers.cool/arxiv/2608.17423)
- Authors: Zeyun Deng, Yuzhe Lu, Yawei Wang, Linbo Liu, Qing Ping, Han Ding, et al. (9 authors)
- Published: 2026-08-18 06:44 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo, ppo; reasoning: outcome reward; planning_and_action: trajectory, rollout
- Abstract skim: GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a critic. This simplification comes with a sampling cost: group-relative advantages require multiple rollouts from each scene. Under binary success rewards, groups whose...

### 55 - Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL

- arXiv: [2608.17253](https://arxiv.org/abs/2608.17253) | [PDF](https://arxiv.org/pdf/2608.17253) | [papers.cool](https://papers.cool/arxiv/2608.17253)
- Authors: Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, Yuanyuan Shi, et al. (9 authors)
- Published: 2026-08-18 01:16 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent, agent training; rl_post_training: reinforcement learning, verifiable reward; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest successes still depend heavily on ground-truth supervision (e.g., verifiable reward). Such annotations are costly to obtain and become increasingly scarce as reasoning...

### 52 - PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs

- arXiv: [2608.17289](https://arxiv.org/abs/2608.17289) | [PDF](https://arxiv.org/pdf/2608.17289) | [papers.cool](https://papers.cool/arxiv/2608.17289)
- Authors: Dayang Liang, Liyuan He, Xuan Feng, Shuxin Li, Bo An, Yunlong Liu
- Published: 2026-08-18 02:39 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: outcome reward; planning_and_action: planning, trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Group-relative policy optimization has emerged as a key paradigm for training agentic large language models (LLMs) on multi-turn interactive tasks. However, most existing variants fail to distinguish advantages among successful trajectories even when these trajectories differ substantially in their interaction...

### 49 - Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation

- arXiv: [2608.17512](https://arxiv.org/abs/2608.17512) | [PDF](https://arxiv.org/pdf/2608.17512) | [papers.cool](https://papers.cool/arxiv/2608.17512)
- Authors: Hongyan Feng, Sunlai Chen, Xuanyu Liu, Miao Pan, Yangfan Xie, Yuxiang Cui, et al. (12 authors)
- Published: 2026-08-18 08:37 UTC | Categories: cs.RO
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: planning, trajectory; memory_and_benchmarks: memory
- Abstract skim: Although Large Vision-Language Models (VLMs) have significantly advanced embodied navigation, their direct deployment remains challenging, as existing methods often force VLMs into unnatural action spaces that misalign with their 2D pre-training priors, compounded by rigid reasoning schedules and inefficient memory...

### 42 - Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements

- arXiv: [2608.17310](https://arxiv.org/abs/2608.17310) | [PDF](https://arxiv.org/pdf/2608.17310) | [papers.cool](https://papers.cool/arxiv/2608.17310)
- Authors: Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee
- Published: 2026-08-18 03:03 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: memory, webarena
- Abstract skim: Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to fine-tune larger...

### 41 - WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization

- arXiv: [2608.16955](https://arxiv.org/abs/2608.16955) | [PDF](https://arxiv.org/pdf/2608.16955) | [papers.cool](https://papers.cool/arxiv/2608.16955)
- Authors: Jiahao Huang, Rongpeng Li, Zhifeng Zhao, Guoru Ding, Honggang Zhang
- Published: 2026-08-16 11:47 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: policy optimization, ppo; planning_and_action: trajectory, world model; downranked: wireless
- Abstract skim: Post-disaster damage to terrestrial infrastructure can disrupt wireless coverage,while Uncrewed Aerial Vehicle (UAV) swarms provide a promising solution for rapid restoration.However, due to the limitations in local geometry observations hidden radio impact,and inter-UAV communication,there exists a significant gap...

### 38 - Offline Multi-Agent Reinforcement Learning with a Physics-Informed World Model for Cooperative Mixed Traffic Control

- arXiv: [2608.17739](https://arxiv.org/abs/2608.17739) | [PDF](https://arxiv.org/pdf/2608.17739) | [papers.cool](https://papers.cool/arxiv/2608.17739)
- Authors: Lu Liu, Chi Xie, Xi Xiong
- Published: 2026-08-18 13:03 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: world model; downranked: traffic
- Abstract skim: This study investigates cooperative control of connected and automated vehicles (CAVs) at partially observable highway bottlenecks in mixed traffic, aiming to mitigate congestion without relying on complete global traffic states or online trial-and-error. We propose a physics-informed world model-based offline...

### 36 - Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation

- arXiv: [2608.17941](https://arxiv.org/abs/2608.17941) | [PDF](https://arxiv.org/pdf/2608.17941) | [papers.cool](https://papers.cool/arxiv/2608.17941)
- Authors: Zhizhao Liu, Zhiliang Tian, Xi Wang, Zhihua Wen, Yihang Xiong, Zhiquan Lai, et al. (7 authors)
- Published: 2026-08-18 16:01 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models but relies on costly rollout exploration. Assigning the same exploration budget to samples with different difficulty levels is inefficient: easy samples may receive redundant rollouts, whereas difficult...

### 36 - Agent Lightning v1.0: Towards Harnessed Agentic RL

- arXiv: [2608.17528](https://arxiv.org/abs/2608.17528) | [PDF](https://arxiv.org/pdf/2608.17528) | [papers.cool](https://papers.cool/arxiv/2608.17528)
- Authors: Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, et al. (10 authors)
- Published: 2026-08-18 08:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl; rl_post_training: post-training, post training
- Abstract skim: Modern agents operate inside agent harnesses that manage tools, context, and control flow, making the harness a critical part of the agent system. Our original Agent Lightning introduced a disaggregated architecture that connects arbitrary agents to RL training through an LLM endpoint proxy, an approach later...

### 33 - Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context

- arXiv: [2608.17499](https://arxiv.org/abs/2608.17499) | [PDF](https://arxiv.org/pdf/2608.17499) | [papers.cool](https://papers.cool/arxiv/2608.17499)
- Authors: Yiwen Zhao, Zhihao Wen, Yuchen Mao, Mingxuan Jiang, Yihao Hu, Pan Wang, et al. (8 authors)
- Published: 2026-08-18 08:25 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, grpo; planning_and_action: rollout
- Abstract skim: User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typically reduces each rollout to a terminal reward, assigning the same credit to effective elicitation, errors, and later repair. The next user turn is more than context: it...

### 28 - Debate Training Reduces Reward Hacking in RLAIF

- arXiv: [2608.17776](https://arxiv.org/abs/2608.17776) | [PDF](https://arxiv.org/pdf/2608.17776) | [papers.cool](https://papers.cool/arxiv/2608.17776)
- Authors: Zachary Kenton, Lili Janzer, Rory Greig, Tian Huey Teh, Kirill Tyshchuk, Jonah Brown-Cohen, et al. (11 authors)
- Published: 2026-08-18 13:40 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent, agent training; rl_post_training: reinforcement learning
- Abstract skim: We demonstrate that RL finetuning an LLM using debate, a two-player adversarial game between a generator and a critic adjudicated by a weaker LLM judge, reduces reward hacking compared to a reinforcement learning from AI feedback (RLAIF) baseline. Reward hacking is a central obstacle in RLAIF: as training...

### 25 - Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning

- arXiv: [2608.17443](https://arxiv.org/abs/2608.17443) | [PDF](https://arxiv.org/pdf/2608.17443) | [papers.cool](https://papers.cool/arxiv/2608.17443)
- Authors: Xingrui Zhuo, Jiapu Wang, Manzong Huang, Gongqing Wu, Xindong Wu
- Published: 2026-08-18 07:21 UTC | Categories: cs.AI
- Why it matched: rl_post_training: grpo; reasoning: reasoning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Knowledge Graph Reasoning (KGR) aims to discover latent facts by leveraging the structural evidence available in KGs, posing a challenge to the structural semantic understanding capability of KGR models. Recent studies have demonstrated that Large Language Models (LLMs) can achieve remarkable progress on KGR tasks...

### 25 - Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics

- arXiv: [2608.17268](https://arxiv.org/abs/2608.17268) | [PDF](https://arxiv.org/pdf/2608.17268) | [papers.cool](https://papers.cool/arxiv/2608.17268)
- Authors: Zhikai Ding, Ziyi Ye
- Published: 2026-08-18 01:51 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Curriculum learning has been widely adopted in the post-training of large language models by organizing training data from easy to hard. However, its effectiveness varies substantially across reasoning tasks, suggesting that no single curriculum is universally optimal and raising a fundamental question: what...

### 23 - An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning

- arXiv: [2608.17804](https://arxiv.org/abs/2608.17804) | [PDF](https://arxiv.org/pdf/2608.17804) | [papers.cool](https://papers.cool/arxiv/2608.17804)
- Authors: Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez
- Published: 2026-08-18 14:04 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: grpo; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified: when a target-adjacent prompt admits a broader answer without target-specific leakage, the model should answer at...

### 23 - HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

- arXiv: [2608.17597](https://arxiv.org/abs/2608.17597) | [PDF](https://arxiv.org/pdf/2608.17597) | [papers.cool](https://papers.cool/arxiv/2608.17597)
- Authors: Yajing Bai, Jinhao Duan, Jie Peng, Xianfeng Wu, Sijia Liu, Song Wang, et al. (7 authors)
- Published: 2026-08-18 10:03 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent harness; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Large language models are increasingly deployed through agent harnesses that manage tools, extensions, persistent state, permissions, and external actions. Existing safety benchmarks mainly target individual attack mechanisms or a limited subset of operational settings, making it difficult to compare how safety...

### 22 - D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory

- arXiv: [2608.17756](https://arxiv.org/abs/2608.17756) | [PDF](https://arxiv.org/pdf/2608.17756) | [papers.cool](https://papers.cool/arxiv/2608.17756)
- Authors: Xule Liu, Yijun Liu, Chao Li, Shao Kun
- Published: 2026-08-18 13:18 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory, evaluation
- Abstract skim: Memory is a key capability of LLM agents. Persistent memory extends this across sessions---enabling recall, revision, and personalization. Yet its multi-stage pipeline (ingestion, retrieval, filtering, generation) makes failures difficult to localize: end-to-end evaluation reveals that an error occurred, but not...

### 22 - LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents

- arXiv: [2608.17393](https://arxiv.org/abs/2608.17393) | [PDF](https://arxiv.org/pdf/2608.17393) | [papers.cool](https://papers.cool/arxiv/2608.17393)
- Authors: Yiming Du, Yuxin Jiang, Tao Yuan, Jianbo Dai, Shaowei Wang, Jierun Chen, et al. (12 authors)
- Published: 2026-08-18 05:34 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: trajectory, rollout
- Abstract skim: Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental crashes and reward...

### 21 - EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection

- arXiv: [2608.17933](https://arxiv.org/abs/2608.17933) | [PDF](https://arxiv.org/pdf/2608.17933) | [papers.cool](https://papers.cool/arxiv/2608.17933)
- Authors: Lei Jiang, Ye Wei, Xinyu Xi, Jordan Langham-Lopez, Yifan Bao, Raad Khraishi, et al. (10 authors)
- Published: 2026-08-18 15:55 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Financial time series exhibit non-stationary and heterogeneous statistical properties, making change-point detection challenging because no single unsupervised algorithm performs consistently across assets and market regimes. Conventional workflows consequently depend heavily on expert-driven model selection,...

### 21 - Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning

- arXiv: [2608.17347](https://arxiv.org/abs/2608.17347) | [PDF](https://arxiv.org/pdf/2608.17347) | [papers.cool](https://papers.cool/arxiv/2608.17347)
- Authors: Hoda Yamani, Yuning Xing, Koen van Rijnsoever, Bruce A. MacDonald, Henry Williams
- Published: 2026-08-18 04:11 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: action sequence; memory_and_benchmarks: memory
- Abstract skim: Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improves future performance. Motivated by this biological principle, we introduce Instant Episode Repetition (IER), a simple and novel mechanism that improves sample...

### 21 - Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents

- arXiv: [2608.17319](https://arxiv.org/abs/2608.17319) | [PDF](https://arxiv.org/pdf/2608.17319) | [papers.cool](https://papers.cool/arxiv/2608.17319)
- Authors: AIMAE Team, Tianxiang Chen, Yan Cheng, Zhangye Han, Xiaowei Li, Chang Liu, et al. (42 authors)
- Published: 2026-08-18 03:23 UTC | Categories: cs.AI
- Why it matched: rl_post_training: grpo; reasoning: reflection; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Browser agents perform well on short, clean demonstrations, but real deployment is fundamentally different: agents must sustain dozens of decisions on live websites while recovering from mistakes and navigating complex UIs. We argue that closing this gap requires alignment at every level of the pipeline, including...

### 20 - Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation

- arXiv: [2608.18072](https://arxiv.org/abs/2608.18072) | [PDF](https://arxiv.org/pdf/2608.18072) | [papers.cool](https://papers.cool/arxiv/2608.18072)
- Authors: Iryna Hartsock, Cesar Lam, Christopher Otteni, Aliya Qayyum, Robert Gatenby, Cyrillo Araujo, et al. (7 authors)
- Published: 2026-08-18 17:57 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: evaluation
- Abstract skim: Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology reports from CT examinations of the chest, abdomen, and pelvis dictated by 15 board-certified radiologists in 2023...

### 20 - Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation for Agent Evaluation and Credit Assignment

- arXiv: [2608.17713](https://arxiv.org/abs/2608.17713) | [PDF](https://arxiv.org/pdf/2608.17713) | [papers.cool](https://papers.cool/arxiv/2608.17713)
- Authors: Zhen Zhang, Ahmad Hafez, Amr Alanwar
- Published: 2026-08-18 12:39 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; planning_and_action: trajectory, rollout; memory_and_benchmarks: evaluation
- Abstract skim: Agent evaluations and trace-based learning often compare outputs across transformed views through a post-response correspondence treated as neutral preprocessing. We show that this correspondence is a measurement intervention: omitting it can manufacture sensitivity, an over-aggressive map can manufacture...

### 20 - GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities

- arXiv: [2608.17665](https://arxiv.org/abs/2608.17665) | [PDF](https://arxiv.org/pdf/2608.17665) | [papers.cool](https://papers.cool/arxiv/2608.17665)
- Authors: Haoran Bu, Zejian Chen, Litian Zhang, Xi Zhang
- Published: 2026-08-18 11:38 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, agent memory; memory_and_benchmarks: memory
- Abstract skim: LLM-driven agents can autonomously exchange opinions on online platforms and form communities. Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization. Existing methods manipulate agent prompts or construct echo chambers, both of which are...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
