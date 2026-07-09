# RL / Post-Training / Agentic RL Reading Queue - 2026-07-09

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 306. Minimum score: 8.

## Top Picks

### 81 - Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

- arXiv: [2607.07508](https://arxiv.org/abs/2607.07508) | [PDF](https://arxiv.org/pdf/2607.07508) | [papers.cool](https://papers.cool/arxiv/2607.07508)
- Authors: Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong
- Published: 2026-07-08 15:02 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks. Recently, asynchronous RL has emerged as a more efficient alternative by...

### 74 - Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning

- arXiv: [2607.07178](https://arxiv.org/abs/2607.07178) | [PDF](https://arxiv.org/pdf/2607.07178) | [papers.cool](https://papers.cool/arxiv/2607.07178)
- Authors: Zetian Hu, Shunyu Liu, Junjie Zhang, Yongcheng Jing, Ting-En Lin, Yongbin Li, et al. (7 authors)
- Published: 2026-07-08 09:13 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: Recent breakthroughs of Reinforcement Learning (RL) have highlighted its potential for complex agentic Large Language Model (LLM) tasks. However, existing efforts largely focus on single-task settings, whereas real-world deployment necessitates a generalist agent capable of solving multiple tasks simultaneously. In...

### 56 - Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF

- arXiv: [2607.07693](https://arxiv.org/abs/2607.07693) | [PDF](https://arxiv.org/pdf/2607.07693) | [papers.cool](https://papers.cool/arxiv/2607.07693)
- Authors: Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
- Published: 2026-07-08 17:49 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, policy optimization, +2 more
- Abstract skim: Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This...

### 48 - Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems

- arXiv: [2607.07674](https://arxiv.org/abs/2607.07674) | [PDF](https://arxiv.org/pdf/2607.07674) | [papers.cool](https://papers.cool/arxiv/2607.07674)
- Authors: Vladislav Beliaev
- Published: 2026-07-08 17:32 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Group Relative Policy Optimization (GRPO) stalls on a model's hardest problems: when no rollout in a group succeeds, the group-relative advantages vanish and the problem contributes no gradient, wasting the frontier examples we most want to learn from. Prepending a correct prefix of a reference solution raises the...

### 37 - Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

- arXiv: [2607.07690](https://arxiv.org/abs/2607.07690) | [PDF](https://arxiv.org/pdf/2607.07690) | [papers.cool](https://papers.cool/arxiv/2607.07690)
- Authors: Vladislav Beliaev
- Published: 2026-07-08 17:49 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reward model, grpo; reasoning: reasoning
- Abstract skim: Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce...

### 37 - RL Post-Training Builds Compositional Reasoning Strategies

- arXiv: [2607.07646](https://arxiv.org/abs/2607.07646) | [PDF](https://arxiv.org/pdf/2607.07646) | [papers.cool](https://papers.cool/arxiv/2607.07646)
- Authors: Azwar Abdulsalam, Nishil Patel, Andrew Saxe
- Published: 2026-07-08 17:04 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A...

### 35 - Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization

- arXiv: [2607.06610](https://arxiv.org/abs/2607.06610) | [PDF](https://arxiv.org/pdf/2607.06610) | [papers.cool](https://papers.cool/arxiv/2607.06610)
- Authors: Sounaq Das, Tanmay Sen, Raghu Nandan Sengupta, Aditya Gupta
- Published: 2026-07-07 06:24 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; planning_and_action: decision making
- Abstract skim: Portfolio optimization under uncertainty is inherently a multi-objective decision problem involving complex interactions among return, risk, market dynamics, and practical investment constraints. Existing reliability based portfolio optimization approaches primarily rely on static optimization frameworks and often...

### 30 - Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies

- arXiv: [2607.07029](https://arxiv.org/abs/2607.07029) | [PDF](https://arxiv.org/pdf/2607.07029) | [papers.cool](https://papers.cool/arxiv/2607.07029)
- Authors: Dennis Gross, Quentin Mazouni, Helge Spieker, Arnaud Gotlieb
- Published: 2026-07-08 06:00 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Reinforcement learning (RL) policies can be unsafe and vulnerable to attacks. Ensuring their reliability is often a pain point as existing automated testing methods target only selected environments, testing scenarios, and RL algorithms. To address this, we propose a comprehensive framework for testing single- and...

### 29 - Geometric Self-Distillation for Reasoning Generalization

- arXiv: [2607.06855](https://arxiv.org/abs/2607.06855) | [PDF](https://arxiv.org/pdf/2607.06855) | [papers.cool](https://papers.cool/arxiv/2607.06855)
- Authors: Josip Jukić, Ivan Titov
- Published: 2026-07-07 23:16 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: On-policy distillation is a practical post-training recipe for large language models, supplying dense teacher supervision on the student's own trajectories. In privileged-context self-distillation, teacher and student are the same model conditioned on the same prefix, but the teacher also sees a hint or the full...

### 29 - When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning

- arXiv: [2607.06720](https://arxiv.org/abs/2607.06720) | [PDF](https://arxiv.org/pdf/2607.06720) | [papers.cool](https://papers.cool/arxiv/2607.06720)
- Authors: Yotam Wolf, Noam Wies, Amnon Shashua
- Published: 2026-07-07 18:36 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, reflection
- Abstract skim: Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines...

### 26 - Reasoning Consistency Scanning: A Framework for Auditing Chain-of-Thought Validity in AI Safety Evaluations

- arXiv: [2607.07229](https://arxiv.org/abs/2607.07229) | [PDF](https://arxiv.org/pdf/2607.07229) | [papers.cool](https://papers.cool/arxiv/2607.07229)
- Authors: Silvia Santano
- Published: 2026-07-08 10:13 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Prior work has shown that chain-of-thought (CoT) reasoning is often unfaithful: a model's stated reasoning does not reliably reflect the process that produced its output. Detecting unfaithfulness, though, requires controlled experimental interventions, which cannot be applied to evaluation transcripts after the...

### 26 - Online Data Selection Is Implicit Alignment

- arXiv: [2607.07023](https://arxiv.org/abs/2607.07023) | [PDF](https://arxiv.org/pdf/2607.07023) | [papers.cool](https://papers.cool/arxiv/2607.07023)
- Authors: Aoxiong Zeng, Yuxin Yang, Xiangquan Yang
- Published: 2026-07-08 05:44 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, preference optimization, reward model; memory_and_benchmarks: evaluation
- Abstract skim: Supervised fine-tuning (SFT) is often treated as a capability-adaptation step, while alignment is attributed to later preference optimization or reinforcement learning. This separation is incomplete: when examples are scored and kept online during fine-tuning, the choice of which data to train on already changes the...

### 25 - A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation

- arXiv: [2607.06990](https://arxiv.org/abs/2607.06990) | [PDF](https://arxiv.org/pdf/2607.06990) | [papers.cool](https://papers.cool/arxiv/2607.06990)
- Authors: Yi-Xiang He, Lan Wei, Haoming Cen, Jian-Jian Jiang, Zhuohao Li, Guanxing Lu, et al. (9 authors)
- Published: 2026-07-08 04:23 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent, tool use; reasoning: reasoning; planning_and_action: planning
- Abstract skim: Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an...

### 25 - UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma

- arXiv: [2607.06987](https://arxiv.org/abs/2607.06987) | [PDF](https://arxiv.org/pdf/2607.06987) | [papers.cool](https://papers.cool/arxiv/2607.06987)
- Authors: Chongyu Fan, Pengfei Liu, Jingjia Huang, Sijia Liu, Yi Lin
- Published: 2026-07-08 04:21 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL) has become the standard paradigm for enhancing the complex reasoning capabilities of large language models (LLMs). To achieve sample efficiency, modern RL frameworks rely on importance sampling (IS). However, these algorithms suffer from an exploration-stability dilemma. Pure IS often...

### 24 - Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety

- arXiv: [2607.07695](https://arxiv.org/abs/2607.07695) | [PDF](https://arxiv.org/pdf/2607.07695) | [papers.cool](https://papers.cool/arxiv/2607.07695)
- Authors: Yujiao Chen
- Published: 2026-07-08 17:53 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-...

### 24 - PeTeR: Post-Training Robustification of Probabilistic Circuits

- arXiv: [2607.07671](https://arxiv.org/abs/2607.07671) | [PDF](https://arxiv.org/pdf/2607.07671) | [papers.cool](https://papers.cool/arxiv/2607.07671)
- Authors: Adrian Ciotinga, Yeming Dai, YooJung Choi
- Published: 2026-07-08 17:25 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training
- Abstract skim: Probabilistic circuits (PCs) can model complex joint distributions while supporting exact and efficient computation of many inference queries. However, standard likelihood-based PC learning is vulnerable to overfitting and fragile generalization when confronted with data noise, small sample sizes, or distribution...

### 24 - A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling

- arXiv: [2607.07666](https://arxiv.org/abs/2607.07666) | [PDF](https://arxiv.org/pdf/2607.07666) | [papers.cool](https://papers.cool/arxiv/2607.07666)
- Authors: Shivendra G. Tewari, Holly Kimko
- Published: 2026-07-08 17:22 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity and quantitative rigor. Here we present Ensemble QSP, a multi-agent framework featuring a three-layer...

### 22 - Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops

- arXiv: [2607.07663](https://arxiv.org/abs/2607.07663) | [PDF](https://arxiv.org/pdf/2607.07663) | [papers.cool](https://papers.cool/arxiv/2607.07663)
- Authors: Mingguang Chen, Licheng Wang, Bo Qu
- Published: 2026-07-08 17:19 UTC | Categories: cs.AI
- Why it matched: reasoning: self-improvement, self improvement, self-play, process reward; memory_and_benchmarks: evaluation
- Abstract skim: AI systems increasingly participate in their own improvement: revising their outputs, adapting their own harnesses during deployment, training on data they generate, and, increasingly, conducting AI research itself. This literature is described under a vocabulary ("self-refine," "self-reward," "self-play," "self-...

### 22 - When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems

- arXiv: [2607.06807](https://arxiv.org/abs/2607.06807) | [PDF](https://arxiv.org/pdf/2607.06807) | [papers.cool](https://papers.cool/arxiv/2607.06807)
- Authors: Haowen Xu, Xue Tan, Lei Ma, Zhihao Zhang, Chao Wang, Qingze Wang, et al. (9 authors)
- Published: 2026-07-07 21:12 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit...

### 21 - SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis

- arXiv: [2607.07467](https://arxiv.org/abs/2607.07467) | [PDF](https://arxiv.org/pdf/2607.07467) | [papers.cool](https://papers.cool/arxiv/2607.07467)
- Authors: Songhan Wang, Haoang Chi, He Li, Zhiheng Zhang, Jiayan Yuan, Cheems Wang, et al. (9 authors)
- Published: 2026-07-08 14:31 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; planning_and_action: planning, trajectory
- Abstract skim: Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a...

### 20 - Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1

- arXiv: [2607.06764](https://arxiv.org/abs/2607.06764) | [PDF](https://arxiv.org/pdf/2607.06764) | [papers.cool](https://papers.cool/arxiv/2607.06764)
- Authors: Kabir Moghe, Peter Chin
- Published: 2026-07-07 19:49 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Recent progress on ARC-AGI-1 from disclosed architectures has come broadly from two regimes: heavy test-time compute over frontier models (evolutionary search, exhaustive sampling, extended chain-of-thought), or benchmark-specific training in which small models are fine-tuned on ARC data, often with task-specialized...

### 19 - RLVP: Penalize the Path, Reward the Outcome

- arXiv: [2607.07435](https://arxiv.org/abs/2607.07435) | [PDF](https://arxiv.org/pdf/2607.07435) | [papers.cool](https://papers.cool/arxiv/2607.07435)
- Authors: Bojie Li, Noah Shi
- Published: 2026-07-08 14:06 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; planning_and_action: acting
- Abstract skim: Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not...

### 19 - Dynamic-in-Few-Step: Unifying Dynamic Computation and Few-Step Distillation for Efficient Video Generation

- arXiv: [2607.06631](https://arxiv.org/abs/2607.06631) | [PDF](https://arxiv.org/pdf/2607.06631) | [papers.cool](https://papers.cool/arxiv/2607.06631)
- Authors: Yu Cheng, Siyue Yao, Zhongang Qi, Shanyan Guan, Wei Li, Fajie Yuan
- Published: 2026-07-07 13:14 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; planning_and_action: rollout
- Abstract skim: Video Diffusion Models (VDMs) have demonstrated superior generation quality but suffer from prohibitive computational costs. While recent few-step distillation techniques significantly accelerate inference, they typically enforce a static model architecture across all denoising stages, ignoring the varying...

### 18 - Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors

- arXiv: [2607.07368](https://arxiv.org/abs/2607.07368) | [PDF](https://arxiv.org/pdf/2607.07368) | [papers.cool](https://papers.cool/arxiv/2607.07368)
- Authors: Oliver Makins, Orazio Angelini, Zohreh Shams, Mary Phuong
- Published: 2026-07-08 13:03 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; planning_and_action: acting, trajectory
- Abstract skim: AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning)...

### 18 - Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning

- arXiv: [2607.07117](https://arxiv.org/abs/2607.07117) | [PDF](https://arxiv.org/pdf/2607.07117) | [papers.cool](https://papers.cool/arxiv/2607.07117)
- Authors: Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee
- Published: 2026-07-08 07:58 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark
- Abstract skim: In text-to-image in-context learning (T2I-ICL), a model has to infer a latent compositional pattern from fewshot demonstrations for generating a query image. Recent studies show that state-of-the-art multimodal large language models struggle with this setting, particularly due to limited compositional reasoning and...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
