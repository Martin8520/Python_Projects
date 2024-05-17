class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    current = head

    while current and current.next:
        if current.val <= current.next.val:
            current = current.next
        else:
            to_insert = current.next
            current.next = to_insert.next
            pre = dummy

            while pre.next.val < to_insert.val:
                pre = pre.next

            to_insert.next = pre.next
            pre.next = to_insert

    return dummy.next


def list_to_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst


head = list_to_linked_list([4, 2, 1, 3])
sorted_head = insertionSortList(head)
print(linked_list_to_list(sorted_head))  # [1, 2, 3, 4]

head = list_to_linked_list([-1, 5, 3, 4, 0])
sorted_head = insertionSortList(head)
print(linked_list_to_list(sorted_head))  # [-1, 0, 3, 4, 5]
