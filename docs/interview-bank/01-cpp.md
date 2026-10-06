# C++ / Linux / 系统编程

## 调试与工具

- 数组越界写入破坏了其他数据结构且现场留有 coredump,应如何排查?
  - 来源:`docs/interview/AI-Infra-一面.md`

- GDB 调试工具的使用方法是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`

- C++ 中数组下标越界会导致什么错误?
  - 来源:`docs/interview/字节跳动-AML-AI-Infra-一二面.md`

- Linux 环境下如何进行程序调试和错误定位?
  - 来源:`docs/interview/字节跳动-AML-AI-Infra-一二面.md`

- 调试时如何设置条件断点?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- 如何进行堆栈监视?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

## Linux

- 在 Linux 下如何批量终止包含 torchrun 的进程?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- Linux 常用命令与基本操作有哪些?
  - 来源:`docs/interview/三星-AI-Infra-一面-1.md`
  - 来源:`docs/interview/中兴-AI-Infra-二面.md`
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`

- Linux 下替换文本内容有哪些常用方法?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- vi/vim 编辑器中有哪些常用命令?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 常用的操作系统命令有哪些?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- 操作系统的文件管理机制是怎样的?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

- cgroup 与 namespace 的原理及作用是什么?
  - 来源:`docs/interview/百度-AI-Infra-校招.md`

- Linux 下查看磁盘使用情况的常用命令有哪些?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-一二面.md`

## C++ 语言特性

- C++ 中如何比较两个 float 是否相等?
  - 来源:`docs/interview/AI-Infra-综合面经题库-1.md`

- 函数模板的声明与定义能否分离到不同文件?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- 用 CRTP 实现静态多态的原理是什么?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`

- 拷贝构造函数的参数为什么必须用引用传递?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 如何限制对象只能在堆上创建?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- C++ 函数重载的规则与实现方式是什么?
  - 来源:`docs/interview/三星-AI-Infra-一面-1.md`

- 模板函数的编译过程是怎样的?
  - 来源:`docs/interview/三星-AI-Infra-一面-2.md`

- 在构造函数中调用虚函数会产生什么行为?
  - 来源:`docs/interview/太初-AI-Infra-一面.md`

- C++ 中 lambda 表达式的语法与使用方式是什么?
  - 来源:`docs/interview/沐曦-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 如何通过 const 的作用域与约束找出代码中的编译错误?
  - 来源:`docs/interview/小鹏汽车-AI-Infra-一面.md`

- C++ 面向对象编程的三大特性(封装、继承、多态)分别是什么?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习-一面.md`

- 阐述 C++ 的继承机制。
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- C++ 多继承的特点与注意事项有哪些?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- static 与 const 关键字有什么区别?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- 父类指针转子类指针的安全性问题及内存布局约束是什么?
  - 来源:`docs/interview/蔚来-AI-Infra-实习.md`

- 函数内联在什么情况下会导致性能下降?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`

- inline 关键字对作用域有什么影响?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`

- 除 inline 外还有哪些机制会触发内联(如模板函数)?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`

- 完美转发的概念与实现方式是什么?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`

- C++ 模板编程的核心概念与使用方式是什么?
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`

- C++ 反射机制的原理与实现方式是什么?
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`

- 有符号字符与无符号字符的取值范围分别是什么?
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`

- 如何判断机器是大端还是小端(至少两种方法)?
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 回调函数的实现原理是什么?
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招.md`

- 右值引用的概念及应用场景是什么?
  - 来源:`docs/interview/网易-AI-Infra-校招.md`
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`

- 四种类型转换(static_cast / dynamic_cast / const_cast / reinterpret_cast)的用法与区别
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`
  - 来源:`docs/interview/小鹏汽车-AI-Infra-一面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习.md`

- C++ 中函数重载的机制是什么?编译器如何实现?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- 如何在 main 函数执行之前运行一个函数?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- static 关键字有哪些用途?修饰成员变量与成员函数时行为有何差异?static 全局变量与普通全局变量有何区别?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-1.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-一面.md`

- const 关键字有哪些不同用法?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

- 析构函数是否支持参数传递?是否允许有返回值?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

- 构造函数为什么不能声明为虚函数?析构函数为什么建议声明为虚函数?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-1.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- std::move 与 std::forward 的作用与区别是什么?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- C++11/14/17/20 各版本有哪些新特性?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-HR面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- 类的成员函数是否可以定义为模板函数?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- 左值与右值的定义及区别是什么?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- C++ 中 POD 类型的定义与特性是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- 指针与引用有哪些异同?
  - 来源:`docs/interview/腾讯-AI-Infra-实习.md`
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 虚函数与多态的实现机制是什么?虚函数表存在哪里?单继承、多继承、虚继承下的内存布局有何不同?
  - 来源:`docs/interview/腾讯-AI-Infra-实习.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-1.md`
  - 来源:`docs/interview/京东-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/太初-AI-Infra-一面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-二面-1.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

