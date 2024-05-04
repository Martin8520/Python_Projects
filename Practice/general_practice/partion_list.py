class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    before_head = ListNode(0)
    after_head = ListNode(0)

    before = before_head
    after = after_head

    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    after.next = None
    before.next = after_head.next

    return before_head.next


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(2)

head2 = ListNode(2)
head2.next = ListNode(1)

printLinkedList(partition(head1, 3))
printLinkedList(partition(head2, 2))
