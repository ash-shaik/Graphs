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

    visited = {(row, col): set() for row in range(rows) for col in range(cols)}
    visited[(start[0], start[1])].add(0)
    parents = {(start[0], start[1], 0): None}

    q = deque()
    q.append((start[0], start[1], 0))
    while q:
        cRow, cCol, keyRing = q.popleft()

        if grid[cRow][cCol] == GOAL:
            break
        for nRow, nCol, newKeyRing in getNeighbors(grid, cRow, cCol, keyRing):
            if not isVisited(nRow, nCol, newKeyRing, visited):
                q.append((nRow, nCol, newKeyRing))
                parents[(nRow, nCol, newKeyRing)] = cRow, cCol, keyRing
                visited[(nRow, nCol)].add(newKeyRing)

    path = []

    while parents[(cRow, cCol, keyRing)] is not None:
        path.append((cRow, cCol))
        cRow, cCol, keyRing = parents[(cRow, cCol, keyRing)]

    path.append((cRow, cCol))
    path.reverse()
    return [list(cord) for cord in path]


def getNeighbors(grid, row, col, keyRing):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(grid), len(grid[0])

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if not (0 <= new_row < rows and 0 <= new_col < cols):
            continue
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
    #'''
    grid = ["+B..."
        , "####."
        , "##b#."
        , "a...A"
        , "##@##"]
    #'''
    '''
    grid = ["...B"
          , ".b#."
          , "@#+."]
    '''

    print(find_shortest_path_in_grid(grid))
