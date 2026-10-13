# FG-TIDA-specific EA tests

> **Navigation:** [Iván Abril Palma](https://github.com/dakleyer/dakleyer) → [Structural Awareness](https://github.com/dakleyer/structural-awareness-contributions) → [Ecosystem Awareness](../../README.md) → [FG-TIDA application package](../README.md) → **FG-TIDA-specific tests**


This folder contains tests whose fixture or interface meaning is specifically tied to FG-TIDA.

## Current tests

- [EA-ITP-01 — EHD / Theme #13 Cross-Implementation Interoperability Test v0.1](./EA-ITP-01_v0.1_FROZEN.md)
- [FG-TIDA Decision Boundary Evaluation Profile v0.1 Draft](./FG_TIDA_DECISION_BOUNDARY_EVALUATION_PROFILE_v0.1_DRAFT.md) — cross-Theme test/conformance projection of the general Decision Boundary Challenge; current staged route is UC-6 semantic mapping → contributor review/freeze → bounded UC-4 executable profile.

EA-ITP-01 tests the Theme #13 / UC #4 interoperability profile of the general EHD without turning Theme #13 fields into the universal EA interface.

The Decision Boundary profile tests a different but complementary property: whether independently owned Theme outputs remain semantically distinct and correctly composed at a material decision boundary. It links back to the programme-independent [Decision Boundary Challenge v0.2](../../DECISION_BOUNDARY_CHALLENGE_v0.2.md) and forward to [Specification Preparation v0.3](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md).

The four general EA validation profiles remain in the [canonical EA corpus](../../baseline/README.md).


## Flores Theme #21 — campaign DDS-EA-FG21-FLORES-01 (registered candidate, 13 October 2026)

[**Open the sole owning campaign record: Population / blind→unblind residual discriminability**](./flores-population-theme21/CAMPAIGN.md). It includes the source-native Stage-1 contract, Olena's identifiability sequence, P0–P3 receiver-only proof-link ablations, EA 04/05A/EHD source-qualification constraints, a matched strong B2 comparator, audit dispositions, archive hashes, 20 mutable-comment SHA records, public mock code and explicit Stage-A readiness gaps. It is a **proposed Stage A campaign**, not a completed Flores run, B2 result or accepted FG-TIDA interface. No upstream code or frozen tests are modified. The DDS methodology remains owned by the [central method index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md).
