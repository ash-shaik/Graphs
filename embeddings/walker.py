import random


class Walker:

    def __init__(self, graph, walk_length, walk_number):
        self.graph = graph
        self.walks = []
        self.walk_length = walk_length
        self.walk_number = walk_number

    def do_walk(self, node):
        walk = [node]
        for _ in range(self.walk_length - 1):
            neighbors = [node for node in self.graph.neighbors(walk[-1])]
            if neighbors:
                walk += random.sample(neighbors, 1)
        walk = [str(w) for w in walk]
        return walk

    def do_walks(self, graph):
        for node in self.graph.nodes():
            for _ in range(self.walk_number):
                walk_from_node = self.do_walk(node)
                self.walks.append(walk_from_node)
