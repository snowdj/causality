import networkx as nx

import numpy.random as npr


def draw_graph(G, edge_weight=None, layout: str="kamada_kawai"):
    pos = nx.kamada_kawai_layout(G)

    if edge_weight:
        edge_labels = {(u, v): d[edge_weight] for u, v, d in G.edges(data=True)}  # noqa: E501
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, with_labels=True)
    nx.draw_kamada_kawai(G, with_labels=True)


def noise(size):
    return npr.normal(loc=0, scale=1, size=size)
