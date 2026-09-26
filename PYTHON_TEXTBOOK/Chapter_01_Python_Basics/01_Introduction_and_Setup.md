# 01 - Introduction and Setup

## Start Here: Python as a Workshop

Imagine a workshop whose machines understand only a precise instruction card. A Python program is that card: each statement specifies an operation, and Python's interpreter carries it out. If the instructions say to display a greeting and then a plan, the workshop performs those actions in order. A typo in the instruction can prevent it from starting; a sound instruction that uses the wrong value can run but produce the wrong result.

This distinction explains why programming requires more than memorizing syntax. We need a model of **source code** (the instructions we write), **execution** (how a Python process interprets them), and **observable behavior** (output, changed data, or files produced).

## Learning Objectives

By the end of this topic, you can:

- Explain the roles of Python source, the interpreter, and program output.
- Run a short program as a script and in a notebook code cell.
- Distinguish a notebook's code cells from Markdown cells.
- Predict sequential output and diagnose basic syntax mistakes.
- Set up the workspace's Python interpreter and notebook kernel consistently.

## Why We Use Python

A programming language gives people a structured way to express operations while leaving details of machine execution to software tools. Python's syntax aims to make many everyday operations readable. This does not make programs automatically correct: types, control flow, input, environment, and assumptions still matter. Python's ecosystem also provides libraries for automation, data work, visualization, and many other domains, allowing a program to combine core language features with reusable tools.

In this course, Python starts as a way to express simple instructions and gradually becomes a way to model data, build reusable operations, and automate workflows. The same reading discipline applies to each stage: identify the inputs, follow the statements, inspect the result, and test important cases.

## The Execution Pipeline

A `.py` file contains source code. A Python implementation reads that source, checks its structure, and executes it. In CPython, source is compiled to an internal code object and evaluated by the Python virtual machine. The exact implementation is an engineering detail that can vary among Python implementations, but the language-level behavior should remain compatible.

```text
source file or notebook code cell
                 |
                 v
        Python implementation
   parse/check -> compile -> execute
                 |
                 v
       output / returned value /
           file or other effect
```

For an ordinary top-level script, statements run in order unless a control-flow construct changes that order. The interpreter does not infer the author's intention: it follows the code that is present. A syntax error can stop execution before the affected code runs. A logic error may produce output successfully while answering the wrong question.

## Three Ways to Work with Python

| Environment | Mental model | Best use |
|---|---|---|
| Interactive shell | A conversation: enter one statement, get a response, continue. | Small experiments and checking a function quickly. |
| `.py` script | An instruction sheet saved as a file and run as a program. | Repeatable tasks and code that should run from beginning to end. |
| Jupyter notebook | A lab notebook with separate explanatory and executable cells. | Lessons, data exploration, and mixed narrative/code. |

A notebook has a **kernel**, a live Python process. Running a cell sends its code to that process. Names and imported modules can remain available between cells. The execution order can therefore differ from the visual top-to-bottom order. Restarting a kernel clears its in-memory state; it does not delete the notebook's saved source cells.

### Markdown and Code Cells

A Markdown cell displays headings, prose, lists, links, images, and formatted examples. A code cell executes Python. The characters `#` have context-specific meanings: at the beginning of a Markdown cell they can form a heading, while in Python code they begin a comment. A Markdown heading such as `# First Program` should not be pasted into a Python code cell unless it is meant to be a comment.

## Set Up Your Workspace

This workspace already contains Python environments and Jupyter notebooks. Use the interpreter configured for the project, and make sure the notebook kernel uses the same environment when a lesson needs third-party packages.

1. Open the repository folder in VS Code.
2. Select the intended Python interpreter for the workspace.
3. Open a `.py` file and run it with that interpreter.
4. Open a notebook and confirm its selected kernel matches the environment you intend to use.
5. Keep explanatory notes in Markdown cells and executable statements in code cells.
6. When notebook results become inconsistent with the source order, restart the kernel and run the notebook from the top.

A quick check in a terminal is `python --version`. The displayed version tells you which `python` command resolved in that terminal; it does not alone prove that VS Code's notebook kernel selected the same interpreter. When behavior differs between terminal and notebook, check both selections before changing the code.

