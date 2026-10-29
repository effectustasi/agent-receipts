# receipts 🧾

[![Validate skills](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml)
[![Latest release](https://img.shields.io/github/v/release/effectustasi/agent-receipts)](https://github.com/effectustasi/agent-receipts/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#install)
[![GitHub stars](https://img.shields.io/github/stars/effectustasi/agent-receipts?style=social)](https://github.com/effectustasi/agent-receipts/stargazers)

[English](README.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · **简体中文** · *希望添加其他语言？[帮助我们翻译](https://github.com/effectustasi/agent-receipts/labels/translation)*

**你的编码智能体说“完成 ✅”，但它根本没有运行代码。**

`receipts` 是一组智能体技能，让 Claude Code、Codex、Cursor 等工具在宣称任何结果前**先展示证据**。

## 使用前 / 使用后

**未使用 receipts**

> 我已经更新了日期解析器，使其支持 ISO 周格式。现在应该可以了。完成 ✅

**使用 receipts 后**

> 已完成。证据如下：
> ```
> $ pytest tests/test_dates.py
> 7 passed in 0.38s
> ```

或者，在无法验证时：

> 已将 `parse_date` 改为接受 ISO 周格式。**尚未验证**：当前环境未配置测试运行器。
> 可这样检查：`python -c "from app.dates import parse_date; print(parse_date('2026-W40'))"`

## 技能

| 技能 | 用于阻止智能体 |
|---|---|
| [`prove-it`](skills/prove-it/SKILL.md) | 在没有运行任何命令时声称“完成”“已修复”或“所有测试通过” |
| [`no-guessing`](skills/no-guessing/SKILL.md) | 凭记忆编造函数名、CLI 参数和配置键 |
| [`repro-first`](skills/repro-first/SKILL.md) | 在没有先复现失败的情况下“修复”问题 |

<a id="install"></a>

## 安装

**Claude Code**

```
/plugin marketplace add effectustasi/agent-receipts
/plugin install receipts@receipts
```

### Codex CLI

Codex CLI 会在开始工作前读取 `AGENTS.md`。在项目根目录运行以下命令，将 receipts 技能追加到该文件：

```bash
for skill in prove-it no-guessing repro-first; do
  curl -fsSL "https://raw.githubusercontent.com/effectustasi/agent-receipts/main/skills/$skill/SKILL.md" >> AGENTS.md
done
```

若要在所有项目中应用这些技能，请将它们追加到 `~/.codex/AGENTS.md`。修改文件后启动新的 Codex 会话，再要求它总结当前生效的指令：

```bash
codex --ask-for-approval never "Summarize the current instructions."
```

有关文件的发现顺序、全局与项目级作用域以及覆盖规则，请参阅 [Codex 官方指令文档](https://developers.openai.com/codex/agent-configuration/agents-md)。

**其他智能体**（Cursor、Copilot、Gemini CLI、OpenCode 等）

将技能文件夹复制到智能体的技能目录，或将每个 `SKILL.md` 的正文粘贴到 `AGENTS.md` 或规则文件中。欢迎为其他智能体补充安装指南：请从 [`agent-support`](https://github.com/effectustasi/agent-receipts/labels/agent-support) 标签中的 issue 开始。

## 基准测试

使用和不使用 `receipts` 运行相同任务，衡量智能体多频繁地声称并不真实的成功结果。每次运行都由脚本核验，而不是由智能体自行判断。

目前结果（Claude Code，300 次运行）：Sonnet 5.5 在所有配置中都没有作出虚假声明。未使用 receipts 时，Haiku 4.5 在 30 次运行中有 13 次作出虚假声明，而 receipts 目前尚未降低这一总数。但它改变了行为：当修复破坏现有测试时，Haiku 现在会停下来询问，而不是修改测试（该任务 10 次运行中 0 次虚假成功）。不过，它仍会修改被固定版本的依赖。

完整表格、对话记录和运行方法见 [benchmark/](benchmark/README.md)。欢迎新增任务，参见 [`benchmark`](https://github.com/effectustasi/agent-receipts/labels/benchmark) 标签。

## 参与贡献

欢迎新增技能、翻译、其他智能体的安装指南和基准测试任务。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [`good first issue`](https://github.com/effectustasi/agent-receipts/labels/good%20first%20issue) 标签。

## 许可证

MIT

## effectustasi 的更多工具

- [blender-dlss5-neural-rendering](https://github.com/effectustasi/blender-dlss5-neural-rendering)：通过 DLSS 5 神经渲染改善 Blender 视口和渲染结果
- [metahuman-face-capture](https://github.com/effectustasi/metahuman-face-capture)：在 Blender 中从网络摄像头捕获 MetaHuman 面部
- [autodesk-inventor-mcp](https://github.com/effectustasi/autodesk-inventor-mcp)：将 AI 智能体连接到正在运行的 Autodesk Inventor 会话
- [unreal-groom-alembic-exporter](https://github.com/effectustasi/unreal-groom-alembic-exporter)：将 Unreal Groom 资产（MetaHuman 头发）导出为 Alembic
