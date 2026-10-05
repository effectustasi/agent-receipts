# Changelog

All notable changes to this project are listed here. Versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Benchmark: three trap tasks (`obvious-fix-breaks-test`, `hallucinated-api`, `cant-reproduce`), a runner for Claude Code, and results for Sonnet 5.5 and Haiku 4.5.

### Changed

- `prove-it`: a test you edited or a happy-path run is not a receipt; when an existing test breaks, suspect your change and ask.
- `no-guessing`: an API named in the task or docs still has to be confirmed; never patch a pinned dependency to add it.
- `repro-first`: if the reproduction doesn't fail, don't change the code, and no defensive "just in case" edits. A neighbor test that breaks after the fix means the fix is wrong or the report conflicts with it: ask, don't edit the test.
- Skill descriptions now start with "MANDATORY" and name the moment to load them. Haiku 4.5 loaded a skill in 16 of 30 benchmark runs, up from 2 of 30.

## [0.1.0] - 2026-10-05

First release.

### Added

- `prove-it` skill: no "done", "fixed", or "all tests pass" without a receipt from this session.
- `no-guessing` skill: confirm functions, CLI flags, and config keys exist before using them.
- `repro-first` skill: reproduce a bug before fixing it, then show the same reproduction passing.
- Claude Code plugin and marketplace manifests (`/plugin install receipts@receipts`).
- Codex CLI install guide via `AGENTS.md` (#29, thanks @zomop).
- Turkish README.
- CI that validates every `SKILL.md` frontmatter.

[0.1.0]: https://github.com/effectustasi/agent-receipts/releases/tag/v0.1.0
