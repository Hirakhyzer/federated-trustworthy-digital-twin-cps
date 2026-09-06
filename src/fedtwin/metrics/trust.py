import numpy as np

def brier_score(prob_malicious, truth_malicious):
    p=np.asarray(prob_malicious,dtype=float); y=np.asarray(truth_malicious,dtype=float)
    return float(np.mean((p-y)**2)) if len(p) else 0.0

def ranking_accuracy(trusts, truth_malicious):
    mal=[t for t,y in zip(trusts,truth_malicious) if y]
    benign=[t for t,y in zip(trusts,truth_malicious) if not y]
    if not mal or not benign: return 1.0
    wins=sum(1 for m in mal for b in benign if m < b)
    ties=sum(1 for m in mal for b in benign if m == b)
    return float((wins+0.5*ties)/(len(mal)*len(benign)))
