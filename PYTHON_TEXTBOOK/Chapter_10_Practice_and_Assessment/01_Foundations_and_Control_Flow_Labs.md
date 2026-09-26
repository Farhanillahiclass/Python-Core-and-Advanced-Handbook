# 01 - Foundations and Control-Flow Labs

## Intuition: Practice as a Flight Simulator

A pilot does not wait for an emergency to practice reading instruments. Small, repeatable drills let a learner predict outcomes and correct mistakes while the cost is low. These labs do the same for Python: each task isolates a concept, then adds an edge case before it becomes part of a larger program.

## Learning Objectives

- Practice output, variables, conversion, operators, conditions, and loops.
- Predict behavior before running code.
- Test boundaries and invalid input instead of relying on one happy path.
- Explain what a test proves and what remains untested.

## Lab Routine

For each exercise, use this cycle:

```text
requirement -> test cases -> prediction -> implementation
      ^                                      |
      +----------- review and refine <--------+
```

Write examples before implementation. Include one typical input, one boundary, and one invalid or unusual input. After running the code, record whether the behavior matches the requirement and why.

## Lab A: Output and Values

The introductory script `unithana_python/module01/basic_function.py` prints a set of messages and then demonstrates strings, integers, addition, concatenation, and reassignment.

### Challenge

Create a short status report with a title, a learner name, a number of completed tasks, and an active/inactive Boolean. Print the values in a readable format. Then change one value and predict what changes.

### Skills exercised

- `print` calls and f-strings;
- strings, integers, Booleans, and `type`;
- assignment and reassignment;
- descriptive names and whitespace in output.

### Test ideas

Try zero completed tasks, all tasks completed, a name with spaces, and both Boolean states. Keep the label separate from the value so the output remains clear.

## Lab B: Conversion and Decision Boundaries

The course's age/eligibility notebook uses input, integer conversion, and an `if`/`elif` chain. One source condition uses `age >= 1 and age >= 11`, which does not represent the intended interval 1 through 11. Repairing it is part of this lab: valid syntax can still encode an incorrect rule.

### Challenge

Define age categories with explicit, non-overlapping ranges, reject nonnumeric input, and test values just below, at, and above each boundary.

| Test | Why it matters |
|---|---|
| One below a threshold | Finds gaps and lower-bound errors |
| Exactly on the threshold | Checks inclusive/exclusive intent |
| One above a threshold | Finds overlaps and wrong branch order |
| Text instead of digits | Tests conversion and validation behavior |

### Hint

Write the category intervals as a table first. Validate conversion before comparing; then use chained comparisons such as `12 <= age <= 17`.

## Lab C: Loop Mechanics

The repository file `college_work/while_loop.py` has two input-driven loops. The first increments by ten while `a <= b`; the second increments by one while `c <= d`.

### Challenge

Predict the output for start 2 and upper bound 25 in the first loop. Then adapt the loop to use a caller-selected positive step. Explain what happens if the initial start is already greater than the bound.

### Hint

A `while` loop tests before its body. Track the loop variable on paper and ensure each continuing path changes it toward termination. Check that the chosen step cannot be zero or move away from the end condition.

## Lab D: Operator Truth Table

Use the variables from `logical_operator.py`: `has_admit_card = True`, `is_on_time = False`, `has_student_id = True`, `has_ticket = False`, and `is_raining = True`.

Predict `and`, `or`, and `not` outcomes before running. Then vary one fact at a time and list the resulting policy decision. Explain when short-circuiting means Python does not need to evaluate the second operand.

## Assessment Rubric

| Criterion | Beginning | Proficient |
|---|---|---|
| Correctness | Handles only the sample input | Passes normal and boundary tests |
| Explanation | Describes syntax only | Explains state changes and branch choices |
| Robustness | Lets conversion errors stop the program | Validates or handles invalid input clearly |
| Readability | Uses opaque names and unclear spacing | Uses descriptive names and consistent output |

## Common Lab Pitfalls

- Changing code before writing an expected result.
- Testing only one value in a conditional range.
- Comparing text input directly to numbers.
- Writing a `while` condition with no progress update.
- Confusing `=` with `==` or logical operators with bitwise operators.

## Summary and Review

Foundational fluency comes from tracing, testing, and explaining code. Use small cases to understand behavior, then add boundaries and invalid inputs. Correctness includes whether the program implements the intended rule, not merely whether it runs.

1. Complete one lab without looking at its previous implementation.
2. Write three tests before running the solution.
3. Keep a short record of prediction, actual output, and one correction.
