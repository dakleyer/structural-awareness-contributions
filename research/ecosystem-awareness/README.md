# Ecosystem Awareness — entry-point router

> **Working router.** This page introduces the architecture, presents the benchmark route and sends readers to three preserved destination indexes. It does not replace or reorganize those corpora.

## What problem this addresses

An agent or institution can be locally correct while the wider decision remains unsupported: evidence may be incomplete or correlated, roles and authority may have changed, another component may operate under a different frame, or the time and capacity required to remove uncertainty may exceed the useful response horizon. Adding more context, agents or review does not by itself establish that the resulting whole is sufficiently determined.

**Ecosystem Awareness is one of the three maintained technical gates of Ecosystem Positioning**, alongside Regime Awareness and Minimum Sufficient Control / MSCA. EA owns the decision-scoped epistemic-qualification layer: for a defined decision, scope and time, it states what can responsibly be relied on, what remains unresolved or outside the active window, and what must be requalified when the ecosystem changes. Ecosystem Positioning composes that EA output with Regime Awareness and MSCA/Role/Cartography/Operation outputs; EA does not own the complete positioning architecture.

## Programme lineage — why this architecture exists

EA is not presented as an isolated invention. The programme-level [Structural Awareness README](../../README.md#2-field-notes--research-series) preserves the explanatory lineage:

- [The Cost of Clarity](https://tegrity.ai/series/cost_of_clarity/) — why obtaining sufficient clarity has cost, delay and risk;
- [Human Intelligence Debt](https://tegrity.ai/series/human-intelligence-gap/) — why human attention/review is a finite system resource rather than free external capacity;
- [The Attribution Gap](https://tegrity.ai/series/attribution_gap/) — why real contribution, ownership and formal visibility can diverge;
- [Informational Friction](https://tegrity.ai/series/informational_friction/) — why a representation can drift from the flow on which action depends;
- [Regime Awareness in Adaptive Systems](https://tegrity.ai/series/regime-awareness-in-adaptive-systems/) — why a once-valid decision frame may cease to be valid.

Historical engineering lines such as xSeil and Phylons provide field provenance for bounded coordination, semantic windows and changing operational state. These series/cases motivate questions and tests; they do **not** transfer validation into EA.

## Visual navigation

For a diagram-first orientation before entering the detailed corpus, use the [**Structural / Ecosystem Awareness Visual Guide**](./VISUAL_GUIDE.md). It shows the cumulative research route, architectural ownership, current positioning cycle, requirements-to-evidence pipeline, scenario/profile matrix, validation/case families and the 04 → 05 → 05A FG-TIDA layering. The source documents remain authoritative.

## Current work / next steps

The live research and integration queue is maintained in [**Ecosystem Awareness / Positioning — Living Workplan**](./WORKPLAN.md). It separates active vNext work (Requirements, Benchmark, Testbed coverage and FG-TIDA Specification) from cross-cutting provenance, execution, product-evidence and publication controls. Completed items move out of the active queue into the workplan's short completion record rather than accumulating indefinitely here.

## Current routed indexes

1. [**Ecosystem Awareness — canonical corpus**](./baseline/README.md) — the authoritative EA reading index for foundation, requirements, topology, functional architecture, interfaces and EHD, validation profiles, benchmarks, research lineage, governance, provenance and linked case material.
2. [**Minimum Sufficient Control / MSCA**](../../standards/minimum-sufficient-control/README.md) — the control-sufficiency and authorized-response line, including its proposed interfaces with EA.
3. [**Regime Awareness**](../regime-awareness/README.md) — the operating-validity line, including Minimalistic Regime-Aware Early Warning Systems and the Regime Change Detection review route.

The canonical corpus index also hosts three additive, non-frozen **Ecosystem Positioning-related extensions for lineage and routing**: [**01H Participant-Local Ecosystem Positioning & Decision-Scoped Epistemic Opportunity**](./baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md), which makes the distributed/no-supercontroller reading explicit and feeds the later canonical agentic-gradient law; [**01I Agentic Citizenship Contract**](./baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md), a separate human-governed participation/constraint neighbour outside the EA core; and [**01J Ecosystem Signalling**](./baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md), the current signalling route for selective disclosure, compatibility mapping, ACC/authority qualification and qualified inputs to downstream agentic repositioning without assuming common governance or a global state. The earlier Distributed Opportunity file remains preserved as provenance in the canonical corpus.

## Benchmark — what is being compared

The [canonical architecture benchmark and reference-scenario evidence](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) remains the current canonical benchmark for EA-H1–EA-H4. The bounded [00D v0.3 Ecosystem Positioning draft](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) is the active Benchmark-vNext design and does **not** supersede v0.2 yet.


| Arm | Compared configuration | Purpose |
|---|---|---|
| **B0** | Ordinary implementation | Establish the unstrengthened baseline. |
| **B1** | Strong conventional architecture | Include provenance, policy/security controls, checkpoints, retries, fallback, human oversight, tracing and evaluation. |
| **B2** | Interoperability and control-plane architecture | Add identity/access, explicit handoff and cross-system observability. |
| **B3** | B2 plus minimum EA semantics | Test scoped non-fungible determination, proportionate window requalification, orthogonal assessment/posture and interoperable re-entry. |

The decisive rule is symmetric: if B1 or B2 reproduces the proposed EA behaviour with equal or lower burden, that result counts **against** EA differentiation.

### Reference scenarios and executable route

- [00E — 100 Million Tokens / compounding context failure](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md)
- [00F — smart-city mobility systemic divergence](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md)
- [00G — collective false-context convergence / "Bar-to-Napoleon" cascade](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md) — additive candidate scenario; integration into the canonical 00D benchmark is still pending.
- [00D-A01 — bounded reference-oracle and test construction](./baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md)
- [00D-A03 — deterministic Stage-0 harness design](./baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md)
- [RS-00E-Q1a fixture and pre-registration](./baseline/fixtures/RS-00E-Q1a/README.md)

**Current benchmark status:** comparison contract defined · hypotheses and falsifiers defined · scenarios documented · implementation profiles analysed · fixture and harness designed · pre-registration published · **comparative execution pending** · **independent validation pending**.

### Benchmark status dashboard

The sentence above remains the compact status statement. The dashboard below exposes the same programme state by artefact so that design, publication and measured execution are not conflated.

| Stage | Artefact | Current status |
|---|---|---|
| Comparison contract — B0/B1/B2/B3 | [00D — Canonical Architecture Benchmark & Evidence v0.2](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | **Defined** |
| EA-H1–EA-H4 hypotheses and decisive falsifiers | [00D — Canonical Architecture Benchmark & Evidence v0.2](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | **Defined** |
| Reference scenarios 00E / 00F | [00E](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) · [00F](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) | **Documented** |
| Candidate signalling / false-context scenario 00G | [00G](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md) | **Documented candidate** — integration into 00D pending |
| Implementation profiles | [00E-A01](./baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md) · [00E-A02](./baseline/00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.1.md) · [00F-A01](./baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.1.md) · [00F-A02](./baseline/00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.1.md) | **Analysed as design profiles** — not measured benchmark results |
| Reference-oracle / test construction | [00D-A01](./baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) | **Designed** |
| Deterministic Stage-0 harness | [00D-A03](./baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md) | **Designed** |
| Pre-registration | [RS-00E-Q1a fixture](./baseline/fixtures/RS-00E-Q1a/README.md) | **Published** |
| Stage-0 descriptive execution trace | — | **Pending** |
| Comparative execution B0–B3 | — | **Pending** |
| Independent validation / replication | — | **Pending** |

**Evidence boundary:** the current 00D matched-comparator programme directly covers the EA differential represented by EA-H1–EA-H4. Later positioning layers — including the Gradient Law, MSCA Operation / Repositioning, Agentic Citizenship and choreography/signalling extensions — have their own architectural, falsification or conformance conditions but are **not thereby claimed to have completed matched comparator execution in 00D**.

The benchmark is therefore presentable as an inspectable test programme and market/architecture gap analysis. It is not yet evidence of comparative superiority.

## Reading routes

- **Five minutes:** this page → [100 Million Tokens](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) → [mobility divergence](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) → [benchmark status](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md).
- **Architecture:** [canonical EA corpus](./baseline/README.md) → topology → documents 01–04 → 01H/01I/01J → interface annexes.
- **Validation:** benchmark → A01/A03 → validation profiles → fixture/pre-registration → future execution traces.
- **Institutional application:** [EA / FG-TIDA package](./fg-tida/README.md) → specifications/interfaces → cases/tests → provenance.

## Routing rule

This page should remain a router while the programme structure is still being consolidated. New substantive documents, cases, interface annexes, validation material and historical records should be indexed in the appropriate destination README rather than duplicated or removed here. The canonical corpus is preserved as-is; this page only exposes stable entry routes.

**Status:** public working research and test proposals; not adopted standards, completed pilots or certified comparative results.
