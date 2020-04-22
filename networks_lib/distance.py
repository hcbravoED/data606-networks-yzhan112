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
    q = deque()

    for u in range(num_vertices):
        visited = np.zeros([num_vertices, num_vertices])
        q.append((u, 0))
        visited[u] = 1
        while len(q) != 0:
            v = q.pop()
            print(f'pop_v {v}')
            #if visited[u, v[0]] == 0:
            #visited[u, v[0]], visited[v[0], u] = (1, 1)
            dist[u, v[0]], dist[v[0], u] = (v[1], v[1])
            print(f'distance mat is {dist}')
            v_neighbors = np.where(mat[v[0], :] > 0)[0]
            print(f'v_neighbors: {v_neighbors}')
            for i in range(len(v_neighbors)):
                if visited[v_neighbors[i]] == 0:
                    q.append((v_neighbors[i], v[1]+1))
                    print(f'Now {q}')
                    visited[v_neighbors[i]] = 1
                    print(f'visited mat is {visited}')

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
