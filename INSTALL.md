# DevSkill 自动安装与环境初始化指令

本文档既是一份**一键配置指令（可直接复制发给 AI Agent 自动执行）**，也是面向开发者的**跨平台安装手册**。

---

## 🤖 方式一：发送给 AI Agent 自动执行（推荐）

将以下内容完整复制并发送给你的 AI 编程助手（**Antigravity** / **Codex** / **Claude Code** / **Gemini CLI**），AI 将自动为你完成全局技能安装与当前项目的 `AGENTS.md` 初始化：

````markdown
请帮我检查并配置 DevSkill (https://github.com/jxoday/DevSkill) 技能库与工作流规范：

1. **仅识别当前正在运行的客户端与全局技能目录**：
   - 先确认你当前所处的宿主环境（**仅针对当前运行的客户端进行检查与配置，切勿检查或操作其他无关客户端的目录**）：
     - **当前是 Antigravity / Gemini CLI**：
       - Windows: `%USERPROFILE%\.gemini\config\skills\`
       - macOS/Linux: `~/.gemini/config/skills/`
     - **当前是 Codex**：
       - Windows: `%USERPROFILE%\.codex\skills\`
       - macOS/Linux: `~/.codex/skills/`
     - **当前是 Claude Code**：
       - macOS/Linux: `~/.claude/skills/`

2. **检查并同步当前客户端缺失的全局技能**：
   - 仅检查当前客户端的全局技能目录下是否存在来自 DevSkill 的核心技能（如 `using-superpowers`, `android-architecture`, `android-native-dev`, `brainstorming`, `grilling`, `writing-plans`, `executing-plans`, `systematic-debugging`, `test-driven-development` 等）。
   - **冲突处理策略**：
     - **默认跳过（增量补齐，推荐）**：若本地已存在同名技能，**默认跳过不覆盖**，优先保护用户本地原有的个性化修改；
     - **缺失补齐**：仅将本地缺失的技能文件夹从 https://github.com/jxoday/DevSkill 复制到当前客户端的全局目录；
     - *(若用户显式要求“强制全量覆盖/更新”，才进行覆盖同步)*。

3. **初始化当前项目的规范文件**：
   - 检查当前项目根目录下是否存在 `AGENTS.md`：
     - **若不存在**：直接从 https://raw.githubusercontent.com/jxoday/DevSkill/main/AGENTS.md 下载并创建；
     - **若已存在**：**必须主动询问用户（作者）的选择**：
       - 🅰️ **增量合并（推荐）**：将 DevSkill 的核心规则（如 Skill 优先、顶部标准导入等）追加合并到现有 `AGENTS.md` 中，保留项目原有自定义规则；
       - 🅱️ **全量覆盖**：使用 DevSkill 的 `AGENTS.md` 完全替换现有文件；
       - 🆑 **跳过保持现状**：不做任何修改，完全保留当前文件。

4. **完成汇报**：
   - 汇报新增了哪些缺失技能、跳过了哪些已存在技能，以及当前项目的 `AGENTS.md` 处理结果。
````

---

## 💻 方式二：手动运行命令行安装

如果你想通过终端自行安装，可根据操作系统执行以下命令：

### Windows (PowerShell)

```powershell
# 1. 克隆 DevSkill 仓库到临时目录
$tempDir = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), "DevSkill")
if (Test-Path $tempDir) { Remove-Item -Recurse -Force $tempDir }
git clone https://github.com/jxoday/DevSkill.git $tempDir

# 2. 复制技能到对应客户端的全局目录（按需选择）
# Antigravity / Gemini CLI:
$geminiSkills = "$HOME\.gemini\config\skills"
New-Item -ItemType Directory -Force -Path $geminiSkills
Get-ChildItem -Directory $tempDir | Where-Object { $_.Name -notlike ".*" } | Copy-Item -Destination $geminiSkills -Recurse -Force

# Codex:
$codexSkills = "$HOME\.codex\skills"
New-Item -ItemType Directory -Force -Path $codexSkills
Get-ChildItem -Directory $tempDir | Where-Object { $_.Name -notlike ".*" } | Copy-Item -Destination $codexSkills -Recurse -Force

# 3. 在当前项目初始化 AGENTS.md（如果尚不存在）
if (-not (Test-Path "AGENTS.md")) {
    Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jxoday/DevSkill/main/AGENTS.md" -OutFile "AGENTS.md"
    Write-Host "已成功在当前项目创建 AGENTS.md"
}

# 4. 清理临时文件
Remove-Item -Recurse -Force $tempDir
Write-Host "DevSkill 全局安装完成！"
```

### macOS / Linux (Bash)

```bash
# 1. 克隆 DevSkill 仓库到临时目录
TEMP_DIR=$(mktemp -d)
git clone https://github.com/jxoday/DevSkill.git "$TEMP_DIR"

# 2. 复制技能到对应客户端的全局目录（按需选择）
# Antigravity / Gemini CLI:
mkdir -p ~/.gemini/config/skills
cp -r "$TEMP_DIR"/*/ ~/.gemini/config/skills/ 2>/dev/null || true

# Codex:
mkdir -p ~/.codex/skills
cp -r "$TEMP_DIR"/*/ ~/.codex/skills/ 2>/dev/null || true

# Claude Code:
mkdir -p ~/.claude/skills
cp -r "$TEMP_DIR"/*/ ~/.claude/skills/ 2>/dev/null || true

# 3. 在当前项目初始化 AGENTS.md（如果尚不存在）
if [ ! -f "AGENTS.md" ]; then
    curl -fsSL https://raw.githubusercontent.com/jxoday/DevSkill/main/AGENTS.md -o AGENTS.md
    echo "已成功在当前项目创建 AGENTS.md"
fi

# 4. 清理临时文件
rm -rf "$TEMP_DIR"
echo "DevSkill 全局安装完成！"
```
