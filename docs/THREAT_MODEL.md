# Threat Model

The benchmark models abstract, synthetic threats to model-update integrity. Malicious clients may scale, invert, displace, stale, replace-like, or coordinate their in-memory update vectors.

The benchmark also includes benign causes of abnormal updates: sensor faults, physical faults, digital-twin mismatch, domain shift, slow clients and offline clients.

The adversary does not interact with real training clusters, networks, CPS controllers, credentials or protocols. The purpose is defensive algorithm evaluation and fault/attack discrimination.
