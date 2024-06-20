import heapq
import collections


def findCheapestPrice(n, flights, src, dst, k):
    graph = collections.defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    pq = [(0, src, 0)]
    costs = {(src, 0): 0}

    while pq:
        cost, current_city, stops = heapq.heappop(pq)

        if current_city == dst:
            return cost

        if stops <= k:
            for neighbor, price in graph[current_city]:
                new_cost = cost + price
                if new_cost < costs.get((neighbor, stops + 1), float('inf')):
                    costs[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))

    return -1


print(findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))  # 700
print(findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))  # 200
print(findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))  # 500
