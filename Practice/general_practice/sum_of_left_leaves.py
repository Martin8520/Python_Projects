# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root):
    def dfs(node, is_left):
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.val
        return dfs(node.left, True) + dfs(node.right, False)

    return dfs(root, False)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sumOfLeftLeaves(root))  # 24

single_node = TreeNode(1)
print(sumOfLeftLeaves(single_node))  # 0
