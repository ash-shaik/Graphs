"""
 How to determine if a given graph (say undirected) is also a valid tree?
 - Have no loop.
 - All nodes in the graph are connected.

"""
from Graph import Graph


def is_valid_tree(graph):
    colors = {}
    has_cycle = False

    def dfs(current_node, current_color):
        if current_node in colors:
            if colors[current_color] != current_color:
                return False
            else:
                return True
        colors[current_node] = current_color
        for neighbor in graph.adjList[current_node]:
            if not dfs(neighbor, not current_color):
                return False
        return True

    for node in graph.adjList:
        if node not in colors:
            if not dfs(node, 0):
                has_cycle = True
                break
    if not has_cycle and len(colors) == graph.numNodes:
        return True
    else:
        return False


if __name__ == '__main__':
    num_vertices = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    graph = Graph(num_vertices, edges)
    print(is_valid_tree(graph))
