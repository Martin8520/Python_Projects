# Definition for singly-linked list.
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


def removeNodes(head):
    reversed_head = reverseList(head)

    max_value = float('-inf')
    current = reversed_head
    new_head = None
    while current:
        if current.val >= max_value:
            max_value = current.val
            new_node = ListNode(current.val)
            new_node.next = new_head
            new_head = new_node
        current = current.next

    return reverseList(new_head)


head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

modified_head = removeNodes(head)

current = modified_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
