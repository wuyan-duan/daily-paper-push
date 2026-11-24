# RL / Post-Training / Agentic RL Reading Queue - 2026-11-24

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 985. Minimum score: 8.

## Top Picks

### 69 - CARE-3D: Reinforcement Learning for Evidence Grounded Agentic Reasoning in Situated 3D Scenes

- arXiv: [2611.29969](https://arxiv.org/abs/2611.29969) | [PDF](https://arxiv.org/pdf/2611.29969) | [papers.cool](https://papers.cool/arxiv/2611.29969)
- Authors: Xiaoqian Hu, Ruihong Qiu, Yanran Tang, Sen Wang
- Published: 2026-11-23 03:36 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more; reasoning: reasoning
- Abstract skim: Situated 3D reasoning requires embodied agents to interpret objects, scene geometry, and viewpoint dependent spatial relations. Existing methods learn grounded interactions from supervised traces, but largely imitate prescribed evidence acquisition patterns rather than optimizing the support that the returned...

### 66 - Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training

- arXiv: [2611.31166](https://arxiv.org/abs/2611.31166) | [PDF](https://arxiv.org/pdf/2611.31166) | [papers.cool](https://papers.cool/arxiv/2611.31166)
- Authors: Nan Chen, Soledad Villar, Soufiane Hayou
- Published: 2026-11-23 18:27 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +3 more; memory_and_benchmarks: memory
- Abstract skim: The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this...

### 63 - Learning What to Change: State-Verified Reinforcement Learning for Educational Agents

- arXiv: [2611.30559](https://arxiv.org/abs/2611.30559) | [PDF](https://arxiv.org/pdf/2611.30559) | [papers.cool](https://papers.cool/arxiv/2611.30559)
- Authors: Shengyao Wang, Siyuan Su, Siyu Song, Mengsong Wu, Yiming Luo, Wenbo Wu, et al. (8 authors)
- Published: 2026-11-23 12:04 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Persistent tutoring agents do more than answer questions: they manage course files, practice records, and learner profiles that govern future lessons. In such stateful settings, knowing what to teach does not guarantee knowing what to change. We identify a pervasive failure mode, content-state decoupling, where...

### 63 - Population-Based Post-Training for Large Language Models

- arXiv: [2611.29014](https://arxiv.org/abs/2611.29014) | [PDF](https://arxiv.org/pdf/2611.29014) | [papers.cool](https://papers.cool/arxiv/2611.29014)
- Authors: Yixuan Even Xu, Aleksei Petrenko, Raja Giryes, Jackson Hamburger, Kevin Chen, Fei Fang, et al. (8 authors)
- Published: 2026-11-21 19:50 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) is one of the most popular post-training paradigms for large language models. RLVR typically trains a single model under hyperparameters chosen before training begins, while researchers tune hyperparameters across consecutive runs. We introduce Population-Based...

### 54 - SAEPO: Sparse-Autoencoder-Guided Credit Assignment for Policy Optimization

- arXiv: [2611.29936](https://arxiv.org/abs/2611.29936) | [PDF](https://arxiv.org/pdf/2611.29936) | [papers.cool](https://papers.cool/arxiv/2611.29936)
- Authors: Yusong Zhao, Zihao Zhao, Zirui Zhang, Tunyu Zhang, Ziyan Wang, Yi Wang, et al. (8 authors)
- Published: 2026-11-23 02:54 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, grpo; reasoning: reasoning; planning_and_action: rollout; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated strong performance in improving large language model (LLM) reasoning, yet its credit-assignment signal remains coarse. Outcome verifiers provide scalable supervision by judging whether a completed response is correct, but they do not directly...

### 51 - AnchorCredit: Output-Anchored Credit Assignment for Structured Generation with Multiple Verifiable Rewards

- arXiv: [2611.30881](https://arxiv.org/abs/2611.30881) | [PDF](https://arxiv.org/pdf/2611.30881) | [papers.cool](https://papers.cool/arxiv/2611.30881)
- Authors: Gen Li, Pengyang Xie, Xiao Xiao, Chuanzhi Tong, Ziyang Ji, Zhigang Xu, et al. (11 authors)
- Published: 2026-11-23 15:48 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: In Reinforcement Learning with Verifiable Rewards (RLVR), Group Relative Policy Optimization (GRPO) and related methods typically compute group-relative advantages from response rewards and broadcast the same advantage to every generated token in a response to guide policy updates. However, we identify a systematic...

### 49 - From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning

- arXiv: [2611.30627](https://arxiv.org/abs/2611.30627) | [PDF](https://arxiv.org/pdf/2611.30627) | [papers.cool](https://papers.cool/arxiv/2611.30627)
- Authors: Kairong Han, Nuanqiao Shan, Ziyu Zhao, Xinpeng Dong, Zijing Hu, Dian Jin, et al. (11 authors)
- Published: 2026-11-23 12:57 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, reward model; reasoning: reasoning, process reward
- Abstract skim: Reinforcement learning (RL) has become an important component in large language models (LLMs). However, existing RL approaches focus on final outputs or textual solution trajectories, leading to coarse-grained rewards and unreliable reasoning. Such paradigms focus mainly on what the model outputs while overlooking...

### 49 - From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)

- arXiv: [2611.29303](https://arxiv.org/abs/2611.29303) | [PDF](https://arxiv.org/pdf/2611.29303) | [papers.cool](https://papers.cool/arxiv/2611.29303)
- Authors: Saadh Jawwadh
- Published: 2026-11-22 07:49 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, reinforcement learning from human feedback, rlhf; reasoning: reasoning, self-improvement, self improvement; memory_and_benchmarks: memory, long-term memory
- Abstract skim: The rapid proliferation of Large Language Model (LLM) research makes it increasingly difficult to distinguish incremental refinements from true paradigm shifts. This review evaluates 22 of the most influential publications spanning nearly three decades (1997-2026), organized through a causal, chronologically...

### 47 - Self-Upgrading Embodied Agents

- arXiv: [2611.31117](https://arxiv.org/abs/2611.31117) | [PDF](https://arxiv.org/pdf/2611.31117) | [papers.cool](https://papers.cool/arxiv/2611.31117)
- Authors: Jiajun Fan, Neil He, Qinglong Zheng, Changyi Yang, Tong Wei, Andy Mao, et al. (21 authors)
- Published: 2026-11-23 17:53 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reward model; reasoning: reasoning, self-improvement, self improvement, reflection; memory_and_benchmarks: memory
- Abstract skim: An embodied agent built on a language model goes to work with the weights it was given and keeps them for life. To get better, it needs more training, or reflection, memory, search or prompts that cost every step and are lost when the task changes. Editing weights by reasoning, weight-space programming, could end...

### 47 - Post-Training Agents for Long-Document Reasoning

- arXiv: [2611.30090](https://arxiv.org/abs/2611.30090) | [PDF](https://arxiv.org/pdf/2611.30090) | [papers.cool](https://papers.cool/arxiv/2611.30090)
- Authors: Sushant Mehta, Logan Ritchie, Edwin Chen
- Published: 2026-11-23 05:51 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Professional documents are a long-context workload that retrieval-style benchmarks do not capture. In a ten-domain enterprise collection, a task's evidence is spread across a source document of median length 27 pages (mean 48.8, maximum 873); a third of tasks rest mainly on charts, drawings, and maps; and 70.9%...

### 46 - Coupling-Aware Reinforcement Learning for Co-Evolving Graph Games

- arXiv: [2611.28351](https://arxiv.org/abs/2611.28351) | [PDF](https://arxiv.org/pdf/2611.28351) | [papers.cool](https://papers.cool/arxiv/2611.28351)
- Authors: Mina Kim, Guanghui Lan, Benoit Montreuil
- Published: 2026-11-20 22:01 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Building hydrogen station networks, electric vehicle charging grids, or vaccine distribution systems requires coordinating two separately operated graphs, demand-side facilities and the supply-side networks they depend on, where each operator's payoff depends on the other's choices. We formalize this as the Co-...

### 45 - From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use

- arXiv: [2611.28558](https://arxiv.org/abs/2611.28558) | [PDF](https://arxiv.org/pdf/2611.28558) | [papers.cool](https://papers.cool/arxiv/2611.28558)
- Authors: Jin Cui, Xinyue Long, Jiepeng Zhou, Boran Zhao, Pengju Ren, Hao Dong
- Published: 2026-11-21 04:24 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging. Existing tool-use reinforcement learning (RL) methods often rely on call-contingent rewards to encourage beneficial tool use, but such...

### 44 - CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting

- arXiv: [2611.31185](https://arxiv.org/abs/2611.31185) | [PDF](https://arxiv.org/pdf/2611.31185) | [papers.cool](https://papers.cool/arxiv/2611.31185)
- Authors: Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran
- Published: 2026-11-23 18:38 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, grpo, ppo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic...

### 44 - On Adaptive Step Sizes for Eligibility Traces in Deep Reinforcement Learning

- arXiv: [2611.29178](https://arxiv.org/abs/2611.29178) | [PDF](https://arxiv.org/pdf/2611.29178) | [papers.cool](https://papers.cool/arxiv/2611.29178)
- Authors: Esraa Elelimy, Martha White
- Published: 2026-11-22 03:15 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: agent environment; rl_post_training: reinforcement learning, ppo; memory_and_benchmarks: memory
- Abstract skim: Many deep reinforcement learning (RL) algorithms store agent-environment interactions in a replay buffer and later learn by sampling transitions from it. However, this approach can be memory-inefficient and can delay learning because the agent can learn from a transition only when the buffer samples it....

### 42 - STRIDE: Strategy-to-Tactics Retrieval-Guided Skill Disclosure and Evolution for Agentic Reinforcement Learning

- arXiv: [2611.28907](https://arxiv.org/abs/2611.28907) | [PDF](https://arxiv.org/pdf/2611.28907) | [papers.cool](https://papers.cool/arxiv/2611.28907)
- Authors: Shixin Hong, Wanqing Cui, Yibo Hu, Naen Xu, Zhiwei Huang, Meiguang Jin, et al. (7 authors)
- Published: 2026-11-21 16:31 UTC | Categories: cs.AI
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; memory_and_benchmarks: alfworld
- Abstract skim: Skill-augmented reinforcement learning enables LLM agents to reuse task-solving knowledge across episodes, but existing systems typically expose agents to a flat skill pool and update skills only from coarse, episode-level outcomes. This conflates two distinct uses of experience: a stable strategy that should frame...

### 41 - Bridging Blind Spots With Words: Decentralized Multi-View Spatial Reasoning via Language-Constrained Communication

- arXiv: [2611.29112](https://arxiv.org/abs/2611.29112) | [PDF](https://arxiv.org/pdf/2611.29112) | [papers.cool](https://papers.cool/arxiv/2611.29112)
- Authors: Soumyabrata Chaudhuri, Joydeep Ghosh
- Published: 2026-11-22 00:23 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: As multimodal LLMs (MLLMs) get increasingly used as collaborative partners across embodied robotics, AR/VR, and multi-user systems, spatial reasoning is now often distributed across agents with partial environment visibility, necessitating spatial reasoning integration. Prior work in language-mediated spatial...

### 39 - Tool-to-Self: Internalizing Visual Tool Capabilities via Scaffolded Reinforcement Learning

- arXiv: [2611.28564](https://arxiv.org/abs/2611.28564) | [PDF](https://arxiv.org/pdf/2611.28564) | [papers.cool](https://papers.cool/arxiv/2611.28564)
- Authors: Jin Cui, Hao Dong, Xinyue Long, Boran Zhao, Pengju Ren
- Published: 2026-11-21 04:38 UTC | Categories: cs.AI, cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead and deployment dependencies. Moreover, conventional tool-use RL can improve visual-task performance, yet the resulting tool gains are...

### 37 - VeriLogic: Reinforcement Learning over Verifiable Logical Reasoning Traces

- arXiv: [2611.29147](https://arxiv.org/abs/2611.29147) | [PDF](https://arxiv.org/pdf/2611.29147) | [papers.cool](https://papers.cool/arxiv/2611.29147)
- Authors: ZeLiang Chen, Yunyao Zhang, Xinglang Zhang, Wenbing Li, Junqing Yu, Zikai Song
- Published: 2026-11-22 01:59 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: Logical reasoning derives conclusions from premises through explicit intermediate inference steps, providing a natural basis for process-level verification and supervision. However, existing learning methods often rely on response-level outcome signals, which overlook heterogeneous correctness within the reasoning...

### 37 - Persuasion from Within: Model-Based Insider Attacks in Multi-Agent LLM Debate and Consensus

- arXiv: [2611.28660](https://arxiv.org/abs/2611.28660) | [PDF](https://arxiv.org/pdf/2611.28660) | [papers.cool](https://papers.cool/arxiv/2611.28660)
- Authors: Bangyan Ju, Xiaolin Sun, Yibin Hu, Zizhan Zheng
- Published: 2026-11-21 08:41 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: planning, decision making, world model
- Abstract skim: Large language models (LLMs) are increasingly deployed in multi-agent systems for collective decision-making, such as multi-agent debate and consensus games, in which agents exchange messages and update their answers over multiple rounds and a resolution mechanism aggregates them into a final outcome. Most multi-...

### 36 - Adopting AI Technologies without Traps: A Multi-Agent Reinforcement Learning Framework

- arXiv: [2611.30200](https://arxiv.org/abs/2611.30200) | [PDF](https://arxiv.org/pdf/2611.30200) | [papers.cool](https://papers.cool/arxiv/2611.30200)
- Authors: Jitong Yang, Avinash Reddy Mudireddy, Ziqing Lu, Huan Cai, Weiyu Xu
- Published: 2026-11-23 07:41 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: AI technologies and AI agents play increasingly important roles in human society, including in education, economics, and research. Adopting AI technologies can bring immediate, and sometimes tremendous, rewards such as through productivity boost, but they can also bring negative effects including but not limited to...

### 33 - Physical regime changes expose formula misuse in large language models

- arXiv: [2611.28669](https://arxiv.org/abs/2611.28669) | [PDF](https://arxiv.org/pdf/2611.28669) | [papers.cool](https://papers.cool/arxiv/2611.28669)
- Authors: Maohao Ran, Yanting Zhang, Chendong Ma, Jun Song
- Published: 2026-11-21 08:49 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Large language models (LLMs) are increasingly employed for scientific computing across the Earth and environmental sciences, but problems in these fields often involve distinct physical regimes. LLMs may fail to recognize these regime-dependent constraints, applying formulas outside their domains of validity and...

### 33 - MedCoast: Semantic Abstraction of Reasoning Trajectories for Test-Time Biomedical Question Answering

- arXiv: [2611.28586](https://arxiv.org/abs/2611.28586) | [PDF](https://arxiv.org/pdf/2611.28586) | [papers.cool](https://papers.cool/arxiv/2611.28586)
- Authors: Yishan Zhong, Jieru Li, Xuanzhe Ding, Shaunna Wang, Yanxin Yang, Micky C. Nnamdi, et al. (16 authors)
- Published: 2026-11-21 05:38 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reward model; reasoning: reasoning, chain-of-thought, chain of thought, process reward
- Abstract skim: Biomedical question answering often requires multi-step reasoning under limited inference budgets. While test-time search methods such as Tree-of-Thought can improve reasoning performance, directly searching over free-form language is computationally expensive and highly redundant, as many reasoning trajectories...

### 32 - OVOGO: Offline Value-Guided On-Policy Generative Optimization for Flow-Based Vision-Language-Action Models

- arXiv: [2611.30477](https://arxiv.org/abs/2611.30477) | [PDF](https://arxiv.org/pdf/2611.30477) | [papers.cool](https://papers.cool/arxiv/2611.30477)
- Authors: Rongzheng Yang, Jiaming Guo, Yuxuan Guo, Zihao Zhang, Yunkai Gao, Siming Lan, et al. (11 authors)
- Published: 2026-11-23 11:04 UTC | Categories: cs.AI, cs.RO
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization
- Abstract skim: Flow-based vision-language-action models can benefit from robot experience collected during deployment, but repeatedly acquiring new physical interactions for policy improvement is costly. Offline reinforcement learning provides a natural way to reuse collected experience, while flow-based policies offer an...

### 32 - Sparse Hodge Preference Optimization: Fine-Tuning Language Models toward Alignment beyond Transitive Preferences

- arXiv: [2611.30135](https://arxiv.org/abs/2611.30135) | [PDF](https://arxiv.org/pdf/2611.30135) | [papers.cool](https://papers.cool/arxiv/2611.30135)
- Authors: Yiming Liu, Jianwei Ma, Zhongwei Xing, Tonghui Yu
- Published: 2026-11-23 06:44 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, preference optimization, dpo
- Abstract skim: The growing adoption of Direct Preference Optimization (DPO), which leverages pairwise preference data, reflects its great success in fine-tuning large language models to align with human expectations. It directly optimizes the policy from human preferences without explicit reward modeling or the complexities of...

### 32 - ARC: Adaptive Rollout Control for Efficient Synchronous LLM Reinforcement Learning

- arXiv: [2611.29156](https://arxiv.org/abs/2611.29156) | [PDF](https://arxiv.org/pdf/2611.29156) | [papers.cool](https://papers.cool/arxiv/2611.29156)
- Authors: Yihui Zhang, Tianyu Wo, Jinghao Wang, Xiao Zhou, Huitian Xue, Xiaoyang Sun, et al. (9 authors)
- Published: 2026-11-22 02:27 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Synchronous reinforcement learning (RL) for large language models proceeds through a repeated rollout--barrier--update loop. Each update must wait for a fixed number of complete, group-relative training samples, yet individual response lengths and reward outcomes vary widely and only emerge as generation progresses....

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
