# 02 - Collections and Function Labs

## Intuition: A Filing System with Reusable Workstations

A collection is a filing system: lists keep an ordered shelf, dictionaries label folders for direct lookup, sets track unique entries, and tuples store fixed-position records. A function is a workstation that performs a repeated operation on those records. These labs combine structures and functions so choices of representation become visible in working code.

## Learning Objectives

- Navigate indexes, slices, nested records, and matrices.
- Select list, tuple, dictionary, or set based on required operations.
- Refactor repeated calculations into functions with return values.
- Test collection invariants and edge cases.

## Lab A: Nested Data and Slicing

The workspace sequence notebooks practice positive/negative indexes, slices, and nested lists. Use this small table:

```python
students = [
    ["Ali", 11, "b1"],
    ["Usman", 22, "b2"],
    ["Sara", 19, "b3"],
]
```

### Challenge

Retrieve the second student's name and roll code, then select the first two records. Explain each index layer and the excluded slice stop.

### Extension

Convert one row to a dictionary so fields can be accessed by name. Compare `student[0]` with `student["name"]` for readability and schema safety.

### Hint

The outer list index selects a row; an inner index selects a field. For `rows[:2]`, index 2 is not included.

## Lab B: Registry with Dictionary and Set

The `dictionary.py` script demonstrates `dict.update`; the variable notebook demonstrates unique skills in a set.

### Challenge

Build a course registry keyed by course code. Keep a set of unique tags for each course. Test:

- an existing code;
- an unknown code;
- a duplicate tag;
- an attempted update that collides with an existing code.

Decide whether collision means “update” or “reject” and state the policy before coding.

### Hint

Use membership (`code in courses`) to distinguish create from update. Use `.get` for expected missing keys. Sets remove duplicates, but they are not ordered lists.

## Lab C: Function and Mean

The source `function_in_python/functions_practice.ipynb` contains:

```python
def mean_of_list(numbers):
    """This function calculates the mean of a list of numbers"""
    return round(sum(numbers) / len(numbers), 2)
```

### Challenge

Add an explicit empty-input rule, then test the function with two different non-empty lists. Keep calculation in the function and printing in the caller.

### Walkthrough

| Expression | Role |
|---|---|
| `def mean_of_list(numbers)` | Declares one parameter for the collection. |
| `sum(numbers)` | Computes the total. |
| `len(numbers)` | Computes the number of elements. |
| division | Produces the arithmetic mean; empty input would divide by zero. |
| `round(..., 2)` | Returns a rounded numeric value; it does not format a string. |
| `return` | Sends the result to the caller. |

### Hint

Choose whether an empty list should raise a clear `ValueError` or return a documented alternative. Do not silently return zero unless that is mathematically and operationally correct for the use case.

## Lab D: Lambda and Transformation

The function practice notebook uses `map` to transform a list of step counts and `filter` to select product dictionaries by price.

### Challenge

Rebuild one operation as a named function first. Then compare it with a lambda-based `map` or `filter`. Test the iterator both lazily and after converting it to a list.

### Hint

Use a named function when the rule has multiple steps, domain-specific meaning, or needs a docstring. Remember that `map`/`filter` results are iterators in modern Python.

## Invariants and Collection Tests

State invariants such as:

- each row contains the same number of fields as the header;
- every course code is unique;
- a returned mean is numeric and only defined for a non-empty input;
- a registry's key agrees with the course code stored in its record.

| Case | Example test |
|---|---|
| Empty | Empty rows, empty tags, or no numbers |
| Boundary | First and last index; slice reaching the end |
| Duplicate | Repeated tag or repeated course code |
| Missing | Unknown key or invalid nested index |

## Common Pitfalls

- Miscounting nested indexes and slices.
- Assuming a set preserves insertion order.
- Allowing parallel lists or registry fields to drift out of sync.
- Using a function that prints when its caller needs a return value.
- Failing to define behavior for empty collections.
- Materializing a large lazy iterator when streaming would suffice.

## Summary and Review

Collections encode order, labels, uniqueness, and mutability. Functions make operations reusable and testable. State invariants explicitly, then exercise empty, boundary, duplicate, and missing-data cases.

1. Complete Labs A-C and add at least three tests per lab.
2. Explain one design choice you changed after testing.
3. Refactor one repeated block into a function with explicit parameters and a return value.
