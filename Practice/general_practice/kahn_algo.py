from collections import deque, defaultdict


def can_finish_bfs(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited = 0

    while queue:
        course = queue.popleft()
        visited += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited == numCourses


numCourses1 = 2
prerequisites1 = [[1, 0]]
print(can_finish_bfs(numCourses1, prerequisites1))  # True

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(can_finish_bfs(numCourses2, prerequisites2))  # False
