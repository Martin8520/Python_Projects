class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None

    clone_map = {}

    def dfs(original_node):
        if original_node in clone_map:
            return clone_map[original_node]

        clone_node = Node(original_node.val)

        clone_map[original_node] = clone_node

        for neighbor in original_node.neighbors:
            clone_node.neighbors.append(dfs(neighbor))

        return clone_node

    return dfs(node)


adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
original_graph1 = [Node(i) for i in range(1, len(adjList1) + 1)]
for i, neighbors in enumerate(adjList1):
    original_graph1[i].neighbors = [original_graph1[j - 1] for j in neighbors]
cloned_graph1 = cloneGraph(original_graph1[0])
print(cloned_graph1.val)  # 1

adjList2 = [[]]
original_graph2 = [Node(i) for i in range(1, len(adjList2) + 1)]
for i, neighbors in enumerate(adjList2):
    original_graph2[i].neighbors = [original_graph2[j - 1] for j in neighbors]
cloned_graph2 = cloneGraph(original_graph2[0])
print(cloned_graph2.val)  # 1

adjList3 = []
if adjList3:
    original_graph3 = [Node(i) for i in range(1, len(adjList3) + 1)]
    for i, neighbors in enumerate(adjList3):
        original_graph3[i].neighbors = [original_graph3[j - 1] for j in neighbors]
    cloned_graph3 = cloneGraph(original_graph3[0])
    print(cloned_graph3.val)  # None
else:
    cloned_graph3 = cloneGraph(None)
    print(cloned_graph3)  # None
