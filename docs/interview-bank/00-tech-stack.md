# AI Infra 技术栈(附录)

本文件不是题库,而是配套的技能地图:把 `docs/interview/` 全量面经里出现的语言、框架、平台、工具与领域知识汇总成一张技术栈全景,用来对照技能缺口、判断岗位方向。题目本身在 `01`–`07` 的分类文件里。

频次取自 181 份面经、1778 条编号条目,括号内为「题库条目数 / 原文出现次数」。

## 一、通用技术栈

### 语言与指令

- **C++(29 / 86)**:语言特性、STL、内存管理、并发,是 AI Infra 面试的基础盘,几乎每场必问 → `01-cpp`
- **CUDA C++(50 / 118)**:出现频次最高的单项技能;编程模型、访存优化、Kernel 实现 → `04-gpu`
- **Python(11 / 16)**:GIL、GC、装饰器、深浅拷贝、进程与线程 → `06-other-language`
- **SQL(3 / 4)**:索引、执行计划、事务 → `05-ai-infra` 的数据库主题
- **OpenCL(4 / 4)**:执行流程、kernel 参数、分支与掩码 → `04-gpu` 的并行编程主题
- **Go / Java / C#(3 / 3 / 1)**:GMP 调度、锁与 GC、线程池、事件机制 → `06-other-language`
- **PTX / SASS(2 / 1)、NEON / 汇编(2 / 2)**:底层指令与硬件细节 → `04-gpu`、`01-cpp`
- **Shell、Rust:语料未覆盖**,待补(见第三节)

### 编译、算子与性能

- **算子优化(高频贯穿)**:访存优化、Kernel 实现、GEMM/Conv 分块、算子融合 → `04-gpu` 的「Kernel 与性能优化」
- **TVM(9 / 16)、MLIR(7 / 9)、LLVM(1 / 3)、XLA(3 / 4)、Halide(2 / 2)**:编译栈与图优化 → `05-ai-infra` 的「编译与图优化」
- **Triton(6 / 8)、CUTLASS / CuTe(1 / 2)、Marlin(1 / 1)、PPL(1 / 1)**:算子库与 DSL → `04-gpu`
- **性能分析(贯穿)**:Profiling 方法、Nsight / NCU(2 / 5、1 / 1)、Roofline、SOL、memory-bound 与 compute-bound 判定 → `04-gpu` 的「性能分析与建模」「调试与性能分析」

### 训练框架与并行

- **PyTorch(8 / 13)**:DDP、图优化、性能分析工具、GPU 资源管理 → `05-ai-infra` 的「训练框架」
- **DeepSpeed / ZeRO(7 / 11、4 / 9)**:Stage 1/2/3 的切分与通信、显存估算 → `05-ai-infra` 的「分布式训练」
- **Megatron(2 / 4)**:TP/SP 切分与通信、序列并行 → `05-ai-infra` 的「分布式训练」
- **FSDP(1 / 1)、Ray(1 / 2)、MindSpore(2 / 2)、TensorFlow(0 / 1)** → `05-ai-infra`、`06-other-language`
- **并行策略**:DP / TP / PP / EP / SP、3D 并行、Zero-Bubble、DualPipe、1F1B → `05-ai-infra` 的「分布式训练」

### 推理与运行时

- **vLLM(6 / 26)**:PagedAttention、Continuous Batching、Chunked Prefill、调度器、Prefix Cache → `05-ai-infra` 的「推理与部署」
- **TensorRT / TensorRT-LLM(7 / 12)**:底层加速原理、Plugin 自定义算子、模型转换问题 → `05-ai-infra`
- **SGLang(4 / 7)、FasterTransformer(1 / 2)、fastllm(1 / 1)、ncnn(2 / 2)、OpenVINO(1 / 1)** → `05-ai-infra`
- **国产栈**:昇腾 CANN / MindIE(1 / 1、1 / 1)、达芬奇架构、RK3588 → `04-gpu`、`05-ai-infra`
- **服务侧**:PD 分离、AF 分离、投机解码、KV Cache 优化与量化、显存池、Memory Pool → `05-ai-infra`

### 通信与互连

- **集合通信**:AllReduce / All-Reduce(5+4 / 10)、AllGather、AllToAll、Ring / Tree AllReduce → `05-ai-infra`
- **库与协议**:NCCL(2 / 3)、NVSHMEM(2 / 2)、NVLink(3 / 3)、RDMA(3 / 3)、MPI(2 / 2)、OpenMP(3 / 4) → `05-ai-infra`、`01-cpp`
- **MoE 通信**:DeepEP(1 / 1)、EPLB(1 / 1)、Expert Parallelism → `05-ai-infra`、`03-ai`

