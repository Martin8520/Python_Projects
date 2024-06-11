def kInversePairs(n, k):
    MOD = 10 ** 9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(0, k + 1):
            dp[i][j] = dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]
            if j - i >= 0:
                dp[i][j] -= dp[i - 1][j - i]
            dp[i][j] %= MOD

    return dp[n][k]


n = 3
k = 0
print(kInversePairs(n, k))  # 1

n = 3
k = 1
print(kInversePairs(n, k))  # 2
