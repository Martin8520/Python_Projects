class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def doubleLinkedList(head):
    head = reverseList(head)

    current = head
    carry = 0
    while current:
        doubled_value = current.val * 2 + carry
        carry = doubled_value // 10
        current.val = doubled_value % 10

        if not current.next and carry > 0:
            current.next = ListNode(carry)
            carry = 0

        current = current.next

    return reverseList(head)


head = ListNode(1)
head.next = ListNode(8)
head.next.next = ListNode(9)

new_head = doubleLinkedList(head)

current = new_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
