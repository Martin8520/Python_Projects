from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0

            gold = grid[x][y]

            grid[x][y] = 0

            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))

            grid[x][y] = gold

            return gold + max_gold

        max_gold_collected = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold_collected = max(max_gold_collected, dfs(i, j))

        return max_gold_collected


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
solution = Solution()
result = solution.getMaximumGold(grid)
print(result)
