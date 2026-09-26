# 03 - Modules, Packages, and Environments

## Intuition: Tool Cabinets and Workspaces

A module is like one labeled tool cabinet: it groups related tools and values in one place. A package is a larger cabinet system that organizes related modules. A Python environment is the workshop where a particular interpreter and set of installed tools are available. Having a tool in one workshop does not mean it exists in another; likewise, installing a library in one Python environment does not automatically make it importable from every terminal or notebook.

Modules and packages exist to reuse code, divide projects into meaningful units, and avoid copying the same implementation into every file. Environments exist to isolate project dependencies so that one project can use a compatible set of packages without disrupting another.

## Learning Objectives

- Distinguish module, package, standard library, and third-party library.
- Use `import`, aliases, and selected imports safely.
- Explain how Python locates and caches modules.
- Match the interpreter, package installation, and notebook kernel.
- Avoid import shadowing and uncontrolled dependencies.

## Modules, Packages, and Libraries

A **module** is an importable unit, commonly a `.py` file. A **package** organizes modules under a dotted namespace. Traditional packages commonly include `__init__.py`; namespace packages can also exist without it, so the file is not universally required. **Library** is a broader, informal term for reusable code, often composed of packages and modules.

The **standard library** ships with Python, such as `math`, `random`, `pathlib`, and `json`. **Third-party packages** are distributed separately, commonly through package indexes such as PyPI. Your data notebooks use pandas, NumPy, Matplotlib, and Seaborn.

| Item | Example | Usually needs separate installation? |
|---|---|---|
| Built-in function | `len`, `print` | No |
| Standard-library module | `math`, `pathlib` | No; included with Python distribution |
| Project module | `helpers.py` | No package installation, but it must be on the import path |
| Third-party package | `pandas`, `seaborn` | Yes, into the selected environment |

## Repository Example: Data-Library Imports

This complete group of imports appears in `python_libraries/01_importing_libraries.ipynb`:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

| Line | Explanation |
|---|---|
| `import pandas as pd` | Imports the pandas module and binds the conventional alias `pd`. |
| `import numpy as np` | Imports NumPy and binds its widely used alias `np`. |
| `import matplotlib.pyplot as plt` | Imports the plotting interface from the Matplotlib package and binds `plt`. |
| `import seaborn as sns` | Imports Seaborn and binds the conventional alias `sns`. |

The aliases are not special Python syntax; `as` binds another local name for the imported module. Consistent conventions help readers recognize libraries across notebooks and projects.

## Import Forms and Name Safety

```python
import math
from pathlib import Path
import pandas as pd
```

`import math` keeps names under the module namespace, so `math.sqrt(16)` clearly identifies where `sqrt` comes from. `from pathlib import Path` brings one selected name into the current namespace. Aliases shorten commonly used module names. Avoid `from module import *` in application code because it obscures where names originated and can overwrite existing names.

A project module might be imported using `import helpers`; its location must be reachable through Python's import search path. A file named `random.py`, `json.py`, or `pandas.py` beside a script can shadow the intended library and cause confusing imports. Use descriptive filenames that do not collide with standard-library or third-party module names.

## Deep Dive: Import Resolution and Caching

When Python executes an import, it first checks whether the module has already been loaded in the process's module cache (`sys.modules`). Otherwise, the import system searches locations described by `sys.path` and package metadata, creates a module object, executes the module code, and records the result. Importing can therefore execute top-level code once per process. Keep module-level statements focused on definitions and constants; avoid starting jobs, prompting users, or writing files merely because a module was imported.

```text
import statement
      |
check sys.modules cache
   | cached       | not cached
   v              v
reuse module   search sys.path -> load/execute -> cache
      \              /
       bind imported name in current namespace
```

This process is why the active interpreter matters: its standard library, site-packages, import paths, and module cache belong to that running process.

## Environments and Notebook Kernels

A virtual environment provides an isolated interpreter context and package-install location. The repository contains both `.venv` and `.conda` environment folders; users should select the intended one for each project workflow. The terminal's `python` command, the VS Code Python interpreter, and a notebook kernel can be different. A package may be installed correctly but still fail to import if the program runs with another interpreter.

Before diagnosing `ModuleNotFoundError`:

1. Check which interpreter is running the script or notebook.
2. Check whether the package is installed in that same environment.
3. Check whether a project file is shadowing the import name.
4. Check the spelling and capitalization of the import.

For an intentionally configured environment, installing via that interpreter's package manager helps target the correct location (for example, `python -m pip ...` after verifying `python`). Follow the project's existing environment/dependency manager rather than installing globally or into an unrelated environment.

## Industry Scenario

A data-analysis project may need pandas and Seaborn, while a small automation script uses only `pathlib` and `csv` from the standard library. Isolating environments prevents an upgrade for the data project from unexpectedly changing the automation project. A dependency file or lockfile can record package requirements so collaborators can reproduce the setup.

## Common Pitfalls and Edge Cases

- Installing a package into one environment and running another interpreter.
- Selecting a notebook kernel different from the workspace interpreter.
- Naming a project file after a module being imported.
- Using wildcard imports and creating ambiguous names.
- Assuming every package must contain `__init__.py`; namespace packages are an exception.
- Treating “library” as a strict import-system category; it is a broad ecosystem term.
- Running side effects at module import time.
- Assuming `pip list` from one shell describes packages available to every kernel.

## Practice Challenges with Hints

1. Rewrite the imports with conventional aliases and call one function from `math`. **Hint:** use module-qualified names.
2. Explain why `import pandas as pd` may succeed in a notebook but fail in a terminal. **Hint:** compare interpreters and installed environments.
3. Create a small `helpers.py` module with a function and describe how another script locates it. **Hint:** the module's directory must be importable.
4. Diagnose a local `random.py` that breaks `import random`. **Hint:** inspect the resolved module path and rename the colliding file.
5. Separate harmless module definitions from code that should run only when executing the file directly. **Hint:** use an `if __name__ == "__main__":` guard.

## Summary

Modules and packages organize reusable code; libraries group functionality; environments determine which interpreter and dependencies are available. Python imports resolve through process paths and caches, and module imports can execute top-level code. Match the environment to the project, use clear import conventions, and keep import-time behavior safe.
