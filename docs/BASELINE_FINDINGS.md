# v0.1 Baseline Findings

These results are generated entirely by the synthetic reduced-order benchmark. They are not measurements from deployed federated-learning systems or operational CPS sites.

## Validation

- 18/18 unit and integration tests pass locally.
- The standard benchmark includes 25 poisoning-fraction/method combinations, 24 attack-suite combinations, five fault/ambiguity configurations, privacy-noise and asynchronous sweeps, and seven leave-one-domain-out representation checks.

## Poisoning robustness

For the fixed seed (`42`), scaling-attack sweeps show that FedAvg degrades as the malicious fraction rises. Median and trimmed mean remain much more robust. The TwinTrust acceptance threshold further reduces synthetic malicious influence.

At 40% malicious clients:

| Method | Global MSE |
|---|---:|
| FedAvg | 0.005459 |
| Coordinate median | 0.001080 |
| Trimmed mean | 0.001228 |
| Trust-weighted FedAvg | 0.003099 |
| TwinTrust | **0.000497** |

This fixed-seed result is illustrative, not sufficient for a publication claim.

## Five-seed result at 30% malicious clients

Across seeds `11, 22, 33, 44, 55` under the scaling attack:

| Method | Mean global MSE | Std. | Mean malicious acceptance | Mean benign rejection |
|---|---:|---:|---:|---:|
| FedAvg | 0.004691 | 0.003351 | 1.000 | 0.000 |
| Coordinate median | 0.000904 | 0.000270 | 1.000 | 0.000 |
| Trimmed mean | **0.000604** | 0.000161 | 1.000 | 0.000 |
| Trust-weighted FedAvg | 0.002690 | 0.001684 | 1.000 | 0.000 |
| TwinTrust | 0.001443 | 0.000742 | **0.033** | 0.000 |

The interpretation is important: trimmed mean currently wins on average utility in this experiment, while TwinTrust adds explicit client filtering/interpretability. A PhD contribution must therefore demonstrate when cyber-physical trust provides value beyond standard robust statistics, rather than assuming it does.

## Attack suite

At 20% malicious clients, TwinTrust strongly reduces the global-model error for scaling, sign-flip, outlier, model-replacement-like and coordinated synthetic update manipulations relative to FedAvg. The stale-update scenario is different: the update vector itself is not geometrically malicious, so the diagnosis layer often interprets it as communication degradation rather than cyber poisoning.

This is a useful ambiguity, because a stale update can arise from either benign network delay or intentional manipulation.

## Fault and domain-shift ambiguity

The v0.1 rule-based diagnosis correctly preserves legitimate domain shift and most modeled sensor/model/network faults without rejecting those clients in the fixed-seed benchmark. However, this result should **not** be treated as evidence of solved root-cause diagnosis: the simulator currently generates evidence that is intentionally correlated with the ground-truth condition, so the classes remain easier to separate than in a real deployment.

## Privacy-noise abstraction

With TwinTrust and 20% scaling attackers, the fixed-seed global MSE changes from approximately 0.0015 at zero added noise to approximately 0.0027 at Gaussian noise sigma `0.2`. Small noise values are not monotonic because stochastic perturbation can occasionally offset synthetic update bias.

No differential-privacy guarantee is claimed.

## Cross-domain heterogeneity

The leave-one-domain-out representation-gap check confirms that the seven domain targets are meaningfully heterogeneous. The largest baseline gaps are for microgrid (~0.578), water (~0.554) and robot (~0.508), while battery is smaller (~0.356). This is only a geometric diagnostic; it is not yet a federated transfer-learning result.

## Main v0.1 research gaps

1. **TwinTrust does not universally beat robust statistics.** Trimmed mean is stronger in the five-seed 30% scaling benchmark.
2. **Trust ranking is too easy in v0.1.** Synthetic attack evidence is strongly separated, producing near-perfect ranking. Future versions must introduce stealthy/overlapping evidence distributions.
3. **Diagnosis is simulator-assisted.** Evidence distributions are condition-dependent and therefore easier than deployment data.
4. **Stale-update intent is ambiguous.** Network degradation and intentional staleness need explicit causal/temporal modeling.
5. **Low-dimensional vectors are not neural models.** Higher-dimensional models may change robustness behavior.
6. **No formal Byzantine or privacy guarantees are claimed.**
7. **Multi-seed analysis is still small.** Publication work should use larger seed sets, confidence intervals and statistical tests.

The strongest next research question is therefore:

> When does digital-twin/cyber-physical evidence improve federated robustness and diagnosis beyond update-only robust aggregation, especially when benign faults, domain shift and stealthy malicious behavior overlap?
