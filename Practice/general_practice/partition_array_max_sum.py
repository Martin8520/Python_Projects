def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * n

    for i in range(n):
        max_val = 0
        for j in range(1, k + 1):
            if i - j + 1 >= 0:
                max_val = max(max_val, arr[i - j + 1])
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] + max_val * j)
                else:
                    dp[i] = max(dp[i], max_val * j)

    return dp[-1]


arr1 = [1, 15, 7, 9, 2, 5, 10]
k1 = 3
print(maxSumAfterPartitioning(arr1, k1))  # 84

arr2 = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
k2 = 4
print(maxSumAfterPartitioning(arr2, k2))  # 83

arr3 = [1]
k3 = 1
print(maxSumAfterPartitioning(arr3, k3))  # 1
