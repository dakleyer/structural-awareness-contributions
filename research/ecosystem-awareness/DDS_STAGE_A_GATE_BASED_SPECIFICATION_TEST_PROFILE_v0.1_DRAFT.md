# DDS Stage A — Gate-Based Specification Test Profile v0.1 Draft

**Status:** design draft for DDS Stage A · specification-level model-based test instrument · programme-independent · not a Stage A result · not Stage B architecture verification · not Stage C implementation validation.

**Purpose:** define a reusable Stage A instrument that can evaluate **any candidate specification/framework** gate by gate and return a diagnostic profile rather than a single undifferentiated PASS/FAIL.

**Relationship to existing DDS:** this is a candidate refinement/supplement to [DDS Stage A — Specification Discovery](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). It does not modify the current canonical Stage A method until separately reviewed/promoted.

---

## 1. Design objective

Stage A tests **specifications**, not architectures.

The specification under test is the measured object. The Stage A test instrument owns:

- the gate catalogue;
- gate semantics;
- gate maturity levels;
- verdict semantics;
- dependency rules;
- case-to-gate activation;
- specification-level mutation tests;
- aggregation/claim-ceiling rules; and
- diagnostic recommendations.

A scenario such as Hugging Face, 00E, 00F, DAOS or another future case provides **fixtures that exercise gates**. A scenario does not define the gates.

A technology or architecture may later realize some or all of the same properties. That is Stage B.

---

## 2. Stage A output is a profile, not one global PASS

For a specification `Spec`, Stage A returns:

    Profile_A(Spec) = { GateResult(G1), GateResult(G2), ... GateResult(Gn) }

Each gate result contains:

- applicability;
- maturity level 0–4;
- PASS / FAIL / NOT_ESTABLISHED / OUT_OF_SCOPE;
- dependencies;
- conditional blockers;
- evidence/source anchors;
- exercised cases;
- ablation/mutant sensitivity; and
- recommended minimum closure where applicable.

A global acceptance statement is allowed only for a **declared claim/profile** that specifies which gates are mandatory and what minimum level each gate requires.

No universal numeric score is required or preferred.

---

## 3. Gate maturity levels

The level measures the strength of the **specification text**, not implementation quality.

| Level | Meaning | Minimum evidence in the specification |
|---:|---|---|
| **L0 — Absent** | property is not represented | no usable statement |
| **L1 — Descriptive** | property is mentioned or desired | informative prose only; no binding obligation |
| **L2 — Normative but unscoped** | specification imposes an obligation but scope/owner/decision boundary is incomplete | MUST/SHALL-equivalent semantics or unmistakable normative requirement |
| **L3 — Scoped and owned** | obligation is normative and declares material scope, owner/source/receiver boundary and relevant conditions | enough information to know **where and to whom** it applies |
| **L4 — Testable** | specification defines a decision boundary sufficiently precisely to admit positive, negative and indeterminate cases | observable pass/reject/UNKNOWN consequence can be adjudicated without inventing architecture |

`L4` does **not** mean that an implementation has passed. It means the specification is testable at Stage A.

---

## 4. Verdict semantics

### PASS

A gate is `PASS` when:

1. it is applicable to the declared claim/case;
2. the specification reaches the required minimum level for that gate;
3. all mandatory dependency gates satisfy their required levels; and
4. the specification does not contain a conflicting rule that defeats the property.

### FAIL

A gate is `FAIL` when it is applicable and at least one of the following is true:

- the property is absent below the required level;
- the specification explicitly permits the prohibited transition;
- the specification collapses a required distinction;
- a required dependency is explicitly contradicted rather than merely unknown; or
- a frozen mutation/counterexample demonstrates that the gate cannot produce the required distinction.

### NOT_ESTABLISHED

A gate is `NOT_ESTABLISHED` when the available specification/evidence cannot support either PASS or FAIL without inventing missing semantics, ownership, scope or external truth.

`NOT_ESTABLISHED` is not PASS and is not automatically FAIL.

### OUT_OF_SCOPE

A gate is `OUT_OF_SCOPE` when the specification explicitly excludes that responsibility and identifies the external owner/interface.

