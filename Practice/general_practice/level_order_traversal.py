class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root):
    if not root:
        return []

    result = []
    current_level = [root]

    while current_level:
        next_level = []
        current_values = []

        for node in current_level:
            current_values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.insert(0, current_values)
        current_level = next_level

    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrderBottom(root))
