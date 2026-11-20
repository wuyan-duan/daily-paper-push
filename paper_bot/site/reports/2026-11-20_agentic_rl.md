# RL / Post-Training / Agentic RL Reading Queue - 2026-11-20

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 526. Minimum score: 8.

## Top Picks

### 63 - ROAM-GRPO: Enforcing Reasoning Diversity in GRPO via Routed Off-mode Approach Mining

- arXiv: [2611.25926](https://arxiv.org/abs/2611.25926) | [PDF](https://arxiv.org/pdf/2611.25926) | [papers.cool](https://papers.cool/arxiv/2611.25926)
- Authors: Jeff Duan, Matt Thomson
- Published: 2026-11-19 11:09 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Supervised fine-tuning (SFT) paired with Reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant recipe for post-training LLMs on complex reasoning tasks, but has been shown to collapse the policy into a low-diversity mode. Repeated LLM outputs are nearly identical, and pass@k accuracy...

### 50 - Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens

- arXiv: [2611.25570](https://arxiv.org/abs/2611.25570) | [PDF](https://arxiv.org/pdf/2611.25570) | [papers.cool](https://papers.cool/arxiv/2611.25570)
- Authors: Jinhan Li, Zhisheng Chen, Yuxuan Li, Yuan Gao, Fan Xu, Hao Wu, et al. (8 authors)
- Published: 2026-11-19 06:10 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; memory_and_benchmarks: benchmark
- Abstract skim: Global medium-range weather forecasting must not only generate ensembles efficiently to characterize uncertainty in future states, but also serve downstream applications such as extreme-event warnings and cross-sphere coupled simulations. We introduce WeatherCraft, a framework that unifies probabilistic generation...

### 47 - AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher

- arXiv: [2611.26510](https://arxiv.org/abs/2611.26510) | [PDF](https://arxiv.org/pdf/2611.26510) | [papers.cool](https://papers.cool/arxiv/2611.26510)
- Authors: Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao
- Published: 2026-11-19 17:57 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent; rl_post_training: post-training, post training; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress...

### 45 - Sage-Evolve-Preview:Adaptive Observation for Post-Training Self-Improvement

- arXiv: [2611.26132](https://arxiv.org/abs/2611.26132) | [PDF](https://arxiv.org/pdf/2611.26132) | [papers.cool](https://papers.cool/arxiv/2611.26132)
- Authors: Yinhao Tang, Youqing Fang, Yanan Sun, Xintian Shen, Hanyu Sun, Wenran Liu, et al. (10 authors)
- Published: 2026-11-19 13:52 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Post-training recursive self-improvement (RSI) iteratively improves a target capability, operationalized by a fixed anchor benchmark, through repeated intervention, training, and evaluation. Yet most loops use the anchor's aggregate score as their sole observation, so early gains give way to stalled progress and...

### 44 - Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy

- arXiv: [2611.26172](https://arxiv.org/abs/2611.26172) | [PDF](https://arxiv.org/pdf/2611.26172) | [papers.cool](https://papers.cool/arxiv/2611.26172)
- Authors: Ilia Zavidnyi, Alexander Kovrigin, Arina Puchkova, Kirill Gelvan, Sergey Titov
- Published: 2026-11-19 14:20 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, rlvr; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reasoning models often become more accurate when they can generate longer answers at test time. This behavior is known as test-time scaling. However, RL with verifiable rewards (RLVR) usually trains them with a fixed rollout cap. We find that this cap changes model behavior, not only training cost. After training,...

### 41 - Decision-Focused Reinforcement Learning for LLM Post-Training

- arXiv: [2611.25597](https://arxiv.org/abs/2611.25597) | [PDF](https://arxiv.org/pdf/2611.25597) | [papers.cool](https://papers.cool/arxiv/2611.25597)
- Authors: Haotian Zhai, Leqi Liu
- Published: 2026-11-19 06:44 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: planning; memory_and_benchmarks: evaluation; downranked: inventory
- Abstract skim: Large language models (LLMs) have shown promise as predictors across various tasks, benefiting from their ability to use information from unstructured context. However, when predictions serve as parameters of downstream optimization problems, higher prediction accuracy does not necessarily translate into lower...

### 41 - Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents

- arXiv: [2611.25123](https://arxiv.org/abs/2611.25123) | [PDF](https://arxiv.org/pdf/2611.25123) | [papers.cool](https://papers.cool/arxiv/2611.25123)
- Authors: Ziyan Yang, Taiwei Shi, Jieyu Zhao
- Published: 2026-11-18 20:02 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agent memory, long-horizon agent; rl_post_training: reinforcement learning; planning_and_action: trajectory; memory_and_benchmarks: memory, evaluation
- Abstract skim: Long-horizon LLM agents often exceed their context windows, forcing them to discard information that may be needed later. Existing context management strategies rely on summarization, masking, or structured memory, requiring decisions about what to preserve or how to retrieve it before future needs are known....

### 40 - Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization

- arXiv: [2611.25380](https://arxiv.org/abs/2611.25380) | [PDF](https://arxiv.org/pdf/2611.25380) | [papers.cool](https://papers.cool/arxiv/2611.25380)
- Authors: BoHao Chen
- Published: 2026-11-19 02:20 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent harness; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning
- Abstract skim: Domain specialization of LLM agents is usually framed as a weight-update problem: collect trajectories, run reinforcement learning (RL) or supervised fine-tuning (SFT), and deploy a new checkpoint. We study a complementary axis: evolving the \textbf{agent harness}---the system prompt, tool schemas, skill library,...

### 38 - Exposure-Aware Informative Path Planning Using Deep Reinforcement Learning

- arXiv: [2611.26302](https://arxiv.org/abs/2611.26302) | [PDF](https://arxiv.org/pdf/2611.26302) | [papers.cool](https://papers.cool/arxiv/2611.26302)
- Authors: Muzaffar Qureshi, Yihui Mao, James W. Cross, Kyle Volle, Rushikesh Kamalapurkar
- Published: 2026-11-19 15:54 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; planning_and_action: planning
- Abstract skim: This paper addresses the finite-budget exposure-aware informative path planning (IPP) problem for a fleet of mobile sensing agents. The agents map an unknown scalar field while limiting exposure to high field intensity. Existing IPP methods optimize informativeness under motion or resource constraints, but do not...

### 38 - EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and RL

- arXiv: [2611.26196](https://arxiv.org/abs/2611.26196) | [PDF](https://arxiv.org/pdf/2611.26196) | [papers.cool](https://papers.cool/arxiv/2611.26196)
- Authors: Wei Dai, Jinkun Liu, Jiayi Chen, Han Liu, Wenbo Ding, Shaolun Huang
- Published: 2026-11-19 14:41 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; reasoning: outcome reward; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Vision-language models (VLMs) can act as closed-loop robot-use agents (RUAs) by writing and executing control code through tool interfaces. However, turning an open-weight VLM into a high-performing embodied agent requires a complete post-training stack: out-of-the-box open VLMs fail completely at interactive tool...

### 35 - Beam Model Technical Report

- arXiv: [2611.26358](https://arxiv.org/abs/2611.26358) | [PDF](https://arxiv.org/pdf/2611.26358) | [papers.cool](https://papers.cool/arxiv/2611.26358)
- Authors: Reflection Team, Adam Abdulhamid, Osama Abuelsorour, Yasmin Alameddine, Carlo Alfano, Duarte Alves, et al. (230 authors)
- Published: 2026-11-19 16:28 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on...

### 33 - Calibrated Decision Rewards: Training Language Models with a Judge That Knows How Sure It Is

- arXiv: [2611.25135](https://arxiv.org/abs/2611.25135) | [PDF](https://arxiv.org/pdf/2611.25135) | [papers.cool](https://papers.cool/arxiv/2611.25135)
- Authors: Rudransh Agnihotri, Manasvi Kapoor
- Published: 2026-11-18 20:15 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, reward model, grpo; reasoning: process reward
- Abstract skim: Reinforcement learning (RL) can only teach a language model what its reward can recognize. Answer checkers are exact but need a reference answer; learned reward models and LLM judges work everywhere, but their scores are not probabilities. We study RLCDR (Reinforcement Learning from Calibrated Decision Rewards). An...

### 32 - RL Post-Training in Diffusion Transformers Is Activation Steering

- arXiv: [2611.26627](https://arxiv.org/abs/2611.26627) | [PDF](https://arxiv.org/pdf/2611.26627) | [papers.cool](https://papers.cool/arxiv/2611.26627)
- Authors: Tuna Han Salih Meral, Kaan Oktay, Alec Helbling, Atakan Kara, Duen Horng Chau, Pinar Yanardag
- Published: 2026-11-19 18:59 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that improving them...

### 30 - WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation

- arXiv: [2611.25251](https://arxiv.org/abs/2611.25251) | [PDF](https://arxiv.org/pdf/2611.25251) | [papers.cool](https://papers.cool/arxiv/2611.25251)
- Authors: Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo, Roberto Martín-Martín
- Published: 2026-11-18 22:36 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: world model
- Abstract skim: Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration is unsafe and simulator RL can exploit residual sim-to-real gaps. We present WEVO, a teleoperation-free framework for post-training a whole-body humanoid VLA in an action-conditioned video world...

### 29 - GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers

- arXiv: [2611.26509](https://arxiv.org/abs/2611.26509) | [PDF](https://arxiv.org/pdf/2611.26509) | [papers.cool](https://papers.cool/arxiv/2611.26509)
- Authors: Sahibzada Allahyar, Julia White, Dhruv Atreja, George Hurn-Maloney, Urchade Zaratiana
- Published: 2026-11-19 17:56 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning. Yet reasoning can substantially improve decision quality, raising the question of whether its benefits can be retained without the cost of generating it....

### 28 - When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards

- arXiv: [2611.25793](https://arxiv.org/abs/2611.25793) | [PDF](https://arxiv.org/pdf/2611.25793) | [papers.cool](https://papers.cool/arxiv/2611.25793)
- Authors: Yingshuo Wang, Weixiang Zhao, Guancheng Li, Jiahe Guo, Yu Zhang, Yanyan Zhao
- Published: 2026-11-19 09:22 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; memory_and_benchmarks: evaluation
- Abstract skim: Multimodal safety guards increasingly generate rationales alongside safety predictions, yet whether these rationales are reliable remains largely unexplored. We systematically study *rationale hallucination* from two perspectives: visual rationale hallucination, where rationales contain unsupported visual facts, and...

### 28 - PAIR-MED: Policy-reward Alternation for Iterative Refinement in Multilingual Medical Reasoning

- arXiv: [2611.25446](https://arxiv.org/abs/2611.25446) | [PDF](https://arxiv.org/pdf/2611.25446) | [papers.cool](https://papers.cool/arxiv/2611.25446)
- Authors: Fan Gao, Xiaohang Xu, Lang Huang, Nan Lu, Irene Li
- Published: 2026-11-19 03:25 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, process reward; planning_and_action: trajectory
- Abstract skim: Large language models demonstrate strong medical question-answering capabilities, yet reasoning performance remains uneven across languages. Process reward models (PRMs) provide step-level feedback for improving reasoning, but a fixed PRM may become increasingly misaligned with the trajectory distribution of an...

### 27 - Actor-Predictor Architecture for Reinforcement Learning with Formal Specification Objectives

- arXiv: [2611.26313](https://arxiv.org/abs/2611.26313) | [PDF](https://arxiv.org/pdf/2611.26313) | [papers.cool](https://papers.cool/arxiv/2611.26313)
- Authors: Josef Brozovich, Qining Zhang, Lei Ying
- Published: 2026-11-19 16:03 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory
- Abstract skim: One fundamental challenge in reinforcement learning (RL) is enforcing temporal safety constraints, such as satisfying formal specifications. Existing methods often transform logic formulas into automata for state augmentation and reward shaping. However, this approach assumes that automaton construction is both...

### 27 - RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration

- arXiv: [2611.26179](https://arxiv.org/abs/2611.26179) | [PDF](https://arxiv.org/pdf/2611.26179) | [papers.cool](https://papers.cool/arxiv/2611.26179)
- Authors: Weiyu Zhou, Jiacong Tang, Tao Hu, Axi Niu, Jinqiu Sun, Peng Wu, et al. (8 authors)
- Published: 2026-11-19 14:29 UTC | Categories: cs.AI
- Why it matched: rl_post_training: preference optimization, dpo; planning_and_action: trajectory
- Abstract skim: Images under non-uniform coupled degradations require diverse restoration capabilities for different degraded regions. Existing methods employ globally uniform operations, potentially overlooking regional differences and causing incomplete restoration or even damage to image content. Moreover, a degraded region may...

### 26 - Training LLMs to Follow Reasoning Instructions with Minimal Edits

- arXiv: [2611.26342](https://arxiv.org/abs/2611.26342) | [PDF](https://arxiv.org/pdf/2611.26342) | [papers.cool](https://papers.cool/arxiv/2611.26342)
- Authors: Alexandra Yakovleva, Luat Gia Khoi Nguyen, Juho Kannala, Harri Valpola, Alexander Ilin
- Published: 2026-11-19 16:18 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Large language models increasingly rely on extended reasoning traces, yet the training signals used to shape this behavior remain coarse. Supervised fine-tuning on full trajectories forces the model to imitate an entire demonstration, overconstraining its output distribution, while trajectory-level reinforcement...

### 25 - RL Can Only Reinforce What It Sees Succeed

- arXiv: [2611.26084](https://arxiv.org/abs/2611.26084) | [PDF](https://arxiv.org/pdf/2611.26084) | [papers.cool](https://papers.cool/arxiv/2611.26084)
- Authors: Ruben Sanchez-Corcuera, Unai Zulaika, Aritz Bilbao-Jayo, Miguel Fernandez-de-Retana
- Published: 2026-11-19 13:24 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: outcome reward
- Abstract skim: When a familiar rule stops working, an agent has to weigh what pre-training taught it against what it now observes. We ask how outcome-reward reinforcement learning (RL) changes this balance, in a puzzle world where both sides are known: small language models trained from scratch on games played by a Bayesian...

### 25 - MatVerse: A Foundation Model for Materials Science

- arXiv: [2611.25651](https://arxiv.org/abs/2611.25651) | [PDF](https://arxiv.org/pdf/2611.25651) | [papers.cool](https://papers.cool/arxiv/2611.25651)
- Authors: Xuanyu Zhu, Qian Tan, Bo Chen, Jiaqing Xie, Yang Han, Mei Wu, et al. (18 authors)
- Published: 2026-11-19 07:33 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Materials science involves highly heterogeneous scientific information, including textual knowledge, molecular and crystal structures, experimental characterization data, microscopy images, and structure-property relationships. Developing a general-purpose foundation model capable of understanding and reasoning over...

### 25 - Cross-Question Reliable Reinforcement Learning

- arXiv: [2611.25292](https://arxiv.org/abs/2611.25292) | [PDF](https://arxiv.org/pdf/2611.25292) | [papers.cool](https://papers.cool/arxiv/2611.25292)
- Authors: Hector G. Rodriguez, Marcus Rohrbach
- Published: 2026-11-18 23:41 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: AI systems operating near the limits of their capabilities can maximize utility while minimizing the risk of error by abstaining or deferring questions they are not confident about to a human or a stronger model. Recently, large language models (LLMs) have been post-trained to estimate confidence in their own...

### 25 - From Self-Play RL to Constrained Control: Distilling DiffMPC Students with DAgger

- arXiv: [2611.25197](https://arxiv.org/abs/2611.25197) | [PDF](https://arxiv.org/pdf/2611.25197) | [papers.cool](https://papers.cool/arxiv/2611.25197)
- Authors: Luca M. Hartmann, Parinaz Naghizadeh
- Published: 2026-11-18 21:17 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, ppo; reasoning: self-play; downranked: driving
- Abstract skim: Self-play reinforcement learning (RL) produces strong driving policies, but these policies are hard to verify or interpret. Differentiable model predictive control (DiffMPC) can enforce explicit constraints, but it is usually trained by imitating logged data or with costly RL. To add constraints to an already...

### 24 - Represented but misread: Post-training changes how language models read out what they represent

- arXiv: [2611.26584](https://arxiv.org/abs/2611.26584) | [PDF](https://arxiv.org/pdf/2611.26584) | [papers.cool](https://papers.cool/arxiv/2611.26584)
- Authors: Jochen Laubrock
- Published: 2026-11-19 18:43 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training
- Abstract skim: Does post-training change what a language model represents, or how this representation is read out into an answer? We compared linear probes with the models' own answers, analyzed with signal detection theory, in six open-weight base models and their post-trained versions. For judgments of whether German texts were...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
