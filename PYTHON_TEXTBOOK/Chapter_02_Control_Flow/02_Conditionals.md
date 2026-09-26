# 02 - Conditionals

## Intuition: A Series of Checkpoints

Imagine a building with several access checkpoints. At the first desk, a visitor's badge is checked. If it is valid, the visitor enters. If not, the next permitted case is checked. If no rule matches, a final fallback explains that access is denied. A conditional is this policy expressed as executable logic: test a condition, run the corresponding indented block, and skip the alternatives that do not apply.

Conditionals exist because useful software must adapt to data. A fixed sequence always does the same thing; a decision allows behavior to depend on age, score, status, permission, or a system state.

## Learning Objectives

- Trace `if`, `elif`, and `else` branches in evaluation order.
- Use comparisons and Boolean expressions as conditions.
- Distinguish a decision ladder from nested decisions.
- Test boundaries and identify overlapping or unreachable conditions.
- Recognize how indentation determines the executed block.

## The Decision Ladder

- `if` begins a conditional chain and is required.
- `elif` means “else if” and is checked only when all earlier conditions in that chain were false.
- `else` has no condition and runs when every earlier condition was false.
- A colon introduces an indented suite.
- Once one branch of an `if`/`elif`/`else` ladder runs, Python skips the remaining branches in that ladder.

```text
                 +-- true --> run branch A --+
start -> test A -+                            +-> continue after ladder
                 +-- false -> test B          |
                                +-- true -> branch B
                                +-- false -> fallback else
```

## Repository Example: Grade Ladder

The following example appears in the explanatory material of `control_flow_statement/if_else_elif.ipynb`:

```python
score = 78

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")
```

| Line | Detailed behavior |
|---|---|
| `score = 78` | Binds the sample integer to `score`. |
| `if score >= 90:` | Evaluates a comparison, which produces `False` for 78. The colon begins the branch suite. |
| indented `print("Grade: A")` | Belongs to the first branch and is skipped because its condition was false. |
| `elif score >= 75:` | Runs only after the `if` test failed. The comparison is true for 78. |
| indented `print("Grade: B")` | Executes; the ladder is now complete, so later checks are not evaluated. |
| `elif score >= 50:` | Would handle scores from 50 up to, but not including, 75 because higher scores have already matched. It is skipped for 78. |
| indented `print("Grade: C")` | Executes only when its `elif` condition is true. |
| `else:` | Fallback when all three comparisons were false. |
| indented `print("Grade: F")` | Runs only for scores below 50. |

Order is essential. If `score >= 50` came before `score >= 75`, every passing score of 75 or more would match the broad condition first and incorrectly receive the lower grade. The ladder expresses priority as well as categories.

## Nested Decisions and Combined Conditions

A nested conditional is a decision inside the suite of another decision. It is appropriate when the inner test only makes sense after an outer requirement has passed. Your notebook demonstrates a ticket gate followed by an ID check:

```python
has_ticket = True
has_id = False

if has_ticket:
    print("Ticket verified. Checking ID...")
    if has_id:
        print("Welcome to the venue!")
    else:
        print("Access denied: Missing valid identification.")
else:
    print("Access denied: No ticket found.")
```

| Line or group | Explanation |
|---|---|
| `has_ticket = True` | Creates the outer gate's test value. |
| `has_id = False` | Creates the inner gate's test value. |
| `if has_ticket:` | Tests the first requirement. Only a valid ticket enters the nested block. |
| ticket message | Gives progress feedback after the ticket succeeds. |
| `if has_id:` | Evaluates the second requirement only after the outer test passed. |
| welcome message | Runs only when both checks pass. |
| nested `else` | Handles an ID failure when the ticket had succeeded. |
| outer `else` | Handles ticket failure and skips the entire inner ID check. |

If the program only needs one success action when both conditions are true, `if has_ticket and has_id:` is flatter and clearer. Use nesting when separate feedback or actions are required at each stage. Deeply nested ladders become difficult to review; refactor complicated policies into small named functions.

## Deep Dive: Truth Values and Branch Selection

A condition need not literally be `True` or `False`; Python evaluates its truth value. Empty strings and containers, numeric zero, and `None` are falsey; most other objects are truthy. Explicit comparisons are often easier for beginners and business rules because they state the test directly.

Python evaluates conditional expressions in order. It evaluates the `if` condition; if true, it executes that suite and skips associated alternatives. If false, it checks the first `elif`, then subsequent `elif` clauses until one matches or reaches `else`. Nested conditions are evaluated only if control enters the containing suite.

```text
score values:  < 50       50..74       75..89       >= 90
branch:         Grade F    Grade C      Grade B      Grade A
checks:         90? no     90? no       90? no       90? yes
                           75? no       75? yes
                                        50? not needed
```

This decision table helps verify that ranges cover expected inputs without overlap. For integer scores, also decide what happens for negative values or scores above 100; the source example assigns them to a grade unless explicit validation is added.

## Industry Scenario: Eligibility Rules

A training platform might allow enrollment only when a learner is active and meets a prerequisite, with a waitlist as a fallback. Translate the policy into named conditions, document the order, and test every combination. If several teams depend on the same eligibility rule, implement it once in a function rather than duplicating slightly different conditional ladders.

## Common Pitfalls and Recovery

- **Missing colon:** `if score >= 50` without `:` is invalid syntax.
- **Wrong indentation:** a statement at the wrong level may execute on the wrong branch or trigger `IndentationError`.
- **Overlapping ranges:** use clear inclusive bounds and test adjacent values.
- **Wrong condition order:** broad checks can make a later, more specific branch unreachable.
- **Independent `if` instead of `elif`:** multiple independent branches may all execute.
- **Input conversion failure:** `int(input(...))` can raise `ValueError` before the conditional runs.
- **Truthiness confusion:** the nonempty string `"False"` is truthy; textual Boolean input must be parsed explicitly.

Your practice notebook has an age line resembling `elif a >= 1 and a >= 11`; that conjunction does not define the intended 1-through-11 range. A correct interval is `1 <= age <= 11`. This is a logic error: the syntax is legal, but the rule is wrong. Boundary testing exposes it.

## Practice Challenges with Hints

1. Trace the grade ladder for 49, 50, 74, 75, 89, and 90. **Hint:** stop at the first true condition.
2. Add explicit validation for scores outside 0 through 100. **Hint:** place the invalid-range test before assigning a grade.
3. Create an age eligibility ladder for three age bands. **Hint:** write the ranges as a table first and make them non-overlapping.
4. Model a two-stage login check with a distinct message for unknown account versus wrong password. **Hint:** nesting is useful when the second test occurs only after the account exists.
5. Simplify nested access logic to `and`, then explain which user feedback is lost. **Hint:** compare what can be reported after each individual failure.

## Summary

Conditionals direct execution based on truth tests. `if` starts a chain, `elif` checks alternatives in order, and `else` provides the fallback. Nested decisions represent dependent checkpoints; combined conditions represent one joint test. Test boundaries, branch order, and invalid input rather than relying on a single typical example.
