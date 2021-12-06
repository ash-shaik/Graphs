"""
 How to find cycles in a Graph.
"""

from collections import defaultdict


def find_cycle(graph):
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

    find_cycle(adjList)
