# RL / Post-Training / Agentic RL Reading Queue - 2026-07-07

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 857. Minimum score: 8.

## Top Picks

### 70 - Progress- and Reliability-Oriented Group Policy Optimization for Agentic Reinforcement Learning

- arXiv: [2607.04242](https://arxiv.org/abs/2607.04242) | [PDF](https://arxiv.org/pdf/2607.04242) | [papers.cool](https://papers.cool/arxiv/2607.04242)
- Authors: Mingxuan Fan, Peiyang Liu
- Published: 2026-07-05 11:41 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Group-based reinforcement learning (RL) has become an effective paradigm for improving large language model agents on long-horizon interactive tasks. To obtain finer-grained policy updates than trajectory-level optimization, recent work has moved toward step-level group-based RL, where intermediate steps are grouped...

### 69 - Reward Granularity in RLVR: Comparing Process and Outcome Reward Structures for Mathematical Reasoning in Small Language Models

- arXiv: [2607.02869](https://arxiv.org/abs/2607.02869) | [PDF](https://arxiv.org/pdf/2607.02869) | [papers.cool](https://papers.cool/arxiv/2607.02869)
- Authors: Anagha Radhakrishna Palandye, Rebecca Glick, Osheen Kaul
- Published: 2026-07-03 02:16 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning, outcome reward
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a promising paradigm for improving mathematical reasoning in language models. Yet most RLVR work rewards only the final answer (outcome-based rewards), leaving the impact of step-level process supervision (process rewards) underexplored especially...

### 68 - STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training

- arXiv: [2607.04963](https://arxiv.org/abs/2607.04963) | [PDF](https://arxiv.org/pdf/2607.04963) | [papers.cool](https://papers.cool/arxiv/2607.04963)
- Authors: Qiuyi Qi, Tian Liang, Mutian Bao, Jinjian Zhang, Dongnan Liu, Wei Zhou, et al. (11 authors)
- Published: 2026-07-06 11:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, agent training; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement Learning (RL) is the dominant paradigm for training Large Language Model (LLM) agents on long-horizon tasks. However, sparse and delayed rewards often lead to trajectory neglect, in which agents lose focus on the task goal and interaction history at intermediate steps. Prior work has explored step-...

### 60 - VideoSearcher: Empowering Video Deep Research with Multi-Tool Agentic Reasoning via Reinforcement Learning

- arXiv: [2607.02927](https://arxiv.org/abs/2607.02927) | [PDF](https://arxiv.org/pdf/2607.02927) | [papers.cool](https://papers.cool/arxiv/2607.02927)
- Authors: Zhenkun Gao, Yicheng Bao, Jinlong Peng, Xueheng Li, Theo Huang, Bangwei Liu, et al. (16 authors)
- Published: 2026-07-03 03:50 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Video understanding is moving beyond closed-context perception toward open-world evidence exploration, a paradigm formalized as Video Deep Research (VDR). However, existing multimodal search agents primarily target static images, and the current VDR benchmark relies on text-centric retrieval that discards crucial...

### 53 - Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations

- arXiv: [2607.04235](https://arxiv.org/abs/2607.04235) | [PDF](https://arxiv.org/pdf/2607.04235) | [papers.cool](https://papers.cool/arxiv/2607.04235)
- Authors: Zichao Li, Gang Wu, Zichao Wang, Ruiyi Zhang, Wanrong Zhu, Ryan A. Rossi, et al. (8 authors)
- Published: 2026-07-05 11:21 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent; rl_post_training: post-training, post training, dpo; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Large language model agents operate in partially observable, long-horizon settings where obtaining supervision remains a major bottleneck. We address this by utilizing a source of supervision overlooked in existing post-training methods: unintended yet successful goals embedded within agent rollouts. Specifically,...

### 52 - NKI-Agent: Domain-Specific Fine-Tuning and Agentic Tool Use for Neuron Kernel Generation

- arXiv: [2607.04395](https://arxiv.org/abs/2607.04395) | [PDF](https://arxiv.org/pdf/2607.04395) | [papers.cool](https://papers.cool/arxiv/2607.04395)
- Authors: Junjie Tang, Jun Huan, Hao Zhou, Yuhao Zhang, Lin Wang
- Published: 2026-07-05 16:37 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: policy optimization, group relative policy optimization, grpo; memory_and_benchmarks: memory, benchmark
- Abstract skim: Recent agentic approaches to LLM-based kernel generation have achieved impressive results on CUDA. For emerging AI accelerators such as AWS Trainium and Inferentia, automated kernel generation and optimization remain largely unaddressed. Writing kernels for these chips via the Neuron Kernel Interface (NKI) is...

### 51 - RL Forgets! Towards Continual Policy Optimization

- arXiv: [2607.04364](https://arxiv.org/abs/2607.04364) | [PDF](https://arxiv.org/pdf/2607.04364) | [papers.cool](https://papers.cool/arxiv/2607.04364)
- Authors: Mao-Lin Luo, Zhe-Xu Wang, Zi-Hao Zhou, Bo Ye, Jian Zhao, Min-Ling Zhang, et al. (7 authors)
- Published: 2026-07-05 15:46 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Continual post-training is becoming a central paradigm for adapting vision-language models to evolving tasks. Recent work has increasingly favored reinforcement learning over supervised fine-tuning, driven by the belief that reinforcement learning is inherently less prone to forgetting. However, the belief remains...

### 49 - Weak-to-Strong Generalization via Direct On-Policy Distillation

- arXiv: [2607.05394](https://arxiv.org/abs/2607.05394) | [PDF](https://arxiv.org/pdf/2607.05394) | [papers.cool](https://papers.cool/arxiv/2607.05394)
- Authors: Shiyuan Feng, Huan-ang Gao, Haohan Chi, Hanlin Wu, Zhilong Zhang, Zheng Jiang, et al. (10 authors)
- Published: 2026-07-06 17:59 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-...

### 49 - NormWorlds-CF: Solver-Verified Counterfactual Normative Reasoning with Metamorphic-Relation GRPO

- arXiv: [2607.03957](https://arxiv.org/abs/2607.03957) | [PDF](https://arxiv.org/pdf/2607.03957) | [papers.cool](https://papers.cool/arxiv/2607.03957)
- Authors: Xinqi Zhang
- Published: 2026-07-04 17:11 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Language models can reach the right normative verdict for the wrong reason. We introduce NormWorlds-CF, a solver-verified environment for counterfactual normative reasoning in executable rule worlds. Its deterministic solver produces final answers, proof and falsification certificates, argument statuses, support...

### 48 - TokAN: Accent Normalization Using Self-Supervised Speech Tokens

- arXiv: [2607.03928](https://arxiv.org/abs/2607.03928) | [PDF](https://arxiv.org/pdf/2607.03928) | [papers.cool](https://papers.cool/arxiv/2607.03928)
- Authors: Qibing Bai, Shuai Wang, Yuhan Du, Bohan Li, Yannan Wang, Haizhou Li
- Published: 2026-07-04 15:45 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more
- Abstract skim: Accent normalization (AN) seeks to convert non-native (L2) accented speech into standard (L1) speech while preserving speaker identity. The current techniques either require naturally recorded parallel L1-L2 speech for training, or suffer from quality degradation when supervised by synthesized targets. In this...

### 48 - CONFLUX: A Latent Diusion Model for 3D Chest-CT Synthesis with RL Post-Training

- arXiv: [2607.02998](https://arxiv.org/abs/2607.02998) | [PDF](https://arxiv.org/pdf/2607.02998) | [papers.cool](https://papers.cool/arxiv/2607.02998)
- Authors: Max Van Puyvelde, Halil Ibrahim Gulluk, Wim Van Criekinge, Olivier Gevaert
- Published: 2026-07-03 06:31 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more
- Abstract skim: Controllable generative models of 3D medical images can synthesize volumes with specified clinical attributes, but this demands samples that are simultaneously high-fidelity, natively 3D, and faithful to the requested conditioning. We present CONFLUX, a latent diffusion model for chest computed tomography (CT): a 3D...

### 45 - Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning

- arXiv: [2607.04681](https://arxiv.org/abs/2607.04681) | [PDF](https://arxiv.org/pdf/2607.04681) | [papers.cool](https://papers.cool/arxiv/2607.04681)
- Authors: Matthew Foutter, Matteo Cercola, Lena Wild, Yunshan Wang, Michelle Li, Daniele Gammelli, et al. (7 authors)
- Published: 2026-07-06 05:10 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory, decision making; memory_and_benchmarks: evaluation; downranked: driving, autonomous driving
- Abstract skim: Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We...

### 42 - Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses

- arXiv: [2607.05029](https://arxiv.org/abs/2607.05029) | [PDF](https://arxiv.org/pdf/2607.05029) | [papers.cool](https://papers.cool/arxiv/2607.05029)
- Authors: Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu, Dinghao Wu
- Published: 2026-07-06 13:10 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, agent memory; reasoning: reasoning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning...

### 42 - RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents

- arXiv: [2607.04713](https://arxiv.org/abs/2607.04713) | [PDF](https://arxiv.org/pdf/2607.04713) | [papers.cool](https://papers.cool/arxiv/2607.04713)
- Authors: Qiang Liu, Taian Guo, Ruizhi Qiao, Xing Sun
- Published: 2026-07-06 06:32 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo, ppo; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks. However, in long-horizon, multi-turn tasks characterized by sparse outcome rewards, directly training with outcome rewards often results in slow convergence due to the sparsity of...

### 40 - Reinforcement Learning for Data-Efficient Code-Switched ASR

- arXiv: [2607.02757](https://arxiv.org/abs/2607.02757) | [PDF](https://arxiv.org/pdf/2607.02757) | [papers.cool](https://papers.cool/arxiv/2607.02757)
- Authors: Ziwei Ye, Peter Vickers
- Published: 2026-07-02 20:44 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization
- Abstract skim: Audio-language models can be prompted for code-switched speech, but their decoding is not optimized for code-switching and often fails at language boundaries. We propose a practical reinforcement learning with verifiable rewards recipe for data-efficient adaptation of audio-language models to code-switched ASR using...

### 38 - Anticipatory Reinforcement Learning for Trajectory Tracking

- arXiv: [2607.03132](https://arxiv.org/abs/2607.03132) | [PDF](https://arxiv.org/pdf/2607.03132) | [papers.cool](https://papers.cool/arxiv/2607.03132)
- Authors: Georg Schäfer, Jakob Rehrl, Stefan Huber, Simon Hirlaender
- Published: 2026-07-03 09:21 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; planning_and_action: trajectory
- Abstract skim: Deep reinforcement learning (DRL) in industrial control often suffers from lag and overshoot due to purely reactive control based on the current tracking error. To achieve anticipatory control without high computational overhead, we introduce a predictive formulation that augments the DRL state space with target...

### 37 - TREK: Distill to Explore, Reinforce to Refine

- arXiv: [2607.05339](https://arxiv.org/abs/2607.05339) | [PDF](https://arxiv.org/pdf/2607.05339) | [papers.cool](https://papers.cool/arxiv/2607.05339)
- Authors: Yuanda Xu, Zhengze Zhou, Kayhan Behdin, Jelena Markovic-Voronov, Hejian Sang, Xiaomin Li, et al. (13 authors)
- Published: 2026-07-06 17:21 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: alfworld, scienceworld
- Abstract skim: Group Relative Policy Optimization (GRPO) is effective when the current policy already samples useful reasoning trajectories, but it stalls on hard prompts whose correct solution modes lie outside the student's on-policy support. We propose TREK (Teacher-Routed Exploration via Forward KL), a simple staged procedure...

### 37 - Forethought: Verifiable Reasoning from Neurosymbolic Primitive Programming

- arXiv: [2607.04096](https://arxiv.org/abs/2607.04096) | [PDF](https://arxiv.org/pdf/2607.04096) | [papers.cool](https://papers.cool/arxiv/2607.04096)
- Authors: Vishvesh Bhat, Jay Vaghasiya, Emmanuel Anaya Gonzalez
- Published: 2026-07-05 03:20 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Current agentic workflows usually involve decomposing user requests into sequences of tool calls with correctly resolved parameters, the results of which are processed through reasoning traces in the language model's context window. The prevailing route to improve such reasoning is test-time scaling, which trains...

### 37 - Reinforcement Learning for Evidence-Seeking Diagnostic Reasoning with Large Language Models

- arXiv: [2607.02983](https://arxiv.org/abs/2607.02983) | [PDF](https://arxiv.org/pdf/2607.02983) | [papers.cool](https://papers.cool/arxiv/2607.02983)
- Authors: Shengyi Hua, Kangzhe Hu, Conghui He, Xiaofan Zhang, Shaoting Zhang
- Published: 2026-07-03 05:43 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Recent reasoning-centric Large Language Models (LLMs) have made significant strides, yet they predominantly operate on a passive-inference pattern that assumes complete information. In contrast, real-world clinical intelligence is inherently an iterative investigative process requiring strategic evidence...

### 36 - Regime-Conditional Stabilisation of LLM-Augmented Cooperative Multi-Agent Reinforcement Learning

- arXiv: [2607.04470](https://arxiv.org/abs/2607.04470) | [PDF](https://arxiv.org/pdf/2607.04470) | [papers.cool](https://papers.cool/arxiv/2607.04470)
- Authors: Faid Keddouri, Sohaib Houhou, Aissa Boulmerka, Nadir Farhi
- Published: 2026-07-05 19:29 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Large Language Models (LLMs) offer a natural interface for translating human objectives into reward signals for cooperative multi-agent reinforcement learning (MARL), yet the training-time dynamics of this integration remain poorly understood. We show that dynamically updating LLM-generated reward weights during...

### 36 - dOPSD: On-Policy Self-Distillation for Diffusion Language Models

- arXiv: [2607.04428](https://arxiv.org/abs/2607.04428) | [PDF](https://arxiv.org/pdf/2607.04428) | [papers.cool](https://papers.cool/arxiv/2607.04428)
- Authors: Phuong Tuan Dat, Qi Li, Xinchao Wang
- Published: 2026-07-05 17:47 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Diffusion large language models (dLLMs) generate text by iteratively denoising a masked sequence, offering a parallel alternative to autoregressive models, but eliciting strong reasoning through post-training remains difficult: supervised fine-tuning is off-policy and suffers from exposure bias, while reinforcement...

### 36 - Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems

- arXiv: [2607.03324](https://arxiv.org/abs/2607.03324) | [PDF](https://arxiv.org/pdf/2607.03324) | [papers.cool](https://papers.cool/arxiv/2607.03324)
- Authors: Hyunsoo Lee, Panggah Prabawa, Dae-Hyun Choi, Joongheon Kim
- Published: 2026-07-03 13:41 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Eco-friendly energy management for artificial intelligence data centers (AIDCs) is crucial because of the significant increase in energy consumption-induced carbon emissions from AIDCs resulting from the rapid expansion of AI applications. This paper proposes a hierarchical carbon-aware multi-agent reinforcement...

### 36 - ACPO: Adaptive Credit Policy Optimization via Fine-Grained Surrogate Entropy

- arXiv: [2607.03126](https://arxiv.org/abs/2607.03126) | [PDF](https://arxiv.org/pdf/2607.03126) | [papers.cool](https://papers.cool/arxiv/2607.03126)
- Authors: Zijun Xie, Yuyang You, Yongzhi Li, Enlei Gong, Zeyu Chen, Quan Chen, et al. (9 authors)
- Published: 2026-07-03 09:14 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement Learning (RL) has substantially improved the reasoning ability of large language models (LLMs), but sparse outcome rewards still make token-level credit assignment difficult. Existing scalable RL methods typically assign trajectory-level rewards uniformly across tokens, while recent entropy-aware...

### 36 - ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability

- arXiv: [2607.02686](https://arxiv.org/abs/2607.02686) | [PDF](https://arxiv.org/pdf/2607.02686) | [papers.cool](https://papers.cool/arxiv/2607.02686)
- Authors: Juarez Monteiro, Nathan Gavenski, Guilherme Lima, Francisco Galuppo, Odinaldo Rodrigues, Adriano Veloso
- Published: 2026-07-02 18:26 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, ppo; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory
- Abstract skim: Reinforcement learning agents operating under partial observability must act on incomplete information, making them natural candidates for guidance from small language models (SLMs) that carry broad reasoning priors. Yet integrating SLM guidance into this setting has proven difficult: across all test environments,...

### 35 - LLM-as-a-Verifier: A General-Purpose Verification Framework

- arXiv: [2607.05391](https://arxiv.org/abs/2607.05391) | [PDF](https://arxiv.org/pdf/2607.05391) | [papers.cool](https://papers.cool/arxiv/2607.05391)
- Authors: Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, et al. (9 authors)
- Published: 2026-07-06 17:59 UTC | Categories: cs.AI, cs.CL, cs.LG, cs.MA, cs.RO
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
