class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    def height(node):
        if not node:
            return 0
        return max(height(node.left), height(node.right)) + 1

    def is_balanced_helper(node):
        if not node:
            return True

        left_height = height(node.left)
        right_height = height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return is_balanced_helper(node.left) and is_balanced_helper(node.right)

    return is_balanced_helper(root)


root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)

root3 = None

print(isBalanced(root1))  # True
print(isBalanced(root2))  # False
print(isBalanced(root3))  # True
