# RL / Post-Training / Agentic RL Reading Queue - 2026-07-10

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 313. Minimum score: 8.

## Top Picks

### 45 - Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing

- arXiv: [2607.08497](https://arxiv.org/abs/2607.08497) | [PDF](https://arxiv.org/pdf/2607.08497) | [papers.cool](https://papers.cool/arxiv/2607.08497)
- Authors: Feng Wang, Canmiao Fu, Zhipeng Huang, Chen Li, Jing Lyu, Ge Li
- Published: 2026-07-09 13:55 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: agent harness; rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: planning, decision making; memory_and_benchmarks: memory, benchmark
- Abstract skim: Recent unified multimodal models show a single architecture can jointly perform vision/language understanding and image generation/editing. However, they repeatedly feed all historical visual and textual inputs into a shared context window, limiting long-horizon multimodal dialogue due to visual token explosion and...

### 40 - When Synthetic Speech Is All You Have: Better Call GRPO

- arXiv: [2607.08409](https://arxiv.org/abs/2607.08409) | [PDF](https://arxiv.org/pdf/2607.08409) | [papers.cool](https://papers.cool/arxiv/2607.08409)
- Authors: Shashi Kumar, Yanis Labrak, Hasindri Watawana, Sergio Burdisso, Esaú Villatoro-Tello, Kadri Hacioğlu, et al. (8 authors)
- Published: 2026-07-09 12:34 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo
- Abstract skim: LLM-based ASR adapted to regulated domains such as banking is bottlenecked by privacy: real speech is costly and legally constrained to collect, making synthetic text-to-speech (TTS) an attractive substitute. Yet synthetic speech stays acoustically mismatched with real recordings, and work on this gap has stayed...

### 40 - DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment

- arXiv: [2607.07820](https://arxiv.org/abs/2607.07820) | [PDF](https://arxiv.org/pdf/2607.07820) | [papers.cool](https://papers.cool/arxiv/2607.07820)
- Authors: Xinyu Geng, Xuanhua He, Sixiang Chen, Yanjing Xiao, Fan Zhang, Shijue Huang, et al. (10 authors)
- Published: 2026-07-08 18:03 UTC | Categories: cs.CL
- Why it matched: agentic_rl: tool use; rl_post_training: reinforcement learning; reasoning: reflection; planning_and_action: trajectory; memory_and_benchmarks: gaia
- Abstract skim: Training tool-use agents to improve from their own experience remains challenging, as supervised fine-tuning relies on fixed teacher-distilled trajectories, while sparse-reward reinforcement learning provides weak supervision for long-horizon interactions. We present DeepSearch-Evolve, a self-distillation framework...

### 36 - When Implausible Tokens Get Reinforced: Tail-Aware Credit Calibration for LLM Reinforcement Learning

- arXiv: [2607.07976](https://arxiv.org/abs/2607.07976) | [PDF](https://arxiv.org/pdf/2607.07976) | [papers.cool](https://papers.cool/arxiv/2607.07976)
- Authors: Xiuyi Lou, Zicheng Xu, Yu-Neng Chuang, Hoang Anh Duy Le, Zhaozhuo Xu, Guanchu Wang, et al. (7 authors)
- Published: 2026-07-08 23:00 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Reinforcement learning (RL) has achieved remarkable success in enhancing the reasoning capabilities of large language models (LLMs). However, widely used critic-free RL methods rely on uniform credit assignment, broadcasting the same advantage to all tokens regardless of their differences. We identify a critical...

### 35 - Reinforcing the Generation Order of Multimodal Masked Diffusion Models

- arXiv: [2607.08056](https://arxiv.org/abs/2607.08056) | [PDF](https://arxiv.org/pdf/2607.08056) | [papers.cool](https://papers.cool/arxiv/2607.08056)
- Authors: Yidong Ouyang, Zhe Wang, Sourav Bhabesh, Dmitriy Bespalov
- Published: 2026-07-09 02:07 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: policy optimization, group relative policy optimization, grpo; reasoning: reasoning; memory_and_benchmarks: benchmark
- Abstract skim: Diffusion Language Models (DLMs) have recently achieved substantial progress in natural language generation tasks. Recent research demonstrates that adaptive token generation ordering can significantly improve performance in mathematical reasoning and code synthesis applications. In this work, we investigate the...

### 33 - WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search

- arXiv: [2607.08662](https://arxiv.org/abs/2607.08662) | [PDF](https://arxiv.org/pdf/2607.08662) | [papers.cool](https://papers.cool/arxiv/2607.08662)
- Authors: Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao, Yutao Zhu, Zhongyuan Wang, Guanting Dong, et al. (11 authors)
- Published: 2026-07-09 16:28 UTC | Categories: cs.AI, cs.CL, cs.MA
- Why it matched: agentic_rl: multi-agent, agent orchestration, agent collaboration; planning_and_action: trajectory
- Abstract skim: Large language model (LLM)-based web search agents are transforming information seeking from simple factoid question answering into complex, deep-and-wide search and research-oriented tasks. A single ReAct-style agent is constrained by one long trajectory and limited context, making it difficult to handle depth and...

### 33 - Selective Left-Shift: Turning Test-Time Compute and Difficulty-based Curation into Training Data for Low-Resource Code Generation

- arXiv: [2607.07748](https://arxiv.org/abs/2607.07748) | [PDF](https://arxiv.org/pdf/2607.07748) | [papers.cool](https://papers.cool/arxiv/2607.07748)
- Authors: Didula Samaraweera, Anjana Supun, Srinath Perera
- Published: 2026-07-08 09:18 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, rlvr, verifiable reward; reasoning: reasoning
- Abstract skim: Large Language Models achieve strong code generation for high resource languages like Python and Java but suffer sharp performance drops on Low-Resource Programming Languages~(LRPLs) such as Julia. Improving Small Language Models~(SLMs) for these languages faces a trilemma: Supervised Fine-Tuning~(SFT) is...

### 32 - Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference

- arXiv: [2607.08724](https://arxiv.org/abs/2607.08724) | [PDF](https://arxiv.org/pdf/2607.08724) | [papers.cool](https://papers.cool/arxiv/2607.08724)
- Authors: Chuning Zhu, Eva Xu, Jose Barreiros, Krishnan Srinivasan, Paarth Shah, Abhishek Gupta
- Published: 2026-07-09 17:30 UTC | Categories: cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, deliberation; planning_and_action: decision making; memory_and_benchmarks: memory
- Abstract skim: Human decision-making is highly flexible -- some actions are taken immediately; others require longer deliberation. Language models have exhibited a similar capacity for adaptive "reasoning." However, transferring this capability to continuous control policies has been challenging, as directly reasoning in language...

### 32 - MPFlow: Learning Budgeted Max-Flow Optimization on the Lightning Network with Deep Graph Reinforcement Learning

- arXiv: [2607.08703](https://arxiv.org/abs/2607.08703) | [PDF](https://arxiv.org/pdf/2607.08703) | [papers.cool](https://papers.cool/arxiv/2607.08703)
- Authors: Harrison Rush, Vincent Davis, Simone Antonelli, Vikash Singh, Jesse Shrader, Emanuele Rossi
- Published: 2026-07-09 17:09 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: We address liquidity placement in the Bitcoin Lightning Network (LN): given a fixed budget, which channels should a node open to maximize its routing capacity? We cast this as a budget-constrained combinatorial optimization problem on graphs, selecting $k$ edge additions that maximize $s$--$t$ max-flow, a theory-...

### 31 - Hallucination Self-Play: Bootstrapping Reinforced Detector via Evolved Generator

- arXiv: [2607.07993](https://arxiv.org/abs/2607.07993) | [PDF](https://arxiv.org/pdf/2607.07993) | [papers.cool](https://papers.cool/arxiv/2607.07993)
- Authors: Shiping Yang, Shining Liang, Weihao Liu, Wenbiao Ding, Linjun Shou, Lu Cheng, et al. (7 authors)
- Published: 2026-07-08 23:54 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning, reward model; reasoning: self-play; memory_and_benchmarks: benchmark
- Abstract skim: Identifying faithfulness hallucinations in LLM-generated outputs remains challenging due to the scarcity of high-quality annotated data. Recent work relies on advanced LLMs to synthesize training data, including rationales, labels, and hallucinated claims. However, these methods treat the generator as a static...

### 28 - DrugGen 2: A disease-aware language model for enhancing drug discovery

- arXiv: [2607.08404](https://arxiv.org/abs/2607.08404) | [PDF](https://arxiv.org/pdf/2607.08404) | [papers.cool](https://papers.cool/arxiv/2607.08404)
- Authors: Ali Motahharynia, Mohammadreza Ghaffarzadeh-Esfahani, Mahsa Sheikholeslami, Navid Mazrouei, Matin Irajpour, Yousof Gheisari, et al. (7 authors)
- Published: 2026-07-09 12:29 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; downranked: protein
- Abstract skim: Current computational approaches for drug design typically focus on generating molecules conditioned on specific targets or general molecular properties, often neglecting the influence of disease context on target behavior and therapeutic outcomes. To address this gap, we introduce DrugGen-2, a novel generative...

### 28 - Open-ended Multi-agent Autocurricula via Visual Inspection of Policies with Multi-modal LLMs

- arXiv: [2607.08193](https://arxiv.org/abs/2607.08193) | [PDF](https://arxiv.org/pdf/2607.08193) | [papers.cool](https://papers.cool/arxiv/2607.08193)
- Authors: Lorenzo Pantè, Andrea Fanti, Roberto Capobianco
- Published: 2026-07-09 07:48 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Open-ended curricula in Reinforcement Learning (RL) aim to train generally-capable agents by identifying tasks that facilitate learning increasingly complex skills. A major challenge when designing such curricula is assessing task difficulty relative to the agent's current learning progress. While previous work has...

### 28 - Trustworthy Machine Learning through the Lens of Combinatorial Optimization: Survey and Research Perspectives

- arXiv: [2607.07762](https://arxiv.org/abs/2607.07762) | [PDF](https://arxiv.org/pdf/2607.07762) | [papers.cool](https://papers.cool/arxiv/2607.07762)
- Authors: Thibaut Vidal, Julien Ferry
- Published: 2026-07-08 15:27 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: decision making
- Abstract skim: Modern machine learning (ML) increasingly relies on complex models whose behavior is difficult to characterize beyond empirical performance metrics. Across a wide range of tasks, including prediction, generation, and decision-making, models with similar empirical performance can exhibit markedly different properties...

### 24 - Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation

- arXiv: [2607.08255](https://arxiv.org/abs/2607.08255) | [PDF](https://arxiv.org/pdf/2607.08255) | [papers.cool](https://papers.cool/arxiv/2607.08255)
- Authors: Miseong Shawn Kim
- Published: 2026-07-09 09:00 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, rlvr, grpo
- Abstract skim: Large language models increasingly serve as teachers generating training data for smaller students. Prior multi-teacher knowledge distillation methods merge outputs without determining which frontier model teaches best, often relying on an LLM judge biased toward its own outputs. We introduce a compete-then-...

### 24 - MuScriptor: An Open Model for Multi-Instrument Music Transcription

- arXiv: [2607.08168](https://arxiv.org/abs/2607.08168) | [PDF](https://arxiv.org/pdf/2607.08168) | [papers.cool](https://papers.cool/arxiv/2607.08168)
- Authors: Simon Rouard, Michael Krause, Axel Roebel, Carl-Johann Simon-Gabriel, Alexandre Défossez
- Published: 2026-07-09 07:12 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Existing methods for automatic music transcription are often limited to single-instrument recordings or fail on complex, real music mixes. Although previous work utilizes synthetic training data, the resulting models generalize poorly, leading to largely unusable transcription output in realistic, multi-instrument...

### 24 - CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

- arXiv: [2607.08093](https://arxiv.org/abs/2607.08093) | [PDF](https://arxiv.org/pdf/2607.08093) | [papers.cool](https://papers.cool/arxiv/2607.08093)
- Authors: Andrej Leban, Yuekai Sun
- Published: 2026-07-09 04:03 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: agentic_rl: tool use; reasoning: reasoning; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Large language models (LLMs) increasingly act as integrated data-science agents, combining abstract reasoning with advanced tool use. Yet the relevant benchmark landscape largely divides into symbolic causal reasoning benchmarks without realistic data analysis or data analysis benchmarks without a principled causal...

### 24 - MASTE: A Multi-Agent Pipeline for Zero-Shot Aspect Sentiment Triplet Extraction

- arXiv: [2607.08080](https://arxiv.org/abs/2607.08080) | [PDF](https://arxiv.org/pdf/2607.08080) | [papers.cool](https://papers.cool/arxiv/2607.08080)
- Authors: Ao Hong, Lehang Wang, Zhirun Yue, Mingxin Wang, Zihan Wang, Houde Liu
- Published: 2026-07-09 03:20 UTC | Categories: cs.CL
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Aspect Sentiment Triplet Extraction (ASTE) requires jointly identifying (aspect, opinion, sentiment) triples from a given review sentence. While large language models (LLMs) achieve strong zero-shot performance on many NLP benchmarks, their effectiveness on ASTE remains limited, as single-pass generation forces the...

### 24 - DreamCharacter-1: From 3D Generative Foundation Models to Product-Ready Character Generation

- arXiv: [2607.07817](https://arxiv.org/abs/2607.07817) | [PDF](https://arxiv.org/pdf/2607.07817) | [papers.cool](https://papers.cool/arxiv/2607.07817)
- Authors: Weizhe Liu, Yunjie Wu, Xiangqian Shu, Guangwei Wang, Xiangyu Xu, Peng Li, et al. (8 authors)
- Published: 2026-07-08 18:02 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, preference optimization
- Abstract skim: We present DreamCharacter-1, a lightweight post-adaptation framework that calibrates pretrained 3D foundation models toward high-fidelity, production-ready 3D character generation. Building upon a 3D foundation backbone, our pipeline incorporates three task-oriented components: (1) geometry post-training, which...

### 24 - A Transdiagnostic Space of Disorder Like Phenotypes in Reinforcement Learning Agents

- arXiv: [2607.07753](https://arxiv.org/abs/2607.07753) | [PDF](https://arxiv.org/pdf/2607.07753) | [papers.cool](https://papers.cool/arxiv/2607.07753)
- Authors: Hari Prasad
- Published: 2026-07-08 12:20 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, ppo
- Abstract skim: Modelling psychological disorders in artificial agents offers both a testbed for computational psychiatry and a lens on the failure modes of affective control. Prior work induces one or two disorders in a reinforcement learning (RL) agent by hand-tuned reward shaping, labels the behaviour post hoc, and reports...

### 21 - When Debiasing Backfires: Counterintuitive Side Effects of Preprocessing-Based Stereotype Mitigation

- arXiv: [2607.07937](https://arxiv.org/abs/2607.07937) | [PDF](https://arxiv.org/pdf/2607.07937) | [papers.cool](https://papers.cool/arxiv/2607.07937)
- Authors: Yahan Zheng, John Guerrerio, Soroush Vosoughi, Weicheng Ma
- Published: 2026-07-08 21:34 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Preprocessing-based methods for stereotype mitigation, such as pre-/post-training on debiased corpora, are widely used in NLP. While these approaches reduce measurable stereotypes for targeted groups, we find they often induce unintended shifts-side effects, where stereotyping or counter-stereotyping can increase...

### 20 - Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution

- arXiv: [2607.08700](https://arxiv.org/abs/2607.08700) | [PDF](https://arxiv.org/pdf/2607.08700) | [papers.cool](https://papers.cool/arxiv/2607.08700)
- Authors: Ethan Leung, Elias Lumer, Corey Feld, Austin Huber, Vamse Kumar Subbiah, Kevin Paul
- Published: 2026-07-09 17:01 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, reward model; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning increasingly relies on an LLM judge to score each rubric criterion, and that judge acts as the reward model during training. Before such a signal can be trusted, we need to know how capable the judge must be and how biased it is. We study this calibration question for citation quality in deep-...

### 20 - Agentic AI and Retrieval-Augmented Models in Straight-Through Underwriting

- arXiv: [2607.07858](https://arxiv.org/abs/2607.07858) | [PDF](https://arxiv.org/pdf/2607.07858) | [papers.cool](https://papers.cool/arxiv/2607.07858)
- Authors: Robert Richardson, Josh Meyers, Brian Hartman, David Sandberg
- Published: 2026-07-08 18:43 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning, reflection; memory_and_benchmarks: evaluation
- Abstract skim: Artificial intelligence (AI) is beginning to reshape actuarial practice, particularly in domains that require reasoning over unstructured documents, heterogeneous data sources, and regulated decision workflows. Actuaries now face a design space that ranges from traditional rule-based automation to large language...

### 20 - Principled Analysis of Deep Reinforcement Learning Evaluation and Design Paradigms

- arXiv: [2607.07769](https://arxiv.org/abs/2607.07769) | [PDF](https://arxiv.org/pdf/2607.07769) | [papers.cool](https://papers.cool/arxiv/2607.07769)
- Authors: Ezgi Korkmaz
- Published: 2026-07-08 16:12 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning; memory_and_benchmarks: evaluation
- Abstract skim: Starting from the utilization of deep neural networks to approximate the state-action value function that led to winning one of the most challenging games, to algorithmic advancements that allowed solving problems without even explicitly stating the rules of the challenge at hand, reinforcement learning research has...

### 19 - Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination

- arXiv: [2607.08403](https://arxiv.org/abs/2607.08403) | [PDF](https://arxiv.org/pdf/2607.08403) | [papers.cool](https://papers.cool/arxiv/2607.08403)
- Authors: Runzhe Liu, Biquan Bie, Zihao Wang, Yuchao Ma, Yexin Liu, Xinghai Li, et al. (10 authors)
- Published: 2026-07-09 12:28 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent; reasoning: reasoning; planning_and_action: planning
- Abstract skim: The application of lightweight Large Language Models in rule-based scientific domains remains severely limited by their tendency to mimic linguistic patterns rather than reproduce axiomatic reasoning, causing frequent hallucinations. Here, we show that G-Frame, an adaptive multi-agent framework integrating Bayesian...

### 19 - TRACE: A Two-Channel Robust Attribution Watermark via Complementary Embeddings for LLM-Agent Trajectories

- arXiv: [2607.08400](https://arxiv.org/abs/2607.08400) | [PDF](https://arxiv.org/pdf/2607.08400) | [papers.cool](https://papers.cool/arxiv/2607.08400)
- Authors: Zheng Gao, Xiaoyu Li, Xiaoyan Feng, Jiaojiao Jiang, Yang Song, Yulei Sui, et al. (8 authors)
- Published: 2026-07-09 12:25 UTC | Categories: cs.AI, cs.LG
- Why it matched: agentic_rl: llm agent; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: alfworld
- Abstract skim: LLM agents reach users through resellers, who may rebrand a developer's agent or substitute a cheaper model. When provenance is disputed, attribution rests on the trajectory log (the record of tool calls, observations, and executed actions, not the model's reasoning), which the reseller stores and processes to meter...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
