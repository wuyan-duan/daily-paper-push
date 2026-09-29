# RL / Post-Training / Agentic RL Reading Queue - 2026-09-29

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 1905. Minimum score: 8.

## Top Picks

### 82 - Coding Agent Memory Post-training: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via Reinforcement Learning

- arXiv: [2609.34422](https://arxiv.org/abs/2609.34422) | [PDF](https://arxiv.org/pdf/2609.34422) | [papers.cool](https://papers.cool/arxiv/2609.34422)
- Authors: Lirui Luo, Kelong Mao, Heming Xia, Rongqing Li, Xinwei Yang, Luyu Chen, et al. (13 authors)
- Published: 2026-09-28 06:40 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agentic rl, agent memory; rl_post_training: post-training, post training, reinforcement learning, ppo; memory_and_benchmarks: memory
- Abstract skim: Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. Recent work has begun to use reinforcement learning to make memory control part of the policy, often relying on predefined memory tools within domain-specific training environments of...

### 70 - Not All Rollouts Are Worth Learning: On Trajectory Valuation for Post-Training Reinforcement Learning

- arXiv: [2609.35072](https://arxiv.org/abs/2609.35072) | [PDF](https://arxiv.org/pdf/2609.35072) | [papers.cool](https://papers.cool/arxiv/2609.35072)
- Authors: Xuesong Jia, Ziao Yang, Zhanhe Huang, Hongfu Liu
- Published: 2026-09-28 12:57 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo, +2 more; planning_and_action: trajectory
- Abstract skim: We consider the problem of trajectory valuation in reinforcement learning: how to identify and mitigate detrimental trajectories during online training. Unlike classification, where data valuation relies on fixed training and validation sets, reinforcement learning involves dynamically generated trajectories without...

### 67 - Cross-Rollout Bellman Closure for Long-Horizon Agentic Reinforcement Learning

- arXiv: [2609.35082](https://arxiv.org/abs/2609.35082) | [PDF](https://arxiv.org/pdf/2609.35082) | [papers.cool](https://papers.cool/arxiv/2609.35082)
- Authors: Yangyang Ren, Haodong Zhu, Linlin Yang, Sheng Xu, Peichao Lai, Baochang Zhang
- Published: 2026-09-28 13:02 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, policy optimization, grpo; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Group-based reinforcement learning such as GRPO trains LLM agents by comparing rollouts sampled for each task, without a learned critic. In long-horizon settings, these rollouts revisit shared anchor states, offering cross-rollout evidence for step-level credit. Ideally, step-level credit should incorporate evidence...

### 58 - KV-streams for Efficient Compaction in Agentic Reinforcement Learning

- arXiv: [2609.35750](https://arxiv.org/abs/2609.35750) | [PDF](https://arxiv.org/pdf/2609.35750) | [papers.cool](https://papers.cool/arxiv/2609.35750)
- Authors: Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda, Roger Creus Castanyer, Siddarth Venkatraman, Abhay Puri, et al. (18 authors)
- Published: 2026-09-28 17:57 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: post-training, post training, reinforcement learning; memory_and_benchmarks: memory
- Abstract skim: Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping GPU memory constant for a given trace. Unfortunately, most compaction strategies rely on prefilling the LLM context...

### 57 - Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large Language Models via Trainable Vectors

- arXiv: [2609.34344](https://arxiv.org/abs/2609.34344) | [PDF](https://arxiv.org/pdf/2609.34344) | [papers.cool](https://papers.cool/arxiv/2609.34344)
- Authors: Yuchen Cai, Ding Cao, Qixiang Yin, Xin Xu, Kai Yang, Siye Wu, et al. (13 authors)
- Published: 2026-09-28 05:21 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL) has become a key paradigm for enhancing the reasoning of large language models, yet the high dimensionality of parameter updates makes its training dynamics hard to analyze. We study reinforcement learning with verifiable rewards (RLVR) and use vector steering to identify a low-...

### 57 - Understanding the Synergy between SFT, RLVR, and OPD in LLM Post-Training

- arXiv: [2609.31900](https://arxiv.org/abs/2609.31900) | [PDF](https://arxiv.org/pdf/2609.31900) | [papers.cool](https://papers.cool/arxiv/2609.31900)
- Authors: Emre Can Acikgoz, Yang Li, Zeyu Leo Liu, Srijan Bansal, Dilek Hakkani-Tür, Shafiq Joty, et al. (7 authors)
- Published: 2026-09-25 18:39 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Modern LLM post-training composes supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and on-policy distillation (OPD) into multi-stage pipelines, yet these stages are typically designed and evaluated in isolation. We show that this composition is consequential: a stage that improves...

### 53 - ASCT: Attentive Search over Counterfactual Trees for Credit Assignment in Agentic Reinforcement Learning

- arXiv: [2609.35215](https://arxiv.org/abs/2609.35215) | [PDF](https://arxiv.org/pdf/2609.35215) | [papers.cool](https://papers.cool/arxiv/2609.35215)
- Authors: Yang Li, Jinhan Yang, hai liu, Di Wan, Xiyu Chen, Zongsi Xu, et al. (11 authors)
- Published: 2026-09-28 14:04 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, ppo; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Terminal utility evaluates a complete agentic workflow, but learning requires credit for the decisions within it. We introduce Attentive Search over Counterfactual Trees (ASCT), a framework that turns training-time multi-step search into local action credit. At actor-visited states, an auxiliary tree evaluates...

### 53 - Improving LLM Collaboration via Multi-Agent Preference Learning

- arXiv: [2609.32827](https://arxiv.org/abs/2609.32827) | [PDF](https://arxiv.org/pdf/2609.32827) | [papers.cool](https://papers.cool/arxiv/2609.32827)
- Authors: Shuo Liu, Xinzichen Li, Tianle Chen, Christopher Amato
- Published: 2026-09-26 17:54 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent, tool use; rl_post_training: reinforcement learning, preference optimization, reward model; planning_and_action: planning
- Abstract skim: Several works have explored multi-agent reinforcement learning (MARL) in LLM collaboration. However, constructing reliable rewards is difficult in practice, as complete and accurate metrics are often unavailable and hard to aggregate. Preference learning provides an alternative by learning from comparative human or...

### 52 - GenMem: Generative Symbolic Memory for Self-Evolving Harness

- arXiv: [2609.34633](https://arxiv.org/abs/2609.34633) | [PDF](https://arxiv.org/pdf/2609.34633) | [papers.cool](https://papers.cool/arxiv/2609.34633)
- Authors: Xinke Jiang, Tao Feng, Weixuan Xu, Zhixin Zhang, Zhibang Yang, Wentao Zhang, et al. (10 authors)
- Published: 2026-09-28 08:50 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent, agent harness; rl_post_training: grpo; reasoning: reasoning; planning_and_action: decision making; memory_and_benchmarks: memory, long-term memory, alfworld
- Abstract skim: Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-horizon decision-making. Yet existing memory management approaches remain limited to discriminative retrieval and to address the sparse,...

### 51 - ARISE: Adapting to Evolving Capability Gaps in Agentic Reinforcement Learning

- arXiv: [2609.35532](https://arxiv.org/abs/2609.35532) | [PDF](https://arxiv.org/pdf/2609.35532) | [papers.cool](https://papers.cool/arxiv/2609.35532)
- Authors: Kun Feng, Yuchen Fang, Yiyang Tan, Shuqi Gu, Yongxiang Zhao, Yu Liu, et al. (9 authors)
- Published: 2026-09-28 16:14 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, long-horizon agent; rl_post_training: reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: As a long-horizon agent improves through experience, previously observed weaknesses may recede while new limitations emerge, continually changing what it still needs to learn. Yet the learning process often remains tied to a static view of these needs: fixed behavioral criteria and training priorities can become...

### 51 - PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learning

- arXiv: [2609.35158](https://arxiv.org/abs/2609.35158) | [PDF](https://arxiv.org/pdf/2609.35158) | [papers.cool](https://papers.cool/arxiv/2609.35158)
- Authors: Jiaan Zhu, Wei Gao, Youhui Bai, Zewen Jin, Ju Huang, Siran Yang, et al. (9 authors)
- Published: 2026-09-28 13:35 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Multi-turn rollout dominates the cost of agentic reinforcement learning (RL). Asynchronous execution and elastic GPU resources can accelerate this stage, but adding rollout replicas yields diminishing returns while training GPUs remain idle between updates. We observe that effective resource use also depends on the...

### 51 - Multi-Agent System Search via Active Substructure-aware Policy Optimization

- arXiv: [2609.32430](https://arxiv.org/abs/2609.32430) | [PDF](https://arxiv.org/pdf/2609.32430) | [papers.cool](https://papers.cool/arxiv/2609.32430)
- Authors: Beicheng Xu, Bowen Fan, Weitong Qian, Lingching Tung, Bin Cui
- Published: 2026-09-26 10:06 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: policy optimization; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: LLMs enable multi-agent systems (MAS) to tackle complex tasks, but manually designing agent roles, prompts, and communication structures requires substantial expertise and effort. This motivates learning policies that construct query-specific MAS from execution reward. Existing approaches typically train these...

### 50 - UniOPSD: Unifying Outcome and Hindsight Feedback for Agentic Reinforcement Learning

- arXiv: [2609.34810](https://arxiv.org/abs/2609.34810) | [PDF](https://arxiv.org/pdf/2609.34810) | [papers.cool](https://papers.cool/arxiv/2609.34810)
- Authors: Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai, Xiaofeng Han, Zelong Zheng, Haoyu Wu, et al. (11 authors)
- Published: 2026-09-28 10:13 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning has become an effective approach to training language model agents, but sparse and delayed outcome rewards provide limited guidance for credit assignment across long interaction sequences. Recent work on on-policy self-distillation (OPSD) offers complementary supervision by evaluating a...

### 50 - Federated Multi-Modal Human Activity Recognition using Multi-Agent Reinforcement Learning

- arXiv: [2609.33492](https://arxiv.org/abs/2609.33492) | [PDF](https://arxiv.org/pdf/2609.33492) | [papers.cool](https://papers.cool/arxiv/2609.33492)
- Authors: Debasmita Dey, Tanmay Sen, Himel Mallick
- Published: 2026-09-27 11:59 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Human Activity Recognition (HAR) from heterogeneous wearable sensors is fundamental to the Internet of Health Things (IoHT), supporting rehabilitation, elderly care, and smart healthcare. Existing multimodal fusion methods often assign fixed equal weights to sensor streams, overlooking differences in modality...

### 49 - Understanding and Exploiting Anisotropy in Post-Training

- arXiv: [2609.32792](https://arxiv.org/abs/2609.32792) | [PDF](https://arxiv.org/pdf/2609.32792) | [papers.cool](https://papers.cool/arxiv/2609.32792)
- Authors: Samyak Jha, Harshvardhan Saini, Yizhen Liao, Yiming Tang, Dianbo Liu
- Published: 2026-09-26 17:08 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: LLM post-training combines supervised fine-tuning (SFT), a mode-covering forward-KL objective, with reinforcement learning (RL), a mode-seeking reverse-KL objective. Frequency-weighted likelihood training leaves a well-known signature: \emph{anisotropy}, in which a few residual channels carry disproportionately...

### 49 - The Alignment Paradox: How Post-Training Amplifies Confident Hallucinations in Language Models

- arXiv: [2609.32617](https://arxiv.org/abs/2609.32617) | [PDF](https://arxiv.org/pdf/2609.32617) | [papers.cool](https://papers.cool/arxiv/2609.32617)
- Authors: Qingjia Huang, Yakai Li, Jianguo Wu, Qihang Zhou, Aimin Yu, Xiaoqi Jia, et al. (8 authors)
- Published: 2026-09-26 13:39 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, preference optimization, dpo; reasoning: reasoning
- Abstract skim: Large language models (LLMs) can produce factually incorrect answers with high confidence, undermining their reliability and limiting the effectiveness of uncertainty-based error detection. While prior research attributes confident hallucinations to factors such as missing knowledge in training data, reasoning...

### 48 - ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control

- arXiv: [2609.34374](https://arxiv.org/abs/2609.34374) | [PDF](https://arxiv.org/pdf/2609.34374) | [papers.cool](https://papers.cool/arxiv/2609.34374)
- Authors: Eric Frankel, Banghua Zhu, Sewoong Oh, Lillian J. Ratliff
- Published: 2026-09-28 05:47 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlhf, +2 more
- Abstract skim: Language model post-training is often bottlenecked by the need for human-collected preference data, which is expensive and difficult to scale. Reinforcement learning from AI feedback (RLAIF) style approaches that leverage pseudo labels offer an abundant alternative but introduce systematic biases that degrade...

### 48 - RMB: Reward Model Boosting Mitigates Reward Hacking

- arXiv: [2609.33221](https://arxiv.org/abs/2609.33221) | [PDF](https://arxiv.org/pdf/2609.33221) | [papers.cool](https://papers.cool/arxiv/2609.33221)
- Authors: Jiabin Fan, Dezhi Ye, Yongchang Hao, Lili Mou
- Published: 2026-09-27 05:03 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, policy optimization, +1 more
- Abstract skim: Reinforcement Learning from Human Feedback (RLHF) is a powerful technique for aligning large language models (LLMs) with human preference. However, it often suffers from the reward hacking issue, where policy optimization improves the proxy reward model while actually degrading performance with respect to the true...

### 47 - MaPP: A Unified Marginalized Posterior-Predictive Framework for Data-Efficient RLVR

- arXiv: [2609.34990](https://arxiv.org/abs/2609.34990) | [PDF](https://arxiv.org/pdf/2609.34990) | [papers.cool](https://papers.cool/arxiv/2609.34990)
- Authors: Yangyang Ren, Haodong Zhu, Sheng Xu, Yanjing Li, Nikolai Yu. Zolotykh, Wentao Zhang, et al. (7 authors)
- Published: 2026-09-28 12:01 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; planning_and_action: planning, rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models but incurs substantial costs from rollouts and policy updates. Online prompt selection improves efficiency by using per-prompt Bayesian posteriors to predict difficulty and prioritize informative...

### 47 - Teach to Learn: Hint Annealing for Self-improving LLM Reasoning

- arXiv: [2609.34975](https://arxiv.org/abs/2609.34975) | [PDF](https://arxiv.org/pdf/2609.34975) | [papers.cool](https://papers.cool/arxiv/2609.34975)
- Authors: Zile Wang, Zijian Li, Haodong Wang, Jian Liu, Qianli Liu, Lucas Muli, et al. (8 authors)
- Published: 2026-09-28 11:53 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: evaluation
- Abstract skim: Group Relative Policy Optimization (GRPO) improves language-model reasoning by comparing verified rewards among multiple solution rollouts for each query. However, difficult training queries can yield only incorrect rollouts, leaving GRPO with no reward contrast or learning signal. Prior hint-based methods construct...

### 47 - Just-In-Time Agent Memory with Runtime Agentic Research

- arXiv: [2609.34385](https://arxiv.org/abs/2609.34385) | [PDF](https://arxiv.org/pdf/2609.34385) | [papers.cool](https://papers.cool/arxiv/2609.34385)
- Authors: Bingyu Yan, Chaofan Li, Hongjin Qian, Shuqi Lu, Chaozhuo Li, Zheng Liu
- Published: 2026-09-28 06:01 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agent memory; rl_post_training: policy optimization, group relative policy optimization; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Memory is critical for AI agents. Many existing agent-memory systems follow an Ahead-of-Time (AOT) design, constructing memory before a specific request arrives. While this reduces online serving cost, such request-agnostic memory construction can discard fine-grained information that later becomes important. To...

### 46 - ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy Learning

- arXiv: [2609.35433](https://arxiv.org/abs/2609.35433) | [PDF](https://arxiv.org/pdf/2609.35433) | [papers.cool](https://papers.cool/arxiv/2609.35433)
- Authors: Yihang Chen, Yuanhao Ban, Cho-Jui Hsieh
- Published: 2026-09-28 15:38 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning from verifiable rewards (RLVR) frequently reuses rollouts across multiple policy updates, increasing the mismatch between the current policy and the data-generating policy. We identify a sign-dependent gradient starvation problem in clipped policy optimization: clipping suppresses under-...

### 46 - CRISP: Cultural Reward Modeling for Implicit Situated Propriety

- arXiv: [2609.34345](https://arxiv.org/abs/2609.34345) | [PDF](https://arxiv.org/pdf/2609.34345) | [papers.cool](https://papers.cool/arxiv/2609.34345)
- Authors: Zekun Yuan, Yangfan Ye, Baohang Li, Shuaibo Zhao, Zekun Zhou, Ziming Li, et al. (9 authors)
- Published: 2026-09-28 05:21 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; rl_post_training: policy optimization, reward model, grpo
- Abstract skim: As large language models (LLMs) are increasingly deployed across countries and regions, the ability to recognize and respond appropriately to diverse cultural contexts becomes increasingly important. However, existing research has largely focused on cultural knowledge or tasks with predefined response spaces, while...

### 46 - GlyphBench: A Playground for Language-Model Reinforcement Learning

- arXiv: [2609.34214](https://arxiv.org/abs/2609.34214) | [PDF](https://arxiv.org/pdf/2609.34214) | [papers.cool](https://papers.cool/arxiv/2609.34214)
- Authors: Roger Creus Castanyer, Marc-Alexandre Côté, Matthew James Sargent, Augustine N. Mavor-Parker, Glen Berseth, Pablo Samuel Castro
- Published: 2026-09-28 03:21 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: We introduce GlyphBench, an environment suite for reinforcement learning (RL) post-training of language-model agents, with over 360 tasks spanning diverse games. GlyphBench renders spatial observations as two-dimensional Unicode grids and connects training, evaluation, and trajectory replay through a unified...

### 46 - Counterfactual Rollout Replay: Forkable Environments as Free Process Rewards for Software Engineering Agents

- arXiv: [2609.33875](https://arxiv.org/abs/2609.33875) | [PDF](https://arxiv.org/pdf/2609.33875) | [papers.cool](https://papers.cool/arxiv/2609.33875)
- Authors: Yuanhao Li, Hongbo Wang, Xuhong Chen, Yiming Cao, Xunzhu Tang
- Published: 2026-09-27 19:50 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reward model, grpo; reasoning: process reward; planning_and_action: trajectory, rollout
- Abstract skim: Outcome-only reinforcement learning gives software engineering (SWE) agents a terminal success signal but little direct guidance about intermediate decisions. We introduce Counterfactual Rollout Replay (CRR), a training-time procedure that uses forkable executable environments to obtain step-level return contrasts....

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
