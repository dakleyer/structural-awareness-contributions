# RS-00E-Q1a Stage-0 Deterministic Harness Design

> **Status:** public implementation design only. This is not a pre-registration, implemented harness, executed fixture, comparative result, validation claim or product assessment.
>
> **Scope:** one Stage-0 fixture family only: declared common dependency `P → {A,B}`, derivable common dependency `feed-7 → P ← vendor-X`, and an independent-source negative-control branch.
>
> **Purpose:** show that the published scenario-fixture discipline can be implemented as a small deterministic harness without claiming that the full 00E scenario, a complete testbed or EA effectiveness has been tested.

## 1. Bounded claim and source anchors

The harness asks one narrow question:

> When two reports carry either a declared or a derivable common upstream source, does a configuration preserve that dependency, avoid calling them independent corroboration, preserve the affected residual and issue a bounded qualified posture?

The fixture family contains three branches. **P1** gives both reports the same received `upstream_source_id=P`; it is a preservation and instrumentation branch, not an expected discriminator. **P2** gives A `feed-7` and B `vendor-X`, while a frozen source registry available equally to every configuration resolves both to `P`; it is the discriminating composition branch. **C0** gives distinct roots `P_A` and `P_B` as the negative control. All branches carry the same proposition, scope, deadline and resource envelope. The registry is a declared context resource, not a primary-source re-query. This family does not claim that the harness discovers every hidden dependency in an open ecosystem.

| Source | Public anchor used by this design |
| --- | --- |
| Requirements and KPI protocol | [00 — Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), especially §5 and §6.1, at commit `5687b26b10dba065d56ccdaf31a2a028a3d06142` |
| Comparator fairness | [00D — Canonical Architecture Benchmark](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) §4, at the same commit |
| Fixture and oracle rules | [00D-A01](./00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_PROOF_SKETCH_v0.1.md) §§3–8, at the same commit |
| Scenario facts and mechanism | [00E — Reference Failure Scenario](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md), at commit `5687b26b10dba065d56ccdaf31a2a028a3d06142` |

The actual pre-registration must replace this design anchor with exact document paths, versions and commits, including its own **prior** public commit. A document cannot self-anchor to the commit that creates it.

## 2. What this harness is — and is not

| It does | It does not do |
| --- | --- |
| Replays three small frozen branches deterministically as one fixture family. | Reproduce the 100-million-token workload or all five 00E gates. |
| Separates direct qualifier preservation (P1) from derivable dependency composition (P2). | Discover arbitrary hidden dependencies or establish world truth. |
| Compares a named B3 configuration with a pre-registered B1 configuration under the same inputs and burden ledger. | Prove an EA differential, unless the comparator is independently defended and the later pre-registration permits that conclusion. |
| Produces traceable, machine-readable results and verifies its own qualifier-loss instrumentation. | Establish independent interoperability, production performance or external validation. |

The smallest viable demonstration is therefore a **deterministic harness**, not a complete testbed. It is a one-fixture proof that the measurement and falsification route can be executed.

## 3. Fixture family and frozen branch model

This is one fixture family under 00D-A01 §3: P1, P2 and C0 use one pre-registration, one public pre-execution commit and one completed evaluation. A run omitting any branch is incomplete, not a positive result. The family is declared **facts self-declared**. It is also **comparator self-configured** unless the later pre-registration names a B1 comparator defender; without that defender no differential conclusion is permitted.

### 3.1 Shared envelope

- **Decision scope `σ(d,t)`:** whether the receiving decision may state that two reports independently corroborate the same proposition.
- **Scarce resource:** response horizon. Stage 0 records modelled processing steps and deterministic elapsed-time budget; it does not claim measured production latency.
- **Source access:** received report and provenance fields plus the frozen source registry in P2/C0. The registry is a declared context resource, not a primary-source re-query; it has identical access and declared cost for B1 and B3.
- **Authority/action library:** emit one bounded assessment posture and handoff; no external action.
- **Closed permitted postures:** P1/P2 permit only `REQUALIFY` or `CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT`; C0 permits only `CONTINUE_QUALIFIED`. `HOLD` is a failure in every branch because a bounded qualified posture is available. The later pre-registration repeats, rather than widens, this set.
- **Common budget:** the same event count, source access, processing-step ceiling and response horizon for B1 and B3.

### 3.2 P1 — declared common dependency (preservation and instrumentation branch)

