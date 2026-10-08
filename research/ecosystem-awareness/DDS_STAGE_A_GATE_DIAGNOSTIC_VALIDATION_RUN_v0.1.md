# DDS Stage A — Gate Diagnostic Validation Run v0.1

**Date:** 8 October 2026.  
**Status:** maintainer-side structural portability run · not an independent candidate adjudication · not a promotion to stable/canonical gate taxonomy.  
**Catalog tested:** [DDS Stage A Gate Catalog v0.1 Draft](./DDS_STAGE_A_GATE_CATALOG_v0.1_DRAFT.json)  
**Profile tested:** [DDS Stage A Gate Diagnostic Profile v0.1 Draft](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.1_DRAFT.md)

## 1. Purpose

Execute the preregistered portability questions against three materially different Stage A families without converting this exercise into a score for EA or any technology.

This run asks whether the gate model can represent each family faithfully, distinguish NOT_APPLICABLE from missing coverage, preserve native semantics, and produce useful dependency/remediation structure without importing Stage B/C claims.

## 2. Validation families used

### V-A — Hugging Face requirement-level package

Source family: `00G-R01/extensions/hugging-face/`, current preregistered v0.3 package.

Relevant properties include authority applicability, identity/representation, cross-domain substitution, UNKNOWN, material change, timeout/expiry, objective displacement, history, bounded disposition, positive continuity, execution ownership and reconstructability.

**Catalog role:** adversarial historical family that materially informed the design. It can expose contradictions but cannot validate generality by itself.

### V-B — R01 probabilistic reduction core

Source family: `00G-R01` base scenario and conditioned mathematical line.

R01 freezes a task origin, binding obligation, evaluator truth for admissibility, permitted/forbidden alternatives, information/query limits, budget/deadline, auditable trajectories and Cost/Risk/Effectiveness acceptance. It explicitly states that the base scenario does not include social redefinition of mission, role or authority.

**Catalog role:** abstract/mathematical stress. Identity resolution, runtime enforcement ownership and some historical-change properties can legitimately be outside the material boundary rather than treated as defects.

### V-C — AWS Step Functions / RDS Semantic-TOCTOU profile

Source family: `00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md`.

The profile freezes ordinary, defended and defended-under-drift trajectories; action-time reads; PolicyManifest; a single-writer broker/lease/version rule; valid-continuity control; targeted requalification; source/dependency/freshness drift; and reconstructable Q0–Q6 traces.

**Catalog role:** non-HF technology/configuration stress using native AWS/workflow concepts rather than EA-native vocabulary.

## 3. Applicability sanity map

This is an applicability/representability check, **not a gate verdict table**.

| Gate | V-A HF | V-B R01 base | V-C AWS/00I | Structural observation |
|---|---|---|---|---|
| SA-G00 decision boundary/scope | material | material | material | general |
| SA-G01 observation/freshness | material | material | material | general |
| SA-G02 provenance/effect basis | material | material | material | general, evidence form differs |
| SA-G03 identity/representation root | material | normally N/A/frozen evaluator fact | normally N/A/frozen configuration fact | N/A rule required; must not force IAM problem into every fixture |
| SA-G04 authority applicability/currentness | material | material as frozen mandate/admissibility | material as current policy/freeze/permission basis | native semantics differ but property is representable |
| SA-G05 principal/domain non-substitution | material | material where composition/admissibility is exercised | profile-specific / may be N/A in base 00I | not universally applicable |
| SA-G06 indeterminacy preservation | material | material through abstention/incompletion | material through REQUALIFY/ambiguity handling | general |
| SA-G07 material-change requalification | material | normally N/A in fixed base unless extension adds change | central | validates selective applicability |
| SA-G08 time/default/expiry discipline | material | material through budget/deadline | material through freshness/horizon/freeze | general |
| SA-G09 objective/mandate integrity | material | material: local reward cannot override binding obligation | normally N/A in base 00I | not workflow-specific |
| SA-G10 history/non-retroactive legitimation | material | normally N/A in static base | material through diagnosis/intervention lineage | selective |
| SA-G11 bounded disposition | material | profile-specific | material through targeted re-entry/EXECUTE vs REQUALIFY | selective |
| SA-G12 positive continuity/no deny-all | material | material: permitted useful route must remain reachable | material: valid-continuity branch must execute | strong cross-family control |
| SA-G13 execution/compliance ownership declaration | material as external-owner boundary | normally N/A in abstract strategy model | material through broker/executor ownership | clean A/B boundary |
| SA-G14 reconstructability | material | material: auditable trajectory record | material: reconstructable Q0–Q6 trace | general |

