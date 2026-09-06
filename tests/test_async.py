import numpy as np
from fedtwin.core.types import ModelUpdate, LocalEvidence
from fedtwin.federation.async_fl import aggregate

def mk(cid,v,created): return ModelUpdate(cid,"battery",np.array([v],dtype=float),1,created,LocalEvidence(.9,.1,.9,.9))
def test_async_downweights_stale_update():
    out=aggregate([mk("fresh",1,5),mk("stale",9,0)],5,decay=1.0)
    assert out[0] < 2.0
