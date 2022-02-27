import networkx as nx
from embeddings.deepwalk import DeepWalk

if __name__ == '__main__':
    G = nx.barbell_graph(m1=10, m2=4)
    dw = DeepWalk(dimensions=2)
    dw.fit(G)
    embeddings = dw.get_embedding()
    print(embeddings)

