# RL / Post-Training / Agentic RL Reading Queue - 2026-10-19

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 495. Minimum score: 8.

## Top Picks

### 72 - Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning

- arXiv: [2610.23181](https://arxiv.org/abs/2610.23181) | [PDF](https://arxiv.org/pdf/2610.23181) | [papers.cool](https://papers.cool/arxiv/2610.23181)
- Authors: Heming Zou, Qi Wang, Yixiu Mao, Yun Qu, Yuyi Guo, Zeyuan Liu, et al. (10 authors)
- Published: 2026-10-16 09:17 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: process reward; planning_and_action: rollout
- Abstract skim: Reinforcement learning with verifiable rewards has become a scalable post-training paradigm for large language models. However, training agents over long-horizon interactions presents two challenges: using only terminal rewards makes turn-level credit assignment sparse and high-variance, while sequential mini-batch...

### 54 - AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents

- arXiv: [2610.22684](https://arxiv.org/abs/2610.22684) | [PDF](https://arxiv.org/pdf/2610.22684) | [papers.cool](https://papers.cool/arxiv/2610.22684)
- Authors: Liqin Ye, Rongzhi Zhang, Xin Liu, Zheng Li, Yuan He, Qingyu Yin, et al. (8 authors)
- Published: 2026-10-15 21:54 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: Forecasting an unresolved event requires finding relevant evidence and deciding how strongly it supports each outcome. Yet outcome-based training of Large Language Model (LLM) forecasters often begins with preassembled evidence at a single prediction date, leaving evidence acquisition outside the learning loop. We...

### 52 - RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory

- arXiv: [2610.23598](https://arxiv.org/abs/2610.23598) | [PDF](https://arxiv.org/pdf/2610.23598) | [papers.cool](https://papers.cool/arxiv/2610.23598)
- Authors: Dabin Sheng, Zhe Wu, Jinming Zhao, Junliang Xing, Yuanchun Shi
- Published: 2026-10-16 15:16 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory, long-horizon agent; rl_post_training: reinforcement learning; memory_and_benchmarks: memory, episodic memory, long-term memory
- Abstract skim: Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory. Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates. Even time-aware approaches inject...

### 51 - Rethinking GRPO for Large Reasoning Model Safety Alignment

- arXiv: [2610.23085](https://arxiv.org/abs/2610.23085) | [PDF](https://arxiv.org/pdf/2610.23085) | [papers.cool](https://papers.cool/arxiv/2610.23085)
- Authors: Jiawei Chen, Yi Zhang, Jiawei Du, Zhonghou Lv, Tairan Chen, Junyuan Shang, et al. (12 authors)
- Published: 2026-10-16 07:53 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Large reasoning models (LRMs) exhibit strong reasoning capabilities but remain vulnerable to unsafe outputs. While Group Relative Policy Optimization (GRPO) is widely used for safety alignment, its group-relative optimization may provide insufficient safety-directed learning signals. In this paper, we identify two...

### 47 - Batched Contextual Reinforcement II: Does RLVR Need Long Rollout Windows?

- arXiv: [2610.22887](https://arxiv.org/abs/2610.22887) | [PDF](https://arxiv.org/pdf/2610.22887) | [papers.cool](https://papers.cool/arxiv/2610.22887)
- Authors: Bangji Yang, Hongbo Ma, Ruihan Guo, Jiajun Fan, Xi Zhu, Ge Liu
- Published: 2026-10-16 03:40 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Long rollout windows make reinforcement learning with verifiable rewards (RLVR) expensive, yet simply shortening them can remove the correctness signal: when every single-problem rollout truncates before an answer, group-relative accuracy advantages vanish. As a technical continuation of Batched Contextual...

### 45 - Diverse Reasoning Paths Matter: Symbolic Equivalence Augmentation for Enhancing RL Exploration

- arXiv: [2610.22665](https://arxiv.org/abs/2610.22665) | [PDF](https://arxiv.org/pdf/2610.22665) | [papers.cool](https://papers.cool/arxiv/2610.22665)
- Authors: Xiaoou Liu, Tiejin Chen, Hanyang Chen, Yuan Ling, Hua Wei
- Published: 2026-10-15 21:31 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for improving the reasoning capabilities of LLMs. However, the role of supervised fine-tuning (SFT) data in enabling effective downstream RL remains underexplored. In this paper, we investigate a key hypothesis: the diversity of...

### 44 - Beyond Reward Scoring: Online Multi-Agent Preference Learning for Multimodal Response Generation

- arXiv: [2610.23256](https://arxiv.org/abs/2610.23256) | [PDF](https://arxiv.org/pdf/2610.23256) | [papers.cool](https://papers.cool/arxiv/2610.23256)
- Authors: Ziyun Zou, Jiwoo Hong, Yifan Lu, Shao Tang, Weiyi Wu, Aman Gupta, et al. (8 authors)
- Published: 2026-10-16 10:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, rlhf, reward model
- Abstract skim: Multimodal preference alignment often follows a score-based RLHF pipeline: a reward model is first trained to learn human preferences, then used to score on-policy responses and optimize the response model's generation. This turns preference supervision into a scalar signal for generation: a model may learn to...

### 43 - Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning

- arXiv: [2610.23550](https://arxiv.org/abs/2610.23550) | [PDF](https://arxiv.org/pdf/2610.23550) | [papers.cool](https://papers.cool/arxiv/2610.23550)
- Authors: Anshul Nayak, Shahil Shaik, Jonathan Smereka, Yue Wang
- Published: 2026-10-16 14:41 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model; planning_and_action: trajectory
- Abstract skim: Reinforcement learning (RL) policies optimized for task rewards may produce behaviors that are efficient but misaligned with human expectations, safety preferences, or intent. This paper presents a reason-guided preference-based reinforcement learning (PbRL) framework that learns a human reward model from...

### 42 - Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards

- arXiv: [2610.22448](https://arxiv.org/abs/2610.22448) | [PDF](https://arxiv.org/pdf/2610.22448) | [papers.cool](https://papers.cool/arxiv/2610.22448)
- Authors: Ruida Wang, Gerald Friedland, Tong Zhang, Chris Kong
- Published: 2026-10-15 15:26 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning, grpo
- Abstract skim: Enhancing the agentic capabilities of Large Language Models (LLMs) to tackle complex software engineering (SWE) and general terminal-usage problems is a pressing challenge. Current state-of-the-art LLMs often go through large-scale agentic Reinforcement Learning (RL). However, they mostly rely on high-level outcome...

### 41 - Are Large Reasoning Models Good Everyday Reasoners? A Comparison with Non-Reasoning Models on Logical Reasoning Tasks

- arXiv: [2610.22538](https://arxiv.org/abs/2610.22538) | [PDF](https://arxiv.org/pdf/2610.22538) | [papers.cool](https://papers.cool/arxiv/2610.22538)
- Authors: Kentaro Ozeki, Risako Ando, Takanobu Morishita, Hirohiko Abe, Koji Mineshima, Mitsuhiro Okada
- Published: 2026-10-15 18:37 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Large reasoning models (LRMs) that leverage test-time computation achieve strong performance on mathematical and scientific benchmarks and are increasingly deployed in real-world applications. However, their ability to perform \textit{everyday logical reasoning}, which often departs from textbook formal logic,...

### 40 - Language Models Learn to Improve Language Models

- arXiv: [2610.23344](https://arxiv.org/abs/2610.23344) | [PDF](https://arxiv.org/pdf/2610.23344) | [papers.cool](https://papers.cool/arxiv/2610.23344)
- Authors: Minhua Lin, Zijun Wang, Zewen Liu, Zhaotian Weng, Bing He, Zhan Shi, et al. (10 authors)
- Published: 2026-10-16 11:51 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model; reasoning: self-improvement, self improvement; planning_and_action: world model
- Abstract skim: Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement. However, turning experimental feedback into a learned ability to propose effective improvements across models faces two challenges....

### 39 - WebCoder: Scaling General Frontend Development with Artifact-Grounded Agentic Reinforcement Learning

- arXiv: [2610.23104](https://arxiv.org/abs/2610.23104) | [PDF](https://arxiv.org/pdf/2610.23104) | [papers.cool](https://papers.cool/arxiv/2610.23104)
- Authors: Zijun Dou, Zhen Yang, Xijun Liu, Dongzhuoran Zhou, Aohan Zeng, Jie Tang
- Published: 2026-10-16 08:17 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: Real-world frontend development requires agents to compose reproduction, generation, modification, and repair over an evolving application state. Learning a general policy for this process requires translating heterogeneous execution feedback into task-aligned rewards and effective credit assignment across long...

### 38 - Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents

- arXiv: [2610.23148](https://arxiv.org/abs/2610.23148) | [PDF](https://arxiv.org/pdf/2610.23148) | [papers.cool](https://papers.cool/arxiv/2610.23148)
- Authors: Qirui Liu, Hao Chen, Yi Wen, Weijie Shi, Yao Zhao, Xianhe Chen, et al. (10 authors)
- Published: 2026-10-16 08:43 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: outcome reward; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Outcome-reward reinforcement learning such as GRPO gives every token of a search-agent rollout the same advantage, although the rollout exercises two capabilities: finding evidence and using it. We show that accuracy improves without grounding: Search-R1 raises accuracy on all seven QA benchmarks, yet on Bamboogle...

### 38 - Where Research Ideation Begins: Forward-Citation Supervision for Actionable Limitation Generation

- arXiv: [2610.23038](https://arxiv.org/abs/2610.23038) | [PDF](https://arxiv.org/pdf/2610.23038) | [papers.cool](https://papers.cool/arxiv/2610.23038)
- Authors: Liyang Zhao, Yong Cao, Haibin Ling
- Published: 2026-10-16 07:14 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Automated research ideation has advanced rapidly, with multi-agent workflows that generate whole research ideas end to end. These frameworks leave largely unexamined the step that seeds a good idea: identifying an actionable limitation from literature. In this paper, we focus on this first step in the research...

### 38 - R$^2$Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop

- arXiv: [2610.22740](https://arxiv.org/abs/2610.22740) | [PDF](https://arxiv.org/pdf/2610.22740) | [papers.cool](https://papers.cool/arxiv/2610.22740)
- Authors: Mingda Zhang, Yun Huang, Qiang Huang, Yanjin Li, Rui Qian, Qichao Zhao, et al. (10 authors)
- Published: 2026-10-15 23:21 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent orchestration; reasoning: self-improvement, self improvement, self-play; memory_and_benchmarks: evaluation
- Abstract skim: In recent years, agentic orchestration has been widely applied to solve complex human tasks. However, existing orchestration learning still faces key challenges, including hand-designed curricula, advantage collapse when a task's rollouts all reach the same outcome, and unreliable evaluation signals that judge each...

### 37 - Reasoning Reranking with Semantic IDs as the Sole Item Representation

- arXiv: [2610.22797](https://arxiv.org/abs/2610.22797) | [PDF](https://arxiv.org/pdf/2610.22797) | [papers.cool](https://papers.cool/arxiv/2610.22797)
- Authors: Zhenwei Tang, Jintao Liu, Di Bai, Xidong Wu, Xinwu Cheng
- Published: 2026-10-16 01:21 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Reasoning rerankers write a rationale before ranking a candidate slate, and existing systems read item metadata to do so, even though generative recommenders increasingly represent items as compact Semantic IDs (SIDs). Ranking from SIDs alone has two appeals: SID prompts are far shorter than the matched item text,...

### 36 - CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning

- arXiv: [2610.23820](https://arxiv.org/abs/2610.23820) | [PDF](https://arxiv.org/pdf/2610.23820) | [papers.cool](https://papers.cool/arxiv/2610.23820)
- Authors: Tianmeng Hu, Biao Luo, Ke Li
- Published: 2026-10-16 17:43 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Designing RNA sequences that reliably fold into specific secondary structures is essential for understanding their biological functions but remains a challenging computational problem. We propose CocoRNA, a cooperative multi-agent reinforcement learning framework for RNA inverse design. CocoRNA simplifies the design...

### 34 - MGE-PO: Entropy-Aware Credit Assignment for Mathematical Reasoning

- arXiv: [2610.23245](https://arxiv.org/abs/2610.23245) | [PDF](https://arxiv.org/pdf/2610.23245) | [papers.cool](https://papers.cool/arxiv/2610.23245)
- Authors: Jihao Huang, Guangjia Chai, Zhirui Chen, Lei Wang, Yao Liu, Liu Qi, et al. (12 authors)
- Published: 2026-10-16 10:15 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: policy optimization, grpo; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: GRPO assigns the same group-relative advantage to equally rewarded responses within a question, leaving their generation uncertainty unused. We introduce MGE-PO, centered on four-quadrant (4Q) advantage shaping that combines verified correctness with rollout generation entropy. Correctness determines the sign of an...

### 33 - Competence-Based Evaluation of Logical Reasoning in Large Language Models

- arXiv: [2610.22894](https://arxiv.org/abs/2610.22894) | [PDF](https://arxiv.org/pdf/2610.22894) | [papers.cool](https://papers.cool/arxiv/2610.22894)
- Authors: Jize Jiang, Chengxiang Zhai
- Published: 2026-10-16 03:52 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: grpo; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: evaluation
- Abstract skim: Recent advances in large language models (LLMs) have brought impressive performance across diverse tasks; however, shortcomings remain in logical reasoning, including inconsistencies under linguistic variation. To improve the reasoning capacity of LLMs, we must be able to accurately measure their reasoning capacity....

### 33 - Predicting Privileged Information Effectiveness for On-Policy Self-Distillation

- arXiv: [2610.22512](https://arxiv.org/abs/2610.22512) | [PDF](https://arxiv.org/pdf/2610.22512) | [papers.cool](https://papers.cool/arxiv/2610.22512)
- Authors: Kaijian Zou, Emiliano Penaloza, MohammadHossein Rezaei, Anisha Gunjal, Mohit Raghavendra, Lu Wang, et al. (8 authors)
- Published: 2026-10-15 18:05 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning
- Abstract skim: On-policy self-distillation (OPSD) enables large language models (LLMs) to learn from privileged information (PI) without a separate teacher model. However, prior work largely treats PI as a fixed design choice, leaving the effects of its content and construction poorly understood. This challenge is particularly...

### 32 - Analyzing Occupational Gender Bias across the LLM Training Lifecycle

- arXiv: [2610.23587](https://arxiv.org/abs/2610.23587) | [PDF](https://arxiv.org/pdf/2610.23587) | [papers.cool](https://papers.cool/arxiv/2610.23587)
- Authors: Manthan Gadhia, Alexander Hoyle, Karolina Stańczak
- Published: 2026-10-16 15:07 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, rlvr, dpo
- Abstract skim: Post-training is widely assumed to reduce the social biases language models inherit from pretraining, yet direct evidence for this assumption remains mixed. In this paper, we examine how gender disparities evolve across the language modeling pipeline. In particular, we study occupational gender bias in OLMo 3, a...

### 32 - Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism

- arXiv: [2610.22937](https://arxiv.org/abs/2610.22937) | [PDF](https://arxiv.org/pdf/2610.22937) | [papers.cool](https://papers.cool/arxiv/2610.22937)
- Authors: Prakhar Gupta, Terry Jingchen Zhang, Zhijing Jin
- Published: 2026-10-16 05:00 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Language models often abandon a correct answer when the prompt contains a cue, a hint toward a wrong option such as "I think the answer is B." Sycophancy and related biases show this failure. They are often studied separately and blamed on alignment. We test this view causally, tracing the attention heads behind...

### 32 - Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors

- arXiv: [2610.22852](https://arxiv.org/abs/2610.22852) | [PDF](https://arxiv.org/pdf/2610.22852) | [papers.cool](https://papers.cool/arxiv/2610.22852)
- Authors: Carl Qi, Weijun Dong, Xiaojie Wang, Peiyi Chen, Rahul Sajnani, Mingyuan Zhang, et al. (11 authors)
- Published: 2026-10-16 02:51 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Generalist robot policies offer strong behavioral priors, but achieving deployment-level reliability and throughput remains difficult. Reinforcement learning (RL) can improve these policies, yet its effectiveness is constrained by the cost of online interaction. Existing methods adapt frozen flow-matching policies...

### 32 - FRACTAL: A Self-Similar Multi-Agent Orchestration Architecture with Formal Communication, Convergence, and Depth Bounds

- arXiv: [2610.22561](https://arxiv.org/abs/2610.22561) | [PDF](https://arxiv.org/pdf/2610.22561) | [papers.cool](https://papers.cool/arxiv/2610.22561)
- Authors: Ohad Dan, Abhinav Taliyan
- Published: 2026-10-15 19:02 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent orchestration; reasoning: self-improvement, self improvement
- Abstract skim: We present FRACTAL, a self-similar multi-agent architecture for recursive goal decomposition, in which the same five-component organizational pattern -- Orchestrator, Ensemble, Knowledge Ledger, Decision Maker, Meta-Observer -- recurs at every level of a decomposition tree. We make four formal contributions: (1) a...

### 31 - Distill Until Divergence: Error-Truncated Hindsight Distillation for Agentic RL

- arXiv: [2610.23048](https://arxiv.org/abs/2610.23048) | [PDF](https://arxiv.org/pdf/2610.23048) | [papers.cool](https://papers.cool/arxiv/2610.23048)
- Authors: Yibin Huang, Conghui Zhu
- Published: 2026-10-16 07:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl; rl_post_training: grpo; planning_and_action: trajectory
- Abstract skim: Long-horizon interaction requires agents to make multiple decisions in a changing environment. Outcome-based GRPO lacks fine-grained guidance for intermediate decisions. Recent methods distill completed trajectories into reusable skills and use hindsight-conditioned OPD to provide dense token-level credit. However,...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
