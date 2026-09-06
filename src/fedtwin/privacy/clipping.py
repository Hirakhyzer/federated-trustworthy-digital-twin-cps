import numpy as np

def clip_vector(vector, max_norm: float = 1.0):
    v=np.asarray(vector, dtype=float)
    norm=np.linalg.norm(v)
    if norm <= max_norm or norm == 0:
        return v.copy()
    return v*(max_norm/norm)
