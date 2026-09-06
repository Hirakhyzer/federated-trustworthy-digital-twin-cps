# Federated Trustworthy Digital-Twin CPS

[![CI](https://github.com/Hirakhyzer/federated-trustworthy-digital-twin-cps/actions/workflows/ci.yml/badge.svg)](https://github.com/Hirakhyzer/federated-trustworthy-digital-twin-cps/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-research%20prototype-orange)

A simulation-first research framework for **trustworthy federated intelligence across heterogeneous cyber-physical systems (CPS)**. It combines edge digital-twin evidence, robust aggregation, dynamic client/update trust, synthetic poisoning and fault scenarios, network heterogeneity, privacy-noise abstractions, explainable client diagnosis, and cross-domain evaluation.

> **Research and safety boundary:** this repository is a synthetic defensive benchmark. It does not attack real federated-learning deployments, industrial systems, vehicles, railway infrastructure, utilities, or operational networks. Adversarial modules modify only in-memory simulated model updates. Privacy-noise utilities are research abstractions and do **not** claim formal differential-privacy guarantees.

## PhD-level research question

**Can cyber-physical evidence from local digital twins improve the robustness and interpretability of federated learning across heterogeneous CPS sites, especially when abnormal client updates may arise from cyber poisoning, physical faults, model mismatch, communication degradation, or legitimate domain shift?**

## Research hypotheses

- **H1:** robust aggregation reduces the influence of synthetic malicious updates compared with FedAvg.
- **H2:** cyber-physical/digital-twin evidence improves malicious-client ranking beyond update geometry alone.
- **H3:** naive trust mechanisms can wrongly reject benign but non-IID or faulty clients; explicit diagnosis should reduce this ambiguity.
- **H4:** trust-aware asynchronous weighting can reduce stale-update influence under heterogeneous latency.
- **H5:** privacy noise creates a measurable robustness/utility trade-off and can interact with trust calibration.

## Architecture

```text
Local CPS sites
  ├─ Battery ─ Digital Twin ─ Local Evidence ─ Local Model ┐
  ├─ Water ─── Digital Twin ─ Local Evidence ─ Local Model ┤
  ├─ Robot ─── Digital Twin ─ Local Evidence ─ Local Model ┤
  ├─ Microgrid Digital Twin ─ Local Evidence ─ Local Model ┤
  ├─ Factory ─ Digital Twin ─ Local Evidence ─ Local Model ┤
  ├─ EV ────── Digital Twin ─ Local Evidence ─ Local Model ┤
  └─ Railway ─ Digital Twin ─ Local Evidence ─ Local Model ┘
                                      │
                              Federated Coordinator
                                      │
                    update geometry + twin evidence
                    + data quality + staleness/history
                                      │
                              Client Trust / Diagnosis
                                      │
                      Robust / Trust-Aware Aggregation
                                      │
                                  Global Model
                                      │
                           redistributed to clients
```

## Implemented in v0.1

- seven synthetic CPS domain profiles;
- heterogeneous client populations and non-IID local targets;
- synchronous and asynchronous federation abstractions;
- FedAvg, coordinate median, trimmed mean, norm-clipped FedAvg;
- trust-weighted FedAvg and `TwinTrust` aggregation;
- digital-twin consistency and uncertainty evidence;
- historical client trust;
- update-norm/outlier evidence;
- staleness and data-quality evidence;
- explainable client diagnosis;
- synthetic update scaling, sign flip, outlier, stale, model-replacement-like and coordinated attacks;
- synthetic sensor fault, model mismatch, domain shift, slow/offline client conditions;
- update clipping and Gaussian privacy-noise abstraction;
- poisoning-fraction, latency, privacy-noise, cross-domain and ablation benchmarks;
- reproducible JSON/CSV outputs, tests and GitHub Actions CI.

## Quick start

```bash
git clone https://github.com/Hirakhyzer/federated-trustworthy-digital-twin-cps.git
cd federated-trustworthy-digital-twin-cps
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]"
pytest
python scripts/run_demo.py
python scripts/run_benchmarks.py
```

## Baseline experiments

```bash
python scripts/run_poisoning_sweep.py
python scripts/run_async_sweep.py
python scripts/run_privacy_sweep.py
python scripts/run_domain_holdout.py
```

Outputs are written under `results/` when requested by scripts.

## What counts as success?

A trustworthy method should not only maintain a useful global model. It should also avoid two dangerous simplifications:

1. treating every unusual client as malicious; and
2. trusting every update that looks statistically typical.

The benchmark therefore separates **global model utility**, **malicious influence**, **malicious-client ranking**, **benign-client rejection**, **fault-vs-attack diagnosis**, **communication efficiency**, and **trust calibration**.

## Scientific integrity

All data and models are synthetic and reduced-order. Default parameters are illustrative. Results must not be described as measurements from real factories, EV chargers, railways, robots, utilities, batteries, or water systems. Publications should record software commit, random seed, client composition, domain mix, malicious fraction, attack type, aggregation method, trust configuration, network model and privacy-noise settings.

See `docs/` for architecture, threat model, benchmark protocol, trust model, TwinTrust formulation, privacy caveats, baseline findings, reproducibility, limitations and the PhD roadmap.
