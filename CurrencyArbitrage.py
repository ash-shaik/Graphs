"""
Problem : To develop a systematic approach to find arbitrage opportunities in a currency exchange

The Bellman Ford algorithm finds the minimum weight path from a single source vertex
to all other vertices on a weighted directed graph. However if there is a negative weight cycle in
that graph, a shortest path between two edged cannot be defined.

And this pattern is key tso detecting arbitrage opportunities in currency exchange.

In this problem, we assign currencies as vertices and edge weight represents the exchange rate.
Bellman-Ford computes the path weight by adding the individual edge weights. However to make this
work for exchange rates, we take the logs of all the edge weights, so when we sum edge weights
along a path we are actually multiplying exchange rates – log(a * b) = log(a) + log(b)
Thus a negative-weight cycle on the negative-log graph corresponds to an arbitrage opportunity.
"""
from collections import defaultdict


def find_currency_arbitrage():
    pass


def bellman_ford_negative_cycle(Graph, source):
    numVertices = len(Graph)
    distance_dict = defaultdict(lambda: float('inf'))
    parent_dict = defaultdict(lambda: -1)

    distance_dict[source] = 0

    for i in range(numVertices - 1):
        # for every edge in the graph
        for u, v in Graph.edges:
            for neighbor, distance in Graph.weightedAdjList[u]:
                oldDist = distance_dict[neighbor]
                newDist = distance_dict[u] + distance
                if newDist < oldDist:
                    distance_dict[neighbor] = newDist
                    parent_dict[neighbor] = u

    visited = []
    for u, v in Graph.edges:
        for neighbor, distance in Graph.weightedAdjList[u]:
            if neighbor in visited:
                continue
            visited.append(neighbor)
            oldDist = distance_dict[neighbor]
            newDist = distance_dict[u] + distance
            if oldDist < newDist:
                print('Found a cycle')


if __name__ == '__main__':
