import numpy as np
from networks_lib.distance import bfs_distance
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
    distance_mat = bfs_distance(mat)
    td_parents = dict()
    q_td = deque()
    q_td.append(vertex)
    td_weight = dict()
    td_weight[vertex] = 1
    q_bu = deque()
    bu_node_weight = dict()
    bu_edge_weight = dict()
    node_layer = {i:j for i, j in enumerate(distance_mat[vertex, :])}
    #print(f'node_layer: {node_layer}')
    #print('\n')
    for node in node_layer.keys():
        if node is not vertex:
            nbs = np.where(mat[node, :] > 0)[0]
            #print(f'{node} nbs is {nbs}')
            node_parents = [p for p in nbs if node_layer[p] < node_layer[node]]
            td_parents[node] = node_parents
            #print(f'{node} parents: {td_parents}')
    while list(q_td):
        node = q_td.popleft()
        node_weight = td_weight.get(node, 1)
        #print(f'parent {node} weight: {node_weight}')
        for key in td_parents.keys():
            if node in td_parents[key]:
                child_weight = td_weight.get(key, 0)
                child_weight += node_weight
                td_weight[key] = child_weight
                #print(f'child {node} weight: {child_weight}')
                q_td.append(key)
    #print(f'td_weight: {td_weight}')

    sorted_node_layer = [key for key, _ in sorted(node_layer.items(), key = lambda item: item[1], reverse = True)]
    #print(f'sorted_node_layer: {sorted_node_layer}')

    for item in sorted_node_layer:
        if item is not vertex:
            q_bu.append(item)
            #print(f'q_bu: {q_bu}')

    while list(q_bu):
        node = q_bu.popleft()
        node_weight = bu_node_weight.get(node, 1.0)
        node_parents = td_parents[node]
        #print(f'{node} parent: {node_parents}')
        node_parents_sum = 0.0
        for parent in node_parents:
            node_parents_sum += td_weight[parent]
        #print(f'{node} parent sum: {node_parents_sum}')
        for parent in node_parents:
            node_parent_weight = bu_node_weight.get(parent, 1.0)
            edge_fraction = td_weight[parent] / node_parents_sum
            #print(f'{node}, {parent} edge fraction is {edge_fraction}')
            bu_edge_weight[(node, parent)] = node_weight * edge_fraction
            #print(f'{node}, {parent} edge weight is {bu_edge_weight[(node, parent)]}')
            node_parent_weight += bu_edge_weight[(node, parent)]
            bu_node_weight[parent] = node_parent_weight
            #print(f'{node} parent {parent} weight: {bu_node_weight[parent]}')
            #print('\n')


    #print(f'bu_edge_weight: {bu_edge_weight}')
    for key in bu_edge_weight:
        res[key[0], key[1]] = bu_edge_weight[key]
        res[key[1], key[0]] = bu_edge_weight[key]
    #print(res)
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
