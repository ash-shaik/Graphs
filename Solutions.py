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


if __name__ == '__main__':
    rooms = [[2147483647, -1, 0, 2147483647]
        , [2147483647, 2147483647, 2147483647, -1]
        , [2147483647, -1, 2147483647, -1]
        , [0, -1, 2147483647, 2147483647]]

    solver = Solution()
    solver.wallsAndGates(rooms)
    print(rooms)
