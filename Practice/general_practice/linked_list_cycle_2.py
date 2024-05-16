class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next
cycle_start_node1 = detectCycle(head1)
if cycle_start_node1:
    print("Output: tail connects to node index", cycle_start_node1.val)
else:
    print("Output: no cycle")

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2
cycle_start_node2 = detectCycle(head2)
if cycle_start_node2:
    print("Output: tail connects to node index", cycle_start_node2.val)
else:
    print("Output: no cycle")

head3 = ListNode(1)
cycle_start_node3 = detectCycle(head3)
if cycle_start_node3:
    print("Output: tail connects to node index", cycle_start_node3.val)
else:
    print("Output: no cycle")