### 硬件与平台

- **GPU(35 / 60)**:架构与调度、显存层级、L1/L2、Shared Memory、Tensor Core、Occupancy → `04-gpu`
- **NPU / 昇腾(7 / 8、3 / 3)**:架构差异、算子开发难点、对 Transformer 的适配 → `04-gpu`
- **具体型号**:A100(3 / 3)、H100(2 / 2)、V100(2 / 2),以及 H 系列与 L 系列差异
- **边缘与嵌入式**:ARM(1 / 3)、RK3588、NEON → `04-gpu`、`01-cpp`

### 工具与工程

- **调试与性能**:Nsight(2 / 5)、NCU(1 / 1)、GDB(1 / 1)、条件断点与堆栈监视、Profiling(3 / 4)
- **开发工具**:Vim(0 / 1)、Git(1 / 3,含 merge/rebase、协作流程)、pytest(1 / 2)
- **平台**:Docker(3 / 5)、Kubernetes(2 / 3):namespace 隔离、容器通信、Pod 创建流程、request/limit → `05-ai-infra` 的「平台与中间件」

### 模型、算法与数据

- **注意力与结构**:Attention(30 / 75)、Transformer(20 / 32)、MHA / MQA / GQA(3+1 / 15)、MLA(5 / 8)、RoPE(1 / 3)、位置编码、FFN、归一化(LayerNorm / RMSNorm / BatchNorm)
- **推理优化**:KV Cache(16 / 30)、FlashAttention(7 / 24)、PagedAttention(1 / 13)、SSM / 稀疏化 → `04-gpu`、`05-ai-infra`
- **训练与对齐**:SFT(8 / 12)、RLHF(5 / 10)、PPO(8 / 23)、DPO(3 / 12)、GRPO(5 / 12)、Reward Model(2 / 2)、LoRA(4 / 10)、P-Tuning → `03-ai` 的「微调与对齐」
- **压缩与量化(61 / 103,单一最热主题)**:INT8 / FP8 / FP4、AWQ / GPTQ / SmoothQuant、蒸馏、剪枝 → `03-ai` 的「量化与压缩」
- **MoE**:路由机制、负载均衡、专家利用率、RL + MoE → `03-ai` 的「MoE」
- **RAG 与 Agent**:RAG(10 / 15)、Agent(20 / 23)、MCP、Prompt 工程、CoT、向量检索、记忆模块 → `05-ai-infra` 的「Agent 与工具调用」
- **机器学习基础**:KNN、GBDT、随机森林、特征筛选、Beam Search、TF-IDF、排序模型 → `03-ai` 的「机器学习」

## 二、按领域细分

面经里的领域信号分布很不均,下面按语料实际覆盖程度排序;带「待补」的表示本库没有或几乎没有相关面经。

### 大模型训练与推理(覆盖最全)

代表公司:字节跳动、阿里巴巴、腾讯、百度、美团、京东、快手、蚂蚁、小红书类岗位。

技术栈:PyTorch / DeepSpeed / Megatron → 并行策略(DP/TP/PP/EP/SP)→ 通信(NCCL / NVLink / RDMA)→ 推理框架(vLLM / SGLang / TensorRT-LLM)→ 优化(KV Cache / PagedAttention / FlashAttention / Chunked Prefill / PD 分离 / 量化)→ 对齐(SFT / RLHF / PPO / DPO / GRPO)。

### 视觉与多模态

代表公司:海康威视、格灵深瞳、商汤、旷视科技、小米。

技术栈:CNN 系(ResNet / MobileNet / GhostNet / SE)、检测与分割(YOLO / SSD / DETR / RT-DETR / NMS / IoU)、多模态(ViT / Swin / CLIP / BLIP / Q-Former)、生成(Diffusion / DiT / Flow Matching)、跟踪(ByteTrack / 卡尔曼滤波)、部署(ncnn / TensorRT / NPU)。

### 自动驾驶与车载

代表公司:辉羲智能、卓驭(大疆车载)、理想汽车、小鹏汽车、文远知行、元戎启行、经纬恒润、易控智驾。

技术栈:BEV 系(LSS → BEVFormer → Diffusion-based BEV)、感知/规划/控制算法、端侧部署(RK3588 / 车载 NPU / TensorRT)、时延-吞吐-功耗权衡、模型剪枝与量化、嵌入式性能瓶颈定位。

### 搜索、推荐与广告

代表公司:百度、阿里巴巴淘天、字节跳动抖音电商、美团。

