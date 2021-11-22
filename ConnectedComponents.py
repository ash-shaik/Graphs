"""
Calculate the number of connected components in an undirected graph.
We are given an edgeList in no particular order.

1. Build the graph from teh given input edgeList.
2. Follow DFS/BFS to explore the vertices until all are explored.
3. Outer loop going over each vertex.
4. THe number of DFS/BFS triggered on such a graph gives us the number of connected components.
"""

from collections import defaultdict
import numpy as np


def naiveNumConnectedComponentsInUDG(n, edges):
    if 0 >= n <= 1:
        return n

    adjList = defaultdict(list)
    for edge in edges:
        if np.isscalar(edge):
            if edge not in adjList:
                adjList[edge].append(edge)
        else:
            v1, v2 = edge
            adjList[v1].append(v2)
            adjList[v2].append(v1)
    # print(adjList)
    cc_count = 0
    visited = []
    for vertex in range(n):
        if vertex not in visited:
            cc_count += 1
            dfs(adjList, vertex, visited)
    return cc_count


def dfs(adjList, source, visited):
    visited.append(source)
    for neighbor in adjList[source]:
        if neighbor not in visited:
            dfs(adjList, neighbor, visited)


if __name__ == '__main__':
    num_nodes = 5
    edges = [[0, 1], [1, 2], [3, 4]]

    print(naiveNumConnectedComponentsInUDG(num_nodes, edges))

    num_nodes = 50
    edges = [3, 2, [0, 0], [1, 1], [2, 2]]
    print(naiveNumConnectedComponentsInUDG(num_nodes, edges))
