from numpy import full, nan, array, sum, diag
from numpy.random import random_sample, seed

from ._compute_norm import _compute_norm
from ._update_H_by_multiplicative_update import _update_H_by_multiplicative_update
from ._update_W_by_multiplicative_update import _update_W_by_multiplicative_update

from heapq import heapify, heappop

def gnmf_by_multiplicative_update(adjMat, l, p, V, k, n_iteration=int(1e3), random_seed=20121020):

    R_norms = full(n_iteration + 1, nan)

    seed(random_seed)

    W = random_sample(size=(V.shape[0], k))

    H = random_sample(size=(k, V.shape[1]))

    R_norms[0] = _compute_norm(V - W @ H)
    
    M = p_nearest_neighbors(adjMat, p)
        
    D = diag([sum(M[i]) for i in range(M.shape[1])])

    for i in range(n_iteration):

        W = _update_W_by_G_multiplicative_update(V, W, H)

        H = _update_H_by_G_multiplicative_update(V, W, H, l, M, D)

        R_norms[i + 1] = _compute_norm(V - W @ H)

        # TODO: stop based on tolerance

    return W, H, R_norms

def p_nearest_neighbors(adjMat, p)
    M = full((adjMat.shape[0], adjList.shape[1]), 0)
    for i in range(adjMat.shape[0])
        heap = [[adjMat[i][j], j] for j in range(adjMat.shape[1])]
        heapify(heap)
        for k in range(p)
            if heap
                tup = heappop(heap)
                M[i][tup[1]] = M[tup[1]][i] = tup[0]
    return M
        