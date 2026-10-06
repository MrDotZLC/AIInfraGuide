# AI Infra

## 分布式训练

- 训练或推理的 GPU 卡数成倍扩展时,系统最容易在哪些环节出现瓶颈?如何缓解?
  - 来源:`docs/interview/AI-Infra-一面.md`

- DeepSpeed ZeRO Stage 1 与 Stage 2 在通信量上有何差异?论文与代码实现有差距吗?
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`

- 多 GPU 通信场景下 NVSHMEM 与 NVLink 有什么区别?
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`

- Megatron-LM 中的通信优化是如何实现的?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- NCCL 包含哪些通信原语?执行一次 All-Reduce 参数更新需要几次通信?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- 小数据量下用 NVSHMEM 让每个 GPU 直接读其他 GPU 数据并本地 Reduce,相比 Ring All-Reduce 有何优势?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- 训练超长序列时应如何设计并行策略?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- All-Reduce 的通信开销如何计算?请给出推导。
  - 来源:`docs/interview/AI-Infra-综合面经题库-5.md`

- 多机多卡分布式训练的基本原理与常见框架是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- 如何从时间和资源两个维度提升训练效率?
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- 训练速度异常缓慢时,应从哪些方面分析排查?
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- 多机多卡训练的通信瓶颈及优化方法有哪些?
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- 梯度累加的工作原理是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- 除 ZeRO 之外,还有哪些大模型训练优化技术?
  - 来源:`docs/interview/MiniMax-AI-Infra-实习-二面.md`

- 序列并行的实现原理是什么?通信开销如何?还有哪些优化手段?
  - 来源:`docs/interview/阶跃星辰-AI-Infra-实习.md`

- 训练稳定性与容错方面有哪些常见技术方案?
  - 来源:`docs/interview/阶跃星辰-AI-Infra-实习.md`

- 在 16 张 GPU 上训练 200B 参数的模型,如何设计分布式训练方案?
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`

- PyTorch DDP 的原理与实现机制是什么?
  - 来源:`docs/interview/理想汽车-AI-Infra-校招-一面.md`

- DDP 在多机多卡场景下如何优化?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`

- 分布式训练中 batch size 的设置需要注意哪些问题?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`

- 预训练中的流水线并行如何设计?1F1B 调度与 DualPipe 的原理是什么?
  - 来源:`docs/interview/小厂-AI-Infra-实习-2.md`

- 通信时延的主要影响因素与缓解方法有哪些?
  - 来源:`docs/interview/数坤科技-AI-Infra-实习-一面.md`

- 分布式训练目前面临的主要性能瓶颈有哪些?
  - 来源:`docs/interview/海康威视-AI-Infra-一面.md`

- 模型训练优化与调优方法有哪些?
  - 来源:`docs/interview/荣耀-AI-Infra-一面.md`

- All-Reduce、All-Gather、All-To-All 分别完成什么数据交换?各适用于哪些并行策略?
  - 来源:`docs/interview/B站-AI-Infra-实习-一面.md`

- 常见的并行切分策略有哪些?3D 并行的组合方式与适用场景是什么?
  - 来源:`docs/interview/华为-AI-Infra-2.md`

- 流水线并行下每张卡的显存占用与计算量是否相同?激活值如何分布?
  - 来源:`docs/interview/华为-AI-Infra-2.md`

- DDP 与 DeepSpeed 中的异步保存机制分别如何实现?
  - 来源:`docs/interview/华为-AI-Infra-2.md`

- 异步保存(异步 checkpoint)方面需要做哪些工作?
  - 来源:`docs/interview/华为-AI-Infra-2.md`

- 给定 4 张卡对矩阵乘法 A×B 做分布式计算,如何分配 A、B 并利用卡间通信节省显存?
  - 来源:`docs/interview/华为-AI-Infra-实习-2.md`

- 常见集合通信原语有哪些?对通信算子有哪些了解?
  - 来源:`docs/interview/华为-AI-Infra-实习-2.md`

- 张量并行中先按列切分与先按行切分有什么区别?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-2.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-5.md`
  - 来源:`docs/interview/数坤科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/快手-AI-Infra-一面.md`

