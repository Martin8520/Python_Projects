def divideArray(nums, k):
    nums.sort()
    result = []
    i = 0

    while i < len(nums):
        if i + 2 < len(nums) and nums[i + 2] - nums[i] <= k:
            result.append([nums[i], nums[i + 1], nums[i + 2]])
            i += 3
        else:
            return []

    return result


nums1 = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k1 = 2
print(divideArray(nums1, k1))  # [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

nums2 = [1, 3, 3, 2, 7, 3]
k2 = 3
print(divideArray(nums2, k2))  # []