## Repository Example: First Program Messages

The following is the complete opening print section from `unithana_python/module01/basic_function.py`:

```python
print("Assalam o Alaikum Everyone,")
print("My name is Muhammad Farhan ")
print("Today  date is 27 june 2026")
print("My python journey is starting from today")
print("this is one month plan")
print("We learn python from different resources")
```

| Statement | Mechanics |
|---|---|
| `print("Assalam o Alaikum Everyone,")` | Looks up the built-in function `print`, passes one string argument, writes its text to the default output stream, and ends with a newline. |
| `print("My name is Muhammad Farhan ")` | Performs another call. The trailing space inside the quotation marks is part of the string value. |
| `print("Today  date is 27 june 2026")` | Displays the exact text, including its two spaces between `Today` and `date`. The statement is valid but a fixed date becomes stale; dynamic dates require a date/time API, which is outside this first example. |
| `print("My python journey is starting from today")` | Executes after the earlier calls because it appears later in the source. |
| `print("this is one month plan")` | Displays a fifth separate message; Python does not combine separate calls into one string. |
| `print("We learn python from different resources")` | Displays the final message in this block. |

The quotation marks delimit string literals; Python removes the syntax delimiters when it displays the contents. `print` adds a newline by default, so each call begins at the left of a new output line.

```text
statement 1 -> output line 1
statement 2 -> output line 2
statement 3 -> output line 3
      ...          ...
statement 6 -> output line 6
```

### Predict Before Running

Read each literal carefully. The third message contains double whitespace; the second message has a trailing space that is usually invisible in a terminal. This is a useful first debugging lesson: the output is determined by the characters in the value, not by what the author meant to type.

## Run and Inspect

For a script, save Python statements in a `.py` file, then run that file with the selected interpreter. For a notebook, place statements in a code cell and execute that cell. In either environment:

1. Read the code before running it.
2. Predict the output.
3. Execute it.
4. Compare the actual output to the prediction.
5. Make one small change and repeat.

When Python reports `SyntaxError`, inspect the source location and nearby punctuation. Missing quotes, unmatched brackets, and malformed expressions are frequent first causes. Do not treat every error as a syntax issue: a valid program can still fail at runtime or compute an incorrect answer.

## Industry Perspective: Logs and Reproducibility

A command-line automation tool may print a start message, progress, completion, or a warning. Those messages help an operator understand what the process reached. In a notebook, output may document an experiment. In both settings, a result is useful only when its code, input, and execution order are understandable. For reliable work, capture the actual configuration and avoid relying on hidden notebook state.

## Common Beginner Errors

- Using curly “smart quotes” rather than Python's straight quotation marks.
- Forgetting to close a string or bracket.
- Expecting the interpreter to execute a Markdown cell.
- Running notebook cells out of order and trusting stale variables.
- Assuming a successful run proves the program is correct.
- Editing output instead of the source statement that produced it.

## Practice with Hints

1. Add a seventh message about a Python goal. **Hint:** add a new `print` statement after the last one.
2. Change one message and predict exactly which output line changes. **Hint:** each call has one independent string argument.
3. Run the six-line block in a notebook code cell and as a script. **Hint:** compare the execution controls and the output destination, not the Python syntax.
4. Add a Markdown heading before the code cell. Explain why it does not execute. **Hint:** cell type determines how its contents are interpreted.
5. Remove one closing quotation mark and run the code. **Hint:** use the error location to find the malformed string, restore it, and rerun.

## Summary

Python source describes operations; an interpreter executes them. Shells, scripts, and notebooks provide different ways to submit code. Notebook kernels retain state between cell runs, so controlled execution order matters. Start with small programs, predict their output, and compare the prediction to what Python actually does.

### Reference Coverage Note

The introductory coverage here is consistent with the foundational scope indicated by the workspace's Python-learning books: source instructions, execution, and a first runnable program. The books are treated only as topic-discovery references; this explanation and its teaching example are original or drawn from the author's own script. Page-level PDF text was not available in the earlier scan, so no page-specific claims are made.