- Megatron 中序列并行(SP)是如何实现的?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`

- AllReduce 的实现原理与常见实现方式有哪些?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- Ring AllReduce 的通信量如何分析?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- Tree AllReduce 相比 Ring AllReduce 有何优势?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- Ray 的底层实现机制与关键特性是什么?
  - 来源:`docs/interview/快手-AI-Infra-一面.md`

- GPU 分布式通信原语有哪些?All-Gather、All-To-All 各适用于什么场景?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-3.md`

- DP 与 TP-SP 中计算与通信重叠的原理是什么?哪些通信与计算操作重叠?
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`

- 使用流水线并行与不使用 PP 时显存峰值是否相同?为什么?
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`

- Zero-Bubble 流水线调度的原理是什么?
  - 来源:`docs/interview/美团-AI-Infra-实习.md`

- DeepEP 的设计思想与核心机制是什么?
  - 来源:`docs/interview/美团-AI-Infra-实习.md`

- 数据并行、张量并行和流水线并行的设计思想与适用条件分别是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/数坤科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/理想汽车-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/太初-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/MiniMax-AI-Infra-实习-二面.md`

- DeepSpeed 的核心功能有哪些?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一面-4.md`
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- DeepSpeed ZeRO 的 Stage-1/2/3 各切分了哪些状态?通信量与显存节省的递进关系是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一面-4.md`
  - 来源:`docs/interview/华为-AI-Infra-2.md`
  - 来源:`docs/interview/MiniMax-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/华为-AI-Infra-实习-2.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-3.md`

- 除 DeepSpeed 外还使用过哪些分布式训练加速框架?它们有何区别?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一面-4.md`

- 训练中优化器状态、梯度、模型参数各自的显存占比是多少?
  - 来源:`docs/interview/百度-AI-Infra-一面-3.md`

- FSDP 与 DeepSpeed ZeRO Stage 1/2/3 的对比
  - 来源:`docs/interview/百度-AI-Infra-一面-3.md`

- DualPipe 的工作原理与设计动机是什么?
  - 来源:`docs/interview/百度-AI-Infra-实习-1.md`

- 节点内有 NVLink、节点间部分有 RDMA 时,如何设计分布式推理方案?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一面-1.md`

- reduce-scatter 与 all-to-all 两种集合通信操作的比较
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一面-1.md`

- 千卡规模出现 NCCL Timeout 时如何定位与解决?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-1.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-4.md`

- MoE 模型与多模态模型的训练过程目前还有哪些可优化方向?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-1.md`

- 大模型预训练与强化学习训练在工程实践层面还有哪些可优化的环节?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-1.md`

- 多卡协同场景下卡间通信有哪些方式?NVLink 与 RDMA 各有什么特点?
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-实习-二面-1.md`

- 如何对互联拓扑进行建模?
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-实习.md`

- 项目中 Dense 模型与 MoE 模型在推理实现上有哪些差异?Expert Parallelism(EP)如何实现?
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-一面.md`
  - 来源:`docs/interview/理想汽车-AI-Infra-一面.md`

- Tensor Parallelism 中 AllReduce 需要执行多少次?如何推导?
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-一面.md`

## 推理与部署

- Mooncake 以 KV-Cache 为中心的 PD 分离方案是怎么设计的?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- DiT 推理框架与 LLM 推理框架的设计有哪些异同?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- Prefill 阶段与 Decode 阶段各有哪些主流优化技术?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- Two-batch overlap 是什么?哪些场景下它反而成为负优化?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- 多机 PD 分离会引入 KV Cache 传输开销,为何仍有必要?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- 如何看待跨 SM 的 PD 分离与 AF 分离方案?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- LLaMA 的模型文件(.bin)需要做哪些预处理?
  - 来源:`docs/interview/旷视科技-AI-Infra-校招.md`

- 模型应该拆分为多个 .bin 文件还是单个文件?
  - 来源:`docs/interview/旷视科技-AI-Infra-校招.md`

- 推理/训练框架的内存管理方案应该如何设计?
  - 来源:`docs/interview/旷视科技-AI-Infra-校招.md`

- 显存池通常采用什么数据结构?
  - 来源:`docs/interview/旷视科技-AI-Infra-校招.md`

- 在 GPU 上做大模型训练与推理的性能优化,通常从哪些方面入手?
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- 线上服务推理场景下如何提升吞吐量?
  - 来源:`docs/interview/太初-AI-Infra-实习-一面-1.md`

- Attention 模块在整个系统端到端延迟中占多大比例?
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`

