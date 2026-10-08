# DDS Stage A — Gate Diagnostic Profile v0.1 Draft

**Status:** additive Stage A diagnostic subprofile · draft for audit and cross-framework validation · not an adopted standard, certification scheme, assurance opinion or Stage A acceptance result.  
**Date:** 8 October 2026.  
**Owning method:** [DDS Stage A — Specification Discovery / Challenge–Trajectory Profile v0.1](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md).  
**Purpose:** make Stage A produce a reusable gate-by-gate diagnostic profile for any candidate specification, mechanism, control profile or technology/configuration trajectory, rather than a single opaque pass/fail result.

> This profile does not replace the DDS Stage A chain. It adds a normalized diagnostic layer after the Challenge and candidate mapping are frozen. Hugging Face, UC-21, 00E–00J, R01 and future technology/framework studies are validation fixtures of the profile; none of them defines the core gate taxonomy.

---

## 1. Design objective

Stage A should answer more than “did this candidate pass?”.

For each applicable property, it should identify:

1. whether the property is satisfied, contradicted, not established or not applicable;
2. how strong/testable the candidate specification is at that property;
3. which upstream properties the conclusion depends on;
4. which downstream properties are blocked by the missing prerequisite;
5. what minimum specification change would improve the result;
6. what architecture capability Stage B would later need to realize the property.

The Stage A output is therefore a **diagnostic profile**, not a scalar score.

A typical result may read:

```text
SA-G03 identity / representation root      PASS @ L3
SA-G04 authority applicability/currentness CONDITIONAL_ON(SA-G03) @ L3
SA-G05 domain non-substitution              NOT_ESTABLISHED @ L1
SA-G11 bounded disposition                  PASS @ L4
SA-G13 execution/compliance owner           NOT_ESTABLISHED @ L1
```

This preserves an important distinction: a candidate may specify a correct disposition without owning runtime enforcement.

---

## 2. Two independent axes: verdict and specification level

### 2.1 Case/gate verdict

Every applicable gate receives exactly one base verdict:

- **PASS** — the frozen candidate supports the required distinction/disposition for the frozen case without inventing facts or importing a later-stage mechanism.
- **FAIL** — inside claimed scope, the candidate explicitly produces, permits or requires a closure contrary to the frozen facts/acceptance rule, or a blanket control defeats a positive continuity case.
- **NOT_ESTABLISHED** — the candidate does not determine the requested property from the frozen text/evidence boundary.
- **NOT_APPLICABLE** — the preregistered Challenge/profile declares that the gate is outside the material decision boundary for this case.

`NOT_APPLICABLE` must be declared by the profile, not added after seeing a difficult result.

### 2.2 Specification-strength level

Independently of verdict, assign a level:

| Level | Meaning |
|---|---|
| **L0 — absent** | no reviewable treatment of the property |
| **L1 — declared** | concept/intent is mentioned but no binding candidate rule is identifiable |
| **L2 — normative candidate** | a required/prohibited behavior is stated, but scope/owner/conditions are incomplete |
| **L3 — scoped and owned** | rule, scope, owner/source, timing/currentness and relevant boundary are sufficiently explicit |
| **L4 — falsifiable/test-ready** | the gate has a frozen positive/negative or boundary criterion that can return PASS/FAIL/NOT_ESTABLISHED reproducibly at Stage A |

Level is not evidence maturity and is not architecture realization. A documentary candidate can be L4 if its semantic rule is falsifiable; a running product can remain L1 if the relevant rule is not specified.

### 2.3 Derived dependency status

Dependency is reported separately:

- **SATISFIED** — all preregistered hard prerequisites for this gate meet the profile threshold.
- **CONDITIONAL_ON(...)** — the gate's own text may be adequate, but one or more hard prerequisites are not yet established.
- **BLOCKED_BY(...)** — the missing/failed prerequisite makes the requested downstream conclusion invalid under the current profile.

A conditional result is not promoted to PASS by arithmetic.

---

## 3. Core cross-framework gate catalog

