"""
 Graph class with Adjacency Matrix internal data structure.
"""


class AMGraph:

    def __init__(self, nV, edges):
        self.numVertices = nV
        self.adjMat = [[0 for i in range(nV)] for j in range(nV)]
        for u, v in edges:
            self.adjMat[u][v] = 1
            self.adjMat[v][u] = 1

    def bfs(self, source):
        visited = [False] * self.numVertices
        stack = [source]
        visited[source] = True

        while stack:
            node = stack.pop(0)
            print(node, end=' ')

            for i in range(self.numVertices):
                if self.adjMat[node][i] == 1 and not visited[i]:
                    stack.append(i)
                    visited[i] = True

    def cycleOfLength(self, n):
        """
        Check if there exits a cycle of length n.
        :param n: length of cycle we are looking for.
        :return: boolean, True if cycle exists, False if not.
        """
        for u in range(n):
            for v in range(u + 1, n):
                if self.adjMat[u][v] == 1:
                    continue
                for w in range(v + 1, n):
                    if self.adjMat[u][w] == 1 and self.adjMat[v][w] == 1:
                        return True
        return False


if __name__ == '__main__':
    numVertices = 4
    edges = [[0, 1], [0, 2], [1, 3]]
    graph = AMGraph(5, edges)
    graph.bfs(0)
    print(graph.cycleOfLength(3))
