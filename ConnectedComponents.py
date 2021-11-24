"""
Calculate the number of connected components in an undirected graph.
We are given an edgeList in no particular order.

1. Build the graph from the given input edgeList.
2. Follow DFS/BFS to explore the vertices until all are explored.
3. Outer loop going over each vertex.
4. The number of DFS/BFS triggered on such a graph gives us the number
   of connected components.
5. O(E + V) x E = O(V2) Quadratic time runtime. O(N2). In a
Dense graph - number of edges E ~= V2, O(E2)
Sparse Graph - O(V2)
"""

from collections import defaultdict
import numpy as np


def naiveNumConnectedComponentsInUDG(n, edges):
    if 0 >= n <= 1:
        return n

    adjList = defaultdict(list)
    for edge in edges:
        if np.isscalar(edge):
            if edge not in adjList:
                adjList[edge].append(edge)
        else:
            v1, v2 = edge
            adjList[v1].append(v2)
            adjList[v2].append(v1)
    # print(adjList)
    cc_count = 0
    visited = []
    for vertex in range(n):
        if vertex not in visited:
            cc_count += 1
            dfs(adjList, vertex, visited)
    return cc_count


def dfs(adjList, source, visited):
    visited.append(source)
    for neighbor in adjList[source]:
        if neighbor not in visited:
            dfs(adjList, neighbor, visited)


"""
 What happens when the edges/connections of the graph are in coming dynamically?
 As in a streaming context. 
 1. We start of the number of connected components equal to the number of vertices
 2. As the edge/connection get added we merge the components in a connected graph 
 and decrement the number of connected components.
 
 We can use the Union-Find pattern here. 
 
 Given an edge, Union : Connects an edge.
 Find :
 If a new edge belongs to the same connected component, # components is unchanged
 If a new edge belongs to a different connected component, # components decreases 
  
  1. Associate component Id for every vertex.
  2. Iterate through the edges, and make the connections with Union operation.
  3. While doing the union recursively find the root parent of the node.
  Time complexity O( E + V)
"""


def connected_components(n, edges):
    parent = [i for i in range(n)]

    # Iterate through every edge.
    for i in range(len(edges)):
        union(edges[i][0], edges[i][1], parent)
    components = set()
    for i in range(n):
        components.add(find(parent[i], parent))

    return len(components)


def find(source, parent):
    p = parent[source]
    while p != parent[p]:
        parent[p] = parent[parent[p]]
        p = parent[p]
    return p


def union(node1, node2, parent):
    source, target = find(node1, parent), find(node2, parent)

    if source != target:
        parent[node2] = node1


def union_r(node1, node2, parent, rank):
    source, target = find(node1, parent), find(node2, parent)

    if source == target:
        return False

    if rank[node1] >= rank[node2]:
        parent[node2] = node1
        rank[node1] += rank[node2]
    else:
        parent[node1] = node2
        rank[node2] += rank[node1]
    return True


def redundant_connections(edges):
    parent_ = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    for node1, node2 in edges:
        if not union_r(node1, node2, parent_, rank):
            return [node1, node2]


def union_c(node1, node2, parent, rank):
    source, target = find(node1, parent), find(node2, parent)

    if source == target:
        return False

    if rank[node1] >= rank[node2]:
        parent[node2] = node1
        rank[node1] += rank[node2]
    else:
        parent[node1] = node2
        rank[node2] += rank[node1]
    return True


def critical_connections(num_nodes, connections):
    """

    :param num_nodes:
    :param connections:
    :return:
    """
    # build the graph.
    adjList = None

    def build_graph(connections):
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def dfs(source, visited):
        visited.append(source)

        for neighbor in adjList[source]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    adjList = build_graph(connections)
    criticalConnection = []
    for u, v in connections:
        adjList[u].remove(v)
        visited = []
        dfs(u, visited)
        if len(visited) != num_nodes:
            criticalConnection.append([u, v])
        adjList.clear()
        adjList = build_graph(connections)

    return criticalConnection


if __name__ == '__main__':
    num_nodes = 5
    edges = [[0, 1], [1, 2], [3, 4]]

    print(naiveNumConnectedComponentsInUDG(num_nodes, edges))

    num_nodes = 50
    edges = [3, 2, [0, 0], [1, 1], [2, 2]]
    print(naiveNumConnectedComponentsInUDG(num_nodes, edges))

    edges = [[0, 0], [1, 1], [2, 2]]
    print(connected_components(num_nodes, edges))

    # edges = [[1, 2], [1, 3], [2, 3]]
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(redundant_connections(edges))

    num_nodes = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(critical_connections(num_nodes, connections))
