from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result


def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


arr = [3, 9, 20, None, None, 15, 7]
root = insert_level_order(arr, None, 0, len(arr))
print(levelOrder(root))  # [[3], [9, 20], [15, 7]]

arr = [1]
root = insert_level_order(arr, None, 0, len(arr))
print(levelOrder(root))  # [[1]]

arr = []
root = insert_level_order(arr, None, 0, len(arr))
print(levelOrder(root))  # []
