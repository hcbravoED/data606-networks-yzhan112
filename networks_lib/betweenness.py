import numpy as np
from collections import deque

## TODO: Implement this function
##
## Implements the breadth-first algorithm of Girvan-Newman to compute
##   number (fractional) of shortest paths starting from a given vertex
##   that go through each edge of the graph
##
## Input:
##   - vertex (int): index of vertex paths start from
##   - mat (np.array): n-by-n adjacency matrix
##
## Output:
##   (np.array): n-by-n edge count matrix
##
## Note: assume input adjacency matrix is binary and symmetric
def edge_counts(vertex, mat):
    num_vertices = mat.shape[0]
    res = np.zeros((num_vertices, num_vertices))
    top_town = np.full(num_vertices, np.inf)
    available = [i is not vertex for i in range(num_vertices)]
    parent_layer = []
    q = deque()
    q.append((vertex, 0))
    while not any(available):
        v = q.popleft()
        print(f'pop_v: {v}')
        top_town[v[0]] += v[1]
        print(f'top_town: {top_down}')
        parent_layer.append(v)
        print(f'parent_layer: {parent_layer}')
        children_layer = np.where(mat[v[0], :] > 0)[0]
        print(f'children_layer: {children_layer}')
        for i in range(len(children_layer)):
            if children_layer[i] not in parent_layer:
                q.append((v_neighbors[i],1))

    return res

## Compute edge betweeness for a graph
##
## Input:
##   - mat (np.array): n-by-n adjacency matrix.
##
## Output:
##   (np.array): n-by-n matrix of edge betweenness
##
## Notes: Input matrix is assumed binary and symmetric
def edge_betweenness(mat):
    res = np.zeros(mat.shape)
    num_vertices = mat.shape[0]
    for i in range(num_vertices):
        res += edge_counts(i, mat)
    return res / 2.
