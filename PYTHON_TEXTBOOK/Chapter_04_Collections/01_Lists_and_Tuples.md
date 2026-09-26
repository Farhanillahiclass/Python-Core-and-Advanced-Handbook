# 01 - Lists and Tuples

## Intuition: Editable Checklist and Sealed Record

A list is an editable checklist: entries have an order, and you can add, remove, or replace an item as circumstances change. A tuple is closer to a sealed record card: its positions are fixed after creation. Both preserve order and support indexing, but the choice tells a reader whether the sequence is expected to change.

These structures exist because programs frequently manage related values together. A single collection is easier to pass, traverse, count, and transform than many unrelated variables. The mutability distinction helps protect data that should remain fixed and makes intended updates explicit.

## Learning Objectives

- Create, inspect, index, iterate over, and update lists.
- Create and unpack tuples, including one-item tuples.
- Explain reference copying and nested mutability.
- Compare common operation costs and select a sequence type intentionally.

## Lists: Ordered and Mutable

A list literal uses square brackets with comma-separated elements. Lists preserve order, allow duplicates and mixed types, and support item assignment. Common operations include `append`, `extend`, `insert`, `remove`, `pop`, and slicing. Use methods that express the intended operation rather than rebuilding the collection manually.

## Repository Example: Build and Inspect Lists

This complete example cell is from `Python_101_Crash_Course_Codanic/variables/types_variables_02.ipynb`:

```python
fruits = ["apple", "banana", "cherry"]  # A list of strings
numbers = [1, 2, 3, 4, 5]               # A list of integers
mixed = ["Alice", 25, True, 4.5]        # A list with different data types
print(fruits)
print(numbers)
print(mixed)
print(type(fruits))
```

| Line | Explanation |
|---|---|
| `fruits = [...]` | Creates a list of three strings, preserving their order. The trailing comment is ignored by Python. |
| `numbers = [...]` | Creates a separate list of integers. |
| `mixed = [...]` | Creates a list containing a string, integer, Boolean, and float. Python permits mixed types, though a single-purpose homogeneous list can be easier to validate. |
| `print(fruits)` | Displays the list representation. |
| `print(numbers)` | Displays the integer list. |
| `print(mixed)` | Displays all four values and their representations. |
| `print(type(fruits))` | Reports the list object's type. |

Mutability means an existing list object can be changed:

```python
fruits[1] = "mango"
fruits.append("pear")
```

The first line replaces the value at index 1; the second adds a new final element. Both mutate the list. The previous `fruits` variable refers to that same updated list.

## Tuples: Ordered and Immutable

A tuple is an ordered sequence whose element slots cannot be reassigned after construction. Parentheses are common notation, but commas define the tuple. A one-element tuple therefore needs a trailing comma: `(7,)`; `(7)` is the integer 7 in parentheses.

Your `unithana_python/module01/complexfunction/python_data_structure/tuple.py` contains:

```python
user_profile = (101, "Alice", 94.5)
print(type(user_profile))

tup1 = ["ali", "farhan", "rehman", "reyan", "hamza"]
tup2 = [1, 2, 9, 0, 99, 190, 80, 56, 33, 23]
print(tup1[0:4])
print(tup2[2:7])
```

| Line | Explanation |
|---|---|
| `user_profile = (...)` | Creates a three-element tuple for an identifier, name, and score. |
| `print(type(...))` | Confirms that `user_profile` is a tuple. |
| `tup1 = [...]` | Despite the name `tup1`, this source value is a list because it uses square brackets. Names do not determine type. |
| `tup2 = [...]` | Also creates a list, not a tuple. |
| `print(tup1[0:4])` | Displays items at indexes 0 through 3; slice stop 4 is excluded. |
| `print(tup2[2:7])` | Displays items from index 2 up to, but not including, index 7. |

This is an excellent type-reading lesson: inspect the literal delimiters or use `type`; a variable's name may be misleading. A tuple can be unpacked when its shape is known:

```python
user_id, name, score = user_profile
```

The number of receiving names must equal the number of tuple elements unless starred unpacking is used.

## Visual Reference and Memory Model

The course array infographic illustrates ordered positions:

![Indexed array positions from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/array.png)

Use the picture to reason about “element at index i,” but do not treat it as a complete representation of a Python list. In CPython, a list is a resizable array of references to objects; the values themselves may live elsewhere. A tuple also stores references in a fixed-size sequence, but its slots cannot be reassigned.

```text
list name -> list object -> [ref A | ref B | ref C]
                                  |      |      |
                                  v      v      v
                                value  value  value
```

Indexing a list or tuple is typically constant-time in CPython. Appending to a list is amortized constant-time over many operations because occasional resizing is spread across appends; inserting at the front shifts later references and is linear-time. These are typical implementation costs, not promises for every sequence implementation.

## Aliasing, Copying, and Mutability

Assignment such as `second = first` binds a second name to the same list; it does not clone it. Mutating through either alias is visible through both. A shallow copy (`first.copy()`) creates a new outer list but shares nested mutable objects. A tuple is immutable only at its own element slots: if it contains a list, that inner list may still be mutated.

| Operation | List | Tuple |
|---|---|---|
| Preserve order | Yes | Yes |
| Update one slot | Yes | No |
| Add/remove elements in place | Yes | No |
| Support duplicates | Yes | Yes |
| Typical use | Collection expected to change | Fixed-size record or sequence |

## Industry Scenario

A task queue's pending items change as work arrives, so a list may be appropriate for simple append-and-traverse workflows. A geographic coordinate pair or fixed RGB color is naturally a tuple. If tuple fields have distinct meanings and are frequently accessed by position, a dictionary or named record may be more readable.

## Common Pitfalls and Edge Cases

- Calling a list `tup1` does not make it a tuple; the literal is `[...]`.
- A tuple literal needs a comma for one element: `(value,)`.
- `second = first` creates an alias, not a copy.
- A shallow copy does not isolate nested lists.
- A tuple containing a mutable object is not deeply immutable.
- Removing elements while iterating over the same list can skip elements; build a filtered result instead.
- Heterogeneous lists are legal, but operations may fail when elements do not support a shared operation.

## Practice Challenges with Hints

1. Add a fruit and replace one list element. **Hint:** use `append` and indexed assignment.
2. Create a tuple for a fixed course title and duration, then unpack it. **Hint:** keep the left and right element counts equal.
3. Make a one-item tuple and inspect its type. **Hint:** include a comma.
4. Assign one list to a second name, mutate it, and predict both names. **Hint:** assignment preserves the reference.
5. Create a shallow copy of a list containing another list. **Hint:** mutate the nested list and observe both outer structures.

## Summary

Lists and tuples are ordered sequences. Lists are mutable; tuples have fixed element slots. Both store references to objects, so aliasing and nested mutability matter. Choose a list for a changing collection and a tuple for a fixed positional record, while preferring named fields when positional meaning becomes hard to remember.
