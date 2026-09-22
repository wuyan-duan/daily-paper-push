# RL / Post-Training / Agentic RL Reading Queue - 2026-09-22

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 795. Minimum score: 8.

## Top Picks

### 60 - MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents

- arXiv: [2609.24259](https://arxiv.org/abs/2609.24259) | [PDF](https://arxiv.org/pdf/2609.24259) | [papers.cool](https://papers.cool/arxiv/2609.24259)
- Authors: Ruike Cao, Fanyu Zhao, Fugen Yao, Liang Dong, Jian Xu, Guanjun Jiang, et al. (9 authors)
- Published: 2026-09-21 08:22 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agent memory; rl_post_training: post-training, post training, policy optimization, group relative policy optimization; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system...

### 52 - RLVR$^{2}$: Reinforcement Learning with Verifiable Rubric-based Ranking

- arXiv: [2609.23457](https://arxiv.org/abs/2609.23457) | [PDF](https://arxiv.org/pdf/2609.23457) | [papers.cool](https://papers.cool/arxiv/2609.23457)
- Authors: Hao Li, Zhengkun Zhang, Gangqiang Hu, Zhen Zhang, Yude Gao, Dai Dai, et al. (7 authors)
- Published: 2026-09-20 08:34 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) is expanding from tasks with well-defined correctness signals, such as mathematics and code, toward multifaceted quality requirements specified by multi-dimensional rubrics. Since policy optimization consumes one scalar per rollout, rubric-based pipelines must...

### 51 - Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation Enforcement

- arXiv: [2609.24243](https://arxiv.org/abs/2609.24243) | [PDF](https://arxiv.org/pdf/2609.24243) | [papers.cool](https://papers.cool/arxiv/2609.24243)
- Authors: Xutao Mao, Jianing Zhu, Jinman Zhao, Tongliang Liu, Xiaowen Chu, Cong Wang, et al. (7 authors)
- Published: 2026-09-21 08:08 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) improves reasoning in vision-language models (VLMs) but can induce chain-of-thought (CoT) obfuscation: an operational, non-intentional outcome where task reward or accuracy rises while traces become less grounded and monitorable. Prior work largely documents this decay behaviorally,...

### 46 - FLARE: A Full-Lifecycle Dense Supervision Paradigm for Long-Horizon Coding Agents via Generative Reward Model

- arXiv: [2609.23808](https://arxiv.org/abs/2609.23808) | [PDF](https://arxiv.org/pdf/2609.23808) | [papers.cool](https://papers.cool/arxiv/2609.23808)
- Authors: Jingxuan Xu, Gang Wu, Yanan Wu, Yutao Mou, Songwei Yu, Tianzhuang He, et al. (16 authors)
- Published: 2026-09-20 18:54 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model; planning_and_action: trajectory, rollout
- Abstract skim: While test-time scaling enhances Large Language Model (LLM) agents in long-horizon software engineering (SWE), sparse binary rewards (Pass/Fail) create a severe credit assignment crisis and waste failed exploratory trajectories. Current trajectory optimization and scaling methods are costly and structurally limited,...

### 45 - General Collaborative Intelligence: Architecting Cognition for Resilient Multi-Agent Ecosystems

- arXiv: [2609.22967](https://arxiv.org/abs/2609.22967) | [PDF](https://arxiv.org/pdf/2609.22967) | [papers.cool](https://papers.cool/arxiv/2609.22967)
- Authors: Lei Zhang, Chun Ye, Le Yang, Zhaozhong Wang, Deng-Ping Fan, Hang Dai, et al. (7 authors)
- Published: 2026-09-19 11:38 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reflection; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Multi-agent unmanned systems are moving from isolated, ego-centric sensing toward collaborative intelligence, in which distributed agents exchange compact features to overcome a local observation trap that no single agent can escape: occlusions, finite sensor range, and environmental degradation. The field has...

### 44 - RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling

- arXiv: [2609.22947](https://arxiv.org/abs/2609.22947) | [PDF](https://arxiv.org/pdf/2609.22947) | [papers.cool](https://papers.cool/arxiv/2609.22947)
- Authors: Zhenchen Tang, Yang Li, Songlin Yang, Bo Peng, Xiaotong Zhao, Shuai Li, et al. (9 authors)
- Published: 2026-09-19 11:01 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Reinforcement learning (RL) is vital for optimizing video generation models, with a robust reward model (RM) serving as the cornerstone. However, existing video reward models often produce unstable scalar scores because they directly map complex, subjective video quality into a single score without explicit...

### 42 - VISTA: An Attention-Based Multi-Agent Reinforcement Learning Architecture for Space Situational Awareness Sensor Tasking

- arXiv: [2609.23875](https://arxiv.org/abs/2609.23875) | [PDF](https://arxiv.org/pdf/2609.23875) | [papers.cool](https://papers.cool/arxiv/2609.23875)
- Authors: Miguel Leiva-Vélez, Adalberto Claudio Quiros, Nicolas Gaston Rozado, Hodei Urrutxua, Víctor Rodríguez-Fernández
- Published: 2026-09-20 21:20 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: memory
- Abstract skim: The rapid growth of resident space objects is increasing the complexity of space situational awareness sensor tasking, challenging classical optimization methods as they allocate finite, heterogeneous, and distributed sensing resources across ever-larger catalogues. Existing deep reinforcement learning approaches...

### 41 - Information-Time Proximal Policy Optimization

- arXiv: [2609.24380](https://arxiv.org/abs/2609.24380) | [PDF](https://arxiv.org/pdf/2609.24380) | [papers.cool](https://papers.cool/arxiv/2609.24380)
- Authors: Yongcheng Zeng, Xinyu Cui, Yan Song, Guoqing Liu, Hongsheng Xin, Kaike Zhang, et al. (12 authors)
- Published: 2026-09-21 10:17 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: rlvr, policy optimization, ppo; reasoning: reasoning
- Abstract skim: RLVR has substantially improved the reasoning capabilities of LLMs. However, existing methods typically parameterize temporal progression in the Markov Decision Process by token-by-token generation, despite the highly non-uniform information flow along autoregressive trajectories. In this paper, we propose InfoPPO,...

### 41 - Listen Then Reason: Perception-Grounded Test-Time Reinforcement Learning for Large Audio-Language Models

- arXiv: [2609.23589](https://arxiv.org/abs/2609.23589) | [PDF](https://arxiv.org/pdf/2609.23589) | [papers.cool](https://papers.cool/arxiv/2609.23589)
- Authors: Jiaheng Dong, Xiaofeng Yu, Jean Honorio, Abhirup Ghosh, Hong Jia, Ting Dang
- Published: 2026-09-20 12:12 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Large audio-language models (LALMs) are increasingly used for a broader range of audio reasoning tasks. These models typically incorporate audio representations into a large language model (LLM) backbone to enable multimodal reasoning. Recent test-time reinforcement learning (TTRL) methods further improve LLM...

### 38 - RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

- arXiv: [2609.24972](https://arxiv.org/abs/2609.24972) | [PDF](https://arxiv.org/pdf/2609.24972) | [papers.cool](https://papers.cool/arxiv/2609.24972)
- Authors: Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhang, Yoonho Lee, et al. (14 authors)
- Published: 2026-09-21 17:54 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: llm agent, agent harness; reasoning: self-improvement, self improvement; memory_and_benchmarks: memory, benchmark
- Abstract skim: An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness,...

### 37 - Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning

- arXiv: [2609.24033](https://arxiv.org/abs/2609.24033) | [PDF](https://arxiv.org/pdf/2609.24033) | [papers.cool](https://papers.cool/arxiv/2609.24033)
- Authors: Kejia Hu, Wentong Zhai, Bo Zhao, Shuai Liang
- Published: 2026-09-21 02:59 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: world model; memory_and_benchmarks: evaluation
- Abstract skim: Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences. Existing noise-space reinforcement learning efficiently steers a frozen Vision-Language-Action (VLA) policy, but its critics largely ignore these consequences. We present...

### 35 - Measured Joules, Learned Routes: Learning to Route for Energy-Efficient LLM Serving

- arXiv: [2609.23085](https://arxiv.org/abs/2609.23085) | [PDF](https://arxiv.org/pdf/2609.23085) | [papers.cool](https://papers.cool/arxiv/2609.23085)
- Authors: Muhammad Abdur Rab Siddiqui, Daniela Rojas, Chen Yang, Wenqi Cui, Yuanyuan Shi, Yize Chen
- Published: 2026-09-19 15:44 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Large language models (LLMs) and agentic AI systems are creating rapidly growing inference energy demands as model sizes grow and reasoning trajectories extend. While in practice, many queries do not require the capabilities of the largest available model, and routinely directing such queries to a high-capability...

### 34 - DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security

- arXiv: [2609.24662](https://arxiv.org/abs/2609.24662) | [PDF](https://arxiv.org/pdf/2609.24662) | [papers.cool](https://papers.cool/arxiv/2609.24662)
- Authors: Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh, Yaroslav Rogoza
- Published: 2026-09-21 14:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, multi-agent; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation...

### 33 - ACLArena: Agent Continue Learning in Multi-stage Post-training

- arXiv: [2609.23989](https://arxiv.org/abs/2609.23989) | [PDF](https://arxiv.org/pdf/2609.23989) | [papers.cool](https://papers.cool/arxiv/2609.23989)
- Authors: Haixin Wang, Xiaoxuan Wang, Junkai Zhang, Han Zhang, Renliang Sun, Alexander K Taylor, et al. (12 authors)
- Published: 2026-09-21 01:48 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Building general-purpose agents for industrial deployment requires integrating multiple capabilities, each typically acquired at a distinct stage of training. Yet there is currently no well-established recipe for Agent Continual Learning (ACL), with little understanding of the trade-offs among existing integration...

### 33 - Towards Full Pipeline FP8 Reinforcement Learning for LLMs

- arXiv: [2609.22870](https://arxiv.org/abs/2609.22870) | [PDF](https://arxiv.org/pdf/2609.22870) | [papers.cool](https://papers.cool/arxiv/2609.22870)
- Authors: Fanchao Chen, Ziheng Jiang, Ziyun Wei, Zheng Zhong, Du Li, Chi Zhang, et al. (8 authors)
- Published: 2026-09-19 08:20 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL) has become a key technique for improving the reasoning and agentic abilities of large language models (LLMs). Although FP8 quantization can accelerate RL training, maintaining stability throughout an FP8 RL pipeline remains challenging. While previous works have focused on resolving...

### 32 - Cost-Aware Reinforcement Learning with Action Masking and Projection for Battery Energy Storage Dispatch under Suppressed-Spread Market Shifts

- arXiv: [2609.23590](https://arxiv.org/abs/2609.23590) | [PDF](https://arxiv.org/pdf/2609.23590) | [papers.cool](https://papers.cool/arxiv/2609.23590)
- Authors: Kuanlin Chen, Chen-Wei Kuo, Cheng-En Ou
- Published: 2026-09-20 12:12 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Battery energy storage system (BESS) dispatch must preserve operational feasibility while declining price spreads reduce the margin available to pay for cycling. We study a proximal policy optimization (PPO) controller whose pre-selection physical action mask and emergency projection are separated from a causal,...

### 30 - Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems

- arXiv: [2609.24474](https://arxiv.org/abs/2609.24474) | [PDF](https://arxiv.org/pdf/2609.24474) | [papers.cool](https://papers.cool/arxiv/2609.24474)
- Authors: Angelo Caregnato-Neto, Paul-Louis Delacour, Raf Van de Plas, Tamás Keviczky, Janito Vaqueiro Ferreira
- Published: 2026-09-21 12:15 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; planning_and_action: planning, trajectory, decision making; memory_and_benchmarks: evaluation
- Abstract skim: This work investigates the use of flow-based connectivity maintenance constraints in mixed-integer linear programming (MILP) trajectory planning and decision-making models for networked multi-agent systems (MAS). We integrate flow-based encodings for standard and k-hop connectivity into MILP multi-vehicle...

### 30 - Verti-WM: A Physics-Aided Exteroceptive World Model for Off-Road Reinforcement Learning

- arXiv: [2609.23118](https://arxiv.org/abs/2609.23118) | [PDF](https://arxiv.org/pdf/2609.23118) | [papers.cool](https://papers.cool/arxiv/2609.23118)
- Authors: Chenhui Pan, Tong Xu, Xuesu Xiao
- Published: 2026-09-19 16:43 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: world model
- Abstract skim: Reinforcement learning for off-road navigation requires extensive vehicle-terrain interaction data, which are costly to collect in high-fidelity simulation. World models offer a promising alternative by replacing simulator roll-outs during policy optimization. However, an off-road world model must condition state...

### 30 - Prioritized Rollouts for Efficient World Model-based Vision-Language-Action Policy Optimization

- arXiv: [2609.22879](https://arxiv.org/abs/2609.22879) | [PDF](https://arxiv.org/pdf/2609.22879) | [papers.cool](https://papers.cool/arxiv/2609.22879)
- Authors: Yifei Sheng, Haoxiang Ren, Zhilong Zhang, Haonan Wang, Runjie Xu, Yihao Sun, et al. (11 authors)
- Published: 2026-09-19 08:34 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: world model
- Abstract skim: Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied intelligence, but fine-tuning them with reinforcement learning (RL) remains constrained by the cost of real-world robot interaction. Model-based reinforcement learning (MBRL) reduces this cost by using a learned world model to...

### 28 - CREDO: Variance-Guided Rubric Evolution for Replay-Corrected Credit Assignment

- arXiv: [2609.24174](https://arxiv.org/abs/2609.24174) | [PDF](https://arxiv.org/pdf/2609.24174) | [papers.cool](https://papers.cool/arxiv/2609.24174)
- Authors: Xuchun Hu
- Published: 2026-09-21 06:43 UTC | Categories: cs.AI
- Why it matched: agentic_rl: language agent; rl_post_training: ppo; memory_and_benchmarks: evaluation
- Abstract skim: Long-horizon language agents receive sparse terminal feedback, while intermediate rubrics provide structured but potentially misspecified assessments of progress. In resettable training environments, counterfactual continuation rollouts can measure local credit, but exhaustive replay is costly. We propose Credo, a...

### 28 - Luck Is Not Skill: When Do Paired Rollouts Help Group-Relative RL of LLM Agents?

- arXiv: [2609.24144](https://arxiv.org/abs/2609.24144) | [PDF](https://arxiv.org/pdf/2609.24144) | [papers.cool](https://papers.cool/arxiv/2609.24144)
- Authors: Nazmus Sakib
- Published: 2026-09-21 05:55 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: Group-relative reinforcement learning compares rollouts of the same prompt, but independent environment noise can obscure these comparisons. We study paired rollouts, which share an event-keyed noise schedule within each group while preserving each rollout's marginal distribution. Pairing removes the between-...

### 28 - Synthesizing Reactive Character Behaviors for Continuous Games via Programmatic Policy Search

- arXiv: [2609.24025](https://arxiv.org/abs/2609.24025) | [PDF](https://arxiv.org/pdf/2609.24025) | [papers.cool](https://papers.cool/arxiv/2609.24025)
- Authors: Maxim Gumin, Hsueh-Ti Derek Liu, Victor Zordan, Daniel Ritchie
- Published: 2026-09-21 02:47 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark
- Abstract skim: We present a method for synthesizing reactive character behaviors for continuous games as compact, human-readable programs. Game AI practice still relies heavily on manually authored behavior trees, state machines, and scripts, while academic reinforcement learning typically produces opaque neural controllers that...

### 27 - Corrective Forcing: Unified Post-Training for Diffusions and Flows in Generative Speech Enhancement

- arXiv: [2609.24651](https://arxiv.org/abs/2609.24651) | [PDF](https://arxiv.org/pdf/2609.24651) | [papers.cool](https://papers.cool/arxiv/2609.24651)
- Authors: Qing Yao, Lijian Gao, Qirong Mao
- Published: 2026-09-21 14:23 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; planning_and_action: rollout
- Abstract skim: Diffusion and flow models, as promising generative paradigms for speech enhancement, face a training--inference mismatch: training uses analytical path states, whereas inference recursively evaluates models on self-generated rollout states along discretized sampling trajectories. This mismatch causes prediction and...

### 27 - DocMIDE: Learning Multi-Hop Implicit Derivation in Visually Rich Documents

- arXiv: [2609.24092](https://arxiv.org/abs/2609.24092) | [PDF](https://arxiv.org/pdf/2609.24092) | [papers.cool](https://papers.cool/arxiv/2609.24092)
- Authors: Jeremy Cerwin Wang, Wai Kit Wong, Jeff Kai Tai Tang
- Published: 2026-09-21 04:24 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Real-world document processing systems rely on rigid, predefined schemas, yet critical target fields often lack direct visual counterparts on the page. Extracting these implicit values requires multi-hop derivation, such as aggregating sub-categories or reasoning over visual marks. While existing methods handle...

### 27 - Stable and Efficient Real-World Online VLA Post-Training via Asynchronous Replay-Anchored Policy Improvement

- arXiv: [2609.22888](https://arxiv.org/abs/2609.22888) | [PDF](https://arxiv.org/pdf/2609.22888) | [papers.cool](https://papers.cool/arxiv/2609.22888)
- Authors: Jiarui Yang, Jiajin Zhang, Bin Zhu, Jingjing Chen, Yu-Gang Jiang
- Published: 2026-09-19 08:45 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; planning_and_action: rollout
- Abstract skim: Online post-training of vision-language-action (VLA) models requires efficient use of robot interaction and reliable policy improvement from continually collected experience. We propose asynchronous Replay-Anchored Policy improvement (RAPolicy), a framework that performs rollout and learning concurrently while...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
