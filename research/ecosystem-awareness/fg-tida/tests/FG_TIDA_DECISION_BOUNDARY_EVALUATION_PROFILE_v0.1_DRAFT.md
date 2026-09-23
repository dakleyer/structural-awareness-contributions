# FG-TIDA Decision Boundary Evaluation Profile — v0.1 Draft

> **FG-TIDA application profile — working draft.** This document projects the programme-independent [Decision Boundary Challenge v0.2](../../DECISION_BOUNDARY_CHALLENGE_v0.2.md) into the FG-TIDA application package. It defines a cross-theme test/conformance route for decision-boundary behavior. It does **not** create a new FG-TIDA Theme, verdict vocabulary, authority model, product ranking, Working Group deliverable or adopted specification.

| | |
|---|---|
| **ID** | FG-TIDA-DBC-01 |
| **Version · date** | v0.1-draft · 23 September 2026 |
| **Status** | Test/conformance preparation; no executed result |
| **General source** | [Decision Boundary Challenge v0.2](../../DECISION_BOUNDARY_CHALLENGE_v0.2.md) |
| **Specification route** | [EA / FG-TIDA Specification Preparation v0.3 Draft](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md) |
| **Initial semantic fixture** | [FG-TIDA Use Case #6](https://github.com/FG-TIDA/use-cases/issues/6) |
| **Initial executable host candidate** | [FG-TIDA Use Case #4](https://github.com/FG-TIDA/use-cases/issues/4) |
| **Evidence rule** | Rank evidence strength, not vendors; preserve native Theme semantics |

---

## 1. Purpose

FG-TIDA contains several independently owned mechanisms that can all affect one operational decision:

- authority provenance and applicability;
- policy / intent / conformance verdicts;
- appraisal and rejection semantics;
- ecosystem signalling and affected-scope state;
- human-oversight authority/capacity/intervention state;
- population-level evidence;
- execution and return-to-operation state.

The profile asks a narrow integration question:

> **When those independently owned outputs meet at a decision boundary, are their meanings preserved, are authority and actuation kept separate, and is the next step testable without inventing a common hidden ontology?**

This profile is therefore a **cross-theme integration test**, not a proposal to make every Theme implement Ecosystem Awareness internally.

---

## 2. Non-negotiable semantic rule

Producer-native results remain producer-native.

The general EA [UC-EA-02 Native-semantic preservation rule](../../baseline/UC-EA-02_v0.6_MAINTENANCE_FREEZE.md) applies unchanged. For example, Theme #6 verdicts such as PERMIT, REMEDIATE, BLOCK, ESCALATE or INDETERMINATE are carried with their issuer, scope and reference semantics; they are not translated into DBC dispositions, Type classes or P1/P2/P3.

The profile keeps five layers separate:

1. **producer-native result**;
2. **Type 0/1/2/NOT_ESTABLISHED**;
3. **P1/P2/P3 posture**;
4. **DBC procedural disposition**;
5. **AuthorityResponse**.

The shared word **ESCALATE** is namespaced when it appears in more than one layer.

---

## 3. Initial FG-TIDA test route — UC-6 first, UC-4 second

The 23 September public discussion now provides a bounded integration path.

### Stage 0A — UC-6 semantic reference

Use Case #6 remains the source of facts and authority-applicability outcomes.

The controlled comparison holds constant:

- Agent A / identity A1;
- grant G1;
- action Q1;
- document set D1;
- recipient U1;
- human reviewer H / authority H1;
- jurisdiction, human-input authenticity and oversight capacity.

Only the declared purpose changes:

- **A — product planning:** G1 remains applicable;
- **B — sales-campaign preparation:** G1 remains in existence but is inapplicable to the new purpose.

The fixture must preserve the distinction between:

- grant provenance;
- current applicability;
- human continuation approval;
- authority to create/expand a grant;
- execution/continuation outcome.

### Stage 0B — Theme #13 matrix annotation

The current public proposal is to apply the v0.2 operational-risk / response-window / epistemic-opportunity matrix to branches A and B.

The worked mapping should identify, field by field:

- actual input;
- source/owner;
- native type or unit;
- derived relation where applicable;
- threshold/rule where applicable;
- structured state where dimensions are not commensurable;
- expected output;
- N/A fields;
- unresolved mappings.

Additional timing variation should be recorded as a separate branch rather than silently modifying the base UC-6 facts.

### Stage 0C — Theme #16 boundary annotation

Against the same UC-6 facts, annotate:

- received authority determination;
- available intervention options;
- human decision;
- separate execution/continuation outcome.

For the base fixture:

- human-input authenticity remains constant;
- oversight capacity remains sufficient;
- H1 approval cannot expand G1;
- no capacity-failure scenario is introduced unless a separate branch explicitly adds it.

Where the current four-part human-review output is used, it should be mapped only where its semantics are supported; no invented confidence score is required.

### Stage 0D — semantic review and freeze

Before executable implementation:

- UC-6 contributor validates case facts and expected authority-applicability outcome;
- matrix contributors validate their mappings;
- semantic owners validate any Theme-owned fields;
- open mappings remain explicit;
- version and adapter scope are frozen.

### Stage 1 — bounded UC-4 executable profile

The current public proposal from Nelson is to implement the reviewed example as a bounded, versioned UC-4 profile containing:

- mapping;
- fixtures;
- traces;
- expected outcomes;
- report against agreed expectations;
- version-pinned adapter.

UC-4's federated signal, corroboration and containment work remains the testbed core. The UC-6 exercise is one imported interface profile, not a rewrite of UC-4.

---

## 4. Candidate contributor / owner map

This table records the current public discussion. It does not assign work or transfer ownership.

| Test object | Current public source / candidate responsibility |
|---|---|
| UC-6 facts and authority-applicability outcomes | Arpita Sarker / UC-6 source |
| Operational-risk / response-window / epistemic-opportunity mapping | Oleksii / Theme #13 matrix contribution, subject to review |
| Human-oversight/intervention annotation | Theme #16 matrix contributors, subject to review |
| DBC cross-theme test semantics and traceability | EA/DBC contribution; no redefinition of Theme outputs |
| UC-4 executable mapping, fixtures, traces and report | Nelson's proposed role after scope/effort agreement |
| UC-4 adapter boundary and testbed-core integrity | UC-4 maintainer/contributors |
| Theme #13 architectural placement/scope | Theme #13 owner/contributors through the FG-TIDA process |
| Final FG-TIDA disposition | Relevant FG-TIDA Working Group / Focus Group process, not this document |

---

## 5. Cross-theme test record

A test vector should preserve, where applicable:

~~~text
fixture
  source_use_case
  source_version
  branch
  frozen_facts
  frozen_authority
  response_horizon

producer_native
  owner/theme
  issuer
  result
  scope
  reference/profile
  unknown_qualifiers

qualification
  validity_time
  freshness
  provenance
  dependency
  residual
  type_class

posture
  P1 | P2 | P3

decision_boundary
  CAN
  KNOW
  MAY
  SHOULD
  dbc_disposition

human_oversight
  authority
  available_options
  decision
  capacity_state

authority
  current_grant
  applicability
  RepositionIntent
  AuthorityResponse

execution
  attempted
  confirmed
  continuation_or_return_state

burden
  elapsed_time
  messages
  external_calls
  human_review
  disclosure
~~~

Not every fixture must populate every field. Missing/non-exercised fields remain explicit N/A or UNKNOWN as appropriate.

---

## 6. Comparison and challenger method

For comparative work, use the general DBC-R0…R3 arms:

- **DBC-R0 Native**;
- **DBC-R1 Strong control**;
- **DBC-R2 Instrumented**;
- **DBC-R3 Sidecar** where admitted.

A strong peer must have the best materially relevant native controls enabled. For a claim beyond descriptive evidence, seek a **comparator defender/challenger** rather than allowing the EA/DBC proposer to define a weak alternative.

A comparative profile should record:

- candidate owner;
- comparator defender/challenger;
- semantic owner(s);
- fixture owner;
- test maintainer;
- adjudicator/reviewer;
- frozen configuration envelope;
- unresolved objections before execution.

If no external defender exists, the run remains useful but the evidence ceiling is lower.

---

## 7. Measures

The FG-TIDA profile uses per-measure rates and structured outcomes, not one composite score.

### Core integrity

- unauthorized execution rate;
- stale-basis use rate;
- false-closure rate;
- native-semantic translation error;
- namespace-collision error;
- contextual-inapplicability misclassification.

### Boundary / recovery

- targeted requalification success;
- qualifier-survival rate;
- unnecessary escalation rate;
- decision-survival rate;
- approved-beneficial-transition rate where a legitimate transition path exists;
- authority-response latency;
- execution-confirmation / return-to-operation correctness.

### Continuity

- nominal continuity pass;
- false containment/migration;
- unnecessary human intervention;
- unnecessary requalification.

### Burden / accountability

- elapsed time;
- messages/handoffs;
- tool/model/external calls;
- human-review demand;
- disclosure burden;
- reconstruction time/error;
- reviewer disagreement.

No safety failure may be averaged away by a utility gain.

---

## 8. Evidence ladder

Use the DBC evidence ladder rather than a vendor score:

| Level | Meaning in the FG-TIDA profile |
|---|---|
| **DBC-EL0** | semantics/fixture/falsifiers defined |
| **DBC-EL1** | deterministic fixture executed reproducibly |
| **DBC-EL2** | cross-theme mapping validated by semantic owners |
| **DBC-EL3** | matched challenger comparison executed |
| **DBC-EL4** | independently governed / cross-implementation interoperability demonstrated |
| **DBC-EL5** | independently replicated or bounded external/industrial applied evidence |

This ladder measures **evidence strength**, not architecture quality.

---

## 9. Immediate executable package

A first bounded package should contain:

1. UC-6 branch A fixture;
2. UC-6 branch B fixture;
3. branch A + human approval;
4. branch B + human approval;
5. machine-readable expected outcomes;
6. field-by-field Theme #13 matrix mapping;
7. Theme #16 annotation;
8. source-owner sign-off / unresolved-field register;
9. adapter mapping into UC-4;
10. deterministic trace and report.

Only after the base package is stable should new branches add:

- validity-time / response-time divergence;
- insufficient evidence;
- authority expiry/revocation;
- human-capacity failure;
- cross-domain propagation;
- hostile signal classes.

This prevents one fixture from silently testing six different failure mechanisms.

---

## 10. Falsifiers / negative evidence

The profile must report results that count against the proposed DBC/EA contribution, including:

- UC-4/native strong controls already preserve the tested distinctions at equal or lower burden;
- the DBC mapping requires translation of Theme-owned semantics;
- the profile cannot distinguish authority existence from applicability;
- human approval is incorrectly promoted into grant expansion;
- instrumentation introduces materially more HOLD/escalation in valid-continuity cases;
- the adapter cannot preserve expected semantics without reproducing another Theme internally;
- source contributors reject the interpretation;
- cross-implementation mapping is not reproducible;
- the same result cannot be reconstructed by an independent reviewer.

---

## 11. Specification disposition

In the current [EA / FG-TIDA Specification Preparation v0.3 Draft](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md), this profile should enter initially as:

> **T — Test/conformance only**

It may support future conformance requirements, but it is not itself evidence that DBC dispositions, the DBC evidence ladder or the complete profile are normative FG-TIDA semantics.

The preferred future home, if a WG chooses to carry it, is the **EA-CONF / cross-theme conformance and decision-boundary evaluation** layer rather than the core EHD wire semantics or a Theme-specific authority model.

---

## 12. Public discussion anchors

- Theme #13 — Iván's UC-6 deterministic-test proposal: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5798563483
- Theme #13 — Nelson's bounded UC-4 executable-profile proposal: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5802619701
- Theme #16 — Nelson's common UC-6 cross-interface mapping proposal: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803023066
- FG-TIDA UC-6: https://github.com/FG-TIDA/use-cases/issues/6
- FG-TIDA UC-4: https://github.com/FG-TIDA/use-cases/issues/4

---

## 13. Claim boundary

This draft establishes only a proposed test/conformance route.

It does not establish that:

- FG-TIDA has adopted DBC;
- UC-4 maintainers have accepted the implementation scope;
- the Theme #13 or #16 matrices have completed semantic review;
- any implementation has passed;
- a DBC-EL level has been achieved beyond what an executed record demonstrates;
- an FG-TIDA Working Group owns this profile;
- one vendor/system is better than another.

**Status:** working FG-TIDA application/test profile; unexecuted; source-owner review and executable-profile agreement remain pending.
