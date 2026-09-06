from dataclasses import dataclass

@dataclass
class SimulationConfig:
    rounds: int = 12
    clients_per_round: int = 14
    model_dim: int = 8
    local_lr: float = 0.35
    local_noise: float = 0.04
    seed: int = 42
