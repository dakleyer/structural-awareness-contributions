# DDS Stage A — Gate Diagnostic Profile v0.2 Audit Candidate

**Status:** frozen audit candidate for the additive Stage A diagnostic subprofile · no external result yet · not an adopted standard, certification scheme, assurance opinion or Stage A acceptance result.  
**Date:** 9 October 2026.  
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

### 2.3 Derived dependency and effective status

The gate record separates what the candidate says from what the dependency graph allows the evaluator to claim.

- **own_verdict** — PASS / FAIL / NOT_ESTABLISHED / NOT_APPLICABLE from the frozen candidate and case, before dependency propagation.
- **dependency_status** — SATISFIED / CONDITIONAL_ON(...) / BLOCKED_BY(...), using only preregistered `requires` edges for a gate and `claim_requires` edges for the named stronger claim being evaluated.
- **effective_status** — the claim-usable result after dependency and minimum-level checks: PASS / FAIL / NOT_ESTABLISHED / NOT_APPLICABLE / CONDITIONAL_ON(...) / BLOCKED_BY(...).

A `supports` edge is explanatory only. It can improve another property but can never turn that property into a failure or conditional result.

A gate can therefore have strong own text while the stronger claim remains conditional. For example, an action-specific authority rule can receive `own_verdict=PASS @ L3`, while `CLAIM-AUTHORITY-RESOLVED` remains `CONDITIONAL_ON(SA-G03)` if the actor/role binding is not frozen as an evaluator fact.

A conditional or blocked status is never promoted to PASS by arithmetic, and remediation of a prerequisite is reported as **potentially unlocking** downstream conclusions, not as guaranteeing them.

### 2.4 Test role

Every exercised gate/case is labelled before adjudication as one of:

- **DISCRIMINATING** — the frozen case can genuinely make the gate PASS or FAIL under the registered candidate.
- **COVERAGE_CONTROL** — verifies that an explicit required distinction exists, but the case itself is not a meaningful falsifier.
- **BOUNDARY_CONTROL** — verifies correct NOT_ESTABLISHED / NOT_APPLICABLE / external-owner handling and prevents forced closure.

A gate that cannot fail under any preregistered case cannot be advertised as a discriminating test merely because the requirement text restates the expected answer.

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

### 4.1 Typed dependency edges

The graph uses three edge types. Only `requires` blocks basic gate adjudication.

- **requires** — logical prerequisite to adjudicate the downstream gate at all.
- **claim_requires** — prerequisite only for a stronger named claim built from several gates.
- **supports** — upstream property that improves or operationalizes the downstream property but is not logically necessary to score it.

#### Default `requires` edges

```text
SA-G04 <- SA-G00
SA-G05 <- SA-G00
SA-G07 <- SA-G00
SA-G08 <- SA-G00
SA-G09 <- SA-G00
SA-G10 <- SA-G00
SA-G11 <- SA-G00
SA-G12 <- SA-G00
SA-G13 <- SA-G00
SA-G14 <- SA-G00
```

SA-G01, SA-G02, SA-G03 and SA-G06 are independently adjudicable.

#### Default named `claim_requires`

```text
CLAIM-AUTHORITY-RESOLVED
  requires SA-G04
  plus SA-G03 when identity/representation is not frozen as an evaluator fact

CLAIM-MATERIAL-CHANGE-DETECTED-AND-REQUALIFIED
  requires SA-G01 + SA-G07

CLAIM-UNRESOLVED-STATE-BOUNDED
  requires SA-G06 + SA-G11

CLAIM-MANDATE-INTEGRITY-ACROSS-DOMAINS
  requires SA-G04 + SA-G05 + SA-G09

CLAIM-VALID-CONTINUITY
  requires SA-G04 + SA-G06 + SA-G12

CLAIM-RECONSTRUCTABLE-EFFECT-BASIS
  requires SA-G02 + SA-G14

CLAIM-RUNTIME-ENFORCEABILITY
  requires SA-G11 + SA-G13 at Stage A declaration level,
  then Stage B architecture verification before runtime enforceability can be claimed

CLAIM-TIMELY-REQUALIFICATION
  requires SA-G01 + SA-G07 + SA-G08

CLAIM-BOUNDED-LEGITIMATE-CONTINUITY
  requires SA-G04 + SA-G06 + SA-G11 + SA-G12

CLAIM-NONAMPLIFYING-CROSS-DOMAIN-AUTHORITY
  requires SA-G03 + SA-G04 + SA-G05

CLAIM-TRACEABLE-DISPOSITION-TO-ENFORCEMENT
  requires SA-G02 + SA-G10 + SA-G13 + SA-G14 at Stage A declaration level,
  then Stage B verification before a runtime chain is claimed
```

