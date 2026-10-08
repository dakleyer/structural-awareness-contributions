# FG-TIDA Decision Boundary Evaluation Profile — v0.2 Draft

> **Successor test/conformance draft.** This file preserves the v0.1 cross-theme route and adds the generic DDS Stage A gate-diagnostic layer. It does not change producer-owned Theme semantics, create an FG-TIDA verdict vocabulary, or claim any executed result.

| | |
|---|---|
| **ID** | FG-TIDA-DBC-01 |
| **Version · date** | v0.2-draft · 8 October 2026 |
| **Status** | Test/conformance preparation; no executed result |
| **Predecessor** | [v0.1 Draft](./FG_TIDA_DECISION_BOUNDARY_EVALUATION_PROFILE_v0.1_DRAFT.md) |
| **General source** | [Decision Boundary Challenge v0.2](../../DECISION_BOUNDARY_CHALLENGE_v0.2.md) |
| **Stage A diagnostic source** | [DDS Stage A Gate Diagnostic Profile v0.1 Draft](../../DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.1_DRAFT.md) |
| **Gate catalog** | [DDS Stage A Gate Catalog v0.1 Draft](../../DDS_STAGE_A_GATE_CATALOG_v0.1_DRAFT.json) |
| **Specification route** | [EA / FG-TIDA Specification Preparation v0.3 Draft](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md) |

---

## 1. What changes from v0.1

v0.1 defined a useful cross-theme decision-boundary route and hard integrity gates, but the output remained too coarse for architecture diagnosis.

v0.2 keeps the same cross-theme intent and adds:

1. a versioned, technology-neutral Stage A gate catalog;
2. one verdict and one specification-strength level per gate;
3. preregistered dependencies between gates;
4. conditional/blocking status rather than forcing downstream PASS/FAIL;
5. root-blocker and downstream-impact analysis;
6. minimum-remediation recommendations;
7. a Stage-B architecture handoff queue;
8. a prohibition on reporting only one aggregate PASS/FAIL.

No Theme-owned output is translated into these gate IDs. The gates evaluate properties of the frozen candidate specification/profile at the decision boundary.

---

## 2. Mandatory result shape

Every evaluated framework/profile must publish the gate table before any summary claim.

Minimum columns:

```text
gate_id
applicability
verdict
level
dependency_status
candidate_surfaces
case_ids
blocker_root
downstream_impacted
stage_a_remediation
stage_b_handoff
evidence_ceiling
```

Permitted verdicts:

- PASS
- FAIL
- NOT_ESTABLISHED
- NOT_APPLICABLE

Permitted levels:

- L0 absent
- L1 declared
- L2 normative candidate
- L3 scoped and owned
- L4 falsifiable/test-ready

Dependency state:

- SATISFIED
- CONDITIONAL_ON(...)
- BLOCKED_BY(...)

An overall summary may follow, but it cannot replace the gate table.

---

## 3. Core gate profile

The current generic catalog is SA-G00…SA-G14. FG-TIDA cases select only materially applicable gates.

For a typical cross-theme authority/decision-boundary fixture, the default profile should consider:

- SA-G00 decision boundary/scope;
- SA-G01 observation/freshness;
- SA-G02 evidence/effect basis;
- SA-G03 identity/representation root;
- SA-G04 authority applicability/currentness;
- SA-G05 cross-domain/principal non-substitution;
- SA-G06 indeterminacy preservation;
- SA-G07 material-change requalification;
- SA-G08 time/default/expiry;
- SA-G09 objective/mandate integrity;
- SA-G10 history/non-retroactive legitimation;
- SA-G11 bounded disposition;
- SA-G12 positive continuity/no deny-all;
- SA-G13 execution/compliance owner declaration;
- SA-G14 reconstructability.

A fixture may preregister NOT_APPLICABLE gates. It may not remove a difficult gate after inspection.

---

## 4. Dependency-aware adjudication

The evaluator scores the candidate's own text/behavioral contract first, then applies the frozen dependency graph.

Example:

```text
SA-G03 identity root              NOT_ESTABLISHED @ L1
SA-G04 authority applicability    own-text PASS @ L3
dependency                        CONDITIONAL_ON(SA-G03)
effective Stage A diagnostic      CONDITIONAL_ON(SA-G03)
```

This means the candidate has a strong authority-applicability rule but cannot support the full claim until identity/representation is independently rooted.

