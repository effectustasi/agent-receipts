# receipts 🧾

[![Validate skills](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml)
[![Latest release](https://img.shields.io/github/v/release/effectustasi/agent-receipts)](https://github.com/effectustasi/agent-receipts/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#install)
[![GitHub stars](https://img.shields.io/github/stars/effectustasi/agent-receipts?style=social)](https://github.com/effectustasi/agent-receipts/stargazers)

**English** · [Türkçe](README.tr.md) · *Your language? [Help translate](https://github.com/effectustasi/agent-receipts/labels/translation)*

**Your coding agent says "Done ✅". It never ran the code.**

`receipts` is a set of agent skills that make Claude Code, Codex, Cursor, and friends **show proof** before they claim anything.

## Before / after

**Without receipts**

> I've updated the date parser to handle ISO week formats. This should work now. Done ✅

**With receipts**

> Done. Receipt:
> ```
> $ pytest tests/test_dates.py
> 7 passed in 0.38s
> ```

or, when it can't check:

> Changed `parse_date` to accept ISO weeks. **Not verified**: no test runner is set up here.
> To check: `python -c "from app.dates import parse_date; print(parse_date('2026-W40'))"`

## The skills

| Skill | Stops your agent from |
|---|---|
| [`prove-it`](skills/prove-it/SKILL.md) | Saying "done", "fixed", or "all tests pass" without running anything |
| [`no-guessing`](skills/no-guessing/SKILL.md) | Inventing function names, CLI flags, and config keys from memory |
| [`repro-first`](skills/repro-first/SKILL.md) | "Fixing" bugs it never saw fail |

## Install

**Claude Code**

```
/plugin marketplace add effectustasi/agent-receipts
/plugin install receipts@receipts
```

### Codex CLI

Codex CLI reads `AGENTS.md` before starting work. From your project root, append the receipt skills to it:

```bash
for skill in prove-it no-guessing repro-first; do
  curl -fsSL "https://raw.githubusercontent.com/effectustasi/agent-receipts/main/skills/$skill/SKILL.md" >> AGENTS.md
done
```

To apply the skills to every project instead, append them to `~/.codex/AGENTS.md`. Start a new Codex run after changing the file, then ask it to summarize the active instructions:

```bash
codex --ask-for-approval never "Summarize the current instructions."
```

See the [official Codex instructions documentation](https://developers.openai.com/codex/agent-configuration/agents-md) for discovery order, global versus project scope, and overrides.

**Any other agent** (Cursor, Copilot, Gemini CLI, OpenCode…)

Copy the skill folders into your agent's skills directory, or paste the body of each `SKILL.md` into your `AGENTS.md` or rules file.
Per-agent guides are welcome: pick your agent from the [`agent-support`](https://github.com/effectustasi/agent-receipts/labels/agent-support) issues.

## Benchmark

Coming soon: the same task set run with and without `receipts`, measuring how often the agent claims success that isn't real.
Want to help build it? Check the issues labeled `benchmark`.

## Contributing

New skills, translations, install guides for other agents, and benchmark tasks are all welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the [`good first issue`](https://github.com/effectustasi/agent-receipts/labels/good%20first%20issue) label.

## License

MIT

## More tools by effectustasi

- [blender-dlss5-neural-rendering](https://github.com/effectustasi/blender-dlss5-neural-rendering): Blender viewport and renders through DLSS 5 neural rendering
- [metahuman-face-capture](https://github.com/effectustasi/metahuman-face-capture): MetaHuman face capture from a webcam in Blender
- [autodesk-inventor-mcp](https://github.com/effectustasi/autodesk-inventor-mcp): Connect AI agents to a live Autodesk Inventor session
- [unreal-groom-alembic-exporter](https://github.com/effectustasi/unreal-groom-alembic-exporter): Export UE Groom assets (MetaHuman hair) to Alembic
