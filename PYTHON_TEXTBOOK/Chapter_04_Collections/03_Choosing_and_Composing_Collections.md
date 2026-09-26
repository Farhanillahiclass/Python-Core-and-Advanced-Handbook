# 03 - Choosing and Composing Collections

## Intuition: Choose the Right Container for the Job

Organizing a workshop involves different storage: a numbered tray for ordered parts, a labeled cabinet for direct lookup, and a sign-in ledger for unique membership. Python collections serve similarly distinct roles. Choosing the wrong one makes code awkward: searching a list for every lookup, using tuple positions without documenting their meaning, or expecting a set to preserve order all add risk.

This topic combines the earlier list, tuple, dictionary, and set lessons. The goal is to choose based on required operations, constraints, and data meaning rather than on which literal syntax looks most familiar.

## Learning Objectives

- Select a collection based on ordering, mutability, uniqueness, and lookup needs.
- Compose nested structures to model records and tables.
- Recognize the maintenance risk of parallel lists and undocumented tuple positions.
- State and check invariants for a collection-backed model.
- Compare approximate performance trade-offs without treating them as absolutes.

## A Selection Framework

Ask these questions before choosing:

1. Does order carry meaning?
2. Must the collection change after creation?
3. Are duplicates meaningful or forbidden?
4. Will access be by numeric position or a named key?
5. Is membership testing a frequent operation?
6. Will the structure contain nested mutable objects?

| Need | Likely fit | Why |
|---|---|---|
| Ordered items that change | `list` | Index, append, replace, and remove |
| Fixed positional record | `tuple` | Ordered slots that cannot be rebound |
| Named lookup or record fields | `dict` | Connects semantic keys to values |
| Uniqueness and membership | `set` | Automatically stores distinct hashable members |
| Rows in order | `list` of records | Preserves row order and supports traversal |
| Stable unique course IDs | `dict` keyed by ID | Direct key-based lookup and collision policy |

## Repository Example: Parallel Labels and Rows

Your beginner type notebook builds a table from parallel lists. This complete excerpt is adapted from its column and row examples:

```python
columns = ["Name", "Age", "Roll_No"]
row_ali = ["Ali", 11, "b1"]
row_usman = ["Usman", 22, "b2"]

print(columns)
print(row_ali)
print(row_usman)
print(row_ali[0])
```

| Line | Explanation |
|---|---|
| `columns = [...]` | Stores the meaning of each field by position. |
| `row_ali = [...]` | Stores values whose positions are expected to align with `columns`. |
| `row_usman = [...]` | Adds another row using the same position convention. |
| `print(columns)` | Displays the field order. |
| `print(row_ali)` | Displays one positional record. |
| `print(row_usman)` | Displays another positional record. |
| `print(row_ali[0])` | Retrieves the value at position zero, which readers must know corresponds to the `Name` column. |

This design is useful for teaching tables, but it relies on a hidden invariant: every row must use the exact same field order and number of fields. If a new field is inserted into `columns` but not each row, positions stop agreeing. A reader must also remember what `row_ali[1]` means.

## Compose Named Records

A list of dictionaries preserves record order while making each field self-describing:

```python
students = [
    {"name": "Ali", "age": 11, "roll_no": "b1"},
    {"name": "Usman", "age": 22, "roll_no": "b2"},
]

for student in students:
    print(student["name"], student["age"], student["roll_no"])
```

The outer list answers “which records and in what order?” Each inner dictionary answers “what value belongs to this field name?” This is one common composition pattern, not the only one. A tuple may be clearer for a stable, fixed-size record; a class or data class may be clearer when validation and behavior accompany the data.

```text
students (list; row order)
  +--> student 0 (dict) -- "name" --> "Ali"
  |                    -- "age" ----> 11
  +--> student 1 (dict) -- "name" --> "Usman"
                       -- "age" ----> 22
```

## Deep Dive: Invariants and Trade-offs

An invariant is a condition that should remain true throughout the program. For the parallel-list table, an invariant might be:

```text
len(columns) == len(each row)
```

For a dictionary-backed course registry, a useful invariant could be that every dictionary key matches the record's stored course code. For a set of identifiers, the invariant is that each identifier appears once.

| Operation | List | Tuple | Dictionary | Set |
|---|---|---|---|---|
| Index by position | Typically O(1) | Typically O(1) | Not positional | Not supported |
| Find a value by scan | Typically O(n) | Typically O(n) | Values scan O(n) | Membership expected O(1) |
| Key lookup | Manual scan unless indexed | Manual scan | Expected O(1) | Membership expected O(1) |
| Add/remove | Flexible, some shifts | Create a new tuple | Key insertion/deletion | Member insertion/deletion |
| Duplicates | Allowed | Allowed | Keys unique | Members unique |

These are broad typical costs for built-in implementations, not absolute guarantees. A list can be a better choice than a dictionary when order and iteration dominate and searches are rare. A set is not a replacement for a list when duplicate counts or stable positions matter.

## Industry Scenario: Course Registration

A course-registration service could store displayed courses in a list to preserve catalog order, map course codes to details in a dictionary for direct lookup, and use a set for a learner's enrolled course codes. Each structure serves a different access pattern. Define what should happen on duplicate enrollment, unknown course code, and removed course before writing the update logic.

## Common Pitfalls and Edge Cases

- Parallel lists can drift out of sync when one is changed alone.
- Tuple positions are compact but can become opaque when records grow.
- A list of dictionaries permits inconsistent fields unless validation checks them.
- A set silently removes duplicates; this is wrong if duplicate counts carry meaning.
- Dictionary insertion order does not turn key access into positional access.
- Nested mutable values can be shared through shallow copies.
- Choosing a hash collection requires hashable keys and stable equality semantics.

## Practice Challenges with Hints

1. Model three ordered books, each with title and price. **Hint:** use a list of dictionaries if title/price names matter.
2. Maintain a unique set of completed courses. **Hint:** decide whether repeated completion should be ignored or reported.
3. Compare a tuple student record with a dictionary student record. **Hint:** consider how a reader finds the age field.
4. Write a function or check that detects row lengths inconsistent with a list of column labels. **Hint:** compare each row length against `len(columns)`.
5. Pick structures for ordered search results, ID-to-profile lookup, and unique permission flags. Explain each choice.

## Solution Hints

- Preserve order with a list; use an inner dictionary for named fields.
- If order is irrelevant and duplicates must disappear, use a set.
- If a field name should be visible at the access site, dictionary lookup such as `student["age"]` is more descriptive than `student[1]`.
- Before mutating a composed structure, state the invariants and validate them at the boundary.

## Summary

Collections are representations chosen for operations and meaning. Lists preserve a changeable order, tuples represent fixed ordered values, dictionaries associate keys with values, and sets enforce uniqueness. Composition lets a program model tables and registries, but invariants and nested references must be kept consistent.
