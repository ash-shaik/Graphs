"""
 A Spanning tree is a subgraph of an un-directed graph G, which is a tree and contains all vertices of G.
 A minimum spanning tree(no cycle) like structure (subgraph) that connects all the vertices in a graph,
 with lowest total cost that depends on the edge weights.

"""
from collections import defaultdict
import heapq


def prims_algorithm(graph, startVertex):
    """
    Works for undirected connected graphs
    1. Build distance table with any vertex as source.
    2. Use the distance table to get paths to all the other vertices
     from the arbitrarily chosen source.
     Object is to minimize the total distance, not just the distance from
     one specific vertex.
     TIme Complexity : O(E log V)

    :param graph:
    :return:
    """

    minSpanningTree = defaultdict(set)
    visited = set([startVertex])
    heap = [(edge[1], startVertex, edge[0]) for edge in graph[startVertex]]
    distance = [float("inf")] * len(graph)

    heapq.heapify(heap)
    while heap:
        weight, u, v = heapq.heappop(heap)
        if v not in visited:
            visited.add(v)
            minSpanningTree[u].add(v)
            for neighbor, weight in graph[v]:
                oldDistance = distance[neighbor]
                newDistance = weight
                if oldDistance > newDistance:
                    distance[neighbor] = newDistance
                    if neighbor not in visited:
                        heapq.heappush(heap, (newDistance, v, neighbor))

    print(visited)
    return minSpanningTree


if __name__ == '__main__':
    # 0, 1, 2, 3, 4, 5, 6
    # A, B, C, D, E, F, G
    edgeExample1 = [(3, 0, 1), (15, 0, 2), (5, 0, 4), (3, 1, 0), (2, 1, 2), (5, 1, 4), (8, 1, 5)
        , (15, 2, 0), (2, 2, 1), (9, 2, 5), (11, 3, 4), (4, 3, 5)
        , (5, 4, 0), (5, 4, 1), (4, 4, 5), (11, 4, 3)
        , (8, 5, 1), (9, 5, 2), (4, 5, 3), (4, 5, 4)]

    edgeExample2 = [(2, 0, 1), (3, 0, 2), (2, 1, 0), (1, 1, 2), (1, 1, 3), (4, 1, 4)
        , (3, 2, 0), (1, 2, 1), (5, 2, 4), (1, 3, 1), (1, 3, 4)
        , (4, 4, 1), (1, 4, 3), (1, 4, 5), (5, 5, 2), (1, 5, 4), (1, 5, 6)
        , (1, 6, 5)

                    ]
    graph = defaultdict(list)
    for edge in edgeExample1:
        weight, u, v = edge
        graph[u].append((v, weight))

    print(prims_algorithm(graph, 0))
