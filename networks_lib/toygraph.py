import numpy as np
from igraph import *

## Return igraph object for the toy graph example
def get_toy_graph():
    mat = get_toy_mat()
    g = Graph.Adjacency((mat > 0).tolist(), mode=ADJ_UNDIRECTED)
    g.vs["label"] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    return g

## Return adjacency matrix for toy graph example
def get_toy_mat():
    mat = np.array([[0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 0, 0, 0],
                    [1, 1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 1, 1, 1, 0]])
    print((mat > 0).tolist())
    return mat

## Plot example toy graph
def plot_toy():
    g = get_toy_graph()
    layout = g.layout("kk")
    return plot(g, layout=layout, bbox=(200,200))
