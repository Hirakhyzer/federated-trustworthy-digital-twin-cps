# Trust and Diagnosis

A low trust score is not equivalent to malicious behavior.

The diagnosis layer distinguishes:

- `CLEAN`
- `CYBER_POISONING`
- `SENSOR_OR_PHYSICAL_FAULT`
- `MODEL_MISMATCH`
- `NETWORK_DEGRADATION`
- `DOMAIN_SHIFT`
- `UNKNOWN`

This is central to the research question. A robust aggregator that protects global accuracy by rejecting every unusual client can still be operationally untrustworthy if it systematically excludes legitimate domain shifts or physically degraded sites.
