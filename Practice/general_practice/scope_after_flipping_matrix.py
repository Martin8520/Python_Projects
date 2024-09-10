from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        for j in range(1, n):
            ones_count = sum(grid[i][j] for i in range(m))
            if ones_count < m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        score = 0
        for i in range(m):
            row_value = 0
            for j in range(n):
                row_value = row_value * 2 + grid[i][j]
            score += row_value

        return score


grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
solution = Solution()
result = solution.matrixScore(grid)
print(result)
