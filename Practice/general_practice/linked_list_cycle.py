class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next
print(hasCycle(head1))  # True

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2
print(hasCycle(head2))  # True

head3 = ListNode(1)
print(hasCycle(head3))  # False
