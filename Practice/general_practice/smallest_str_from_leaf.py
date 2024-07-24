class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def smallestFromLeaf(root: TreeNode) -> str:
    def dfs(node, path):
        if not node:
            return
        path = chr(ord('a') + node.val) + path
        if not node.left and not node.right:
            nonlocal smallest
            if path < smallest:
                smallest = path
        dfs(node.left, path)
        dfs(node.right, path)

    smallest = "~"
    dfs(root, "")
    return smallest



root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

result = smallestFromLeaf(root)
print(result)
