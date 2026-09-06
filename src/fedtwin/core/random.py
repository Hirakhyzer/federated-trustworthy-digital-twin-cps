import numpy as np

def rng(seed: int | None = None) -> np.random.Generator:
    return np.random.default_rng(seed)
