from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        print("Sorted workers by ratio:", workers)

        heap = []
        sumQ = 0
        ans = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            sumQ += q
            print("Current heap:", heap)
            print("Current sumQ:", sumQ)

            if len(heap) > k:
                sumQ += heapq.heappop(heap)
                print("Popped from heap, new sumQ:", sumQ)

            if len(heap) == k:
                ans = min(ans, sumQ * ratio)
                print("Current answer:", ans)

        return ans


quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2

solution = Solution()
result = solution.mincostToHireWorkers(quality, wage, k)
print("Minimum cost to hire k workers:", result)
