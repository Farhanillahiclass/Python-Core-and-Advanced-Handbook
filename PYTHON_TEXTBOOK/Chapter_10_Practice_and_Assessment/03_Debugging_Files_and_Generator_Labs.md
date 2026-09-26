# 03 - Debugging, Files, and Generator Labs

## Intuition: Rehearsing the Failure Path

A reliable operation is not one that assumes every input and device behaves perfectly. It is one that knows what to do when a number is invalid, a file cannot be opened, or a stream ends. These labs deliberately exercise those paths so students can practice diagnosing rather than hiding failures.

## Learning Objectives

- Trace exceptions and select specific recovery behavior.
- Use context managers and safe file modes.
- Understand generator creation, advancement, and exhaustion.
- Reproduce failures and test successful and unsuccessful paths.

## Lab A: Safe Division and Error Diagnosis

The exception notebook demonstrates integer conversion, division, `ValueError`, `ZeroDivisionError`, and `finally`.

### Challenge

Extend the pattern to divide a balance among a requested number of accounts. Handle malformed integer input separately from a zero account count. Add a success-only report and an unconditional completion message.

### Test matrix

| Input | Expected path |
|---|---|
| `5000`, `2` | Successful calculation |
| `5000`, `0` | `ZeroDivisionError` handler |
| `5000`, `abc` | `ValueError` handler |

### Hint

Keep risky conversion/calculation in `try`. Use specific handlers. Put success-only output in `else`; use `finally` only for work that should occur on both success and failure.

## Lab B: Safe File Report

The print-method notebook writes a message using `with open(..., "w") as file:` and `print(..., file=file)`.

### Challenge

Write a small summary file containing a title and two result lines. Run it twice and explain the difference between write and append modes. Then test behavior when the target directory is missing.

### Hint

`w` truncates an existing file; `a` appends. The `with` statement closes the file, but it does not create missing parent directories automatically. Relative paths use the process working directory.

## Lab C: Generator State

The repository's `generator_practice.ipynb` defines `count_to_three`, calls `next(gen)` in one cell, then advances it in another cell.

### Challenge

Consume the generator with `for`, then attempt to consume it again. Restart the kernel and run only the second cell. Explain both outcomes.

### Hint

A generator is stateful and one-pass. The second cell depends on `gen` having been defined and advanced in the current kernel session.

## Lab D: Minimal Debugging Report

Use the debugging worksheet's method to document one failure:

1. Expected behavior
2. Actual behavior
3. Smallest code and input that reproduce it
4. Exact traceback or error type
5. Root cause and proposed fix
6. Tests that show the fix and guard against regression

Do not remove error handling simply to make the sample appear to pass. The goal is to distinguish expected user mistakes from defects that should remain visible to developers.

## Deep Dive: Failure Boundaries

```text
external input -> validate/convert -> domain calculation -> persist/output
       |                 |                   |                |
  malformed text     ValueError          domain rule      OSError
```

Place checks near the boundary where uncertainty enters. Keep the calculation independently testable. File writes should be designed around replacement/append policy and partial-failure consequences; generator consumption should be explicit when retries or replay are required.

## Common Pitfalls

- A bare `except` catches unrelated defects and erases useful evidence.
- A `finally` block is not a substitute for a successful-result branch.
- Write mode can destroy previous content.
- A file path may resolve somewhere other than expected.
- A missing directory and a missing file are distinct situations.
- Re-running a notebook cell may create new state or reuse stale state.
- A generator cannot be rewound after exhaustion.

## Summary and Assessment

Reliable programs define both normal and failure behavior. Exception types, file modes, path resolution, and generator state are all observable parts of the contract. Reproduce, explain, correct, and retest each issue.

1. Complete Labs A-C and record expected versus actual behavior.
2. For each lab, add a normal case and two failure or boundary cases.
3. Explain why a narrow exception handler is better than suppressing every error.
