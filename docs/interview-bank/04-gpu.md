# GPU / CUDA / Kernel

## GPU 体系结构与调度

- GPU 多线程与 CPU 多线程在调度机制上有何本质差异?
  - 来源:`docs/interview/美团-AI-Infra-一面.md`

- SM(Streaming Multiprocessor)与 SP(Streaming Processor)是什么关系?
  - 来源:`docs/interview/AI-Infra-校招-1.md`

- Hopper 架构 TMA 的优势是什么?如何调用?数据传输是否需要经过 L1 缓存?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- 把 Ampere 架构上的算子迁移适配到 Hopper,需要升级改造哪些方面?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- Hopper 的 Warp Specialization 机制及其底层实现原理是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-4.md`

- sin 函数在 GPU 的哪个硬件单元上执行?该单元还支持哪些运算?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- Volta 架构有哪些特性?ITS(Independent Thread Scheduling)是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- PTX 与 SASS 有什么区别?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- SIMT(Single Instruction, Multiple Threads)的含义与工作原理是什么?
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- Occupancy 受哪些因素影响?如何调控?
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- 一个 Block 是否可能被调度到不同的 SM 上执行?
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- NVIDIA GPU 中指令级并行(ILP)是如何实现的?
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- A100 的理论显存带宽上限是多少?
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`

- GPU 计算架构与芯片架构包含哪些关键内容?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`

- 昇腾 NPU 与 NVIDIA GPU 在架构设计上有哪些差异?内存层级如何设计?
  - 来源:`docs/interview/卓驭-AI-Infra-校招-一面.md`

- NVIDIA GPU PTX 机器模型的核心概念有哪些?
  - 来源:`docs/interview/小马智行-AI-Infra-实习.md`

- CUDA 代码的完整编译流程是怎样的?
  - 来源:`docs/interview/小马智行-AI-Infra-实习.md`

- CPU、GPU 与 NPU 在优化策略上有哪些差异?各自适用什么场景?
  - 来源:`docs/interview/小鹏汽车-AI-Infra-实习.md`

- NPU 的计算执行流程是怎样的?
  - 来源:`docs/interview/易控智驾-AI-Infra-二面.md`

- blockDim.x 与 gridDim.x 的最大值分别是多少?
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`

- 华为达芬奇架构的设计特点有哪些?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 影响 GPU 计算性能的硬件因素有哪些?
  - 来源:`docs/interview/小厂-AI-Infra-实习-一面.md`

- 国产计算平台与国外主流平台的主要差异体现在哪些方面?
  - 来源:`docs/interview/海康威视-AI-Infra-一面.md`

- NPU 开发中有哪些主要难点?应对策略是什么?
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招-一面.md`

- NVIDIA GPU 对 FP8 数据类型有哪些专门的硬件优化?
  - 来源:`docs/interview/科大讯飞-飞星-AI-Infra-校招.md`

- H 系列与 L 系列 GPU 在架构设计上有哪些不同?
  - 来源:`docs/interview/科大讯飞-飞星-AI-Infra-校招.md`

- 昇腾 NPU 架构对 Transformer 类模型的适配性如何?
  - 来源:`docs/interview/荣耀-AI-Infra-校招-二面.md`

- Warp 与 Block 的划分方式和 SIMT 执行模型之间有什么内在联系?
  - 来源:`docs/interview/OPPO-云-AI-Infra-实习-一面.md`

- DCU 与华为 AI 加速卡在架构、生态与通信库方面有哪些差异?
  - 来源:`docs/interview/华为-AI-Infra-2.md`

- CUDA 中 Block 是软件概念还是硬件概念?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- GPU 与 CUDA 的基本概念是什么?GPU 最基础的物理执行单元是什么?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-1.md`

- H100 相比 A100 在架构层面有哪些关键改进?
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`

- CUDA 中 Warp 的概念及其在执行模型中的作用是什么?
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`

- Hopper 架构中 warp specialization 的机制与底层实现是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一面-1.md`

- GPU 的内存层次结构是怎样的?各级存储的作用域是什么?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-二面-1.md`

- CPU 与 GPU 各自的架构特点与设计差异是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/美团-AI-Infra-一面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/AI-Infra-校招-1.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-一二面.md`

- shuffle、Hyper-Q、SM、slot 分别是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- GPU 架构包含哪些关键组成部分,各自承担什么职责?
  - 来源:`docs/interview/腾讯-AI-Infra.md`
  - 来源:`docs/interview/太初-AI-Infra-一面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- Hopper 架构下 Warp Specialization 的机制原理与底层实现是什么?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-1.md`

- 不同 GPU 生态之间存在哪些主要差异?
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-实习-二面-1.md`