- Decode 阶段是 compute bound 还是 memory bound?KV-Cache 量化提升的是哪方面性能?
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`

- 大模型推理分为哪几个阶段?各阶段的特点是什么?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- 算子与 tensor 之间是什么关系?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- 模型和算子确定后,影响推理速度的因素有哪些?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- prompt 长度与上下文长度如何影响推理速度?decode 阶段呢?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- 如何把权重文件导入到自行搭建的模型中?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- prefill 阶段有哪些加速 KV Cache 生成的方法?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- prefill 阶段各 token 之间是否存在依赖关系?能否并行处理?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- 稀疏化 KV Cache 是否需要修改训练流程,还是纯工程优化?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- KV Cache、算子融合、量化等模型级优化手段的原理分别是什么?
  - 来源:`docs/interview/卓驭-AI-Infra-校招-一面.md`

- TensorRT 与 OpenVINO 的异同是什么?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- TensorRT 模型转换过程中会遇到哪些问题?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- vLLM 与 SGLang 有哪些差别?SGLang 的优势体现在哪里?
  - 来源:`docs/interview/Teleai-AI-Infra-实习-一面.md`

- 昇腾平台的 CANN 与 MindIE 分别包含哪些核心组件?
  - 来源:`docs/interview/Teleai-AI-Infra-实习-一面.md`

- V100 显存有多大?32B 模型 INT8 量化后能否在 V100 上运行?部署方案如何设计?
  - 来源:`docs/interview/Teleai-AI-Infra-实习-一面.md`

- 吞吐量的定义是什么?推理场景中如何衡量?
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- 常见推理框架的对比与选型依据是什么?
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/经纬恒润-AI-Infra-二面.md`

- FasterTransformer 框架的核心特性有哪些?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`
  - 来源:`docs/interview/太初-AI-Infra-实习-一面-1.md`

- 常见 AI 推理与训练框架有哪些?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`

- 投机采样中草稿模型与主模型如何交互?vLLM 与 SGLang 的实现有何差异?
  - 来源:`docs/interview/小厂-AI-Infra-实习-1.md`

- SGLang 多模态场景开启 TP 时,ViT 的 image embedding 如何在进程间高效复用?
  - 来源:`docs/interview/小厂-AI-Infra-实习-1.md`

- TensorRT 的优势与不足是什么?缺少算子时如何用 Plugin 自定义?
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`
  - 来源:`docs/interview/理想汽车-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- 为什么选用 RK3588 芯片?环境搭建与模型部署的完整流程是什么?
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`

- 端侧大模型部署面临哪些挑战?有哪些常用优化手段?
  - 来源:`docs/interview/智源研究院-AI-Infra-一面.md`
  - 来源:`docs/interview/海康威视-AI-Infra.md`

- 面对一个全新模型和指定硬件平台,性能优化的整体分析与优化思路是什么?
  - 来源:`docs/interview/格灵深瞳-AI-Infra-一面.md`

- 你对模型推理优化有哪些整体认识?
  - 来源:`docs/interview/海康威视-AI-Infra-一面.md`

- 模型导出时如何处理动态维度问题?
  - 来源:`docs/interview/海康威视-AI-Infra.md`

- 针对大模型进行性能和效率优化的具体方法有哪些?
  - 来源:`docs/interview/米哈游-AI-Infra-实习-二面.md`

- LLM 在 NPU 上推理的主要性能瓶颈是什么?
  - 来源:`docs/interview/荣耀-AI-Infra-校招-二面.md`

- Prefill 与 Decoding 阶段各自的 Matmul 优化策略是什么?
  - 来源:`docs/interview/荣耀-AI-Infra-校招-二面.md`

- 如何估算 Qwen3-8B 模型推理所需的显存?
  - 来源:`docs/interview/京东-AI-Infra-实习.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-1.md`

- PD 分离机制的原理是什么?如何设计两个队列的调度策略?
  - 来源:`docs/interview/京东-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/小米-AI-Infra-校招.md`
  - 来源:`docs/interview/快手-AI-Infra-一面.md`
  - 来源:`docs/interview/美团-北斗-AI-Infra-校招.md`

- Fastllm.cpp 的核心技术细节有哪些?
  - 来源:`docs/interview/小米-AI-Infra-校招-一面.md`

- KV Cache 有哪些加载方式?
  - 来源:`docs/interview/小米-AI-Infra-校招.md`

- 使用 vLLM 部署过模型吗?实测吞吐量是多少?
  - 来源:`docs/interview/小米-AI-Infra-校招.md`

- TensorRT 的底层加速原理是什么?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-1.md`

