from fedtwin.core.math import clamp01

def twin_trust(consistency: float, uncertainty: float) -> float:
    return clamp01(0.72*consistency + 0.28*(1.0-uncertainty))