#### Default `supports` edges

```text
SA-G03 supports SA-G04
SA-G04 supports SA-G05 and SA-G09
SA-G01 supports SA-G07 and SA-G08
SA-G06 supports SA-G07, SA-G11 and SA-G12
SA-G02 supports SA-G10 and SA-G14
SA-G11 supports SA-G13
```

A profile may add/remove typed edges only prospectively, with rationale and versioning.

### 4.2 Reading a conditional result

The basic gate verdict and a stronger multi-gate claim are deliberately separate.

Example:

- SA-G04 has a strong action-specific authority rule: `own_verdict=PASS @ L3`;
- SA-G03 identity/representation root is `NOT_ESTABLISHED @ L1`;
- the profile is evaluating `CLAIM-AUTHORITY-RESOLVED`, whose preregistered `claim_requires` includes SA-G03 when identity/representation is not frozen as an evaluator fact.

Result:

```text
SA-G04 own verdict: PASS @ L3
SA-G04 basic dependency status: SATISFIED
CLAIM-AUTHORITY-RESOLVED: CONDITIONAL_ON(SA-G03)
```

SA-G04 is not rewritten as a failure. The stronger authority-resolved claim remains conditional until SA-G03 is established or the profile preregisters identity/representation as a frozen evaluator fact.

The same rule applies to other named claims. `supports` edges may explain likely remediation value, but they never create blocking by themselves.


---

## 5. v0.2 audit-candidate freeze

This successor freezes the diagnostic semantics for external audit without rewriting v0.1.

**Freeze status:** `FROZEN_AUDIT_CANDIDATE__NO_EXTERNAL_RESULT`  
**Freeze date:** 9 October 2026.

The v0.2 audit candidate adds four controls that are mandatory for any result-producing run:

1. **Profile-required gates are explicit.** A run must declare `required_for_profile` per gate before adjudication. There is no universal rule that all fifteen gates apply.
2. **Discriminating gates must be able to fail.** Every `DISCRIMINATING` gate must cite at least one preregistered `fail_capable_case_id`. A gate that merely restates the candidate text is a `COVERAGE_CONTROL`, not a falsifier.
3. **Conditional claim dependencies are executable.** A conditional dependency must be tied to a frozen profile fact, not left as prose. The first registered case is `CLAIM-AUTHORITY-RESOLVED`: it requires SA-G03 unless `identity_representation_frozen_as_evaluator_fact=true` is frozen before adjudication.
4. **The gate table is primary.** The overall profile outcome is only a summary. It never replaces the gate-by-gate result, levels, root blockers, conditional dependencies, remediation candidates or Stage-B handoff.

### 5.1 Frozen profile outcomes

- **PROFILE_PASS** — every required gate is effective PASS, every required named claim is PASS, and at least one active discriminating gate has a preregistered fail-capable case.
- **PROFILE_PARTIAL** — no required FAIL exists, but one or more required gates/claims remain NOT_ESTABLISHED, CONDITIONAL_ON, BLOCKED_BY or below their frozen minimum level.
- **PROFILE_FAIL** — at least one required gate or required named claim is an effective FAIL.
- **PROFILE_COVERAGE_ONLY** — required coverage/boundary controls pass but the frozen profile contains no active fail-capable discriminating gate. This is useful documentary coverage evidence, not a passed discriminating test.

### 5.2 Required run inputs

Before a reader sees candidate outcomes, freeze:

- Challenge/fixture and candidate refs;
- gate applicability and `required_for_profile`;
- minimum level per required gate;
- test role per exercised gate;
- case IDs and fail-capable case IDs;
- evaluator facts used to suppress conditional dependencies;
- required named claims;
- acceptance wording and evidence ceiling.

### 5.3 Audit recommendation semantics

Recommendations are diagnostic, not prescriptive proof.

For a blocker `Y`, the checker may report that remediation of `Y` would **potentially unlock** gates or claims `X1...Xn`. It must not report that `X` will pass after the change. The candidate must be frozen again and re-adjudicated.

The Stage-B handoff is separate: it states what architecture capability would later be needed to realize the Stage-A property. It grants no Stage-A credit and makes no runtime-effectiveness claim.
