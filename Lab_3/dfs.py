# -----------------------------
# Tree Node Definition
# -----------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

# -----------------------------
# DFS Function (Iterative)
# Uses 2 Data Structures:
#   1. Stack
#   2. Visited
# -----------------------------
def dfs(root):
    if root is None:
        return []

    stack = [root]      # DS 1: Stack
    visited = set()     # DS 2: Visited
    result = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        result.append(node.val)

        # push children in reverse (to maintain order)
        for child in reversed(node.children):
            stack.append(child)

    return result

# -----------------------------
# DRIVER CODE
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

    # Run DFS
    output = dfs(A)
    print("DFS Traversal:", output)
