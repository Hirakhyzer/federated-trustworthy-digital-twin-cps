from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class DomainProfile:
    name: str
    target: tuple[float, ...]
    twin_reliability: float
    intrinsic_noise: float
    shift_sensitivity: float

DOMAIN_PROFILES = {
    "battery": DomainProfile("battery", (0.62,0.41,0.55,0.31,0.48,0.72,0.38,0.51), 0.94, 0.025, 0.45),
    "water": DomainProfile("water", (0.44,0.69,0.37,0.58,0.33,0.46,0.71,0.29), 0.91, 0.035, 0.52),
    "robot": DomainProfile("robot", (0.75,0.28,0.63,0.42,0.67,0.35,0.49,0.56), 0.88, 0.045, 0.66),
    "microgrid": DomainProfile("microgrid", (0.31,0.77,0.59,0.68,0.41,0.61,0.27,0.74), 0.90, 0.040, 0.62),
    "factory": DomainProfile("factory", (0.52,0.36,0.73,0.47,0.64,0.43,0.58,0.34), 0.92, 0.030, 0.55),
    "ev": DomainProfile("ev", (0.69,0.54,0.32,0.71,0.39,0.57,0.46,0.63), 0.89, 0.040, 0.58),
    "railway": DomainProfile("railway", (0.37,0.62,0.78,0.26,0.53,0.69,0.42,0.57), 0.95, 0.025, 0.50),
}

def domain_target(name: str, dim: int = 8) -> np.ndarray:
    profile=DOMAIN_PROFILES[name]
    arr=np.asarray(profile.target, dtype=float)
    if dim <= len(arr):
        return arr[:dim].copy()
    return np.resize(arr, dim).astype(float)

def population_oracle(domains: list[str], dim: int = 8) -> np.ndarray:
    return np.mean([domain_target(d, dim) for d in domains], axis=0)
