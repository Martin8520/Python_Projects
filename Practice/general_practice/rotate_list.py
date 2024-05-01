class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    if not head or k == 0:
        return head

    length = 1
    tail = head
    while tail.next:
        length += 1
        tail = tail.next

    k %= length

    if k == 0:
        return head

    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    new_tail.next = None
    tail.next = head

    return new_head


def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)

print("Original list 1:")
printList(head1)
print("\nRotated list 1:")
printList(rotateRight(head1, 2))

print("\nOriginal list 2:")
printList(head2)
print("\nRotated list 2:")
printList(rotateRight(head2, 4))
