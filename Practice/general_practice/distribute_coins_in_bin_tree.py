class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0

        def postOrder(node):
            if not node:
                return 0

            left_excess = postOrder(node.left)
            right_excess = postOrder(node.right)

            total_excess = node.val - 1 + left_excess + right_excess

            self.moves += abs(left_excess) + abs(right_excess)

            return total_excess

        postOrder(root)

        return self.moves


def print_tree(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


root = TreeNode(3, TreeNode(0), TreeNode(0))
sol = Solution()
print(sol.distributeCoins(root))

root = TreeNode(0, TreeNode(3), TreeNode(0))
sol = Solution()
print(sol.distributeCoins(root))
