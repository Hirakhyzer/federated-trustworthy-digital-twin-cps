from fedtwin.experiments.simulator import run_experiment

def run(seed=42):
    return [run_experiment(method="twintrust",malicious_fraction=0.2,privacy_sigma=s,seed=seed) for s in [0.0,0.01,0.03,0.05,0.1,0.2]]
