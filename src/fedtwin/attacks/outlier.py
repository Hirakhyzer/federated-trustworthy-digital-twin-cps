from dataclasses import replace
import numpy as np

def apply(update, magnitude: float = 2.2):
    direction=np.sign(update.vector + 1e-9)
    return replace(update, vector=update.vector + magnitude*direction, condition="outlier_attack")
