# RL / Post-Training / Agentic RL Reading Queue - 2026-06-18

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 368. Minimum score: 8.

## Top Picks

### 62 - STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability

- arXiv: [2606.19236](https://arxiv.org/abs/2606.19236) | [PDF](https://arxiv.org/pdf/2606.19236) | [papers.cool](https://papers.cool/arxiv/2606.19236)
- Authors: Haipeng Luo, Qingfeng Sun, Songli Wu, Can Xu, Wenfeng Deng, Han Hu, et al. (7 authors)
- Published: 2026-06-17 16:13 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning, reflection; planning_and_action: trajectory
- Abstract skim: Reinforcement Learning with Verifiable Rewards algorithms like GRPO have emerged as the dominant post-training paradigm for complex reasoning in LLMs, yet commonly suffer from policy entropy collapse during training. We conduct a first-order gradient analysis of token-level entropy dynamics under GRPO and identify a...

### 57 - ThinkDeception: A Progressive Reinforcement Learning Framework for Interpretable Multimodal Deception Detection

- arXiv: [2606.18988](https://arxiv.org/abs/2606.18988) | [PDF](https://arxiv.org/pdf/2606.18988) | [papers.cool](https://papers.cool/arxiv/2606.18988)
- Authors: Jinhao Song, Shan Liang, Yiqun Yue, Zhuhuayang Zhang, Tianqi Gao
- Published: 2026-06-17 12:08 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Multimodal deception detection is critical for identifying fraudulent intentions, yet existing approaches predominantly rely on end to end black--box paradigms. These methods suffer from a severe lack of interpretability failing to provide transparent reasoning trajectories and struggling to explicitly capture the...

### 57 - Sparsity Curse: Understanding RLVR Model Parameter Space from Model Merging

- arXiv: [2606.18521](https://arxiv.org/abs/2606.18521) | [PDF](https://arxiv.org/pdf/2606.18521) | [papers.cool](https://papers.cool/arxiv/2606.18521)
- Authors: Chenrui Wu, Zexi Li, Jiajun Bu, Jiangchuan Liu, Haishuai Wang
- Published: 2026-06-16 22:22 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more; reasoning: reasoning
- Abstract skim: Reinforcement Learning with Verifiable Reward (RLVR) has emerged as a powerful post-training paradigm that surpasses Supervised Fine-Tuning (SFT) in eliciting reasoning intelligence and resisting catastrophic forgetting. Recent studies further reveal that RLVR induces highly sparse and off-principal parameter...

### 55 - DeFAb: A Verifiable Benchmark for Defeasible Abduction in Foundation Models

- arXiv: [2606.18557](https://arxiv.org/abs/2606.18557) | [PDF](https://arxiv.org/pdf/2606.18557) | [papers.cool](https://papers.cool/arxiv/2606.18557)
- Authors: Patrick Cooper, Alvaro Velasquez
- Published: 2026-06-17 00:13 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: rlvr, preference optimization, grpo, dpo; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: A rule-based logic solver resolves every instance in our benchmark in under 50 microseconds with 100% accuracy; the best frontier language model reaches 65% at best and drops to 23.5% under rendering-robust evaluation (worst case over four surface renderings). We introduce DeFAb (Defeasible Abduction Benchmark), a...

### 49 - Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation

- arXiv: [2606.19327](https://arxiv.org/abs/2606.19327) | [PDF](https://arxiv.org/pdf/2606.19327) | [papers.cool](https://papers.cool/arxiv/2606.19327)
- Authors: Siyi Gu, Jialin Chen, Sophia Zhou, Arman Cohan, Rex Ying
- Published: 2026-06-17 17:54 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Post-training of reasoning language models is commonly driven by supervised distillation and reinforcement learning with verifiable rewards. Distillation often relies on chain-of-thought annotations that are expensive to obtain and may themselves be noisy, incomplete, or partially incorrect; even when the final...

### 45 - GraphPO: Graph-based Policy Optimization for Reasoning Models

- arXiv: [2606.18954](https://arxiv.org/abs/2606.18954) | [PDF](https://arxiv.org/pdf/2606.18954) | [papers.cool](https://papers.cool/arxiv/2606.18954)
- Authors: Yuliang Zhan, Xinyu Tang, Jian Li, Dandan Zheng, Weilong Chai, Jingdong Chen, et al. (10 authors)
- Published: 2026-06-17 11:37 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) has become a standard paradigm for enhancing the capability of large reasoning models. RLVR typically samples responses independently and optimizes the policy using from final answers. This paradigm has two limitations. First, independently responses often...

### 45 - Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards

- arXiv: [2606.18810](https://arxiv.org/abs/2606.18810) | [PDF](https://arxiv.org/pdf/2606.18810) | [papers.cool](https://papers.cool/arxiv/2606.18810)
- Authors: Yingyu Shan, Yuhang Guo, Zihao Cheng, Zeming Liu, Xiangrong Zhu, Xinyi Wang, et al. (10 authors)
- Published: 2026-06-17 08:26 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning, process reward
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in training LLMs for reasoning tasks, but representative methods such as GRPO assign uniform credit across all tokens, wasting gradient on routine tokens while under-crediting pivotal reasoning steps. Existing token-level credit...

### 44 - Native Active Perception as Reasoning for Omni-Modal Understanding

- arXiv: [2606.19341](https://arxiv.org/abs/2606.19341) | [PDF](https://arxiv.org/pdf/2606.19341) | [papers.cool](https://papers.cool/arxiv/2606.19341)
- Authors: Zhenghao Xing, Ruiyang Xu, Yuxuan Wang, Jinzheng He, Ziyang Ma, Qize Yang, et al. (11 authors)
- Published: 2026-06-17 17:59 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Passive models for long video understanding typically rely on a "watch-it-all" paradigm, processing frames uniformly regardless of query difficulty, causing computational cost to grow with video duration. Although interactive frameworks have emerged, they often rely on global pre-scanning, and their context cost...

### 44 - R2D-RL: A RoboCup 2D Soccer Environment for Multi-Agent Reinforcement Learning

- arXiv: [2606.18786](https://arxiv.org/abs/2606.18786) | [PDF](https://arxiv.org/pdf/2606.18786) | [papers.cool](https://papers.cool/arxiv/2606.18786)
- Authors: Haobin Qin, Baofeng Zhang, Hidehisa Akiyama, Keisuke Fujii
- Published: 2026-06-17 07:57 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: memory, benchmark
- Abstract skim: Robot soccer is a challenging testbed for multi-agent reinforcement learning because it combines partial observability, cooperative and adversarial interaction, sparse rewards, and long-horizon tactical behavior. RoboCup 2D Soccer Simulation (RCSS2D) provides a mature robot-soccer platform, but its competition-...

### 41 - EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts

- arXiv: [2606.18967](https://arxiv.org/abs/2606.18967) | [PDF](https://arxiv.org/pdf/2606.18967) | [papers.cool](https://papers.cool/arxiv/2606.18967)
- Authors: Minseo Kim, Minjae Lee, Seunghyuk Oh, Kevin Galim, Donghoon Kim, Coleman Hooper, et al. (10 authors)
- Published: 2026-06-17 11:51 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Reinforcement learning (RL) has become a representative post-training paradigm for LLMs, enabling strong reasoning and agentic capabilities. However, rollout generation remains a dominant latency bottleneck because autoregressive sampling decodes responses sequentially and a small number of long-tailed generations...

### 41 - Be Your Own Teacher: Steering Protein Language Models via Unsupervised Reward Optimization

- arXiv: [2606.18961](https://arxiv.org/abs/2606.18961) | [PDF](https://arxiv.org/pdf/2606.18961) | [papers.cool](https://papers.cool/arxiv/2606.18961)
- Authors: Lanqing Li, Shentong Mo, Yang Yu, Pheng-Ann Heng
- Published: 2026-06-17 11:42 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, rlhf, dpo; reasoning: self-improvement, self improvement; downranked: protein
- Abstract skim: Protein language models (PLMs) have emerged as powerful tools for controllable biomolecular design, yet their post-training adaptation typically relies on costly wet-lab validation or curated preference datasets. To overcome this supervision bottleneck, we introduce unsupervised reward optimization of PLMs, a...

### 41 - REVES: REvision and VErification--Augmented Training for Test-Time Scaling

- arXiv: [2606.18910](https://arxiv.org/abs/2606.18910) | [PDF](https://arxiv.org/pdf/2606.18910) | [papers.cool](https://papers.cool/arxiv/2606.18910)
- Authors: Yuanxin Liu, Ruida Zhou, Xinyan Zhao, Amr Sharaf, Hongzhou Lin, Arijit Biswas, et al. (9 authors)
- Published: 2026-06-17 10:37 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: Test-time scaling via sequential revision has emerged as a powerful paradigm for enhancing Large Language Model (LLM) reasoning. However, standard post-training methods primarily optimize single-shot objectives, creating a fundamental misalignment with multi-step inference dynamics. While recent work treats this as...

### 38 - When Does Trajectory-Level Supervision Permit Efficient Offline Reinforcement Learning?

- arXiv: [2606.18531](https://arxiv.org/abs/2606.18531) | [PDF](https://arxiv.org/pdf/2606.18531) | [papers.cool](https://papers.cool/arxiv/2606.18531)
- Authors: Xuanfei Ren, Tengyang Xie
- Published: 2026-06-16 22:55 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model; planning_and_action: trajectory
- Abstract skim: Offline reinforcement learning is typically analyzed under process-level reward supervision, yet many sequential decision datasets record only trajectory-level outcomes. We develop a statistical theory for offline policy optimization from such outcome-level supervision. We first study the canonical setting where the...

### 37 - Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications

- arXiv: [2606.18502](https://arxiv.org/abs/2606.18502) | [PDF](https://arxiv.org/pdf/2606.18502) | [papers.cool](https://papers.cool/arxiv/2606.18502)
- Authors: Paresh Dashore, Shreyas Kulkarni, Uttam Gurram, Nadia Bathaee, Kartik Balasubramaniam, Genta Indra Winata, et al. (8 authors)
- Published: 2026-06-16 21:30 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; rl_post_training: preference optimization; reasoning: reasoning
- Abstract skim: Large language model (LLM)-based multi-agent systems demonstrate strong performance on complex reasoning and task execution, enabling broad enterprise applications. However, production deployment remains challenging due to domain-specific customization requirements and high latency and inference costs in agentic...

### 36 - Beyond Safe Data: Pretraining-Stage Alignment with Regular Safety Reflection

- arXiv: [2606.19168](https://arxiv.org/abs/2606.19168) | [PDF](https://arxiv.org/pdf/2606.19168) | [papers.cool](https://papers.cool/arxiv/2606.19168)
- Authors: Jinhan Li, Kexian Tang, Yihan Xu, Zhuorui Ye, Kaifeng Lyu
- Published: 2026-06-17 15:11 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, reflection; planning_and_action: acting
- Abstract skim: To achieve deeper safety alignment for large language models (LLMs), recent efforts have studied how to push safety interventions earlier into the pretraining stage, primarily by filtering unsafe data or rewriting it into safer forms. We argue that pretraining-stage alignment should go beyond making the data safe:...

### 36 - TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning

- arXiv: [2606.18308](https://arxiv.org/abs/2606.18308) | [PDF](https://arxiv.org/pdf/2606.18308) | [papers.cool](https://papers.cool/arxiv/2606.18308)
- Authors: Zijie Meng, Ziwei Li, Yufei Liu, Zhiyu Li, Jiyuan Liu, Wenhua Nie, et al. (8 authors)
- Published: 2026-06-16 07:41 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Safe coordination in networked cyber-physical systems forces learning algorithms to simultaneously handle hybrid discrete-continuous actions, hard training-time safety constraints, and physics-governed dynamics. We show that these three features form a directed cycle of biases that defeats any naive composition of...

### 35 - Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training

- arXiv: [2606.19004](https://arxiv.org/abs/2606.19004) | [PDF](https://arxiv.org/pdf/2606.19004) | [papers.cool](https://papers.cool/arxiv/2606.19004)
- Authors: Ruiqi Lai, Dakai An, Wei Gao, Ju Huang, Siran Yang, Jiamang Wang, et al. (9 authors)
- Published: 2026-06-17 12:31 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) post-training of Diffusion Transformers (DiTs) is prohibitively expensive, requiring thousands of high-end GPUs. Existing works explore two directions to reduce cost: seed exploration improves training convergence by selecting high-contrast samples, yet adds compute to the critical path;...

### 35 - Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning

- arXiv: [2606.18831](https://arxiv.org/abs/2606.18831) | [PDF](https://arxiv.org/pdf/2606.18831) | [papers.cool](https://papers.cool/arxiv/2606.18831)
- Authors: Xiaoyue Xu, Sikui Zhang, Xiaorong Wang, Xu Han, Chaojun Xiao
- Published: 2026-06-17 09:07 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; memory_and_benchmarks: gaia
- Abstract skim: Long-context reasoning is an essential capability for large language models, particularly when they are deployed as autonomous agents that must reason over lengthy trajectories. Reinforcement learning (RL) has recently emerged as a dominant paradigm for improving this ability, yet existing work largely focuses on...

### 34 - PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning

- arXiv: [2606.18633](https://arxiv.org/abs/2606.18633) | [PDF](https://arxiv.org/pdf/2606.18633) | [papers.cool](https://papers.cool/arxiv/2606.18633)
- Authors: Zhiyuan Wen, Jiannong Cao, Peng Gao, Haochen Shi, Wengpan Kuan, Bo Yuan, et al. (7 authors)
- Published: 2026-06-17 03:03 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: grpo; planning_and_action: planning
- Abstract skim: Effective programming education requires personalized instruction adapted to diverse learner backgrounds. However, while LLM-based multi-agent systems (MAS) excel at complex planning, existing planners often lack profile-grounding and pedagogical scaffolding, thereby undermining personalized programming learning. To...

### 33 - UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning

- arXiv: [2606.19328](https://arxiv.org/abs/2606.19328) | [PDF](https://arxiv.org/pdf/2606.19328) | [papers.cool](https://papers.cool/arxiv/2606.19328)
- Authors: Mohamed Nabail, Leo Cheng, Jingmin Wang, Nicholas Rhinehart
- Published: 2026-06-17 17:54 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Preference-based RL provides an approach to learning reward models from pairwise comparisons of behaviors, bypassing the need for explicit reward design. However, existing methods typically rely on passive data collection and suffer from poor sample efficiency, especially during the early stages of learning. We...

### 32 - Steerable Cultural Preference Optimization of Reward Models

- arXiv: [2606.18606](https://arxiv.org/abs/2606.18606) | [PDF](https://arxiv.org/pdf/2606.18606) | [papers.cool](https://papers.cool/arxiv/2606.18606)
- Authors: Minsik Oh, Advit Deepak, Sophie Wu, Douwe Kiela, Ekaterina Shutova
- Published: 2026-06-17 02:10 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: preference optimization, reward model
- Abstract skim: It is essential for large language model (LLM) technology to serve many different cultural sub-communities in a manner that is acceptable to each community. However, research on LLM alignment has so far predominantly focused on predicting a unified response preference of annotators from certain regions. This paper...

### 32 - LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents

- arXiv: [2606.18388](https://arxiv.org/abs/2606.18388) | [PDF](https://arxiv.org/pdf/2606.18388) | [papers.cool](https://papers.cool/arxiv/2606.18388)
- Authors: Haoyang Fang, Wei Zhu, Boran Han, Alex Zhang, Zhenyu Pan, Shuo Yang, et al. (14 authors)
- Published: 2026-06-16 18:33 UTC | Categories: cs.AI, cs.CL, cs.LG, cs.MA
- Why it matched: rl_post_training: post-training, post training, grpo
- Abstract skim: RL post-training strategies are dataset-dependent and reveal a recurring empirical pattern: capacity parameters accumulate monotonically across stages, while regularization parameters predominantly oscillate in response to shifting training dynamics. This distinction matters because fixed schedules commit all...

### 29 - Mechanism-Guided Selective Unlearning for RLVR-Induced Reasoning

- arXiv: [2606.19222](https://arxiv.org/abs/2606.19222) | [PDF](https://arxiv.org/pdf/2606.19222) | [papers.cool](https://papers.cool/arxiv/2606.19222)
- Authors: Chenyu Zhou, Qiliang Jiang, Shuning Wu, Xu Zhou
- Published: 2026-06-17 15:59 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: rlvr; reasoning: reasoning
- Abstract skim: We propose MAST (Mechanism-Aligned Selective Targeting), a mechanism-guided method for unlearning RLVR-induced reasoning with substantially lower collateral damage than standard full-parameter updates. In matched SFT/RLVR checkpoints on Qwen2.5-Math-1.5B and Qwen3-1.7B-Base, the SFT-to-RLVR increment differs sharply...

### 29 - Seeing Before Reasoning: Decoupling Perception and Reasoning for Shortcut-Resilient Multimodal On-Policy Self-Distillation

- arXiv: [2606.19120](https://arxiv.org/abs/2606.19120) | [PDF](https://arxiv.org/pdf/2606.19120) | [papers.cool](https://papers.cool/arxiv/2606.19120)
- Authors: Sihan Wang, Xiyao Liu, Lianqing Liu, Zhi Han
- Published: 2026-06-17 14:33 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: On-policy self-distillation (OPSD) trains a model on its own rollouts and uses a frozen copy to provide dense token-level targets conditioned on a reference target. This works well for LLM reasoning, but a direct extension to multimodal large language models (MLLMs) can create a shortcut: the privileged target may...

### 28 - Learning from Your Own Mistakes: Constructing Learnable Micro-Reflective Trajectories for Self-Distillation

- arXiv: [2606.18844](https://arxiv.org/abs/2606.18844) | [PDF](https://arxiv.org/pdf/2606.18844) | [papers.cool](https://papers.cool/arxiv/2606.18844)
- Authors: Zhilin Huang, Hang Gao, Ziqiang Dong, Yuan Chen, Yifeng Luo, Chujun Qin, et al. (9 authors)
- Published: 2026-06-17 09:24 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Self-distillation improves reasoning in large language models by using the model's own rollouts as training signal, typically through implicit logit-level alignment that minimizes KL divergence toward a privileged target distribution. However, because this supervision is generated via uncontrolled sampling, it...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
