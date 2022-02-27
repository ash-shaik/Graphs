import networkx as nx
from embeddings.deepwalk import DeepWalk
import matplotlib.pyplot as plt

if __name__ == '__main__':
    G = nx.barbell_graph(m1=10, m2=4)
    dw = DeepWalk(dimensions=2)
    dw.fit(G)
    embeddings = dw.get_embedding()
    # print(embeddings)

    fig, ax = plt.subplots(figsize=(10, 10))
    for x in G.nodes():
        v = dw.get_embedding()[x]
        ax.scatter(v[0], v[1], s=1000)
        ax.annotate(str(x), (v[0], v[1]), fontsize=12)

