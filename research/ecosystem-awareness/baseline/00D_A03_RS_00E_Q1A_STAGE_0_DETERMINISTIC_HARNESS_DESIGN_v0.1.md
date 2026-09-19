# RS-00E-Q1a Stage-0 Deterministic Harness Design

> **Status:** public implementation design only. This is not a pre-registration, implemented harness, executed fixture, comparative result, validation claim or product assessment.
>
> **Scope:** one Stage-0 fixture family only: `RS-00E-Q1a` — declared common dependency `P → {A,B}` — and its independent-source negative-control branch.
>
> **Purpose:** show that the published scenario-fixture discipline can be implemented as a small deterministic harness without claiming that the full 00E scenario, a complete testbed or EA effectiveness has been tested.

## 1. Bounded claim and source anchors

The harness asks one narrow question:

> When two reports carry a declared common upstream source, does a configuration preserve that dependency, avoid calling them independent corroboration, preserve the affected residual and issue a bounded qualified posture?

The primary branch has one upstream source `P` producing reports `A` and `B`. The negative-control branch has independent upstream sources `P_A` and `P_B`. Both branches carry the same proposition, scope, deadline and resource envelope. This is a **preservation** fixture: the shared dependency is represented in the received provenance field. It does not claim that the harness discovers every hidden dependency in an open ecosystem.

| Source | Public anchor used by this design |
| --- | --- |
| Requirements and KPI protocol | [00 — Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), especially §5 and §6.1, at commit `5687b26b10dba065d56ccdaf31a2a028a3d06142` |
| Comparator fairness | [00D — Canonical Architecture Benchmark](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) §4, at the same commit |
| Fixture and oracle rules | [00D-A01](./00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_PROOF_SKETCH_v0.1.md) §§3–8, at the same commit |
| Scenario facts and mechanism | [00E — Reference Failure Scenario](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) |

The actual pre-registration must replace this design anchor with exact document paths, versions and commits, including its own **prior** public commit. A document cannot self-anchor to the commit that creates it.

## 2. What this harness is — and is not

| It does | It does not do |
| --- | --- |
| Replays two small frozen branches deterministically. | Reproduce the 100-million-token workload or all five 00E gates. |
| Tests whether a received provenance/dependency qualifier survives the configured handoff. | Discover arbitrary hidden dependencies or establish world truth. |
| Compares a named B3 configuration with a pre-registered B1 configuration under the same inputs and burden ledger. | Prove an EA differential, unless the comparator is independently defended and the later pre-registration permits that conclusion. |
| Produces traceable, machine-readable results and verifies its own qualifier-loss instrumentation. | Establish independent interoperability, production performance or external validation. |

The smallest viable demonstration is therefore a **deterministic harness**, not a complete testbed. It is a one-fixture proof that the measurement and falsification route can be executed.

## 3. Fixture family and frozen branch model

The primary and control branch are one fixture family under the rule in 00D-A01 §3. The later pre-registration publishes them together and no primary-only execution is interpretable.

### 3.1 Shared envelope

- **Decision scope `σ(d,t)`:** whether the receiving decision may state that two reports independently corroborate the same proposition.
- **Scarce resource:** response horizon. Stage 0 records modelled processing steps and deterministic elapsed-time budget; it does not claim measured production latency.
- **Source access:** received report and provenance fields only; no primary-source re-query.
- **Authority/action library:** emit one bounded assessment posture and handoff; no external action.
- **Allowed postures:** `CONTINUE_QUALIFIED`, `REQUALIFY`, `HOLD`. The exact permitted set and threshold belong in the later pre-registration.
- **Common budget:** the same event count, source access, processing-step ceiling and response horizon for B1 and B3.

### 3.2 Primary branch — declared common dependency

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

### 3.3 Negative-control branch — independent sources

The control changes only the upstream-source relation:

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

All remaining declared facts, task and budget are identical. A configuration that raises a common-dependency warning in this branch fails the negative control.

## 4. Deterministic reference oracle

`O_ref` is stipulative and bounded. It has privileged access only to the frozen branch facts; that privilege is not attributed to B1 or B3.

