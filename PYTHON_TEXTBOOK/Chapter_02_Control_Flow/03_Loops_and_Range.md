# 03 - Loops and `range`

## Intuition: Conveyor Belt and Repeating Gate

A `for` loop resembles a conveyor belt: each item arrives, the same action is applied, and the belt stops when it is empty. A `while` loop is more like a gate controlled by a sensor: as long as its condition remains true, the process repeats. The first is naturally tied to a stream of items; the second is tied to a condition that must eventually change.

Loops exist because repeating a task manually is error-prone and unmaintainable. A loop expresses repetition once, making the program shorter and allowing it to handle collections or counts that vary at runtime.

## Learning Objectives

- Choose `for` or `while` based on the source of repetition.
- Trace initialization, condition, body, update, and termination.
- Use `range(start, stop, step)` correctly.
- Explain `break`, `continue`, `pass`, and loop `else`.
- Prevent infinite loops and avoid mutating a collection unsafely during iteration.

## `for`: Iterate Over Available Items

A `for` statement requests an iterator from an iterable, gets one item, assigns it to the loop target, runs the body, and repeats until the iterator is exhausted. The iterable might be a list, tuple, string, dictionary, file, or range. The target is rebound each iteration.

The following loop appears in the teaching material of `control_flow_statement/loops_whole_for.ipynb`:

```python
fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(f"I want to eat an {fruit}")
```

| Line | Explanation |
|---|---|
| `fruits = [...]` | Creates an ordered list containing three string objects. |
| `for fruit in fruits:` | Obtains an iterator and begins requesting items. On each pass, `fruit` refers to the current item. |
| indented `print` | Runs once per item and inserts its text into the f-string. |

The wording uses “an” before every fruit, which is grammatically wrong for some items; the loop itself is correct. A polished message could use a neutral phrase such as `"Fruit: {fruit}"`.

## `range`: Generate Integer Positions

`range(stop)` begins at zero and stops before `stop`. `range(start, stop, step)` starts at `start`, advances by `step`, and excludes the stop value. A positive step moves upward; a negative step moves downward. A step of zero raises `ValueError`.

```python
for index in range(3):
    print(f"Loop count: {index}")
```

| Line | Explanation |
|---|---|
| `for index in range(3):` | Creates a range object representing 0, 1, and 2, then iterates through it. |
| `print(...)` | Displays the current zero-based index. The loop runs three times. |

A `range` is not a pre-built list of all values. It stores its start, stop, and step and computes requested integer values during iteration. Convert it with `list(range(...))` when a visible list is useful for inspection, not just to loop over the values.

## Repository Example: Two `while` Loops

This is the complete `college_work/while_loop.py` file:

```python
a = int(input("Enter value"))
b = int(input("Enter value"))
while a <= b:
    print(a)
    a += 10


c = int(input("Enter value"))
d = int(input("Enter value"))
while c <= d:
    print(c)
    c += 1
```

| Line | Explanation |
|---|---|
| `a = int(input(...))` | Prompts for text, converts it to an integer, and stores the first loop's starting value. Invalid text raises `ValueError`. |
| `b = int(input(...))` | Reads and converts the first loop's upper bound. |
| `while a <= b:` | Tests the condition before every iteration. If false initially, the loop body is skipped. |
| `print(a)` | Displays the current value. |
| `a += 10` | Increases the state variable by ten, making progress toward the condition becoming false. |
| blank lines | Separate the two examples; whitespace here has no runtime effect. |
| `c = int(input(...))` | Reads and converts the second loop's start value. |
| `d = int(input(...))` | Reads and converts its upper bound. |
| `while c <= d:` | Starts a new pre-test loop using different variables. |
| `print(c)` | Displays the current value in the second sequence. |
| `c += 1` | Advances by one per iteration. |

If the first inputs are 2 and 25, the loop prints 2, 12, and 22. The update changes `a` to 32; the next condition is false, so execution proceeds to the second input sequence. If `a` begins greater than `b`, the body runs zero times. The second loop prints every integer in its inclusive range.

## Deep Dive: Loop State and Termination

A `while` loop is a pre-test loop: condition first, body second. A safe loop has a **variant** (a value or state that changes toward termination) or an explicit exit path. To reason about it, identify:

1. **Initialization:** what state exists before the first test?
2. **Condition:** exactly when does another iteration occur?
3. **Body:** what work happens each time?
4. **Progress:** what changes so the condition may eventually become false?
5. **Exit:** can every intended path stop?

```text
initialize
    |
    v
check condition --false--> continue after loop
    |
  true
    v
execute body -> update state
    |              |
    +<-------------+
```

For a finite collection, `for` delegates exhaustion handling to the iterator protocol. For a state-controlled process, `while` makes the condition explicit but places responsibility for progress on the programmer.

## Loop-Control Statements

- `break` immediately exits the nearest enclosing loop.
- `continue` skips the rest of the current body and starts the next iteration.
- `pass` does nothing; it provides a syntactically valid placeholder.
- A loop `else` suite runs when the loop finishes without `break`. It is useful for a search that completes without finding a target.

```python
for value in range(1, 6):
    if value == 3:
        continue
    if value == 5:
        break
    print(value)
else:
    print("Search completed without break")
```

Here, `continue` skips printing 3. When the loop reaches 5, `break` exits, so the loop's `else` does not run. The printed values are 1, 2, and 4.

## Industry Scenario: Batch Processing

A data-cleaning job might scan a list of records, skip inactive records, and stop early when it finds a required identifier. Use `for` when there is a collection to consume. Use `while` for retries or an interactive menu whose end time is determined by input. Make retry limits and cancellation paths explicit so invalid input cannot trap the process forever.

## Common Pitfalls and Edge Cases

- Forgetting a `while` update creates an infinite loop.
- Updating in the wrong direction may move away from termination.
- A `continue` before the update in a `while` loop can skip that update forever.
- `range(1, 5)` produces 1 through 4, not 5.
- A negative or zero step may create an empty range or raise `ValueError`, depending on its relation to the bounds.
- Changing a list while iterating can skip elements or produce surprising behavior; build a new list or iterate over a copy.
- `break` exits only the innermost loop.
- Floating-point equality can fail as a loop stopping condition due to representation rounding.
- An input conversion error occurs before the loop begins; handle it if the interface must recover.

If a notebook cell gets stuck in an unintended infinite loop, interrupt the kernel. Then inspect the condition and update before running the cell again.

## Practice Challenges with Hints

1. Use `range` to print 2, 4, 6, 8, and 10. **Hint:** the stop is excluded; choose a stop one increment beyond the last desired value.
2. Modify the first repository loop to count by fives. **Hint:** change only the update and state the termination condition.
3. Search a list for a name and exit when found. **Hint:** put `break` inside the matching branch and use loop `else` for not found.
4. Print numbers 1-20 except multiples of three. **Hint:** use `%` with `continue`.
5. Write an input retry loop that stops after three invalid attempts. **Hint:** track attempts and ensure every path updates that counter.
6. Explain why the second `college_work` loop prints its upper bound while a `range` stop value is excluded. **Hint:** the loop condition uses `<=`; `range` uses a half-open interval.

## Summary

Use `for` to consume items and `while` to repeat while a condition holds. `range` represents an integer progression with an excluded stop. Every `while` loop needs a termination argument. Loop-control statements change the path through the nearest loop, and collection mutation should be planned rather than improvised.