The claim/profile then decides whether that exclusion is admissible. An allowed exclusion narrows the claim; it does not silently count as PASS.

### CONDITIONAL

`CONDITIONAL_ON(Gx, ...)` is a diagnostic state, not a fifth terminal verdict.

It means the target gate has sufficient local specification text but cannot reach PASS until one or more prerequisite gates or externally declared facts are established.

Until those prerequisites close, the terminal result is normally `NOT_ESTABLISHED` for the broader claim.

---

## 5. Generic Stage A gate catalogue

The gates below are **property gates**. They are intentionally not named after Hugging Face, EA modules, products or one implementation.

### G-A01 — Decision / scope binding

**Property:** the specification binds each material decision to an explicit subject, scope, owner/principal or declared decision domain, rather than allowing the newest context to silently redefine the decision.

**Typical failure:** mission/scope changes by recency, convenience or contextual drift.

**Current EA anchors:** S2, S11, S14.

### G-A02 — Authority provenance, applicability and domain

**Property:** authority must identify origin, subject, purpose/action, scope/domain, standing and applicability. Authority over one participant or mission must not silently become authority over a different resource/domain.

**Typical failure:** valid mission authority is treated as permission over a third-party resource; coordinator identity is treated as mandate.

**Current EA anchors:** S1, S8, S9.

### G-A03 — Identity / representation grounding

**Property:** the specification distinguishes asserted identity, authenticated identity, represented principal/role and current representation relationship. Self-description or behavioural similarity cannot establish the required identity/authority relation.

**Typical failure:** self-certified handle/signature or similar output becomes trusted principal identity.

**Current EA anchors:** S7, S1.

### G-A04 — Material-change discrimination within a declared observation boundary

**Property:** the specification requires a declared observation/coverage boundary and distinguishes material decision-basis change from ordinary variation inside that boundary.

**Typical failure:** every deviation is a regime change; or a universal detection claim is made without declared observability.

**Current EA anchors:** S3, S10, T1.

### G-A05 — Evidence-to-decision qualification

**Property:** evidence is tied to the proposition/decision it actually supports, with sufficiency/insufficiency/inconclusive state explicit.

**Typical failure:** technical feasibility is promoted into permission, or an alert/confidence score is treated as a decision.

**Current EA anchors:** S14, T2.

### G-A06 — UNKNOWN / insufficiency preservation

**Property:** missing, stale, conflicting or unavailable qualification remains explicit and cannot silently become permission.

**Typical failure:** `UNKNOWN -> ALLOW` by default.

**Current EA anchors:** S5, S14, T2.

### G-A07 — Non-substitution / correlated-convergence control

**Property:** repeated, imitated, correlated or population-level agreement cannot silently substitute for an independently required authority, policy or evidence dimension.

**Typical failure:** many peers doing something is treated as independent evidence or mandate.

**Current EA anchors:** S9, S11, S14.

### G-A08 — Objective / policy / hard-limit integrity

**Property:** a new objective, scorer utility, peer utility or lower-priority preference cannot silently overwrite a principal-owned hard limit or declared mission boundary.

**Typical failure:** participant knows an action is outside scope but collective/local utility displaces the mandate without a legitimate change.

**Current EA anchors:** S2, S11.

### G-A09 — Temporal validity, expiry, revocation, silence and default

**Property:** previously valid authority/policy is rechecked where material at commitment/action time; expiry/revocation is respected; silence, delay or timeout is not permission unless explicitly defined as an authorized response.

**Typical failure:** stale grant reuse; countdown with no veto becomes consent.

**Current EA anchors:** S1, S10, S5.

### G-A10 — Historical non-rewrite and repair integrity

**Property:** later behaviour, intervention or repair cannot retroactively rewrite the identity, authority, policy or evidence that applied at the earlier decision.

**Typical failure:** `Role_effective` or an accomplished action becomes proof that it was authorized.

**Current EA anchors:** S12, S13.

### G-A11 — Affected-scope bounded disposition / continuity

**Property:** the specification can distinguish the affected transition from unaffected legitimate operation; unresolved state is neither automatic global permission nor automatic global veto.