| Branch | `O_ref` expected facts | Permitted assessment outcome |
| --- | --- | --- |
| Primary common dependency | `A` and `B` share `P`; independent-support claim is unsupported; affected residual remains explicit. | Dependency preserved; no independent-corroboration claim; `REQUALIFY` or another pre-registered bounded qualified posture. |
| Independent-source control | `A` and `B` are independent in the frozen branch. | No fabricated dependency warning or unnecessary containment; a pre-registered qualified continuation is permitted. |

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
  frozen_facts.primary.json
  frozen_facts.control.json
  oracle.primary.json
  oracle.control.json
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

Each adapter receives the same `report_id`, proposition, scope, freshness, producer ID, `upstream_source_id`, deadline and resource ledger. No arm receives extra evidence, authority, time, reviewers or source re-query.

The candidate must emit:

```json
{
  "configuration_id": "B1-or-B3",
  "dependency_assessment": {
    "independent_support": false,
    "shared_upstream_sources": ["P"]
  },
  "residual": {
    "present": true,
    "reason": "no_independent_support"
  },
  "posture": "REQUALIFY",
  "affected_scope": "sigma_release_t0",
  "handoff_target": "declared_receiving_owner",
  "burden": {
    "processing_steps": 0,
    "modelled_time_steps": 0
  }
}
```

B1 is not a weakened strawman. Its exact configuration is frozen and reviewed by its comparator defender in the later pre-registration. If B1 preserves the same dependency and reaches the same qualified outcome with equal or lower burden, that is a negative EA differential result, not a harness failure. If no defender is available, the run is labelled **comparator self-configured** and remains descriptive only.

## 7. Measures, gates and falsification

The fixture uses the canonical measures:

- **Correlated-evidence error rate:** unsupported independent-corroboration claims ÷ primary branches.
- **Residual-scope preservation:** required residual/scope fields retained ÷ handoffs requiring them.
- **False-convergence rate:** unsupported shared closure from the two correlated reports ÷ designated convergence branches.
- **Total decision burden:** declared modelled processing cost per run.

The pre-registration fixes thresholds, numerator/denominator details, tolerance for equal/lower burden and the permitted posture set. It also identifies any fixture-local measure; none is needed for this minimal family.

A result is interpreted separately:

| Observation | Meaning |
| --- | --- |
| B3 loses `P`, calls A/B independent or silently closes. | Candidate failure. |
| B3 manufactures a dependency warning in the independent control. | Candidate/control failure. |
| B1 reaches the same qualified result with equal/lower burden. | Differential falsifier; a negative EA result is legitimate. |
| Instrumentation fails to trace the injected loss. | Harness failure; no candidate result is interpretable. |
| B1 lacks a defensible configuration. | Descriptive configuration finding only; no EA differential claim. |

## 8. Mandatory Step 0: instrumentation self-test

Before a candidate run, the harness deliberately removes `upstream_source_id` from a named adapter handoff in the primary branch.

The trace must record:

1. fixture ID and branch;
2. exact handoff name;
3. expected qualifier `upstream_source_id=P`;
4. observed loss;
5. timestamp/step;
6. self-test disposition `PASS`.

If any field is absent, or the loss is not detected at that handoff, the self-test fails and the candidate run must not be reported as evidence.

## 9. Execution sequence

1. Create and publicly commit the `RS-00E-Q1a` pre-registration record, with final owners, B1 configuration/defender, thresholds, tolerance, stop rule and source anchors.
2. Build the fixture bundles, `O_ref`, adapters, evaluator and trace writer from this design.
3. Run the instrumentation self-test and publish its trace.
4. Execute the primary and independent-control branches as one fixture family.
5. Publish the result trace, report and the cited pre-registration commit.
6. Report candidate failure, differential falsification, harness failure or descriptive-only status exactly as produced; do not convert a planned or negative result into an EA success claim.

## 10. Deliberate incompleteness and next boundary

This design leaves out B0/B2, stochastic repetition, real producers, human-capacity Q2, bounded-requalification Q4, 00F and the common-dependency cascade fixture. It does not validate EA or justify a Stage-1 claim.

Its sole purpose is to make one public, reproducible Stage-0 execution possible. Once its pre-registration and first trace exist, the corpus will contain evidence of an executed measurement path rather than only evidence-design documentation.
