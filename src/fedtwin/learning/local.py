from __future__ import annotations
import numpy as np
from fedtwin.core.types import ClientProfile, ModelUpdate
from fedtwin.domains.profiles import domain_target, DOMAIN_PROFILES
from fedtwin.twins.evidence import generate_evidence

def local_update(client: ClientProfile, global_model: np.ndarray, round_index: int, rng: np.random.Generator,
                 local_lr: float = 0.35, local_noise: float = 0.04, condition: str | None = None) -> ModelUpdate:
    condition=condition or client.condition
    target=domain_target(client.domain, len(global_model)).copy()
    p=DOMAIN_PROFILES[client.domain]
    if condition == "domain_shift":
        target = target + p.shift_sensitivity*0.18
    if condition == "model_mismatch":
        target = target + 0.10
    gradient=target-global_model
    update=local_lr*gradient + rng.normal(0, local_noise+p.intrinsic_noise, size=len(global_model))
    evidence=generate_evidence(client, rng, condition)
    return ModelUpdate(client.client_id, client.domain, update, client.sample_count, round_index, evidence, condition)
