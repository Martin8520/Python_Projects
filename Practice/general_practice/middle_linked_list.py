class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


head = create_linked_list([1, 2, 3, 4, 5])
middle = middleNode(head)
print_linked_list(middle)  # [3, 4, 5]

head = create_linked_list([1, 2, 3, 4, 5, 6])
middle = middleNode(head)
print_linked_list(middle)  # [4, 5, 6]