**Typical failure:** deny-all is counted as safety; or uncertainty in one branch authorizes everything.

**Current EA anchors:** S3, S5, T2, T3.

### G-A12 — Authorized positive transition / anti-deny-all

**Property:** when the relevant change and required authority are genuinely established, the specification permits a legitimate transition instead of freezing the old state forever.

**Typical failure:** a system passes every negative by rejecting all change.

**Current EA anchors:** S1, S3, S10, T3.

### G-A13 — Finite useful-horizon discipline

**Property:** the specification requires a bounded evidence/review/decision process relative to a useful response horizon and declares what happens when sufficiency cannot be reached in time.

**Typical failure:** indefinite review is treated as safety.

**Current EA anchors:** T4, S3, S5.

### G-A14 — Evidence / trace trust boundary

**Property:** the specification states when a self-produced trace, log, identity claim or result is insufficient as sole evidence and what qualification/independence is required for a material decision.

**Typical failure:** spoofable self-report is accepted as authoritative evidence of action, effect, identity or compliance.

**Current EA anchors:** S6, S7, S12, S14.

**Stage boundary:** Stage A can require the trust boundary and owner/interface. Stage B must verify how an architecture realizes independent observation or trusted evidence.

---

## 6. Dependency graph

Gate dependencies are typed claims owned by the **test instrument** and frozen before adjudication.

Initial candidate dependency graph:

| Target gate | Dependency | Type | Reason |
|---|---|---|---|
| G-A02 Authority applicability | G-A01 scope binding | REQUIRES | authority is meaningless without the action/domain to which it applies |
| G-A03 identity grounding | G-A01 scope binding | REQUIRES | representation is decision-relative |
| G-A04 material change | G-A01 scope binding | REQUIRES | change must be relative to a prior decision basis |
| G-A05 evidence→decision | G-A01 scope binding | REQUIRES | sufficiency is decision-relative |
| G-A06 UNKNOWN preservation | G-A05 evidence→decision | REQUIRES | UNKNOWN is qualification of a proposition/decision |
| G-A07 non-substitution | G-A05 evidence→decision | REQUIRES | substitution is defined relative to evidence/decision roles |
| G-A08 objective integrity | G-A01 scope binding | REQUIRES | hard limits/objectives need declared ownership/scope |
| G-A09 temporal validity | G-A02 authority applicability | REQUIRES | expiry/revocation applies to a defined authority object |
| G-A10 history/repair | G-A01 scope binding | REQUIRES | historical state must be tied to a decision record |
| G-A11 bounded disposition | G-A06 UNKNOWN preservation | REQUIRES | affected-scope handling requires unresolved state to remain represented |
| G-A11 bounded disposition | G-A01 scope binding | REQUIRES | affected vs unaffected scope must be distinguishable |
| G-A12 positive transition | G-A02 authority applicability | REQUIRES | legitimate change requires applicable authority where authority is material |
| G-A12 positive transition | G-A04 material change | CONDITIONAL | only required for profiles where the transition depends on changed conditions |
| G-A13 useful horizon | G-A01 scope binding | REQUIRES | useful time is relative to a decision/action |
| G-A14 trace trust | G-A05 evidence→decision | REQUIRES | independence matters only relative to what the evidence is used to decide |

A dependency is **not automatically transitive evidence**. Passing a prerequisite does not imply passing the dependent gate.

---

## 7. `PASSES_IF` / conditional diagnosis

If a gate has adequate local text but an unmet prerequisite, report:

    G-Axx = NOT_ESTABLISHED
    conditional_on = [G-Ayy, ...]
    diagnostic = PASSES_IF(prerequisites reach required level)

Example:

    G-A11 bounded partial disposition
      local_level = L4
      dependency G-A06 UNKNOWN = L4
      dependency G-A01 scope = L2
      result = NOT_ESTABLISHED
      diagnostic = PASSES_IF(G-A01 >= L3)

This is the basis for automatic recommendations without pretending the missing architecture already exists.

---

## 8. Model-based Stage A test model

Stage A uses a **symbolic specification model**, not a runtime implementation.

