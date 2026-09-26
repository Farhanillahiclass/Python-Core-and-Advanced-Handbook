# 02 - Sequence Model and Indexing

## Intuition: Numbered Seats on a Train

Imagine a train with cars in a fixed order. A seat label lets you go directly to a position; counting all seats tells you the train's length. Python sequences work similarly: they preserve order, support a length, and let you select elements by an integer index. Python numbers positions from zero, while negative indexes count back from the end.

Sequences exist because order is meaningful in many tasks: a sentence has character order, a playlist has track order, and a row of measurements has positional meaning. A sequence provides a common interface for retrieving, traversing, and combining ordered items.

## Learning Objectives

- Define the common behavior of a sequence.
- Use `len`, positive and negative indexes, and membership correctly.
- Distinguish sequence access from dictionary key lookup and set membership.
- Explain indexing cost for common built-in sequences without overgeneralizing.
- Trace the repository's complete length and indexing examples.

## What Makes a Sequence?

Built-in sequences such as strings, lists, and tuples are ordered, support integer indexing, and have a length. They differ in element type and mutability: strings and tuples are immutable; lists are mutable. `range` is another immutable sequence type, useful for integer progressions without immediately constructing a list.

Not every container is a sequence. A dictionary associates keys with values, and a set represents unique membership. Neither promises positional access through integer indexes. In a dictionary, `record[0]` means “look up key `0`,” not “give me the first item.”

## Length Versus Index

`len(sequence)` reports the number of top-level elements. If a list contains another list, the nested list counts as one item at the outer level. For an ordinary non-empty sequence of length `n`, valid positive indexes are `0` through `n-1`; valid negative indexes range from `-n` through `-1`.

```text
sequence:    [ P ][ y ][ t ][ h ][ o ][ n ]
positive:      0    1    2    3    4    5
negative:     -6   -5   -4   -3   -2   -1
length: 6
```

The first index is zero, but the length is one for a one-element sequence. That difference is the source of many off-by-one mistakes.

## Repository Example: Length Across Types

This complete code cell is from `Data_structure/squences_practice.ipynb`:

```python
a = [768, 7.8, "ali"]
print(len(a))
b = "Squences"
print(len(b))
c = (9, 44, 20)
print(type(c))
print(len(c))
```

| Line | Explanation |
|---|---|
| `a = [...]` | Creates a list with three top-level elements of different types. |
| `print(len(a))` | Calls `len` on the list; result is `3`. It does not count characters inside `"ali"`. |
| `b = "Squences"` | Creates a string. The source spelling is retained as written. |
| `print(len(b))` | Counts code points in the string; result is `8`. |
| `c = (...)` | Creates a three-item tuple. Commas make it a tuple. |
| `print(type(c))` | Displays that `c` has type `tuple`. |
| `print(len(c))` | Counts three top-level tuple items. |

## Repository Example: Forward and Reverse Indexing

From the same notebook:

```python
a = "pakistan"
print(a[1])
print(a[-1])

b = "what is the defination of range"
print(b[9])
print(b[-6])
```

| Line | Explanation |
|---|---|
| `a = "pakistan"` | Creates an eight-code-point string. |
| `print(a[1])` | Retrieves the second character, `a`, because indexing begins at zero. |
| `print(a[-1])` | Retrieves the final character, `n`. |
| `b = ...` | Creates a longer string containing spaces as ordinary positions. |
| `print(b[9])` | Retrieves the character at positive index 9. |
| `print(b[-6])` | Retrieves the sixth position counted from the end. It may be a space; printing a space can look like a blank result. |

Use `repr(b[-6])` when debugging invisible characters because `repr` shows whitespace escapes or quotes around the value.

## Deep Dive: Indexing and Complexity

For built-in strings, lists, and tuples, indexing by position is typically constant time in CPython because the implementation can locate a slot directly. This does not mean every sequence in Python has constant-time indexing; other sequence implementations may have different costs. Repeatedly searching for an element by value is a different operation from retrieving by index.

Strings and tuples cannot be updated by index. Lists can:

```python
names = ["Ali", "Sara", "Zain"]
print(names[1])
names[1] = "Mina"
print(names)
```

The first lookup reads an element. The assignment changes the list's slot to refer to another object. Attempting `text[0] = "M"` on a string raises `TypeError` because the string is immutable.

The repository's array infographic may help visualize positions:

![Array positions from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/array.png)

This is a conceptual indexed-sequence visual. It does not specify the complete internal representation of Python strings, lists, or tuples.

## Membership and Sequence Operations

`value in sequence` checks whether a matching element or substring exists. It returns a Boolean. Membership in a list or tuple may examine elements one by one, so it is typically linear in sequence length. String substring search uses a specialized algorithm. Do not assume identical performance across types.

Your notebook's example `"fruit" in bazar` checks for an exact list element. In the tuple `("bisket", "juice", "ice cream", "water botal")`, `"Juice" in tuck_shop` is false because string comparison is case-sensitive.

For compatible same-kind sequences, `+` concatenates and `*` repeats. These operations create result sequences; they do not mutate an immutable operand. Concatenating a list and tuple directly is invalid because the types differ. Convert deliberately when a mixed representation is truly wanted.

## Industry Scenario: Reading a Data Row

A fixed sequence can represent fields such as `[customer_id, item_count, total]`, but consumers must remember what index 1 means. This is workable for a small, stable structure; named columns or dictionaries are clearer as the schema grows. Indexes are useful for ordered records and grids, while names are useful for self-describing fields.

## Common Pitfalls

- Using index `len(sequence)`; the final positive index is `len(sequence) - 1`.
- Confusing zero-based index with one-based human numbering.
- Forgetting that a space is a character in a string.
- Assuming nested contents contribute recursively to `len(outer)`.
- Treating a dictionary key as a sequence position.
- Searching for a substring inside a list instead of an exact element.
- Updating a tuple or string by index.
- Assuming indexing and membership have the same performance.

## Practice Challenges with Hints

1. For `values = ["red", "green", "blue"]`, predict `len(values)`, `values[0]`, and `values[-1]`. **Hint:** count items separately from indexes.
2. Inspect the first and final character of a user-provided word. **Hint:** use index `0` and `-1`, but guard against an empty string.
3. Given `nested = [1, [2, 3]]`, what is `len(nested)`? **Hint:** count only outer slots.
4. Check whether `"Python"` occurs in a message, then compare lowercase `"python"`. **Hint:** string membership is case-sensitive.
5. Explain why `mapping[0]` may be a key lookup rather than positional access. **Hint:** dictionaries are mappings, not sequences.

## Summary

Sequences preserve order and support length and index-based access. Positive positions start at zero; negative positions start at `-1` from the end. `len` counts immediate elements, not recursively nested contents. Lists are mutable; strings and tuples are not. Dictionaries and sets solve different problems and should not be treated as positional sequences.
