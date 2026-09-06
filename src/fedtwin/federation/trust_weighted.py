from .fedavg import aggregate as fedavg

def aggregate(updates, trusts):
    weights=[]
    for u in updates:
        weights.append(max(1e-6, trusts.get(u.client_id, 0.0))*u.sample_count)
    return fedavg(updates, weights=weights)
