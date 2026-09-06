from fedtwin.core.types import ModelUpdate, LocalEvidence
from fedtwin.diagnosis.classifier import diagnose
import numpy as np

def test_domain_shift_not_forced_to_cyber():
    u=ModelUpdate("c","robot",np.zeros(2),1,0,LocalEvidence(.75,.15,.9,.9,.8),"domain_shift")
    label,_=diagnose(u,.7,{"twin":.75,"geometry":.7,"network":.9,"data_quality":.9,"freshness":1,"history":.75})
    assert label=="DOMAIN_SHIFT"
