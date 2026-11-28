# RL / Post-Training / Agentic RL Reading Queue - 2026-11-28

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 535. Minimum score: 8.

## Top Picks

### 70 - ZeroHero: Training Small Language Agents from Scratch

- arXiv: [2611.34635](https://arxiv.org/abs/2611.34635) | [PDF](https://arxiv.org/pdf/2611.34635) | [papers.cool](https://papers.cool/arxiv/2611.34635)
- Authors: Nikita Sorokin, Zoya Volovikova, Alexey Skrynnik, Aleksandr Panov
- Published: 2026-11-25 16:20 UTC | Categories: cs.AI
- Why it matched: agentic_rl: language agent; rl_post_training: post-training, post training, policy optimization, ppo; reasoning: reasoning; planning_and_action: acting; memory_and_benchmarks: alfworld
- Abstract skim: Large pretrained language models provide capable policies for interactive tasks, but how much model capacity is necessary for a specialized language agent? We introduce ZeroHero, a framework for training small language agents (SLAs) from scratch. In each environment, a large language model acts as the expert, and we...

### 60 - Post-Training Policy Replication for Strategy-Following Multi-Agent Deep Reinforcement Learning across Team Sizes

- arXiv: [2611.34035](https://arxiv.org/abs/2611.34035) | [PDF](https://arxiv.org/pdf/2611.34035) | [papers.cool](https://papers.cool/arxiv/2611.34035)
- Authors: Yamato Takahagi, Yoshinari Motokawa, Toshiharu Sugawara
- Published: 2026-11-25 09:18 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Although multi-agent deep reinforcement learning enables coordinated behavior, aligning it with managerial intent remains difficult due to complex agent interactions. Although the strategy-following distributed attentional actor architecture (sfDA7-X) improves controllability via regional instructions, instruction...

### 53 - Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion

- arXiv: [2611.33470](https://arxiv.org/abs/2611.33470) | [PDF](https://arxiv.org/pdf/2611.33470) | [papers.cool](https://papers.cool/arxiv/2611.33470)
- Authors: Jeremy Canale
- Published: 2026-11-24 21:48 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization, +1 more; reasoning: reasoning
- Abstract skim: We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Recall at B alerts/day). Across 56...

### 53 - HumblePRM: Improving VLM Abstention in Ambiguous Situations through Process Reward Modeling

- arXiv: [2611.33452](https://arxiv.org/abs/2611.33452) | [PDF](https://arxiv.org/pdf/2611.33452) | [papers.cool](https://papers.cool/arxiv/2611.33452)
- Authors: Saket Reddy, Ke Yang, ChengXiang Zhai
- Published: 2026-11-24 21:20 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reward model; reasoning: reasoning, process reward, outcome reward
- Abstract skim: Reliable deployment of Vision Language Models (VLMs) requires that a model's expressed confidence remain grounded in what it can actually see, and that it recognize when the visual evidence is too ambiguous to commit to a confident response. Standard post-training uses outcome reward models (ORMs) that supervise...

### 50 - What Does RL Post-Training Teach Text-to-Image Models? A Skill-Wise Analysis of Flow-GRPO

- arXiv: [2611.33316](https://arxiv.org/abs/2611.33316) | [PDF](https://arxiv.org/pdf/2611.33316) | [papers.cool](https://papers.cool/arxiv/2611.33316)
- Authors: Cheng Zhang, Jiesong Liu
- Published: 2026-11-24 19:06 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning (RL) post-training has become a standard way to improve text-to-image flow models: Flow-GRPO lifts the GenEval score of SD3.5-M from 0.63 to 0.95, a gain read as the model having learned compositional generation. We ask how much of that gain the base model's own samples already contained, by...

### 45 - When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL

- arXiv: [2611.34777](https://arxiv.org/abs/2611.34777) | [PDF](https://arxiv.org/pdf/2611.34777) | [papers.cool](https://papers.cool/arxiv/2611.34777)
- Authors: Haowen Hou, Yicheng Liu, Zhen Huang, Jiaqi Wang
- Published: 2026-11-25 17:38 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: long-horizon agent; rl_post_training: reinforcement learning, grpo; planning_and_action: trajectory, rollout
- Abstract skim: Group-based reinforcement learning with verifiable rewards often yields all-fail groups on long-horizon agent tasks: every sampled trajectory receives zero reward, leaving group-relative methods without a reward-based policy gradient. A common remedy supplies complete solutions from a stronger model, but full...

### 45 - Find the Clue, Not the Scene: Rethinking Reasoning for Entity Recognition in Vision-Language Models

- arXiv: [2611.34681](https://arxiv.org/abs/2611.34681) | [PDF](https://arxiv.org/pdf/2611.34681) | [papers.cool](https://papers.cool/arxiv/2611.34681)
- Authors: Kyungmin Min, Soyeon Kim, Junseok Kim, Kyomin Jung
- Published: 2026-11-25 16:44 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; reasoning: reasoning
- Abstract skim: Answering a knowledge-based visual question requires first recognizing the entity in the image and then recalling knowledge about it. Thinking vision-language models (VLMs) reason for thousands of tokens before answering, yet it remains underexplored how well such thinking VLMs perform each of these two steps. We...

### 45 - Do We Still Need Reinforcement Learning When We Can Read the World Model?

- arXiv: [2611.34656](https://arxiv.org/abs/2611.34656) | [PDF](https://arxiv.org/pdf/2611.34656) | [papers.cool](https://papers.cool/arxiv/2611.34656)
- Authors: Mingchao Zhang, Miduo Cui, Kangze He, Yuanjun Li, Dapeng Li, Ce Zhang, et al. (13 authors)
- Published: 2026-11-25 16:29 UTC | Categories: cs.AI, cs.LG, cs.MA
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning; planning_and_action: planning, decision making, world model
- Abstract skim: Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically used to support planning or policy...

### 44 - MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems

- arXiv: [2611.34327](https://arxiv.org/abs/2611.34327) | [PDF](https://arxiv.org/pdf/2611.34327) | [papers.cool](https://papers.cool/arxiv/2611.34327)
- Authors: Yue Xu, Leikun Yin, Ruiming Min, Yufeng Lai, Justin Andrew Johnson, Sitao Luan, et al. (7 authors)
- Published: 2026-11-25 13:09 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: policy optimization, group relative policy optimization, grpo
- Abstract skim: Multi-agent systems (MAS) built on large language models (LLMs) outperform single-agent systems, but inter-agent communication incurs substantial token overhead. While assigning a large LLM to every agent is common, it results in inefficient resource utilization, leaving the system far from the Pareto frontier. The...

### 43 - Evaluation and Restoration of Safety in Reasoning-Tuned LLMs

- arXiv: [2611.33515](https://arxiv.org/abs/2611.33515) | [PDF](https://arxiv.org/pdf/2611.33515) | [papers.cool](https://papers.cool/arxiv/2611.33515)
- Authors: Ehsan Latif, Roberto Dailey, Risto Miikkulainen, Elliot Meyerson
- Published: 2026-11-24 22:46 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, grpo; reasoning: reasoning; memory_and_benchmarks: memory, evaluation
- Abstract skim: Open-source LLMs that are optimized for reasoning, such as VibeThinker, aim to democratize AI by bringing high-capability models to users with limited resources. They are broadly available but lack regulation and external guardrails; therefore, in order to integrate them safely into human society, it is critical...

### 42 - How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models

- arXiv: [2611.33232](https://arxiv.org/abs/2611.33232) | [PDF](https://arxiv.org/pdf/2611.33232) | [papers.cool](https://papers.cool/arxiv/2611.33232)
- Authors: Salil Bhatnagar
- Published: 2026-11-24 10:49 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning (RL) on a reward that can be checked automatically has become a common last step in the training of text-to-image models. A simpler way to get more correct images is best-of-N: draw N images from the base model and keep the one that a picker prefers. We ask how many base model samples one RL...

### 36 - vSFT: Learning to Verbally Tune Agents at Test Time

- arXiv: [2611.34440](https://arxiv.org/abs/2611.34440) | [PDF](https://arxiv.org/pdf/2611.34440) | [papers.cool](https://papers.cool/arxiv/2611.34440)
- Authors: Qishuai Wen, Rui Chen, Haiwen Li, Zhiyuan Huang, Qiwen Gu, Bingjie Gao, et al. (10 authors)
- Published: 2026-11-25 14:22 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning, grpo; memory_and_benchmarks: alfworld
- Abstract skim: Large language model agents are increasingly improved via agentic reinforcement learning, which can be on-policy but suffers from expensive rollouts and sparse rewards, limiting its application at test time. In this paper, we present a verbally Supervised Fine-Tuning (vSFT) framework that enables the conjunction of...

### 36 - PROVE: Mitigating Long-Horizon LLM Collusion with Reinforcement Learning from Verified Evidence

- arXiv: [2611.34215](https://arxiv.org/abs/2611.34215) | [PDF](https://arxiv.org/pdf/2611.34215) | [papers.cool](https://papers.cool/arxiv/2611.34215)
- Authors: Haochen Luo, Jie Fu, Mukai Li, Yuqi Wang, Qi Liu
- Published: 2026-11-25 11:39 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: memory
- Abstract skim: When LLM agents verify each other's work over a long interaction, they drift into collusion: they come to accept work without the evidence that the verification protocol requires. Collusion is absent at the start and builds up episode by episode, which we trace to accurate feedback accumulating in memory. An agent...

### 35 - BRIAR: Martingale Belief Smoothing on Bifurcation-Guided Reasoning Trees

- arXiv: [2611.34746](https://arxiv.org/abs/2611.34746) | [PDF](https://arxiv.org/pdf/2611.34746) | [papers.cool](https://papers.cool/arxiv/2611.34746)
- Authors: Tianyi Yang, Haoran Zhang, Yifan Chen, Zixuan Li
- Published: 2026-11-25 17:23 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: trajectory, rollout
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has rapidly advanced long-chain reasoning, yet standard policy optimizers distribute rollout compute and gradient credit blindly across a trajectory. On hard problems, an early misstep derails the remaining trace, whereas on solvable problems, the policy keeps...

### 35 - Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning

- arXiv: [2611.34703](https://arxiv.org/abs/2611.34703) | [PDF](https://arxiv.org/pdf/2611.34703) | [papers.cool](https://papers.cool/arxiv/2611.34703)
- Authors: Jiacheng Zhang, Qixing Zhou, Haiyang Wang, Qipeng Gu, Shuzhe Wu, Feiyang Pan, et al. (9 authors)
- Published: 2026-11-25 16:59 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: rollout
- Abstract skim: Mixed-task reinforcement learning (MixRL) directly trains a unified policy across domains to continually expand agent capabilities without training separate specialists or requiring an extra distillation stage. Despite its appeal, scaling MixRL poses significant challenges in achieving stable and efficient mixed-...

### 35 - InstructTTS-OPD: On-Policy Distillation for Multi-Objective Instruction-Following TTS

- arXiv: [2611.33937](https://arxiv.org/abs/2611.33937) | [PDF](https://arxiv.org/pdf/2611.33937) | [papers.cool](https://papers.cool/arxiv/2611.33937)
- Authors: Haitao Li, Tian Tan, Yuguang Yang, Guanrou Yang, Wenhao Guan, Chenglin Li, et al. (8 authors)
- Published: 2026-11-25 07:56 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; planning_and_action: rollout
- Abstract skim: Instruction-following text-to-speech (Instruct-TTS) renders a target transcript in the manner described by a free-form natural-language instruction, and a good rendition must succeed on three fronts at once: following the instruction, pronouncing the transcript correctly, and sounding natural. Reinforcement learning...

### 35 - PRIOR: Pre-Call Reasoning in SFT and Its Influence on Tool-Use Retention under RL

- arXiv: [2611.33648](https://arxiv.org/abs/2611.33648) | [PDF](https://arxiv.org/pdf/2611.33648) | [papers.cool](https://papers.cool/arxiv/2611.33648)
- Authors: Kaiwen Hu, Hyunin Lee, Joseph Suh, Serina Chang, Shuai Shao, Yong Zhang, et al. (10 authors)
- Published: 2026-11-25 02:14 UTC | Categories: cs.LG
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Tool use learned during supervised fine-tuning (SFT) is not always retained during reinforcement learning (RL). We study how properties of SFT data may affect this retention by constructing Low, Medium, and High SFT datasets with approximately matched token budgets but different tool-call depths. Under the same RL...

### 34 - iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control

- arXiv: [2611.33922](https://arxiv.org/abs/2611.33922) | [PDF](https://arxiv.org/pdf/2611.33922) | [papers.cool](https://papers.cool/arxiv/2611.33922)
- Authors: Lisiyu Pan, Ting Huang, Zeyu Zhang, Hao Tang
- Published: 2026-11-25 07:43 UTC | Categories: cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Flow-based generative policies offer expressive action modeling for embodied control, yet achieving efficient one-step generation under reward-driven policy optimization remains challenging. In particular, evolving action distributions during online reinforcement learning may introduce inconsistencies between...

### 34 - FIG-MAC: A Fine-grained Inspiration Graph Empowered Multi-Agent Collaboration for Automated Scientific Hypothesis Generation

- arXiv: [2611.33563](https://arxiv.org/abs/2611.33563) | [PDF](https://arxiv.org/pdf/2611.33563) | [papers.cool](https://papers.cool/arxiv/2611.33563)
- Authors: Siyuan Chen, Yuping Gao, Tai Huang, Yuling Zhou, Dongyu Su, Tongguan Wang
- Published: 2026-11-25 00:25 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent collaboration; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Automated Scientific Hypothesis Generation (ASHG) leveraging large language models (LLMs) aims to harness their strengths in knowledge integration, logical reasoning, and text generation for efficiently producing innovative, verifiable scientific hypotheses. However, existing approaches face three critical...

### 34 - Differentially Private Policy Optimization in Linear MDPs with Adversarial Rewards

- arXiv: [2611.33469](https://arxiv.org/abs/2611.33469) | [PDF](https://arxiv.org/pdf/2611.33469) | [papers.cool](https://papers.cool/arxiv/2611.33469)
- Authors: Yi He
- Published: 2026-11-24 21:46 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning (RL) in personalized services often relies on sensitive interaction data. Motivated by the need to protect these data, we study differentially private (DP) policy optimization in episodic linear Markov decision processes (MDPs) with unknown transitions and adaptive adversarial linear rewards...

### 32 - DiversePlace: Diversity-Seeking Curriculum Reinforcement Learning for Macro Placement

- arXiv: [2611.34472](https://arxiv.org/abs/2611.34472) | [PDF](https://arxiv.org/pdf/2611.34472) | [papers.cool](https://papers.cool/arxiv/2611.34472)
- Authors: Wenrui Zhou, Jiashun Liu, Wenji Fang, Zhiyao Xie, Ling Pan
- Published: 2026-11-25 14:39 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Macro placement is a critical early-stage decision in physical design because macro locations strongly constrain subsequent implementation stages. The task is difficult because these high-impact discrete decisions must be made before downstream quality can be measured accurately, forcing training to rely on fast but...

### 30 - FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers

- arXiv: [2611.33769](https://arxiv.org/abs/2611.33769) | [PDF](https://arxiv.org/pdf/2611.33769) | [papers.cool](https://papers.cool/arxiv/2611.33769)
- Authors: Zirui Li, Yujie Yan, Jingxuan Qian, Yangang Ren, Haizhou Yin, Haoran Xu, et al. (7 authors)
- Published: 2026-11-25 04:48 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Human takeovers offer corrective supervision for vision-language-action (VLA) policies, but their contribution to offline post-training must be separated from that of continued optimization. We introduce FailPoint-X, a benchmark for offline VLA post-training with human takeovers. To represent uncertainty in failure...

### 30 - CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems

- arXiv: [2611.33242](https://arxiv.org/abs/2611.33242) | [PDF](https://arxiv.org/pdf/2611.33242) | [papers.cool](https://papers.cool/arxiv/2611.33242)
- Authors: Danil Kostromin, Andrey Sakhovskiy, Semen Budennyy
- Published: 2026-11-24 14:39 UTC | Categories: cs.AI, cs.CL, cs.MA
- Why it matched: agentic_rl: multi-agent, tool use; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Multi-agent systems (MAS) built on large language models (LLMs) distribute reasoning across specialized agents that must exchange messages and invoke tools reliably. Existing evaluations typically couple communication with open domain tasks, making it difficult to determine whether a failure arises from reasoning,...

### 29 - Diverse Alternative Reasoning Traces for Hard Math Problems

- arXiv: [2611.34928](https://arxiv.org/abs/2611.34928) | [PDF](https://arxiv.org/pdf/2611.34928) | [papers.cool](https://papers.cool/arxiv/2611.34928)
- Authors: Lukas Aichberger, Adam Golinski, Arno Blaas, Arwen Bradley, Jacob Springer, Mehrdad Farajtabar, et al. (8 authors)
- Published: 2026-11-25 18:59 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning
- Abstract skim: Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a...

### 29 - Procedure Inference as Memory: Learning Recruiter Decision Procedures from OKF-Structured Episodes in Multi-Session Hiring Assistants

- arXiv: [2611.34576](https://arxiv.org/abs/2611.34576) | [PDF](https://arxiv.org/pdf/2611.34576) | [papers.cool](https://papers.cool/arxiv/2611.34576)
- Authors: Praveen Kumar Bodigutla, Yizhi Zhang, Sai Vivek Kanaparthy, Arup De
- Published: 2026-11-25 15:41 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, reflection; memory_and_benchmarks: memory, episodic memory, evaluation
- Abstract skim: Multi-session hiring assistants must infer evolving recruiter preferences and decision patterns across projects and time. We introduce Open Knowledge Format (OKF)-indexed episodic memory to organize interactions and retrieve related events through their lineage. We also introduce Procedure Memory, which learns...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
