'''
 The key in finding a shortest path from source to goal is to :
 * Build up the distance of each vertex from the source
 * the parent vertex in the path from the source.
 * then compute the shortest path from source to destination.

 # In the solution , we not just track the visited cells but also the keys in our possession
 as we traverse the maze.
 The possession of the keys we collection along the traversal - we will call it the keyring here.
 That way we allow visiting a cell , when approached with a new set of keyring.

 we'll use a 10-bit integer to represent the keyring.
 water	don’t include
 locked door	don’t include
 door w/key	include
 land	include
 door or land w/keyring already seen	don’t include

'''

import heapq

from collections import defaultdict, deque

WATER = '#'
START = '@'
GOAL = '+'


def find_shortest_path_in_grid(grid):
    rows, cols = len(grid), len(grid[0])
    start, end = None, None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == START:
                start = (i, j)
            if grid[i][j] == GOAL:
                end = (i, j)

    keyRing = 0
    visited = defaultdict(list)
    visited[(start[0], start[1])].append(keyRing)
    parents = {(start[0], start[1]): None}

    q = deque()
    q.append((start[0], start[1], keyRing))
    while q:
        cRow, cCol, key = q.popleft()

        if (cRow, cCol) == end:
            break
        for neighbor in getNeighbors(grid, cRow, cCol, keyRing):
            nRow, nCol, newKeyRing = neighbor[0], neighbor[1], neighbor[2]
            if not isVisited(nRow, nCol, newKeyRing, visited):
                q.append((nRow, nCol, newKeyRing))
                parents[(nRow, nCol)] = cRow, cCol
                visited[(nRow, nCol)].append(newKeyRing)

    path = []
    current = end
    path.append(current)

    while current:
        row, col = parents[current]
        path.append((row, col))
        current = row, col
    path.reverse()
    return [list(cord) for cord in path]


def getNeighbors(grid, row, col, keyRing):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(grid), len(grid[0])

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            value = grid[new_row][new_col]
            if value == WATER:
                continue
            # check for access to door.
            if value in 'ABCDEFGHIJ':
                if keyRing & (1 << (ord(value) - ord('A'))) == 0:
                    continue
            if value in 'abcdefghij':
                # we found a key so we'll add it in our keyring
                newKeyRing = keyRing | (1 << (ord(value) - ord('a')))
            else:
                newKeyRing = keyRing
            neighbors.append((new_row, new_col, newKeyRing))
    return neighbors


def isVisited(new_row, new_col, newKeyring, visited):
    for key in visited[(new_row, new_col)]:
        if newKeyring == key:
            return True
    return False


'''
 We'll use bitwise operations and bit masks to find if we have a key to a door.
 mask - bits you want to keep and which bits you want to clear.
 
'''
if __name__ == '__main__':
    ''' 
    grid = ["+B..."
        , "####."
        , "##b#."
        , "a...A"
        , "##@##"]
    '''
    grid = ["...B"
          , ".b#."
          , "@#+."]

    print(find_shortest_path_in_grid(grid))