- 模型训练与推理在资源消耗上有哪些区别?训练中有哪些性能优化手段?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-1.md`

- Memory Pool 的设计与构建思路是什么?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-2.md`

- 如何分析推理链路的性能瓶颈?最有效的优化手段是什么?
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-2.md`

- KV Cache 的离线预计算方案是什么?低频使用的 KV Cache 如何卸载与加载?
  - 来源:`docs/interview/蚂蚁-AI-Infra-校招-一面.md`

- 还有哪些 KV Cache 优化的技巧?
  - 来源:`docs/interview/蚂蚁-AI-Infra-校招-一面.md`

- 进一步提升大模型推理性能有哪些技术手段?
  - 来源:`docs/interview/字节跳动-AI-Infra-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-2.md`
  - 来源:`docs/interview/京东-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`
  - 来源:`docs/interview/小鹏汽车-AI-Infra.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-校招-1.md`
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-1.md`
  - 来源:`docs/interview/字节跳动-AML-AI-Infra-一二面.md`
  - 来源:`docs/interview/字节跳动-豆包-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/百度-AI-Infra-一面-2.md`

- 大模型推理中的系统资源调度与并发处理需要关注哪些要点?
  - 来源:`docs/interview/字节跳动-AI-Infra-2.md`

- 模型训练和推理中显存占用过高时有哪些应对方案?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- 常见的模型量化方法与推理加速方案有哪些?
  - 来源:`docs/interview/字节跳动-AI-Infra-校招-1.md`
  - 来源:`docs/interview/小米-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/海康威视-AI-Infra.md`
  - 来源:`docs/interview/理想汽车-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/快手-AI-Infra-实习.md`
  - 来源:`docs/interview/快手-AI-Infra-校招-1.md`
  - 来源:`docs/interview/美团-北斗-AI-Infra-校招.md`

- Prefix Cache 的机制是什么?适用于哪些场景?
  - 来源:`docs/interview/字节跳动-AI-Infra-校招-1.md`

- 大模型推理的主要性能瓶颈有哪些?
  - 来源:`docs/interview/字节跳动-AML-AI-Infra-一二面.md`

- Orca 迭代级请求调度的设计思路是什么?
  - 来源:`docs/interview/字节跳动-AML-AI-Infra-一二面.md`

- 大模型 prefill 阶段与 decoding 阶段的区别及其成因是什么?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`

- Chunked Prefill 的核心思想与应用场景是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/京东-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-2.md`

- TensorRT-LLM、vLLM 的源码实现有哪些差异?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`

- Continuous Batching 的概念及其作用是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-2.md`

- fastllm.cpp 的源码结构与实现思路是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`

- Paged Attention 的设计思路与工作机制是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-2.md`
  - 来源:`docs/interview/京东-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/美团-AI-Infra-一面.md`
  - 来源:`docs/interview/小米-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/拼多多-AI-Infra.md`
  - 来源:`docs/interview/美团-北斗-AI-Infra-校招.md`
  - 来源:`docs/interview/字节跳动-AML-AI-Infra-一二面.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`

- 推理服务上线前需要做哪些性能优化?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-1.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-4.md`

- KV Cache 的工作原理是什么?有哪些优化方法?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-一面-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-2.md`
  - 来源:`docs/interview/华为-AI-Infra-实习-2.md`
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/联想-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`
  - 来源:`docs/interview/数坤科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-3.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-三面.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-校招-1.md`

- 大模型在训练和推理过程中显存不足时有哪些优化方案?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-一面-2.md`

- vLLM 推理框架的核心机制与特点是什么?
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-二面.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-1.md`
  - 来源:`docs/interview/小米-AI-Infra-校招.md`
  - 来源:`docs/interview/Teleai-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/旷视科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-1.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-2.md`
  - 来源:`docs/interview/虾皮-AI-Infra-实习-2.md`
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-实习-二面-2.md`
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-一面.md`

- 你认为当前 LLM 推理的主要瓶颈在哪里?
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-实习.md`

## 训练框架