The same root blocker may condition SA-G05 and SA-G09. The report must show that relationship rather than count three independent defects.

---

## 5. Automatic audit recommendations

After adjudication, produce two recommendation classes.

### 5.1 Stage A remediation

Only specification/test changes count here, for example:

- make owner/scope explicit;
- distinguish message authentication from represented authority;
- state action-time expiry/revocation semantics;
- preserve UNKNOWN rather than defaulting;
- add a positive continuity case;
- define a falsifier/ablation for a gate.

### 5.2 Stage B handoff

Architecture recommendations are generated from the gate gap but do not increase the Stage A result.

Examples:

- bind identity/representation to an independently governed trust/delegation source;
- add effect evidence outside the acting agent's self-report;
- bind a disposition to an enforcement owner;
- implement targeted hold/requalification instead of global stop;
- expose the minimum trace needed to reconstruct the decision basis.

The report must label these as **Stage B handoff**, never “Stage A fixed”.

---

## 6. Minimum remediation cut set

For a failed/conditional profile:

1. identify earliest root blockers in the dependency DAG;
2. compute which downstream gates each root blocks;
3. rank the smallest remediation sets by unlock yield;
4. show residual unresolved gates after each proposed set;
5. separate specification-only work from architecture realization.

Illustrative output:

```text
Priority 1: SA-G03 -> target L3
Potentially unlocks: SA-G04, SA-G05, SA-G09
Stage A change: specify independent identity/representation root
Stage B realization: implement auditable trust/delegation binding

Priority 2: SA-G06 -> target L3
Potentially unlocks: SA-G07, SA-G11, SA-G12
Stage A change: preserve unresolved state explicitly
Stage B realization: implement state propagation/hold semantics
```

This is a diagnostic recommendation, not a guarantee that the resulting architecture will pass Stage B/C.

---

## 7. Relationship to UC-6 / UC-4 and other FG-TIDA routes

The v0.1 UC-6 → UC-4 route remains valid.

v0.2 changes only the evaluation/reporting layer:

- UC-6 or another source owns the facts and source-domain expected outcomes;
- Theme contributors own their native semantics;
- UC-4 or another testbed may host an executable profile;
- the Stage A gate profile evaluates whether the composed candidate specification preserves the required distinctions;
- Stage B later verifies whether the architecture realizes the selected gate requirements;
- Stage C later validates pinned implementation behavior.

The gate catalog is therefore reusable for UC-4, UC-6, UC-21, future Challenges and non-FG-TIDA frameworks without renaming their native outputs.

---

## 8. Preregistration requirements

Before result-producing adjudication, freeze:

- gate-catalog version;
- applicable gates;
- local gates, if any;
- minimum level required per applicable gate;
- dependency graph changes, if any;
- positive controls;
- falsifiers;
- boundary cases;
- NOT_APPLICABLE declarations;
- author predictions/ablations where used;
- blind-reader packet;
- disagreement rule;
- acceptance wording.

A gate introduced because a framework failed a case belongs only to a successor profile/version.

---

## 9. Comparison rule

Comparative reports use the same frozen gate profile across all arms.

Do not report a single vendor/framework score. Publish:

1. hard gate outcomes;
2. PASS/FAIL/NOT_ESTABLISHED/N/A counts;
3. level distribution;
4. dependency/root-blocker graph;
5. burden/accountability vectors;
6. Stage-B handoff queue;
7. evidence maturity (DBC-EL#) separately.

A framework with more PASS gates is not automatically “better” if it fails a preregistered hard gate.

---

## 10. Current evidence state

This v0.2 file defines the successor evaluation design only.

It does not assert that:

- any FG-TIDA use case has been rerun with SA-G00…SA-G14;
- Hugging Face validates the generic gate catalog;
- UC-4/UC-6 contributors accepted this successor;
- any framework passes or fails;
- Stage A recommendations are implemented in architecture;
- FG-TIDA adopted the profile.

The next evidence step is to freeze at least three materially different validation families against the same gate-catalog version before promoting the catalog from draft.


### 4.1 NOT_APPLICABLE prerequisites

A preregistered `NOT_APPLICABLE` prerequisite does not automatically block a downstream gate. It counts as satisfied-by-profile only when the fixture explains why that mechanism is irrelevant and freezes the substitute fact required by the downstream decision. This is required for abstract/reduced fixtures where, for example, principal identity is a fixed evaluator fact rather than a property under test.
