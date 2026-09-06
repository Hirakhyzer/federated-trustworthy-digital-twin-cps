from dataclasses import replace
import numpy as np

def apply(update, shared_direction=None, strength: float = 1.8):
    if shared_direction is None:
        shared_direction=np.ones_like(update.vector)
    d=np.asarray(shared_direction, dtype=float)
    d=d/(np.linalg.norm(d)+1e-12)
    return replace(update, vector=update.vector+strength*d, condition="coordinated_attack")