## 性能分析与建模

- 如何用 Roofline 模型判断一个算子是否已达到计算瓶颈?
  - 来源:`docs/interview/AI-Infra-一面.md`

- 性能调优时如何定位瓶颈?常用哪些方法与工具?
  - 来源:`docs/interview/AI-Infra-一面.md`

- GPU 标称的 TFLOPS 性能指标是如何计算的?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- 计算密集型与访存密集型有什么区别?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 常用的性能优化思路有哪些?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 可分离卷积在 GPU 上为何性能不佳?为什么属于访存密集型?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- Little's Law 中访存延迟与计算延迟是什么关系?
  - 来源:`docs/interview/寒武纪-AI-Infra-实习.md`

- 对标官方 baseline 时如何选择实现与数据类型?
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`

- 性能提升数据从哪里来?动态分块策略与算子配置如何影响结果?
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`

- 算子优化的完整流程是什么?如何判断算子属于 memory-bound 还是 compute-bound?
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`
  - 来源:`docs/interview/卓驭-AI-Infra-校招-一面.md`

- 算术强度分析与矩阵乘法的性能瓶颈如何分析?
  - 来源:`docs/interview/小鹏汽车-AI-Infra.md`

- 如何用 profiling 判断 GPU 算子的瓶颈在访存还是计算?确认瓶颈后有哪些针对性调优手段?
  - 来源:`docs/interview/B站-AI-Infra-实习-一面.md`

- 数据类型精度转换时如何保证数值计算的稳定性?
  - 来源:`docs/interview/OPPO-云-AI-Infra-实习-一面.md`

- 如何判断性能优化是否已接近瓶颈?有哪些衡量指标?
  - 来源:`docs/interview/快手-AI-Infra-校招-1.md`

- 如何判断一个算子是否需要优化?分析路径是什么?
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-1.md`

- SOL(Speed of Light)指标的含义是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- 如何分析系统性能瓶颈?
  - 来源:`docs/interview/腾讯-AI-Infra.md`

- 什么是访存密集型算子?请举例说明
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-一二面.md`

- 算子优化的效果如何传导到整网?如何与多卡互联、Profiling、软硬件协同衔接?
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-实习-二面-1.md`

## GEMM 与 Tensor Core

- GEMM 是否一定属于计算瓶颈型算子?如何优化?
  - 来源:`docs/interview/AI-Infra-一面.md`

- 单个 tile 内需要执行多少次计算?
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- 与 CUTLASS 相比,自实现 GEMM 版本的性能对比如何?
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- 低比特 GEMM 的开发要点有哪些?
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- GEMM kernel 中为什么常让单个线程计算 8x8 个输出元素?
  - 来源:`docs/interview/寒武纪-AI-Infra-实习.md`
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- GEMM 的分块(Tiling)大小受哪些因素制约?如何选取?
  - 来源:`docs/interview/快手-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习.md`
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- 详细描述 GEMM 优化的实现过程
  - 来源:`docs/interview/百度-AI-Infra-一面-2.md`
  - 来源:`docs/interview/快手-AI-Infra-一面.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-2.md`
  - 来源:`docs/interview/壁仞科技-AI-Infra-实习.md`
  - 来源:`docs/interview/太初-AI-Infra-一面.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习.md`
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`
  - 来源:`docs/interview/快手-AI-Infra-实习.md`

- Tensor Core 与 CUDA Core 在矩阵乘法加速上哪个更快?Tensor Core 的工作原理是什么?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/美团-北斗-AI-Infra-校招.md`
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

## 访存与 Shared Memory

- 使用共享内存时需要注意哪些事项(线程同步、bank conflict 等)?
  - 来源:`docs/interview/AI-Infra-校招-1.md`

- GPU 矩阵转置使用 Shared Memory 有什么优势?
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`

- 实现 Weight-Only 量化 CUDA kernel 时如何优化访存?Marlin kernel 是怎么做的?
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`

- CUDA Global Memory 与 Shared Memory 在访存时分别要关注哪些问题?
  - 来源:`docs/interview/AI-Infra-综合面经题库-3.md`

