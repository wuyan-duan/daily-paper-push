# RL / Post-Training / Agentic RL Reading Queue - 2026-08-08

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 348. Minimum score: 8.

## Top Picks

### 69 - EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning

- arXiv: [2608.06197](https://arxiv.org/abs/2608.06197) | [PDF](https://arxiv.org/pdf/2608.06197) | [papers.cool](https://papers.cool/arxiv/2608.06197)
- Authors: Zishan Xu, Zhiyuan Yao, Yuxin Chen, Yifu Guo, Zhengxi Lu, Yuquan Lu, et al. (12 authors)
- Published: 2026-08-06 15:54 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, llm agent, tool use, agent training; rl_post_training: reinforcement learning; planning_and_action: acting, decision making, world model; memory_and_benchmarks: evaluation
- Abstract skim: Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to ground. We introduce EnvACE, an agentic reinforcement learning method that...

### 61 - AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

- arXiv: [2608.05987](https://arxiv.org/abs/2608.05987) | [PDF](https://arxiv.org/pdf/2608.05987) | [papers.cool](https://papers.cool/arxiv/2608.05987)
- Authors: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, et al. (13 authors)
- Published: 2026-08-06 13:00 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, policy optimization, grpo; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser...

### 61 - In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use

- arXiv: [2608.05738](https://arxiv.org/abs/2608.05738) | [PDF](https://arxiv.org/pdf/2608.05738) | [papers.cool](https://papers.cool/arxiv/2608.05738)
- Authors: Jiarui Yang, Wen Huang, Jiale Zhang, Maowei Hu, Hang Guo
- Published: 2026-08-06 08:21 UTC | Categories: cs.RO
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Vision-Language-Action (VLA) models have become the dominant recipe for generalist manipulation, yet they are almost universally trained by behavior cloning: a policy imitates expert action chunks conditioned on a static image and a fixed instruction. A natural remedy is to inject explicit reasoning through textual...

### 52 - When Agentic AI Meets Integrated Sensing and Communication

- arXiv: [2608.05792](https://arxiv.org/abs/2608.05792) | [PDF](https://arxiv.org/pdf/2608.05792) | [papers.cool](https://papers.cool/arxiv/2608.05792)
- Authors: Kai Li, Conggai Li, Sarah Ali Siddiqui, Syed Sohail Ahmed, Xin Yuan, Shenghong Li, et al. (7 authors)
- Published: 2026-08-06 09:26 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, tool use, agent collaboration; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: evaluation
- Abstract skim: Agentic artificial intelligence (AI) is transforming Integrated Sensing and Communication (ISAC) from a function-oriented physical-layer technology into a goal-driven, closed-loop intelligent system, a paradigm we term AISAC. Existing work on learning-based sensing, resource allocation, reconfigurable intelligent...

### 47 - Contextual Information Policy Optimization for Search Agents

- arXiv: [2608.06128](https://arxiv.org/abs/2608.06128) | [PDF](https://arxiv.org/pdf/2608.06128) | [papers.cool](https://papers.cool/arxiv/2608.06128)
- Authors: Xingyu Guo, Wei Chen, Linlin Yang, Baochang Zhang
- Published: 2026-08-06 15:01 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model; reasoning: reasoning, outcome reward; memory_and_benchmarks: memory
- Abstract skim: Search agents extend large language models beyond static parametric memory by enabling them to acquire and use ex ternal evidence during multi-step reasoning. For knowledge intensive tasks involving complex or evolving information, their reliability depends not only on retrieving relevant ev idence but also on using...

### 46 - Multi-Agent Reinforcement Learning for Online Traffic Scheduling in Time-Sensitive Application

- arXiv: [2608.05346](https://arxiv.org/abs/2608.05346) | [PDF](https://arxiv.org/pdf/2608.05346) | [papers.cool](https://papers.cool/arxiv/2608.05346)
- Authors: Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
- Published: 2026-08-05 19:06 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, autonomous agent; rl_post_training: reinforcement learning, policy optimization; downranked: traffic
- Abstract skim: Time-sensitive networking (TSN) is increasingly integrated into mobile edge computing (MEC) to support applications with stringent latency requirements, such as extended reality (XR). However, existing TSN scheduling solutions predominantly rely on static optimization techniques or centralized learning models that...

### 45 - Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations

- arXiv: [2608.05588](https://arxiv.org/abs/2608.05588) | [PDF](https://arxiv.org/pdf/2608.05588) | [papers.cool](https://papers.cool/arxiv/2608.05588)
- Authors: He Jiang, Jingtian Yan, Yulun Zhang, Yimin Tang, Tanishq Duhan, Rishi Veerapaneni, et al. (8 authors)
- Published: 2026-08-06 04:17 UTC | Categories: cs.AI, cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent, agent environment; rl_post_training: reinforcement learning; planning_and_action: planning
- Abstract skim: Lifelong Multi-Agent Path Finding (LMAPF) requires repeatedly planning collision-free paths for agents that continuously receive new goals upon reaching their current ones. While many learning-based planners have been proposed for LMAPF, most rely on oversimplified kinematic assumptions that may overlook motion...

### 44 - Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level Goal Rewarding

- arXiv: [2608.05832](https://arxiv.org/abs/2608.05832) | [PDF](https://arxiv.org/pdf/2608.05832) | [papers.cool](https://papers.cool/arxiv/2608.05832)
- Authors: Xiaofeng Wang, Kakam Chong, Shuai Xiao, DeXin Kong, Qingyuan Tian, Chen Ju, et al. (12 authors)
- Published: 2026-08-06 10:00 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: Large language models (LLMs) excel in structured tasks but struggle with dynamic social interactions, where success requires long-term goal coordination and rapid adaptation. Current methods often apply uniform goal-based rewards to every utterance, overlooking the specificity of objectives at each dialogue turn and...

### 37 - On-Policy Delta Distillation for Multilingual Math Reasoning

- arXiv: [2608.05802](https://arxiv.org/abs/2608.05802) | [PDF](https://arxiv.org/pdf/2608.05802) | [papers.cool](https://papers.cool/arxiv/2608.05802)
- Authors: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- Published: 2026-08-06 09:37 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored. We study OPD and its advanced variant, On-Policy Delta Distillation (OPD$^2$), for mathematical reasoning in English, Korean, and...

### 35 - Learning When to Trust via Selective Context Preference Optimization

- arXiv: [2608.06377](https://arxiv.org/abs/2608.06377) | [PDF](https://arxiv.org/pdf/2608.06377) | [papers.cool](https://papers.cool/arxiv/2608.06377)
- Authors: Xian Sun, Wei Chow, Yingshuo Wang, Junhao Liu, Wei Gao, Qing Wu, et al. (7 authors)
- Published: 2026-08-06 17:59 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: preference optimization, dpo; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. We...

### 35 - Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation

- arXiv: [2608.05999](https://arxiv.org/abs/2608.05999) | [PDF](https://arxiv.org/pdf/2608.05999) | [papers.cool](https://papers.cool/arxiv/2608.05999)
- Authors: He Kong, Zengjue Chen, Qi Wang, Qianli Xing, Runliang Niu, Peidong Liu, et al. (9 authors)
- Published: 2026-08-06 13:07 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: planning
- Abstract skim: Vision-language-action (VLA) models have demonstrated remarkable capabilities in robotic manipulation by leveraging pretrained vision-language models. However, existing post-training methods predominantly optimize VLA models as flat policies, making it difficult to explicitly model task progression and perform...

### 35 - LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction

- arXiv: [2608.05600](https://arxiv.org/abs/2608.05600) | [PDF](https://arxiv.org/pdf/2608.05600) | [papers.cool](https://papers.cool/arxiv/2608.05600)
- Authors: Yingqing Guo, Hui Yuan, Zijian He, Mengdi Wang, Zheng Ding
- Published: 2026-08-06 04:47 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; planning_and_action: rollout
- Abstract skim: Flow-based generative models are typically sampled by solving a deterministic ordinary differential equation (ODE), whereas online reinforcement learning requires stochastic rollouts for policy exploration and optimization. Existing GRPO methods for flow models therefore replace the inference-time ODE with a...

### 34 - DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models

- arXiv: [2608.06243](https://arxiv.org/abs/2608.06243) | [PDF](https://arxiv.org/pdf/2608.06243) | [papers.cool](https://papers.cool/arxiv/2608.06243)
- Authors: ZhiYan Hou, Xinyu Tang, Hongyan An, Jianjin Zhang, Weizhen Wang, Yunyun Han, et al. (12 authors)
- Published: 2026-08-06 16:29 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models using automatically verifiable outcome signals, but these signals are typically sparse and at the sequence-level. On-policy self-distillation (OPSD) mitigates this sparsity by querying a privileged...

### 34 - iARCS: Iterative Agentic RL for Controllable 3D Scene Generation

- arXiv: [2608.06161](https://arxiv.org/abs/2608.06161) | [PDF](https://arxiv.org/pdf/2608.06161) | [papers.cool](https://papers.cool/arxiv/2608.06161)
- Authors: Saugat Adhikari, Ashok Prasad Neupane, Pramish Paudel, Ajad Chhatkuli, Danda Pani Paudel
- Published: 2026-08-06 15:30 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning
- Abstract skim: Synthetic 3D scene generation is increasingly used as a data source for computer vision and embodied AI, but existing generators often optimize perceptual realism without reliably satisfying task-critical functional constraints. This mismatch limits the usefulness of synthetic data for downstream training, where...

### 28 - OrchestraBench: Evaluating Multi-Agent Orchestration Failure Modes, Recovery, and Decomposition Quality

- arXiv: [2608.05263](https://arxiv.org/abs/2608.05263) | [PDF](https://arxiv.org/pdf/2608.05263) | [papers.cool](https://papers.cool/arxiv/2608.05263)
- Authors: Yidian Chen, Yingzi Gu, Natan Vidra, Spurthi Setty, Sharon Zheng
- Published: 2026-08-05 17:27 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent orchestration; reasoning: reasoning
- Abstract skim: Multi-agent orchestration frameworks are moving from demos to production, yet benchmarks typically report task accuracy without diagnosing why a pipeline failed, where a cascade began, or which routing decision caused the breakdown. OrchestraBench evaluates failure, recovery, and decomposition through a controlled,...

### 27 - TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories

- arXiv: [2608.06346](https://arxiv.org/abs/2608.06346) | [PDF](https://arxiv.org/pdf/2608.06346) | [papers.cool](https://papers.cool/arxiv/2608.06346)
- Authors: Yunjia Qi, Zehua Yin, Xintong Shi, Hao Peng, Songyuanyi Lu, Yixian Liu, et al. (13 authors)
- Published: 2026-08-06 17:51 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use, long-horizon agent; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest error step in a failed trajectory that is responsible for the final failure. However, progress faces two main...

### 26 - A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance

- arXiv: [2608.06246](https://arxiv.org/abs/2608.06246) | [PDF](https://arxiv.org/pdf/2608.06246) | [papers.cool](https://papers.cool/arxiv/2608.06246)
- Authors: Fardin Afdideh, Fernando Seoane, Farhad Abtahi
- Published: 2026-08-06 16:32 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: evaluation
- Abstract skim: Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains...

### 25 - RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction

- arXiv: [2608.06310](https://arxiv.org/abs/2608.06310) | [PDF](https://arxiv.org/pdf/2608.06310) | [papers.cool](https://papers.cool/arxiv/2608.06310)
- Authors: Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, et al. (12 authors)
- Published: 2026-08-06 17:24 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative reward models have not realized their potential in reinforcement learning (RL). Our analysis reveals that this limitation...

### 24 - On-Policy Self-Distillation without Any Supervision

- arXiv: [2608.06296](https://arxiv.org/abs/2608.06296) | [PDF](https://arxiv.org/pdf/2608.06296) | [papers.cool](https://papers.cool/arxiv/2608.06296)
- Authors: Yijiang Li, Bingyang Wang, Yijun Liang, Yunjie Tian, Di Fu, Nuno Vasconcelos
- Published: 2026-08-06 17:18 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, grpo
- Abstract skim: On-policy (Self-)Distillation (OPD / OPSD) has shown strong potential for post-training large language models (LLMs). However, existing methods still rely heavily on external supervision, including ground-truth signals, environmental feedback, or guidance from larger models, and therefore fall short of genuine...

### 24 - Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning

- arXiv: [2608.05643](https://arxiv.org/abs/2608.05643) | [PDF](https://arxiv.org/pdf/2608.05643) | [papers.cool](https://papers.cool/arxiv/2608.05643)
- Authors: Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Lena Trigg, Ali Subhan, Muhammad Ali, et al. (7 authors)
- Published: 2026-08-06 06:38 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reward model; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Test-time scaling improves LLM reasoning by using additional inference compute, but wider sampling alone can suffer from diminishing returns: new rollouts often repeat existing answer patterns instead of adding useful reasoning diversity. Verifier-based selection offers an alternative, but its performance depends on...

### 24 - Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation

- arXiv: [2608.05341](https://arxiv.org/abs/2608.05341) | [PDF](https://arxiv.org/pdf/2608.05341) | [papers.cool](https://papers.cool/arxiv/2608.05341)
- Authors: Yuta Kobayashi, Pradyun Ramesh, Muhammad Ahmed Chaudhry, Vincent Jeanselme, Judy Wawira Gichoya, Sanmi Koyejo, et al. (8 authors)
- Published: 2026-08-05 18:59 UTC | Categories: cs.LG
- Why it matched: rl_post_training: preference optimization, dpo
- Abstract skim: Vision-Language Models (VLMs) for radiology report generation are typically trained on retrospective clinical reports, which suffer from omission noise: clinically present findings are left unreported due to the omission of subtle findings. For example, prior studies show that cardiomegaly may be omitted from ICU...

### 24 - Multi-Agent Transformer for Queue-Level XR Traffic Scheduling in TSN Networks

- arXiv: [2608.05340](https://arxiv.org/abs/2608.05340) | [PDF](https://arxiv.org/pdf/2608.05340) | [papers.cool](https://papers.cool/arxiv/2608.05340)
- Authors: Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
- Published: 2026-08-05 18:57 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; downranked: traffic
- Abstract skim: Time-Sensitive Networking (TSN) and Mobile Edge Computing (MEC) hold strong potential for enabling ultra-reliable low-latency communication for time-sensitive applications, such as eXtended Reality (XR). However, the widespread adoption of XR introduces significant challenges due to co-located services in MEC...

### 23 - When History Lies: Evaluating and Improving Tool Use under Misleading Multi-Turn Histories

- arXiv: [2608.06057](https://arxiv.org/abs/2608.06057) | [PDF](https://arxiv.org/pdf/2608.06057) | [papers.cool](https://papers.cool/arxiv/2608.06057)
- Authors: Xiaoqing Wu, Xingyu Fan, Feifei Li, Wenhui Que
- Published: 2026-08-06 14:04 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; planning_and_action: trajectory; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Tool-calling agents infer task state from accumulated dialogue and tool traces. In persistent interactions, however, historical traces may remain structurally valid and semantically plausible after they cease to be authoritative for the current request. We show that such history can hijack a policy the model already...

### 22 - Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay

- arXiv: [2608.05784](https://arxiv.org/abs/2608.05784) | [PDF](https://arxiv.org/pdf/2608.05784) | [papers.cool](https://papers.cool/arxiv/2608.05784)
- Authors: Nossa Iyamu
- Published: 2026-08-06 09:17 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agent memory; memory_and_benchmarks: memory, evaluation
- Abstract skim: Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the user did. We compile passively captured screen activity into agent memory with a deterministic, zero-model pipeline: it segments a local...

### 22 - SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution

- arXiv: [2608.05573](https://arxiv.org/abs/2608.05573) | [PDF](https://arxiv.org/pdf/2608.05573) | [papers.cool](https://papers.cool/arxiv/2608.05573)
- Authors: Zhi Han, Chenxi Zeng, Liuhaichen Yang, Zihan Guo, Ming Zhou, Yang Li
- Published: 2026-08-06 03:52 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; planning_and_action: trajectory, rollout; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: LLM agents increasingly execute long-horizon tasks through tool use and environment interaction, shifting evaluation from final-response scoring to verification of complete executions. For skill-augmented agents, verification additionally requires the procedural knowledge encoded in task-time skills, because this...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
