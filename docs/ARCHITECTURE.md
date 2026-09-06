# Architecture

The framework separates local cyber-physical reasoning from federated coordination.

Each simulated client has a CPS domain profile, local model target, digital-twin consistency/uncertainty evidence, data-quality state and network state. The coordinator receives only an abstract model update plus metadata/evidence. It does not receive raw sensor streams.

The coordinator computes update geometry, fuses it with twin/data/network/history evidence, produces a trust score and diagnosis, then aggregates updates using a selected method.

This separation supports ablations such as geometry-only trust versus twin-aware trust and makes it possible to study benign non-IID clients, faulty clients and malicious clients under the same interface.
