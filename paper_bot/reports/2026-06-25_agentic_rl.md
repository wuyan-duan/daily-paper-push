# RL / Post-Training / Agentic RL Reading Queue - 2026-06-25

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 387. Minimum score: 8.

## Top Picks

### 102 - The Hitchhiker's Guide to Agentic AI: From Foundations to Systems

- arXiv: [2606.24937](https://arxiv.org/abs/2606.24937) | [PDF](https://arxiv.org/pdf/2606.24937) | [papers.cool](https://papers.cool/arxiv/2606.24937)
- Authors: Haggai Roitman
- Published: 2026-06-22 17:48 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, tool use, agent harness; rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, grpo, +2 more; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory; memory_and_benchmarks: memory, evaluation
- Abstract skim: The Hitchhiker's Guide to Agentic AI is a comprehensive practitioner's reference for building autonomous AI systems. The book covers the full stack from first principles to production deployment, organized around a central thesis: building great agentic systems requires understanding every layer of the pipeline, not...

### 54 - Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents

- arXiv: [2606.26080](https://arxiv.org/abs/2606.26080) | [PDF](https://arxiv.org/pdf/2606.26080) | [papers.cool](https://papers.cool/arxiv/2606.26080)
- Authors: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
- Published: 2026-06-24 17:54 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model; reasoning: process reward; planning_and_action: environment feedback; memory_and_benchmarks: evaluation
- Abstract skim: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this...

### 51 - Learning with a Single Rollout via Monte Carlo Pass@k Critic

- arXiv: [2606.25451](https://arxiv.org/abs/2606.25451) | [PDF](https://arxiv.org/pdf/2606.25451) | [papers.cool](https://papers.cool/arxiv/2606.25451)
- Authors: Fengdi Che, Yang Liu, Lei Yu, Meng Cao, Tong Che, Rupam Mahmood, et al. (7 authors)
- Published: 2026-06-24 06:26 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo, ppo; reasoning: reasoning, outcome reward; planning_and_action: rollout
- Abstract skim: Estimating token-level advantages in reinforcement learning (RL) for language models remains challenging because scaling up episodic experience collection is expensive. The difficulty intensifies for baseline advantage estimation methods, where repeated sampling causes trajectories to diverge into substantially...

### 50 - ExTra: Exploratory Trajectory Optimization for Language Model Reinforcement Learning

- arXiv: [2606.24994](https://arxiv.org/abs/2606.24994) | [PDF](https://arxiv.org/pdf/2606.24994) | [papers.cool](https://papers.cool/arxiv/2606.24994)
- Authors: Wenyang Hu, Junxiang Jia, Zhen Shu, Daniel Dahlmeier, See-Kiong Ng, Bryan Kian Hsiang Low
- Published: 2026-06-23 15:51 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) for language-model reasoning can fail at both extremes of task difficulty: easy prompts often produce all-correct, low-diversity rollout groups with little gradient signal, while hard prompts can produce all-incorrect groups with no positive reward. We introduce...

### 49 - Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models

- arXiv: [2606.25519](https://arxiv.org/abs/2606.25519) | [PDF](https://arxiv.org/pdf/2606.25519) | [papers.cool](https://papers.cool/arxiv/2606.25519)
- Authors: Xinyu Lian, Walid Krichene, Beichen Huang, Masahiro Tanaka, Olatunji Ruwase, Li Zhang, et al. (7 authors)
- Published: 2026-06-24 07:54 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency. We show that low-bit post-training quantization can introduce a hidden test-time compute cost: quantized reasoning models often...

### 45 - Multi-Agent Goal Recognition with Team- and Goal-Conditioned Reinforcement Learning and Factorized Branch-and-Bound

- arXiv: [2606.25978](https://arxiv.org/abs/2606.25978) | [PDF](https://arxiv.org/pdf/2606.25978) | [papers.cool](https://papers.cool/arxiv/2606.25978)
- Authors: Thiago Thomas, Gabriel de Oliveira Ramos, Felipe Meneguzzi
- Published: 2026-06-24 15:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Multi-agent goal recognition asks an observer to jointly infer which agents act together and what each team is trying to achieve, so the hypothesis space grows combinatorially with the number of team partitions and goals per team. Real applications such as drone surveillance and collaborative robotics expose only...

### 45 - Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR

- arXiv: [2606.25178](https://arxiv.org/abs/2606.25178) | [PDF](https://arxiv.org/pdf/2606.25178) | [papers.cool](https://papers.cool/arxiv/2606.25178)
- Authors: Yongjin Yang, Jiarui Liu, Yinghui He, Lezhen Zhang, Bernhard Schölkopf, Zhijing Jin
- Published: 2026-06-23 21:10 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has been extended from single-domain training to multi-domain reasoning suites spanning mathematics, programming, and science. However, the training curriculum (how often each domain is sampled) is typically fixed or hand-tuned, even though reasoning skills...

### 42 - ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning

- arXiv: [2606.24601](https://arxiv.org/abs/2606.24601) | [PDF](https://arxiv.org/pdf/2606.24601) | [papers.cool](https://papers.cool/arxiv/2606.24601)
- Authors: Anurag Akula, Satheesh K. Perepu, Abhishek Sarkar, Kaushik Dey
- Published: 2026-06-23 14:03 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark
- Abstract skim: Multi-agent reinforcement learning (MARL) addresses the problem of training multiple agents that pursue collaborative, competitive, or mixed objectives. Prior work has investigated transfer learning between source and target domains in MARL; however, the majority of existing approaches impose the constraint that the...

### 40 - Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents

- arXiv: [2606.25852](https://arxiv.org/abs/2606.25852) | [PDF](https://arxiv.org/pdf/2606.25852) | [papers.cool](https://papers.cool/arxiv/2606.25852)
- Authors: Peng Xu, Sijia Chen, Junzhuo Li, Xuming Hu
- Published: 2026-06-24 14:02 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on...

### 39 - Omni-Perception Policy Optimization for Multimodal Emotion Reasoning

- arXiv: [2606.25325](https://arxiv.org/abs/2606.25325) | [PDF](https://arxiv.org/pdf/2606.25325) | [papers.cool](https://papers.cool/arxiv/2606.25325)
- Authors: Zhiyuan Han, Beier Zhu, Wenwen Tong, Pengyang Shao, Peipei Song, Xinyi Wang, et al. (9 authors)
- Published: 2026-06-24 02:43 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: We find that current emotion-oriented Omni-MLLMs still lack reliable omni-modal perception: they (i) underutilize multimodal cues in their reasoning trajectories and (ii) exhibit unfaithful behavior, often hallucinating modality-specific statements from other modalities. Building on these insights, we propose OPPO...

### 37 - Weight-Space Geometry of Offline Reasoning Training

- arXiv: [2606.23740](https://arxiv.org/abs/2606.23740) | [PDF](https://arxiv.org/pdf/2606.23740) | [papers.cool](https://papers.cool/arxiv/2606.23740)
- Authors: Aleksandr Nikolich, Igor Kiselev, Vladimir Platonov, Karina Romanova
- Published: 2026-06-21 15:34 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo, dpo; reasoning: reasoning
- Abstract skim: Offline reinforcement-learning losses (RFT, RIFT, DFT, Offline GRPO, DPO) are widely used to distill reasoning from large teachers into smaller students, and are typically compared on downstream accuracy alone. We ask whether they are mechanistically distinct or converge to a similar weight update. Training six...

### 36 - GCT-MARL: Graph-Based Contrastive Transfer for Sample-Efficient Cooperative Multi-Agent Reinforcement Learning

- arXiv: [2606.25073](https://arxiv.org/abs/2606.25073) | [PDF](https://arxiv.org/pdf/2606.25073) | [papers.cool](https://papers.cool/arxiv/2606.25073)
- Authors: Animesh Animesh, Satheesh K Perepu, Kaushik Dey
- Published: 2026-06-23 18:31 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: In cooperative multi-agent reinforcement learning (MARL), from a deployment perspective, it is challenging and expensive to train agents from scratch for each new environment or task. In this work, we propose GCT-MARL, a transfer learning framework that builds on the multi-view graph contrastive backbone of MAIL and...

### 36 - AsyncOPD: How Stale Can On-Policy Distillation Be?

- arXiv: [2606.24143](https://arxiv.org/abs/2606.24143) | [PDF](https://arxiv.org/pdf/2606.24143) | [papers.cool](https://papers.cool/arxiv/2606.24143)
- Authors: Wonjun Kang, Kevin Galim, Seunghyuk Oh, Minjun Kang, Sanghyun Park, Donghoon Kim, et al. (12 authors)
- Published: 2026-06-23 04:50 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: On-policy distillation (OPD) trains a student on its own rollouts guided by teacher feedback and is becoming increasingly important for large language model (LLM) post-training. Like reinforcement learning (RL), however, OPD faces an on-policy systems bottleneck, as rollouts can dominate training time for reasoning...

### 33 - Qwen-AgentWorld: Language World Models for General Agents

- arXiv: [2606.24597](https://arxiv.org/abs/2606.24597) | [PDF](https://arxiv.org/pdf/2606.24597) | [papers.cool](https://papers.cool/arxiv/2606.24597)
- Authors: Yuxin Zuo, Zikai Xiao, Li Sheng, Fei Huang, Jianhong Tu, Yuxuan Liu, et al. (33 authors)
- Published: 2026-06-23 13:53 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic rl; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: planning, world model; memory_and_benchmarks: benchmark
- Abstract skim: A world model predicts environment dynamics based on current observations and actions, serving as a core cognitive mechanism for reasoning and planning. In this work, we investigate how world modeling based on language models can further push the boundaries of general agents. (i) We first focus on building...

### 32 - KLip-PPO: A per-sample KL perspective on PPO-Clip

- arXiv: [2606.23932](https://arxiv.org/abs/2606.23932) | [PDF](https://arxiv.org/pdf/2606.23932) | [papers.cool](https://papers.cool/arxiv/2606.23932)
- Authors: Riccardo Colletti, Robin Holzinger
- Published: 2026-06-22 20:52 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Proximal Policy Optimization (PPO) is the standard policy-gradient algorithm for on-policy reinforcement learning. The literature presents it in two forms, a clipped surrogate that bounds the importance ratio between successive policies and a Kullback-Leibler penalty between them. These forms are treated as separate...

### 29 - MiniOpt: Reasoning to Model and Solve General Optimization Problems with Limited Resources

- arXiv: [2606.25832](https://arxiv.org/abs/2606.25832) | [PDF](https://arxiv.org/pdf/2606.25832) | [papers.cool](https://papers.cool/arxiv/2606.25832)
- Authors: Ke Zhao, Zixiang Di, Hong Qian, Xiang Shu, Yaolin Wen, Qitao Shi, et al. (12 authors)
- Published: 2026-06-24 13:48 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: Achieving strong optimization generalization across diverse optimization problems while requiring limited training resources remains a challenging problem for optimization-oriented large language models (LLMs). Existing approaches typically rely on large-scale supervised datasets, costly reasoning annotations, and...

### 29 - Cliff Tokens: Identifying Single-Token Failure Triggers in LLM Mathematical Reasoning

- arXiv: [2606.25524](https://arxiv.org/abs/2606.25524) | [PDF](https://arxiv.org/pdf/2606.25524) | [papers.cool](https://papers.cool/arxiv/2606.25524)
- Authors: Jaeyong Ko, Pilsung Kang, Yukyung Lee
- Published: 2026-06-24 08:03 UTC | Categories: cs.AI
- Why it matched: rl_post_training: preference optimization, dpo; reasoning: reasoning
- Abstract skim: Large language models (LLMs) reach high accuracy in mathematical reasoning, but individual traces on the same problem diverge; some arrive at the correct answer while others fail. Prior work analyzes failure at the step, chunk, or sentence level, or at tokens where failure has already occurred. Neither identifies...

### 29 - Geo-Strat-RL: Learning Geological Event Reasoning from Verifiable Tasks

- arXiv: [2606.25000](https://arxiv.org/abs/2606.25000) | [PDF](https://arxiv.org/pdf/2606.25000) | [papers.cool](https://papers.cool/arxiv/2606.25000)
- Authors: Lukas Mosser
- Published: 2026-06-23 16:20 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: To evaluate whether vision-language models can reason about geological histories, it is necessary to construct observations for which the underlying process history is known. Furthermore, reasoning over geological histories is not just a question of recognizing visual patterns, but also of understanding temporal and...

### 29 - Learning to Trigger: Reinforcement Learning at the Large Hadron Collider

- arXiv: [2606.23993](https://arxiv.org/abs/2606.23993) | [PDF](https://arxiv.org/pdf/2606.23993) | [papers.cool](https://papers.cool/arxiv/2606.23993)
- Authors: Zixin Ding, Shaghayegh Emam, Giovanna Salvi, Cecilia Tosciri, Abhijith Gandrakota, Jennifer Ngadiuba, et al. (10 authors)
- Published: 2026-06-22 22:56 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: decision making; memory_and_benchmarks: benchmark
- Abstract skim: High-throughput scientific facilities such as the Large Hadron Collider depend on real-time event filtering (\textit{triggering}) under tight constraints on bandwidth, latency, and storage. In practice, trigger menus are largely static and hand-tuned and can become suboptimal as detector conditions, pileup, and...

### 27 - Power-Budgeted Underwater Vehicle Control via Constrained Reinforcement Learning

- arXiv: [2606.25680](https://arxiv.org/abs/2606.25680) | [PDF](https://arxiv.org/pdf/2606.25680) | [papers.cool](https://papers.cool/arxiv/2606.25680)
- Authors: Yinuo Wang, Gavin Tao, Yuze Liu
- Published: 2026-06-24 10:48 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, ppo; planning_and_action: trajectory
- Abstract skim: Underwater vehicles operate from a fixed onboard energy budget that propulsion rapidly depletes, so a controller that completes its task while drawing less thruster power directly extends mission range and endurance. Reinforcement learning yields capable model-free controllers for station-keeping and trajectory...

### 27 - Yuvion VL: A Multimodal Foundation Model for Adversarial Content and AI Safety

- arXiv: [2606.25034](https://arxiv.org/abs/2606.25034) | [PDF](https://arxiv.org/pdf/2606.25034) | [papers.cool](https://papers.cool/arxiv/2606.25034)
- Authors: Shikai Qiu, Xiaowen Xu, Benlei Cui, Ting Ma, Xiufeng Huang, Wenjing Jiang, et al. (54 authors)
- Published: 2026-06-23 18:00 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: General-purpose models often struggle to reliably identify and understand real-world multimodal risks, largely due to the inherent multimodal adversarial nature of content and AI safety. We present Yuvion VL, a family of multimodal large language models purpose-built for content and AI safety, with both instruction-...

### 27 - MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery

- arXiv: [2606.24595](https://arxiv.org/abs/2606.24595) | [PDF](https://arxiv.org/pdf/2606.24595) | [papers.cool](https://papers.cool/arxiv/2606.24595)
- Authors: Enze Ma, Yufan Zhou, Wei-Chieh Huang, Jie Yang, Huanhuan Ma, Zixuan Wang, et al. (10 authors)
- Published: 2026-06-23 13:52 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agent memory; planning_and_action: trajectory; memory_and_benchmarks: memory, long-term memory, benchmark
- Abstract skim: Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which...

### 26 - BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents

- arXiv: [2606.25556](https://arxiv.org/abs/2606.25556) | [PDF](https://arxiv.org/pdf/2606.25556) | [papers.cool](https://papers.cool/arxiv/2606.25556)
- Authors: Hanyang Wang, Weijieying Ren, Yuxiang Zhang, Ding Cao, Zhizhao Zeng, Ke Zeng, et al. (7 authors)
- Published: 2026-06-24 08:32 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, grpo; memory_and_benchmarks: alfworld
- Abstract skim: Stepwise group-based RL is an attractive way to train long-horizon LLM agents without a learned critic: it reuses multiple sampled rollouts to estimate local advantages. Its weakness is less visible but more fundamental: every group-relative estimator assumes that the steps it compares are equivalent for credit...

### 25 - Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning

- arXiv: [2606.25357](https://arxiv.org/abs/2606.25357) | [PDF](https://arxiv.org/pdf/2606.25357) | [papers.cool](https://papers.cool/arxiv/2606.25357)
- Authors: Yivan Zhang, Ziyan Luo, Manuel Baltieri
- Published: 2026-06-24 03:43 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: State abstraction plays a key role in scaling reinforcement learning to complex but structured systems. In studying such systems, a wide range of behavioral structures have been studied in reinforcement learning, including value functions, invariants, bisimulation relations, and behavioral metrics. However, a...

### 25 - TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory

- arXiv: [2606.25161](https://arxiv.org/abs/2606.25161) | [PDF](https://arxiv.org/pdf/2606.25161) | [papers.cool](https://papers.cool/arxiv/2606.25161)
- Authors: Tianyu Yang, Sudipta Paul, Vijay Srinivasan, Vivek Kulkarni, Srinivas Chappidi
- Published: 2026-06-23 20:49 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: memory, long-term memory
- Abstract skim: Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. Existing memory agents actively update external memory through generated write, revise, and delete operations, but these updates may omit important information,...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
