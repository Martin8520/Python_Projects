def findPaths(m, n, maxMove, startRow, startColumn):
    MOD = 10**9 + 7
    dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]

    for move in range(1, maxMove + 1):
        for i in range(m):
            for j in range(n):
                ways = 0
                if i == 0: ways += 1
                else: ways += dp[move - 1][i - 1][j]
                if i == m - 1: ways += 1
                else: ways += dp[move - 1][i + 1][j]
                if j == 0: ways += 1
                else: ways += dp[move - 1][i][j - 1]
                if j == n - 1: ways += 1
                else: ways += dp[move - 1][i][j + 1]
                dp[move][i][j] = ways % MOD

    return dp[maxMove][startRow][startColumn]

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(findPaths(m, n, maxMove, startRow, startColumn))  # 6

m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
print(findPaths(m, n, maxMove, startRow, startColumn))  # 12
