# 04 General Interfaces vNext Review & Delta — Ecosystem Awareness

> **Working delta only — not a new interface specification.**  
> The current programme-independent interface reference remains [**04 — General Functional Interfaces & Agentic Security v0.5 Integrated**](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md).  
> The historical controlled v0.4 source remains preserved separately.  
> This file accumulates post-baseline addenda, clarifications and review questions. It may remain partial while review is active. Nothing here changes O1–O6, IF-S1–IF-S13, the EHD kernel, the Composition-Critical profile or Appendix A unless a later 04 version is explicitly promoted.

| | |
|---|---|
| **ID** | 04-vNext Review & Delta |
| **Version · date** | v0.1-draft · opened 24 September 2026 |
| **Status** | Cumulative interface delta / review; incomplete by design; no change to 04 v0.5 baseline |
| **Current 04 baseline** | General Functional Interfaces & Agentic Security v0.5 Integrated |
| **Historical controlled source** | 04 Functional Interfaces & Agentic Security v0.4 split source |
| **Upstream control** | [00 Requirements frozen baseline](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) + [Requirements vNext Review & Delta](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) |
| **Downstream consumers** | FG-TIDA 05 ideal mapping, 05A current-state bridge, validation/test profiles and later specification-preparation work |

---

## 1. Delta rule

04 is the **programme-independent interface layer**. This delta therefore asks only whether post-baseline work requires a change to the generic EA interface architecture.

It does **not** import FG-TIDA Theme numbers, Theme ownership or programme-specific mappings into 04. Those belong downstream in 05/05A.

For each new development, the review asks:

1. does the upstream Requirements delta expose a genuinely new solution-neutral obligation?;
2. if not, does the current 04 already express the needed interface semantics?;
3. if partly, is only an editorial clarification or optional profile refinement needed?;
4. does the proposed change belong instead to component conformance, a test profile, a signalling/control annex or a programme-specific mapping?;
5. would adding the field/family create unnecessary metadata or semantic coupling for simple routes?

A new architecture object, scenario field, test disposition or programme-specific mapping is **not** automatically a new O#/IF-S# family or universal EHD field.

---

## 2. Upstream Requirements disposition

The current [Requirements vNext Review & Delta](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) does **not** justify S15, T5, H7 or a new canonical KPI family.

That constrains 04-vNext in the same direction:

- do **not** create O7 merely because later architecture adds a new processing object;
- do **not** create IF-S14 merely because a later scenario or test names another boundary;
- do **not** expand the six-element EHD interoperability kernel merely because one fixture benefits from an extra qualifier;
- prefer conditional/profile semantics where the information is material only to specific compositions.

Three Requirements clarification candidates are interface-relevant.

### CAND-R1 — effective-role drift

The later corpus makes the distinction

`Role_bound ≠ Role_effective`

more operationally visible.

**Tentative 04 consequence:** where role/function drift is material to the receiving decision, a producer or adapter may need to preserve enough source-owned state to distinguish:

- declared/bound role or representation;
- observed effective function/state;
- the basis and time of the observation; and
- whether current authority/applicability for that effective function is established, not established or external to the producer.

This should initially remain a **conditional qualifier/profile concern**, not a new universal EHD kernel field and not a new identity/authority interface family.

Continuity of identity, name, runtime lineage or newly acquired capability must not be interpreted by 04 as proof of continuity or expansion of authority.

### CAND-R2 — opportunity / admissibility / authority / execution

The later corpus increasingly uses the reading rule:

`opportunity ≠ admissibility ≠ authority ≠ execution`.

**Tentative 04 consequence:** the generic interface architecture should remain capable of carrying these distinctions without translating one into another.

In particular:

- a high-value or technically reachable candidate may be preserved as information without becoming permission;
- a policy/admissibility result remains source-owned;
- an authority response remains authority-owner state;
- an execution/outcome record remains distinct from the decision or request that preceded it.

The current 04 already supports most of this through O1/O5, IF-S2, IF-S4, IF-S8, IF-S11/12 and the Composition-Critical EHD profile. The delta therefore records a likely **editorial clarification**, not a new interface family.

### CAND-R3 — per-action compliance versus aggregate/composed authorization

The upstream Requirements delta now makes explicit:

`per-action compliance ≠ aggregate/composed authorization`.

00H supplies the concrete falsifier: every atomic action may satisfy a local cap or rule while the cumulative campaign remains outside the participant's legitimate authority boundary.

**Tentative 04 consequence:** where authority is defined over a cumulative, campaign-level, resource-time or other composed effect, the interface route may need a **conditional Composition-Critical relation** that preserves enough action-history / aggregate-lineage state for the legitimate owner or relying party to evaluate the composed effect.

This should **not** become a seventh mandatory EHD kernel element. The relevant aggregate/composition boundary is source-owned and context-specific. A simple single-action route should not carry aggregate-history metadata merely because another profile needs it.

