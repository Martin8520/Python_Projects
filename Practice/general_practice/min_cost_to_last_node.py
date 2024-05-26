import heapq


def dijkstra(n, graph, start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def find_minimum_cost(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        graph[u].append((v, c))

    distances = dijkstra(n, graph, 1)

    return distances[n] if distances[n] != float('inf') else -1


n = 5
m = 6
edges = [
    (1, 2, 2),
    (1, 3, 4),
    (2, 4, 7),
    (3, 4, 3),
    (4, 5, 1),
    (2, 3, 1)
]
print(find_minimum_cost(n, edges))  # 7
