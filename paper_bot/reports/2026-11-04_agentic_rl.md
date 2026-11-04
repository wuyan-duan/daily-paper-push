# RL / Post-Training / Agentic RL Reading Queue - 2026-11-04

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 504. Minimum score: 8.

## Top Picks

### 72 - JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks

- arXiv: [2611.05263](https://arxiv.org/abs/2611.05263) | [PDF](https://arxiv.org/pdf/2611.05263) | [papers.cool](https://papers.cool/arxiv/2611.05263)
- Authors: Shanka Subhra Mondal, Jiayun Wang
- Published: 2026-11-03 17:49 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; planning_and_action: planning, rollout; memory_and_benchmarks: webarena
- Abstract skim: Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer high-level plans, navigate through...

### 52 - Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning

- arXiv: [2611.05266](https://arxiv.org/abs/2611.05266) | [PDF](https://arxiv.org/pdf/2611.05266) | [papers.cool](https://papers.cool/arxiv/2611.05266)
- Authors: Kevin Frans, Alexander M Rush, Sergey Levine, Pieter Abbeel, Ashvin Nair
- Published: 2026-11-03 17:54 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time, rewards in modern post-training systems often come from rich textual sources, e.g. judge models with a rubric of criteria. Can we...

### 42 - Training LLM Agents to Automate LLM Post-Training with RSI-Dojo

- arXiv: [2611.03698](https://arxiv.org/abs/2611.03698) | [PDF](https://arxiv.org/pdf/2611.03698) | [papers.cool](https://papers.cool/arxiv/2611.03698)
- Authors: Shuzheng Gao, Zhaojian Yu, Penghao Yin, Yuling Shi, Kai Cai, Shilin He, et al. (7 authors)
- Published: 2026-10-29 10:27 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Recursive Self-Improvement (RSI) aims to enable AI systems to autonomously build and improve AI systems themselves, including models, harnesses, and underlying infrastructure. Within this broader agenda, a central capability is enabling agents to train and improve base models. However, existing studies on automated...

### 41 - On the Primacy Bias in RLVR Training

- arXiv: [2611.04061](https://arxiv.org/abs/2611.04061) | [PDF](https://arxiv.org/pdf/2611.04061) | [papers.cool](https://papers.cool/arxiv/2611.04061)
- Authors: Phuc Minh Nguyen, Ngoc-Hieu Nguyen, Parshin Shojaee, Chinh Duc La, Duy Minh Ho Nguyen, Rui Zhang, et al. (9 authors)
- Published: 2026-11-02 23:04 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, verifiable reward; reasoning: reasoning
- Abstract skim: Reinforcement Learning with Verifiable Reward (RLVR) has emerged as a promising approach for enhancing the reasoning capabilities of large language models. However, it still remains unclear whether RLVR can extend reasoning capabilities beyond what is already encoded in the base model. In this paper, we study this...

### 38 - Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards

- arXiv: [2611.04774](https://arxiv.org/abs/2611.04774) | [PDF](https://arxiv.org/pdf/2611.04774) | [papers.cool](https://papers.cool/arxiv/2611.04774)
- Authors: Yasaman Zolfimoselo, Nikolas Geroliminis, Maryam Kamgarpour
- Published: 2026-11-03 12:14 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: trajectory; downranked: traffic
- Abstract skim: We study cooperative multi-agent reinforcement learning with decoupled dynamics and a monotone submodular reward function over joint trajectories. Due to the non-additive reward, an optimal policy may depend on the history of all agents. This dependence makes exact optimization exponential in the horizon and the...

### 37 - RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training

- arXiv: [2611.04368](https://arxiv.org/abs/2611.04368) | [PDF](https://arxiv.org/pdf/2611.04368) | [papers.cool](https://papers.cool/arxiv/2611.04368)
- Authors: Shresth Grover, Andrey Kolobov, Dhruv Shah
- Published: 2026-11-03 05:56 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions. We introduce reasoning-aligned fine-tuning (RAFT), a two-stage post-training procedure: RAFT first...

### 35 - FourSight: Stable FP4 RL Post-Training via Sequence Filtering and Sparse Channel Compensation

- arXiv: [2611.04887](https://arxiv.org/abs/2611.04887) | [PDF](https://arxiv.org/pdf/2611.04887) | [papers.cool](https://papers.cool/arxiv/2611.04887)
- Authors: Yining Wei, Tianyuan Wu, Gu Gong, Yuechen Tao, Yinghao Yu, Xiaowen Chu, et al. (7 authors)
- Published: 2026-11-03 13:33 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) post-training increasingly targets low-bit deployment, with NVFP4 weight-and activation quantization (W4A4) becoming the state-of-the-practice format. However, integrating NVFP4 into RL degrades rollout quality and amplifies cross-engine training-inference mismatch (TIM), destabilizing...

### 35 - Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training

- arXiv: [2611.04873](https://arxiv.org/abs/2611.04873) | [PDF](https://arxiv.org/pdf/2611.04873) | [papers.cool](https://papers.cool/arxiv/2611.04873)
- Authors: Zicheng Kong, Zhenbo Xu, Haoyan Zhang, Jinghan Yang, Zhenzhen Li, Yiwei Ru, et al. (10 authors)
- Published: 2026-11-03 13:26 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reward model; planning_and_action: trajectory
- Abstract skim: Video world models enable candidate actions to be evaluated through imagined outcomes, but high predicted rewards can favor trajectories with poor execution quality. We introduce Trusting Imagined Futures (TIF), an offline supervision selection method for vision-language-action (VLA) post-training that audits...

### 33 - Self-Privileged Fine-Tuning

- arXiv: [2611.04632](https://arxiv.org/abs/2611.04632) | [PDF](https://arxiv.org/pdf/2611.04632) | [papers.cool](https://papers.cool/arxiv/2611.04632)
- Authors: Yangrong Hu, Xueyu Zhou, Yue Wu, Jian Huang
- Published: 2026-11-03 10:21 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Supervised fine-tuning (SFT) is a key component of language model post-training, enabling effective task adaptation and serving as an important foundation for subsequent reinforcement learning. Recent methods seek to improve SFT by introducing token-level weights into the training objective, where these weights are...

### 32 - Safeguarding Multi-Agent Reinforcement Learning for Connected and Automated Vehicles with Recursively Feasible Control Barrier Functions

- arXiv: [2611.04957](https://arxiv.org/abs/2611.04957) | [PDF](https://arxiv.org/pdf/2611.04957) | [papers.cool](https://papers.cool/arxiv/2611.04957)
- Authors: Jianye Xu, Yousef Sayed, Bassam Alrifaee
- Published: 2026-11-03 14:16 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: traffic
- Abstract skim: Multi-Agent Reinforcement Learning (MARL) shows promise in coordinating connected and automated vehicles but offers no safety guarantee. Although Control Barrier Functions (CBFs) can add this guarantee, their optimization problem can become infeasible in practice due to control bounds. Moreover, they often...

### 32 - ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement

- arXiv: [2611.04787](https://arxiv.org/abs/2611.04787) | [PDF](https://arxiv.org/pdf/2611.04787) | [papers.cool](https://papers.cool/arxiv/2611.04787)
- Authors: Yao Cui, Zhen Yang, Yuandong Wang, Yangfu Zhu, Tianyu Wo, Zhenzhou Shao
- Published: 2026-11-03 12:25 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has become an effective approach for improving mathematical reasoning in large language models. However, a fundamental question remains: when a model fails to solve a problem, does it truly lack the underlying capability? In this work, we reveal that direct...

### 31 - Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training

- arXiv: [2611.04277](https://arxiv.org/abs/2611.04277) | [PDF](https://arxiv.org/pdf/2611.04277) | [papers.cool](https://papers.cool/arxiv/2611.04277)
- Authors: Kangning Zhang, Wenxiang Jiao, Bowen Fang, Shuai Shao, Jiachen Zhu, Rong Shan, et al. (11 authors)
- Published: 2026-11-03 04:03 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failures of a base execution system...

### 30 - Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs

- arXiv: [2611.04376](https://arxiv.org/abs/2611.04376) | [PDF](https://arxiv.org/pdf/2611.04376) | [papers.cool](https://papers.cool/arxiv/2611.04376)
- Authors: Hei Yi Mak, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Huan Lin, Zhengzhi Tang, et al. (11 authors)
- Published: 2026-11-03 06:03 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models. Recent work on FP4 RL has introduced effective recovery recipes that restore accuracy under aggressive low-precision quantization for dense models, but we find that the same approach...

### 30 - Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies

- arXiv: [2611.04072](https://arxiv.org/abs/2611.04072) | [PDF](https://arxiv.org/pdf/2611.04072) | [papers.cool](https://papers.cool/arxiv/2611.04072)
- Authors: Yizhou Zhang, Yashaswini Murthy, Laixi Shi, Adam Vierman
- Published: 2026-11-02 23:34 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization
- Abstract skim: We study the problem of average reward Multi-Agent Reinforcement Learning (MARL) where agents interact within a network. Each agent in the network conducts local updates with information within its $k$-hop neighborhood and collaboratively maximizes the overall reward of the entire network. We first provide...

### 29 - Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning

- arXiv: [2611.04819](https://arxiv.org/abs/2611.04819) | [PDF](https://arxiv.org/pdf/2611.04819) | [papers.cool](https://papers.cool/arxiv/2611.04819)
- Authors: Huilin He, Weiyu Han, Linbo Shao, Ruobing Zuo, Xiao Tan, Shuai Chen, et al. (7 authors)
- Published: 2026-11-03 12:47 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Payment fraud causes financial losses and undermines users' trust in web payment services. Although fraud detection is a critical defense for payment security, complex and diverse fraudulent behaviors can still evade detection. Generating fraud samples for data augmentation can broaden detectors' coverage of...

### 29 - Think Less, Locally: Local Preference Learning for Reasoning Compression

- arXiv: [2611.04814](https://arxiv.org/abs/2611.04814) | [PDF](https://arxiv.org/pdf/2611.04814) | [papers.cool](https://papers.cool/arxiv/2611.04814)
- Authors: Muyao Yuan, Liyan Xu, Weizhan Zhang, Muyan Jiao, Jiangnan Li, Jinchao Zhang, et al. (7 authors)
- Published: 2026-11-03 12:44 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: dpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Large reasoning models achieve strong performance on challenging tasks, but their long chain-of-thought often incurs substantial inference costs by continuing to deliberate after sufficient information has been obtained. Existing reasoning compression methods primarily operate on reasoning trajectories, paying less...

### 27 - PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations

- arXiv: [2611.04870](https://arxiv.org/abs/2611.04870) | [PDF](https://arxiv.org/pdf/2611.04870) | [papers.cool](https://papers.cool/arxiv/2611.04870)
- Authors: Travis Davies, Wentao Ma, Lihao Guo, Tengfei Ma, Xiaowen Chang, Jiafeng Xu, et al. (13 authors)
- Published: 2026-11-03 13:25 UTC | Categories: cs.RO
- Why it matched: rl_post_training: policy optimization, grpo; planning_and_action: rollout, world model; memory_and_benchmarks: memory
- Abstract skim: A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views, and sustain coherent long-horizon rollouts. We present PrimeSim, an action-conditioned, multiview world model simulator that addresses...

### 27 - Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling

- arXiv: [2611.04792](https://arxiv.org/abs/2611.04792) | [PDF](https://arxiv.org/pdf/2611.04792) | [papers.cool](https://papers.cool/arxiv/2611.04792)
- Authors: Ria Shekhawat, Abhijeet Sinha, Yingtao Zhu, Dianbo Liu
- Published: 2026-11-03 12:29 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; planning_and_action: rollout
- Abstract skim: Reinforcement learning objectives that maximize expected return can concentrate probability mass on a small subset of high-reward outcomes, limiting diversity when multiple distinct solutions are desirable. We introduce Density-Aware Reward Scaling (DARS), a simple reward-processing mechanism that promotes reward-...

### 27 - ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems

- arXiv: [2611.04321](https://arxiv.org/abs/2611.04321) | [PDF](https://arxiv.org/pdf/2611.04321) | [papers.cool](https://papers.cool/arxiv/2611.04321)
- Authors: Maisha Maliha, Vishal Pramanik, Sumit Kumar Jha
- Published: 2026-11-03 04:57 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; planning_and_action: planning, trajectory; memory_and_benchmarks: memory
- Abstract skim: Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turns, however, an agent can produce a...

### 27 - Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI

- arXiv: [2611.04315](https://arxiv.org/abs/2611.04315) | [PDF](https://arxiv.org/pdf/2611.04315) | [papers.cool](https://papers.cool/arxiv/2611.04315)
- Authors: Vishal Pramanik, Maisha Maliha, Susmit Jha, Sumit Kumar Jha
- Published: 2026-11-03 04:46 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent, tool use; planning_and_action: acting; memory_and_benchmarks: memory
- Abstract skim: Long-horizon multi-agent systems suffer from three tightly coupled failures: task drift, role drift, and state staleness. We test the hypothesis that these share a common representational cause: agent hidden states move away from the directions encoding the active task, assigned role, and current shared state. A...

### 26 - MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution

- arXiv: [2611.05313](https://arxiv.org/abs/2611.05313) | [PDF](https://arxiv.org/pdf/2611.05313) | [papers.cool](https://papers.cool/arxiv/2611.05313)
- Authors: Dian Jin, Jinluan Yang, Kairong Han, Baohong Li, Zijing Hu, Yi He, et al. (12 authors)
- Published: 2026-11-03 18:19 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: memory, alfworld
- Abstract skim: Skill memories encode past experiences as textual prompts to improve reinforcement learning (RL) for self-evolving agents. Complementing RL, On-Policy Self-Distillation (OPSD) provides dense, fine-grained supervision to internalize knowledge from skill-guided trajectories and accelerate policy learning. However,...

### 26 - Feeling of Knowing in Large Language Models

- arXiv: [2611.04834](https://arxiv.org/abs/2611.04834) | [PDF](https://arxiv.org/pdf/2611.04834) | [papers.cool](https://papers.cool/arxiv/2611.04834)
- Authors: Zichuan Fu, Xian Wu, Jingtong Gao, Wenlin Zhang, Jiaxuan Li, Binhao Wang, et al. (12 authors)
- Published: 2026-11-03 13:04 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization; memory_and_benchmarks: evaluation
- Abstract skim: Post-training updates change what large language models (LLMs) can answer, but may leave their answerability judgments misaligned. We study this knowledge-judgment desynchronization through functional feeling of knowing (FoK), which supports selective generation, retrieval triggering, and model routing without...

### 26 - When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation

- arXiv: [2611.04289](https://arxiv.org/abs/2611.04289) | [PDF](https://arxiv.org/pdf/2611.04289) | [papers.cool](https://papers.cool/arxiv/2611.04289)
- Authors: Qinghua Mao, Xi Lin, Yuxin Qi, Zihao Xu, Jinze Gu, Yuliang Chen
- Published: 2026-11-03 04:16 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: deliberation; memory_and_benchmarks: evaluation
- Abstract skim: Retrieval-augmented Web applications increasingly employ multi-agent debate (MAD) to aggregate conflicting, noisy, and heterogeneous information, yet deliberation is fundamentally a social process susceptible to interpersonal dynamics. When retrieved Web sources contain latent hazards alongside safe factual content,...

### 26 - AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data

- arXiv: [2611.03815](https://arxiv.org/abs/2611.03815) | [PDF](https://arxiv.org/pdf/2611.03815) | [papers.cool](https://papers.cool/arxiv/2611.03815)
- Authors: Yueh-Hua Wu, Kei Ota, Hanlong Li, Hayata Yuasa, Jason Wang, Kengo Ikeuchi, et al. (20 authors)
- Published: 2026-11-02 19:00 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; memory_and_benchmarks: evaluation
- Abstract skim: AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage. The demonstrations are recorded with YUBI, our open-source handheld gripper, which lets people record manipulation data anywhere with no robot present. From a single...

### 25 - GeoFaham: Domain-Specialized Multi-Agent Geospatial Analytics for Disaster Response

- arXiv: [2611.04977](https://arxiv.org/abs/2611.04977) | [PDF](https://arxiv.org/pdf/2611.04977) | [papers.cool](https://papers.cool/arxiv/2611.04977)
- Authors: Muhammad Sohail Danish, Gilles Q. Hacheme, Akram Zaytar, Satej S. Soman, Inbal Becker-Reshef, Juan Lavista Ferres, et al. (8 authors)
- Published: 2026-11-03 14:32 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Real-world geospatial decision support requires more than single-step retrieval or code generation. Disaster-response questions often involve multi-source workflows that combine spatial databases, map-derived features, satellite imagery, raster products, and reusable geospatial artifacts, where correctness depends...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
