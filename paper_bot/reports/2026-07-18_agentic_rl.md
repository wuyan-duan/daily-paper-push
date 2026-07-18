# RL / Post-Training / Agentic RL Reading Queue - 2026-07-18

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 341. Minimum score: 8.

## Top Picks

### 88 - Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning

- arXiv: [2607.14171](https://arxiv.org/abs/2607.14171) | [PDF](https://arxiv.org/pdf/2607.14171) | [papers.cool](https://papers.cool/arxiv/2607.14171)
- Authors: Bowei He, Yankai Chen, Xiaokun Zhang, Xue Liu
- Published: 2026-07-15 09:37 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: language agent; rl_post_training: reinforcement learning, rlhf, policy optimization, grpo, +1 more; planning_and_action: trajectory, rollout; memory_and_benchmarks: alfworld
- Abstract skim: Reinforcement learning has emerged as the dominant paradigm for training large language model (LLM) agents that interact with executable sandboxes. State-of-the-art algorithms such as PPO, RLOO, and GRPO inherit their rollout topology from RLHF: for each prompt, N independent trajectories are sampled from the...

### 76 - A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models

- arXiv: [2607.14522](https://arxiv.org/abs/2607.14522) | [PDF](https://arxiv.org/pdf/2607.14522) | [papers.cool](https://papers.cool/arxiv/2607.14522)
- Authors: Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang
- Published: 2026-07-16 03:19 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +3 more; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: We formulate reinforcement learning (RL) in continuous time with discrete state spaces and possibly arbitrary action spaces via a stochastic control approach, where the state dynamics are modeled as a controlled continuous-time Markov chain (CTMC). We consider policy optimization problems and derive the...

### 69 - Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment

- arXiv: [2607.14682](https://arxiv.org/abs/2607.14682) | [PDF](https://arxiv.org/pdf/2607.14682) | [papers.cool](https://papers.cool/arxiv/2607.14682)
- Authors: Harikrishnan P M, Goutham Vignesh, Ganesh Parab, Saisubramaniam Gopalakrishnan, Vishal Vaddina, Varun V, et al. (7 authors)
- Published: 2026-07-16 07:43 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; reasoning: reasoning
- Abstract skim: Efficient multimodal document question answering with explicit visual grounding, locating the precise document region that supports each answer remains an open challenge. Current approaches bifurcate into Supervised Fine-Tuning (SFT), which requires large annotated datasets and reaches optimization plateaus, and...

### 59 - ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability

- arXiv: [2607.14145](https://arxiv.org/abs/2607.14145) | [PDF](https://arxiv.org/pdf/2607.14145) | [papers.cool](https://papers.cool/arxiv/2607.14145)
- Authors: Weiting Liu, Jieyi Bi, Wanqi Zhou, Jianfeng Feng, Yining Ma, Ai Han, et al. (7 authors)
- Published: 2026-07-14 06:03 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning, tool use; rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; memory_and_benchmarks: gaia
- Abstract skim: Tool-augmented large language model agents excel at long-horizon tasks, yet they are typically post-trained on fixed toolsets. When tasks demand new tools, these agents struggle to incorporate them effectively, and retraining from scratch is often impractical. We identify the core obstacle in such toolset expansion...

### 54 - Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents

- arXiv: [2607.15095](https://arxiv.org/abs/2607.15095) | [PDF](https://arxiv.org/pdf/2607.15095) | [papers.cool](https://papers.cool/arxiv/2607.15095)
- Authors: Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel
- Published: 2026-07-16 15:08 UTC | Categories: cs.AI, cs.CL, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf, preference optimization, +1 more
- Abstract skim: The formation of political coalitions is a complex negotiation driven by both concrete policy objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new avenues for computational political science, the neutrality and helpfulness biases instilled by Reinforcement Learning from...

### 51 - SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

- arXiv: [2607.14777](https://arxiv.org/abs/2607.14777) | [PDF](https://arxiv.org/pdf/2607.14777) | [papers.cool](https://papers.cool/arxiv/2607.14777)
- Authors: Jinyang Wu, Shuo Yang, Zhengxi Lu, Fan Zhang, Yuhao Shen, Lang Feng, et al. (11 authors)
- Published: 2026-07-16 09:57 UTC | Categories: cs.CL
- Why it matched: agentic_rl: agentic reinforcement learning, tool use; rl_post_training: reinforcement learning; planning_and_action: trajectory, environment feedback, decision making
- Abstract skim: Large language models are increasingly trained as interactive agents for long-horizon tasks involving multi-turn interaction, tool use, and environment feedback. Outcome-based reinforcement learning (RL) provides a practical optimization paradigm, but its sparse trajectory-level rewards offer limited guidance on...

### 49 - SD-MAR: Multi-image Analytical Reasoning via Synthetic Data and Reinforcement Learning

- arXiv: [2607.14333](https://arxiv.org/abs/2607.14333) | [PDF](https://arxiv.org/pdf/2607.14333) | [papers.cool](https://papers.cool/arxiv/2607.14333)
- Authors: Shiyu Yuan, Sourav Sanjukta Bhabesh, Zhe Wang, Dmitriy Bespalov, Wesley Rose, Huzefa Rangwala
- Published: 2026-07-15 19:55 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Vision Language Models (VLMs) demonstrate strong perceptual abilities but remain limited in tasks requiring analytical reasoning across multiple visual states, such as multi-image comparison, change detection, and multi-step visual inference. These capabilities are critical for real-world multimodal applications...

### 43 - Step-Level Preference Learning for Generative Agents in Social Simulations

- arXiv: [2607.14485](https://arxiv.org/abs/2607.14485) | [PDF](https://arxiv.org/pdf/2607.14485) | [papers.cool](https://papers.cool/arxiv/2607.14485)
- Authors: Wenchang Gao, Pingyue Sheng, Lanlan Qiu, Yunfei Ma, Jian Zhao, Baicheng Chen, et al. (10 authors)
- Published: 2026-07-16 01:58 UTC | Categories: cs.AI
- Why it matched: agentic_rl: long-horizon agent; rl_post_training: preference optimization; reasoning: reflection; planning_and_action: planning, decision making; memory_and_benchmarks: memory
- Abstract skim: Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning, memory retrieval, reflection, and action selection. However, fine-grained human annotations of these intermediate steps remain scarce, and...

### 42 - LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget

- arXiv: [2607.14952](https://arxiv.org/abs/2607.14952) | [PDF](https://arxiv.org/pdf/2607.14952) | [papers.cool](https://papers.cool/arxiv/2607.14952)
- Authors: Changhai Zhou, Kieran Liu, Yuhua Zhou, Qian Qiao, Jun Gao, Harry Zhang, et al. (20 authors)
- Published: 2026-07-16 13:00 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization, +1 more; memory_and_benchmarks: memory
- Abstract skim: A growing gap separates inference context lengths from RL post-training: inference systems are approaching million-token contexts, while post-training workloads often remain at 256K tokens or below and rely on length generalization at deployment. The gap is especially important for AI agents, whose observations,...

### 40 - ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System

- arXiv: [2607.14178](https://arxiv.org/abs/2607.14178) | [PDF](https://arxiv.org/pdf/2607.14178) | [papers.cool](https://papers.cool/arxiv/2607.14178)
- Authors: Yutong He, Daibo Li, Guohong Li, Jiahe Geng, Zhengyang Huang, Can Ren, et al. (18 authors)
- Published: 2026-07-15 13:27 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent, autonomous agent; reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: evaluation
- Abstract skim: Recent advances in Large Language Models have fueled autonomous AI agents capable of tackling complex scientific tasks, yet existing automated research systems remain predominantly focused on empirically driven domains with quantitative benchmarks, leaving theory-driven discovery, particularly in mathematically...

### 34 - A Noise-Robust Elicit-to-Optimize Framework for Distortion Riskmetrics via Inverse Reinforcement Learning

- arXiv: [2607.14373](https://arxiv.org/abs/2607.14373) | [PDF](https://arxiv.org/pdf/2607.14373) | [papers.cool](https://papers.cool/arxiv/2607.14373)
- Authors: Yang Liu, Yuhao Liu, Yunran Wei
- Published: 2026-07-15 21:22 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: We propose a noise-robust elicit-to-optimize framework that integrates inverse reinforcement learning (IRL) and reinforcement learning (RL) for eliciting agents' risk preferences and optimizing policies under a broad class of risk objectives characterized by distortion riskmetrics. On the elicitation side, we...

### 33 - On-Policy Delta Distillation

- arXiv: [2607.15161](https://arxiv.org/abs/2607.15161) | [PDF](https://arxiv.org/pdf/2607.15161) | [papers.cool](https://papers.cool/arxiv/2607.15161)
- Authors: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- Published: 2026-07-16 16:07 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: On-policy distillation is an alternative post-training method in reinforcement learning that alleviates the constraints imposed by reward models by providing token-level supervision from a teacher model. Although on-policy distillation has been studied and applied across various settings, its fundamental design...

### 33 - Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards

- arXiv: [2607.14506](https://arxiv.org/abs/2607.14506) | [PDF](https://arxiv.org/pdf/2607.14506) | [papers.cool](https://papers.cool/arxiv/2607.14506)
- Authors: Yuxuan Zhu, Rohan Alur, Daniel Kang
- Published: 2026-07-16 02:42 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: While reinforcement learning with verifiable rewards (RLVR) is widely used to improve the reasoning capabilities of large language models (LLMs), the generalizability of the resulting models remains poorly understood. In this work, we establish the first non-vacuous generalization bounds for parameter-efficient RLVR...

### 32 - Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy Optimization

- arXiv: [2607.14614](https://arxiv.org/abs/2607.14614) | [PDF](https://arxiv.org/pdf/2607.14614) | [papers.cool](https://papers.cool/arxiv/2607.14614)
- Authors: Weiwen Xu, Jia Liu, Hou Pong Chan, Long Li, Deng Cai, Min Chen, et al. (7 authors)
- Published: 2026-07-16 06:25 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) commonly uses entropy for advantage shaping. However, entropy cannot distinguish useful uncertainty from detrimental confusion, limiting its effectiveness as a correctness signal. We propose Contrastive Policy Optimization (CPO), which uses token-level...

### 29 - NavCMPO: Critic-Guided MeanFlow Policy Optimization for Adaptive Navigation

- arXiv: [2607.14643](https://arxiv.org/abs/2607.14643) | [PDF](https://arxiv.org/pdf/2607.14643) | [papers.cool](https://papers.cool/arxiv/2607.14643)
- Authors: Junjie An, Yi Wu, Xiao Liu, Yiqun Zhou, Yuechen Wu, Xiaoqing Guan, et al. (8 authors)
- Published: 2026-07-16 07:10 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: End-to-end diffusion-based policies have demonstrated strong performance in mapless visual navigation, but their iterative denoising process introduces substantial inference latency, while behavior cloning limits performance to the quality of expert demonstrations. We present NavCMPO, a two-stage adaptive navigation...

### 28 - Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making

- arXiv: [2607.14277](https://arxiv.org/abs/2607.14277) | [PDF](https://arxiv.org/pdf/2607.14277) | [papers.cool](https://papers.cool/arxiv/2607.14277)
- Authors: Amirhosein Ghasemabadi, Ruichen Chen, Bahador Rashidi, Di Niu
- Published: 2026-07-15 18:36 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent, tool use; reasoning: reasoning; planning_and_action: decision making
- Abstract skim: Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction. At inference time, it is preferred that an agent can decide whether to proceed with its current reasoning, defer to a stronger model, request additional information, invoke external...

### 27 - MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers

- arXiv: [2607.14642](https://arxiv.org/abs/2607.14642) | [PDF](https://arxiv.org/pdf/2607.14642) | [papers.cool](https://papers.cool/arxiv/2607.14642)
- Authors: Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, et al. (9 authors)
- Published: 2026-07-16 07:09 UTC | Categories: cs.AI
- Why it matched: agentic_rl: llm agent; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: benchmark
- Abstract skim: As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities...

### 27 - Lyapunov Guidance: A Unified Framework for Stabilizing Generative Flows

- arXiv: [2607.14272](https://arxiv.org/abs/2607.14272) | [PDF](https://arxiv.org/pdf/2607.14272) | [papers.cool](https://papers.cool/arxiv/2607.14272)
- Authors: Jingdong Zhang, Xinze Li, Yize Jiang, Luan Yang, Minkai Xu, Junhong Liu
- Published: 2026-07-15 18:28 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: planning
- Abstract skim: Flow matching has emerged as an effective framework for learning complex data distributions, but adapting pretrained flow models to new tasks often requires computationally expensive retraining. Post-training guidance provides a more efficient alternative, but existing methods are largely heuristic and offer no...

### 26 - Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection

- arXiv: [2607.14236](https://arxiv.org/abs/2607.14236) | [PDF](https://arxiv.org/pdf/2607.14236) | [papers.cool](https://papers.cool/arxiv/2607.14236)
- Authors: Yi Wang, Wendi Chen, Zimo Wen, Han Xue, Xueqi Li, Wenye Yu, et al. (11 authors)
- Published: 2026-07-15 18:01 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: memory
- Abstract skim: Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline...

### 25 - CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking

- arXiv: [2607.15004](https://arxiv.org/abs/2607.15004) | [PDF](https://arxiv.org/pdf/2607.15004) | [papers.cool](https://papers.cool/arxiv/2607.15004)
- Authors: Ruilong Ren, Songsheng Cheng, Yunpeng Zhou, Hanxuan Chen, Xiangyue Wang, Tianle Zeng, et al. (12 authors)
- Published: 2026-07-16 13:52 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Dynamic target tracking is essential for Unmanned Aerial Vehicles (UAVs) operating in complex urban environments, where both the target and the camera viewpoint change continuously. Existing Vision-Language-Action (VLA) policies can track visible targets effectively, but their performance often degrades when...

### 24 - SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration

- arXiv: [2607.15257](https://arxiv.org/abs/2607.15257) | [PDF](https://arxiv.org/pdf/2607.15257) | [papers.cool](https://papers.cool/arxiv/2607.15257)
- Authors: Yuyao Zhang, Junjie Gao, Zhengxian Wu, Jiaming Fan, Jin Zhang, Shihan Ma, et al. (14 authors)
- Published: 2026-07-16 17:51 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent collaboration; memory_and_benchmarks: memory
- Abstract skim: Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents. However, as interaction histories grow, agents increasingly struggle to track task progress. When search attempts fail to yield useful evidence, current single- and multi-agent systems can...

### 24 - BrainPilot: Automating Brain Discovery with Agentic Research

- arXiv: [2607.15079](https://arxiv.org/abs/2607.15079) | [PDF](https://arxiv.org/pdf/2607.15079) | [papers.cool](https://papers.cool/arxiv/2607.15079)
- Authors: Haoxuan Li, Tianci Gao, Jianhe Li, Yang Fan, Runze Shi, Weiran Wang, et al. (16 authors)
- Published: 2026-07-16 14:49 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, tool use; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Understanding the brain increasingly depends on integrating evidence across scales, modalities, and disciplines. Addressing a single research question therefore requires a coordinated sequence of operations, from surveying prior work to executing analyses and interpreting results in light of domain knowledge. AI...

### 24 - RetroAgent: Harnessing LLMs to Search Over Structured Memory for Agentic Retrosynthesis Planning

- arXiv: [2607.14512](https://arxiv.org/abs/2607.14512) | [PDF](https://arxiv.org/pdf/2607.14512) | [papers.cool](https://papers.cool/arxiv/2607.14512)
- Authors: Yanqiao Zhu, Jingru Gan, Xiaoqi Sun, Fang Sun, Yidan Shi, Md Mofijul Islam, et al. (11 authors)
- Published: 2026-07-16 03:05 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: llm agent; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: memory
- Abstract skim: Multi-step retrosynthesis planning seeks to decompose a target molecule into commercially available building blocks through a sequence of feasible reactions. The vast combinatorial search space makes this task challenging even for expert chemists. Traditional methods combine tree search with offline-trained value...

### 24 - MemoHarness: Agent Harnesses That Learn from Experience

- arXiv: [2607.14159](https://arxiv.org/abs/2607.14159) | [PDF](https://arxiv.org/pdf/2607.14159) | [papers.cool](https://papers.cool/arxiv/2607.14159)
- Authors: Yue Huang, Wenjie Wang, Han Bao, Yuchen Ma, Xiaonan Luo, Yi Nian, et al. (10 authors)
- Published: 2026-07-14 21:22 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: agent harness; reasoning: reasoning; memory_and_benchmarks: memory, evaluation
- Abstract skim: An agent harness is the external control layer that turns a base LLM into an executable agent by managing context, tools, orchestration, memory, decoding, and output handling. While harness design strongly affects agent behavior, most automatic improvement methods optimize narrower artifacts such as prompts,...

### 23 - Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation

- arXiv: [2607.14895](https://arxiv.org/abs/2607.14895) | [PDF](https://arxiv.org/pdf/2607.14895) | [papers.cool](https://papers.cool/arxiv/2607.14895)
- Authors: Yu-Du Feng, Niels Mündler-Sasahara, Mark Vero, Martin Vechev
- Published: 2026-07-16 12:11 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Reasoning language models (RLMs) have demonstrated impressive performance in domains such as mathematics and coding. These domains permit reliable verification of model outputs, which is important for enabling the reinforcement learning that drives RLM performance gains. However, training RLMs on domains that lack...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
