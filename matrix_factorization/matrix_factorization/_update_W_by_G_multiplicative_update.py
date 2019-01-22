def _update_W_by_G_multiplicative_update(V, W, H):

    return W * (V @ W) / (H @ W.T @ W)
