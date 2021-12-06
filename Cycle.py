"""
 How to find cycles in a Graph.
 A graph contains a cycle if during a graph traversal, we find a node whose neighbor
 (other than the previous node) has already been visited.


"""

from collections import defaultdict


def has_cycle(graph, start):
    visited = []

    def dfs(source):
        if source in visited:
            return True
        visited.append(source)
        for neighbor in graph[source]:
            if neighbor not in visited:
                dfs(neighbor)
        return False

    return dfs(start)


def bipartite_conflict(graph):
    colors = {}

    numVertices = len(graph)

    def dfs(currentNode, currentColor):
        if currentNode in colors:
            if colors[currentNode] != currentColor:
                return False
            else:
                return True
        else:
            colors[currentNode] = currentColor
        for node_ in graph[currentNode]:
            if not dfs(node_, not currentColor):
                return False
        return True

    for node in range(numVertices):
        if node not in colors:
            if not dfs(node, True):
                return False
        return True


if __name__ == '__main__':

    edges = []
    adjList = defaultdict(list)
    for u, v in edges:
        adjList[u].append(v)
    bipartite_conflict(adjList)
