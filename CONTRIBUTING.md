# Contributing

Thanks for helping agents show their receipts. First PRs are very welcome.

## Good first contributions

- **Translations:** `README.<lang>.md` (for example `README.tr.md`, `README.zh-CN.md`).
- **Install guides:** a short section for an agent we don't cover yet.
- **Benchmark tasks:** a small, self-contained coding task where agents tend to claim false success (see [`benchmark/`](benchmark/README.md)).
- **Skill improvements:** a real transcript where a skill failed to trigger or was ignored, plus the wording change that fixes it.

## Adding a new skill

1. Create `skills/<name>/SKILL.md` with `name` and `description` frontmatter.
2. The skill must be about **evidence**: making the agent prove, check, or admit something it would otherwise claim.
3. Include one concrete report example.
4. Keep it under ~100 lines. Agents read every word.
5. Add a row to the table in `README.md`.

## Pull requests

- One topic per PR.
- Say in the description what you tested and how. Yes, we ask for receipts too 🧾
- Maintainers aim to review within 48 hours.

## Code of conduct

Be kind. Low-effort or spam PRs (whitespace changes, auto-generated filler) will be closed.
