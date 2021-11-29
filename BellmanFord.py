"""
Find shortest path in a weighted graph with negative weights.
- Considers weight of an edge between vertex.
- Not a greedy algorithm.
  Search all adjacent vertices (neighbors) of a particular vertex.
  not just the one with lowest weight/distance.

- If there is a cycle, we need to detect it , otherwise it will make the
  path between two vertices longer than the longest possible path in a graph.
  Time Complexity : O( E * V)

 A Negative Cycle - A cycle with weights sum up to a negative number.
 Presence of a negative weight cycle can cause the node expansion to go on indefinitely.
 Reference : https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture14.pdf


"""

from Dijkstra import WeightedGraph
from collections import defaultdict


def bellmanFordShortestPath(Graph, source):
    weightMap = defaultdict(lambda: float('inf'))
    weightMap[source] = 0

    # Iterate through all egdes |V| - 1 times
    for i in range(Graph.numNodes - 1):
        queue = [v for v in range(Graph.numNodes)]
        # print(queue)

        visited = list()
        while queue:
            currentVertex = queue.pop()
            for neighbor, weight in Graph.weightedAdjList[currentVertex]:
                currentEdge = currentVertex, neighbor
                if currentEdge in visited:
                    continue
                visited.append(currentEdge)
                oldCost = weightMap[neighbor]
                newCost = weightMap[currentVertex] + weight
                if weightMap[currentVertex] != float('inf') and newCost < oldCost:
                    weightMap[neighbor] = newCost

    # if the weights tables can be updated for any vertex
    # after |V| - 1 iterations, then it indicates a negative cycle in the graph.

    queue = [v for v in range(Graph.numNodes)]
    while queue:
        currentVertex = queue.pop()
        for neighbor, weight in Graph.weightedAdjList[currentVertex]:
            oldCost = weightMap[neighbor]
            newCost = weightMap[currentVertex] + weight
            if weightMap[currentVertex] != float('inf') and newCost < oldCost:
                print("Graph contains negative cycle")
                break
    print(weightMap)
    return weightMap


if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [3, 1], [2, 4], [4, 1], [4, 3]]
    weights = [2, 3, 2, 6, -5, -6]
    weightedGraph = WeightedGraph(5, edges, weights)
    source, target = 0, 3
    bellmanFordShortestPath(weightedGraph, source)
