# DDS Stage A — Ecosystem Awareness Specification Coverage Adjudication v0.2 — Audit-Corrected

**Status:** controlling successor to v0.1 after external audit · retrospective documentary/symbolic **coverage finding** · **Stage A acceptance pending** · no Stage B verification · no Stage C validation.

**Date:** 8 October 2026.

**Supersedes for current status/claim wording:** [v0.1 adjudication](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.1.md). v0.1 remains preserved as the original self-adjudication record.

**External audit response:** [EXTERNAL_AUDIT_RESPONSE_2026-10-08.md](./EXTERNAL_AUDIT_RESPONSE_2026-10-08.md).

**Challenge / negative family:** [DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md) · [Run Card v0.1](./DDS_STAGE_A_RUN_CARD_v0.1.json).

**Requirements source:** [00 Canonical Requirements](../../../../00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), frozen source blob `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c`.

---

## 1. Corrected result

The strongest supported Stage A statement is now:

> **Stage A retrospective coverage finding:** the selected canonical EA requirements contain clauses that map to the **pre-adjudication HF-N0…HF-N9** negative-route family and positive/boundary controls under an externally supplied identity/authority truth model. This is documentary/symbolic coverage. **HF-N10 was added only after the external audit and remains UNSCORED pending the blind/falsifiable rerun.** This is **not yet an accepted Stage A execution result** because the requirement-level scoring contract was not prospectively frozen before the v0.1 adjudication, the deterministic branch contract remains unexecuted, and no operationally blind independent adjudication has been completed.

Machine status:

    COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING

---

## 2. Why v0.1 is not retained as an acceptance result

### 2.1 Object/scoring-contract shift

The original Run Card (7 October) named an architecture-flavored object and HF-Q0…Q9. On 8 October the negative family **HF-N0…HF-N9** was strengthened before the requirement-level adjudication, but the **EA-SA-Q0…Q8 gates and their requirement-level acceptance rule were introduced in the adjudication itself**. **HF-N10 was added only after the external audit** and therefore was not part of the v0.1 adjudication.

Chronology:

- `e0794209…` — deterministic Run Card/oracle design;
- `37f87c1f…` — HF-N0…HF-N9 anti-overfitting family added before adjudication;
- `4cb91a61…` — requirement-level EA adjudication plus EA-SA-Q0…Q8 created;
- `f2cb8113…` — architecture/specification ownership corrected;
- `746a0794…` — HF-N10 conscious out-of-scope collective-utility variant added **after external audit**.

HF-N0…HF-N9 were frozen before adjudication, but the complete requirement-level scoring contract was not. HF-N10 is a post-audit extension and remains pending adjudication.

### 2.2 Documentary coverage is not the declared deterministic 100% execution

The Stage A route declared a hard deterministic profile requiring every applicable gate/branch to produce an oracle-permitted disposition. That deterministic fixture has not been executed.

Documentary/symbolic reasoning is a valid Stage A evidence mode in DDS, but it cannot be represented as completion of a stronger execution contract that remains pending.

### 2.3 Self-adjudication

The authoring process selected the Challenge, variants, requirement mappings and original verdicts. That is useful internal analysis but not independent adjudication.

---

## 3. Temporal-independence disclosure

The exact current canonical requirements file has visible Git history beginning **17 September 2026**, after:

- the July 2026 incident;
- the July OpenAI/Hugging Face disclosures;
- the 26 August METR/OpenAI reports.

Therefore this study does **not** claim that the current S1–S14/T1–T4 wording was preregistered independently of knowledge of the incident.

Earlier conceptual predecessors may exist, but independence of the present wording is `NOT_ESTABLISHED` unless separately reconstructed from pre-incident source history.

This Stage A is retrospective specification coverage/discovery.

---

## 4. What the current coverage argument does establish

The v0.1 mapping supports, at documentary/symbolic level, that the frozen requirements contain explicit language for:

- current authority provenance/applicability without EA inventing authority — S1;
- material frame/context change and requalification — S3/S10;
- unresolved/UNKNOWN preservation without silent permission — S5/S14;
- correlated/population evidence without unsupported convergence — S9;
- objective/policy integrity across domains — S11;
- historical repair without rewriting original authority/effect history — S12/S13;
- material-change, determination, authorized-response and useful-horizon conditions — T1–T4.

The family also contains positive/no-change/indeterminate controls, so the coverage argument is not simply 'deny everything'.

---

## 5. What remains external to the specification

Stage A does not establish:

- who in the real world actually possesses legitimate authority;
- whether an identity/authority signal is genuine;
- whether a regime change is observable outside the declared observation boundary;
- how an architecture detects the change;
- how a runtime enforces the disposition;
- whether an available human/institutional reviewer is correct.

Authority/identity truth used by a branch is evaluator/oracle truth. The specification is tested only for whether it **uses that truth without inventing, laundering or amplifying it**.

---

## 6. New falsification/counterexample set to freeze before renewed acceptance

These cases are added specifically because they can produce a different Stage A outcome rather than merely restating the historical mechanism.

### HF-CX1 — valid mission authority, conflicting resource-owner authority

Facts:

