# DevSkill - 智能编程助手技能与工作流集合

DevSkill 是专为 AI Agent（如 Claude Code、Codex、Gemini CLI、Hermes Agent、Antigravity 等）打造的高质量技能（Skills）与工作流规范集合。旨在通过结构化 SOP、领域专业指南与严格的行为守则，将通用 AI 助手转变为专业的全栈开发与结对编程专家。

---

## ✨ 核心特性

- 🧠 **工程方法论驱动**：内置 TDD（测试驱动开发）、系统化调试、头脑风暴构思与多步骤执行计划等高质量研发工作流。
- 🛠️ **多领域专家技能**：覆盖 Android 原生开发、iOS 应用开发、现代前端、全栈架构、着色器（Shader）开发等领域。
- 🇨🇳 **本地化工程增强**：提供中文 Code Review 沟通模板、中文技术文档排版规范、中文 Git 提交规范等中国特色技能。
- 📐 **严格代码守则**：内置 `AGENTS.md` 行为准则，强约束顶部标准导包、杜绝内联长路径调用，确保生成代码一次性编译通过。

---

## 📂 技能库概览 (Skills Index)

### 1. 核心流程与工程方法 (Core Workflows)
| 技能目录 | 作用与适用场景 |
| :--- | :--- |
| **`using-superpowers`** | 技能优先检索与启动调度中心，确保所有请求在响应前先检查并调用适用的 Skill。 |
| **`brainstorming`** | 头脑风暴与需求探索，在开始任何功能实现前先探索设计方案与用户意图。 |
| **`writing-plans`** | 编写清晰详尽的分步实施计划，包含检查点与风险分析。 |
| **`executing-plans`** | 计划执行引擎，分批次执行任务并设立审查检查点。 |
| **`test-driven-development`** | 测试驱动开发（TDD）规范，编写实现代码前先编写并运行失败测试（红-绿-重构）。 |
| **`systematic-debugging`** | 系统化调试方法论，遇到异常或 Bug 时根因分析，杜绝盲目试错。 |
| **`verification-before-completion`** | 交付前验证规范，用实际运行结果与测试数据支撑完成断言。 |

### 2. 团队协作与代码审查 (Collaboration & Review)
| 技能目录 | 作用与适用场景 |
| :--- | :--- |
| **`requesting-code-review`** | 请求代码审查，完成重要功能或合并前进行自检与审查准备。 |
| **`receiving-code-review`** | 接收审查反馈，对反馈进行技术验证与精准实施，避免敷衍附和。 |
| **`dispatching-parallel-agents`** | 分发并行子智能体，处理无顺序依赖的独立任务。 |
| **`subagent-driven-development`** | 子任务分发与驱动开发工作流。 |
| **`workflow-runner`** | 跨多角色协作工作流执行引擎。 |

