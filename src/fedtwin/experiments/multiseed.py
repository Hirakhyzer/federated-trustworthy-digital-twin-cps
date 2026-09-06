from __future__ import annotations
import numpy as np
from fedtwin.experiments.simulator import run_experiment

def summarize(seeds=(11,22,33,44,55), malicious_fraction=0.3, attack_type="scaling_attack"):
    rows=[]
    for method in ["fedavg","median","trimmed_mean","trust_weighted","twintrust"]:
        runs=[run_experiment(method=method,malicious_fraction=malicious_fraction,attack_type=attack_type,seed=s) for s in seeds]
        row={"method":method,"n_seeds":len(seeds),"malicious_fraction":malicious_fraction,"attack_type":attack_type}
        for key in ["global_mse","worst_domain_mse","cyber_f1","trust_brier","trust_ranking","malicious_acceptance","benign_rejection","final_diagnosis_accuracy"]:
            vals=np.asarray([r[key] for r in runs],dtype=float)
            row[key+"_mean"]=float(vals.mean())
            row[key+"_std"]=float(vals.std(ddof=1)) if len(vals)>1 else 0.0
        rows.append(row)
    return rows
