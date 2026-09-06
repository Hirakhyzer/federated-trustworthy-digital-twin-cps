from __future__ import annotations
from fedtwin.core.types import ModelUpdate

ATTACK_CONDITIONS={"scaling_attack","sign_flip","outlier_attack","stale_update","model_replacement","coordinated_attack"}

def is_attack(condition: str) -> bool:
    return condition in ATTACK_CONDITIONS
