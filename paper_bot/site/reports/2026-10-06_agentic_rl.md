# RL / Post-Training / Agentic RL Reading Queue - 2026-10-06

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 1173. Minimum score: 8.

## Top Picks

### 82 - ThunderSyncRL: Lossless Acceleration of Agentic Reinforcement Learning

- arXiv: [2610.05935](https://arxiv.org/abs/2610.05935) | [PDF](https://arxiv.org/pdf/2610.05935) | [papers.cool](https://papers.cool/arxiv/2610.05935)
- Authors: Seil Kang, Hangoo Kang, Tarun Suresh, Youngeun Kim, Shreyas Pimpalgaonkar, Seong Jae Hwang, et al. (7 authors)
- Published: 2026-10-05 07:51 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; planning_and_action: trajectory, rollout
- Abstract skim: Language models are moving beyond generating answers to pursuing long-horizon goals in interactive environments. Post-training these agents requires long, heterogeneous trajectories, and synchronous systems leave learner engines idle until rollout and verification finish. To squeeze out these pipeline bubbles,...

### 73 - DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation

- arXiv: [2610.04596](https://arxiv.org/abs/2610.04596) | [PDF](https://arxiv.org/pdf/2610.04596) | [papers.cool](https://papers.cool/arxiv/2610.04596)
- Authors: Karn Tiwari, Varnith Chordia, Prathosh A P
- Published: 2026-10-03 15:33 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +3 more; reasoning: reasoning; planning_and_action: trajectory, rollout; memory_and_benchmarks: evaluation
- Abstract skim: On-policy distillation (OPD) has emerged as a widely used paradigm for post-training large language models, reducing the train--test mismatch of conventional distillation by supervising the student on its own generated trajectories. However, existing OPD objectives remain largely token-local and outcome-agnostic,...

### 72 - Ontology Concept Overlap as a Training Signal: Knowledge-Grounded Reinforcement Learning for Clinical Question Answering

- arXiv: [2610.06360](https://arxiv.org/abs/2610.06360) | [PDF](https://arxiv.org/pdf/2610.06360) | [papers.cool](https://papers.cool/arxiv/2610.06360)
- Authors: Aditya Tanna, Abhishek Jindal
- Published: 2026-10-05 13:59 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlhf, +4 more
- Abstract skim: Reinforcement learning post-training for language models relies on two reward designs: human preferences (RLHF, DPO) and binary verifiers (RLVR). Clinical question answering fits neither. Near-correct answers differ by a single substituted entity, and no executable check decides clinical correctness. We instantiate...

### 52 - Rewrite What Matters: Adaptive Multilingual Query Rewriting for Reasoning via Agentic Reinforcement Learning

- arXiv: [2610.04899](https://arxiv.org/abs/2610.04899) | [PDF](https://arxiv.org/pdf/2610.04899) | [papers.cool](https://papers.cool/arxiv/2610.04899)
- Authors: Rui Qi, Yufeng Chen, Yunlong Liang, Chuan Meng, Sijin Lu, Ge Shi, et al. (9 authors)
- Published: 2026-10-04 03:19 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: decision making
- Abstract skim: In multilingual scenarios, queries with equivalent semantics but in different languages could guide the model into different reasoning trajectories, leading to performance disparities. To mitigate this gap, previous studies typically apply a one-size-fits-all query rewriting strategy, such as translation, which...

### 47 - Asynchronous Is Nearly Free for Evolution Strategies on Long-Horizon Agentic Tasks

- arXiv: [2610.04196](https://arxiv.org/abs/2610.04196) | [PDF](https://arxiv.org/pdf/2610.04196) | [papers.cool](https://papers.cool/arxiv/2610.04196)
- Authors: William Hoy, Jingxuan Fan, Nurcin Celik, Xu Pan
- Published: 2026-10-03 01:18 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more; planning_and_action: rollout; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: LLM-based long-horizon agentic post-training is often bottlenecked by rollout generation: trajectories span many interaction turns, completion times vary substantially, and synchronous update barriers leave faster workers waiting for stragglers. Asynchronous reinforcement learning which has been adopted in LLM post-...

### 44 - CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling

- arXiv: [2610.06829](https://arxiv.org/abs/2610.06829) | [PDF](https://arxiv.org/pdf/2610.06829) | [papers.cool](https://papers.cool/arxiv/2610.06829)
- Authors: Yifan Zhang, Yutong Dai, Viraj Prabhu, Zhiyuan Hu, Ran Xu, Zeyuan Chen
- Published: 2026-10-05 17:57 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning; planning_and_action: trajectory, rollout; memory_and_benchmarks: benchmark, evaluation, webarena
- Abstract skim: Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed...

### 44 - Can LLM Agents Automate Reinforcement Learning for Text-to-Speech?

- arXiv: [2610.04488](https://arxiv.org/abs/2610.04488) | [PDF](https://arxiv.org/pdf/2610.04488) | [papers.cool](https://papers.cool/arxiv/2610.04488)
- Authors: Xuanjun Chen, Zixiong Su, Hao Shi, Chang Zeng, Kai Li, Jyh-Shing Roger Jang, et al. (7 authors)
- Published: 2026-10-03 12:44 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Although reinforcement learning (RL) post-training repairs the localized segmental errors of zero-shot text-to-speech (TTS), arriving at a working recipe still relies on tedious manual tuning, and whether LLM agents can take over this research pipeline is unclear. We investigate this question with AgenticTTS-Forge,...

### 44 - Hierarchical Credit Assignment for RLVR on Fused Gromov-Wasserstein Geometry

- arXiv: [2610.04344](https://arxiv.org/abs/2610.04344) | [PDF](https://arxiv.org/pdf/2610.04344) | [papers.cool](https://papers.cool/arxiv/2610.04344)
- Authors: Qi Yu, Ruizhong Qiu, Zhichen Zeng, Xuying Ning, Yanjun Zhao, Dongqi Fu, et al. (9 authors)
- Published: 2026-10-03 07:11 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has been shown to improve the reasoning capability of large language models (LLMs) across diverse reasoning tasks. However, group-based RLVR methods, such as GRPO, assign a uniform advantage to all tokens within rollouts of the same outcome. While existing works...

### 43 - MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution for Medical VQA Tasks

- arXiv: [2610.06695](https://arxiv.org/abs/2610.06695) | [PDF](https://arxiv.org/pdf/2610.06695) | [papers.cool](https://papers.cool/arxiv/2610.06695)
- Authors: Jiuheng Wan, Runze Li, Chen Chen, Tingyuan Hu, Daiyang Yu, Yimin Jing, et al. (8 authors)
- Published: 2026-10-05 16:55 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent, agent collaboration; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: While medical multimodal large language models (Med-MLLMs) advance medical visual question answering (VQA), existing clinical workflow-inspired multi-agent frameworks suffer from interaction patterns and excessive computational overhead caused by redundant communication topologies. In this paper, we propose...

### 43 - LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches

- arXiv: [2610.06647](https://arxiv.org/abs/2610.06647) | [PDF](https://arxiv.org/pdf/2610.06647) | [papers.cool](https://papers.cool/arxiv/2610.06647)
- Authors: Shaokun Zhang, Yifan Zhang, Jian Hu, Yueying Li, Hao Zhang, Binfeng Xu, et al. (8 authors)
- Published: 2026-10-05 16:28 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Reinforcement learning (RL) has greatly advanced the capabilities of large language models (LLMs), but its memory demands remain a barrier to broader adoption. We introduce LoGRA, an approach to RL post-training that reduces memory by retaining useful learning signals in low-rank gradient sketches. These compact...

### 43 - ImproveAnyTask: An Autonomous Post-Training Harness for Iterative Model Self-Improvement

- arXiv: [2610.06347](https://arxiv.org/abs/2610.06347) | [PDF](https://arxiv.org/pdf/2610.06347) | [papers.cool](https://papers.cool/arxiv/2610.06347)
- Authors: Xingbo Yao, Xiaoman Wang, Zhengwu Lei, Tinghui Luo, YiLin Zhang, Yuefeng Wu, et al. (14 authors)
- Published: 2026-10-05 13:48 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement; memory_and_benchmarks: evaluation
- Abstract skim: Adapting general-purpose large language models to specific tasks requires substantial human effort in designing data and training strategies. Sustaining improvement is especially challenging because model updates change the error distribution, requiring strategies to be continually refined. We introduce...

### 43 - Sibyl: An Efficient Small-large Model Collaboration Framework for Long-horizon Tasks

- arXiv: [2610.05383](https://arxiv.org/abs/2610.05383) | [PDF](https://arxiv.org/pdf/2610.05383) | [papers.cool](https://papers.cool/arxiv/2610.05383)
- Authors: Zhewei Fang, Yuxin Zhang, Zhenwei Shao, Mengze Li, Zheng Lin, Long Chen, et al. (11 authors)
- Published: 2026-10-04 17:14 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning, trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Small language models (SLMs) offer a promising foundation for on-device agents through low-latency, resource-efficient inference, yet limited reasoning and planning capabilities constrain their performance on long-horizon tasks requiring multi-step interaction with the environment. Step-level collaboration between...

### 42 - MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents

- arXiv: [2610.06830](https://arxiv.org/abs/2610.06830) | [PDF](https://arxiv.org/pdf/2610.06830) | [papers.cool](https://papers.cool/arxiv/2610.06830)
- Authors: Haozhen Zhang, Haodong Yue, Quanyu Long, Jianzhu Bao, Qingyuan Liu, Tao Feng, et al. (9 authors)
- Published: 2026-10-05 17:58 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: llm agent, agent memory; rl_post_training: reinforcement learning; memory_and_benchmarks: memory
- Abstract skim: Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies...

### 42 - Dynamic Minimax Regret Optimization for Robust LLM Post-Training

- arXiv: [2610.06329](https://arxiv.org/abs/2610.06329) | [PDF](https://arxiv.org/pdf/2610.06329) | [papers.cool](https://papers.cool/arxiv/2610.06329)
- Authors: Chengbo Zang, Haoyu Dong, Mehmet Kerem Turkcan, Gil Zussman, Zoran Kostic, Javad Ghaderi
- Published: 2026-10-05 13:39 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, preference optimization; memory_and_benchmarks: evaluation
- Abstract skim: Modern LLM training increasingly relies on heterogeneous data sources spanning different domains, tasks, preference distributions, and difficulty levels. We study dynamic minimax regret for group-distributionally robust LLM post-training under instantaneous mini-batch-only bandit feedback. The framework views the...

### 42 - Reinforcement Learning on the Discrete Composition Channel of a Crystal Generator: Validated Gains and Reward Hacking

- arXiv: [2610.03880](https://arxiv.org/abs/2610.03880) | [PDF](https://arxiv.org/pdf/2610.03880) | [papers.cool](https://papers.cool/arxiv/2610.03880)
- Authors: Pawan Prakash, Philipp Höllmer, Addis Fuhr, Peter Hirschfeld, P. Ganesh, Stefano Martiniani, et al. (7 authors)
- Published: 2026-10-02 18:02 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; memory_and_benchmarks: benchmark
- Abstract skim: Inverse materials design is a long-standing goal of computational materials discovery. Generative models for crystalline materials are typically trained to match the distribution of a structure database, while nothing in their training objective points them at specific design goals such as targeted properties. We...

### 40 - Residual Visual Credit Optimization: Conserved Evidence Routing for Multimodal Reinforcement Learning

- arXiv: [2610.04918](https://arxiv.org/abs/2610.04918) | [PDF](https://arxiv.org/pdf/2610.04918) | [papers.cool](https://papers.cool/arxiv/2610.04918)
- Authors: Lin Qiu, Yao Liu, Diyi Hu, Hanqing Zeng, Onur Gungor, Chujie Chen, et al. (9 authors)
- Published: 2026-10-04 03:56 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning, outcome reward; planning_and_action: trajectory
- Abstract skim: Reinforcement learning with verifiable rewards scales multimodal reasoning, but an outcome reward says how much a trajectory is worth, not how that value should be spread over the decisions that produced it. We introduce Residual Visual Credit Optimization (RVCO), which treats token credit as a conserved routing...

### 40 - MASBench: Benchmarking LLM-based Multi-Agent Collaboration under Partial Observability

- arXiv: [2610.04672](https://arxiv.org/abs/2610.04672) | [PDF](https://arxiv.org/pdf/2610.04672) | [papers.cool](https://papers.cool/arxiv/2610.04672)
- Authors: Qizhi Chu, Zekai Yu, Sijie Wen, Yang Liu, Chen Qian, Cheng Yang, et al. (8 authors)
- Published: 2026-10-03 17:40 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent collaboration; reasoning: reasoning; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: Large language models (LLMs) have progressively evolved into the core of autonomous agents. Building on this progress, LLM-based multi-agent systems (MAS) coordinate multiple agents into a synergistic team to accomplish complex tasks that exceed the capabilities of individual agents. The effectiveness of such...

### 40 - PB-GRPO: Learning Socially Adaptive LLM Agents from Persona-Driven Simulation with Preference-Batched GRPO

- arXiv: [2610.04132](https://arxiv.org/abs/2610.04132) | [PDF](https://arxiv.org/pdf/2610.04132) | [papers.cool](https://papers.cool/arxiv/2610.04132)
- Authors: Jingquan Wang, Jun Yin, Xu Han, Yongsheng Mei, Jie Hao, Bin Guo
- Published: 2026-10-02 23:07 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo
- Abstract skim: Building LLMs that behave well socially, not merely correctly, requires Building LLMs that behave well socially, not merely correctly, requires more than producing locally helpful responses. A socially competent agent must infer users' unstated goals, respect their preferences, and adapt as the conversation unfolds....

### 40 - Pareto-Dominant Clarification: Post-Training Coding LLMs via PPO-Lagrangian Budget Constraints

- arXiv: [2610.04089](https://arxiv.org/abs/2610.04089) | [PDF](https://arxiv.org/pdf/2610.04089) | [papers.cool](https://papers.cool/arxiv/2610.04089)
- Authors: Abhinav Rajput, Acey Vogelstein
- Published: 2026-10-02 21:54 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, ppo
- Abstract skim: Coding agents operating under ambiguous instructions or user prompts must decide whether to ask clarifying questions or attempt a solution directly. While clarification from the user may improve the correctness of the agent's solution, each back-and-forth interaction incurs user and system costs, forming an explicit...

### 38 - Bidirectional Preference Synthesis: Learning Prompt-Conditioned Preferences from Boundary Failures

- arXiv: [2610.04328](https://arxiv.org/abs/2610.04328) | [PDF](https://arxiv.org/pdf/2610.04328) | [papers.cool](https://papers.cool/arxiv/2610.04328)
- Authors: Junbo Wang, Lidong Lu, Zhuoqun Li, Guiping Jiang, Xiangyu Wu, Tinghai Zhang, et al. (7 authors)
- Published: 2026-10-03 06:48 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: preference optimization, reward model, dpo
- Abstract skim: Correction-based offline preference pipelines commonly treat model failures only as rejected responses under the original prompt. This supervision is incomplete for boundary failures: responses that violate the given instruction yet coherently satisfy a nearby intent or constraint setting. We introduce Bidirectional...

### 37 - Strategic Multi-Agent Learning for Interpretable Action Valuation of All Players in Football

- arXiv: [2610.05961](https://arxiv.org/abs/2610.05961) | [PDF](https://arxiv.org/pdf/2610.05961) | [papers.cool](https://papers.cool/arxiv/2610.05961)
- Authors: Kenjiro Ide, Taiga Someya, Kohei Kawaguchi, Keisuke Fujii
- Published: 2026-10-05 08:13 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent, autonomous agent; rl_post_training: reinforcement learning; planning_and_action: decision making
- Abstract skim: Valuing player actions in football requires accounting for strategic interactions among 22 players, including off-ball movements and defensive positioning. Existing reinforcement-learning-based methods commonly aggregate decisions at the team level or estimate player values independently, leaving strategic...

### 35 - Exploration-Preserving Policy Optimization

- arXiv: [2610.04011](https://arxiv.org/abs/2610.04011) | [PDF](https://arxiv.org/pdf/2610.04011) | [papers.cool](https://papers.cool/arxiv/2610.04011)
- Authors: Hangzhan jin, Mohammad Hamdaqa, Doina Precup
- Published: 2026-10-02 20:17 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning with verifiable rewards improves reasoning, while the allocation of learning signal shapes which solutions remain accessible under repeated sampling. Group-relative objectives assign equal advantages to equally rewarded responses, making aggregate credit proportional to sampled mode frequency....

### 34 - GPlaceRL: An Open-Source Graph Reinforcement Learning Framework for Detailed Placement

- arXiv: [2610.06489](https://arxiv.org/abs/2610.06489) | [PDF](https://arxiv.org/pdf/2610.06489) | [papers.cool](https://papers.cool/arxiv/2610.06489)
- Authors: Pavlos Stoikos, Foteini Oikonomou, Christos Poulos, Maria Pantazi-Kypriou, Athanasios Tziouvaras, Christos Anagnostopoulos, et al. (8 authors)
- Published: 2026-10-05 15:12 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) has emerged as a promising approach for placement optimization, particularly when combined with graph neural networks (GNNs) that capture circuit connectivity. However, most learning-based placement approaches focus on floorplanning, macro placement, or global placement, while detailed...

### 34 - OceanMind: A multi-agent AI system for ocean diagnosis

- arXiv: [2610.03780](https://arxiv.org/abs/2610.03780) | [PDF](https://arxiv.org/pdf/2610.03780) | [papers.cool](https://papers.cool/arxiv/2610.03780)
- Authors: Fan Zhang, Weicong Cheng, Yuheng Chen, Hiuseut Kung, Ying Zhang, Aixi Han, et al. (9 authors)
- Published: 2026-09-30 06:51 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, multi-agent; reasoning: reflection; planning_and_action: planning, decision making; memory_and_benchmarks: benchmark
- Abstract skim: Time-dependent, three-dimensional (3D) oceanic multi-variables define coherent states of the evolving ocean to facilitate ocean diagnosis and advance ocean science to better inform environmental and hazard management. However, extracting quantitative evidence from these variables requires substantial and complex...

### 33 - Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision

- arXiv: [2610.05151](https://arxiv.org/abs/2610.05151) | [PDF](https://arxiv.org/pdf/2610.05151) | [papers.cool](https://papers.cool/arxiv/2610.05151)
- Authors: Yuzhi Zhang, Xinyu Liu, Yu Zhang
- Published: 2026-10-04 11:54 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement
- Abstract skim: Visuomotor policies can execute familiar tasks yet lack the corrective behavior needed after their own mistakes. We present a framework for recursive self-improvement through local recovery supervision. Each round audits the current policy, generates corrective demonstrations at supported failure states, and uses...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
