import heapq


def dijkstra(n, adj, source):
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for nei, w in adj[node]:
            new_dist = d + w
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(pq, (new_dist, nei))

    return dist


def modifiedGraphEdges(n, edges, source, destination, target):
    adj = [[] for _ in range(n)]

    for u, v, w in edges:
        if w != -1:
            adj[u].append((v, w))
            adj[v].append((u, w))

    initial_dist = dijkstra(n, adj, source)[destination]

    if initial_dist < target:
        return []

    if initial_dist == target:
        return [[u, v, w if w != -1 else 1] for u, v, w in edges]

    for i, (u, v, w) in enumerate(edges):
        if w == -1:
            edges[i][2] = 1
            adj[u].append((v, 1))
            adj[v].append((u, 1))

    dist_with_minimal_ones = dijkstra(n, adj, source)[destination]

    if dist_with_minimal_ones > target:
        return []

    for i, (u, v, w) in enumerate(edges):
        if w == -1:
            adj[u].pop()
            adj[v].pop()

    low, high = 1, 2 * 10 ** 9

    while low < high:
        mid = (low + high) // 2

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            if w != -1:
                adj[u].append((v, w))
                adj[v].append((u, w))
            else:
                adj[u].append((v, mid))
                adj[v].append((u, mid))

        dist = dijkstra(n, adj, source)[destination]

        if dist < target:
            low = mid + 1
        else:
            high = mid

    for i, (u, v, w) in enumerate(edges):
        if w == -1:
            edges[i][2] = low

    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    final_dist = dijkstra(n, adj, source)[destination]

    return edges if final_dist == target else []


n1 = 5
edges1 = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
source1 = 0
destination1 = 1
target1 = 5
print(modifiedGraphEdges(n1, edges1, source1, destination1, target1))

n2 = 3
edges2 = [[0, 1, -1], [0, 2, 5]]
source2 = 0
destination2 = 2
target2 = 6
print(modifiedGraphEdges(n2, edges2, source2, destination2, target2))

n3 = 4
edges3 = [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]]
source3 = 0
destination3 = 2
target3 = 6
print(modifiedGraphEdges(n3, edges3, source3, destination3, target3))