- C++ 函数调用时的栈帧压栈过程是怎样的?
  - 来源:`docs/interview/腾讯-AI-Infra-实习.md`

- 如何把函数作用域内的局部变量返回到外部使用?
  - 来源:`docs/interview/腾讯-AI-Infra-实习.md`

- 设计并实现一个事件系统的整体思路是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习.md`

- 事件系统中注册的事件如何与 GameObject 的生命周期绑定?
  - 来源:`docs/interview/腾讯-AI-Infra-实习.md`

- C++ 中继承的底层实现机制是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`

- C++ 编译期运行的实现方式(constexpr 等)有哪些?
  - 来源:`docs/interview/腾讯-AI-Infra-校招-一二面-1.md`

## 计算机系统与性能

- CPU 按列遍历行优先存储的矩阵为何比按行遍历慢很多?是哪个性能指标劣化了?
  - 来源:`docs/interview/AI-Infra-综合面经题库-2.md`

- DMA 与 RDMA 的原理及区别是什么?
  - 来源:`docs/interview/阶跃星辰-AI-Infra-实习.md`

- 共享内存的概念及其使用场景是什么?
  - 来源:`docs/interview/太初-AI-Infra-一面.md`

- Cache 的层级结构与常见替换策略有哪些?
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`

- IEEE 浮点标准中 FP16、FP32、FP64 的位宽分配是怎样的?
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`

- 虚拟内存的概念与作用是什么?
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`

- Linux 内存管理机制包括哪些核心内容?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- Linux 下多进程间通信的方式有哪些?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- Linux 内核虚拟地址空间的布局与机制是怎样的?
  - 来源:`docs/interview/小光子-AI-Infra-实习-一面.md`

- 零拷贝技术的原理与应用场景是什么?
  - 来源:`docs/interview/小光子-AI-Infra-实习-一面.md`

- ARM 平台有哪些性能优化方法?
  - 来源:`docs/interview/小厂-AI-Infra-实习-4.md`

- 计算机内存的分级体系是怎样的?
  - 来源:`docs/interview/小厂-AI-Infra-实习-一面.md`

- OpenMP 与 MPI 的区别和使用场景分别是什么?
  - 来源:`docs/interview/海康威视-AI-Infra.md`

- 设计一个 CPU 需要考虑哪些方面?指令集设计与流水线各阶段的作用是什么?
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招-一面.md`

- 用户态与内核态的区别是什么?两者如何切换?
  - 来源:`docs/interview/科大讯飞-AI-Infra-校招-一面.md`

- 零拷贝(Zero-Copy)的实现原理是什么?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- 从按下开机按钮到打开浏览器进入面试链接,计算机底层依次经历了哪些过程?
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- CPU cache 中每条 cache line 由哪三部分组成?各自的作用是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- 为什么需要设计多级缓存?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- 发生 cache miss 后硬件的处理流程是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- 页表机制引入的性能开销有哪些?如何缓解?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- 页表机制带来了哪些好处?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- Cache 映射方式的分类与特点(组相联、全相联、直接映射)
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-二面-1.md`

- 计算机的存储层次结构是怎样的?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- CPU 中应用程序员可见的寄存器有哪些分类?程序计数器(PC)的作用是什么?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- 寄存器与 Cache 哪个更快?Cache 与主存分别采用什么技术实现?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- CPU 上进行算子优化有哪些方法(如 AVX-512)?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`

- CPU 针对分支语句(if)做了哪些预测与优化?
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-2.md`

- Array of Struct 与 Struct of Array 的区别及适用场景是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- Linux 系统的启动过程是怎样的?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 中断处理模块的实现机制是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- CPU 如何处理多个并发中断?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 用户态到内核态的切换过程是怎样的?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

## STL

- vector 的扩容机制是什么?为什么通常按 2 倍扩容?resize 与 reserve 有什么区别?
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 用 STL 迭代器遍历时如何正确删除元素?
  - 来源:`docs/interview/三星-AI-Infra-一面-2.md`

- 常用的 STL 容器有哪些?各自的使用方式与区别是什么?
  - 来源:`docs/interview/三星-AI-Infra-一面-2.md`
  - 来源:`docs/interview/三星-AI-Infra-一面-3.md`

- vector、map、unordered_map 的底层实现分别是什么?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- 如何释放 vector 已分配的内存?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- `std::map` 与 `std::unordered_map` 的底层实现原理有何区别?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/小鹏汽车-AI-Infra.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习-一面.md`

