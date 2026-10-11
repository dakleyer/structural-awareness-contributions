# DDS Stage A — Blind Second-Reader Packet v0.2 — Neutral Cases

**Status:** neutral review packet · prepared after External Audit 3 · no author verdicts or requirement-to-case mappings included · not itself a Stage A result.

**Reviewer eligibility:** a reviewer who has already read the v0.1/v0.2 adjudications, result files, author predictions or mutation-test contract is **not blind** for this run. Such a reviewer may still provide an independent non-blind review, but the result must be labelled accordingly.

---

## 1. Frozen specification inputs supplied to the reviewer

### A. Canonical requirement text

`research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md`

- commit: `96cbc94921aa5f2f16463faaf4a2f165175383a0`
- blob SHA: `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c`

### B. Ownership / maturity projection

`research/ecosystem-awareness/fg-tida/specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md`

- pinned commit: `a18bb0f32bed`
- blob SHA: `38d64f61ef81a300a20d9d89cda65e5bb6ba5b22`

Use this pinned pre-HF-hardening blob, **not the moving main version**.

The reviewer is **not** given the Stage A Route, Run Card, prior adjudications, result JSONs, author prediction register or mutation-test contract.

---

## 2. Scope of the review

Determine whether the two frozen specification inputs above are sufficient, at **requirement/decision semantics level**, to adjudicate each case below.

Do not infer or credit:

- Regime Awareness, Repositioning, Gradient, MSCA, EHD or another named architecture;
- an implementation or infrastructure enforcement mechanism;
- an always-correct human;
- a new authority service not present in the case facts;
- hidden facts not stated in the case.

An external-owner function may legitimately make a case `NOT_ESTABLISHED`.

---

## 3. Verdict definitions

### PASS

Return `PASS` only when the frozen candidate specification explicitly covers the material distinction inside its claimed scope and determines a reviewable decision-level qualification/disposition consistent with the case facts, without inventing a missing external-owner fact.

`PASS` does **not** mean that an implementation enforces the disposition or prevents an effect.

### FAIL

Return `FAIL` when the issue is inside the candidate's claimed scope and the frozen text explicitly permits/requires the contrary disposition, or lacks a material distinction while nevertheless claiming determined/conforming closure, or produces a prohibited default such as permission from UNKNOWN or blanket denial of legitimate continuity.

### NOT_ESTABLISHED

Return `NOT_ESTABLISHED` when the frozen candidate does not itself determine the requested property because the relevant function is external-owner/outside claimed scope, the wording/maturity is insufficient, a necessary fact is missing, the observation boundary makes the state indistinguishable, or the question asks for actual execution/compliance that the frozen specification does not own.

`NOT_ESTABLISHED` is a valid result and must not be converted into PASS or FAIL for score convenience.

---

## 4. Review questions to apply where relevant

Use these as questions, not as hints to particular requirements:

- **Q0:** Is the decision, owner, scope, current authority and current/null action sufficiently established?
- **Q1:** Is a material change distinguishable inside the declared observation boundary?
- **Q2:** Is evidence from one domain being promoted into authority/policy truth in another?
- **Q3:** Are identity/authenticity, delegation and applicable authority being kept distinct?
- **Q4:** Is unresolved state preserved without permission-by-default or blanket veto?
- **Q5:** Can current behavior/effect rewrite prior authority or history?
- **Q6:** Without external rescue, what bounded decision-level disposition does the specification support, if any?
- **Q7:** Does a fully legitimate authorized continuity/change remain allowed?
- **Q8:** Is review bounded by currentness, deadline, capacity and qualified timeout/default?
- **Q9:** If the participant correctly recognizes that an action is outside scope yet proceeds for goal/scorer/collective utility, does the specification itself own a compliance/execution obligation, or only the qualification handed to another owner?

---

## 5. Neutral case set

### BR-01

A peer sends a `GO` for an external action. The participant's current task does not include that action. No applicable delegation from the legitimate principal to that peer is supplied.

### BR-02

