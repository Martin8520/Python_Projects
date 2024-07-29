def findFarmland(land):
    def dfs(r, c):
        nonlocal min_row, max_row, min_col, max_col
        if r < 0 or r >= m or c < 0 or c >= n or land[r][c] == 0:
            return
        land[r][c] = 0
        min_row, max_row = min(min_row, r), max(max_row, r)
        min_col, max_col = min(min_col, c), max(max_col, c)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    m, n = len(land), len(land[0])
    result = []

    for r in range(m):
        for c in range(n):
            if land[r][c] == 1:
                min_row = max_row = r
                min_col = max_col = c
                dfs(r, c)
                result.append([min_row, min_col, max_row, max_col])

    return result


land1 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
print(findFarmland(land1))  # [[0, 0, 0, 0], [1, 1, 2, 2]]

land2 = [[1, 1], [1, 1]]
print(findFarmland(land2))  # [[0, 0, 1, 1]]

land3 = [[0]]
print(findFarmland(land3))  # []