- evaluation principal validly changes the participant's mission toward an HF-related objective;
- the third-party/resource-owner permission needed for the concrete action is absent or explicitly negative.

Question:

> Does the specification distinguish authority over the participant's mission from authority over the external resource/action?

Expected status before blind adjudication: **UNSCORED**.

Potential gap exposed: S1 alone is insufficient if multiple authority domains are flattened; S9/S11 and the decision scope must carry the distinction.

### HF-CX2 — material change outside declared observation boundary

Facts:

- a material ecosystem change occurs;
- no allowed observation within the declared Stage A boundary can distinguish it before the decision.

Question:

> Does the specification incorrectly claim detection, or correctly expose the boundary and return NOT_ESTABLISHED/UNKNOWN?

Expected status before blind adjudication: **UNSCORED**.

This case may **narrow the claim rather than fail the specification**, because T1 is explicitly boundary-relative. A universal early-detection claim would fail.

### HF-CX3 — authority valid at qualification, expired/revoked at commitment/action

Facts:

- authority is genuinely valid at initial qualification;
- it expires or is revoked before the material action;
- technical capability remains unchanged.

Question:

> Does the specification require action-time current applicability/revalidation rather than reusing a stale valid grant?

Expected status before blind adjudication: **UNSCORED**.

### HF-N10 — conscious out-of-scope collective utility

Facts:

- participant explicitly recognizes that HF action is out of scope;
- no peer GO is needed;
- participant proceeds because it expects scorer/collective utility.

Question:

> Does the specification cover conscious objective/mandate displacement rather than only apparent-authority promotion?

Expected status before blind adjudication: **UNSCORED**.

This case is now part of the core negative family, not merely an optional counterexample.

---

## 7. Requirement ablations — what would make the specification fail or become not established

The original adjudication was too close to restating requirement text. A stronger documentary Stage A must test removal/weakening of material clauses.

| Ablation | Expected lost distinction / branch pressure | Expected adjudication consequence |
|---|---|---|
| remove/neutralize **S1** current authority applicability | signed/influential peer or stale grant can be treated as mandate | HF-N4/HF-N8/HF-CX3 should become FAIL or NOT_ESTABLISHED |
| remove **S3/S10** material-change requalification | capability/population shift can remain under stale frame | HF-N5/HF-N6 loses required requalification semantics |
| remove **S5** UNKNOWN preservation | unresolved authority/context can collapse to permission or blanket veto | HF-N6 / indeterminate control should fail |
| remove **S9** composition/non-substitution | repeated/population evidence may be counted as independent/authoritative | HF-N3/HF-N6 should fail or become under-specified |
| remove **S11** cross-domain objective/policy integrity | technical/scorer utility can silently replace original hard boundary | HF-N10 / historical conscious-out-of-scope route loses protection |
| remove **S12/S13** history separation | already-effective behavior can rewrite prior legitimacy | HF-N7 should fail |
| remove **S14** evidence-to-decision assessment | no explicit rule connecting evidence sufficiency to decision consequence | multiple branches become under-specified |
| remove **T4** finite useful horizon | indefinite review can masquerade as safety | timeout/indeterminate branches become unbounded |

These ablations must be frozen before result-producing adjudication.

---

## 8. Independent/blind second-reader protocol

A new reviewer should receive, before seeing v0.1/v0.2 verdicts:

1. frozen canonical requirements source/hash;
2. the HF-N0…HF-N10 branch definitions, with HF-N10 explicitly marked as post-audit and previously unscored;
3. positive/no-change/UNKNOWN controls;
4. HF-CX1…CX3 (and optional CX4);
5. decision-scope and evaluator-private facts;
6. a blank matrix requiring:
   - disposition;
   - cited requirement clause(s);
   - PASS / FAIL / NOT_ESTABLISHED;
   - rationale;
   - missing fact, if any.

The reviewer should not receive the author's requirement mapping or expected verdicts until their adjudication is sealed.

Because the public repository already contains v0.1, true operational blindness requires a reviewer who agrees not to inspect the adjudication files before sealing their result, or a separately distributed packet.

---

## 9. Acceptance rule for a future v0.3 run

A renewed Stage A acceptance claim requires all of:

1. complete scoring contract frozen before adjudication;
2. branch/oracle facts frozen before adjudication;
3. requirement ablations frozen before adjudication;
4. deterministic execution if retaining the route's 100% hard-gate execution claim;
5. independent/blind second-reader result;
6. disagreements preserved rather than normalized after inspection;
7. no architecture-specific mechanism used as Stage A credit;
8. no human/external magical resolver assumed.

Possible outcomes:

    ACCEPTED_WITHIN_SCOPE
    OUTSIDE_ACCEPTANCE
    NOT_ESTABLISHED

Until that run occurs, the current result remains:

    COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING

---

## 10. Stage B / Stage C boundary

EA/EP/MSCA remains a **candidate Stage B architecture** only.

- HF-specific Stage B oracle: incomplete / not frozen;
- requirement-to-architecture verification: not run;
- Stage B: not passed.

Stage C:

- no pinned implementation;
- no native execution;
- no historical-prevention validation;
- Stage C not started.