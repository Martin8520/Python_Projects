class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode) -> int:
    max_diameter = [0]

    def dfs(node):
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        max_diameter[0] = max(max_diameter[0], left_depth + right_depth)

        return 1 + max(left_depth, right_depth)

    dfs(root)
    return max_diameter[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameterOfBinaryTree(root))  # 3

root = TreeNode(1)
root.left = TreeNode(2)

print(diameterOfBinaryTree(root))  # 1
