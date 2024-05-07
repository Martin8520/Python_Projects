class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n):
    def generate_trees_helper(start, end):
        if start > end:
            return [None]

        result = []

        for i in range(start, end + 1):
            left_subtrees = generate_trees_helper(start, i - 1)
            right_subtrees = generate_trees_helper(i + 1, end)

            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)

        return result

    if n == 0:
        return []

    return generate_trees_helper(1, n)


def print_trees(trees):
    for tree in trees:
        print_tree(tree)
        print()


def print_tree(root, indent=0):
    if root:
        print_tree(root.right, indent + 4)
        print(" " * indent + str(root.val))
        print_tree(root.left, indent + 4)


n1 = 3
trees1 = generateTrees(n1)
print_trees(trees1)

n2 = 1
trees2 = generateTrees(n2)
print_trees(trees2)
