from __future__ import annotations
from fedtwin.trust.update_evidence import update_geometry_scores
from fedtwin.trust.client_trust import compute_client_trust
from fedtwin.diagnosis.classifier import diagnose
from fedtwin.core.types import ClientAssessment

def assess_updates(updates, round_now: int, history):
    geometry=update_geometry_scores(updates)
    assessments=[]
    trust_map={}
    for u in updates:
        trust,reasons=compute_client_trust(u, geometry[u.client_id], history.get(u.client_id), round_now)
        label,confidence=diagnose(u, trust, reasons)
        history.update(u.client_id, trust)
        trust_map[u.client_id]=trust
        assessments.append(ClientAssessment(u.client_id, trust, label, confidence, reasons))
    return assessments, trust_map
