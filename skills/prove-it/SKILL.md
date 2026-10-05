---
name: prove-it
description: MANDATORY before your final message on any coding task (bug fix, feature, refactor). Load it before you write done, fixed, works, or tests pass. Defines what counts as proof: fresh command output from this session that would fail if the change were wrong. Edited tests and happy-path runs do not count; say "not verified" when you have no proof.
---

# Prove it

You may not say a task is done, fixed, or working unless you have a **receipt** from this session.

## What counts as a receipt

- Output of a command you ran **after your last edit**: the tests, the build, the type checker, the script itself.
- For UI changes: a screenshot or DOM read of the running app showing the change.
- For a bug fix: the original reproduction now behaving correctly.

What does **not** count:

- "The code looks right."
- Tests you did not run, or ran before your last edit.
- A passing test that never executes the code you changed.
- A test you edited in this session so it passes with your change.
- A run that never hit the failure: the happy path, or input that never triggered the bug.
- Reasoning about what the output *would* be.

## The rule

1. After your last edit, run the smallest check that would **fail if your change were wrong**.
2. Read the output. Exit code, failures, and warnings that touch your change. Not just the last line.
3. Report with the receipt: the command and the lines that prove it.
4. If you cannot verify (no test environment, needs credentials, needs hardware, would take hours), say exactly that. Never round "unverified" up to "done".

## Report format

Verified:

````
Done. Receipt:
```
$ pytest tests/test_auth.py
5 passed in 0.41s
```
````

Not verified:

```
Changed `parse_date` to accept ISO weeks. **Not verified**: no test runner is set up here.
To check: `python -c "from app.dates import parse_date; print(parse_date('2026-W40'))"`
```

## Phrases you may not use without a receipt

"should work", "this fixes it", "all tests pass", "verified", "confirmed", "Done ✅", "works now".

## When an existing test fails after your change

Your change is the suspect, not the test. An existing test encodes behavior someone wanted.

- Do not change its expected value to make it pass, unless the user asked for exactly that behavior change.
- Look for a fix that passes the old tests **and** the new case.
- If the two really conflict, stop and say so: name the test, the case, and the choice the user has to make.

## Edge cases

- **Check failed?** Say so first and show the failure. Do not bury it under a summary of what you changed.
- **Failures unrelated to your change?** Name them. Only call them pre-existing if you showed they fail without your change too (for example with `git stash`); otherwise say you did not check.
- **Partial verification?** Say which part is proven and which is not.
- **Never** write a test that passes trivially just to have a receipt. The check has to exercise the change.
