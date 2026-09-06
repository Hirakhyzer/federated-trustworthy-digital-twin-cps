import numpy as np

def aggregate(updates):
    return np.median(np.stack([u.vector for u in updates]), axis=0)
