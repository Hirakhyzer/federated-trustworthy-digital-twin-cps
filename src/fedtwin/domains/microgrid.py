from .profiles import DOMAIN_PROFILES, domain_target

def profile():
    return DOMAIN_PROFILES["microgrid"]

def target(dim: int = 8):
    return domain_target("microgrid", dim)