- torch.repeat 与 torch.expand 在功能和内存行为上有何差异?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- torchrun 的启动参数有哪些?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- tensor.view 与 tensor.contiguous 的区别与联系是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-5.md`

- 混合精度训练的原理与实现方式是什么?训练与推理各有哪些关键问题?
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`

- PyTorch 的基础知识包括哪些?
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`

- PyTorch 的底层原理是什么?
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`

- MindSpore 框架的主要特点是什么?
  - 来源:`docs/interview/上海AI实验室-AI-Infra-实习-二面.md`

- MindSpore 前端与后端的架构设计是怎样的?
  - 来源:`docs/interview/上海AI实验室-AI-Infra-实习-二面.md`

- PyTorch 2.0 引入了哪些关键新特性?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`

- AI 框架前端中算子注册的机制是什么?为什么加宏定义就能完成注册?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-2.md`

- AI 框架开发通常涉及哪些核心模块?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- DeepSpeed、DDP 与 FlashAttention 的核心功能与原理分别是什么?
  - 来源:`docs/interview/京东-AI-Infra-实习.md`

- PyTorch 的核心基础功能有哪些?如何进行 GPU 资源管理?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-1.md`

## 性能估算

- 已知训练所需 Token 总量,如何估算训练总耗时?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- 训练 70B 量级的模型时,如何粗略估算单张 GPU 所需的显存?
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/MiniMax-AI-Infra-实习-二面.md`

- 如何计算使用 FP8 存储时的 KV Cache 大小?
  - 来源:`docs/interview/科大讯飞-飞星-AI-Infra-校招.md`

- 量化后的大模型(如 INT8/INT4)运行时内存占用约为多少?
  - 来源:`docs/interview/荣耀-AI-Infra-校招-二面.md`

- 部署模型与推理模型所需的参数量分别如何估算?
  - 来源:`docs/interview/华为-AI-Infra-实习-2.md`

- KV Cache 的大小如何计算(涉及 batch size、序列长度、head 数、head dim、层数、数据类型)?
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-三面.md`

- 如何计算 KV Cache 的显存占用大小?
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-一面.md`

## 编译与图优化

- 实现 Graph Fusion 算法
  - 来源:`docs/interview/AI-Infra-综合面经题库-5.md`

- 实现计算图
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 编译器 IR(中间表示)的转换流程是怎样的?
  - 来源:`docs/interview/三星-AI-Infra-一面-3.md`

- AI 编译器(如 TVM、XLA)的工作原理是什么?
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`

- MLIR 的表示方式与优化流程是怎样的?
  - 来源:`docs/interview/燧原科技-AI-Infra-社招-一面.md`

- XLA 在动态性方面有哪些不足?有哪些应对方案(如手写算子)?
  - 来源:`docs/interview/燧原科技-AI-Infra-社招-一面.md`

- TVM 自动代码生成的现状与局限性是什么?NPU 上手写算子与自动生成的性能差异如何?
  - 来源:`docs/interview/燧原科技-AI-Infra-社招-一面.md`

- 是否定义过自定义的 MLIR Dialect?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- 参考 torch-mlir 的设计时需要解决哪些问题?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- 编译器中如何处理动态图?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- 转换为 TOSA 和 Tensor Dialect 之后还需要 Lower 到哪些 Dialect?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- One-shot Bufferization 与基于 Dialect 的 Bufferization 有什么区别?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- LLVM 中 isa 与 dyn_cast 的用法与实现原理是什么?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- 给定一个计算图,如何计算运行它所需的最小内存?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- MLIR 中如何处理 In-place 操作?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- MLIR 框架的设计目标是什么?为什么需要 MLIR?
  - 来源:`docs/interview/小马智行-AI-Infra-实习.md`

- PyTorch 的图优化机制是如何工作的?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`

- 计算图通常使用什么方式构建?
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- HalideIR 的核心概念与 Schedule 原语的运作机制是什么?
  - 来源:`docs/interview/vivo-AI-Infra-校招.md`

- 除 TVM 外还有哪些主流深度学习编译框架(XLA、TensorRT 等)?它们有何异同?
  - 来源:`docs/interview/vivo-AI-Infra-校招.md`

- TVM 中图级别优化与算子级别优化分别如何实现?目标硬件平台提供哪些支持?
  - 来源:`docs/interview/vivo-AI-Infra-校招.md`

