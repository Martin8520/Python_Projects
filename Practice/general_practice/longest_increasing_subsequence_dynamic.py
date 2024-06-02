def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums1))  # 4

nums2 = [0, 1, 0, 3, 2, 3]
print(length_of_lis(nums2))  # 4

nums3 = [7, 7, 7, 7, 7, 7, 7]
print(length_of_lis(nums3))  # 1
