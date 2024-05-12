class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    if not root:
        return

    def flatten_helper(node):
        if not node:
            return

        flatten_helper(node.left)
        flatten_helper(node.right)

        right_subtree = node.right

        node.right = node.left
        node.left = None

        while node.right:
            node = node.right

        node.right = right_subtree

    flatten_helper(root)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)

root2 = None

root3 = TreeNode(0)

flatten(root1)
flatten(root2)
flatten(root3)


def print_flattened_tree(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")


print_flattened_tree(root1)  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
print_flattened_tree(root2)  # None
print_flattened_tree(root3)  # 0 -> None
