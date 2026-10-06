---
name: interview-classification
description: 把 docs/interview 下的面经整理成去重分类题库:提取独立问题、规范化、语义去重、按九个分类归档到 docs/interview-bank,并保留每题来源。用于用户要求整理/分类全部或指定面经文件时。
---

# 面试题库整理

## 目标与边界

把面经中的**独立面试问题**提取出来,规范化、语义去重、分类,输出到 `docs/interview-bank/`。

- 输入:用户指定的面经文件;用户指定目录时处理该目录下所有 Markdown 面经;只有用户没有限定范围时才处理整个 `docs/interview/`。
- `docs/interview/` 只读:不删除、不覆盖、不重命名、不改正文、不写入分类信息。
- 只写 `docs/interview-bank/`:输出目录已存在时,更新本次涉及的分类文件,不动本次未处理的分类文件。
- 不处理用户未指定的文件。
- 每道题只允许一个主分类,共七类。**不是对候选人的提问**的条目(公司介绍、面试流程说明、面试官自我介绍、寒暄与信息同步、招聘信息、面试覆盖说明)不进分类文件,记入附录 `00-tech-stack.md` 的「面试覆盖说明」。

流水线:

```text
面经文件 → 提取独立问题 → 项目背景抽象 → 规范化 → 语义去重 → 分类 → 按分类写题库 → 保留来源
```

规模提示:`docs/interview/` 有 180+ 份面经。按文件分批读取,用一份临时清单(如 /tmp 下的 JSON 或文本)累积问题与来源,不要依赖上下文记住全集;语义去重针对**本次输入范围的全集**,而不是当前批次。

## 分类

每道题只允许一个 `primary_category`,共九类。

### 01-cpp

C++ / Linux / 系统编程基础本身:语言特性、OOP、STL、模板、内存、智能指针、RAII、并发、原子、mutex、线程、进程、Linux、socket、epoll、mmap。

判断标准:核心考察 C++、Linux 或系统编程知识本身,而不是用代码解决算法问题。

### 02-algorithm

数据结构 / 算法 / 编程题,**不区分语言**:数组、字符串、链表、树、图、DP、贪心、二分、回溯、LRU、LFU、Top-K、线程池、内存池、并发队列,以及用 Python / Go / Java / Rust 等语言写的编程题。

判断标准:核心要求是编写程序解决一个问题。

编程题按**实现对象所属领域**归类,不是一律进本类:纯算法 / 数据结构 / 语言设施实现(手写 shared_ptr、线程池、LRU、Python 实现矩阵旋转)→ 本类;手写 CUDA kernel、GEMM、Softmax 算子 → 04-gpu;手写 Transformer、GQA、Attention 等模型结构 → 03-ai。语言本身的基础知识(GIL、GC、反射、锁)不属于本类,归 06-other-language。

### 03-ai

模型与算法本身:深度学习、Transformer、Attention、RoPE、FFN、MoE、LLM、SFT、RLHF、DPO、GRPO、训练、Loss、Optimizer、量化、蒸馏、剪枝、CLIP、Diffusion、DiT、多模态。

若重点在部署、推理、Serving、Runtime 或分布式系统,归 05-ai-infra。

### 04-gpu

GPU 架构、CUDA、Kernel 与 GPU 侧优化:SM、Warp、Block、Grid、SIMT、CUDA、Stream、Graph、Shared Memory、Register、L1/L2、访存合并、Bank Conflict、Occupancy、Kernel 优化、GEMM、Tiling、WMMA、MMA、Tensor Core、CUTLASS、Triton、FlashAttention Kernel、Nsight、Roofline。

判断标准:核心是如何优化 GPU 上的计算、Kernel、访存或性能。

### 05-ai-infra

训练 / 推理 / 部署 / 分布式 / Serving / Runtime:AI Infra 架构、分布式训练、NCCL、AllReduce / AllGather / AllToAll、TP/PP/EP/DP、推理、Prefill、Decode、TTFT、TPOT、KV Cache、PagedAttention、连续批处理、vLLM、SGLang、TensorRT、TensorRT-LLM、llama.cpp、ONNX Runtime、算子融合、图优化、Runtime、Serving、调度、GPU 调度、模型部署、推理优化、AI 系统设计。

