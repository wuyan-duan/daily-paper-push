# RL / Post-Training / Agentic RL Reading Queue - 2026-10-05

Source: papers.cool Atom feeds for cs.AI, cs.CL, cs.LG, cs.RO, cs.MA.
Window: last 7 day(s). Candidates fetched in window: 576. Minimum score: 8.

## Top Picks

### 60 - All Work And No Play Makes Jack a Dull Boy: Understanding and Preventing Catastrophic Strategy Collapse in RLVR

- arXiv: [2610.02835](https://arxiv.org/abs/2610.02835) | [PDF](https://arxiv.org/pdf/2610.02835) | [papers.cool](https://papers.cool/arxiv/2610.02835)
- Authors: Qiyuan Huang, Tianshi Xu, Meng Li
- Published: 2026-10-02 05:27 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr, +1 more; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: During post-training of large language models (LLMs) with Reinforcement Learning with Verifiable Rewards (RLVR), GRPO-style algorithms can exhibit severe late-stage collapse. Prompt-based probing reveals that this is not benign strategic pruning, but a harmful contraction of effective strategy capacity that makes...

### 48 - FSPO: Policy-Consistent Risk and Pareto-Feasible Control for Budgeted LLM RL Post-Training

- arXiv: [2610.02828](https://arxiv.org/abs/2610.02828) | [PDF](https://arxiv.org/pdf/2610.02828) | [papers.cool](https://papers.cool/arxiv/2610.02828)
- Authors: Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Daren Zha, et al. (7 authors)
- Published: 2026-10-02 05:19 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, grpo; planning_and_action: trajectory, rollout; memory_and_benchmarks: evaluation
- Abstract skim: Adaptive LLM reinforcement-learning post-training changes multiple training actuators online, including rollout temperature, group size, clipping, KL regularization, verifier allocation, and update budget. Three coupled issues remain unresolved. A future-risk model trained from behavior trajectories need not...

### 47 - AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning

- arXiv: [2610.03223](https://arxiv.org/abs/2610.03223) | [PDF](https://arxiv.org/pdf/2610.03223) | [papers.cool](https://papers.cool/arxiv/2610.03223)
- Authors: Xin Wang, Wenhao Wu, Menghao Zhang, Zhi Wang, Kun Shao, Jian Luan
- Published: 2026-10-02 12:38 UTC | Categories: cs.CL, cs.LG
- Why it matched: agentic_rl: agentic reinforcement learning; rl_post_training: reinforcement learning; planning_and_action: trajectory; memory_and_benchmarks: alfworld, scienceworld
- Abstract skim: Long-horizon LLM agents are typically trained with sparse outcome rewards, making trajectory-level objectives too coarse to distinguish the contribution of individual decisions. Step-level credit assignment provides finer-grained supervision, but its estimates can be unreliable because observed returns also depend...

### 45 - Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT

- arXiv: [2610.03361](https://arxiv.org/abs/2610.03361) | [PDF](https://arxiv.org/pdf/2610.03361) | [papers.cool](https://papers.cool/arxiv/2610.03361)
- Authors: Joery Ariën de Vries, Neil David Lawrence, Zhenwen Dai
- Published: 2026-10-02 14:24 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: post-training, post training, grpo, ppo, +1 more; planning_and_action: acting; memory_and_benchmarks: memory
- Abstract skim: Critic-free reinforcement fine-tuning (RFT) for agentic large language models is often done through GRPO-style methods, which compute a group baseline over repeated rollouts to reduce target variance. However, this setup is ill-suited to agents acting in stateful environments such as live services or security...

### 45 - Text-Centric Post-Training for Omni-Modal Reasoning

- arXiv: [2610.02819](https://arxiv.org/abs/2610.02819) | [PDF](https://arxiv.org/pdf/2610.02819) | [papers.cool](https://papers.cool/arxiv/2610.02819)
- Authors: Ziyang Cheng, Yuhao Wang, Hongcheng Liu, Qimin Wu, Jingru Fan, Chen Qian, et al. (8 authors)
- Published: 2026-10-02 05:08 UTC | Categories: cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; reasoning: reasoning
- Abstract skim: Improving joint audio-visual reasoning in Omni Large Language Models typically incurs substantial data construction and training costs. Our diagnostics reveal multi-hop reasoning difficulties despite correct answers to all corresponding single-hop questions and suggest partial decoupling in the local optimization of...

### 44 - Lexicographic Multi-Objective On-Policy Distillation

- arXiv: [2610.02359](https://arxiv.org/abs/2610.02359) | [PDF](https://arxiv.org/pdf/2610.02359) | [papers.cool](https://papers.cool/arxiv/2610.02359)
- Authors: Doseok Jang, Jon Ander Campos, Youran Qi
- Published: 2026-10-01 18:35 UTC | Categories: cs.AI, cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, rlvr; reasoning: reasoning; planning_and_action: rollout
- Abstract skim: Reinforcement learning from verifiable rewards (RLVR) usually optimizes answer correctness, yet useful language-model behavior also requires high-quality reasoning and concise responses. Existing multi-reward post-training methods typically scalarize rewards or combine specialists without explicitly protecting a...

### 42 - Turnover-Orthogonal Credit Assignment for Open-Team Multi-Agent Reinforcement Learning

- arXiv: [2610.02847](https://arxiv.org/abs/2610.02847) | [PDF](https://arxiv.org/pdf/2610.02847) | [papers.cool](https://papers.cool/arxiv/2610.02847)
- Authors: Amit Thakur, Mukesh Singhal
- Published: 2026-10-02 05:35 UTC | Categories: cs.LG, cs.MA
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning; memory_and_benchmarks: benchmark
- Abstract skim: Open-team multi-agent reinforcement learning studies cooperative systems in which agents may join, leave, or be replaced during an episode. In such settings, the team return changes both because agents choose useful actions and because the active population itself changes. Standard centralized critics and shared...

### 40 - Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective

- arXiv: [2610.03185](https://arxiv.org/abs/2610.03185) | [PDF](https://arxiv.org/pdf/2610.03185) | [papers.cool](https://papers.cool/arxiv/2610.03185)
- Authors: Han Cui, Jianhao Yan, Yun Luo, Hongbo Zhang, Zhizhang Fu, Yue Zhang
- Published: 2026-10-02 11:57 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training, reinforcement learning, reward model
- Abstract skim: On-policy distillation (OPD) has become an important approach to language model post-training. However, despite its performance gains, OPD can also collapse into excessively long and repetitive generation, and the mechanism underlying these divergent outcomes remains poorly understood. We explain these outcomes...

### 33 - Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis

- arXiv: [2610.03548](https://arxiv.org/abs/2610.03548) | [PDF](https://arxiv.org/pdf/2610.03548) | [papers.cool](https://papers.cool/arxiv/2610.03548)
- Authors: Wenlong Zhang, Zhengbo Jiao, Chenxu Zhang, Lekang Jiang, SiYuan Ma, Qituan Zhang, et al. (8 authors)
- Published: 2026-10-02 16:30 UTC | Categories: cs.AI
- Why it matched: rl_post_training: grpo; reasoning: reasoning, self-improvement, self improvement
- Abstract skim: Generating progressively harder reasoning problems requires synthesis procedures that adapt as the task distribution evolves. Existing task-level recursion reuses generated problems as seeds but leaves the construction harness unchanged. We present task-harness co-evolution, a framework for recursive harness self-...

### 32 - Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards

- arXiv: [2610.02967](https://arxiv.org/abs/2610.02967) | [PDF](https://arxiv.org/pdf/2610.02967) | [papers.cool](https://papers.cool/arxiv/2610.02967)
- Authors: Yuanhao Ban, I-Hung Hsu, Anastasios Angelopoulos, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh
- Published: 2026-10-02 08:05 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, preference optimization
- Abstract skim: Recent text-to-image generation models have achieved remarkable visual quality, but improving them through post-training remains challenging because no single reward signal captures the full range of human preference. In this work, we develop a simple and effective post-training recipe for open-domain text-to-image...

### 32 - MetaRubric: Learning to Reward for Rubric-Based Reinforcement Learning

- arXiv: [2610.02824](https://arxiv.org/abs/2610.02824) | [PDF](https://arxiv.org/pdf/2610.02824) | [papers.cool](https://papers.cool/arxiv/2610.02824)
- Authors: Yuxuan Fan, Jaehong Yoon
- Published: 2026-10-02 05:16 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization, grpo
- Abstract skim: Rubric-based reinforcement learning extends reward-driven optimization to open-ended tasks by assigning partial credit to individual response requirements. However, rubric judges can assign a high criterion score even when the information or action it requires is absent from the response, a failure mode we term...

### 32 - Mitigating Social Sycophancy via Pluralistic Preference Optimization

- arXiv: [2610.02568](https://arxiv.org/abs/2610.02568) | [PDF](https://arxiv.org/pdf/2610.02568) | [papers.cool](https://papers.cool/arxiv/2610.02568)
- Authors: Stephane Hatgis-Kessell, Myra Cheng, Xiaoxuan Hou, Qian Hu, Rahul Gupta, Natasha Jaques, et al. (7 authors)
- Published: 2026-10-01 23:00 UTC | Categories: cs.AI
- Why it matched: rl_post_training: post-training, post training, preference optimization
- Abstract skim: Personal advice, including relationship advice, now ranks among the most common uses of generative AI. But language models (LMs) exhibit sycophancy: they affirm users much more often than humans do, which can make people overconfident and less willing to repair their relationships after a conflict. Prior work on...

### 32 - Multi-Fidelity Policy Gradients Stabilize Data-Scarce Reinforcement Learning

- arXiv: [2610.02505](https://arxiv.org/abs/2610.02505) | [PDF](https://arxiv.org/pdf/2610.02505) | [papers.cool](https://papers.cool/arxiv/2610.02505)
- Authors: Xinjie Liu, Ruihan Zhao, Anirban Chaudhuri, Cyrus Neary, Ufuk Topcu, David Fridovich-Keil
- Published: 2026-10-01 21:27 UTC | Categories: cs.AI, cs.LG, cs.RO
- Why it matched: rl_post_training: reinforcement learning, policy optimization, ppo
- Abstract skim: Policy gradient methods for on-policy reinforcement learning (RL) can become unstable when expensive, scarce target-domain data yield noisy gradient estimates. We address this challenge by complementing limited high-fidelity (HF) target-domain data with abundant, cheap, but biased low-fidelity (LF) data, e.g., from...

### 30 - Planning to Learn

- arXiv: [2610.03667](https://arxiv.org/abs/2610.03667) | [PDF](https://arxiv.org/pdf/2610.03667) | [papers.cool](https://papers.cool/arxiv/2610.03667)
- Authors: Ian Osband
- Published: 2026-10-02 17:38 UTC | Categories: cs.LG
- Why it matched: rl_post_training: post-training, post training, reinforcement learning; planning_and_action: planning
- Abstract skim: Policy-gradient methods are central to modern reinforcement learning, including LLM post-training. When they struggle, the usual suspects are exploration, credit assignment and action-sampling noise. Classification has none of them. A classifier is a policy whose expected reward, its \emph{expected accuracy}, is the...

### 30 - EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures

- arXiv: [2610.03394](https://arxiv.org/abs/2610.03394) | [PDF](https://arxiv.org/pdf/2610.03394) | [papers.cool](https://papers.cool/arxiv/2610.03394)
- Authors: Yuhai Long, Yuanxin Wei, Kai Wu, Jinhui Wei, Dan Huang, Jiangsu Du
- Published: 2026-10-02 14:43 UTC | Categories: cs.MA
- Why it matched: agentic_rl: multi-agent, tool use; reasoning: reasoning; memory_and_benchmarks: memory
- Abstract skim: Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore,...

### 29 - Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps

- arXiv: [2610.02740](https://arxiv.org/abs/2610.02740) | [PDF](https://arxiv.org/pdf/2610.02740) | [papers.cool](https://papers.cool/arxiv/2610.02740)
- Authors: Jiaxin Zhang, Xiangyu Peng, Qinglin Chen, Yu Li, Hiroaki Hayashi, Chien-Sheng Wu
- Published: 2026-10-02 03:12 UTC | Categories: cs.AI, cs.LG
- Why it matched: rl_post_training: reinforcement learning, grpo; planning_and_action: rollout; memory_and_benchmarks: evaluation
- Abstract skim: Reinforcement learning for long-horizon agents relies on purely retrospective training signals: credit is assigned only after observing environmental consequences, leaving the agent's belief at action time invisible to the gradient. We introduce Prospective Hindsight (PH), a self-calibrating training principle that...

### 29 - Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents

- arXiv: [2610.02525](https://arxiv.org/abs/2610.02525) | [PDF](https://arxiv.org/pdf/2610.02525) | [papers.cool](https://papers.cool/arxiv/2610.02525)
- Authors: Ankur Samanta, Yonathan Efroni, Paul Sajda, Kaveh Hassani, Anirudh Goyal
- Published: 2026-10-01 21:54 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; reasoning: reasoning
- Abstract skim: Long-horizon research agents must decide both how to investigate and what to investigate next as evidence accumulates. This is hard to learn because such decisions are sparse in long execution traces, and their consequences may emerge several investigations later. We introduce Meta-reasoning for Iterative Research...

### 28 - Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models

- arXiv: [2610.03665](https://arxiv.org/abs/2610.03665) | [PDF](https://arxiv.org/pdf/2610.03665) | [papers.cool](https://papers.cool/arxiv/2610.03665)
- Authors: Seo Hyun Kim, Sunwoo Hong, Younwoo Choi, Chen-Hao Chao, Se-Young Yun, Rahul G. Krishnan
- Published: 2026-10-02 17:37 UTC | Categories: cs.CL, cs.LG
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: trajectory
- Abstract skim: Masked diffusion language models (dLMs) offer a promising parallel alternative to autoregressive models for complex reasoning. However, they face a distinct credit-assignment challenge, since a few commitments during denoising sharply reduce the uncertainty over the remaining masked positions and shape much of the...

### 28 - A Near-Zero Monitor Readout Is Not Evidence of Behavioral Control

- arXiv: [2610.03458](https://arxiv.org/abs/2610.03458) | [PDF](https://arxiv.org/pdf/2610.03458) | [papers.cool](https://papers.cool/arxiv/2610.03458)
- Authors: Zhe Zhou, Tianhua Tao
- Published: 2026-10-02 15:33 UTC | Categories: cs.AI, cs.CL
- Why it matched: rl_post_training: post-training, post training; reasoning: reasoning; planning_and_action: planning
- Abstract skim: Post-training with verifiable rewards can induce reward hacking, motivating the use of monitors within the training objective rather than solely for offline auditing. We show that a low monitor readout does not identify whether such an intervention controls behavior. In a code-generation environment whose dominant...

### 28 - Beyond Single Videos: Benchmarking and Active Evidence Seeking for E-Commerce Cross-Video Reasoning

- arXiv: [2610.03099](https://arxiv.org/abs/2610.03099) | [PDF](https://arxiv.org/pdf/2610.03099) | [papers.cool](https://papers.cool/arxiv/2610.03099)
- Authors: Jinghan Zhao, Yiman Hu, Liang Wu, Jian Xu, Bo Zheng
- Published: 2026-10-02 10:19 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning; reasoning: reasoning; planning_and_action: trajectory; memory_and_benchmarks: benchmark
- Abstract skim: E-commerce videos are information-dense and frequently compared by consumers evaluating products and merchants assessing marketing strategies. However, existing multimodal models mainly focus on single-video understanding and have limited ability to compare information across videos. We introduce AdsCVR, the first...

### 28 - Permutation Robustness Is Not Enough: Action Collapse in Multi-Agent Transformer Policies

- arXiv: [2610.02848](https://arxiv.org/abs/2610.02848) | [PDF](https://arxiv.org/pdf/2610.02848) | [papers.cool](https://papers.cool/arxiv/2610.02848)
- Authors: Amit Thakur, Mukesh Singhal
- Published: 2026-10-02 05:35 UTC | Categories: cs.LG, cs.MA, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: ppo
- Abstract skim: Transformer policies are attractive for multi-agent robot learning because self-attention can model interactions among agents. However, multi-agent teams are unordered, while transformers typically process agents as ordered token sequences. We study how this mismatch affects cooperative navigation policies under...

### 28 - Test-time Multi-agent Coordination by Decomposed Value Gradient Flow

- arXiv: [2610.02554](https://arxiv.org/abs/2610.02554) | [PDF](https://arxiv.org/pdf/2610.02554) | [papers.cool](https://papers.cool/arxiv/2610.02554)
- Authors: Dongsu Lee, Haoran Xu, Amy Zhang
- Published: 2026-10-01 22:38 UTC | Categories: cs.LG, cs.RO
- Why it matched: agentic_rl: multi-agent; rl_post_training: reinforcement learning
- Abstract skim: Offline multi-agent reinforcement learning (MARL) faces a persistent trade-off. Expressive generative policies can represent multi-modal coordination in the data, but cannot distinguish high-value regions, while value-optimized policies exploit the learned Q-function but collapse the multi-modal into a single...

### 27 - On the Convergence of Success Conditioning for Policy Optimization

- arXiv: [2610.03642](https://arxiv.org/abs/2610.03642) | [PDF](https://arxiv.org/pdf/2610.03642) | [papers.cool](https://papers.cool/arxiv/2610.03642)
- Authors: Matthew Brun, Xu Andy Sun
- Published: 2026-10-02 17:29 UTC | Categories: cs.LG
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: decision making
- Abstract skim: Success conditioning is a strategy for improving decision-making policies in stochastic environments; it updates a policy by increasing the probability of taking actions that yield successful outcomes. Success conditioning is common to many reinforcement learning applications, yet its limiting behavior and...

### 27 - Credit Where It Matters: Dependency-Aware Policy Optimization for Terminal Agents

- arXiv: [2610.03634](https://arxiv.org/abs/2610.03634) | [PDF](https://arxiv.org/pdf/2610.03634) | [papers.cool](https://papers.cool/arxiv/2610.03634)
- Authors: Yu Li, Guangfeng Cai, Long-Fei Li, Shuo Han, Shengtian Yang, Han Luo, et al. (8 authors)
- Published: 2026-10-02 17:24 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, policy optimization; planning_and_action: trajectory
- Abstract skim: Terminal-using agents benefit from reinforcement learning (RL) in coding, debugging, and other multi-step terminal tasks. In these tasks, later commands often depend on information or intermediate results produced by earlier commands. However, existing trajectory-level and step-level credit assignment methods do not...

### 26 - When a Correct Reward Is Not Enough: Diagnosing and Guiding PPO in an Analytically Solved Broker-Trader Game

- arXiv: [2610.03598](https://arxiv.org/abs/2610.03598) | [PDF](https://arxiv.org/pdf/2610.03598) | [papers.cool](https://papers.cool/arxiv/2610.03598)
- Authors: Siu Tung Wong, Carlo Campajola
- Published: 2026-10-02 17:03 UTC | Categories: cs.AI
- Why it matched: rl_post_training: reinforcement learning, ppo; memory_and_benchmarks: benchmark
- Abstract skim: Reinforcement learning (RL) is increasingly used for financial optimal-control problems when complex dynamics make analytical strategies difficult to obtain. There are financial mathematics literactures which provides many solved models whose equations and controls could evaluate and guide learning; we ask whether...

## Tuning Notes

- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.
- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.
