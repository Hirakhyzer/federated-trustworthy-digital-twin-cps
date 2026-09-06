# Limitations

v0.1 is intentionally reduced-order.

- Model updates are low-dimensional synthetic vectors, not neural-network tensors.
- Domain profiles are illustrative rather than calibrated to real facilities.
- Digital-twin evidence is generated from abstract consistency/uncertainty profiles.
- Client trust is heuristic and not formally Byzantine secure.
- Privacy noise has no formal DP guarantee.
- Network behavior is not packet-level.
- The diagnosis rules use simulator-accessible evidence and may not transfer directly to deployments.
- Global MSE is measured against a synthetic oracle that is known only because this is a simulator.

These are research baselines, not deployment claims.
