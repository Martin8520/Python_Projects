class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def doubleLinkedList(head: ListNode) -> ListNode:
    head = reverseLinkedList(head)

    carry = 0
    current = head

    while current:
        total = current.val * 2 + carry
        current.val = total % 10
        carry = total // 10

        if current.next is None and carry > 0:
            current.next = ListNode(carry)
            carry = 0

        current = current.next

    head = reverseLinkedList(head)

    return head


def printLinkedList(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


head1 = ListNode(1)
head1.next = ListNode(8)
head1.next.next = ListNode(9)

new_head1 = doubleLinkedList(head1)

printLinkedList(new_head1)  # 3 -> 7 -> 8

head2 = ListNode(9)
head2.next = ListNode(9)
head2.next.next = ListNode(9)

new_head2 = doubleLinkedList(head2)

printLinkedList(new_head2)  # 2 -> 9 -> 9 -> 8
