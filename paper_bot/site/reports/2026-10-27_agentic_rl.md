# RL / Post-Training / Agentic RL Reading Queue - 2026-10-27

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 915. Minimum score: 8.

## Top Picks

### 69 - Improving Reasoning with Rollout Agreement for Group-Based Policy Optimization

- arXiv: [2610.34951](https://arxiv.org/abs/2610.34951) | [PDF](https://arxiv.org/pdf/2610.34951) | [papers.cool](https://papers.cool/arxiv/2610.34951)
- Authors: Sohyun Son, Yerim Hong, Jaeyun Park, Mujeen Sung
- Published: 2026-10-26 07:19 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Recent methods for Reinforcement Learning with Verifiable Rewards (RLVR) use rollout diversity to improve reasoning performance or training efficiency. Despite these gains, the extent to which differences among correct-answer rollouts reflect useful alternative reasoning or unresolved errors remains poorly...

### 66 - When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing

- arXiv: [2610.35497](https://arxiv.org/abs/2610.35497) | [PDF](https://arxiv.org/pdf/2610.35497) | [papers.cool](https://papers.cool/arxiv/2610.35497)
- Authors: Lei Zhao, Zongheng Cao, Xinyu Hu
- Published: 2026-10-26 14:25 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, tool use; rl_post_training: reinforcement learning, grpo; reasoning: reasoning, process reward; planning_and_action: planning
- Abstract skim: Reinforcement learning (RL) has shown promise for training multimodal agents to reason and use tools. However, it remains unclear when fine-grained credit assignment improves learning and when it fails to improve task performance. Video editing provides a useful testbed for this question, combining multimodal...

### 60 - Priority-Preserving Advantage Aggregation for Multi-Reward Policy Optimization

- arXiv: [2610.34862](https://arxiv.org/abs/2610.34862) | [PDF](https://arxiv.org/pdf/2610.34862) | [papers.cool](https://papers.cool/arxiv/2610.34862)
- Authors: Xiangchi Yuan, Xingjian Diao, Zheyuan Liu, Chunhui Zhang, Dachuan Shi, Kejing Xia, et al. (10 authors)
- Published: 2026-10-26 05:26 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization, grpo, +1 more; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: LLM post-training often optimizes multiple objectives with unequal priorities, such as correctness and reasoning efficiency. However, the widely used additive reward aggregation in RL can violate these priorities: when primary and auxiliary advantages conflict, a sufficiently large auxiliary signal can overturn the...

### 59 - A Comprehensive Framework for All Stages of Large-Model Training: From Data and Tokenization, through Pretraining, to Post-Training Alignment

- arXiv: [2610.33451](https://arxiv.org/abs/2610.33451) | [PDF](https://arxiv.org/pdf/2610.33451) | [papers.cool](https://papers.cool/arxiv/2610.33451)
- Authors: Xiangjing An, Zhibin Jiao, Aiting Chen
- Published: 2026-10-24 05:09 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlhf, +1 more; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: The capabilities of large language models (LLMs) and multimodal LLMs (MLLMs) arise from the synergy of the full training pipeline, including data and tokenization, pretraining, and post-training (supervised fine-tuning, preference alignment, reinforcement learning, and continual optimization), rather than any...

### 55 - GRASP: Group-Adaptive Hybrid RL-SFT Post-Training for Medical VQA without Reasoning Annotations

- arXiv: [2610.34561](https://arxiv.org/abs/2610.34561) | [PDF](https://arxiv.org/pdf/2610.34561) | [papers.cool](https://papers.cool/arxiv/2610.34561)
- Authors: Wanqi Dong, Wanyue Dong, Jingze Ge, Mehul Motani
- Published: 2026-10-25 21:00 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Adapting general-purpose vision-language models (VLMs) to medical visual question answering (VQA) is valuable for helping clinicians read images and make diagnoses, but annotated data are scarce and provide only short answers, without reasoning annotations. Supervised fine-tuning (SFT) fits these labels but overfits...

### 55 - Self-Evolution Reasoner: Continuous Optimization via Policy-Intrinsic Exploration and Exploitation

- arXiv: [2610.34137](https://arxiv.org/abs/2610.34137) | [PDF](https://arxiv.org/pdf/2610.34137) | [papers.cool](https://papers.cool/arxiv/2610.34137)
- Authors: Wenhang Shi, Yiren Chen, Zhe Zhao, Jinhao Dong, Wei Lu, Xiaoyong Du
- Published: 2026-10-25 08:18 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning, self-improvement, self improvement
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) enables large language models (LLMs) to continuously self-improve their reasoning capabilities. Compared to RLVR's scalar rewards, recent self-supervised on-policy distillation methods leverage denser supervision signals. However, both paradigms suffer from...

### 54 - Intervention-Certified Amplification: A Validity Gate for $σ$-Weighted Post-Training

- arXiv: [2610.33882](https://arxiv.org/abs/2610.33882) | [PDF](https://arxiv.org/pdf/2610.33882) | [papers.cool](https://papers.cool/arxiv/2610.33882)
- Authors: Leiyue Chen, Meng Wei, Xuefeng Hu, Wei Liu
- Published: 2026-10-24 19:49 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Hybrid post-training often mixes supervised fine-tuning (SFT) and reinforcement learning (RL), using training-side signals to set each sample's balance. Such signals characterize the anchor data and policy, but not whether the emphasized behavior helps in the target task and evaluation setting. This mismatch can...

### 53 - Learning When to Collaborate: Selective Multi-Agent Medical Reasoning via Uncertainty-Aware Routing

- arXiv: [2610.33544](https://arxiv.org/abs/2610.33544) | [PDF](https://arxiv.org/pdf/2610.33544) | [papers.cool](https://papers.cool/arxiv/2610.33544)
- Authors: Jiacheng Hou, Xueliang Cui, Dan Lu, Ruxin Wang
- Published: 2026-10-24 08:39 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reward model, grpo; reasoning: reasoning, deliberation
- Abstract skim: Multi-agent systems have emerged as a promising paradigm for multimodal medical reasoning, but existing methods rely on two assumptions that hinder practical deployment: (i) always-active dense collaboration among multiple agents, and (ii) dependence on large cloud-based models that raise privacy and efficiency...

### 49 - Of Chains and Gains: What Reinforcement Learning changes on Reasoning-based Image Quality Assessment

- arXiv: [2610.33203](https://arxiv.org/abs/2610.33203) | [PDF](https://arxiv.org/pdf/2610.33203) | [papers.cool](https://papers.cool/arxiv/2610.33203)
- Authors: Yixuan Li, Yuxuan Jiang, Hanwei Zhu, Hancheng Zhu, Fan Zhang, Shiqi Wang, et al. (7 authors)
- Published: 2026-10-23 18:49 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) has improved the performance of large Vision-Language Models (VLMs) on image quality assessment (IQA). Existing approaches often attribute these gains to improved reasoning before scoring, supported by increasingly plausible Chain-of-Thought (CoT). However,...

### 48 - S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning

- arXiv: [2610.35518](https://arxiv.org/abs/2610.35518) | [PDF](https://arxiv.org/pdf/2610.35518) | [papers.cool](https://papers.cool/arxiv/2610.35518)
- Authors: Shuo Shen, Guangran Cheng, Chengqi Lyu, Xiangsen Wang, Yanan Sun, Wenwei Zhang
- Published: 2026-10-26 14:38 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: rollout
- Abstract skim: Critic-free methods are widely used in reinforcement learning with verifiable rewards (RLVR) for long chain-of-thought (CoT) reasoning, avoiding difficult and costly critic training. Common alternatives lack token-level credit assignment and typically rely on grouped rollouts to estimate prompt-specific baselines. A...

### 47 - Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution

- arXiv: [2610.35733](https://arxiv.org/abs/2610.35733) | [PDF](https://arxiv.org/pdf/2610.35733) | [papers.cool](https://papers.cool/arxiv/2610.35733)
- Authors: Zhenshuo Zhang, Ruoxuan Xiong, Hongyang R. Zhang
- Published: 2026-10-26 16:52 UTC | Categories: cs.AI, cs.LG, cs.MA, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Multi-objective reinforcement learning is a fundamental problem for modern AI, with applications spanning post-training, reasoning models, and robotic control. A central challenge is to learn policies that balance competing objectives, such as helpfulness versus honesty in safety and alignment, or speed versus...

### 45 - FOCUS: Active Critic Learning for Long-Horizon Language Model Agents

- arXiv: [2610.35801](https://arxiv.org/abs/2610.35801) | [PDF](https://arxiv.org/pdf/2610.35801) | [papers.cool](https://papers.cool/arxiv/2610.35801)
- Authors: Zhengping Jiang, William Jurayj, Liaoyaqi Wang, Chunsheng Zuo, Anqi Liu, Benjamin Van Durme
- Published: 2026-10-26 17:34 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Sparse outcome rewards make it difficult for long-horizon language-model agents to assign credit to earlier actions. Learned critics provide value estimates for intermediate states, but these estimates can be inaccurate, while estimating intermediate values with repetitive continuation samples from points within a...

### 45 - Audio-R1: Audio Reasoning through Reinforcement Learning on Self-Supervised Tasks

- arXiv: [2610.34609](https://arxiv.org/abs/2610.34609) | [PDF](https://arxiv.org/pdf/2610.34609) | [papers.cool](https://papers.cool/arxiv/2610.34609)
- Authors: Jihoon Jeong, Mirco Ravanelli, Zhepei Wang, Cem Subakan
- Published: 2026-10-25 22:17 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Reasoning is increasingly important for large audio-language models (LALMs), yet remains relatively underexplored compared with text-only and vision-language models. We introduce Audio-R1, a reinforcement learning (RL) post-training framework that revisits audio self-supervised learning as a source of verifiable...

### 44 - EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation

- arXiv: [2610.35690](https://arxiv.org/abs/2610.35690) | [PDF](https://arxiv.org/pdf/2610.35690) | [papers.cool](https://papers.cool/arxiv/2610.35690)
- Authors: Yitao Xiao, Xu Zhang, Ye Cheng, Shaoyong Guo, Yan Sun, Ziyue Zhu, et al. (9 authors)
- Published: 2026-10-26 16:21 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: self-improvement, self improvement; planning_and_action: planning
- Abstract skim: Serving web queries at scale with multi-agent systems requires jointly configuring large language models, collaboration modes, agent counts, interaction rounds, and skills. However, the resulting configuration space grows combinatorially, while sparse execution rewards provide limited fine-grained supervision for...

### 43 - Test-Time Confidence Adaptation under RL-Induced Trajectory Shift

- arXiv: [2610.35500](https://arxiv.org/abs/2610.35500) | [PDF](https://arxiv.org/pdf/2610.35500) | [papers.cool](https://papers.cool/arxiv/2610.35500)
- Authors: Zhenzhen Ren, Xiaoqing Zhang, GuoBiao Li, Bowen Fang, Yanxi Wang, Xinpeng Zhang, et al. (7 authors)
- Published: 2026-10-26 14:27 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Trajectory-based confidence estimation has shown promising performance for large language models (LLMs) by leveraging rich signals from their reasoning processes. However, we find that such confidence estimators can degrade substantially after agentic reinforcement learning (Agentic RL) as it induces substantial...

### 43 - Movable-Element Multi-Functional RIS-Assisted Hybrid RSMA-NOMA: A Constrained Hybrid Reinforcement Learning Approach

- arXiv: [2610.34701](https://arxiv.org/abs/2610.34701) | [PDF](https://arxiv.org/pdf/2610.34701) | [papers.cool](https://papers.cool/arxiv/2610.34701)
- Authors: Li-Hsiang Shen, Chi-Te Kuo
- Published: 2026-10-26 01:46 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization; reasoning: reflection; downranked: wireless
- Abstract skim: In this work, we propose a movable-element (ME) multi-functional reconfigurable intelligent surface (MF-RIS) architecture, termed MM-RIS, which integrates element mobility with adaptive signal reflection, transmission, amplification, and energy harvesting (EH) to enhance communication flexibility and energy self-...

### 40 - Correlation-Aware Exploration for Long-Trace Reasoning

- arXiv: [2610.34949](https://arxiv.org/abs/2610.34949) | [PDF](https://arxiv.org/pdf/2610.34949) | [papers.cool](https://papers.cool/arxiv/2610.34949)
- Authors: Junxing Hu, Zicheng Zhang, Zhiqian Zhang, Ai Han, Yifeng Zhang, Pengzhang Liu, et al. (7 authors)
- Published: 2026-10-26 07:19 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reasoning models trained with Group Relative Policy Optimization (GRPO) now produce chains of thought thousands of tokens long, and recent studies reveal that such training is prone to policy collapse. Entropy regularization is the standard remedy, but it works by pushing probability mass away from the few tokens...

### 40 - How Does Post-Training Shape LLM Value Preferences?

- arXiv: [2610.33371](https://arxiv.org/abs/2610.33371) | [PDF](https://arxiv.org/pdf/2610.33371) | [papers.cool](https://papers.cool/arxiv/2610.33371)
- Authors: Yang Liu, Shaoyang Xu, Masahiro Kaneko, Chengzhi Zhong, Wenxuan Zhang, Chenhui Chu
- Published: 2026-10-23 23:52 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, grpo, dpo
- Abstract skim: During post-training, large language models (LLMs) learn value preferences from corpora that may contain imbalanced proportions of opinions associated with different demographic groups. Amplifying these imbalances may further underrepresent some groups' opinions. However, how opinion mixtures shape value preferences...

### 39 - InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL

- arXiv: [2610.35303](https://arxiv.org/abs/2610.35303) | [PDF](https://arxiv.org/pdf/2610.35303) | [papers.cool](https://papers.cool/arxiv/2610.35303)
- Authors: Yingbo Hao, Song Liu, Guanghua Yu, Zhaojing Zhou, Jianchen Zhu, Yi Zou
- Published: 2026-10-26 12:08 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: alfworld, scienceworld
- Abstract skim: Multi-turn agent reinforcement learning (RL) relies on long closed-loop rollouts, making generation and KV-cache costs a major bottleneck. Quantized rollout reduces these costs, but its low-precision executor also serves as the behavior policy and can induce execution mismatch with the learner. Existing quantized-RL...

### 39 - ClinVerse: A Realistic Multi-Agent Diagnostic Environment for Training and Evaluating Medical Agents

- arXiv: [2610.34878](https://arxiv.org/abs/2610.34878) | [PDF](https://arxiv.org/pdf/2610.34878) | [papers.cool](https://papers.cool/arxiv/2610.34878)
- Authors: Sirry Chen, Fangke Chen, Xuanwen Ding, Wei Chen, Zhongyu Wei
- Published: 2026-10-26 05:50 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent, agent training, agent environment; planning_and_action: trajectory, environment feedback, decision making; memory_and_benchmarks: evaluation
- Abstract skim: Disease diagnosis is a key application of large language model (LLM) agents in healthcare. However, existing medical agents are primarily trained and evaluated with static question-answering data, providing limited opportunities to learn active information acquisition, examination decision-making, and dynamic...

### 39 - BE-CTDE: Blockchain-Enabled Multi-Agent Reinforcement Learning with Anomaly Detection and Token Economics

- arXiv: [2610.34121](https://arxiv.org/abs/2610.34121) | [PDF](https://arxiv.org/pdf/2610.34121) | [papers.cool](https://papers.cool/arxiv/2610.34121)
- Authors: Chih-Wei Huang, Hsin-Chieh Lee, Yun-Chen Yu, Ibrahim Althamary, Rongxing Lu, Phone Lin
- Published: 2026-10-25 07:39 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: decision making
- Abstract skim: Multi-agent reinforcement learning supports cooperative decision-making in Internet of Things systems, but strategic deviations can disrupt coordination and undermine confidence in the training process. This paper proposes Blockchain-Enabled Centralized Training and Decentralized Execution (BE-CTDE), which uses...

### 38 - HA-DiPO: Diffusion Policy Optimization for Heterogeneous Cooperative Transport

- arXiv: [2610.33584](https://arxiv.org/abs/2610.33584) | [PDF](https://arxiv.org/pdf/2610.33584) | [papers.cool](https://papers.cool/arxiv/2610.33584)
- Authors: Xuebin Li, Jinpeng Xiao, Zong Chen, Pierluigi Arpenti, Bruno Siciliano, Jiebao Sun, et al. (7 authors)
- Published: 2026-10-24 10:24 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization
- Abstract skim: Cooperative transport with heterogeneous legged robots requires coordinating different motion capabilities while supporting an unfixed shared payload. We present HA-DiPO (Heterogeneous-Agent Diffusion Policy Optimization), a hierarchical multi-agent reinforcement learning framework under centralized training with...

### 37 - RSI Arena: Towards Recursive Self-Improvement with Human Feedback

- arXiv: [2610.33624](https://arxiv.org/abs/2610.33624) | [PDF](https://arxiv.org/pdf/2610.33624) | [papers.cool](https://papers.cool/arxiv/2610.33624)
- Authors: Yue Huang, Yanbo Wang, Lichi Li, Yuanyuan Chen, Andreas Haupt, Xiaonan Luo, et al. (18 authors)
- Published: 2026-10-24 11:54 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as training agents, each starting from NVIDIA Nemotron 3.5 Lightning 30B-A3B...

### 36 - Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning

- arXiv: [2610.35736](https://arxiv.org/abs/2610.35736) | [PDF](https://arxiv.org/pdf/2610.35736) | [papers.cool](https://papers.cool/arxiv/2610.35736)
- Authors: Qiyue Xia, J. Michael Herrmann
- Published: 2026-10-26 16:53 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Multi-objective multi-agent reinforcement learning (MOMARL) addresses agent coordination and objective trade-offs simultaneously while optimising overall system performance. Existing work tends to treat multi-agent cooperation and multi-objective optimisation as largely independent components of a learning problem,...

### 35 - Humans in Space: Can MLLMs Construct Human-Centric Spatial Understanding via Active Exocentric Exploration?

- arXiv: [2610.34149](https://arxiv.org/abs/2610.34149) | [PDF](https://arxiv.org/pdf/2610.34149) | [papers.cool](https://papers.cool/arxiv/2610.34149)
- Authors: Tianchen Guo, Tengyue Zhang, Chen Liu, Ling Chen, Xin Yu
- Published: 2026-10-25 08:35 UTC | Categories: cs.CL
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: While Multimodal Large Language Models (MLLMs) excel at zero-shot reasoning, their spatial capabilities are primarily evaluated through static, passive observation. In complex, human-centric scenes, occlusion often hides crucial geometric evidence, and passive benchmarks force models to guess rather than recognize...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