The following catalog is technology-neutral. A Challenge selects the gates that are material; it may add local gates, but local gates do not become core gates without a versioned catalog revision.

| ID | Core property | Stage A question |
|---|---|---|
| **SA-G00** | Decision boundary and scope | Are the decision, action/alternative, affected resource/domain, current task/mission, owner and null/fallback boundary explicit enough to adjudicate? |
| **SA-G01** | Observation boundary and freshness | Does the candidate declare what can be known/observed, from which sources, at what time/freshness, and where indistinguishability remains? |
| **SA-G02** | Evidence provenance and effect basis | Are evidence source, provenance and the distinction among intent/command/action/effect sufficiently preserved to avoid self-report becoming outcome truth? |
| **SA-G03** | Identity and representation root | Does the candidate distinguish self-asserted identity, authenticated message/key, represented role/principal and independently established trust/delegation root? |
| **SA-G04** | Authority applicability and currentness | Is authority evaluated for the concrete action/resource/purpose at the relevant commitment/action time, including expiry/revocation/current applicability? |
| **SA-G05** | Domain/principal non-substitution | Can evidence, authority, approval, population convergence or a grant from one owner/domain silently substitute for another owner/domain? |
| **SA-G06** | Indeterminacy preservation | Is UNKNOWN/conflict/insufficiency preserved without silently becoming permission, success or a universal veto? |
| **SA-G07** | Material-change requalification | Does material change in facts, scope, role, purpose, authority or dependency trigger bounded requalification rather than stale reuse? |
| **SA-G08** | Time/default/expiry discipline | Are response horizons finite and are silence, delay, timeout, stale approval or expiry handled without creating permission by default? |
| **SA-G09** | Objective/mandate integrity | Can scorer utility, local reward, collective benefit, peer pressure or another objective silently displace a known mandate/hard boundary? |
| **SA-G10** | History and non-retroactive legitimation | Can later behavior/effect, repeated success or repaired state rewrite whether the earlier action was authorized/conforming? |
| **SA-G11** | Bounded disposition / least affected scope | Does the candidate define the smallest reviewable hold/requalification/continuation boundary rather than all-or-nothing control? |
| **SA-G12** | Positive continuity / no deny-all | When all relevant conditions are established, can legitimate work continue/change without a blanket default-deny solution winning the test? |
| **SA-G13** | Execution/compliance ownership declaration | Does the specification identify who/what owns compliance, enforcement or actuation after a decision-level disposition, including when that owner is explicitly external? |
| **SA-G14** | Decision-basis reconstructability | Can an independent reviewer reconstruct the material basis, unresolved facts, source/owner boundaries and resulting disposition without private chain-of-thought? |

These gates are properties of the test. They are not synonyms for any one EA S#/T# clause, Hugging Face N-case, FG-TIDA Theme or vendor feature.

---

## 4. Dependency graph

Dependencies are preregistered as a directed graph. They express logical diagnostic prerequisites, not implementation architecture.

### 4.1 Default hard prerequisites

```text
SA-G04 <- SA-G00 + SA-G03
SA-G05 <- SA-G00 + SA-G04
SA-G07 <- SA-G00 + SA-G01 + SA-G06
SA-G08 <- SA-G00 + SA-G01 + SA-G04
SA-G09 <- SA-G00 + SA-G04 + SA-G05
SA-G10 <- SA-G00 + SA-G02
SA-G11 <- SA-G00 + SA-G06 + SA-G07
SA-G12 <- SA-G00 + SA-G04 + SA-G06
SA-G13 <- SA-G00 + SA-G11
SA-G14 <- SA-G00 + SA-G02
```

A Challenge may narrow these dependencies only by preregistered profile/version, with rationale. It may not delete a prerequisite after seeing the result.

### 4.2 Reading a conditional result

Example:

- candidate text has a strong action-specific authority rule: SA-G04 reaches L3;
- identity/representation root is only self-asserted: SA-G03 is NOT_ESTABLISHED @ L1.

Result:

