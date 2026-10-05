---
name: no-guessing
description: Use before writing code that calls a library function, CLI flag, config key, environment variable, API endpoint, or file path you have not seen in this session. Requires confirming it exists (in the repo, the installed package, --help, or official docs) instead of writing it from memory. Prevents hallucinated APIs, made-up flags, and wrong parameter names.
---

# No guessing

Memory is a hint, not a source. Before you use a name you have not **seen in this session**, look it up.
That includes names you were told: a task, an issue, or a doc page saying "call `client.upload(..., resumable=True)`" is a claim to check, not proof it exists in the installed version.

## Applies to

- Functions, methods, classes, and their parameter names, from any library.
- CLI commands and flags.
- Config keys, environment variables, feature flags.
- API endpoints, request and response fields.
- File paths and module imports inside the project.

## How to confirm (cheapest first)

1. **The repo:** grep for an existing use. If the project already calls it, copy that usage.
2. **The installed version:** read the package source or type definitions in `node_modules`, `site-packages`, `vendor`, or equivalent. Versions differ; the installed one is the truth.
3. **The tool itself:** `<cmd> --help`, `man <cmd>`, `python -c "import x; help(x.y)"`.
4. **Official docs** for the installed version.

One lookup is enough. This is a reflex, not a research project.

## When you cannot confirm

Do not silently write it anyway. Either pick something you *can* confirm, or mark it:

```
Uses `client.batch_upsert(...)`. **Unconfirmed**: could not find it in the installed SDK (v2.3).
If it fails, check the SDK changelog for the batch method name.
```

## When the docs and the installed version disagree

The installed version wins.

- **Never edit a dependency** to add what the docs promised: vendored or pinned packages, `node_modules`, `site-packages`, `vendor/`, `third_party/`. The next install erases the change, and the code then breaks.
- Solve it in the project's own code, or say the upgrade it needs:

```
`DataFrame.map` only exists from pandas 2.1; the installed version is 1.5.3.
Used `DataFrame.applymap` instead, which 1.5.3 has. After upgrading pandas, switch to `map`.
```

## Red flags you are guessing

- You are about to write a parameter name "that it's probably called".
- The API "looks like" another library you know.
- You are writing a flag from a different version of the tool.
- An error says the name does not exist and your next move is to try a similar name. Stop and look it up instead.
