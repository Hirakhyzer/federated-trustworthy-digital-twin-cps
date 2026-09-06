from __future__ import annotations
from fedtwin.core.types import ClientProfile

DEFAULT_DOMAINS = ["battery","water","robot","microgrid","factory","ev","railway"]

def make_population(n_clients: int = 21, malicious_fraction: float = 0.0, seed: int = 42):
    import numpy as np
    rng=np.random.default_rng(seed)
    clients=[]
    malicious_n=int(round(n_clients*malicious_fraction))
    malicious=set(rng.choice(n_clients, size=malicious_n, replace=False).tolist()) if malicious_n else set()
    for i in range(n_clients):
        domain=DEFAULT_DOMAINS[i % len(DEFAULT_DOMAINS)]
        condition="scaling_attack" if i in malicious else "clean"
        clients.append(ClientProfile(
            client_id=f"c{i:02d}", domain=domain,
            sample_count=int(rng.integers(70, 180)),
            data_quality=float(rng.uniform(0.88, 1.0)),
            latency=float(rng.uniform(0.0, 2.0)),
            available=True,
            condition=condition,
        ))
    return clients
