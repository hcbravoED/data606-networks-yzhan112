import numpy as np
from collections import deque

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
##
## returns:
##   (np.array): distance matrix
##
## Note: You can assume input matrix is binary, square and symmetric
##       Your output should be square and symmetric
def bfs_distance(mat):
    num_vertices = mat.shape[0]
    dist = np.full((num_vertices, num_vertices), np.inf)
    visited = np.zeros([num_vertices, num_vertices])
    q = deque()

    for u in range(num_vertices):
        q.append((u, 0))
        while len(q) != 0:
            v = q.pop()
            print(f'pop_v {v}')
            if visited[u, v[0]] == 0:
                visited[u, v[0]], visited[v[0], u] = (1, 1)
                dist[u, v[0]], dist[v[0], u] = (v[1], v[1])
                v_neighbors = np.where(mat[v[0], :] > 0)[0]
                print(f'v_neighbors: {v_neighbors}')
                for i in range(len(v_neighbors)-1):
                    if visited[u, v_neighbors[i]] == 0:
                        q.append((v_neighbors[i], v[1]+1))
                        #visited[u, v_neighbors[i]], visited[v_neighbors[i], u] = (1, 1)

    return dist

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
##
## returns:
##   (list of np.array): list of components
##
## Note: You can assume input matrix is binary, square and symmetric
##       Your output should be square and symmetric
def get_components(mat):
    dist_mat = bfs_distance(mat)
    num_vertices = mat.shape[0]
    available = [False for _ in range(num_vertices)]

    components = []

    # finish this loop
    while any(available):
        pass

    # this is for testing purposes remove from final solution
    components = [np.arange(num_vertices)]

    return components
