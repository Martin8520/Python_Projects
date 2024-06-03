import heapq


def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]


nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(find_kth_largest(nums1, k1))  # 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(find_kth_largest(nums2, k2))  # 4
