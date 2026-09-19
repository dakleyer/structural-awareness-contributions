# Pre-Registration Record — RS-00E-Q1a Stage-0 Fixture Family — v0.3

> **Status:** pre-registration record. It is frozen and publicly committed **before** any execution of this fixture family. It is not an executed fixture, a trace, a comparative result, a validation claim or a product assessment.
>
> **Binding rule:** every result trace produced for this fixture family cites the Git commit of *this* record. A run executed before this record is committed, or against a later edited copy, is **pre-registration declared** only and carries no differential conclusion.
>
> **Version relation:** v0.3 supersedes v0.2 before any execution. v0.1 and v0.2 remain immutable historical records; a new run under the corrected family cites this v0.3 record.

**Fixture family:** `RS-00E-Q1a` — declared and derivable common upstream dependency, with independent-source negative control
**Record version:** 0.3
**Frozen on:** 2026-09-19 (the public Git commit timestamp is authoritative)
**Record path:** `research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/pre_registration_v0.3.md`
**Record commit:** the first public Git commit containing this exact file. It is intentionally not written into this file because a document cannot self-anchor to the commit that creates it; every later trace cites that immutable commit.

---

## 1. Identity and traceability

| Item | Declaration |
| --- | --- |
| Fixture family ID / version | `RS-00E-Q1a` / v0.3 |
| Branches in this family | `Q1a-P1` declared shared dependency; `Q1a-P2` derivable shared dependency; `Q1a-C0` independent-source negative control |
| Scenario and gate | 00E, gate Q1 (production/evidence stage) |
| `σ(d,t)` | `sigma_release_t0` — whether the receiving decision may state that two reports independently corroborate proposition `release_basis_supported` at `t0`, under the declared deadline and evidence boundary |
| Requirement route (00 §6.1) | S5 / S9 / S14 → T1 / T2 / T4 → H2 / H3 / H4. S14 component exercised: **(1) evidence sufficiency**; component **(3) conflict/arbitration record** is not exercised here |
| KPI set (00 §5) | Correlated-evidence error rate; residual-scope preservation; false-convergence rate; total decision burden. No fixture-local measure is used in this family |
| Linked 04 ICR | None. No interface handoff crosses an external producer boundary in Stage 0; if an adapter handoff is later treated as an interface unit, an Appendix-A ICR is opened separately |

### 1.1 Public source anchors

This record anchors only to commits that exist **before** it.

| Source | Path | Version | Commit |
| --- | --- | --- | --- |
| Canonical requirements and KPI protocol | `00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md` | current | `5687b26b10dba065d56ccdaf31a2a028a3d06142` |
| Benchmark and comparator fairness (§4) | `00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md` | v0.2 | `5687b26b10dba065d56ccdaf31a2a028a3d06142` |
| Fixture, oracle and family rules (§§3–8) | `00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_PROOF_SKETCH_v0.1.md` | v0.1 | `5687b26b10dba065d56ccdaf31a2a028a3d06142` |
| Harness design | `00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md` | v0.1 | `db22634686c02f82592967b8ae6a45bb0545fd0b` |
| Scenario facts and mechanism | `00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md` | v0.1 | `5687b26b10dba065d56ccdaf31a2a028a3d06142` |

---

## 2. Frozen facts

### 2.1 Shared envelope — identical across all three branches

- Proposition: `release_basis_supported`; scope: `sigma_release_t0`
- Event order: `A` then `B`, fixed; deterministic step counter; `deadline_step = 6`
- Freshness: both reports at `freshness_step = 1`
- Action library: emit one bounded assessment posture plus one handoff envelope to `declared_receiving_owner`. No external action, no authority grant
- Source access: received report fields and the declared context resources named below. **No primary-source re-query** in any branch
- Resource ledger: identical event count, processing-step ceiling and response horizon for every configuration
- Injected material perturbation: the upstream-source relation only. Nothing else varies between branches

