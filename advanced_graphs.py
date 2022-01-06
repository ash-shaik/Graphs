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


def find_shortest_path_in_maze(grid):
    start, goal, water, land = '@', '+', '#', '.'
    keys, doors = {}, {}
    lands = []

    parent, distance = {}, {}

    start_cord, goal_cord = None, None
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            parent[(r, c)] = -1
            distance[(r, c)] = float('inf')

            coordinates = (r, c)
            element = grid[r][c]

            if element == start:
                start_cord = coordinates
                distance[start_cord] = 0
            elif element == goal:
                goal_cord = coordinates
                distance[goal_cord] = 0
            elif element in 'abcdefghijklmnopqrstuvwxyz':
                keys[element] = coordinates
            elif element in 'ABCDEFGHIJKLMNOPQRSTUVQXYZ':
                doors[element] = coordinates
            elif grid[r][c] == '.':
                lands.append(coordinates)
            else:
                continue

    def start_to_goal_bfs(start_cord, goal_cord, ):
        # Tracks the keys visited if any.
        visited = [start_cord]
        queue = [start_cord]

        while queue:
            current = queue[0]
            queue.pop(0)
            if current == goal_cord:
                break
            r, c = current
            directions = [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]
            for dr, dc in directions:
                r, c = dr, dc
                neighbor = (r, c)
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] != start and grid[r][c] != water \
                        and (r, c) not in visited:
                    currentElement = grid[r][c]
                    # if currentElement == goal:
                    #    break
                    # if the element is a door, check if its key has been visited.
                    if currentElement in doors and currentElement.lower() in keys and keys[
                        currentElement.lower()] not in visited:
                        continue
                    # add to visited if we see a key.
                    # if currentElement in keys:
                    visited.append(neighbor)
                    distance[neighbor] = distance[current] + 1
                    parent[neighbor] = current
                    queue.append(neighbor)

    start_to_goal_bfs(start_cord, goal_cord)
    path = []
    current = goal_cord
    x, y = current
    path.append([x, y])

    while parent[current] != -1:
        # x, y = parent[current]
        # path.append([x, y])
        path.append(parent[current])
        current = parent[current]
    path.reverse()
    return [list(cord) for cord in path]


if __name__ == '__main__':
    numVertices = 8
    edges = [[0, 1], [0, 3], [1, 2], [3, 4], [3, 7], [4, 5], [4, 6]
        , [4, 7], [5, 6], [6, 7]]

    shortestDistance(numVertices, 0, 7, edges)
    grid = ["...B"
        , ".b#."
        , "@#+."]
    print(find_shortest_path_in_maze(grid))
