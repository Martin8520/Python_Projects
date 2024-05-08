class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False

        return True

    return helper(root)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(isValidBST(root1))

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(isValidBST(root2))

root3 = TreeNode(10)
print(isValidBST(root3))

root4 = TreeNode(5)
root4.left = TreeNode(4)
root4.left.left = TreeNode(3)
print(isValidBST(root4))

root5 = TreeNode(5)
root5.right = TreeNode(6)
root5.right.right = TreeNode(7)
print(isValidBST(root5))

root6 = TreeNode(2)
root6.left = TreeNode(2)
root6.right = TreeNode(3)
print(isValidBST(root6))

root7 = TreeNode(2)
root7.left = TreeNode(1)
root7.right = TreeNode(2)
print(isValidBST(root7))
