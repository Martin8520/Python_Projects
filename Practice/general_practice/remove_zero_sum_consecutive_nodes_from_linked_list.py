class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeZeroSumSublists(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = {}
    current = dummy
    current_sum = 0

    while current:
        current_sum += current.val
        prefix_sum[current_sum] = current
        current = current.next

    current = dummy
    current_sum = 0
    while current:
        current_sum += current.val
        current.next = prefix_sum[current_sum].next
        current = current.next

    return dummy.next


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


head = create_linked_list([1, 2, -3, 3, 1])
new_head = removeZeroSumSublists(head)
print(linked_list_to_list(new_head))  # [3, 1]

head = create_linked_list([1, 2, 3, -3, 4])
new_head = removeZeroSumSublists(head)
print(linked_list_to_list(new_head))  # [1, 2, 4]

head = create_linked_list([1, 2, 3, -3, -2])
new_head = removeZeroSumSublists(head)
print(linked_list_to_list(new_head))  # [1]
