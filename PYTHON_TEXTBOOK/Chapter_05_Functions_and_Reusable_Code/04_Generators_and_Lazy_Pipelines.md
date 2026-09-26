# 04 - Generators and Lazy Pipelines

## Intuition: Stream One Package at a Time

Imagine a fulfillment center receiving thousands of packages. One approach is to unload everything into a warehouse before processing; another is to process each package as it arrives. A generator is like the second approach: it produces a value when the caller asks for one and then pauses. This helps when sequential processing matters more than random access or repeated traversal.

Generators exist to represent potentially large, incremental, or even unbounded sequences without requiring every result to be constructed in advance. They use Python's iteration protocol, so they can be consumed by `next()` or a `for` loop.

## Learning Objectives

- Explain the iterator protocol and generator objects.
- Trace a generator function across successive `yield` statements.
- Understand suspended state, exhaustion, and one-pass consumption.
- Compare generator expressions with eager list comprehensions.
- Evaluate memory and performance claims accurately.

## The Iterator Protocol

An iterable can produce an iterator with `iter(value)`. An iterator yields its next item when asked and signals that it has no more items by raising `StopIteration`. A `for` loop handles this signal automatically. A generator function is a convenient way to create an iterator: it contains `yield` and preserves its execution state between values.

```text
iterable -> iterator -> next() -> item
                           |
                           +-- next() -> next item
                           |
                           +-- exhausted -> StopIteration
```

## Repository Example: `count_to_three`

These are the complete code cells from `python_intermaediate/generator_practice.ipynb`, shown in execution order:

```python
def count_to_three():
    print("Starting Machine...")
    yield 1
    yield 2
    yield 3

gen = count_to_three()  # Creates the generator object

print(next(gen))
print(next(gen))
```

| Line | Detailed mechanics |
|---|---|
| `def count_to_three():` | Defines a generator function because its body contains `yield`. |
| `print("Starting Machine...")` | Is part of the function body and does not execute when the generator is created. |
| `yield 1` | Returns 1 to the caller and suspends execution at this point. |
| `yield 2` | Produces the second value when the generator resumes. |
| `yield 3` | Produces the third value; the next advance reaches the end of the function. |
| `gen = count_to_three()` | Creates a generator object; it does not yet print the start message or yield a value. |
| first `print(next(gen))` | `next` resumes the generator, causing the message to print, then receives 1; the outer `print` displays 1. |
| second `print(next(gen))` | Resumes after `yield 1`, receives 2, and displays it. |

A third call returns 3. A fourth call raises `StopIteration`, which is the protocol's normal signal that the sequence is exhausted. If the second notebook cell is run after restarting the kernel without running the first cell, `gen` is undefined; if the first cell is rerun, it creates a fresh generator.

## Deep Dive: Suspended Frames and State

Calling a generator function constructs a generator object. The first request begins executing its body. At a `yield`, Python returns a value while preserving the active generator frame: local bindings and the instruction position needed to resume. The next request continues after that yield. This differs from an ordinary function's `return`, which ends that invocation.

```text
call count_to_three()
        |
        v
 generator object (body has not started)
        |
      next()
        v
 print start -> yield 1 -> pause with frame/state
                              |
                            next()
                              v
                         yield 2 -> pause
```

A generator does not normally precompute and store the full sequence. Its memory use includes the generator object, execution frame, retained local references, and whatever the consumer stores. Therefore “generators always use O(1) memory” is incorrect: a generator that accumulates an ever-growing list or retains large objects can still consume growing memory. Laziness reduces eager materialization only when the whole pipeline remains incremental.

## Generator Expressions and Eager Collections

Your generator notes compare a list comprehension with a generator expression. This smaller version demonstrates the same mechanism without allocating millions of items:

```python
values = [x * 1.5 for x in range(10)]
stream = (x * 1.5 for x in range(10))
print(values[:3])
print(next(stream))
print(next(stream))
```

| Line | Explanation |
|---|---|
| list comprehension | Computes all ten products and stores them immediately in `values`. |
| generator expression | Creates a lazy iterator recipe; values are calculated as requested. |
| `values[:3]` | Reads the first three already-stored elements and returns a new list. |
| first `next(stream)` | Computes and returns 0.0. |
| second `next(stream)` | Resumes the expression and returns 1.5. |

Use a list when you need indexing, length, or repeated traversal. Use a generator when values can be consumed sequentially and materializing all of them is unnecessary. A generator's one-pass behavior is a design constraint, not just a memory optimization.

## Pipeline Design

Generator pipelines can compose transformations without storing every intermediate result:

```text
source -> parse one record -> validate -> transform -> consume/write
```

If a consumer needs a global sort, random access, or multiple passes, it may force materialization or another storage strategy. Streaming is not automatically faster: each value still requires computation, and a simple list may be clearer and more efficient for small data.

## Industry Scenario: Log Processing

A monitoring job can read a large log incrementally, parse one line, keep only errors, and update a counter. This avoids storing every line at once. If the process crashes, however, a generator alone does not provide checkpointing or replay. Reliable pipelines need an explicit recovery strategy, such as remembering an offset or processing durable batches.

## Common Pitfalls and Edge Cases

- Expecting generator code to execute at the function call rather than first iteration.
- Advancing beyond the final `yield` without recognizing normal `StopIteration`.
- Trying to index a generator or call `len` on it.
- Reusing an exhausted generator; call the generator function again for a new stream.
- Converting an unbounded generator to a list; it will never finish.
- Assuming constant memory regardless of retained state and downstream consumers.
- Sharing one generator between consumers that advance the same state unexpectedly.
- Expecting `return` inside a generator to yield a normal item; it ends the generator (with an optional value carried by `StopIteration`).

## Practice Challenges with Hints

1. Add a fourth yielded value and consume all values with `for`. **Hint:** iteration handles exhaustion automatically.
2. Call `next(gen)` four times and describe the fourth outcome. **Hint:** there are three yield points.
3. Consume a generator, then try to consume it again. **Hint:** iterators remember their position.
4. Re-create the generator and consume it from the start. **Hint:** call `count_to_three()` again.
5. Build a generator expression for squares from 1 through 10. **Hint:** use parentheses and a `for` clause.
6. Give an example of a generator that still uses growing memory. **Hint:** consider retaining every produced item in an internal list.

## Summary

Generators implement iteration with suspended execution. `yield` produces one item and preserves the frame for resumption; exhaustion is signaled by `StopIteration`. Generator expressions defer computation, but their memory and speed advantages depend on the complete pipeline. Choose them for sequential on-demand work, not as a universal replacement for lists.
