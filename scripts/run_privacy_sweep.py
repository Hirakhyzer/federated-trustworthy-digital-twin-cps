from fedtwin.experiments.privacy_sweep import run
from fedtwin.experiments.reporting import write_csv
if __name__ == "__main__":
    rows=run(); write_csv(rows,"results/privacy_sweep.csv")
    for r in rows: print(r["privacy_sigma"],round(r["global_mse"],4),round(r["trust_brier"],3))
