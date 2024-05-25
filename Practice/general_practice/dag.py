from collections import defaultdict, deque


def find_longest_path(n, m, edges):
    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)

    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    topo_order = []
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    dp = [0] * (n + 1)

    for u in topo_order:
        for v in adj_list[u]:
            dp[v] = max(dp[v], dp[u] + 1)

    return max(dp)


n = 6
m = 6
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
    (4, 5),
    (5, 6)
]
print(find_longest_path(n, m, edges))  # 4