- STL 中 deque 的底层实现原理是什么?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- 除优先队列外还有哪些 STL 容器可实现堆结构?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

## 内存管理

- C++ 内存模型包含哪些内容?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- C++ 中的内存管理机制有哪些?
  - 来源:`docs/interview/太初-AI-Infra-一面.md`

- 智能指针的实现原理是什么?
  - 来源:`docs/interview/太初-AI-Infra-一面.md`

- 智能指针能否管理一段连续的内存空间?
  - 来源:`docs/interview/太初-AI-Infra-一面.md`

- `new`、`malloc` 以及智能指针的使用场景与区别是什么?
  - 来源:`docs/interview/沐曦-AI-Infra-实习-一面.md`

- 堆内存与栈内存有什么区别?
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/小厂-AI-Infra-实习-一面.md`

- 野指针是如何产生的?智能指针如何使用?
  - 来源:`docs/interview/传音-AI-Infra-校招-一面.md`

- 写时拷贝(Copy-on-Write)的实现原理是什么?
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`

- 内存对齐的概念与结构体对齐规则是什么?如何计算给定结构体的 sizeof?
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- C++ 中内存对齐的规则和意义是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-1.md`

- `new` 与 `malloc` 的底层实现原理分别是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/百度-AI-Infra-校招-一面-2.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/沐曦-AI-Infra-实习-一面.md`

- 深拷贝与浅拷贝的概念是什么?什么场景下必须使用深拷贝?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- 智能指针有哪几种?各自的适用场景是什么?shared_ptr 线程安全吗?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-3.md`
  - 来源:`docs/interview/百度-AI-Infra-校招-二面-2.md`
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-二面-1.md`
  - 来源:`docs/interview/小米-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`
  - 来源:`docs/interview/AI-Infra-综合面经题库-6.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- C++ 中内存泄漏的常见原因及解决方案有哪些?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-2.md`
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`

- 程序在内存中的分段结构是怎样的?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`

- C++ 程序的内存布局(栈、堆、全局区、代码区等)是怎样的?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

- 解释 RAII(资源获取即初始化)的概念与应用
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

- unique_ptr 如何保证所有权的唯一性?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- shared_ptr 引用计数归零后何时触发析构?
  - 来源:`docs/interview/百度-AI-Infra-实习-一面-1.md`

- 程序内存中栈、堆与静态/全局存储区各有什么特点与区别?
  - 来源:`docs/interview/百度-AI-Infra-校招-一面-2.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/网易-AI-Infra-校招.md`

- vector 在内存中的存储方式是怎样的?new 分配的 vector 与栈上 vector 是否相同?
  - 来源:`docs/interview/百度-AI-Infra-校招-一面-2.md`

## 并发与线程

- 线程间共享内存时,条件变量与互斥锁各自适用于什么场景?二者有何区别?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 双重检查锁(Double-Checked Locking)存在哪些隐患?
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`

- 进程与线程有什么区别?
  - 来源:`docs/interview/卓驭-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-实习-一面.md`
  - 来源:`docs/interview/阶跃星辰-AI-Infra-实习.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一面-1.md`

- 多线程之间如何进行资源共享?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- C++ 异步编程有哪些实现方式?
  - 来源:`docs/interview/蔚来-AI-Infra-实习-一二三面.md`

- 如何对协程数量进行限制?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 并发编程有哪些常见的实现方式?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 线程同步有哪些常见方法?
  - 来源:`docs/interview/南湖研究院-AI-Infra-一面.md`
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`

- 互斥锁与无锁操作的区别是什么?各自适用于哪些场景?
  - 来源:`docs/interview/海康威视-AI-Infra-实习-一面.md`

- 使用互斥锁可能带来哪些风险?
  - 来源:`docs/interview/海康威视-AI-Infra-实习-一面.md`

- 自旋锁与互斥锁有什么不同?各自的使用场景是什么?
  - 来源:`docs/interview/海康威视-AI-Infra-实习-一面.md`

- 线程无法获取互斥锁时,操作系统会执行哪些操作?
  - 来源:`docs/interview/海康威视-AI-Infra-实习-一面.md`

