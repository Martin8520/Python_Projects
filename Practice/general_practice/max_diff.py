class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxAncestorDiff(root):
    def dfs(node, current_min, current_max):
        if not node:
            return current_max - current_min

        current_min = min(current_min, node.val)
        current_max = max(current_max, node.val)

        left_diff = dfs(node.left, current_min, current_max)
        right_diff = dfs(node.right, current_min, current_max)

        return max(left_diff, right_diff)

    return dfs(root, root.val, root.val)


root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(13)
print(maxAncestorDiff(root))  # 7

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(0)
root.right.right.left = TreeNode(3)
print(maxAncestorDiff(root))  # 3
