# 03 - Lambdas and Higher-Order Functions

## Intuition: A Small Tool Passed Down a Line

Imagine a workshop conveyor carrying records. At one station, a small tool changes each value; at another, a gate lets through only records meeting a rule. Python's `map` and `filter` work with functions in this way. A lambda is a compact way to write a one-expression tool when giving it a full named definition would add unnecessary ceremony.

This style exists because functions are values in Python: they can be assigned, passed to another function, and called later. Higher-order functions separate the operation to perform from the traversal of the data.

## Learning Objectives

- Define and call a lambda expression.
- Explain what makes a function higher-order.
- Use `map` to transform items and `filter` to select items.
- Use a `key` function to customize ordering.
- Understand lazy iterator results and choose readability over needless brevity.

## Lambda Expressions

A lambda expression has the form `lambda parameters: expression`. It creates a function that evaluates one expression and returns its result. It cannot contain statements such as `return`, assignment, or a multi-line loop. A `def` function is usually preferable when logic has a name, documentation, branches, validation, or more than one meaningful step.

Your `functions_practice.ipynb` compares a named adder with a lambda:

```python
def user_defined(a, b):
    """Add two values."""
    return a + b

add_lambda = lambda a, b: a + b

print(user_defined(90, 90))
print(add_lambda(1, 4))
```

| Line | Explanation |
|---|---|
| `def user_defined(a, b):` | Defines a named function with two parameters. |
| docstring | Documents the operation. |
| `return a + b` | Computes and returns the sum. |
| `add_lambda = ...` | Creates an anonymous function object and binds it to the variable `add_lambda`. The parameters are `a` and `b`; the expression after the colon is returned. |
| first print | Calls the named function with arguments 90 and 90, then displays 180. |
| second print | Calls the lambda through its variable with 1 and 4, then displays 5. |

The lambda is not inherently faster or more powerful than `def`; it is merely concise syntax for a small function expression.

## `map`: Transform Every Item

`map(function, iterable)` applies the function to each item and returns an iterator in Python 3. The function does not need to be a lambda; a named function is often clearer for a meaningful transformation.

This is the complete step-conversion example from the notebook:

```python
steps = [4000, 8500, 12000, 3100]
kilometers = list(map(lambda x: round(x / 1300, 2), steps))
print(kilometers)
```

| Line | Explanation |
|---|---|
| `steps = [...]` | Creates the input list. |
| `map(...)` | Creates a lazy iterator that applies the supplied function as values are requested. |
| lambda parameter `x` | Receives one step count at a time. |
| `round(x / 1300, 2)` | Divides by the exercise's conversion factor and rounds the result to two decimal places. The factor is illustrative, not a universal measured conversion. |
| `list(...)` | Consumes the map iterator and stores its results in a new list. |
| `print(kilometers)` | Displays the transformed values. |

## `filter`: Keep Items that Match

`filter(predicate, iterable)` returns an iterator containing items for which the predicate is truthy. The original items are kept; `filter` does not transform them.

From the same notebook:

```python
items = [
    {"name": "Book", "price": 15},
    {"name": "Headphones", "price": 85},
    {"name": "Water Bottle", "price": 25},
    {"name": "Shoes", "price": 120},
]
budget_items = list(filter(lambda item: item["price"] <= 50, items))
print(budget_items)
```

Each element is a dictionary. For each item, the lambda looks up its `price` and returns whether that price is at most 50. `filter` keeps the Book and Water Bottle records. `list` consumes the iterator so the result can be displayed and revisited.

## Deep Dive: Lazy Pipelines and Higher-Order Functions

A higher-order function accepts a function as an argument or returns one. `map`, `filter`, and `sorted(key=...)` all accept callables. With `map` and `filter`, Python can defer work until the iterator is consumed, which can avoid intermediate collections. But laziness changes behavior: exceptions may arise during consumption, and an iterator is usually exhausted after one pass.

```text
source iterable -> map(transform) -> filter(predicate) -> consumer
                                                   |
                                           requests next item
```

For ordering, `sorted(records, key=lambda record: record["price"])` computes a key for each record and sorts by that key. The returned result is a new list; `sorted` does not mutate the input. Use a named key function when the rule needs explanation or reuse.

## Industry Scenario

An order-processing pipeline may normalize incoming amounts, filter records eligible for promotion, and sort options by cost. Keep the transformation and eligibility predicate independently testable. If the rule includes several conditions or must produce a reason for rejection, use a named function that can return richer information rather than a dense lambda.

## Common Pitfalls and Edge Cases

- Forgetting that `map` and `filter` return iterators rather than lists.
- Consuming a lazy iterator once, then expecting a second traversal to repeat it.
- Writing a lambda so dense that the rule becomes hard to review.
- Confusing `map` (transform each item) with `filter` (keep or discard original items).
- Capturing a loop variable in a lambda and calling it later; late binding can make all functions observe the final value unless the value is captured deliberately.
- Assuming a sample unit-conversion constant applies universally.
- Failing to decide how predicates handle missing dictionary keys or invalid types.

## Practice Challenges with Hints

1. Replace the step-conversion lambda with a named function. **Hint:** preserve the same arithmetic and return the rounded value.
2. Filter a list of course dictionaries by duration. **Hint:** the predicate should return a Boolean.
3. Sort the item records by price. **Hint:** pass a key function to `sorted`.
4. Print a `map` object without converting it, then materialize it. **Hint:** iterator representation is not its contents.
5. Decide whether an item with no `price` key should be rejected or reported. **Hint:** handle the data contract explicitly rather than hiding `KeyError`.

## Summary

A lambda is a compact one-expression function. Higher-order tools accept functions to transform, filter, or order data. `map` and `filter` are lazy iterators, so the consumer controls when the work occurs. Prefer clarity: concise code is valuable only when the rule remains easy to understand.
