from __future__ import annotations
from fedtwin.experiments.simulator import run_experiment

def poisoning_sweep(seed=42):
    methods=["fedavg","median","trimmed_mean","trust_weighted","twintrust"]
    rows=[]
    for frac in [0.0,0.1,0.2,0.3,0.4]:
        for method in methods:
            rows.append(run_experiment(method=method,malicious_fraction=frac,attack_type="scaling_attack",seed=seed))
    return rows

def attack_suite(seed=42):
    rows=[]
    for attack in ["scaling_attack","sign_flip","outlier_attack","stale_update","model_replacement","coordinated_attack"]:
        for method in ["fedavg","median","trimmed_mean","twintrust"]:
            rows.append(run_experiment(method=method,malicious_fraction=0.2,attack_type=attack,seed=seed))
    return rows

def fault_ambiguity(seed=42):
    rows=[]
    for mix in [
        {"sensor_fault":0.2}, {"model_mismatch":0.2}, {"domain_shift":0.2},
        {"slow_client":0.2}, {"sensor_fault":0.1,"scaling_attack":0.1},
    ]:
        rows.append(run_experiment(method="twintrust",malicious_fraction=0.0,condition_mix=mix,seed=seed))
    return rows
