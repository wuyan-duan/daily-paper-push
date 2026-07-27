# RL / Post-Training / Agentic RL Reading Queue - 2026-07-27

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 246. Minimum score: 8.

## Top Picks

### 60 - Deconstructing Off-Policy Ratios: Entropy-Scaled Trust Regions for Asynchronous Reinforcement Learning

- arXiv: [2607.22186](https://arxiv.org/abs/2607.22186) | [PDF](https://arxiv.org/pdf/2607.22186) | [papers.cool](https://papers.cool/arxiv/2607.22186)
- Authors: Guanqun Zhao, Zijun Xie, Binbin Zheng, Enlei Gong, Jiafeng Lu, Yehan Yang, et al. (8 authors)
- Published: 2026-07-24 10:55 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Asynchronous reinforcement learning (RL) accelerates large language model (LLM) post-training by overlapping rollout generation with policy optimization, but the resulting stale, off-policy data can destabilize optimization and ultimately cause policy collapse. Existing methods typically retain or discard tokens...

### 59 - Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning

- arXiv: [2607.22002](https://arxiv.org/abs/2607.22002) | [PDF](https://arxiv.org/pdf/2607.22002) | [papers.cool](https://papers.cool/arxiv/2607.22002)
- Authors: Heyang Jiang, Henry Liu, Baharan Mirzasoleiman
- Published: 2026-07-24 06:04 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has emerged as a highly effective framework for improving LLM reasoning, with methods such as GRPO among its most successful instantiations. However, GRPO relies on repeated generation of long chain-of-thought rollouts. Training time scales with the number of...

### 49 - QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization

- arXiv: [2607.21793](https://arxiv.org/abs/2607.21793) | [PDF](https://arxiv.org/pdf/2607.21793) | [papers.cool](https://papers.cool/arxiv/2607.21793)
- Authors: Siwei Chen, Siqi Chen, Xupeng Miao, Bin Cui
- Published: 2026-07-23 20:20 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Recent large reasoning models often develop long chain-of-thought responses during reinforcement learning (RL), resulting in high inference latency and deployment cost. Existing methods for response length control typically rely on explicit length penalties or additional control modules, which require careful tuning...

### 44 - Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning

- arXiv: [2607.21971](https://arxiv.org/abs/2607.21971) | [PDF](https://arxiv.org/pdf/2607.21971) | [papers.cool](https://papers.cool/arxiv/2607.21971)
- Authors: Shujin Wu, Cheng Qian, Xiusi Chen, Heng Ji
- Published: 2026-07-24 04:35 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reflection; planning_and_action: environment feedback
- Abstract skim: Test-time scaling through iterative self-evolution with environment feedback, as demonstrated by AlphaEvolve, shows remarkable performance gains. We hypothesize that the success of such evolution frameworks hinges on meta-skills, such as self-reflection with environment feedback, that enable effective multi-round...

### 40 - Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Mode

- arXiv: [2607.22083](https://arxiv.org/abs/2607.22083) | [PDF](https://arxiv.org/pdf/2607.22083) | [papers.cool](https://papers.cool/arxiv/2607.22083)
- Authors: Nanbeige Lab, :, Chen Yang, Chengrui Huang, Fufeng Lan, Hanhui Chen, et al. (26 authors)
- Published: 2026-07-24 08:33 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agentic rl, tool use; rl_post_training: rlhf; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: We present Nanbeige4.2-3B, a compact general agentic model with 3B non-embedding parameters. It delivers strong performance across code-agent, office-agent, and complex tool-use tasks while maintaining highly competitive reasoning capabilities in mathematics, coding, and science. Nanbeige4.2-3B is pretrained from...

### 39 - Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills

- arXiv: [2607.22529](https://arxiv.org/abs/2607.22529) | [PDF](https://arxiv.org/pdf/2607.22529) | [papers.cool](https://papers.cool/arxiv/2607.22529)
- Authors: Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, et al. (13 authors)
- Published: 2026-07-24 17:59 UTC | Categories: cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning, self-play
- Abstract skim: LLM training is shifting from manual design and annotation to interaction-driven self-evolution. However, existing self-evolutionary methods face a fundamental dilemma between task diversity and verification reliability: environment-bound methods obtain precise feedback but confine learning to narrow domains, while...

### 39 - Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning

- arXiv: [2607.21653](https://arxiv.org/abs/2607.21653) | [PDF](https://arxiv.org/pdf/2607.21653) | [papers.cool](https://papers.cool/arxiv/2607.21653)
- Authors: Jian Hu, Huiying Li, Hao Zhang, Binfeng Xu, Yifan Zhang, Shaokun Zhang, et al. (11 authors)
- Published: 2026-07-22 18:06 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration. Molt is a...

### 30 - Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings

- arXiv: [2607.21962](https://arxiv.org/abs/2607.21962) | [PDF](https://arxiv.org/pdf/2607.21962) | [papers.cool](https://papers.cool/arxiv/2607.21962)
- Authors: Quentin Spencer
- Published: 2026-07-24 04:19 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent, agent memory; memory_and_benchmarks: memory, evaluation
- Abstract skim: Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction histories. We invert the pipeline: a seeded life-script sampler emits facts with validity intervals,...

### 28 - Addressing the Orchestration Gap in Generalist Robots via Physical Agency

- arXiv: [2607.21725](https://arxiv.org/abs/2607.21725) | [PDF](https://arxiv.org/pdf/2607.21725) | [papers.cool](https://papers.cool/arxiv/2607.21725)
- Authors: Liane Galanti, Dhruv Shah, Tri Dao
- Published: 2026-07-23 18:18 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: planning
- Abstract skim: General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success detection, recovery, and low-level control. Today's state-of-the-art models attempt to combine all these capabilities into the learned policy via large-scale pre-training. Instead, we show that these...

### 26 - Filling Before Advancing: Capability-Gap-Driven Post-Training for Scenario-Specialized Remote Sensing MLLMs

- arXiv: [2607.22205](https://arxiv.org/abs/2607.22205) | [PDF](https://arxiv.org/pdf/2607.22205) | [papers.cool](https://papers.cool/arxiv/2607.22205)
- Authors: Yuheng Zong, Minghua Wang, Xin Zhao, Zhi-Hui Zhan, Antonio Plaza, Jon Atli Benediktsson
- Published: 2026-07-24 11:21 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: benchmark
- Abstract skim: Remote sensing multimodal large language models (RS-MLLMs) have improved general aerial-image understanding. However, Earth observation applications require fine-grained scenario specialization, constrained by scarce high-quality scenario data and incomplete capability coverage. We formulate this adaptation as a...

### 22 - Predictive Lightweight MARL for Resilient Coverage in Sparse-Signaling Aerial Networks

- arXiv: [2607.22109](https://arxiv.org/abs/2607.22109) | [PDF](https://arxiv.org/pdf/2607.22109) | [papers.cool](https://papers.cool/arxiv/2607.22109)
- Authors: Chuan-Chi Lai, Ang-Hsun Tsai
- Published: 2026-07-24 09:02 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: This letter proposes the Predictive Lightweight Multi-Agent Reinforcement Learning (PL-MARL) framework to ensure resilient coverage in bandwidth-constrained UAV swarms. To counter coordination collapse caused by sparse signaling and information aging, we introduce a Kinematic-Aware Inference Engine that proactively...

### 21 - Integrated Order Dispatching and Routing for Last-Mile Pickup via Deep Reinforcement Learning

- arXiv: [2607.22356](https://arxiv.org/abs/2607.22356) | [PDF](https://arxiv.org/pdf/2607.22356) | [papers.cool](https://papers.cool/arxiv/2607.22356)
- Authors: Yida Xu, Zhaofang Mao, Yuheng Miao, Jiaxin Zhang, Yiting Sun
- Published: 2026-07-24 14:37 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: decision making; memory_and_benchmarks: evaluation
- Abstract skim: In recent years, the growing complexity of last-mile pickup operations has increased the need for fast and accurate decision-making on logistics platforms. This challenge is fundamentally driven by two key and tightly coupled decision-making processes: order dispatching and routing. Solving them separately overlooks...

### 20 - Visual Saliency Steering Distillation for Multimodal Chain-of-Thought Reasoning

- arXiv: [2607.22013](https://arxiv.org/abs/2607.22013) | [PDF](https://arxiv.org/pdf/2607.22013) | [papers.cool](https://papers.cool/arxiv/2607.22013)
- Authors: Hao Yang, Jin Wang, Xuejie Zhang
- Published: 2026-07-24 06:22 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Multimodal chain-of-thought (CoT) reasoning integrates visual and textual cues through step-by-step inference. In small models with limited token budgets, modality-interaction fusion often suppresses tiny cross-modal differences. In particular, multimodal CoT often struggles when different images pair with identical...

### 18 - The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents

- arXiv: [2607.22520](https://arxiv.org/abs/2607.22520) | [PDF](https://arxiv.org/pdf/2607.22520) | [papers.cool](https://papers.cool/arxiv/2607.22520)
- Authors: Darshan Tank, Baran Nama
- Published: 2026-07-24 17:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; memory_and_benchmarks: evaluation
- Abstract skim: Adding procedural skills to an LLM agent is typically evaluated by average improvement in task success. However, this metric hides an important cost: skills can also make agents worse. We measure both sides by comparing agents with and without skills across nearly 6,000 runs spanning two office automation benchmarks...

### 18 - One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments

- arXiv: [2607.22119](https://arxiv.org/abs/2607.22119) | [PDF](https://arxiv.org/pdf/2607.22119) | [papers.cool](https://papers.cool/arxiv/2607.22119)
- Authors: Jan Ole von Hartz, Abhinav Valada, Joschka Boedecker
- Published: 2026-07-24 09:14 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: benchmark
- Abstract skim: Multi-stream robot manipulation policies achieve unparalleled sample efficiency and generalization by modeling actions relative to environmental reference frames. However, existing approaches typically assume these frames to be strictly exogenous. This causal assumption collapses in dynamic settings, such as when a...

### 18 - J-CoT: Chain-of-Thought in J-Space

- arXiv: [2607.21981](https://arxiv.org/abs/2607.21981) | [PDF](https://arxiv.org/pdf/2607.21981) | [papers.cool](https://papers.cool/arxiv/2607.21981)
- Authors: Junde Wu, Jiayuan Zhu, Fengling Liu, Minhao Hu, Jiazhen Pan
- Published: 2026-07-24 04:57 UTC | Categories: cs.AI, cs.CL
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark
- Abstract skim: Chain-of-thought prompting improves language-model reasoning by carrying intermediate states across successive computation steps. However, relying on natural language as the only recurrent interface is overly restrictive, since many transient computations do not need to be fully verbalized. Existing latent-reasoning...

### 18 - Reliability-Contagion Feasibility in LLM Multi-Agent Networks

- arXiv: [2607.21912](https://arxiv.org/abs/2607.21912) | [PDF](https://arxiv.org/pdf/2607.21912) | [papers.cool](https://papers.cool/arxiv/2607.21912)
- Authors: Ruiwu Niu, Xincheng Shu, Ying Zhao
- Published: 2026-07-24 02:38 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: benchmark
- Abstract skim: Communication allows large language model agents to pool evidence, but it also creates paths along which an erroneous claim can spread. We formulate a correction-aware network model that tracks susceptible, exposed, infectious, and corrected agents and derive its early-invasion condition for heterogeneous...

### 18 - Quasi-Monte Carlo Initialization for Meta-Reinforcement Learning

- arXiv: [2607.21637](https://arxiv.org/abs/2607.21637) | [PDF](https://arxiv.org/pdf/2607.21637) | [papers.cool](https://papers.cool/arxiv/2607.21637)
- Authors: Julian G. Soltes
- Published: 2026-07-21 03:30 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark
- Abstract skim: This paper explores the efficacy of quasi-Monte Carlo (QMC) weight initialization for meta-reinforcement learning within modern benchmark environments. Various sampling methods are used to bound a population-based search and aggregate an optimal prior from a baseline set of tasks. The QMC meta-priors show...

### 17 - Conformal Constraint Tightening for Chance-Constrained Motion Planning with Unknown Dynamics

- arXiv: [2607.22409](https://arxiv.org/abs/2607.22409) | [PDF](https://arxiv.org/pdf/2607.22409) | [papers.cool](https://papers.cool/arxiv/2607.22409)
- Authors: Shubham Natraj, Bruno Sinopoli, Yiannis Kantaros
- Published: 2026-07-24 15:27 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, trajectory
- Abstract skim: Motion planning algorithms compute control sequences that drive autonomous robots to goal regions while avoiding unsafe states. Existing methods, from sampling-based planning to deep reinforcement learning, typically provide task-completion guarantees only with respect to a nominal model or simulator, which may be...

### 16 - Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture

- arXiv: [2607.22445](https://arxiv.org/abs/2607.22445) | [PDF](https://arxiv.org/pdf/2607.22445) | [papers.cool](https://papers.cool/arxiv/2607.22445)
- Authors: Halil Burak Noyan
- Published: 2026-07-24 16:08 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Enterprise AI agents are typically granted static credential sets at configuration time, holding every tool the role might need for every task they perform. This persistent over-privilege expands the attack surface. We argue that capability scoping must follow a dynamic least-privilege principle and be treated as a...

### 16 - Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs

- arXiv: [2607.22039](https://arxiv.org/abs/2607.22039) | [PDF](https://arxiv.org/pdf/2607.22039) | [papers.cool](https://papers.cool/arxiv/2607.22039)
- Authors: Zixuan Ren, Jinliang Lu, Junhong Wu, Yang Zhao, Dai Dai, Hua Wu, et al. (8 authors)
- Published: 2026-07-24 07:08 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning
- Abstract skim: Model merging plays a crucial role in consolidating multiple specialized models into a single, unified model, especially in the era of large language models (LLMs). Recent research has primarily focused on developing strategies to enhance merging performance with the trained models, while the impact of training...

### 16 - Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge

- arXiv: [2607.21946](https://arxiv.org/abs/2607.21946) | [PDF](https://arxiv.org/pdf/2607.21946) | [papers.cool](https://papers.cool/arxiv/2607.21946)
- Authors: Jiseok Kwak, Suhyeon Jo, Taewoo Kim, Yeongmin Kim, Byeonghu Na, Il-chul Moon
- Published: 2026-07-24 03:44 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning
- Abstract skim: This technical report presents our approach to Challenge Track~3: SeePhys Pro at the 3rd AI for Math Workshop, where the task is to answer college-level physics questions whose statement and figure may be given partly or entirely as an image. Visual physics problems become substantially harder for large language...

### 15 - Learning Structural Convergence: A Neuro-Symbolic Benchmark for Temporal Reasoning

- arXiv: [2607.22365](https://arxiv.org/abs/2607.22365) | [PDF](https://arxiv.org/pdf/2607.22365) | [papers.cool](https://papers.cool/arxiv/2607.22365)
- Authors: Michael Romei De Socio, Gian Luca Pozzato, Alessio Merlo
- Published: 2026-07-24 14:50 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: High-complexity operational environments require methods that detect and anticipate temporally distributed patterns rather than classify isolated events. This paper introduces TRACTA (Temporal Reasoning and Capability-Trajectory Analysis), a controlled synthetic benchmark for temporal structural reasoning in high-...

### 15 - Multi-Agent System-driven Digital Twins for predictive maintenance: architectures, technologies and open research challenges

- arXiv: [2607.21873](https://arxiv.org/abs/2607.21873) | [PDF](https://arxiv.org/pdf/2607.21873) | [papers.cool](https://papers.cool/arxiv/2607.21873)
- Authors: Korota Arsène Coulibaly, Mohamed Hamlich
- Published: 2026-07-24 00:09 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; planning_and_action: decision making
- Abstract skim: Digital twins have emerged as a foundational technology within the context of Industry 4.0, offering a paradigm for the real-time virtual representation of physical systems. However, managing their growing complexity, particularly in distributed industrial environments, requires intelligent architectures capable of...

### 14 - ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation

- arXiv: [2607.22530](https://arxiv.org/abs/2607.22530) | [PDF](https://arxiv.org/pdf/2607.22530) | [papers.cool](https://papers.cool/arxiv/2607.22530)
- Authors: Yunao Huang, Shiyu Sang, Haotao Lu, Suting Ni, Shijie Wu, Ziyang Guo, et al. (8 authors)
- Published: 2026-07-24 17:59 UTC | Categories: cs.RO
- Why it matched: planning_and_action: trajectory, rollout, world model; memory_and_benchmarks: evaluation
- Abstract skim: Contact-rich robot manipulation requires physical interaction cues that are often invisible to cameras, making tactile sensing essential for robust control. However, scaling visuo-tactile robot learning remains difficult because real tactile interaction data are expensive to collect, hardware-dependent, and limited...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
