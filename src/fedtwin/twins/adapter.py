from dataclasses import dataclass
from fedtwin.domains.profiles import domain_target

@dataclass
class TwinAdapter:
    domain: str
    dim: int = 8
    def expected_model(self):
        return domain_target(self.domain, self.dim)