The current 04 already provides the right extension point through decision/operation references, predecessor/parent relations, decision-basis references and source-owned authority semantics in the Composition-Critical EHD profile. The vNext question is therefore whether that profile should state the aggregate/cumulative case explicitly, not whether a new interface family is needed.

---

## 3. 00G — false-context convergence and source-dependence pressure

[00G — Collective False-Context Convergence](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md) adds a post-baseline stress case in which repeated claims, role drift, authority claims and attractive opportunity can displace the legitimate operating frame.

### Interface pressure

A sufficiently expressive route must be able, where material, to preserve:

- source/provenance and upstream dependence;
- independent versus correlated corroboration;
- claimed versus established scope;
- claimed versus established role/authority;
- current objective/mission or the reference that owns it;
- material unresolved qualifiers;
- a bounded requalification target rather than an indiscriminate request for more context.

### Current 04 coverage

The current 04 already contains:

- EHD source/provenance/dependency semantics;
- explicit UNKNOWN handling;
- decision-scope projection;
- source-native ownership;
- O1 objective/mission references;
- IF-S1/IF-S2 identity and authority boundaries;
- IF-S7 drift/observability;
- IF-S11 ecosystem signal/incident exchange;
- optional Composition-Critical lineage/dependency fields.

### Delta disposition

**No new O#/IF-S# family established.**

Potential later clarification:

- make the “correlated repetition is not independent corroboration” rule more prominent in the general interface reading;
- cross-reference CAND-R1 where role drift is material.

00G remains scenario/test pressure, not an interface-specification source by itself.

---

## 4. 00H — beneficial opportunity beyond current authority

[00H — Batch Opportunity Beyond Authority](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.1.md) adds a post-baseline stress case in which a candidate action is valuable, technically reachable and well evidenced but lies outside the participant's current role/grant.

It also tests a second failure: individually compliant actions may form an unauthorized aggregate campaign.

### Interface pressure

Where the receiving decision depends on these facts, a route may need to preserve:

- current grant/authority reference and scope;
- action/operation reference;
- aggregate lineage or action-history relation when the authority condition is aggregate rather than per transaction;
- the candidate finding/opportunity as a separate information object;
- request/re-contract/requalification state;
- authority-owner response;
- response expiry/no-valid-response;
- requalification before any subsequent execution;
- actual execution/outcome separately from approval or request.

### Current 04 coverage

The Composition-Critical EHD profile already allows decision/operation references, parent/predecessor relationships, decision-basis references, validity/review conditions, targeted re-entry and external authority ownership.

IF-S2, IF-S8, IF-S11 and IF-S12 already separate authority, record, signal/request and execution/control concerns.

### Delta disposition

**No universal EHD expansion yet.**

The aggregate-action relation is material only for some authority models. It should first be treated as a **conditional Composition-Critical profile requirement** or external record reference, not a metadata tax on every handoff.

`RepositionIntent`, `AuthorityResponse` and DBC dispositions remain owned by their signalling/control/test layers. 04 only needs to preserve the semantic separability of request, authority response, requalification and execution.

Silence/expiry must remain representable without being silently translated into permission.

---

## 5. Decision Boundary Challenge v0.2 — test vocabulary must not become interface ontology

[Decision Boundary Challenge v0.2](../DECISION_BOUNDARY_CHALLENGE_v0.2.md) distinguishes:

- producer-native result;
- determination condition / Type 0/1/2;
- operating posture;
- DBC procedural disposition;
- authority-owner response;
- execution/outcome.

Its CAN / KNOW / MAY / SHOULD / ACT questions are useful for testing boundary collapse.

### 04 consequence

The generic interface architecture should be able to **preserve the separability** of these layers where a test route uses them.

It should **not**:

- translate external verdicts into DBC dispositions;
- make DBC disposition a universal EHD field;
- make P1/P2/P3 universal interface semantics;
- make AuthorityResponse a universal transport enum; or
- create a new interface family solely for DBC.

### Delta disposition

**Test/conformance pressure only.**  
Use DBC to expose missing or laundered boundaries in 04 implementations; do not use it to redefine 04 by default.

---

## 6. Semantic/qualification validity window versus response window

Two independent post-baseline routes make the same temporal distinction visible. Theme #13 work — especially the Operational Risk / Response Window / Epistemic Opportunity v0.2 discussion — separates qualification validity from response timing. Independently, [DBC-C02 — semantic TOCTOU](../DECISION_BOUNDARY_CHALLENGE_v0.2.md#5-challenge-pack-families) tests whether a result can remain technically available or syntactically valid while a material authority/evidence/context condition has become stale before use. Together they make two temporal concepts more explicit:

1. **semantic / qualification validity window** — how long evidence, authority, delegation, policy, configuration and supporting assumptions remain applicable; and
2. **operational response window** — how long remains to materially affect the outcome.

The same work distinguishes:

