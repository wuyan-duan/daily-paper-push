# RL / Post-Training / Agentic RL Reading Queue - 2026-10-14

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 1762. Minimum score: 8.

## Top Picks

### 83 - RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution

- arXiv: [2610.15772](https://arxiv.org/abs/2610.15772) | [PDF](https://arxiv.org/pdf/2610.15772) | [papers.cool](https://papers.cool/arxiv/2610.15772)
- Authors: Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Xiao Luo, et al. (10 authors)
- Published: 2026-10-11 16:54 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning, rlvr, policy optimization, grpo; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Recent focus in agentic reinforcement learning (RL) seeks to improve credit assignment in long-horizon tasks. One promising direction combines reinforcement learning with verifiable rewards (RLVR) and on-policy self-distillation (OPSD), integrating trajectory-level advantages with dense token-level supervision. This...

### 66 - Double-Rollout Reinforcement Learning with Sampling-based Reward Estimation

- arXiv: [2610.16593](https://arxiv.org/abs/2610.16593) | [PDF](https://arxiv.org/pdf/2610.16593) | [papers.cool](https://papers.cool/arxiv/2610.16593)
- Authors: Haifeng Qian, David Mosallanezhad, Christian Munley, Adithya Renduchintala, Oleksii Kuchaiev
- Published: 2026-10-12 11:16 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) implemented with Group Relative Policy Optimization (GRPO) has driven substantial progress in training reasoning language models. However, verifiable outcome rewards provide an imperfect measure of reasoning quality: a correct final answer may not be supported by...

### 65 - A Production-Grade, High-Efficiency Agentic RL Framework for Frontier LLMs with Validated Recipes

- arXiv: [2610.16352](https://arxiv.org/abs/2610.16352) | [PDF](https://arxiv.org/pdf/2610.16352) | [papers.cool](https://papers.cool/arxiv/2610.16352)
- Authors: LoonSage Team, Bowei Song, Caiwei Zhao, Chuwen Liu, Dechuang Gu, Dong Fang, et al. (48 authors)
- Published: 2026-10-12 08:08 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: trajectory, decision making; memory_and_benchmarks: memory
- Abstract skim: Reinforcement learning (RL) has emerged as a critical phase in the post-training pipeline of large language models (LLMs). As the frontier of LLM capabilities shifts from static reasoning to agentic tasks--characterized by external tool invocation, multi-turn interactions, and long-horizon decision-making--existing...

### 61 - Agent-Reflex: Teaching Language Agents to Act Reflectively

- arXiv: [2610.17953](https://arxiv.org/abs/2610.17953) | [PDF](https://arxiv.org/pdf/2610.17953) | [papers.cool](https://papers.cool/arxiv/2610.17953)
- Authors: Guanting Dong, Xinyu Yang, Jiajie Jin, Yuyang Hu, Xiaoshuai Song, Yifei Chen, et al. (12 authors)
- Published: 2026-10-13 08:36 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning, tool use, agent training; rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning, reflection; memory_and_benchmarks: benchmark
- Abstract skim: Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision for reflection learning and failure...

### 58 - TSRL: Trigger-based Supervised Reinforcement Learning for Continual Agent Training

- arXiv: [2610.17726](https://arxiv.org/abs/2610.17726) | [PDF](https://arxiv.org/pdf/2610.17726) | [papers.cool](https://papers.cool/arxiv/2610.17726)
- Authors: Yuqian Fu, Kaiwen Jiang, Zijun Song, Jiawei Wang, Yuanheng Zhu, Dongbin Zhao
- Published: 2026-10-13 05:02 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agent training; rl_post_training: post-training, post training, reinforcement learning; memory_and_benchmarks: alfworld
- Abstract skim: Large language model (LLM) agents excel at complex, multi-step tasks but suffer from catastrophic forgetting during continual learning--acquiring new skills often degrades previously mastered capabilities. Existing post-training paradigms face a fundamental trade-off: Supervised Fine-Tuning (SFT) is sample-efficient...

### 57 - Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards

- arXiv: [2610.17893](https://arxiv.org/abs/2610.17893) | [PDF](https://arxiv.org/pdf/2610.17893) | [papers.cool](https://papers.cool/arxiv/2610.17893)
- Authors: Keru Chen, Sen Lin, Yingbin Liang, Nathaniel D. Bastian, Shaofeng Zou
- Published: 2026-10-13 07:46 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: multi-agent, agent collaboration; rl_post_training: post-training, post training; reasoning: self-play
- Abstract skim: Effective collaboration among large language model (LLM) agents in multi-agent systems requires sharing relevant evidence, requesting missing information, and incorporating teammates' contributions into decisions. Training these behaviors is challenging because final task outcomes provide limited feedback on the...

### 55 - SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection

- arXiv: [2610.18807](https://arxiv.org/abs/2610.18807) | [PDF](https://arxiv.org/pdf/2610.18807) | [papers.cool](https://papers.cool/arxiv/2610.18807)
- Authors: Wenlin Zhong, Hao Wang, Kun Yuan, Fan Yang, Jinluan Yang, Dian Jin, et al. (9 authors)
- Published: 2026-10-13 17:46 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: evaluation, alfworld, scienceworld
- Abstract skim: Agentic reinforcement learning (RL) enables large language models (LLMs) to learn from multi-turn interactions with verifiable outcomes. Textual skills can improve exploration by distilling prior interactions into reusable guidance. However, existing skill-based RL approaches often either assume skill injection is...

### 53 - ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning

- arXiv: [2610.18683](https://arxiv.org/abs/2610.18683) | [PDF](https://arxiv.org/pdf/2610.18683) | [papers.cool](https://papers.cool/arxiv/2610.18683)
- Authors: Bowen Ding, Mingda Wan, Yuhan Chen, Jiyao Yuan, Qi Zhu, Futing Wang, et al. (10 authors)
- Published: 2026-10-13 16:39 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning (RL) has emerged as the primary paradigm for optimizing Large Language Model (LLM) agents, yet efficient critic-free algorithms (e.g., GRPO) suffer from a fundamental uniform credit assignment dilemma that broadcasts trajectory-level advantages equally to all actions. Our analysis reveals that...

### 53 - SPROUT: Scaling Agentic Reinforcement Learning for Long-Horizon Software Engineering

- arXiv: [2610.14405](https://arxiv.org/abs/2610.14405) | [PDF](https://arxiv.org/pdf/2610.14405) | [papers.cool](https://papers.cool/arxiv/2610.14405)
- Authors: Mengyang Liu, Weiming Wang, Haixin Nan, Yu Wu, Peize Li, Shihong Huang, et al. (9 authors)
- Published: 2026-10-09 23:58 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning, grpo; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) has driven substantial progress in coding agents by relying on verified successful trajectories as learning signals. However, such trajectories are scarce in long-horizon software engineering tasks, where a minor error can invalidate the entire rollout. Repeatedly restarting from the...

### 52 - Adaptive-Group Process Rewards for GUI Agents

- arXiv: [2610.17710](https://arxiv.org/abs/2610.17710) | [PDF](https://arxiv.org/pdf/2610.17710) | [papers.cool](https://papers.cool/arxiv/2610.17710)
- Authors: Zirui Shang, Yang Liu, Xin Shu, Zhi Gao, Xinxiao Wu, Lifeng Fan
- Published: 2026-10-13 04:37 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning, grpo; reasoning: process reward; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Training graphical user interface (GUI) agents with reinforcement learning suffers from sparse outcome rewards, leading to inefficient learning. Process rewards offer a promising direction for credit assignment to intermediate actions; however, accurately evaluating an action requires identifying evidence across...

### 52 - ClawLoop: Self-Improving Agents via Harness-Native Training Loop

- arXiv: [2610.14118](https://arxiv.org/abs/2610.14118) | [PDF](https://arxiv.org/pdf/2610.14118) | [papers.cool](https://papers.cool/arxiv/2610.14118)
- Authors: Hansi Yang, Linji Hao, Hongyan Hao, An Wang, Han Wu, Qi Gu, et al. (7 authors)
- Published: 2026-10-09 08:52 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training; reasoning: self-improvement, self improvement; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: The rapid advancement of Large Language Models (LLMs) has driven their deployment toward general-purpose harness environments, where LLM-based agents operate in sandbox workspaces and interact directly with file systems and shells. While numerous post-training pipelines exist for tool-use agents, their counterparts...

### 51 - A Sovereign, Indic-First, Reasoning Model

- arXiv: [2610.15371](https://arxiv.org/abs/2610.15371) | [PDF](https://arxiv.org/pdf/2610.15371) | [papers.cool](https://papers.cool/arxiv/2610.15371)
- Authors: Sutanshu Saksena Raj, Prasanjith Pasunuti, Parijat Chatterjee, Daksh Maan, Purusharth Malik, Nayanjit Sarkar, et al. (7 authors)
- Published: 2026-10-11 05:52 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Gnani-Evon-v3.3-30B-A3B is a long-context hybrid Mamba-Transformer mixture-of-experts model for reasoning, instruction following, and tool use in English and eight Indian languages. Starting from NVIDIA's Nemotron-3-Nano-30B-A3B checkpoint, it retains the 52-layer backbone and changes the vocabulary, training data,...

### 50 - Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents

- arXiv: [2610.18614](https://arxiv.org/abs/2610.18614) | [PDF](https://arxiv.org/pdf/2610.18614) | [papers.cool](https://papers.cool/arxiv/2610.18614)
- Authors: Ashutosh Hathidara
- Published: 2026-10-13 16:00 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: llm agent; rl_post_training: reinforcement learning, grpo; planning_and_action: acting, rollout; memory_and_benchmarks: evaluation, alfworld
- Abstract skim: Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own self-reported verbalized confidence...

### 49 - APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation

- arXiv: [2610.18097](https://arxiv.org/abs/2610.18097) | [PDF](https://arxiv.org/pdf/2610.18097) | [papers.cool](https://papers.cool/arxiv/2610.18097)
- Authors: Sirui Zhang, Fangyun Wei, Dong Chen, Jinjing Zhao, Yitong Wang, Yunuo Chen, et al. (8 authors)
- Published: 2026-10-13 10:14 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: self-improvement, self improvement; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model according to its evolving capability...

### 49 - EventLens: Event-Structure Reinforcement Learning for Video Understanding

- arXiv: [2610.16172](https://arxiv.org/abs/2610.16172) | [PDF](https://arxiv.org/pdf/2610.16172) | [papers.cool](https://papers.cool/arxiv/2610.16172)
- Authors: Guowen Zhang, Boshen Xu, Zihao Yue, Ziheng Wang, Xiaokun Liu, Xin Tao, et al. (9 authors)
- Published: 2026-10-12 04:46 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Recent multimodal large language models (MLLMs) achieve strong results on video question answering, yet often fail to recover the temporal structure that makes a video coherent. They may merge neighboring events, miss single-event progression, or infer implausible relations across events. We study structured...

### 49 - Bridging Risk Approximation Gaps in Model Predictive Task Sampling via In-Context Modeling

- arXiv: [2610.14913](https://arxiv.org/abs/2610.14913) | [PDF](https://arxiv.org/pdf/2610.14913) | [papers.cool](https://papers.cool/arxiv/2610.14913)
- Authors: Jiarong Wen, Qi Tao, Kaiyu Zhang, Yun Qu, Lizhou Cai, Heming Zou, et al. (8 authors)
- Published: 2026-10-10 13:35 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agent environment; rl_post_training: post-training, post training, reinforcement learning, policy optimization; planning_and_action: decision making
- Abstract skim: Reinforcement learning (RL) is essential for adaptive decision-making, e.g., robust Meta-RL and domain randomization (DR), and efficient post-training of large language models (LLMs), where tasks are commonly structured as Markov decision processes or prompts. A central bottleneck in all these settings is the cost...

### 49 - Target-ESS Tempered Policy Optimization (TETPO): Smooth Variance Control via Bridge Importance Sampling

- arXiv: [2610.14440](https://arxiv.org/abs/2610.14440) | [PDF](https://arxiv.org/pdf/2610.14440) | [papers.cool](https://papers.cool/arxiv/2610.14440)
- Authors: Shayan Mohajer Hamidi, Kayhan Behdin, Wenhui Zhu, Aida Rahmattalabi, Jincheng Cao, Jelena Markovic-Voronov, et al. (7 authors)
- Published: 2026-10-10 01:15 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: Asynchronous reinforcement-learning post-training of large language models is computationally efficient but inherently off-policy: the learner updates on rollouts generated by a stale policy, while correcting this mismatch requires importance weights that can be extremely heavy-tailed. A small number of trajectories...

### 48 - WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution

- arXiv: [2610.18067](https://arxiv.org/abs/2610.18067) | [PDF](https://arxiv.org/pdf/2610.18067) | [papers.cool](https://papers.cool/arxiv/2610.18067)
- Authors: Hang He, Linting Wang, Guanming Liu, Bo Mao, Jinxiu Liu, Yiran Suo, et al. (17 authors)
- Published: 2026-10-13 09:52 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory, rollout; memory_and_benchmarks: evaluation
- Abstract skim: Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and verifier. However, existing...

### 48 - TPPO: Tracking-Value PPO For Language Model Reasoning

- arXiv: [2610.16794](https://arxiv.org/abs/2610.16794) | [PDF](https://arxiv.org/pdf/2610.16794) | [papers.cool](https://papers.cool/arxiv/2610.16794)
- Authors: Futing Wang, Chenxi Li, Jianhao Yan, Yun Luo, Zhi Wang, Yizhuo Li, et al. (9 authors)
- Published: 2026-10-12 13:47 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Proximal Policy Optimization (PPO) is widely used in reinforcement learning with verifiable rewards for language-model reasoning. While \emph{value evolution along trajectory} characterizes relative token-level credit, yet standard critics often fail to track it under sparse terminal rewards. To model this...

### 48 - Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcement Learning

- arXiv: [2610.16592](https://arxiv.org/abs/2610.16592) | [PDF](https://arxiv.org/pdf/2610.16592) | [papers.cool](https://papers.cool/arxiv/2610.16592)
- Authors: Chiheng Lou, Xiangwei Deng, Bangjun Xiao, Xiaodong Ji, Yikai Zhao, Xin Jin, et al. (7 authors)
- Published: 2026-10-12 11:16 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; planning_and_action: trajectory, rollout
- Abstract skim: Agentic reinforcement learning (RL) is commonly used to enhance the capabilities of large language models (LLMs) in solving complex multi-turn tasks. During rollout, agentic RL exhibits a workload pattern distinct from that of traditional RL: multi-turn interactions repeatedly introduce prefill requests, causing...

### 48 - ObsSpec: Accelerating Agentic Reinforcement Learning with Observation Speculation

- arXiv: [2610.15246](https://arxiv.org/abs/2610.15246) | [PDF](https://arxiv.org/pdf/2610.15246) | [papers.cool](https://papers.cool/arxiv/2610.15246)
- Authors: Kyle Montgomery, Wang Zhang, Chenguang Wang
- Published: 2026-10-11 00:40 UTC | Categories: cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning; planning_and_action: rollout, world model
- Abstract skim: Tool-using agents alternate between model generation and tool execution, waiting for each tool call to complete before starting the next generation. This sequential execution is costly during agentic reinforcement learning (RL), which requires large batches of multi-turn rollouts. We introduce ObsSpec, an...

### 47 - Beyond Policy Rollouts: Embedding-Space Directional Exploration with Anchored Noise for LLM RLVR

- arXiv: [2610.16105](https://arxiv.org/abs/2610.16105) | [PDF](https://arxiv.org/pdf/2610.16105) | [papers.cool](https://papers.cool/arxiv/2610.16105)
- Authors: Daijiao Liu, Huiyi Wang, Lina Yao, Dong Gong
- Published: 2026-10-12 03:13 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) typically uses small rollout groups per prompt, where repeated sampling from the same policy can yield highly similar trajectories, reducing within-group reward variation and weakening group-relative advantage signals. Existing remedies such as higher sampling...

### 47 - LLM Value Functions for Credit Assignment in Agentic RL

- arXiv: [2610.15840](https://arxiv.org/abs/2610.15840) | [PDF](https://arxiv.org/pdf/2610.15840) | [papers.cool](https://papers.cool/arxiv/2610.15840)
- Authors: Kaijie Zhu, Weixiang Yan, Omar Attia, Abbas Kazerouni, Alexander Toshev, Andrew Szot
- Published: 2026-10-11 18:46 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: reinforcement learning, grpo, ppo; planning_and_action: trajectory
- Abstract skim: Reinforcement learning (RL) for large language model (LLM) agents remains challenging in long-horizon tasks with sparse outcome rewards, where assigning credit to individual actions is difficult. Methods such as GRPO assign the same trajectory-level advantage to all actions, while critic-based methods require...

### 47 - MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL

- arXiv: [2610.14883](https://arxiv.org/abs/2610.14883) | [PDF](https://arxiv.org/pdf/2610.14883) | [papers.cool](https://papers.cool/arxiv/2610.14883)
- Authors: Ulixes Tariq Hawili, Subramanian Ramamoorthy, Yoann Altmann, Ignacio Carlucho
- Published: 2026-10-10 12:57 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: self-play; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: We present MARL-BattleGrounds (MARL-BGs), an easy-to-use JAX-native benchmark for heterogeneous and competitive multi-agent reinforcement learning (MARL), designed to be sample-efficient, computationally efficient, and researcher-centric. MARL benchmarks are typically simple and efficient, like SMAX, where winning...

### 46 - Trust-Calibrated VLA Policy Post-Training with Evolving Imagination

- arXiv: [2610.16517](https://arxiv.org/abs/2610.16517) | [PDF](https://arxiv.org/pdf/2610.16517) | [papers.cool](https://papers.cool/arxiv/2610.16517)
- Authors: Wenzhan Li, Yiran Qin, Heng Zhou, Huirui Wang, Yulan Guo, Ruimao Zhang
- Published: 2026-10-12 10:08 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; planning_and_action: rollout, world model
- Abstract skim: Vision-Language-Action (VLA) models are often pretrained via imitation learning, making reinforcement learning (RL) post-training important when deployment moves beyond demonstration coverage. Existing refinement paradigms expose a reliability--efficiency tension: model-free refinement avoids simulator bias but is...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