### 2.2 `Q1a-P1` — declared shared dependency (preservation arm)

`A` and `B` each carry `upstream_source_id = "P"` in the received provenance field.
Frozen fact: `A` and `B` are **not** independent corroboration. Neither report is false.

### 2.3 `Q1a-P2` — derivable shared dependency (discriminating arm)

`A` carries `upstream_source_id = "feed-7"`; `B` carries `upstream_source_id = "vendor-X"`.
A declared, frozen **source registry** is available as a context resource, equally accessible to every configuration at equal declared cost, and resolves `feed-7 → P` and `vendor-X → P`.
Frozen fact: `A` and `B` are not independent corroboration; the shared ancestry is derivable from declared, available facts and is not stated in either report.

### 2.4 `Q1a-C0` — independent sources (negative control)

`A` carries `upstream_source_id = "P_A"`; `B` carries `upstream_source_id = "P_B"`. The frozen registry explicitly resolves `P_A → P_A` and `P_B → P_B`: distinct roots through the same resolution path exercised in P2.
Frozen fact: `A` and `B` are independent in the declared branch.

### 2.5 Fact-freezing authority and label

Fact-freezing authority: **Iván Abril Palma (EA corpus maintainer)**. Because the fact-freezing authority is also the designer of the candidate configuration, this family is labelled **facts self-declared** at pre-registration and in every trace.

### 2.6 Validity

Freeze date: **2026-09-19**. Validity horizon: 12 months from freeze, or until any of the following changes, whichever is earlier: the declared registry semantics, the permitted posture set, the resource ledger, the KPI definitions in 00 §5, or the fixture-family rule in 00D-A01 §3. Any such change creates a new fixture version and a new pre-registration record.

---

## 3. Source-access assumption

Primary-source re-query is **unavailable** in all three branches. Consequently any distinction lost at the adapter handoff is an explicit informational loss within this fixture, not a recoverable cost. The registry of §2.3 is not a primary-source re-query: it is a declared context resource with a fixed declared cost, available identically to every configuration.

---

## 4. Scarce resource

The binding resource is the **response horizon**, expressed as deterministic steps to `deadline_step = 6`. Burden is recorded in modelled processing steps and modelled elapsed steps.

**Pre-registered expectation:** at this fixture size the burden of the compared configurations is *not* expected to discriminate. A near-equal burden result is therefore not reported as a finding in either direction, and "equal or lower burden" is evaluated only against the tolerance in §7.3.

---

## 5. Configuration under test and comparator

| Item | Declaration |
| --- | --- |
| Configuration under test | `B3` — deterministic EA-profiled dependency-preservation adapter, version `B3-Q1A-EA-PRESERVATION-v0.1` |
| Comparator | `B1` — deterministic conventional provenance-and-registry-join peer, version `B1-Q1A-PROVENANCE-JOIN-v0.1`; configuration frozen in this record |
| Configuration owner | **Iván Abril Palma (EA corpus maintainer)** |
| Comparator defender | **None named at freeze** |
| Defender envelope | The defender may change the `B1` configuration only within: the same received fields, the same registry access and declared cost, the same processing-step ceiling, and the same response horizon. Changes are made **before** freeze and recorded here |
| Label if no defender | **Comparator self-configured** — the run supports bounded configuration verification only and no EA differential claim |
| Unresolved defender objection | None at freeze. Any later objection is recorded in the trace and blocks any differential conclusion; it does not block the descriptive run. |

Both adapters receive identical fields: `report_id`, `proposition_id`, `producer_id`, `upstream_source_id`, `freshness_step`, `scope_id`, `deadline_step`, registry access and resource ledger. No arm receives extra evidence, authority, time, reviewers or re-query.

