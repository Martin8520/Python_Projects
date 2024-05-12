class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, targetSum):
    def dfs(node, path, curr_sum):
        if not node:
            return

        curr_sum += node.val
        path.append(node.val)

        if not node.left and not node.right and curr_sum == targetSum:
            result.append(path[:])

        dfs(node.left, path, curr_sum)
        dfs(node.right, path, curr_sum)

        path.pop()

    result = []
    dfs(root, [], 0)
    return result


root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.left = TreeNode(5)
root1.right.right.right = TreeNode(1)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

root3 = TreeNode(1)
root3.left = TreeNode(2)

print(pathSum(root1, 22))  # [[5, 4, 11, 2], [5, 8, 4, 5]]
print(pathSum(root2, 5))  # []
print(pathSum(root3, 0))  # []