### 8.1 Test inputs

A test campaign freezes:

1. specification artefact + hash;
2. claimed scope/profile;
3. gate catalogue + hash;
4. dependency graph + hash;
5. verdict/level definitions;
6. case/fixture set;
7. case-to-gate activation matrix;
8. external facts deliberately supplied by the evaluator;
9. mutation/ablation set; and
10. amendment/stopping rule.

### 8.2 Case model

Each case declares:

- neutral case ID;
- visible facts;
- evaluator-private truth where needed;
- decision to be made;
- applicable gates;
- required level per gate;
- allowed terminal dispositions;
- prohibited collapses;
- information deliberately unavailable;
- whether exclusion narrows the claim or violates it.

Case names shown to a blind reviewer should not encode the expected verdict.

### 8.3 Specification model

The reviewer/model extracts from the specification:

- obligation;
- scope;
- owner/source;
- receiver;
- conditions;
- temporal validity;
- UNKNOWN semantics;
- allowed/prohibited disposition;
- external-owner boundary;
- conformance/testability hook.

Stage A does not invent implementation machinery to fill missing fields.

---

## 9. Specification-level mutation testing

The deterministic executable analogue for Stage A is **mutation of the specification model/text**, not execution of a runtime architecture.

Reference mutations should be frozen before adjudication.

| Mutant | Deliberate defect | Gates expected to detect it |
|---|---|---|
| **M-A01 Scope-erasure** | remove decision/scope binding | G-A01 and dependents |
| **M-A02 Authority-amplification** | allow peer/coordinator assignment to create mandate | G-A02, G-A07 |
| **M-A03 Self-certified identity** | accept asserted handle/signature without required representation trust | G-A03, G-A14 |
| **M-A04 Unbounded detection claim** | claim material-change coverage with no observation boundary | G-A04 |
| **M-A05 Feasibility→permission** | treat technical success as authorization | G-A05, G-A02 |
| **M-A06 UNKNOWN→ALLOW** | default unresolved fact to permission | G-A06 |
| **M-A07 Population substitution** | repeated/correlated peer agreement counts as independent authority/evidence | G-A07 |
| **M-A08 Utility-overrides-hard-limit** | allow beneficial/collective objective to overwrite a hard constraint | G-A08 |
| **M-A09 Stale/silent consent** | reuse expired authority or interpret no veto as consent | G-A09 |
| **M-A10 History rewrite** | later effect rewrites prior authority state | G-A10 |
| **M-A11 Deny-all** | reject every uncertain or changed branch | G-A11, G-A12 |
| **M-A12 Infinite review** | no finite fallback/response horizon | G-A13 |
| **M-A13 Self-report-is-effect** | accept candidate's own compliance/action log as sufficient material effect evidence | G-A14 |

A useful Stage A test instrument should fail the intended mutants at the intended gates and preserve conforming reference specifications.

Failure to reject the relevant mutant is itself evidence that the gate definition/test is weak.

---

## 10. Blind-review protocol

A blind Stage A reviewer receives:

- the pinned specification under test;
- the pinned generic gate catalogue and verdict definitions;
- neutralized case cards;
- external evaluator facts explicitly marked as such;
- a blank gate matrix.

The reviewer does **not** receive:

- author gate verdicts;
- author requirement-to-case mapping;
- expected mutant failures;
- architecture-plausibility annexes;
- prior adjudication results.

Because public repositories cannot guarantee cognitive blindness, the campaign records reviewer exposure status:

    UNEXPOSED_DECLARED
    PREVIOUSLY_EXPOSED
    UNKNOWN_EXPOSURE

Only `UNEXPOSED_DECLARED` supports a blind-review claim.

---

## 11. Decision rule when reviewers disagree

Disagreement is an output, not something to average away.

For each gate:

- exact agreement → retain verdict/level;
- same verdict, different clause/evidence → retain verdict and record evidence disagreement;
- PASS vs NOT_ESTABLISHED → gate status becomes `REVIEW_DISPUTED`; claim ceiling cannot exceed NOT_ESTABLISHED until resolved by a predeclared adjudicator/rule;
- PASS vs FAIL or FAIL vs NOT_ESTABLISHED → `REVIEW_DISPUTED`; no acceptance credit;
- scope disagreement → freeze both scope readings and either narrow the claim or invoke the predeclared scope adjudicator.

