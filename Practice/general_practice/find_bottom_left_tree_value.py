from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(root: TreeNode) -> int:
    if not root:
        return None

    queue = deque([(root, 0)])
    current_level = -1
    leftmost_value = None

    while queue:
        node, level = queue.popleft()

        if level > current_level:
            current_level = level
            leftmost_value = node.val

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return leftmost_value


# [2, 1, 3]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(findBottomLeftValue(root))  # 1

# [1, 2, 3, 4, null, 5, 6, null, null, 7]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.right = TreeNode(7)

print(findBottomLeftValue(root))  # 7