判断标准:核心是如何让模型、推理引擎、服务或分布式系统跑起来。

与 03-ai 的边界(全库最易两边都成立的一类):**模型与算法本身的原理**(量化格式与粒度、校准方法、模型结构、压缩方法)归 03-ai;**把模型跑起来的工程**(推理引擎、调度、显存管理、服务、集群、编译与图优化)归本类。带「部署」字样的题先看考点是模型侧还是系统侧。

### 06-other-language

Python / Go / Rust / Java / Shell 等语言本身的基础知识:Python GIL、GC、asyncio、生成器、Go goroutine / channel / GMP、Rust 所有权 / 借用 / 生命周期、JVM、Java GC、Shell。

只放语言基础与生态知识;**用这些语言写的算法 / 编程题归 02-algorithm**。

### 07-behavioral

HR 与中高层都会问的非技术问题:

- 个人动机与规划:自我介绍、为什么离职 / 转 AI Infra / 选择该公司、职业规划、优缺点、Offer 选择。
- 行业与业务看法:对行业趋势、技术路线、公司业务的判断。
- 团队协作:团队冲突、跨部门协作、推动他人与影响力。
- 难题突破:最有挑战的问题、失败经历、压力与挫折、从 0 到 1。
- 快速上手:如何快速熟悉新项目或新领域、学习方法、自驱与主动性。

本类还包含**项目复盘与经历**这一类问题,统一放在「项目与经历」主题下:项目分工与个人贡献、创新点、开源项目与论文产出、方案改进与重新设计(「如果重新设计这个项目你会怎么做」)。判断顺序:问项目事实、技术方案与取舍 → 先做项目背景抽象,再归对应技术类;问行为、反思和方法(怎么带人、怎么突破、怎么快速上手、怎么复盘)→ 本类。

命中行为关键词(自我介绍 / 英文介绍 / 职业规划 / 离职原因 / 团队协作 / 学习方法 / 最大难题 / offer / 行业看法)的条目先归本类,不要因为它写在原文的「项目经历」标题下就归技术类;一条里行为框架与技术考点并存时拆成两条,分别归本类与对应技术类。

### 非题目条目

**不是对候选人的提问**的条目不入库,记入附录 `00-tech-stack.md` 的「面试覆盖说明」:公司介绍、部门介绍、面试流程说明、面试官自我介绍、寒暄与信息同步、招聘信息、面试范围说明(如「CUDA 编程相关问题」)、泛化的项目介绍(如「介绍你的项目经历」「围绕项目深入提问」)。

它与 `## 待人工确认` 的分工:能确定是考题、只是归属拿不准的,写进对应分类文件末尾的 `## 待人工确认`;能确定不是考题的,放附录。

### 冲突裁决

| 情形 | 归属 |
| --- | --- |
| CUDA / Kernel / Warp / 访存 / Tensor Core / GEMM / GPU 性能 | 04-gpu |
| 推理 / Serving / KV Cache / 并行 / 分布式 / Runtime | 05-ai-infra |
| 模型结构、数学原理、训练算法 | 03-ai |
| 模型推理、部署、系统实现 | 05-ai-infra |
| 解释 C++ / STL / 内存 / 并发原理 | 01-cpp |
| 手写纯算法 / 数据结构 / 语言设施(不分语言) | 02-algorithm |
| 手写 CUDA kernel、GEMM、算子 | 04-gpu |
| 手写模型结构(Transformer、GQA、Attention) | 03-ai |
| 项目复盘、经历与反思类问题 | 07-behavioral 的「项目与经历」 |
| 有技术考点的项目问题(抽象为通用问题后) | 按技术领域归类 |
| 与项目无关的普通技术问题 | 按技术主题归类 |
| 非技术(HR / 职业规划 / 行业看法 / 协作 / 难题突破 / 快速上手) | 07-behavioral |
| 不是提问的流程 / 介绍类内容、招聘信息 | 不入库,记附录 |