**Frozen adapter profiles.** B1 compares direct provenance in P1 and deterministically joins the received registry in P2/C0 before emitting the closed branch posture. B3 uses the same direct provenance and registry access, then emits the dependency assessment, affected scope and required residual/handoff fields. Both profiles are deterministic by definition; neither uses a model, primary-source re-query or external producer.

---

## 6. Oracle contract

`O_ref` is stipulative, deterministic and post-run only. It has privileged access to the frozen branch facts and the registry resolution. That privilege is an evaluator privilege and is not attributed to any configuration.

| Branch | `O_ref` reference facts | `R_ref` |
| --- | --- | --- |
| `Q1a-P1` | `A` and `B` share `P`; an independent-support claim is unsupported | None material for this test question |
| `Q1a-P2` | `feed-7` and `vendor-X` both resolve to `P`; an independent-support claim is unsupported; the ancestry is derivable from declared available facts | None material for this test question |
| `Q1a-C0` | `A` and `B` have distinct roots; independent support is supported within the branch | None material for this test question |

`O_ref` output contains reference facts, permitted observable result, `R_ref` and trace reason only. It contains no threshold, disposition or comparative policy. The runtime cannot query `O_ref`.

---

## 7. Gate policy, permitted postures and tolerance

### 7.1 Permitted postures — exact and closed

The permitted set is closed. Any posture outside the listed set is a **candidate failure**, not "another bounded qualified posture".

| Branch | Required assessment fields | Permitted postures | Failure |
| --- | --- | --- | --- |
| `Q1a-P1` | `independent_support = false`; `shared_upstream_sources` includes `P`; `residual.present = true` | `REQUALIFY`, `CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT` | Any independent-support claim; loss of the shared-source field; missing residual; `HOLD` (over-containment: a bounded qualified posture is available); any other posture |
| `Q1a-P2` | as `Q1a-P1`, with `shared_upstream_sources` resolved to `P` and the resolution basis recorded | `REQUALIFY`, `CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT` | as `Q1a-P1`; additionally, asserting independence on the basis that the two `upstream_source_id` strings differ |
| `Q1a-C0` | `independent_support = true` permitted; no dependency warning | `CONTINUE_QUALIFIED` | Any manufactured dependency warning; `REQUALIFY` or `HOLD` (false containment) |

### 7.2 Measures (00 §5) — numerator and denominator

| Measure | Numerator | Denominator |
| --- | --- | --- |
| Correlated-evidence error | Unsupported independent-corroboration claims | Primary branches executed (`Q1a-P1`, `Q1a-P2`) |
| Residual-scope preservation | Required residual/scope fields retained and interpretable at the receiving envelope | Required residual/scope fields for the branch |
| False-convergence rate | Unsupported shared closures from the two correlated reports | Primary branches executed |
| Total decision burden | Modelled processing steps and modelled elapsed steps per run | Reported per branch per configuration; not aggregated across branches |

**Reporting rule:** with three branches per configuration, all measures are reported as **counts with their denominator**, never as percentages or rate estimates.

### 7.3 Tolerance and sensitivity

- Equal-or-lower burden tolerance: ±10% of modelled processing steps. Differences inside the band are reported as "no burden difference at this fixture size".
- Threshold sensitivity: the only thresholds in this family are the closed posture sets of §7.1, which are categorical. The record therefore declares **no threshold-sensitivity range**; a later fixture with numeric thresholds must declare one.

---

## 8. Evidence status and stability

- Evidence status: **Stage-0 stipulative verification** only. Not Stage 1, not observational, not validation.
- Determinism: all configurations in this family are expected to be deterministic. Pre-registered run count: **2 identical runs per branch per configuration**, used solely for the determinism check of §9.2, not as repetition for dispersion.
- If any configuration is in fact non-deterministic, execution stops and a new record pre-registers a run count, seed rule and outcome-distribution comparison.

---

## 9. Mandatory Step 0 — harness gates

No candidate result in this family is interpretable, publishable or citable unless both gates pass first and their traces are published.

### 9.1 Instrumentation self-test

