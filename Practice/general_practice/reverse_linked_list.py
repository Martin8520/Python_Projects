class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseListIterative(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def display_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    return elements


head = create_linked_list([1, 2, 3, 4, 5])
reversed_head_iterative = reverseListIterative(head)
print(display_linked_list(reversed_head_iterative))  # [5, 4, 3, 2, 1]

head = create_linked_list([1, 2, 3, 4, 5])
reversed_head_recursive = reverseListRecursive(head)
print(display_linked_list(reversed_head_recursive))  # [5, 4, 3, 2, 1]

head = create_linked_list([1, 2])
reversed_head_iterative = reverseListIterative(head)
print(display_linked_list(reversed_head_iterative))  # [2, 1]

head = create_linked_list([1, 2])
reversed_head_recursive = reverseListRecursive(head)
print(display_linked_list(reversed_head_recursive))  # [2, 1]

head = create_linked_list([])
reversed_head_iterative = reverseListIterative(head)
print(display_linked_list(reversed_head_iterative))  # []

head = create_linked_list([])
reversed_head_recursive = reverseListRecursive(head)
print(display_linked_list(reversed_head_recursive))  # []
