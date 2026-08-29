# RL / Post-Training / Agentic RL Reading Queue - 2026-08-29

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 362. Minimum score: 8.

## Top Picks

### 88 - Performance Foundations of Parallel & Distributed Reasoning Language Models

- arXiv: [2608.27046](https://arxiv.org/abs/2608.27046) | [PDF](https://arxiv.org/pdf/2608.27046) | [papers.cool](https://papers.cool/arxiv/2608.27046)
- Authors: Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, et al. (10 authors)
- Published: 2026-08-27 12:33 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +4 more; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: planning
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training ("RL-...

### 63 - Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO

- arXiv: [2608.27351](https://arxiv.org/abs/2608.27351) | [PDF](https://arxiv.org/pdf/2608.27351) | [papers.cool](https://papers.cool/arxiv/2608.27351)
- Authors: Yunpeng Ba, Zhi Zheng, Yue Xie, Jiaqing Li, Xialiang Tong, Tao Zhong, et al. (10 authors)
- Published: 2026-08-27 16:48 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define its advantage scope compared to mainstream post-training paradigms (e.g., Group Relative Policy Optimization (GRPO))....

### 53 - One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles

- arXiv: [2608.27338](https://arxiv.org/abs/2608.27338) | [PDF](https://arxiv.org/pdf/2608.27338) | [papers.cool](https://papers.cool/arxiv/2608.27338)
- Authors: Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu, Ying Chen, et al. (10 authors)
- Published: 2026-08-27 16:40 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training, grpo; reasoning: reasoning
- Abstract skim: Specializing Large Language Models (LLMs) toward distinct abilities underpins successes ranging from personalized assistants to multi-agent systems (MAS). Single-agent paradigms rely on pre-defined personas or steering vectors to induce specialization, yet they impose a single fixed specialization that fails to...

### 53 - GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL

- arXiv: [2608.27142](https://arxiv.org/abs/2608.27142) | [PDF](https://arxiv.org/pdf/2608.27142) | [papers.cool](https://papers.cool/arxiv/2608.27142)
- Authors: Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke, Huozhi Zhou, et al. (13 authors)
- Published: 2026-08-27 13:53 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl, multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often...

### 49 - TTPO: Test-Time Policy Optimization

- arXiv: [2608.27448](https://arxiv.org/abs/2608.27448) | [PDF](https://arxiv.org/pdf/2608.27448) | [papers.cool](https://papers.cool/arxiv/2608.27448)
- Authors: Aozhe Wang, Zhengxi Lu, Jianze Wang, Shangke Lv, Ying Liu, Weiming Lu, et al. (11 authors)
- Published: 2026-08-27 17:58 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: Recent prominent post-training methods, such as Reinforcement Learning (RL) and On-Policy Self-Distillation (OPSD), have driven rapid progress in mathematical reasoning for large language models, yet their reliance on ground-truth labels precludes test-time training (TTT). Replacing ground truth with majority-vote...

### 42 - SpeechGym: An Audio-Native Gym for Training Voice Agents via Reinforcement Learning

- arXiv: [2608.26432](https://arxiv.org/abs/2608.26432) | [PDF](https://arxiv.org/pdf/2608.26432) | [papers.cool](https://papers.cool/arxiv/2608.26432)
- Authors: Jiajun Fan, Jingyuan Li, Prashanth Gurunath Shivakumar, Jia-Hong Huang, Qi Luo, M. Maruf, et al. (9 authors)
- Published: 2026-08-26 22:16 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning, process reward; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: Voice agents must call tools and hold multi-turn dialogue entirely through speech, yet the dominant paradigm trains them in text. Existing frameworks either cascade TTS and ASR around a proprietary voice API, where gradients cannot flow and per-call cost makes on-policy reinforcement learning prohibitive, or stay in...

### 40 - Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training

- arXiv: [2608.26730](https://arxiv.org/abs/2608.26730) | [PDF](https://arxiv.org/pdf/2608.26730) | [papers.cool](https://papers.cool/arxiv/2608.26730)
- Authors: Tingyun Li, Wenfeng Feng, Weiqing Li, Abudukelimu Wuerkaixi, Guohua Liu, Yuewei Zhang
- Published: 2026-08-27 07:22 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: memory, evaluation
- Abstract skim: Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals. As evidence...

### 37 - Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation

- arXiv: [2608.27158](https://arxiv.org/abs/2608.27158) | [PDF](https://arxiv.org/pdf/2608.27158) | [papers.cool](https://papers.cool/arxiv/2608.27158)
- Authors: Wendong Li, Jochen Garcke
- Published: 2026-08-27 14:10 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; planning_and_action: planning, decision making; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Robot crowd navigation requires safe and efficient decision-making under dense, dynamic, and multimodal human--robot interactions. Existing reinforcement-learning methods typically output a single reactive action at each timestep, which limits their ability to represent diverse short-term avoidance strategies. We...

### 36 - MemToC: Benchmarking Memory-Tool Conflict Resolution in Large Language Models

- arXiv: [2608.26295](https://arxiv.org/abs/2608.26295) | [PDF](https://arxiv.org/pdf/2608.26295) | [papers.cool](https://papers.cool/arxiv/2608.26295)
- Authors: Arseniy Varlamov, Rishat Zinnatullin, Elisei Rykov, Alexander Panchenko, Ilseyar Alimova
- Published: 2026-08-26 18:22 UTC | Categories: cs.AI, cs.CL, cs.MA
- Why it matched: agentic_rl: tool use; rl_post_training: dpo; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: Tool-augmented LLMs must arbitrate between two fallible sources when a tool return conflicts with their parametric memory, yet existing evaluations measure source preference without establishing source correctness. We introduce MemToC, a controlled benchmark for post-tool-return arbitration with executable tools....

### 35 - SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in Reinforcement Learning

- arXiv: [2608.26550](https://arxiv.org/abs/2608.26550) | [PDF](https://arxiv.org/pdf/2608.26550) | [papers.cool](https://papers.cool/arxiv/2608.26550)
- Authors: Zhuochun Li, Yuelyu Ji, Yiming Zeng, Daqing He
- Published: 2026-08-27 02:41 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, process reward; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning-based knowledge distillation has the potential to transfer complex reasoning from teacher to student models, yet it currently faces a critical dilemma: researchers must choose between sparse outcome-based rewards, which provide insufficient logical guidance, or expensive neural Process Reward...

### 33 - Boosting LLM Exploration via Weak-Model Guidance in RLVR

- arXiv: [2608.27420](https://arxiv.org/abs/2608.27420) | [PDF](https://arxiv.org/pdf/2608.27420) | [papers.cool](https://papers.cool/arxiv/2608.27420)
- Authors: Xingyu Shen, Huishuai Zhang, Peng Li, Yinchun Wang, Dongyan Zhao
- Published: 2026-08-27 17:45 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) significantly improves LLM reasoning but often causes a drop in policy entropy, leading to narrowed reasoning coverage and degraded pass@$k$ for large $k$. While existing methods mitigate this entropy collapse through algorithmic regularizations, cross-model non-...

### 33 - PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents

- arXiv: [2608.26530](https://arxiv.org/abs/2608.26530) | [PDF](https://arxiv.org/pdf/2608.26530) | [papers.cool](https://papers.cool/arxiv/2608.26530)
- Authors: Yang Xiao, Yusong Sun, Haoyi Wu, Wenyang Hui, Wen Da, Zhaokai Luo, et al. (10 authors)
- Published: 2026-08-27 02:06 UTC | Categories: cs.AI
- Why it matched: agentic_rl: long-horizon agent; reasoning: self-improvement, self improvement; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Long-horizon agent runs generate experience that can improve both the current run and future work. Most self-improvement methods process this experience only after execution ends, so they cannot redirect the active run or immediately apply and validate lessons learned from it. We argue that self-improvement should...

### 31 - SIGMA: Structured Noise-Effect-Aware Grouped Multi-Agent Aggregation

- arXiv: [2608.26683](https://arxiv.org/abs/2608.26683) | [PDF](https://arxiv.org/pdf/2608.26683) | [papers.cool](https://papers.cool/arxiv/2608.26683)
- Authors: Li Mingqian
- Published: 2026-08-27 06:40 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: decision making
- Abstract skim: Cooperative multi-agent reinforcement learning (MARL) faces significant challenges in maintaining robust coordination under noisy observations. Although observation disturbances are often introduced independently across agents, their downstream effects on cooperative decision-making can become structured through...

### 29 - AffectOmni: RL-Verifiable People-Centric Grounded Affective Reasoning for Social and Art-Related Scenes

- arXiv: [2608.26193](https://arxiv.org/abs/2608.26193) | [PDF](https://arxiv.org/pdf/2608.26193) | [papers.cool](https://papers.cool/arxiv/2608.26193)
- Authors: Yibo Wang, Rui Yang, Jisheng Dang, Bimei Wang, Yitao Wu, Pengfei Cao, et al. (10 authors)
- Published: 2026-08-24 11:25 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Multimodal large language models (MLLMs) achieve strong performance on VQA and scene understanding, yet affective reasoning remains vulnerable to shortcut behavior. Models may predict correct answers while neglecting people-centric cues such as micro expressions and body language, which weakens traceability and...

### 28 - Naive Prompt Optimization: Rethinking the Need for Complex Prompt Search

- arXiv: [2608.27266](https://arxiv.org/abs/2608.27266) | [PDF](https://arxiv.org/pdf/2608.27266) | [papers.cool](https://papers.cool/arxiv/2608.27266)
- Authors: Yuan Chang, Xiaoqi Chen
- Published: 2026-08-27 15:47 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: grpo; reasoning: reasoning, self-improvement, self improvement; planning_and_action: rollout
- Abstract skim: Efficiently improving autonomous agents across diverse tasks is central to accelerating recursive self-improvement (RSI) in agentic AI, with prompt optimization emerging as a promising approach capable of delivering performance gains comparable to those achieved by fine-tuning model weights, while reducing...

### 27 - Don't Overthink, Don't Underthink: Toward Adaptive Reasoning in Agentic AI

- arXiv: [2608.26442](https://arxiv.org/abs/2608.26442) | [PDF](https://arxiv.org/pdf/2608.26442) | [papers.cool](https://papers.cool/arxiv/2608.26442)
- Authors: Md Jueal Mia, M. Hadi Amini
- Published: 2026-08-26 22:45 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: memory, benchmark, gaia
- Abstract skim: Recent advances in Large Language Models (LLMs) have shown that increased inference-time reasoning can improve performance on complex tasks. However, many existing approaches rely on fixed or preallocated reasoning controls, such as fixed token budgets, pre-execution difficulty estimates, or activation-space...

### 26 - Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms

- arXiv: [2608.27409](https://arxiv.org/abs/2608.27409) | [PDF](https://arxiv.org/pdf/2608.27409) | [papers.cool](https://papers.cool/arxiv/2608.27409)
- Authors: Siye Wu, Kai Yang, Yuchen Cai, Xin Xu, Peng-Yuan Wang, Jiaxuan Wang, et al. (11 authors)
- Published: 2026-08-27 17:38 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) improves specific capabilities of large language models, but covering multiple capabilities often involves training separate domain experts and subsequently consolidating them. We organize three fusion paradigms by the artefacts they reuse: Merge combines expert...

### 25 - Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper

- arXiv: [2608.26596](https://arxiv.org/abs/2608.26596) | [PDF](https://arxiv.org/pdf/2608.26596) | [papers.cool](https://papers.cool/arxiv/2608.26596)
- Authors: Rongjin Li, Yuanxin Liu, Hao Zhou, Fandong Meng, Jie Zhou, Xu Sun
- Published: 2026-08-27 04:24 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Multimodal large language models (MLLMs) are increasingly capable scientific assistants, yet they remain far from fully autonomous research. This transition requires models to actively inspect academic papers, build global evidence views, and make traceable judgments without prespecified issues or evidence. However,...

### 24 - Circuit Condensation: Post-Training that Concentrates a Behavior's Causal Circuit

- arXiv: [2608.27254](https://arxiv.org/abs/2608.27254) | [PDF](https://arxiv.org/pdf/2608.27254) | [papers.cool](https://papers.cool/arxiv/2608.27254)
- Authors: Sai Adith Senthil Kumar
- Published: 2026-08-27 15:38 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training
- Abstract skim: One approach to mechanistic interpretability explains behavior through circuits: the components and connections that carry it. Frozen discovery often returns hundreds of edges, making them hard to inspect, compare, or verify exhaustively. We introduce Circuit Condensation, which post-trains models to concentrate...

### 24 - Disentangling Optimization Scale from Preference Scale in DPO

- arXiv: [2608.27032](https://arxiv.org/abs/2608.27032) | [PDF](https://arxiv.org/pdf/2608.27032) | [papers.cool](https://papers.cool/arxiv/2608.27032)
- Authors: Ivan Kruzhilov
- Published: 2026-08-27 12:21 UTC | Categories: cs.LG
- Why it matched: rl_post_training: preference optimization, dpo
- Abstract skim: Direct Preference Optimization (DPO) is a widely used objective for aligning language models from preference data, with the coefficient $β$ commonly interpreted as controlling the KL constraint to a reference policy. We show that $β$ entangles two distinct roles: it governs the effective inverse preference-noise...

### 24 - Reinforcement Learning-Based Control of CAV Platoon Joining Maneuvers in Mixed Traffic

- arXiv: [2608.26860](https://arxiv.org/abs/2608.26860) | [PDF](https://arxiv.org/pdf/2608.26860) | [papers.cool](https://papers.cool/arxiv/2608.26860)
- Authors: Biao Yin, Abderrahmane Kasmi, Nadir Farhi
- Published: 2026-08-27 09:27 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; downranked: traffic, driving
- Abstract skim: Connected and automated vehicle (CAV) platooning offers a promising approach to improving road safety and traffic capacity. However, platoon control in real-world traffic is challenging due to uncertainty and heterogeneous driving behaviors. Reinforcement learning (RL) has strong potential for addressing such...

### 24 - Behavior2Trip: Towards Personalized Travel Planning via User Behavior Trajectory

- arXiv: [2608.26807](https://arxiv.org/abs/2608.26807) | [PDF](https://arxiv.org/pdf/2608.26807) | [papers.cool](https://papers.cool/arxiv/2608.26807)
- Authors: Zihao Cheng, Yingyu Shan, Hongru Wang, Zeming Liu, Xinyi Wang, Xiangrong Zhu, et al. (9 authors)
- Published: 2026-08-27 08:47 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, trajectory; memory_and_benchmarks: memory, benchmark
- Abstract skim: Travel planning agents assist users in generating personalized travel plans by modeling their individual preferences. Existing agents either rely on explicit user instructions or engage in multi-turn clarification to elicit user preferences. However, both approaches overlook the rich behavioral signals latent in...

### 23 - AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design

- arXiv: [2608.26747](https://arxiv.org/abs/2608.26747) | [PDF](https://arxiv.org/pdf/2608.26747) | [papers.cool](https://papers.cool/arxiv/2608.26747)
- Authors: Mingquan Liu, Jiangyu Chen, Hanqun Cao, Xujun Zhang, Pengsen Ma, Xiangru Tang, et al. (11 authors)
- Published: 2026-08-27 07:38 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, tool use; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: memory, evaluation; downranked: protein
- Abstract skim: Scientific LLM agents have shown promise in literature reasoning, tool use, and experiment planning, but it remains unclear whether they can autonomously improve large, tightly coupled scientific machine-learning systems through executable code changes and computationally expensive validation. We study this question...

### 22 - DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research

- arXiv: [2608.26990](https://arxiv.org/abs/2608.26990) | [PDF](https://arxiv.org/pdf/2608.26990) | [papers.cool](https://papers.cool/arxiv/2608.26990)
- Authors: Linsen Zhu, Yi Shi
- Published: 2026-08-27 11:37 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: llm agent, agent orchestration; reasoning: reasoning
- Abstract skim: Large language models can summarize financial information, but an operational stock-research system must first assemble heterogeneous evidence, expose unavailable data and model capabilities, and control how generated opinions affect a final report. We present DSA, an evidence-aware orchestration framework for...

### 22 - GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory

- arXiv: [2608.26983](https://arxiv.org/abs/2608.26983) | [PDF](https://arxiv.org/pdf/2608.26983) | [papers.cool](https://papers.cool/arxiv/2608.26983)
- Authors: Geng Li, Yuhao Wang, Dong Li, Jianye Hao, Yuxin Peng
- Published: 2026-08-27 11:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory, long-term memory
- Abstract skim: Organizing long-term memory for multimodal agents remains challenging because existing methods either suffer from expensive question-agnostic offline summaries or naive embedding similarity matching that introduces incomplete and redundant context. To address these issues, we propose GraphMemix, a combinatorial-...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