Remove `upstream_source_id` from a named adapter handoff in `Q1a-P1`. The trace must record: fixture ID and branch; exact handoff name; expected qualifier `upstream_source_id=P`; observed loss; step; disposition `PASS`. Any missing field, or a loss not detected at that handoff, is a **harness failure**.

### 9.2 Determinism check

Two executions of the same frozen bundle and configuration must produce byte-identical **canonical traces** after excluding the run identifier and wall-clock timestamps. Their canonical-trace hashes must match. A mismatch is a **harness failure**.

---

## 10. Falsification, controls and pre-registered interpretation

The family is one evaluation unit: `Q1a-P1`, `Q1a-P2` and `Q1a-C0` execute under this record, and a primary-only run is incomplete rather than positive.

| Observation | Pre-registered meaning |
| --- | --- |
| `B3` loses the shared-source field, claims independent support, or closes without residual in `P1` or `P2` | Candidate failure |
| `B3` raises a dependency warning in `C0` | Candidate/control failure |
| `B1` reaches a permitted posture in `P1` **and** `P2` within tolerance | Differential falsifier — a negative EA result, reported as such |
| `B1` passes `P1` but fails `P2` while `B3` passes both | The declared differential is limited to derivable, non-stated dependency. It is not evidence of a general EA advantage |
| Both configurations pass all three branches | Non-discriminating fixture. Reported as such; no EA claim follows |
| Self-test or determinism check fails | Harness failure; no candidate result reported |
| No comparator defender is named before freeze | Descriptive configuration finding only; no differential conclusion in any branch |

**Pre-registered expectation, recorded before execution:** `Q1a-P1` is expected to be non-discriminating, because the dependency is stated in the received field and any configuration that compares two strings can preserve it. `Q1a-P2` is the discriminating arm, but the frozen B1 provenance-and-registry-join peer is expected to resolve it and reach a permitted result. That outcome is therefore pre-registered as a negative EA differential result in principle, not reinterpreted after execution. Because no comparator defender or independent reviewer is named in this record, the v0.3 run remains descriptive only: this P2 expectation cannot support a differential conclusion. Recording these expectations in advance prevents a later reading of either primary arm as a positive result.

---

## 11. Ownership, review and stop rule

| Role | Holder |
| --- | --- |
| Semantic owner | **Iván Abril Palma (EA corpus maintainer)** |
| Fact-freezing authority | **Iván Abril Palma (EA corpus maintainer)** |
| Configuration owner (`B3`) | **Iván Abril Palma (EA corpus maintainer)** |
| Comparator defender (`B1`) | **None named at freeze** — triggers the §5 label |
| Reviewer (distinct from any adapter/maintenance owner of a mapping under review) | **None named at freeze** — internal pre-registration only; no independent review claim |
| Declared relationships | Semantic owner, fact-freezing authority and B3 configuration owner are the same person. No comparator defender or distinct reviewer is named at freeze; any run, **including P2**, is limited to descriptive Stage-0 verification and carries no EA differential conclusion. |

**Stop rule.** Execution stops, and the result is recorded as a finding rather than a route change, if: the self-test or determinism check fails; a branch cannot be executed without inventing a fact, producer or receiver not in this record; or the declared response horizon cannot be met in the deterministic harness (recorded as **modelled burden — provisional**).

**Deviation rule.** Any deviation from this record after freeze is recorded in the trace with its reason, and the affected result is reported as deviated. Reducing the required-field set of §7.1 is a registrable finding, never an improvement in preservation.

---

## 12. Declared labels for this family

At freeze, and in every trace produced under this record:

- **facts self-declared** — yes (§2.5)
- **comparator self-configured** — yes; no defender is named at freeze, so no EA differential conclusion is permitted under this record, including for P2
- **evidence status** — Stage-0 stipulative verification
- **independent interoperability** — not claimed; no Level-2 producer is involved
