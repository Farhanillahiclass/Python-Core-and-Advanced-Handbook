# 02 - Variables, Data Types, and Memory

## Intuition: The Warehouse Label

Imagine a warehouse where each shelf contains an item and a label tells a worker how to find it. In Python, a variable name is more like the label in a lookup system than a cardboard box that permanently owns its contents: the name is bound to an object. Reassigning the name can point it at a different object; two labels can point to the same object. This mental model explains why Python variables do not have a fixed type and why mutation can be visible through multiple names.

## Learning Objectives

- Distinguish names, values, objects, and types.
- Trace assignment, reassignment, and concatenation.
- Recognize Python's core scalar and collection types.
- Explain mutability, aliasing, identity, and equality.
- Use `type()` and `id()` responsibly as inspection tools.

## Why Variables and Types Exist

A useful program has to retain facts between operations. A name lets later instructions refer to a value without repeating its literal. Types describe which operations make sense for an object: adding two integers computes a sum; concatenating two strings joins text; adding a string to an integer is not automatically meaningful.

Python is dynamically typed: names are bound at runtime, and a name may later be rebound to an object of another type. Python is not “typeless.” Each object has a type, and that type defines behavior, supported operations, and representation.

## Repository Example: Names, Concatenation, Arithmetic, Reassignment

This is the complete variable-and-reassignment section from `unithana_python/module01/basic_function.py`:

```python
# How to store data in variable
# Variable is defined as a container in which data is store
a = "Variable"
print(a)
b = "MRS"
print(b)
c = a + b
print(c)
# here we declare a and b both are variables
a1 = 55
b1 = 45
c1 = a1 + b1
print("The sum of a1 and b1 =", c1)
a2 = "ali"
b2 = "98"
print(a2 + str(b2))  # here value of b consider as string
# this program is also called Concatination program
# now we will defined the difference between local and global variables
g = "ali"
print(g)
g = 10
print(g)
# this program is called   Variable Re-declaration
```

| Line(s) | Line-by-line mechanics |
|---|---|
| first comment | Begins with `#`; Python ignores it during execution. It is for the reader. |
| second comment | Offers an introductory analogy. It is helpful, but the more precise model is name-to-object binding. |
| `a = "Variable"` | Creates a string object and binds name `a` to it. `=` performs assignment, not equality comparison. |
| `print(a)` | Evaluates the name lookup, passes the resulting string to `print`, and displays it. |
| `b = "MRS"` | Binds a second name to a second string value. |
| `print(b)` | Displays the current value referred to by `b`. |
| `c = a + b` | Looks up both names, applies string concatenation, creates the result `"VariableMRS"`, and binds `c` to it. No space is inserted automatically. |
| `print(c)` | Displays the concatenated result. |
| comment before the numeric example | Marks a conceptual section; it does not affect program state. |
| `a1 = 55` | Binds an integer object to `a1`. |
| `b1 = 45` | Binds an integer object to `b1`. |
| `c1 = a1 + b1` | Uses integer addition and binds the result, `100`, to `c1`. |
| `print("The sum of a1 and b1 =", c1)` | Passes two arguments. `print` inserts a separator space by default and displays the integer without manual string conversion. |
| `a2 = "ali"` | Binds a string to `a2`. |
| `b2 = "98"` | Binds a string containing digit characters, not the integer 98. |
| `print(a2 + str(b2))` | Calls `str` and concatenates strings. Here the conversion is redundant because `b2` is already a string; result: `ali98`. |
| concatenation comment | Describes the previous string operation. |
| scope comment | Announces a scope discussion; the final lines show reassignment rather than local/global scope. |
| `g = "ali"` | Initially binds the name `g` to a string object. |
| `print(g)` | Displays `ali`. |
| `g = 10` | Rebinds `g` to an integer object; it does not transform the old string in place. |
| `print(g)` | Displays `10`. |
| final comment | Correctly points to reassignment/rebinding; it does not demonstrate local versus global scope. |

This line-by-line distinction is useful: the name remains `g`, but the object it designates changes. A variable does not carry a permanent “string box” or “integer box” label.

## The Core Built-in Types

| Type | Example | Typical meaning |
|---|---|---|
| `str` | `"Muhammad Farhan"` | Text |
| `int` | `16`, `-101` | Whole-number quantities |
| `float` | `5.0`, `0.18` | Approximate fractional numeric values |
| `bool` | `True`, `False` | Truth values used in decisions |
| `list` | `["Ali", 11, "b1"]` | Ordered, mutable collection |
| `tuple` | `(101, "Alice", 94.5)` | Ordered, immutable sequence of references |
| `dict` | `{"name": "Ali", "age": 11}` | Key-to-value mapping |
| `set` | `{"Python", "English"}` | Unique hashable elements |
| `complex` | `7 + 8j` | Real and imaginary components |
| `NoneType` | `None` | Absence of an available value |

The repository's `variable_o1.ipynb` demonstrates `a = "ali"`, `print(a)`, and `print(type(a))`. That minimal sequence answers two questions: what object does the name currently designate, and which type governs its behavior? Use descriptive names such as `student_name` when the example grows beyond a quick experiment.

