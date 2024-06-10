class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pseudoPalindromicPaths(root):
    def dfs(node, path):
        if not node:
            return 0

        path ^= 1 << node.val
        if not node.left and not node.right:
            if path & (path - 1) == 0:
                return 1
            else:
                return 0

        left_paths = dfs(node.left, path)
        right_paths = dfs(node.right, path)

        return left_paths + right_paths

    return dfs(root, 0)


#  [2,3,1,3,1,null,1]
root1 = TreeNode(2)
root1.left = TreeNode(3)
root1.right = TreeNode(1)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(1)
root1.right.right = TreeNode(1)

print(pseudoPalindromicPaths(root1))  # 2

# [2,1,1,1,3,null,null,null,null,null,1]
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(1)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.left.right.right = TreeNode(1)

print(pseudoPalindromicPaths(root2))  # 1