### 3. 领域开发专家技能 (Domain Development)
| 技能目录 | 核心技术栈与重点能力 | 作用与适用场景 |
| :--- | :--- | :--- |
| **`android-architecture`** | **NowInAndroid 现代化工程架构**<br>• Offline-First 离线优先架构（Room + Flow）<br>• 多模块化设计（`api` / `impl` 分离）<br>• Jetpack Compose + MVI/UDF 单向数据流<br>• Hilt 依赖注入、Version Catalog 与 Gradle 约定插件 | 构建符合 Google 官方规范的高质量中大型 Android 项目、多模块拆分、ViewModel + UiState 设计与数据层封装。 |
| **`android-native-dev`** | **Android 原生开发与 Material 3 全流程**<br>• Material Design 3 设计规范（8dp 网格/48dp 热区/动态配色）<br>• Kotlin 协程与线程模型（Main/IO/Default 线程安全）<br>• Product Flavors 多渠道配置与 Build Variants<br>• 编译错误诊断与 Android Vitals 性能优化 | Android 应用端到端开发、MD3 界面设计、无障碍适配、Kotlin 语法避坑、Gradle 构建配置与故障排查。 |
| **`ios-application-dev`** | **iOS 原生开发与 Apple HIG 规范**<br>• SwiftUI 响应式声明与 UIKit + SnapKit 自动布局<br>• Apple Human Interface Guidelines 规范适配<br>• Safe Area、Dynamic Type 动态字体与 Dark Mode<br>• CollectionView/List 性能调优与无障碍（A11y） | iOS 原生应用开发、Swift 页面与组件构建、Apple 平台设计规范审查、复杂列表与交互实现。 |
| **`frontend-dev`** | **现代前端工程与高质感 UI**<br>• 响应式布局、Design Tokens 与现代化 CSS<br>• 微交互与动效体验设计（Micro-interactions）<br>• 语义化 HTML5 与 Web 无障碍访问规范 | 现代化 Web 前端开发、高品质 UI/UX 设计实现、组件库封装与页面交互调优。 |
| **`fullstack-dev`** | **全栈架构与端到端系统设计**<br>• RESTful API / GraphQL 接口设计规范<br>• 端到端状态管理与前后端数据契约<br>• 身份认证（JWT/OAuth）与数据库建模 | 全栈 Web 应用开发、系统架构拆分、前后端接口对接与全链路功能交付。 |
| **`shader-dev`** | **图形着色器与渲染特效**<br>• GLSL / HLSL / Metal 着色器开发<br>• 渲染管线与光照/后处理特效计算<br>• 图形数学算法与 GPU 性能优化 | 2D/3D 视觉特效制作、自定义 Shader 编写、Canvas/WebGL/图形渲染管线开发。 |

### 4. 中文与本地化规范 (Localization)
| 技能目录 | 作用与适用场景 |
| :--- | :--- |
| **`chinese-documentation`** | 中文技术文档排版指南（遵循中英文混排空格、标点及术语规范）。 |
| **`chinese-code-review`** | 中文 Code Review 话术模板、分级标注与反模式应对。 |
| **`chinese-git-workflow`** | 中文 Git 提交规范与协作工作流。 |

---

## 🚀 安装与使用指南

你可以将本仓库的技能引入到你的 AI 编程工作流中：

### 方式一：作为全局技能引入（推荐）

将对应技能文件夹复制到你的全局配置目录：

- **Antigravity / Gemini CLI**:
  ```bash
  # Windows
  xcopy /E /I DevSkill\* "%USERPROFILE%\.gemini\config\skills\"
  
  # macOS / Linux
  cp -r DevSkill/* ~/.gemini/config/skills/
  ```

- **Codex**:
  ```bash
  # Windows
  xcopy /E /I DevSkill\* "%USERPROFILE%\.codex\skills\"
  
  # macOS / Linux
  cp -r DevSkill/* ~/.codex/skills/
  ```

- **Claude Code**:
  ```bash
  # macOS / Linux
  cp -r DevSkill/* ~/.claude/skills/
  ```

### 方式二：作为项目级技能引入

在你的项目根目录下创建 `.agents/skills` 目录，并将所需技能放入其中：

```bash
mkdir -p .agents/skills
cp -r /path/to/DevSkill/<skill-name> .agents/skills/
```

并在项目根目录下放置 `AGENTS.md`，使项目成员和 Agent 保持一致的工作习惯。

---

## 📜 工作流规范配置 (AGENTS.md)

本项目根目录下提供了预置的 `AGENTS.md`，用于约束 Agent 的底层行为：
1. **Skill 优先**：任何回复和行动前先检索匹配的 Skill。
2. **多语言导入规范**：强制顶部标准 `import`，严禁在正文中使用冗长的全限定类名内联调用，杜绝漏导包。
3. **执行透明化**：每次回答末尾明确标注所使用的 Skill 及检查过程。

*(注：`AGENTS.md` 中的人设及称呼部分为个性化定制示例，可按需修改或移除)*

---

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request 来完善技能库！
- 如果你设计了新的专业领域 Skill，请遵循标准 YAML Frontmatter 格式编写 `SKILL.md`。
- 中文文档与技能描述请遵循 `chinese-documentation` 排版规范。

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 授权。
