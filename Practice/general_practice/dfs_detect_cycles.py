from collections import defaultdict


def can_finish_dfs(numCourses, prerequisites):
    graph = defaultdict(list)
    for dest, src in prerequisites:
        graph[src].append(dest)

    visited = [0] * numCourses

    def dfs(course):
        if visited[course] == -1:
            return False
        if visited[course] == 1:
            return True

        visited[course] = -1

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        visited[course] = 1
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


numCourses1 = 2
prerequisites1 = [[1, 0]]
print(can_finish_dfs(numCourses1, prerequisites1))  # True

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(can_finish_dfs(numCourses2, prerequisites2))  # False