同一主题按语境区分,例如:「FlashAttention Kernel 如何 Tiling?」→ 04-gpu,「FlashAttention 为什么能降低 LLM 推理延迟?」→ 05-ai-infra;「RoPE 的数学原理是什么?」→ 03-ai,「KV Cache 如何管理?」→ 05-ai-infra;「shared_ptr 的引用计数如何实现?」→ 01-cpp,「手写一个 shared_ptr」→ 02-algorithm。

## 提取

只提取**独立面试问题**,不要把整段面经当成一道题。

拆分判据:每个问号是一个待判单元。指向不同机制或不同对象的问句各成一题(如「Kafka 如何实现顺序消费?」与「如何保证消息不丢失?」);只有确属同一机制的不同表述才合并。一条最多拆 3 条,把一条泛化描述拆成七八个碎片不算提取。

原文:

```text
面试官先问了 CUDA Stream 是什么,然后问多个 Stream 怎么保证顺序,最后让我说一下 Stream 和 Event 的关系。
```

提取为三道题:CUDA Stream 是什么?多个 CUDA Stream 如何保证执行顺序?CUDA Stream 和 CUDA Event 有什么关系?

## 项目背景抽象

**所有与项目相关的问题**,都要先抽象成脱离项目上下文的通用问法,再进入去重与分类。原因是同一类问题在不同项目里的方案并不一样,带着项目表述的题干既没法比较,也没法合并。

做法:去掉个人指向与具体项目名(「你的」「你项目中」「简历里的 XX 项目」「实习中」「实习期间做的」),换成中性场景。只换主语与场景,不新增原文没有的约束,抽象后必须能脱离候选人独立作答。

```text
原:项目中为何针对不同场景选用不同的量化方法?GPTQ 和 SmoothQuant 分别适用什么场景?
→ 一个要覆盖多种场景的 LLM 推理服务,为什么会针对不同场景选用不同量化方法?GPTQ 与 SmoothQuant 分别适用什么场景?

原:实习中开发的 Timing 插件底层实现是什么?为什么不直接用 Nsight / NCU?
→ 自研 CUDA Timing 插件与 Nsight / NCU 在底层实现和适用场景上有什么差异?

原:单个线程计算 C 矩阵 8x8 个元素的原因
→ GEMM kernel 中为什么常让单个线程计算 8x8 个输出元素?
```

抽象完成后按技术领域归类(04-gpu / 05-ai-infra / 03-ai …),不再默认进项目类;抽象不掉、仍然依赖候选人经历的,才归 07-behavioral 的「项目与经历」。

## 规范化

把口语化、重复、残缺的问题改写成标准问题,但不改变原意,也不新增原文不存在的考点。原文含多个明确不同的问题时拆开:

```text
原文:你了解 TP 吗?TP 为什么能加速?
→ 什么是 Tensor Parallel?Tensor Parallel 为什么能够提升推理性能?
```

## 语义去重

必须做语义去重,而不是字符串去重。**顺序要求:项目类问题先做完项目背景抽象,再进入去重**,不要拿带项目上下文的原始表述判断重不重复。

合并的是题目,不是答案:同一考点在不同项目里的方案本来就不一样,合并后把全部来源累加即可,不要用某一个项目的方案代表其他项目。

应合并(同一考点的不同问法):

```text
什么是 Tensor Parallel?
Tensor Parallel 的基本原理是什么?
介绍一下 Tensor Parallel。
→ 什么是 Tensor Parallel?它的基本原理是什么?
```

不应合并(共享关键词但考点不同):

```text
什么是 Tensor Parallel?
Tensor Parallel 如何进行通信?
Tensor Parallel 的通信开销如何优化?
```

原理 ≠ 通信机制 ≠ 通信优化,三道都保留。上下位问题同理:什么是 KV Cache? / 为什么能降低 Decode 阶段的计算量? / 如何进行量化? 分属概念、原理、优化,都要保留。

合并后保留一条规范问题并汇总**全部**来源;同题问法不同但考点完全一致时可以合并。

## 输出

```text
docs/interview-bank/
├── 01-cpp.md
├── 02-algorithm.md
├── 03-ai.md
├── 04-gpu.md
├── 05-ai-infra.md
├── 06-other-language.md
├── 07-behavioral.md
└── 00-tech-stack.md      # 附录:AI Infra 技术栈与面试覆盖说明,不是题目
```

