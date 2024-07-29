from collections import deque, defaultdict


def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    queue = deque([source])
    visited = set()

    while queue:
        current = queue.popleft()
        if current == destination:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return False


n1 = 3
edges1 = [[0, 1], [1, 2], [2, 0]]
source1 = 0
destination1 = 2
print(validPath(n1, edges1, source1, destination1))  # True

n2 = 6
edges2 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source2 = 0
destination2 = 5
print(validPath(n2, edges2, source2, destination2))  # False
