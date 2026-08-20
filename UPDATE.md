# DevSkill 技能库上游同步与更新手册 (UPDATE.md)

本文档旨在指导开发者与维护者如何从上游开源项目中**同步、更新并合并最新的技能（Skills）、文档指南（References）、自动化脚本（Scripts）与模版资源（Templates）**。

---

## 🌐 上游开源参考源与全景技能映射 (Upstream Sources & Mapping)

DevSkill 融合并精选了以下优秀开源项目的最佳实践、工业级研发规范与多模态资产：

| 上游开源仓库 | 核心技能与对应文件路径 | DevSkill 对应模块与设计定位 | 开源地址 |
| :--- | :--- | :--- | :--- |
| **`mattpocock/skills`** | • `skills/productivity/grill-me/SKILL.md`<br>• `skills/engineering/grill-with-docs/SKILL.md`<br>• `skills/engineering/improve-codebase-architecture/`<br>• `skills/engineering/domain-modeling/`<br>• `skills/engineering/codebase-design/` | • **`grilling`**：整合 Matt Pocock 的 `grill-me`（决策树收敛）与 `grill-with-docs`（文档驱动推敲），支持 `/grill-me` 与 `/grill-with-docs` 双模式，实时沉淀 `CONTEXT.md` 与 ADRs 架构决策记录。<br>• **架构演化思想**：吸收高内聚深模块设计（Deep Modules）与领域建模最佳实践。 | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **`superpowers-zh`** | • `skills/using-superpowers/`<br>• `skills/brainstorming/`<br>• `skills/writing-plans/` & `skills/executing-plans/`<br>• `skills/subagent-driven-development/`<br>• `skills/test-driven-development/`<br>• `skills/systematic-debugging/`<br>• `skills/verification-before-completion/`<br>• `skills/chinese-*`（Code Review、排版、Git 等） | • **流程总控与工程硬门禁**：前置 `using-superpowers` 路由决策树；TDD 红绿循环；系统化排错；子智能体驱动开发（SDD）；完工前新鲜证据门禁。<br>• **中文本土化体系**：中文技术排版指北、中文审查话术模板与国内 Git 平台接入。 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh/tree/main) |
| **`MiniMax-AI/skills`** | • `skills/frontend-dev/`（含 `scripts/`, `references/`, `templates/`, `canvas-fonts/`）<br>• `skills/fullstack-dev/`（含 `references/`）<br>• `skills/android-native-dev/`（含 `references/`）<br>• `skills/ios-application-dev/`（含 `references/`）<br>• `skills/shader-dev/`<br>*(可选扩展：`flutter-dev`, `react-native-dev`, Office 系列等)* | • **领域专家与深度知识库**：<br>  - `frontend-dev`：旗舰前端（动效 + Minimax TTS/音乐/视频/图像脚本 + Canvas 字体库）；<br>  - `fullstack-dev`：REST/SSE/WebSocket 契约、鉴权流、DB 建模与上线清单；<br>  - `android-native-dev` & `ios-application-dev`：MD3、Android Vitals 监控、SnapKit/SwiftUI、Metal Shader、Apple HIG 指南；<br>  - `shader-dev`：GLSL、Ray Marching、SDF 几何建模与后处理管线。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) |

---

## 🤖 方式一：发送给 AI Agent 自动同步更新（推荐）

将以下内容完整复制并发送给你的 AI 编程助手（**Antigravity** / **Codex** / **Claude Code**），AI 将自动克隆上游最新代码、检测差异并协助合并更新：

