import numpy as np
from fedtwin.core.types import ModelUpdate, LocalEvidence
from fedtwin.federation.median import aggregate

def mk(i,x): return ModelUpdate(str(i),"battery",np.array([x,x]),1,0,LocalEvidence(.9,.1,.9,.9))
def test_median_rejects_extreme_coordinate():
    assert np.allclose(aggregate([mk(1,0),mk(2,1),mk(3,100)]),[1,1])
