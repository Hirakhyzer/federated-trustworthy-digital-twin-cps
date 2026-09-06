from fedtwin.experiments.multiseed import summarize
from fedtwin.experiments.reporting import write_csv
if __name__ == "__main__":
    rows=summarize(); write_csv(rows,"results/multiseed_summary.csv")
    for r in rows:
        print(r["method"], round(r["global_mse_mean"],5), round(r["cyber_f1_mean"],3), round(r["malicious_acceptance_mean"],3), round(r["benign_rejection_mean"],3))