## Deep Dive: Namespaces, References, and Memory

At the language level, assignment binds a name to an object. In CPython, objects have implementation-level metadata including a type pointer and reference-management information; names in a namespace refer to those objects. Exact addresses and object sizes depend on the implementation, build, and runtime state. Do not design programs around a printed memory address.

```text
namespace (name table)
+-------------+       +-----------------------------+
| student_age | ----> | int object: value 16, type int |
+-------------+       +-----------------------------+
```

When `student_age = 17` executes, Python binds that name to the new value object. Other names that still refer to the former value are not automatically changed. This resembles changing the destination written on one warehouse label, not repainting every object with the same old label.

`id(value)` returns an identity token that is unique among simultaneously live objects in a given process. In CPython it is commonly related to an object's address, but Python code should treat it as an opaque identity number. Small integers and some strings may be reused or interned by an implementation; observing equal `id` values for some literals is not evidence that `is` is a substitute for `==`.

### Mutability and Aliasing

Immutable objects (such as integers and strings) cannot be changed in place. Operations produce or select values and rebind names. Mutable objects (such as lists and dictionaries) can change while retaining their identity. If two names refer to one mutable object, mutation through either name is visible through both.

```python
first_labels = ["Python", "Data"]
second_labels = first_labels
second_labels.append("AI")
print(first_labels)
print(first_labels is second_labels)
```

| Line | Explanation |
|---|---|
| list creation | Creates one mutable list object and binds `first_labels` to it. |
| alias assignment | Binds `second_labels` to the same list; it does not copy the list. |
| `.append(...)` | Mutates that shared list in place. |
| first `print` | Shows the mutation through the other alias too. |
| `is` expression | Tests identity; result is `True` because both names refer to one object. |

If an independent outer list is needed, use `first_labels.copy()` or `list(first_labels)`. These are shallow copies: nested mutable objects remain shared. `copy.deepcopy` can recursively copy many structures but is not always suitable or desirable for complex resources.

### Equality versus Identity

`==` asks whether two values compare equal. `is` asks whether two references designate the same object. Use `is None` for the singleton `None`; use `==` for strings, numbers, and ordinary value comparisons. Identity is primarily useful when object identity itself matters, such as checking a sentinel.

## Repository Visual References

The repository's ASCII chart is a character-encoding reference, not a diagram of Python variable memory:

![ASCII character table from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/ASCII_TAble.png)

ASCII assigns numeric codes to a limited set of characters. Modern Python `str` values represent Unicode text, so ASCII is a subset and a useful historical reference, not a complete model of all text. Encoding a string (for example, as UTF-8) produces bytes; those bytes are distinct from the original `str` object.

The repository also has an array visual:

![Array diagram from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/array.png)

Use it to picture indexed positions in an array-like sequence. It does **not** depict CPython's exact layout for names, list objects, or values. A Python list is a sequence of references to objects, and its implementation details are separate from a generic array infographic.

## Real-World Application

A student profile might bind `student_name` to text, `age` to an integer, `is_enrolled` to a Boolean, and `subjects` to a list. Types make later operations meaningful: ages can be compared numerically, names can be formatted, and subjects can be appended. A data pipeline must also account for values crossing boundaries: a form or file may supply `"16"` as text even when the program needs the integer 16.

## Common Errors and Recovery

- **String versus number:** `"98" + 2` raises `TypeError`; decide whether the data means text or a number, then convert intentionally.
- **Using `=` to compare:** assignment binds a name; `==` compares values.
- **Shadowing built-ins:** avoid names such as `list`, `str`, or `type`, which hide callable built-in objects.
- **Changing a list through an alias:** assignment does not copy a mutable object. Make a copy when independent mutation is required.
- **Using `is` for text comparison:** use `==` for value equality.
- **Assuming `id` is a permanent address:** identity tokens are only meaningful within the object's lifetime and process.
- **Empty collection type confusion:** `{}` creates a dictionary; use `set()` for an empty set.

## Practice Challenges with Hints

1. Rewrite the source names `a`, `b`, and `c` as descriptive names. **Hint:** the names should reveal that the values are text labels.
2. Predict the output of `print("A" + "B")` and `print(4 + 5)`. **Hint:** the operator acts according to operand types.
3. Add `print(type(c1))` to the source example. **Hint:** addition of two integers returns an integer.
4. Create `left = [1, 2]`, assign `right = left`, mutate `right`, and predict `left`. **Hint:** both names refer to the same mutable object.
5. Make an independent shallow copy and explain what would still be shared if the list contained nested lists.
6. Create a profile with string, integer, float, Boolean, list, tuple, dictionary, set, complex, and `None` values. Inspect each with `type()`.

### Solution Hints

- Appending through one alias changes the shared list; `left is right` reports that sharing.
- `left.copy()` creates a new outer list, but nested lists inside it remain shared.
- `None` has the type `NoneType`, and only one `None` object is used in normal Python programs.

## Summary

Variable names are bindings to objects, and types describe object behavior. Reassignment changes a binding; mutation changes a mutable object. Aliasing makes mutations visible through multiple names. `==` compares value and `is` compares identity. Treat implementation-specific memory details as explanations, not as portable contracts.
