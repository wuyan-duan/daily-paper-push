# RL / Post-Training / Agentic RL Reading Queue - 2026-11-06

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 457. Minimum score: 8.

## Top Picks

### 61 - AttnSR: Attention Step Reward for Long-Horizon Agentic RL

- arXiv: [2611.07932](https://arxiv.org/abs/2611.07932) | [PDF](https://arxiv.org/pdf/2611.07932) | [papers.cool](https://papers.cool/arxiv/2611.07932)
- Authors: Mengsong Wu, Tianchen Zhou, Zhaochen Su, Zhenhua Liu, Zhe Cui, Aimin Zhou
- Published: 2026-11-05 12:37 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic rl; rl_post_training: reinforcement learning, reward model, ppo; reasoning: outcome reward; memory_and_benchmarks: alfworld, scienceworld
- Abstract skim: Long-horizon LLM agents make multi-step decisions, yet outcome-reward-only reinforcement learning provides little direct supervision for individual steps. We introduce AttnSR, a step-level reward augmentation method that derives reward allocations from policy attention extracted during training replay, without a...

### 53 - Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis

- arXiv: [2611.08219](https://arxiv.org/abs/2611.08219) | [PDF](https://arxiv.org/pdf/2611.08219) | [papers.cool](https://papers.cool/arxiv/2611.08219)
- Authors: Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, et al. (8 authors)
- Published: 2026-11-05 16:08 UTC | Categories: cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows,...

### 53 - Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning

- arXiv: [2611.06956](https://arxiv.org/abs/2611.06956) | [PDF](https://arxiv.org/pdf/2611.06956) | [papers.cool](https://papers.cool/arxiv/2611.06956)
- Authors: Tianming Sha
- Published: 2026-11-03 22:42 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branches, exchange findings by re-prefilling...

### 48 - Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback

- arXiv: [2611.07561](https://arxiv.org/abs/2611.07561) | [PDF](https://arxiv.org/pdf/2611.07561) | [papers.cool](https://papers.cool/arxiv/2611.07561)
- Authors: Weiqin Chen, Xinmeng Huang, Dongsheng Ding, Santiago Paternain
- Published: 2026-11-05 07:14 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, reward model
- Abstract skim: Safe reinforcement learning from human feedback (Safe-RLHF) seeks to improve helpfulness while satisfying harmlessness constraints. Existing primal-dual approaches can converge to feasible policies but do not prevent constraint violations during training. We study a stronger requirement, safe exploration for RLHF,...

### 45 - Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism

- arXiv: [2611.06984](https://arxiv.org/abs/2611.06984) | [PDF](https://arxiv.org/pdf/2611.06984) | [papers.cool](https://papers.cool/arxiv/2611.06984)
- Authors: Jia Wei, Ziyi Qiu, Yi Xu, Xuehai Qian
- Published: 2026-11-04 15:36 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Reinforcement learning post-training improves the capabilities of large language models, but generating training responses is a major computational bottleneck. In mixture-of-experts models, workers that finish their assigned responses may remain occupied because their experts are still needed by workers processing...

### 42 - Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration

- arXiv: [2611.07066](https://arxiv.org/abs/2611.07066) | [PDF](https://arxiv.org/pdf/2611.07066) | [papers.cool](https://papers.cool/arxiv/2611.07066)
- Authors: Sungil Son, Hoseong Jung, Dahyun Oh, H. Jin Kim
- Published: 2026-11-04 19:24 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark
- Abstract skim: Discovering cooperative behavior in multi-agent reinforcement learning (MARL) is challenging due to the combinatorial complexity of joint state-action spaces, which hinders the emergence of coordinated behaviors from trial-and-error alone. Intrinsic rewards are often used to aid discovery, but naively combining them...

### 40 - Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO

- arXiv: [2611.08453](https://arxiv.org/abs/2611.08453) | [PDF](https://arxiv.org/pdf/2611.08453) | [papers.cool](https://papers.cool/arxiv/2611.08453)
- Authors: Zeyu Leo Liu, Yang Li, Bo Pang, Emre Can Acikgoz, Xuan-Phi Nguyen, Anurag Koul, et al. (10 authors)
- Published: 2026-11-05 18:47 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: On-policy distillation (OPD) trains a student on its own rollouts under a frozen teacher's per-token supervision. Does this dense signal reduce the training FLOPs needed to reach a target accuracy compared with reinforcement learning? We systematically compare vanilla reverse-KL OPD with Group Relative Policy...

### 40 - Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement

- arXiv: [2611.07495](https://arxiv.org/abs/2611.07495) | [PDF](https://arxiv.org/pdf/2611.07495) | [papers.cool](https://papers.cool/arxiv/2611.07495)
- Authors: Kaixuan Liu, Guojun Xiong
- Published: 2026-11-05 05:58 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent, agent orchestration; rl_post_training: policy optimization
- Abstract skim: Learned orchestration has emerged as a promising paradigm for large language model (LLM)-based multi-agent systems, in which a central orchestrator selects agents and controls the information they receive throughout a task. Despite rapid empirical progress, existing methods train the orchestrator by crediting each...

### 37 - SAVeR$^2$: Reasoning-based Safety Alignment for Large Reasoning Models via Verifiable Rewards

- arXiv: [2611.07482](https://arxiv.org/abs/2611.07482) | [PDF](https://arxiv.org/pdf/2611.07482) | [papers.cool](https://papers.cool/arxiv/2611.07482)
- Authors: Yichen Sun, Qirui Liu, Yan Wang, Jianan Lin, Linbo Jiang, Shiyu Wang, et al. (8 authors)
- Published: 2026-11-05 05:42 UTC | Categories: cs.AI
- Why it matched: rl_post_training: verifiable reward; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Large Reasoning Models (LRMs) have achieved impressive performance via explicit Chain-of-Thought (CoT) reasoning, yet this process introduces critical safety risks. We formalize LRM safety objectives as requiring non-malicious reasoning and answers, safety consistency, and explicit intent identification. We argue...

### 36 - Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning

- arXiv: [2611.08144](https://arxiv.org/abs/2611.08144) | [PDF](https://arxiv.org/pdf/2611.08144) | [papers.cool](https://papers.cool/arxiv/2611.08144)
- Authors: Zuo Gou, Chenhao Lu
- Published: 2026-11-05 15:05 UTC | Categories: cs.LG, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: evaluation
- Abstract skim: Robot reinforcement learning increasingly runs environments outside the trainer: in another process, on another machine, in another language. Many faults at this boundary raise no error. We make the boundary a wire protocol and ask what notices a fault in it. On Pendulum, HalfCheetah, Hopper and a 7-joint arm...

### 36 - Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach

- arXiv: [2611.07122](https://arxiv.org/abs/2611.07122) | [PDF](https://arxiv.org/pdf/2611.07122) | [papers.cool](https://papers.cool/arxiv/2611.07122)
- Authors: Korbinian Kügler, Carolin Schmidt, Florian Dandl, Filipe Rodrigues
- Published: 2026-11-04 20:38 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility system can limit surge pricing and...

### 35 - DictLLM: Post-training Compression of Large Language Model with Dictionary Kernels

- arXiv: [2611.08082](https://arxiv.org/abs/2611.08082) | [PDF](https://arxiv.org/pdf/2611.08082) | [papers.cool](https://papers.cool/arxiv/2611.08082)
- Authors: Jinho Park, Se Young Chun, Mingoo Seok
- Published: 2026-11-05 14:31 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Efficient deployment of large language models (LLMs) on mobile devices requires balancing performance with compute and memory constraints. Post-training compression is an effective approach to managing this trade-off, while requiring much less computation than in-training counterparts. We propose DictLLM, a...

### 34 - PSGAgent: Enhancing MLLMs' Dynamic Visual Perception for Panoptic Scene Graph Generation via Agentic Reasoning

- arXiv: [2611.07408](https://arxiv.org/abs/2611.07408) | [PDF](https://arxiv.org/pdf/2611.07408) | [papers.cool](https://papers.cool/arxiv/2611.07408)
- Authors: Qingyun Liu, Yuankun Liu, Jiaye Feng, Jie Huang, Zonghong Dai, Haochen Li, et al. (9 authors)
- Published: 2026-11-05 04:02 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: decision making; memory_and_benchmarks: benchmark
- Abstract skim: Panoptic Scene Graph generation (PSG) requires holistic yet fine-grained reasoning over complex relations among objects. However, current Multimodal Large Language Models (MLLMs) applied to PSG suffer from a perception bottleneck: they function as static observers limited by fixed-resolution views. As a result,...

### 33 - CST-Bench: Benchmarking Counterfactual Spatial Transition Reasoning with Causal Transition On-Policy Self-Distillation

- arXiv: [2611.07541](https://arxiv.org/abs/2611.07541) | [PDF](https://arxiv.org/pdf/2611.07541) | [papers.cool](https://papers.cool/arxiv/2611.07541)
- Authors: Ying Li, Yongle Cheng, Jing Li, Xingquan Cai, Yawei Luo
- Published: 2026-11-05 06:49 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Spatial reasoning is a fundamental capability of multimodal large language models (MLLMs), yet existing benchmarks mainly focus on static scene understanding. When objects are moved or swapped, models must infer not only spatial relations but also how interventions change the scene state. To address this problem, we...

### 32 - FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning

- arXiv: [2611.08240](https://arxiv.org/abs/2611.08240) | [PDF](https://arxiv.org/pdf/2611.08240) | [papers.cool](https://papers.cool/arxiv/2611.08240)
- Authors: Haitao Lin, Minsi Ren, Yang Li, Xingtong Ge, Zheyuan Hu, Peiyan Hu, et al. (7 authors)
- Published: 2026-11-05 16:19 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Reinforcement learning (RL) has become a standard post-training method for diffusion models, but most RL objectives roll out the current policy at every iteration, and with a many-step sampler these rollouts typically dominate the cost of training. Few-step models cut this cost, yet they model an average velocity...

### 32 - SEER: A Scalable Event-Driven Runtime for Parallel Execution of Multi-Agent Reinforcement Learning Environments

- arXiv: [2611.07996](https://arxiv.org/abs/2611.07996) | [PDF](https://arxiv.org/pdf/2611.07996) | [papers.cool](https://papers.cool/arxiv/2611.07996)
- Authors: Jiming Su, Feng Zhu, Yuhao Xiao, Miao Zhang
- Published: 2026-11-05 13:24 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: wireless
- Abstract skim: Multi-agent reinforcement learning (MARL) is increasingly used in systems where many entities interact in a shared environment. In these workloads, policy inference can be batched on GPUs, but the CPU-side environment path still updates entity states, resolves local interactions, and builds observations inside each...

### 32 - Learning Robotic World Models with Semantic and Visual Feedback

- arXiv: [2611.07850](https://arxiv.org/abs/2611.07850) | [PDF](https://arxiv.org/pdf/2611.07850) | [papers.cool](https://papers.cool/arxiv/2611.07850)
- Authors: Hao Wu, Yuqi Li, Yizhou Zhao, Kun Wang, Xiao Luo, Yu Cheng, et al. (10 authors)
- Published: 2026-11-05 11:30 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, policy optimization; planning_and_action: planning, decision making; memory_and_benchmarks: evaluation
- Abstract skim: Robot world models predict action-conditioned future visual states to support robotic planning and decision making. However, visual reconstruction does not fully capture task progress, semantic evaluation alone provides limited constraints on fine-grained visual errors, and homogeneous predictions limit comparative...

### 31 - TileQuant: Tile as the Precision-Allocation Unit for LLM Mixed-Precision Post-Training Quantization

- arXiv: [2611.07217](https://arxiv.org/abs/2611.07217) | [PDF](https://arxiv.org/pdf/2611.07217) | [papers.cool](https://papers.cool/arxiv/2611.07217)
- Authors: Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, et al. (7 authors)
- Published: 2026-11-04 23:09 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; memory_and_benchmarks: memory; downranked: traffic
- Abstract skim: Post-training quantization (PTQ) reduces large language model (LLM) deployment costs, but preserving quality requires accounting for uneven weight sensitivity. Uniform PTQ uses one weight bit-width, importance-aware PTQ adjusts scales or reconstructs weights within that width, and column-wise mixed precision retains...

### 30 - Accelerating Safe Reinforcement Learning with Massive Parallelism

- arXiv: [2611.08273](https://arxiv.org/abs/2611.08273) | [PDF](https://arxiv.org/pdf/2611.08273) | [papers.cool](https://papers.cool/arxiv/2611.08273)
- Authors: Joonyoung Lim, Younghwan Yoo
- Published: 2026-11-05 16:43 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory, rollout
- Abstract skim: We investigate the problem of scaling safe reinforcement learning (safe RL) to massively parallel training regimes, where a large number of environments are exe- cuted with short rollout horizons. Although this setting improves data throughput and wall-clock efficiency, it creates a mismatch with constrained Markov...

### 28 - Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes

- arXiv: [2611.07730](https://arxiv.org/abs/2611.07730) | [PDF](https://arxiv.org/pdf/2611.07730) | [papers.cool](https://papers.cool/arxiv/2611.07730)
- Authors: Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang
- Published: 2026-11-05 09:42 UTC | Categories: cs.AI, cs.RO
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: acting, world model; memory_and_benchmarks: evaluation
- Abstract skim: Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of crossing pedestrians, or bottleneck a narrow passage. These failure modes are invisible from the current...

### 26 - Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking

- arXiv: [2611.08249](https://arxiv.org/abs/2611.08249) | [PDF](https://arxiv.org/pdf/2611.08249) | [papers.cool](https://papers.cool/arxiv/2611.08249)
- Authors: Michael Brown, Maryam Rahimimovassagh, Mehdi Yazdani-Jahromi, Sanjeda Sara Jennifer, Ivan Garibay
- Published: 2026-11-05 16:26 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: evaluation
- Abstract skim: Diffusion-based molecular docking requires learning a corrective score field across a broad corruption distribution, yet individual pose errors can differ substantially in their structural consequences. This creates a post-training conflict between preserving broad score-field coverage and concentrating supervision...

### 26 - Measuring the Marginal Value of Verifier-Based RL Beyond Supervised Fine-Tuning

- arXiv: [2611.07639](https://arxiv.org/abs/2611.07639) | [PDF](https://arxiv.org/pdf/2611.07639) | [papers.cool](https://papers.cool/arxiv/2611.07639)
- Authors: Amit Sagtani, Saloni Garg
- Published: 2026-11-05 08:23 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning from verifiable rewards (RLVR) is usually evaluated as an alternative to supervised fine-tuning (SFT), or as a stage that follows it, with the implicit assumption that the RL stage contributes gains of its own. We measure that contribution directly, in a controlled setting where both stages...

### 25 - Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning

- arXiv: [2611.08414](https://arxiv.org/abs/2611.08414) | [PDF](https://arxiv.org/pdf/2611.08414) | [papers.cool](https://papers.cool/arxiv/2611.08414)
- Authors: Chenruo Liu, Zihan Wang, Yijun Dong, Qi Lei
- Published: 2026-11-05 18:17 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two stages manifest in the low-rank increment that LoRA optimizes remains unclear. Tracking the singular spectrum and...

### 25 - Towards Foundation Decision Models: Drex

- arXiv: [2611.07854](https://arxiv.org/abs/2611.07854) | [PDF](https://arxiv.org/pdf/2611.07854) | [papers.cool](https://papers.cool/arxiv/2611.07854)
- Authors: Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, et al. (9 authors)
- Published: 2026-11-05 11:31 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency....

### 25 - Reinforcing What the Student Has Learned: Teacher-Guided On-Policy Distillation

- arXiv: [2611.07722](https://arxiv.org/abs/2611.07722) | [PDF](https://arxiv.org/pdf/2611.07722) | [papers.cool](https://papers.cool/arxiv/2611.07722)
- Authors: Bozhen Fang, Linhao Zhong, Xuehao Wang, Huanyi Zheng, Hao Chen, Chunhua Shen
- Published: 2026-11-05 09:38 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: On-policy distillation (OPD) improves language-model reasoning through dense teacher feedback on student-generated responses.We first observe an amplitude disparity in this feedback: on math reasoning responses, style-related positions exhibit 3.5 times the mean absolute teacher--student log-probability difference...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
