# TwinTrust Baseline

`TwinTrust` is the v0.1 research baseline. It is deliberately simple and interpretable.

For client *i*, trust combines:

- local digital-twin trust derived from consistency and uncertainty;
- update-geometry similarity based on robust norm statistics;
- local data quality;
- network quality;
- update freshness;
- historical trust.

The trust score is used as an aggregation weight and optionally as an acceptance threshold.

This is **not** presented as an optimal or theoretically Byzantine-secure method. Its value is as a transparent baseline for testing whether cyber-physical evidence adds information beyond update geometry.
