# 04 - Iteration and Generators

## Intuition: A Tap, Not a Warehouse

A list resembles a warehouse in which every item is placed on shelves before a worker begins. A generator resembles a tap that produces the next item when requested. If a task needs to process one record at a time, producing values on demand can avoid storing a full result collection. The trade-off is that a generator is normally consumed in one direction and cannot be indexed or rewound.

Iteration exists as a common protocol so loops can consume many kinds of objects with the same syntax. Generators provide a convenient way to implement that protocol while retaining the function's local progress between outputs.

## Learning Objectives

- Distinguish iterable, iterator, and generator.
- Explain what happens when a generator function is called and advanced.
- Trace `yield`, `next`, and exhaustion.
- Compare eager list construction with lazy generator expressions.
- Choose generators carefully and understand one-pass, memory, and error behavior.

## Iterable and Iterator

An **iterable** can provide an iterator, often through `iter(value)`. An **iterator** produces the next item when asked, commonly through `next(iterator)`, and signals exhaustion with `StopIteration`. A list is iterable; `iter(a_list)` returns an iterator over it. A generator is both an iterator and an iterable, and returns itself from `iter(generator)`.

```text
iterable --iter(...)--> iterator --next()--> item 1
                                       --next()--> item 2
                                       --next()--> ...
                                       --exhausted--> StopIteration
```

A `for` loop automates these protocol steps. It requests the next item, assigns it to the loop variable, executes the body, then requests another. It catches the normal exhaustion signal and ends the loop. Calling `next()` directly exposes that step to the programmer.

## Repository Example: Step Through a Generator

These are the complete code cells from `python_intermaediate/generator_practice.ipynb`, shown together in notebook execution order:

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

| Line | Detailed behavior |
|---|---|
| `def count_to_three():` | Defines a function. Since it contains `yield`, calling it will create a generator rather than run the body to completion. |
| `print("Starting Machine...")` | Executes only when the generator is first advanced. It does not run at generator creation. |
| `yield 1` | Produces 1 to the caller and suspends the function at this point. |
| `yield 2` | Produces 2 when the generator resumes and advances to this statement. |
| `yield 3` | Produces 3 on the next advance; after that, the function ends. |
| blank line | Separates definition from consumption. |
| `gen = count_to_three()` | Creates the generator object and binds it to `gen`. No start message is printed yet. |
| `print(next(gen))` | Requests the first item. The generator begins, prints its start message, yields 1, then the outer `print` displays 1. |
| second `print(next(gen))` | Resumes after the first yield, obtains 2, and displays it. |

The notebook has a second code cell containing the second `print(next(gen))`. In the notebook, it works because the first cell left the generator paused after yielding 1. If the second cell is run first after a kernel restart, `gen` is undefined. If the first cell is rerun, it creates a fresh generator and rebinds `gen`.

Add a third call to get 3. A fourth call raises `StopIteration`, which means the iterator has no further values. This is normal protocol behavior, not a failure of the generator's earlier outputs.

## Deep Dive: Suspended Function State

A regular function call runs until it returns or raises. A generator function call creates a generator object; execution begins on the first request for an item. At `yield`, Python returns a value while preserving enough execution state to resume later: the instruction position, local bindings, and active generator frame. The next request continues after the previous `yield`.

```text
call count_to_three()
        |
        v
 generator object (body paused before first statement)
        |
      next()
        v
 print start -> yield 1 -> suspended
                            |
                          next()
                            v
                         yield 2 -> suspended
```

A generator does not generally store every future output, but saying it always uses constant memory is too broad. The generator frame and its retained local objects consume memory. A generator that accumulates a growing list internally can still use memory proportional to that list. Lazy generation reduces the need to materialize the entire result sequence; it does not make all workloads constant-space automatically.

## Generator Expressions and Eager Lists

Your generator notes compare list comprehensions and generator expressions. Here is the same idea with a smaller size so it can be explored safely:

```python
values = [x * 1.5 for x in range(10)]
stream = (x * 1.5 for x in range(10))
print(values[:3])
print(next(stream))
print(next(stream))
```

The square brackets construct all ten results immediately. The parentheses create a generator expression that calculates each item when requested. `values[:3]` returns a list slice, while each `next(stream)` advances the stream by one item. Both approaches are appropriate in different contexts: lists support indexing and repeated traversal; generators are suited to sequential, on-demand processing.

| Property | List | Generator |
|---|---|---|
| Evaluation | Eager: constructs all items | Lazy: computes items as requested |
| Indexing | Direct positional access | Sequential consumption; no indexing |
| Reuse | Can be traversed repeatedly | Usually exhausted after one pass |
| Memory | Proportional to stored items | Holds generator state plus current/referenced data; may be much smaller, but not guaranteed constant |
| Infinite sequence | Cannot materialize all items | Can describe an unbounded stream if consumption is bounded |

## Industry Scenario: Processing a Large Log

Suppose a monitoring tool scans a large text file and counts error records. Reading every line into a list is unnecessary if each line can be checked and discarded before the next arrives. A generator pipeline can stream lines through parsing and filtering stages. However, if a downstream stage needs to revisit records, calculate a global sort, or retry after failure, it may need buffering or a persistent checkpoint. Choose laziness to match the workflow, not as a universal speed trick.

## Common Pitfalls and Edge Cases

- Expecting the generator body to execute when the generator function is called.
- Calling `next` after exhaustion and not understanding `StopIteration`.
- Trying to use `len(generator)` or `generator[0]`; a generator does not promise a known length or random access.
- Consuming the generator once and then expecting it to contain the same items.
- Materializing an infinite generator with `list(...)`, which cannot finish.
- Assuming a generator always uses `O(1)` memory, even when it retains large objects.
- Sharing a generator between consumers that unexpectedly advance the same state.
- Treating all exceptions raised while advancing as exhaustion; only `StopIteration` is the normal end signal.

## Practice Challenges with Hints

1. Add a fourth yielded value and use a `for` loop to display all values. **Hint:** the loop consumes the same protocol as repeated `next` calls.
2. Call `next` four times on the original generator. Describe the fourth result. **Hint:** the function has only three yields.
3. Consume `stream` fully, then try to consume it again. **Hint:** the iterator retains its exhausted state.
4. Create a new generator by calling the function again. **Hint:** a new generator object starts fresh.
5. Generate squares from 0 up to a limit without storing a list. **Hint:** use a generator expression or a function containing `yield`.
6. Explain why an unbounded generator can still use increasing memory. **Hint:** inspect what objects the generator itself keeps references to.

## Summary

Iteration is a shared protocol for requesting values. Generators implement that protocol by pausing at `yield` and retaining execution state. They are lazy and typically one-pass, which can reduce eager storage, but the actual memory profile depends on retained state and consumers. Use a list when indexing or repeated traversal is needed; use a generator when sequential on-demand production fits the task.
