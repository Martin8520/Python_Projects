def longestConsecutive(nums):
    if not nums:
        return 0

    numset = set(nums)
    max_length = 0

    for num in nums:
        if num - 1 not in numset:
            cur_length = 1
            next_num = num + 1

            while next_num in numset:
                cur_length += 1
                next_num += 1

            max_length = max(max_length, cur_length)

    return max_length


nums1 = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums1))  # 4

nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums2))  # 9
