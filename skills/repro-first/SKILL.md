---
name: repro-first
description: Use when fixing any bug, error, crash, traceback, failing test, or "X doesn't work" report. Requires reproducing the failure and showing it before changing code, finding the root cause, then showing the same reproduction passes after the fix. Prevents blind fixes, symptom patches, and "fixed" claims for bugs that were never observed.
---

# Repro first

A fix for a bug you never saw fail is a guess.

## Steps

1. **Reproduce.** Find a command, test, or request that shows the failure. Run it. Show the failing output.
2. **Locate the root cause.** Trace from the failure to the line that is actually wrong. Before editing a shared function, find its other callers: the fix usually belongs where they all pass through, not in the one path the report mentions.
3. **Fix** the cause, not the symptom. No `try/except: pass`, no special case for the one input from the report, unless that really is the bug.
4. **Re-run the same reproduction.** Show it passing now.
5. **Check the neighbors.** Run the tests around the code you touched, so the fix did not break a sibling case.

## Report format

````
Repro (before):
```
$ python -m app import data/broken.csv
KeyError: 'date'
```
Cause: `load_rows` assumed every CSV has a `date` header; exports from v1 call it `Date`.
Fix: normalize header case in `load_rows` (all 3 importers go through it).
Repro (after):
```
$ python -m app import data/broken.csv
Imported 1,204 rows.
```
Neighbors: `pytest tests/test_import.py` → 12 passed.
````

## When you cannot reproduce

If the reproduction does not fail, **do not change the code**. Your answer starts with **Could not reproduce**.

No defensive edits "just in case": `errors="replace"`, a broad `try/except`, a fallback list of encodings, a retry. They hide the cause and turn a crash into silent bad data. Running the code after such an edit and seeing it work proves nothing; it worked before the edit too.

```
**Could not reproduce**: `import data/broken.csv` succeeds here (Python 3.12, macOS).
Likely differences: OS line endings, file encoding. Can you share the exact file or the full traceback?
```

If the user wants a best-guess fix anyway, label it **unreproduced** and explain what would confirm it.

## Write the repro down

If the project has tests, turn the reproduction into a test that failed before the fix and passes after. That is the receipt that keeps the bug fixed.
