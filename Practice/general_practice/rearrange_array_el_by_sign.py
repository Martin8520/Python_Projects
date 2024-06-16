def rearrangeArray(nums):
    positive_nums = [num for num in nums if num > 0]
    negative_nums = [num for num in nums if num < 0]

    result = []
    for pos, neg in zip(positive_nums, negative_nums):
        result.append(pos)
        result.append(neg)

    return result


nums1 = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums1))  # [3, -2, 1, -5, 2, -4]

nums2 = [-1, 1]
print(rearrangeArray(nums2))  # [1, -1]
