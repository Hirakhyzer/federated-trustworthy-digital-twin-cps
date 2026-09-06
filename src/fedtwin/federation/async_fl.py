from .fedavg import aggregate as fedavg
from fedtwin.network.model import staleness_weight

def aggregate(updates, round_now: int, trusts=None, decay: float = 0.35):
    weights=[]
    trusts=trusts or {}
    for u in updates:
        t=trusts.get(u.client_id, 1.0)
        weights.append(u.sample_count*t*staleness_weight(round_now,u.round_created,decay))
    return fedavg(updates, weights=weights)
