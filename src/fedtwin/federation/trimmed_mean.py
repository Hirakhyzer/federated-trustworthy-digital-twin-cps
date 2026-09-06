import numpy as np

def aggregate(updates, trim_fraction: float = 0.2):
    X=np.sort(np.stack([u.vector for u in updates]), axis=0)
    n=len(X); k=int(n*trim_fraction)
    if 2*k >= n: k=0
    return X[k:n-k].mean(axis=0) if k else X.mean(axis=0)
