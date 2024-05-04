class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        if current.next and current.val == current.next.val:
            while current.next and current.val == current.next.val:
                current = current.next
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next

    return dummy.next


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(4)
head1.next.next.next.next.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(1)
head2.next.next = ListNode(1)
head2.next.next.next = ListNode(2)
head2.next.next.next.next = ListNode(3)

printLinkedList(deleteDuplicates(head1))
printLinkedList(deleteDuplicates(head2))
