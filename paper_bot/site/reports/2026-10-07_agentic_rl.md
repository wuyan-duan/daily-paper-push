# RL / Post-Training / Agentic RL Reading Queue - 2026-10-07

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 725. Minimum score: 8.

## Top Picks

### 68 - RIWANav: Recursive World-Action Models with Self-Improvement for Urban Navigation

- arXiv: [2610.08640](https://arxiv.org/abs/2610.08640) | [PDF](https://arxiv.org/pdf/2610.08640) | [papers.cool](https://papers.cool/arxiv/2610.08640)
- Authors: Jing Xie, Shouwei Ruan, Yubin Wang, Yuxiang Zhang, Haitao Yang, Songchang Jin, et al. (7 authors)
- Published: 2026-10-06 16:33 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; reasoning: self-improvement, self improvement; planning_and_action: world model
- Abstract skim: Long-horizon urban navigation requires sequential local decisions whose errors can compound over time. Imitation learning (IL) rarely learns from failures, while physical trial-and-error reinforcement learning (RL) is costly. Action-conditioned world models can provide imagined feedback by predicting visual...

### 62 - Independent Multi-Agent Reinforcement Learning with Counterfactual Semantic-Social World Models

- arXiv: [2610.07704](https://arxiv.org/abs/2610.07704) | [PDF](https://arxiv.org/pdf/2610.07704) | [papers.cool](https://papers.cool/arxiv/2610.07704)
- Authors: Fernando Martinez, Tao Li, Yingdong Lu, Juntao Chen
- Published: 2026-10-06 03:53 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, ppo; planning_and_action: trajectory, rollout, world model; memory_and_benchmarks: benchmark
- Abstract skim: Fully decentralized multi-agent reinforcement learning (MARL), also referred to as independent learning, requires each agent to learn and act using only its local information and experience, without a centralized critic or inter-agent communication. Such a stringent information structure renders the conventional...

### 61 - What pass@k Cannot Measure: Evaluating Diversity and Capability Retention after Post-Training

- arXiv: [2610.07405](https://arxiv.org/abs/2610.07405) | [PDF](https://arxiv.org/pdf/2610.07405) | [papers.cool](https://papers.cool/arxiv/2610.07405)
- Authors: Subham Rath, Raj Dandekar, Rajat Dandekar, Sreedath Panat
- Published: 2026-10-05 21:16 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: pass@$k$, the fraction of problems a model solves within $k$ sampled attempts, is the field's default protocol for deciding whether reinforcement-learning (RL) post-training on verifiable rewards improved a model. At the population level, pass@$k$ depends only on a problem's probability of a correct sample, with no...

### 55 - Structuring MoE Expert Selection for Agentic Reinforcement Learning

- arXiv: [2610.07332](https://arxiv.org/abs/2610.07332) | [PDF](https://arxiv.org/pdf/2610.07332) | [papers.cool](https://papers.cool/arxiv/2610.07332)
- Authors: Bolian Li, Ting-Yao Hu, Cheng-Yu Hsieh, Sanjoy Chowdhury, Oncel Tuzel, Raviteja Vemulapalli
- Published: 2026-10-05 20:06 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: post-training, post training, reinforcement learning; planning_and_action: trajectory
- Abstract skim: Long-horizon LLM agents are frequently implemented using sparse mixture-of-experts (MoE) models, yet the co-design of agentic behavior and MoE structures remains underexplored. In this work, we comprehensively study the connections between agentic post-training and MoE expert selection. In off-the-shelf MoE models,...

### 53 - Reinforcement Learning for Hierarchical Reasoning Rewards: Minimax-Optimal Rates with Transformers

- arXiv: [2610.08561](https://arxiv.org/abs/2610.08561) | [PDF](https://arxiv.org/pdf/2610.08561) | [papers.cool](https://papers.cool/arxiv/2610.08561)
- Authors: Naoki Nishikawa, Taiji Suzuki
- Published: 2026-10-06 15:43 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL) has become a standard tool for post-training language models on reasoning tasks, where the policy is updated by reward feedback while exploring the space of responses. Despite its empirical success, theoretical understanding of RL post-training remains limited, in particular of why on-...

### 52 - VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning

- arXiv: [2610.08761](https://arxiv.org/abs/2610.08761) | [PDF](https://arxiv.org/pdf/2610.08761) | [papers.cool](https://papers.cool/arxiv/2610.08761)
- Authors: Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng, Boyi Li, et al. (13 authors)
- Published: 2026-10-06 17:50 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: agent harness; rl_post_training: policy optimization; reasoning: reasoning, self-improvement, self improvement; planning_and_action: decision making; memory_and_benchmarks: evaluation; downranked: driving
- Abstract skim: Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied...

### 49 - FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents

- arXiv: [2610.07898](https://arxiv.org/abs/2610.07898) | [PDF](https://arxiv.org/pdf/2610.07898) | [papers.cool](https://papers.cool/arxiv/2610.07898)
- Authors: Jia Liufu, Bin Hu, Linglin Jing, Terry Kong, Yuki Huang, Ashwath Aithal, et al. (8 authors)
- Published: 2026-10-06 07:44 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; planning_and_action: trajectory
- Abstract skim: Repository-level software engineering (SWE) is a challenging long-horizon setting: agents must reason over extended interactions, use tools, and adapt to stateful environments. Recent work trains SWE agents with reinforcement learning methods such as Group Relative Policy Optimization (GRPO), which independently...

### 49 - TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models

- arXiv: [2610.07767](https://arxiv.org/abs/2610.07767) | [PDF](https://arxiv.org/pdf/2610.07767) | [papers.cool](https://papers.cool/arxiv/2610.07767)
- Authors: Xin Wang, Hao Yu, Zhengyang Zhuge, Bochao Mao, Zheng Li, Junda Feng, et al. (12 authors)
- Published: 2026-10-06 05:03 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL methods suffer from a key limitation: they primarily optimize quantization...

### 43 - Learning to Retrieve via Reinforcement Learning in Embedding Space

- arXiv: [2610.07731](https://arxiv.org/abs/2610.07731) | [PDF](https://arxiv.org/pdf/2610.07731) | [papers.cool](https://papers.cool/arxiv/2610.07731)
- Authors: Qi Liu, Fengming Liang, Yiqun Chen, Erhan Zhang, Jiaxin Mao
- Published: 2026-10-06 04:29 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Dense retrieval models are typically trained with contrastive objectives that learn effective representations but do not directly optimize retrieval metrics or downstream task performance. To address this problem, we introduce RELER (REinforcement LEarning for Retrieval), a reinforcement learning framework that...

### 41 - Enhancing Diffusion Language Models with Autoregressive Post-Training Weights

- arXiv: [2610.08108](https://arxiv.org/abs/2610.08108) | [PDF](https://arxiv.org/pdf/2610.08108) | [papers.cool](https://papers.cool/arxiv/2610.08108)
- Authors: Yiming Qin, Ke Wang, Amel Abdelraheem, Adam Hazimeh, Pascal Frossard
- Published: 2026-10-06 10:31 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Diffusion language models (dLLMs) have emerged as a promising alternative to autoregressive (AR) language models, offering flexible token-update orders and parallel decoding. Recent dLLMs are often initialized from pretrained AR models before diffusion conversion in order to inherit their learned representations....

### 41 - DHCG: Dynamic Construction of Hierarchical Collaboration Graphs for LLM-Based Multi-Agent Reasoning

- arXiv: [2610.07835](https://arxiv.org/abs/2610.07835) | [PDF](https://arxiv.org/pdf/2610.07835) | [papers.cool](https://papers.cool/arxiv/2610.07835)
- Authors: Jie Ren, Jiakang Yuan, Chenyu Huang, Hezeer Ma, Jiayuan Fan, Tao Chen
- Published: 2026-10-06 06:33 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: preference optimization; reasoning: reasoning
- Abstract skim: LLM-based multi-agent systems (MAS) have demonstrated strong capabilities in solving complex problems across diverse domains. Recently, the dynamic orchestration of agent systems has become an important research direction. However, existing methods suffer from limited composition, misaligned dependencies, and...

### 41 - Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding

- arXiv: [2610.07342](https://arxiv.org/abs/2610.07342) | [PDF](https://arxiv.org/pdf/2610.07342) | [papers.cool](https://papers.cool/arxiv/2610.07342)
- Authors: Hoang Phan, Minh Pham, Chau Pham, Chinmay Hegde, Trung Le, Qi Lei
- Published: 2026-10-05 20:15 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning
- Abstract skim: On-policy reinforcement learning has become a central paradigm for improving the reasoning abilities of large language models. However, its effectiveness is often limited by reward sparsity: when a model fails to discover correct trajectories for difficult problems, the optimization process receives little useful...

### 40 - LSC-DPO: Learning-Signal-Controlled Direct Preference Optimization

- arXiv: [2610.07592](https://arxiv.org/abs/2610.07592) | [PDF](https://arxiv.org/pdf/2610.07592) | [papers.cool](https://papers.cool/arxiv/2610.07592)
- Authors: Yang Qu, Yusheng Han, Chengjia Feng, Handan Liu
- Published: 2026-10-06 01:32 UTC | Categories: cs.AI
- Why it matched: rl_post_training: preference optimization, reward model, dpo
- Abstract skim: Direct Preference Optimization (DPO) has become a standard reward-model-free approach for aligning language models with preference data. However, as the scaled preference margin grows during training, the logistic DPO loss becomes progressively less sensitive to further changes. We study DPO from a loss-level...

### 38 - Quantization Effects on Tool-Failure Recovery Vary Across Prompts and Evaluation Designs

- arXiv: [2610.07781](https://arxiv.org/abs/2610.07781) | [PDF](https://arxiv.org/pdf/2610.07781) | [papers.cool](https://papers.cool/arxiv/2610.07781)
- Authors: Yuhe Hu
- Published: 2026-10-06 05:17 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training; memory_and_benchmarks: evaluation
- Abstract skim: Post-training quantization reduces the cost of deploying language-model agents, but its effect on recovery from temporary tool failures can depend on how recovery is evaluated. We compare 8-bit and 4-bit variants of Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct on twenty deterministic tool-use tasks and five...

### 37 - PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation

- arXiv: [2610.08784](https://arxiv.org/abs/2610.08784) | [PDF](https://arxiv.org/pdf/2610.08784) | [papers.cool](https://papers.cool/arxiv/2610.08784)
- Authors: Kun Song, Yiming Wang, Yilin Chen, Tianyi Ding, Jiaxin Tian, Tianqi Gong, et al. (8 authors)
- Published: 2026-10-06 17:59 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Pretrained robotic policies can suffer substantial performance degradation under out-of-distribution (OOD) conditions encountered during deployment, motivating post-training through real-world interaction. However, reinforcement-learning (RL)-based post-training typically requires substantial environment...

### 37 - Selective Transfer of RL Updates for Visual Reasoning

- arXiv: [2610.08659](https://arxiv.org/abs/2610.08659) | [PDF](https://arxiv.org/pdf/2610.08659) | [papers.cool](https://papers.cool/arxiv/2610.08659)
- Authors: Suxin Ji, Hungtao Wan, Mingjun Liu, An Zhang
- Published: 2026-10-06 16:43 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Model merging provides a training-free way to transfer reasoning capabilities from language models to vision-language models (VLMs), but endpoint-based transfer can conflate pre-existing model differences with changes acquired during reasoning post-training. We instead formulate capability transfer around the...

### 37 - NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale

- arXiv: [2610.08430](https://arxiv.org/abs/2610.08430) | [PDF](https://arxiv.org/pdf/2610.08430) | [papers.cool](https://papers.cool/arxiv/2610.08430)
- Authors: Songlin Jiang, Zhiyu Li, Terry Kong, Yu Yao, Youngeun Kwon, Bernard Nguyen, et al. (8 authors)
- Published: 2026-10-06 14:30 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: Agentic reinforcement learning (RL) disaggregates training from rollout, so each policy update must reach the rollout clusters before the next batch. Transferring a full 1T checkpoint for such weight synchronization (refit) takes 87.5 min between two AWS regions. Measurements of BF16 training show that about 1% of...

### 37 - SIGMA: Self-Improving Alignment Generalization from a Model Spec

- arXiv: [2610.07935](https://arxiv.org/abs/2610.07935) | [PDF](https://arxiv.org/pdf/2610.07935) | [papers.cool](https://papers.cool/arxiv/2610.07935)
- Authors: Jingyu Zhang, Shruti Palaskar, Daniel Khashabi, Benjamin Van Durme, Leon A. Gatys, Joseph Yitan Cheng
- Published: 2026-10-06 08:09 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, reward model; reasoning: reasoning, self-improvement, self improvement, deliberation
- Abstract skim: LLM agents are increasingly capable of executing complex tasks and of recursively improving themselves on easy-to-verify objectives such as software engineering and mathematics. Since alignment is much harder to verify, this creates a growing risk of capabilities increasing without appropriate safety alignment,...

### 36 - Principled Under Pressure: Post-Training Decides Whether LLMs Act on Their Own Moral Judgment

- arXiv: [2610.08670](https://arxiv.org/abs/2610.08670) | [PDF](https://arxiv.org/pdf/2610.08670) | [papers.cool](https://papers.cool/arxiv/2610.08670)
- Authors: Orion Reblitz-Richardson
- Published: 2026-10-06 16:52 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: acting
- Abstract skim: Language models increasingly act as agents. An agent that says an action is wrong and then takes it anyway is a different failure from one that does not know better, and evaluations of stated values cannot see it. We build a pre-registered panel of 248 scenarios across five kinds of pressure. Each scenario is posed...

### 36 - CuratorMAS: Automating Dataset Curation via Multi-Agent Orchestration

- arXiv: [2610.07075](https://arxiv.org/abs/2610.07075) | [PDF](https://arxiv.org/pdf/2610.07075) | [papers.cool](https://papers.cool/arxiv/2610.07075)
- Authors: Yixin Zhang, Wenjie Feng
- Published: 2026-10-05 09:19 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent orchestration, agent collaboration; memory_and_benchmarks: evaluation
- Abstract skim: High-quality datasets are essential for reliable machine learning, but dataset curation remains costly and hard to generalize across domains. Existing methods typically rely on manually designed heuristics or model-dependent signals, limiting their applicability across tasks and user queries. To address these...

### 36 - TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning

- arXiv: [2610.07043](https://arxiv.org/abs/2610.07043) | [PDF](https://arxiv.org/pdf/2610.07043) | [papers.cool](https://papers.cool/arxiv/2610.07043)
- Authors: Zhen Li, Shuai Zhang, Yanggan Gu, Yiming Zhang, Yang Yu, Mingfa Feng, et al. (10 authors)
- Published: 2026-10-05 00:53 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Low-precision execution can substantially accelerate reinforcement learning (RL) for large language models, but discrepancies between learner and sampler execution can destabilize policy optimization. In this paper, we characterize the interaction between mismatch and the policy-gradient direction, distinguishing...

### 34 - Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight

- arXiv: [2610.08077](https://arxiv.org/abs/2610.08077) | [PDF](https://arxiv.org/pdf/2610.08077) | [papers.cool](https://papers.cool/arxiv/2610.08077)
- Authors: Haoxiang Zhang, Qinglin Chen, Hiroaki Hayashi, Zhuofeng Li, Siming Zhang, Jiaxin Zhang, et al. (12 authors)
- Published: 2026-10-06 10:06 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: acting, trajectory, rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful...

### 34 - Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA

- arXiv: [2610.08033](https://arxiv.org/abs/2610.08033) | [PDF](https://arxiv.org/pdf/2610.08033) | [papers.cool](https://papers.cool/arxiv/2610.08033)
- Authors: Jordy Kieto
- Published: 2026-10-06 09:26 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: ppo; planning_and_action: acting, world model; memory_and_benchmarks: evaluation
- Abstract skim: World models are usually judged from the inside: by prediction loss, by the return a policy earns in imagination, or by how convincing their frames look. We judge one from the outside. We learn a structured, multi-agent world model of a complete ten-hero MOBA (206 units, every hero acting every tick, games of up to...

### 32 - RELACE: retrospective likelihood-based action credit estimation for long-horizon language agents

- arXiv: [2610.07349](https://arxiv.org/abs/2610.07349) | [PDF](https://arxiv.org/pdf/2610.07349) | [papers.cool](https://papers.cool/arxiv/2610.07349)
- Authors: Sayak Chakrabarti, Sathish Reddy Indurthi
- Published: 2026-10-05 20:19 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Group Relative Policy Optimization (GRPO) avoids a separate critic by estimating advantages from rollout groups. For multi-turn agents, however, trajectory-level supervision provides coarse, noisy credit: terminal rewards do not locate errors and can penalize useful actions alongside mistakes. Group-in-Group Policy...

### 31 - On-Policy Distillation with Negative-Policy Rollouts

- arXiv: [2610.07874](https://arxiv.org/abs/2610.07874) | [PDF](https://arxiv.org/pdf/2610.07874) | [papers.cool](https://papers.cool/arxiv/2610.07874)
- Authors: Jaehui Hwang, Dongyoon Han, Sangdoo Yun, Byeongho Heo
- Published: 2026-10-06 07:25 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: On-policy distillation (OPD) has been widely studied as a post-training method in which a student model obtains token-level supervision from a stronger teacher on its own rollouts. Recent studies have improved OPD through alternative distillation reward formulations and teacher configurations, while the objective of...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
