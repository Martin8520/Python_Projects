class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def minimum_cost_to_connect_cities(n, edges):
    if n == 1:
        return 0
    if m == 0:
        return -1

    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_cost = 0
    edges_used = 0

    for u, v, cost in edges:
        if uf.union(u - 1, v - 1):
            mst_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                return mst_cost

    return -1


n, m = 4, 5
edges = [
    (1, 2, 1),
    (2, 3, 4),
    (3, 4, 3),
    (4, 1, 2),
    (1, 3, 5)
]
print(minimum_cost_to_connect_cities(n, edges))  # 6
