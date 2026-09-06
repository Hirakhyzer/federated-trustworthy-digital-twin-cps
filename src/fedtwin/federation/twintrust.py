from fedtwin.federation.trust_weighted import aggregate as trust_aggregate

def aggregate(updates, trust_map, min_trust: float = 0.62):
    kept=[u for u in updates if trust_map.get(u.client_id,0.0) >= min_trust]
    if not kept:
        kept=list(updates)
    return trust_aggregate(kept, trust_map), [u.client_id for u in kept]
