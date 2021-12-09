from DGraph import DGraph


def find_mother_vertex(G):
    """
    One of the mother vertex will be the last vertex to finish the dfs
    (which causes all vertices to be visited), causing any other remaining vertices
    to not trigger a dfs (because all nodes have been visited)
    :param G: Directed graph
    :return: the vertex which can reach all other vertices of the graph
    Time Complexity : O( V + E)
    """
    visited = [0] * G.numNodes
    mother_vertex = None

    def dfs_(node):
        visited[node] = 1
        # go over the neighbors of current node
        for neighbor in G.adjList[node]:
            if not visited[neighbor]:
                dfs_(neighbor)

    for c_node in range(G.numNodes):
        if not visited[c_node]:
            dfs_(c_node)
            mother_vertex = c_node

    return mother_vertex


if __name__ == '__main__':
    n = 7
    edges = [[0, 2], [0, 1], [1, 3], [4, 1], [5, 2]
        , [5, 6], [6, 0], [6, 4]]
    graph = DGraph(n, edges)
    print(find_mother_vertex(graph))

    n = 8
    another_set_of_edges = [[0, 1], [1, 3], [2, 1], [3, 2]
        , [3, 4], [4, 5], [6, 4], [5, 7], [7, 6]]
    a_graph = DGraph(n, another_set_of_edges)
    # print(find_mother_vertex(a_graph))
