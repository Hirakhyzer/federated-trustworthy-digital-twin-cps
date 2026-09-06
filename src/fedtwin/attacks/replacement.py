from dataclasses import replace
import numpy as np

def apply(update, target=None, strength: float = 3.0):
    vec=np.ones_like(update.vector)*0.9 if target is None else np.asarray(target, dtype=float)
    return replace(update, vector=strength*vec, condition="model_replacement")
