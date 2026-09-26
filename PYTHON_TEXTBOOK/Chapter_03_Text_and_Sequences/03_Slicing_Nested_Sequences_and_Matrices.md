# 03 - Slicing, Nested Sequences, and Matrices

## Intuition: Take a Portion or Open a Drawer

Indexing is like asking for one numbered seat; slicing is like reserving a continuous block of seats. Nested sequences resemble drawers inside a cabinet: first identify the outer drawer, then select an item inside it. A matrix adds a regular row-and-column layout to this nesting.

These operations exist because programs often need a portion of an ordered collection, a cell from a table, or a value buried in structured data. Explicit boundaries prevent manual loops for common extraction tasks, but they require care: the slice stop is excluded, while nested indexing follows one container layer at a time.

## Learning Objectives

- Read and write slices using `start:stop:step`.
- Explain inclusive start, exclusive stop, default bounds, and negative steps.
- Navigate nested lists and two-dimensional data.
- Build independent matrix rows and identify repeated-reference bugs.
- Compare direct indexing errors with slice boundary behavior.

## Slicing: A Half-Open Window

The general slice form is `sequence[start:stop:step]`. The selected indexes begin at `start`, advance by `step`, and stop before `stop`. The start is included when reachable; the stop is excluded. Omitting a bound selects the appropriate beginning or end for the direction of the step. A negative step walks backward.

```text
values = [10, 20, 30, 40, 50, 60, 70]
index:     0   1   2   3   4   5   6
slice [1:5]    ^----------------^
selected:       20  30  40  50   (stop index 5 is excluded)
```

Half-open ranges are useful because the number of elements in a unit-step slice is usually `stop - start` when both bounds are normalized and ordered. Adjacent slices can meet at one boundary without duplicating the boundary item.

## Repository Example: Slice a List and a Range

This complete code cell is from `Data_structure/squences_practice.ipynb`:

```python
a = [1, 2, 3, 4, 5, 6, 7]
print(a[1:-2])

b = 10
print(range(b, 550, 10))
print(list(range(b, 550, 10)))
list_range = list(range(b, 550, 10))
print(list_range[1:-2:5])
```

| Line | Explanation |
|---|---|
| `a = [...]` | Creates seven ordered integers at indexes 0 through 6. |
| `print(a[1:-2])` | Starts at index 1 (value 2), stops before index -2 (index 5, value 6), and displays `[2, 3, 4, 5]`. |
| `b = 10` | Stores the starting value for the progression. |
| `print(range(...))` | Displays a range object's representation, not the full sequence of values. |
| `print(list(range(...)))` | Materializes the finite progression as a list for visible inspection. |
| `list_range = ...` | Stores the same integer progression in a list for subsequent slicing. |
| final `print(...)` | Starts at list index 1, excludes index -2, and advances five positions each time. The selected values are 20, 70, 120, and so on through 520. |

For `range(10, 550, 10)`, values run from 10 through 540; the stop 550 is excluded. Its list has 54 items. Negative index `-2` is the item 530; a slice ending there excludes it, so the last available selected value can be 520.

## Defaults, Reversal, and Safe Bounds

Examples:

| Expression | Meaning |
|---|---|
| `items[:3]` | From the beginning up to, but not including, index 3 |
| `items[2:]` | From index 2 through the end |
| `items[::2]` | Every second item |
| `items[::-1]` | A reversed copy of the sequence |
| `items[-4:-1]` | A range near the end, excluding index -1 |

A slice whose bounds exceed sequence length is clipped and normally returns the available portion (or an empty sequence). This differs from single-item access: `items[100]` raises `IndexError` if that position does not exist.

## Nested Lists and Matrix Coordinates

A nested sequence contains another sequence as an element. `records[row][column]` is evaluated in two steps: retrieve the row object from `records`, then retrieve an item from that row. The brackets are chained because each operation acts on the result of the previous one.

Your `squences_practice.ipynb` contains this complete nested-data example:

