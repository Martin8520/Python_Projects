import heapq


def furthestBuilding(heights, bricks, ladders):
    min_heap = []
    n = len(heights)

    for i in range(n - 1):
        diff = heights[i + 1] - heights[i]

        if diff > 0:
            heapq.heappush(min_heap, diff)

        if len(min_heap) > ladders:
            bricks -= heapq.heappop(min_heap)

        if bricks < 0:
            return i

    return n - 1


print(furthestBuilding([4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))  # 4
print(furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))  # 7
print(furthestBuilding([14, 3, 19, 3], bricks=17, ladders=0))  # 3
