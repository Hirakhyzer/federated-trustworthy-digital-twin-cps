from fedtwin.experiments.benchmarks import poisoning_sweep
from fedtwin.experiments.reporting import write_csv
if __name__ == "__main__":
    rows=poisoning_sweep(); write_csv(rows,"results/poisoning_sweep.csv")
    for r in rows: print(r["malicious_fraction"],r["method"],round(r["global_mse"],4),round(r["cyber_f1"],3))
