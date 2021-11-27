"""
 Algorithm to find the shortest distance/path from a single source node
 to all other nodes in a weighted Graph.
 Works only for edge weights that are positive.

"""

from collections import defaultdict
import heapq


def dijkstra(Graph, source):
    visited = set()
    parents = {}
    distance = defaultdict(lambda: float('inf'))
    distance[source] = 0

    heap = []
    heapq.heappush(heap, (0, source))

