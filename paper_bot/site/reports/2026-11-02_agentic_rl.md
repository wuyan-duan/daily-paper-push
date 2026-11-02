# RL / Post-Training / Agentic RL Reading Queue - 2026-11-02

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 428. Minimum score: 8.

## Top Picks

### 57 - RTL-Interact: Training EDA-Interactive Models for Multi-Task RTL Design

- arXiv: [2610.41225](https://arxiv.org/abs/2610.41225) | [PDF](https://arxiv.org/pdf/2610.41225) | [papers.cool](https://papers.cool/arxiv/2610.41225)
- Authors: Wenxuan Shi, Yaoyu Zhu, Di Huang, Chongxiao Li, Xiaoyun Zhang, Muxin Song, et al. (16 authors)
- Published: 2026-10-30 04:03 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Large language models offer a promising route to register-transfer-level (RTL) design, but reliable implementations require checking and revision based on electronic design automation (EDA) tools' feedback. Existing RTL-specialized models often lack learned interaction with such EDA tools or rely on separate...

### 48 - Subliminal Reinforcement Learning: traits travel through a judge's scores

- arXiv: [2610.41301](https://arxiv.org/abs/2610.41301) | [PDF](https://arxiv.org/pdf/2610.41301) | [papers.cool](https://papers.cool/arxiv/2610.41301)
- Authors: Keuntae Kim, Yong Suk Choi
- Published: 2026-10-30 06:02 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, policy optimization, +1 more
- Abstract skim: Subliminal learning, the transfer of a model's trait through data with no semantic trace of it, has been shown for students trained on a teacher's text. Post-training relies on group relative policy optimization with a language-model judge, where the student learns only from its own outputs and one judge's scores....

### 48 - Steering Vectors as a Training Signal in LLM Post-Training

- arXiv: [2610.40998](https://arxiv.org/abs/2610.40998) | [PDF](https://arxiv.org/pdf/2610.40998) | [papers.cool](https://papers.cool/arxiv/2610.40998)
- Authors: Tiejin Chen, Maunil Vyas, Huaiyuan Yao, Hua Wei
- Published: 2026-10-29 21:28 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more
- Abstract skim: Steering vectors (SVs) are residual-stream directions that shift the behavior of LLMs when added to hidden states at inference time. While prior work has mainly used SVs as post-hoc controls, we ask whether the same directions can also guide parameter updates during post-training. We study this question across...

### 47 - Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping

- arXiv: [2610.40726](https://arxiv.org/abs/2610.40726) | [PDF](https://arxiv.org/pdf/2610.40726) | [papers.cool](https://papers.cool/arxiv/2610.40726)
- Authors: Zichen Bai, Yanli Wang, Yang Liu, Junhao Shi, Xueqin Liu, Jinguo Sun, et al. (12 authors)
- Published: 2026-10-29 09:02 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Asynchronous reinforcement learning (RL) is becoming a mainstream paradigm for post-training large language models (LLMs), as it improves training efficiency by updating the model as rollouts arrive. Recent work argues that group-wise sampling in GRPO does not naturally fit asynchronous RL training because rollout...

### 46 - CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

- arXiv: [2610.40799](https://arxiv.org/abs/2610.40799) | [PDF](https://arxiv.org/pdf/2610.40799) | [papers.cool](https://papers.cool/arxiv/2610.40799)
- Authors: Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang, Xiangyu Yue
- Published: 2026-10-29 18:01 UTC | Categories: cs.RO
- Why it matched: agentic_rl: tool use; rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code...

### 36 - RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks

- arXiv: [2610.42068](https://arxiv.org/abs/2610.42068) | [PDF](https://arxiv.org/pdf/2610.42068) | [papers.cool](https://papers.cool/arxiv/2610.42068)
- Authors: Xin Ming Li, Peng Hu
- Published: 2026-10-30 17:26 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: memory, episodic memory; downranked: traffic
- Abstract skim: Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions. Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to...

### 36 - CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning

- arXiv: [2610.42028](https://arxiv.org/abs/2610.42028) | [PDF](https://arxiv.org/pdf/2610.42028) | [papers.cool](https://papers.cool/arxiv/2610.42028)
- Authors: Yanming Zhang, Eric Papenhausen, Klaus Mueller
- Published: 2026-10-30 16:55 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: decision making; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Reinforcement learning is a powerful paradigm for training autonomous agents and has achieved impressive performance in complex environments. However, this success often comes at the cost of interpretability, diminishing trust and complicating efforts to debug and improve agent behavior. To address these challenges,...

### 34 - TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking

- arXiv: [2610.41275](https://arxiv.org/abs/2610.41275) | [PDF](https://arxiv.org/pdf/2610.41275) | [papers.cool](https://papers.cool/arxiv/2610.41275)
- Authors: Mingyang Lyu, Gongce Cao, Yiyang Jia, Lu Jia, Erliang Lin, Yuhao Zhang, et al. (10 authors)
- Published: 2026-10-30 05:26 UTC | Categories: cs.RO
- Why it matched: rl_post_training: post-training, post training, policy optimization, ppo; memory_and_benchmarks: evaluation
- Abstract skim: Embodied visual tracking requires a robot to follow a language-specified person under occlusion, look-alike distractors, and ambiguous instructions. We show that improving tracking persistence can simultaneously increase safety violations. Using a compact 0.6B vision-language-action (VLA) tracker with a frozen...

### 34 - CoFiBreak: A Coarse-to-Fine Diversity Reward for Effective Multi-Turn Jailbreak

- arXiv: [2610.40926](https://arxiv.org/abs/2610.40926) | [PDF](https://arxiv.org/pdf/2610.40926) | [papers.cool](https://papers.cool/arxiv/2610.40926)
- Authors: Jialin Song, Xiaodong Liu, Weiwei Yang, Mingqian Feng, Chengquan Guo, Qiyao Ma, et al. (10 authors)
- Published: 2026-10-29 19:51 UTC | Categories: cs.CL
- Why it matched: rl_post_training: reinforcement learning, policy optimization, group relative policy optimization, grpo; memory_and_benchmarks: evaluation
- Abstract skim: Automated red teaming trains an attacker large language model (LLM) to elicit harmful responses from a victim LLM, but reinforcement learning can collapse attackers onto a narrow set of prompts when attack success is the only reward. Such a collapse of attack diversity can bias safety evaluation toward repeatedly...

### 33 - Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective

- arXiv: [2610.41903](https://arxiv.org/abs/2610.41903) | [PDF](https://arxiv.org/pdf/2610.41903) | [papers.cool](https://papers.cool/arxiv/2610.41903)
- Authors: Yuxin Chen, Yuejie Chi, Jianqing Fan, Gen Li, Yuting Wei, Yuling Yan
- Published: 2026-10-30 15:39 UTC | Categories: cs.LG
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; planning_and_action: decision making
- Abstract skim: Reinforcement learning (RL) embodies a foundational paradigm for sequential decision-making in the face of uncertainty. The rapid growth of model complexity in emerging applications has significantly amplified the challenges of achieving data-efficient RL, particularly in sample-starved scenarios where data...

### 33 - Can Personal Requirements Become Supervision for Planning?

- arXiv: [2610.40992](https://arxiv.org/abs/2610.40992) | [PDF](https://arxiv.org/pdf/2610.40992) | [papers.cool](https://papers.cool/arxiv/2610.40992)
- Authors: Junwei Wu, Runze Yan, Yuzhang Xie, Hanqi Luo, Ziwei Dong, Jiaying Lu, et al. (8 authors)
- Published: 2026-10-29 21:20 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: planning; memory_and_benchmarks: evaluation
- Abstract skim: Managing multiple chronic conditions through diet requires satisfying disease- and medication-specific requirements jointly across meals and days while preserving established eating habits. These requirements are public in clinical guidelines and drug labels, yet turning them into a feasible plan for one person...

### 32 - Coarse-Graining Optimal Transport for Rollout-Free Post-Training of Flow Matching

- arXiv: [2610.41269](https://arxiv.org/abs/2610.41269) | [PDF](https://arxiv.org/pdf/2610.41269) | [papers.cool](https://papers.cool/arxiv/2610.41269)
- Authors: Soon Hoe Lim, Aditi Gupta, Michael W. Mahoney, N. Benjamin Erichson
- Published: 2026-10-30 05:24 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Flow matching depends critically on the coupling used to pair source and target samples. Optimal transport (OT) couplings can reduce velocity conflict and straighten trajectories; but, in practice, challenges remain: the source comes from a continuous distribution, only a finite number of target samples data are...

### 32 - From Evaluation to Evolution: Benchmarking Image Editing and Evolving Image Models

- arXiv: [2610.41210](https://arxiv.org/abs/2610.41210) | [PDF](https://arxiv.org/pdf/2610.41210) | [papers.cool](https://papers.cool/arxiv/2610.41210)
- Authors: Jun He, Canmiao Fu, Ying Zhang, Zhipeng Huang, Chenyu Mu, Yazhen Xie, et al. (10 authors)
- Published: 2026-10-30 03:42 UTC | Categories: cs.AI
- Why it matched: agentic_rl: multi-agent, agent harness; reasoning: self-improvement, self improvement; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Real-world image editing requires coordinating multiple visual transformations with content preservation and reference constraints, yet aggregate scores can readily obscure unmet local requirements. Effective evaluation must therefore identify local failures and translate them into priorities for subsequent model...

### 31 - GRIT: Gradient Masking for Visually Misgrounded Tokens in Text-Rich Reasoning

- arXiv: [2610.41629](https://arxiv.org/abs/2610.41629) | [PDF](https://arxiv.org/pdf/2610.41629) | [papers.cool](https://papers.cool/arxiv/2610.41629)
- Authors: Chanseul Cho, Noori Bae, Dongheon Lee, Youngmin Ro
- Published: 2026-10-30 12:05 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has recently been extended to vision-language models (VLMs), yet its effectiveness remains limited for text-rich reasoning tasks. We highlight a key factor contributing to this limitation: models frequently arrive at correct final answers despite misperceiving...

### 30 - Chance-Constrained Inspection Viewpoint Sequencing for On-Orbit Servicing via Safe Reinforcement Learning

- arXiv: [2610.41639](https://arxiv.org/abs/2610.41639) | [PDF](https://arxiv.org/pdf/2610.41639) | [papers.cool](https://papers.cool/arxiv/2610.41639)
- Authors: Chloé Carer, Adam Abdin
- Published: 2026-10-30 12:15 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: planning, trajectory
- Abstract skim: Autonomous inspection of a target spacecraft is typically the initial step in on-orbit servicing. Planning close-proximity observation viewpoints involves a complex combinatorial problem constrained by coverage, fuel, and safety considerations. This paper models the viewpoint selection as a Constrained Markov...

### 29 - Latent Reasoning in Continuous Space for Unified Multimodal Models

- arXiv: [2610.42149](https://arxiv.org/abs/2610.42149) | [PDF](https://arxiv.org/pdf/2610.42149) | [papers.cool](https://papers.cool/arxiv/2610.42149)
- Authors: Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin
- Published: 2026-10-30 17:59 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning, chain-of-thought, chain of thought
- Abstract skim: Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time...

### 29 - CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness

- arXiv: [2610.42054](https://arxiv.org/abs/2610.42054) | [PDF](https://arxiv.org/pdf/2610.42054) | [papers.cool](https://papers.cool/arxiv/2610.42054)
- Authors: Xiao Yu, Justin Chih-Yao Chen, Zaid Khan, Hyunji Lee, Mohit Bansal
- Published: 2026-10-30 17:18 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: reinforcement learning, rlvr; reasoning: reasoning
- Abstract skim: Reinforcement learning with verifiable rewards (RLVR) has become the standard method for training language models to reason. However, RLVR typically relies solely on outcome correctness, which does not guarantee that the CoT causally contributes to the final answer. Without this connection, outcome rewards may fail...

### 26 - TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language Agents

- arXiv: [2610.41697](https://arxiv.org/abs/2610.41697) | [PDF](https://arxiv.org/pdf/2610.41697) | [papers.cool](https://papers.cool/arxiv/2610.41697)
- Authors: Rui Yu, Chong Mu, Jinchuan Zhang
- Published: 2026-10-30 13:04 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: policy optimization; planning_and_action: trajectory, rollout; memory_and_benchmarks: evaluation, alfworld
- Abstract skim: Training interactive language agents from terminal outcomes poses three coupled problems: which task and state continuations to sample, how to assign delayed feedback to decisions, and how to aggregate token losses for multi-token actions. We present TSBPO, a tree-structured sampling-to-update paradigm that...

### 25 - When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning

- arXiv: [2610.41962](https://arxiv.org/abs/2610.41962) | [PDF](https://arxiv.org/pdf/2610.41962) | [papers.cool](https://papers.cool/arxiv/2610.41962)
- Authors: Eduardo C. Garrido-Merchán
- Published: 2026-10-30 16:12 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning; reasoning: self-play
- Abstract skim: Reinforcement learning and game theory describe the same object from two sides. Game theory says what a rational outcome of a strategic interaction is; reinforcement learning says how an agent could reach one through experience. The two literatures nevertheless keep separate vocabularies for identical structures,...

### 25 - Risk-Sensitive Mission Planning for Multi-Target On-Orbit Inspection via Distributional Reinforcement Learning

- arXiv: [2610.41647](https://arxiv.org/abs/2610.41647) | [PDF](https://arxiv.org/pdf/2610.41647) | [papers.cool](https://papers.cool/arxiv/2610.41647)
- Authors: Adam Abdin
- Published: 2026-10-30 12:20 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; planning_and_action: planning, decision making
- Abstract skim: Multi-target on-orbit servicing missions require planning tools that can adapt to evolving operational conditions while accounting for the outcome variability inherent to safety-critical spaceflight. This paper presents an adaptive planning approach for multi-target servicing campaigns in low Earth orbit and applies...

### 24 - Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning

- arXiv: [2610.41949](https://arxiv.org/abs/2610.41949) | [PDF](https://arxiv.org/pdf/2610.41949) | [papers.cool](https://papers.cool/arxiv/2610.41949)
- Authors: Zhuguanyu Wu, Congjia Chen, Ruihao Gong, Yang Yong, Shiqiao Gu, Yi Xu, et al. (7 authors)
- Published: 2026-10-30 16:05 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo
- Abstract skim: Few-step flow models generate samples through a handful of large denoising transitions. Applying GRPO to such models requires introducing stochasticity into the denoising transitions, and when a single transition spans a wide range of noise levels, the choice of the resulting stochastic policy becomes a major factor...

### 24 - Reliability-Weighted Direct Preference Optimization: Penalized Weights for Robust Preference Learning

- arXiv: [2610.41588](https://arxiv.org/abs/2610.41588) | [PDF](https://arxiv.org/pdf/2610.41588) | [papers.cool](https://papers.cool/arxiv/2610.41588)
- Authors: Bin Luo, Param Venkat Vivek Kesireddy, Anil Vallepu
- Published: 2026-10-30 11:24 UTC | Categories: cs.LG
- Why it matched: rl_post_training: preference optimization, dpo
- Abstract skim: Direct Preference Optimization (DPO) treats every reported comparison as correct, yet preference data contain reversed, tied or otherwise noisy comparisons. RW-DPO gives each comparison an unknown reliability weight $w_i\in[0,1]$ that enters the likelihood linearly -- DPO is $w\equiv1$, a reversed comparison $w_i=0$...

### 24 - bf16 Rounding Silently Discards Most RL Policy Updates: A Hidden Training-Inference Mismatch and an Unbiased One-Line Fix

- arXiv: [2610.41073](https://arxiv.org/abs/2610.41073) | [PDF](https://arxiv.org/pdf/2610.41073) | [papers.cool](https://papers.cool/arxiv/2610.41073)
- Authors: Andrew Gao, William Gao
- Published: 2026-10-29 23:40 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning
- Abstract skim: Reinforcement learning (RL) post-training of language models keeps fp32 master weights in the optimizer and serves rollouts from a bf16 copy produced by round-to-nearest conversion. At the learning rates in common use, most per-step updates are smaller than half a bf16 spacing and the conversion discards them: on...

### 23 - Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and Evaluating Transfer

- arXiv: [2610.41296](https://arxiv.org/abs/2610.41296) | [PDF](https://arxiv.org/pdf/2610.41296) | [papers.cool](https://papers.cool/arxiv/2610.41296)
- Authors: Minju Gwak, Alan Ritter
- Published: 2026-10-30 05:57 UTC | Categories: cs.AI
- Why it matched: reasoning: reasoning, self-improvement, self improvement; planning_and_action: trajectory; memory_and_benchmarks: benchmark, evaluation
- Abstract skim: Answer-level rewards cannot distinguish reasoning traces with equally correct outcomes. We study whether auxiliary trajectory preferences improve small-language-model self-improvement and transfer under limited supervision. We compare confidence-based (SC) and entropy-based metrics (UID-Conj.), which combines global...

### 23 - Do Language Models Know What Compelling Scientific Evidence Looks Like?

- arXiv: [2610.41015](https://arxiv.org/abs/2610.41015) | [PDF](https://arxiv.org/pdf/2610.41015) | [papers.cool](https://papers.cool/arxiv/2610.41015)
- Authors: Conor Igoe, Gabriel Grand, Zane Koch, Albert Bou, Eli Moss, Michaela M. Hinks, et al. (9 authors)
- Published: 2026-10-29 21:51 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning, deliberation; memory_and_benchmarks: benchmark; downranked: genome, driving
- Abstract skim: Expert scientists excel at weighing empirical findings from multiple sources that vary in both statistical reliability and epistemic relevance. To what extent are language models, which are increasingly driving autonomous discovery systems, capable of such evidence deliberation? We introduce EDB-Bio, a scientific...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
