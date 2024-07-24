from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addOneRow(root: TreeNode, val: int, depth: int) -> TreeNode:
    if depth == 1:
        new_root = TreeNode(val)
        new_root.left = root
        return new_root

    queue = deque([root])
    current_depth = 1

    while queue and current_depth < depth - 1:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        current_depth += 1

    while queue:
        node = queue.popleft()
        temp_left = node.left
        temp_right = node.right
        node.left = TreeNode(val)
        node.right = TreeNode(val)
        node.left.left = temp_left
        node.right.right = temp_right

    return root


def print_tree(root: TreeNode):
    if not root:
        print("Empty tree")
        return

    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        if any(item is not None for item in level):
            print(level)



root = TreeNode(4)
root.left = TreeNode(2, TreeNode(3), TreeNode(1))
root.right = TreeNode(6, TreeNode(5))

print("Original tree:")
print_tree(root)

new_tree = addOneRow(root, 1, 2)

print("\nTree after adding a row with value 1 at depth 2:")
print_tree(new_tree)
