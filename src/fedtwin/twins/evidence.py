from __future__ import annotations
import numpy as np
from fedtwin.core.types import ClientProfile, LocalEvidence
from fedtwin.domains.profiles import DOMAIN_PROFILES
from fedtwin.core.math import clamp01

def generate_evidence(client: ClientProfile, rng: np.random.Generator, condition: str | None = None) -> LocalEvidence:
    condition = condition or client.condition
    p=DOMAIN_PROFILES[client.domain]
    consistency=p.twin_reliability + rng.normal(0, p.intrinsic_noise)
    uncertainty=(1.0-p.twin_reliability) + abs(rng.normal(0, p.intrinsic_noise/2))
    dq=client.data_quality
    net=clamp01(1.0 - 0.08*client.latency)
    shift=0.0
    if condition in {"sensor_fault", "physical_fault"}:
        consistency -= 0.45
        dq -= 0.18
    elif condition == "model_mismatch":
        consistency -= 0.38
        uncertainty += 0.25
    elif condition == "domain_shift":
        consistency -= 0.12
        shift = 0.72
    elif condition in {"scaling_attack","sign_flip","outlier_attack","model_replacement","coordinated_attack"}:
        consistency -= 0.50
    elif condition == "stale_update":
        net -= 0.35
    elif condition == "slow_client":
        net -= 0.25
    return LocalEvidence(
        twin_consistency=clamp01(consistency),
        twin_uncertainty=clamp01(uncertainty),
        data_quality=clamp01(dq),
        network_quality=clamp01(net),
        operational_shift=clamp01(shift),
    )
