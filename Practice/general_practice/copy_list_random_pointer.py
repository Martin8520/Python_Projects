class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None

    node_map = {}

    curr = head
    while curr:
        node_map[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        if curr.next:
            node_map[curr].next = node_map[curr.next]

        if curr.random:
            node_map[curr].random = node_map[curr.random]

        curr = curr.next

    return node_map[head]


head1 = Node(7)
head1.next = Node(13)
head1.next.next = Node(11)
head1.next.next.next = Node(10)
head1.next.next.next.next = Node(1)

head1.random = None
head1.next.random = head1
head1.next.next.random = head1.next.next.next.next
head1.next.next.next.random = head1.next.next
head1.next.next.next.next.random = head1

copied_head1 = copyRandomList(head1)
print(copied_head1.val)  # 7
