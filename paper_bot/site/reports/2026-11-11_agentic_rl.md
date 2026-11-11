# RL / Post-Training / Agentic RL Reading Queue - 2026-11-11

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 501. Minimum score: 8.

## Top Picks

### 58 - Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation

- arXiv: [2611.14009](https://arxiv.org/abs/2611.14009) | [PDF](https://arxiv.org/pdf/2611.14009) | [papers.cool](https://papers.cool/arxiv/2611.14009)
- Authors: Lirui Luo, Kelong Mao, Xinwei Yang, Rongqing Li, Luyu Chen, Kieran Wong, et al. (12 authors)
- Published: 2026-11-10 12:49 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agentic rl, agent memory; rl_post_training: post-training, post training; memory_and_benchmarks: memory
- Abstract skim: Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. They must therefore decide what to write down and what to read back, and when to do either. Recent work has begun to use on-policy distillation (OPD) to make memory control part of the policy,...

### 57 - How Post-Training Influences Verbalized Algorithmic Computation in Language Models

- arXiv: [2611.13552](https://arxiv.org/abs/2611.13552) | [PDF](https://arxiv.org/pdf/2611.13552) | [papers.cool](https://papers.cool/arxiv/2611.13552)
- Authors: Niall Dalton
- Published: 2026-11-10 04:12 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, rlvr, dpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Post-training improves language-model reasoning, but how it changes the use of internal information and verbalized chain of thought (CoT) remains unclear. We study successive SFT, DPO, and RLVR checkpoints of Olmo-3-7B-Instruct on multi-digit addition, using carry values as known intermediate state. Probes recover...

### 56 - A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets

- arXiv: [2611.14467](https://arxiv.org/abs/2611.14467) | [PDF](https://arxiv.org/pdf/2611.14467) | [papers.cool](https://papers.cool/arxiv/2611.14467)
- Authors: Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster
- Published: 2026-11-10 18:31 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization, grpo, +1 more
- Abstract skim: Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to identify algorithms that learn near-optimal policies using total samples and gradient steps governed by the base model's response coverage, a measure of how readily it...

### 45 - Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics

- arXiv: [2611.13161](https://arxiv.org/abs/2611.13161) | [PDF](https://arxiv.org/pdf/2611.13161) | [papers.cool](https://papers.cool/arxiv/2611.13161)
- Authors: Sepideh Ravanbakhsh, Hamidreza Moradi
- Published: 2026-11-09 19:45 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction following and...

### 40 - Are Dense Rewards Worth Their Tokens in GRPO?

- arXiv: [2611.13560](https://arxiv.org/abs/2611.13560) | [PDF](https://arxiv.org/pdf/2611.13560) | [papers.cool](https://papers.cool/arxiv/2611.13560)
- Authors: Vikash Singh, Weicong Chen, Debargha Ganguly, Yanyan Zhang, Mohsen Hariri, Sreehari Sankar, et al. (19 authors)
- Published: 2026-11-10 04:25 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: rlvr, policy optimization, group relative policy optimization, grpo
- Abstract skim: RLVR trains language models to reason by rewarding correct final answers. A widely used algorithm, group-relative policy optimization (GRPO), gives every token of a solution the same credit, so dense process rewards have been proposed to credit intermediate steps, for example with a Monte-Carlo reward that scores...

### 40 - Leveraging Psychophysical Attentional Distribution for Gaze-Augmented Reward Modeling

- arXiv: [2611.13477](https://arxiv.org/abs/2611.13477) | [PDF](https://arxiv.org/pdf/2611.13477) | [papers.cool](https://papers.cool/arxiv/2611.13477)
- Authors: Chaeho Lee, Junyup Kim, Wansoo Kim, Young Min Jung, Sang Ho Lee
- Published: 2026-11-10 02:36 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, reward model
- Abstract skim: Integrating human feedback into language models has gained increasing attention as a means to align model outputs with human preferences, with Reinforcement Learning from Human Feedback (RLHF) serving as a prominent framework for preference-based alignment. Recent studies have incorporated eye-tracking (ET) data as...

### 37 - AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models

- arXiv: [2611.14515](https://arxiv.org/abs/2611.14515) | [PDF](https://arxiv.org/pdf/2611.14515) | [papers.cool](https://papers.cool/arxiv/2611.14515)
- Authors: Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, et al. (7 authors)
- Published: 2026-11-10 18:58 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; memory_and_benchmarks: evaluation, alfworld
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this...

### 35 - Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic Rounding

- arXiv: [2611.13545](https://arxiv.org/abs/2611.13545) | [PDF](https://arxiv.org/pdf/2611.13545) | [papers.cool](https://papers.cool/arxiv/2611.13545)
- Authors: Mahdi Nazemi, Oleg Rybakov, Tijmen Blankevoort, Asit Mishra, Carlo del Mundo
- Published: 2026-11-10 04:07 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: BF16 is widely used to pretrain large language models because it has the same dynamic range as FP32 and converges similarly to FP32 training. However, in reinforcement learning with verifiable rewards, where learning rates are typically low, we find that standard mixed-precision BF16 training converges more slowly...

### 34 - Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards

- arXiv: [2611.14015](https://arxiv.org/abs/2611.14015) | [PDF](https://arxiv.org/pdf/2611.14015) | [papers.cool](https://papers.cool/arxiv/2611.14015)
- Authors: Chi Liu, Xin Chen, Yuchuan Weng, Srinivasan Manoharan
- Published: 2026-11-10 12:51 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; memory_and_benchmarks: evaluation
- Abstract skim: In reinforcement learning with verifiable rewards, a language model is rewarded for a correct final answer, and GRPO passes that reward to every token of the solution in equal measure. We instead place the credit where the model hesitated, in a method we call MCPO (Margin-Credit Policy Optimization). We measure...

### 33 - Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents

- arXiv: [2611.14511](https://arxiv.org/abs/2611.14511) | [PDF](https://arxiv.org/pdf/2611.14511) | [papers.cool](https://papers.cool/arxiv/2611.14511)
- Authors: Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
- Published: 2026-11-10 18:56 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark; downranked: protein
- Abstract skim: Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-...

### 32 - Enforcing Axioms for AI Alignment under Loss-Based Rules

- arXiv: [2611.13369](https://arxiv.org/abs/2611.13369) | [PDF](https://arxiv.org/pdf/2611.13369) | [papers.cool](https://papers.cool/arxiv/2611.13369)
- Authors: Alexandros Hollender, Sonja Kraiczy
- Published: 2026-11-09 23:44 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, reward model
- Abstract skim: Many alignment methods, most notably reinforcement learning from human feedback (RLHF), train reward models by minimizing a loss on pairwise comparisons of model responses. Inspired by principle-guided methods such as Constitutional AI, we treat each principle as a voter that compares responses according to that...

### 32 - Wrong the Same Way: Cross-Prompt Sharing Both Suppresses and Amplifies Reward Hacking in RLVR

- arXiv: [2611.13218](https://arxiv.org/abs/2611.13218) | [PDF](https://arxiv.org/pdf/2611.13218) | [papers.cool](https://papers.cool/arxiv/2611.13218)
- Authors: Michael Li, Rohan Pandey, Ray Chen
- Published: 2026-11-09 20:39 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo
- Abstract skim: Two accounts of how reinforcement learning with verifiable rewards (RLVR) interacts with an imperfect verifier coexist: in one, reward hacking is inherited from the base model; in the other, RL amplifies it. We study both in a controlled environment small enough to compute the entire response distribution exactly....

### 31 - GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning

- arXiv: [2611.13028](https://arxiv.org/abs/2611.13028) | [PDF](https://arxiv.org/pdf/2611.13028) | [papers.cool](https://papers.cool/arxiv/2611.13028)
- Authors: Jiajun Chen, Shicheng Fang, Jiahao Lu, Yuxin Wang, Xipeng Qiu
- Published: 2026-11-09 08:59 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applying it for Reinforcement Learning (RL)....

### 29 - Reasoning-Aware Relational Representation Learning for Open-Vocabulary Scene Graph Generation

- arXiv: [2611.13496](https://arxiv.org/abs/2611.13496) | [PDF](https://arxiv.org/pdf/2611.13496) | [papers.cool](https://papers.cool/arxiv/2611.13496)
- Authors: Jiawei Xiao, Boya Wang, Longtian Qiu, Shan Ning, Xuming He
- Published: 2026-11-10 03:08 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Open-Vocabulary Scene Graph Generation (OV-SGG) requires models to recognize visual relationships beyond the training vocabulary, yet existing methods often rely on dataset-specific object--predicate co-occurrence patterns. Under long-tailed distributions and noisy object localization, such reliance leads to biased,...

### 28 - Curriculum proof repair with learned counterexamples

- arXiv: [2611.13627](https://arxiv.org/abs/2611.13627) | [PDF](https://arxiv.org/pdf/2611.13627) | [papers.cool](https://papers.cool/arxiv/2611.13627)
- Authors: Yuechun Sun, Jun Yang, Kexin Pei
- Published: 2026-11-10 06:14 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory
- Abstract skim: Language models (LMs) have substantially lowered the barrier to applying formal verification for building reliable and secure software. Existing approaches commonly follow the verifier-in-the-loop paradigm, but the verifier often provides only coarse, binary pass/fail feedback, which offers little actionable signal...

### 28 - Seeing Is Not Believing: Counterfactual Lesion Erasure Teaches a Small Medical Vision-Language Agent to Report Only What the Image Shows

- arXiv: [2611.13006](https://arxiv.org/abs/2611.13006) | [PDF](https://arxiv.org/pdf/2611.13006) | [papers.cool](https://papers.cool/arxiv/2611.13006)
- Authors: Bhaskar Gurram
- Published: 2026-11-08 23:09 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: language agent; rl_post_training: dpo
- Abstract skim: Medical vision-language models (VLMs) often report a finding because the question names it; standard benchmarks miss this. From public segmentation datasets we build counterfactual views without manual annotation: the lesion erased by inpainting, a same-shape control edit elsewhere, and unedited lesion-free images....

### 27 - Train High, Ship Low: Efficient LoRA Synchronization for Distributed On-Policy Post-Training

- arXiv: [2611.13306](https://arxiv.org/abs/2611.13306) | [PDF](https://arxiv.org/pdf/2611.13306) | [papers.cool](https://papers.cool/arxiv/2611.13306)
- Authors: Shenghui Li, Li Ju, Thiemo Voigt
- Published: 2026-11-09 22:18 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; planning_and_action: rollout
- Abstract skim: Transmitting LoRA adapters to rollout workers can bottleneck distributed on-policy post-training over bandwidth-constrained networks. Lowering the training rank may limit the capacity a workload needs, while adaptive optimizer updates are difficult to compress. Rollout workers can instead reconstruct updates from...

### 27 - Audited Gradients, Anchored Policies: Model-Based Reinforcement Learning for Efficient Flow Control

- arXiv: [2611.13203](https://arxiv.org/abs/2611.13203) | [PDF](https://arxiv.org/pdf/2611.13203) | [papers.cool](https://papers.cool/arxiv/2611.13203)
- Authors: Ruige Kong, Stefania Fresca
- Published: 2026-11-09 20:28 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory
- Abstract skim: Feedback controllers for flows are expensive to design, since each candidate must be evaluated with a high-fidelity solver. Differentiable surrogates reduce that cost, but they also introduce a failure mode that prediction error cannot detect. Policy optimization uses the derivative of the objective with respect to...

### 25 - Opportunity-Cost Option-Critic: Adaptive Switching Costs for Robust Hierarchical Reinforcement Learning

- arXiv: [2611.14099](https://arxiv.org/abs/2611.14099) | [PDF](https://arxiv.org/pdf/2611.14099) | [papers.cool](https://papers.cool/arxiv/2611.14099)
- Authors: Khaled Ammoura, Aya Kayal, Naseem Daher
- Published: 2026-11-10 13:55 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: deliberation
- Abstract skim: Deliberation costs are commonly used in hierarchical reinforcement learning (HRL) to prevent options from collapsing to primitive actions. Existing approaches rely on fixed penalties or duration-based adaptations, both of which are indirect proxies for an option's utility. This paper argues that option persistence...

### 25 - Discrete Model-Based Diffusion for Combinatorial Optimization in Multi-Robot Task Allocation

- arXiv: [2611.13382](https://arxiv.org/abs/2611.13382) | [PDF](https://arxiv.org/pdf/2611.13382) | [papers.cool](https://papers.cool/arxiv/2611.13382)
- Authors: Haejoon Lee, Thomas Marshall Vielmetti, Xinyi Wang, Dimitra Panagou
- Published: 2026-11-09 23:59 UTC | Categories: cs.LG, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: decision making
- Abstract skim: Decision making in multi-agent and multi-robot systems often involves discrete decision variables, leading to NP-hard combinatorial optimization problems that must be solved within seconds for near real-time implementation. Denoising diffusion has emerged as a powerful tool for such problems, but existing approaches...

### 24 - When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents

- arXiv: [2611.14326](https://arxiv.org/abs/2611.14326) | [PDF](https://arxiv.org/pdf/2611.14326) | [papers.cool](https://papers.cool/arxiv/2611.14326)
- Authors: Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, Zecheng Sheng, et al. (7 authors)
- Published: 2026-11-10 16:52 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: tool use; reasoning: self-improvement, self improvement; memory_and_benchmarks: memory, long-term memory, webarena
- Abstract skim: LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-...

### 24 - Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them

- arXiv: [2611.13254](https://arxiv.org/abs/2611.13254) | [PDF](https://arxiv.org/pdf/2611.13254) | [papers.cool](https://papers.cool/arxiv/2611.13254)
- Authors: Shaohuang Wang, Jinghao Wen, Xulei Zhang, Xun Jiao
- Published: 2026-11-09 21:25 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, multi-agent; planning_and_action: trajectory
- Abstract skim: When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradicted it, or which control could have...

### 24 - Reinforcement Learning based control of Cancer Chemotherapy treatments

- arXiv: [2611.12940](https://arxiv.org/abs/2611.12940) | [PDF](https://arxiv.org/pdf/2611.12940) | [papers.cool](https://papers.cool/arxiv/2611.12940)
- Authors: Jayakody Kankanamalage Chamani Shiranthika
- Published: 2026-11-06 16:31 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization
- Abstract skim: Reinforcement Learning has achieved tremendous success in recent years. Extending its scope from the traditional complex games such as Atari, Go, Pokeman, and Chess, reinforcement learning has caught researchers' attention on modelling real-life scenarios. Personalized medicine and the dynamic treatment regimen are...

### 23 - Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning

- arXiv: [2611.14419](https://arxiv.org/abs/2611.14419) | [PDF](https://arxiv.org/pdf/2611.14419) | [papers.cool](https://papers.cool/arxiv/2611.14419)
- Authors: Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig
- Published: 2026-11-10 17:58 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially...

### 21 - DrugCoding: A Scientific Programming Agent for Drug Discovery

- arXiv: [2611.13651](https://arxiv.org/abs/2611.13651) | [PDF](https://arxiv.org/pdf/2611.13651) | [papers.cool](https://papers.cool/arxiv/2611.13651)
- Authors: Junwei Hu, Zhuohao Lin, Kun Li, Hengnan Zhang
- Published: 2026-11-10 06:47 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent, agent collaboration; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Drug discovery involves multiple interconnected research stages, including molecular design, property prediction, and virtual screening. These processes are characterized by complex workflows, interdependent computational tasks, and diverse specialized tools, placing substantial demands on the coordination of...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