```python
a = ["ali", "ahmad", 3], ["usman", "umar", 90]
print(a[1][0])

b = [["ali", "arman", "python"], ["java", "c++", "replit"]]
print(b[0][1])
print(b[1][-1])
```

| Line | Explanation |
|---|---|
| `a = [...], [...]` | The comma-separated pair of lists forms a tuple containing two inner lists. This is subtly different from wrapping both lists in an outer list. |
| `print(a[1][0])` | Selects the second inner list, then its first item; displays `usman`. |
| `b = [[...], [...]]` | Creates an outer list containing two equal-length inner lists. |
| `print(b[0][1])` | Selects row 0, then column 1; displays `arman`. |
| `print(b[1][-1])` | Selects row 1, then its last item; displays `replit`. |

For an explicit matrix, use a list of rows:

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]
center = matrix[1][1]
print(center)
```

The outer index selects the row; the inner index selects the column. `center` receives 50. The matrix may be visualized as:

```text
             column 0   column 1   column 2
row 0           10         20         30
row 1           40         50         60
row 2           70         80         90
```

## Deep Dive: Slices and References

For built-in lists, slicing creates a new outer list containing references to the selected elements. It is a shallow copy, not a recursive duplication. If a selected element is itself mutable, the original and sliced lists may still refer to that same nested object. String and tuple slices produce new sequence values of the same immutable type.

The repository's `squence.ipynb` warns about this matrix construction:

```python
matrix = [[0, 0]] * 3
secure_matrix = [[0, 0] for _ in range(3)]
```

The first expression repeats the reference to one inner list three times. Updating one row changes the shared object, making all displayed rows appear changed. The comprehension constructs a fresh inner list on each iteration, so the rows can change independently.

```text
matrix = [[0, 0]] * 3
row 0 ----+
row 1 ----+----> one shared inner list
row 2 ----+

secure_matrix = [[0, 0] for _ in range(3)]
row 0 --------> independent list A
row 1 --------> independent list B
row 2 --------> independent list C
```

This is a reference-sharing issue, not a failure of matrix indexing. Check identity with `matrix[0] is matrix[1]` to see the difference. A shallow outer copy does not repair repeated references already inside it.

## Industry Scenario: Spreadsheet or Image Grid

A spreadsheet-like table uses row and column coordinates. A cropped image may similarly use ranges of rows and columns. Before indexing, validate that the row exists and is rectangular if the algorithm assumes equal row lengths. For user-facing coordinates that start at 1, convert to Python's zero-based index explicitly and document the conversion.

## Common Pitfalls and Edge Cases

- Assuming slice stop is included.
- Confusing the index `-2` with a positive index counted from zero.
- Using `a[0, 1]` for a nested list; use `a[0][1]` unless using a specialized array library with tuple indexing.
- Expecting `len(matrix)` to count every cell; it reports the number of rows.
- Assuming every row has the same number of columns.
- Attempting to assign into an immutable inner tuple even though the outer list is mutable.
- Building rows with `[[value] * columns] * rows`, which repeats references to one row.
- Treating a slice as a deep copy.

## Practice Challenges with Hints

1. Extract the middle three elements from a seven-item list. **Hint:** the stop position is one past the last included index.
2. Return every third value from a list. **Hint:** set the slice step.
3. Reverse a string using slicing. **Hint:** use a negative step.
4. Retrieve the value in row 2, column 1 of a 3-by-3 matrix. **Hint:** subtract one if the stated coordinates are one-based.
5. Create three independent rows of four zeros. **Hint:** use a comprehension that constructs a new inner list each time.
6. Explain why changing `matrix[0][0]` after using list repetition can affect multiple rows. **Hint:** compare row identities.

## Summary

Slicing selects a half-open range with optional step; negative steps reverse direction. Nested indexing applies one index per container layer. A two-dimensional list uses outer indexes for rows and inner indexes for columns. Slices are shallow for nested mutable elements, and repeated-list construction can alias the same row multiple times.
