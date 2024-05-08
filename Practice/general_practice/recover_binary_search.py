class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(root):
    def inorder_traversal(node):
        nonlocal first, second, prev
        if not node:
            return

        inorder_traversal(node.left)

        if prev and prev.val > node.val:
            if not first:
                first = prev
            second = node

        prev = node

        inorder_traversal(node.right)

    first, second, prev = None, None, None
    inorder_traversal(root)

    first.val, second.val = second.val, first.val

    def print_inorder(node):
        if not node:
            print("null", end=" ")
            return
        print_inorder(node.left)
        print(node.val, end=" ")
        print_inorder(node.right)

    print_inorder(root)
    print()


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.right = TreeNode(2)
recoverTree(root1)

root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(2)
recoverTree(root2)
