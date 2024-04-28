class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head and head.next:
        first_node = head
        second_node = head.next

        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev = first_node
        head = first_node.next

    return dummy.next


def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
printLinkedList(swapPairs(head1))

head2 = None
printLinkedList(swapPairs(head2))

head3 = ListNode(1)
printLinkedList(swapPairs(head3))
