# RL / Post-Training / Agentic RL Reading Queue - 2026-08-16

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 339. Minimum score: 8.

## Top Picks

### 57 - Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning

- arXiv: [2608.13026](https://arxiv.org/abs/2608.13026) | [PDF](https://arxiv.org/pdf/2608.13026) | [papers.cool](https://papers.cool/arxiv/2608.13026)
- Authors: Yao Zhou, Hang Gao, Fengge Wu, Changwen Zheng, Wenwen Qiang
- Published: 2026-08-13 09:54 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; planning_and_action: trajectory, rollout
- Abstract skim: Outcome-driven reinforcement learning offers a scalable way to post-train vision-language-action (VLA) policies from sparse task-success feedback. In common GRPO-based VLA post-training, one rollout-level advantage is applied to every action in the trajectory. A rollout that completes several valid stages but fails...

### 56 - Intern-S2-Preview: Scientific Agentic Foundation Model

- arXiv: [2608.13505](https://arxiv.org/abs/2608.13505) | [PDF](https://arxiv.org/pdf/2608.13505) | [papers.cool](https://papers.cool/arxiv/2608.13505)
- Authors: Lei Bai, Jiaqi Cao, Chiyu Chen, Guanzhou Chen, Kai Chen, Guangran Cheng, et al. (125 authors)
- Published: 2026-08-13 17:31 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to...

### 54 - Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents

- arXiv: [2608.12764](https://arxiv.org/abs/2608.12764) | [PDF](https://arxiv.org/pdf/2608.12764) | [papers.cool](https://papers.cool/arxiv/2608.12764)
- Authors: Haoze Wu, Chuqiao Kuang, Tianyi Zhuang, Xiaoguang Li
- Published: 2026-08-13 03:13 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; reasoning: reasoning, outcome reward; planning_and_action: trajectory; memory_and_benchmarks: gaia
- Abstract skim: Deep search agents operate over trajectories spanning dozens of steps, yet standard reinforcement learning provides only a single outcome reward per trajectory, which is far too sparse for effective credit assignment. On-policy self-distillation (OPSD) addresses this by using the model's own logits as dense token-...

### 46 - Latent On-Policy Self-Distillation

- arXiv: [2608.13040](https://arxiv.org/abs/2608.13040) | [PDF](https://arxiv.org/pdf/2608.13040) | [papers.cool](https://papers.cool/arxiv/2608.13040)
- Authors: Guibin Zhang, Jiayang Lyu, Ran Sun, Xinlei Yu, Haoyu Zhao, Qibing Ren, et al. (7 authors)
- Published: 2026-08-13 10:05 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: rlvr, grpo; reasoning: self-improvement, self improvement; planning_and_action: rollout
- Abstract skim: Enabling agents to learn from experience and internalize it into their policy has become a central problem in self-evolving AI. On-policy self-distillation (OPSD) offers an effective pathway by using a privileged self-teacher to provide dense supervision on the student's own trajectories; however, existing methods...

### 44 - Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence

- arXiv: [2608.12743](https://arxiv.org/abs/2608.12743) | [PDF](https://arxiv.org/pdf/2608.12743) | [papers.cool](https://papers.cool/arxiv/2608.12743)
- Authors: Haokai Zhang, Yuhang Ding, Yunshu Zhou, Xinze Du, Shengtao Zhang, Zhiyue Zhao, et al. (8 authors)
- Published: 2026-08-13 02:42 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning, reflection; planning_and_action: planning; memory_and_benchmarks: memory
- Abstract skim: Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants. To improve the spatial reasoning ability of VLM agents, existing work has mainly followed two lines. One line uses post-training methods, such as supervised fine-tuning and reinforcement learning. Another...

### 41 - LongEarth-R1: Benchmarking and Aligning Vision-Language Models for Long-Horizon Earth Observation Reasoning

- arXiv: [2608.13344](https://arxiv.org/abs/2608.13344) | [PDF](https://arxiv.org/pdf/2608.13344) | [papers.cool](https://papers.cool/arxiv/2608.13344)
- Authors: Yupan Ding, Jing Xiao, Zhenyuan Zhang, Chaofeng Chen, Liang Liao, Gui-Song Xia, et al. (7 authors)
- Published: 2026-08-13 15:14 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark
- Abstract skim: Long-horizon Earth observation reasoning requires models to organize multi-stage geographic evolution, localize spatial changes, detect temporal anomalies, and infer future from extended image sequences. However, existing remote sensing vision-language models mainly focus on isolated images, image pairs, or short...

### 41 - Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents

- arXiv: [2608.13179](https://arxiv.org/abs/2608.13179) | [PDF](https://arxiv.org/pdf/2608.13179) | [papers.cool](https://papers.cool/arxiv/2608.13179)
- Authors: Zechuan Wang, Siyuan Lu, Hongxuan Zhang, Linjian Mo, Chenyi Zhuang, Leilei Gan
- Published: 2026-08-13 12:44 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, rlvr, policy optimization; planning_and_action: trajectory
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) offers a verifier-bounded performance ceiling for training multi-turn tool-use agents, yet its trajectory-level credit assignment conflates heterogeneous per-turn outcomes into a single reward signal. On-policy distillation provides dense per-token supervision...

### 36 - Entropy-Augmented Multi-Objective Policy Optimization in Multiagent Systems

- arXiv: [2608.12534](https://arxiv.org/abs/2608.12534) | [PDF](https://arxiv.org/pdf/2608.12534) | [papers.cool](https://papers.cool/arxiv/2608.12534)
- Authors: Jamie Santos, Ayhan Alp Aydeniz, Raghav Thakar, Kagan Tumer
- Published: 2026-08-12 19:07 UTC | Categories: cs.MA, cs.RO
- Why it matched: agentic_rl: autonomous agent; rl_post_training: policy optimization; memory_and_benchmarks: evaluation
- Abstract skim: Autonomous agent teams deployed in settings such as marine and extraterrestrial outposts must coordinate actions to achieve optimal outcomes across multiple competing objectives. Multi-objective evolutionary algorithms such as NSGA-II optimize for diversity in the objective space, but neglect diversity in the...

### 36 - Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach

- arXiv: [2608.12436](https://arxiv.org/abs/2608.12436) | [PDF](https://arxiv.org/pdf/2608.12436) | [papers.cool](https://papers.cool/arxiv/2608.12436)
- Authors: Jiaao Ma, Chuan Lin, Guangjie Han, Shengchao Zhu, Qian Zhu, Ying Liu, et al. (7 authors)
- Published: 2026-08-12 14:15 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Multi-AUV ad-hoc network-based target tracking requires networked autonomous underwater vehicles (AUVs) to cooperatively track maneuvering targets under constrained acoustic communication, dynamic topology, and uncertain ocean disturbances. Although multi-agent reinforcement learning (MARL) enables decentralized...

### 35 - FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving

- arXiv: [2608.13395](https://arxiv.org/abs/2608.13395) | [PDF](https://arxiv.org/pdf/2608.13395) | [papers.cool](https://papers.cool/arxiv/2608.13395)
- Authors: Hao Dou
- Published: 2026-08-13 15:53 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; planning_and_action: planning, trajectory, rollout; memory_and_benchmarks: evaluation; downranked: driving, autonomous driving
- Abstract skim: Reinforcement learning improves autonomous-driving vision-language-action (VLA) models by evaluating trajectories sampled from the current policy. Group relative policy optimization (GRPO) learns from reward differences within each rollout group. When all sampled trajectories are poor, this relative signal can rank...

### 35 - I-SDPO: Instance-Level Adaptive Self-Distillation Policy Optimization

- arXiv: [2608.12957](https://arxiv.org/abs/2608.12957) | [PDF](https://arxiv.org/pdf/2608.12957) | [papers.cool](https://papers.cool/arxiv/2608.12957)
- Authors: Yubo Zhang, Xinhong Ma, Zezhong Tan, Ziqiang Dong
- Published: 2026-08-13 08:37 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; planning_and_action: rollout
- Abstract skim: Group Relative Policy Optimization (GRPO) learns from reward differences within a rollout group, but receives no useful relative signal when every sampled response is incorrect. Privileged self-distillation can fill this gap with dense token supervision, yet applying it throughout training creates a different...

### 34 - DIVE: Unlocking Self-Improvement in Frozen Language Models Through Diversity-Driven Skill Evolution

- arXiv: [2608.12486](https://arxiv.org/abs/2608.12486) | [PDF](https://arxiv.org/pdf/2608.12486) | [papers.cool](https://papers.cool/arxiv/2608.12486)
- Authors: Siheng Xiong, Ali Payani, Oguzhan Gungordu, Faramarz Fekri
- Published: 2026-08-12 18:06 UTC | Categories: cs.CL
- Why it matched: rl_post_training: grpo; reasoning: reasoning, self-improvement, self improvement; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Large language models (LLMs) cannot retain post-deployment experience without parameter updates. We introduce DIVE, a diversity-driven framework that enables frozen LLMs to improve by evolving persistent natural-language skills from task experience and verifier feedback. These skills encode reusable reasoning...

### 33 - DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data

- arXiv: [2608.13517](https://arxiv.org/abs/2608.13517) | [PDF](https://arxiv.org/pdf/2608.13517) | [papers.cool](https://papers.cool/arxiv/2608.13517)
- Authors: Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina, Kenneth Enevoldsen, Lukas Galke Poech
- Published: 2026-08-13 17:37 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is...

### 33 - HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments

- arXiv: [2608.12860](https://arxiv.org/abs/2608.12860) | [PDF](https://arxiv.org/pdf/2608.12860) | [papers.cool](https://papers.cool/arxiv/2608.12860)
- Authors: Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, et al. (11 authors)
- Published: 2026-08-13 06:16 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Vision-Language Navigation (VLN) for humanoid robots poses challenges existing benchmarks fail to address: bipedal locomotion imposes physical constraints absent from wheeled agents, humanoid morphologies vary across platforms, and egocentric observations are distorted by locomotion-induced camera dynamics. We...

### 32 - MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination

- arXiv: [2608.13476](https://arxiv.org/abs/2608.13476) | [PDF](https://arxiv.org/pdf/2608.13476) | [papers.cool](https://papers.cool/arxiv/2608.13476)
- Authors: Saisha Shetty, Satvik Tripathi, Austin Lin, Colin Zhao, Theodore Kim, Don Enwerem, et al. (9 authors)
- Published: 2026-08-13 17:00 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: multi-agent, agent orchestration; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context...

### 32 - OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways

- arXiv: [2608.12995](https://arxiv.org/abs/2608.12995) | [PDF](https://arxiv.org/pdf/2608.12995) | [papers.cool](https://papers.cool/arxiv/2608.12995)
- Authors: Mao Jiayang, Wang Lanfeng, Peng Zhao-Han
- Published: 2026-08-13 09:19 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: traffic
- Abstract skim: Heterogeneous USV cooperative pursuit in constrained port waterways requires evader interception under navigation, traffic, and role constraints. This paper proposes OGR-MARL, an option-guided residual multi-agent reinforcement learning framework that is decoupled from a specific MARL algorithm. OGR-MARL integrates...

### 30 - TsuGO: Probing Search Efficiency in LLM Reasoning via Go Life-and-Death Problems

- arXiv: [2608.13221](https://arxiv.org/abs/2608.13221) | [PDF](https://arxiv.org/pdf/2608.13221) | [papers.cool](https://papers.cool/arxiv/2608.13221)
- Authors: Shunwen Bai, Ziping Ma, Chaoyang Zhang, Yarong Wang, Jiale Liu, Zhen Qin, et al. (7 authors)
- Published: 2026-08-13 13:24 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: The evaluation of LLM reasoning is moving from final-answer accuracy to process-level assessment, yet existing methods still fail to capture how models plan reasoning paths and allocate reasoning resources--that is, how they organize search. Prior process-level methods focus on the coherence and redundancy of chain-...

### 29 - TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval

- arXiv: [2608.13495](https://arxiv.org/abs/2608.13495) | [PDF](https://arxiv.org/pdf/2608.13495) | [papers.cool](https://papers.cool/arxiv/2608.13495)
- Authors: Yi-Chung Chen, Philip Jacobson, Tom Lampo, Yiren Lu, Jin Yao, David I. Inouye, et al. (9 authors)
- Published: 2026-08-13 17:24 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: benchmark; downranked: driving
- Abstract skim: Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly target driving events, but typically require expert-defined rules, auxiliary data, and multi-stage perception...

### 28 - RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory

- arXiv: [2608.13334](https://arxiv.org/abs/2608.13334) | [PDF](https://arxiv.org/pdf/2608.13334) | [papers.cool](https://papers.cool/arxiv/2608.13334)
- Authors: Jingbo Ji, Lingyi Li, Xilong Cheng, Yuhao Zhou, Wenji Zhang, Yuting Tan, et al. (7 authors)
- Published: 2026-08-13 15:05 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agent memory; reasoning: reasoning; memory_and_benchmarks: memory, episodic memory, long-term memory
- Abstract skim: LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction. However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions. Existing approaches struggle with...

### 28 - Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories

- arXiv: [2608.12847](https://arxiv.org/abs/2608.12847) | [PDF](https://arxiv.org/pdf/2608.12847) | [papers.cool](https://papers.cool/arxiv/2608.12847)
- Authors: Yifei Li, Heng Wang, Lingling Zhang, Muye Huang, Xinyu Zhang, Jiashuai Liu, et al. (8 authors)
- Published: 2026-08-13 05:39 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: long-horizon agent; planning_and_action: acting, trajectory; memory_and_benchmarks: memory, evaluation, webarena
- Abstract skim: Retrieval can identify a past trajectory that may matter, yet it does not specify how an acting agent should use that trajectory after users, entities, constraints, or environment state have changed. We identify this post-retrieval reuse step as a distinct bottleneck for long-horizon trajectory memory and formulate...

### 27 - ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification

- arXiv: [2608.12877](https://arxiv.org/abs/2608.12877) | [PDF](https://arxiv.org/pdf/2608.12877) | [papers.cool](https://papers.cool/arxiv/2608.12877)
- Authors: Runze Zhao, Zixin Tang, Xiaoshuai Hao, Leyuan Chang, Xiaopeng Fu, Boyu Qiao, et al. (7 authors)
- Published: 2026-08-13 06:41 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent collaboration; reasoning: reasoning, reflection; planning_and_action: planning
- Abstract skim: Multi-hop fact verification, which verifies claims by reasoning over multiple pieces of evidence, is critical for combating misinformation on social media yet remains highly challenging. Recent methods primarily rely on multi-agent collaboration to decompose fact verification into specialized subtasks. However,...

### 27 - Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces

- arXiv: [2608.12585](https://arxiv.org/abs/2608.12585) | [PDF](https://arxiv.org/pdf/2608.12585) | [papers.cool](https://papers.cool/arxiv/2608.12585)
- Authors: Congchao Wang, Diwakar Singh, Qiaozi Gao, Spyros Matsoukas, Yang Liu, Mahdi Namazifar
- Published: 2026-08-12 21:00 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, deliberation; memory_and_benchmarks: evaluation
- Abstract skim: Improving reasoning LLMs requires the ability to judge the quality of long reasoning traces for effective reasoning data curation, strong training signals during reinforcement learning, and an in-depth understanding of reasoning behaviors during model performance evaluation. Additionally, surfacing reasoning...

### 26 - MergeOver: Post-Training Token Merging for Recursive Vision Transformers

- arXiv: [2608.13141](https://arxiv.org/abs/2608.13141) | [PDF](https://arxiv.org/pdf/2608.13141) | [papers.cool](https://papers.cool/arxiv/2608.13141)
- Authors: Junseo Kim, Uraz Odyurt, Amirreza Yousefzadeh
- Published: 2026-08-13 12:15 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: memory
- Abstract skim: Vision Transformers (ViTs) demonstrate exceptional performance in computer vision but suffer from large parameter counts and quadratic computational complexity, severely limiting their deployment on resource-constrained edge hardware. While recursive weight-sharing reduces parameter counts and token merging...

### 26 - BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs

- arXiv: [2608.13046](https://arxiv.org/abs/2608.13046) | [PDF](https://arxiv.org/pdf/2608.13046) | [papers.cool](https://papers.cool/arxiv/2608.13046)
- Authors: Sanjeev Manivannan
- Published: 2026-08-13 10:11 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: deliberation; memory_and_benchmarks: evaluation
- Abstract skim: Organizational decisions are co-created while evidence, constraints, and human priorities continue to evolve. In conventional transcript-based multi-agent systems, humans typically provide an initial problem, agents deliberate internally, and the system returns a final response. BoardroomAI instead treats the human...

### 26 - Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games

- arXiv: [2608.12547](https://arxiv.org/abs/2608.12547) | [PDF](https://arxiv.org/pdf/2608.12547) | [papers.cool](https://papers.cool/arxiv/2608.12547)
- Authors: Deborah Sinishaw, Qile Zhu, Edwin Meriaux, Gregory Dudek
- Published: 2026-08-12 19:36 UTC | Categories: cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; reasoning: self-play; memory_and_benchmarks: benchmark
- Abstract skim: Large language model agents deployed without a central controller are often assumed to require communication to coordinate their actions. We ask what remains possible without it: when independent instances of the same model cannot communicate, can they still reason about their counterparts well enough to exceed the...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
