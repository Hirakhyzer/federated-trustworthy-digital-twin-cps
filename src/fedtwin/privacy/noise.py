import numpy as np

def add_gaussian_noise(vector, sigma: float, rng: np.random.Generator):
    if sigma <= 0:
        return np.asarray(vector, dtype=float).copy()
    return np.asarray(vector, dtype=float)+rng.normal(0, sigma, size=len(vector))
