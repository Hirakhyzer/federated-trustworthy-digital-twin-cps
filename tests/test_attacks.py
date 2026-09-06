import numpy as np
from fedtwin.core.types import ClientProfile
from fedtwin.learning.local import local_update
from fedtwin.attacks.scaling import apply

def test_scaling_attack_changes_vector():
    rng=np.random.default_rng(1); c=ClientProfile("c","battery")
    u=local_update(c,np.ones(8)*0.5,1,rng)
    a=apply(u,5)
    assert np.linalg.norm(a.vector) > np.linalg.norm(u.vector)
    assert a.condition=="scaling_attack"
