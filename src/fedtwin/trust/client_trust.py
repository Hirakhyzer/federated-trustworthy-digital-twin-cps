from __future__ import annotations
from fedtwin.core.math import clamp01
from fedtwin.twins.trust import twin_trust
from fedtwin.network.model import staleness_weight

def compute_client_trust(update, geometry_score: float, historical: float, round_now: int,
                         twin_weight: float = 0.34, geometry_weight: float = 0.22) -> tuple[float, dict]:
    twin=twin_trust(update.evidence.twin_consistency, update.evidence.twin_uncertainty)
    data=update.evidence.data_quality
    net=update.evidence.network_quality
    stale=staleness_weight(round_now, update.round_created, decay=0.45)
    score=(
        twin_weight*twin +
        geometry_weight*geometry_score +
        0.14*data +
        0.10*net +
        0.10*stale +
        0.10*historical
    )
    if update.evidence.operational_shift > 0.5:
        # legitimate domain shift should not automatically mean malicious.
        score += 0.05
    reasons={"twin":twin,"geometry":geometry_score,"data_quality":data,"network":net,"freshness":stale,"history":historical}
    return clamp01(score), reasons
