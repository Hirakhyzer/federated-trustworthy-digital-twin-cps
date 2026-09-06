from __future__ import annotations
from fedtwin.core.math import clamp01

def diagnose(update, trust: float, reasons: dict) -> tuple[str,float]:
    twin=reasons["twin"]; geom=reasons["geometry"]; net=reasons["network"]; fresh=reasons["freshness"]
    shift=update.evidence.operational_shift
    if shift > 0.55 and twin > 0.45:
        return "DOMAIN_SHIFT", clamp01(0.55+0.35*shift)
    if fresh < 0.60 and net < 0.80 and geom > 0.40:
        return "NETWORK_DEGRADATION", clamp01(0.55+0.30*(1-fresh))
    if update.evidence.twin_uncertainty > 0.32 and geom > 0.42:
        return "MODEL_MISMATCH", clamp01(0.55+0.30*update.evidence.twin_uncertainty)
    if twin < 0.68 and update.evidence.data_quality < 0.82 and geom > 0.40:
        return "SENSOR_OR_PHYSICAL_FAULT", clamp01(0.58+0.25*(1-twin))
    if geom < 0.42 and twin < 0.65:
        return "CYBER_POISONING", clamp01(0.60+0.25*(1-trust))
    if trust >= 0.62:
        return "CLEAN", clamp01(0.60+0.35*trust)
    return "UNKNOWN", clamp01(0.45+0.30*(1-trust))
