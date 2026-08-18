# DevSkill 自动安装与环境初始化指令

本文档既是一份**一键配置指令（可直接复制发给 AI Agent 自动执行）**，也是面向开发者的**跨平台安装手册**。

---

## 🤖 方式一：发送给 AI Agent 自动执行（推荐）

将以下内容完整复制并发送给你的 AI 编程助手（**Antigravity** / **Codex** / **Claude Code** / **Gemini CLI**），AI 将自动为你完成全局技能安装与当前项目的 `AGENTS.md` 初始化：

````markdown
请帮我检查并配置 DevSkill (https://github.com/jxoday/DevSkill) 技能库与工作流规范：

1. **识别当前客户端与全局技能目录**：
   - Antigravity / Gemini CLI:
     - Windows: `%USERPROFILE%\.gemini\config\skills\`
     - macOS/Linux: `~/.gemini/config/skills/`
   - Codex:
     - Windows: `%USERPROFILE%\.codex\skills\`
     - macOS/Linux: `~/.codex/skills/`
   - Claude Code:
     - macOS/Linux: `~/.claude/skills/`

2. **检查并同步缺失的全局技能**：
   - 检查上述对应的全局技能目录下是否存在来自 DevSkill 的核心技能（如 `using-superpowers`, `android-architecture`, `android-native-dev`, `brainstorming`, `grilling`, `writing-plans`, `executing-plans`, `systematic-debugging`, `test-driven-development` 等）。
   - 如果尚未安装或缺少技能，请自动克隆 https://github.com/jxoday/DevSkill 到临时目录，并将所有技能文件夹同步复制到你的全局技能目录中。

3. **初始化当前项目的规范文件**：
   - 检查当前项目根目录下是否存在 `AGENTS.md`。
   - 如果不存在，请从 https://raw.githubusercontent.com/jxoday/DevSkill/main/AGENTS.md 读取内容并在当前项目根目录创建 `AGENTS.md`。

4. **完成汇报**：
   - 汇报安装了哪些技能、全局路径位置，以及当前项目的 `AGENTS.md` 初始化状态。
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
