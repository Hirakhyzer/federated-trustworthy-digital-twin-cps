from .profiles import DOMAIN_PROFILES, domain_target

def profile():
    return DOMAIN_PROFILES["battery"]

def target(dim: int = 8):
    return domain_target("battery", dim)
