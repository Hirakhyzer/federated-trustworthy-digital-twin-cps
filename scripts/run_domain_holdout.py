from fedtwin.experiments.domain_holdout import leave_one_domain_out
from fedtwin.experiments.reporting import write_csv
if __name__ == "__main__":
    rows=leave_one_domain_out(); write_csv(rows,"results/domain_holdout.csv",fields=["held_out","representation_gap"])
    for r in rows: print(r["held_out"],round(r["representation_gap"],3))