```json
{
  "fixture_id": "RS-00E-Q1a",
  "branch": "primary_common_dependency",
  "proposition_id": "release_basis_supported",
  "scope_id": "sigma_release_t0",
  "deadline_step": 6,
  "reports": [
    {
      "report_id": "A",
      "proposition_id": "release_basis_supported",
      "producer_id": "producer_A",
      "upstream_source_id": "P",
      "freshness_step": 1
    },
    {
      "report_id": "B",
      "proposition_id": "release_basis_supported",
      "producer_id": "producer_B",
      "upstream_source_id": "P",
      "freshness_step": 1
    }
  ]
}
```

The frozen fact is not that either report is false. It is that `A` and `B` are **not independent corroboration** because both descend from `P`.

### 3.3 P2 — derivable common dependency (discriminating composition branch)

P2 keeps the same reports but makes the common ancestry derivable rather than directly stated:

```json
{
  "fixture_id": "RS-00E-Q1a",
  "branch": "P2_derivable_common_dependency",
  "reports": [
    {"report_id": "A", "upstream_source_id": "feed-7"},
    {"report_id": "B", "upstream_source_id": "vendor-X"}
  ],
  "source_registry": {
    "feed-7": "P",
    "vendor-X": "P"
  }
}
```

The registry is received context with a fixed, identical declared cost. It is not primary-source re-query. P2 is informative because the configuration must compose the two references; a B1 configuration that does so within the common envelope legitimately falsifies the EA differential.

### 3.4 C0 — independent-source negative control

The control changes only the source-registry resolution:

```json
{
  "fixture_id": "RS-00E-Q1a",
  "branch": "control_independent_sources",
  "reports": [
    {"report_id": "A", "upstream_source_id": "P_A"},
    {"report_id": "B", "upstream_source_id": "P_B"}
  ]
}
```

All remaining declared facts, task and budget are identical. A configuration that raises a common-dependency warning in this branch fails the negative control. P1, P2 and C0 are never interpreted separately as completed fixture results.

## 4. Deterministic reference oracle

`O_ref` is stipulative and bounded. It has privileged access only to the frozen branch facts; that privilege is not attributed to B1 or B3.

| Branch | `O_ref` expected facts | Permitted assessment outcome |
| --- | --- | --- |
| P1 declared common dependency | `A` and `B` share `P`; independent-support claim is unsupported; `R_ref: none material for this question`. | `REQUALIFY` or `CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT`, with required dependency and residual fields. |
| P2 derivable common dependency | `feed-7` and `vendor-X` resolve to `P`; independent-support claim is unsupported; `R_ref: none material for this question`. | `REQUALIFY` or `CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT`, with recorded resolution basis. |
| C0 independent-source control | `A` and `B` resolve to distinct roots; `R_ref: none material for this question`. | `CONTINUE_QUALIFIED`; no fabricated dependency warning or containment. |

The oracle output contains only reference facts, permitted observable result, `R_ref` and trace reason. Thresholds, release disposition and comparative policy remain in the gate policy.

## 5. Minimal harness architecture

| Component | Responsibility | Output |
| --- | --- | --- |
| Fixture loader | Loads one immutable branch bundle and validates schema/version. | Normalized events or a validation error. |
| Event player | Emits `A` and `B` in fixed order with a deterministic step counter. | Replay events. |
| Configuration adapter | Invokes B1 or B3 with identical allowed fields and ledger. | Candidate assessment and handoff envelope. |
| `O_ref` module | Evaluates the frozen branch independently of the candidate. | Expected facts and permitted posture set. |
| Constraint evaluator | Compares candidate output, oracle and gate policy without changing either. | Candidate-failure status, control status and measured KPI values. |
| Trace writer | Records every handoff, loss detection, outcome and source anchor. | Append-only JSONL trace and human-readable report. |
| Instrumentation self-test | Injects one known qualifier loss before candidate runs. | Pass/fail evidence that the trace sees the loss at the named handoff. |

A minimal file layout is:

```text
fixtures/RS-00E-Q1a/
  frozen_facts.p1.json
  frozen_facts.p2.json
  frozen_facts.c0.json
  oracle.p1.json
  oracle.p2.json
  oracle.c0.json
  gate_policy.json
  pre_registration.md                 # created and committed before execution
harness/
  replay
  adapters/b1
  adapters/b3
  oracle
  evaluator
  trace
runs/
  RS-00E-Q1a/<run-id>/trace.jsonl
  RS-00E-Q1a/<run-id>/report.md
```

This is a proposed implementation layout, not a claim that these files or modules already exist.

## 6. Candidate contract and fairness

