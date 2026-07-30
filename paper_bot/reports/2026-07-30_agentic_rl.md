# RL / Post-Training / Agentic RL Reading Queue - 2026-07-30

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 317. Minimum score: 8.

## Top Picks

### 68 - ReCo: Reweighting GRPO Against Distributional Concentration

- arXiv: [2607.26862](https://arxiv.org/abs/2607.26862) | [PDF](https://arxiv.org/pdf/2607.26862) | [papers.cool](https://papers.cool/arxiv/2607.26862)
- Authors: Junoh Park, Junseo Hwang, Wonguk Cho, Taesup Kim
- Published: 2026-07-29 12:45 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Group Relative Policy Optimization (GRPO) has become a standard reinforcement learning method for post-training language models. Recent work shows that GRPO can reduce the base model's reasoning capacity and underperform it in Pass@k when k is large, indicating reduced coverage of reasoning paths. We find that this...

### 64 - Meta-Learned Reward Shaping for Reinforcement Learning from Human Feedback

- arXiv: [2607.26094](https://arxiv.org/abs/2607.26094) | [PDF](https://arxiv.org/pdf/2607.26094) | [papers.cool](https://papers.cool/arxiv/2607.26094)
- Authors: Yunpeng Chu
- Published: 2026-07-28 02:09 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, grpo, +2 more
- Abstract skim: Reinforcement Learning from Human Feedback (RLHF) is the standard approach for aligning large language models with human preferences, but its quality is limited by static, task-agnostic reward models. This mismatch leads to sparse learning signals and suboptimal alignment. We introduce MeRLa (Meta-Learned Reward...

### 50 - Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for Compute-Efficient RLVR

- arXiv: [2607.26253](https://arxiv.org/abs/2607.26253) | [PDF](https://arxiv.org/pdf/2607.26253) | [papers.cool](https://papers.cool/arxiv/2607.26253)
- Authors: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
- Published: 2026-07-28 20:43 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; reasoning: reasoning; planning_and_action: planning, rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) is bottlenecked by rollout generation, yet many sampled prompts produce saturated groups (all responses correct or all incorrect) whose zero reward variance yields no policy-gradient signal. Existing remedies either oversample a larger candidate pool and discard...

### 48 - Graph Is the Verifier: Agentic Reinforcement Learning for Interprocedural Vulnerability Detection

- arXiv: [2607.26656](https://arxiv.org/abs/2607.26656) | [PDF](https://arxiv.org/pdf/2607.26656) | [papers.cool](https://papers.cool/arxiv/2607.26656)
- Authors: Yikun Li, Ting Zhang, Jiakun Liu, Jinfeng Jiang, Yuheng Yieh, Yixin Yang, et al. (12 authors)
- Published: 2026-07-29 09:16 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl, tool use; rl_post_training: reinforcement learning
- Abstract skim: Real-world vulnerabilities often span multiple functions, yet most learning-based detectors classify each function in isolation: on a sample of real CVEs, we find that 71.7% of vulnerable functions require evidence from outside the function to be classified correctly. Agentic reinforcement learning (RL) could close...

### 44 - SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution

- arXiv: [2607.26784](https://arxiv.org/abs/2607.26784) | [PDF](https://arxiv.org/pdf/2607.26784) | [papers.cool](https://papers.cool/arxiv/2607.26784)
- Authors: Zhiyuan Yao, Yuxin Chen, Zhengxi Lu, Zishan Xu, Yueqing Sun, Yifu Guo, et al. (16 authors)
- Published: 2026-07-29 11:26 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; memory_and_benchmarks: alfworld, scienceworld
- Abstract skim: Large language model agents often encounter related yet distinct tasks that share reusable solution patterns. Yet standard agentic reinforcement learning treats tasks as independent episodes, while existing approaches to skill learning either focus on repeated attempts of one task or use pipelines with multiple...

### 43 - HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models

- arXiv: [2607.26515](https://arxiv.org/abs/2607.26515) | [PDF](https://arxiv.org/pdf/2607.26515) | [papers.cool](https://papers.cool/arxiv/2607.26515)
- Authors: Hei Yi Mak, Shadan Golestan, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Yaoyuan Wang, et al. (13 authors)
- Published: 2026-07-29 06:28 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision. A systematic study reveals that the dominant source of degradation in FP4 RL is not training-side quantization error but...

### 39 - WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models

- arXiv: [2607.26621](https://arxiv.org/abs/2607.26621) | [PDF](https://arxiv.org/pdf/2607.26621) | [papers.cool](https://papers.cool/arxiv/2607.26621)
- Authors: Hao Jiang, Peiru Du, Pengfei Yao, Mengting Li, Siyuan Lou, Kuo Cai, et al. (13 authors)
- Published: 2026-07-29 08:48 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark
- Abstract skim: Large language models (LLMs) have demonstrated strong reasoning capabilities, motivating their adoption as backbones for foundation recommendation models (FRMs). Existing approaches typically enhance recommendation with explicit Chain-of-Thought (CoT) under the Think-then-Answer paradigm. However, generating lengthy...

### 38 - RLMM-Flow: A Flow-based Mobile Manipulation Framework with Latent-Space Reinforcement Learning

- arXiv: [2607.26460](https://arxiv.org/abs/2607.26460) | [PDF](https://arxiv.org/pdf/2607.26460) | [papers.cool](https://papers.cool/arxiv/2607.26460)
- Authors: Shuhang Wang, Ziming Li, Hui Cheng
- Published: 2026-07-29 04:22 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: planning, trajectory
- Abstract skim: Mobile manipulation requires generating whole-body action chunks that jointly satisfy goal reaching, collision avoidance, base kinematic constraints, manipulator joint limits, and trajectory smoothness. Flow-based generative policies provide an efficient paradigm for learning multimodal and temporally consistent...

### 37 - FAS-R1: A Unified Multi-Task MLLM for Reasoning Face Anti-Spoofing

- arXiv: [2607.26432](https://arxiv.org/abs/2607.26432) | [PDF](https://arxiv.org/pdf/2607.26432) | [papers.cool](https://papers.cool/arxiv/2607.26432)
- Authors: Hongyang Wang, Yichen Shi, Hongrui Li, Yiru Huo, Jun Feng, Zitong Yu
- Published: 2026-07-29 03:19 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning
- Abstract skim: Face anti-spoofing (FAS) is increasingly expected to provide not only bona fide/spoof decisions, but also attack semantics and image-grounded evidence for human inspection. Existing discriminative FAS models remain largely label-centric, while recent MLLM-based methods offer structured outputs but still rely mainly...

### 37 - GPT-Red: Automated Red Teaming via Self-Play at Scale

- arXiv: [2607.26115](https://arxiv.org/abs/2607.26115) | [PDF](https://arxiv.org/pdf/2607.26115) | [papers.cool](https://papers.cool/arxiv/2607.26115)
- Authors: Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal, Sam Toyer, Dylan Hunn, Stephanie Lin, et al. (18 authors)
- Published: 2026-07-28 16:03 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: self-improvement, self improvement, self-play
- Abstract skim: We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it to adversarially train GPT-5.6, our most robust model to...

### 34 - SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement Learning

- arXiv: [2607.26873](https://arxiv.org/abs/2607.26873) | [PDF](https://arxiv.org/pdf/2607.26873) | [papers.cool](https://papers.cool/arxiv/2607.26873)
- Authors: Jianze Wang, Kunwang Zheng, Ying Liu, Yu Cao, Qilong Zhang, Jinlong Chen, et al. (8 authors)
- Published: 2026-07-29 13:03 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization; memory_and_benchmarks: benchmark
- Abstract skim: Test-time reinforcement learning (TTRL) enables language models to self-evolve at inference time without labeled feedback. Existing methods rely on answer voting and therefore do not extend naturally to open-ended generation, where valid responses cannot be mapped to a shared canonical answer. Without external...

### 32 - DHRCL:Training Code LLMs with Dense Hierarchical Rewards and Curriculum Learning

- arXiv: [2607.26457](https://arxiv.org/abs/2607.26457) | [PDF](https://arxiv.org/pdf/2607.26457) | [papers.cool](https://papers.cool/arxiv/2607.26457)
- Authors: Shuhang Wang, Ziming Li, Hui Cheng
- Published: 2026-07-29 04:16 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model
- Abstract skim: Reinforcement learning is a natural post-training paradigm for code-oriented large language models because generated programs can be evaluated through parsing, execution, unit tests, and structural analysis.However, existing methods often rely on sparse outcome rewards or statically combine heterogeneous dense...

### 32 - Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning

- arXiv: [2607.26358](https://arxiv.org/abs/2607.26358) | [PDF](https://arxiv.org/pdf/2607.26358) | [papers.cool](https://papers.cool/arxiv/2607.26358)
- Authors: Keegan Harris, Brian W. Lee, Ian Waudby-Smith, Philip Amortila, Nika Haghtalab, Michael I. Jordan
- Published: 2026-07-29 00:19 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Reinforcement learning (RL) fine-tuning is widely used in language model training to improve model performance on a target task while limiting drift from a reference policy. A standard way to balance this trade-off is via a KL-regularized RL objective, although this formulation does not by itself provide a...

### 30 - MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair

- arXiv: [2607.27080](https://arxiv.org/abs/2607.27080) | [PDF](https://arxiv.org/pdf/2607.27080) | [papers.cool](https://papers.cool/arxiv/2607.27080)
- Authors: Xuanze Chen, Xukang Xie, Wentao Fu, Jiajun Zhou, Shanqing Yu, Qi Xuan
- Published: 2026-07-29 16:06 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory, agent harness; memory_and_benchmarks: memory, long-term memory, benchmark
- Abstract skim: Memory systems allow agents to retain and reuse information from past interactions, but they can also let malicious content persist. A malicious instruction crafted by an attacker may be stored in long-term memory, recalled much later, and quietly shape a real action. Recent benchmarks increasingly examine agent...

### 28 - Learning Implicit Causal World Models from Multi-Agent Demonstrations

- arXiv: [2607.26336](https://arxiv.org/abs/2607.26336) | [PDF](https://arxiv.org/pdf/2607.26336) | [papers.cool](https://papers.cool/arxiv/2607.26336)
- Authors: Jasorsi Ghosh
- Published: 2026-07-28 23:18 UTC | Categories: cs.LG, cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: In model-based reinforcement learning, world models exist as internal simulators, but their training often conflates statistical correlations with causal mechanisms. This problem is exacerbated in multi-agent systems where physical transitions are intertwined with strategic agent intents, causing world models to...

### 26 - GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning

- arXiv: [2607.26160](https://arxiv.org/abs/2607.26160) | [PDF](https://arxiv.org/pdf/2607.26160) | [papers.cool](https://papers.cool/arxiv/2607.26160)
- Authors: Lang Cao, Yuhao Shen, Tianyang Luo, Simo Du, Hao Peng, Yue Guo
- Published: 2026-07-28 18:10 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Clinical practice guidelines (CPGs) encode diagnostic criteria, but LLM systems typically retrieve guideline text or absorb it through training rather than execute its rules. We introduce GuideSkill, an external reasoning layer that compiles disease-specific criteria into executable functions returning ordinal...

### 25 - Constitutional Midtraining: Content Presence Drives Alignment Gains

- arXiv: [2607.26654](https://arxiv.org/abs/2607.26654) | [PDF](https://arxiv.org/pdf/2607.26654) | [papers.cool](https://papers.cool/arxiv/2607.26654)
- Authors: Desiree Cho, Cameron Tice, Bernie Hogan, Hunar Batra, Puria Radmard, Jun Zhao, et al. (7 authors)
- Published: 2026-07-29 09:15 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Post-training alignment is often shallow, eroding under fine-tuning. Whether midtraining interventions, cleanly isolated from post-training, can produce durable alignment remains untested. We test this via constitutional midtraining: inserting principled, values-based content into midtraining against a replay-only...

### 24 - A Physics-Informed Framework for PID Tuning of Chemical Processes Using Large Language Model Agents

- arXiv: [2607.26594](https://arxiv.org/abs/2607.26594) | [PDF](https://arxiv.org/pdf/2607.26594) | [papers.cool](https://papers.cool/arxiv/2607.26594)
- Authors: Zhoupeng Shou, Xiaodong Hong, Congjing Ren, Jingdai Wang, Yongrong Yang, Zuwei Liao
- Published: 2026-07-29 08:14 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo
- Abstract skim: PID tuning for chemical processes commonly relies on identified process models, whereas plant engineers often retune loops iteratively by observing responses, diagnosing deficiencies, adjusting gains, and validating the result. This work formalizes this engineer-like workflow in a language-model-assisted PID tuning...

### 24 - Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models

- arXiv: [2607.26513](https://arxiv.org/abs/2607.26513) | [PDF](https://arxiv.org/pdf/2607.26513) | [papers.cool](https://papers.cool/arxiv/2607.26513)
- Authors: Mingyang Sun, Jiude Wei, Xiujian Liang, Qichen He, Donglin Wang, Cewu Lu, et al. (7 authors)
- Published: 2026-07-29 06:24 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Current Vision-Language-Action (VLA) models rely mainly on 2D inputs, neglecting the rich object structural information and commonsense knowledge inherent in the 3D physical world. This deficiency restricts their spatial awareness and adaptability for complex, high-precision manipulation. To bridge this crucial gap,...

### 21 - SCOUT: Per-Context Reset Curricula for Sparse-Reward Reinforcement Learning

- arXiv: [2607.26417](https://arxiv.org/abs/2607.26417) | [PDF](https://arxiv.org/pdf/2607.26417) | [papers.cool](https://papers.cool/arxiv/2607.26417)
- Authors: Siddharth Aphale, Ayushman Singh
- Published: 2026-07-29 02:59 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Sparse-reward reinforcement learning often fails because rollouts from the unassisted evaluation start rarely reach later task stages. Reset curricula address this by starting some training rollouts from easier intermediate states, called scaffolds. Such a curriculum faces two decisions: scaffold access, obtaining...

### 21 - Probing the Origins of Reasoning Performance: Representational Quality for Mathematical Problem-Solving in RL vs. SFT Fine-Tuned Models

- arXiv: [2607.26119](https://arxiv.org/abs/2607.26119) | [PDF](https://arxiv.org/pdf/2607.26119) | [papers.cool](https://papers.cool/arxiv/2607.26119)
- Authors: Antyabha Rahman, Akshaj Gurugubelli, Omar Ankit, Kevin Zhu, Aishwarya Balwani
- Published: 2026-07-28 17:42 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Large reasoning models trained via reinforcement learning (RL) have been increasingly shown to outperform their supervised fine-tuned (SFT) counterparts on mathematical reasoning tasks; Yet the mechanistic basis for this advantage remains unclear. We therefore ask, what internal representational differences enable...

### 20 - Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data

- arXiv: [2607.27056](https://arxiv.org/abs/2607.27056) | [PDF](https://arxiv.org/pdf/2607.27056) | [papers.cool](https://papers.cool/arxiv/2607.27056)
- Authors: Lingyang Zeng, Guangze Chen, Kaichen Yu, Zhicheng Pan, Siyang Weng, Zirui Hu, et al. (12 authors)
- Published: 2026-07-29 15:47 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory, episodic memory, benchmark, evaluation
- Abstract skim: Personalized agents are increasingly applied to assist users across a wide range of tasks. Effective personalized assistance requires not only retrieving explicit facts from past interactions stored in agent memory, but also inferring abstract personal characteristics. However, existing memory benchmarks primarily...

### 20 - TREK: A Travel Reasoning and Evaluation Kit for LLM Agents in Complex Trip Planning

- arXiv: [2607.26977](https://arxiv.org/abs/2607.26977) | [PDF](https://arxiv.org/pdf/2607.26977) | [papers.cool](https://papers.cool/arxiv/2607.26977)
- Authors: Jinhu Qi, Wentao Zhang, Siu Man Ng, Feiyang Xu, Yanyu Chen, Yaoman Li, et al. (7 authors)
- Published: 2026-07-29 14:35 UTC | Categories: cs.CL
- Why it matched: reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Travel planning is a demanding stress test for tool-using LLM agents: a usable itinerary is a single artifact that must be right along many axes at once - every flight, hotel, and attraction must exist and be bookable, the days must be physically traversable, the total must clear a budget, and the plan must serve a...

### 20 - UrbanDS: A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks

- arXiv: [2607.26724](https://arxiv.org/abs/2607.26724) | [PDF](https://arxiv.org/pdf/2607.26724) | [papers.cool](https://papers.cool/arxiv/2607.26724)
- Authors: Zhilun Zhou, Jianghao Yu, Yuming Lin, yongjun yang, Sun Yongquan, Depeng Jin, et al. (7 authors)
- Published: 2026-07-29 10:14 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; memory_and_benchmarks: memory, benchmark
- Abstract skim: Large language model (LLM) agents have been widely applied in automating data science tasks. However, existing methods typically rely on a limited set of provided datasets, and they face challenges in data-intensive scenarios that require discovering and leveraging relevant information from large-scale and...

### 19 - Q-Steer: Action-Value Guidance for Molecular Policy Optimization

- arXiv: [2607.26391](https://arxiv.org/abs/2607.26391) | [PDF](https://arxiv.org/pdf/2607.26391) | [papers.cool](https://papers.cool/arxiv/2607.26391)
- Authors: Xinyu Wang, Jinbo Bi, Minghu Song
- Published: 2026-07-29 01:53 UTC | Categories: cs.LG
- Why it matched: rl_post_training: policy optimization; planning_and_action: rollout
- Abstract skim: Oracle-limited molecular optimization gives reward only after a complete molecule is generated, while each rollout requires many local next-token decisions. This delayed-feedback interface makes molecular policy optimization myopic: an optimizer can learn that a molecule was good without knowing which intermediate...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
