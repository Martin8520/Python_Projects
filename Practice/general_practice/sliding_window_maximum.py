from collections import deque


def max_sliding_window(nums, k):
    if not nums:
        return []

    deq = deque()
    result = []

    for i in range(len(nums)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
print(max_sliding_window(nums1, k1))  # [3, 3, 5, 5, 6, 7]

nums2 = [1]
k2 = 1
print(max_sliding_window(nums2, k2))  # [1]
