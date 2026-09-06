from __future__ import annotations
import numpy as np

def init_model(dim: int, seed: int = 0) -> np.ndarray:
    rng=np.random.default_rng(seed)
    return rng.normal(0.5, 0.08, size=dim)

def model_error(model, target) -> float:
    return float(np.mean((np.asarray(model)-np.asarray(target))**2))
