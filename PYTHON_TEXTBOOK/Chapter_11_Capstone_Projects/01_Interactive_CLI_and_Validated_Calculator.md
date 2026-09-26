# 01 - Interactive CLI and Validated Calculator

## Project Overview

This capstone combines input validation, conversion, functions, conditions, exception handling, and formatted output into one command-line workflow. The repository already contains each building block in separate exercises; this project connects them without relying on hidden notebook state.

## Intuition: A Calculator as a Small Service Desk

A calculator receives two values and an operation request, checks that the request is valid, performs exactly one operation, and reports the result. Treat each step like a desk with a contract: input parsing returns a valid number, calculation returns a value or a known error, and the interface communicates the result.

## Learning Objectives

- Separate user interaction from calculation logic.
- Validate numeric input and reject non-finite values.
- Handle supported operators and division by zero explicitly.
- Test functions independently from the command-line interface.
- Document normal and invalid behavior.

## Project Specification

The program must:

- request two finite numeric values;
- support addition, subtraction, multiplication, and division;
- reject unknown operators;
- report division by zero clearly;
- avoid crashing on malformed numeric input;
- keep the calculation logic testable without `input()`.

## Complete Teaching Implementation

This is a new synthesis of the repository's input-validation, arithmetic-function, and exception examples:

```python
import math


def read_number(prompt):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("Enter a valid number.")
            continue
        if not math.isfinite(value):
            print("Enter a finite number.")
            continue
        return value


def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("The second value must not be zero.")
        return first / second
    raise ValueError("Supported operators are +, -, *, and /.")


def main():
    first = read_number("First number: ")
    operator = input("Operation (+, -, *, /): ").strip()
    second = read_number("Second number: ")
    try:
        result = calculate(first, operator, second)
    except (ValueError, ZeroDivisionError) as error:
        print(f"Cannot calculate: {error}")
        return
    print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
```

| Line or group | Explanation |
|---|---|
| `import math` | Imports `math.isfinite` to reject NaN and positive/negative infinity. |
| `read_number(prompt)` | Defines a reusable parser that owns the prompt/retry responsibility. |
| `while True:` | Repeats until a valid value is returned. Each failure path must continue or return. |
| `input(...).strip()` | Reads text and removes surrounding whitespace. |
| `try` / `float(...)` | Attempts numeric conversion; malformed text raises `ValueError`. |
| `except ValueError` | Reports a correction and continues to request a new value. |
| finite-value check | Rejects `nan` and infinities, which `float` can parse but are unsuitable for ordinary calculator results. |
| `return value` | Ends the successful parser call and sends the number to its caller. |
| `calculate(first, operator, second)` | Defines pure calculation logic with explicit inputs. |
| arithmetic branches | Select one operation and return its result; these branches do not prompt or print. |
| division guard | Raises a specific exception before division by zero. |
| final `ValueError` | Rejects an unsupported operator rather than silently returning an arbitrary result. |
| `main()` | Coordinates prompts, calculation, and display. |
| `try` / `calculate(...)` | Catches only the expected user-facing calculation errors. |
| exception handler | Formats a useful error message and exits the interface function. |
| result print | Uses general format `g` to avoid unnecessary trailing decimal zeroes. |
| main guard | Runs the interactive interface only when the file is executed directly, not when imported for tests. |

## Execution Flow

```text
prompt -> parse finite number -> read operator -> parse second number
                                                    |
                                                    v
                                       calculate or raise known error
                                          |                  |
                                       result             message
                                          \                  /
                                         display and exit
```

## Test Plan

| Case | Expected behavior |
|---|---|
| `8`, `+`, `4` | Displays 12 |
| `8`, `/`, `0` | Reports a zero-divisor message, no traceback |
| `abc` as a number | Re-prompts without terminating |
| `nan` or `inf` | Rejects and re-prompts |
| `8`, `%`, `4` | Reports unsupported operator |

Test `calculate` directly with ordinary values and expected exceptions. Test `read_number` separately using controlled input when practical. Avoid tests that depend on unpredictable manual interaction.

## Common Pitfalls and Extensions

- Keeping prompts inside `calculate` makes arithmetic harder to test.
- Catching every exception can hide programming defects.
- Accepting `NaN` can produce confusing comparisons and formatted output.
- Returning a string instead of a number prevents later numeric use.
- Silently treating an unknown operator as addition is a logic bug.
- Extend with a menu, calculation history, or file report only after the core contract passes tests.

## Review Exercises

1. Add exponentiation while documenting accepted input limits. **Hint:** handle potentially huge results deliberately.
2. Add a menu option to quit. **Hint:** keep loop control in `main`, not in `calculate`.
3. Write direct tests for every operator and each error condition. **Hint:** test returned values and exception types separately.
4. Explain why `main` is behind a main guard. **Hint:** importing should not unexpectedly prompt a test runner.

## Completion Checklist

- Each input path has a clear validation rule.
- Calculation returns values and does not print.
- Supported and unsupported operators have defined behavior.
- Division by zero and malformed input are handled specifically.
- Tests cover ordinary, boundary, and invalid cases.
- The program has a short README with run instructions and limitations.
