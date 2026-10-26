# 04 — A/B/C/D Recognition Guide and Example EA Interface Map — Working Proposal

> **Status:** v0.1 Working Proposal · 2 October 2026.  
> **Position in the corpus:** candidate successor direction for the 04 interface line. It is **not** the 04 baseline, does not replace [04 v0.5 Integrated](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md), and does not claim a permanent or universal interface model.  
> **Semantic source:** [00M §1](./00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical).  
> **Requirements source:** [00 Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md).

## 1. What 04 is for in this Working Proposal

04 has two deliberately different purposes.

**Part A — Recognition guide.**  
00M defines A/B/C/D theoretically. 04 gives a practical, bounded way to recognize those roles in an actual interface or process without pretending that field names determine semantics.

**Part B — Example interface map.**  
04 then shows one practical EA input/output map across familiar agentic and trust/security functions. This is an implementation example for reading and testing the method. It is not the ideal architecture for all systems, not a mandatory schema and not a claim that future EA implementations must keep the same families or fields.

The map is therefore useful only if every included item has an interpretable role under a declared producer/process/profile. Items that cannot yet be classified with sufficient confidence remain **PROFILE-DEPENDENT / UNRESOLVED** rather than being forced into A/B/C/D.

## 2. The key rule: direction is not the role

"Input to EA" and "output from EA" do not define A/B/C/D.

A/B/C/D are always relative to a **producer, functional process, question, subject/scope, capability and time**.

A value can therefore be:

- **A of the source process** and simultaneously an input to EA;
- **B of the source process** because it qualifies the source's A;
- **C of the source process** because it identifies a grounded exploration route whose evaluation basis is not yet established;
- **D of the source process** because a potentially material effect lies beyond that process's effective evaluation route;
- **A of EA** when EA itself delivers a qualified assessment, requalification request, posture or other operative result to its consumer.

The same message can contain several atomic assertions with different roles. The message itself is not "an A message" or "a C message".

## 3. Bounded recognition procedure

This is a guide, not a universal classifier.

### R0 — Fix the frame

Before assigning a role, identify:

- producer;
- functional process;
- question or proposition;
- subject/scope;
- capability and access boundary;
- relevant time/version;
- operative consumer.

If those cannot be established, do not guess a role.

### R1 — Identify A first

Ask:

> What does this process actually establish and deliver as its operative result for this question, scope and time?

That delivered result is **A**.

A can be a verdict, probability, rate, interval, plan, capability assessment, execution status, identity result, attestation result or another datatype. Datatype does not determine the role.

### R2 — Separate atomic assertions

Split the surrounding information into concrete assertions about:

- basis/method;
- coverage;
- validity/freshness;
- provenance;
- dependencies;
- exclusions;
- additional assessable work;
- exploration routes;
- effective evaluation barriers.

Do not classify a large field or document as one role when it contains several different assertions.

### R3 — Recognize B

Use **B** only where the producer already has a defensible basis for describing A or an additional characterized assessment reserve.

Typical evidence can include:

- method/reference/version;
- coverage and known exclusion;
- calibration or uncertainty actually supported by the method;
- validity/freshness conditions;
- characterized additional measurement or check;
- defensible effort/time/cost bounds for that characterized work;
- known provenance/dependency limits.

A known, evaluable option remains **B** even when the producer did not use it because of cost, policy, time or priority.

### R4 — Recognize C

Use **C** only where:

1. there is a grounded reason to believe a relevant exploration route exists; and
2. the evaluation basis for that aspect is not yet sufficiently established.

C does not require an enumerable population, known total cost or expected benefit.

A merely unused capability is not C if its question, variables and evaluation method are already characterized; that remains B.

### R5 — Recognize D

Use **D** only where:

1. a potentially material condition or dependency is identified; and
2. its relevant effect lies beyond the producer's effective evaluation route under the declared access, authority, method, capability and time.

D is not "external", "uncontrolled" or "unknown" by label alone. A well-characterized external risk may be A or B. A missing field without evidence of an effective evaluation barrier remains unresolved, not automatically D.

### R6 — Preserve PROFILE-DEPENDENT / UNRESOLVED

When the same native field can play different roles depending on the producer's function, or when the available source does not establish the required boundary, retain:

**PROFILE-DEPENDENT / UNRESOLVED**

