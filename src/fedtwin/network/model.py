from __future__ import annotations
import numpy as np

def participates(availability: float, rng: np.random.Generator) -> bool:
    return bool(rng.random() < availability)

def simulated_latency(base_latency: float, jitter: float, rng: np.random.Generator) -> float:
    return max(0.0, float(base_latency+rng.normal(0,jitter)))

def staleness_weight(round_now: int, round_created: int, decay: float = 0.35) -> float:
    age=max(0, round_now-round_created)
    return float(np.exp(-decay*age))
