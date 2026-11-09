# RL / Post-Training / Agentic RL Reading Queue - 2026-11-09

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 424. Minimum score: 8.

## Top Picks

### 53 - It Takes Two to Tangram: Multi-Agent Object Centric Reinforcement Learning for Assembly

- arXiv: [2611.08814](https://arxiv.org/abs/2611.08814) | [PDF](https://arxiv.org/pdf/2611.08814) | [papers.cool](https://papers.cool/arxiv/2611.08814)
- Authors: Paul Knaußt, Kay Pompetzki, Nico Bohlinger, Niklas Funk, Cristiana de Farias, Rolf Findeisen, et al. (7 authors)
- Published: 2026-11-06 00:11 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization; planning_and_action: planning; memory_and_benchmarks: evaluation
- Abstract skim: Geometric assembly requires fine spatiotemporal coordination to place parts without causing collisions or deadlocks under tight clearances. To address this, we present an object-centric reinforcement learning framework that treats each part as an agent and learns a shared policy for continuous assembly control. A...

### 48 - Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters

- arXiv: [2611.09634](https://arxiv.org/abs/2611.09634) | [PDF](https://arxiv.org/pdf/2611.09634) | [papers.cool](https://papers.cool/arxiv/2611.09634)
- Authors: Constantinos Karouzos, Nikolaos Aletras
- Published: 2026-11-06 15:50 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, preference optimization, +1 more
- Abstract skim: Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned...

### 45 - Alignment by Confident Debate: Preference Learning from Multi-Agent Debate

- arXiv: [2611.09568](https://arxiv.org/abs/2611.09568) | [PDF](https://arxiv.org/pdf/2611.09568) | [papers.cool](https://papers.cool/arxiv/2611.09568)
- Authors: Nikhil Verma, Dingxian Wang, Mohammad Reza Rezaei, Andrew Rabinovich, Zhao Chen
- Published: 2026-11-06 15:08 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Post-training language models for reasoning typically rely on gold answers, task-specific verifiers, or learned reward models, limiting scalability when such signals are scarce. Multi-agent debate offers a self-supervised alternative, but converting debate into reliable training supervision remains challenging:...

### 44 - On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning

- arXiv: [2611.09872](https://arxiv.org/abs/2611.09872) | [PDF](https://arxiv.org/pdf/2611.09872) | [papers.cool](https://papers.cool/arxiv/2611.09872)
- Authors: Haoyu Wang, Ru Wang, Yuanyuan Wang, Jiaxian Guo, Mingming Gong
- Published: 2026-11-06 18:49 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, preference optimization, dpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Test-time reinforcement learning (TTRL) adapts pretrained language models to unlabeled target-domain data using self-generated pseudo-labels, whose reliability remains poorly understood. We analyze majority-vote supervision for TTRL with online Direct Preference Optimization (DPO) and decompose its error into...

### 38 - MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory

- arXiv: [2611.09721](https://arxiv.org/abs/2611.09721) | [PDF](https://arxiv.org/pdf/2611.09721) | [papers.cool](https://papers.cool/arxiv/2611.09721)
- Authors: David H. Yang, Blake Bullwinkel, Amanda Minnich, Mohammad Mohammadi Amiri, Giorgio Severi
- Published: 2026-11-06 17:00 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: llm agent, agent memory; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions....

### 36 - A Separation Principle for Cooperative Multi-Agent Reinforcement Learning

- arXiv: [2611.09644](https://arxiv.org/abs/2611.09644) | [PDF](https://arxiv.org/pdf/2611.09644) | [papers.cool](https://papers.cool/arxiv/2611.09644)
- Authors: Lucia Pezzetti, Nicolas Lanzetti, Antonio Terpin, Florian Dörfler, Giorgia Ramponi
- Published: 2026-11-06 15:57 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: We study cooperative multi-agent reinforcement learning (MARL) problems in which agents evolve under decoupled noisy dynamics but share a population objective. A canonical example is a mobility operator that orchestrates a fleet of vehicles to meet customer demand. The stochastic and time-varying nature of these...

### 36 - Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards

- arXiv: [2611.09448](https://arxiv.org/abs/2611.09448) | [PDF](https://arxiv.org/pdf/2611.09448) | [papers.cool](https://papers.cool/arxiv/2611.09448)
- Authors: Song Yu, Li Li, Zhenming Wu
- Published: 2026-11-06 13:22 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Policy entropy is widely used to diagnose exploration and collapse in reinforcement learning with verifiable rewards (RLVR), yet its magnitude does not consistently track reasoning performance across optimization objectives. We argue that this ambiguity arises because global token entropy conflates uncertainty in...

### 35 - Adaptive Scheduling Pipeline for Multi-Instance Asynchronous Reinforcement Learning

- arXiv: [2611.08864](https://arxiv.org/abs/2611.08864) | [PDF](https://arxiv.org/pdf/2611.08864) | [papers.cool](https://papers.cool/arxiv/2611.08864)
- Authors: Salah Chikhi, Luis Zuin, Entong Li, Zeng Li
- Published: 2026-11-06 01:47 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: We present the Adaptive Scheduling Pipeline (ASP), an offline rollout scheduler for multi-instance asynchronous reinforcement learning (RL) of large language models (LLMs). ASP jointly reduces three sources of rollout underutilization - padding bubbles from intra-minibatch length heterogeneity, skewness bubbles from...

### 33 - Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning

- arXiv: [2611.09625](https://arxiv.org/abs/2611.09625) | [PDF](https://arxiv.org/pdf/2611.09625) | [papers.cool](https://papers.cool/arxiv/2611.09625)
- Authors: Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte
- Published: 2026-11-06 15:45 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, world model; memory_and_benchmarks: memory, long-term memory, benchmark
- Abstract skim: Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term...

### 32 - PhyCAD: Physics-Aware Text-to-CAD Generation via Hierarchical Reinforcement Learning

- arXiv: [2611.09401](https://arxiv.org/abs/2611.09401) | [PDF](https://arxiv.org/pdf/2611.09401) | [papers.cool](https://papers.cool/arxiv/2611.09401)
- Authors: Yuxin Cui, Weijie Zheng, Zhengyang Li, Han Wang, Wenjie Feng, Qiyu Kang
- Published: 2026-11-06 12:35 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization
- Abstract skim: Language-driven computer-aided design (CAD) generation enables the creation of editable parametric models from text, yet geometric correctness alone does not ensure physical feasibility. We present PhyCAD, a framework for physics-aware Text-to-CAD generation that trains language models to produce executable CadQuery...

### 31 - Does Reasoning Improve Psychological Depth in Large Language Models?

- arXiv: [2611.09061](https://arxiv.org/abs/2611.09061) | [PDF](https://arxiv.org/pdf/2611.09061) | [papers.cool](https://papers.cool/arxiv/2611.09061)
- Authors: Ruichen Zheng, Yihe Wang, Fabrice Harel-Canada, Sara Khosravi, Zeynep Senahan Yildiz, Amit Sahai, et al. (7 authors)
- Published: 2026-11-06 06:39 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Benchmark gains from reasoning-enhanced large language models encourage the assumption that these models should broadly perform better on complex generative tasks, but this remains underexplored in open-ended, creative domains shaped by nuances of reader experience. We tested this assumption through the lens of...

### 29 - Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making

- arXiv: [2611.08971](https://arxiv.org/abs/2611.08971) | [PDF](https://arxiv.org/pdf/2611.08971) | [papers.cool](https://papers.cool/arxiv/2611.08971)
- Authors: Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha, Tirthankar Dasgupta
- Published: 2026-11-06 04:33 UTC | Categories: cs.AI, cs.CL, cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: decision making; memory_and_benchmarks: benchmark
- Abstract skim: Multi-agent LLM systems increasingly aggregate judgments across model instances, but reasoning about other agents can itself introduce failure. We study a setting in which LLMs shift their public decisions after observing ambiguous social signals while reporting inaccurate estimates of what other agents privately...

### 28 - CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving

- arXiv: [2611.09139](https://arxiv.org/abs/2611.09139) | [PDF](https://arxiv.org/pdf/2611.09139) | [papers.cool](https://papers.cool/arxiv/2611.09139)
- Authors: Jingjia Teng, Yang Li, Wenjie Huang
- Published: 2026-11-06 08:14 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: traffic, driving
- Abstract skim: This study presents Causal Attribution and Responsibility-Guided Optimization (CARGO), a multi-agent reinforcement learning framework for cooperative on-ramp merging in mixed traffic. A shared latent-context posterior and an action-conditioned response model estimate directed behavioral influence, with posterior...

### 28 - s$^3$: Simple Scaling of Swarms via Cooperative Multi-agent RL

- arXiv: [2611.08615](https://arxiv.org/abs/2611.08615) | [PDF](https://arxiv.org/pdf/2611.08615) | [papers.cool](https://papers.cool/arxiv/2611.08615)
- Authors: Kunal Jha, Gonçalo Faria, Shuyue Stella Li, Scott Geng, Faeze Brahman, Noah A. Smith, et al. (9 authors)
- Published: 2026-11-05 19:07 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Groups can achieve more than individuals in the same amount of time, but only if their members coordinate: they must decide who works on what and what to share. However, this organization in multi-agent systems today usually comes from arbitrary, static harnesses designed a priori without adapting to agent behaviors...

### 27 - Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation

- arXiv: [2611.08718](https://arxiv.org/abs/2611.08718) | [PDF](https://arxiv.org/pdf/2611.08718) | [papers.cool](https://papers.cool/arxiv/2611.08718)
- Authors: Emilly Pitman de Castro, Vanessa Silva, Gustavo Kanno, Marcus Santos, Bruno Ferraz do Amaral, Marcelo Nogueira, et al. (21 authors)
- Published: 2026-11-05 21:14 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; planning_and_action: decision making; memory_and_benchmarks: memory, long-term memory, evaluation
- Abstract skim: Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time. While large language models (LLMs) have improved semantic understanding, they are typically used as isolated components, without addressing how memory, retrieval, and...

### 24 - V-STORM: A Structure-Aware Grounded Chain of Thought Dataset for Faithful and Fine-Grained Spatio-Temporal Video Reasoning

- arXiv: [2611.09511](https://arxiv.org/abs/2611.09511) | [PDF](https://arxiv.org/pdf/2611.09511) | [papers.cool](https://papers.cool/arxiv/2611.09511)
- Authors: Dian Jiao, Yuqian Yuan, Jiaqi Zhu, Mingjian Gao, Siwen Tan, Yunqi Cao, et al. (12 authors)
- Published: 2026-11-06 14:27 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: While MLLMs can often identify what happens in a video, they still struggle with fine-grained spatio-temporal reasoning, which requires precise grounding when and where the supporting evidence appears and composing such evidence into a coherent reasoning chain. This challenge is exacerbated by the lack of scalable...

### 24 - Ordered Policy Optimization

- arXiv: [2611.08936](https://arxiv.org/abs/2611.08936) | [PDF](https://arxiv.org/pdf/2611.08936) | [papers.cool](https://papers.cool/arxiv/2611.08936)
- Authors: Dongkyu Derek Cho, Pan Xu
- Published: 2026-11-06 03:28 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: policy optimization, ppo
- Abstract skim: Proximal Policy Optimization (PPO) stabilizes policy updates by clipping the importance ratio between the new policy and the data-collecting policy. The standard rule uses one fixed clipping range for all samples. While this choice offers simplicity and effectiveness, it fails to distinguish statistically harmful...

### 23 - RPEG: Training Reasoning Language Models Scalably and Cost-Effectively

- arXiv: [2611.09207](https://arxiv.org/abs/2611.09207) | [PDF](https://arxiv.org/pdf/2611.09207) | [papers.cool](https://papers.cool/arxiv/2611.09207)
- Authors: Maciej Besta, Leonard Schmidt, Pierre Pang, Patrik Okanovic, Robert Gerstenberger, Torsten Hoefler
- Published: 2026-11-06 09:28 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Reinforcement learning (RL) is now central to training Reasoning Language Models (RLMs), but RLM pipelines are difficult to scale and costly to run because each RL step couples multiple large models, heterogeneous stages, cross-step state, and complex asynchronous dependencies. Existing systems typically optimize...

### 23 - Learning When to Think: Dual-Reference Offline Optimization for Adaptive VLM Reasoning

- arXiv: [2611.09154](https://arxiv.org/abs/2611.09154) | [PDF](https://arxiv.org/pdf/2611.09154) | [papers.cool](https://papers.cool/arxiv/2611.09154)
- Authors: Hongbin Lin, Sizhe Zou, Juangui Xu, Xinyue Xu, Zhuoli Ouyang, Stanislav Kolchin, et al. (9 authors)
- Published: 2026-11-06 08:35 UTC | Categories: cs.AI
- Why it matched: rl_post_training: grpo; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Reasoning traces improve vision-language models on complex multimodal tasks, but forcing every input to follow a long reasoning process leads to overthinking and unnecessary inference cost. We study adaptive fast/slow thinking for VLMs, where one model answers directly for simple inputs and reasons step by step when...

### 22 - Incentive Pathologies in a Live LLM Agent Arena: An Empirical Study of Concentration, Reward-Rule Implementation Discrepancy, and Network Dilution

- arXiv: [2611.09445](https://arxiv.org/abs/2611.09445) | [PDF](https://arxiv.org/pdf/2611.09445) | [papers.cool](https://papers.cool/arxiv/2611.09445)
- Authors: Lei Zhenbing, Lei Chang
- Published: 2026-11-06 13:19 UTC | Categories: cs.MA
- Why it matched: agentic_rl: llm agent, autonomous agent; reasoning: reasoning
- Abstract skim: We audit one live LLM agent arena (AITRAP; 22 autonomous agent seats, ~96,000 reasoning nodes) over nine days (Oct 16-25, 2026), during which the platform deployed two bundled incentive changes: a progressive tax reform (V2.9.3, Oct 19) and a seed-inversion with explorer-side action update (V3.0, Oct 21). These...

### 22 - ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use

- arXiv: [2611.09036](https://arxiv.org/abs/2611.09036) | [PDF](https://arxiv.org/pdf/2611.09036) | [papers.cool](https://papers.cool/arxiv/2611.09036)
- Authors: Mohamed Elmoghany, Kehan Li, Ruoqu Chen, Tarun Chiruvolu, Shutong Zhang, Ryan Wang, et al. (14 authors)
- Published: 2026-11-06 06:12 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: tool use; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Creative tool use is a fundamental human capability and an important step toward general-purpose embodied intelligence. It requires agents to reason about object affordances, physical constraints, and manipulation strategies, especially when standard tools are unavailable. However, progress in this area is limited...

### 22 - AIM: Adaptive Interaction in Multi-Agent Debate for Multimodal LLM Inference

- arXiv: [2611.08950](https://arxiv.org/abs/2611.08950) | [PDF](https://arxiv.org/pdf/2611.08950) | [papers.cool](https://papers.cool/arxiv/2611.08950)
- Authors: Wei Fan, JinYi Yoon, Bo Ji
- Published: 2026-11-06 03:58 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Multi-Agent Debate (MAD) improves reasoning on multimodal tasks, but its accuracy and token efficiency depend on how agents interact during debate. A largely overlooked design choice is which interaction modalities agents use to exchange evidence. Existing methods rely on fixed text- or graph-based interaction,...

### 22 - Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents

- arXiv: [2611.08946](https://arxiv.org/abs/2611.08946) | [PDF](https://arxiv.org/pdf/2611.08946) | [papers.cool](https://papers.cool/arxiv/2611.08946)
- Authors: Jingdong Zhang, Jionghao Wang, Zhengming Yu, Yancheng Cai, Wei Chow, Chris Choy, et al. (22 authors)
- Published: 2026-11-06 03:51 UTC | Categories: cs.AI, cs.RO
- Why it matched: reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: memory, benchmark
- Abstract skim: Frontier language models are increasingly deployed as agents, and how well an agent performs depends not only on its model but also on its harness: the prompts, tools, memory, and control loop through which the model acts. When an agent is applied to a new problem, a natural question is whether it can use the...

### 21 - Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use

- arXiv: [2611.09113](https://arxiv.org/abs/2611.09113) | [PDF](https://arxiv.org/pdf/2611.09113) | [papers.cool](https://papers.cool/arxiv/2611.09113)
- Authors: Chuxue Cao, Jingru Zeng, Boqin Yin, Yujin Zhou, Yidan Huang, Sujin Chen, et al. (10 authors)
- Published: 2026-11-06 07:47 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant...

### 20 - ReSUM: Reasoning-Driven Multi-Agent Framework for Query-Focused Summarization

- arXiv: [2611.09349](https://arxiv.org/abs/2611.09349) | [PDF](https://arxiv.org/pdf/2611.09349) | [papers.cool](https://papers.cool/arxiv/2611.09349)
- Authors: Sonali, Deeksha Varshney, Asif Ekbal
- Published: 2026-11-06 11:45 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning
- Abstract skim: LLMs excel at language tasks, but long-meeting QFS remains difficult due to complex speaker dynamics, sparse key information, and limited data. Meetings involve disfluencies, long transcripts and complex discourse. QFS have high risk of information omission, hallucination, even for advanced models such as GPT-4-mini...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
