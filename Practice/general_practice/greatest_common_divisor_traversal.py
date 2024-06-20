import math
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

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


def prime_factors(x):
    factors = set()
    while x % 2 == 0:
        factors.add(2)
        x //= 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            factors.add(i)
            x //= i
    if x > 2:
        factors.add(x)
    return factors


def can_traverse_all_pairs(nums):
    n = len(nums)
    uf = UnionFind(n)
    prime_to_indices = defaultdict(list)

    for idx, num in enumerate(nums):
        primes = prime_factors(num)
        for prime in primes:
            prime_to_indices[prime].append(idx)

    for indices in prime_to_indices.values():
        for i in range(1, len(indices)):
            uf.union(indices[0], indices[i])

    root = uf.find(0)
    for i in range(1, n):
        if uf.find(i) != root:
            return False
    return True


print(can_traverse_all_pairs([2, 3, 6]))  # True
print(can_traverse_all_pairs([3, 9, 5]))  # False
print(can_traverse_all_pairs([4, 3, 12, 8]))  # True
