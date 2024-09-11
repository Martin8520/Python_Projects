from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        safeness = [[float('inf')] * n for _ in range(n)]
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    safeness[r][c] = 0

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safeness[nr][nc] == float('inf'):
                    safeness[nr][nc] = safeness[r][c] + 1
                    queue.append((nr, nc))

        print("Safeness Matrix:")
        for row in safeness:
            print(row)

        def can_reach_with_safeness(mid):
            if safeness[0][0] < mid:
                return False

            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True

            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and safeness[nr][nc] >= mid:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            return False

        low, high = 0, min(safeness[0][0], safeness[n - 1][n - 1])
        print(f"Binary Search Start: low={low}, high={high}")
        while low < high:
            mid = (high + low + 1) // 2
            print(f"Checking mid: {mid}")
            if can_reach_with_safeness(mid):
                print(f"Can reach with safeness {mid}")
                low = mid
            else:
                print(f"Cannot reach with safeness {mid}")
                high = mid - 1

        print(f"Final Safeness Factor: {low}")
        return low


grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
solution = Solution()
result = solution.maximumSafenessFactor(grid)
print("Result:", result)