- 在 3090 上单个 block 可用的 Shared Memory 最大容量是多少?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- GPU 全局内存与共享内存有什么区别?如何有效利用共享内存?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- Cache 的工作原理是什么?如何提升缓存命中率?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 时间局部性与空间局部性分别是什么?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 主流 GPU 型号的 Cache 容量分别是多少?
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- 同一 Warp 内不同线程的访存约束条件有哪些?
  - 来源:`docs/interview/蔚来-AI-Infra-实习.md`

- 共享内存中的广播机制(Broadcast)是什么?
  - 来源:`docs/interview/蔚来-AI-Infra-实习.md`

- 什么是线程束分歧(warp divergence)?它对性能有什么影响?
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- 分块计算中如何保证数据在缓存中的连续性?
  - 来源:`docs/interview/荣耀-AI-Infra-校招-二面.md`

- 某些特殊 Shape 下使用 Shared Memory 导致计算结果出错,应如何排查与诊断?
  - 来源:`docs/interview/OPPO-AI-Infra-实习-二面.md`

- NHWC 与 NCHW 数据排布各有什么特点?训练与推理部署中应如何选择?
  - 来源:`docs/interview/OPPO-AI-Infra-实习-二面.md`

- 什么情况下应该放弃使用 Shared Memory(如 Bank Conflict 严重或直接走 L2 更快)?
  - 来源:`docs/interview/OPPO-AI-Infra-实习-二面.md`

- 访存优化有哪些具体策略?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- GPU 的 L1/L2 缓存各自承担什么角色?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/AI-Infra-校招-1.md`

- 共享内存与 L1 Cache 的关系与差异是什么?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- 访存优化方案通常如何设计?
  - 来源:`docs/interview/快手-AI-Infra-校招-1.md`

- 模型训练过程中如何优化访存效率?
  - 来源:`docs/interview/拼多多-AI-Infra.md`

- 使用 float4 读写全局内存为什么能提升性能?
  - 来源:`docs/interview/网易-AI-Infra-校招.md`
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- 如何通过数据填充(padding)或内存布局调整避免 bank conflict?
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- 使用寄存器时可能遇到哪些问题(如寄存器溢出)?应如何处理?
  - 来源:`docs/interview/美团-AI-Infra-一面.md`
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- 共享内存(Shared Memory)与硬件缓存(Cache)的区别是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`

- 什么是 Shared Memory Bank Conflict?产生原因和规避策略有哪些?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习.md`
  - 来源:`docs/interview/寒武纪-AI-Infra-实习.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习.md`
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`
  - 来源:`docs/interview/美团-AI-Infra-一面.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/海康威视-AI-Infra.md`

- 编写算子时如何最大化利用缓存,并根据 L1、L2 容量进行数据分块?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`

## Kernel 与性能优化

- 针对一个 CUDA kernel 做性能优化,可以从哪些维度入手?
  - 来源:`docs/interview/AI-Infra-校招-1.md`

- 用 CuTe DSL 或手写 CUDA 实现算子融合的具体做法是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-4.md`

- 实现 kernel fusion 时通常采用哪种方式?
  - 来源:`docs/interview/AI-Infra-综合面经题库-4.md`

- 算子融合后性能反而下降的情况,原因是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-4.md`

- 如何用 Agent 自动生成 CUDA kernel?
  - 来源:`docs/interview/AI-Infra-综合面经题库-4.md`

- CUDA 中如何实现排序算法?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- #pragma unroll 的作用与使用场景是什么?
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- 是否了解 PPL(商汤高性能计算库)?它提供哪些能力?
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- 对 CUDA 算子做过哪些优化?具体手段是什么?
  - 来源:`docs/interview/旷视科技-AI-Infra-实习-一面.md`

- 算子优化的整体思路与实施过程是怎样的?
  - 来源:`docs/interview/旷视科技-AI-Infra-校招.md`

- Reduce 操作中计算顺序的不同会影响数值精度吗?
  - 来源:`docs/interview/原粒半导体-AI-Infra-一面.md`

- 用 CUDA 实现算子的主要难点有哪些?
  - 来源:`docs/interview/寒武纪-AI-Infra-实习.md`

- Triton 算子的实现逻辑与分块策略是怎样的?
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`

- 是否考虑过用 CUDA 替代 Triton?选择 Triton 的原因是什么?
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`

- RMSNorm 的计算公式是什么?计算访存特性如何?可以从哪些角度优化(负载均衡、Double Buffer、指令替换)?
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`

