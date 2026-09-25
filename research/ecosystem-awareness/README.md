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

## Requirements necessity / principle ablation

The current follow-on to the S1–S14 requirements result is the [**00K — Six-Principle Sufficiency & Adversarial Ablation Test v0.1 Draft**](./baseline/00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md). The six principles are the object under test; S1–S14 are the observable specification/measurement layer. Each ablation removes one principle, gives the other five the strongest fair opportunity to redesign the route, and asks whether they can pass the frozen negative and positive controls without reconstructing the removed semantic invariant. [A01](./baseline/00K_A01_REVIEWED_PRE_PRINCIPLE_FIRST_DESIGN_ADDENDUM_v0.1.md) preserves the previously reviewed design verbatim, [A02](./baseline/00K_A02_REQUIREMENTS_COVERAGE_MATRIX_ADDENDUM_v0.1.md) isolates the verified S1–S14 × 00E–00J coverage matrix, and [A03](./baseline/00K_A03_P4_00H_PAPER_ABLATION_EXECUTION_v0.1.md) records the first P4/00H paper execution. Its runnable companion [A4 harness](./baseline/fixtures/00K-A4-P4-00H/README.md) preserves the reviewed source, independently reproduces the reviewed v0.2 package at **21/21**, and passes **29/29** in the active composed harness after additive indistinguishability and bounded-grid strengthening. The P4 result remains deterministic/symbolic evidence, not a live product or vendor benchmark. The programme now also includes executable harnesses for [P1/00J](./baseline/fixtures/00K-A1-P1-00J/README.md), [P2/00E](./baseline/fixtures/00K-A2-P2-00E/README.md), [P3/00F](./baseline/fixtures/00K-A3-P3-00F/README.md), [P5/00I](./baseline/fixtures/00K-A5-P5-00I/README.md) and [P6/00G](./baseline/fixtures/00K-A6-P6-00G/README.md). The [six-principle execution summary](./baseline/00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md) plus [bounded-grid audit](./baseline/00K_A05_BOUNDED_GRID_HARDENING_AND_P5_AUDIT_v0.1.md) record **346 passing core symbolic tests** across P1–P6 after serious hardening of all six principles. The [P1 falsifier/isolation note](./baseline/00K_A07_P1_CONFOUND_FALSIFIER_AND_MATCHED_SEMANTIC_ISOLATION_v0.1.md) preserves an important negative result: the original A1 pair admits a source-authority TRUE SUBSTITUTE and is rejected as a P1 necessity isolation; the corrected matched-semantic fixture retains the bounded P1 result. The [P2 strongest-repair audit](./baseline/00K_A08_P2_STRONGEST_REPAIR_AND_PREFIX_INDISTINGUISHABILITY_v0.1.md) expands 00E with matched-prefix late-resolution branches and serious TTL/circuit-breaker/parallel/scheduler/probe alternatives. The [P3 falsifier/isolation note](./baseline/00K_A09_P3_CONFOUND_FALSIFIER_AND_MATCHED_CONFLICT_ISOLATION_v0.1.md) records that the original HOLD-marked base branch admitted a literal-HOLD shortcut and replaces it with a matched conflict isolation. The [P4 minimal-authority audit](./baseline/00K_A10_P4_MINIMAL_AUTHORITY_BASIS_AND_LINEAGE_REFINEMENT_v0.1.md) adds a substantive refinement: 00H does not require the relying component to possess full historical delegation lineage if a legitimate owner-side PDP/capability supplies a current scoped authority basis; the minimal non-amplifying authority-qualification invariant survives. The [P5 exhaustive material-basis audit](./baseline/00K_A11_P5_EXHAUSTIVE_MATERIAL_BASIS_ABLATION_v0.1.md) enumerates all 16 subsets of the declared four-field decision basis; only complete current-basis coverage survives every single-field mutation while preserving continuity. The [P6 transitive-dependency audit](./baseline/00K_A12_P6_TRANSITIVE_DEPENDENCY_AND_STRONGEST_REPAIR_AUDIT_v0.1.md) further hardens the corrected P6 fixture: distinct immediate source IDs are shown to be only a partial proxy when they share one upstream root. The [P6 falsifier/isolation note](./baseline/00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md) preserves the original authority-confound negative result: the unmodified 00G F/G pair admits an authority-only TRUE SUBSTITUTE and is therefore rejected as a P6 necessity isolation; corrected matched-authority 00G and independent 00F isolation retain the bounded P6 result. The [full campaign router](./baseline/fixtures/00K-SUITE/README.md) registers **379 symbolic tests** including supplemental falsification/isolation/cross-scenario checks. The [serious-ablation completion review](./baseline/00K_A13_SIX_PRINCIPLE_SERIOUS_ABLATION_COMPLETION_REVIEW_v0.1.md) consolidates the final symbolic dispositions for P1–P6. The [complete six-principle ablation testbook](./baseline/00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) is the compact reader route that places each narrative ablation, serious repair search, Python harness, result and falsifier side by side. The [formal relative-independence proof](./baseline/00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) gives the model-theoretic six-countermodel proof that no current Pi follows from the other five inside the declared 00K model class; [A17](./baseline/00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md) is the documentation/reproducibility map for the whole workstream. The [CI reproduction record](./baseline/00K_A14_GITHUB_ACTIONS_REPRODUCTION_379_v0.1.md) documents a clean GitHub Actions reproduction of the current campaign at **379/379** across all 10 jobs ([run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548)). This remains fixture-level symbolic evidence; live technology/runtime validation is still pending.

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

