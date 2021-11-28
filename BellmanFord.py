"""
Find shortest path in a weighted graph with negative weights.
- Considers weight of an edge between vertex.
- Not a greedy algorithm.
  Search all adjacent vertices (neighbors) of a particular vertex.
  not just the one with lowest weight/distance.

- If there is a cycle, we need to detect it , otherwise it will make the
  path between two vertices longer than the longest possible path in a graph.
  Time Complexity : O( E * V)


"""

from Dijkstra import WeightedGraph
from collections import defaultdict


def bellmanFordShortestPath(Graph, source, target):
    weightMap = defaultdict(lambda: float('inf'))
    weightMap[source] = 0

    for i in range(Graph.numNodes - 1):
        for u, v, weight in Graph.weightedAdjList:
            oldCost = weightMap[v]
            newCost = weightMap[u] + weight

            if weightMap[u] != float('inf') and newCost < oldCost:
                weightMap[v] = newCost

    for u, v, weight in Graph.weightedAdjList:
        oldCost = weightMap[v]
        newCost = weightMap[u] + weight

        if weightMap[u] != float('inf') and newCost < oldCost:
            print("Graph contains negative cycle")
            break
    print(weightMap)


if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [3, 1], [2, 4], [4, 1], [4, 3]]
    weights = [2, 3, 2, 6, -5, -6]
    weightedGraph = WeightedGraph(5, edges, weights)
    source, target = 0, 3
    bellmanFordShortestPath(weightedGraph, source, target)
