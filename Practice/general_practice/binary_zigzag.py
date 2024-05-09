from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    zigzag = False
    while queue:
        level_size = len(queue)
        level_values = deque() if zigzag else []

        for _ in range(level_size):
            node = queue.popleft()
            if zigzag:
                level_values.appendleft(node.val)
            else:
                level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_values))
        zigzag = not zigzag

    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(zigzag_level_order(root))
