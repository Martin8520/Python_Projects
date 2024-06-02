import bisect


def length_of_lis(nums):
    if not nums:
        return 0

    lis = []

    for num in nums:
        pos = bisect.bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num

    return len(lis)


nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums1))  # 4

nums2 = [0, 1, 0, 3, 2, 3]
print(length_of_lis(nums2))  # 4

nums3 = [7, 7, 7, 7, 7, 7, 7]
print(length_of_lis(nums3))  # 1
