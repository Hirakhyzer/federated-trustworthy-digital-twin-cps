from fedtwin.experiments.async_sweep import run
from fedtwin.experiments.reporting import write_csv
if __name__ == "__main__":
    rows=run(); write_csv(rows,"results/async_sweep.csv")
    for r in rows: print(round(r["global_mse"],4),round(r["cyber_f1"],3))
