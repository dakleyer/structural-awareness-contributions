# Annex 00D-A01 — Reference-Scenario Test Artifacts and Bounded Reference-Oracle Construction & Test Design — Ecosystem Awareness

| | |
|---|---|
| **ID** | 00D-A01 |
| **Type** | Reference-scenario fixture, bounded-oracle construction and test-design annex |
| **Status** | Additive annex · evidence design · not an executed test or validation result |
| **Version · date** | v0.1 · current filename since 2026-09-21 |
| **Owner corpus** | Ecosystem Awareness benchmark route |
| **Supersedes / superseded by** | Renamed successor to the historical “Proof Sketch” filename; historical alias preserved |

> **Additive working evidence-design annex.** This annex turns selected branches of the 00E and 00F Reference Failure Scenarios into a traceable future fixture and testbed programme. It does not modify the canonical requirements, the benchmark, the scenarios, the frozen validation profiles or Appendix A of 04. It does not report an executed test, a completed comparison, an independently validated oracle or an EA result.

**Version:** 0.1 — 19 September 2026

**Status:** public working annex to [00D — Canonical Architecture Benchmark and Reference-Scenario Evidence](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md). It is deliberately incomplete evidence design, not evidence.
**Dependencies:** [00 — Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), [00 — Canonical Architecture Topology](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md), [00D](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md), [00E](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md), [00F](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md), [01C — EA / Regime Awareness](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) and [04 Appendix A — Interface Quality and Conformance Plan](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part03.md#appendix-a--interface-quality-and-conformance-plan-for-ecosystem-awareness).

## 1. Purpose, reading rule and claim boundary

The canonical route remains:

`reference scenario → Quality-Gate Plan → S# → T# → H# → KPI → evidence/disposition`.

This annex does not replace that route with a test-first route. It supplies a small, conventional software-engineering representation of it where a repeatable run is useful:

`requirement route → fixture admission → frozen scenario branch → configuration under test → bounded reference oracle → gate policy → result`.

No fixture is admitted merely because it tells a persuasive scenario. Before facts are instantiated, it must cite the applicable `σ(d,t)`, S#, T#, H#, KPI and a result that would count against the candidate. The scenario supplies the frozen facts only after that admission.

### 1.1 What this annex does and does not verify

| Activity | What it can establish | What it cannot establish by itself |
| --- | --- | --- |
| **Stage 0 verification** | A deterministic harness can execute the declared frozen branch and distinguish a stated configuration under test from its controls. | That the stipulated branch is true in the world, that a real producer is interoperable, or that EA is superior. |
| **Stage 1 verification** | A versioned implementation can be compared with B0–B3 using observable producer/receiver data and independent-boundary evidence where claimed. | That the requirement is the right societal or operational need. |
| **Validation** | Requires a party independent of the requirement author to corroborate relevance, need and outcome in a real decision context. | It is not completed by Stage 0 or Stage 1 alone. |

`S#` are asserted challenge surfaces to be corroborated; they are not external binding requirements. `T#` are target sufficiently-good properties and can act as acceptance conditions only for their declared scope. `H#` are falsifiable research hypotheses and never acceptance criteria. KPIs are evidence, not truth.

### 1.2 Relation to Appendix A of 04

Appendix A remains the sole generic discipline for an interface unit under test: the Interface Conformance Record (ICR), its owners and reviewer, its positive/boundary/rejection/adversarial fixtures, observable-oracle entry condition and conformance findings are not redefined here.

This annex adds only the **scenario unit under test**: frozen facts, `σ(d,t)`, configuration B0–B3, reference state, residual, outcome disposition and scenario-level falsification. An interface fixture inside a scenario run must cite the relevant ICR under Appendix A. A scenario fixture is not a substitute for an ICR, and an ICR is not a substitute for scenario-level evidence.

## 2. Bounded deterministic reference oracle and qualified regime-change dependency

### 2.1 Three distinct roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| **Qualified regime-change / early-warning dependency (GEEW)** | Supplies a scoped, fresh, provenance-qualified indication that an observable regime may remain compatible with, or depart from, its stated baseline. | It does not forecast the future, reconstruct the whole ecosystem, establish the hidden cause, set EA posture or authorize action. Its representation, context, threshold and delay limits remain visible. |
| **EA candidate** | Uses available signals and other qualified evidence to preserve scope/residual/dependency, requalify the affected decision frame and request an owner-preserving bounded response. | It does not become the detector, oracle, authority, precedence owner or actuator. |
| **Bounded deterministic reference oracle `O_ref`** | For a fixture, evaluates a frozen or observed reference state inside a declared represented universe `U_ref` and returns expected facts/outcomes for the stated test question. | It has no runtime role and no claim over the open ecosystem `Ω`. It must report what remains outside `U_ref`. |

The relation is therefore:

`GEEW(W,d,t) → qualified change evidence and limits → EA candidate → configuration result; O_ref(U_ref) → post-run reference assessment only`.

The GEEW dependency can be deliberately lighter than the T1/T4 conditions applied to the EA candidate. It need only be qualified for the injected change family, observation map, threshold, freshness and response horizon stated by a fixture. A qualified GEEW signal is an input to EA’s T1/T4 test; it is not proof that T1 or T4 holds, and a neutral signal is not evidence that the wider EA frame remains valid.

### 2.2 Determinism, stipulation and residual

`O_ref` is a conventional, implementable deterministic procedure. It may use the same overall compute budget as the compared configurations while using a different, declared information architecture: for example, a frozen source graph, uncompressed upstream state or a whole declared dependency relation. That reference access is an evaluator privilege, not a deployable advantage attributed to EA.

In Stage 0, the oracle is **stipulative**: the fixture author freezes the reference facts and deterministic expected outcome inside `U_ref`. This demonstrates that the harness can test a stated distinction; it does not demonstrate world truth. In a later run, an **observational** oracle may use independently collected traces or effects. It remains bounded by its data, scope, freshness and measurement method.

The fixture records an explicit residual `R_ref`: facts or distinctions not decided by `O_ref` inside the declared test question. Some fixtures may have no material residual for their narrow, deterministic question. Others may retain a possible residual because the declared frame cannot determine it. No assertion is made here that every residual is formally undecidable, or that a non-conventional computational component is required. The operational rule is simpler: a residual that the declared oracle cannot decide remains explicit and cannot be promoted to PASS.

### 2.3 Controlled circularity

The design does not claim to remove every dependency recursively. It controls it by declaring three independent limits:

1. the GEEW detector’s observable boundary and known performance for the injected change family;
2. the deterministic oracle’s `U_ref`, source access, representation and residual; and
3. the EA candidate’s own decision scope, authority, capacity and response horizon.

This prevents a circular claim of the form “EA is correct because EA says the frame is correct.” A fixture asks instead whether a candidate preserves and reacts to a reference condition that is deterministically decidable **within the declared test boundary**. Where it is not decidable there, the expected result is qualified indeterminacy or bounded requalification, not invented certainty.

## 3. Scenario fixture record

A **Reference Failure Scenario** remains the complete 00E or 00F story and Quality-Gate Plan. A **scenario fixture** is one frozen, runnable branch of that story. `Route N` and `Route Q` remain useful scenario narratives; they are not fixture fields. The fixture compares a named configuration under test, normally B0–B3 of 00D, against pre-registered controls.

Every future scenario-fixture record contains at least:

| Field | Required declaration |
| --- | --- |
| Identity and traceability | Fixture ID/version; scenario and branch; `σ(d,t)`; applicable S#/T#/H#/KPI; and a public source-anchor set: exact document path, document version and Git commit for the requirements, benchmark and any linked 04 ICR reference. |
| Frozen facts | Event order, source graph, correlation/dependency, authority, commitment state, action library, normal envelope and injected material perturbation; named fact-freezing authority and whether facts are self-declared. |
| Source-access assumption | Whether the runtime and later agents may re-query the primary source; if yes, the time/cost; if no, the loss is explicitly informational. |
| Scarce resource | The binding resource for the branch: decision time, human attention, regulatory window, communication, compute, budget or physical capacity. “Tokens” are not presumed to be the scarce resource. |
| Validity of facts | Freeze date/version, validity horizon and material change that invalidates the fixture. |
| Pre-registration record | Versioned public record, frozen and committed to this repository before the first execution, of the expected result, comparator configuration, KPI/threshold and burden tolerances, run/repetition rule, stop rule and permitted deviations. It declares its exact repository path and Git commit; every result trace cites that commit. A local or unpublished record is **pre-registration declared**, not publicly verifiable pre-registration. Later deviations remain visible and justified. |
| Configuration under test and comparator | Exact B0/B1/B2/B3 version/configuration, permitted source access, common resource ledger and any legitimate control already supplied by the peer; named configuration owner and named comparator defender who may improve the comparator only inside the pre-registered envelope. |
| Oracle contract | `U_ref`, deterministic procedure or observational source, known/reference facts, `R_ref`, expected observable result and runtime-access prohibition. |
| Gate policy and tolerance | KPI thresholds, permitted dispositions, authority/expiry, threshold-sensitivity range and pre-registered error/burden tolerance for “equal or lower burden.” Any local burden or null-action cost is measured in the declared scarce-resource unit. These are policy, not oracle truth. |
| Evidence status and stability | Planned / Stage-0 stipulative verification / Stage-1 observational comparison / Stage-2 external validation; and, for every non-deterministic configuration, pre-registered run count, seed/control rule and outcome-distribution comparison. |
| Falsification and controls | Candidate failure condition; comparator result that defeats the claimed differential; negative control; null/valid-continuity fixture where applicable; and harness self-test result. |
| Ownership and review | Semantic owner; adapter/maintenance owner for each ICR; named reviewer distinct from that adapter owner; authority that freezes scenario facts; their relationships and unresolved objections. |

Changing any frozen source, material qualifier, branch condition, resource, source-access assumption, oracle boundary or threshold creates a new fixture version. Reducing the material set is recorded as a finding, not silently treated as a stronger result.

Before the first run, the semantic owner, comparator defender and reviewer freeze and publicly commit the pre-registration record. A B1/B2 result can falsify an EA differential only where the compared configuration has a named defender and the frozen common resource/access conditions are reviewable. If that person is unavailable, the record is labelled **comparator self-configured**. It may support bounded configuration verification, but not an EA differential claim. If the authority freezing the facts is also the candidate designer, the record is additionally labelled **facts self-declared**. An unresolved comparator-defender objection remains visible and blocks a differential conclusion, not the descriptive run.

Where a candidate failure condition relies on a negative, null or control branch, that branch and the primary branch form one **fixture family**: one pre-registration record, one pre-execution public commit and one completed evaluation unit. The control must execute under that record before the primary result is reported as interpretable. A primary-only run is incomplete, not a positive result.

## 4. Core traceability matrix

The matrix is the core of this annex. “Planned” means evidence design exists; it does not mean a fixture or testbed has been implemented. It currently covers 00E Q1, Q2, Q4 and two 00F composition branches; it does not yet cover every gate of either scenario. The wider S1–S14 portfolio and its uncovered routes remain in the [Use-Case Portfolio Requirements Coverage Map](./USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md).

`Evidence status` is not the E1–E4 taxonomy of 00D, which classifies external sources. It records what the fixture itself can support. “Stage 0” means stipulative verification only.

The challenge route in each row is read through **00 §6.1**; KPI names and calculations are read through **00 §5**. A measure absent from that canonical KPI protocol is labelled fixture-local rather than silently promoted to a canonical KPI; its pre-registration declares numerator, denominator, reference branch and threshold.

| Fixture ID / branch | Requirement route and KPI set | Required state or field | 04 relation | Oracle class | Candidate failure condition | Differential falsifier | Evidence status | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **RS-00E-Q1a** — common dependency | S5/S9/S14 → T1/T2/T4 → H2/H3/H4; correlated-evidence error rate, residual-scope preservation, false-convergence rate. | Shared upstream source, independence status, affected scope, explicit residual and re-entry target. | ICR where dependency status crosses an interface; otherwise N/A. | Stage-0 deterministic stipulative `O_ref`: dependency is known inside `U_ref`. | B3 treats A/B as independent corroboration or loses the dependency/residual. | Pre-registered B1/B2 preserves dependency and prevents false corroboration within tolerance. | Planned Stage 0. | Planned atomic fixture. |
| **RS-00E-Q1b** — omitted uncertainty | S3/S5/S10/S14 → T1/T2/T4 → H1/H2/H5/H6; qualification-loss rate, false-continuation rate, deadline-pass rate, total decision burden. | Omitted qualifier, materiality, affected basis, `UNKNOWN`, expiry and bounded posture. | ICR boundary/rejection fixture if qualifier is dropped in handoff. | Stage-0 deterministic stipulative oracle. | B3 closes or continues without the material qualifier. | Pre-registered strong peer preserves the qualifier or reaches equal/better error, deadline and burden results within tolerance. | Planned Stage 0. | Planned atomic fixture. |
| **RS-00E-Q1c-R** — compression, re-query permitted | S2/S5/S9/S12/S14 → T2/T4 → H2/H3/H4/H6; primary-source retrievability, compression exposure, decision-relevant evidence yield, total decision burden. | Compression point, primary-source retrievability, declared re-query cost, deadline and scarce resource. | ICR composition-critical mapping if the compression is a handoff. | Deterministic stipulative oracle; `U_ref` retains the declared primary state. | B3 cannot preserve/recover the material basis within the declared budget. | A compressed peer recovers it within the common budget, or no pre-registered error/burden difference appears. | Planned Stage 0. | Planned atomic fixture, paired with Q1c-NR. |
| **RS-00E-Q1c-NR** — compression, re-query prohibited | Same route and measures as Q1c-R. | Same frozen branch and budget except primary-source re-query is unavailable; information loss remains explicit. | Same as Q1c-R. | Same deterministic stipulative oracle. | B3 treats unavailable primary state as recovered or silently closes. | A pre-registered strong peer preserves the declared information loss and reaches the same qualified posture without primary-source re-query inside the common budget. | Planned Stage 0. | Planned atomic fixture, paired with Q1c-R; the pair's no-difference outcome remains a legitimate negative result. |
| **RS-00E-Q1d** — combined mechanism | Same routes and measures as Q1a–Q1c. | Combined dependency, omitted qualifier and compression. | Applicable linked ICRs. | Deterministic stipulative oracle. | B3 fails any required atomic preservation. | Interpretable only if Q1a–Q1c behave as pre-registered; otherwise it reports interaction, not confirmation. | Planned Stage 0. | Planned after atomics. |
| **RS-00E-Q1e** — degraded GEEW input | S3/S5/S14 → T1/T2/T4 → H1/H5/H6; material-break precision, false-continuation rate, false containment, requalification latency. | Late, threshold-miscalibrated or unqualified regime signal; its representation/context/freshness limitation and affected decision frame. | ICR where the GEEW signal crosses an interface; otherwise N/A. | Deterministic stipulative oracle knows the injected signal limitation; a qualified-signal branch is the control. | B3 inherits detector confidence, continues without qualification or adds false containment in the qualified-signal control. | A strong peer closes the stated gap within tolerance. | Planned Stage 0. | Planned fixture family; qualified-signal control executes with the primary branch. |
| **RS-00E-Q2** — human approval under saturation | S4/S5/S14 → T2/T3/T4 → H1/H4/H6; human-capacity binding/escalation demand, Type-1→Type-2 forced-closure rate, remaining response margin, deadline-pass rate. | Reviewer demand/capacity, binding deadline, current evidence, approval status, bounded fallback and explicit `UNKNOWN`. | Relevant ICR where the reviewer/approval handoff crosses an interface; otherwise N/A. | Deterministic stipulative capacity schedule; expected result distinguishes approval from new evidence. | B3 treats approval as new determination or leaves unbounded HOLD. | Pre-registered peer preserves the limitation and applies an authorized bounded fallback within tolerance; Q2-N0 supplies sufficient-capacity control. | Planned Stage 0. | Planned fixture family; Q2-N0 executes with the saturated branch. |
| **RS-00E-Q4** — bounded requalification | S3/S4/S5/S10/S14 → T1/T2/T3/T4 → H1/H5/H6; false-continuation rate, false containment, deadline-pass rate, remaining response margin, decision-relevant evidence yield, total decision burden and marginal decision value. | Material residual after declared additional search, binding deadline, authority, scarce-resource ledger, permitted bounded experiment and `NO COMMITMENT` posture. | ICR where residual/requalification status crosses an interface; otherwise N/A. | Deterministic stipulative `O_ref` declares whether the residual is reducible inside the horizon. | B3 searches without bound, silently closes, or remains contained when the negative-control residual is reducible. | A pre-registered strong peer reaches an equally qualified outcome within common tolerance, or B3 incurs avoidable false containment, deadline loss or burden. | Planned Stage 0. | Planned fixture family; reducible-residual control executes with the primary branch. |
| **RS-00E-N0** — valid continuity / null | S3/S5/S14 → T1/T2/T4 → H1/H5/H6; material-break precision, false containment, false-positive response cost, total decision burden. | No material break, normal basis still valid, expected continuation and false-positive cost. | ICR positive fixture when an interface route applies. | Deterministic stipulative oracle. | B3 detects/requalifies without a material break. | B3 exceeds the pre-registered false-containment/burden tolerance against B1. | Planned Stage 0. | Planned negative/null control. |
| **RS-00F-C1** — competing corridor postures | S1/S3/S5/S9/S11/S14 → T1/T2/T3/T4 → H1/H2/H3/H4/H5/H6; incompatible-posture exposure, **fixture-local conflict precision**, deadline-pass rate. | Shared resource-time segment, scope, source dependency, A/B/NORMAL/HOLD, authority/expiry and residual. | Composition-Critical ICR for each exercised interface handoff. | Deterministic stipulative oracle identifies conflict; it does not decide precedence. | B3 hides conflict, arbitrates without authority or misses deadline. | Pre-registered B1/B2 exposes conflict and preserves a qualified partial result within tolerance. | Planned Stage 0. | Planned primary mobility fixture. |
| **RS-00F-C2** — precedence absent | S1/S9/S13/S14 → T2/T3/T4 → H2/H4; authority-field completeness, handoff integrity, observable outcome effect. | Competing directives, source-owned precedence reference absent, authority/intervention history and escalation receiver. | Composition-Critical ICR where directives cross interfaces. | Deterministic stipulative oracle. | B3 resolves precedence or hides the absent owner. | A configuration exposes conflict and the named/absent precedence owner with equal/lower burden. | Planned Stage 0. | Planned boundary fixture. |
| **RS-00F-N0** — no material shared conflict | S3/S5/S9/S14 → T1/T2/T4 → H1/H5/H6; false containment, false-positive response cost, total decision burden and deadline-pass rate. | Compatible postures or separated resource-time use; expected no unnecessary hold. | ICR positive fixture where applicable. | Deterministic stipulative oracle. | B3 raises material conflict/containment without the injected break. | B3 is less viable than the pre-registered B1 tolerance. | Planned Stage 0. | Planned negative/null control. |

This annex does not claim a scenario fixture for every S#. In particular, S7/S8 require the separate requirements-first workbook identified in the coverage map. A scenario-level test can preserve externally owned identity or delegation qualifiers, but cannot establish their underlying truth unless the appropriate producer and independent boundary are included.

The simultaneous-reversal cascade mechanism of 00E §4.2—dependent signals reversing together through a common dependency—does **not** yet have its own fixture. Q1d is a combined preservation branch and RS-00E-N0 is a false-positive/null control; neither is credited as Stage-0 coverage of that cascade mechanism.

## 5. Oracle output, gate policy and falsification

The oracle answers the fixture’s declared reference question. A gate policy decides what the organisation treats as a passing, requalification, containment, escalation or no-commitment result. They are deliberately separate.

| Object | Contains | Must not contain |
| --- | --- | --- |
| **`O_ref` output** | Reference facts within `U_ref`; expected permitted state or observable effect; explicit `R_ref`; reason/trace for the result. | KPI thresholds, release disposition, policy authority or a claim about all of `Ω`. |
| **Gate policy** | KPI thresholds, expected disposition, authority, expiry, stop rule and threshold-sensitivity range. | Hidden “truth” about the scenario. |
| **KPI evidence** | Measured outcome, numerator/denominator, burden and dispersion where relevant. | A replacement for the oracle or authority. |

Each fixture declares which small movement of a threshold changes the disposition. If the result is stable only at one exact threshold, the fixture reports that brittleness rather than treating it as a pass.

“Equal or lower burden” has no meaning without a pre-registered tolerance. The gate policy therefore fixes the permitted error and burden difference before execution. A comparator result supports an EA differential only if its B0–B3 configuration has the ownership/review status required in §3; a **comparator self-configured** result remains a bounded configuration finding, not differential evidence.

`O_ref` may be deterministic while a B1/B2/B3 implementation is not. Every non-deterministic configuration is run the pre-registered number of times under the stated seed/control rule. The comparison reports outcome distributions, material qualifier dispersion and burden dispersion; a single run is not comparative evidence in either direction.

The Q4 **cost of action or inaction relative to `O_ref`** is a local fixture measure, not a new canonical KPI. It selects the applicable existing measures from 00 §5: false containment or false-positive response cost, deadline pass, remaining response margin, total decision burden, decision-relevant evidence yield and marginal decision value. The record declares its numerator, denominator and the scarce-resource unit—such as decision time, reviewer attention or a regulatory window. Results are not aggregated across fixtures unless that unit and conversion rule are the same and pre-registered.

Falsification is mandatory. Examples include:

- B1/B2 preserves the material qualifier, discovers the common dependency or exposes the corridor conflict with equal/lower burden;
- the compressed route recovers the primary source within the declared budget;
- a separate pre-registered null branch contains no cascade-triggering loss and B3 nevertheless reports one; or, in Stage 1 or later, the observed change does not produce the claimed cascade;
- B3 produces more false containment, delay, oscillation or unauthorized action than the strong peer; or
- a negative control detects a break that is not present.

The last condition is especially important: a test harness that detects every branch demonstrates only that it is noisy, not that EA distinguishes a material break.

## 6. Deterministic fixture construction and oracle rationale

The test-design rationale is not a claim that all fixtures have been built. It shows the minimum shape of an implementable deterministic test before investment in a full testbed.

### 6.1 RS-00E-Q1a — shared dependency

**Question.** Does the configuration treat two reports from one hidden upstream source as independent corroboration?

- `U_ref` contains source `P`, derived reports `A` and `B`, their declared timestamps and a decision requiring independent support.
- The runtime receives only `A` and `B` plus the access allowed to its B0–B3 configuration. `O_ref` retains the declared `P → {A,B}` relation for post-run evaluation.
- The scarce resource is the response horizon; source re-query is either forbidden or charged explicitly.
- The expected result is not necessarily HOLD. It is that an independent-support claim is not issued without a second qualified route; the candidate preserves dependency and selects a bounded owner-preserving posture.
- **Negative control:** provide genuinely independent `A` and `B`; a correct candidate must not manufacture a dependency warning.
- **Falsifier:** B1 preserves the relation or reaches the same qualified posture with equal/lower burden; B3 yields an unsupported closure, an indefinite hold or greater burden without compensating benefit.

### 6.2 RS-00F-C2 — competing directives without a precedence owner

**Question.** Does the configuration expose incompatible directives over one resource-time segment without silently inventing authority?

- `U_ref` contains the Central Bridge corridor-time segment, valid A and B directives, their source owners, the absence of a declared precedence owner and the authoritative scope/expiry facts.
- The runtime receives only those representations permitted to the configuration. `O_ref` evaluates whether the conflict and absent precedence reference were preservable inside the fixture.
- The expected EA result is an explicit conflict, residual/affected scope and a request or escalation to the legitimate precedence owner. EA must not choose Plan A or Plan B.
- **Negative control:** A/B use separated corridor-time segments; a correct candidate must not manufacture a composition conflict.
- **Falsifier:** B1/B2 reaches the same owner-preserving result with equal/lower burden; B3 hides the conflict, makes a universal precedence decision or leaves an unbounded HOLD.

## 7. Testbed progression and independence

| Stage | Minimum implementation | Permitted conclusion | Explicit incompleteness |
| --- | --- | --- | --- |
| **Stage 0 — deterministic harness** | Simulated producers, frozen facts, deterministic `O_ref`, publicly commit-anchored pre-registered B0–B3 definitions and comparator defender, event playback, logs, null and negative controls, and a passed qualifier-loss instrumentation self-test. | The harness can distinguish declared fixture outcomes and test a configuration against stipulated semantics. | It demonstrates the harness and a bounded behaviour test, not production architecture effectiveness, independent interoperability or validation. |
| **Stage 1 — observable comparative run** | Versioned real or independently operated producer/receiver where claimed; shared resource ledger; retained traces; reviewer and ICR evidence; repeated runs for non-deterministic configurations. | Comparative verification within the declared environment. A Level-2 interface claim follows Appendix A’s independent-operation rule. | It is still not validation of broader relevance/need unless the requirement and outcome are independently corroborated. |
| **Stage 2 — external validation** | Identified decision owner and candidate real context in which the stated decision matters; a party independent of the requirement author evaluates relevance, practical outcome and trade-off. | Evidence that the test question matters and is useful in that context. | It does not automatically generalise beyond the stated domain. |

Stage 0 requires the same owner/review discipline as Appendix A: semantic owner, adapter/maintenance owner, reviewer distinct from the adapter owner, and a named authority who freezes the scenario facts. It additionally requires the comparator defender and the pre-registration record in §3 before a differential is claimed. “Internal” is recorded as internal; it does not waive the reviewer rule. Stage 1 requires independent producer/consumer evidence for any claim of independent interoperability.

The programme stops before Stage 1 if any of the following occurs:

1. a negative control systematically detects a material break that is not present;
2. no fixture can obtain an observable oracle without inventing a producer, receiver or fact that the proposed test needs; or
3. a B0–B3 route cannot meet the declared horizon or scarce-resource limit even in the deterministic harness. This is recorded as **modelled burden — provisional**; it stops the current Stage-0 route but cannot permanently reject viability before Stage-1 measurement.

These are findings, not reasons to silently widen the scope or lower the test condition.

## 8. Implementation plan and preservation rule

| Work item | Output | State in this annex |
| --- | --- | --- |
| Validate harness instrumentation | Inject a known qualifier loss at the named handoff; trace must record it at that handoff before any candidate run is interpretable. | Planned Step 0. |
| Freeze and publish pre-registration and comparator record | Commit, before any run, a versioned public record containing expected outcomes, B0–B3 configuration, comparator defender, thresholds, burden tolerance, repetition rule, stop rule and deviation log; each result trace cites that commit. | Planned prerequisite. |
| Freeze atomic 00E branches | RS-00E-Q1a, Q1b, paired Q1c-R/Q1c-NR and Q1e records; Q1d only after its atomics. | Planned. |
| Freeze 00E Q2 human-capacity branch | Saturated-reviewer fixture plus Q2-N0 sufficient-capacity control; approval remains distinct from evidence. | Planned. |
| Freeze 00E Q4 bounded-requalification branch | Non-reducing residual, response horizon, bounded experiment or `NO COMMITMENT`, reducible-residual negative control, and local null-action measure in the declared scarce-resource unit. | Planned. |
| Freeze 00F composition branches | C1 conflict and C2 absent-precedence records, including no-conflict control. | Planned. |
| Register B0–B3 configurations | Version, source access, common budget, legitimate peer controls and named comparator defender. | Planned; self-configured comparator carries no differential conclusion. |
| Build deterministic Stage-0 harness | Replay, reference-oracle module, trace store, gate-policy module and reproducible reports. | Planned. |
| Exercise stochastic configurations | Pre-registered repeated-run/distribution comparison, including qualifier and burden dispersion. | Planned when applicable. |
| Attach interface ICRs | Appendix-A records for handoffs actually exercised. | Planned; this annex does not define their schema. |
| Review sensitivity and stop criteria | Threshold-range report and programme decision. | Planned. |
| Add independent Stage-1 producer/receiver evidence | Observable comparison with stated independence limits. | Future work, not assumed. |
| Open EA-ITP-01 counterpart ledger | Before the 90-day search clock starts, record at least one named prospective external producer or receiver implementation, role, owner and contact date. No “no counterpart” finding is permitted without this dated ledger. | Planned prerequisite for the independent-interoperability search. |
| Identify Stage-2 decision context | Candidate decision owner and real context for an independent relevance/outcome review. | Future work, not assumed. |

00's S14 aggregate reading is clarified only; 00D, 00E, 00F, the frozen validation profiles and 04 remain unchanged. This annex may be revised as fixture records and a testbed become real; it must not retrospectively turn a planned fixture into a completed result.

## 9. Summary of the architectural boundary

The design needs neither an absolute oracle nor a claim that every residual is unknowable. It uses a deterministic, bounded reference oracle wherever the fixture makes a relevant distinction decidable; it explicitly preserves a possible residual where the declared test frame does not. A qualified regime-change detector is a useful but limited input, not the oracle and not a substitute for EA’s stronger T1/T4 obligations. The resulting programme is sufficient to produce a traceable evidence design now; it is not yet evidence that EA is necessary, sufficient or superior.

## Editorial continuity note — selected fixture programme

This annex is a construction and test-design layer for **selected** 00E/00F branches. Its traceability matrix, bounded oracle, negative controls and Stage 0–2 progression are not an exhaustive testbed for every S1–S14 requirement, every validation profile, every scenario or every later Ecosystem Positioning component.

Coverage gaps remain visible in the Use-Case Portfolio Requirements Coverage Map and in later pre-registration records. 00G, ACC/admissibility, agentic-gradient and full repositioning/choreography tests require their own admitted fixtures or a versioned extension of this programme; they are not silently covered by the existing matrix.
