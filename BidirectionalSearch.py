from collections import defaultdict


class BidirectionalSearch:

    def __init__(self, num_vertices, edges):
        self.num_vertices = num_vertices
        self.adjList = defaultdict(list)
        for u, v in edges:
            self.adjList[u].append(v)

        self.forward_queue = []
        self.backward_queue = []

        self.visited_forward = [False] * self.num_vertices
        self.visited_backward = [False] * self.num_vertices

        self.parent_forward = [None] * self.num_vertices
        self.parent_backward = [None] * self.num_vertices

    def bidirectional_search(self, start, goal):
        path = []

        self.forward_queue.append(start)
        self.visited_forward[start] = True
        self.parent_forward[start] = -1

        self.backward_queue.append(goal)
        self.visited_backward[goal] = True
        self.parent_backward[goal] = -1
        return path

    def bfs(self, direction=1):
        if direction:
            # forward
            while self.forward_queue:
                current = self.forward_queue.pop(0)
                for neighbor in self.adjList[current]:
                    if not self.visited_forward[neighbor]:
                        self.visited_forward[neighbor] = True
                        self.forward_queue.append(neighbor)
                        self.parent_forward[neighbor] = current

        else:
            while self.backward_queue:
                current = self.backward_queue.pop(0)
                for neighbor in self.adjList[current]:
                    if not self.visited_backward[neighbor]:
                        self.visited_backward[neighbor] = True
                        self.backward_queue.append(neighbor)
                        self.parent_backward[neighbor] = current

    def has_common(self):
        for i in range(self.num_vertices):
            if self.visited_forward[i] and self.visited_backward[i]:
                return i
        return -1


if __name__ == '__main__':
    num_vertices = 17
    edges = [(1, 4), (2, 4), (3, 6), (5, 6), (4, 8), (6, 8), (8, 9), (9, 10)
        , (10, 11), (11, 13), (11, 14), (10, 12), (12, 15), (12, 16)]

    graph = BidirectionalSearch()
