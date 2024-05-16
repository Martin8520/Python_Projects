class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half_head = slow.next
    slow.next = None

    prev = None
    current = second_half_head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    second_half_head = prev

    first_half = head
    second_half = second_half_head

    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next

        first_half.next = second_half
        second_half.next = temp1

        first_half = temp1
        second_half = temp2

    return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
print("Input:")
printList(head1)
reorderList(head1)
print("Output:")
printList(head1)

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
print("\nInput:")
printList(head2)
reorderList(head2)
print("Output:")
printList(head2)
