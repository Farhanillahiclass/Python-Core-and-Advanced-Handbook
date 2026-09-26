# 02 - Arrays, Linked Lists, Stacks, and Queues

## Intuition: Numbered Shelves and Linked Paperclips

An array-like sequence is a row of numbered lockers: the locker number lets you jump directly to a position. A linked list is a paperclip chain: each clip tells you where the next clip is, so reaching a later item means following the chain. A stack is a pile of trays where the top tray is handled first; a queue is a waiting line where the earliest arrival leaves first.

These structures exist because access patterns differ. Positional retrieval, insertion, and arrival-order processing require different representations.

## Learning Objectives

- Compare indexed array-like storage with singly and doubly linked nodes.
- Explain why Python lists are dynamic arrays of references, not fixed-size textbook arrays.
- Apply LIFO stack and FIFO queue behavior.
- Choose `list` or `collections.deque` based on operations.
- Interpret the repository's data-structure diagrams.

## Arrays and Python Lists

An array stores elements in positions that can be addressed by an index. In a low-level fixed-width array, elements may occupy a contiguous block; Python's built-in `list` is a resizable sequence that stores references to Python objects. Index access is typically $O(1)$ in CPython. Inserting or removing near the beginning usually requires shifting references and is typically $O(n)$.

The repository's array visual illustrates indexed slots:

![Array diagram from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/array.png)

Read the diagram as “position maps to value.” Do not infer from the image that a Python list stores every object's raw value in one fixed-width block; the list holds references, and its capacity can grow.

## Linked Lists

A singly linked node stores a value and a reference to the next node. A doubly linked node also stores a reference to the previous node. The repository includes images for both:

![Singly linked list diagram from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/LINKED_LIST.png)

![Doubly linked list diagram from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/DOUBLEY_LINKED.png)

A singly linked list is traversed forward; a doubly linked list can move both directions but uses additional references. Inserting after a node is $O(1)$ if that node is already known; finding the location first still costs $O(n)$. Linked lists are not built into Python as a dedicated general-purpose collection because lists and `deque` cover many common needs with lower overhead.

A small teaching implementation, included here to make the diagram operational, is:

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

head = Node("first", Node("second", Node("third")))
current = head
while current is not None:
    print(current.value)
    current = current.next
```

| Line | Explanation |
|---|---|
| `class Node:` | Defines the record shape for one link in the chain. |
| `__init__(...)` | Initializes each new node with a value and optional successor. |
| `self.value = value` | Stores the payload in this node. |
| `self.next = next_node` | Stores a reference to the next node or `None` at the end. |
| nested `Node(...)` construction | Creates three nodes whose `next` links form one chain. |
| `current = head` | Starts traversal at the first node. |
| `while current is not None:` | Continues until the traversal reaches the end marker. |
| `print(current.value)` | Processes the current node's payload. |
| `current = current.next` | Advances exactly one link; omitting this update would create an infinite loop. |

This implementation is a new teaching example, not a Python source file from the repository. It mirrors the linked-list infographic.

## Stacks: LIFO

A stack supports adding and removing at one end, the **top**. The most recently added item is removed first: Last In, First Out. The course diagrams show stack concepts:

![Stack illustration from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/stack_in_python.png)

![Stack and queue comparison diagram](../../Python_101_Crash_Course_Codanic/python_course_screenshort/STACK_QUEU.png)

A Python list can implement a stack efficiently at the end:

```python
stack = []
stack.append("open file")
stack.append("parse header")
latest = stack.pop()
```

`append` pushes to the top; `pop()` removes and returns the latest item. This is useful for undo history, nested operations, and depth-first traversal.

## Queues: FIFO

A queue adds at the rear and removes from the front. First In, First Out preserves arrival order. Avoid repeatedly using `list.pop(0)` for a large queue: the remaining references shift. The standard-library `collections.deque` supports efficient operations at both ends:

```python
from collections import deque

queue = deque(["request A", "request B"])
queue.append("request C")
next_request = queue.popleft()
```

The import provides `deque`; construction places two requests in the queue; `append` adds a new arrival at the rear; `popleft` removes the oldest request from the front.

## Deep Dive: Memory and Trade-offs

```text
Array-like list:     index 0    index 1    index 2
                     [ref A] -> [ref B] -> [ref C]
                       direct positional access

Singly linked:       [A | next] -> [B | next] -> [C | None]
                       traversal follows references

Doubly linked:       [prev | A | next] <-> [prev | B | next]
```

The diagrams are conceptual; Python object layouts include implementation metadata. Array-like lists trade occasional resizing and shifting for excellent indexed access and cache locality. Linked structures trade direct indexing for flexible local relinking, with per-node allocation and reference overhead. A queue's abstract behavior can be implemented by different concrete structures; choose the implementation that supports the required operations efficiently.

| Structure | Retrieval | Add/remove | Typical fit |
|---|---|---|---|
| Python list | Index typically $O(1)$ | End append/pop amortized $O(1)$; front/middle shifts $O(n)$ | Ordered collections, indexing, stack |
| Singly linked list | Position search $O(n)$ | Relink $O(1)$ given predecessor/node | Specialized insert-heavy chains |
| Doubly linked list | Position search $O(n)$ | Relink $O(1)$ given node | Bidirectional traversal and local updates |
| `deque` queue | Ends efficient | Append/pop at either end efficient | FIFO queues and double-ended worklists |

## Industry Scenario

A print server queues jobs in arrival order and processes the oldest available request. An editor uses a stack to undo recent operations in reverse order. A media playlist may require insertion and navigation; a Python list may be simpler than a custom linked list unless measurements justify a specialized structure.

## Common Pitfalls

- Calling a Python list a fixed-size array; it is dynamic and stores references.
- Expecting a linked list to provide constant-time access by index.
- Claiming linked-list insertion is always $O(1)$ without accounting for finding the position.
- Using `pop(0)` repeatedly for a large list-backed queue.
- Forgetting to advance a linked-list traversal pointer.
- Confusing stack LIFO with queue FIFO.
- Forgetting that an empty stack/queue needs an explicit behavior when removing an item.

## Practice Challenges with Hints

1. Trace the stack code and list its contents after each line. **Hint:** the rightmost list item is the stack top.
2. Trace the queue code and identify which request leaves first. **Hint:** `popleft` removes the oldest.
3. Extend the node traversal to count nodes. **Hint:** increment a counter inside the loop.
4. Describe the benefit and cost of adding a `prev` link. **Hint:** compare reverse traversal with memory use.
5. Choose between `list` and `deque` for repeated left removals. **Hint:** consider how many elements shift.

## Summary

Array-like lists excel at indexing and end operations. Linked lists follow references and support local relinking when the node is known, but searching remains linear. Stacks are LIFO; queues are FIFO. Python's list and `deque` provide practical implementations for many everyday tasks.
