---
name: grilling
description: Grill the user relentlessly about a plan, decision, or architecture. Stress-tests thinking, exposes unexamined assumptions, and maps decisions as a design tree before implementation. Use when the user wants to stress-test their plan, explore edge cases, resolve ambiguity, or uses '/grill-me', 'grill', '极限推敲', '审视方案', '压力测试'.
license: MIT
metadata:
  category: workflow
  version: "1.0.0"
---

# Grilling (极限推敲与决策树收敛)

在实施任何复杂功能、技术重构或系统架构之前，对设计方案进行严密、无情的**极限推敲（Grilling）与压力测试**，直至消除所有模糊假设与架构死角。

---

## 核心流程与工作流 (The Grilling Workflow)

### 1. 映射设计树 (Map the Design Tree)
将用户的想法/需求抽象为一棵**设计树（Design Tree）**：
- 每一个顶层决策都会分叉为依赖它的子决策。
- 例如：`数据存储选型` → 如果选本地 Room 数据库 → `是否需要离线缓存同步机制` → `冲突解决策略`。

### 2. 按轮次发问前沿决策 (Work the Frontier in Rounds)
- **前沿边界（The Frontier）**：当前前提条件已明确、可以立即决定的问题集合。
- 每一轮中，集中向用户提出当前前沿的所有问题。**绝不凭空跳步猜测未决定的前提**。
- **必须提供推荐答案**：降低用户思考成本，给出明确选项及理由。

### 3. 标准提问格式 (Question Format)

每一轮中的每个问题严格采用如下结构输出：

```markdown
❓ **Q[序号]** - **[问题标题]**
[问题详细描述、背景与面临的权衡/边界情况]

- **选项 A**: [方案描述]
- **选项 B**: [方案描述]
- **选项 C**: [方案描述]

➡️ **推荐方案**: [明确给出 AI 推荐的选项及技术理由]
```

### 4. 逐轮重构与收敛 (Reshape & Converge)
1. **用户回复后**：根据用户的决定剪枝、展开新的子决策分支，更新设计树的前沿（Frontier）。
2. **继续下一轮**：提出下一轮的前沿问题，直到前沿为空（所有决策与边界情况均已达成共识）。
3. **输出定稿摘要 (Design Summary)**：当无后续未决问题时，输出一份结构清晰的《最终技术决策与架构总结》，并引导进入实施计划（`writing-plans`）或代码编写阶段。

---

## 提问聚焦点 (Focus Areas)

在推敲过程中，重点考察以下维度：
1. **边界与极端情况 (Edge Cases)**：网络中断、数据为空、超大并发、非法输入、竞态条件等。
2. **技术选型与权衡 (Trade-offs)**：内存占用 vs 响应速度、单模块快速开发 vs 多模块解耦维护性。
3. **向后兼容与迁移 (Compatibility)**：旧版本数据结构升级、破坏性变更（Breaking Changes）。
4. **依赖与安全边界 (Security & Dependencies)**：权限申请、认证鉴权、敏感数据存储。
