"""
 It involves constructing a distance matrix,
 The algorithm initializes D to L, that is, to the direct distances between nodes.
 It then does n iterations, after iteration k, D gives the length of the shortest paths
 that only use nodes in {1,2….k} as intermediate nodes.
 Time Complexity : O(V3)
"""

from copy import deepcopy

INF = float('inf')


def floyd_warshall(Graph):
    numVertices = len(Graph)
    graphDistance = deepcopy(Graph)
    # print(gCopy)

    for r in range(numVertices):
        for node1 in range(numVertices):
            for node2 in range(numVertices):
                graphDistance[node1][node2] = min(graphDistance[node1][node2]
                                                  , graphDistance[node1][r] + graphDistance[r][node2])
    printCosts(numVertices, graphDistance)


def printCosts(numVertices, graphDistance):
    for i in range(numVertices):
        for j in range(numVertices):
            if graphDistance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(graphDistance[i][j], end=" ")
        print(" ")


if __name__ == '__main__':
    Graph = [
        [0, 5, INF, INF],
        [50, 0, 15, 5],
        [30, INF, 0, 15],
        [15, INF, 5, 0]]

    floyd_warshall(Graph)
