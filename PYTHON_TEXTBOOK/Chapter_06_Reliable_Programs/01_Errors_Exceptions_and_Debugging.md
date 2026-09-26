# 01 - Errors, Exceptions, and Debugging

## Intuition: Emergency Procedures in a Building

A well-run building has normal routes and emergency procedures. A visitor follows the ordinary path until a condition requires a detour; a fire alarm does not mean the building has no design, but that an exceptional event needs a controlled response. Programs also have normal execution and failure paths. Exceptions let a program respond to a particular runtime problem, while debugging is the investigation that finds why the problem happened.

Handling an error is not the same as fixing its cause. A safe system reports expected failures appropriately while still exposing programmer defects instead of hiding them.

## Learning Objectives

- Distinguish syntax, runtime, and logic errors.
- Read a traceback and build a minimal reproduction.
- Handle specific exception types with `try`, `except`, `else`, and `finally`.
- Decide when to recover, retry, report, or allow an exception to propagate.
- Use a repeatable debugging process and test edge cases.

## Three Broad Error Categories

| Category | When it appears | Example |
|---|---|---|
| Syntax/parse error | Python cannot interpret the source structure | Missing colon after `if` |
| Runtime exception | Valid code encounters an unavailable operation during execution | `100 / 0` raises `ZeroDivisionError` |
| Logic error | The code runs but computes or selects the wrong result | Incorrect age range such as `age >= 1 and age >= 11` |

A logic error may produce no traceback. Tests and manual reasoning are required to catch it. In the earlier age exercise, testing values at both ends of the intended 1-to-11 range would reveal that the conjunction described a different interval.

## Repository Example: Exception Handling

The following complete example is from the exception-handling lesson in `control_flow_statement/Exception_Handling _in_Python.ipynb`:

```python
try:
    age = int(input("Enter your age in whole numbers: "))
    result = 100 / age
    print(f"Calculation complete: {result}")
except ValueError:
    print("Error caught: You must enter numbers, not alphabet text letters!")
except ZeroDivisionError:
    print("Error caught: Age cannot be zero! You cannot divide by 0.")
finally:
    print("System Notification: Exception handling block fully executed.")
```

| Line | Execution behavior |
|---|---|
| `try:` | Begins a suite containing operations that may raise expected exceptions. |
| `age = int(input(...))` | Prompts for text, converts it to an integer, and binds the result. Nonnumeric text raises `ValueError`. |
| `result = 100 / age` | Divides by the value; zero raises `ZeroDivisionError`. |
| success `print` | Executes only if conversion and division succeeded. |
| `except ValueError:` | Handles conversion failures of this type; Python skips the remaining `try` statements and enters the matching handler. |
| first handler print | Gives a user-facing message for malformed numeric input. |
| `except ZeroDivisionError:` | Handles a zero divisor separately. |
| second handler print | Explains why zero cannot be used in this operation. |
| `finally:` | Runs as control leaves the structure, whether the `try` succeeded or a handled exception occurred. |
| final print | Emits a completion message. In production, `finally` is most useful for unconditional cleanup, such as releasing a resource. |

When input is 20, the result is 5.0 and both handlers are skipped; `finally` still runs. When input is `"Ali"`, `int` raises `ValueError`, so the division and success print are skipped, the first handler runs, then `finally` runs. When input is 0, division raises `ZeroDivisionError`, the corresponding handler runs, then `finally` runs.

## Deep Dive: Exception Propagation and Cleanup

When an exception is raised, Python unwinds the active call stack until it finds a matching handler. Statements after the failing operation in the same `try` suite do not run. If no matching handler exists, the exception propagates to the caller and ultimately produces a traceback. A `finally` suite runs while the stack unwinds, making it useful for cleanup regardless of the outcome.

```text
try suite
  |-- no error --> else suite (if present) --> finally --> continue
  |
  +-- exception --> matching except --------> finally --> continue/propagate
```

`else` runs only when the `try` suite completed without an exception. It is a useful place for success-only work that should not accidentally be treated as part of the risky operation. Catch the narrowest useful exception. A broad `except Exception` can be appropriate at an application boundary that logs and translates failures, but silently suppressing it makes defects difficult to diagnose. Avoid catching `BaseException` for ordinary application recovery; it includes process-control exceptions.

## A Disciplined Debugging Workflow

1. **Reproduce:** record exact input, environment, and steps.
2. **Classify:** determine whether the failure is syntax, runtime, or incorrect behavior.
3. **Read the traceback:** start from the exception type and failing line, then inspect relevant caller frames.
4. **Reduce:** build the smallest code/input that still demonstrates the issue.
5. **Inspect assumptions:** check values, types, boundaries, and state transitions.
6. **Change one cause:** avoid changing unrelated logic while testing a theory.
7. **Verify:** retest the failing case, a normal case, and boundary cases.

The repository's debugging worksheet encourages precise prompts: include expected behavior, actual behavior, a minimal code example, exact error text, and edge cases tried. AI-suggested fixes should be reviewed and tested; a plausible explanation is not proof.

## Industry Scenario

A batch import might encounter a malformed row. The system can report that row and continue if the business rule permits it; a missing required source file may require stopping the entire job. Catching both with one generic message loses important information. Define which failures are recoverable, what gets logged, and whether partial output is safe to keep.

## Common Pitfalls

- Catching the wrong exception type and assuming every failure is handled.
- Using bare `except:` and suppressing bugs or process-control signals.
- Printing “success” inside `try` before all required work is complete.
- Assuming `finally` only runs on errors; it runs on success too.
- Returning from `finally`, which can override a prior return or suppress an exception.
- Treating a logic error as a syntax problem.
- Fixing only the exact sample input and leaving boundary cases broken.

## Practice Challenges with Hints

1. Test the example with 20, 0, and `"Ali"`. **Hint:** trace which line fails and which exception type is raised.
2. Add an `else` message for successful division. **Hint:** it runs only if the `try` suite completed without an exception.
3. Protect a list lookup from `IndexError`. **Hint:** first consider whether validating the index is clearer than catching it.
4. Find and repair an incorrect grade boundary. **Hint:** make a decision table with one value below, at, and above each threshold.
5. Write a bug report with expected result, actual result, minimal reproduction, and full traceback. **Hint:** remove unrelated code without removing the failure.

## Summary

Exceptions represent runtime failures and propagate until handled. Specific handlers make expected recovery paths clear; `finally` supports unconditional cleanup. Debugging requires reproduction, traceback reading, state inspection, and regression tests. Catching an error without understanding it can hide rather than solve the problem.