````markdown
请帮我从上游开源仓库同步并更新 DevSkill (https://github.com/jxoday/DevSkill) 技能库：

### 1. 上游源与精准映射规则：
1. **mattpocock/skills** (https://github.com/mattpocock/skills.git):
   - **`grilling` 技能**：参考 `skills/productivity/grill-me/SKILL.md` 与 `skills/engineering/grill-with-docs/SKILL.md`，同步更新 DevSkill `grilling` 的极限推敲决策树逻辑与 `CONTEXT.md` / ADR 内联沉淀规范；
   - **架构设计理念**：提取 `improve-codebase-architecture`、`domain-modeling` 与 `codebase-design` 的最佳实践，丰富到各领域技能的 `references/` 中。
2. **superpowers-zh** (https://github.com/jnMetaCode/superpowers-zh.git):
   - **核心工程流程**：同步 `using-superpowers`, `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents`, `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `requesting-code-review`, `receiving-code-review`；
   - **本土化技能**：同步 `chinese-code-review`, `chinese-documentation`, `chinese-git-workflow`, `workflow-runner`。
3. **MiniMax-AI/skills** (https://github.com/MiniMax-AI/skills.git):
   - **领域专家资产**：同步 `frontend-dev`（含 `scripts/` 多媒体生成脚本、`references/` 动效指南、`templates/`、`canvas-fonts/` 字体库）；
   - **移动端与全栈指南**：同步 `android-native-dev`（性能与 Vitals 指南）、`ios-application-dev`（HIG 与布局指南）、`fullstack-dev`（API 契约与发布清单）与 `shader-dev`（着色器技术指南）下的 `references/`。

### 2. 差异检测与更新规则：
- 将上游仓库克隆到系统的临时目录（如 `/tmp/upstream-sync` 或 `$env:TEMP\upstream-sync`）；
- **纯新增文件/子目录**：直接复制补齐到对应的技能目录中；
- **同名文件内容比对**：
  - 若内容与大小一致：跳过；
  - 若存在差异：保留 DevSkill 已有的中文排版优化与个性化定制（如 `AGENTS.md` 约束），智能增量合并新增的参考文档、指南与工具脚本；
- **清理临时目录**：同步完成后删除克隆的临时文件。

### 3. 完成汇报：
- 输出更新摘要：列出具体更新了哪些技能、新增了哪些 `references/` 或 `scripts/` 文件。
````

---

## 💻 方式二：手动运行命令行一键同步脚本

如果你在本地终端维护 DevSkill 仓库，可以使用以下脚本快速拉取上游最新资产：

### macOS / Linux (Bash)

```bash
#!/usr/bin/env bash
set -e

TMP_DIR="/tmp/devskill-upstream-sync"
DEV_SKILL_DIR="$(pwd)"

echo "🚀 开始从上游开源仓库同步技能库..."
rm -rf "$TMP_DIR" && mkdir -p "$TMP_DIR"

# 1. 同步 mattpocock/skills (grilling 及其核心工程思路)
echo "📦 正在拉取 mattpocock/skills..."
git clone --depth 1 https://github.com/mattpocock/skills.git "$TMP_DIR/mattpocock-skills"
if [ -d "$TMP_DIR/mattpocock-skills/skills/productivity/grill-me" ]; then
  mkdir -p "$DEV_SKILL_DIR/grilling"
  echo "  ✅ 已对比同步: mattpocock/skills (grill-me & grill-with-docs -> grilling)"
fi

# 2. 同步 superpowers-zh
echo "📦 正在拉取 superpowers-zh..."
git clone --depth 1 https://github.com/jnMetaCode/superpowers-zh.git "$TMP_DIR/superpowers-zh"
SP_CORE=(using-superpowers brainstorming writing-plans executing-plans subagent-driven-development dispatching-parallel-agents test-driven-development systematic-debugging verification-before-completion requesting-code-review receiving-code-review chinese-code-review chinese-documentation chinese-git-workflow workflow-runner)
for skill in "${SP_CORE[@]}"; do
  if [ -d "$TMP_DIR/superpowers-zh/skills/$skill" ]; then
    mkdir -p "$DEV_SKILL_DIR/$skill"
    cp -r "$TMP_DIR/superpowers-zh/skills/$skill/"* "$DEV_SKILL_DIR/$skill/"
    echo "  ✅ 已同步: $skill"
  elif [ -d "$TMP_DIR/superpowers-zh/$skill" ]; then
    mkdir -p "$DEV_SKILL_DIR/$skill"
    cp -r "$TMP_DIR/superpowers-zh/$skill/"* "$DEV_SKILL_DIR/$skill/"
    echo "  ✅ 已同步: $skill"
  fi
done

# 3. 同步 MiniMax-AI/skills (领域专家与资产)
echo "📦 正在拉取 MiniMax-AI/skills..."
git clone --depth 1 https://github.com/MiniMax-AI/skills.git "$TMP_DIR/minimax-skills"
if [ -d "$TMP_DIR/minimax-skills/skills" ]; then
  MINIMAX_DOMAINS=(frontend-dev fullstack-dev android-native-dev ios-application-dev shader-dev)
  for domain in "${MINIMAX_DOMAINS[@]}"; do
    if [ -d "$TMP_DIR/minimax-skills/skills/$domain" ]; then
      mkdir -p "$DEV_SKILL_DIR/$domain"
      cp -r "$TMP_DIR/minimax-skills/skills/$domain/"* "$DEV_SKILL_DIR/$domain/"
      echo "  ✅ 已同步: $domain 完整资产与指南"
    fi
  done
fi

# 4. 清理临时目录
rm -rf "$TMP_DIR"
echo "🎉 全量上游技能同步完成！请使用 git diff 检查变动并提交。"
```

### Windows (PowerShell)

```powershell
$ErrorActionPreference = "Stop"
$TmpDir = Join-Path $env:TEMP "devskill-upstream-sync"
$DevSkillDir = Get-Location

Write-Host "🚀 开始从上游开源仓库同步技能库..." -ForegroundColor Cyan
if (Test-Path $TmpDir) { Remove-Item -Recurse -Force $TmpDir }
New-Item -ItemType Directory -Force -Path $TmpDir | Out-Null

# 1. 同步 mattpocock/skills
Write-Host "📦 正在拉取 mattpocock/skills..." -ForegroundColor Yellow
git clone --depth 1 https://github.com/mattpocock/skills.git (Join-Path $TmpDir "mattpocock-skills")
Write-Host "  ✅ 已对比同步: mattpocock/skills (grill-me & grill-with-docs -> grilling)" -ForegroundColor Green

# 2. 同步 superpowers-zh
Write-Host "📦 正在拉取 superpowers-zh..." -ForegroundColor Yellow
git clone --depth 1 https://github.com/jnMetaCode/superpowers-zh.git (Join-Path $TmpDir "superpowers-zh")
$SpSkills = @("using-superpowers", "brainstorming", "writing-plans", "executing-plans", "subagent-driven-development", "dispatching-parallel-agents", "test-driven-development", "systematic-debugging", "verification-before-completion", "requesting-code-review", "receiving-code-review", "chinese-code-review", "chinese-documentation", "chinese-git-workflow", "workflow-runner")

foreach ($skill in $SpSkills) {
    $src = Join-Path $TmpDir "superpowers-zh\skills\$skill"
    if (-not (Test-Path $src)) { $src = Join-Path $TmpDir "superpowers-zh\$skill" }
    if (Test-Path $src) {
        $dest = Join-Path $DevSkillDir $skill
        if (-not (Test-Path $dest)) { New-Item -ItemType Directory -Force -Path $dest | Out-Null }
        Copy-Item -Path "$src\*" -Destination $dest -Recurse -Force
        Write-Host "  ✅ 已同步: $skill" -ForegroundColor Green
    }
}

# 3. 同步 MiniMax-AI/skills
Write-Host "📦 正在拉取 MiniMax-AI/skills..." -ForegroundColor Yellow
git clone --depth 1 https://github.com/MiniMax-AI/skills.git (Join-Path $TmpDir "minimax-skills")
$mmSkills = Join-Path $TmpDir "minimax-skills\skills"
if (Test-Path $mmSkills) {
    $domains = @("frontend-dev", "fullstack-dev", "android-native-dev", "ios-application-dev", "shader-dev")
    foreach ($d in $domains) {
        $srcDomain = Join-Path $mmSkills $d
        if (Test-Path $srcDomain) {
            $destDomain = Join-Path $DevSkillDir $d
            if (-not (Test-Path $destDomain)) { New-Item -ItemType Directory -Force -Path $destDomain | Out-Null }
            Copy-Item -Path "$srcDomain\*" -Destination $destDomain -Recurse -Force
            Write-Host "  ✅ 已同步: $d 完整资产与指南" -ForegroundColor Green
        }
    }
}

# 4. 清理临时目录
Remove-Item -Recurse -Force $TmpDir
Write-Host "🎉 全量上游技能同步完成！请使用 git status / git diff 检查变动并提交。" -ForegroundColor Cyan
```

---

## 🛠️ 上游更新后的维护与合规检查清单 (Checklist)

每次从上游同步完成后，必须执行以下 4 步检查与校准：

- [ ] **1. AGENTS.md 行为规则保护校验**：确认 `AGENTS.md` 中的 8 大核心守则（顶部导包、三大硬门禁、阿里 Javadoc 规范等）未被意外修改或覆盖；
- [ ] **2. 相对路径与死链扫描（Reference Validation）**：静态扫描每个技能的 `SKILL.md`，确认其引用的 `references/xxx.md`、`scripts/xxx.py` 和 `templates/` 文件在本地磁盘真实存在；
- [ ] **3. 中文排版合规性（Chinese Documentation）**：遵循 `chinese-documentation` 规范，检查新增文档的中英文混排空格、全半角标点与术语规范；
- [ ] **4. Git Diff 干净度审计**：使用 `git diff` 检查所有变动，剔除不必要的临时缓存、构建残留或操作系统元数据文件（如 `.DS_Store`、`Thumbs.db`）。
