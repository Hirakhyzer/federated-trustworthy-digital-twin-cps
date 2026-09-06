from dataclasses import replace
from fedtwin.privacy.clipping import clip_vector
from .fedavg import aggregate as fedavg

def aggregate(updates, max_norm: float = 1.0):
    clipped=[replace(u, vector=clip_vector(u.vector, max_norm)) for u in updates]
    return fedavg(clipped)
