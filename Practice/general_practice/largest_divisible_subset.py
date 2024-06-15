def largestDivisibleSubset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)

    dp = [1] * n
    parent = [-1] * n
    max_size = 0
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
        if dp[i] > max_size:
            max_size = dp[i]
            max_index = i

    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = parent[max_index]

    result.reverse()
    return result


print(largestDivisibleSubset([1, 2, 3]))  # [1, 2]
print(largestDivisibleSubset([1, 2, 4, 8]))  # [1, 2, 4, 8]
