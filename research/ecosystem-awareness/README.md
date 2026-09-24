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


## FG-TIDA / Theme #13 — current charter preparation

The current public working draft for the proposed Theme #13 work structure is:

- [**Annex 01G — FG-TIDA Theme #13 Working Group / Charter Preparation Draft**](./fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md)

This is the direct entry point for the **Ecosystem-level Agent Defense + Ecosystem Awareness** charter preparation. It is a living preparation draft, not a submitted or adopted FG-TIDA charter.

The draft itself contains a short **About / minimum reading path** and links directly to the architecture it depends on:

- frozen Requirements + Requirements vNext Delta;
- 04 General Interfaces + 04 vNext Delta;
- 05 Ideal FG-TIDA Interfaces + 05 Ideal Delta; and
- 05A Current-State Bridge + 05A Current-State Delta.

The drafting rule is: **05 defines the target architecture; 05A determines what can responsibly be treated as current/mature in the draft.** The broader [FG-TIDA application package](./fg-tida/README.md) remains available for specification preparation, interfaces, cases, tests and provenance, but a reviewer who only needs the current charter draft should use the direct 01G link above.

## Current routed indexes

1. [**Ecosystem Awareness — canonical corpus**](./baseline/README.md) — the authoritative EA reading index for foundation, requirements, topology, functional architecture, interfaces and EHD, validation profiles, benchmarks, research lineage, governance, provenance and linked case material.
2. [**Minimum Sufficient Control / MSCA**](../../standards/minimum-sufficient-control/README.md) — the control-sufficiency and authorized-response line, including its proposed interfaces with EA.
3. [**Regime Awareness**](../regime-awareness/README.md) — the operating-validity line, including Minimalistic Regime-Aware Early Warning Systems and the Regime Change Detection review route.

The canonical corpus index also hosts three additive, non-frozen **Ecosystem Positioning-related extensions for lineage and routing**: [**01H Participant-Local Ecosystem Positioning & Decision-Scoped Epistemic Opportunity**](./baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md), which makes the distributed/no-supercontroller reading explicit and feeds the later canonical agentic-gradient law; [**01I Agentic Citizenship Contract**](./baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md), a separate human-governed participation/constraint neighbour outside the EA core; and [**01J Ecosystem Signalling**](./baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md), the current signalling route for selective disclosure, compatibility mapping, ACC/authority qualification and qualified inputs to downstream agentic repositioning without assuming common governance or a global state. The earlier Distributed Opportunity file remains preserved as provenance in the canonical corpus.

## Benchmark — what is being compared

The [canonical architecture benchmark and reference-scenario evidence](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) uses matched comparison arms so that EA is tested against progressively stronger alternatives rather than against a weak strawman:

**Benchmark vNext:** the bounded [00D v0.3 Ecosystem Positioning draft](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) extends the design toward the later positioning architecture but does **not** supersede v0.2. v0.2 remains the current canonical benchmark for EA-H1–EA-H4 until the v0.3 adoption gates close.


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
- [00G — collective false-context convergence / "Bar-to-Napoleon" cascade](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.3_DRAFT.md) — latest working draft; v0.3 retains the paired opaque false/genuine control and adds DBC-namespaced gate dispositions, S1 authority-applicability coverage and fully instrumented KPI rates; v0.2 remains preserved; 00D/W3 admission remains pending.
- [00H — batch opportunity beyond authority / "The Quiet Four Thousand"](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.4_DRAFT.md) — latest working draft for C12 / DBC-C05; preserves the base and V14–V18 strong-peer stress, then adds V19/V20 adaptive delegation / authority-laundering: locally valid leaf grants can compose into one root-unauthorized campaign. U/G/I paired controls and S8 non-amplification/root-lineage gates prevent trivial deny-all or aggregate-everything solutions; not yet W3-admitted.
- [00I — semantic TOCTOU / "The Patch That Undid the Fix"](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.2_DRAFT.md) — latest working draft for DBC-C02; a previously correct queued database remediation remains technically authorized after a later fix/freeze changes the decision basis. Q0–Q6 distinguish technical validity, explicit decision basis, time-of-use requalification, authoritative freshness, intervening state/version change, bounded response and check-to-act binding. The scenario maps the core failure to existing S1/S3/S10/S14 → T1–T4 → H2/H5/H6, records CAND-R4 as a clarification candidate rather than a new requirement, and includes public database/cloud corroboration; not yet W3-admitted or executed.
- [00J — rights-provenance inversion / "The Author Pays for Their Own Work"](./baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) — a valid generation/provenance record is allowed to propagate into an unsupported downstream rights claim. Q0–Q5 is derived directly from the frozen S1–S14/T1–T4/H1–H6/KPI route and separates a deliberately misimplemented failure route from a requirements-conforming route; current design review finds no new universal gate or S/T/H family necessary; not yet W3-admitted or executed.
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
| Candidate signalling / false-context scenario 00G | [00G](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.3_DRAFT.md) | **Latest working draft v0.3** — DBC gate namespace / S1 route / KPI instrumentation added; v0.2 preserved; 00D/W3 execution pending |
| Candidate opportunity / authority scenario 00H | [00H](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.4_DRAFT.md) | **Latest working draft v0.4** — V19/V20 adaptive delegation, U/G/I controls and root-authority-lineage quality-plan correction added; W3 admission/execution pending |
| Candidate semantic-TOCTOU scenario 00I | [00I](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.2_DRAFT.md) | **Latest working draft v0.2** — “The Patch That Undid the Fix”; Q0–Q6 quality gates, positive continuity control, strong-peer arms, requirements-gap probe and external corroboration added; CAND-R4 remains review-only; W3 admission/execution pending |
| Candidate rights-provenance inversion scenario 00J | [00J](./baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) | **Working draft v0.1** — “The Author Pays for Their Own Work”; Q0–Q5 projects existing canonical requirements into bad-vs-conforming routes with positive/negative controls; no new universal gate or S/T/H family identified; execution pending |
| Implementation profiles | [00E-A01](./baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00E-A02](./baseline/00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00F-A01](./baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00F-A02](./baseline/00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00G-A01 OpenAI](./baseline/00G_A01_OPENAI_AGENTS_STACK_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) · [00H-A01 Claude](./baseline/00H_A01_CLAUDE_AGENT_SDK_IMPLEMENTATION_PROFILE_v0.3_DRAFT.md) · [00H-A02 Stripe](./baseline/00H_A02_STRIPE_RADAR_IMPLEMENTATION_PROFILE_v0.3_DRAFT.md) | **Draft implementation trajectories; source basis reviewed 24 Sep 2026** — 00H Claude/Stripe v0.3 successors now include the V19/V20 authority-laundering U/G/I stress; no measured vendor benchmark results |
| Reference-oracle / test construction | [00D-A01](./baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) | **Designed** |
| Deterministic Stage-0 harness | [00D-A03](./baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md) | **Designed** |
| Pre-registration | [RS-00E-Q1a fixture](./baseline/fixtures/RS-00E-Q1a/README.md) | **Published** |
| Stage-0 descriptive execution trace | — | **Pending** |
| Comparative execution B0–B3 | — | **Pending** |
| Independent validation / replication | — | **Pending** |

**Evidence boundary:** the current 00D matched-comparator programme directly covers the EA differential represented by EA-H1–EA-H4. Later positioning layers — including the Gradient Law, MSCA Operation / Repositioning, Agentic Citizenship and choreography/signalling extensions — have their own architectural, falsification or conformance conditions but are **not thereby claimed to have completed matched comparator execution in 00D**.

The benchmark is therefore presentable as an inspectable test programme and market/architecture gap analysis. It is not yet evidence of comparative superiority.

## Applied validation route — Decision Boundary Challenge

The [**Decision Boundary Challenge — Applied Agentic Validation Protocol v0.2**](./DECISION_BOUNDARY_CHALLENGE_v0.2.md) is a separate applied-evidence route for reviewing what happens when an agent reaches the boundary between capability, sufficient evidence, admissibility, authority, opportunity and actuation.

It is designed to be **cross-platform and sector-agnostic**: the initial unit under review is an agent stack, framework, control plane or research platform rather than a logistics, energy or other vertical application. The protocol begins with a standard challenge pack and offline trace audit; sandbox/sidecar execution is admitted only after a material signal exists and the comparison is preregistered.

The protocol:

- preserves producer-native semantics rather than translating external verdicts into EA/DBC states;
- keeps Type 0/1/2, P1/P2/P3, Decision Boundary dispositions and AuthorityResponse as separate semantic layers;
- explicitly namespaces the different meanings of ESCALATE;
- includes challenge families for semantic TOCTOU, handoff qualifier loss, hidden common dependencies, attractive inadmissible opportunities, effective-role drift, Type 0/1/2, slow authority response and legitimate re-contracting;
- defines integrity, value-preservation, continuity, burden and accountability measures;
- compares configurations through hard admission gates plus an outcome–burden–accountability/Pareto review rather than a single unvalidated score;
- treats Control Preservation Efficiency only as a research placeholder until the underlying variables are shown to be robust and non-redundant.

**DBC-C02 narrative scenario:** [00I — Semantic TOCTOU / “The Patch That Undid the Fix”](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.2_DRAFT.md) gives stale decision-basis applicability a bounded database-remediation case and Q0–Q6 quality-gate plan. It distinguishes controls already required by the frozen Requirements from the CAND-R4 check-to-act binding clarification candidate. It remains a candidate scenario, not an executed result.

**DBC-C05 narrative scenario:** [00H — Batch Opportunity Beyond Authority](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.4_DRAFT.md) gives the attractive-inadmissible-opportunity branch a bounded synthetic case and Q0–Q5 quality-gate plan. It remains a candidate scenario, not an executed result.

**FG-TIDA projection:** the programme-independent protocol is projected into the [FG-TIDA Decision Boundary Evaluation Profile v0.1 Draft](./fg-tida/tests/FG_TIDA_DECISION_BOUNDARY_EVALUATION_PROFILE_v0.1_DRAFT.md) and is bidirectionally mapped into [Specification Preparation v0.3](./fg-tida/specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md). The current public test route starts with UC-6 semantic mapping and may then enter Nelson's bounded UC-4 executable profile after contributor review and scope agreement.

**Boundary:** this is not part of the frozen/canonical EA baseline, does not supersede the 00D benchmark, and currently contains no executed comparative result or vendor ranking. It runs in parallel with W2 and may later contribute admitted fixtures/evidence through the normal W3 or external-owner process. [v0.1](./DECISION_BOUNDARY_CHALLENGE_v0.1.md) remains preserved as the predecessor.

## Reading routes

- **Five minutes:** this page → [100 Million Tokens](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) → [mobility divergence](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) → [benchmark status](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md).
- **Architecture:** [canonical EA corpus](./baseline/README.md) → topology → documents 01–04 → 01H/01I/01J → interface annexes.
- **Validation:** benchmark → A01/A03 → validation profiles → fixture/pre-registration → future execution traces.
- **Institutional application:** [**current Theme #13 charter-preparation draft (01G)**](./fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md) for the direct working document; use the broader [EA / FG-TIDA package](./fg-tida/README.md) for specifications/interfaces → cases/tests → provenance.

## Routing rule

This page should remain a router while the programme structure is still being consolidated. New substantive documents, cases, interface annexes, validation material and historical records should be indexed in the appropriate destination README rather than duplicated or removed here. The canonical corpus is preserved as-is; this page only exposes stable entry routes.

**Status:** public working research and test proposals; not adopted standards, completed pilots or certified comparative results.
