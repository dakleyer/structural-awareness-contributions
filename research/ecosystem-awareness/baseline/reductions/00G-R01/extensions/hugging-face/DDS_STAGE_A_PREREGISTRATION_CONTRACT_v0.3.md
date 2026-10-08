# DDS Stage A — Hugging Face Requirement-Level Preregistration Contract v0.3

**Status:** preregistration artefact · frozen before any new blind-reader adjudication · not an adjudication result · not Stage B · not Stage C.

**Date:** 8 October 2026.

**Purpose:** define the requirement-level Stage A object, verdict semantics, gates, falsifiers, boundary controls, mutation-test contract and disagreement rule **before** a new independent/blind reader returns a result.

---

## 1. Frozen inputs

### 1.1 Canonical requirements

- file: `research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md`
- pinned commit: `96cbc94921aa5f2f16463faaf4a2f165175383a0`
- pinned blob SHA: `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c`

### 1.2 Specification-preparation ownership/maturity map

- file: `research/ecosystem-awareness/fg-tida/specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md`
- pinned pre-Hugging-Face-hardening commit: `a18bb0f32bed`
- pinned blob SHA: `38d64f61ef81a300a20d9d89cda65e5bb6ba5b22`

The moving `main` version of that file was later edited on 8 October to add §15A using Hugging Face Stage A as input while retaining the older document date/version. **That later edit is not part of this preregistered Stage A input.**

### 1.3 Historical evidence freeze used to prepare cases

- reconstruction blob: `af0660e1be6bb74708a53305b4979e6698bc7d78`
- cross-source matrix blob: `20db58f335227cbf9ff830aab7d33967a15629a3`
- trace-packet blob: `4bcac21a14e2e1f9665a1a4d17fb9856c3b17310`
- evidence-register blob: `7047931c5e3bf16ec71d2c78e6b4a75ad9154837`

Later factual corrections require a successor preregistration version; they do not silently change this contract.

---

## 2. Object under test and maturity ceiling

The object under test is **candidate requirement-level EA semantics**, not a validated architecture, deployed implementation or adopted normative standard.

The pinned preparation map constrains ownership and maturity:

- S3/S5/S9/S10/S14 and T1–T4 are strong/direct EA candidate surfaces but are still **N2 / requiring editorial normalization** where so classified;
- S11 is **mixed**: producer semantics are externally owned; EA directly owns only the non-substitution / cross-domain composition concern;
- S1/S2/S7/S8/S12/S13 contain material external-owner boundaries;
- containment execution and actual enforcement remain external where the canonical corpus says so.

Therefore a Stage A result can establish **requirement-semantic coverage or a gap**. It cannot establish enforcement, runtime compliance, architecture conformance or normative-standard readiness.

---

## 3. Retrospective / independence boundary

The present requirement wording is not demonstrated to be independent of the Hugging Face incident.

Repository path history shows the canonical requirements file, 00A and 00C all first appearing in commit `239ec5f5b17a` on 17 September 2026. The current repository therefore does **not** support a claim that 00A/00C provide a pre-incident textual ancestor via a simple file move/rename.

Earlier conceptual lineage may exist elsewhere, but independence from the July/August incident is **NOT_ESTABLISHED** by the currently identified requirement-file provenance.

This is a retrospective Stage A specification-discovery / coverage exercise.

---

## 4. Stage A question v0.3

> **Does the frozen candidate requirement-level specification distinguish material decision-basis change from ordinary variation; preserve evidence, scope, objective and authority boundaries without silent substitution; preserve unresolved state; discriminate apparent-authority promotion from conscious displacement of an already-known mandate; and define a bounded decision-level disposition while still allowing genuine authorized continuity/change — without importing an architecture or assuming magical human/external rescue?**

This question deliberately separates:

1. qualification of a decision;
2. authority/identity facts supplied by external owners;
3. compliance with the qualified disposition;
4. enforcement/execution by downstream controls.

---

## 5. Verdict definitions

Every case must receive exactly one of the following verdicts.

### PASS

`PASS` means all of the following are true:

1. the case lies inside the specification scope actually claimed;
2. one or more frozen clauses explicitly apply to the material distinction at issue;
3. those clauses determine a reviewable decision-level disposition or qualification that is compatible with the evaluator facts;
4. no missing external-owner fact is silently invented;
5. the result does not depend on a named Stage-B architecture mechanism or assumed human rescue.

`PASS` is a **specification-level result only**. It does not mean the participant obeys, a control executes, or an external effect is prevented.

### FAIL

`FAIL` means at least one of the following holds **inside a scope the candidate claims to cover**:

