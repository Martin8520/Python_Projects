class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


head = ListNode(4)
node1 = ListNode(5)
node2 = ListNode(1)
node3 = ListNode(9)
head.next = node1
node1.next = node2
node2.next = node3

deleteNode(node1)

current = head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
