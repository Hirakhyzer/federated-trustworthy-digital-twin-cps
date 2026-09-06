import numpy as np
from fedtwin.core.types import ClientProfile
from fedtwin.twins.evidence import generate_evidence

def test_attack_reduces_twin_consistency_on_average_case():
    c=ClientProfile("c","battery")
    clean=generate_evidence(c,np.random.default_rng(5),"clean")
    attacked=generate_evidence(c,np.random.default_rng(5),"scaling_attack")
    assert attacked.twin_consistency < clean.twin_consistency
