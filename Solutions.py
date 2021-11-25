from collections import deque


class Solution:

    def wallsAndGates(self, rooms):
        """
        Given a maze with cells being: gates, walls or empty spaces.
        Fill the empty spaces with the number of steps to the closest gate.
        :param rooms:
        :return:
        """
        rows, cols = len(rooms), len(rooms[0])
        visit = set()

        q = deque()
        for r in range(rows):
            for c in range(cols):
                # Adding all the gates.
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        gateDistance = 0
        while q:
            q_len = len(q)
            for i in range(q_len):
                r, c = q.popleft()
                rooms[r][c] = gateDistance
                for a, b in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= a < rows and 0 <= b < cols and (a, b) not in visit and rooms[a][b] != -1:
                        visit.add((a, b))
                        q.append((a, b))
            gateDistance += 1

    def rectangleMania(self, coordinates):
        """
        Takes a list of coordinates and returns the number of rectangles formed by these
        rectangles.
        :param coordinates:
        :return:
        """
        coordinatesTable = self.buildCoordinatesTable(coordinates)
        return self.countRectangles(coordinates, coordinatesTable)

    def buildCoordinatesTable(self, coordinates):
        coordinatesTable = {}
        for coordinate in coordinates:
            coordinateInString = self.coordinateToString(coordinate)
            coordinatesTable[coordinateInString] = True
        return coordinatesTable

    def countRectangles(self, coordinates, coordinatesTable):
        rectangleCount = 0
        for x, y in coordinates:
            for dx, dy in coordinates:
                if not (dx > x and dy > y):
                    continue
                upper = self.coordinateToString([x, dy])
                right = self.coordinateToString([dx, y])
                if upper in coordinatesTable and right in coordinatesTable:
                    rectangleCount += 1
        return rectangleCount

    def coordinateToString(self, coordinate):
        """
        Helper function to be used to build a key for the hashmap.
        :param coordinate:
        :return:
        """
        x, y = coordinate
        return str(x) + "_" + str(y)


if __name__ == '__main__':
    rooms = [[2147483647, -1, 0, 2147483647]
        , [2147483647, 2147483647, 2147483647, -1]
        , [2147483647, -1, 2147483647, -1]
        , [0, -1, 2147483647, 2147483647]]

    solver = Solution()
    solver.wallsAndGates(rooms)
    print(rooms)

    coordinates = [[0, 0], [0, 1], [1, 1], [1, 0]
        , [2, 1], [2, 0], [3, 1], [3, 0]]

    print(solver.rectangleMania(coordinates))
