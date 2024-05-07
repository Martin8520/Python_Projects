def numTrees(n):
    if n == 0:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]


n1 = 3
print(numTrees(n1))

n2 = 1
print(numTrees(n2))