技术栈:生成式推荐、SID、Tiger、排序模型与训练数据构造、正负样本处理、召回与排序瓶颈分析、RAG 在检索场景的结合、TF-IDF 与向量检索。

### 芯片、编译器与算子

代表公司:英伟达、沐曦、壁仞科技、寒武纪、摩尔线程、燧原科技、遂原科技、太初、飞腾、北极雄芯、后摩智能、原粒半导体、中科曙光。

技术栈:GPU / NPU / DCU 架构、CUDA 与 Triton 算子开发、GEMM / Conv / Reduce / Norm 等算子实现与调优、TVM / MLIR / XLA / LLVM 编译栈、图优化与算子融合、国产平台适配(CANN / MindIE / 达芬奇)。

### Agent 与 RAG 应用

代表公司:阿里巴巴(淘天、控股集团)、百度、字节跳动、MiniMax、阶跃星辰。

技术栈:Agent 架构与规划(Multi-step Planning)、工具调用与调度、记忆模块、链路追踪与可观测性、MCP、Prompt 工程与评估、RAG 全链路(切分 / 召回 / 生成 / 评估)、LLM as a Judge。

### 云原生与平台

代表公司:百度、腾讯、华为、中科曙光。

技术栈:Docker 与 namespace 隔离、Kubernetes(Pod / CSI / CNI / request-limit / Informer)、调度器设计、etcd / Redis / Kafka 等中间件、集群级高可用与容错。

### 机器人(待补)

语料未覆盖:**ROS 与「机器人」在 181 份面经里一次都没有出现**。这一节暂时留空,规划中的技术栈(ROS 1/2、MoveIt、仿真、SLAM、具身智能推理、Jetson / 边缘 NPU)需要靠岗位需求来补,见第三节。

### 其他

- 医疗影像:数坤科技有面经,但语料中没有出现「医疗」相关技术词,可归入视觉领域参考。
- 音视频、电商:仅作为部门背景出现(快手、字节抖音电商),没有独立技术栈信号。

## 三、岗位技术栈(需求占位)

> **需求占位**:目前只有面经推导出的技术栈,缺少岗位侧的输入。计划收集招聘 JD(岗位描述 / 任职要求),按「公司 × 方向」汇总真实要求,再与本附录对照,输出「岗位 → 技术栈 → 学习优先级」的映射,并补上面经语料没覆盖的领域(机器人、Rust、Shell 等)。

计划内的收集与产出:

- 数据来源:招聘官网 JD、内推 JD、面经里出现的岗位职责描述
- 字段:公司、部门、方向、学历/年限、语言、框架、平台、加分项
- 产出:各方向的技术栈频次表;与第一节的差异清单(语料没考但岗位要的);缺口优先级

已有的第一批输入:

- 快手 AI Infra 校招(岗位职责与任职要求):AI 编译器与异构推理引擎、并行计算优化与稀疏优化、LLVM Pass 开发、C++ 与体系结构、XLA/MLIR/TVM/Triton/TensorRT、CPU/GPU Kernel 开发、CUDA 编程 → 来源 `docs/interview/快手-AI-Infra-校招-3.md`

## 四、面试覆盖说明(非题目)

下面这些条目来自面经原文,但不是可作答的问题,记录在此以保持提取过程完整、便于回溯。

- 围绕候选人的项目经历进行深入提问 —— 出现在绝大多数面经中(项目深挖是标配环节)
- C++ 基础知识考察(面试范围说明)—— 小米、蔚来
- CUDA 编程基础知识考察(面试范围说明)—— 小米
- CUDA / TensorRT / TVM 相关问题(面试范围说明)—— 蔚来
- LeetCode 3 道 Medium + 1 道 Hard(面试范围说明)—— 蔚来
- 编程题考察(面试范围说明)—— 字节跳动
- C++ 编程题(原文未记录具体题目)—— 拼多多
- 现场出题(基础难度)—— 理想汽车
- 围绕相关论文进行深入讨论 —— 旷视科技
- 公司介绍与基本情况沟通 —— 辉羲智能
- 部门业务介绍(训练框架方向)—— 蔚来
- 部门工作方向介绍(训练加速、推理优化、模型前瞻性探索)—— 理想汽车
- 主要沟通实习工作内容与安排 —— 寒武纪

## 维护方式

- 频次与条目会随面经和题库更新而变化,更新时重跑 `scripts/build_worklist.py` 与关键词统计即可。
- 新增岗位 JD 时,补到第三节,并把「语料未覆盖」的技能从待补清单里划掉。
- 本文件不参与题库结构校验(校验只针对 `01`–`07` 分类文件)。
