"""
 Undirected Graph class with Adjacency Matrix internal data structure.
"""


class AMGraph:

    def __init__(self, nV, edges):
        self.numVertices = nV
        """
         Bit mask optimization, 
         store A[i][j] as bits of 32 or 64-bit integers.
        """
        self.adjMat = [[0 for i in range(nV)] for j in range(nV)]
        for u, v in edges:
            self.adjMat[u][v] = 1
            self.adjMat[v][u] = 1
        # print(self.adjMat)

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
        Time Complexity : O(|V|3), lets improve this by bitmask optimization
        Allows for parallel operations.

        """
        N = self.numVertices
        for u in range(N):
            for v in range(u + 1, N):
                if self.adjMat[u][v] == 0:
                    continue
                # if there is an edge between u and v, continue to third point
                for w in range(v + 1, N):
                    if self.adjMat[u][w] == 1 and self.adjMat[v][w] == 1:
                        return True
        return False

    def cycleOfLength4(self):
        """
        Check if there exits a cycle of length 4.
        :return: boolean, True if cycle exists, False if not.
        Time Complexity : O(|V|4)
        """
        N = self.numVertices
        for u in range(N):
            for v in range(u + 1, N):
                if self.adjMat[u][v] == 0:
                    continue
                # if there is an edge between u and v, continue to third point
                for w in range(v + 1, N):
                    if self.adjMat[v][w] == 0:
                        continue
                    for x in range(w + 1, N):
                        if self.adjMat[w][x] == 1 and self.adjMat[u][x] == 1:
                            return True
        return False


if __name__ == '__main__':
    numVertices = 4
    edges = [[0, 1], [0, 2], [1, 3]]
    graph = AMGraph(4, edges)
    graph.bfs(0)

    edges = [
        [0, 1], [0, 3], [1, 2], [1, 4], [2, 3], [3, 4]
    ]
    aGraph = AMGraph(5, edges)
    print(aGraph.cycleOfLength4())
