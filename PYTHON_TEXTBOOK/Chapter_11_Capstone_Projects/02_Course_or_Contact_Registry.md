# 02 - Course or Contact Registry

## Project Overview

This capstone builds a small registry that stores records by a unique key and supports lookup, creation, and tag membership. It combines the repository's dictionary update example, student/course records, and set-based skill practice.

## Intuition: A Library Catalog

A library catalog uses an identifier to retrieve a book record. Searching a pile of cards one by one works for a tiny collection, but a key-based mapping expresses the lookup directly. A set attached to each record can track unique categories or skills without duplicates.

## Learning Objectives

- Choose a stable dictionary key and define duplicate behavior.
- Store named record fields instead of relying on undocumented positions.
- Use a set for unique tags and define its ordering limits.
- Validate data at the registry boundary.
- Identify where persistence and privacy concerns begin.

## Project Contract

This teaching design follows these rules:

- course codes are stripped and normalized to uppercase;
- title must not be empty;
- duration is a positive integer number of months;
- duplicate codes are rejected rather than silently overwritten;
- tags are unique; display order is sorted when needed;
- missing lookup returns `None` instead of raising `KeyError`.

## Complete Registry Implementation

This is a new teaching implementation based on the repository's dictionary and set exercises:

```python
def normalize_code(code):
    return code.strip().upper()


def add_course(registry, code, title, months):
    normalized_code = normalize_code(code)
    clean_title = title.strip()
    if not normalized_code or not clean_title:
        raise ValueError("Course code and title are required.")
    if not isinstance(months, int) or months <= 0:
        raise ValueError("Duration must be a positive whole number of months.")
    if normalized_code in registry:
        return False
    registry[normalized_code] = {
        "title": clean_title,
        "months": months,
        "tags": set(),
    }
    return True


def add_tag(registry, code, tag):
    normalized_code = normalize_code(code)
    course = registry.get(normalized_code)
    if course is None:
        return False
    clean_tag = tag.strip()
    if not clean_tag:
        raise ValueError("Tag must not be empty.")
    course["tags"].add(clean_tag)
    return True


def find_course(registry, code):
    return registry.get(normalize_code(code))


courses = {}
add_course(courses, "py101", "Python Foundations", 3)
add_tag(courses, "PY101", "beginner")
add_tag(courses, "PY101", "beginner")
print(find_course(courses, "Py101"))
```

| Line or group | Explanation |
|---|---|
| `normalize_code` | Defines one normalization rule and reuses it at each boundary. |
| `.strip().upper()` | Removes surrounding whitespace and standardizes case. It does not validate the full allowed code format. |
| `add_course(...)` | Receives the registry explicitly rather than relying on hidden global state. |
| `clean_title` | Trims surrounding spaces before storing the title. |
| required-field test | Rejects empty code/title with a specific `ValueError`. |
| duration validation | Requires a positive integer. A Boolean is technically an `int` subclass in Python; stricter validation may also reject `True`/`False` explicitly. |
| duplicate membership check | Uses dictionary key membership; returns `False` for a duplicate according to the stated policy. |
| dictionary assignment | Stores a nested record under the normalized code. |
| `"tags": set()` | Creates an empty set for unique tags. |
| `add_tag` lookup | Retrieves the course or returns `False` if no record exists. |
| empty-tag check | Prevents meaningless empty tags. |
| `.add(clean_tag)` | Inserts a unique value; adding the same tag again leaves one member. |
| `find_course` | Uses `.get` so a missing key produces `None`. |
| example calls | Add one record, attempt the same tag twice, then look it up using mixed-case input. |
| final `print` | Displays a record. Set representation order should not be treated as a stable display contract. |

## Data Model and Invariants

```text
courses (dict)
  "PY101" -> {title, months, tags (set)}
  "DS110"  -> {title, months, tags (set)}
```

The registry should maintain these invariants:

- each dictionary key is normalized;
- duplicate keys follow the chosen policy;
- every duration is positive;
- each tag set contains no duplicates;
- displayed tags are sorted if deterministic order is required.

## Industry Scenario and Extensions

A small training provider could use a registry to show courses and maintain topic tags. A contact registry would require additional care: personal data should be minimized, access-controlled, and stored in an appropriate persistent system rather than committed to a public repository. A production registry also needs persistence, concurrent update strategy, schema validation, and possibly a database rather than an in-memory dictionary.

## Common Pitfalls

- Using a mutable global dictionary instead of passing the registry.
- Silently overwriting duplicates when policy says reject.
- Assuming set display order is stable.
- Accepting negative or zero duration.
- Using user-controlled values as a filename or SQL fragment without safe handling.
- Storing sensitive personal records in a demo file or public Git repository.
- Updating data in memory but failing to persist it when the process exits.

## Review Exercises

1. Change duplicate policy from reject to update and explain what fields should be merged. **Hint:** make the policy explicit and test it.
2. Add a function that returns course codes in sorted order. **Hint:** dictionary keys are iterable; `sorted` gives deterministic output.
3. Validate tag length and allowed characters. **Hint:** separate normalization from validation.
4. Design a persistence format and explain its trade-offs. **Hint:** distinguish a simple JSON demo from concurrent production storage.
5. Add tests for missing code, duplicate code, invalid duration, duplicate tag, and empty tag.

## Completion Checklist

- Registry operations have explicit inputs and outcomes.
- Duplicate and missing-record behavior is documented.
- Data invariants are tested.
- Sensitive values are not included in sample commits.
- README explains limitations of in-memory persistence.