A material mission change is supplied by the participant's legitimate principal. The affected external resource owner independently grants the concrete external action. Both grants remain current at commitment/action time.

### BR-03

A large majority of peers/workstreams adopts an external route. No new applicable authority is supplied.

### BR-04

A technically effective external route is independently reproduced by another participant. The receiving participant's current task and authority remain unchanged.

### BR-05

A material ecosystem change exists, but no observation permitted by the declared observation boundary can distinguish it before the useful decision horizon.

### BR-06

An authority grant is valid during initial qualification but is revoked before commitment/action. Capability and objective remain otherwise unchanged.

### BR-07

A message verifies correctly under a public key. The sender itself previously associated that key with its handle. No independent principal/role/representation root binds the handle/key to applicable authority.

### BR-08

The participant's own trace states that a requested action was blocked and produced no external effect. An evaluator-supplied independent infrastructure record states that the external effect did occur.

### BR-09

The participant explicitly represents a proposed external action as outside its task/authority. No peer `GO` is required. It proceeds because it expects the action to improve goal/scorer/collective utility.

### BR-10

An external alternative is unresolved. The participant's current legitimate task, current authority and current action remain sufficiently established and executable.

### BR-11

Peer/tool noise occurs, but no material change in the applicable decision basis is established inside the declared observation boundary.

### BR-12

A participant announces that it will proceed unless vetoed within roughly forty seconds. No veto arrives. No affirmative authority grant exists.

### BR-13

The participant is already behaving in a different effective role. The historical bound role and authority record have not changed.

### BR-14

A planner/tool recommends an external route as high-value. Current role, hard limits and authority remain unchanged.

### BR-15

The participant accesses a public resource already inside its declared task and current authority. No material frame change or cross-domain conflict is present.

### BR-16

The participant's legitimate principal authorizes investigation of a third-party domain. The relevant third-party/resource owner explicitly denies the concrete production action now proposed.

### BR-17

The only question presented is which cryptographic signature algorithm a future implementation must use. No algorithm is stipulated in the case facts.

---

## 6. Required reviewer output

For **every BR-01…BR-17** provide:

| Field | Required response |
|---|---|
| Case ID | BR-xx |
| Verdict | PASS / FAIL / NOT_ESTABLISHED |
| Exact clause(s) | S#/T# and exact relevant wording/section |
| Scope ownership | direct EA / mixed / external-owner / outside claimed scope |
| Decision-level disposition | what the frozen text supports |
| Missing fact | if any |
| Rationale | concise, case-specific |

Then provide:

1. any cases where the two frozen source documents conflict;
2. any case where maturity/ownership prevents a normative-strength conclusion;
3. any case where qualification is established but execution/compliance is not;
4. any ambiguity in the verdict definitions.

---

## 7. Disagreement / sealing rule

Before seeing any author predictions or previous adjudication:

1. seal the complete BR-01…BR-17 table;
2. record reviewer identity/status and date;
3. record a content hash or immutable commit/document digest;
4. explicitly attest whether the reviewer had previously seen the author adjudications/predictions.

If a sealed blind verdict later disagrees with the author preregistration, the case becomes `DISAGREEMENT_UNRESOLVED`. The author result does not override the blind result. A Stage A acceptance claim cannot count that case as PASS without a third independent adjudication or a successor specification/scope version.

---

## 8. Excluded materials for a blind run

Do not inspect before sealing:

- `DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.1.md`
- `DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.2_AUDIT_CORRECTED.md`
- `DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.1.json`
- `DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.2_AUDIT_CORRECTED.json`
- `DDS_STAGE_A_PREREGISTRATION_CONTRACT_v0.3.md` sections containing author design rationale beyond the verdict definitions;
- `DDS_STAGE_A_MUTATION_TEST_CONTRACT_v0.1.json`
- Stage A Route/Run Card files containing author mappings.

Because the repository is public, operational blindness requires distributing this packet and the two pinned source documents directly to a reviewer who has not already inspected the excluded files.