# RL / Post-Training / Agentic RL Reading Queue - 2026-08-25

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 681. Minimum score: 8.

## Top Picks

### 59 - GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning

- arXiv: [2608.22479](https://arxiv.org/abs/2608.22479) | [PDF](https://arxiv.org/pdf/2608.22479) | [papers.cool](https://papers.cool/arxiv/2608.22479)
- Authors: Jun Chen, Yongchao Liu, Pengyu Qiu, Jiajun Zheng, Juelu Zhang, Yujie Zeng, et al. (9 authors)
- Published: 2026-08-23 16:05 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Retrieval-augmented generation (RAG) enables LLMs to access external knowledge for answering knowledge-intensive questions. For complex multi-hop questions, multi-turn retrieval-augmented reasoning extends RAG into an iterative process that repeatedly searches for and integrates evidence across documents. However,...

### 57 - BioMed-Agent-RL: A Meta Learning, All You Need for Biomedical Applications

- arXiv: [2608.21864](https://arxiv.org/abs/2608.21864) | [PDF](https://arxiv.org/pdf/2608.21864) | [papers.cool](https://papers.cool/arxiv/2608.21864)
- Authors: Md Asaduzzaman Jabin, Zihao Wu, Tianming Liu
- Published: 2026-08-22 09:16 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, preference optimization, policy optimization, group relative policy optimization, +2 more; reasoning: reasoning
- Abstract skim: The current progress of Clinical Vision Large Language Models (C-VLLMs) has substantially improved digital diagnostics, still these frameworks often endure lesion noises, modality misalignment, hallucination, and missed contextual grounding in complex clinical cases. Moreover, prevailing agent systems usually depend...

### 56 - Agent-G$^2$: Gaussian Guidance for Agentic Reinforcement Learning

- arXiv: [2608.23318](https://arxiv.org/abs/2608.23318) | [PDF](https://arxiv.org/pdf/2608.23318) | [papers.cool](https://papers.cool/arxiv/2608.23318)
- Authors: Zixuan Wang, Yanrui Miao, Zhengxi Lu, Teng Pan, Yiwen Qiu, Hongxing Li, et al. (9 authors)
- Published: 2026-08-24 14:34 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Hint-based reinforcement learning addresses reward sparsity in long-horizon agentic tasks by retaining a prefix of an expert trajectory before each rollout, letting the policy explore from a state closer to success. Its effectiveness hinges on the guidance depth: how much of the trajectory to keep. Existing methods...

### 54 - HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning

- arXiv: [2608.21863](https://arxiv.org/abs/2608.21863) | [PDF](https://arxiv.org/pdf/2608.21863) | [papers.cool](https://papers.cool/arxiv/2608.21863)
- Authors: Yucan Guo, Xiaohan Wang, Miao Su, Saiping Guan, Zhongni Hou, Jiajun Chai, et al. (11 authors)
- Published: 2026-08-22 09:14 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Tool-Integrated Reasoning (TIR) is a fundamental capability for LLM agents to solve complex tasks by interacting with external tools iteratively. Reinforcement Learning (RL) has become the dominant paradigm for enabling this capability. However, existing approaches typically assign uniform trajectory-level...

### 53 - EDGE: Experience-Distillation for Guided Exploration in Agentic Reinforcement Learning

- arXiv: [2608.21946](https://arxiv.org/abs/2608.21946) | [PDF](https://arxiv.org/pdf/2608.21946) | [papers.cool](https://papers.cool/arxiv/2608.21946)
- Authors: Can Xie, Yuyi Zhou, Wen Yang, Ziyi zhang, Siyao Song, Yingzhuo Deng, et al. (8 authors)
- Published: 2026-08-22 13:16 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, grpo; planning_and_action: rollout; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning with outcome-based objectives such as GRPO enables LLM-based agents to solve complex, long-horizon tasks, yet the reusable exploration patterns embedded in interaction trajectories are largely discarded after a single policy update. Existing experience-augmented approaches retrieve historical...

### 51 - SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning

- arXiv: [2608.23493](https://arxiv.org/abs/2608.23493) | [PDF](https://arxiv.org/pdf/2608.23493) | [papers.cool](https://papers.cool/arxiv/2608.23493)
- Authors: Jialong Liu, Yuling Shi, Ning Yang, Xiaodong Gu, Zuchao Li
- Published: 2026-08-24 16:55 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, policy optimization; reasoning: reasoning, reflection; memory_and_benchmarks: alfworld
- Abstract skim: Self-reflection is a powerful mechanism for credit assignment in human learning, converting sparse outcome feedback into actionable guidance. However, its potential for post-training Large Language Models (LLMs) remains underexplored. We propose Self-Reflective Policy Optimization (SRPO), a framework that...

### 51 - Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding

- arXiv: [2608.22429](https://arxiv.org/abs/2608.22429) | [PDF](https://arxiv.org/pdf/2608.22429) | [papers.cool](https://papers.cool/arxiv/2608.22429)
- Authors: Changjiang Jiang, Qiannian Zhao, Lei Xin, Jinxiang Xie, Preslav Nakov, Zhuohan Xie
- Published: 2026-08-23 14:07 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, grpo; reasoning: reasoning, process reward
- Abstract skim: Multimodal Large Language Models (MLLMs) capable of thinking with images often rely on external tools for fine-grained perception. However, this reliance introduces significant inference latency and fails to effectively resolve the spatial-structural gap-a fundamental challenge in text-dense and structurally...

### 51 - ESCRAG-R1: Retrieval-Augmented Reinforcement Learning for Emotional Support Conversation

- arXiv: [2608.21925](https://arxiv.org/abs/2608.21925) | [PDF](https://arxiv.org/pdf/2608.21925) | [papers.cool](https://papers.cool/arxiv/2608.21925)
- Authors: Weichu Liu, Yuxuan Hu, Yirong Sun, Ningning Mao, Ziyun Zhang, Jian Chen, et al. (9 authors)
- Published: 2026-08-22 11:32 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Emotional Support Conversation (ESC) systems aim to provide holistic support by balancing professional therapeutic competence with natural empathy. However, existing methods struggle to simultaneously achieve structured, stage-aware reasoning and seamless empathy-expertise alignment, often resulting in an artificial...

### 49 - MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks

- arXiv: [2608.23035](https://arxiv.org/abs/2608.23035) | [PDF](https://arxiv.org/pdf/2608.23035) | [papers.cool](https://papers.cool/arxiv/2608.23035)
- Authors: Yi Zhu, Xiongwei Wu, Qiyi Wang, Tingyu Qu, Jiajun Liu, Sihan Cao, et al. (11 authors)
- Published: 2026-08-24 09:38 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, tool use, agent collaboration; rl_post_training: reinforcement learning; planning_and_action: planning; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation...

### 45 - Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data

- arXiv: [2608.23256](https://arxiv.org/abs/2608.23256) | [PDF](https://arxiv.org/pdf/2608.23256) | [papers.cool](https://papers.cool/arxiv/2608.23256)
- Authors: Yinhao Tang, Youqing Fang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, et al. (11 authors)
- Published: 2026-08-24 13:47 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, rlvr; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Recent work proposes next-chunk reasoning RL for leveraging no-CoT data---corpora such as worked solutions and textbook derivations that contain reasoning-rich content but lack explicit chain-of-thought annotations. The method trains a model to generate implicit reasoning traces and rewards them by their ability to...

### 45 - Decoupled Physical Modeling and Execution for Physics Reasoning

- arXiv: [2608.22126](https://arxiv.org/abs/2608.22126) | [PDF](https://arxiv.org/pdf/2608.22126) | [papers.cool](https://papers.cool/arxiv/2608.22126)
- Authors: Ye Zhang, Xuehang Guo, Rui Pan, Pengfei Yu, Denghui Zhang, Manling Li, et al. (7 authors)
- Published: 2026-08-22 22:50 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Physics reasoning requires constructing a consistent model of the underlying physical system rather than relying solely on symbolic or formula-based manipulation. Although large language models have shown strong ability in solving math and coding problems, they still struggle with physics problems, as these problems...

### 45 - MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning

- arXiv: [2608.21808](https://arxiv.org/abs/2608.21808) | [PDF](https://arxiv.org/pdf/2608.21808) | [papers.cool](https://papers.cool/arxiv/2608.21808)
- Authors: Suifeng Zhao, Zida Liu, Xinyu Lei, Lei Sun, Jun Gao, Sujian Li
- Published: 2026-08-22 07:04 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Multimodal Retrieval-Augmented Generation (RAG) with visual citation is crucial for ensuring the traceability and verifiability of MLLMs. However, current RAG and SFT-based methods struggle to achieve robust cross-modal reasoning, causing imprecise visual citations or decoupling between the citation and the...

### 43 - Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World Video Agents

- arXiv: [2608.23329](https://arxiv.org/abs/2608.23329) | [PDF](https://arxiv.org/pdf/2608.23329) | [papers.cool](https://papers.cool/arxiv/2608.23329)
- Authors: Wenqi Liu, Shijie Ma, Yunxiao Wang, Meng Liu, Qile Su, Han Liu, et al. (21 authors)
- Published: 2026-08-24 14:42 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: memory, benchmark
- Abstract skim: Open-world video understanding often requires a model to locate sparse visual evidence and acquire external knowledge that is absent from the video and its parametric memory. While Thinking-with-Videos enables active temporal perception and Deep Research supports multi-step information seeking, the two capabilities...

### 43 - Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents

- arXiv: [2608.21830](https://arxiv.org/abs/2608.21830) | [PDF](https://arxiv.org/pdf/2608.21830) | [papers.cool](https://papers.cool/arxiv/2608.21830)
- Authors: Chengyang Gu, Le Zhang, Jingbo Zhou, Yize Chen, Yu Shi, Siqi Bao, et al. (9 authors)
- Published: 2026-08-22 08:01 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; planning_and_action: trajectory
- Abstract skim: Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) have shown strong potential for automating tasks across diverse digital environments, where reinforcement learning (RL) has become a dominant training paradigm. However, widely used methods such as Group Relative Policy...

### 42 - Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation

- arXiv: [2608.23152](https://arxiv.org/abs/2608.23152) | [PDF](https://arxiv.org/pdf/2608.23152) | [papers.cool](https://papers.cool/arxiv/2608.23152)
- Authors: Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty
- Published: 2026-08-24 11:55 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent, agent memory; reasoning: reasoning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To...

### 41 - Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM Policy Optimization

- arXiv: [2608.23311](https://arxiv.org/abs/2608.23311) | [PDF](https://arxiv.org/pdf/2608.23311) | [papers.cool](https://papers.cool/arxiv/2608.23311)
- Authors: Xianlei Zhou, Xiangdi Meng, Yu He, Tianyu Qi, Shuyan Guan, Xianli Zhang, et al. (10 authors)
- Published: 2026-08-24 14:30 UTC | Categories: cs.CL
- Why it matched: rl_post_training: policy optimization, grpo, ppo; reasoning: reasoning
- Abstract skim: Policy optimization (PO) for Large Language Models faces a stability--exploration trade-off, currently mediated by an action-side Policy-KL regularizer. This puts practitioners in a double bind: keeping Policy-KL constrains response behavior and consumes the action-side exploration budget, while dropping it leaves...

### 41 - Meta-Moderator: Empowering Multi-Agent Debate with Meta-Cognition

- arXiv: [2608.23029](https://arxiv.org/abs/2608.23029) | [PDF](https://arxiv.org/pdf/2608.23029) | [papers.cool](https://papers.cool/arxiv/2608.23029)
- Authors: Wentao Hu, Zhuoyue Wan, Jinhao Shen, Chen Jason Zhang, Xiaoyong Wei, Qing Li
- Published: 2026-08-24 09:33 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; rl_post_training: policy optimization; reasoning: reasoning, deliberation
- Abstract skim: Multi-agent debate can improve large language model reasoning by eliciting diverse hypotheses and critiques, yet its performance is often constrained by weak moderation. Common pipelines rely on fixed budgets, agreement-based stopping, or untrained judges, leading to redundant deliberation and unreliable evidence...

### 40 - Let Credit Follow Computation: Architecture-Aware Credit Transport for Large Language Model Reinforcement Learning

- arXiv: [2608.21501](https://arxiv.org/abs/2608.21501) | [PDF](https://arxiv.org/pdf/2608.21501) | [papers.cool](https://papers.cool/arxiv/2608.21501)
- Authors: Qifan Shi, Zhaolu Kang, Chenghua Zhu
- Published: 2026-08-21 16:25 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, grpo, ppo; planning_and_action: trajectory, rollout; memory_and_benchmarks: evaluation
- Abstract skim: Credit assignment in large-language-model reinforcement learning (LLM RL) can be separated into three objects: evidence about success, a transport operator that converts this evidence into token-level advantages, and an update geometry that turns advantages into policy changes. Recent work has greatly improved...

### 39 - GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis

- arXiv: [2608.22847](https://arxiv.org/abs/2608.22847) | [PDF](https://arxiv.org/pdf/2608.22847) | [papers.cool](https://papers.cool/arxiv/2608.22847)
- Authors: Long Zhang, Yuhan Chen, Chaoran Zhang, Wanxia Cao, Kun Huang, Pengzhi Gao, et al. (10 authors)
- Published: 2026-08-24 06:27 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Vision-Language Models (VLMs) based GUI agents stand to benefit significantly from online reinforcement learning (RL). However, their training is bottlenecked by two fundamental issues: current data synthesis methods for GUI Agents rely on specific environments and struggle to generate diverse data, while existing...

### 35 - Small Reasoning Models are Instruction Followers in Function Calling

- arXiv: [2608.22472](https://arxiv.org/abs/2608.22472) | [PDF](https://arxiv.org/pdf/2608.22472) | [papers.cool](https://papers.cool/arxiv/2608.22472)
- Authors: Yalda Taheri, Mohammad Hassan Heydari, Erfan Naaman, Afsaneh Fatemi
- Published: 2026-08-23 15:51 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Function calling represents the core capability of agentic large language models (LLMs). Existing research has focused on enhancing LLMs function-calling accuracy through fine-tuning, reinforcement learning (RL), and multi-agent frameworks, particularly for native function-calling LLMs. This work demonstrates that...

### 34 - HERO: Human-profile Enhanced Retrieval Optimization Framework for Long-term Agent Memory

- arXiv: [2608.22310](https://arxiv.org/abs/2608.22310) | [PDF](https://arxiv.org/pdf/2608.22310) | [papers.cool](https://papers.cool/arxiv/2608.22310)
- Authors: Yuanhua Lin, Yile Li, Zhiyuan Zhao, Jing Shang, Jian Sun
- Published: 2026-08-23 09:19 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory, long-horizon agent; reasoning: reasoning; memory_and_benchmarks: memory, long-term memory, benchmark
- Abstract skim: Long-term memory is crucial for personalized responses and long-horizon agent interactions. Existing methods often rely on LLMs to compress or rewrite dialogue histories and use the transformed memories as retrieval evidence. Despite the progress in organizing fragmented contexts, two major drawbacks persist: (1)...

### 34 - Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning

- arXiv: [2608.21811](https://arxiv.org/abs/2608.21811) | [PDF](https://arxiv.org/pdf/2608.21811) | [papers.cool](https://papers.cool/arxiv/2608.21811)
- Authors: Qiqian Fu
- Published: 2026-08-22 07:17 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning for vision-language math reasoning starves under sparse reward: on a pool of 20,830 visual-math problems where Qwen2-VL-2B answers 3.6% of rollouts correctly, 85-97% of GRPO rollout groups are entirely wrong and contribute zero gradient. We train eleven methods under identical conditions in...

### 33 - MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning

- arXiv: [2608.22167](https://arxiv.org/abs/2608.22167) | [PDF](https://arxiv.org/pdf/2608.22167) | [papers.cool](https://papers.cool/arxiv/2608.22167)
- Authors: Ziyang Luo, Yan Yang, Xiangru Jian, Ziji Shi, Xiaoqiang Lin, Jun Hao Liew, et al. (8 authors)
- Published: 2026-08-23 01:49 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) has become an effective way to improve the tool-use ability of large language models (LLMs), but most existing RL frameworks stop at the policy update. For every new domain, the user is left with two hard systems problems: standing up an isolated environment for each of hundreds of...

### 33 - ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning

- arXiv: [2608.21860](https://arxiv.org/abs/2608.21860) | [PDF](https://arxiv.org/pdf/2608.21860) | [papers.cool](https://papers.cool/arxiv/2608.21860)
- Authors: Weihang Pan, Zhengxu Yu, Yuxiang Zhang, Wenzhi Li, Zhongming Jin, Binbin Lin, et al. (8 authors)
- Published: 2026-08-22 09:09 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: dpo; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Chain-of-Thought (CoT) reasoning has significantly enhanced the multi-step problem-solving capabilities of large language models (LLMs) by introducing explicit intermediate reasoning. However, advanced Large Reasoning Models (LRMs) often exhibit overthinking behaviors, including excessively long reasoning steps,...

### 33 - Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data

- arXiv: [2608.21727](https://arxiv.org/abs/2608.21727) | [PDF](https://arxiv.org/pdf/2608.21727) | [papers.cool](https://papers.cool/arxiv/2608.21727)
- Authors: Renfei Zhang, Niloofar Mireshghallah
- Published: 2026-08-22 02:17 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) is deployed to make models better at reasoning tasks, but its side effect on what models will divulge is under studied. Here we show that RLVR on facts increases extraction of personally identifiable information (PII) the instruct model had already memorized. We...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