The matrix demonstrates why the core catalog cannot use a universal “all 15 gates must pass” rule.

## 4. False-blocking defect found during this run

The first draft example treated SA-G03 as if it directly blocked SA-G04 and then implied that the same missing identity root blocked SA-G05 and SA-G09.

That contradicted the catalog's own typed graph:

- SA-G03 → SA-G04 was a non-blocking `supports` edge;
- identity was a `claim_requires` condition for the stronger `CLAIM-AUTHORITY-RESOLVED`, not a universal prerequisite for basic SA-G04 adjudication.

This has been corrected.

Current rule:

1. score `own_verdict` and level first;
2. only `requires` blocks basic gate adjudication;
3. apply `claim_requires` only to the named stronger claim;
4. `supports` never creates FAIL/CONDITIONAL;
5. report the stronger claim as conditional without rewriting the gate's own verdict.

This correction is important for R01 and AWS fixtures where identity may be frozen as an evaluator/configuration fact rather than a property under test.

## 5. Result model tested

The current result tuple is now:

```text
gate
  -> applicability
  -> test_role
  -> own_verdict
  -> specification level L0..L4
  -> required minimum level
  -> hard dependency status
  -> effective status
  -> root blocker(s)
  -> potential unlocks
  -> Stage A remediation
  -> Stage B handoff
  -> evidence ceiling
```

This supports the requested diagnostic form:

```text
Gate X: own PASS @ L3
Stronger claim: CONDITIONAL_ON(Gate Y)
If Gate Y reaches the frozen threshold, X/claim becomes adjudicable without that blocker.
No automatic PASS is inferred.
```

## 6. Automatic recommendation logic tested structurally

The catalog now contains generic Stage A remediation and Stage B realization hints for every SA-G00…SA-G14 gate.

The deterministic helper:

`gate-diagnostic/check_gate_profile.py`

is designed to:

- validate IDs, verdicts, levels and test roles;
- reject cycles in hard `requires` dependencies;
- derive gate effective status without treating `supports` as blocking;
- evaluate unconditional named-claim requirements;
- expose root blockers;
- show potential unlock relationships;
- build a Stage-B handoff queue without granting Stage-A credit.

The machine-readable result template is:

`DDS_STAGE_A_GATE_DIAGNOSTIC_RESULT_TEMPLATE_v0.1.json`.

Mechanical catalog validation on the current draft found:

- 15 core gate IDs;
- no unknown hard/support dependency reference;
- no hard-dependency cycle;
- all 15 gates contain a Stage A question, Stage A remediation hint and Stage B handoff hint.

## 7. What this run establishes

**Established at design/structural level:**

- the gate model is not tied to Hugging Face case IDs;
- the same gate vocabulary can represent an incident-derived family, a mathematical reduction and a conventional workflow technology profile without renaming their native mechanisms;
- NOT_APPLICABLE is necessary and can be used without automatic downstream failure when a substitute evaluator fact is preregistered;
- gate verdict, specification strength and dependency/claim status must remain separate;
- combinations of gates are best expressed through preregistered named claims rather than by making every conceptual relation a hard dependency;
- automatic audit recommendations can identify root specification gaps and Stage-B realization needs without asserting that remediation will pass.

## 8. What remains unvalidated

This run does **not** establish:

- completeness or uniqueness of SA-G00…SA-G14;
- independent reviewer agreement;
- empirical false-positive/false-negative rates of the dependency graph;
- that the remediation recommender improves a real architecture;
- any HF, R01 or AWS gate PASS/FAIL result;
- Stage B or Stage C evidence.

A result-producing candidate evaluation still requires a frozen applicable-gate profile, minimum levels, test roles, cases/falsifiers and acceptance wording.

## 9. Validation verdict

**Structural portability: PASS WITH LIMITS.**

The original false-blocking inconsistency was found and repaired. The current draft is coherent enough to be used for controlled gate-by-gate trial runs, but it should remain **draft** until at least one non-author/independent review and actual frozen result table are produced.

This is the correct stopping point for the generic Stage A design work: the instrument is defined and machine-readable; the next work is evidence generation, not more hidden redesign after outcomes.
