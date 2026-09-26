# 01 - Operators and Expressions

## Intuition: A Workshop of Actions

Think of values as components on a workbench and operators as tools. A `+` tool joins text or adds numbers depending on the components given to it; a comparison tool checks a relationship; a logical tool combines decisions. The tool is not meaningful without its operands. A program's expression is the complete operation: values, names, and operators arranged so Python can evaluate a result.

Operators exist so programs can calculate, compare, update state, and make decisions. Understanding their behavior prevents subtle errors such as confusing assignment with equality, logical operators with bitwise operators, or identity with value equality.

## Learning Objectives

- Identify Python's arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators.
- Trace expression precedence and use parentheses to make intent clear.
- Explain short-circuit evaluation.
- Distinguish `==` from `is` and `in` from mapping-value search.
- Read and explain the repository's complete logical and membership operator scripts.

## Operator Reference

| Category | Operators | Typical result or effect |
|---|---|---|
| Arithmetic | `+ - * / // % **` | Numeric calculation, or `+` concatenation/repetition in supported types |
| Assignment | `= += -= *= /= //= %= **=` | Binds or updates a name |
| Comparison | `== != < <= > >=` | Boolean result |
| Logical | `and or not` | Short-circuiting truth-value combination |
| Identity | `is`, `is not` | Whether two references designate the same object |
| Membership | `in`, `not in` | Whether an item is contained in a container |
| Bitwise | `& | ^ ~ << >>` | Operations on integer bit patterns |

## Arithmetic, Assignment, and Comparison

For numbers, `+` adds, `-` subtracts, `*` multiplies, `/` performs true division, `//` floors a quotient, `%` returns a remainder, and `**` raises to a power. The same symbols can have type-dependent behavior: strings support concatenation with `+` and repetition with `*`. Other combinations may raise `TypeError`.

Assignment `=` binds a name to the result on the right. Augmented assignment, such as `total += amount`, combines an operation with a rebinding or in-place update, depending on the object's type and implementation. Comparisons like `score >= 75` evaluate to `True` or `False`. Python supports chained comparisons such as `10 <= score < 20`, which is equivalent in meaning to checking both linked comparisons.

## Precedence and Evaluation

Precedence determines how an expression groups when parentheses are absent. For example, multiplication is evaluated before addition:

```text
2 + 3 * 4       -> 2 + (3 * 4) -> 14
(2 + 3) * 4     -> (2 + 3) * 4 -> 20
```

Python follows a defined precedence table, but parentheses improve readability and prevent maintenance errors. For logical operators, `not` binds more tightly than `and`, and `and` binds more tightly than `or`. Prefer parentheses for mixed Boolean logic:

```python
eligible = (has_id and is_active) or has_guest_pass
```

### Deep Dive: Short-Circuiting

`A and B` does not always evaluate both operands. If `A` is false, the result is already determined, so Python skips `B`. If `A` is true, Python evaluates `B`. Similarly, `A or B` skips `B` when `A` is true. This both saves work and supports guarded expressions, but code with side effects inside expressions can become harder to reason about.

```text
A and B:  evaluate A --false--> result is false; skip B
                    \--true----> evaluate B; result follows B

A or B:   evaluate A --true----> result is true; skip B
                    \--false---> evaluate B; result follows B
```

Python's `and` and `or` may return one of their operands, not strictly a `bool`, although they are commonly used with Boolean values. In conditions, Python tests the truth value of that returned object.

## Repository Example: Logical Operators

This is the complete `logical_operator.py` script from `unithana_python/module01/complexfunction/python_data_structure/`:

```python
# ==========================================
# PYTHON LOGICAL OPERATORS: AND, OR, NOT
# ==========================================

# Dummy data for testing
has_admit_card = True
is_on_time = False

has_student_id = True
has_ticket = False

is_raining = True

# ------------------------------------------
# 1. TESTING 'and' OPERATOR (Both must be True)
# ------------------------------------------
print("--- Testing 'and' ---")
can_sit_in_exam = has_admit_card and is_on_time
print("Can sit in exam?", can_sit_in_exam)  # Will print False because is_on_time is False

# ------------------------------------------
# 2. TESTING 'or' OPERATOR (At least one must be True)
# ------------------------------------------
print("\n--- Testing 'or' ---")
can_enter_park = has_student_id or has_ticket
print("Can enter park?", can_enter_park)  # Will print True because has_student_id is True

# ------------------------------------------
# 3. TESTING 'not' OPERATOR (Inverts the value)
# ------------------------------------------
print("\n--- Testing 'not' ---")
print("Is it raining?", is_raining)
print("Is it a sunny day?", not is_raining)  # Will print False
```

### Line-by-Line Walkthrough

