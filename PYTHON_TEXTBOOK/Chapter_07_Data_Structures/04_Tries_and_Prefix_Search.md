# 04 - Tries and Prefix Search

## Intuition: A Word-Finding Maze

Imagine a word maze where every junction represents the next character. Words that begin the same way share the same early route: `CAR` and `CART` travel through `C` → `A` → `R`, then `CAR` ends while `CART` continues. A trie (pronounced “try”) stores strings in this shared-prefix form.

Tries exist when prefix operations matter: autocomplete, dictionary lookup, spell checking, and prefix routing. A hash table can be excellent for checking one complete key, but it does not naturally reveal all words beginning with a prefix.

## Learning Objectives

- Explain trie nodes, child mappings, and terminal markers.
- Trace insertion, exact search, and prefix search.
- Understand why a prefix node may not represent a complete word.
- Estimate time and memory costs in terms of input length and shared prefixes.
- Use the repository's interactive trie visualizer as a guide to operations.

## Trie Structure

Each node contains a mapping from a character to a child node. The root represents the empty prefix. A Boolean terminal marker records whether the path to that node is a complete stored word. The marker is necessary because `CAR` may be stored while `CART` shares and extends its path.

```text
(root)
  |
  C
  |
  A
  |
  R* ---- T*

* marks a complete word
CAR is complete at R; CART is complete at T
```

Without terminal markers, the structure could tell that a path exists but not whether the user inserted that entire string.

## Repository Example: Python Trie Implementation

The following implementation is embedded in `python_course_screenshort/trie_data_structure.html`:

```python
class TrieNode:
    """Represents a single node in the Trie structure."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Trie structure with insert, search, and starts_with operations."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### Line-by-Line Walkthrough

| Line or group | Explanation |
|---|---|
| `class TrieNode:` | Defines the data held at one character-path position. |
| node docstring | Documents the node's role. |
| `__init__` | Initializes every newly created node. |
| `self.children = {}` | Maps outgoing characters to child nodes. A dictionary supports lookup by the next character. |
| `self.is_end_of_word = False` | Starts with no complete word ending at this node. |
| `class Trie:` | Defines the overall trie operations. |
| trie docstring | Names insertion, exact lookup, and prefix lookup as supported operations. |
| trie `__init__` | Creates a single root node for the empty prefix. |
| `insert` | Declares an operation that consumes a word and returns no explicit result (`None`). |
| `node = self.root` | Begins walking from the root for every inserted word. |
| `for char in word:` | Processes characters left to right. |
| missing-child condition | Checks whether this character branch already exists. |
| child creation | Creates a node only for a previously unseen branch. |
| `node = node.children[char]` | Advances one level down the path. |
| terminal assignment | Marks the final node as a complete word. This allows one word to be a prefix of another. |
| `search` initialization | Starts exact lookup at the root. |
| search loop | Tries to follow each character of the requested word. |
| missing branch return | Ends immediately with `False` when no such path exists. |
| search advance | Follows the existing child for this character. |
| `return node.is_end_of_word` | Returns true only if the entire path ends at a marked word boundary. A mere prefix is not enough. |
| `starts_with` initialization and loop | Walks the prefix path similarly to exact search. |
| missing path return | Returns false if any prefix character cannot be followed. |
| final `return True` | Confirms the prefix path exists; it need not be a complete word. |

## Repository Visualizer

Your HTML visualizer shows insertion, exact lookup, and prefix checks step by step, and labels terminal word nodes:

[Open the interactive trie visualizer](../../Python_101_Crash_Course_Codanic/python_course_screenshort/trie_data_structure.html)

The simulator's browser-side JavaScript mirrors the Python idea with a root, per-character child maps, and an end-of-word flag. Its visual animation is a teaching aid; the Python implementation above is the authoritative example for Python code.

## Deep Dive: Complexity and Memory

For a string of length $L$, insertion, exact search, and prefix search each follow at most $L$ character edges, so their basic traversal time is $O(L)$, plus dictionary lookup costs. Memory depends on the number of distinct nodes, which is bounded by the total number of characters inserted but reduced when words share prefixes. A trie may use more memory than a hash set of complete words because each node and child mapping has overhead.

A trie is case-sensitive unless normalization is added. The visualizer uppercases its interactive input; the Python class shown above does not normalize, so `"Cat"` and `"cat"` are different paths. Decide normalization policy at the input boundary and apply it consistently during insertion and search.

| Operation | What it answers | Terminal marker needed? |
|---|---|---|
| `insert(word)` | Store a string | Sets marker at final node |
| `search(word)` | Is this exact word stored? | Yes |
| `starts_with(prefix)` | Does any stored word have this path prefix? | No, path existence is sufficient |
| Suggestions | Which complete words extend this prefix? | Yes, to know where suggestions end |

## Industry Scenario: Autocomplete

A search box can use a trie to navigate the typed prefix and enumerate terminal words beneath that node. Shared prefixes reduce repeated path storage. Production autocomplete often adds ranking, language normalization, deletion, persistence, and limits on returned suggestions; a basic trie is the indexing structure, not the whole product.

## Common Pitfalls and Edge Cases

- Returning true for exact search whenever the path exists, even if it is only a prefix.
- Forgetting to set the terminal marker during insertion.
- Removing a word's shared node without checking whether another word uses that path.
- Treating case variants or Unicode normalization inconsistently.
- Assuming tries always use less memory than hash sets.
- Calling `starts_with("")`: this implementation returns true because the root is the path for the empty prefix. Decide whether this behavior matches the application.
- Inserting the empty string marks the root as a complete word in this implementation; decide whether empty keys are allowed.

## Practice Challenges with Hints

1. Insert `CAR`, `CART`, and `CAT`; draw shared nodes and terminal markers. **Hint:** `CAR` and `CART` share the first three nodes.
2. Search for `CA` after inserting `CAR`. **Hint:** path exists, but the terminal marker may be false.
3. Add a `starts_with` test for `DOG` when only `DOT` is stored. **Hint:** compare character paths one at a time.
4. Decide whether the trie accepts lowercase and uppercase as equivalent. **Hint:** normalize input consistently before both insertion and lookup.
5. Sketch a safe deletion strategy for a word that shares prefixes. **Hint:** clear its terminal marker, then prune only nodes with no children and no terminal word.

## Summary

A trie stores strings as character paths and shares common prefixes. Child maps support traversal; terminal markers distinguish complete words from prefixes. Core operations take time proportional to the query length, while memory depends on distinct prefixes and representation overhead. Prefix matching is the trie’s defining strength.
