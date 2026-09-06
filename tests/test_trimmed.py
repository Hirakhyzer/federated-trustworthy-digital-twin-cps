import numpy as np
from fedtwin.core.types import ModelUpdate, LocalEvidence
from fedtwin.federation.trimmed_mean import aggregate

def mk(i,x): return ModelUpdate(str(i),"battery",np.array([x]),1,0,LocalEvidence(.9,.1,.9,.9))
def test_trimmed_mean_reduces_outliers():
    out=aggregate([mk(1,-100),mk(2,0),mk(3,1),mk(4,2),mk(5,100)],0.2)
    assert np.allclose(out,[1.0])
