# RL / Post-Training / Agentic RL Reading Queue - 2026-11-18

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 473. Minimum score: 8.

## Top Picks

### 51 - Eyes in the Update? Learning Where Rewards Land in Multimodal Reasoning

- arXiv: [2611.22438](https://arxiv.org/abs/2611.22438) | [PDF](https://arxiv.org/pdf/2611.22438) | [papers.cool](https://papers.cool/arxiv/2611.22438)
- Authors: Lixuan He, Tianzhe Chu, Shulin Tian, Shikang Zheng, Feng Chen, Yi Ma
- Published: 2026-11-17 09:11 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Multimodal post-training has moved from broad instruction tuning toward reinforcement learning for image and video reasoning, where outcome rewards can improve final-answer accuracy. Yet these rewards are assigned to complete generated trajectories, while visual evidence is used only at sparse and uneven positions...

### 48 - Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies

- arXiv: [2611.22878](https://arxiv.org/abs/2611.22878) | [PDF](https://arxiv.org/pdf/2611.22878) | [papers.cool](https://papers.cool/arxiv/2611.22878)
- Authors: Yuhan Wang, Ruiyang Wang, Jiaguan Zhu
- Published: 2026-11-17 14:52 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more
- Abstract skim: Reinforcement learning (RL) enables post-training of flow-based vision-language-action (VLA) policies by optimizing expected task return through environment interaction. However, this optimization raises two challenges: policy updates can alter the velocity-field geometry underlying the score approximation used for...

### 43 - Better Rankers, Worse Retrievers: The Hidden Cost of RL Post-Training in Generative Recommendation

- arXiv: [2611.22838](https://arxiv.org/abs/2611.22838) | [PDF](https://arxiv.org/pdf/2611.22838) | [papers.cool](https://papers.cool/arxiv/2611.22838)
- Authors: Yuheng Chen, Fan Zhang, Yixuan Xu, Chao Yang, Yang Xiang, Can Yang
- Published: 2026-11-17 14:19 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model; planning_and_action: rollout
- Abstract skim: Generative recommenders decode the semantic ID of a user's next item with a language model, and post-training them with reinforcement learning (RL) after supervised fine-tuning (SFT) has become standard practice. The gains are mostly reported on the first ten results, yet in deployment such models hand hundreds of...

### 43 - TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks

- arXiv: [2611.22115](https://arxiv.org/abs/2611.22115) | [PDF](https://arxiv.org/pdf/2611.22115) | [papers.cool](https://papers.cool/arxiv/2611.22115)
- Authors: Xingchen AGI Lab, :, Baotian Hu, Bingkai Yang, Boyang Wang, Changzai Pan, et al. (140 authors)
- Published: 2026-11-17 02:58 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, policy optimization; reasoning: reasoning; planning_and_action: trajectory, rollout; memory_and_benchmarks: memory, evaluation
- Abstract skim: We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale...

### 42 - Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model

- arXiv: [2611.22998](https://arxiv.org/abs/2611.22998) | [PDF](https://arxiv.org/pdf/2611.22998) | [papers.cool](https://papers.cool/arxiv/2611.22998)
- Authors: Jiaqi Wu, Yongqi Dong, Yijie Zhong, Maple Shao, Yide Tao, Linsen Cai, et al. (9 authors)
- Published: 2026-11-17 16:12 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; planning_and_action: trajectory, world model; memory_and_benchmarks: evaluation; downranked: driving
- Abstract skim: In automated driving, world models provide future scene predictions for evaluating candidate trajectories, but fixed selection rules may not capture scene-dependent trade-offs. We propose a residual-guided reinforcement learning (RL) framework for lightweight trajectory selection with a frozen world model and a...

### 40 - RiDEx: Reward-Informed Directional Exploration for Diffusion Reinforcement Learning

- arXiv: [2611.22052](https://arxiv.org/abs/2611.22052) | [PDF](https://arxiv.org/pdf/2611.22052) | [papers.cool](https://papers.cool/arxiv/2611.22052)
- Authors: Song Yan, Chenfeng Wang, Wei Zhai, Xingchen Wang, Tao Zhang, Yawen Shao, et al. (9 authors)
- Published: 2026-11-17 01:27 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization
- Abstract skim: Reward-based diffusion post-training updates model parameters from task rewards. While existing approaches improve sampling and policy optimization, they still rely largely on isotropic random perturbations in a high-dimensional latent space for exploration. Such variation often spends the perturbation budget on...

### 39 - Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration

- arXiv: [2611.22275](https://arxiv.org/abs/2611.22275) | [PDF](https://arxiv.org/pdf/2611.22275) | [papers.cool](https://papers.cool/arxiv/2611.22275)
- Authors: Ting-Hsuan Chen, Siheng Zhao, Han Jiang, Qi Pan, Louison Lu, Jiaheng Luo, et al. (10 authors)
- Published: 2026-11-17 06:21 UTC | Categories: cs.LG, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-...

### 39 - WM-Quant: Rollout-Aware Post-Training Quantization for JEPA-Style World Models

- arXiv: [2611.21882](https://arxiv.org/abs/2611.21882) | [PDF](https://arxiv.org/pdf/2611.21882) | [papers.cool](https://papers.cool/arxiv/2611.21882)
- Authors: William Hammer, Andrew Heuer, Nikhil Krishna, Matthew Grenier, Ramtin Zand
- Published: 2026-11-16 20:51 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; planning_and_action: planning, rollout, world model
- Abstract skim: We present WM-Quant, to our knowledge, the first post-training quantization (PTQ) framework designed specifically for JEPA-style world models. Although world models typically feature relatively few parameters, action planning algorithms often require thousands of inferences, which can quickly become computationally...

### 37 - RLDE: A Reinforcement Learning Framework for Interpretable Iterative Document Editing

- arXiv: [2611.22039](https://arxiv.org/abs/2611.22039) | [PDF](https://arxiv.org/pdf/2611.22039) | [papers.cool](https://papers.cool/arxiv/2611.22039)
- Authors: Nikhil Parkar, M. Marimuthu, Riya Joshi, Karthikeyan N
- Published: 2026-11-17 01:00 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, ppo; reasoning: chain-of-thought, chain of thought
- Abstract skim: Improving the quality, clarity, and flow of long documents remains a challenging problem in NLP, as human editing typically occurs through iterative refinement rather than a single-pass rewrite. Most existing automated systems act as black-box generators or rely on supervised learning, limiting interpretability and...

### 36 - Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning

- arXiv: [2611.22067](https://arxiv.org/abs/2611.22067) | [PDF](https://arxiv.org/pdf/2611.22067) | [papers.cool](https://papers.cool/arxiv/2611.22067)
- Authors: Seongmin Kim, Woohyeon Byeon, Jiwon Jeon, Seungyul Han, Youngchul Sung
- Published: 2026-11-17 01:43 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Cooperative multi-agent reinforcement learning (MARL) often fails under exogenous variability such as shifts in opponents or environment regimes that cannot be controlled by the team but alter the transition dynamics. We formalize this challenge as Exogenous Dec-POMDP (ED-POMDP), in which an episode-level exogenous...

### 35 - EgoLink: Egocentric Language-Vision Interactive Network Knowledge Challenge Summary

- arXiv: [2611.21690](https://arxiv.org/abs/2611.21690) | [PDF](https://arxiv.org/pdf/2611.21690) | [papers.cool](https://papers.cool/arxiv/2611.21690)
- Authors: Renhe Sun, Yueying Feng, Bohan Yu, Tong Niu, Yunqi Liu, Zitong Wang, et al. (15 authors)
- Published: 2026-11-16 07:43 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: planning, acting, decision making; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: The EgoLink Challenge at ACM Multimedia 2026 benchmarks egocentric multimodal intelligence linking first-person perception, social reasoning, and interactive action. Unlike benchmarks centered on visible objects and activities, EgoLink evaluates whether models can interpret emotional and social cues, resolve...

### 34 - Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents

- arXiv: [2611.22245](https://arxiv.org/abs/2611.22245) | [PDF](https://arxiv.org/pdf/2611.22245) | [papers.cool](https://papers.cool/arxiv/2611.22245)
- Authors: Hejia Zhang, Zhongming Yu, Yimin Ding, Wei-Ting Chen, Hengjia Yu, Wentao Ni, et al. (12 authors)
- Published: 2026-11-17 05:47 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent, agent memory; memory_and_benchmarks: memory, benchmark
- Abstract skim: Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark and evidence-flow profiler for...

### 34 - What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super

- arXiv: [2611.22161](https://arxiv.org/abs/2611.22161) | [PDF](https://arxiv.org/pdf/2611.22161) | [papers.cool](https://papers.cool/arxiv/2611.22161)
- Authors: Sushant Mehta, Edwin Chen
- Published: 2026-11-17 03:48 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: acting
- Abstract skim: We post-train NVIDIA's Nemotron 3.5 Super (120B total, 12B active parameters) with reinforcement learning (RL) on five expert-built task datasets, one at a time: real-world software engineering, complex constraints, long-horizon tool use, professional chart understanding and enterprise document reasoning. Each run...

### 33 - Get Hint-Augmented GRPO Done Right Through Activation Steering

- arXiv: [2611.23124](https://arxiv.org/abs/2611.23124) | [PDF](https://arxiv.org/pdf/2611.23124) | [papers.cool](https://papers.cool/arxiv/2611.23124)
- Authors: Khiem Le, Ting Hua, Nitesh V. Chawla
- Published: 2026-11-17 17:43 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: GRPO has become the dominant reinforcement learning method for eliciting reasoning capability in LLMs using verifiable rewards. However, it suffers from a fundamental failure mode: when a training question exceeds the base model's current capability, all generated responses fail and receive zero reward, yielding no...

### 32 - Simplicity Goes Far: Auditing Prompt Optimizers with Demonstration-Conditioned Prompt Search

- arXiv: [2611.22605](https://arxiv.org/abs/2611.22605) | [PDF](https://arxiv.org/pdf/2611.22605) | [papers.cool](https://papers.cool/arxiv/2611.22605)
- Authors: Bohe Chen
- Published: 2026-11-17 11:22 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, ppo; reasoning: reasoning, reflection; planning_and_action: rollout
- Abstract skim: Automatic prompt optimization is growing more elaborate. Recent methods stack policy-gradient updates, trace reflection, and evolutionary search. These methods share a generate-and-select step; without controlling for it, reported gains may conflate the contributions of optimizer mechanisms and larger sampling...

### 32 - ReMaRL: Learning to Unmask and Remask in Frozen Diffusion Language Models

- arXiv: [2611.22576](https://arxiv.org/abs/2611.22576) | [PDF](https://arxiv.org/pdf/2611.22576) | [papers.cool](https://papers.cool/arxiv/2611.22576)
- Authors: Egor Shibaev, Danila Biktimirov, Ivan Klimov, Artem Makoian, Viacheslav Meshchaninov, Dmitry Vetrov
- Published: 2026-11-17 11:01 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: Masked diffusion language models generate tokens in parallel, and the order in which tokens are unmasked affects final-answer accuracy. Several methods learn unmasking policies from task rewards, but these policies cannot remask earlier predictions. Remasking lets the model correct those predictions using newly...

### 31 - RSI-Prime: Training Models to Train Models

- arXiv: [2611.23138](https://arxiv.org/abs/2611.23138) | [PDF](https://arxiv.org/pdf/2611.23138) | [papers.cool](https://papers.cool/arxiv/2611.23138)
- Authors: Dewu Zheng, Yang Ye, Hongyu Zhang, Jun Yu, Yanlin Wang
- Published: 2026-11-17 17:55 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement; memory_and_benchmarks: benchmark
- Abstract skim: Enabling large language models (LLMs) to autonomously conduct training and improve target models is an important foundation for recursive self-improvement (RSI). As LLMs expand their role from being trained to conducting training, their model-training capability warrants dedicated study and systematic development....

### 31 - Regularized Score Centering

- arXiv: [2611.21791](https://arxiv.org/abs/2611.21791) | [PDF](https://arxiv.org/pdf/2611.21791) | [papers.cool](https://papers.cool/arxiv/2611.21791)
- Authors: Hao Bai, Chenlu Ye, Xuanchang Zhang, Aviral Kumar, Tong Zhang
- Published: 2026-11-16 19:12 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Asynchronous reinforcement learning increases training throughput, but data from stale policies and numerical mismatch between training and inference can destabilize learning. To stabilize off-policy learning, score centering (SC) removes the effect of reward baselines on the expected update. Our gradient...

### 30 - CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training

- arXiv: [2611.22777](https://arxiv.org/abs/2611.22777) | [PDF](https://arxiv.org/pdf/2611.22777) | [papers.cool](https://papers.cool/arxiv/2611.22777)
- Authors: Zhengfeng Yu, Tian Lan, Zhijing Wu, Enbo Zhao, Xuannan Liu, Feihu Jiang, et al. (11 authors)
- Published: 2026-11-17 13:44 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use, agent training, long-horizon agent
- Abstract skim: Executable synthetic environments provide scalable training tasks and verifiable feedback for long-horizon agents. Existing environment synthesis methods primarily generate tasks within individual environments. However, these tasks do not adequately capture real-world interactions across services, where actions in...

### 30 - Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses

- arXiv: [2611.22299](https://arxiv.org/abs/2611.22299) | [PDF](https://arxiv.org/pdf/2611.22299) | [papers.cool](https://papers.cool/arxiv/2611.22299)
- Authors: Deep Shah, Nehal Kathrotia
- Published: 2026-11-17 06:55 UTC | Categories: cs.AI
- Why it matched: agentic_rl: autonomous agent, agent harness; reasoning: reflection; memory_and_benchmarks: memory, benchmark
- Abstract skim: Whether a foundation model succeeds as an autonomous agent depends as much on its runtime software as on its weights. This runtime, the agent harness, manages context and memory, steers multi-turn control, executes tool actions in sandboxes, and verifies work before stopping. Because models differ in how they use...

### 29 - EviDARL: Evidence-Centric Dual-Agent Reasoning via Alternating Reinforcement Learning for Multi-Table Question Answering

- arXiv: [2611.22310](https://arxiv.org/abs/2611.22310) | [PDF](https://arxiv.org/pdf/2611.22310) | [papers.cool](https://papers.cool/arxiv/2611.22310)
- Authors: Dunhan Li, Leilei Gan, Lirong Gao, Wenyan Fan, Yongwei Wang, Sheng Guo, et al. (7 authors)
- Published: 2026-11-17 07:07 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Despite advances in LLM-based table reasoning, most studies focus on single-table settings. Multi-table QA requires multi-hop reasoning over complex table relationships and evidence dispersed across long contexts, often without verifiable intermediate traces. To address these challenges, we introduce EviDA, an...

### 27 - DAQ: Decision-Aligned Post-Training Quantization for Spiking Transformers

- arXiv: [2611.22611](https://arxiv.org/abs/2611.22611) | [PDF](https://arxiv.org/pdf/2611.22611) | [papers.cool](https://papers.cool/arxiv/2611.22611)
- Authors: Jialin Chen, Xiaochen Zhao, Aili Wang
- Published: 2026-11-17 11:25 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; planning_and_action: trajectory
- Abstract skim: Spiking transformers combine attention-based representation learning with sparse spike communication, yet their weights and membrane variables still incur substantial storage and computation overhead. Post-training quantization (PTQ) offers a practical way to reduce these overheads, but preserving neuronal firing...

### 26 - Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving

- arXiv: [2611.22691](https://arxiv.org/abs/2611.22691) | [PDF](https://arxiv.org/pdf/2611.22691) | [papers.cool](https://papers.cool/arxiv/2611.22691)
- Authors: Jia Hu, Yang Chang, Panqu Wang, Zhijun Fu, Chang Liu, Changjian Yu, et al. (7 authors)
- Published: 2026-11-17 12:39 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: world model; memory_and_benchmarks: evaluation; downranked: driving, autonomous driving
- Abstract skim: World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationship between vehicle interactions and...

### 26 - Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate

- arXiv: [2611.22461](https://arxiv.org/abs/2611.22461) | [PDF](https://arxiv.org/pdf/2611.22461) | [papers.cool](https://papers.cool/arxiv/2611.22461)
- Authors: Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal, Nheng Vanchhay, Md Ariful Islam Mozumder, Hee-Cheol Kim
- Published: 2026-11-17 09:23 UTC | Categories: cs.CL, cs.MA
- Why it matched: agentic_rl: multi-agent, agent memory; memory_and_benchmarks: memory
- Abstract skim: Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so five mechanisms from the agent-memory...

### 26 - EvoDisco: Strategy Discovery for Evolving Agent Memory

- arXiv: [2611.22102](https://arxiv.org/abs/2611.22102) | [PDF](https://arxiv.org/pdf/2611.22102) | [papers.cool](https://papers.cool/arxiv/2611.22102)
- Authors: Mingyang Liu, Qingcan Kang, Shixiong Kai, Kaichao Liang, Xiaojin Fu, Tao Zhong, et al. (7 authors)
- Published: 2026-11-17 02:37 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; reasoning: reasoning; memory_and_benchmarks: memory, alfworld
- Abstract skim: Large language model agents accumulate experience in memory, and how that memory evolves during interaction is as important as what it stores. Recent methods update memory online, yet both the operators that transform memory and the rules that select them remain fixed by design. We propose EvoDisco, which formulates...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
