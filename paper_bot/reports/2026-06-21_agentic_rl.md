# RL / Post-Training / Agentic RL Reading Queue - 2026-06-21

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 412. Minimum score: 8.

## Top Picks

### 64 - Uncertainty-Aware Reward Modeling for Stable RLHF

- arXiv: [2606.19818](https://arxiv.org/abs/2606.19818) | [PDF](https://arxiv.org/pdf/2606.19818) | [papers.cool](https://papers.cool/arxiv/2606.19818)
- Authors: Licheng Pan, Haocheng Yang, Haoxuan Li, Yichen Sun, Yunsheng Lu, Shijian Wang, et al. (10 authors)
- Published: 2026-06-18 05:46 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, policy optimization, +2 more
- Abstract skim: Reinforcement learning from human feedback (RLHF) aligns large language models by training reward models on preference data and optimizing policies to maximize predicted rewards. However, this pipeline faces two fundamental challenges: (1) reward models cannot signal when their predictions are unreliable, since they...

### 61 - MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments

- arXiv: [2606.19893](https://arxiv.org/abs/2606.19893) | [PDF](https://arxiv.org/pdf/2606.19893) | [papers.cool](https://papers.cool/arxiv/2606.19893)
- Authors: Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, et al. (7 authors)
- Published: 2026-06-18 07:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent training; rl_post_training: reinforcement learning, grpo; reasoning: reflection; memory_and_benchmarks: benchmark, gaia
- Abstract skim: Deep research agents have demonstrated remarkable capabilities in autonomous information gathering and synthesis, yet their training remains constrained by the static nature of simulated environments, the limits of fact-retrieval-only task designs, and the inefficiency of outcome-based reinforcement learning. In...

### 60 - VIMPO: Value-Implicit Policy Optimization for LLMs

- arXiv: [2606.20008](https://arxiv.org/abs/2606.20008) | [PDF](https://arxiv.org/pdf/2606.20008) | [papers.cool](https://papers.cool/arxiv/2606.20008)
- Authors: Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song, Xuandong Zhao
- Published: 2026-06-18 09:44 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, grpo, +1 more; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement learning with verifiable rewards has become a central tool for improving the reasoning ability of large language models, but current methods face a trade-off between simplicity and credit assignment. Group-relative methods such as GRPO avoid training a critic, but typically assign a trajectory-level...

### 46 - Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution

- arXiv: [2606.20014](https://arxiv.org/abs/2606.20014) | [PDF](https://arxiv.org/pdf/2606.20014) | [papers.cool](https://papers.cool/arxiv/2606.20014)
- Authors: Jannik Hösch, Alessandro Sestini, Florian Fuchs, Amir Baghi, Joakim Bergdahl, Konrad Tollmar, et al. (8 authors)
- Published: 2026-06-18 09:47 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning, decision making
- Abstract skim: Reinforcement learning (RL) has achieved strong performance in sequential decision-making, yet scaling to complex multi-agent environments remains challenging due to sparse rewards, large state-action spaces, and the difficulty of learning coordinated strategies. We propose a hierarchical architecture where a...

### 43 - Process-Verified Reinforcement Learning for Theorem Proving via Lean

- arXiv: [2606.20068](https://arxiv.org/abs/2606.20068) | [PDF](https://arxiv.org/pdf/2606.20068) | [papers.cool](https://papers.cool/arxiv/2606.20068)
- Authors: Minsu Kim, Se-Young Yun
- Published: 2026-06-18 10:40 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: While reinforcement learning from verifiable rewards (RLVR) typically has relied on a single binary verification signal, symbolic proof assistants in formal reasoning offer rich, fine-grained structured feedback. This gap between structured processes and unstructured rewards highlights the importance of feedback...

### 40 - Which Pairs to Compare for LLM Post-Training?

- arXiv: [2606.19607](https://arxiv.org/abs/2606.19607) | [PDF](https://arxiv.org/pdf/2606.19607) | [papers.cool](https://papers.cool/arxiv/2606.19607)
- Authors: Jiangze Han, Vineet Goyal, Will Ma
- Published: 2026-06-17 21:19 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, preference optimization, dpo
- Abstract skim: Preference-based post-training has become a central paradigm for aligning language models. A common data-collection strategy is to generate a small set of completions for each prompt and label the resulting comparison pairs. However, human preference labels are often much more expensive than generating additional...

### 33 - SPOT-E: Test-Time Entropy Shaping with Visual Spotlights for Frozen VLMs

- arXiv: [2606.20244](https://arxiv.org/abs/2606.20244) | [PDF](https://arxiv.org/pdf/2606.20244) | [papers.cool](https://papers.cool/arxiv/2606.20244)
- Authors: Bo Yin, Xiaobin Hu, Chengming Xu, Ruolin Shen, Mo Yang, Jiangning Zhang, et al. (9 authors)
- Published: 2026-06-18 13:56 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: Vision-language models (VLMs) often underperform on evidence intensive tasks because decisive visual evidence are small, localized, and easy to overlook, leading to failures in evidence readout even when high-level reasoning is intact. Prior inference-time visual interventions can improve grounding without...

### 33 - Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning

- arXiv: [2606.19771](https://arxiv.org/abs/2606.19771) | [PDF](https://arxiv.org/pdf/2606.19771) | [papers.cool](https://papers.cool/arxiv/2606.19771)
- Authors: Xuanzhi Feng, Zhengyang Li, Zeyu Liu, Haoxi Li, Yuming Jiang, Bing Guo, et al. (9 authors)
- Published: 2026-06-18 04:11 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; downranked: driving
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) has significantly advanced Large Language Model (LLM) reasoning; however, it faces a fundamental optimization instability: uniform token updates precipitate entropy collapse, leading to premature convergence to suboptimal strategies, whereas excessive Shannon...

### 31 - A Multi-Agent system for Multi-Objective constrained optimization

- arXiv: [2606.20236](https://arxiv.org/abs/2606.20236) | [PDF](https://arxiv.org/pdf/2606.20236) | [papers.cool](https://papers.cool/arxiv/2606.20236)
- Authors: Federica Filippini
- Published: 2026-06-18 13:47 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: decision making
- Abstract skim: Many decision-making problems in computing and networking systems can be naturally formulated as cost-minimization problems under performance constraints. In dynamic environments, reinforcement learning (RL) is often used to solve such problems at runtime by embedding both costs and constraint violations into a...

### 30 - When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents

- arXiv: [2606.20023](https://arxiv.org/abs/2606.20023) | [PDF](https://arxiv.org/pdf/2606.20023) | [papers.cool](https://papers.cool/arxiv/2606.20023)
- Authors: Kaiyue Yang, Yuyan Bu, Jingwei Yi, Yuchi Wang, Biyu Zhou, Juntao Dai, et al. (8 authors)
- Published: 2026-06-18 09:54 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training
- Abstract skim: As LLM agents increasingly select tools autonomously, their choices among tools with different privileges become safety-relevant. However, prior tool-selection studies focus on safety-agnostic metadata preferences, leaving privilege-sensitive choices underexplored. To address this gap, we study over-privileged tool...

### 30 - Multi-Granular Attention-Driven Reinforcement Learning Framework for Web Intelligent Enhancement Systems

- arXiv: [2606.19690](https://arxiv.org/abs/2606.19690) | [PDF](https://arxiv.org/pdf/2606.19690) | [papers.cool](https://papers.cool/arxiv/2606.19690)
- Authors: Navin Chhibber, Deepak Singh, Anokh Kishore, Nikita Chawla, K. Anguraj
- Published: 2026-06-18 01:38 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: From the past few years, web intelligent enhancement systems increasingly rely on heterogeneous and dynamic web data to deliver personalized, context-aware services. However, traditional machine learning, deep learning, and reinforcement learning models often struggle with semantic understanding, adaptability, and...

### 29 - Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning

- arXiv: [2606.20002](https://arxiv.org/abs/2606.20002) | [PDF](https://arxiv.org/pdf/2606.20002) | [papers.cool](https://papers.cool/arxiv/2606.20002)
- Authors: Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, et al. (7 authors)
- Published: 2026-06-18 09:38 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: This work presents a general framework for training large language models (LLMs) to "Connect the Dots" (CoD), a meta-capability required by long-lifecycle agents: as an LLM-based AI agent gets deployed in an environment, it solves a long sequence of tasks while continuously exploring the environment, learning from...

### 28 - Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation

- arXiv: [2606.19632](https://arxiv.org/abs/2606.19632) | [PDF](https://arxiv.org/pdf/2606.19632) | [papers.cool](https://papers.cool/arxiv/2606.19632)
- Authors: Ahmad Farooq, Kamran Iqbal
- Published: 2026-06-17 22:22 UTC | Categories: cs.AI, cs.LG, cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Multi-agent reinforcement learning (MARL) enables agents to develop coordination strategies through emergent communication, but neural policies lack the formal safety guarantees required for safety-critical robotic deployment in drone swarms and autonomous vehicle fleets. We present the first end-to-end framework...

### 25 - LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems

- arXiv: [2606.20408](https://arxiv.org/abs/2606.20408) | [PDF](https://arxiv.org/pdf/2606.20408) | [papers.cool](https://papers.cool/arxiv/2606.20408)
- Authors: Hanwool Lee, Dasol Choi, Bokyeong Kim, Seung Geun Kim, Haon Park
- Published: 2026-06-18 15:57 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; planning_and_action: acting; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Large language model (LLM) agents are increasingly proposed as supervisory components for safety-critical systems, yet their robustness under sustained, adaptive adversarial pressure remains poorly characterized. We present NRT-Bench, a benchmark for multi-turn red-teaming of LLM agents acting as operators of a...

### 25 - Emergent Alignment

- arXiv: [2606.19527](https://arxiv.org/abs/2606.19527) | [PDF](https://arxiv.org/pdf/2606.19527) | [papers.cool](https://papers.cool/arxiv/2606.19527)
- Authors: Martin Kolář
- Published: 2026-06-17 19:18 UTC | Categories: cs.AI
- Why it matched: rl_post_training: preference optimization, dpo; reasoning: reasoning
- Abstract skim: Can Large Language Models (LLMs) discern when their own outputs are misaligned with human ethics? And can they self-correct? We endow an LLM with a conscience step that reviews its own reasoning and outputs, and we extend the training loss with an alignment component using Direct Preference Optimization (DPO) to...

### 24 - Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining

- arXiv: [2606.20363](https://arxiv.org/abs/2606.20363) | [PDF](https://arxiv.org/pdf/2606.20363) | [papers.cool](https://papers.cool/arxiv/2606.20363)
- Authors: Yuexing Hao, Xiaomin Li
- Published: 2026-06-18 15:25 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reward model, grpo; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Explicit skill libraries make computer-using agents easier to inspect, but it remains unclear whether such libraries can be mined from interaction data in a way that improves downstream policies. We study this question through a three-stage pipeline that segments GUI trajectories, clusters segments into candidate...

### 24 - Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale

- arXiv: [2606.20058](https://arxiv.org/abs/2606.20058) | [PDF](https://arxiv.org/pdf/2606.20058) | [papers.cool](https://papers.cool/arxiv/2606.20058)
- Authors: Harsh Rao Dhanyamraju, Leonidas Raghav, Aaron Lee
- Published: 2026-06-18 10:32 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent orchestration
- Abstract skim: Enterprise AI aims to move toward continuous event monitoring, detection, and action across specialist agents, yet existing multi-agent systems largely assume discrete request-response workflows and remain underexplored at enterprise scale. We evaluate DAG Plan and Execute and ReAct across 208 production-derived...

### 24 - Multi-Agent Transactive Memory

- arXiv: [2606.19911](https://arxiv.org/abs/2606.19911) | [PDF](https://arxiv.org/pdf/2606.19911) | [papers.cool](https://papers.cool/arxiv/2606.19911)
- Authors: To Eun Kim, Xuhong He, Dishank Jain, Ambuj Agrawal, Negar Arabzadeh, Fernando Diaz
- Published: 2026-06-18 08:04 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: memory, webarena, alfworld
- Abstract skim: The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations. Just as search engines index human-generated artifacts to support human problem solving, retrieval systems can organize agent-generated...

### 24 - AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA

- arXiv: [2606.19782](https://arxiv.org/abs/2606.19782) | [PDF](https://arxiv.org/pdf/2606.19782) | [papers.cool](https://papers.cool/arxiv/2606.19782)
- Authors: Aravind Narayanan, Shaina Raza
- Published: 2026-06-18 04:33 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: multi-agent; planning_and_action: planning, acting; memory_and_benchmarks: evaluation
- Abstract skim: Financial chart question answering in regulated settings demands more than accuracy: practitioners must know which answers to trust before acting on them, and many institutions cannot send client data to external model providers. Yet existing chart-QA agents are accuracy-focused and opaque, and most assume...

### 24 - Beyond Uniform Forgetting: A Study of Sequential Direct Preference Optimization Across Preference Settings

- arXiv: [2606.19744](https://arxiv.org/abs/2606.19744) | [PDF](https://arxiv.org/pdf/2606.19744) | [papers.cool](https://papers.cool/arxiv/2606.19744)
- Authors: Pranav Bhandari, Nicolas Fay, Amitava Datta, Usman Naseem, Mehwish Nasim
- Published: 2026-06-18 03:20 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: preference optimization, dpo
- Abstract skim: Aligning language models with human preferences often requires optimising multiple behavioural objectives. A practical approach is to apply these objectives sequentially using preference optimisation methods such as Direct Preference Optimisation (DPO), but it remains unclear whether later training uniformly...

### 24 - Hidden Anchors in Multi-Agent LLM Deliberation

- arXiv: [2606.19494](https://arxiv.org/abs/2606.19494) | [PDF](https://arxiv.org/pdf/2606.19494) | [papers.cool](https://papers.cool/arxiv/2606.19494)
- Authors: Apurba Pokharel, Ram Dantu
- Published: 2026-06-17 18:29 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, deliberation
- Abstract skim: Multi-agent LLM deliberation, where agents exchange and revise answers over several rounds, is increasingly used to improve reasoning and accuracy, yet how and why it works is rarely modelled. Such deliberation mirrors how humans reach decisions. As social animals we are pulled both by the group, the herd effect...

### 21 - ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

- arXiv: [2606.19980](https://arxiv.org/abs/2606.19980) | [PDF](https://arxiv.org/pdf/2606.19980) | [papers.cool](https://papers.cool/arxiv/2606.19980)
- Authors: Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, et al. (17 authors)
- Published: 2026-06-18 09:21 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; reasoning: self-improvement, self improvement; planning_and_action: rollout
- Abstract skim: Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely...

### 21 - Insulin4RL: Real-Time Insulin Management in the Intensive Care Unit for Offline Reinforcement Learning

- arXiv: [2606.19481](https://arxiv.org/abs/2606.19481) | [PDF](https://arxiv.org/pdf/2606.19481) | [papers.cool](https://papers.cool/arxiv/2606.19481)
- Authors: Thomas Frost, Steve Harris
- Published: 2026-06-17 18:13 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: decision making; memory_and_benchmarks: evaluation
- Abstract skim: Offline reinforcement learning (ORL) offers the potential to improve the quality of clinical decision-making using historical electronic health record (EHR) data. Current training and evaluative practices in this field rely heavily on EHR datasets that have been temporally discretised into fixed, regular time...

### 19 - What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis

- arXiv: [2606.20075](https://arxiv.org/abs/2606.20075) | [PDF](https://arxiv.org/pdf/2606.20075) | [papers.cool](https://papers.cool/arxiv/2606.20075)
- Authors: Xinghao Chen, Chak Tou Leong, Wenjin Guo, Jian Wang, Wenjie Li, Xiaoyu Shen
- Published: 2026-06-18 10:51 UTC | Categories: cs.CL, cs.LG
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory
- Abstract skim: Latent Chain-of-Thought (CoT) internalizes reasoning within continuous hidden states, offering a promising alternative to verbose discrete reasoning traces. However, robust latent reasoning remains difficult because outcome supervision provides weak learning signals and leaves latent trajectories prone to semantic...

### 19 - Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models

- arXiv: [2606.19750](https://arxiv.org/abs/2606.19750) | [PDF](https://arxiv.org/pdf/2606.19750) | [papers.cool](https://papers.cool/arxiv/2606.19750)
- Authors: Darrien McKenzie, Nicklas Hansen, Xiaolong Wang
- Published: 2026-06-18 03:31 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) is a central approach for improving reasoning capabilities in large language models (LLMs), where training efficiency depends critically on how problems are sampled during optimization. Existing adaptive curriculum learning methods typically prioritize prompts of intermediate difficulty,...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
