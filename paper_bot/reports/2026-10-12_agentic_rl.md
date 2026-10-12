# RL / Post-Training / Agentic RL Reading Queue - 2026-10-12

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 502. Minimum score: 8.

## Top Picks

### 86 - AdaC-GRPO: Towards Mastering Long-Horizon Visual Sudoku Puzzles via Adaptive Curriculum Learning

- arXiv: [2610.13184](https://arxiv.org/abs/2610.13184) | [PDF](https://arxiv.org/pdf/2610.13184) | [papers.cool](https://papers.cool/arxiv/2610.13184)
- Authors: Sida Li, Yuanxin Liu, Linli Yao, Shicheng Li, Xu Sun, Haoli Bai, et al. (7 authors)
- Published: 2026-10-09 08:08 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +4 more; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: While reinforcement learning with verifiable reward (RLVR) enhances reasoning in large language models, its efficacy in long-horizon multimodal tasks remains underexplored. Visual Sudoku puzzles pose a representative challenge, requiring multi-step deductive reasoning over both local constraints and global...

### 77 - Masked Diffusion Language Agents for Tool-Integrated Chemical Reasoning

- arXiv: [2610.13330](https://arxiv.org/abs/2610.13330) | [PDF](https://arxiv.org/pdf/2610.13330) | [papers.cool](https://papers.cool/arxiv/2610.13330)
- Authors: Mengdi Liu, Chenghao Jia, Hong Chang, Shiguang Shan
- Published: 2026-10-09 10:07 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: language agent, tool use; rl_post_training: post-training, post training, preference optimization; reasoning: reasoning; planning_and_action: planning, trajectory; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Designing tool-integrated reasoning agent systems for complex chemical tasks remains a fundamental challenge. Although recent chemical agents have demonstrated promising performance through the integration of external tools, they are still built on the autoregressive paradigm, which is inherently constrained by...

### 74 - Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits

- arXiv: [2610.13438](https://arxiv.org/abs/2610.13438) | [PDF](https://arxiv.org/pdf/2610.13438) | [papers.cool](https://papers.cool/arxiv/2610.13438)
- Authors: Chen Xi, Ding Ruixue, Wang Zhigaoyuan, Zhang Fanrui, Zhang Qiang, Chen Boli, et al. (12 authors)
- Published: 2026-10-09 11:37 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, tool use; rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: planning, rollout; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) has emerged as a key paradigm for improving large language model (LLM) agents, enabling stronger reasoning, planning, and tool-use in interactive environments. However, existing agent RL methods remain fundamentally constrained by an on-policy reasoning bottleneck: when tasks exceed the...

### 62 - TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents

- arXiv: [2610.12828](https://arxiv.org/abs/2610.12828) | [PDF](https://arxiv.org/pdf/2610.12828) | [papers.cool](https://papers.cool/arxiv/2610.12828)
- Authors: Debajoy Mukherjee, Jeremy Carleton, Sushil Vemuri, Srinivas Shakkottai, Dileep Kalathil
- Published: 2026-10-09 00:23 UTC | Categories: cs.LG
- Why it matched: agentic_rl: llm agent, agent training; rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Outcome-supervised group-relative policy optimization (GRPO) assigns the same advantage to every token in an LLM agent trajectory, leaving useful and unhelpful decisions undifferentiated. Hindsight credit assignment (HCA) can refine this feedback, but its estimates rely on trajectories containing informative...

### 57 - Matched-Context Group Policy Optimization for LLM Agent Training

- arXiv: [2610.13755](https://arxiv.org/abs/2610.13755) | [PDF](https://arxiv.org/pdf/2610.13755) | [papers.cool](https://papers.cool/arxiv/2610.13755)
- Authors: Chenxu Zhang, Yaorui Shi, Wenlong Zhang, Jianchao Tan, Zihan Wang, Yiming Cheng
- Published: 2026-10-09 15:41 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: llm agent, agent training; rl_post_training: policy optimization; planning_and_action: rollout; memory_and_benchmarks: alfworld
- Abstract skim: Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-...

### 55 - MENTOR: Learning from Failure with On-Policy Pedagogical Intervention

- arXiv: [2610.13594](https://arxiv.org/abs/2610.13594) | [PDF](https://arxiv.org/pdf/2610.13594) | [papers.cool](https://papers.cool/arxiv/2610.13594)
- Authors: Guanlan Yue, Hang Yu, Xiaoyong Huang, Ruipeng Li, Wei Zhang, Bingchang Liu, et al. (7 authors)
- Published: 2026-10-09 13:43 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, rlvr, policy optimization, grpo; reasoning: reasoning
- Abstract skim: Reinforcement Learning from Verifiable Rewards (RLVR) is a key driver for Large Reasoning Models, but it is vulnerable to "zero-reward collapse", a training failure where a sudden increase in task difficulty causes the learning signal to vanish. We argue that the conventional approach of discarding these failed...

### 51 - Cross-Behavior Policy Optimization: Unified Learning from Offline Demonstrations and On- and Off-Policy Rollouts via a Shared Regression Target

- arXiv: [2610.12830](https://arxiv.org/abs/2610.12830) | [PDF](https://arxiv.org/pdf/2610.12830) | [papers.cool](https://papers.cool/arxiv/2610.12830)
- Authors: Du Cheng, Junyu Lu, Jingfan Zhang, Yuzhuo Zhang, Haoxuan Jia, Shichao Weng
- Published: 2026-10-09 00:29 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Reasoning post-training draws on offline demonstrations and policy-generated rollouts, yet conventional supervised fine-tuning (SFT) followed by reinforcement learning (RL) separates their objectives and limits continued reuse of collected responses. We propose \textbf{Cross-Behavior Policy Optimization} (CBPO),...

### 49 - Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence

- arXiv: [2610.13015](https://arxiv.org/abs/2610.13015) | [PDF](https://arxiv.org/pdf/2610.13015) | [papers.cool](https://papers.cool/arxiv/2610.13015)
- Authors: Zhicheng Cai, Xinyuan Guo, Hanlin Wu, Weinan Dai, Yuyan Zhou, Wei-Ying Ma, et al. (8 authors)
- Published: 2026-10-09 05:17 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo, ppo; reasoning: reasoning
- Abstract skim: Reinforcement learning has become the foundational paradigm for enhancing the reasoning capabilities of LLMs. Yet the dominant approach, Proximal Policy Optimization (PPO), relies on a geometrically degenerate clipping proxy that cannot adapt its resistance to policy shifts, leading to premature clipping and...

### 47 - Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL

- arXiv: [2610.13020](https://arxiv.org/abs/2610.13020) | [PDF](https://arxiv.org/pdf/2610.13020) | [papers.cool](https://papers.cool/arxiv/2610.13020)
- Authors: Zhicheng Cai, Weinan Dai, Yuyan Zhou, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- Published: 2026-10-09 05:22 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement learning (RL) has become a dominant paradigm for enhancing LLMs' reasoning capabilities. Yet long-horizon autoregressive rollouts introduce a fundamental limitation: local policy mismatch can compound into severe state distribution shift over trajectories. Existing LLM RL methods, such as GRPO and...

### 45 - Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics

- arXiv: [2610.13522](https://arxiv.org/abs/2610.13522) | [PDF](https://arxiv.org/pdf/2610.13522) | [papers.cool](https://papers.cool/arxiv/2610.13522)
- Authors: Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen
- Published: 2026-10-09 12:44 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization, +1 more; planning_and_action: world model; memory_and_benchmarks: evaluation
- Abstract skim: Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions. However, existing robotic datasets provide limited coverage of the diverse interaction dynamics required for generalizable world modeling. Large-scale egocentric human videos...

### 45 - Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training

- arXiv: [2610.12933](https://arxiv.org/abs/2610.12933) | [PDF](https://arxiv.org/pdf/2610.12933) | [papers.cool](https://papers.cool/arxiv/2610.12933)
- Authors: Suorong Yang, Jiaxin Wang, Jiaming Su, Chentao Yue, Furao Shen, Peng Ye, et al. (7 authors)
- Published: 2026-10-09 03:26 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Large language models have achieved remarkable advances in complex reasoning. However, scaling reasoning post-training with ever-larger corpora can substantially increase training cost without proportional performance gains. In this study, we therefore ask: how far can reasoning supervision be compressed without...

### 44 - SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories

- arXiv: [2610.13356](https://arxiv.org/abs/2610.13356) | [PDF](https://arxiv.org/pdf/2610.13356) | [papers.cool](https://papers.cool/arxiv/2610.13356)
- Authors: Jiajun Hu, Chun Yong Chong
- Published: 2026-10-09 10:30 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Coding agents are increasingly deployed for end-to-end software engineering tasks, where a readily available oracle evaluator that defines the success criteria is often absent. This motivates verifications for coding agents that can reliably judge and explain their behavior. However, verification is non-trivial as...

### 42 - EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for Multimodal Emotion Preference Learning

- arXiv: [2610.13353](https://arxiv.org/abs/2610.13353) | [PDF](https://arxiv.org/pdf/2610.13353) | [papers.cool](https://papers.cool/arxiv/2610.13353)
- Authors: Zilong Huang, Kong Aik Lee, Zezhong Jin, Man-Wai Mak, Tatsuya Kawahara
- Published: 2026-10-09 10:28 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; memory_and_benchmarks: evaluation
- Abstract skim: Multimodal emotion preference learning uses pairwise comparisons to identify which open-ended emotion descriptions align more closely with human judgments. However, existing methods primarily focus on the final preference decision and provide little explicit supervision for localizing and correcting erroneous...

### 42 - MORAD: Reinforcement Learning with Multi-Objective Rewards for RNA Inverse Design

- arXiv: [2610.13305](https://arxiv.org/abs/2610.13305) | [PDF](https://arxiv.org/pdf/2610.13305) | [papers.cool](https://papers.cool/arxiv/2610.13305)
- Authors: Jixin Tang, Ji Guo, Jun Zhao
- Published: 2026-10-09 09:50 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, preference optimization; memory_and_benchmarks: evaluation
- Abstract skim: We introduce MORAD, an online reinforcement learning framework for backbone-conditioned RNA diffusion models that trains a single shared policy across diverse target backbones. Structure-conditioned RNA inverse design seeks nucleotide sequences compatible with a target three-dimensional backbone, yet existing...

### 42 - MADS: Multi-Agent Dialog Simulation for Robust Conversational Agents

- arXiv: [2610.12757](https://arxiv.org/abs/2610.12757) | [PDF](https://arxiv.org/pdf/2610.12757) | [papers.cool](https://papers.cool/arxiv/2610.12757)
- Authors: Arkajyoti Chakraborty, Adam Zernik, Ishika Kulkarni, Mudit Arora, Hugo Lin, Justin Chiu, et al. (9 authors)
- Published: 2026-10-08 22:08 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, rlvr; memory_and_benchmarks: benchmark
- Abstract skim: Task-oriented conversational agents remain fragile under realistic conditions, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present...

### 40 - Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation

- arXiv: [2610.12793](https://arxiv.org/abs/2610.12793) | [PDF](https://arxiv.org/pdf/2610.12793) | [papers.cool](https://papers.cool/arxiv/2610.12793)
- Authors: Yudong Liu, Yueqian Lin, Zijia Tang, Yuxi Zheng, Yuan Li, Shuai Zhang, et al. (14 authors)
- Published: 2026-10-08 23:00 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent, agent memory; reasoning: reasoning; memory_and_benchmarks: memory, episodic memory, benchmark
- Abstract skim: Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic memory directly to action chunks is hard. Yet the same policy, finetuned once to follow a...

### 37 - OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models

- arXiv: [2610.12914](https://arxiv.org/abs/2610.12914) | [PDF](https://arxiv.org/pdf/2610.12914) | [papers.cool](https://papers.cool/arxiv/2610.12914)
- Authors: Xule Gao, Xi Wang, Zehua Zang, Rui Wang, Changwen Zheng, Chuxiong Sun
- Published: 2026-10-09 03:04 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations. While effective for learning feasible actions, this paradigm supervises policies to reproduce expert actions at...

### 36 - Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems

- arXiv: [2610.12822](https://arxiv.org/abs/2610.12822) | [PDF](https://arxiv.org/pdf/2610.12822) | [papers.cool](https://papers.cool/arxiv/2610.12822)
- Authors: Yuepeng Hu, Pegah Ghahremani, Reza Aghajani, Mahesh Pasupuleti, Himaghna Bhattacharjee
- Published: 2026-10-09 00:02 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Multi-agent systems are increasingly used to solve coding tasks by coordinating agents that share code and plans. These agents are often optimized with reinforcement learning (RL) using automated evaluators, but bypassing evaluation can earn reward without producing a genuine solution. Prior work has largely treated...

### 35 - S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding

- arXiv: [2610.13202](https://arxiv.org/abs/2610.13202) | [PDF](https://arxiv.org/pdf/2610.13202) | [papers.cool](https://papers.cool/arxiv/2610.13202)
- Authors: Yuhang He, Hongyu Ge, Zihan Lin, Siyi Liu, Yongqi Zhang
- Published: 2026-10-09 08:22 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning; planning_and_action: rollout; downranked: traffic
- Abstract skim: Fast rollout generation for long-context reinforcement learning with verifiable rewards (RLVR) requires reducing KV-cache traffic without changing the response groups used for policy optimization. In our profiled RLVR workloads, attention accounts for 72--76\% of autoregressive decoding kernel time. Sparse attention...

### 35 - What Should SFT Learn? Conditional Information Gain for Generalizable Post-Training

- arXiv: [2610.12995](https://arxiv.org/abs/2610.12995) | [PDF](https://arxiv.org/pdf/2610.12995) | [papers.cool](https://papers.cool/arxiv/2610.12995)
- Authors: Yuxuan Gu, Kequan Niu, Xiaocheng Feng, Yun Li, Yiqiao Yang, Bing Qin
- Published: 2026-10-09 04:57 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Supervised fine-tuning (SFT) remains a widely used approach for post-training large language models, because fixed demonstrations can directly introduce desired reasoning strategies and behavioral patterns. Yet forcing a model to imitate externally provided trajectories may also interfere with behaviors already...

### 35 - Collaborative Learning and Reasoning over Model Slices

- arXiv: [2610.12927](https://arxiv.org/abs/2610.12927) | [PDF](https://arxiv.org/pdf/2610.12927) | [papers.cool](https://papers.cool/arxiv/2610.12927)
- Authors: Yuheng Wang, Runde Yang, Zhuohan Bao, Qiran Zhang, Huatao Li, Yiyang Zheng, et al. (12 authors)
- Published: 2026-10-09 03:17 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Large language models (LLMs) excel across diverse tasks, benefiting from knowledge priors, in-context reasoning, and test-time computation. Despite these strengths, single-model reasoning remains vulnerable to error propagation, as later steps depend on the model's earlier outputs, leaving reasoning blind spots...

### 33 - Collaborative Theory of Mind: Learning to Self-Revise by Anticipating User Responses

- arXiv: [2610.12872](https://arxiv.org/abs/2610.12872) | [PDF](https://arxiv.org/pdf/2610.12872) | [papers.cool](https://papers.cool/arxiv/2610.12872)
- Authors: Fanzhi Zeng, Anubrata Das, Maytal Saar-Tsechansky, Liu Leqi
- Published: 2026-10-09 02:01 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: Large language models (LLMs) demonstrate strong individual task performance, yet still struggle to collaborate with users over extended, multi-turn interactions, for example by attempting solutions before understanding the user's needs or by failing to revise mistaken assumptions after receiving feedback. We propose...

### 33 - Mitigating Capability Degradation in LLM Self-Improvement via Representation Geometry Regularization

- arXiv: [2610.12855](https://arxiv.org/abs/2610.12855) | [PDF](https://arxiv.org/pdf/2610.12855) | [papers.cool](https://papers.cool/arxiv/2610.12855)
- Authors: Jiaqi Tian, Ting Long
- Published: 2026-10-09 01:28 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement
- Abstract skim: On-Policy Self-distillation is a self-improvement paradigm that enables large language models (LLMs) to improve their capabilities by leveraging the same model as both teacher and student under different conditioning contexts. However, we find that OPSD methods can progressively degrade previously acquired...

### 32 - Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning

- arXiv: [2610.13923](https://arxiv.org/abs/2610.13923) | [PDF](https://arxiv.org/pdf/2610.13923) | [papers.cool](https://papers.cool/arxiv/2610.13923)
- Authors: Sajjad Baghaeea, Aimin Lib, Shanmugarajan Balasubramanian, Elif Uysal
- Published: 2026-10-09 17:53 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Deep-space communications operate under intermittent connectivity, long propagation delays, and relay storage constraints. In such networks, the Bundle Protocol enables store-carry-forward communication, requiring relay nodes to manage limited storage and scarce contact opportunities. Relay-side scheduling and...

### 32 - A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning

- arXiv: [2610.13744](https://arxiv.org/abs/2610.13744) | [PDF](https://arxiv.org/pdf/2610.13744) | [papers.cool](https://papers.cool/arxiv/2610.13744)
- Authors: Mayug Maniparambil, Ayush Rai, Ekansh Verma, Noel E. O'Connor, Fergal Reid
- Published: 2026-10-09 15:36 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: verifiable reward, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: On-policy self-distillation promises to replace the sparse outcome signal of verifiable-reward RL with dense token-level credit: a teacher conditioned on the reference solution scores the student's own rollout, and the resulting distributional shift is distilled back into the policy. We investigate whether this...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
