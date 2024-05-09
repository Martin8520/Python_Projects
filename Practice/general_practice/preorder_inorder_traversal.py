class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    root_index = inorder.index(root_val)

    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

tree = build_tree(preorder, inorder)


def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)


print_tree(tree)
