from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isEvenOddTree(root: TreeNode) -> bool:
    if not root:
        return True

    queue = deque([root])
    level = 0

    while queue:
        level_size = len(queue)
        prev_value = None

        for i in range(level_size):
            node = queue.popleft()

            if level % 2 == 0:
                if node.val % 2 == 0 or (prev_value is not None and node.val <= prev_value):
                    return False
            else:
                if node.val % 2 != 0 or (prev_value is not None and node.val >= prev_value):
                    return False

            prev_value = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1

    return True


# [1,10,4,3,null,7,9,12,8,6,null,null,2]
root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(12)
root.left.left.right = TreeNode(8)
root.right.left.left = TreeNode(6)
root.right.right.right = TreeNode(2)

print(isEvenOddTree(root))  # true

# Tree: [5,4,2,3,3,7]
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(7)

print(isEvenOddTree(root))  # false

# Tree: [5,9,1,3,5,7]
root = TreeNode(5)
root.left = TreeNode(9)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(7)

print(isEvenOddTree(root))  # false
