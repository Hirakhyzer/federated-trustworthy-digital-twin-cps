from __future__ import annotations
import numpy as np
from dataclasses import replace
from fedtwin.core.config import SimulationConfig
from fedtwin.domains.population import make_population, DEFAULT_DOMAINS
from fedtwin.domains.profiles import population_oracle
from fedtwin.learning.model import init_model, model_error
from fedtwin.learning.local import local_update
from fedtwin.learning.evaluation import worst_domain_error
from fedtwin.attacks.engine import apply_condition
from fedtwin.attacks.base import ATTACK_CONDITIONS
from fedtwin.privacy.clipping import clip_vector
from fedtwin.privacy.noise import add_gaussian_noise
from fedtwin.trust.history import TrustHistory
from fedtwin.trust.engine import assess_updates
from fedtwin.federation import fedavg, median, trimmed_mean, clipped, trust_weighted, twintrust, async_fl
from fedtwin.metrics.trust import brier_score, ranking_accuracy
from fedtwin.metrics.classification import confusion
from fedtwin.metrics.federation import acceptance_rates
from fedtwin.network.communication import estimated_bytes

AGGREGATORS=("fedavg","median","trimmed_mean","clipped","trust_weighted","twintrust","async_twintrust")

def _aggregate(method, updates, trust_map, round_index):
    if method == "fedavg": return fedavg.aggregate(updates), [u.client_id for u in updates]
    if method == "median": return median.aggregate(updates), [u.client_id for u in updates]
    if method == "trimmed_mean": return trimmed_mean.aggregate(updates,0.2), [u.client_id for u in updates]
    if method == "clipped": return clipped.aggregate(updates,1.0), [u.client_id for u in updates]
    if method == "trust_weighted": return trust_weighted.aggregate(updates,trust_map), [u.client_id for u in updates]
    if method == "twintrust": return twintrust.aggregate(updates,trust_map,0.62)
    if method == "async_twintrust": return async_fl.aggregate(updates,round_index,trust_map,0.35), [u.client_id for u in updates if trust_map.get(u.client_id,0)>=0.62]
    raise ValueError(method)

def run_experiment(method: str = "twintrust", malicious_fraction: float = 0.2, attack_type: str = "scaling_attack",
                   n_clients: int = 21, rounds: int = 12, seed: int = 42, privacy_sigma: float = 0.0,
                   condition_mix: dict[str,float] | None = None):
    cfg=SimulationConfig(rounds=rounds, clients_per_round=n_clients, seed=seed)
    rng=np.random.default_rng(seed)
    clients=make_population(n_clients, malicious_fraction=0.0, seed=seed)
    # assign conditions deterministically under RNG
    idx=np.arange(n_clients); rng.shuffle(idx)
    cursor=0
    if malicious_fraction > 0:
        k=int(round(n_clients*malicious_fraction))
        for i in idx[cursor:cursor+k]: clients[int(i)].condition=attack_type
        cursor += k
    if condition_mix:
        for condition, frac in condition_mix.items():
            k=int(round(n_clients*frac))
            for i in idx[cursor:cursor+k]: clients[int(i)].condition=condition
            cursor += k
    model=init_model(cfg.model_dim, seed)
    history=TrustHistory()
    all_truth=[]; all_pred=[]; all_trust=[]; total_bytes=0
    last_assessments=[]; last_updates=[]; accepted=[]
    for r in range(cfg.rounds):
        updates=[]
        for c in clients:
            if c.condition == "offline_client":
                continue
            u=local_update(c,model,r,rng,cfg.local_lr,cfg.local_noise,c.condition)
            u=apply_condition(u,c.condition)
            if c.condition == "slow_client":
                u=replace(u, round_created=max(0,r-2))
            if privacy_sigma > 0:
                v=clip_vector(u.vector,1.0)
                v=add_gaussian_noise(v,privacy_sigma,rng)
                u=replace(u,vector=v)
            updates.append(u)
        assessments,trust_map=assess_updates(updates,r,history)
        delta,accepted=_aggregate(method,updates,trust_map,r)
        model=model+delta
        total_bytes += estimated_bytes(len(updates),len(model))
        amap={a.client_id:a for a in assessments}
        for u in updates:
            truth=u.condition in ATTACK_CONDITIONS
            pred=amap[u.client_id].label == "CYBER_POISONING"
            all_truth.append(truth); all_pred.append(pred); all_trust.append(amap[u.client_id].trust)
        last_assessments=assessments; last_updates=updates
    domains=sorted({c.domain for c in clients})
    oracle=population_oracle([c.domain for c in clients],cfg.model_dim)
    cls=confusion(all_truth,all_pred)
    prob_mal=[1-t for t in all_trust]
    rates=acceptance_rates(accepted,last_updates,ATTACK_CONDITIONS)
    truth_label={
        "clean":"CLEAN", "sensor_fault":"SENSOR_OR_PHYSICAL_FAULT", "physical_fault":"SENSOR_OR_PHYSICAL_FAULT",
        "model_mismatch":"MODEL_MISMATCH", "domain_shift":"DOMAIN_SHIFT", "slow_client":"NETWORK_DEGRADATION",
        "offline_client":"NETWORK_DEGRADATION", "scaling_attack":"CYBER_POISONING", "sign_flip":"CYBER_POISONING",
        "outlier_attack":"CYBER_POISONING", "stale_update":"CYBER_POISONING", "model_replacement":"CYBER_POISONING",
        "coordinated_attack":"CYBER_POISONING",
    }
    amap={a.client_id:a for a in last_assessments}
    diag_correct=sum(amap[u.client_id].label==truth_label.get(u.condition,"UNKNOWN") for u in last_updates)
    diag_accuracy=diag_correct/(len(last_updates) or 1)
    return {
        "method":method,"seed":seed,"rounds":rounds,"n_clients":n_clients,"malicious_fraction":malicious_fraction,
        "attack_type":attack_type,"privacy_sigma":privacy_sigma,
        "global_mse":model_error(model,oracle),"worst_domain_mse":worst_domain_error(model,domains),
        "cyber_precision":cls["precision"],"cyber_recall":cls["recall"],"cyber_f1":cls["f1"],
        "trust_brier":brier_score(prob_mal,all_truth),"trust_ranking":ranking_accuracy(all_trust,all_truth),
        "communication_bytes":total_bytes,
        "malicious_acceptance":rates["malicious_acceptance"],
        "benign_rejection":rates["benign_rejection"],
        "final_diagnosis_accuracy":diag_accuracy,
        "final_model":model.tolist(),
        "accepted_final":accepted,
        "final_assessments":[{"client_id":a.client_id,"trust":a.trust,"label":a.label,"confidence":a.confidence,"reasons":a.reasons} for a in last_assessments],
        "final_conditions":{u.client_id:u.condition for u in last_updates},
    }
