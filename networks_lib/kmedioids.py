import numpy as np
from collections import defaultdict
from networks_lib.communities import components_to_assignment as cta

## TODO: Implement this function
##
## Input:
##  - dmat (np.array): symmetric array of distances
##  - K (int): Number of clusters
##
## Output:
##   (np.array): initialize by choosing random number of points as medioids
def random_init(dmat, K):
    num_vertices = dmat.shape[0]
    medioids = np.arange(num_vertices)
    np.random.shuffle(medioids)
    #print(medioids[:2])
    #print(type(medioids[:2]))
    return medioids[:2]

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - medioids (np.array): indices of current medioids
##
## Output:
##   - (np.array): assignment of each point to nearest medioid
def assign(dmat, mediods):
    num_vertices = dmat.shape[0]
    num_clusters = len(mediods)
    k_clusters = dict.fromkeys(range(num_clusters))
    k_medioids = []

    for key in k_clusters.keys():
        k_clusters[key] = [mediods[key].tolist()]

    #print(f'before, k_clusters: {k_clusters}')

    for i in range(dmat.shape[0]):
        min_dist = np.min(dmat[[mediods], i])
        if i not in mediods:
            min_position = np.where(dmat[[mediods], i] == np.min(dmat[[mediods], i]))[1]
            #np.random.shuffle(min_position)
            #print(min_position)
            mediods_index = min_position[0]
            #print(mediods_index)
            k_clusters[mediods_index].append(i)
         #   print(f'{i} min_dist {min_dist}, index: {mediods_index}')
        #print(f'after, k_clusters: {k_clusters}')
        #print('\n')

    for key in k_clusters.keys():
        k_medioids.append(k_clusters[key])

    assign_list = cta(k_medioids, num_vertices)
#    print(assign_list)

    return assign_list

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - assignment (np.array): cluster assignment for each point
##   - K (int): number of clusters
##
## Output:
##   (np.array): indices of selected medioids
def get_medioids(dmat, assignment, K):
    mediods = np.array([])
    clusters = defaultdict(list)
    cost = dict()
    min_cost = dict()
    for idx, val in enumerate(assignment):
        clusters[val].append(idx)
    #print(f'before, clusters:{clusters}')

    for key in clusters.keys():
        min_cost[key] = (0.0, np.inf)
        #print(f'before, min_cost {key}: {min_cost[key]}')
        for i in range(len(clusters[key])):
            cost[i] = np.sum(dmat[[clusters[key]], clusters[key][i]])
            #print(f'cost {clusters[key][i]}: {cost[i]}')
            if cost[i] < min_cost[key][1]:
                min_cost[key] = (clusters[key][i], cost[i])
                #print(f'after, min_cost {key}: {min_cost[key]}')

    #print(f'after, min_cost: {min_cost}')
    for key in min_cost.keys():
        #print(f'key:{min_cost[key][0]}')
        mediods = np.append(mediods, min_cost[key][0])
        mediods = mediods.astype(np.int64)
    return mediods

## TODO: Finish implementing this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - K (int): number of clusters
##   - niter (int): maximum number of iterations
##
## Output:
##   - (np.array): assignment of each point to cluster
def kmedioids(dmat, K, niter=10):
    num_vertices = dmat.shape[0]

    # we're checking for convergence by seeing if medioids
    # don't change so set some value to compare to
    old_mediods = np.full((K), np.inf, dtype=np.int)
    medioids = random_init(dmat, K)

    # this is here to define the variable before the loop
    assignment = np.full((num_vertices), np.inf)
    it = 0
    while np.any(old_mediods != medioids) and it < niter:
        it += 1
        old_medioids = medioids
        #print(f'old_medioids: {old_medioids}')
        assignment = assign(dmat, medioids)
        #print(f'assignment: {assignment}')
        medioids = get_medioids(dmat, assignment, K)
        #print(f'medioids: {medioids}')

    return assignment

