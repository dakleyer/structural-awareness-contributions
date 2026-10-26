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
test_role
own_verdict
level
required_min_level
dependency_status
effective_status
candidate_surfaces
case_ids
blocker_root
downstream_impacted
unlock_candidates
stage_a_remediation
stage_b_handoff
evidence_ceiling
```

Permitted own verdicts:

- PASS
- FAIL
- NOT_ESTABLISHED
- NOT_APPLICABLE

Permitted test roles:

- DISCRIMINATING
- COVERAGE_CONTROL
- BOUNDARY_CONTROL

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

Effective status is the claim-usable result after hard-prerequisite and minimum-level checks. It may be PASS / FAIL / NOT_ESTABLISHED / NOT_APPLICABLE / CONDITIONAL_ON(...) / BLOCKED_BY(...).

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

The evaluator first records the candidate's **own verdict** and specification-strength level, then applies the frozen dependency graph and the preregistered minimum level.

A basic gate and a stronger multi-gate claim are not the same thing.

Example:

```text
SA-G03 identity root                 NOT_ESTABLISHED @ L1
SA-G04 authority applicability       own verdict PASS @ L3
SA-G04 basic dependency              SATISFIED
CLAIM-AUTHORITY-RESOLVED             CONDITIONAL_ON(SA-G03)
```

This means the candidate has a strong authority-applicability rule. SA-G04 itself is not rewritten as a failure merely because the actor/role trust root is unresolved. The stronger authority-resolved claim remains conditional when the frozen claim contract requires SA-G03.
