import numpy as np
from fedtwin.privacy.noise import add_gaussian_noise

def test_zero_noise_is_identity():
    v=np.array([1.,2.])
    assert np.allclose(add_gaussian_noise(v,0,np.random.default_rng(1)),v)
