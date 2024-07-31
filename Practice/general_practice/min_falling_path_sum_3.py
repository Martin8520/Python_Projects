def minFallingPathSum(grid):
    n = len(grid)
    if n == 1:
        return grid[0][0]

    dp = [[float('inf')] * n for _ in range(n)]
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(n):
            min_prev_row = float('inf')
            for k in range(n):
                if k != j:
                    min_prev_row = min(min_prev_row, dp[i - 1][k])
            dp[i][j] = grid[i][j] + min_prev_row

    return min(dp[-1])


grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(minFallingPathSum(grid1))  # 13

grid2 = [[7]]
print(minFallingPathSum(grid2))  # 7