```text
SA-G04 own-text verdict: PASS @ L3
dependency status: CONDITIONAL_ON(SA-G03)
effective diagnostic: CONDITIONAL_ON(SA-G03), not unconditional PASS
```

The same missing SA-G03 may also block SA-G05 and SA-G09. This is exactly why the graph is diagnostically useful.

---

## 5. Profile-specific admission and acceptance

The core catalog does not impose one universal “all 15 gates must pass” rule.

Before adjudication, each Challenge/profile freezes:

- applicable core gates;
- any local gates;
- minimum acceptable level per gate;
- hard prerequisites;
- positive/continuity controls;
- falsifiers;
- boundary cases;
- allowed NOT_APPLICABLE gates;
- whether NOT_ESTABLISHED is claim-narrowing or acceptance-blocking for each gate;
- Stage A acceptance wording.

Therefore Stage A may legitimately conclude:

- accepted for a bounded specification package;
- partially accepted / conditional;
- no material differential against a peer;
- outside acceptance;
- insufficient evidence / NOT_ESTABLISHED.

A global PASS without the gate table is non-conforming to this diagnostic profile.

---

## 6. Gate test design

Every applicable gate should have, where meaningful:

1. **positive control** — valid behavior must remain possible;
2. **negative/falsifier** — a materially wrong closure must be detectable;
3. **boundary case** — insufficient or external-owner facts must not be forced into PASS/FAIL;
4. **ablation/mutation target** — removing or weakening the relevant specification rule should change the correct case outcome;
5. **evidence ceiling** — what Stage A can and cannot conclude.

A gate that cannot fail under any preregistered case is a **coverage control**, not a discriminating test. Report it as such.

---

## 7. Standard Stage A diagnostic record

For every evaluated candidate, produce one row per gate:

| Field | Meaning |
|---|---|
| gate_id | core or local gate ID |
| applicability | applicable / not applicable with preregistered reason |
| verdict | PASS / FAIL / NOT_ESTABLISHED / NOT_APPLICABLE |
| level | L0…L4 |
| dependency_status | SATISFIED / CONDITIONAL_ON(...) / BLOCKED_BY(...) |
| candidate_surfaces | exact clauses/features/configuration evidence |
| case_ids | frozen cases that exercise the gate |
| missing_fact_or_owner | if any |
| blocker_root | earliest unresolved prerequisite(s) |
| downstream_impacted | gates whose conclusions are blocked/conditional |
| stage_a_remediation | minimum specification/test change |
| stage_b_handoff | architecture capability that would later need realization |
| evidence_ceiling | maximum supported claim |
| reviewer_rationale | concise and reproducible |

The report then publishes a graph view and a matrix view. No opaque weighted score is required.

---

## 8. Automatic recommendation logic

The recommendation engine operates on the frozen dependency graph and the observed gate table.

### 8.1 Root-cause closure

For each non-PASS/conditional gate:

1. walk upstream through hard prerequisites;
2. stop at the earliest FAIL/NOT_ESTABLISHED/L0-L1 prerequisite;
3. record that gate as a root blocker;
4. propagate the impact to all dependent gates.

This prevents five downstream symptoms from being reported as five unrelated defects.

### 8.2 Minimum remediation cut set

Compute the smallest set of root blockers whose remediation to the preregistered threshold would unlock the largest number of conditional gates.

Report, for each candidate remediation:

- gate to improve;
- current verdict/level;
- target minimum level;
- direct gates unlocked;
- transitive gates potentially unlocked;
- whether the change is specification-only or requires Stage B realization;
- residual gates still unresolved.

This is an architectural audit recommendation, not proof that the architecture has been fixed.

### 8.3 Example

```text
Root blocker: SA-G03 Identity/representation root — NOT_ESTABLISHED @ L1

Potential unlock:
  SA-G04 Authority applicability/currentness
  SA-G05 Domain/principal non-substitution
  SA-G09 Objective/mandate integrity

Stage A recommendation:
  define a reviewable external trust/delegation root and distinguish it from message signature/authentication.

Stage B handoff:
  realize that root with an independently governed identity/delegation mechanism and auditable binding.

Claim boundary:
  Stage A may recommend the capability; it may not credit the architecture as implemented.
```

