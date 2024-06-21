class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next


def create_linked_list(elements):
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    return elements


head = create_linked_list([1, 2, 3, 4, 5])
n = 2
new_head = removeNthFromEnd(head, n)
print(linked_list_to_list(new_head))  # [1, 2, 3, 5]

head = create_linked_list([1])
n = 1
new_head = removeNthFromEnd(head, n)
print(linked_list_to_list(new_head))  # []

head = create_linked_list([1, 2])
n = 1
new_head = removeNthFromEnd(head, n)
print(linked_list_to_list(new_head))  # [1]
