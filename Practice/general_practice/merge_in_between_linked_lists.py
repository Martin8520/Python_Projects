class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    current = list1
    for _ in range(a - 1):
        current = current.next
    node_before_a = current

    current = node_before_a
    for _ in range(b - a + 2):
        current = current.next
    node_after_b = current

    node_before_a.next = list2

    current = list2
    while current.next:
        current = current.next

    current.next = node_after_b

    return list1


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


list1 = create_linked_list([10, 1, 13, 6, 9, 5])
list2 = create_linked_list([1000000, 1000001, 1000002])
a, b = 3, 4
result = mergeInBetween(list1, a, b, list2)
print(display_linked_list(result))  # [10, 1, 13, 1000000, 1000001, 1000002, 5]

list1 = create_linked_list([0, 1, 2, 3, 4, 5, 6])
list2 = create_linked_list([1000000, 1000001, 1000002, 1000003, 1000004])
a, b = 2, 5
result = mergeInBetween(list1, a, b, list2)
print(display_linked_list(result))  # [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