---

## 9. Stage A versus Stage B/C boundary

Stage A tests the **specified semantics and declared ownership**.

It may establish that a candidate:

- requires an external stop owner;
- requires effect evidence independent of self-report;
- requires action-time authority validation;
- requires bounded requalification.

Stage A does **not** establish that those mechanisms exist, are correctly connected, meet latency, resist spoofing or actually stop an action.

Those questions move to:

- **Stage B** — architecture realization and interfaces;
- **Stage C** — pinned implementation behavior against the originating Challenge.

The Stage A report should therefore contain a Stage-B handoff queue generated from the gate table, but never count that queue as Stage A PASS evidence.

---

## 10. Cross-framework comparison

When comparing frameworks/platforms under the same frozen Challenge:

- use the same gate catalog version;
- use the same applicable-gate profile and minimum levels;
- use the same facts, authority states, horizons and evaluator-private information;
- allow each framework its strongest admissible native configuration;
- preserve framework-native semantics;
- report gate-by-gate profiles side by side;
- report burden separately;
- do not average hard-gate failure into a utility score.

A useful comparison can therefore say:

```text
Framework A: 9 gates PASS, 3 conditional, 2 NOT_ESTABLISHED, 1 N/A
Framework B: 11 gates PASS, 1 FAIL, 2 conditional, 1 N/A
No global winner: B covers more properties but fails a hard continuity case.
```

The exact counts are illustrative; only executed/frozen studies may publish actual counts.

---

## 11. Validation of this gate model

Before treating this diagnostic profile as stable, validate it against at least three materially different families:

1. one historical/incident-derived family;
2. one synthetic or mathematical/reduction family;
3. one independent technology/framework family not used to derive the gates.

For each family, record:

- gates exercised;
- gates not applicable;
- whether any gate is impossible to falsify;
- whether dependencies created false blocking;
- whether a local gate was needed;
- whether the recommendation engine identified a useful root blocker;
- whether the profile changed after seeing outcomes.

Any material change produces v0.2; historical runs remain tied to their catalog version.

---

## 12. Explicit non-claims

This draft does not establish:

- that the 15-gate catalog is complete or unique;
- that a framework with more PASS gates is universally safer/better;
- that Stage A predicts production behavior;
- that Stage A architecture recommendations are implemented;
- that Hugging Face or another historical case validates the catalog by itself;
- that a local gate automatically belongs in the core catalog;
- FG-TIDA, ITU-T, NIST or other standards-body adoption.

**Current status:** draft diagnostic layer ready for audit and cross-framework validation; no framework result is created by this document alone.


### 4.3 Prerequisite NOT_APPLICABLE rule

A hard prerequisite marked `NOT_APPLICABLE` does **not** automatically block a downstream gate.

It may be treated as dependency-satisfied only when the preregistered Challenge/profile states why the prerequisite mechanism is irrelevant **and** supplies the frozen fact/assumption that the downstream gate needs instead.

Example: a mathematical reduction may freeze principal/mandate identity as an evaluator fact and contain no identity-resolution problem. In that profile, SA-G03 may be `NOT_APPLICABLE` while SA-G04 remains directly adjudicable. If the authority claim depends on resolving a real-world actor/key/role binding, SA-G03 is applicable and cannot be bypassed.

Therefore dependency evaluation uses:

```text
PASS prerequisite -> satisfied
NOT_APPLICABLE + preregistered substitute/frozen assumption -> satisfied-by-profile
NOT_APPLICABLE without that justification -> BLOCKED_BY(prerequisite-profile-gap)
FAIL / NOT_ESTABLISHED below threshold -> conditional or blocked as registered
```

This rule prevents the generic catalog from forcing implementation-specific identity or authority machinery into reductions where those facts are intentionally abstracted away.
