import networkx as nx

"""
Networkx is a python based graph library used for modeling property graphs.
Its an in-memory graph database.

Modeling an company 360 Engineering.

"""

if __name__ == '__main__':
    g = nx.DiGraph()
    g.add_edge('Engineer', 'Project')
    g.add_edge('Project', 'Service')
    g.add_edge('Service', 'Platform')
    g.add_edge('Platform', 'Product')

    print(nx.info(g))
    # Get the nodes and edges from the graph

    print("Nodes:", g.nodes())
    print("Edges:", g.edges())
