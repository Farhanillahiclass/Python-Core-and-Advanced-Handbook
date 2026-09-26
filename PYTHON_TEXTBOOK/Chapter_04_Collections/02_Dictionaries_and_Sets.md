# 02 - Dictionaries and Sets

## Intuition: Phone Directory and Membership Ledger

A dictionary resembles a phone directory: you look up a label (a name or account number) to find the associated value. A set resembles a membership ledger: it records which distinct items are present, without assigning each one a position. These structures exist because many problems are about lookup by identity or checking membership, not navigating by an integer slot.

## Learning Objectives

- Create, read, update, merge, and iterate over dictionaries.
- Explain key lookup, missing keys, and dictionary membership.
- Create sets, add/remove members, and use uniqueness intentionally.
- Describe hashability and expected lookup behavior.

## Dictionaries: Key-to-Value Associations

A dictionary literal uses braces and `key: value` pairs. Keys must be hashable and equality-stable while stored; strings, integers, and tuples of hashable values are common keys. Values may be any Python objects. Assigning an existing key replaces its value; assigning a new key adds an entry.

## Repository Example: Merge Two Dictionaries

This is the complete script `unithana_python/module01/complexfunction/python_data_structure/dictionary.py`:

```python
# ==========================================
# PYTHON DICTIONARY IMPLEMENTATION
# ==========================================

# 1. Defining proper dictionaries using curly braces {}
dict1 = {"ali": 45, "hasan": 55, "usman": 33, "furquan": 34}

dict2 = {5: 6, 7: 90, 2: 66, 33: 554}

# 2. Updating dict1 with the key-value pairs from dict2
dict1.update(dict2)
# 3. Printing the final merged dictionary
print("Merged Dictionary:")
print(dict1)
```

| Line or group | Detailed behavior |
|---|---|
| comment banners | Mark the script's subject; all `#` comments are ignored during execution. |
| `dict1 = {...}` | Creates a mapping from four string keys to integer values. |
| `dict2 = {...}` | Creates a second mapping whose keys and values are integers. Dictionary keys need not all have one type, although consistent key schemas are usually clearer. |
| `dict1.update(dict2)` | Iterates over the second mapping's pairs and inserts them into `dict1`. If a key collides, the incoming value replaces the existing one. |
| merge comment | Describes the update operation. |
| `print("Merged Dictionary:")` | Displays a label on its own line. |
| `print(dict1)` | Displays the resulting dictionary, containing the original entries and the added integer-key entries. |

`dict1` and `dict2` are not automatically merged into a third object: `update` mutates `dict1`. If preserving the original is important, copy first or use a merge expression to create a new mapping.

## Lookup and Safe Missing Keys

`record[key]` retrieves the value for a key and raises `KeyError` if it is missing. Use `record.get(key)` when absence is an expected possibility; it returns `None` or a supplied default. To test for a key, write `key in record`. This checks keys, not values. To search values, use `value in record.values()`.

```text
key -> hash(key) -> locate candidate entry -> equality check -> value
```

Dictionaries preserve insertion order in modern Python as a language guarantee, but they are still mappings rather than sequences: integer lookup means key lookup. Do not rely on position to express the meaning of a field.

## Sets: Uniqueness and Membership

A set stores unique hashable elements. Adding a value already present leaves the set unchanged. A set is useful for removing duplicates and testing membership, but it does not support indexing. Use `set()` to create an empty set; `{}` creates an empty dictionary.

The repository's variable notebook introduces `my_skills` as a set and then modifies it. A compact example of the same pattern is:

```python
my_skills = {"Python", "English", "Python"}
simple_set = {2, 4, 8, 7, 4, 9, 8, 67, 12}
my_skills.add("Markdown")
my_skills.remove("English")
print(my_skills)
print(simple_set)
print("Python" in my_skills)
```

| Line | Explanation |
|---|---|
| `my_skills = {...}` | Creates a set; duplicate `"Python"` collapses to one member. |
| `simple_set = {...}` | Creates a numeric set; repeated 4 and 8 appear only once in the final set. |
| `.add("Markdown")` | Adds a member if it is not already present. |
| `.remove("English")` | Removes an existing member; raises `KeyError` if absent. Use `.discard` when absence should be harmless. |
| `print(my_skills)` | Displays the members; do not depend on a particular display order. |
| `print(simple_set)` | Displays the unique values. |
| membership print | Checks whether a string is present, returning a Boolean. |

## Deep Dive: Hash Tables and Expected Complexity

Dictionaries and sets use hashing to narrow where a key/member can be found. Python calculates a hash, checks candidate entries, and uses equality to resolve collisions. Average lookup, insertion, and deletion are typically efficient (often described as expected O(1)), but pathological collisions and resizing mean the worst-case behavior is not constant-time. Hashing is an implementation aid, not an ordering rule.

Mutable lists and dictionaries are unhashable because their contents can change, which would make a stored hash location unreliable. Immutable tuples are hashable only when all their elements are hashable. The guarantee is based on the object's hash/equality behavior, not simply whether the syntax looks immutable.

## Industry Scenario

A registration system might map `course_code` to a course record and maintain a set of enrolled learner IDs. The dictionary answers “what details belong to this code?”; the set answers “is this learner enrolled?” Separate these responsibilities rather than storing a list and repeatedly scanning it when keyed access is required.

## Common Pitfalls and Edge Cases

- Assuming `key in dictionary` searches values; it searches keys.
- Using a missing `mapping[key]` without handling `KeyError`.
- Using `.remove` on a set when the member might not exist; choose `.discard` if absence is acceptable.
- Expecting a set to preserve a meaningful order or support indexing.
- Treating `{}` as an empty set; use `set()`.
- Using a list as a key or set member; it is unhashable.
- Forgetting that `dict.update` mutates the target and overwrites collisions.
- Putting a custom mutable object into a set without a sound, stable hash/equality design.

## Practice Challenges with Hints

1. Merge two course dictionaries and state what happens when keys collide. **Hint:** `update` uses the incoming value for matching keys.
2. Safely retrieve an optional phone number. **Hint:** provide a default to `.get`.
3. Check a dictionary key and then separately check a value. **Hint:** use `.values()` for the latter.
4. Deduplicate a list of tags. **Hint:** construct a set; convert back to a list only if a sequence is required.
5. Remove a possibly absent skill without raising an exception. **Hint:** use `.discard`.
6. Explain why a tuple containing a list cannot be used as a dictionary key. **Hint:** the tuple's hashability depends on its contents.

## Summary

Dictionaries associate keys with values; sets track unique membership. Both rely on hashable keys/elements and usually provide efficient lookup. Know whether an operation mutates its collection, how missing values behave, and whether order or positional access is actually required.
