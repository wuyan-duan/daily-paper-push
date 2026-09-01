# RL / Post-Training / Agentic RL Reading Queue - 2026-09-01

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 811. Minimum score: 8.

## Top Picks

### 60 - AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing

- arXiv: [2608.29622](https://arxiv.org/abs/2608.29622) | [PDF](https://arxiv.org/pdf/2608.29622) | [papers.cool](https://papers.cool/arxiv/2608.29622)
- Authors: Xinke Jiang, Yue Fang, Zhibang Yang, Jiaran Gao, Zhixin Zhang, Tao Feng, et al. (15 authors)
- Published: 2026-08-30 07:31 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: memory
- Abstract skim: Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learning (RL)-based agentic RAG methods...

### 60 - Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space

- arXiv: [2608.29188](https://arxiv.org/abs/2608.29188) | [PDF](https://arxiv.org/pdf/2608.29188) | [papers.cool](https://papers.cool/arxiv/2608.29188)
- Authors: Qiancheng Zhou, Ruizhe Li
- Published: 2026-08-29 10:46 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo, ppo, +1 more; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) substantially improves single-sample accuracy (pass@1) but causes the policy's solution space to contract, diminishing the returns of test-time scaling. In this work, we investigate where inside a reasoning trajectory this breadth is lost: does the policy fail to...

### 58 - HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving

- arXiv: [2608.30672](https://arxiv.org/abs/2608.30672) | [PDF](https://arxiv.org/pdf/2608.30672) | [papers.cool](https://papers.cool/arxiv/2608.30672)
- Authors: Boyang Mu, Zhiwei Wei, Mugen Peng, Wenjia Xu
- Published: 2026-08-31 12:13 UTC | Categories: cs.AI, cs.MA
- Why it matched: agentic_rl: multi-agent, tool use, agent collaboration; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: decision making; memory_and_benchmarks: benchmark
- Abstract skim: Recent advances in large language models and multimodal models have pushed remote sensing (RS) processing from simple perception models to agentic systems designed to tackle complex, long-horizon RS tasks. However, existing systems often rely on monolithic decision-making frameworks, which fail to accommodate the...

### 53 - Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses

- arXiv: [2608.29641](https://arxiv.org/abs/2608.29641) | [PDF](https://arxiv.org/pdf/2608.29641) | [papers.cool](https://papers.cool/arxiv/2608.29641)
- Authors: Xinke Jiang, Zhixin Zhang, Zhibang Yang, Jiaran Gao, Rihong Qiu, Shijin Chen, et al. (9 authors)
- Published: 2026-08-30 08:07 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent, agent training; rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory
- Abstract skim: Large language model agents increasingly solve long-horizon tasks through multi-agent harnesses in which a central agent coordinates specialized sub-agents, tools, and environments. Training the central policy in such a harness raises two challenges. First, an action label is a low-cardinality decision, whereas its...

### 53 - JPO: Juris Policy Optimization for Structured Legal Reasoning in Criminal Judgment Prediction

- arXiv: [2608.29616](https://arxiv.org/abs/2608.29616) | [PDF](https://arxiv.org/pdf/2608.29616) | [papers.cool](https://papers.cool/arxiv/2608.29616)
- Authors: Zhaolu Kang, Yantao Liu, Tailong Luo, Leqi Zheng, Lei Wei, Chenghua Zhu, et al. (17 authors)
- Published: 2026-08-30 07:14 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: Criminal judgment prediction requires models to infer statutory articles, charges, and sentencing outcomes from case facts. Unlike standard classification tasks, it involves a structured reasoning process in which statutes should be matched with facts, charges should be justified by statutes, and sentencing outcomes...

### 53 - RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs

- arXiv: [2608.29263](https://arxiv.org/abs/2608.29263) | [PDF](https://arxiv.org/pdf/2608.29263) | [papers.cool](https://papers.cool/arxiv/2608.29263)
- Authors: Yuwei Lou, Hao Hu, Yuzhou Jiang, Zongfei Zhang, Liang Wang, Jincai Liu, et al. (8 authors)
- Published: 2026-08-29 13:36 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent collaboration; rl_post_training: reinforcement learning; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Large Language Models (LLMs) often suffer from hallucination and struggle with complex reasoning tasks requiring multi-hop domain knowledge. While integrating Knowledge Graphs (KGs) provides a structured and verifiable information source, current KG-enhanced LLM paradigms usually rely on single-agent path extraction...

### 52 - PAC: Progress-Augmented Advantage Curriculum for Multi-Task Reinforcement Learning of LLMs

- arXiv: [2608.30528](https://arxiv.org/abs/2608.30528) | [PDF](https://arxiv.org/pdf/2608.30528) | [papers.cool](https://papers.cool/arxiv/2608.30528)
- Authors: Yuanqiang Yu, Yanzhao Zheng, Zhentao Zhang, Tianze Xu, Chao Ma, Jihuai Zhu, et al. (11 authors)
- Published: 2026-08-31 09:59 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement learning (RL) is used to improve the reasoning abilities of LLMs, while training data span heterogeneous tasks. However, most RL post-training pipelines rely on fixed or manually designed task mixtures, even though task usefulness changes as training progresses. Online curriculum methods often define...

### 51 - One Policy Is Enough: Single-Agent Reinforcement Learning Outperforms Tree Search for Chemistry Tool Learning

- arXiv: [2608.30952](https://arxiv.org/abs/2608.30952) | [PDF](https://arxiv.org/pdf/2608.30952) | [papers.cool](https://papers.cool/arxiv/2608.30952)
- Authors: Armin Dariani, Sifan Wu, Bang Liu, Entao Yang
- Published: 2026-08-31 15:22 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: tool use, tool learning; rl_post_training: reinforcement learning; reasoning: reasoning
- Abstract skim: Chemistry questions often demand exact computation and database lookups that a language model cannot supply from its parameters, so it must reach for external tools. Tool use here is a three-part problem: select the right tool from a large pool, fill it with correctly typed arguments, and chain calls so that each...

### 50 - BCPPO: Bachelier-Inspired Constrained Proximal Policy Optimization for Tail-Risk-Aware Safe Reinforcement Learning

- arXiv: [2608.30283](https://arxiv.org/abs/2608.30283) | [PDF](https://arxiv.org/pdf/2608.30283) | [papers.cool](https://papers.cool/arxiv/2608.30283)
- Authors: Dongsheng Hou, Yanqiao Chen, Yuhan Rui
- Published: 2026-08-31 05:52 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Expected-cost constraints can still permit rare, high-cost events. Monte Carlo conditional value at risk (CVaR) gradients can be noisy at high confidence, whereas critics that model an outcome distribution add complexity. We propose BCPPO (Bachelier-Inspired Constrained Proximal Policy Optimization), a proximal...

### 49 - GPAgentBench-2K: Benchmarking Large Language Model Agents in Complex Clinical Action Space

- arXiv: [2608.30188](https://arxiv.org/abs/2608.30188) | [PDF](https://arxiv.org/pdf/2608.30188) | [papers.cool](https://papers.cool/arxiv/2608.30188)
- Authors: Boqi Chen, Xudong Liu, Yunke Ao, Heejin Do, Jianing Qiu
- Published: 2026-08-31 03:13 UTC | Categories: cs.CL
- Why it matched: agentic_rl: llm agent; rl_post_training: policy optimization, group relative policy optimization, grpo; planning_and_action: decision making; memory_and_benchmarks: benchmark
- Abstract skim: Large Language Models (LLMs) show great potential as clinical agents, yet existing benchmarks reduce clinical workflows to static predictions or unconstrained Markov Decision Processes (MDPs) with coarse action sets. To address this, we introduce GPAgentBench-2K, the first Constrained MDP (CMDP) LLM-agent benchmark...

### 49 - JudgePanel: A Compact Judge with Panel Deliberation via Adaptive Multi-Reward Reinforcement Learning

- arXiv: [2608.29168](https://arxiv.org/abs/2608.29168) | [PDF](https://arxiv.org/pdf/2608.29168) | [papers.cool](https://papers.cool/arxiv/2608.29168)
- Authors: Yiyue Qian, Shinan Zhang, Huan Song, Hannah Marlowe
- Published: 2026-08-29 09:33 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; reasoning: deliberation; memory_and_benchmarks: evaluation
- Abstract skim: The LLM-as-a-Judge paradigm has emerged as a scalable alternative to human evaluation. However, single-model judges are limited by their inherent model biases, while multi-agent evaluation protocols that mitigate this through diverse deliberation are prohibitively expensive at inference time. To this end, we propose...

### 48 - When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models

- arXiv: [2608.31035](https://arxiv.org/abs/2608.31035) | [PDF](https://arxiv.org/pdf/2608.31035) | [papers.cool](https://papers.cool/arxiv/2608.31035)
- Authors: Joonyong Park, Jerry Li
- Published: 2026-08-31 16:14 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +2 more
- Abstract skim: Codec-based text-to-speech (TTS) models make language-model post-training applicable to speech generation, but it remains unclear when learned perceptual predictors can serve as reinforcement learning rewards without losing alignment with human listeners. We study this question with Group Relative Policy...

### 45 - Efficient Geothermal Well-Control Optimization via Diffusion-Surrogate Reinforcement Learning

- arXiv: [2608.28791](https://arxiv.org/abs/2608.28791) | [PDF](https://arxiv.org/pdf/2608.28791) | [papers.cool](https://papers.cool/arxiv/2608.28791)
- Authors: Ruimin Dai, Guodong Chen, Randy Harsuko, Kunpeng Liu, Nori Nakata
- Published: 2026-08-28 18:52 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, reward model, ppo; planning_and_action: decision making; memory_and_benchmarks: benchmark
- Abstract skim: Real-time decision-making for enhanced geothermal systems (EGS) is challenging because long-term production periods involve high-dimensional control spaces and a large number of time-consuming high-fidelity hydrothermal simulations. Reinforcement learning provides a natural framework for state-dependent sequential...

### 44 - TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models

- arXiv: [2608.29999](https://arxiv.org/abs/2608.29999) | [PDF](https://arxiv.org/pdf/2608.29999) | [papers.cool](https://papers.cool/arxiv/2608.29999)
- Authors: Apoorva Kulkarni, Kaousheik Jayakumar, Sreyan Ghosh, Utathya Aich, Ramani Duraiswami, Dinesh Manocha
- Published: 2026-08-30 19:49 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Large audio-language models (LALMs) describe audio at the clip level but cannot assign timestamps to the events, speakers, or sounds they identify. Despite being essential for downstream tasks like speech recognition and dense audio captioning, timestamping remains a key limitation of most LALMs. We present TEMPO...

### 44 - FRAMEWORKERS: A Dynamic Multi-Agent Framework for AI-Generated Video Production

- arXiv: [2608.29814](https://arxiv.org/abs/2608.29814) | [PDF](https://arxiv.org/pdf/2608.29814) | [papers.cool](https://papers.cool/arxiv/2608.29814)
- Authors: Zhendong Li, Lei Sun, Letian Shi, Deheng Zhang, Ruibo Ming, Mengshun Hu, et al. (11 authors)
- Published: 2026-08-30 14:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: policy optimization, group relative policy optimization, grpo
- Abstract skim: Modern video generators excel at synthesizing individual clips, but complete video production requires coordinating a long sequence of interdependent creative steps, including scripting, storyboarding, generation, and editing. It further demands persistent asset management and dynamic task orchestration as...

### 44 - LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO

- arXiv: [2608.29357](https://arxiv.org/abs/2608.29357) | [PDF](https://arxiv.org/pdf/2608.29357) | [papers.cool](https://papers.cool/arxiv/2608.29357)
- Authors: Saeed Khaki, Nima Safaei, Kamal Ginotra
- Published: 2026-08-29 16:33 UTC | Categories: cs.AI
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning, dpo; planning_and_action: trajectory
- Abstract skim: Multimodal search agents answer visual questions by interleaving image understanding, web retrieval, tool use, and evidence synthesis. Strong systems exist, but in two expensive regimes: proprietary frontier models such as GPT-5 and Gemini, or large open vision-language backbones trained with substantial agentic...

### 43 - RAGDiffusion++: From Macro-Retrieval to Micro-Fidelity Alignment for Garment Generation

- arXiv: [2608.29280](https://arxiv.org/abs/2608.29280) | [PDF](https://arxiv.org/pdf/2608.29280) | [papers.cool](https://papers.cool/arxiv/2608.29280)
- Authors: Yuhan Li, Xianfeng Tan, Fangao Zeng, Wenxiang Shang, Pipei Huang, Hao Zhou, et al. (9 authors)
- Published: 2026-08-29 14:06 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model, +1 more; planning_and_action: trajectory
- Abstract skim: Standard clothing asset generation---restoring forward-facing flat-lay garment images from diverse real-world contexts---holds immense commercial value yet demands both macroscopic topological accuracy and microscopic physical fidelity. Although our previous work RAGDiffusion effectively eradicated large-scale...

### 42 - A-MADiff: Attention-Guided Multi-Agent DRL with Diffusion Policies for Memory-Aware Task Orchestration in Mobile AIGC Networks

- arXiv: [2608.29255](https://arxiv.org/abs/2608.29255) | [PDF](https://arxiv.org/pdf/2608.29255) | [papers.cool](https://papers.cool/arxiv/2608.29255)
- Authors: Chongzhi Wu, Zhengtao Li, Jiawen Kang, Jinbo Wen, Xiaohuan Li, Maomao Zhang, et al. (7 authors)
- Published: 2026-08-29 13:19 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent, agent orchestration; rl_post_training: reinforcement learning; memory_and_benchmarks: memory
- Abstract skim: Artificial Intelligence-Generated Content (AIGC) services employ Generative AI (GenAI) models to automatically generate diverse content. Mobile AIGC networks host GenAI models on edge-located AIGC Service Providers (ASPs) to deliver low-latency and personalized AIGC services for mobile users. However, AIGC inference...

### 40 - Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization

- arXiv: [2608.31079](https://arxiv.org/abs/2608.31079) | [PDF](https://arxiv.org/pdf/2608.31079) | [papers.cool](https://papers.cool/arxiv/2608.31079)
- Authors: Camila Blank, Zhuofan Ying, Christopher Potts, Peter Hase, Jing Huang
- Published: 2026-08-31 16:52 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, preference optimization, dpo
- Abstract skim: Sycophantic agreement refers to a behavior in which language models excessively affirm the user, often at the cost of factual accuracy. Although sycophantic agreement is a well-known failure of model alignment, there is limited understanding of how it emerges from model training. In this work, we demonstrate that...

### 37 - GMTS: Gradient Magnitude-based Token Selection Improves RLVR Training for LLM Reasoning

- arXiv: [2608.30632](https://arxiv.org/abs/2608.30632) | [PDF](https://arxiv.org/pdf/2608.30632) | [papers.cool](https://papers.cool/arxiv/2608.30632)
- Authors: Outongyi Lv, Yuanwei Zhang, Xiaoqun Zhang
- Published: 2026-08-31 11:41 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Reinforcement learning (RL), particularly RL with Verifiable Rewards (RLVR), has recently emerged as a central paradigm for enhancing large language models' (LLMs) reasoning abilities, demonstrating remarkable effectiveness across reasoning tasks. Recent studies suggest that high-entropy tokens play an exceptionally...

### 37 - Sequential Trajectories and Simultaneous Blending: Multi-Emotion Modeling for Instruction-Following TTS

- arXiv: [2608.30325](https://arxiv.org/abs/2608.30325) | [PDF](https://arxiv.org/pdf/2608.30325) | [papers.cool](https://papers.cool/arxiv/2608.30325)
- Authors: Yan Zhou, Yun Hong, Yang Feng
- Published: 2026-08-31 06:42 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, policy optimization, group relative policy optimization; planning_and_action: trajectory; memory_and_benchmarks: evaluation
- Abstract skim: Natural-language instructions enable flexible control of synthesized speech, yet emotional TTS systems primarily model a single utterance-level affect, leaving multi-emotion control underexplored. We study two complementary multi-emotion TTS tasks: emotion trajectory, which spans several ordered affective stages,...

### 37 - Aligning Multi-Trajectory Supervision with Policy Optimization for VLA Driving

- arXiv: [2608.30122](https://arxiv.org/abs/2608.30122) | [PDF](https://arxiv.org/pdf/2608.30122) | [papers.cool](https://papers.cool/arxiv/2608.30122)
- Authors: Tian Zhang, Zhuo Huang, Hongrui Ye, Yu Wu, Zengmao Wang, Kaixuan Zhou
- Published: 2026-08-31 01:17 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; planning_and_action: trajectory, rollout; downranked: driving
- Abstract skim: Vision-language-action (VLA) driving methods increasingly combine multi-trajectory imitation learning with group-relative policy optimization (GRPO), making trajectory selection critical to final performance. However, some high-scoring trajectories that improve imitation can degrade subsequent GRPO by inducing...

### 37 - When Do Larger Batches Help Scale LLM Reinforcement Learning?

- arXiv: [2608.29296](https://arxiv.org/abs/2608.29296) | [PDF](https://arxiv.org/pdf/2608.29296) | [papers.cool](https://papers.cool/arxiv/2608.29296)
- Authors: Ziniu Li, Jinbo Wang, Guanhua Huang, Feiyuan Zhang, Pengbo Li, Alex Chen
- Published: 2026-08-29 14:32 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo, ppo; planning_and_action: rollout; memory_and_benchmarks: memory
- Abstract skim: Larger batches reduce the variance of stochastic gradients per update and are therefore often expected to accelerate training. Yet whether this statistical benefit translates into lower wall-clock time-to-target remains unclear, because each update consumes more samples and may take longer to execute. We study this...

### 37 - ERR+: Sequential Entropy Resolution for Efficient and Decisive LLM Reasoning

- arXiv: [2608.28771](https://arxiv.org/abs/2608.28771) | [PDF](https://arxiv.org/pdf/2608.28771) | [papers.cool](https://papers.cool/arxiv/2608.28771)
- Authors: Xin Jiang, Minhao Wang, Wen Wu, Zhentao Xie, Shangheng Du, Jinxin Shi, et al. (7 authors)
- Published: 2026-08-28 18:28 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Large reasoning models achieve strong performance on complex tasks by generating extended chain-of-thought (CoT) traces via reinforcement learning with verifiable rewards (RLVR). While current RLVR methods have achieved strong results with correctness-based reward signals, they provide limited guidance on the...

### 36 - The Role of Network Topology and Opponent Information in Shaping Cooperation in Multi-Agent Reinforcement Learning Systems

- arXiv: [2608.28977](https://arxiv.org/abs/2608.28977) | [PDF](https://arxiv.org/pdf/2608.28977) | [papers.cool](https://papers.cool/arxiv/2608.28977)
- Authors: Seongho Son, Stephen Hailes, Mirco Musolesi
- Published: 2026-08-29 01:05 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Several works have investigated the influence of graph topology on cooperation among artificial agents, while the majority of the literature has focused on modelling agents' adaptation through strategy imitation, which relies solely on the cumulative payoffs of others. This paper investigates scenarios in which each...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