- 自动调优(Tuning)方案的设计思路是什么?与手动优化相比各有何优劣?
  - 来源:`docs/interview/vivo-AI-Infra-校招.md`

- 静态图与动态图的区别是什么?
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- 多面体模型(Polyhedral Model)的基本原理是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- TVM 编译框架的基本概念有哪些?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`
  - 来源:`docs/interview/上海AI实验室-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- Halide 编程语言的设计理念是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- 图优化与算子调度方法有哪些?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- MLIR 与 TVM 各自的设计理念及主要差异是什么?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-2.md`

- TVM 中 Relay 与 TIR 的调度原语分别承担什么角色?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-2.md`

## 系统设计

- 大模型训练与推理的主流加速方案有哪些?
  - 来源:`docs/interview/AI-Infra-综合面经题库-7.md`

- 一个 Agent 流程要依次调用 3 个外部工具,高并发下端到端延迟偏高,有哪些工程手段可以降低延迟?
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- 项目中的高并发设计是为了解决什么问题?如何实现?
  - 来源:`docs/interview/三星-AI-Infra-一面-1.md`

- 自动驾驶领域的高性能计算需求与实现方式是什么?时延、吞吐与功耗如何权衡?
  - 来源:`docs/interview/卓驭-AI-Infra-校招-二面.md`
  - 来源:`docs/interview/易控智驾-AI-Infra-二面.md`

- 自动驾驶领域的技术栈包括哪些?
  - 来源:`docs/interview/小鹏汽车-AI-Infra-实习.md`

- 调度器的设计思路与关键考量有哪些?
  - 来源:`docs/interview/易控智驾-AI-Infra-二面.md`

- 如果接手推理优化工作,你会如何展开?
  - 来源:`docs/interview/理想汽车-云-AI-Infra-实习-一面.md`

- 高并发下如何对推理服务做压力测试以确定最大并发量?需要监控哪些指标?
  - 来源:`docs/interview/Teleai-AI-Infra-实习-一面.md`

- AI 推理框架中常用的通信协议有哪些?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 如何设计一个分布式推理框架?整体架构与关键模块是什么?
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`

- 推理框架中计算图、运行图和内存管理各承担什么职责?如何设计整体架构?
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`

- 缓存的核心功能是什么?典型应用场景有哪些?
  - 来源:`docs/interview/海康威视-AI-Infra-实习-一面.md`

- 三层缓存架构中各层的使用场景与容量量级是什么?如何合理使用?
  - 来源:`docs/interview/海康威视-AI-Infra-实习-一面.md`

- 大模型训练与推理所需的大规模计算资源有哪些可行解决方案?
  - 来源:`docs/interview/米哈游-AI-Infra-实习-二面.md`

- 如何系统性评估一个 RAG 系统的表现?有哪些常用指标或测评框架?
  - 来源:`docs/interview/虾皮-AI-Infra-实习-2.md`
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- 如何保障系统的高性能运行?
  - 来源:`docs/interview/识渊科技-AI-Infra-实习-一面.md`

- RAG 是什么?它如何改善生成质量?标准 RAG 方案有哪些不足?
  - 来源:`docs/interview/贝壳-AI-Infra.md`
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- 作为技术负责人优化云端 CV 模型推理服务,如何在提升单卡吞吐的同时降低响应延迟?
  - 来源:`docs/interview/OPPO-云-AI-Infra-实习-一面.md`

- 后端的整体架构设计与关键实现细节是什么?
  - 来源:`docs/interview/vivo-AI-Infra-校招.md`

- RAG(检索增强生成)的完整流程是什么?有哪些可行的优化策略?
  - 来源:`docs/interview/京东-AI-Infra-实习.md`

- 多设备或多任务场景下如何解决负载均衡问题?
  - 来源:`docs/interview/快手-AI-Infra-校招-1.md`

- 设计高吞吐、低延迟的模型推理服务时,架构与工程层面要考虑哪些问题?
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- 如何设计方案识别平台上的刷赞行为?
  - 来源:`docs/interview/字节跳动-抖音-AI-Infra.md`

- 知识库数据的清洗与构造流程是怎样的?数据质量不一致会有什么影响?
  - 来源:`docs/interview/百度-AI-Infra-二面-2.md`

