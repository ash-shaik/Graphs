from collections import defaultdict


def shortestDistance(numVertex, source, target, edges):
    adjList = defaultdict(list)
    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)

    parent, distance = [-1] * numVertex, [float("inf")] * numVertex

    if not updateDistanceBFS(adjList, source, target, numVertex, parent, distance):
        print("Source and Target are not connected")

    path = []
    current = target
    path.append(current)

    while parent[current] != -1:
        path.append(parent[current])
        current = parent[current]
    path.reverse()
    print("Path is : ", path)


def updateDistanceBFS(adjList, source, target, numVertex, parent, distance):
    queue = []
    visited = [False] * numVertex

    visited[source] = True
    distance[source] = 0
    queue.append(source)

    while queue:
        current = queue[0]
        queue.pop(0)
        if current == target:
            return True

        for neighbor in adjList[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)
    return False


if __name__ == '__main__':
    numVertices = 8
    edges = [[0, 1], [0, 3], [1, 2], [3, 4], [3, 7], [4, 5], [4, 6]
        , [4, 7], [5, 6], [6, 7]]

    shortestDistance(numVertices, 0, 7, edges)
