# RL / Post-Training / Agentic RL Reading Queue - 2026-11-19

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 470. Minimum score: 8.

## Top Picks

### 49 - Self-Rewarded Reinforcement Learning for Better-Structured Medical Explanations in Small Language Models

- arXiv: [2611.24650](https://arxiv.org/abs/2611.24650) | [PDF](https://arxiv.org/pdf/2611.24650) | [papers.cool](https://papers.cool/arxiv/2611.24650)
- Authors: Prakhar Mishra, Bhavya Yajush Awasthi, Tanuja, Nishant
- Published: 2026-11-18 15:52 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Small language models (SLMs) can run on commodity hardware and support privacy-preserving, on-premises clinical deployment, but their medical explanations are often short and poorly structured compared with large language models. Recent supervised approaches such as Meerkat transfer chain-of-thought reasoning into...

### 45 - QDA: Closed-Loop LLM Quantization Design with Agents

- arXiv: [2611.23388](https://arxiv.org/abs/2611.23388) | [PDF](https://arxiv.org/pdf/2611.23388) | [papers.cool](https://papers.cool/arxiv/2611.23388)
- Authors: Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
- Published: 2026-11-17 19:00 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: llm agent; rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this...

### 44 - Replay, Don't Resample: Off-Policy Consolidation of Long-Horizon RL Experts

- arXiv: [2611.24059](https://arxiv.org/abs/2611.24059) | [PDF](https://arxiv.org/pdf/2611.24059) | [papers.cool](https://papers.cool/arxiv/2611.24059)
- Authors: Zhenrui Yue, Gongxiaohui Chen, Huimin Zeng, Honglei Zhuang, Jiashuo Sun, Zhen Han, et al. (7 authors)
- Published: 2026-11-18 08:51 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Frontier post-training follows a common recipe: train one expert per domain with reinforcement learning (RL), then consolidate the experts into one model via multi-teacher on-policy distillation (MOPD). Such consolidation is expensive: the student samples in every environment again, an expert scores every sampled...

### 40 - Depth Before Breadth: Reverse-to-Forward Curriculum with Advantage Decomposition for LLM Agent

- arXiv: [2611.24697](https://arxiv.org/abs/2611.24697) | [PDF](https://arxiv.org/pdf/2611.24697) | [papers.cool](https://papers.cool/arxiv/2611.24697)
- Authors: Siyuan Du, Yuxin Liu, Meng Tang, Haoran Li, Yechao Bai, Feiyang Pan, et al. (7 authors)
- Published: 2026-11-18 16:25 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl, llm agent; rl_post_training: reinforcement learning; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning (RL) has become a common approach for training large language model (LLM) agents on long-horizon tasks. However, learning from sparse terminal rewards makes credit assignment and exploration difficult. We approach these challenges through a policy-induced capability region, the set of states...

### 40 - Option-GRPO: Hierarchical RL Against AI Slop in Code Generation for Unseen SDKs

- arXiv: [2611.23633](https://arxiv.org/abs/2611.23633) | [PDF](https://arxiv.org/pdf/2611.23633) | [papers.cool](https://papers.cool/arxiv/2611.23633)
- Authors: Prashank Kadam
- Published: 2026-11-17 23:52 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: Large language models increasingly produce AI slop in generated code: verbose, redundant, non-idiomatic implementations that pass functional checks but bloat codebases. The problem compounds on SDKs released after the model's training cutoff, where the model has neither idiomatic priors nor compositional...

### 39 - Cooperative UAV and Ground Station for Robust MEC of Dynamic Aquatic IoT: A Generative AI-Enhanced Approach

- arXiv: [2611.24466](https://arxiv.org/abs/2611.24466) | [PDF](https://arxiv.org/pdf/2611.24466) | [papers.cool](https://papers.cool/arxiv/2611.24466)
- Authors: Jiahao You, Ziye Jia, Chao Dong, Qihui Wu, Zhu Han
- Published: 2026-11-18 14:05 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: The increasing aquatic Internet of Things (AIoTs) require computational support and coverage in applications such as maritime search and rescue. Unmanned aerial vehicles (UAVs) can offer low-cost, flexible aerial services, and ground stations (GSs) can provide powerful supports, which can cooperate to help the AIoTs...

### 38 - CoSlice: Coordinated Multi-Agent Reinforcement Learning for 5G Network Slicing Allocation

- arXiv: [2611.23909](https://arxiv.org/abs/2611.23909) | [PDF](https://arxiv.org/pdf/2611.23909) | [papers.cool](https://papers.cool/arxiv/2611.23909)
- Authors: Pengxin Wang, Nakjung Choi, Jingdi Chen
- Published: 2026-11-18 06:00 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: evaluation; downranked: traffic
- Abstract skim: Radio Access Network (RAN) slicing is a shared resource allocation problem: each slice seeks to satisfy its Service Level Agreement (SLA) with minimal radio-resource consumption, while all slices compete for a limited resource budget. This creates both an intra-slice trade-off between SLA assurance and resource...

### 35 - A Survey on RLOps for Large Language Models

- arXiv: [2611.23357](https://arxiv.org/abs/2611.23357) | [PDF](https://arxiv.org/pdf/2611.23357) | [papers.cool](https://papers.cool/arxiv/2611.23357)
- Authors: Lingzhe Zhang, Tong Jia, Chiming Duan, Minghua He, Leyi Pan, Kening Zheng, et al. (10 authors)
- Published: 2026-11-17 14:15 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) has become increasingly important for improving the reasoning, instruction-following, and task-solving capabilities of large language models (LLMs). However, scaling RL training exposes failures in distributed execution, feedback computation, and learning dynamics that can waste...

### 30 - CoRA-VTLA: Contact-Guided Attention and Queryable Response Memory for Tactile Post-Training

- arXiv: [2611.23963](https://arxiv.org/abs/2611.23963) | [PDF](https://arxiv.org/pdf/2611.23963) | [papers.cool](https://papers.cool/arxiv/2611.23963)
- Authors: Chengye Song, Rui Song, Shengqi Wang, Jiawei Zhang, Hongzhou Wang, Xueyang Guo, et al. (7 authors)
- Published: 2026-11-18 06:57 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: memory, benchmark
- Abstract skim: In precision manipulation, small errors in alignment or force can cause jamming or deformation, making contact feedback essential for adapting pretrained vision-language-action (VLA) models to these tasks. A single tactile observation leaves the response to recent actions ambiguous. Direct tactile fusion during...

### 30 - EVA-RSI: Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality

- arXiv: [2611.23890](https://arxiv.org/abs/2611.23890) | [PDF](https://arxiv.org/pdf/2611.23890) | [papers.cool](https://papers.cool/arxiv/2611.23890)
- Authors: Yu Yuan, Ruizhou Ding, Shaoheng Fang, Stanley H. Chan, Zhuo Chen
- Published: 2026-11-18 05:41 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, multi-agent; reasoning: self-improvement, self improvement; memory_and_benchmarks: evaluation
- Abstract skim: Video evaluators play an important role in video generation, yet they miss motion defects, limiting the quality of generated videos. Recursive self-improvement (RSI) has made strong progress in mathematics and coding, where explicit verifiers provide reliable feedback on a single goal. Video evaluation poses two...

### 30 - Evidence-Based Credit Assignment for Search-Augmented Language Models

- arXiv: [2611.23824](https://arxiv.org/abs/2611.23824) | [PDF](https://arxiv.org/pdf/2611.23824) | [papers.cool](https://papers.cool/arxiv/2611.23824)
- Authors: Wen Wang, Jindong Wang, Jiahua Bao, Tu Yongsiqi, Yihao Liu, Junwei He, et al. (7 authors)
- Published: 2026-11-18 04:24 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every search in a trajectory regardless of whether it retrieved useful information. This limitation is...

### 27 - HINT-WAM: Hindsight-Informed Training for World Action Models

- arXiv: [2611.24789](https://arxiv.org/abs/2611.24789) | [PDF](https://arxiv.org/pdf/2611.24789) | [papers.cool](https://papers.cool/arxiv/2611.24789)
- Authors: Phuong Tuan Dat, Qi Li, Xinchao Wang
- Published: 2026-11-18 17:36 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: trajectory
- Abstract skim: World action models (WAMs) have shown promising generalization and data efficiency in robot manipulation by coupling action generation with predictions of future visual dynamics. Translating these capabilities into reliable task execution, however, remains a challenge for existing post-training methods. Offline...

### 26 - Beyond Corpus-Driven Imitation: Evolving Musical Mindsets in the Agentic Orchestra via Quantum Reinforcement Learning

- arXiv: [2611.24290](https://arxiv.org/abs/2611.24290) | [PDF](https://arxiv.org/pdf/2611.24290) | [papers.cool](https://papers.cool/arxiv/2611.24290)
- Authors: Eduardo Reck Miranda, Moein Fahmideh Vatandoost
- Published: 2026-11-18 12:03 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: quantum
- Abstract skim: This paper presents a framework for computer-aided music composition and performance based on quantum reinforcement learning and multi-agent interaction. We introduce the agentic orchestra, where musical agents evolve distinct mindsets through trial-and-error engagement with a musical environment, rather than...

### 26 - CommDreamer: Radio-Geometric World Models for Mapless Cellular-Connected UAV Trajectory Planning

- arXiv: [2611.24244](https://arxiv.org/abs/2611.24244) | [PDF](https://arxiv.org/pdf/2611.24244) | [papers.cool](https://papers.cool/arxiv/2611.24244)
- Authors: Yuqi Ping, Tianhao Liang, Tingting Zhang
- Published: 2026-11-18 11:22 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, trajectory, world model
- Abstract skim: Reliable cellular connectivity and collision-free flight are essential for unmanned aerial vehicle (UAV) operations in low-altitude urban canyons, where dense 3D buildings obstruct flight clearance, shadow serving base stations, and create strong co-channel interference at street intersections. Existing planners...

### 26 - Improve How You Improve: Recursive Policy Self-Improvement for Zero-Shot Open-Vocabulary Multi-Object Navigation

- arXiv: [2611.23774](https://arxiv.org/abs/2611.23774) | [PDF](https://arxiv.org/pdf/2611.23774) | [papers.cool](https://papers.cool/arxiv/2611.23774)
- Authors: Yang Li, Ziju Han, Aming WU, Zihao Zhang, Sijia Zhang, Yahong Han, et al. (7 authors)
- Published: 2026-11-18 03:31 UTC | Categories: cs.RO
- Why it matched: reasoning: self-improvement, self improvement, reflection; planning_and_action: planning, trajectory; memory_and_benchmarks: memory, benchmark
- Abstract skim: To advance the development of embodied general navigation, zero-shot open-vocabulary multi-object navigation has attracted increasing attention, aiming to enable robots to efficiently search multiple objects in unseen environments without training. For this task, the key lies in improving navigation policies from...

### 22 - GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance

- arXiv: [2611.23476](https://arxiv.org/abs/2611.23476) | [PDF](https://arxiv.org/pdf/2611.23476) | [papers.cool](https://papers.cool/arxiv/2611.23476)
- Authors: Minghe Zhang, Xuetao Kang, Yifei Ming, Yanfei Chen, Han Yu, Yufan Zhuang, et al. (7 authors)
- Published: 2026-11-17 20:26 UTC | Categories: cs.AI, cs.LG
- Why it matched: reasoning: reasoning, self-improvement, self improvement, reflection; memory_and_benchmarks: memory
- Abstract skim: Autonomous AI agents pair a frozen base model with an editable harness of prompts, skills, tool rules, and memory. Recursive self-improvement (RSI) adapts this harness from experience without weight updates, yet self-editing without external graders often backfires: reflection and scalar scores conflate what an edit...

### 22 - Tracking Representations in LLM Reasoning Traces for Iterated Games

- arXiv: [2611.23403](https://arxiv.org/abs/2611.23403) | [PDF](https://arxiv.org/pdf/2611.23403) | [papers.cool](https://papers.cool/arxiv/2611.23403)
- Authors: Chaipat Tirapongprasert, Rajarshi Das, Parijat Dube
- Published: 2026-11-17 19:03 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Large language model (LLM) agents achieve state-of-the-art performance across domains through chain-of-thought (CoT) reasoning. Despite their ubiquitous use, little is understood about the relationship between the externalized trace and the model's actual computation. We address this by investigating how LLM agents...

### 21 - A Comparison of Heuristic, Human-Sensitive, and Self-Play DRL Policies in Human-Agent Teaming

- arXiv: [2611.23747](https://arxiv.org/abs/2611.23747) | [PDF](https://arxiv.org/pdf/2611.23747) | [papers.cool](https://papers.cool/arxiv/2611.23747)
- Authors: Ayman bin Kamruddin, Christopher Lam, Gaurav Patil, Mirco Musolesi, Mario di Bernardo, Michael J. Richardson
- Published: 2026-11-18 02:59 UTC | Categories: cs.MA
- Why it matched: rl_post_training: reinforcement learning; reasoning: self-play
- Abstract skim: Dynamical Perceptual-Motor Primitives (DPMPs) offer a tractable framework for generating human-like movement dynamics in artificial agents (AAs) and have been used to support coordination in human-AI teaming tasks. Traditionally, DPMP controllers rely on heuristic (rule-based) decision policies derived from human...

### 20 - Resolution as Attention for Efficient Agent Memory Perception

- arXiv: [2611.24422](https://arxiv.org/abs/2611.24422) | [PDF](https://arxiv.org/pdf/2611.24422) | [papers.cool](https://papers.cool/arxiv/2611.24422)
- Authors: Siqi Xiang, Zhipeng Xu, Shengrui Liu, Zulong Chen, Chunyan Miao, Shijian Lu
- Published: 2026-11-18 13:43 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory
- Abstract skim: LLM-based agents accumulate extensive interaction histories when solving complex, long-horizon tasks, making efficient memory management critical to their performance and scalability. While existing memory management methods primarily focus on what to retain or retrieve, they often overlook how much perceptual...

### 19 - Efficient Variance-Aware Reinforcement Learning in Time-Inhomogeneous Linear MDPs

- arXiv: [2611.23596](https://arxiv.org/abs/2611.23596) | [PDF](https://arxiv.org/pdf/2611.23596) | [papers.cool](https://papers.cool/arxiv/2611.23596)
- Authors: Qingyue Zhao, Qiwei Di, Jiafan He, Heyang Zhao, Kaixuan Ji, Quanquan Gu
- Published: 2026-11-17 22:51 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: trajectory
- Abstract skim: We study variance-dependent reinforcement learning in episodic time-inhomogeneous linear Markov decision processes (MDPs) with feature dimension $d$, horizon $H$, and $K$ episodes. While recent works have established variance-dependent regret with $\tilde{O}(1)$ deterministic-regime overhead for linear mixture MDPs...

### 19 - Receiver-Conditioned Clarification for Multi-Agent Food Assistance

- arXiv: [2611.23572](https://arxiv.org/abs/2611.23572) | [PDF](https://arxiv.org/pdf/2611.23572) | [papers.cool](https://papers.cool/arxiv/2611.23572)
- Authors: Kaiwen Shi, Zheyuan Zhang, Changzhi Liu, Han Bao, Yanfang Ye
- Published: 2026-11-17 22:16 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: planning
- Abstract skim: Food insecurity creates a pressing need for guidance that helps households find usable food resources and assess food choices in light of their circumstances. Such guidance must connect eligibility requirements, practical access constraints, and dietary needs rather than return isolated listings or generic...

### 18 - Phoenix: Learning Scene Structure Representations for Generalizable World-Action Models

- arXiv: [2611.24938](https://arxiv.org/abs/2611.24938) | [PDF](https://arxiv.org/pdf/2611.24938) | [papers.cool](https://papers.cool/arxiv/2611.24938)
- Authors: Yupeng Zheng, Chaoyue Li, Linbo Wang, Xiang Li, Yuhang Zheng, Xiaotong Su, et al. (18 authors)
- Published: 2026-11-18 18:59 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: benchmark
- Abstract skim: World-action models jointly predict future observations and actions, yet reconstruction-oriented visual representations do not explicitly emphasize the spatial relationships and object-state changes needed for manipulation. We introduce Phoenix, which learns representations of scene structure for world-action...

### 18 - Kaer: Security-Aware Replanning for Multi-Agent Systems

- arXiv: [2611.24839](https://arxiv.org/abs/2611.24839) | [PDF](https://arxiv.org/pdf/2611.24839) | [papers.cool](https://papers.cool/arxiv/2611.24839)
- Authors: Tushin Mallick, Evan Rose, Matthew Laws, Alina Oprea, Cristina Nita-Rotaru
- Published: 2026-11-18 18:05 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: benchmark
- Abstract skim: One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces a critical vulnerability: malicious...

### 18 - Isabelle Pool Server: a pooled verification service for prover training and multi-agent proving

- arXiv: [2611.24788](https://arxiv.org/abs/2611.24788) | [PDF](https://arxiv.org/pdf/2611.24788) | [papers.cool](https://papers.cool/arxiv/2611.24788)
- Authors: Xuanwei Ren, Wenda Li
- Published: 2026-11-18 17:35 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: memory
- Abstract skim: Isabelle Pool Server (IPS), a verification service with a pool of warm headless Isabelle sessions behind an HTTP API, with session leasing and reclamation, memory-aware admission control, and a time budget on every call. Its verification interface spans single-step execution, block-level proof checking and whole-...

### 18 - Asymmetric Decomposition for Multi-Agent Path Finding with Unassigned Agents

- arXiv: [2611.24108](https://arxiv.org/abs/2611.24108) | [PDF](https://arxiv.org/pdf/2611.24108) | [papers.cool](https://papers.cool/arxiv/2611.24108)
- Authors: Xi Jin, Chen Qian, Renjun Zhang, Guowei Wu, Xiaobo Li, Jun Jiang, et al. (7 authors)
- Published: 2026-11-18 09:26 UTC | Categories: cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: benchmark
- Abstract skim: Robots without assigned tasks may obstruct active robots, while routing them to designated parking locations can cause unnecessary travel. This article proposes flow-oracle conflict-based search (FOCBS) for Multi-Agent Path Finding with unassigned agents (MAPF-UA). FOCBS searches over assigned-agent paths using...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
