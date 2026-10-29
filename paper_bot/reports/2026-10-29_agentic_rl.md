# RL / Post-Training / Agentic RL Reading Queue - 2026-10-29

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 525. Minimum score: 8.

## Top Picks

### 66 - Bayes-Adaptive MDPs for Rollout Allocation to Enhance GRPO Training

- arXiv: [2610.37429](https://arxiv.org/abs/2610.37429) | [PDF](https://arxiv.org/pdf/2610.37429) | [papers.cool](https://papers.cool/arxiv/2610.37429)
- Authors: Faeze Moradi Kalarde, Armin Toroghi, Nam Ho Koh, Doo Hwan Hwang, Seungjin Kim, Kee-Eung Kim, et al. (7 authors)
- Published: 2026-10-27 15:41 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning; planning_and_action: rollout, decision making
- Abstract skim: Group Relative Policy Optimization (GRPO) has demonstrated strong performance in LLM post-training. However, it allocates a uniform rollout budget to every training question, ignoring variations in question difficulty. As a result, highly difficult questions may receive too few rollouts to generate informative...

### 63 - PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions

- arXiv: [2610.37471](https://arxiv.org/abs/2610.37471) | [PDF](https://arxiv.org/pdf/2610.37471) | [papers.cool](https://papers.cool/arxiv/2610.37471)
- Authors: Tongkun Guan, Zhibo Yang, Mingkun Yang, Haocheng Wang, Wei Shen, Xiaokang Yang
- Published: 2026-10-27 16:04 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl, multi-agent, tool use; rl_post_training: post-training, post training, verifiable reward; reasoning: reasoning, process reward
- Abstract skim: Fine-grained visual perception remains a bottleneck during post-training of multimodal large language models (MLLMs), as perceptual errors can constrain gains from reasoning-focused optimization. Although image-caption pre-training improves perception, its influence can weaken as subsequent stages change data...

### 57 - Uncovering Shortcut Amplification in Video RLVR through the Lens of Perceptual Uncertainty Collapse

- arXiv: [2610.37211](https://arxiv.org/abs/2610.37211) | [PDF](https://arxiv.org/pdf/2610.37211) | [papers.cool](https://papers.cool/arxiv/2610.37211)
- Authors: Jiafeng Liang, Xianhao Ou, Tao Ren, Rongchuan Mu, Runxuan Liu, Dandan Tu, et al. (9 authors)
- Published: 2026-10-27 13:26 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has emerged as an effective post-training paradigm for enhancing the video reasoning capability of Large Multimodal Models (LMMs). Despite its empirical effectiveness, we show that outcome-level optimization can introduce an undesirable shortcut amplification...

### 48 - Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning

- arXiv: [2610.37195](https://arxiv.org/abs/2610.37195) | [PDF](https://arxiv.org/pdf/2610.37195) | [papers.cool](https://papers.cool/arxiv/2610.37195)
- Authors: Yingjian Chen, Lang Zhou, Zixin Zhao, Pingfan Li, Weishi Zheng, Zhilin Zhao
- Published: 2026-10-27 13:16 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning for long-horizon agents relies on feedback from sequences of interactions, making credit assignment to individual actions difficult. Existing methods such as GiGPO compare actions at shared states to compute relative advantages, but estimate each action's value from a single sampled...

### 48 - SetGRPO: Calibrating Grader-Induced Policy Optimization

- arXiv: [2610.36807](https://arxiv.org/abs/2610.36807) | [PDF](https://arxiv.org/pdf/2610.36807) | [papers.cool](https://papers.cool/arxiv/2610.36807)
- Authors: Jiale Huang, Zixu Li, Zhiwei Chen, Zhiheng Fu, Jinhe Bi, Yupeng Hu
- Published: 2026-10-27 08:11 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: Rubric-based reinforcement learning uses fine-grained grader feedback to train large language models on open-ended tasks, but grader randomness can alter GRPO updates in ways that score discrepancies alone cannot characterize. Because GRPO jointly normalizes rewards within each response group and combines the...

### 44 - Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning

- arXiv: [2610.36075](https://arxiv.org/abs/2610.36075) | [PDF](https://arxiv.org/pdf/2610.36075) | [papers.cool](https://papers.cool/arxiv/2610.36075)
- Authors: Koen Ponse, Aske Plaat, Thomas M. Moerland
- Published: 2026-10-26 18:03 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Hardware-accelerated reinforcement learning in JAX has gained rapid popularity in recent years and has proven to be a successful method of scaling online reinforcement learning. The resulting ecosystem, however, is fragmented: environment suites define their own interfaces, and algorithm implementations are...

### 43 - When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem Reasoning

- arXiv: [2610.36849](https://arxiv.org/abs/2610.36849) | [PDF](https://arxiv.org/pdf/2610.36849) | [papers.cool](https://papers.cool/arxiv/2610.36849)
- Authors: Zehao Wang, Hanzhu Chen, Runquan Gui, Zhe Wang, Lin Yang
- Published: 2026-10-27 08:47 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) derives its learning signal from binary rewards via on-policy exploration and becomes a powerful paradigm for improving the reasoning of large language models. Yet it faces a learning cliff on problems beyond model's current ability: when every rollout fails, the...

### 43 - DocSkill: Skill-Integrated Agentic Reasoning for Multilingual Multi-Hop Document Question Answering

- arXiv: [2610.36759](https://arxiv.org/abs/2610.36759) | [PDF](https://arxiv.org/pdf/2610.36759) | [papers.cool](https://papers.cool/arxiv/2610.36759)
- Authors: Jing Huang, Zhiya Tan, Changtao Miao, Shutao Gong, Yang Wang, Joey Tianyi Zhou, et al. (8 authors)
- Published: 2026-10-27 07:14 UTC | Categories: cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: preference optimization, dpo; reasoning: reasoning
- Abstract skim: Multilingual multi-hop document question answering (MMHop-DocQA) requires locating and integrating evidence across complex layouts, document pages, and diverse languages. Existing approaches include single-pass processing and adaptive tool use, but learning to coordinate evidence acquisition, cross-page integration,...

### 41 - Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards

- arXiv: [2610.37041](https://arxiv.org/abs/2610.37041) | [PDF](https://arxiv.org/pdf/2610.37041) | [papers.cool](https://papers.cool/arxiv/2610.37041)
- Authors: Bo Yang, Zishuai Zhang, Weihua Li, Qinnan Zhang, Sijia Wen, Hainan Zhang
- Published: 2026-10-27 11:13 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has shown strong empirical gains in improving the reasoning ability of large language models (LLMs) on tasks such as mathematics and programming. However, recent studies have shown that RLVR rollouts often collapse onto a narrow set of reasoning trajectories,...

### 37 - From Solver Trajectories to Teaching Trajectories: Cognition-Aligned Reasoning Distillation

- arXiv: [2610.36445](https://arxiv.org/abs/2610.36445) | [PDF](https://arxiv.org/pdf/2610.36445) | [papers.cool](https://papers.cool/arxiv/2610.36445)
- Authors: Yashuo Luo, Qianren Mao, Ziqi Qin, Junnan Liu, Haitao Li, Qili Zhang, et al. (9 authors)
- Published: 2026-10-27 00:46 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, rlhf; reasoning: reasoning
- Abstract skim: Knowledge distillation from large reasoning models (LRMs) often uses raw teacher trajectories as supervision. However, this practice creates a mismatch between the goal of distillation and the nature of teacher trajectories. Advanced LRMs typically improve their reasoning capabilities through reward-driven post-...

### 36 - EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning

- arXiv: [2610.37609](https://arxiv.org/abs/2610.37609) | [PDF](https://arxiv.org/pdf/2610.37609) | [papers.cool](https://papers.cool/arxiv/2610.37609)
- Authors: Sihan Yang, Weichen Bai, Ruichuan An, Yiming Cheng, Zhiyuan Feng, Tianyi Jiang, et al. (12 authors)
- Published: 2026-10-27 17:38 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organizing,...

### 36 - Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction

- arXiv: [2610.37441](https://arxiv.org/abs/2610.37441) | [PDF](https://arxiv.org/pdf/2610.37441) | [papers.cool](https://papers.cool/arxiv/2610.37441)
- Authors: Yifei Yuan, Jakob Wolf, Ghaith Androwis, Xianlian Zhou
- Published: 2026-10-27 15:49 UTC | Categories: cs.LG, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Objective: This study aims to determine whether a hip-exoskeleton policy trained in simulation, by co-adapting with a musculoskeletal human model under a metabolic-energy reward, reduces the metabolic cost of walking in new users without per-user tuning, and how mechanical-power shaping affects the learned...

### 33 - Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives Policy Collapse in Unsupervised RLVR

- arXiv: [2610.37553](https://arxiv.org/abs/2610.37553) | [PDF](https://arxiv.org/pdf/2610.37553) | [papers.cool](https://papers.cool/arxiv/2610.37553)
- Authors: Peize Ding
- Published: 2026-10-27 17:01 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Label-free reinforcement learning with verifiable rewards (RLVR) rewards a language model for agreeing with its own majority vote. It improves reasoning at first but eventually collapses: the self-assessed reward goes to one while accuracy falls, often until the model gives the same answer to every problem. The...

### 33 - Watermark Basins: Black-Box Detection of Distilled LLMs

- arXiv: [2610.37266](https://arxiv.org/abs/2610.37266) | [PDF](https://arxiv.org/pdf/2610.37266) | [papers.cool](https://papers.cool/arxiv/2610.37266)
- Authors: Hongyan Chang, Hady Elsahar, Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Sylvestre-Alvise Rebuffi, et al. (13 authors)
- Published: 2026-10-27 13:59 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Proprietary language models and their reasoning traces are vulnerable to API-based distillation, where an adversary trains a student model on the teacher model's outputs. To obtain evidence of distillation, model providers can watermark the teacher's outputs, aiming to leave a radioactive signal in the student's...

### 32 - RPSD: Retrieval-Privileged On-Policy Self-Distillation with Optimal Transport

- arXiv: [2610.37281](https://arxiv.org/abs/2610.37281) | [PDF](https://arxiv.org/pdf/2610.37281) | [papers.cool](https://papers.cool/arxiv/2610.37281)
- Authors: Dongyue Li, Zebang Cheng, Zhongyi Deng, Hongboxu, Yi Bin, Fei Ma
- Published: 2026-10-27 14:08 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo
- Abstract skim: Sequential recommendation predicts a user's next interaction from historical behavior. Recent LLM-based methods recast this task as generative recommendation and increasingly adopt reinforcement learning such as GRPO for post-training. However, these methods suffer from two limitations, namely credit-blind...

### 32 - On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime

- arXiv: [2610.37085](https://arxiv.org/abs/2610.37085) | [PDF](https://arxiv.org/pdf/2610.37085) | [papers.cool](https://papers.cool/arxiv/2610.37085)
- Authors: Kensuke Sasaki, Issei Sato
- Published: 2026-10-27 11:48 UTC | Categories: cs.LG
- Why it matched: rl_post_training: rlhf, preference optimization, dpo
- Abstract skim: Direct Preference Optimization (DPO) has been widely adopted for aligning language models with human preferences. Recent empirical work has revealed that DPO induces remarkably sparse parameter updates, yet no theoretical explanation for this phenomenon has been offered. We analyze DPO's optimization dynamics under...

### 31 - TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments

- arXiv: [2610.37592](https://arxiv.org/abs/2610.37592) | [PDF](https://arxiv.org/pdf/2610.37592) | [papers.cool](https://papers.cool/arxiv/2610.37592)
- Authors: Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck, Prashant Doshi
- Published: 2026-10-27 17:28 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: acting
- Abstract skim: Cooperative multi-agent reinforcement learning under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic that observes the global state, then removes the critic at execution. The policies are optimized to rely on information they will not have when they...

### 31 - Proposing Better Rollouts for On-Policy Distillation

- arXiv: [2610.36477](https://arxiv.org/abs/2610.36477) | [PDF](https://arxiv.org/pdf/2610.36477) | [papers.cool](https://papers.cool/arxiv/2610.36477)
- Authors: Sirui Chen, Yunzhe Qi, Haobo Xu, Jiaru Zou, Mengting Ai, Zihao Li, et al. (7 authors)
- Published: 2026-10-27 01:33 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: On-policy distillation (OPD) improves language-model post-training by letting the student learn from its own sampled trajectories under teacher supervision, aligning the training process with inference-time behavior. However, the rollout policy in OPD is usually treated as fixed: each round samples directly from the...

### 30 - CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning

- arXiv: [2610.36469](https://arxiv.org/abs/2610.36469) | [PDF](https://arxiv.org/pdf/2610.36469) | [papers.cool](https://papers.cool/arxiv/2610.36469)
- Authors: Jianwen Chen, Peng Xia, Kaide Zeng, Siwei Han, Zhen-Yu Zhang, Charles Fleming, et al. (8 authors)
- Published: 2026-10-27 01:25 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning
- Abstract skim: Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the interface that generates its training...

### 29 - VideoLVR: Latent Visual Reasoning over Grounded Video Evidence

- arXiv: [2610.37613](https://arxiv.org/abs/2610.37613) | [PDF](https://arxiv.org/pdf/2610.37613) | [papers.cool](https://papers.cool/arxiv/2610.37613)
- Authors: Shilong Li, Xingyuan Bu, Hao Shi, Yun Xing, Weixin Feng, Qiangpeng Yang, et al. (7 authors)
- Published: 2026-10-27 17:41 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Chain-of-thought reasoning has substantially advanced video understanding in multimodal large language models (MLLMs). However, language-based reasoning traces do not provide a reliable mechanism for models to revisit relevant visual evidence, leading to visual forgetting and impairing their ability to reason over...

### 29 - Repulsive Population Policy Gradients for Behaviorally Diverse Reinforcement Learning

- arXiv: [2610.36425](https://arxiv.org/abs/2610.36425) | [PDF](https://arxiv.org/pdf/2610.36425) | [papers.cool](https://papers.cool/arxiv/2610.36425)
- Authors: Saeed Hedayatian, Harsh Shah, Celine Mneimneh, Stefanos Nikolaidis
- Published: 2026-10-27 00:16 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, ppo; planning_and_action: decision making; memory_and_benchmarks: evaluation
- Abstract skim: The goal of Quality-Diversity Reinforcement Learning (QD-RL) is to find a population of high-performing policies that solve a decision-making problem in diverse ways. Despite recent progress, QD-RL methods predominantly rely on evolutionary operators--including black-box optimizers, mutations, and crossovers--to...

### 28 - VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning

- arXiv: [2610.37378](https://arxiv.org/abs/2610.37378) | [PDF](https://arxiv.org/pdf/2610.37378) | [papers.cool](https://papers.cool/arxiv/2610.37378)
- Authors: Bojun Zou, Wenhao Yu, Jiaohao Li, Jiaxuan Lin, Guanting Ye, Haohan Geng, et al. (9 authors)
- Published: 2026-10-27 15:07 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control. However, most VLA models target static manipulation in unconstrained environments, overlooking spatial constraints and dynamic obstacles. Fine-tuning VLAs on obstacle-avoidance data is a...

### 27 - When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies

- arXiv: [2610.37547](https://arxiv.org/abs/2610.37547) | [PDF](https://arxiv.org/pdf/2610.37547) | [papers.cool](https://papers.cool/arxiv/2610.37547)
- Authors: Anukriti Singh, Maxime Caniot, Pratap Tokekar, Firas Abi-Farraj
- Published: 2026-10-27 16:58 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: trajectory
- Abstract skim: Imitation policies that reliably execute most of a manipulation trajectory can still fail in localized regions requiring last-mile precision. Updating the full policy or exploring residual actions everywhere treats this local failure as a global learning problem. We introduce Adaptive Residual Correction (ARC), a...

### 26 - When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models

- arXiv: [2610.37430](https://arxiv.org/abs/2610.37430) | [PDF](https://arxiv.org/pdf/2610.37430) | [papers.cool](https://papers.cool/arxiv/2610.37430)
- Authors: Ananth K Suresh, Aveen Dayal, Gouthaman KV, Aditya Pola, Vineeth N Balasubramanian
- Published: 2026-10-27 15:42 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: benchmark
- Abstract skim: For reliable deployment, multimodal large language models (MLLMs) should recognize when an image provides insufficient evidence to answer a question and withhold unsupported answers. Yet refusal alone is not necessarily evidence of such recognition: models may refuse because of unrelated safety constraints or...

### 26 - Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning

- arXiv: [2610.36309](https://arxiv.org/abs/2610.36309) | [PDF](https://arxiv.org/pdf/2610.36309) | [papers.cool](https://papers.cool/arxiv/2610.36309)
- Authors: Andrea Vasco Grieco, Evelyn D'Elia, Edoardo Caldarelli, Raffaello Camoriano
- Published: 2026-10-26 21:32 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: benchmark
- Abstract skim: Deep reinforcement learning (RL) algorithms have been observed to lose the ability to adaptively learn from new data, a phenomenon termed Loss of Plasticity (LoP). While many metrics have been shown to correlate with it, the causal mechanisms and the geometric conditions from which it can arise have not been clearly...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
