from collections import defaultdict, deque


def bfs_farthest_node(start, n, graph):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])

    farthest_node = start
    max_distance = 0

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > max_distance:
                    max_distance = dist[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_distance


def tree_diameter(n, edges):
    if n == 1:
        return 0

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    node_A, _ = bfs_farthest_node(1, n, graph)

    node_B, diameter = bfs_farthest_node(node_A, n, graph)

    return diameter


n = 5
edges = [
    (1, 2),
    (1, 3),
    (3, 4),
    (3, 5)
]
print(tree_diameter(n, edges))  # 3
