# 01 - Built-ins and Function Foundations

## Intuition: A Reusable Workshop Machine

Imagine a workshop with a machine for calculating a mean. You supply a tray of measurements, the machine performs a defined sequence, and it hands back one result. Once built, the same machine can process another tray without rewriting the arithmetic. A Python function plays that role: a named, reusable unit of behavior with optional inputs and an optional result.

Functions exist to reduce duplication, divide a large task into understandable units, name important operations, and make behavior easier to test. Built-in functions are tools Python supplies; user-defined functions package logic specific to a program.

## Learning Objectives

- Use common built-ins including `print`, `input`, `type`, `len`, `sum`, `min`, and `max`.
- Define and call a function using `def`.
- Distinguish a parameter from an argument.
- Use positional, keyword, and default arguments.
- Explain the difference between printing and returning a value.
- Document a function with a docstring and define its input contract.

## Built-in Functions

A function call has a name followed by parentheses: `len(values)`. Python evaluates the arguments, invokes the function, and produces a result or side effect. Common built-ins include:

| Function | Typical behavior |
|---|---|
| `print(value)` | Writes a human-readable representation to an output stream; returns `None`. |
| `input(prompt)` | Displays a prompt and returns entered text as a string. |
| `type(value)` | Returns the object's type. |
| `len(container)` | Returns the number of top-level elements or characters. |
| `sum(numbers)` | Adds numeric items from an iterable. |
| `min(values)` / `max(values)` | Find the smallest/largest item under the relevant ordering. |

The workspace's `functions_practice.ipynb` uses `sum`, `min`, `max`, and `len` on lists. These built-ins save the programmer from manually maintaining totals or scanning for extremes, while their input constraints still matter: `sum` expects compatible addable values, and `min`/`max` need a non-empty iterable unless a default is supplied.

## Anatomy of a Function

```python
def add_numbers(first, second):
    """Return the sum of two values."""
    return first + second

result = add_numbers(12, 8)
print(result)
```

| Line | Explanation |
|---|---|
| `def add_numbers(first, second):` | `def` defines a function; `add_numbers` is its name; `first` and `second` are parameter names. The colon begins the function suite. |
| docstring | The first string expression in the body documents purpose and can be read by `help`. |
| `return first + second` | Evaluates addition and sends the result back to the caller. `return` also ends this call. |
| `result = add_numbers(12, 8)` | Calls the function; the arguments 12 and 8 are bound to the parameters for this call. The returned value is assigned to `result`. |
| `print(result)` | Displays the returned integer. |

The function definition creates a callable object and binds its name; its body does not run until the function is called. This separation between definition and invocation is essential: a definition is a recipe, not an execution of every instruction inside it.

## Repository Example: Mean of a List

This complete example is from `function_in_python/functions_practice.ipynb`:

```python
def mean_of_list(numbers):
    """This function calculates the mean of a list of numbers"""
    # return the mean and round it off to 2 decimal places
    return round(sum(numbers) / len(numbers), 2)

price = [200, 300, 600, 550, 566, 1000, 2000, 3500, 2]
print(mean_of_list(price))
```

| Line | Mechanics |
|---|---|
| `def mean_of_list(numbers):` | Defines a function with one parameter, `numbers`. |
| docstring | States that the function calculates an arithmetic mean. A stronger production contract should also state the accepted data and empty-input behavior. |
| comment | Explains the intended calculation; comments do not execute. |
| `sum(numbers)` | Calls the built-in `sum` to add the values. |
| `len(numbers)` | Calls the built-in `len` to count elements. |
| division and `round(..., 2)` | Divides total by count, then rounds the result to two decimal places. |
| `price = [...]` | Creates the sample input list from the notebook. |
| `print(mean_of_list(price))` | Passes `price` as the argument, receives the result, and displays it. |

For this list, the total is 8718 and there are 9 values, giving approximately 968.67. The formula needs a non-empty numeric input; an empty list causes division by zero. A robust version should define that case rather than leaving it implicit.

## Parameters, Arguments, and Defaults

A **parameter** is a name in the function definition; an **argument** is a value supplied at the call. Positional arguments bind by order, while keyword arguments bind by parameter name:

```python
def introduce(name, age=18):
    return f"{name} is {age} years old"

introduce("Sara")
introduce(age=21, name="Zain")
```

The first call uses the default age. The second uses keywords, so order is explicit. Parameters with defaults must follow required parameters in the function signature. Avoid mutable default values such as `items=[]`: that object is created once and shared between calls. Use `None` as a sentinel and create a fresh collection inside the function when needed.

## Deep Dive: Call Frames and Return Values

At a call, Python establishes a new execution frame with local bindings for parameters and variables. The function executes until `return`, an exception, or the end of its body. A returned object becomes available to the caller; a function that reaches its end without a `return` statement returns `None`.

```text
caller: answer = add_numbers(12, 8)
                    |
                    v
frame: first -> 12; second -> 8
       evaluate first + second
                    |
                  return 20
                    v
caller resumes: answer -> 20
```

`print` and `return` solve different problems. Printing communicates with a human or output stream; returning makes a value available for further computation. The workspace mean function correctly returns its result, allowing another caller to store it or use it in a larger calculation.

## Industry Scenario

A billing service might have `calculate_subtotal`, `apply_discount`, and `format_receipt` functions. Each function should own one clear responsibility. The calculation function returns a number; the output function formats it. Separating them makes it possible to test arithmetic without capturing terminal output.

## Common Pitfalls

- Defining a function but never calling it.
- Calling before the definition has executed in the current module flow.
- Forgetting `return` and receiving `None`.
- Printing a result and expecting it to be usable by the caller.
- Passing too few, too many, or incorrectly ordered positional arguments.
- Using a mutable default parameter unintentionally.
- Calling `mean_of_list([])` and dividing by zero.
- Naming a variable `sum`, `list`, or `len`, thereby shadowing a built-in.

## Practice Challenges with Hints

1. Write `rectangle_area(width, height)` that returns an area. **Hint:** return the product; do not print inside the calculation.
2. Add a defined empty-list behavior to `mean_of_list`. **Hint:** decide whether to raise a clear `ValueError` or return a documented sentinel.
3. Call a function once positionally and once by keyword. **Hint:** preserve parameter names exactly.
4. Write a function that returns the highest score using `max`. **Hint:** state what should happen for an empty score list.
5. Create a function with a default greeting language. **Hint:** put required parameters before parameters with defaults.

## Summary

Functions name a reusable operation. Parameters receive arguments; `return` transfers data to the caller; `print` produces output. Built-ins cover common operations, while user-defined functions encode application rules. Define input contracts, edge behavior, and responsibilities so functions remain easy to reuse and test.