| Source line or group | What it does |
|---|---|
| Comment banners | Lines beginning with `#` document the sections and are ignored by Python. |
| `has_admit_card = True` | Binds a Boolean value representing one requirement. |
| `is_on_time = False` | Records a second requirement, deliberately false in this test case. |
| `has_student_id = True` | Sets up the first access credential. |
| `has_ticket = False` | Sets up an alternate credential. |
| `is_raining = True` | Sets the condition to be inverted by `not`. |
| `print("--- Testing 'and' ---")` | Displays a section label; the single quotes inside the string do not terminate its outer double-quoted literal. |
| `can_sit_in_exam = has_admit_card and is_on_time` | Evaluates both truth values as needed. Since the first is true, Python evaluates the second; `True and False` is `False`. The result is bound to a descriptive name. |
| `print("Can sit in exam?", can_sit_in_exam)` | Prints a label and Boolean with the default space separator. The trailing comment explains this test case. |
| `print("\n--- Testing 'or' ---")` | Writes a newline escape before the next section label, creating a blank line. |
| `can_enter_park = has_student_id or has_ticket` | The first value is true, so the `or` result is already true; Python short-circuits and need not evaluate the second operand. |
| `print("Can enter park?", can_enter_park)` | Displays the resulting true decision. |
| `print("\n--- Testing 'not' ---")` | Separates the third example visually. |
| `print("Is it raining?", is_raining)` | Displays the original Boolean condition. |
| `print("Is it a sunny day?", not is_raining)` | Applies logical negation; `not True` is `False`, and prints that result. |

The variable names describe the business rule, while the Boolean operators express its structure. In a real system, the variables would come from validated data rather than fixed sample values.

## Membership and Identity

`item in container` tests membership. In a list or tuple it searches for an equal element; in a string it searches for a substring; in a dictionary it tests keys by default. To search dictionary values, use `item in mapping.values()`.

The companion `membership_operator.py` is a complete compact example:

```python
search_x = 10
search_y = 5
numbers_list = [1, 2, 3, 4, 5, 6]

print("--- Testing 'in' Operator ---")
if search_x in numbers_list:
    print(f"{search_x} is available in the list.")
else:
    print(f"{search_x} is NOT available in the list.")

print("\n--- Testing 'not in' Operator ---")
if search_y not in numbers_list:
    print(f"{search_y} is NOT available in the list.")
else:
    print(f"{search_y} is available in the list.")
```

`search_x` is not present, so the first `else` executes. `search_y` is present, so the condition `search_y not in numbers_list` is false and the second `else` executes. The indentation determines which message belongs to each branch.

Use `==` to compare values, for example `first_name == second_name`. Use `is` for object identity, most notably `value is None`. Two separately created strings may be equal but are not guaranteed to be the same object. Identity is not a faster or stronger spelling of equality.

## Bitwise Operators

Integers can be viewed as binary bit patterns. `&`, `|`, and `^` combine corresponding bits; `~` complements bits; `<<` and `>>` shift bits. These operators are useful for flags, masks, compact protocols, and low-level work. They are not replacements for `and` and `or`: their precedence and operand behavior differ. Parenthesize bitwise expressions when combining them with comparisons.

## Industry Scenario

Access rules often combine conditions: an account must be active **and** have a required role, or an approved guest pass must be present. Use names that mirror the policy, and test combinations such as both false, exactly one true, and both true. A truth table exposes overlooked cases:

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

## Common Pitfalls and Edge Cases

- Confusing `=` (assignment) with `==` (comparison).
- Using `is` for strings or numbers instead of `==`.
- Assuming `in` searches dictionary values rather than keys.
- Confusing logical `and`/`or` with bitwise `&`/`|`.
- Misreading precedence in mixed expressions; add parentheses.
- Assuming `and`/`or` always return a Boolean.
- Forgetting that `%` is remainder for numbers but a formatting operator in older string formatting.
- Comparing incompatible types with `<` or `>` and receiving `TypeError`.

## Practice with Hints

1. Add a Boolean for `is_registered`; allow entry only when the learner has an ID and is registered. **Hint:** use `and` and give the expression a descriptive name.
2. Change the values in the source script and predict all three decisions. **Hint:** trace each operand before running.
3. For a dictionary `profile`, test for key `"age"`, then test for a value `18`. **Hint:** use `.values()` for the second search.
4. Evaluate `5 + 2 * 3`, then add parentheses to make addition happen first. **Hint:** multiplication precedes addition.
5. Write a short-circuit guard for a nonempty string before accessing its first character. **Hint:** put the emptiness check on the left side of `and`.

## Summary

Operators transform values and express relationships. Precedence controls grouping, parentheses make intent clear, and logical operators short-circuit. Membership checks depend on the container type. Equality compares values; identity compares references. Choose operators according to the concept being expressed, not because their symbols look similar.