Each adapter receives the same `report_id`, proposition, scope, freshness, producer ID, `upstream_source_id`, deadline, frozen source-registry access and resource ledger. No arm receives extra evidence, authority, time, reviewers or source re-query.

The candidate must emit:

```json
{
  "configuration_id": "<B1-or-B3>",
  "dependency_assessment": {
    "independent_support": "<boolean>",
    "shared_upstream_sources": ["<zero-or-more-source-ids>"],
    "resolution_basis": ["<received-field-or-registry-reference>"]
  },
  "residual": {
    "present": "<boolean>",
    "reason": "<declared-reason-or-none>"
  },
  "posture": "<closed-posture-for-branch>",
  "affected_scope": "sigma_release_t0",
  "handoff_target": "declared_receiving_owner",
  "burden": {
    "processing_steps": "<non-negative-integer>",
    "modelled_time_steps": "<non-negative-integer>"
  }
}
```

B1 is not a weakened strawman. Its exact configuration is frozen and reviewed by its comparator defender in the later pre-registration. If B1 preserves the same dependency and reaches the same qualified outcome with equal or lower burden, that is a negative EA differential result, not a harness failure. If no defender is available, the run is labelled **comparator self-configured** and remains descriptive only.

## 7. Measures, gates and falsification

The fixture uses the canonical measures:

- **Correlated-evidence error rate:** unsupported independent-corroboration claims ÷ the two primary branches (P1 and P2) executed for that configuration.
- **Residual-scope preservation:** required residual/scope fields retained ÷ required residual/scope fields for the branch.
- **False-convergence rate:** unsupported shared closures from the two correlated reports ÷ the two primary branches (P1 and P2) executed for that configuration.
- **Total decision burden:** declared modelled processing cost per branch per run; it is recorded but is not expected to discriminate at this fixture size.

The pre-registration fixes the count denominators, tolerance for equal/lower burden and the closed permitted posture set. At this fixture size it pre-registers burden as modelled and non-discriminating; a near-equal burden is not a finding. It also identifies any fixture-local measure; none is needed for this family.

A result is interpreted separately:

| Observation | Meaning |
| --- | --- |
| B3 loses the dependency, calls A/B independent, omits the required residual or emits a posture outside the closed branch set. | Candidate failure. |
| B3 manufactures a dependency warning in C0. | Candidate/control failure. |
| B1 reaches a permitted result in both P1 and P2 within tolerance. | Differential falsifier; a negative EA result is legitimate. |
| Instrumentation fails to trace the injected loss. | Harness failure; no candidate result is interpretable. |
| B1 lacks a defensible configuration. | Descriptive configuration finding only; no EA differential claim. |

## 8. Mandatory Step 0: harness self-tests

### 8.1 Qualifier-loss instrumentation self-test

Before a candidate run, the harness deliberately removes `upstream_source_id` from a named adapter handoff in P1.

The trace must record:

1. fixture ID and branch;
2. exact handoff name;
3. expected qualifier `upstream_source_id=P`;
4. observed loss;
5. timestamp/step;
6. self-test disposition `PASS`.

If any field is absent, or the loss is not detected at that handoff, the self-test fails and the candidate run must not be reported as evidence.

### 8.2 Determinism self-test

Two executions of the same frozen bundle and configuration must produce byte-identical **canonical traces** after excluding run ID and wall-clock timestamps. Their canonical-trace hashes must match. A mismatch is a harness failure, not a candidate finding.

## 9. Execution sequence

1. Create and publicly commit the `RS-00E-Q1a` pre-registration record, with final owners, B1 configuration/defender, closed postures, tolerances, stop rule and source anchors.
2. Build the P1, P2 and C0 bundles, `O_ref`, adapters, evaluator and trace writer from this design.
3. Run the determinism self-test and qualifier-loss instrumentation self-test; publish both traces.
4. Execute P1, P2 and C0 as one fixture family.
5. Publish the result trace, report and the cited pre-registration commit.
6. Report candidate failure, differential falsification, harness failure or descriptive-only status exactly as produced; do not convert a planned or negative result into an EA success claim.

## 10. Deliberate incompleteness and next boundary

This design leaves out B0/B2, stochastic repetition, real producers, human-capacity Q2, bounded-requalification Q4, 00F and the common-dependency cascade fixture. Modelled burden is deliberately non-discriminating in this small family. It does not validate EA or justify a Stage-1 claim.

Its sole purpose is to make one public, reproducible Stage-0 execution possible. Once its pre-registration and first trace exist, the corpus will contain evidence of an executed measurement path rather than only evidence-design documentation.
