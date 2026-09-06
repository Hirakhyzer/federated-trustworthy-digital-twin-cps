import numpy as np

def aggregate(updates, weights=None):
    X=np.stack([u.vector for u in updates])
    if weights is None:
        w=np.asarray([u.sample_count for u in updates], dtype=float)
    else:
        w=np.asarray(weights, dtype=float)
    if w.sum() <= 0:
        w=np.ones(len(updates), dtype=float)
    return np.average(X, axis=0, weights=w)
