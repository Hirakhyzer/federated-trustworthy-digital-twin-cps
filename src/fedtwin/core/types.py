from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import numpy as np

@dataclass
class ClientProfile:
    client_id: str
    domain: str
    sample_count: int = 100
    data_quality: float = 1.0
    latency: float = 0.0
    available: bool = True
    condition: str = "clean"

@dataclass
class LocalEvidence:
    twin_consistency: float
    twin_uncertainty: float
    data_quality: float
    network_quality: float
    operational_shift: float = 0.0

@dataclass
class ModelUpdate:
    client_id: str
    domain: str
    vector: np.ndarray
    sample_count: int
    round_created: int
    evidence: LocalEvidence
    condition: str = "clean"
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class ClientAssessment:
    client_id: str
    trust: float
    label: str
    confidence: float
    reasons: dict[str, float]

@dataclass
class RoundResult:
    round_index: int
    global_model: np.ndarray
    assessments: list[ClientAssessment]
    accepted_clients: list[str]
    metrics: dict[str, float]
