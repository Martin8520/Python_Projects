class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    def split(head: ListNode):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        return head, mid

    def merge(l1: ListNode, l2: ListNode):
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next

    def mergeSort(head: ListNode):
        if not head or not head.next:
            return head
        left, right = split(head)
        return merge(mergeSort(left), mergeSort(right))

    return mergeSort(head)


def list_to_linked_list(lst):
    if not lst:
        return None
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
sorted_head = sortList(head)
print(linked_list_to_list(sorted_head))  # [1, 2, 3, 4]

head = list_to_linked_list([-1, 5, 3, 4, 0])
sorted_head = sortList(head)
print(linked_list_to_list(sorted_head))  # [-1, 0, 3, 4, 5]

head = list_to_linked_list([])
sorted_head = sortList(head)
print(linked_list_to_list(sorted_head))  # []