- 矩阵乘法与反量化融合算子在内存方面有哪些优化策略?
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`

- 稀疏矩阵 SpMV 运算中如何实现负载均衡与带宽优化?
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`

- 针对特定 shape 的算子如何调优以超越官方库性能?
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`

- CUDA Kernel 开发需要掌握哪些内容?
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-1.md`

- Warp 利用率偏低时如何归因?负载不均衡问题如何解决?
  - 来源:`docs/interview/卓驭-AI-Infra-校招-一面.md`

- 推理框架中卷积算子的常见实现方式有哪些?
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/智源研究院-AI-Infra-一面.md`

- NEON 汇编指令的基本用法是什么?
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/壁仞科技-AI-Infra-实习.md`

- 用 CUDA 加速图像预处理有哪些实现方法与优化策略?
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`

- CUDA 中实现 softmax 时,warp 级处理与 block 级处理有什么区别?
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`

- 手写 CUDA Softmax 算子
  - 来源:`docs/interview/海康威视-AI-Infra.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/太初-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/AI-Infra-校招-1.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- Softmax 运算中如何解决负载不均衡问题?
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招-一面.md`

- 底层性能优化包括哪些算法层面与硬件层面的手段?
  - 来源:`docs/interview/荣耀-AI-Infra-一面.md`

- Softmax 的数值稳定性如何处理?Online Softmax 的原理是什么?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/海康威视-AI-Infra.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-3.md`
  - 来源:`docs/interview/后摩智能-AI-Infra-实习.md`
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`

- 计算与访存如何实现重叠(Overlap)?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- KV Cache 稀疏计算的实现细节是什么?vLLM Triton kernel 如何编写?为何不采用掩码方式?
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-3.md`

- Triton 与 CUDA 在算子开发中的主要区别是什么?
  - 来源:`docs/interview/拼多多-AI-Infra.md`

- 针对 KL 散度算子做了哪些具体优化?
  - 来源:`docs/interview/拼多多-AI-Infra.md`

- 在静态图中如何筛选适合融合的算子组合?
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-2.md`

- 卷积算子的优化通常从哪些方面入手?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-3.md`
  - 来源:`docs/interview/商汤-AI-Infra-一面.md`

- 手写 CUDA 矩阵乘法算子(naive 版本),并说明后续优化方向及最佳分块大小的确定方法
  - 来源:`docs/interview/字节跳动-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/美团-北斗-AI-Infra-校招.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/AI-Infra-校招-1.md`

- RMSNorm 相比 LayerNorm 性能提升的原因是什么?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- RMSNorm 的具体实现方式是怎样的?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`

- CUDA 算子优化的具体实践有哪些?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/Teleai-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/易控智驾-AI-Infra-二面.md`
  - 来源:`docs/interview/理想汽车-AI-Infra-一面.md`
  - 来源:`docs/interview/理想汽车-云-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`
  - 来源:`docs/interview/原粒半导体-AI-Infra-一面.md`
  - 来源:`docs/interview/壁仞科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/英伟达-AI-Infra.md`
  - 来源:`docs/interview/旷视科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/上海AI实验室-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`
  - 来源:`docs/interview/好未来-AI-Infra-一面.md`
  - 来源:`docs/interview/小光子-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/识渊科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/小米-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/快手-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/拼多多-AI-Infra.md`
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/阿里巴巴-AI-Infra-1.md`
  - 来源:`docs/interview/阿里巴巴-云-AI-Infra-实习-二面-1.md`

- Reduce 操作有哪些常见的优化策略?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/太初-AI-Infra-一面.md`
  - 来源:`docs/interview/好未来-AI-Infra-一面.md`
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`

- 多头注意力与多 batch 场景下如何实现并行计算?
  - 来源:`docs/interview/腾讯-AI-Infra.md`

- 突破现有执行模型瓶颈的优化方向有哪些(CRTP 减少虚函数开销、物化模型批量返回数据)?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 算子融合是什么?conv + BN 融合的公式如何推导?为什么可以融合?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/字节跳动-豆包-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/OPPO-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/上海AI实验室-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-3.md`
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/快手-AI-Infra-校招-1.md`
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-2.md`

- 针对单算子性能优化有哪些常见方法与手段(如 GEMM / Conv 优化策略)?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-2.md`

