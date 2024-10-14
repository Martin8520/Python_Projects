import heapq


def maxProbability(n, edges, succProb, start, end):
    adj = [[] for _ in range(n)]

    for i, (u, v) in enumerate(edges):
        adj[u].append((v, succProb[i]))
        adj[v].append((u, succProb[i]))

    prob = [0] * n
    prob[start] = 1
    pq = [(-1, start)]

    while pq:
        p, node = heapq.heappop(pq)
        p = -p

        if node == end:
            return p

        for neighbor, edge_prob in adj[node]:
            new_prob = p * edge_prob
            if new_prob > prob[neighbor]:
                prob[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))

    return 0


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))

n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.3]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))

n = 3
edges = [[0, 1]]
succProb = [0.5]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))
