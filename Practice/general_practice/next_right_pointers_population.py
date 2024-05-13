class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    if not root:
        return

    level_start = root
    while level_start.left:
        curr = level_start
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        level_start = level_start.left


def print_connected_nodes(root):
    while root:
        curr = root
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("#")
        root = root.left


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connect(root)
print_connected_nodes(root)