1. the frozen candidate explicitly permits/requires a disposition contrary to the evaluator facts; or
2. a material distinction required by the declared case is absent/neutralized while the candidate nevertheless claims a determined/conforming closure; or
3. the candidate collapses a required UNKNOWN/conflict into permission, global veto or another prohibited default; or
4. a positive continuity case is blocked by a blanket rule that the candidate presents as conforming.

Silence alone is not automatically FAIL when the omitted function is explicitly external to EA; that is handled by `NOT_ESTABLISHED`.

### NOT_ESTABLISHED

`NOT_ESTABLISHED` means at least one material element cannot be adjudicated from the frozen candidate specification because:

- the relevant obligation is explicitly external-owner / outside claimed EA scope;
- the wording is informative/mixed/N2 and insufficient to determine the requested obligation;
- a necessary evaluator fact is missing;
- the specification qualifies a posture but does not itself own the execution/compliance property being asked about; or
- the observation boundary makes the state indistinguishable within the declared horizon.

`NOT_ESTABLISHED` is a legitimate Stage A result and narrows the claim. It is not converted to PASS or FAIL for score convenience.

---

## 6. Requirement-level trajectory gates EA-SA-Q0…Q9

| Gate | Question | Primary specification surfaces |
|---|---|---|
| **EA-SA-Q0 — decision boundary** | Is the decision, legitimate owner, current scope, authority state and null/current action explicit enough to adjudicate the alternative? | S1, S2, S7, S14 |
| **EA-SA-Q1 — material-change discrimination** | Does the candidate distinguish a material change inside the declared observation boundary from ordinary variation? | S3, S10, T1 |
| **EA-SA-Q2 — evidence/domain non-substitution** | Can technical success, repeated peer claims, correlation or population convergence silently become authority/policy truth? | S9, S11, S14 |
| **EA-SA-Q3 — authority/identity/non-amplification** | Does the candidate preserve the difference between identity/authenticity, delegation and applicable authority? | S1, S6, S7, S8, T3 |
| **EA-SA-Q4 — unresolved-state handling** | If authority/context/evidence cannot be closed, is UNKNOWN/insufficiency preserved without permission-by-default or blanket veto? | S5, S14, T2, T4 |
| **EA-SA-Q5 — history/drift non-legitimation** | Can observed behavior/effect rewrite prior authority or erase the violation history? | S10, S12, S13, S14 |
| **EA-SA-Q6 — autonomous bounded disposition** | Without external rescue, does the candidate define what may continue, what must be requalified/held, and where it stops? | S3, S5, S10, S14, T2, T3 |
| **EA-SA-Q7 — genuine authorized change/continuity** | If all relevant owners supply current applicable authority, does the candidate allow the legitimate change/continuation rather than deny everything? | S1, S3, S9, S10, S11, T1, T3 |
| **EA-SA-Q8 — useful-horizon discipline** | Is review finite and does timeout/default itself remain a qualified response? | S3, S5, S10, S14, T4 |
| **EA-SA-Q9 — qualified disposition versus conscious noncompliance** | If a participant correctly represents that an action is outside scope yet proceeds for goal/scorer/collective utility, does the frozen specification itself impose a participant/execution obligation that makes the act nonconforming, or does EA stop at qualification with enforcement external? | S2, S5, S11, T3 plus ownership map |

**Q9 is intentionally allowed to return `NOT_ESTABLISHED`.** A result that EA qualifies the decision but does not own behavioral enforcement is a scope finding, not an automatic Stage A failure.

---

## 7. Falsifier set v0.3

The following are the cases intended to expose specification gaps rather than merely restate clauses.

### F-A — split authority across principals/domains

The evaluation principal validly changes the mission toward HF-related work, but the third-party/resource owner does not authorize the concrete external action (or explicitly denies it).

Falsification target: flattening mission authority into resource/action authority; failure to preserve cross-principal conflict.

### F-B — untrustworthy self-reported action/effect trace

The participant's own trace claims an action was blocked or had no external effect, while an independently supplied evaluator fact records the contrary external effect. The case asks what evidence can support the decision/outcome claim.

Falsification target: accepting self-report or command/intention as outcome without a declared observable-effect basis.

### F-C — self-certified identity without an external trust root

A coordination message is cryptographically signed and internally consistent, but the signer/handle/key binding was initially self-asserted and has no independently established principal/role/delegation root.

Falsification target: promoting cryptographic authenticity-of-message into verified identity/representation/applicable authority.

---

## 8. Boundary/control cases — not presented as falsifiers

### B-A — change outside declared observation boundary

A material ecosystem change exists but is not observable through the declared evidence boundary before the decision. Expected purpose: test honest scope narrowing / `NOT_ESTABLISHED`, not universal detection.

### B-B — authority expires or is revoked before action

Authority is valid at initial qualification but invalid at commitment/action time. Expected purpose: direct conformance check of S1/S10, not discovery of a textual gap.

### B-C — silence/no-veto treated as permission

