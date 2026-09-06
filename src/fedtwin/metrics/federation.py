import numpy as np

def malicious_influence(aggregate_vector, clean_aggregate):
    return float(np.linalg.norm(np.asarray(aggregate_vector)-np.asarray(clean_aggregate)))

def acceptance_rates(accepted_ids, updates, attack_conditions):
    malicious=[u.client_id for u in updates if u.condition in attack_conditions]
    benign=[u.client_id for u in updates if u.condition not in attack_conditions]
    aset=set(accepted_ids)
    mal_accept=sum(i in aset for i in malicious)/(len(malicious) or 1)
    benign_reject=sum(i not in aset for i in benign)/(len(benign) or 1)
    return {"malicious_acceptance":float(mal_accept),"benign_rejection":float(benign_reject)}
