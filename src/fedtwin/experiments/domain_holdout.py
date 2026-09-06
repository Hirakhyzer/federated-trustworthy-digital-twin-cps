from __future__ import annotations
import numpy as np
from fedtwin.domains.profiles import DOMAIN_PROFILES, domain_target

def leave_one_domain_out(dim: int = 8):
    rows=[]
    domains=list(DOMAIN_PROFILES)
    for held in domains:
        train=[d for d in domains if d != held]
        center=np.mean([domain_target(d,dim) for d in train],axis=0)
        held_target=domain_target(held,dim)
        gap=float(np.linalg.norm(held_target-center))
        rows.append({"held_out":held,"train_domains":train,"representation_gap":gap})
    return rows
