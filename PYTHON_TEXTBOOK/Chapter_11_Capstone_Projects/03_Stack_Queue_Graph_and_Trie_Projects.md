# 03 - Stack, Queue, Graph, and Trie Projects

## Project Overview

This project set turns the repository's structure diagrams and interactive graph/trie visualizers into implementable Python exercises. Choose one track first; each track has a distinct invariant and access pattern.

## Intuition: Four Different Workflows

- A stack is a pile: the newest item is removed first.
- A queue is a waiting line: the oldest item is removed first.
- A graph is a route map: nodes connect through edges, possibly in cycles.
- A trie is a word maze: characters share prefix paths and terminal nodes mark complete words.

The structures are not interchangeable. Their behavior is defined by the operation users need most.

## Learning Objectives

- Select an implementation matching LIFO, FIFO, graph traversal, or prefix search.
- State the structure's invariant before coding.
- Test empty, duplicate, cyclic, disconnected, and shared-prefix cases.
- Use repository visuals and HTML simulators as conceptual references.

## Track A: Undo Stack

Use a Python list as a stack, adding actions at the end and undoing the latest action first:

```python
undo_history = []
undo_history.append("add heading")
undo_history.append("change font")
last_action = undo_history.pop()
print(last_action)
```

`append` pushes a new action; `pop()` removes and returns the most recent one. The output is `change font`. Define what happens when the stack is empty before calling `pop`.

**Tests:** one action, multiple actions, undo until empty, and an extra undo.  
**Extension:** pair each action with enough prior state to reverse it safely.

## Track B: FIFO Task Queue

Use `collections.deque` so removing the front does not require shifting every remaining item:

```python
from collections import deque

pending = deque()
pending.append("job A")
pending.append("job B")
next_job = pending.popleft()
print(next_job)
```

The first `append` records the earliest task; the second follows it. `popleft()` removes `job A`, preserving FIFO order. The repository visuals show this behavior:

![Stack and queue reference diagram](../../Python_101_Crash_Course_Codanic/python_course_screenshort/STACK_QUEU.png)

**Tests:** enqueue order, dequeue order, empty queue, and burst arrivals.  
**Extension:** add a maximum queue size or a cancellation policy.

## Track C: Graph Explorer

Use the repository's interactive graph visualizer as a guide to vertices, edges, directed/undirected graphs, adjacency lists/matrices, BFS, and DFS:

[Open the interactive graph visualizer](../../Python_101_Crash_Course_Codanic/python_course_screenshort/graph_data_structure_visualizer.html)

The visualizer includes a Python adjacency-list implementation. Reuse or extend that structure to:

- add vertices and weighted/unweighted edges;
- traverse from a start vertex with BFS and DFS;
- report reachable nodes;
- detect a cycle or return a path;
- include disconnected components when requested.

**Required invariant:** every traversed vertex is recorded in `visited` before it is queued/recursed into. This prevents repeated processing in cyclic graphs.

**Tests:** a line graph, a cycle, a disconnected vertex, directed one-way edge, duplicate edge, and missing start vertex. For weighted graphs, do not report BFS as a minimum-cost algorithm; it minimizes edge count only in unweighted graphs.

## Track D: Autocomplete Trie

The repository's trie visualizer includes a Python implementation with `TrieNode`, `insert`, `search`, and `starts_with`:

[Open the interactive trie visualizer](../../Python_101_Crash_Course_Codanic/python_course_screenshort/trie_data_structure.html)

Use the terminal marker invariant: a node may both end one word and have children continuing longer words. Add a `suggest(prefix, limit)` operation by traversing to the prefix node and enumerating terminal descendants.

```text
root -> C -> A -> R* -> T*
                 CAR     CART
```

**Tests:** a word, a prefix that is not a word, a word that is also another word's prefix, missing branch, repeated insertion, case differences, and empty prefix. Define normalization consistently before insert and search.

## Project Engineering Plan

1. Choose one track and write its invariant in a sentence.
2. Define the input and output behavior for normal and empty cases.
3. Implement the minimal operations before adding a visual interface.
4. Test edge cases before extending the feature set.
5. Add complexity notes and limits in the README.
6. Compare the Python behavior with the repository visualizer where applicable.

## Common Pitfalls

- Using list front removal for a large queue.
- Forgetting a visited set in cyclic graph traversal.
- Assuming DFS always returns the shortest path.
- Treating a heap or queue as a sorted collection.
- Failing to distinguish prefix existence from a complete trie word.
- Implementing deletion without preserving shared branches.
- Designing a UI before defining data-structure behavior.

## Review Exercises

1. Which structure should undo use, and why? **Hint:** reverse the order of actions.
2. Draw BFS and DFS frontiers on the same graph. **Hint:** queue versus stack/call stack.
3. Add a graph test where a vertex is unreachable from the start. **Hint:** decide whether the method returns only reachable nodes or all components.
4. Insert `CAT`, `CAR`, and `CART` into a trie sketch. **Hint:** mark complete words separately from nodes with children.
5. State worst-case input size limits for a recursive DFS or suggestion enumeration. **Hint:** consider recursion depth and number of matching words.

## Completion Checklist

- Required operations are implemented and documented.
- Empty and edge cases are tested.
- The visualizer is cited as a learning reference, not mistaken for the implementation under test.
- Complexity and limitations are described honestly.
- No output is called “shortest,” “sorted,” or “complete” unless the algorithm guarantees it.
