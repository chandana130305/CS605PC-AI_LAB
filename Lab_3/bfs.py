from collections import deque

# -----------------------------
# Tree Node Definition
# -----------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

# -----------------------------
# BFS Function
# Uses 2 Data Structures:
#   1. Queue
#   2. Visited
# -----------------------------
def bfs(root):
    if root is None:
        return []

    queue = deque([root])   # DS 1: Queue
    visited = set()         # DS 2: Visited
    result = []

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        result.append(node.val)

        # add children to queue
        for child in node.children:
            queue.append(child)

    return result

# -----------------------------
# DRIVER CODE (Tree Input)
# -----------------------------
if __name__ == "__main__":
    # Build sample tree
    #        A
    #      /   \
    #     B     C
    #    /
    #   D

    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')

    A.children = [B, C]
    B.children = [D]

    # Run BFS
    output = bfs(A)
    print("BFS Traversal:", output)
