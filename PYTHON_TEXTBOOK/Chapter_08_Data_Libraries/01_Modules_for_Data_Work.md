# 01 - Modules for Data Work

## Intuition: Specialist Departments in a Workshop

A data project resembles a workshop with specialist departments. One team handles numerical arrays, another organizes tables, and another prepares charts. You could build every tool yourself, but reliable libraries let you reuse tested capabilities and focus on the question. An import is the act of bringing a department's tools into the current program.

Libraries exist to reduce repeated implementation, standardize common operations, and make complex workflows accessible through consistent interfaces. Choosing a dependency still has costs: installation, version compatibility, environment management, and maintenance.

## Learning Objectives

- Describe the roles of NumPy, pandas, Matplotlib, and Seaborn.
- Read conventional import aliases and use module-qualified names.
- Distinguish an installed package from an import statement.
- Recognize when a third-party library adds value and when Python's standard library is enough.

## The Data-Library Toolkit

| Library | Main abstraction or purpose | Common alias |
|---|---|---|
| NumPy | Numerical arrays and vectorized computations | `np` |
| pandas | Labeled tabular data (`DataFrame`, `Series`) | `pd` |
| Matplotlib | General plotting framework | `plt` for `pyplot` |
| Seaborn | Statistical graphics with convenient defaults | `sns` |

The names overlap in places. Seaborn builds on Matplotlib; pandas plotting can also use Matplotlib. NumPy arrays are often used under pandas data structures. Choose based on the operation and the representation required, not merely because a project imports every common package.

## Repository Example: Import Data Libraries

This is the complete import cell from `python_libraries/01_importing_libraries.ipynb`:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

| Line | Explanation |
|---|---|
| `import pandas as pd` | Imports pandas and binds the conventional short alias `pd`. A DataFrame can then be constructed or loaded through pandas APIs. |
| `import numpy as np` | Imports NumPy as `np`, the standard community convention for array operations. |
| `import matplotlib.pyplot as plt` | Imports the pyplot interface, not the entire Matplotlib namespace under `plt`. |
| `import seaborn as sns` | Imports Seaborn as `sns`, commonly used for statistical plots and sample datasets. |

The import statements make names available; they do not load a dataset or plot anything. The packages must already be installed in the interpreter executing the code. Import errors often indicate an environment mismatch, which the previous chapter covers.

## Deep Dive: Import and Package Layers

Python imports modules into a running process. A package groups related modules; a library is a broader term for reusable capabilities. Import aliases are ordinary name bindings, not special package features. A package can be installed in an environment but still unavailable to a different Python interpreter or notebook kernel.

```text
selected interpreter
       |
       +-- standard library (ships with Python)
       +-- installed third-party packages
       +-- project modules on the import path
                    |
                    v
             `import` binds names
```

Use `import pandas as pd` for a widely recognized module alias. Use `from pathlib import Path` when a specific name is appropriate. Avoid wildcard imports because they can hide where names originated. Avoid naming files after dependencies (for example, `numpy.py`), since a local file can shadow the real module.

## Industry Scenario: Selecting a Toolchain

A small script that reads a CSV and computes a basic count may be adequately served by Python's `csv` and `collections` modules. A workflow with typed columns, grouping, missing-value analysis, Excel output, and statistical plots benefits from pandas and visualization libraries. Every extra dependency should earn its place through functionality, reliability, or maintainability.

## Common Pitfalls

- Assuming `import` installs a library; it only loads a module already available to the interpreter.
- Installing a package into one environment and running code in another.
- Treating `plt` as all of Matplotlib rather than the imported `pyplot` module.
- Assuming every project needs all four libraries.
- Shadowing a package with a same-named local file.
- Using aliases inconsistently, making examples harder to recognize.

## Practice Challenges with Hints

1. Explain the role of each imported name in the repository cell. **Hint:** identify the alias and library domain.
2. Which import would you remove from a program that only loads a DataFrame? **Hint:** retain imports that the code actually calls.
3. A notebook imports pandas successfully but a script gets `ModuleNotFoundError`. **Hint:** inspect the notebook kernel and script interpreter separately.
4. Write a sentence describing when a built-in module may be preferable to pandas. **Hint:** compare task complexity and dependencies.

## Summary

Data libraries provide specialized abstractions, but they do not replace good questions, validation, or environment management. Import only what the workflow needs, use conventional aliases, and confirm the running interpreter has the dependencies available.
