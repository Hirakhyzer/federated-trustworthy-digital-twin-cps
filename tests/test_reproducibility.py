from fedtwin.experiments.simulator import run_experiment

def test_fixed_seed_reproducible():
    a=run_experiment(rounds=3,n_clients=7,malicious_fraction=.2,seed=9)
    b=run_experiment(rounds=3,n_clients=7,malicious_fraction=.2,seed=9)
    assert a["final_model"] == b["final_model"]
