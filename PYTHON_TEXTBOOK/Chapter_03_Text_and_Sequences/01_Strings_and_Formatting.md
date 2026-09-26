# 01 - Strings and Formatting

## Intuition: A Sentence on a Message Board

A string is like a message written on a sign: the characters have an order, and the sign can be read, searched, or copied. If the wording must change, you generally create a revised sign rather than reach into the existing string and replace one character. This immutability makes text behavior predictable when values are passed between parts of a program.

Strings exist because programs must represent names, messages, codes, file paths, and human-readable output. A number like 42 is useful for arithmetic; the text `"42"` is useful for displaying, searching, or preserving the exact characters. Those are different jobs, so Python gives them different types.

## Learning Objectives

- Read and write string literals using single, double, and triple quotes.
- Explain escapes, whitespace, concatenation, repetition, and immutability.
- Format mixed values with f-strings and recognize older formatting methods.
- Distinguish Unicode text (`str`) from encoded bytes.
- Use the repository's ASCII reference accurately and understand its limits.

## Creating and Reading Strings

A string literal is text enclosed by matching quotes. Single and double quotes are interchangeable for many literals; choose the delimiter that avoids unnecessary escaping. Triple quotes can preserve line breaks in a multiline literal. Backslash escapes include `\n` (newline), `\t` (tab), and `\\` (a literal backslash).

```python
message = "Python is readable."
multiline = """First line
Second line"""
print(message)
print(multiline)
```

The name `message` refers to a `str` object. `print` displays its characters, not its quotation delimiters. The newline embedded in `multiline` is part of the string value and separates its displayed lines.

## String Operations

Strings support sequence operations. `len(text)` counts code points in the string, `text[index]` retrieves one position, `part in text` checks for a substring, `left + right` concatenates, and `text * count` repeats. `+` does not insert a space automatically.

Your `squences_practice.ipynb` joins a first and last name this way:

```python
first_name = "Muhammad "
second_name = "Farhan"
print(first_name + second_name)  # string + string
```

| Line | Explanation |
|---|---|
| `first_name = "Muhammad "` | Binds a string ending in a space; that trailing space is intentional data. |
| `second_name = "Farhan"` | Binds the second string. |
| `print(first_name + second_name)` | Concatenates the values in order and displays `Muhammad Farhan`. The inline comment is ignored by Python. |

Repetition uses `*` between a string and an integer, for example `"-" * 8` creates a separator. Multiplication with two strings is not defined and raises `TypeError`.

## Deep Dive: Unicode, ASCII, and Encoding

Python's `str` represents Unicode text. ASCII is a smaller historical character set that assigns numeric codes to basic Latin letters, digits, punctuation, and control characters. The course screenshot is a useful reference for those codes:

![ASCII character table from the Python course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/ASCII_TAble.png)

The image shows character-to-number mappings, not the entirety of modern text. Many characters used in names and messages are outside ASCII. A Python string is also not the same thing as bytes on disk or across a network. Encoding transforms text to bytes; decoding transforms bytes back to text using a compatible encoding, commonly UTF-8.

```text
Python str (Unicode characters) --encode("utf-8")--> bytes
bytes                          --decode("utf-8")--> Python str
```

A visible glyph does not always correspond to one byte or even one Unicode code point. Combining marks and emoji sequences can contain multiple code points. Therefore, `len(text)` is not universally equivalent to “number of characters perceived by a person.”

## Repository Example: F-String Formatting

This complete cell is from `python_intermaediate/print_method_practice.ipynb`:

```python
name = "ali"
age = 44
interst = " My interst is in ai"
print(f"My name is{name} and i am {age} years old.{interst}")
```

| Line | Explanation |
|---|---|
| `name = "ali"` | Binds a string to the name used in the formatted message. |
| `age = 44` | Binds an integer. The f-string formats it without an explicit call to `str`. |
| `interst = ...` | Binds a phrase. The source misspells the identifier and phrase, but Python allows the identifier; spelling can still affect code quality. |
| f-string `print` | The `f` prefix enables brace expressions. Python evaluates `{name}`, `{age}`, and `{interst}`, substitutes their display text, and prints the result. The literal text has no space after `is`, so output starts `name isali`; the leading space in `interst` adds a space before the final phrase. |

A cleaned version fixes the presentation without changing the concept:

```python
name = "Ali"
age = 44
interest = "AI"
print(f"My name is {name}, I am {age} years old, and I am interested in {interest}.")
```

An f-string can apply formatting: `f"Score: {score:.2f}"` displays two digits after the decimal point. Keep expressions inside braces simple; compute complex logic before constructing the message.

## Other Formatting Forms

Your notebook also includes `str.format()` and percent formatting. They remain useful to recognize in older code:

```python
print("Hello, {}!".format("everyone"))
print("Name: %s; age: %d" % ("Ali", 44))
```

F-strings are generally clearer for new code because a reader sees the variable alongside its position in the message. String concatenation is appropriate when joining string fragments, but it becomes awkward when values require conversion or spacing.

## Industry Scenario: User-Provided Text

Names and comments may contain apostrophes, accents, non-Latin characters, or emoji. Do not assume English-only ASCII unless a domain requirement demands it. Normalize only when the task calls for it, preserve the original when appropriate, and choose an explicit encoding when reading or writing files. Never build a shell command or SQL query by blindly concatenating user-provided text; use the safe parameterized interface for that system.

## Common Pitfalls

- Missing a closing quote or mixing quote styles without escaping.
- Forgetting that spaces inside quotes are part of the string.
- Expecting concatenation to insert a separator.
- Adding a string and integer without a conversion or formatting step.
- Trying to modify a string character in place; strings are immutable.
- Treating ASCII as all of Unicode, or `len()` as a count of visual glyphs.
- Using `is` to compare string contents; use `==` for value equality.
- Forgetting that user-controlled text needs safe handling in external commands and queries.

## Practice with Hints

1. Join a first and last name with exactly one space. **Hint:** include a space in one string or add a separate string containing a space.
2. Repeat a string divider 20 times. **Hint:** multiply a `str` by an `int`.
3. Format a price to two decimal places. **Hint:** use `{price:.2f}`.
4. Change the source f-string so it has correct spacing and spelling. **Hint:** spaces outside `{...}` are literal characters.
5. Explain why the ASCII chart cannot represent every string Python can hold. **Hint:** ASCII is only a subset of Unicode.
6. Encode a string as UTF-8 and decode the bytes. **Hint:** distinguish the resulting `bytes` object from the original `str`.

## Summary

Strings are immutable ordered text values. Python supports indexing, slicing, membership, concatenation, repetition, and interpolation, but each operation preserves exact character content. Unicode `str` values are distinct from encoded bytes. Use f-strings for clear output and treat ASCII as a useful subset reference, not a universal character model.
