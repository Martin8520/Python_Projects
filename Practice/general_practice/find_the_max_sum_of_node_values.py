from collections import defaultdict


class Solution:
    def maximumSum(self, nums, k, edges):
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            no_xor_sum = nums[node]
            xor_sum = nums[node] ^ k

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    sub_no_xor, sub_xor = dfs(neighbor)

                    no_xor_sum += max(sub_no_xor, sub_xor)
                    xor_sum += max(sub_no_xor ^ k, sub_xor ^ k)

            return no_xor_sum, xor_sum

        result = dfs(0)

        return max(result)


sol = Solution()

nums = [1, 2, 1]
k = 3
edges = [[0, 1], [0, 2]]
print(sol.maximumSum(nums, k, edges))

nums = [2, 3]
k = 7
edges = [[0, 1]]
print(sol.maximumSum(nums, k, edges))

nums = [7, 7, 7, 7, 7, 7]
k = 3
edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
print(sol.maximumSum(nums, k, edges))
