import heapq


def findKthLargest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]


# Test cases
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  #: 4
print(findKthLargest([1], 1))  # 1
print(findKthLargest([2, 1], 2))  # 1
print(findKthLargest([7, 10, 4, 3, 20, 15], 3))  # 10