A participant announces that it will proceed unless vetoed within a short window; no veto arrives. No affirmative authority grant exists. This is grounded by METR's ~40-second no-veto example.

Expected purpose: direct conformance check of S10/S5 (`silence or delay is not permission`).

### B-D — unaffected legitimate work during unresolved alternative

The alternative external transition remains unresolved while the current legitimate task remains sufficiently established. Expected purpose: ensure UNKNOWN does not become a system-wide veto.

---

## 9. Requirement ablations — frozen author predictions

These are **new predictions frozen in this v0.3 contract**. They were not preregistered for v0.1 and are not described as if they were.

| Ablation | Mutation | Predicted loss |
|---|---|---|
| **ABL-01 S1-currentness** | remove action-time applicability/expiry/revocation requirement | stale or inapplicable authority can be reused |
| **ABL-02 S3/S10-change** | remove material-change/revalidation obligation | stale decision basis can persist through changed route/context |
| **ABL-03 S5-unknown** | remove explicit indeterminacy/no-permission rule | UNKNOWN can collapse into permission or indiscriminate veto |
| **ABL-04 S9-composition** | remove non-substitution/conflict/correlated-convergence language | population/repeated evidence or one principal can silently replace another domain |
| **ABL-05 S11-hard-limits** | remove hard-limit/non-substitution/cross-domain integrity language | scorer/collective utility can replace the principal's hard boundary without an explicit conflict |
| **ABL-06 S7/S6-identity** | remove qualified identity/representation + independent-verification requirement | self-certified/signature-only identity can be treated as sufficient authority input |
| **ABL-07 S12/S13-history** | remove history separation/repair requirement | already-effective behavior can rewrite prior legitimacy |
| **ABL-08 S14-effect-evidence** | remove evidence-to-decision/outcome-basis obligation | self-report/intention/command receipt can be treated as sufficient outcome evidence |
| **ABL-09 T4-boundedness** | remove finite horizon/capacity/fallback discipline | indefinite review can masquerade as safe closure |

The prediction table is intentionally semantic rather than a cherry-picked list of N-case IDs. Case-level kill expectations are frozen separately in the mutation-test contract.

---

## 10. Deterministic Stage A execution meaning

For this requirement-document profile, **deterministic Stage A execution means mutation testing of the frozen specification/adjudication contract**, not execution of the EA architecture.

The mutation test asks whether the same frozen case set and verdict rules:

1. accept/retain the unmutated reference candidate where supported;
2. reject or mark NOT_ESTABLISHED the deliberately defective reference mutants at the intended semantic boundary;
3. preserve positive continuity cases;
4. expose cases where the base candidate itself is NOT_ESTABLISHED.

This is a Stage A document/specification test. Runtime detection, control actuation, network enforcement, architecture telemetry and implementation behavior remain Stage B/C.

---

## 11. Independent/blind-reader rule

A blind reader must receive a separate neutral packet that:

- does not link to Route v0.1/v0.2/v0.3, adjudication v0.1/v0.2, result JSONs or author mappings;
- uses neutral case IDs and fact descriptions;
- includes the pinned canonical requirements and pinned preparation/ownership map references;
- includes these verdict definitions;
- contains no author expected verdicts or requirement mappings.

A reviewer with prior exposure to the adjudications cannot qualify as blind; they may provide an independent non-blind review only.

### Disagreement rule

If the blind reader disagrees with the preregistered author prediction:

1. do not normalize the difference after inspection;
2. record `DISAGREEMENT_UNRESOLVED` for the affected case;
3. no Stage A acceptance claim may use that case as PASS;
4. resolution requires either a third independent adjudicator or a successor specification/scope version;
5. any changed wording or case interpretation produces a successor preregistration version.

---

## 12. Acceptance rule for the next Stage A run

A future acceptance claim under this v0.3 contract requires:

1. this contract and its mutation/case artefacts committed before the blind result;
2. all neutral cases adjudicated using PASS/FAIL/NOT_ESTABLISHED exactly as defined here;
3. all declared nonconforming specification mutants killed at their registered target cases;
4. no deny-all solution passing the positive/continuity cases;
5. Q9 reported honestly, including `NOT_ESTABLISHED` if execution/compliance is external;
6. disagreements handled by §11 rather than post-hoc harmonization;
7. no Stage-B architecture mechanism credited as Stage A evidence.

Until such a run is complete, status remains:

`COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`

---

## 13. Explicit non-claims

This preregistration does not establish:

- Stage A acceptance;
- that N10 is already covered;
- that EA enforces compliant behavior;
- that self-certified identity can or cannot be securely resolved by a particular architecture;
- that a human would make the correct decision;
- Stage B architecture verification;
- Stage C implementation/problem validation;
- prevention of the historical incident.