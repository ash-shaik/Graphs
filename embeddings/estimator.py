import random


class Estimator(object):
    def __init__(self):
        pass

    def fit(self):
        pass

    def get_embedding(self):
        pass

    def _set_seed(self, seed):
        random.seed(seed)
