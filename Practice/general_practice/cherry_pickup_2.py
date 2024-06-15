def cherryPickup(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[[-float('inf')] * cols for _ in range(cols)] for _ in range(rows)]
    dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]

    for i in range(rows - 1):
        for j1 in range(cols):
            for j2 in range(cols):
                if dp[i][j1][j2] == -float('inf'):
                    continue
                for new_j1 in [j1, j1 + 1, j1 - 1]:
                    for new_j2 in [j2, j2 + 1, j2 - 1]:
                        if 0 <= new_j1 < cols and 0 <= new_j2 < cols:
                            if new_j1 == new_j2:
                                dp[i + 1][new_j1][new_j2] = max(dp[i + 1][new_j1][new_j2],
                                                                dp[i][j1][j2] + grid[i + 1][new_j1])
                            else:
                                dp[i + 1][new_j1][new_j2] = max(dp[i + 1][new_j1][new_j2],
                                                                dp[i][j1][j2] + grid[i + 1][new_j1] + grid[i + 1][
                                                                    new_j2])

    result = 0
    for j1 in range(cols):
        for j2 in range(cols):
            result = max(result, dp[rows - 1][j1][j2])

    return result


print(cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))  # 24
print(cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                    [1, 0, 2, 3, 0, 0, 6]]))  # 28
