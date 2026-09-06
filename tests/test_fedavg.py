import numpy as np
from fedtwin.core.types import ModelUpdate, LocalEvidence
from fedtwin.federation.fedavg import aggregate

def u(cid,v,n): return ModelUpdate(cid,"battery",np.array(v,dtype=float),n,0,LocalEvidence(.9,.1,.9,.9))
def test_fedavg_weighted():
    out=aggregate([u("a",[1,1],1),u("b",[3,3],3)])
    assert np.allclose(out,[2.5,2.5])