## 编程题

- 实现 NCHW 到 NHWC 的数据格式转换
  - 来源:`docs/interview/AI-Infra-校招-1.md`

- 实现支持 torch broadcast 语义的 4D tensor elementwise 乘法
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- 给定 A(1,256)、B(256,128)、C(128,256),计算 (A*B)*C 时如何选择结合顺序
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- Embedding Sparse Feature Pooling:用 10^6 个离散 ID 与 10^6 个 float 求长度为 1000 的分桶求和数组
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- 实现 Flash Attention v1
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`

- 用 CUDA 实现平均池化(Avg Pooling)
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- 手写一个 CUDA 算子
  - 来源:`docs/interview/摩尔线程-AI-Infra-实习-二面.md`

- 实现向量外积运算
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`

- 用 CUDA 编写四维张量的 Concat Kernel(针对不同维度分别实现)
  - 来源:`docs/interview/元戎启行-AI-Infra-校招-一面-2.md`

- 阅读给定的 CUDA Kernel 代码并分析其功能。
  - 来源:`docs/interview/小鹏汽车-AI-Infra-一面.md`

- 用 CUDA 在 uint8 数组中查找第 K 大的值
  - 来源:`docs/interview/小鹏汽车-AI-Infra-实习.md`

- 编写 CUDA 算子:计算矩阵每一行的 reduce sum
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习.md`

- 手写 CUDA kernel:conv2d 实现
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一面-2.md`

- 手写一个自定义 CUDA kernel
  - 来源:`docs/interview/小厂-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一面-2.md`

- 用 CUDA 实现 Reduction 归约求和
  - 来源:`docs/interview/B站-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- 用 CUDA 实现矩阵转置
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/小鹏汽车-AI-Infra.md`
  - 来源:`docs/interview/英伟达-AI-Infra-校招-2.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- 用 CUDA 编写 Norm 算子:norm = (x - mean) / std
  - 来源:`docs/interview/快手-AI-Infra-实习.md`

- 编写 Online Softmax 与 FlashAttention 的伪代码
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`

- 如何用 CUDA 实现前缀和(prefix sum)?
  - 来源:`docs/interview/美团-北斗-AI-Infra-校招.md`
  - 来源:`docs/interview/寒武纪-AI-Infra-实习.md`

- 实现 Histogram 算子并讨论原子操作与 Shared Memory 局部直方图的优化方案
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-2.md`

- 如何编写 GPU 并行计算相关代码?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- 实现 CUDA 向量加法 Kernel
  - 来源:`docs/interview/百度-AI-Infra-一面-2.md`

- 实现 CUDA LayerNorm Kernel
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`

- 使用 Triton 实现 PagedAttention 的思路是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`

- 用 CUDA 实现向量加法
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-一二面.md`

## Attention Kernel

- Flash Attention v2 的外层循环为何选择遍历 Q?Flash Decoding 的 combine kernel 耗时占比大约多少?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- 如何分析 MLA decode 的计算访存比?它与序列长度、batch size 是否相关?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- Attention 算子的实现方式有哪些?
  - 来源:`docs/interview/三星-AI-Infra-一面-3.md`

- FusedAttention 的优化策略有哪些?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- FlashAttention 中 Bc 块的切分策略与 1-loop FlashAttention 的实现方式
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`

- FlashAttention 在 decoding 阶段存在什么问题?FlashDecoding 如何改进?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`

- Attention 算子层面的加速方案有哪些?
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-1.md`

- Flash Attention 的核心原理是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-1.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-2.md`
  - 来源:`docs/interview/京东-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`
  - 来源:`docs/interview/AI-Infra-一面.md`
  - 来源:`docs/interview/美团-AI-Infra-一面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招.md`
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/小米-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/快手-AI-Infra-一面.md`
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`
  - 来源:`docs/interview/腾讯-AI-Infra.md`
  - 来源:`docs/interview/阿里巴巴-AI-Infra-校招-一面.md`

- FlashAttention 中注意力矩阵的维度推导过程是怎样的?
  - 来源:`docs/interview/腾讯-AI-Infra.md`

- FlashAttention 中 K 矩阵是否包含 Q 对应的那个维度?
  - 来源:`docs/interview/腾讯-AI-Infra.md`

