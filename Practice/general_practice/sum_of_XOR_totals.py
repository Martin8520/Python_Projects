def subsetXORSum(nums):
    n = len(nums)
    total_sum = 0

    for i in range(1 << n):
        xor_total = 0
        for j in range(n):

            if i & (1 << j):
                xor_total ^= nums[j]
        total_sum += xor_total

    return total_sum


nums1 = [1, 3]
print("Result for nums = [1, 3]:", subsetXORSum(nums1))  # 6

nums2 = [5, 1, 6]
print("Result for nums = [5, 1, 6]:", subsetXORSum(nums2))  # 28

nums3 = [3, 4, 5, 6, 7, 8]
print("Result for nums = [3, 4, 5, 6, 7, 8]:", subsetXORSum(nums3))  # 480
