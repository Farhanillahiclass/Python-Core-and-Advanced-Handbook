# 02 - Text Files, Paths, and Resource Management

## Intuition: Borrowing a Library Book

Opening a file is like checking a book out of a library. You need to identify the right shelf location, choose whether you are reading or writing, and return the resource when finished. A file object is the active handle to the open file; a path is only its address. Confusing the address with the open handle leads to errors, and choosing the wrong write mode can erase useful content.

File I/O exists because a program's in-memory values disappear when its process ends. Files let programs read inputs and persist reports, settings, and records across runs.

## Learning Objectives

- Distinguish a path string from an open file object.
- Use `with open(...)` to close resources reliably.
- Choose read, write, or append mode intentionally.
- Explain relative paths and the current working directory.
- Handle likely encoding and file-system failures.

## Repository Example: Print to a File

This complete cell is from `python_intermaediate/print_method_practice.ipynb`:

```python
with open("deomo_print.txt", "w") as file:
    print(
        "that a great ,files will make and the output of printing command print the input in that file",
        file=file,
    )
```

The line wrapping and spacing are formatted for this chapter; the operations and source text come from the original cell.

| Line | Explanation |
|---|---|
| `with open(..., "w") as file:` | Opens the relative path for writing and binds the returned file object to `file`. Mode `w` creates or truncates the target. |
| `print(...)` | Calls `print` with one string argument. |
| `file=file` | Sends the output to the open file object rather than the default terminal stream. `print` also appends a newline by default. |
| end of `with` block | The context manager closes the file, including if an exception exits the block. |

The original notebook also opens `"../deomo_print.txt"` in write mode. That path means “go to the parent of the current working directory, then use this filename”; it does not necessarily mean “parent of the notebook file.” The process's working directory determines how a relative path is resolved.

## File Modes and Consequences

| Mode | Behavior | Risk to existing content |
|---|---|---|
| `"r"` | Read text (default) | Does not replace content |
| `"w"` | Write from the beginning; create if absent | Truncates existing content |
| `"a"` | Append at end; create if absent | Preserves prior content, may duplicate repeated writes |
| `"x"` | Create a new file exclusively | Fails if a file already exists |

A program should choose a mode based on its purpose. A fresh report might use `w`; an audit trail might use `a`; a safety-sensitive output can use a temporary file and replace the destination only after successful completion.

## Deep Dive: File Objects, Encodings, and Lifetimes

The path identifies a filesystem object. `open` asks the operating system for a handle and returns a Python file object that manages buffered text or byte operations. In text mode, an encoding converts between Python strings and stored bytes. Specifying `encoding="utf-8"` makes text expectations explicit:

```python
with open("report.txt", "w", encoding="utf-8") as report:
    report.write("Status: complete\n")
```

The `with` statement uses the context manager protocol: entry acquires the resource; exit invokes cleanup even when an exception occurs. This reduces the risk of leaving files open and ensures buffered output is flushed as the handle closes.

```text
current working directory + relative path
                    |
                    v
                 open()
                    |
                    v
       file object / operating-system handle
                    |
          read, write, flush, close
                    |
             context manager closes
```

## Paths and Working Directories

A relative path is resolved from the process's current working directory, which may differ between a terminal, a VS Code run configuration, and a notebook kernel. Absolute paths identify a location from a root, but are less portable. For reusable applications, build paths from a known project or data directory rather than relying on an undocumented launch location.

Path libraries such as `pathlib` provide structured path composition. Avoid manual string concatenation with slash characters when paths must work across operating systems.

## Industry Scenario: Report Generation

A scheduled report may read a source file, transform rows, and write a new output. Before running, define whether a previous report should be replaced or archived, which encoding is expected, and what to do if the input is missing or output permission is denied. For sensitive data, minimize what is written and protect destination permissions.

## Common Pitfalls and Recovery

- Passing a filename string as `print(file=...)`; `file` requires a writable file-like object.
- Using `w` and unintentionally erasing old contents.
- Assuming `../` is relative to the source file rather than the current working directory.
- Forgetting to close a manually opened file; prefer `with`.
- Reading text with the wrong encoding or assuming every byte sequence is valid UTF-8.
- Treating `FileNotFoundError` and `PermissionError` as the same operational problem.
- Assuming a successful write means the intended file location was used; inspect the resolved path and output.

## Practice Challenges with Hints

1. Change the example to append and run it twice. **Hint:** observe whether the messages accumulate.
2. Write a report with a heading and two lines. **Hint:** use one `with` block and `write` or `print(file=...)`.
3. Explain why `print("hello", file="report.txt")` is invalid. **Hint:** compare path string with file object.
4. Open a non-existent file for reading and identify the exception. **Hint:** read mode does not create a missing file.
5. Make an output path independent of the launch directory. **Hint:** construct it from a known project/data directory with `pathlib`.

## Summary

A path names a location; a file object represents an active interaction. `with` manages its lifetime. Write mode truncates, append mode preserves existing bytes while adding content, and relative paths depend on the process working directory. Encoding, permissions, and failure handling are part of reliable file design.