- more can still be known within current available capacity; from
- more knowledge would still be useful for the current decision.

### Current 04 coverage

04 already contains:

- freshness/as-of;
- validity interval or revalidation condition;
- response horizon;
- capacity binding;
- observation/determination burden;
- targeted re-entry;
- F2/F4/F5/F6/F7 responsibilities for acquisition, qualification, composition, posture and requalification.

### Tentative 04-vNext clarification

A later 04 version should make explicit that **validity time and response time are not interchangeable**.

Where material, a producer/adapter should be able to preserve both without forcing them into one scalar or universal field.

Likewise, an epistemic-processing outcome such as:

- continue investigation;
- stop because current support is sufficient;
- redirect effort;
- request targeted corroboration/requalification;

must remain distinct from an authorized operational intervention.

### Delta disposition

Likely **editorial/interface clarification**, not a new function or interface family.

DBC-C02 provides the applied-validation route for this distinction now. If a future 00I Semantic TOCTOU scenario is committed, it should be cited here as an additional scenario-level stressor only after its repository text is reviewed; it must not be presumed from a chat-only draft.

---

## 7. Human-review outputs under the general handoff discipline

Later human-oversight discussion has made a useful generic distinction visible:

1. human decision/result;
2. assurance in the received review event;
3. capacity binding/qualification;
4. residual/inherited indeterminacy.

The important boundary is that assurance concerns the evidentiary status of the received human-review event; it is not a generalized judgment of human competence.

### Current 04 coverage

IF-S6 already owns Human Oversight & Intervention Capacity, while EHD can carry result, uncertainty/assurance semantics, capacity and residual qualifiers conditionally.

### Tentative 04-vNext consequence

A future editorial pass may make explicit that **human-produced outputs are not exempt from bounded epistemic handoff discipline** merely because the channel is authenticated or the actor is authorized.

That does not require every human decision to carry a complex score. Lightweight categorical/structured qualifiers remain sufficient where they preserve the material distinction.

### Delta disposition

Candidate clarification within IF-S6/EHD guidance.  
No new mandatory kernel field at this stage.

---

## 8. IF-S11 peer capability relation — preserve, do not redesign

The current 04 already states that an incident-signal / blast-radius mechanism is a concrete **IF-S11 peer capability** that EA can consume rather than reproduce, and that EA may also be needed where no incident or malicious agent exists.

This is the correct programme-independent boundary.

The stronger Theme #13-specific evidence that Ecosystem Awareness and the incident/signal lifecycle are independently testable peer mechanisms belongs downstream in **05 / 05A**, not in the generic 04 as Theme-specific prose.

### Delta disposition

**No generic architectural change required. Preserve the current peer-capability boundary.**

A future 04 editorial revision may make the bidirectionality more visible generically:

external signal/incident capability ↔ EA qualification/requalification,

while leaving programme-specific ownership and lifecycle semantics outside 04.

---

## 9. Relationship to 05 and 05A

The correct change-control order is:

**00 Requirements baseline**  
→ **00 Requirements delta**  
→ **04 General Interfaces baseline**  
→ **04 General Interfaces delta**  
→ **05 FG-TIDA Ideal mapping baseline/delta**  
→ **05A FG-TIDA Current-State bridge baseline/delta**

Therefore:

- 05 may specialize or map a reviewed 04 capability into FG-TIDA Theme relationships;
- 05 cannot create a new generic EA interface merely because a Theme needs it;
- 05A must be narrower still and support each mapped field/relationship from current public FG-TIDA source evidence;
- a 05/05A issue that reveals a genuine generic gap should return upstream to this 04 delta rather than silently changing 04 semantics downstream.

---

## 10. Current delta determination

The post-baseline material reviewed through 24 September 2026 does **not** currently justify:

- O7;
- IF-S14;
- a seventh mandatory EHD kernel element;
- a mandatory DBC/ACC/MSCA/FG-TIDA-specific vocabulary in the generic interface layer; or
- a new universal human-review or incident payload.

The strongest likely 04-vNext changes are presently **clarifications and conditional profile refinements**:

1. make effective-role drift preservable where material without treating observed function as authority;
2. make opportunity / admissibility / authority / execution separation visually explicit;
3. make per-action compliance versus aggregate/composed authorization explicit where the authority boundary is cumulative;
4. distinguish qualification-validity time from operational response time;
5. clarify that human review outputs can carry bounded assurance/capacity/residual qualification;
6. reinforce source-dependence / independent-corroboration preservation;
7. treat cumulative/aggregate action-history as a **conditional Composition-Critical profile element** where the authority rule is aggregate rather than per transaction, without adding it to the universal EHD kernel; and
8. preserve the current IF-S11 peer-capability relation while making generic bidirectionality easier to read.

This delta remains open and cumulative. New post-baseline interface findings should be appended here first. The 04 v0.5 Integrated baseline is not silently rewritten while review is active.
