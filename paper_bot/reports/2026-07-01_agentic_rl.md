# RL / Post-Training / Agentic RL Reading Queue - 2026-07-01

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 405. Minimum score: 8.

## Top Picks

### 62 - Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models

- arXiv: [2606.31846](https://arxiv.org/abs/2606.31846) | [PDF](https://arxiv.org/pdf/2606.31846) | [papers.cool](https://papers.cool/arxiv/2606.31846)
- Authors: Lang Cao, Renhong Chen, Luyi Li, Peng Wang, Mofan Peng, Yitong Li
- Published: 2026-06-30 15:46 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; planning_and_action: trajectory, rollout
- Abstract skim: Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides...

### 61 - Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning

- arXiv: [2606.31825](https://arxiv.org/abs/2606.31825) | [PDF](https://arxiv.org/pdf/2606.31825) | [papers.cool](https://papers.cool/arxiv/2606.31825)
- Authors: Junha Jung, Minbyul Jeong, Suhyeon Lim, Sungwook Jung, Jaehoon Yun, Taeyun Roh, et al. (8 authors)
- Published: 2026-06-30 15:35 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more; reasoning: reasoning
- Abstract skim: Recent multimodal large language models have shown great promise in clinical image reasoning, but existing post-training pipelines remain predominantly outcome-centric, relying on final answer correctness or sequence-level preferences. This suffers from sparse credit assignment, making it difficult to optimize the...

### 59 - TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

- arXiv: [2606.32017](https://arxiv.org/abs/2606.32017) | [PDF](https://arxiv.org/pdf/2606.32017) | [papers.cool](https://papers.cool/arxiv/2606.32017)
- Authors: Yuanda Xu, Zhengze Zhou, Hejian Sang, Xiaomin Li, Jiaxin Zhang, Xinchen Du, et al. (8 authors)
- Published: 2026-06-30 17:48 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, grpo; reasoning: process reward; memory_and_benchmarks: alfworld
- Abstract skim: Agentic reinforcement learning requires assigning credit to environment-facing actions such as searches, clicks, edits, navigation commands, and object interactions. Standard GRPO uses the final verifier outcome as a uniform advantage over all action tokens. This outcome signal is useful but structurally incomplete:...

### 49 - Which Tokens Matter? Adaptive Token Selection for RLVR with the Relative Surprisal Index

- arXiv: [2606.31575](https://arxiv.org/abs/2606.31575) | [PDF](https://arxiv.org/pdf/2606.31575) | [papers.cool](https://papers.cool/arxiv/2606.31575)
- Authors: Outongyi Lv, Yanzhao Zheng, Yuanwei Zhang, Zhenghao Huang, Xingjun Wang, Baohua Dong, et al. (8 authors)
- Published: 2026-06-30 12:33 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, grpo; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL) has become a powerful tool for propelling Large Language Models (LLMs) beyond imitation-based training towards more robust reasoning capabilities. Among existing approaches, RL with Verifiable Rewards (RLVR) has emerged as a pivotal paradigm for advancing LLM reasoning. Despite its...

### 44 - Xiaomi-GUI-0 Technical Report

- arXiv: [2606.31410](https://arxiv.org/abs/2606.31410) | [PDF](https://arxiv.org/pdf/2606.31410) | [papers.cool](https://papers.cool/arxiv/2606.31410)
- Authors: Wanxia Cao, Chengzhen Duan, Pei Fu, Pengzhi Gao, Niu Lian, Fazhan Liu, et al. (30 authors)
- Published: 2026-06-30 09:36 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; reasoning: reflection; planning_and_action: rollout; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: Graphical user interface (GUI) agents build on vision-language models to complete user tasks end-to-end in real applications through interface actions such as tapping, swiping, text entry, and navigation. However, existing GUI agents are trained and evaluated largely on offline trajectories, simulated environments,...

### 44 - HyPOLE: Hyperproperty-Guided Multi-Agent Reinforcement Learning under Partial Observation

- arXiv: [2606.30966](https://arxiv.org/abs/2606.30966) | [PDF](https://arxiv.org/pdf/2606.30966) | [papers.cool](https://papers.cool/arxiv/2606.30966)
- Authors: Arshia Rafieioskouei, Tzu-Han Hsu, Matthew Lucas, Borzoo Bonakdarpour
- Published: 2026-06-29 23:03 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Formal specification is a powerful tool to guide the learning process and provides significant advantages over reward shaping: (1) mathematical rigor; (2) expressiveness to specify objectives and constraints, and (3) the ability to define tactics to achieve objectives. However, these benefits remain largely...

### 44 - Predictable GRPO: A Closed-Form Model of Training Dynamics

- arXiv: [2606.30789](https://arxiv.org/abs/2606.30789) | [PDF](https://arxiv.org/pdf/2606.30789) | [papers.cool](https://papers.cool/arxiv/2606.30789)
- Authors: Rajat Ghosh, Datta Nimmaturi, Aryan Singhal, Vaishnavi Bhargava, Henry Wong, Johnu George, et al. (7 authors)
- Published: 2026-06-29 18:19 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Group Relative Policy Optimization (GRPO) has become a standard tool for improving the reasoning ability of large language models, yet its training dynamics are still described empirically: reward trajectories are fit with low-parameter functional forms whose constants carry no mechanistic meaning, and...

### 42 - ReGRPO: Reflection-Augmented Policy Optimization for Tool-Using Agents

- arXiv: [2606.31392](https://arxiv.org/abs/2606.31392) | [PDF](https://arxiv.org/pdf/2606.31392) | [papers.cool](https://papers.cool/arxiv/2606.31392)
- Authors: Binjie Zhang, Mike Zheng Shou
- Published: 2026-06-30 09:19 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization; reasoning: reflection; planning_and_action: trajectory; memory_and_benchmarks: gaia
- Abstract skim: Tool-augmented vision-language models (VLMs) can solve multimodal, multi-step tasks by calling external tools, yet they remain fragile in practice. Existing works have two common gaps. Supervised fine-tuning (SFT) is built mostly on successful trajectories and offers little signal for recovery after tool failures,...

### 39 - ECHO: Prune to act, trace to learn with selective turn memory in agentic RL

- arXiv: [2606.31650](https://arxiv.org/abs/2606.31650) | [PDF](https://arxiv.org/pdf/2606.31650) | [papers.cool](https://papers.cool/arxiv/2606.31650)
- Authors: Zijun Xie, Binbin Zheng, Enlei Gong, Jihua Liu, Yuyang You, Lingfeng Liu, et al. (10 authors)
- Published: 2026-06-30 13:29 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: grpo; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Long-horizon language agents must repeatedly interact with tools, accumulate evidence, and make decisions under bounded context windows. Existing context-management methods make such rollouts feasible by truncating distant history, folding past turns into summaries, or selecting compact memory states. However, these...

### 38 - A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems

- arXiv: [2606.31639](https://arxiv.org/abs/2606.31639) | [PDF](https://arxiv.org/pdf/2606.31639) | [papers.cool](https://papers.cool/arxiv/2606.31639)
- Authors: Seyed Bagher Hashemi Natanzi, Bo Tang
- Published: 2026-06-30 13:21 UTC | Categories: cs.AI
- Why it matched: agentic_rl: long-horizon agent; rl_post_training: post-training, post training; memory_and_benchmarks: memory, evaluation
- Abstract skim: Large language models are no longer only text generators. They are increasingly embedded in retrieval pipelines, enterprise assistants, coding environments, robotic systems, security-operation workflows, and autonomous agents that can read private data, call tools, write files, execute code, and act across...

### 37 - Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents

- arXiv: [2606.31648](https://arxiv.org/abs/2606.31648) | [PDF](https://arxiv.org/pdf/2606.31648) | [papers.cool](https://papers.cool/arxiv/2606.31648)
- Authors: Utsav Garg, Sungjin Hong, Jason Jung, Justin Lee, Shaan Desai, Joon Hee Kim, et al. (9 authors)
- Published: 2026-06-30 13:29 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: We present LuckyStar 111B, a 111B-parameter hybrid reasoning model developed through a collaboration between Cohere and LG CNS for Korean-English enterprise agents under practical memory and serving constraints. The model trains from Cohere's fully post-trained Command A model rather than a new pretraining run, and...

### 36 - Smart charging of large fleets of Electric Vehicles: Independent Multi-Agent Reinforcement Learning approaches

- arXiv: [2606.31347](https://arxiv.org/abs/2606.31347) | [PDF](https://arxiv.org/pdf/2606.31347) | [papers.cool](https://papers.cool/arxiv/2606.31347)
- Authors: Xavier Rate, Eloann Le Guern, Raphaël Féraud, Fatma Salem, Melissa Chiknoun, Eymeric Giabicani, et al. (11 authors)
- Published: 2026-06-30 08:43 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: The electrification of transportation through electric vehicles introduces new challenges for power grid management, such as increased peak demand, voltage fluctuations, line overloads, and the integration of variable renewable energy sources. To enable efficient integration of EVs while minimizing costs for users...

### 33 - Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR

- arXiv: [2606.31813](https://arxiv.org/abs/2606.31813) | [PDF](https://arxiv.org/pdf/2606.31813) | [papers.cool](https://papers.cool/arxiv/2606.31813)
- Authors: Ruijia Zhang, Jiacheng Zhu, Hanqing Zhu, Laixi Shi
- Published: 2026-06-30 15:27 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Low-rank adaptation (LoRA) and its variants enable parameter-efficient fine-tuning of large language models under the supervised fine-tuning (SFT) paradigm. However, their efficacy and behavior under Reinforcement learning with verifiable rewards (RLVR) are less well understood. In particular, two structurally...

### 32 - Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning

- arXiv: [2606.31599](https://arxiv.org/abs/2606.31599) | [PDF](https://arxiv.org/pdf/2606.31599) | [papers.cool](https://papers.cool/arxiv/2606.31599)
- Authors: Kaitao Chen, Weiqian Zhao, Jiamin Wu, Qihao Zheng, Shangquan Sun, Chunfeng Song, et al. (9 authors)
- Published: 2026-06-30 12:47 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: decision making
- Abstract skim: Vision-language models (VLMs) combining reinforcement learning (RL) ignite remarkable progress in multimodal reasoning, yet still struggle with medical images, which typically exhibit extremely sparse visual evidence to inform clinical decision-making. We recognize that pruning visual tokens outside the grounding...

### 30 - Investigating Multi-Agent Deliberation in Law

- arXiv: [2606.30906](https://arxiv.org/abs/2606.30906) | [PDF](https://arxiv.org/pdf/2606.30906) | [papers.cool](https://papers.cool/arxiv/2606.30906)
- Authors: Cor Steging, Ludi van Leeuwen, Tadeusz Zbiegień
- Published: 2026-06-29 20:56 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, deliberation; memory_and_benchmarks: evaluation
- Abstract skim: Artificial Intelligence is increasingly applied to the field of law, and has the potential to increase access to justice. One particular movement that is gaining traction is that of agentic AI, wherein AI agents, based on Large Language Models (LLMs) can take autonomous actions. In particular, multi-agent approaches...

### 30 - Sampling-Based Coordination-Informed Multi-Objective Multi-Robot Reinforcement Learning

- arXiv: [2606.30893](https://arxiv.org/abs/2606.30893) | [PDF](https://arxiv.org/pdf/2606.30893) | [papers.cool](https://papers.cool/arxiv/2606.30893)
- Authors: Antonio Marino, Esteban Restrepo, Soon-jo Chung, Paolo Robuffo Giordano, Claudio Pacchierotti
- Published: 2026-06-29 20:31 UTC | Categories: cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Multi-robot systems must simultaneously optimize competing objectives while maintaining coordinated behavior. Existing multi-agent reinforcement learning approaches often rely on fixed or centralized coordination, which limits adaptability and violates distributed constraints. This work introduces the Coordination-...

### 29 - DSIP: A Dynamic Coordination Planner for Signal-Free Intersections using Diffusion-Model-Based Multi-Agent Motion Planning

- arXiv: [2606.30694](https://arxiv.org/abs/2606.30694) | [PDF](https://arxiv.org/pdf/2606.30694) | [papers.cool](https://papers.cool/arxiv/2606.30694)
- Authors: Qian Hu, Haoyang Peng, Songan Zhang, Ming Yang, Hongtei Eric Tseng
- Published: 2026-06-29 01:35 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: planning, trajectory; downranked: traffic signal, traffic
- Abstract skim: Traffic signal control at urban intersections inherently introduces stop-and-go behavior, resulting in increased delays and reduced traffic efficiency, especially under high traffic demand. With the emergence of connected and automated vehicles (CAVs), trajectory-level coordination has emerged as a high-potential...

### 28 - Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

- arXiv: [2606.31700](https://arxiv.org/abs/2606.31700) | [PDF](https://arxiv.org/pdf/2606.31700) | [papers.cool](https://papers.cool/arxiv/2606.31700)
- Authors: Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, Sebastian Risi, David Ha, Robert Tjarko Lange
- Published: 2026-06-30 14:09 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically...

### 25 - Addressing Over-Refusal in LLMs with Competing Rewards

- arXiv: [2606.31748](https://arxiv.org/abs/2606.31748) | [PDF](https://arxiv.org/pdf/2606.31748) | [papers.cool](https://papers.cool/arxiv/2606.31748)
- Authors: Taeyoun Kim, Aviral Kumar
- Published: 2026-06-30 14:38 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Safety training on language models often induces over-refusal: improved safety on harmful prompts at the cost of increased refusal on harmless ones. Though this trade-off can be mitigated by training models with reinforcement learning (RL) to reason before answering, it does not remove the underlying problem that...

### 25 - Gradient Smoothing: Coupling Layer-wise Updates for Improved Optimization

- arXiv: [2606.30813](https://arxiv.org/abs/2606.30813) | [PDF](https://arxiv.org/pdf/2606.30813) | [papers.cool](https://papers.cool/arxiv/2606.30813)
- Authors: Haoming Meng, Anton Sugolov, Vardan Papyan
- Published: 2026-06-29 18:37 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Deep neural networks with repeated architectural blocks, such as transformers, often exhibit structured relationships across layers that emerge during training. Motivated by this observation, we introduce \emph{Depth-wise Gradient Augmentation}, a general optimization paradigm in which the update applied to each...

### 25 - From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators

- arXiv: [2606.30704](https://arxiv.org/abs/2606.30704) | [PDF](https://arxiv.org/pdf/2606.30704) | [papers.cool](https://papers.cool/arxiv/2606.30704)
- Authors: Gan Luo, Zihan Qin, Bin Dong, Wotao Yin
- Published: 2026-06-29 14:17 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Large language models (LLMs) excel across a wide range of tasks, yet their instance-specific solutions often lack the structural consistency needed for reliable deployment. Workflows that encode recurring algorithmic patterns at the task level provide a principled framework, offering robustness across instance...

### 24 - Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs

- arXiv: [2606.32032](https://arxiv.org/abs/2606.32032) | [PDF](https://arxiv.org/pdf/2606.32032) | [papers.cool](https://papers.cool/arxiv/2606.32032)
- Authors: Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona, Idan Szpektor, Arman Cohan
- Published: 2026-06-30 17:56 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, preference optimization
- Abstract skim: Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal...

### 24 - CSO-LLM: Class Subspace Orthogonalization for Post-Training Backdoor Detection and Trigger Inversion in LLMs

- arXiv: [2606.31309](https://arxiv.org/abs/2606.31309) | [PDF](https://arxiv.org/pdf/2606.31309) | [papers.cool](https://papers.cool/arxiv/2606.31309)
- Authors: Zhengxing Li, David J. Miller, Guangmingmei Yang, George Kesidis
- Published: 2026-06-30 08:19 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training
- Abstract skim: While post-training backdoor detection and trigger inversion schemes have been developed for AIs used e.g. for images, there is a paucity of such methods for LLMs. First, the LLM input space is discrete, with up to 150,000^k k-tuples to consider with k the token-length of a putative trigger. Second, one must...

### 24 - Plan Right, Then Plan Tight: Symbolic RL for Efficient Embodied Reasoning

- arXiv: [2606.31260](https://arxiv.org/abs/2606.31260) | [PDF](https://arxiv.org/pdf/2606.31260) | [papers.cool](https://papers.cool/arxiv/2606.31260)
- Authors: Xiangli Shi, Xiaomeng Zhu, Ye Tian, Yuchun Guo, Ziyang Sun, Lujie Yin, et al. (8 authors)
- Published: 2026-06-30 07:37 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning
- Abstract skim: Embodied task planning asks an agent to turn a natural-language instruction into an executable sequence of actions in a physical scene, and is a building block for household, assistive, and service robots. Recent prompting-based and reinforcement-learning planners generate fluent action text but lack a cheap...

### 24 - Learning Where to Look: A Reinforcement Learning Framework for Robust Micro-Ultrasound Prostate Cancer Detection

- arXiv: [2606.30951](https://arxiv.org/abs/2606.30951) | [PDF](https://arxiv.org/pdf/2606.30951) | [papers.cool](https://papers.cool/arxiv/2606.30951)
- Authors: Mohammad Mahdi Abootorabi, Sina Namazi, Armin Saadat, Lyuyang Wang, Obed Dzikunu, Paul F. R. Wilson, et al. (10 authors)
- Published: 2026-06-29 22:07 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization
- Abstract skim: Micro-ultrasound ($μ$US) is a new, emerging, and promising imaging modality for prostate cancer (PCa) detection, but accurate identification of suspicious tissue remains highly dependent on clinical experience, leading to substantial inter-observer variability. Machine-learning assistance can reduce this...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
