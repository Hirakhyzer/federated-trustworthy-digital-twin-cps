from dataclasses import dataclass, field
from fedtwin.core.math import clamp01

@dataclass
class TrustHistory:
    values: dict[str, float] = field(default_factory=dict)
    momentum: float = 0.75
    def get(self, client_id: str) -> float:
        return self.values.get(client_id, 0.75)
    def update(self, client_id: str, observation: float) -> float:
        old=self.get(client_id)
        new=clamp01(self.momentum*old+(1-self.momentum)*observation)
        self.values[client_id]=new
        return new