`00-tech-stack.md` 由人工维护(技术栈全景、按领域细分、岗位需求占位、面试覆盖说明),不参与结构校验;每次新增面经或岗位 JD 时按需更新。

每个文件用二级标题分主题、三级标题分子主题;题目一律写成顶层列表项,来源写在题目下方:

```markdown
# GPU / CUDA / Kernel

## CUDA

### CUDA Stream

- CUDA Stream 是什么?
  - 来源:`docs/interview/xxx-AI-Infra-一面.md`
- 多个 CUDA Stream 如何保证执行顺序?
  - 来源:`docs/interview/yyy-AI-Infra-二面.md`、`docs/interview/zzz-AI-Infra-校招.md`
```

来源写相对仓库根的路径,能定位到行号时补上(`docs/interview/xxx.md:120-125`)。去重合并的题目要列出全部来源,不得因去重丢失来源信息。

来源也可以另起一行写 `来源:` 标记再接缩进的来源列表,列表与下一条问题之间空一行;两种写法脚本都认,顶层不缩进的列表会被当成新问题。

## 校验

生成后运行脚本核对结构:

```bash
python <skill-dir>/scripts/check_interview_bank.py --bank docs/interview-bank --sources docs/interview
```

脚本检查七个分类文件是否齐全、每道题是否带来源、来源文件是否存在、是否存在跨文件完全重复的题目、`docs/interview/` 是否被改动。脚本报出的 error 必须修掉。

再加 `--reconcile` 做漏提对账:按来源文件列出「原文编号条目数 / 原文问句数(按问号计) / 入库条目数」,数字对不上的文件回查原文。它是粗筛,能发现整条漏提;一件多问的拆分是否漏了子问题,仍然要靠上面「每个问号是一个待判单元」的判据逐条核。

```bash
python <skill-dir>/scripts/check_interview_bank.py --reconcile
```

另外自查:指定面经是否全部读过;独立问题是否都提取;是否做了语义去重且没有错误合并;每道题只有一个分类;原面经未被修改;未处理未指定的文件。

## 分批处理流程

面经数量多时分批做,用中间表(TSV)保存进度,任何一批都能单独重跑。

```bash
# 1. 抽取工作清单(每条编号条目一个 id)
python <skill-dir>/scripts/build_worklist.py --sources docs/interview --out worklist.tsv [--tier T0] [--company 百度]

# 2. 逐批写分类表:列 = id[,id...] / category / topic / subtopic / 改写文本(可留空沿用原文)
#    合并到已有题目时,把题干锚点写进 id 列,例如  `123,@bank conflict`

# 3. 规范化分类表(纠正写到分类列的锚点、去掉重复与越界 id、报告非法分类)
python <skill-dir>/scripts/normalize_classify.py --in classify-T0a.tsv --min-id 1 --max-id 343

# 4. 展开成中间表(把 id 换回题干、把锚点换成目标题目的来源累加)
python <skill-dir>/scripts/classify_io.py --worklist worklist.tsv --in classify-T0a.tsv --out bank.tsv --bank-tsv <上一批的 bank.tsv>

# 5. 生成题库 markdown
python <skill-dir>/scripts/bank_io.py generate --in bank.tsv --bank docs/interview-bank
```

两条纪律:**每批先做覆盖率检查**(工作清单里该批的 id 是否都出现在分类表中),**再落库**;合并引用只写题干锚点,不要写行号——行号在中间表重建后会漂移,锚点不会。

无法确定归属的考题不要硬分类:记录到对应分类文件末尾的 `## 待人工确认` 小节,并在报告中统计。

## 报告

```text
处理文件:X 个
提取问题:X 道
去重后:X 道

分类结果:
01-cpp:X             02-algorithm:X        03-ai:X
04-gpu:X             05-ai-infra:X         06-other-language:X
07-behavioral:X

待人工确认:X 道
附录更新:00-tech-stack.md(新增技能 / 领域 / 岗位需求时)
```

用户只指定了几个文件时,只统计本次处理的文件。
