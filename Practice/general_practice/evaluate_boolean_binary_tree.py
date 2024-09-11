class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return bool(root.val)

        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        if root.val == 2:
            return left_val or right_val
        elif root.val == 3:
            return left_val and right_val


root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
sol = Solution()
result = sol.evaluateTree(root)
print(result)
