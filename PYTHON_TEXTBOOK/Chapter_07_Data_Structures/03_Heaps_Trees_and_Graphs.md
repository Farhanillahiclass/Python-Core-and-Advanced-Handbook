# 03 - Heaps, Trees, and Graphs

## Intuition: Dispatch Board, Family Tree, and City Map

A dispatch board ranks jobs by urgency; the most urgent item should be easy to retrieve, even if every job is not fully sorted. A family tree places relationships into a hierarchy with ancestors and descendants. A city map connects intersections in a network where routes branch, merge, and loop. Heaps, trees, and graphs are different structures because they model different relationships and operations.

## Learning Objectives

- Explain heap, tree, and graph vocabulary.
- Use `heapq` for priority-ordered retrieval.
- Distinguish trees from general graphs.
- Represent graphs with adjacency lists and matrices.
- Trace breadth-first and depth-first traversal with visited state.
- Interpret the repository's heap, tree, and graph visuals.

## Heaps and Priority Queues

A heap is a partially ordered structure: in a min-heap, the parent is no greater than its children, so the minimum is at the root. The rest of the values are not globally sorted. Python's `heapq` module uses a list to represent a binary min-heap.

The repository's heap diagram gives a visual guide:

![Heap and priority-queue diagram from course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/HEAPQ.png)

```python
import heapq

priorities = [7, 2, 5]
heapq.heapify(priorities)
next_priority = heapq.heappop(priorities)
heapq.heappush(priorities, 1)
```

| Line | Explanation |
|---|---|
| `import heapq` | Imports the standard-library heap operations. |
| `priorities = [...]` | Creates a list of priority values. |
| `heapq.heapify(priorities)` | Rearranges the list in place to satisfy the min-heap invariant. |
| `heappop` | Removes and returns the smallest value, 2. |
| `heappush` | Inserts 1 and restores the heap invariant. |

The root is easy to inspect, and push/pop operations are typically $O(\log n)$. If the task requires displaying every element in sorted order, repeatedly pop from a copy or use `sorted`; do not assume a heap's backing list is sorted.

## Trees

A tree is a connected hierarchical structure with a root and child relationships. In a rooted tree, each non-root node has one parent; nodes with no children are leaves. A binary tree has at most two children per node. Search trees add an ordering invariant, but not every tree is a search tree.

![Tree diagram from the course screenshots](../../Python_101_Crash_Course_Codanic/python_course_screenshort/TREE.png)

```text
             root
           /      \
        child A   child B
        /   \
     leaf  leaf
```

Trees represent folder hierarchies, menus, syntax, and decision paths. Traversal order matters: preorder visits parent before children; inorder visits the left subtree, parent, then right subtree; postorder visits children before parent. A degenerate tree can have height $n$, so a tree's height affects traversal/search cost.

## Graphs

A graph is described by vertices (entities) and edges (relationships), often written $G=(V,E)$. Edges may be directed or undirected and may carry weights. Unlike a tree, a graph can have cycles, self-loops, multiple components, and many paths between vertices.

The repository's graph visualizer describes adjacency lists and matrices and demonstrates BFS and DFS:

[Open the interactive graph visualizer](../../Python_101_Crash_Course_Codanic/python_course_screenshort/graph_data_structure_visualizer.html)

| Representation | Space pattern | Edge lookup | Best fit |
|---|---|---|---|
| Adjacency list | $O(V+E)$ | Depends on a vertex's neighbor count | Sparse graphs |
| Adjacency matrix | $O(V^2)$ | Typically $O(1)$ by matrix position | Dense graphs or frequent edge-existence queries |

## Repository Example: Graph Traversal

The following Python implementation is embedded in `graph_data_structure_visualizer.html`. It uses a dictionary adjacency list, a `deque` for BFS, and recursion for DFS:

```python
from collections import deque

class Graph:
    """A Class representing an Adjacency List Graph with BFS/DFS searches."""
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_node(self, node):
        """Creates a unique node if not present."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2, weight=1):
        """Connects two nodes with an optional weighted path."""
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append((node2, weight))
        if not self.directed:
            self.adj_list[node2].append((node1, weight))

    def bfs(self, start_node):
        """Breadth-First Search (Uses a Queue / FIFO structure)."""
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        traversal_order = []
        while queue:
            current = queue.popleft()
            traversal_order.append(current)
            for neighbor, weight in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal_order

    def dfs(self, start_node, visited=None, traversal_order=None):
        """Depth-First Search (Uses recursion/Call Stack LIFO structure)."""
        if visited is None:
            visited = set()
        if traversal_order is None:
            traversal_order = []
        visited.add(start_node)
        traversal_order.append(start_node)
        for neighbor, weight in self.adj_list.get(start_node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, traversal_order)
        return traversal_order

routes = Graph(directed=False)
routes.add_edge("Lahore", "Islamabad", 1)
routes.add_edge("Islamabad", "Peshawar", 1)
routes.add_edge("Lahore", "Karachi", 1)
print(routes.bfs("Lahore"))
print(routes.dfs("Lahore"))
```

