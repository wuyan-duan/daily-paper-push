# RL / Post-Training / Agentic RL Reading Queue - 2026-09-09

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 1038. Minimum score: 8.

## Top Picks

### 65 - NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness

- arXiv: [2609.08183](https://arxiv.org/abs/2609.08183) | [PDF](https://arxiv.org/pdf/2609.08183) | [papers.cool](https://papers.cool/arxiv/2609.08183)
- Authors: NeoHorse Team, Guoliang Cao, Guohao Dai, Tianyu Guo, Kai Han, Hailin Hu, et al. (37 authors)
- Published: 2026-09-08 03:14 UTC | Categories: cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training; reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: evaluation
- Abstract skim: Recursive self-improvement (RSI) requires a concrete mechanism through which an AI system observes its capabilities and converts that evidence into the next round of learning. We present NeoHorse-1, a family of agent-native models developed to explore this path through agentic post-training. Our system combines a...

### 56 - Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning Coverage in RLVR

- arXiv: [2609.08650](https://arxiv.org/abs/2609.08650) | [PDF](https://arxiv.org/pdf/2609.08650) | [papers.cool](https://papers.cool/arxiv/2609.08650)
- Authors: Youngjun Yu, Sanghwan Jang, Hwanjo Yu
- Published: 2026-09-08 12:21 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) has been central to the recent success of Large Reasoning Models. However, while RLVR significantly improves single-sample accuracy, it often fails to expand the model's intrinsic reasoning coverage (pass@k) due to limited exploration during training. To address...

### 56 - SRPO: Setwise Relative Policy Optimization for Multi-Agent LLMs

- arXiv: [2609.08452](https://arxiv.org/abs/2609.08452) | [PDF](https://arxiv.org/pdf/2609.08452) | [papers.cool](https://papers.cool/arxiv/2609.08452)
- Authors: Shengtian Yang, Ziyu Xiong, Yu Li, Yewen Li, Qingpeng Cai, Lei Feng
- Published: 2026-09-08 08:52 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Multi-agent large language models solve complex tasks by coordinating several policies in a shared environment. However, existing reinforcement learning methods usually optimize each response or trajectory separately, even when several outputs jointly cause one state transition. Consequently, the update unit differs...

### 55 - VERPO: Verified Evidence Regularized Policy Optimization

- arXiv: [2609.06100](https://arxiv.org/abs/2609.06100) | [PDF](https://arxiv.org/pdf/2609.06100) | [papers.cool](https://papers.cool/arxiv/2609.06100)
- Authors: Haijiang Li, Chengyu Lv, Yi Zhang, Zhibing Zhang, Rui Qian, Yuchen Zhang, et al. (11 authors)
- Published: 2026-09-05 13:52 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, policy optimization; reasoning: reasoning
- Abstract skim: Verifiable outcome rewards guide language-model post-training, but sequence-level advantages do not identify which token-level decisions should be preserved or revised. Evidence-conditioned Teachers provide denser supervision by replaying sampled trajectories with privileged feedback. Yet indiscriminate imitation...

### 54 - ThinkPrior: Zero-Rollout Difficulty Priors for Cold-Start Prompt Selection in RLVR

- arXiv: [2609.09075](https://arxiv.org/abs/2609.09075) | [PDF](https://arxiv.org/pdf/2609.09075) | [papers.cool](https://papers.cool/arxiv/2609.09075)
- Authors: Tommy Sha, Skylar Zhai, Siqi Zhao
- Published: 2026-09-08 17:30 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; planning_and_action: rollout
- Abstract skim: In reinforcement learning with verifiable rewards (RLVR) trained with group relative policy optimization (GRPO), the KL-free reward-advantage term studied here depends on within-group reward variation. If all rollouts in a group are correct or all are wrong, their group-relative advantages are identically zero;...

### 51 - Eliciting Self-Verification in Multimodal Reasoning Agents with Reinforcement Learning

- arXiv: [2609.08025](https://arxiv.org/abs/2609.08025) | [PDF](https://arxiv.org/pdf/2609.08025) | [papers.cool](https://papers.cool/arxiv/2609.08025)
- Authors: Vishwas Sathish, Viresh Ranjan, Xinliang Zhu, Arnab Dhua, Douglas Gray
- Published: 2026-09-07 22:15 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Reasoning agents increasingly rely on external tools such as web search to answer complex queries. Reinforcement learning (RL) finetuning algorithms such as GRPO have improved long-form reasoning in text-only language models, particularly for coding and mathematics. Reliable tool use in multimodal agents, however,...

### 50 - SMaRT-Tug: Structured Multi-Agent Reinforcement Learning for Physics-Based Tugboat-Barge Collaborative Manipulation

- arXiv: [2609.07445](https://arxiv.org/abs/2609.07445) | [PDF](https://arxiv.org/pdf/2609.07445) | [papers.cool](https://papers.cool/arxiv/2609.07445)
- Authors: Junkai Lu, Jiadong Zhao, Jiacheng Zhang, Wenqi Zhao, Hao Gen Chia, Qun Shen Png, et al. (11 authors)
- Published: 2026-09-07 12:51 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent, agent training; rl_post_training: reinforcement learning, ppo
- Abstract skim: Autonomous tugboating is central for automating maritime operations such as port logistics and vessel maneuvering, where multiple tugboats must cooperatively transport/manipulate a larger vessel. Collaborative pushing in this setting is challenging due to coupled hydrodynamics, low resistance, strong environmental...

### 49 - Miles v0.1: Production-Level Post-Training

- arXiv: [2609.08368](https://arxiv.org/abs/2609.08368) | [PDF](https://arxiv.org/pdf/2609.08368) | [papers.cool](https://papers.cool/arxiv/2609.08368)
- Authors: RadixArk, :, Tom Chen, Mao Cheng, Shi Dong, Kangrui Du, et al. (14 authors)
- Published: 2026-09-08 07:35 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: We present Miles v0.1, a full-stack, production-ready system for frontier post-training. Building upon the clean design of slime, Miles designs each stage of the reinforcement-learning (RL) training loop around a single principle: components should be verified, clean, and customizable. With accuracy, efficiency,...

### 49 - Inference-Time Graph Engineering for Multi-Agent LLM Workflows

- arXiv: [2609.05774](https://arxiv.org/abs/2609.05774) | [PDF](https://arxiv.org/pdf/2609.05774) | [papers.cool](https://papers.cool/arxiv/2609.05774)
- Authors: Katherine Tieu, Dongqi Fu, Yinglong Xia, Hong Li, Hong Yan, Jingrui He
- Published: 2026-09-04 23:32 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent orchestration; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: gaia
- Abstract skim: Recent multi-agent LLM systems increasingly rely on graph-structured communication to coordinate specialized agents. We revisit multi-agent orchestration from a graph-engineering perspective: rather than optimizing a static topology, we synthesize a task-conditioned temporal workflow graph that jointly specifies...

### 48 - Revisiting Complete Reasoning Traces for Post-Training

- arXiv: [2609.07103](https://arxiv.org/abs/2609.07103) | [PDF](https://arxiv.org/pdf/2609.07103) | [papers.cool](https://papers.cool/arxiv/2609.07103)
- Authors: Jaehui Hwang, Sangdoo Yun, Byeongho Heo, Dongyoon Han
- Published: 2026-09-07 06:46 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Large language models (LLMs) are often post-trained on pre-collected reasoning trajectories to improve their reasoning capability. Such trajectories tend to be long due to complex, interwoven paths, which often include detours on the path toward the answer. However, it has been underexplored whether LLMs indeed...

### 43 - Tracking the Moving Frontier: Long-Short Term Advantage Estimator

- arXiv: [2609.06671](https://arxiv.org/abs/2609.06671) | [PDF](https://arxiv.org/pdf/2609.06671) | [papers.cool](https://papers.cool/arxiv/2609.06671)
- Authors: Xinhao Yao, Lu Yu, Changhao Wang, Fengwei Teng, Yuyao Zhang, Qing Cui, et al. (8 authors)
- Published: 2026-09-06 15:24 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agent training, long-horizon agent; rl_post_training: rlvr; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Group-based RLVR methods estimate advantages by repeatedly sampling multiple trajectories for each prompt, making long-horizon agent training expensive and discarding useful experience accumulated across iterations. We ask whether historical experience can replace these repeated within-iteration comparisons without...

### 42 - Flow3D-OPD: Multi-Teacher On-Policy Distillation for 3D Geometry Generation with Flow-Matching Diffusion Transformer

- arXiv: [2609.07137](https://arxiv.org/abs/2609.07137) | [PDF](https://arxiv.org/pdf/2609.07137) | [papers.cool](https://papers.cool/arxiv/2609.07137)
- Authors: Zhiwei Ning, Zhen Zhou, Puhua Jiang, Xintong Han, Gengming Zhang, Jie Yang, et al. (10 authors)
- Published: 2026-09-07 07:36 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, preference optimization, +1 more; memory_and_benchmarks: evaluation
- Abstract skim: Recent image-to-3D generation models built on flow-matching diffusion Transformers (DiT) can produce high-fidelity meshes, yet their post-training strategy remains largely unexplored. There exist several critical bottlenecks in reinforcement learning: the inherent difficulty of defining comprehensive rewards for 3D...

### 42 - Generating Adversarial Texts for Machine Translation via GRPO

- arXiv: [2609.06048](https://arxiv.org/abs/2609.06048) | [PDF](https://arxiv.org/pdf/2609.06048) | [papers.cool](https://papers.cool/arxiv/2609.06048)
- Authors: Florian Zogaj, Jakob Hütteneder, Giovanni De Muri, Federico Villa, Aryan Sood, Vilém Zouhar
- Published: 2026-09-05 12:06 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; memory_and_benchmarks: evaluation
- Abstract skim: As machine translation (MT) systems continue to improve, standard benchmarks become less informative for exposing remaining weaknesses. Traditional methods for creating challenging test sets rely on expensive manual creation or curation, while automated approaches struggle to produce sets with the necessary...

### 41 - DataFlex-RL: An Evaluation Platform for RLVR Data Policies

- arXiv: [2609.06107](https://arxiv.org/abs/2609.06107) | [PDF](https://arxiv.org/pdf/2609.06107) | [papers.cool](https://papers.cool/arxiv/2609.06107)
- Authors: Hao Liang, Mingrui Chen, Hengyi Feng, Meiyi Qiang, Wentao Zhang
- Published: 2026-09-05 14:04 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; planning_and_action: rollout; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Data policies for reinforcement learning with verifiable rewards (RLVR) determine which rollouts are used, how strongly they are weighted, and which domains contribute to subsequent training batches. We introduce DataFlex-RL, an evaluation platform for comparing these choices under a common GRPO recipe. Our primary...

### 41 - UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms

- arXiv: [2609.05910](https://arxiv.org/abs/2609.05910) | [PDF](https://arxiv.org/pdf/2609.05910) | [papers.cool](https://papers.cool/arxiv/2609.05910)
- Authors: Peng Lai, Yichao Du, Junchao Wu, Weibo Gao, Linan Yue, Longyue Wang, et al. (9 authors)
- Published: 2026-09-05 06:05 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, reward model; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) excels on tasks with verifiable rewards, but in open-ended tasks, the reliability of reward models remains a key challenge. Existing solutions either depend on costly proprietary LLM-as-a-Judge systems or opaque scalar reward models that lack interpretability. Recent works on generative...

### 40 - CircuitLens: Reasoning Circuits as Data Selection Signals for Reinforcement Learning with Verifiable Rewards

- arXiv: [2609.07183](https://arxiv.org/abs/2609.07183) | [PDF](https://arxiv.org/pdf/2609.07183) | [papers.cool](https://papers.cool/arxiv/2609.07183)
- Authors: Zhuofan Chen, Ziqian Jiao, Yikai Cui, Zhixin Cai, Jun Bai, Wenge Rong
- Published: 2026-09-07 08:14 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) is sensitive to which problems a model trains on, yet existing selection criteria--difficulty filtering, hand-curation, reward-trajectory scoring--assess data value as an intrinsic property of problems, independent of the model that will learn from them. We...

### 40 - EnvCraft: Synthesizing Executable Environments in Agentic RL for Claw-like Agent

- arXiv: [2609.05576](https://arxiv.org/abs/2609.05576) | [PDF](https://arxiv.org/pdf/2609.05576) | [papers.cool](https://papers.cool/arxiv/2609.05576)
- Authors: Yirong Zeng, Shen You, Jinhang Feng, Yufei Liu, Xiao Ding, Yutai Hou, et al. (11 authors)
- Published: 2026-09-04 10:13 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl, tool use; rl_post_training: reinforcement learning
- Abstract skim: The paradigm of LLMs has rapidly shifted from passive language interfaces to autonomous Claw-like agents that execute long-horizon tasks across stateful workspaces. While Agentic Reinforcement Learning (Agentic RL) provides a promising path to optimize these agents, its scaling is heavily bottlenecked by the severe...

### 39 - Elastic Horizon: Discovering the Effective Interaction Frontier in Agentic Reinforcement Learning

- arXiv: [2609.07247](https://arxiv.org/abs/2609.07247) | [PDF](https://arxiv.org/pdf/2609.07247) | [papers.cool](https://papers.cool/arxiv/2609.07247)
- Authors: Gangyi Zhang, Junjie Meng, Letian Zhang, Wei Wu, Yang Zheng, Dong Wang, et al. (9 authors)
- Published: 2026-09-07 09:09 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: trajectory
- Abstract skim: Scaling the interaction horizon-the maximum number of environment interactions per episode-improves LLM agents on long-horizon tasks, and curriculum-based methods that progressively expand the horizon outperform fixed-horizon alternatives. However, existing schedules are open-loop: they monotonically increase the...

### 37 - Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training

- arXiv: [2609.07108](https://arxiv.org/abs/2609.07108) | [PDF](https://arxiv.org/pdf/2609.07108) | [papers.cool](https://papers.cool/arxiv/2609.07108)
- Authors: Zili Wang, Zhaopeng Qiu, Yuekai Zhang, Shuang Yu, Junjie Lai
- Published: 2026-09-07 06:48 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Speculative decoding accelerates rollout generation, which dominates the cost of reinforcement learning (RL) post-training. Online co-training can further increase the draft's accuracy, yielding greater speedups. However, scaling this approach to co-training on large models with long contexts poses two obstacles:...

### 36 - Graph-Based Safe Reinforcement Learning for Multi-Agent Systems with Time-Varying Topology

- arXiv: [2609.08802](https://arxiv.org/abs/2609.08802) | [PDF](https://arxiv.org/pdf/2609.08802) | [papers.cool](https://papers.cool/arxiv/2609.08802)
- Authors: Xiao Sizhe, Dong Lijing, Bai Rui, Tan Xin
- Published: 2026-09-08 14:30 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: This paper presents a graph-based safe multi-agent reinforcement learning (MARL) framework for cooperative navigation with time-varying topology. To address the critical challenge of ensuring safety in environments with sensing constraints, a safety-decoupled mechanism is introduced through a Control Barrier-Like...

### 36 - Decentralized Safe Multi-Agent Reinforcement Learning via Predictive Shielding

- arXiv: [2609.07618](https://arxiv.org/abs/2609.07618) | [PDF](https://arxiv.org/pdf/2609.07618) | [papers.cool](https://papers.cool/arxiv/2609.07618)
- Authors: Yacine El Yamani, Hanna Krasowski, Elena Vanneaux
- Published: 2026-09-07 15:22 UTC | Categories: cs.AI, cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Environments are increasingly populated by multiple robots performing independent tasks with limited prior knowledge of each other. Deploying such multi-agent systems presents significant challenges. Specifically, shifts in deployment states compared to training data can lead to poor policy performance and...

### 34 - MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games

- arXiv: [2609.06563](https://arxiv.org/abs/2609.06563) | [PDF](https://arxiv.org/pdf/2609.06563) | [papers.cool](https://papers.cool/arxiv/2609.06563)
- Authors: Hwang Yechan, Bae Sangjun, Kim Jeongmo, Bang Sangwoo, Han Seungyul
- Published: 2026-09-06 12:18 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: llm agent, multi-agent; rl_post_training: preference optimization
- Abstract skim: Social deduction games (SDGs) require agents to reason under partial observability by maintaining relational beliefs about hidden roles and team alignments. While recent LLM-agent approaches improve gameplay through prompting and preference optimization, they often optimize actions and in-game speech without...

### 33 - CantoneseLLM v2: Reasoning in a Low-Resource Language

- arXiv: [2609.06970](https://arxiv.org/abs/2609.06970) | [PDF](https://arxiv.org/pdf/2609.06970) | [papers.cool](https://papers.cool/arxiv/2609.06970)
- Authors: Tsz Chung Cheng, Chung Shing Cheng, Chaak Ming Lau, Cheuk Hei Chong
- Published: 2026-09-07 03:08 UTC | Categories: cs.CL
- Why it matched: rl_post_training: rlvr, dpo; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Cantonese is widely spoken but remains low-resource in written data, with no large corpus of native Cantonese reasoning traces available for model training. We develop and release CantoneseLLM v2, comprising models based on Qwen3 8B and 30B-A3B. The models are trained through CPT on 784 million Cantonese and Hong...

### 33 - One Step, One Lead: Mitigating Higher-Order Interference in Multi-Domain Reinforcement Learning via Cross-Step Control

- arXiv: [2609.06469](https://arxiv.org/abs/2609.06469) | [PDF](https://arxiv.org/pdf/2609.06469) | [papers.cool](https://papers.cool/arxiv/2609.06469)
- Authors: Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Guojun Yin, Wei Lin, et al. (7 authors)
- Published: 2026-09-06 08:32 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL) across multiple domains can broaden the reasoning capabilities of large language models (LLMs), yet joint training often degrades individual-domain performance and can destabilize optimization. Existing work typically diagnoses such interference from a single-step view using first-order...

### 33 - Local and Global Stability in Performative Reinforcement Learning

- arXiv: [2609.06467](https://arxiv.org/abs/2609.06467) | [PDF](https://arxiv.org/pdf/2609.06467) | [papers.cool](https://papers.cool/arxiv/2609.06467)
- Authors: Debmalya Mandal
- Published: 2026-09-06 08:29 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: trajectory
- Abstract skim: In performative reinforcement learning the deployed policy shapes the environment that generates the learner's future data, and the natural solution concept is a performatively stable policy that is optimal in the environment it induces. Existing convergence guarantees rely on Lipschitz sensitivity assumptions on...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
