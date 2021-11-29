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
import numpy as np


def exchangeInLog(Graph):
    """
    Convert the edge rates into their log values.
    :param Graph:
    :return: Graph with transformed rates.
    """
    transformedGraph = []
    for currency, rates in enumerate(Graph):
        transformedGraph.append([])
        for rate in rates:
            transformedGraph[currency].append(-np.log10(rate))
    return transformedGraph


def bellman_ford_negative_cycle(Graph, source):
    """
    Detects if there is a negative-weight cycle.
    :param Graph:
    :param source:
    :return: all -ve weight cycles from the source vertex.
    Time Complexity : O(EV)
    """
    numVertices = len(Graph)
    distance_dict = [float('inf') for v in range(numVertices)]
    parent = defaultdict(lambda: -1)

    distance_dict[source] = 0

    for i in range(numVertices - 1):
        # for every edge in the graph
        for U, exchangeRates in enumerate(Graph):
            for V, distance in enumerate(exchangeRates):
                oldDist = distance_dict[V]
                newDist = distance_dict[U] + distance
                if newDist < oldDist:
                    distance_dict[V] = newDist
                    parent[V] = U

    visited = []
    cycles = []
    for U, exchangeRates in enumerate(Graph):
        for V, distance in enumerate(exchangeRates):
            if V in visited:
                continue

            oldDist = distance_dict[V]
            newDist = distance_dict[U] + distance
            if newDist < oldDist:
                distance_dict[V] = newDist
                # print('Found a cycle')
                cycle = []
                current = V
                while True:
                    visited.append(V)
                    cycle.append(current)
                    current = parent[current]
                    if current == V or current in cycle:
                        break
                # return True
                total = 0
                for (p1, p2) in zip(cycle, cycle[1:]):
                    total += Graph[p1][p2]
                arbValue = np.exp(-total) - 1
                print("Path:", cycle)
                print(f"{arbValue*100:.2g}%\n")
                cycles.append(cycle)
    return cycles


if __name__ == '__main__':
    exchangeRates = [
        [1.0, 0.8631, 0.5903],
        [1.1586, 1.0, 0.6849],
        [1.6939, 1.46, 1.0]
    ]
    tGraph = exchangeInLog(exchangeRates)
    print(bellman_ford_negative_cycle(tGraph, 0))