- 进程、线程和协程的定义分别是什么?在资源占用与调度方式上有哪些关键差异?
  - 来源:`docs/interview/B站-AI-Infra-实习-一面.md`

- 以进程为单位和以线程为单位调度时,公平性方面会产生哪些不同影响?
  - 来源:`docs/interview/B站-AI-Infra-实习-一面.md`

- C++ 中原子操作的概念及其引入的原因是什么?
  - 来源:`docs/interview/字节跳动-AI-Infra-实习-一二三面.md`

- OpenMP 并行区如何开启(pragma omp parallel 语法)?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`

- 并行区内执行 sum++ 与串行执行结果是否一致?如何保证正确性?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-二面-1.md`

- OpenMP 中如何声明并行区域?基本用法是什么?
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-二面-1.md`

- 进程、线程、协程三者的区别与联系是什么?
  - 来源:`docs/interview/百度-AI-Infra-二面-3.md`

- MPI 的基本概念与使用方式是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- 多线程编程的基本原理是什么?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- 常见的锁机制有哪些?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- 死锁的四个必要条件与预防方法是什么?lock_guard 与 unique_lock 有何区别?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 进程与线程(包括用户态线程)的区别是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- 用户态线程的调度方式及可能存在的问题是什么?
  - 来源:`docs/interview/腾讯-TEG-AI-Infra-一二三面.md`

- C++ 中锁有哪些类型?分别适用于什么场景?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-一二面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

## 编译与链接

- C++ 如何调用 C 语言编写的函数?
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 动态链接库的依赖顺序问题及其解决方式是什么?
  - 来源:`docs/interview/小鹏汽车-AI-Infra-一面.md`

- 链接两个库存在同名函数时,最终的调用结果是什么?
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`

- C++ 程序的编译流程是怎样的?动态库与静态库有什么区别?
  - 来源:`docs/interview/字节跳动-AI-Infra-一面-1.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`
  - 来源:`docs/interview/AI-Infra-面经-1.md`

- 动态链接与动态绑定有什么区别?
  - 来源:`docs/interview/百度-AI-Infra-一面-4.md`
  - 来源:`docs/interview/百度-AI-Infra-三面.md`
  - 来源:`docs/interview/百度-AI-Infra-二面-1.md`

- 如何查看动态链接库(.so)中的符号信息?
  - 来源:`docs/interview/百度-AI-Infra-实习-2.md`

## 计算机网络

- TCP 三次握手与四次挥手的流程是什么?
  - 来源:`docs/interview/三星-AI-Infra-一面-1.md`

- TCP/IP 协议栈各层的作用与职责是什么?
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`

- 网络通信中如何通过 IP 地址找到目标主机?
  - 来源:`docs/interview/文远知行-AI-Infra-校招-一面.md`

- 多路复用技术有哪些?在推理框架中如何应用?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- HTTP/2.0 相比 HTTP/1.1 有哪些核心改进?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 视频会议场景通常采用什么通信协议?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- Socket 编程的完整流程是怎样的?
  - 来源:`docs/interview/小光子-AI-Infra-实习-一面.md`

- 视频会议底层为什么使用 UDP 而非 TCP?
  - 来源:`docs/interview/美团-AI-Infra-校招-一面.md`

- TCP、UDP、HTTP、HTTPS 的特点与适用场景对比
  - 来源:`docs/interview/百度-AI-Infra-二面-3.md`

- 浏览器输入 URL 后的完整访问流程是怎样的?
  - 来源:`docs/interview/百度-AI-Infra-二面-3.md`

- send、write、mmap、sendfile 在内核缓冲区与用户缓冲区间的数据传输方式对比
  - 来源:`docs/interview/百度-AI-Infra-二面-3.md`

- UDP 与 TCP 协议的异同有哪些?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- TCP 通过哪些机制保证可靠传输?
  - 来源:`docs/interview/腾讯-AI-Infra-实习-一二面.md`

- UDP 与 TCP 协议分别适用于什么场景?各自的优缺点是什么?
  - 来源:`docs/interview/阿里巴巴-AI-Infra-实习-一二面.md`

## 设计模式

- 开闭原则在实际编码中如何体现?
  - 来源:`docs/interview/中科类脑-AI-Infra-实习-一面.md`

- 常见的设计模式有哪些?单例模式与工厂模式分别适用于什么场景?
  - 来源:`docs/interview/小厂-AI-Infra-一面.md`
  - 来源:`docs/interview/北极雄芯-AI-Infra-一面.md`
  - 来源:`docs/interview/飞腾-AI-Infra-校招-二面.md`
