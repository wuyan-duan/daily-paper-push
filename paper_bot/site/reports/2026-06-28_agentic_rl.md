# RL / Post-Training / Agentic RL Reading Queue - 2026-06-28

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 374. Minimum score: 8.

## Top Picks

### 79 - RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning

- arXiv: [2606.26997](https://arxiv.org/abs/2606.26997) | [PDF](https://arxiv.org/pdf/2606.26997) | [papers.cool](https://papers.cool/arxiv/2606.26997)
- Authors: Rongjian Chen, Jianmin Hu, Kejiang Ye, Minxian Xu
- Published: 2026-06-25 13:14 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +3 more; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Large language model (LLM) post-training for reasoning increasingly relies on reinforcement learning with verifiable rewards (RLVR), where models learn from ground-truth feedback on mathematical, logical, and scientific tasks. To enable flexible resource allocation and support heterogeneous training setups, modern...

### 63 - GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning

- arXiv: [2606.26917](https://arxiv.org/abs/2606.26917) | [PDF](https://arxiv.org/pdf/2606.26917) | [papers.cool](https://papers.cool/arxiv/2606.26917)
- Authors: Ting Zhou, Zhenqing Ling, Yiyang Zhao, Ying Shen, Daoyuan Chen
- Published: 2026-06-25 11:53 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model, grpo, +1 more; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Online reinforcement learning is widely used to align large language models (LLMs) with reward signals, yet training can be unstable under noisy or misspecified rewards. We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space...

### 61 - Improving General Role-Playing Agents via Psychology-Grounded Reasoning and Role-Aware Policy Optimization

- arXiv: [2606.27025](https://arxiv.org/abs/2606.27025) | [PDF](https://arxiv.org/pdf/2606.27025) | [papers.cool](https://papers.cool/arxiv/2606.27025)
- Authors: Zhenhua Xu, Dongsheng Chen, Jian Li, Yitong Lin, Zhebo Wang, Jiafu Wu, et al. (10 authors)
- Published: 2026-06-25 13:34 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model, grpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Building general-purpose role-playing agents that faithfully portray any character from a natural-language profile remains challenging. The dominant paradigm -- supervised fine-tuning -- encourages behavioral mimicry without deep, human-like internal thought processes, resulting in poor out-of-distribution...

### 53 - OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning

- arXiv: [2606.26790](https://arxiv.org/abs/2606.26790) | [PDF](https://arxiv.org/pdf/2606.26790) | [papers.cool](https://papers.cool/arxiv/2606.26790)
- Authors: Shuo Yang, Jinyang Wu, Zhengxi Lu, Yuhao Shen, Fan Zhang, Lang Feng, et al. (11 authors)
- Published: 2026-06-25 09:24 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Outcome-based reinforcement learning provides a stable optimization backbone for language agents, but its sparse trajectory-level rewards provide little guidance on which intermediate decisions should be reinforced or suppressed. On-policy self-distillation offers dense token-level supervision, yet existing skill-...

### 51 - NebulaExp-8B: An Empirical Post-Training Pipeline via Full-Scale Ablation Research

- arXiv: [2606.26671](https://arxiv.org/abs/2606.26671) | [PDF](https://arxiv.org/pdf/2606.26671) | [papers.cool](https://papers.cool/arxiv/2606.26671)
- Authors: Qiaobo Hao, Yangqian Wu, Shunyi Wang, Zhongjian Zhang, Ziqun Li, Yayin He, et al. (8 authors)
- Published: 2026-06-25 07:03 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Post-training alignment determines the reasoning and human preference following capabilities of large language models, yet most existing works withhold detailed data construction, filtering rules and training recipes, which hinders community reproducibility and lightweight model optimization. This work presents...

### 41 - Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs

- arXiv: [2606.26387](https://arxiv.org/abs/2606.26387) | [PDF](https://arxiv.org/pdf/2606.26387) | [papers.cool](https://papers.cool/arxiv/2606.26387)
- Authors: Xi Xiao, Chen Liu, Chih-Ting Liao, Yunbei Zhang, Qizhen Lan, Yuxiang Wei, et al. (12 authors)
- Published: 2026-06-24 21:12 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, preference optimization; reasoning: reasoning
- Abstract skim: Multimodal large language models (MLLMs) extend large language models (LLMs) with visual perception, enabling joint reasoning over images and text. Despite inheriting strong reasoning capabilities from LLMs, they remain prone to hallucinations that contradict their visual inputs. Mechanistic studies indicate that...

### 37 - Designing Reward Signals for Portable Query Generation: A Case Study in Industrial Semantic Job Search

- arXiv: [2606.27291](https://arxiv.org/abs/2606.27291) | [PDF](https://arxiv.org/pdf/2606.27291) | [papers.cool](https://papers.cool/arxiv/2606.27291)
- Authors: Ping Liu, Qianqi Shen, Jianqiang Shen, Wenqiong Liu, Rajat Arora, Yunxiang Ren, et al. (14 authors)
- Published: 2026-06-25 17:09 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model, grpo; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Job-search platforms rely on low-bandwidth query interfaces that often fail to capture the high-dimensional complexity of candidate profiles. We present an end-to-end RLAIF (Reinforcement Learning from AI Feedback) framework to generate \emph{portable} job search queries, terms that abstract away seeker-specific...

### 34 - EVOM: Agentic Meta-Evolution of Actor-Critic Architectures for Reinforcement Learning

- arXiv: [2606.26327](https://arxiv.org/abs/2606.26327) | [PDF](https://arxiv.org/pdf/2606.26327) | [papers.cool](https://papers.cool/arxiv/2606.26327)
- Authors: Boyun Zhang, Chao Wang, Kai Wu
- Published: 2026-06-24 19:13 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: In actor-critic reinforcement learning, network architectures are typically manually designed. Automating this design is challenging because each candidate must be trained before evaluation, and the design space is open-ended. To address these challenges, we introduce EVOM, an agentic meta-evolution framework for...

### 33 - Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes

- arXiv: [2606.27210](https://arxiv.org/abs/2606.27210) | [PDF](https://arxiv.org/pdf/2606.27210) | [papers.cool](https://papers.cool/arxiv/2606.27210)
- Authors: Jeremias Ferrao, Niclas Müller-Hof, Iustin Sîrbu, Traian Rebedea, Yftah Ziser
- Published: 2026-06-25 16:03 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo, dpo; reasoning: reasoning
- Abstract skim: We argue that safety classifiers should model user intent as an explicit signal between the prompt and the final label. To study this, we introduce AIMS, a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label. We use AIMS to evaluate intent-aware training...

### 32 - AIGP: An LLM-Based Framework for Long-Term Value Alignment in E-Commerce Pricing

- arXiv: [2606.26787](https://arxiv.org/abs/2606.26787) | [PDF](https://arxiv.org/pdf/2606.26787) | [papers.cool](https://papers.cool/arxiv/2606.26787)
- Authors: Chennan Ma, Yanning Zhang, Siqi Hong, Xiuchong Wang, Fei Xiao, Keping Yang
- Published: 2026-06-25 09:21 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, preference optimization, reward model, dpo
- Abstract skim: Traditional dynamic pricing models in large-scale e-commerce suffer from limited interpretability, poor utilization of unstructured information, and misalignment with long-term business objectives such as cumulative Gross Merchandise Value (GMV), Return on Investment (ROI) and milestone achievement. We propose AIGP,...

### 32 - VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation

- arXiv: [2606.26534](https://arxiv.org/abs/2606.26534) | [PDF](https://arxiv.org/pdf/2606.26534) | [papers.cool](https://papers.cool/arxiv/2606.26534)
- Authors: Tianxin Xie, Chenxing Li, Dong Yu, Li Liu
- Published: 2026-06-25 02:18 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, preference optimization, grpo
- Abstract skim: Recently, zero-shot text-to-speech (TTS) has enabled high-fidelity and expressive speech synthesis, but it often fails to imitate unseen speaking styles from uncommon scenarios (e.g., crosstalk, dialects). Moreover, fine-tuning pretrained models requires large, high-quality datasets, limiting rapid personalization....

### 30 - ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent

- arXiv: [2606.26403](https://arxiv.org/abs/2606.26403) | [PDF](https://arxiv.org/pdf/2606.26403) | [papers.cool](https://papers.cool/arxiv/2606.26403)
- Authors: Sriram Selvam, Anneswa Ghosh
- Published: 2026-06-24 21:43 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent, tool use; memory_and_benchmarks: memory, evaluation
- Abstract skim: Foundation-model research increasingly needs data about people: user state, personal histories, relationships, contact-like fields, documents, and longitudinal updates. Real user data is difficult to share, perturb, audit, or redistribute responsibly, while independently generated fake fields rarely preserve the...

### 27 - Semantic Early-Stopping for Iterative LLM Agent Loops

- arXiv: [2606.27009](https://arxiv.org/abs/2606.27009) | [PDF](https://arxiv.org/pdf/2606.27009) | [papers.cool](https://papers.cool/arxiv/2606.27009)
- Authors: Sahil Shrivastava
- Published: 2026-06-25 13:24 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: llm agent, multi-agent; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Multi-agent large language model (LLM) loops, for example a Writer that drafts and a Critic that revises, are almost always terminated by a fixed iteration cap (max_iterations). This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and...

### 27 - From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP

- arXiv: [2606.26535](https://arxiv.org/abs/2606.26535) | [PDF](https://arxiv.org/pdf/2606.26535) | [papers.cool](https://papers.cool/arxiv/2606.26535)
- Authors: Zhixing Li, Yinan Yu
- Published: 2026-06-25 02:18 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Current VLM evaluations often conflate language priors with genuine spatial reasoning. To address this, we introduce CRISP, a novel structural-diagnostic evaluation paradigm that assesses visual spatial intelligence through consistency, the alignment between implicit perception and explicit reasoning. Unlike...

### 26 - Reinforcement Learning without Ground-Truth Solutions can Improve LLMs

- arXiv: [2606.27369](https://arxiv.org/abs/2606.27369) | [PDF](https://arxiv.org/pdf/2606.27369) | [papers.cool](https://papers.cool/arxiv/2606.27369)
- Authors: Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang, Xunpeng Huang, Kun Zhou, Tongtong Liang, et al. (9 authors)
- Published: 2026-06-25 17:59 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) for training LLMs typically rely on ground-truth answers to assign rewards, limiting their applicability to tasks where the ground-truth solution is unknown. We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs...

### 26 - Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents

- arXiv: [2606.26627](https://arxiv.org/abs/2606.26627) | [PDF](https://arxiv.org/pdf/2606.26627) | [papers.cool](https://papers.cool/arxiv/2606.26627)
- Authors: Nada Lahjouji, Ashwin Gerard Colaco
- Published: 2026-06-25 05:44 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, agent memory; memory_and_benchmarks: memory, benchmark
- Abstract skim: Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf. As they move from answering questions to operating over sensitive data, privacy becomes harder to enforce. An agent touches many data sources, runs multi-...

### 25 - Sample-efficient Transfer Reinforcement Learning via Adaptive Reward Shaping and Policy-Ratio Reweighting Strategy

- arXiv: [2606.26527](https://arxiv.org/abs/2606.26527) | [PDF](https://arxiv.org/pdf/2606.26527) | [papers.cool](https://papers.cool/arxiv/2606.26527)
- Authors: Wenjie Huang, Yang Li, Jingjia Teng, Mingwei Jin, Kai Song, Yougang Bian, et al. (9 authors)
- Published: 2026-06-25 02:02 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: decision making; memory_and_benchmarks: evaluation; downranked: traffic
- Abstract skim: Transfer learning improves policy learning efficiency by reusing knowledge from source tasks, providing a feasible paradigm for safe and efficient autonomous highway lane changing decision-making. Existing methods frequently encounter transfer mismatch induced by distribution shifts between source and target...

### 24 - PlanRL: A Trajectory Planning Architecture for Reinforcement Learning-based Driving Experts

- arXiv: [2606.26858](https://arxiv.org/abs/2606.26858) | [PDF](https://arxiv.org/pdf/2606.26858) | [papers.cool](https://papers.cool/arxiv/2606.26858)
- Authors: Joonhee Lim, Yongjae Lee, Jangho Shin, Dongsuk Kum
- Published: 2026-06-25 10:42 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, trajectory; downranked: driving
- Abstract skim: Reinforcement learning (RL) has become a prominent framework for developing driving experts in autonomous vehicles. However, most existing RL-based experts are designed to output direct control commands (e.g., throttle, steering), which suffer from a lack of interpretability, high spatial complexity in learning road...

### 23 - OpenFinGym: A Verifiable Multi-Task Gym Environment for Evaluating Quant Agents

- arXiv: [2606.26350](https://arxiv.org/abs/2606.26350) | [PDF](https://arxiv.org/pdf/2606.26350) | [papers.cool](https://papers.cool/arxiv/2606.26350)
- Authors: Kaicheng Zhang, Wen Ge, Lei Jiang, Weixin Yang, Jordan Langham-Lopez, Jialin Yu, et al. (8 authors)
- Published: 2026-06-24 19:42 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; planning_and_action: decision making; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Although large language model agents are increasingly applied to quantitative-finance workflows, their evaluation remains fragmented across isolated tasks, while the financial relevance of benchmark tasks is often overlooked. Yet financial workflows are inherently multi-stage, spanning interdependent tasks such as...

### 20 - Confidence-Aware Tool Orchestration for Robust Video Understanding

- arXiv: [2606.26904](https://arxiv.org/abs/2606.26904) | [PDF](https://arxiv.org/pdf/2606.26904) | [papers.cool](https://papers.cool/arxiv/2606.26904)
- Authors: Yangfan He, Yujin Choi, Jaehong Yoon
- Published: 2026-06-25 11:37 UTC | Categories: cs.AI
- Why it matched: rl_post_training: grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Video reasoning language models implicitly assume that every input frame is equally reliable. This leads to what we term the Blind Trust Problem: under realistic perturbations such as motion blur, glare, or occlusion, frontier video reasoning models can suffer 15-30%p accuracy drops on real-world embodied...

### 20 - Zero-shot Tweet-Level Stance Detection Enhanced by External Knowledge and Reflective Chain-of-Thought Reasoning

- arXiv: [2606.26571](https://arxiv.org/abs/2606.26571) | [PDF](https://arxiv.org/pdf/2606.26571) | [papers.cool](https://papers.cool/arxiv/2606.26571)
- Authors: Yiju Huang, Wenxian Wang, Lijun Zhou, Rui Tang, Xiao Lan, Tao Zhang, et al. (7 authors)
- Published: 2026-06-25 03:46 UTC | Categories: cs.CL
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Zero-shot tweet-level stance detection confronts two primary challenges: (1) mitigating the context sparsity inherent in short texts, and (2) establishing the relevance between implicit targets and textual content. While existing methods primarily focus on incorporating external knowledge, they neglect the intrinsic...

### 20 - Perception, Verdict, and Evolution: Hindsight-Driven Self-Refining Forensics Agent for AI-Generated Image Detection

- arXiv: [2606.26552](https://arxiv.org/abs/2606.26552) | [PDF](https://arxiv.org/pdf/2606.26552) | [papers.cool](https://papers.cool/arxiv/2606.26552)
- Authors: Yangjun Wu, Keyu Yan, Yu Liu, Jingren Zhou, Fei Huang, Rong Zhang, et al. (8 authors)
- Published: 2026-06-25 02:59 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, self-improvement, self improvement, reflection; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: The rapid advancement of generative models presents a significant challenge to existing deepfake detection methods, particularly given the widespread dissemination of highly realistic AI-generated images. Although Multimodal Large Language Models (MLLMs) show strong potential for this task, existing approaches...

### 20 - Mean-Field PhiBE: Continuous-Time Mean-Field Reinforcement Learning from Discrete-Time Data

- arXiv: [2606.26498](https://arxiv.org/abs/2606.26498) | [PDF](https://arxiv.org/pdf/2606.26498) | [papers.cool](https://papers.cool/arxiv/2606.26498)
- Authors: Erhan Bayraktar, Martin Hernandez, Qinxin Yan, Yuhua Zhu
- Published: 2026-06-25 01:05 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: This paper addresses model-free continuous-time mean-field control in a setting where the population dynamics evolve continuously according to an unknown McKean-Vlasov stochastic differential equation, while only discrete-time transition data are available. In the model-based formulation, policy evaluation is...

### 19 - Deterministic Pareto-Optimal Policy Synthesis for Multi-Objective Reinforcement Learning

- arXiv: [2606.26397](https://arxiv.org/abs/2606.26397) | [PDF](https://arxiv.org/pdf/2606.26397) | [papers.cool](https://papers.cool/arxiv/2606.26397)
- Authors: Aniruddha Joshi, Niklas Lauffer, Sanjit Seshia
- Published: 2026-06-24 21:28 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: decision making
- Abstract skim: Real-world decision-making often requires balancing multiple conflicting objectives, a challenge that standard Reinforcement Learning (RL) frequently addresses by aggregating rewards into a single scalar signal. While effective for simple tasks, this approach often fails to capture the full spectrum of optimal...

### 19 - Mesh-RL: Coupled subgrid reinforcement learning

- arXiv: [2606.26333](https://arxiv.org/abs/2606.26333) | [PDF](https://arxiv.org/pdf/2606.26333) | [papers.cool](https://papers.cool/arxiv/2606.26333)
- Authors: Behnam Gheshlaghi, Bahador Rashidi, Shahin Atakishiyev
- Published: 2026-06-24 19:16 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning
- Abstract skim: Reinforcement learning in large or sparse-reward environments suffers from slow temporal-difference reward propagation, as value information spreads only locally across the state space. We propose Mesh-RL, a spatial domain-decomposition framework inspired by the finite element method and domain decomposition theory,...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
