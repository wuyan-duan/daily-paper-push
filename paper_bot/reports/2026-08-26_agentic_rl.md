# RL / Post-Training / Agentic RL Reading Queue - 2026-08-26

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 400. Minimum score: 8.

## Top Picks

### 68 - On-policy Distillation with Verifiable Reward

- arXiv: [2608.24696](https://arxiv.org/abs/2608.24696) | [PDF](https://arxiv.org/pdf/2608.24696) | [papers.cool](https://papers.cool/arxiv/2608.24696)
- Authors: Wenze Lin, Jiale Zhao, Xitai Jiang, Songde Rao, Yining Li, Shenzhi Wang, et al. (8 authors)
- Published: 2026-08-25 15:21 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +2 more; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) and on-policy distillation (OPD) have become two widely adopted paradigms for post-training large language models. However, RLVR suffers from sparse task-level feedback, while OPD provides dense token-level guidance but ignores trajectory correctness, limiting...

### 61 - Contrastive Branch Policy Optimization

- arXiv: [2608.24300](https://arxiv.org/abs/2608.24300) | [PDF](https://arxiv.org/pdf/2608.24300) | [papers.cool](https://papers.cool/arxiv/2608.24300)
- Authors: Ying Wang, Changlin Qiu, Bang Lin, Linbo Jin, Wen Jiang, Zhe Sun, et al. (7 authors)
- Published: 2026-08-25 09:25 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning, rlvr, policy optimization; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) enables language models to learn multi-turn interaction with external tools, yet its sparse outcome rewards provide no signal for identifying which intermediate decisions are responsible for success. Branch sampling induces local comparisons among alternative...

### 59 - SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL

