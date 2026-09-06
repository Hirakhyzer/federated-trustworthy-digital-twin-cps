import numpy as np
from fedtwin.privacy.clipping import clip_vector

def test_clip_vector_respects_norm():
    v=clip_vector(np.array([3.0,4.0]),1.0)
    assert np.linalg.norm(v) <= 1.0000001