### Failure → success case-study extensibility

The six active scenarios **00E–00J are minimum concrete instantiations of structural case families, not claims limited to their memorable story details**. [**A25 — Failure Case-Study Extensibility & Requirements-Conformance Transfer**](./baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) applies the DAOS Annex-II discipline: **upward/vertical** extension increases scale or organizational depth, **downward** extension reduces the case to its smallest structural implementation, and **horizontal** extension changes domain while preserving the same kernel, decision boundary, requirement route and positive controls.

[**A26 — Failure → Success Model Case Conversion & Three-Axis Extensibility**](./baseline/00K_A26_FAILURE_TO_SUCCESS_MODEL_CASE_AND_EXTENSIBILITY_v0.1.md) adds the positive layer. Each failure family is paired with a minimum requirements-conforming traversal and a success predicate; the same up/down/horizontal admission discipline then determines where that positive case can be reused **without adding a new canonical requirement**.

| Family | Extensibility profile | Success Model Case |
|---|---|---|
| **00E** | [profile](./baseline/00E_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) | [Qualified Synthesis Under Finite Capacity](./baseline/00E_SUCCESS_MODEL_CASE_QUALIFIED_SYNTHESIS_v0.1.md) |
| **00F** | [profile](./baseline/00F_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) | [Coherent Shared-Capacity Requalification](./baseline/00F_SUCCESS_MODEL_CASE_SHARED_CAPACITY_REQUALIFICATION_v0.1.md) |
| **00G** | [profile](./baseline/00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) | [Source-Aware Frame Stability](./baseline/00G_SUCCESS_MODEL_CASE_SOURCE_AWARE_FRAME_STABILITY_v0.1.md) |
| **00H** | [profile](./baseline/00H_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) | [Preserve the Finding, Do Not Overreach](./baseline/00H_SUCCESS_MODEL_CASE_PRESERVE_WITHOUT_OVERREACH_v0.1.md) |
| **00I** | [profile](./baseline/00I_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) | [Action-Time Requalification](./baseline/00I_SUCCESS_MODEL_CASE_ACTION_TIME_REQUALIFICATION_v0.1.md) |
| **00J** | [profile](./baseline/00J_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) | [Proposition-Scoped Provenance](./baseline/00J_SUCCESS_MODEL_CASE_PROPOSITION_SCOPED_PROVENANCE_v0.1.md) |

**00G is the clearest horizontal/downward transfer example:** the robot/multi-agent story reduces to a single LLM or SLM when conversation-derived statements, memory summaries, RAG/vector-store entries or prior assistant outputs are recursively reused and their common provenance/dependence can be flattened. The extension is admitted only when that propagation affects the receiving task/frame/role; one-turn agreeableness alone is not the same case.

Family membership is structural, not analogical. For an admitted extension, A23 + A25/A26 gives the bounded transfer result: canonical conformance to the inherited S/T route prevents the **same family failure** and realizes the declared success predicate. If a proposed extension needs a decision-material obligation not expressible through the current A21 requirement grammar, it is Requirements-vNext evidence rather than a silent S15. Listed extensions remain design-level mappings unless separately frozen/executed.


### Benchmark status dashboard

The sentence above remains the compact status statement. The dashboard below exposes the same programme state by artefact so that design, publication and measured execution are not conflated.

