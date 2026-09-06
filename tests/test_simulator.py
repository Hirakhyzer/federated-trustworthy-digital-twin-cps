from fedtwin.experiments.simulator import run_experiment

def test_simulator_runs_and_returns_metrics():
    r=run_experiment(rounds=3,n_clients=7,malicious_fraction=.2,seed=3)
    assert r["global_mse"] >= 0
    assert 0 <= r["trust_ranking"] <= 1
