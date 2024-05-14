class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root):
    def dfs(node, num):
        if not node:
            return 0
        if not node.left and not node.right:
            return num * 10 + node.val
        return dfs(node.left, num * 10 + node.val) + dfs(node.right, num * 10 + node.val)

    return dfs(root, 0)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print(sumNumbers(root1))  # 25

root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)
print(sumNumbers(root2))  # 1026
