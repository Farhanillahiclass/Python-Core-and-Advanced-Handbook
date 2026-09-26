# 02 - Scope and Function Design

## Intuition: Rooms and Shared Notice Boards

Imagine a building with private rooms and a shared notice board. A value created inside one room is local to that room; a notice posted at the building level can be read by rooms below. If someone creates a new local notice with the same label, it does not erase the shared one. Python's scopes work similarly: functions have local namespaces, and module-level names can be visible inside a function unless a local binding shadows them.

Scope exists to prevent every variable from colliding with every other variable. It lets functions use temporary names safely, supports reusable components, and clarifies which data a piece of code can read or change.

## Learning Objectives

- Explain local and module/global names.
- Trace shadowing when names have the same spelling.
- Describe Python's LEGB name-lookup model.
- Understand function call frames and variable lifetime at a conceptual level.
- Design functions with explicit inputs and outputs instead of hidden state.
- Explain the `if __name__ == "__main__"` guard.

## Repository Example: Global and Local Names

This is the complete script from `unithana_python/module01/complexfunction/global_local.py`:

```python
# ==========================================
# PYTHON VARIABLE SCOPE: GLOBAL VS LOCAL
# ==========================================

# 1. GLOBAL VARIABLE DEFINITION
# This lives in the main script body and can be accessed anywhere.
pizza = "Main bahar hoon (Global)"


def mera_function():
    # 2. LOCAL VARIABLE DEFINITION
    # This lives strictly inside the function boundary.
    toy = "Main andar hoon (Local)"

    print("--- Inside Function Execution ---")
    print("Local access:", toy)
    print("Global access from inside:", pizza)


def show_same_name_handling():
    # 3. IDENTICAL NAMES HANDLING
    # Python treats these as entirely separate variables.
    pizza = "This is a Local Variable with a Global Name"

    print("\n--- Testing Same-Name Shadowing ---")
    print("Inside function (local priority):", pizza)


# ==========================================
# EXECUTION / TESTING THE CODE
# ==========================================
if __name__ == "__main__":
    # Run the basic scope function
    mera_function()

    print("\n--- Outside Function Execution ---")
    print("Global access from outside:", pizza)

    # Attempting to print 'toy' here would cause a NameError:
    # print(toy)

    # Run the shadowing demonstration
    show_same_name_handling()
    print("Outside function after shadowing test:", pizza)
```

| Line or group | Explanation |
|---|---|
| banner comments | Identify the lesson; comments do not create Python values. |
| `pizza = ...` | Binds a module-level name to a string. Because it is not inside a function, it is global to this module. |
| `def mera_function():` | Defines a function and creates a local scope when called. |
| `toy = ...` | Creates a local name in that function's call. It is not available at module level. |
| first `print` | Displays a heading. |
| `print(..., toy)` | Looks up the local name and displays its value. |
| `print(..., pizza)` | The function has not assigned to `pizza`, so Python finds the module-level binding. |
| `def show_same_name_handling():` | Defines a second independent function scope. |
| local `pizza = ...` | Assignment inside this function makes `pizza` local here; it shadows the global name without changing it. |
| two prints in second function | Display a label and the local `pizza` value. |
| `if __name__ == "__main__":` | Executes the following block only when the file is run as the main program, not when imported under another module name. |
| `mera_function()` | Calls the first function; its local `toy` is created for this invocation. |
| outside heading and print | Runs in module scope and reads the original global `pizza`. |
| commented `print(toy)` | Does not execute. If uncommented, it raises `NameError` because `toy` is local to `mera_function`. |
| `show_same_name_handling()` | Calls the shadowing example. |
| final `print` | Confirms the global `pizza` was not replaced by the local assignment. |

## Deep Dive: LEGB and Call Frames

When Python resolves a name inside a function, the practical lookup order is **LEGB**:

- **Local:** names assigned in the current function.
- **Enclosing:** names in surrounding function scopes (for nested functions).
- **Global:** names at module level.
- **Built-in:** names supplied by Python, such as `len` and `sum`.

Assignment normally creates or updates a local binding inside a function. Reading a global is allowed, but rebinding a global requires `global`; rebinding an enclosing name may require `nonlocal`. These declarations are rarely needed in well-factored beginner programs. Passing values in and returning results usually makes dependencies easier to see.

```text
module namespace: pizza -> "Main bahar hoon (Global)"
        |
        +-- call mera_function():
        |       local frame: toy -> local string
        |       reads global pizza
        |
        +-- call show_same_name_handling():
                local frame: pizza -> local string (shadows global)
                module-level pizza is unchanged
```

Each function call has an execution frame that holds its local bindings and the point where execution should resume in the caller. When the call returns, the frame is no longer active. Objects referenced by that frame may remain alive if another reference still points to them; scope is name visibility, not the same thing as object lifetime.

## Function Design: Make Dependencies Visible

A function that reads and mutates a global depends on hidden state. Its output may change based on call order, tests can interfere with one another, and concurrent operations can conflict. Prefer:

```python
def add_tax(price, rate):
    return price * (1 + rate)
```

The required inputs are explicit, and the returned result can be tested. Keep user input/output at the boundary and place calculation logic in functions that receive arguments and return values.

## Industry Scenario

In a web application, module-level configuration may be shared, but request-specific values should be passed into the request handler. A mutable global holding “current user” can leak data between requests. Explicit arguments and returned values reduce accidental cross-request state and make tests reproducible.

## Common Pitfalls

- Trying to access a local name outside the function that created it.
- Assuming a local assignment updates a global of the same name.
- Using `global` to bypass an unclear function interface.
- Shadowing built-ins or imported names with local variables.
- Confusing when a name is visible with whether an object still exists.
- Running import-time code unintentionally; protect script-only execution with the main guard.
- Expecting a local mutation and a global rebinding to be the same operation. Mutating a shared list can be visible from multiple scopes even when the name is local.

## Practice Challenges with Hints

1. Trace the exact value printed by each function in the repository script. **Hint:** track the module binding separately from each local binding.
2. Rename the local `pizza` in `show_same_name_handling`; predict the final global output. **Hint:** the module name is still untouched either way.
3. Write `discounted_price(price, rate)` without a global price. **Hint:** return the calculation.
4. Uncomment the `print(toy)` line and predict the error. **Hint:** name lookup cannot find that local in module scope.
5. Import a script that contains the main guard. State which code should run on import and which should run only as a script. **Hint:** compare the value of `__name__` in each context.

## Summary

Scope controls where names are resolved. Function-local names shadow outer names; a local assignment does not rebind a global unless explicitly declared. Call frames provide temporary execution contexts, while object lifetime depends on references. Design functions around explicit parameters and return values to minimize hidden dependencies.
