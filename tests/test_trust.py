import numpy as np
from fedtwin.core.types import ClientProfile
from fedtwin.learning.local import local_update
from fedtwin.attacks.scaling import apply
from fedtwin.trust.history import TrustHistory
from fedtwin.trust.engine import assess_updates

def test_extreme_attacked_client_gets_lower_trust():
    rng=np.random.default_rng(2); g=np.ones(8)*0.5
    clean=local_update(ClientProfile("clean","battery"),g,1,rng,condition="clean")
    bad=local_update(ClientProfile("bad","water"),g,1,rng,condition="scaling_attack"); bad=apply(bad,8)
    assessments,_=assess_updates([clean,bad],1,TrustHistory())
    d={a.client_id:a.trust for a in assessments}
    assert d["bad"] < d["clean"]