### Line-by-Line Mechanics

| Line or group | Explanation |
|---|---|
| `from collections import deque` | Imports a double-ended queue for efficient FIFO removal. |
| `class Graph:` | Defines a graph abstraction that keeps its representation and operations together. |
| `__init__(directed=False)` | Initializes an empty adjacency list and records whether edges are directed. |
| `self.adj_list = {}` | Maps each node to its list of outgoing neighbors. |
| `add_node` | Creates a neighbor list only if the node is not already present. |
| `add_edge` | Ensures both endpoints exist, then stores a `(destination, weight)` pair. |
| `if not self.directed` | For an undirected graph, stores the reverse adjacency as well. |
| `bfs` | Initializes a visited set, queue, and traversal result. |
| `queue.popleft()` | Removes the oldest frontier node, enforcing breadth-first order. |
| `adj_list.get(current, [])` | Gets neighbors, or an empty list if the key is absent. |
| `if neighbor not in visited` | Prevents revisiting nodes and looping forever on cycles. |
| `visited.add` before enqueue | Marks when discovered, preventing duplicate queue entries. |
| BFS `return` | Returns nodes in their traversal order; it does not compute weighted shortest paths. |
| `dfs` default setup | Creates a fresh visited set/result only when callers did not supply them. `None` is used instead of mutable defaults. |
| DFS mark and append | Records the current node before exploring neighbors. |
| recursive call | Follows one branch deeply; the Python call stack tracks where to resume. |
| `routes = Graph(...)` | Constructs an undirected graph instance. |
| three `add_edge` calls | Create a small network; the third connection makes an alternate route from Lahore. |
| two `print` calls | Display BFS and DFS traversals; order depends on adjacency insertion order. |

The example accepts edge weights but BFS ignores them, as do the DFS traversal operations. BFS finds a shortest path in number of edges for an unweighted graph, not necessarily the lowest total weight. Weighted shortest paths require an algorithm designed for weights, such as Dijkstra's algorithm under its nonnegative-weight assumption.

## Deep Dive: Traversal Invariants and Costs

A traversal maintains a **frontier** of discovered but not yet processed vertices and a `visited` set. BFS uses a queue so older discoveries are processed first and explores by distance layers. DFS uses a stack—explicit or the recursion call stack—and explores deeply before backtracking. With adjacency lists, complete BFS/DFS is $O(V+E)$ when every vertex and edge in a component is visited.

The repository DFS uses recursion. Very deep graphs can exceed Python's recursion limit; an explicit list stack avoids that particular recursion-depth constraint. A start-node traversal only visits its reachable component; loop over all vertices if every disconnected component must be included.

## Industry Scenario

A route planner models intersections as vertices and roads as weighted edges. A social network models accounts as vertices and follows/friendships as directed or undirected edges. The representation and traversal must match the question: fewest transfers, lowest travel cost, reachable users, or connected components are different queries.

## Common Pitfalls

- Assuming a tree and a general graph are interchangeable.
- Forgetting `visited` when traversing a cyclic graph.
- Claiming BFS solves weighted shortest path without accounting for weights.
- Assuming traversal order is unique; it depends on neighbor order.
- Forgetting disconnected vertices outside the start component.
- Treating a heap's internal list as sorted.
- Using recursive DFS on extreme depth without considering Python's recursion limit.

## Practice Challenges with Hints

1. Draw an adjacency list and matrix for a four-node graph. **Hint:** include isolated vertices in the matrix.
2. Add a cycle to the `routes` graph. **Hint:** the visited set must prevent an endless revisit.
3. Run BFS from a disconnected vertex. **Hint:** only its reachable component is returned.
4. Explain why the graph code stores reverse edges only for undirected mode. **Hint:** directed adjacency has one-way meaning.
5. Add edge weights and describe why BFS is not sufficient for cheapest-route selection. **Hint:** BFS counts edges; weights change path cost.

## Summary

A heap supports priority access; a tree models hierarchy; a graph models general relationships. Graph representation affects space and lookup. BFS uses a queue; DFS uses a stack or recursion. Correct traversal requires visited-state management and a clear account of edge direction, weights, and disconnected components.