until the profile is explicit.

This is preferable to manufacturing a false A/B/C/D assignment.

### R7 — Bind the role to history

A classification must retain the relevant profile/version and time basis. If the producer's function, field semantics, scope or capability boundary changes, review the role. Do not rewrite older exchanges as if the new mapping had always applied.

## 4. Proposed disposition of the earlier H06 issue

The earlier input-only contract deliberately excluded the value of A from its metadata route. That produced **H06** because the existing 04 EHD kernel and some F9 uses consume an operational result.

For this Working Proposal, the proposed disposition is:

> **Do not impose a universal exclusion of A.**

A may be an EA input when the EA function actually needs the source result. Where a lightweight metadata-only profile is sufficient, the value of A may remain on its ordinary operational route and EA may receive only a stable reference/binding plus the eligible B/C/D qualifiers.

Therefore:

- **full-result profile:** `A + eligible B/C/D → EA`;
- **metadata-only profile:** `A_ref + eligible B/C/D → EA`;
- the profile must state which one it uses;
- a metadata-only profile must not claim to support an EA use that requires the value of A;
- A must not be relabelled as B merely to pass through a metadata route.

This keeps the architecture lightweight without detaching B/C/D from the result they qualify.

H06 remains historically valid for the older input-only proposal. This section is a **candidate disposition for a future 04 successor**, not a retroactive rewrite of that document.

## 5. Worked profile used for the example map

The following map is intentionally illustrative.

**Profile P-04-EA-01**

- Each neighbouring function keeps ownership of its native semantics.
- Its delivered native result is A of that source process.
- Stable basis/limits/coverage are B where justified.
- A grounded but uncharacterized exploration route is C.
- A material effect beyond effective evaluation is D.
- EA may consume A or A_ref according to the declared profile.
- EA's delivered qualification/request/posture is **A(EA)**.
- EA's own basis, limits and characterized reserve are **B(EA)**.
- EA may expose a **C(EA)** frontier or **D(EA)** residual where justified.
- No row below creates authority, execution ownership, truth or completeness.

## 6. Example EA interface map

This table is a **worked implementation example**, not the permanent 04 schema. It uses the existing O1–O6 / IF-S1–IF-S13 families because they are familiar and already reviewed in 04.

