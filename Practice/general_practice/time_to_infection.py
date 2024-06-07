from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def amount_of_time(root, start):
    if not root:
        return 0

    graph = defaultdict(list)

    def build_graph(node, parent=None):
        if node:
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)

    build_graph(root)

    queue = deque([start])
    visited = set([start])
    minutes = -1

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        minutes += 1

    return minutes


root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(2)
start = 3
print(amount_of_time(root, start))
root = TreeNode(1)
start = 1
print(amount_of_time(root, start))
