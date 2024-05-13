class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        def maxPathDown(node):
            if not node:
                return 0

            left_sum = max(0, maxPathDown(node.left))
            right_sum = max(0, maxPathDown(node.right))

            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)

            return node.val + max(left_sum, right_sum)

        maxPathDown(root)
        return self.max_sum


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print(Solution().maxPathSum(root1))  # 6

root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
print(Solution().maxPathSum(root2))  # 42
