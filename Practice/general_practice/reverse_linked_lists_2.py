class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    current = prev.next
    next_node = current.next

    for _ in range(right - left):
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
        next_node = current.next

    return dummy.next


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

left1 = 2
right1 = 4

new_head1 = reverseBetween(head1, left1, right1)

while new_head1:
    print(new_head1.val, end=" ")
    new_head1 = new_head1.next
