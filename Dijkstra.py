"""
 Algorithm to find the shortest distance/path from a single source node
 to all other nodes in a weighted Graph.
 Works only for edge weights that are positive.
 It uses a priority queue to greedily select the closest vertex and visits its neighbors.

"""

from collections import defaultdict
import heapq
from DGraph import DGraph


class WeightedGraph(DGraph):

    def __init__(self, numVertex, edges, weights):
        """

        :param numVertex:
        :param edges:
        :param weights:
        """
        super(WeightedGraph, self).__init__(numVertex, edges)
        # super().__int__(numVertex, edges)
        self.weightedAdjList = defaultdict(list)
        i = 0
        for u, v in edges:
            self.weightedAdjList[u].append((v, weights[i]))
            i += 1

    def getNeighbors(self, source):
        """
        :param source:
        :return:
        """
        return self.weightedAdjList[source]


def dijkstra(Graph, source, target):
    """
    Builds costMap along the path from source to target and build the pathCrawl.
    Time Complexity of O(|E| + |V|log|V|)
    :param Graph:
    :param source:
    :param target:
    :return:
    """
    visited = set()
    parents = {}
    weightMap = defaultdict(lambda: float('inf'))
    weightMap[source] = 0

    heap = []
    heapq.heappush(heap, (0, source))
    parents[source] = None

    while heap:
        wght, current = heapq.heappop(heap)
        visited.add(current)

        if current == target:
            break

        for neighbor, weight in Graph.getNeighbors(current):
            if neighbor not in visited:
                oldCost = weightMap[neighbor]
                newCost = weightMap[current] + weight
                if newCost < oldCost:
                    parents[neighbor] = current
                    weightMap[neighbor] = newCost
                    heapq.heappush(heap, (newCost, neighbor))
    print(parents)
    return parents


def buildPath(parents, vertex):
    path = [vertex]
    current = parents[vertex]
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path


if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [1, 3], [2, 4], [4, 1], [4, 3]]
    weights = [2, 3, 2, 6, 5, 4]
    weightedGraph = WeightedGraph(5, edges, weights)
    source, target = 2, 3
    pathCrawl = dijkstra(weightedGraph, source, target)

    print(buildPath(pathCrawl, target))
