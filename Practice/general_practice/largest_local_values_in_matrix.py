from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                localMax = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        localMax = max(localMax, grid[x][y])
                maxLocal[i][j] = localMax

        return maxLocal


grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
solution = Solution()
result = solution.largestLocal(grid)
print(result)
