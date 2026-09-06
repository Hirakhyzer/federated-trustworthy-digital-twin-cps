import numpy as np

def l2(x):
    return float(np.linalg.norm(np.asarray(x, dtype=float)))

def cosine(a, b):
    a=np.asarray(a, dtype=float); b=np.asarray(b, dtype=float)
    d=np.linalg.norm(a)*np.linalg.norm(b)
    if d == 0:
        return 1.0
    return float(np.dot(a,b)/d)

def clamp01(x):
    return float(max(0.0, min(1.0, x)))
