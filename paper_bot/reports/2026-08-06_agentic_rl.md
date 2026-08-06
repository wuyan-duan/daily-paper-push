# RL / Post-Training / Agentic RL Reading Queue - 2026-08-06

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 350. Minimum score: 8.

## Top Picks

### 65 - Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO

- arXiv: [2608.04698](https://arxiv.org/abs/2608.04698) | [PDF](https://arxiv.org/pdf/2608.04698) | [papers.cool](https://papers.cool/arxiv/2608.04698)
- Authors: Xuzheng Yang, Jun Ling, Tao Huang, Caiyan Qin, Peng Wang
- Published: 2026-08-05 11:07 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; reasoning: reasoning
- Abstract skim: We tackle the challenging yet underexplored task of Generalized Referring Expression Comprehension (GREC), which requires a model to localize the object described by a textual expression when it exists (positive sample) and to refuse output when it does not (negative sample). Although Multimodal Large Language...

### 58 - SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement Learning Rollouts

- arXiv: [2608.04962](https://arxiv.org/abs/2608.04962) | [PDF](https://arxiv.org/pdf/2608.04962) | [papers.cool](https://papers.cool/arxiv/2608.04962)
- Authors: Nhat Minh Pham, Duy Tung Doan, Thi Duyen Ngo, Vinh Van Nguyen, Khac-Hoai Nam Bui
- Published: 2026-08-05 15:32 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Reinforcement learning (RL) post-training improves the reasoning capabilities of large language models, but autoregressive rollout generation remains a major efficiency bottleneck. Speculative decoding can accelerate generation, yet applying it during RL is difficult because the target policy continually evolves:...

### 56 - Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation

- arXiv: [2608.04788](https://arxiv.org/abs/2608.04788) | [PDF](https://arxiv.org/pdf/2608.04788) | [papers.cool](https://papers.cool/arxiv/2608.04788)
- Authors: Yi Yang, Cong Qin, Xiaodan Liu, Chishui Chen, Qing Dong, Yan Zhang, et al. (11 authors)
- Published: 2026-08-05 12:52 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory, environment feedback; memory_and_benchmarks: alfworld
- Abstract skim: Large language model agents are commonly trained through reinforcement learning with sparse trajectory-level rewards, which offer limited guidance on how strongly individual tokens should be updated. On-Policy Self-Distillation (OPSD) addresses this by re-scoring generated tokens under a privileged replay view to...

### 53 - Trident : How to Break Deep Reinforcement Learning Cyber Defenses (Agentic)

- arXiv: [2608.04317](https://arxiv.org/abs/2608.04317) | [PDF](https://arxiv.org/pdf/2608.04317) | [papers.cool](https://papers.cool/arxiv/2608.04317)
- Authors: Ryozo Masukawa, Ian Bryant, Armita Kazeminajafabadi, Sanggeon Yun, Hyunwoo Oh, SungHeon Jeong, et al. (9 authors)
- Published: 2026-08-05 00:54 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Autonomous cyber defense systems based on Deep Reinforcement Learning (DRL) have attracted significant research attention, yet remain evaluated almost exclusively against static, heuristic red agents, leaving their robustness against adaptive threats critically understudied. Meanwhile, recent advances in...

### 50 - Calibrating Artificial Guilt: Neurally Grounded Reward Shaping for Prosocial Multi-Agent Reinforcement Learning

- arXiv: [2608.04663](https://arxiv.org/abs/2608.04663) | [PDF](https://arxiv.org/pdf/2608.04663) | [papers.cool](https://papers.cool/arxiv/2608.04663)
- Authors: Aaditya Mehta, Arya Shah
- Published: 2026-08-05 10:21 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: evaluation
- Abstract skim: Cooperative multi-agent reinforcement learning often adds social terms to individual rewards, yet the scale of those terms is usually chosen by hand. We ask whether a guilt signal can instead be calibrated from human neural and behavioural data and transferred to artificial agents. Using the public SoDec...

### 41 - Structured LLM Reasoning for Zero-Shot Human--Robot Coordination Under Hidden Goals

- arXiv: [2608.04309](https://arxiv.org/abs/2608.04309) | [PDF](https://arxiv.org/pdf/2608.04309) | [papers.cool](https://papers.cool/arxiv/2608.04309)
- Authors: Dong Hae Mangalindan, Anand Gokhale, Francesco Bullo, Vaibhav Srivastava
- Published: 2026-08-05 00:40 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning, decision making
- Abstract skim: We present a structured large-language-model (LLM) architecture for zero-shot human--robot coordination in a cooperative construction task with private goal views. Guided by a Dec-POMDP formulation, the architecture decomposes decision-making into (i) action-conditioned Theory-of-Mind (ToM) inference, (ii)...

### 37 - WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models

- arXiv: [2608.04964](https://arxiv.org/abs/2608.04964) | [PDF](https://arxiv.org/pdf/2608.04964) | [papers.cool](https://papers.cool/arxiv/2608.04964)
- Authors: Bohai Gu, Yueyang Yuan, Taiyi Wu, Dazhao Du, Jian Liu, Xiaoyi Pang, et al. (12 authors)
- Published: 2026-08-05 15:34 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Interactive video world models are essential for long-horizon planning and exploration, yet they suffer from compounding errors. Post-training methods such as reinforcement learning (RL) can improve these models, but they hit a verification bottleneck: for arbitrary action sequences, no ground-truth future state...

### 37 - Privileged, but Biased: How PI-Conditioned Teachers Break Self-Distillation

- arXiv: [2608.04794](https://arxiv.org/abs/2608.04794) | [PDF](https://arxiv.org/pdf/2608.04794) | [papers.cool](https://papers.cool/arxiv/2608.04794)
- Authors: Sarthak Harne, Chinmay Karkar, Yash Pandya, Ahmed Awadallah, Akshay Nambi
- Published: 2026-08-05 12:59 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Self-distillation (SD) has emerged as a compute-efficient alternative to reinforcement learning with verifiable rewards: a self-teacher, conditioned on privileged information (PI) about the answer such as a reference solution, supplies dense per-token supervision to a student that never sees it. Reported gains,...

### 36 - Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems

- arXiv: [2608.04746](https://arxiv.org/abs/2608.04746) | [PDF](https://arxiv.org/pdf/2608.04746) | [papers.cool](https://papers.cool/arxiv/2608.04746)
- Authors: Kartikey Singh Bhandari, Aarya Wadhwani, Dhruv Kumar, Pratik Narang
- Published: 2026-08-05 12:12 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent, agent memory; reasoning: reasoning; memory_and_benchmarks: memory, episodic memory, benchmark
- Abstract skim: LLM agents that persist across sessions accumulate stored memories whose validity varies enormously by content type, yet existing memory architectures treat all memories as equally persistent and systematically contaminate retrieved context with outdated facts. We show that per-memory, type-conditioned temporal...

### 36 - Joint UAV Flight and Opportunistic Routing under Reinforcement Learning for Delay-Tolerant Networks

- arXiv: [2608.04590](https://arxiv.org/abs/2608.04590) | [PDF](https://arxiv.org/pdf/2608.04590) | [papers.cool](https://papers.cool/arxiv/2608.04590)
- Authors: Xiao Wang, Shun-Ren Yang
- Published: 2026-08-05 08:51 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; downranked: traffic
- Abstract skim: The growing deployment of delay-tolerant networks (DTNs) has made store-carry-forward (SCF) communication indispensable under sparse connectivity. However, intermittent contacts, finite buffers, and limited message time-to-live (TTL) often give rise to sparse delivery and congestion, leading to substantial end-to-...

### 36 - Learning Sexism Detection Using Multi-Agent Perspectivist Preference Optimization

- arXiv: [2608.04056](https://arxiv.org/abs/2608.04056) | [PDF](https://arxiv.org/pdf/2608.04056) | [papers.cool](https://papers.cool/arxiv/2608.04056)
- Authors: Hadi Mohammadi, Tina Shahedi, Robert A. Bagheri, Mehdi Dastani, Masoume M. Raeissi
- Published: 2026-08-04 11:35 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: preference optimization
- Abstract skim: When people label text for sexism, they often disagree, and not because some of them are wrong: they genuinely perceive sexism differently. Most NLP systems discard this disagreement by collapsing it into a majority vote. We propose the Multi-Agent Perspectivist Preference Optimization (MAP-PO) framework to keep...

### 33 - Optimizing What Policies Learn From: Recoverability-aware Rollout Intervention Learning

- arXiv: [2608.05080](https://arxiv.org/abs/2608.05080) | [PDF](https://arxiv.org/pdf/2608.05080) | [papers.cool](https://papers.cool/arxiv/2608.05080)
- Authors: Zheyuan Zhang, Manqing Mao, Hong Wang, Zhuoer Wang, Samson Koelle, Jie Yuan, et al. (11 authors)
- Published: 2026-08-05 17:22 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: trajectory, rollout
- Abstract skim: Critic-free group-based reinforcement learning has become a scalable approach for post-training large language models. However, most existing methods allocate the same number of rollouts to every task and trajectory state, even though some rollouts provide much more useful learning signals than others. Recent work...

### 32 - MCHA: A Memory-Centric Hierarchical Architecture for Parallel-Sequential Computing

- arXiv: [2608.04443](https://arxiv.org/abs/2608.04443) | [PDF](https://arxiv.org/pdf/2608.04443) | [papers.cool](https://papers.cool/arxiv/2608.04443)
- Authors: Daijing Shi, Hongxiao Zhao, Yihan Fu, Zhan Chen, Jiayi Li, Yihang Zhu, et al. (10 authors)
- Published: 2026-08-05 04:41 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: memory, benchmark
- Abstract skim: Emerging workloads, such as Multi-Agent Reinforcement Learning (MARL), large-scale neuromorphic computing, and probabilistic graphical models, intrinsically exhibit parallel-sequential computing patterns. While these tasks demand massive parallelism to achieve high throughput, they are severely bottlenecked by...

### 30 - Spoken Function Calling: A New Perspective on Spoken Language Understanding for Large Audio Language Models

- arXiv: [2608.05126](https://arxiv.org/abs/2608.05126) | [PDF](https://arxiv.org/pdf/2608.05126) | [papers.cool](https://papers.cool/arxiv/2608.05126)
- Authors: Yuezhang Peng, Yuxin Liu, Changfeng Gao, Zhifu Gao, Xiangang Li, Xie Chen
- Published: 2026-08-05 17:50 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training
- Abstract skim: Spoken Language Understanding (SLU) is the core component of task-oriented dialogue systems and a pivotal link in achieving seamless human-agent interaction. While traditional SLU can effectively extract user semantics for closed-set tasks after in-domain supervised fine-tuning, it faces significant challenges in...

### 30 - State2State: Environment-Derived Mid-Training for LLM Agents

- arXiv: [2608.04934](https://arxiv.org/abs/2608.04934) | [PDF](https://arxiv.org/pdf/2608.04934) | [papers.cool](https://papers.cool/arxiv/2608.04934)
- Authors: Xuanyu Lei, Yiqi Zhu, Chenliang Li, Kaiming Liu, Peng Li, Ming Yan, et al. (9 authors)
- Published: 2026-08-05 15:02 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agent training; rl_post_training: reinforcement learning; memory_and_benchmarks: alfworld, scienceworld
- Abstract skim: Training LLM agents commonly relies on supervised fine-tuning from expert trajectories or online reinforcement learning over human-specified tasks with handcrafted verifiers. Though effective, both remain bottlenecked by externally specified tasks and supervision signals, limiting the scalability and diversity of...

### 30 - Pun Intended: Multi-Agent Translation of Wordplay with Contrastive Learning and Phonetic-Semantic Embeddings

- arXiv: [2608.04311](https://arxiv.org/abs/2608.04311) | [PDF](https://arxiv.org/pdf/2608.04311) | [papers.cool](https://papers.cool/arxiv/2608.04311)
- Authors: Russell Taylor, Benjamin Herbert, Michael Sana
- Published: 2026-08-05 00:40 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: evaluation
- Abstract skim: Translating wordplay across languages has long challenged both professional translators and machine translation systems. We investigate three approaches to translating puns from English to French by combining large language models with linguistic constraints for wordplay generation. Our baseline uses a large...

### 29 - Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering

- arXiv: [2608.04124](https://arxiv.org/abs/2608.04124) | [PDF](https://arxiv.org/pdf/2608.04124) | [papers.cool](https://papers.cool/arxiv/2608.04124)
- Authors: Haotian Xia, Zilin Xiao, Junbo Zou, Vicente Ordonez, Hanjie Chen
- Published: 2026-08-04 18:23 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Video question answering requires models to ground language queries in visual evidence and, when necessary, reason over that evidence across time. Existing methods typically rely on long textual chain-of-thought rationales, even though many questions can be answered as soon as the relevant object, action, or frame...

### 28 - PRIMAL3: Pathfinding via Reinforcement and Imitation Multi-Agent Learning - Leveraging LaCAM3

- arXiv: [2608.04905](https://arxiv.org/abs/2608.04905) | [PDF](https://arxiv.org/pdf/2608.04905) | [papers.cool](https://papers.cool/arxiv/2608.04905)
- Authors: Chengyang He, Tanishq Duhan, Gadiel Sznaier Camps, Fangyuan Wang, Yuhong Cao, Jiankai Sun, et al. (9 authors)
- Published: 2026-08-05 14:33 UTC | Categories: cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: We present PRIMAL3, an ultra-large-scale learning-based framework for multi-agent pathfinding (MAPF) that integrates reinforcement learning, topology-aware communication, LaCAM3-guided training, and PIBT-based action refinement. PRIMAL3 targets failures at topologically critical states, where agents must coordinate...

### 27 - Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning

- arXiv: [2608.04771](https://arxiv.org/abs/2608.04771) | [PDF](https://arxiv.org/pdf/2608.04771) | [papers.cool](https://papers.cool/arxiv/2608.04771)
- Authors: Qiyuan Zhu, Dezhi Li, Pengyu Cheng, Tianle Chen, Jiacheng Wang, Ruijie Shen, et al. (11 authors)
- Published: 2026-08-05 12:36 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought, process reward, +1 more; planning_and_action: trajectory
- Abstract skim: Large Reasoning Models (LRMs) excel on complex tasks through long chain-of-thought (CoT) reasoning, but their lengthy intermediate steps cause severe overthinking that inflates inference cost. KV-cache compression is a common solution, yet existing reasoning-oriented methods apply a uniform policy across the...

### 27 - K-EXAONE 2.0 Technical Report

- arXiv: [2608.04505](https://arxiv.org/abs/2608.04505) | [PDF](https://arxiv.org/pdf/2608.04505) | [papers.cool](https://papers.cool/arxiv/2608.04505)
- Authors: Eunbi Choi, Kibong Choi, Sehyun Chun, Seokhee Hong, Junwon Hwang, Hyojin Jeon, et al. (77 authors)
- Published: 2026-08-05 06:41 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: This technical report presents K-EXAONE 2.0, an open-weight multilingual foundation model developed by LG AI Research as a step in our effort toward global frontier-scale foundation models. Rather than training from scratch, we upcycle K-EXAONE and expand its architecture, yielding a Mixture-of-Experts (MoE) model...

### 26 - EASy: Towards Efficient LLM-Based Agentic System

- arXiv: [2608.04588](https://arxiv.org/abs/2608.04588) | [PDF](https://arxiv.org/pdf/2608.04588) | [papers.cool](https://papers.cool/arxiv/2608.04588)
- Authors: Junnan Liu, Linhao Luo, Thuy-Trang Vu, Gholamreza Haffari
- Published: 2026-08-05 08:50 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory, rollout, decision making
- Abstract skim: Agentic systems have emerged as a promising paradigm for solving complex tasks by coordinating specialized LLM-based agents. However, most existing systems primarily optimize task success while giving limited consideration to execution efficiency under practical constraints such as executor capability and...

### 25 - OPD-V: Visual On-Policy Self-Distillation with Modality Balance

- arXiv: [2608.05131](https://arxiv.org/abs/2608.05131) | [PDF](https://arxiv.org/pdf/2608.05131) | [papers.cool](https://papers.cool/arxiv/2608.05131)
- Authors: Aniri, Jinhe Bi, Peng Liao, Zengjie Jin, Volker Tresp, Fei Shen, et al. (8 authors)
- Published: 2026-08-05 17:53 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: On-Policy Self-Distillation (OPSD) has become a standard post-training approach for improving visual reasoning in multimodal large language models (MLLMs). Existing methods draw privileged information from diverse input sources to guide self-distillation. Yet these designs overlook Modality Imbalance, a challenge...

### 24 - ArtAnno: Annotating Implicit Semantics in Artworks through LLM Agent-Driven Bidirectional Human-AI Augmentation

- arXiv: [2608.05026](https://arxiv.org/abs/2608.05026) | [PDF](https://arxiv.org/pdf/2608.05026) | [papers.cool](https://papers.cool/arxiv/2608.05026)
- Authors: Xiaoyan Gu, Yifang Wang, Wenqing Zheng, Haozhong Liu, Yixia Zheng, Peiyi Jiang, et al. (9 authors)
- Published: 2026-08-05 16:30 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent, multi-agent; memory_and_benchmarks: evaluation
- Abstract skim: High-quality annotation of artworks is essential for computational art research, yet extracting implicit semantics remains challenging due to the reliance on culturally grounded meanings and deep contextual knowledge behind the images. Current AI-assisted annotation tools often lack assistance or rely on one-way...

### 23 - Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning

- arXiv: [2608.05144](https://arxiv.org/abs/2608.05144) | [PDF](https://arxiv.org/pdf/2608.05144) | [papers.cool](https://papers.cool/arxiv/2608.05144)
- Authors: Boxiu Li, Zimo Wen, Yijia Fan, Junxiang Lei, Sufeng Guo, Jiaao Wu, et al. (26 authors)
- Published: 2026-08-05 17:58 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Long-horizon reasoning requires an agentic runtime that can persist when evidence supports its current approach and pivot when measurements reveal failure, hidden constraints, or a misspecified objective. We present Argus, a persistent, self-evolving runtime in which Manager, Planner, Engineer, and Reviewer execute...

### 21 - EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement

- arXiv: [2608.04968](https://arxiv.org/abs/2608.04968) | [PDF](https://arxiv.org/pdf/2608.04968) | [papers.cool](https://papers.cool/arxiv/2608.04968)
- Authors: Jun Nie, Yonggang Zhang, Qianshu Cai, Yiu-ming Cheung, Xinmei Tian, Bo Han
- Published: 2026-08-05 15:37 UTC | Categories: cs.LG
- Why it matched: agentic_rl: llm agent; reasoning: self-improvement, self improvement; planning_and_action: trajectory
- Abstract skim: The capabilities of an LLM agent depend not only on its model but on the harness: the executable program that constructs context, invokes tools, verifies results, and recovers from failure. Recent work shows that evolving the harness yields persistent improvements without updating model weights. Existing approaches,...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
