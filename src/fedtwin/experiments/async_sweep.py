from fedtwin.experiments.simulator import run_experiment

def run(seed=42):
    rows=[]
    for slow in [0.0,0.1,0.2,0.3,0.4]:
        rows.append(run_experiment(method="async_twintrust",malicious_fraction=0.1,condition_mix={"slow_client":slow},seed=seed))
    return rows
