
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(preorderTraversal(root))  # [1, 2, 3]

root = None
print(preorderTraversal(root))  # []

root = TreeNode(1)
print(preorderTraversal(root))  # [1]
