import numpy as np
from fedtwin.domains.profiles import domain_target

def per_domain_error(model, domains):
    return {d: float(np.mean((model-domain_target(d, len(model)))**2)) for d in domains}

def worst_domain_error(model, domains):
    vals=per_domain_error(model, domains)
    return max(vals.values()) if vals else 0.0
