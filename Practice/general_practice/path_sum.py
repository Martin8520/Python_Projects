class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False

    def dfs(node, curr_sum):
        if not node.left and not node.right:
            return curr_sum + node.val == targetSum
        left = dfs(node.left, curr_sum + node.val) if node.left else False
        right = dfs(node.right, curr_sum + node.val) if node.right else False
        return left or right

    return dfs(root, 0)


root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.right = TreeNode(1)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

root3 = None

print(hasPathSum(root1, 22))  # True
print(hasPathSum(root2, 5))  # False
print(hasPathSum(root3, 0))  # False