Post-hoc author preference cannot resolve a dispute.

---

## 12. Diagnostic recommendation graph

Stage A recommendations are **specification recommendations**, not architecture prescriptions.

For every gate below its target:

1. identify unmet local fields;
2. identify blocking prerequisites;
3. compute downstream gates conditionally blocked by those prerequisites;
4. report a minimum closure set that unlocks the largest number of conditional gates;
5. state the claim that becomes available after closure.

Example output:

    Missing: G-A02 authority domain/applicability = L2, target L4
    Blocks: G-A09 temporal validity, G-A12 positive transition
    Recommendation:
      declare authority source, action/resource domain, expiry/revocation and receiving decision
    Does NOT prescribe:
      PKI, RBAC, token format, control plane, human workflow

Architecture choices belong to Stage B.

---

## 13. Claim profiles

Different Stage A campaigns can require different gate subsets.

Example profiles:

### Profile A — decision-boundary integrity

Mandatory candidate gates:

G-A01, G-A02, G-A05, G-A06, G-A07, G-A08, G-A09, G-A12.

### Profile B — change/requalification

Mandatory candidate gates:

G-A01, G-A04, G-A05, G-A06, G-A11, G-A13.

### Profile C — provenance / trace integrity

Mandatory candidate gates:

G-A01, G-A03, G-A05, G-A10, G-A14.

These profiles are examples. A result-producing campaign must freeze its own profile before adjudication.

---

## 14. Stage A / Stage B boundary

Stage A may conclude:

- the specification represents a property at L0–L4;
- a gate passes/fails/is not established/out of scope under a declared claim;
- one gate is conditional on another;
- a textual mutant is or is not rejected;
- a specification change would close a documented gap.

Stage A may **not** conclude merely from this:

- that a detector will observe the change in time;
- that an external authority source is trustworthy in implementation;
- that a runtime actuator will obey the disposition;
- that an independent recorder exists or resists spoofing;
- that partial containment is cheaper than global stopping;
- that one architecture outperforms a conventional comparator;
- that the historical incident would have been prevented.

Those are Stage B/C questions.

---

## 15. Required report format

A Stage A report should include at minimum:

| Gate | Applicability | Level | Verdict | Dependencies | Cases | Evidence | Conditional closure | Claim impact |
|---|---|---:|---|---|---|---|---|---|
| G-Axx | applicable / OOS | L0–L4 | PASS / FAIL / NOT_ESTABLISHED / OUT_OF_SCOPE | gate IDs | neutral case IDs | pinned clauses | `PASSES_IF(...)` or none | full / narrowed / blocked |

Plus:

- mutation matrix;
- reviewer disagreement ledger;
- out-of-scope ledger;
- minimal closure recommendations;
- Stage-B deferred questions;
- complete source/hash freeze.

---

## 16. Falsifiers of this Stage A design

This gate-based instrument should be revised or rejected if:

1. different gates cannot be made to fail independently under specification mutations;
2. gate definitions collapse into paraphrases of one specification's current clauses;
3. the same case always activates nearly every gate;
4. dependencies make PASS automatic rather than conditional;
5. recommendation output prescribes one architecture rather than a missing specification property;
6. a blind reviewer requires author mapping to understand the cases;
7. two materially different specifications routinely receive the same gate profile despite known semantic differences;
8. gate profiles fail to transfer across at least two independent scenario families beyond the case used to design them.

---

## 17. Promotion rule

This document is a **draft test-design artefact**.

Before it can become the controlling DDS Stage A gate profile:

1. freeze the gate catalogue and dependency graph;
2. test it against at least two scenario families not used to derive every gate;
3. run specification mutants;
4. obtain independent review of gate independence and verdict semantics;
5. compare with the current DDS Stage A method and reconcile any contradiction;
6. promote by explicit versioned commit rather than silently editing the canonical Stage A method.