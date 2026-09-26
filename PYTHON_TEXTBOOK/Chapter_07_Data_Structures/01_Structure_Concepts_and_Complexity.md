# 01 - Structure Concepts and Complexity

## Intuition: Organizing a Busy Workshop

A busy workshop does not keep every tool in one pile. Frequently used tools go on a labeled rack, urgent tasks go into a priority tray, and related components are linked together. Data structures make similar choices for information: they organize values so the operations a program needs can be performed clearly and efficiently.

The reason to study data structures is not to memorize a taxonomy. The important question is: **which operations must be fast, safe, and natural for this problem?** A representation optimized for one operation may make another more expensive.

## Learning Objectives

- Define data structure, element, node, reference, invariant, and operation.
- Classify common structures as sequence-oriented, associative, or relational.
- Explain time and space complexity at an introductory level.
- Choose a representation by expected access and update patterns.
- Correct oversimplifications in primitive/non-primitive classifications for Python.

## Vocabulary and Classification

A **data structure** is a way to organize values together with the operations used to access or update them. An **element** is a stored value. A **node** is a record that often contains a value and one or more references to other nodes. An **invariant** is a condition the structure must preserve (for example, a heap's parent/child ordering rule).

The repository's `intro_data_structure.ipynb` classifies structures as primitive/non-primitive and then divides non-primitive structures into linear and non-linear examples. This is a useful first visual classification, but categories depend on the textbook's model. Python does not have a separate built-in `char` type; one character is a string of length one. Nor do Python programs normally manipulate raw pointers as beginner-level primitive values. Python references exist under the hood, but a list or dictionary is generally the abstraction a Python programmer uses.

```text
Data organization
├── Sequential access
│   ├── list / tuple / range
│   ├── linked list
│   ├── stack / queue
│   └── heap (priority ordering)
└── Relationship-based access
    ├── dictionary / set (key or membership)
    ├── tree (hierarchy)
    └── graph (network)
```

This diagram groups structures by the kinds of operations they support, rather than claiming that categories are mutually exclusive. A tree, for instance, is also a graph with additional constraints.

## Repository Connection: Representation Changes Operations

The graph visualizer's Python section represents a graph using an adjacency list such as `{"A": ["B", "C"], "B": ["A"]}`. This compact representation groups each vertex with its neighbors. The same relationships could be represented by a two-dimensional adjacency matrix. Both model a graph, but memory use and edge lookup behavior differ.

| Question | Array/list-like sequence | Dictionary/set | Linked structure | Graph adjacency list |
|---|---|---|---|---|
| Primary access | Position | Key/membership | Follow references | Vertex then neighbors |
| Strength | Ordered iteration and indexing | Lookup and uniqueness | Local insertion/removal given a node | Sparse relationships |
| Typical cost caveat | Middle insertion shifts elements | Hash operations are expected fast, not absolute | Finding a target may still require traversal | Traversal visits vertices and edges |

## Deep Dive: Time and Space Complexity

Complexity describes how resource use changes as the input grows. Big-O notation focuses on a growth class, not a stopwatch measurement. If a loop processes each of `n` items once, its work grows approximately linearly: $O(n)$. A nested full scan often grows quadratically: $O(n^2)$. If a structure stores each of `n` elements, its storage is linear: $O(n)$.

| Complexity | Informal growth | Example shape |
|---|---|---|
| $O(1)$ | Approximately fixed work | Read a list item by index |
| $O(\log n)$ | A small number of shrinking search steps | Binary search in sorted data |
| $O(n)$ | Proportional to item count | Scan a list once |
| $O(n \log n)$ | Sort-like growth | Comparison sorting in common cases |
| $O(n^2)$ | Every item paired with many others | Compare every pair |

These are operation-level models, not guarantees about elapsed time. Constant factors, memory locality, data distribution, and implementation matter. A Python list can outperform a linked structure in practice for many workloads because its compact reference array is cache-friendly, even where a linked structure offers a favorable theoretical insertion operation.

## Choosing by Operations and Invariants

Before selecting a structure, write down the operations and constraints:

- Need order and index access? Consider a list or tuple.
- Need key-based lookup? Consider a dictionary.
- Need unique membership? Consider a set.
- Need first-in/first-out processing? Consider a queue.
- Need repeated access to the smallest priority? Consider a heap.
- Need parent/child hierarchy? Consider a tree.
- Need arbitrary many-to-many links? Consider a graph.
- Need common-prefix search? Consider a trie.

Then state invariants. A queue preserves arrival order. A trie must distinguish a complete word from a path that is only a prefix. A graph traversal must not repeatedly visit the same vertex in cycles.

## Industry Scenario

A service receives millions of jobs, and operators need the next job with highest urgency. A plain list can store jobs, but repeated full scans to find the minimum priority become expensive. A priority queue/heap fits the repeated “remove most urgent” operation better. If the primary requirement changes to preserving arrival order, a FIFO queue is the better model.

## Common Pitfalls

- Choosing a data structure based only on its name or diagram.
- Treating a complexity class as an exact runtime promise.
- Assuming every tree or graph is represented the same way.
- Forgetting that a structure's invariant must be restored after mutation.
- Overengineering a small dataset before measuring a real performance need.
- Applying non-Python classifications (such as a separate built-in `char`) literally to Python.

## Practice Challenges with Hints

1. For a list of 10,000 jobs, identify the cost of repeatedly scanning for the smallest priority. **Hint:** a full scan is linear per selection.
2. Pick structures for an ordered history, unique tags, and an account-ID-to-profile lookup. **Hint:** match sequence, set, and mapping semantics.
3. Explain why the same graph can have both adjacency-list and adjacency-matrix representations. **Hint:** both encode vertices and edges but trade memory for lookup.
4. State an invariant for a queue and a heap. **Hint:** describe the order that must hold after each operation.
5. Identify a case where a theoretically cheaper structure may be slower in practice. **Hint:** consider memory locality and implementation overhead.

## Summary

A data structure is chosen to support operations while preserving invariants. Complexity helps compare growth, but it does not predict every real runtime. In Python, use abstractions that express ordering, mapping, uniqueness, priority, hierarchy, or network relationships, then measure when performance matters.
