import numpy as np
from gensim.models.word2vec import Word2Vec
from embeddings.walker import Walker
from embeddings.estimator import Estimator


class DeepWalk(Estimator):

    def __init__(self, walk_number: int = 10, walk_length: int = 80
                 , dimensions: int = 128, workers: int = 4, window_size: int = 5
                 , epochs: int = 1, learning_rate: float = 0.05
                 , min_count: int = 1, seed: int = 42):
        self.walk_number = walk_number
        self.walk_length = walk_length
        self.dimensions = dimensions
        self.workers = workers
        self.window_size = window_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.min_count = min_count
        self.seed = seed
        self._embedding = None

    def fit(self, graph):
        self._set_seed(self.seed)
        walker = Walker(self.walk_length, self.walk_number)
        walker.do_walk(graph)

        model = Word2Vec(walker.walks,
                         hs=1,
                         alpha=self.learning_rate,
                         epochs=self.epochs,
                         vector_size=self.dimensions,
                         window=self.window_size,
                         min_count=self.min_count,
                         workers=self.workers,
                         seed=self.seed, )

        num_of_nodes = graph.number_of_nodes()
        self._embedding = [model.wv[str(n)] for n in range(num_of_nodes)]

    def get_embedding(self):
        return np.array(self._embedding)