- 文档切分策略如何设计?Chunk Size 与 Overlap 如何影响召回与生成?
  - 来源:`docs/interview/百度-AI-Infra-二面-2.md`

- 用户问题在知识库中确实存在但未被召回正确文档,应如何排查?
  - 来源:`docs/interview/百度-AI-Infra-二面-2.md`

- 检索到了正确文档但生成答案仍有误,应如何定位问题?
  - 来源:`docs/interview/百度-AI-Infra-二面-2.md`

- 召回结果经常语义相似但事实无关,应如何优化检索模块?
  - 来源:`docs/interview/百度-AI-Infra-二面-2.md`

- 一个问题需要跨多个文档才能回答时,RAG 系统应如何处理?
  - 来源:`docs/interview/百度-AI-Infra-二面-2.md`

- 如何判断 RAG 的问题出在检索模块还是生成模块?
  - 来源:`docs/interview/百度-AI-Infra-二面-2.md`

- 搜索准确性不高时应如何进行问题排查?
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-3.md`

- 召回阶段与排序阶段哪个更容易成为瓶颈?
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-3.md`

- 生成式搜索能否保证 top-1 结果的准确性?如何提升?
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-3.md`

- 项目中做过哪些相关性优化?有量化评估结果吗?
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-3.md`

- Agent 服务的高可用与鲁棒性如何保障?
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-3.md`

- UI 优化中合批处理的实现方式是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习.md`

- RAG 系统中检索模块的实现方案有哪些?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-一面-1.md`

- 多模态 RAG 的基本思路与实现方案是什么?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-一面-2.md`

- Skills 读取超长 SOP 的场景有哪些常见优化技巧?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-2.md`

## Agent 与工具调用

- 把 RAG 封装成 Agent 形态能带来哪些好处?
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- Prompt 自动推荐功能如何优化?可以用 Prompt 压缩或基于 Embedding 的表征来提升效率吗?
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- 工具调用的调度机制如何设计?系统是否支持异常情况下的 Fallback 降级?
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- Agent 的多步规划(Multi-step Planning)如何实现?
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- Agent 的评估体系涵盖哪些方面?规划质量和幻觉频率如何度量?
  - 来源:`docs/interview/MiniMax-AI-Infra-一面.md`

- 构建一个 AI Agent 应用需要包含哪些核心模块?
  - 来源:`docs/interview/字节跳动-AI-Infra-校招-1.md`

- 阐述你设计的 Agent 系统的整体架构
  - 来源:`docs/interview/阿里巴巴-AI-Infra-一面-1.md`

- 开发一个 MCP 后如何评测其实际效果?后续如何迭代优化?
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-实习-一面.md`

- Agent 系统如何实现链路追踪与可观测性?
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-实习-一面.md`

- Agent 的对话记录采用什么方式保存?使用了怎样的数据结构?
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-实习-一面.md`

- 目前主流的 Agent 开发框架有哪些?各自特点是什么?
  - 来源:`docs/interview/阿里巴巴-控股集团-AI-Infra-实习-一面.md`

- Agent 的记忆模块应如何设计?有哪些常见的记忆管理策略?
  - 来源:`docs/interview/阿里巴巴-淘天-AI-Infra-一面-1.md`

- Workflow、Agent、Skill 三者的区别与定位是什么?
  - 来源:`docs/interview/阿里巴巴-淘天-AI-Infra-一面-1.md`

- 编写 Prompt 时需要考虑哪些关键因素?如何评估 Prompt 质量?
  - 来源:`docs/interview/阿里巴巴-淘天-AI-Infra-一面-1.md`

- Agent 系统中各个 Agent 分别负责什么任务?输入输出是什么?
  - 来源:`docs/interview/阿里巴巴-淘天-AI-Infra-一面-1.md`

## 平台与中间件

