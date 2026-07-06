# RL / Post-Training / Agentic RL Reading Queue - 2026-07-06

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 391. Minimum score: 8.

## Top Picks

### 52 - DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models

- arXiv: [2607.02374](https://arxiv.org/abs/2607.02374) | [PDF](https://arxiv.org/pdf/2607.02374) | [papers.cool](https://papers.cool/arxiv/2607.02374)
- Authors: Xi Fang, Weijie Xu, Yingqiang Ge, Yuhui Xu, Stephanie Eckman, Chandan K. Reddy
- Published: 2026-07-02 16:15 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, grpo, dpo; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Personalization changes what a model says to a user; we show that it can also change the reasoning trajectory used to justify the response. Modern LLMs personalize interactions by storing user attributes, preferences, and prior context, then injecting this information into future prompts. We study whether such...

### 48 - Denser $\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training

- arXiv: [2607.01763](https://arxiv.org/abs/2607.01763) | [PDF](https://arxiv.org/pdf/2607.01763) | [papers.cool](https://papers.cool/arxiv/2607.01763)
- Authors: Meng Wang, Haohan Zhao, Wenzhuo Liu, Lu Yang, Geng Liu, Haiyang Guo, et al. (10 authors)
- Published: 2026-07-02 06:24 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more
- Abstract skim: Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities. Recent work suggests that on-policy learning can mitigate forgetting, with on-policy self-distillation emerging as a particularly attractive approach. In this work, we revisit this optimistic view...

### 46 - Beyond Next-Token Prediction: An RLVR Proof of Concept for Tool-Use Agents on Atlassian Workflows

- arXiv: [2607.01465](https://arxiv.org/abs/2607.01465) | [PDF](https://arxiv.org/pdf/2607.01465) | [papers.cool](https://papers.cool/arxiv/2607.01465)
- Authors: Karthikeya Aditya Vissa, Sankalp Mane, Ananya Mantravadi, Harshit Rajgarhia, Abhishek Mukherji
- Published: 2026-07-01 20:55 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, rlvr, grpo
- Abstract skim: Large language models are trained to predict the next token, not to act inside a specific API. In niche enterprise SaaS workflows -- where success means hitting the right endpoint with the right nested arguments in the right order -- this objective mismatch shows up as silent failures: dropped required fields,...

### 41 - Enhancing Fitness Intelligence through Domain-Specific LLM Post-Training

- arXiv: [2607.02118](https://arxiv.org/abs/2607.02118) | [PDF](https://arxiv.org/pdf/2607.02118) | [papers.cool](https://papers.cool/arxiv/2607.02118)
- Authors: Xingtao Zhao, Tian Yang, Han Jiang
- Published: 2026-07-02 12:53 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Scientific Fitness Coaching (SFC) is typically delivered by human professionals, making it costly and inaccessible to many. While recent advances in Large Language Models (LLMs) show considerable promise for more inclusive fitness coaching, directly deploying prevailing general-purpose LLMs in SFC reveals critical...

### 40 - Rank-Then-Act: Reward-Free Control from Frame-Order Progress

- arXiv: [2607.01897](https://arxiv.org/abs/2607.01897) | [PDF](https://arxiv.org/pdf/2607.01897) | [papers.cool](https://papers.cool/arxiv/2607.01897)
- Authors: Yuriy Maksyuta, George Bredis, Ruslan Rakhimov, Daniil Gavrilov
- Published: 2026-07-02 08:50 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model, group relative policy optimization, +1 more
- Abstract skim: We introduce Rank-Then-Act (RTA), a framework for learning control policies from expert video demonstrations without environment rewards. RTA trains a Vision-Language Model (VLM) offline as a progress-based ordinal scorer, using a Group Relative Policy Optimization (GRPO) objective over shuffled frame sequences,...

### 38 - The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning

- arXiv: [2607.01415](https://arxiv.org/abs/2607.01415) | [PDF](https://arxiv.org/pdf/2607.01415) | [papers.cool](https://papers.cool/arxiv/2607.01415)
- Authors: Daniel Thi Graviet, Lovre Pesut, Ivan Dagelic, Vedran Jukic, Ivan Burazin
- Published: 2026-07-01 19:20 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: Coding-agent reinforcement learning treats execution infrastructure as a background implementation detail, despite relying on large numbers of interactive software rollouts. This is a missed opportunity: measuring infrastructure overhead can reveal practical efficiency gains for RL post-training, where small per-...

### 36 - Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning

- arXiv: [2607.02490](https://arxiv.org/abs/2607.02490) | [PDF](https://arxiv.org/pdf/2607.02490) | [papers.cool](https://papers.cool/arxiv/2607.02490)
- Authors: Liyan Tang, Fangcong Yin, Greg Durrett
- Published: 2026-07-02 17:53 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, reflection; planning_and_action: trajectory
- Abstract skim: Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during...

### 36 - CLAP: Closed-Loop Training, Evaluation, and Release Control for Domain Agent Post-training

- arXiv: [2607.01846](https://arxiv.org/abs/2607.01846) | [PDF](https://arxiv.org/pdf/2607.01846) | [papers.cool](https://papers.cool/arxiv/2607.01846)
- Authors: Fangfei Li, Chenyang Zhao, Long Wang, Feng Tian, Zhiyue Zheng, Lv Guo
- Published: 2026-07-02 08:07 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, grpo; memory_and_benchmarks: evaluation
- Abstract skim: Domain agents often face noisy business data, uncertain post-training gains, offline/application mismatch, and adapter-release risk. This paper presents CLAP (Closed-Loop Agent Post-training), a closed-loop method that converts business data into structured SFT samples, decision-preference samples, holdout sets,...

### 36 - Procedural Memory Distillation: Online Reflection for Self-Improving Language Models

- arXiv: [2607.01480](https://arxiv.org/abs/2607.01480) | [PDF](https://arxiv.org/pdf/2607.01480) | [papers.cool](https://papers.cool/arxiv/2607.01480)
- Authors: Ye Liu, Srijan Bansal, Bo Pang, Yang Li, Zeyu Leo Liu, Yifei Ming, et al. (9 authors)
- Published: 2026-07-01 21:20 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reflection; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR), along with recent selfdistillation variants such as SDPO, evaluates each rollout against a verifier and updates the policy from that episode-level signal. However, the richer procedural information in the rollout is rarely retained or reused. Across episodes and...

### 34 - Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model

- arXiv: [2607.01595](https://arxiv.org/abs/2607.01595) | [PDF](https://arxiv.org/pdf/2607.01595) | [papers.cool](https://papers.cool/arxiv/2607.01595)
- Authors: Junyan Tan, Haoran Lin, Siyuan Guo, Yichen Fang, Xinyue Luo, Tianyu Shen, et al. (7 authors)
- Published: 2026-07-02 01:45 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: planning, world model
- Abstract skim: As the scale and complexity of cloud-based AI systems continue to escalate, ensuring service reliability through rapid fault detection and adaptive recovery has become a critical challenge. While existing approaches integrate Large Language Models (LLMs) for semantic understanding and Deep Reinforcement Learning...

### 33 - WorldSample: Closed-loop Real-robot RL with World Modelling

- arXiv: [2607.02431](https://arxiv.org/abs/2607.02431) | [PDF](https://arxiv.org/pdf/2607.02431) | [papers.cool](https://papers.cool/arxiv/2607.02431)
- Authors: Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, et al. (8 authors)
- Published: 2026-07-02 17:00 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout, world model
- Abstract skim: Reinforcement learning (RL) can overcome the demonstration-coverage limitation of imitation learning (IL) by allowing robots to improve through trial-and-error interaction beyond the states observed in demonstrations. However, deploying RL on real robots remains constrained by high interaction costs, since each...

### 33 - TUDUM: A Turkish-Thinking Reasoning Pipeline for Qwen3.5-27B

- arXiv: [2607.01927](https://arxiv.org/abs/2607.01927) | [PDF](https://arxiv.org/pdf/2607.01927) | [papers.cool](https://papers.cool/arxiv/2607.01927)
- Authors: Baran Bingol, Bahaeddin Turkoglu
- Published: 2026-07-02 09:22 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: This paper presents TUDUM (Türkçe Düşünen Üretken Model), a project pipeline for adapting a Qwen-family 27B thinking model toward Turkish reasoning. The central problem is not only to answer Turkish prompts in Turkish, but to make the explicit reasoning trace itself Turkish. A thinking model may translate a Turkish...

### 33 - Don't Let Gains FADE: Breaking Down Policy Gradient Weights in RL

- arXiv: [2607.01490](https://arxiv.org/abs/2607.01490) | [PDF](https://arxiv.org/pdf/2607.01490) | [papers.cool](https://papers.cool/arxiv/2607.01490)
- Authors: Juliette Decugis, Sean O'Brien, Francis Bach, Gabriel Synnaeve, Taco Cohen
- Published: 2026-07-01 21:39 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Reinforcement learning post-training dramatically improves LLM reasoning, but suffers from training instability and diversity collapse. Advantage functions offer an appealing fix: they reshape the training objective, reweight which rollouts drive learning, and are trivial to implement. Yet a proliferation of methods...

### 31 - Evidence-State Rewards for Long-Context Reasoning

- arXiv: [2607.02073](https://arxiv.org/abs/2607.02073) | [PDF](https://arxiv.org/pdf/2607.02073) | [papers.cool](https://papers.cool/arxiv/2607.02073)
- Authors: Ya Gao, Pekka Marttinen
- Published: 2026-07-02 12:11 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Long-context reasoning requires models to locate, revise, and synthesize evidence distributed across lengthy inputs. Existing long-context RL methods usually reward final answers or static evidence extraction, offering little feedback on how intermediate actions change the model's evidence state. We propose Maven, a...

### 30 - UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development

- arXiv: [2607.02186](https://arxiv.org/abs/2607.02186) | [PDF](https://arxiv.org/pdf/2607.02186) | [papers.cool](https://papers.cool/arxiv/2607.02186)
- Authors: Temitayo Olamilekan Ogunsusi, Lijun Qian, Xishuang Dong
- Published: 2026-07-02 13:56 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent collaboration; memory_and_benchmarks: benchmark
- Abstract skim: Software development is a complex task that demands cooperation among agents with diverse roles. Large language models (LLMs) have enabled autonomous multi-agent software development frameworks that leverage role-based collaboration to automate requirements analysis, coding, testing, and refinement. However,...

### 30 - Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry

- arXiv: [2607.01661](https://arxiv.org/abs/2607.01661) | [PDF](https://arxiv.org/pdf/2607.01661) | [papers.cool](https://papers.cool/arxiv/2607.01661)
- Authors: Yuante Li, Yicheng Tao, Kate Zhang, Taozhi Wang, Gefei Gu, Yaxin Zhou
- Published: 2026-07-02 03:41 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, deliberation; memory_and_benchmarks: benchmark
- Abstract skim: Multi-agent systems are increasingly used for forecasting future events, as deliberation among multiple LLMs is believed to improve reasoning and calibration. Yet existing approaches overlook a critical design choice: what information each agent receives. When all agents are given identical evidence, deliberation...

### 30 - Mean Field Reinforcement Learning

- arXiv: [2607.01525](https://arxiv.org/abs/2607.01525) | [PDF](https://arxiv.org/pdf/2607.01525) | [papers.cool](https://papers.cool/arxiv/2607.01525)
- Authors: René Carmona, Mathieu Laurière
- Published: 2026-07-01 22:44 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: This monograph provides an introduction to mean field reinforcement learning through the lens of Markov decision processes arising from large-population stochastic control with mean field interactions and common noise. Starting from the connection between multi-agent reinforcement learning and mean field control, it...

### 29 - Wind-Aware Reinforcement Learning Control of a Small Quadrotor Using Learned Onboard Wind Estimation in Simulated Atmospheric Turbulence

- arXiv: [2607.01528](https://arxiv.org/abs/2607.01528) | [PDF](https://arxiv.org/pdf/2607.01528) | [papers.cool](https://papers.cool/arxiv/2607.01528)
- Authors: Abdullah Al Tasim, Wei Sun
- Published: 2026-07-01 22:59 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Small multirotor aircraft are increasingly tasked with operations in the atmospheric boundary layer, where turbulent winds comparable to the vehicle's airspeed degrade trajectory tracking and can defeat conventional feedback control. This work illustrates a two-stage learning pipeline that first estimates the local...

### 28 - RusFinChain: A Russian Benchmark for Verifiable Chain-of-Thought Reasoning in Finance with Fuzzy-Aligned Evaluation

- arXiv: [2607.01388](https://arxiv.org/abs/2607.01388) | [PDF](https://arxiv.org/pdf/2607.01388) | [papers.cool](https://papers.cool/arxiv/2607.01388)
- Authors: M. K. Arabov
- Published: 2026-07-01 18:48 UTC | Categories: cs.CL
- Why it matched: reasoning: reasoning, chain-of-thought, chain of thought; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Multi-step symbolic reasoning is essential for robust financial analysis, yet most benchmarks neglect intermediate reasoning steps. FINCHAIN introduced verifiable Chain-of-Thought (CoT) evaluation but is limited to English. FINESSE-Bench includes a Russian block but relies on multiple-choice questions without step-...

### 28 - Simulation Based Reward Function Validation for Multi-Agent On Orbit Inspection

- arXiv: [2607.01367](https://arxiv.org/abs/2607.01367) | [PDF](https://arxiv.org/pdf/2607.01367) | [papers.cool](https://papers.cool/arxiv/2607.01367)
- Authors: Patrick Quinn, Bala Prenith Reddy Gopu, George M. Nehma, Madhur Tiwari
- Published: 2026-07-01 18:32 UTC | Categories: cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: A proposed method for the control of groups of inspection spacecraft is Multi-Agent Reinforcement Learning (MARL). While MARL has already been employed for this purpose in previous work, the reward functions used focus on reaching a finite set of predetermined inspection points around the target. In this work, we...

### 26 - A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory

- arXiv: [2607.01935](https://arxiv.org/abs/2607.01935) | [PDF](https://arxiv.org/pdf/2607.01935) | [papers.cool](https://papers.cool/arxiv/2607.01935)
- Authors: Zitong Shi, Yixuan Tang, Anthony Kum Hoe Tung
- Published: 2026-07-02 09:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory, long-term memory, benchmark, evaluation
- Abstract skim: Long term memory lets LLM agents act as persistent assistants, but user facts change. A useful memory system must know what is true now, what used to be true, and what changed. We study \emph{ghost memory}, a state coordination failure in which old, current, and transition facts coexist in the memory bank, remain...

### 26 - Decomposer: Learning to Decompile Symbolic Music to Programs

- arXiv: [2607.01849](https://arxiv.org/abs/2607.01849) | [PDF](https://arxiv.org/pdf/2607.01849) | [papers.cool](https://papers.cool/arxiv/2607.01849)
- Authors: Yewon Kim, Apurva Gandhi, David Chung, Graham Neubig, Chris Donahue
- Published: 2026-07-02 08:09 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; memory_and_benchmarks: evaluation
- Abstract skim: Musical performance involves executing a set of high-level musical instructions, yet recovering those instructions from the performance is a challenging inverse problem. We present Decomposer, a post-training framework for symbolic music decompilation: the task of recovering executable, editable music programs from...

### 26 - Many Voices, One Reward: Multi-Role Rubric Generation for LLM Judging and Reward Modeling

- arXiv: [2607.01830](https://arxiv.org/abs/2607.01830) | [PDF](https://arxiv.org/pdf/2607.01830) | [papers.cool](https://papers.cool/arxiv/2607.01830)
- Authors: Dazhi Fu, Jiuding Yang, Yiwen Guo, Jicong Fan
- Published: 2026-07-02 07:50 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; memory_and_benchmarks: evaluation
- Abstract skim: Reliable reward and preference signals are critical for evaluating and optimizing large language models on open-ended tasks. Rubric-based judges offer a transparent way to decompose such judgments into explicit evaluation criteria, but existing annotation-free rubric generators typically rely on a single generic...

### 26 - Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning

- arXiv: [2607.01308](https://arxiv.org/abs/2607.01308) | [PDF](https://arxiv.org/pdf/2607.01308) | [papers.cool](https://papers.cool/arxiv/2607.01308)
- Authors: Carlos Baquero, Luís Brito
- Published: 2026-07-01 17:05 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Multi-agent latent reasoning composes agents' KV-caches into one context for a final agent. Prior work (Agent Primitives) does this by concatenating caches along the sequence axis with RoPE re-encoding, which we call BagMerge. BagMerge is non-commutative, and the best input ordering is unpredictable, shifting with...

### 25 - FaithMed: Training LLMs For Faithful Evidence-Based Medical Reasoning

- arXiv: [2607.01440](https://arxiv.org/abs/2607.01440) | [PDF](https://arxiv.org/pdf/2607.01440) | [papers.cool](https://papers.cool/arxiv/2607.01440)
- Authors: Zhiyun Zhang, Liwen Sun, Xiang Qian, Chenyan Xiong
- Published: 2026-07-01 20:02 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, process reward
- Abstract skim: Faithful reasoning is essential in medicine, where clinical decisions require transparent justification grounded in reliable evidence. Current medical LLMs either lack active access to evidence or use retrieved evidence without supervising how it should be appraised and applied during reasoning. To address this, we...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