- arXiv: [2608.24870](https://arxiv.org/abs/2608.24870) | [PDF](https://arxiv.org/pdf/2608.24870) | [papers.cool](https://papers.cool/arxiv/2608.24870)
- Authors: Kai Ruan, Jinghao Lin, Qianshan Wei, Ziqi Zhou, Zihe Huang
- Published: 2026-08-25 17:52 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl, tool use; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Group-relative reinforcement learning waits for sibling rollouts of the same prompt, which is costly for long and variable tool-use trajectories. Single-stream Policy Optimization (SPO) removes this dependency with a persistent prompt-level value estimate, but its recipe whitens one advantage per trajectory before...

### 48 - AHEAD: Adaptive Hindsight with Environment-Augmented Distillation for Agentic RL

- arXiv: [2608.24114](https://arxiv.org/abs/2608.24114) | [PDF](https://arxiv.org/pdf/2608.24114) | [papers.cool](https://papers.cool/arxiv/2608.24114)
- Authors: Xiaolong Jin, Dingmin Wang, Vijay Lingam, Varun Kumar
- Published: 2026-08-25 06:23 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic rl; rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory, environment feedback; memory_and_benchmarks: alfworld
- Abstract skim: Training multi-turn LLM agents with reinforcement learning typically relies on trajectory-level rewards, which assign a uniform advantage to every step and cannot identify which decisions led to success or failure. Self-distillation methods can provide finer-grained supervision by augmenting RL with privileged...

### 41 - STRIVE: Multi-Agent Structured Temporal Reasoning with Integrated Verification for Longitudinal Radiology Report Generation

- arXiv: [2608.24237](https://arxiv.org/abs/2608.24237) | [PDF](https://arxiv.org/pdf/2608.24237) | [papers.cool](https://papers.cool/arxiv/2608.24237)
- Authors: Junyeong Maeng, Eunsong Kang, Heung-Il Suk
- Published: 2026-08-25 08:43 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: grpo; reasoning: reasoning
- Abstract skim: Longitudinal radiology report generation (LRRG) requires identifying both current findings and their changes relative to a prior study. Existing methods jointly model diagnosis, attribute estimation, temporal comparison, and language generation within implicit representations, which can cause task interference,...

### 41 - RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges

- arXiv: [2608.24231](https://arxiv.org/abs/2608.24231) | [PDF](https://arxiv.org/pdf/2608.24231) | [papers.cool](https://papers.cool/arxiv/2608.24231)
- Authors: Kaiyuan Liu, Ziyuan Zhuang, Rongxiang Weng, Jieping Ye
- Published: 2026-08-25 08:35 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, self-improvement, self improvement, process reward; memory_and_benchmarks: evaluation
- Abstract skim: LLM-as-judge is essential for evaluating open-ended text and steering post-training, yet improving the judge itself typically relies on expensive annotations, reward models, or distillation from stronger teachers. In this work, we eliminate external gold supervision from the RL training reward: the model's own...

### 40 - Preference Optimization for Non-Verbal Vocalization Synthesis

- arXiv: [2608.24163](https://arxiv.org/abs/2608.24163) | [PDF](https://arxiv.org/pdf/2608.24163) | [papers.cool](https://papers.cool/arxiv/2608.24163)
- Authors: Haoyang Li, Chenglin Xu, Junchuan Zhao, Yuang Cao, Liumeng Xue, Yiwen Guo, et al. (7 authors)
- Published: 2026-08-25 07:27 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, preference optimization, dpo
- Abstract skim: Non-verbal vocalizations (NVs), such as laughter, coughs, and sighs, are essential for expressive TTS, but the effectiveness of preference optimization for NV generation remains poorly understood. We systematically study preference optimization for NV-capable TTS, focusing on preference signals, preference-pair...

### 37 - Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning

- arXiv: [2608.24658](https://arxiv.org/abs/2608.24658) | [PDF](https://arxiv.org/pdf/2608.24658) | [papers.cool](https://papers.cool/arxiv/2608.24658)
- Authors: Zhengyang Zhang, Zijian Zhang, Jiaxuan Gao, Shusheng Xu, Yi Wu, Song Han, et al. (7 authors)
- Published: 2026-08-25 15:02 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: Scaling test-time reasoning has substantially improved the problem-solving ability of large language models (LLMs), but standard autoregressive decoding still executes long reasoning traces sequentially, creating severe latency for difficult tasks (up to days and weeks). Parallel reasoning offers a natural remedy....

### 34 - Joint Optimization of Tool Creation and Use for Large Language Model Agents

- arXiv: [2608.24571](https://arxiv.org/abs/2608.24571) | [PDF](https://arxiv.org/pdf/2608.24571) | [papers.cool](https://papers.cool/arxiv/2608.24571)
- Authors: Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee
- Published: 2026-08-25 13:59 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Tool-augmented language models are bounded by the APIs humans bothered to write; existing tool-creation systems patch this by prompting a frozen LLM at inference time, leaving the model that writes a tool decoupled from the one that uses it, with no signal that the schemas it produces are schemas it can invoke. We...

### 34 - Reinforcement Learning-Guided Evolutionary Policy Optimization for Preference-Adjustable Heterogeneous Agile Earth Observation Satellite Scheduling

- arXiv: [2608.24470](https://arxiv.org/abs/2608.24470) | [PDF](https://arxiv.org/pdf/2608.24470) | [papers.cool](https://papers.cool/arxiv/2608.24470)
- Authors: He Wang, Junyu Wu, Hui Li, Yanjie Song, Witold Pedrycz, Liang Li
- Published: 2026-08-25 12:16 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: evaluation
- Abstract skim: Heterogeneous agile Earth observation satellite (AEOS) scheduling requires task selection, satellite assignment, and observation sequencing under satellite-dependent visibility windows, attitude maneuvering requirements, energy consumption, and onboard storage constraints. Since satellites differ in orbital access,...

### 33 - NeuralParker: A Reinforcement Learning Planner for Irregular Parking Environments

- arXiv: [2608.24485](https://arxiv.org/abs/2608.24485) | [PDF](https://arxiv.org/pdf/2608.24485) | [papers.cool](https://papers.cool/arxiv/2608.24485)
- Authors: Zihan Wang, Bai Huang, Yang Guan, Xiao Li, Haoyu Xu, Naizheng Wang, et al. (7 authors)
- Published: 2026-08-25 12:33 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning, trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Automated parking commonly assumes marked slots and short approach maneuvers. Delivery and service vehicles, however, may need to reach an operator-specified pose in an irregular bounded environment from a distant start. Existing learning-based parking planners often rely on local observations, which can restrict...

### 33 - FARCA: Fact-Aligned Reliability-Aware Credit Assignment for Reinforcement Learning with Factual Supervision

- arXiv: [2608.24350](https://arxiv.org/abs/2608.24350) | [PDF](https://arxiv.org/pdf/2608.24350) | [papers.cool](https://papers.cool/arxiv/2608.24350)
- Authors: Qiming Xie, Wenjie Zheng, Xiangqing Shen, Rui Xia
- Published: 2026-08-25 10:07 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: To reduce the hallucination risk caused by outcome-driven rewards in large language models trained through reinforcement learning with verifiable rewards, existing mitigation approaches introduce process-level factual supervision. However, due to coarse-grained aggregation of factual signals and the lack of...

### 33 - Function-Level Execution Feedback for Code Preference Optimization

- arXiv: [2608.23632](https://arxiv.org/abs/2608.23632) | [PDF](https://arxiv.org/pdf/2608.23632) | [papers.cool](https://papers.cool/arxiv/2608.23632)
- Authors: Idris Nechnech, Sehwan Kim, Jimin Seo, Yeongoon Kim, Minhae Oh, Sangwoo Hong, et al. (7 authors)
- Published: 2026-08-23 13:53 UTC | Categories: cs.AI
- Why it matched: rl_post_training: preference optimization, dpo; reasoning: reasoning
- Abstract skim: Process supervision has improved mathematical reasoning, where intermediate steps are naturally expressed as chains of thought. In code generation, however, process supervision remains underexplored because there is no standard notion of a step. Supervision can target lines, reasoning traces, or program states,...

### 32 - Generating Biomedical Fact-Checking Reports with RL-Enhanced Agentic Search

- arXiv: [2608.23811](https://arxiv.org/abs/2608.23811) | [PDF](https://arxiv.org/pdf/2608.23811) | [papers.cool](https://papers.cool/arxiv/2608.23811)
- Authors: Jiongxiao Wang, Dingli Ma, Chaoqun Ni
- Published: 2026-08-24 20:25 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: Automated fact-checking is essential for ensuring the reliability of public health information, yet the biomedical domain poses unique challenges. Validating biomedical claims requires rigorous interpretation of scientific literature, assessment of retrieved evidence, and comprehensive justification toward the...

### 31 - Quantization Effects on Bangla Language Understanding in Large Language Models: A Systematic Evaluation

- arXiv: [2608.24615](https://arxiv.org/abs/2608.24615) | [PDF](https://arxiv.org/pdf/2608.24615) | [papers.cool](https://papers.cool/arxiv/2608.24615)
- Authors: Ismail Hossain, Nafi Ullah Shafin, Mohammad Abdullah Al Mumin
- Published: 2026-08-25 14:36 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Post-training quantization lowers the memory footprint of Large Language Models (LLMs) and speeds up inference, which is why it is now common for on-device deployment. Most of what we know about its effects, however, comes from English benchmarks. It is not clear whether the same holds for morphologically complex,...

### 30 - Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses

- arXiv: [2608.24876](https://arxiv.org/abs/2608.24876) | [PDF](https://arxiv.org/pdf/2608.24876) | [papers.cool](https://papers.cool/arxiv/2608.24876)
- Authors: Zhaochen Yu, Yingcheng Wu, Zhenfei Yin, Kaiyuan Chen, Zhe Zhao, Mengdi Wang, et al. (8 authors)
- Published: 2026-08-25 17:56 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: long-horizon agent; reasoning: self-improvement, self improvement; memory_and_benchmarks: memory, benchmark
- Abstract skim: Recursive self-improvement (RSI) remains hard in long-horizon tasks, where growing histories obscure the task state and misalign skill invocation. We introduce Recuris, a recursive Experiential-Working Memory architecture for long-horizon agent harnesses, in which Working Memory tracks task progress and guides skill...

### 30 - IAPO: Influence-Aware Policy Optimization for Credit Assignment in Multi-Turn Service Agents

- arXiv: [2608.24588](https://arxiv.org/abs/2608.24588) | [PDF](https://arxiv.org/pdf/2608.24588) | [papers.cool](https://papers.cool/arxiv/2608.24588)
- Authors: Bo Ren, Yirong Mao, Yi Yang, Wenhui Que
- Published: 2026-08-25 14:14 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory, rollout
- Abstract skim: Large Language Model (LLM) agents increasingly solve long-horizon tasks through multi-turn interactions with users and external tools. In these settings, relevant task information often unfolds over time rather than being fully specified at the initial prompt. Service agents make this challenge especially concrete:...

### 30 - The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses

- arXiv: [2608.23953](https://arxiv.org/abs/2608.23953) | [PDF](https://arxiv.org/pdf/2608.23953) | [papers.cool](https://papers.cool/arxiv/2608.23953)
- Authors: Dai Jiahong
- Published: 2026-08-25 01:26 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, autonomous agent, agent harness
- Abstract skim: An agent harness is what turns a language model into an autonomous agent: the surrounding code that builds the model's context, mediates its tools, runs the loop, and persists state across a long-horizon run. This layer, not the model it wraps, is increasingly the binding constraint on agent behaviour. We present a...

### 29 - RoG-DAgger: Rollout-Guided Post-Training for End-to-End Driving

- arXiv: [2608.24525](https://arxiv.org/abs/2608.24525) | [PDF](https://arxiv.org/pdf/2608.24525) | [papers.cool](https://papers.cool/arxiv/2608.24525)
- Authors: Liangyu Zhong, Joachim Sicking, Fabian Hueger, Hanno Gottschalk
- Published: 2026-08-25 13:11 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; planning_and_action: trajectory, rollout; downranked: driving
- Abstract skim: Recent end-to-end driving systems demonstrate strong performance on closed-loop benchmarks, yet are still predominantly trained on fixed expert-collected data using open-loop imitation learning. This training-inference mismatch leaves the policy vulnerable in policy-induced states, where accumulated errors can lead...

### 29 - Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments

- arXiv: [2608.24099](https://arxiv.org/abs/2608.24099) | [PDF](https://arxiv.org/pdf/2608.24099) | [papers.cool](https://papers.cool/arxiv/2608.24099)
- Authors: Guo Gan, Yilun Zhao, Cong Chen, Jinbiao Wei, Tingyu Song, Zheyuan Yang, et al. (8 authors)
- Published: 2026-08-25 05:57 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations into agent...

### 28 - Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings

- arXiv: [2608.24039](https://arxiv.org/abs/2608.24039) | [PDF](https://arxiv.org/pdf/2608.24039) | [papers.cool](https://papers.cool/arxiv/2608.24039)
- Authors: Muhammad Tayyab Khan, Lequn Chen, Wenhe Feng, Seung Ki Moon
- Published: 2026-08-25 03:57 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Manufacturing process planning transforms heterogeneous design information into coherent manufacturing decisions. However, existing approaches focus on isolated subtasks, such as feature recognition, drawing interpretation, or tool selection, and struggle to support the full reasoning chain from design artifacts to...

### 27 - Selective Regenerative Decoding: Trajectory-Level Intervention for Inference-Time Reasoning

- arXiv: [2608.24338](https://arxiv.org/abs/2608.24338) | [PDF](https://arxiv.org/pdf/2608.24338) | [papers.cool](https://papers.cool/arxiv/2608.24338)
- Authors: Sophia Xiao Pu, Yumo Xu, Sailik Sengupta, Millennium Bismay, Ruixue Lian, James Gung, et al. (8 authors)
- Published: 2026-08-25 10:01 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reward model; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Inference-time decoding methods improve LLM reasoning by exploring multiple candidate trajectories, yet treat each trajectory as atomic: either retaining it whole or discarding it irreversibly. This wastes computation on partially promising candidates whose high-quality prefixes are abandoned alongside degraded...

### 27 - RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards

- arXiv: [2608.24275](https://arxiv.org/abs/2608.24275) | [PDF](https://arxiv.org/pdf/2608.24275) | [papers.cool](https://papers.cool/arxiv/2608.24275)
- Authors: Houcheng Jiang, Boxuan Zhang, Qiyong Zhong, Junfeng Fang, Xiang Wang, Xiangnan He
- Published: 2026-08-25 09:01 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory
- Abstract skim: Safeguarding language model agents requires assessing complete execution trajectories under context-dependent safety policies. Existing policy-aware safeguards mainly rely on prompting or supervised fine-tuning, limiting their ability to adapt to unseen trajectories and changing policy contexts. We propose RePolicy,...

### 27 - Scaling Reinforcement Learning for Diffusion Models via Velocity Matching

- arXiv: [2608.23664](https://arxiv.org/abs/2608.23664) | [PDF](https://arxiv.org/pdf/2608.23664) | [papers.cool](https://papers.cool/arxiv/2608.23664)
- Authors: Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, et al. (7 authors)
- Published: 2026-08-24 17:13 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory
- Abstract skim: Reward fine-tuning is becoming an important tool for adapting diffusion models to human preferences and task-specific objectives, but existing methods largely inherit policy-gradient machinery from large language models. Unlike autoregressive models, diffusion models do not provide tractable likelihoods for...

### 26 - Where Entropy Is Measured Matters: Policy Geometry in Bounded Continuous-Control PPO

- arXiv: [2608.24488](https://arxiv.org/abs/2608.24488) | [PDF](https://arxiv.org/pdf/2608.24488) | [papers.cool](https://papers.cool/arxiv/2608.24488)
- Authors: Yiyang He, Zhichun Zhou, Ziwei Wang, Tao Xue, Haolin Fei
- Published: 2026-08-25 12:36 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Many continuous-control policies are optimized as unbounded Gaussians and then mapped into bounded actions. We show that where entropy is measured changes the policy geometry learned by proximal policy optimization (PPO). In an 80-muscle MyoLeg task, a clipped Gaussian executes 89.07% of actions within 5% of a...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
