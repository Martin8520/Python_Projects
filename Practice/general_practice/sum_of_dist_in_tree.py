def sumOfDistancesInTree(n, edges):
    from collections import defaultdict

    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    subtreeSize = [0] * n
    sumDist = [0] * n

    def dfs1(node, parent):
        subtreeSize[node] = 1
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs1(neighbor, node)
            subtreeSize[node] += subtreeSize[neighbor]
            sumDist[0] += sumDist[neighbor] + subtreeSize[neighbor]

    dfs1(0, -1)

    def dfs2(node, parent):
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            sumDist[neighbor] = sumDist[node] - subtreeSize[neighbor] + (n - subtreeSize[neighbor])
            dfs2(neighbor, node)

    dfs2(0, -1)

    return sumDist


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
print(sumOfDistancesInTree(n, edges))  # [8, 12, 6, 10, 10, 10]

n = 1
edges = []
print(sumOfDistancesInTree(n, edges))  # [0]

n = 2
edges = [[1, 0]]
print(sumOfDistancesInTree(n, edges))  # [1, 1]