| Family | Example input to EA | Role in P-04-EA-01 | Example EA output | Role of EA output |
|---|---|---|---|---|
| **O1 Mission / Objective / Orchestration** | current mission/commitment state; objective/reference; criticality, horizon and dependency basis | mission/commitment state can be **A(O1)**; reference, criticality, horizon and characterized dependencies are **B(O1)**; uncharacterized relevant dependency may be C/D only when R4/R5 are met | qualified posture; targeted requalification / scope-review request | operative result/request **A(EA)**; affected scope, basis, expiry and limits **B(EA)**; unresolved frontier/residual only as justified **C/D(EA)** |
| **O2 Discovery / Capability** | discovered participant/capability result; provenance, freshness and coverage | discovery/capability result **A(O2)**; provenance/freshness/coverage **B(O2)**; an evidenced but uncharacterized discovery path **C(O2)**; material unreachable dependency **D(O2)** | reliance qualification or refresh request | **A(EA)** with B/C/D(EA) qualification as applicable |
| **O3 Runtime / Worker / Model** | operational result; local scope, method, uncertainty semantics, capacity and unresolved dependencies | operational result **A(O3)**; scope/method/validity/capacity **B(O3)**; grounded unexplored route **C(O3)**; material effect beyond effective evaluation **D(O3)** | re-evaluation, preserve-indeterminate, source-change or window-adjustment request | **A(EA)**; request basis/limits **B(EA)** |
| **O4 Context / Memory / Retrieval / Research** | retrieved evidence set/result; source lineage, freshness, coverage and search bounds | retrieval result **A(O4)**; lineage/freshness/coverage/search basis **B(O4)**; grounded uncharacterized source route **C(O4)**; inaccessible material source effect **D(O4)** | widen/narrow/redirect, primary-source or corroboration request | **A(EA)**; characterized budget/stop basis **B(EA)**; open search frontier/residual **C/D(EA)** when explicitly justified |
| **O5 Tool / Resource / Action Execution** | execution/result/status; authorization reference; reversibility/confirmation scope | execution/result/status **A(O5)**; authorization reference, reversibility and confirmation basis **B(O5)**; possible but uncharacterized verification route **C(O5)**; external side effect without effective evaluation route **D(O5)** | delay/restrict/reconcile/containment request to the legitimate owner | request **A(EA)**; scope/basis/re-entry criterion **B(EA)**; not authority or execution |
| **O6 Task / Message / Artifact Transport** | delivery/update/lifecycle result; sender/receiver binding, freshness and correlation | delivery/lifecycle state **A(O6)**; binding/freshness/correlation semantics **B(O6)**; no C/D is presumed merely because delivery is incomplete | EA envelope / correction / requalification signal for transport | transported EA result **A(EA)** plus B/C/D(EA) qualifiers already established by EA |
| **IF-S1 Identity / Principal Binding** | identity/binding/validity result; assurance, scope, provenance, freshness | native identity/binding result **A(IF-S1)**; assurance/scope/provenance/freshness **B(IF-S1)**; C/D only for separately justified unresolved aspects | refresh/requalification or insufficient-binding indication | **A(EA)** with affected scope and limits **B(EA)** |
| **IF-S2 Authority / Delegation / Authorization** | grant/applicability/standing result; grant provenance, scope, chain, validity | native authority/applicability result **A(IF-S2)**; provenance/scope/chain/validity **B(IF-S2)**; unexplored authority question **C(IF-S2)** only if a route exists; inaccessible material standing effect **D(IF-S2)** | refresh authority, narrow-scope or requalification request | **A(EA)**; EA does not issue the grant |
| **IF-S3 Attestation / Runtime Assurance** | Attestation Result; attested scope, verifier, appraisal reference, freshness and limitations | Attestation Result **A(IF-S3)**; scope/verifier/reference/freshness/limitations **B(IF-S3)**; C/D only for explicitly separate unresolved aspects | re-attestation, independent-route or reduced-reliance request | **A(EA)**; qualification basis **B(EA)** |
| **IF-S4 Policy / Intent / Runtime Conformance** | conformance verdict; policy/version, examined scope, evaluator and verdict basis | verdict **A(IF-S4)**; reference/version/scope/evaluator/freshness **B(IF-S4)**; unresolved route **C/D** only when separately grounded | re-evaluation / preserve-indeterminate / insufficient-scope request | **A(EA)** with B(EA) basis; no policy authorship |
| **IF-S5 Evidence Appraisal** | appraisal result or rejection; checks/profile, freshness, limitations | appraisal result/rejection **A(IF-S5)**; checks/profile/freshness/limitations **B(IF-S5)**; omitted check is **B** if already evaluable, **C** only if exploration is needed, **D** only under an effective evaluation barrier | appraisal/profile-change request or preserved evidence-side uncertainty | **A(EA)** |
| **IF-S6 Human Oversight / Intervention Capacity** | human-capacity/decision/outcome result; role, authority, response window, evidence basis | capacity/decision/outcome can be **A(IF-S6)** according to the observed human-oversight process; role/authority/window/evidence basis **B(IF-S6)**; inaccessible institutional dependency may be **D(IF-S6)** | targeted human-review request or capacity-insufficient determination | **A(EA)**; affected scope/need **B(EA)**; EA does not make the human decision |
| **IF-S7 Observability / Telemetry / Evaluation / Drift** | measurement/drift result; coverage, period, method, confidence and burden | measurement/drift result **A(IF-S7)**; coverage/period/method/confidence/burden **B(IF-S7)**; grounded measurement frontier **C(IF-S7)**; material unobservable effect **D(IF-S7)** | instrumentation/refresh/revalidation/redirection request | **A(EA)**; measurement priority/basis **B(EA)** |
| **IF-S8 Accountability / Action Records** | recorded action/outcome/integrity result; identity, policy, authority and provenance links | record/integrity result **A(IF-S8)** when that is the record process's deliverable; provenance/scope/links **B(IF-S8)**; no missing event is automatically C or D | bounded EA statement or preservation/re-entry request | **A(EA)** plus B(EA) provenance/limits |
| **IF-S9 External / Population Evaluation** | population assessment/rate; population, period, taxonomy, evaluator-dependence and identifiability limits | population assessment/rate **A(IF-S9)**; population/period/taxonomy/dependence/statistical basis/known limits **B(IF-S9)**; grounded but uncharacterized additional population/evaluator route **C(IF-S9)**; material effect not evaluable under the observation architecture **D(IF-S9)** | qualified use / insufficiency / requalification feedback to the legitimate consumer; any new measurement remains #21/producer-owned | EA qualification **A(EA)**; scope and reason **B(EA)**; unresolved frontier/residual **C/D(EA)** |
| **IF-S10 Privacy / Minimum Disclosure** | disclosure/permission decision or profile; retention/linkability and permitted-attribute constraints | source decision/profile can be **A(IF-S10)** when it is the privacy function's deliverable; its scope/constraints **B(IF-S10)**; omitted content is not automatically C/D | minimum-disclosure requirement or insufficient-disclosure qualification | **A(EA)**; missing qualification may remain D/UNKNOWN only with the required grounds |
| **IF-S11 Ecosystem Signal / Incident Exchange** | alert/signal/blast-radius/resolution result; source, freshness, provenance, dependence and corroboration history | native signal/result **A(IF-S11)**; source/freshness/provenance/dependence/history **B(IF-S11)**; uncharacterized corroboration route **C(IF-S11)**; material effect beyond signal mechanism's evaluation route **D(IF-S11)** | qualified signal, corroboration request, posture/requalification state | **A(EA)** plus B/C/D(EA) qualification |
| **IF-S12 Enforcement / Containment / Recovery / Migration** | execution/status/recovery/readiness result; authority, response window, reversibility and residual exposure | execution/status/readiness **A(IF-S12)**; authority reference/window/reversibility/characterized residual **B(IF-S12)**; alternative route **C** only if not yet evaluable; unevaluable material effect **D** | scope-indexed EA posture / containment or migration request / return criterion | **A(EA)**; criterion and limits **B(EA)**; no enforcement ownership |
| **IF-S13 Trust Framework / Assurance / Jurisdiction** | equivalence/applicability/assurance result; framework/version/rules and unresolved incompatibilities | native equivalence/applicability result **A(IF-S13)** when delivered by the trust function; framework/version/rule basis **B(IF-S13)**; possible but uncharacterized comparison **C(IF-S13)**; material incompatibility beyond effective determination **D(IF-S13)** | insufficient-equivalence / alternate-profile / residual treatment | **A(EA)** with scope/limits **B(EA)** |

