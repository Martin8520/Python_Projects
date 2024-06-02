from collections import Counter
import heapq


def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    result = [num for freq, num in heap]

    return result


nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(top_k_frequent(nums1, k1))  # [1, 2]

nums2 = [1]
k2 = 1
print(top_k_frequent(nums2, k2))  # [1]
