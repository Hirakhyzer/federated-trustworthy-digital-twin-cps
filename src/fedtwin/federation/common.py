from __future__ import annotations
import numpy as np

def stack(updates):
    if not updates:
        raise ValueError("at least one update is required")
    return np.stack([u.vector for u in updates], axis=0)
