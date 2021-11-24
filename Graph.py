from collections import defaultdict, deque


class Graph:
    """Undirected Graph class"""

    def __init__(self, numNodes, edges):
        self.adjList = defaultdict(list)
        self.numNodes = numNodes
        for v1, v2 in edges:
            self.adjList[v1].append(v2)
            self.adjList[v2].append(v1)

    def dfs(self, source, visited):
        """
        Traverse graph from the source in preorder.
        PreOrder : Visit each node before its children.
        Time complexity : O(E + V), with num edges varying from O(1) in a Sparse Graph
        to O(V2) in a Dense Graph.
        :param source:
        :param visited:
        :return:

        """
        visited.append(source)
        print(source, end=' ')
        for neighbor in self.adjList[source]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def dfs_iter(self, source, visited):
        stack = deque()
        stack.append(source)
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                print(current, end=' ')
                for neighbor in reversed(self.adjList[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)


def search_helper(graph):
    visited = []

    for i in range(graph.numNodes):
        if i not in visited:
            graph.dfs(i, visited)


def search_iterative(graph):
    visited = []
    for i in range(graph.numNodes):
        if i not in visited:
            graph.dfs_iter(i, visited)


if __name__ == '__main__':
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
    n = 13

    graph = Graph(13, edges)
    search_helper(graph)
    print('\n')
    search_iterative(graph)