## 7. What the example intentionally does not fix

The table does **not** claim that a field name has one permanent role.

For example:

- a probability is A when probability estimation is the producer's delivered function, but B when it qualifies another A;
- a "capability" can be A of a discovery function, B as a characterized reserve, or only a label with insufficient grounds;
- an "unknown" is not automatically D;
- an omitted check is B if its evaluation basis is already characterized, C if a grounded exploration route exists but that basis is not yet established, and D only if the relevant effect is beyond effective evaluation;
- a population rate is A of the population-evaluation process; its method, population and known dependence limits can be B;
- an EA request is A of EA's request/requalification function even though it does not authorize the requested action.

## 8. Relation to the earlier 176-row input map

The existing [04 Input Interface Contract v0.4](./04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md) remains useful source material because it decomposes 176 reviewed inputs and records Q/N/H/X review logic.

This Working Proposal does **not** claim that all 176 historical row classifications have been revalidated under 00M v0.8.

A future promotion should re-check each retained row against R0–R7 and record one of:

- **CONFIRMED A/B/C/D** under a named profile;
- **PROFILE-DEPENDENT** with the conditions stated;
- **UNRESOLVED** where the source does not establish enough;
- **LINK / CONFIGURATION** where the item is not itself an epistemic role;
- **REMOVE FROM EXAMPLE** where the field is not needed for the worked profile.

That revalidation is review work, not a semantic assumption.

## 9. Draft promotion conditions

This document should remain **Working Proposal** until at least:

1. the recognition guide is reviewed against 00M v0.8;
2. the earlier H06 tension is either accepted with the profile-based disposition above or replaced by a better explicit rule;
3. the selected practical map is checked family by family against the source semantics;
4. at least one end-to-end worked profile shows both EA input and EA output classification;
5. the result is checked against S1–S14 / T1–T4 without creating new requirements by accident.

No baseline promotion is proposed here.
