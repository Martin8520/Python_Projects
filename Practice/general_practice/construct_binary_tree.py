class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder, postorder):
    def helper(in_left, in_right):
        nonlocal post_idx
        if in_left > in_right:
            return None
        root_val = postorder[post_idx]
        root = TreeNode(root_val)
        in_idx = idx_map[root_val]
        post_idx -= 1
        root.right = helper(in_idx + 1, in_right)
        root.left = helper(in_left, in_idx - 1)
        return root

    idx_map = {val: idx for idx, val in enumerate(inorder)}
    post_idx = len(postorder) - 1
    return helper(0, len(inorder) - 1)


def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
tree_root = buildTree(inorder, postorder)
print("Inorder:", inorder_traversal(tree_root))
print("Postorder:", postorder_traversal(tree_root))