| Stage | Artefact | Current status |
|---|---|---|
| Comparison contract — B0/B1/B2/B3 | [00D — Canonical Architecture Benchmark & Evidence v0.2](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | **Defined** |
| EA-H1–EA-H4 hypotheses and decisive falsifiers | [00D — Canonical Architecture Benchmark & Evidence v0.2](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | **Defined** |
| Reference scenario 00E | [00E](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) | **Documented** |
| Reference scenario 00F | [00F technical v0.2](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) · [Freeze Edition](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) | **Current working successor v0.2** — “The City That Stopped Safely”; complete Q0–Q5 / N0-N1-Q / V0–V9 / R0-R1-R2 design; FIWARE/AWS profiles; source audit + zero-loss Freeze Edition; comparative execution pending |
| Canonical signalling / false-context scenario 00G | [00G](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) | **Canonical working v0.4** — integrated scenario, Q0–Q5 quality plan, KPI contract and OpenAI OAI-G0/G1/G2 trajectories; historical drafts preserved as lineage; 00D/W3 execution pending |
| Candidate opportunity / authority scenario 00H | [00H](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) | **Latest working draft v0.5** — primary no-attacker "Quiet Four Thousand" with paired execution-vs-preservation silent failures; outsourced-Dispatcher V19/V20 adversarial hardening; EA0 gate audit; W3 admission/execution pending |
| Candidate semantic-TOCTOU scenario 00I | [00I technical v0.5](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md) · [Freeze Edition](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) | **Latest working draft v0.5** — “The Patch That Undid the Fix”; OOTB/top-notch/frozen-top-notch-under-drift + V11 adaptive basis-model drift; audited AWS v0.2 profile, implementation skeletons and zero-loss Freeze Edition published; CAND-R4 remains review-only; W3 admission/execution pending |
| Candidate rights-provenance inversion scenario 00J | [00J](./baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) | **Working draft v0.1** — “The Author Pays for Their Own Work”; Q0–Q5 projects existing canonical requirements into bad-vs-conforming routes with positive/negative controls; no new universal gate or S/T/H family identified; execution pending |
| Implementation profiles | [00E-A01](./baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00E-A02](./baseline/00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00F-A01](./baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00F-A02](./baseline/00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00H-A01 Claude](./baseline/00H_A01_CLAUDE_AGENT_SDK_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) · [00H-A02 Stripe](./baseline/00H_A02_STRIPE_RADAR_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) · [00I-A01 AWS Step Functions/RDS](./baseline/00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [00J-A01 Panodyssey/TEMS](./baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) | **Draft implementation trajectories; source basis reviewed 24 Sep 2026** — 00I-A01 adds the audited ordinary/top-notch/frozen-under-drift AWS trajectory plus inspectable skeletons; 00J-A01 adds the rights-portability/regime-change trajectory; no measured vendor benchmark results |
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

**DBC-C02 narrative scenario:** [00I — Semantic TOCTOU / “The Patch That Undid the Fix”](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md) gives stale decision-basis applicability a bounded database-remediation case and Q0–Q6 quality-gate plan, now including a frozen strong-peer regime-drift branch. It distinguishes controls already required by the frozen Requirements from the CAND-R4 check-to-act binding clarification candidate. It remains a candidate scenario, not an executed result.

**DBC-C05 narrative scenario:** [00H — Batch Opportunity Beyond Authority](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) gives the attractive-inadmissible-opportunity branch a bounded synthetic case and Q0–Q5 quality-gate plan. It remains a candidate scenario, not an executed result.

**FG-TIDA projection:** the programme-independent protocol is projected into the [FG-TIDA Decision Boundary Evaluation Profile v0.1 Draft](./fg-tida/tests/FG_TIDA_DECISION_BOUNDARY_EVALUATION_PROFILE_v0.1_DRAFT.md) and is bidirectionally mapped into [Specification Preparation v0.3](./fg-tida/specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md). The current public test route starts with UC-6 semantic mapping and may then enter Nelson's bounded UC-4 executable profile after contributor review and scope agreement.

**Boundary:** this is not part of the frozen/canonical EA baseline, does not supersede the 00D benchmark, and currently contains no executed comparative result or vendor ranking. It runs in parallel with W2 and may later contribute admitted fixtures/evidence through the normal W3 or external-owner process. [v0.1](./DECISION_BOUNDARY_CHALLENGE_v0.1.md) remains preserved as the predecessor.

## Reading routes

- **Five minutes:** this page → [100 Million Tokens](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) → [Mobility Chaos — The City That Stopped Safely](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) → [00I Freeze Edition — The Patch That Undid the Fix](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) → [benchmark status](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md).
- **Architecture:** [canonical EA corpus](./baseline/README.md) → topology → documents 01–04 → 01H/01I/01J → interface annexes.
- **Validation:** benchmark → A01/A03 → validation profiles → fixture/pre-registration → future execution traces.
- **Institutional application:** [**current Theme #13 charter-preparation draft (01G)**](./fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md) for the direct working document; use the broader [EA / FG-TIDA package](./fg-tida/README.md) for specifications/interfaces → cases/tests → provenance.

## Routing rule

This page should remain a router while the programme structure is still being consolidated. New substantive documents, cases, interface annexes, validation material and historical records should be indexed in the appropriate destination README rather than duplicated or removed here. The canonical corpus is preserved as-is; this page only exposes stable entry routes.

**Status:** public working research and test proposals; not adopted standards, completed pilots or certified comparative results.