- Kubernetes 的基本架构是什么?Pod、Container 等核心概念有哪些?
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`

- Docker 的 namespace 隔离机制是如何工作的?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- Docker 容器间通信的方式有哪些?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 如何理解最左前缀匹配原则?
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- 对表 a、b、c 建联合索引,查询条件为 a > 1 AND c = 1 时索引使用情况如何?
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- 线上出现慢查询时如何定位和排查?
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- 从应用层面介绍 MySQL 的核心知识点。
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- 如何判断一条 SQL 是否走了索引?EXPLAIN 输出中通常关注哪些字段?
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- 描述你实际使用过的一张数据库表的字段设计与索引情况。
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- SELECT、FROM、WHERE、GROUP BY、HAVING 的执行顺序是怎样的?
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- Kubernetes Informer 的工作原理是什么?
  - 来源:`docs/interview/百度-AI-Infra-二面-3.md`

- Docker 的底层实现原理是什么?
  - 来源:`docs/interview/百度-AI-Infra-二面-3.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 容器如何实现 PID 隔离?如何关闭该隔离?
  - 来源:`docs/interview/百度-AI-Infra-二面-3.md`

- etcd 与 Redis 在索引实现上有何区别?为什么采用不同的设计?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

- Kafka 如何实现顺序消费?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

- Kafka 如何保证消息不丢失?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

- Kafka 在顺序消费场景下的写文件机制是怎样的?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

- K8s 中 Pod 的创建流程是什么?CSI 与 CNI 分别在哪个阶段被调用?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

- K8s 中 request 与 limit 的底层实现原理是什么?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

## 工具与工程

- PyTorch 中有哪些常用的性能分析工具和方法?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`

- pytest 的常用命令与功能有哪些?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`
  - 来源:`docs/interview/原粒半导体-AI-Infra-一面.md`

- 跨平台环境下系统级算子的测试策略应如何设计?
  - 来源:`docs/interview/中科曙光-AI-Infra-二面-2.md`

- Git 中拉取远程分支有哪些方式?fetch+checkout 与 pull 有什么区别?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`

- 测试架构如何设计?单元测试主要覆盖哪些内容?
  - 来源:`docs/interview/海康威视-AI-Infra-实习-一面.md`

- ncnn 的交叉编译流程是怎样的?
  - 来源:`docs/interview/海康威视-AI-Infra.md`

- 你对 ncnn 源码的了解程度如何?
  - 来源:`docs/interview/海康威视-AI-Infra.md`

- 框架测试方案如何设计?测试数据规模有多大?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-2.md`

- git merge 与 git rebase 的区别是什么?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

- 如何撤回已提交的 commit?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

## RL 训练系统

- RL 训练中 Rollout 阶段耗时占比多少?MFU 如何计算?6Nd 公式的含义是什么?
  - 来源:`docs/interview/小厂-AI-Infra-实习-2.md`

- RL 中 Rollout 阶段有哪些常见优化手段(如 Rollout 量化、异步 Rollout)?
  - 来源:`docs/interview/小厂-AI-Infra-实习-2.md`

- RL 训练流程中如何把预训练权重同步到推理引擎?
  - 来源:`docs/interview/小厂-AI-Infra-实习-2.md`

- 强化学习中有哪些异步调度方案?各自优缺点是什么?
  - 来源:`docs/interview/美团-AI-Infra-实习.md`

- RL 异步调度在算法层面需要做哪些适配与改进?
  - 来源:`docs/interview/美团-AI-Infra-实习.md`

- 异步强化学习训练场景下如何修正损失函数?
  - 来源:`docs/interview/百度-AI-Infra-实习-1.md`

## 数据库

- 聚合函数与 GROUP BY 的底层实现方式是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- JOIN 操作的实现方法及优化策略(索引优化、哈希表优化)有哪些?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 哈希 JOIN 中一侧表远大于另一侧时如何优化?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 数据库优化器的作用及实现原理是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- EXPLAIN 语句的执行机制是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- Buffer Pool 的设计与实现思路是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 脏页的管理策略及数据丢失问题如何解决(redo log)?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- LRU 算法的缺陷(预读失效、缓存污染)及改进方案有哪些?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 并发 B+ 树的实现机制是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 火山模型与其他执行模型(物化模型)如何比较?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 行存储与列存储分别适用于哪些场景?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 事务与 MVCC 的基本概念是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 从单机数据库扩展为分布式数据库的设计思路是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 哈希分片与范围分片有什么区别?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 元数据节点的高可用方案有哪些?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- MySQL 主从复制中如何保证强一致性?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- SELECT * FROM table 的执行计划是怎样的?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 分布式场景下需要增加哪些算子来实现跨节点查询?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 带 WHERE 条件和 GROUP BY COUNT 的分布式执行计划如何设计?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 查询过程中最影响性能的关键环节是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 火山模型与 Pipeline 模型是什么关系?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`