- 除 Flash Attention 和 KV-Cache 外还有哪些注意力机制优化方法?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-校招-一面.md`

## CUDA 编程模型

- 如何确定合适的 blockSize 与 gridSize?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- default stream 是什么?存在哪些潜在问题?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- threadfence 的作用是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- Unified Memory 与 Zero-Copy Memory 有什么区别?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- CPU 上的数据如何拷贝到 GPU?
  - 来源:`docs/interview/旷视科技-AI-Infra-校招.md`

- CUDA Graph 的作用与原理是什么?kernel launch 的完整流程是怎样的?
  - 来源:`docs/interview/小马智行-AI-Infra-实习.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- blockDim 与 blockIdx 的含义及使用方式是什么?
  - 来源:`docs/interview/好未来-AI-Infra-一面.md`

- 跨 Block 的通信方式与 Warp 级原语有哪些?常用 Warp 原语的功能是什么?
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`
  - 来源:`docs/interview/小马智行-AI-Infra-实习.md`

- cudaMemcpy 时为什么需要锁定(pin)内存?
  - 来源:`docs/interview/经纬恒润-AI-Infra-二面.md`
  - 来源:`docs/interview/阶跃星辰-AI-Infra-实习.md`

- CUDA Stream 是什么?同步流与异步流有什么区别?
  - 来源:`docs/interview/OPPO-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`
  - 来源:`docs/interview/AI-Infra-校招-1.md`

- 如何确定一个 CUDA kernel 最优的线程数量配置?
  - 来源:`docs/interview/OPPO-AI-Infra-实习-二面.md`

- CUDA 编程模型的层次结构(grid、block、thread)是什么?
  - 来源:`docs/interview/OPPO-AI-Infra-实习-二面.md`
  - 来源:`docs/interview/智源研究院-AI-Infra-二面.md`
  - 来源:`docs/interview/辉羲智能-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/AI-Infra-校招-1.md`
  - 来源:`docs/interview/美团-AI-Infra-一面.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- CUDA_DEVICE_MAX_CONNECTIONS 环境变量的含义是什么?
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`

- CUDA 中 launch bound 的含义是什么?H2D 与 D2H 传输能否重叠?
  - 来源:`docs/interview/快手-AI-Infra-校招-2.md`

- CUDA 内核中线程局部变量存在哪里?与寄存器分配有什么关系?
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- Warp shuffle 指令的概念是什么?在 warp 内数据交换与规约中有何优势?
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- CUDA 中的内存分类有哪些?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- Kernel 函数是什么?__global__ 关键字的作用是什么?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- 如何获取 GPU 允许的最大线程数量?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- 设计一种比 cudaMalloc 更灵活高效的显存分配方案
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- CUDA 提供了哪几种编程模型或方式?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- 有哪些方法可以降低 launch kernel 的开销?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一面-1.md`

- CUDA 内存模型包含哪些层级?各自的特点是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`
  - 来源:`docs/interview/美团-AI-Infra-一面.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`
  - 来源:`docs/interview/AI-Infra-校招-1.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-一面.md`

- CUDA 编程中并行性与并发性分别指什么?二者有何区别?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习-一面.md`

## 并行编程(OpenCL)

- OpenCL 的执行流程是怎样的?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 编写 OpenCL kernel 时为什么要减少分支?掩码的作用是什么?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- OpenCL kernel 的主要参数包括哪些?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 用 OpenCL 实现矩阵乘法与向量求和
  - 来源:`docs/interview/AI-Infra-面经-1.md`

## 调试与性能分析

- 如何验证和确定计算精度?
  - 来源:`docs/interview/原粒半导体-AI-Infra-一面.md`

- 如何调试 CUDA kernel?
  - 来源:`docs/interview/壁仞科技-AI-Infra-实习.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- 显存越界问题有哪些常见排查方法?
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招.md`

- 如何用 Profiling 工具定位性能瓶颈(带宽利用率、流水线空泡、指令级耗时)?
  - 来源:`docs/interview/快手-AI-Infra-校招-一面.md`

- 自研 Timing 插件的底层实现是什么?为什么不直接使用 Nsight / NCU?
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-1.md`

- Profiling / Nsight 工具链如何使用?应关注哪些计算效率与带宽效率指标?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/蚂蚁-AI-Infra-实习-一面-2.md`
  - 来源:`docs/interview/卓驭-AI-Infra-实习.md`
  - 来源:`docs/interview/卓驭-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`
  - 来源:`docs/interview/遂原科技-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`
