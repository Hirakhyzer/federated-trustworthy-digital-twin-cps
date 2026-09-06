from __future__ import annotations
import numpy as np
from fedtwin.core.math import clamp01

def update_geometry_scores(updates):
    norms=np.asarray([np.linalg.norm(u.vector) for u in updates], dtype=float)
    med=float(np.median(norms)); mad=float(np.median(np.abs(norms-med)))+1e-6
    scores={}
    for u,n in zip(updates,norms):
        z=abs(float(n-med))/(1.4826*mad+1e-6)
        scores[u.client_id]=clamp01(np.exp(-0.45*z))
    return scores
