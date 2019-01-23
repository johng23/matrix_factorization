def _update_H_by_G_multiplicative_update(V, W, H, l, M, D):

    return H * (W.T @ V + l * H @ M.T) / (W.T @ W @ H + l * H @ D.T)