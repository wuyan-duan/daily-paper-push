# RL / Post-Training / Agentic RL Reading Queue - 2026-07-13

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 215. Minimum score: 8.

## Top Picks

### 58 - KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling

- arXiv: [2607.09153](https://arxiv.org/abs/2607.09153) | [PDF](https://arxiv.org/pdf/2607.09153) | [papers.cool](https://papers.cool/arxiv/2607.09153)
- Authors: Peng Kuang, Haibo Jin, Xiaoyu Han, Yanli Wang, Xiaopeng Yuan, Ye Yu, et al. (8 authors)
- Published: 2026-07-10 07:16 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reward model; reasoning: process reward; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Process Reward Models (PRMs) have been proven to be highly effective in guiding test-time scaling (TTS) methods, which significantly boost the capabilities of LLM-based multi-agent systems. However, existing PRMs are text-based: they re-encode the entire trajectory text from scratch. In long multi-agent rollouts,...

### 42 - PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers

- arXiv: [2607.09590](https://arxiv.org/abs/2607.09590) | [PDF](https://arxiv.org/pdf/2607.09590) | [papers.cool](https://papers.cool/arxiv/2607.09590)
- Authors: Yujie Pang, Zudong Li
- Published: 2026-07-10 16:42 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; memory_and_benchmarks: memory
- Abstract skim: Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-...

### 41 - Mach-Mind-4-Flash Technical Report

- arXiv: [2607.09375](https://arxiv.org/abs/2607.09375) | [PDF](https://arxiv.org/pdf/2607.09375) | [papers.cool](https://papers.cool/arxiv/2607.09375)
- Authors: Foundation Model Team
- Published: 2026-07-10 12:57 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: We present Mach-Mind-4-Flash, a 35B-parameter Mixture-of-Experts (MoE) agentic model with 3B activated parameters. Through post-training optimization alone without scaling pre-training compute, the model achieves performance on par with or surpassing that of 100B-parameter-class models. By introducing scalable...

### 35 - Learning More from Less: Reinforcement Learning from Hindsight

- arXiv: [2607.09042](https://arxiv.org/abs/2607.09042) | [PDF](https://arxiv.org/pdf/2607.09042) | [papers.cool](https://papers.cool/arxiv/2607.09042)
- Authors: Iris Xu, Sunshine Jiang, John Marangola, Nitish Dashora, Richard Li, Thomas Liu, et al. (11 authors)
- Published: 2026-07-10 02:17 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, but every update consumes robot rollouts that are slow and costly to collect, making sample efficiency a central concern. Manipulation tasks typically provide only sparse rewards, so a weak policy fails almost every...

### 34 - SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions

- arXiv: [2607.08925](https://arxiv.org/abs/2607.08925) | [PDF](https://arxiv.org/pdf/2607.08925) | [papers.cool](https://papers.cool/arxiv/2607.08925)
- Authors: Elham Daneshmand, Majid Khadiv, Glen Berseth, Hsiu-Chin Lin
- Published: 2026-07-09 20:41 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: benchmark
- Abstract skim: Training reinforcement-learning agents directly on physical robots makes every fall costly, since a fall can damage the platform and cannot be undone like a simulator reset; the goal is therefore to minimize falls during training rather than trade them off against return, as constrained Markov decision process (MDP)...

### 32 - Action-Factored Multi-Agent Reinforcement Learning for Scalable Quantum Device Tuning

- arXiv: [2607.09422](https://arxiv.org/abs/2607.09422) | [PDF](https://arxiv.org/pdf/2607.09422) | [papers.cool](https://papers.cool/arxiv/2607.09422)
- Authors: Edwin De Nicolo, Rahul Marchand, Cornelius Carlsson, Pranav Vaidhyanathan, Natalia Ares
- Published: 2026-07-10 13:50 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: quantum
- Abstract skim: Cooperative multi-agent reinforcement learning is well suited to problems with large parameter spaces and exploitable local structure, such as the tuning of electrostatically-defined quantum-dot arrays. However, if parameter cross-talk is strong, a non-stationary environment from the perspective of any individual...

### 32 - L-MAD: A Systematic Evaluation of Multi-Agent Debate Structures in Legal Reasoning

- arXiv: [2607.09099](https://arxiv.org/abs/2607.09099) | [PDF](https://arxiv.org/pdf/2607.09099) | [papers.cool](https://papers.cool/arxiv/2607.09099)
- Authors: Tan-Minh Nguyen, Hoang-Trung Nguyen, Huu-Dong Nguyen, Dinh-Truong Do, Thi-Hai-Yen Vuong, Le-Minh Nguyen
- Published: 2026-07-10 05:08 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, deliberation; memory_and_benchmarks: evaluation
- Abstract skim: While multi-agent debate (MAD) frameworks have shown significant potential in general reasoning, their effectiveness in highly structured, knowledge-heavy legal domains remains under-explored. In this work, we introduce the Legal Multi-Agent Debate (L-MAD) framework to systematically evaluate different debate...

### 31 - Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks

- arXiv: [2607.09330](https://arxiv.org/abs/2607.09330) | [PDF](https://arxiv.org/pdf/2607.09330) | [papers.cool](https://papers.cool/arxiv/2607.09330)
- Authors: Nuocheng Yang, Sihua Wang, Zihan Chen, Tony Q. S. Quek, Changchuan Yin
- Published: 2026-07-10 12:10 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: llm agent; rl_post_training: ppo; reasoning: reasoning
- Abstract skim: Embodied agent teams powered by heterogeneous large language models (LLMs) are being widely deployed in physical artificial intelligence such as smart factories, warehouses, and service robotics. To enable collaboration among such an agent team, efficient coordination mechanisms that operate reliably under limited...

### 31 - LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making

- arXiv: [2607.09322](https://arxiv.org/abs/2607.09322) | [PDF](https://arxiv.org/pdf/2607.09322) | [papers.cool](https://papers.cool/arxiv/2607.09322)
- Authors: Yanzhen Chen, Zihan Xu, Xiaocheng Zhang, Zhiting Fan, Weiqi Zhai, Hongxia Xu, et al. (7 authors)
- Published: 2026-07-10 12:04 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use, agent memory; reasoning: reasoning; planning_and_action: decision making; memory_and_benchmarks: memory, benchmark, evaluation
- Abstract skim: In this work, we introduce LongMedBench, a real-world EHR-based benchmark for long-horizon clinical decision-making. Prior evaluations of LLM-based medical agents have largely emphasized short-context knowledge QA and tool use. However, real-world medical care is inherently longitudinal, and clinicians must...

### 28 - Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning

- arXiv: [2607.09336](https://arxiv.org/abs/2607.09336) | [PDF](https://arxiv.org/pdf/2607.09336) | [papers.cool](https://papers.cool/arxiv/2607.09336)
- Authors: Guanquan Wang, Yoshimasa Tsuruoka
- Published: 2026-07-10 12:17 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, trajectory
- Abstract skim: Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline...

### 25 - Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents

- arXiv: [2607.09195](https://arxiv.org/abs/2607.09195) | [PDF](https://arxiv.org/pdf/2607.09195) | [papers.cool](https://papers.cool/arxiv/2607.09195)
- Authors: Izumi Takahara, Teruyasu Mizoguchi
- Published: 2026-07-10 08:39 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use, agent harness; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: evaluation
- Abstract skim: Large language model (LLM) agents are increasingly expected to play a central role in AI-driven scientific discovery. Equipped with broad knowledge, flexible reasoning, and tool use, they have the potential to autonomously explore and solve scientific problems by repeatedly proposing hypotheses, testing them, and...

### 24 - Mosaic: Runtime-Efficient Multi-Agent Embodied Planning

- arXiv: [2607.09603](https://arxiv.org/abs/2607.09603) | [PDF](https://arxiv.org/pdf/2607.09603) | [papers.cool](https://papers.cool/arxiv/2607.09603)
- Authors: Kunjal Panchal, Saayan Mitra, Sunav Choudhary, Victor Bursztyn, Somdeb Sarkhel, Hui Guan
- Published: 2026-07-10 16:57 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; planning_and_action: planning; memory_and_benchmarks: memory
- Abstract skim: LLM-based multi-agent embodied planning remains impractical due to prohibitively high execution latency. We identify failed actions as the dominant bottleneck, stemming from two core challenges: inaccurate state tracking under partial observability and inefficient coordination that produces redundant or conflicting...

### 24 - Multimodal Reward Hacking in Reinforcement Learning

- arXiv: [2607.09492](https://arxiv.org/abs/2607.09492) | [PDF](https://arxiv.org/pdf/2607.09492) | [papers.cool](https://papers.cool/arxiv/2607.09492)
- Authors: Jiayu Yao, Yiwei Wang, Anmeng Zhang, Zhe Sun, Songsong Wang, Lingrui Mei, et al. (8 authors)
- Published: 2026-07-10 15:06 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, grpo
- Abstract skim: Reinforcement learning (RL) is increasingly used to align multimodal large language models (MLLMs), but higher rewards do not always imply better task performance. This risk is amplified when visual evidence is evaluated by text-only or weakly grounded rewards. We study reward hacking in MLLM RL across safety VQA,...

### 22 - AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs

- arXiv: [2607.09092](https://arxiv.org/abs/2607.09092) | [PDF](https://arxiv.org/pdf/2607.09092) | [papers.cool](https://papers.cool/arxiv/2607.09092)
- Authors: Yumin Heo, Hyeon-gu Lee, Sumin Seo, Youngjoong Ko
- Published: 2026-07-10 04:22 UTC | Categories: cs.CL
- Why it matched: rl_post_training: grpo; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: Knowledge graphs (KGs) are often automatically constructed from large-scale corpora, but they inevitably contain factual errors due to noisy sources and extraction failures, and verifying them reliably at industrial scale remains a critical challenge. To address this, we propose AgentKGV, the Agentic LLM-RAG...

### 22 - Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution

- arXiv: [2607.08960](https://arxiv.org/abs/2607.08960) | [PDF](https://arxiv.org/pdf/2607.08960) | [papers.cool](https://papers.cool/arxiv/2607.08960)
- Authors: Ning Liu, Kalle Kujanpää, Zhaoxuan Zhu, P Aditya Sreekar, Kaiwen Liu, Chuanneng Sun, et al. (14 authors)
- Published: 2026-07-09 21:51 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: memory, benchmark
- Abstract skim: Warehouse operations are governed by Standard Operating Procedures (SOPs) that encode complex, multi-system decision logic, which must be executed reliably under strict time constraints, yet LLM agents lack mechanisms to enforce procedural compliance and degrade under the context overload full SOP specifications...

### 20 - Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation

- arXiv: [2607.09600](https://arxiv.org/abs/2607.09600) | [PDF](https://arxiv.org/pdf/2607.09600) | [papers.cool](https://papers.cool/arxiv/2607.09600)
- Authors: Kaiji Zhou, Ales Leonardis, Yue Feng
- Published: 2026-07-10 16:54 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: llm agent; reasoning: reasoning
- Abstract skim: Enhancing the reasoning capabilities of large language model (LLM) agents requires effective orchestration of diverse expert models and tools. However, existing frameworks typically call APIs based on coarse-grained matching between tasks and the functions of expert models or tools, while overlooking critical...

### 20 - FreyaTTS Technical Report

- arXiv: [2607.09530](https://arxiv.org/abs/2607.09530) | [PDF](https://arxiv.org/pdf/2607.09530) | [papers.cool](https://papers.cool/arxiv/2607.09530)
- Authors: Ahmet Erdem Pamuk, Ömer Yentür, Ahmet Tunga Bayrak, Yavuz Alp Sencer Öztürk, Mustafa Yavuz
- Published: 2026-07-10 15:36 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: We introduce Freya-TTS, a compact, tokenizer-free, Turkish-first text-to-speech model designed for highly reliable and efficient conversational synthesis. Freya-TTS is a 183.2M-parameter non-autoregressive conditional flow-matching Diffusion Transformer (DiT) that operates in the frozen continuous latent space of...

### 20 - ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning

- arXiv: [2607.09059](https://arxiv.org/abs/2607.09059) | [PDF](https://arxiv.org/pdf/2607.09059) | [papers.cool](https://papers.cool/arxiv/2607.09059)
- Authors: Kunbo Zhang, Lei Fu, Zeyu Wang, Zijing Liu, Kejian Tong
- Published: 2026-07-10 03:03 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning
- Abstract skim: We present ARCANA, a collaborative multi agent framework for solving ARC AGI 2 tasks under strict test time and hardware constraints. ARCANA decomposes each task into iterative perception, hypothesis generation, symbolic execution, and reflective refinement. A perceptual grounding agent builds object centric scene...

### 19 - CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding

- arXiv: [2607.08974](https://arxiv.org/abs/2607.08974) | [PDF](https://arxiv.org/pdf/2607.08974) | [papers.cool](https://papers.cool/arxiv/2607.08974)
- Authors: Yuri Ishitoya, Jeremy Siburian, Masashi Hamaya, Kuniaki Saito, Cristian C. Beltran-Hernandez, Mai Nishimura
- Published: 2026-07-09 22:34 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training; planning_and_action: action sequence
- Abstract skim: Vision-language-action models (VLAs) inherit semantic capabilities from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained VLMs...

### 18 - Shared Selective Persistent Memory for Agentic LLM Systems

- arXiv: [2607.09493](https://arxiv.org/abs/2607.09493) | [PDF](https://arxiv.org/pdf/2607.09493) | [papers.cool](https://papers.cool/arxiv/2607.09493)
- Authors: Sanjana Pedada, Aditya Dhavala, Neelraj Patil
- Published: 2026-07-10 15:07 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: tool use; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation histories...

### 18 - GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning

- arXiv: [2607.08894](https://arxiv.org/abs/2607.08894) | [PDF](https://arxiv.org/pdf/2607.08894) | [papers.cool](https://papers.cool/arxiv/2607.08894)
- Authors: Maureese Williams, Dymitr Nowicki
- Published: 2026-07-09 19:34 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: language agent; planning_and_action: planning, world model
- Abstract skim: Large Language Model (LLM) agents have shown promise in multi-step planning tasks, but existing approaches like LATS (Language Agent Tree Search) and ReAct rely heavily on LLM inference during planning, leading to high computational costs and stochastic behavior. We present \textbf{GATS} (Graph-Augmented Tree...

### 17 - Toward Active Object Detection for UAVs in the Wild: A Large-Scale Dataset, Benchmark and Method

- arXiv: [2607.09078](https://arxiv.org/abs/2607.09078) | [PDF](https://arxiv.org/pdf/2607.09078) | [papers.cool](https://papers.cool/arxiv/2607.09078)
- Authors: Tianpeng Liu, Xinhua Jiang, Li Liu, Qinmu Shen, Siwei Tang, Zhen Liu, et al. (7 authors)
- Published: 2026-07-10 03:49 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: world model; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Object detection is a fundamental component in numerous Unmanned Aerial Vehicle (UAV) applications, yet it has long been plagued by hindrances like occlusion or target pixel scarcity. Active Object Detection (AOD) provides a novel paradigm to address these challenges via active vision, while UAV-based AOD research...

### 16 - Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for Financial Anomaly Detection

- arXiv: [2607.09641](https://arxiv.org/abs/2607.09641) | [PDF](https://arxiv.org/pdf/2607.09641) | [papers.cool](https://papers.cool/arxiv/2607.09641)
- Authors: Cláudio Lúcio do Val Lopes, Lucca Machado da Silva
- Published: 2026-07-10 17:39 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning
- Abstract skim: Financial anomaly detection suffers from extreme class imbalance, causing traditional single-objective algorithms to exhibit ``fraud collapse'', defaulting to the majority class and failing to balance anomaly interdiction with customer friction. To overcome this without distortive data resampling, we propose the...

### 16 - MultiView-Bench: A Diagnostic Benchmark for World-Centric Multi-View Integration in VLMs

- arXiv: [2607.08970](https://arxiv.org/abs/2607.08970) | [PDF](https://arxiv.org/pdf/2607.08970) | [papers.cool](https://papers.cool/arxiv/2607.08970)
- Authors: Hantao Zhang, Jinru Sui, Ed Li, Dirk Bergemann, Zhuoran Yang
- Published: 2026-07-09 22:22 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Recent benchmarks for VLMs largely assess single- or limited-view perception, leaving untested the core cognitive ability to integrate observations across viewpoints into a coherent, world-centric (allocentric) 3D mental model. We introduce MultiView-Bench, a diagnostic benchmark expressly designed to evaluate...

### 16 - EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins

- arXiv: [2607.08793](https://arxiv.org/abs/2607.08793) | [PDF](https://arxiv.org/pdf/2607.08793) | [papers.cool](https://papers.cool/arxiv/2607.08793)
- Authors: Joshua Pickard, Wei Qi, Na Li, Ann Woolley, Lisa Cosimi, Roy Kishony, et al. (7 authors)
- Published: 2026-07-07 19:24 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, decision making; memory_and_benchmarks: evaluation
- Abstract skim: Sepsis is a leading cause of mortality, yet optimal treatment policies remain contested. Existing reinforcement learning (RL) approaches learn fixed strategies for sepsis treatment, limiting adaptability to changing clinical objectives during inference. We propose EHRMPC, a framework that decouples learning patient...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
