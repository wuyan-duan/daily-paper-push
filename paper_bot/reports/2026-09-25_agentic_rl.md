# RL / Post-Training / Agentic RL Reading Queue - 2026-09-25

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 470. Minimum score: 8.

## Top Picks

### 68 - Back to the Definition: Estimating Step-Level Advantages via Trajectory Graphs for Agentic Reinforcement Learning

- arXiv: [2609.28963](https://arxiv.org/abs/2609.28963) | [PDF](https://arxiv.org/pdf/2609.28963) | [papers.cool](https://papers.cool/arxiv/2609.28963)
- Authors: Xincheng Yao, Haobo Fu, Weiming Liu, Chongyang Zhang
- Published: 2026-09-24 03:20 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, agentic rl; rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Group-based reinforcement learning (RL) methods, such as GRPO and its variants, have become a leading paradigm for training reasoning and agentic large language models (LLMs). While their group-normalized advantage estimation is reliable at the response level, it becomes systematically biased at the step level,...

### 57 - Small yet Assistive: Spatially-Aware Post-Training for Low Vision

- arXiv: [2609.28757](https://arxiv.org/abs/2609.28757) | [PDF](https://arxiv.org/pdf/2609.28757) | [papers.cool](https://papers.cool/arxiv/2609.28757)
- Authors: Rishabh Choudhary, Shreyansh Raj, Umesh Goyal, Shubh Kashyap, Shrestha Kumar, Sushovan Jena, et al. (9 authors)
- Published: 2026-09-23 20:10 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning
- Abstract skim: An estimated 1 billion people worldwide live with vision impairment, yet current vision-language models (VLMs) produce descriptions too vague for safe navigation by blind and low-vision (BLV) users. Large VLMs can generate high-quality audio-description-compliant narrations but cannot run on mobile devices; small...

### 53 - Pistis Technical Report

- arXiv: [2609.28554](https://arxiv.org/abs/2609.28554) | [PDF](https://arxiv.org/pdf/2609.28554) | [papers.cool](https://papers.cool/arxiv/2609.28554)
- Authors: Heyun Chen, Xiaohan Lan, Jiaxi Li, Zhilin Lu, Qi She, Weiwen Xu, et al. (20 authors)
- Published: 2026-09-23 08:03 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; planning_and_action: planning, trajectory
- Abstract skim: We introduce the Pistis model family, comprising 27B- and 9B-parameter multimodal large language models built on Qwen3.6 and Qwen3.5, respectively, and developed through a general and scalable post-training framework. The framework first establishes a strong foundation through large-scale multimodal supervised fine-...

### 50 - Reinforcement Learning with Verifiable Rewards for Small Search Agents

- arXiv: [2609.28765](https://arxiv.org/abs/2609.28765) | [PDF](https://arxiv.org/pdf/2609.28765) | [papers.cool](https://papers.cool/arxiv/2609.28765)
- Authors: Gaurisankar Jayadas, Aske Plaat, Álvaro Serra-Gómez, Sandheep P
- Published: 2026-09-23 20:21 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) performs well on problems with clear rewards, such as mathematics and coding, but whether it also works where the reward is less clear remains open. The reason-over-search recipe applies RLVR to open-domain question answering, where retrieval grounds the answer...

### 46 - Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents

- arXiv: [2609.29892](https://arxiv.org/abs/2609.29892) | [PDF](https://arxiv.org/pdf/2609.29892) | [papers.cool](https://papers.cool/arxiv/2609.29892)
- Authors: Tingyu Qu, Weigao Sun, Yuecheng Liu, Yucheng Zhao, Yi Zhu, Yifeng Ding, et al. (26 authors)
- Published: 2026-09-24 14:38 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning, tool use; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: memory
- Abstract skim: The rapid progression of large language models is extending AI from passive content generation into the active workflows of engineering and scientific discovery. This shift raises a compelling question: can AI be both the object of development and an active participant in building next-generation AI systems? We...

### 46 - AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining

- arXiv: [2609.29014](https://arxiv.org/abs/2609.29014) | [PDF](https://arxiv.org/pdf/2609.29014) | [papers.cool](https://papers.cool/arxiv/2609.29014)
- Authors: Qingzhuo Wang, Zikun Wei, Zhihua Wei, Wen Shen
- Published: 2026-09-24 04:29 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training, grpo
- Abstract skim: Large language model (LLM)-based multi-agent systems can automate alpha factor mining, but their reliance on external APIs limits control over cost, availability, and confidentiality. Long research loops also tend to revisit a few successful economic mechanisms that lead to research path collapse. To address these...

### 46 - DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs

- arXiv: [2609.28570](https://arxiv.org/abs/2609.28570) | [PDF](https://arxiv.org/pdf/2609.28570) | [papers.cool](https://papers.cool/arxiv/2609.28570)
- Authors: Yingxuan Zhuang, Miao Pan, Wangjie Gan, Jingxiao Yang, Fan Wang, Weiming Liu, et al. (9 authors)
- Published: 2026-09-23 11:39 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) is widely used to sharpen reasoning in multimodal large language models (MLLMs), yet its effect on hallucination is uneven. We trace this to two weak points in the \emph{correction chain} from reward to parameter update. At the rollout level, hard queries---those with high semantic...

### 41 - Rufus-Air: An Open LLM Post-Training Recipe

- arXiv: [2609.29421](https://arxiv.org/abs/2609.29421) | [PDF](https://arxiv.org/pdf/2609.29421) | [papers.cool](https://papers.cool/arxiv/2609.29421)
- Authors: Chia-Yuan Chang, Renyuan Cheng, Rui Feng, Xiaotian Han, Yuan He, Hongye Jin, et al. (22 authors)
- Published: 2026-09-24 11:45 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, rlhf; reasoning: reasoning
- Abstract skim: Rufus-Air is an open and reproducible post-training recipe on GLM-4.5-Air-Base (106B-A12B), organized as a serial pipeline of eight stages: SFT, Reasoning RL, Coding RL, Instruction-Following RL, General Agent, Coding Agent, Search Agent, and RLHF. We document the data, reward design, infrastructure, stage order,...

### 41 - RLVR landscapes for iterated multiplications can be benign: Insights from spin-glass theory

- arXiv: [2609.28625](https://arxiv.org/abs/2609.28625) | [PDF](https://arxiv.org/pdf/2609.28625) | [papers.cool](https://papers.cool/arxiv/2609.28625)
- Authors: Noa Rubin, Zohar Ringel
- Published: 2026-09-23 18:00 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Despite the importance of reinforcement learning with verifiable rewards (RLVR), the extent to which it can learn new reasoning capabilities remains debated. Here we study the optimization landscape of RLVR on algorithmic tasks, such as iterated group and quasigroup multiplication. To this end, we map entropy-...

### 38 - Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management

- arXiv: [2609.30150](https://arxiv.org/abs/2609.30150) | [PDF](https://arxiv.org/pdf/2609.30150) | [papers.cool](https://papers.cool/arxiv/2609.30150)
- Authors: Giacomo Arcieri, Gregory Duthé, Christophe Muller, Konstantinos G. Papakonstantinou, Daniel Straub, Eleni Chatzi
- Published: 2026-09-24 17:12 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: planning, decision making; downranked: railway
- Abstract skim: Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration correlations and economies of scale. While deep reinforcement learning has shown promise in optimizing maintenance...

### 37 - Agent Memory with Episodic Retrieval for Financial Decision-Making

- arXiv: [2609.28771](https://arxiv.org/abs/2609.28771) | [PDF](https://arxiv.org/pdf/2609.28771) | [papers.cool](https://papers.cool/arxiv/2609.28771)
- Authors: Nuoyue Xu, Jiang Liu, Wenxuan Huang, Xiang Zhang, Juntai Cao, Jiaqi Wei
- Published: 2026-09-23 20:32 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent memory; reasoning: reasoning; planning_and_action: decision making; memory_and_benchmarks: memory, episodic memory, evaluation
- Abstract skim: Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their...

### 37 - Thinking Leakage: A Causal Audit of NoThink Post-Training in Hybrid Reasoning Models

- arXiv: [2609.28682](https://arxiv.org/abs/2609.28682) | [PDF](https://arxiv.org/pdf/2609.28682) | [papers.cool](https://papers.cool/arxiv/2609.28682)
- Authors: Zehao Liu, Vasant G. Honavar
- Published: 2026-09-23 18:22 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Post-training hybrid reasoning models in NoThink mode has attracted growing interest as a way to improve performance while keeping inference fast. However, these gains may draw on thinking behavior already accessible through the base model's Think mode. We formulate this thinking leakage in a causal mediation...

### 33 - Post-Training Leaves Behavioral Shadows on Unrelated Decisions

- arXiv: [2609.29233](https://arxiv.org/abs/2609.29233) | [PDF](https://arxiv.org/pdf/2609.29233) | [papers.cool](https://papers.cool/arxiv/2609.29233)
- Authors: Ziyang Zhang, Yubin Jing, Yuanhao Zeng, Yuyao Li, Haofan Wang, Yichen Gong
- Published: 2026-09-24 08:39 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: We find that language models can transfer capabilities through task-unrelated text. Post-training typically improves language models using task-specific data. Prior work on subliminal learning shows that information about these updates can pass through unrelated generations, but has largely focused on traits or...

### 32 - PoEM: Predicting RL Outcomes from Existing Policies

- arXiv: [2609.30226](https://arxiv.org/abs/2609.30226) | [PDF](https://arxiv.org/pdf/2609.30226) | [papers.cool](https://papers.cool/arxiv/2609.30226)
- Authors: Kimia Hamidieh, Giannis Daras, Antonio Torralba
- Published: 2026-09-24 17:50 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model
- Abstract skim: Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we...

### 31 - When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression

- arXiv: [2609.29875](https://arxiv.org/abs/2609.29875) | [PDF](https://arxiv.org/pdf/2609.29875) | [papers.cool](https://papers.cool/arxiv/2609.29875)
- Authors: Mingxuan Wang, Fei Luo, Bo Wang, Guorun Yao, Yinglong Guo, Chao Ning, et al. (9 authors)
- Published: 2026-09-24 14:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: long-horizon agent; reasoning: reasoning, chain-of-thought, chain of thought; planning_and_action: trajectory
- Abstract skim: Long horizon language model agents continually accumulate reasoning history, increasing context length and inference cost even after earlier decisions have been executed and observed. Unlike static Chain of Thought compression, removing historical reasoning can change future actions and the resulting interaction...

### 29 - CounterRoute: Self-Routed Reasoning via Hierarchical Counterfactual Credit Assignment

- arXiv: [2609.29109](https://arxiv.org/abs/2609.29109) | [PDF](https://arxiv.org/pdf/2609.29109) | [papers.cool](https://papers.cool/arxiv/2609.29109)
- Authors: Ruochen Jiao, Besnik Fetahu, Zhenyu Shi, Priyanka Nigam
- Published: 2026-09-24 06:39 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning
- Abstract skim: Reasoning-capable language models often produce long chains of thought when direct answers suffice, wasting inference compute. Many dual-mode models leave this choice to users. Automating it is challenging because routing targets evolve with the policy, initial mode preferences destabilize exploration, and sequence-...

### 29 - SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL

- arXiv: [2609.29050](https://arxiv.org/abs/2609.29050) | [PDF](https://arxiv.org/pdf/2609.29050) | [papers.cool](https://papers.cool/arxiv/2609.29050)
- Authors: Yan Zhan, Shaobo Liu, Qiunan Liu, Yuanjun Shi, Siqi Xu, WeiYi Hou, et al. (10 authors)
- Published: 2026-09-24 05:31 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Tool-calling agents produce heterogeneous outputs, interleaving structured tool invocations with user-facing natural language summaries. This output heterogeneity presents a structural failure mode in standard on-policy Reinforcement Learning (RL): algorithms like GRPO indiscriminately broadcast a homogeneous...

### 28 - From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative Recommendation

- arXiv: [2609.29983](https://arxiv.org/abs/2609.29983) | [PDF](https://arxiv.org/pdf/2609.29983) | [papers.cool](https://papers.cool/arxiv/2609.29983)
- Authors: Mengdan Zhu, Yufan Zhao, Yao Zhao, Sophie Di, Tao Di, Yulan Yan, et al. (8 authors)
- Published: 2026-09-24 15:34 UTC | Categories: cs.AI
- Why it matched: rl_post_training: policy optimization, group relative policy optimization; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Semantic IDs (SIDs) encode each catalog item as a short token sequence, enabling generative recommenders to predict the next item autoregressively. Reasoning-enhanced variants, an increasingly common extension, first generate a textual trace and then decode a next-item SID by beam search. Such recommenders are...

### 28 - MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks

- arXiv: [2609.29015](https://arxiv.org/abs/2609.29015) | [PDF](https://arxiv.org/pdf/2609.29015) | [papers.cool](https://papers.cool/arxiv/2609.29015)
- Authors: Keru Chen, Sen Lin, Yingbin Liang, Nathaniel D. Bastian, Shaofeng Zou
- Published: 2026-09-24 04:29 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: llm agent, multi-agent; reasoning: deliberation; memory_and_benchmarks: evaluation
- Abstract skim: Decentralized LLM-based multi-agent systems coordinate through local interactions, but an agent can remain responsive while its task-solving quality persistently degrades. Such gray failures require protecting current tasks before sufficient evidence exists to alter future routing, while still allowing recovered...

### 27 - Breaking the Environment Wall: Evolving LLM Agent Environments for Recursive Self-Improvement

- arXiv: [2609.29773](https://arxiv.org/abs/2609.29773) | [PDF](https://arxiv.org/pdf/2609.29773) | [papers.cool](https://papers.cool/arxiv/2609.29773)
- Authors: Yukai Wu, Yuanjing Yang, Le Zhou, Shaokun Han, Haoyu Wang, Zirui Tang, et al. (10 authors)
- Published: 2026-09-24 13:17 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; reasoning: self-improvement, self improvement; planning_and_action: trajectory
- Abstract skim: Many real-world tasks (e.g., office workflows, scientific experimentation) require LLM agents to interact repeatedly with their environments for context-dependent operations. However, such environments are often not agent-ready. First, information is often scattered and fragmented across the environment. Second,...

### 25 - AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control

- arXiv: [2609.30264](https://arxiv.org/abs/2609.30264) | [PDF](https://arxiv.org/pdf/2609.30264) | [papers.cool](https://papers.cool/arxiv/2609.30264)
- Authors: Jiabin Qiu, Zixuan Chen, Hongye Cao, Jieqi Shi, Jing Huo, Yang Gao
- Published: 2026-09-24 17:59 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training; planning_and_action: planning, world model
- Abstract skim: Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low factual prediction error yet poorly distinguish candidate actions. We introduce AD-WM, an action-discriminative...

### 24 - Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning

- arXiv: [2609.30258](https://arxiv.org/abs/2609.30258) | [PDF](https://arxiv.org/pdf/2609.30258) | [papers.cool](https://papers.cool/arxiv/2609.30258)
- Authors: Sudip Bhujel, Shanghao Shi, Ruiquan Huang, Ning Zhang, Yang Xiao
- Published: 2026-09-24 17:59 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal structure can amplify this leakage beyond single-frame attacks. We introduce Temporal Reconstruction Attack on...

### 24 - Transcript-Supervised Post-Training of Generative Speech Enhancement on Real Recordings via Reinforce Adjoint Matching

- arXiv: [2609.29405](https://arxiv.org/abs/2609.29405) | [PDF](https://arxiv.org/pdf/2609.29405) | [papers.cool](https://papers.cool/arxiv/2609.29405)
- Authors: Julius Richter, Christoph Boeddeker, Yoshiki Masuyama, Kohei Saijo, Dominik Klement, Gordon Wichern, et al. (7 authors)
- Published: 2026-09-24 11:30 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training
- Abstract skim: We adapt Reinforce Adjoint Matching (RAM), a reward-based post-training method, to generative speech enhancement (SE). Starting from a pretrained SE model, RAM tilts the model's conditional distribution toward outputs with higher reward. During training, the current model generates enhanced speech on-policy,...

### 24 - From Self-Distillation to Self-Practice: Privileged Information for Multi-Turn Agents

- arXiv: [2609.29051](https://arxiv.org/abs/2609.29051) | [PDF](https://arxiv.org/pdf/2609.29051) | [papers.cool](https://papers.cool/arxiv/2609.29051)
- Authors: Xingyu Su, Abhishek Kumar, Qing Ping, Youzhi Luo, Jonathan Buck, Zach Zhang, et al. (8 authors)
- Published: 2026-09-24 05:32 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, grpo
- Abstract skim: On-policy self-distillation (OPSD) has become a popular recipe for post-training LLM agents. It supervises the agent model at the token level with a stronger teacher view of the same model, obtained by conditioning on privileged information (PI). In this work, we show that in multi-turn agents, this paradigm teaches...

### 24 - Multi-Agent Orchestration of 3GPP Channel Estimators

- arXiv: [2609.29044](https://arxiv.org/abs/2609.29044) | [PDF](https://arxiv.org/pdf/2609.29044) | [papers.cool](https://papers.cool/arxiv/2609.29044)
- Authors: I. Zakir Ahmed, Hamid Sadjadpour
- Published: 2026-09-24 05:23 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent orchestration
- Abstract skim: Pilot-aided channel estimation is a decisive block in orthogonal frequency-division multiplexing (OFDM) receivers for both 5G New Radio (5G-NR) and Long-Term Evolution (LTE). A large body of estimators exists, from simple least-squares (LS) interpolation to statistically optimal linear minimum-mean-square-error...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
