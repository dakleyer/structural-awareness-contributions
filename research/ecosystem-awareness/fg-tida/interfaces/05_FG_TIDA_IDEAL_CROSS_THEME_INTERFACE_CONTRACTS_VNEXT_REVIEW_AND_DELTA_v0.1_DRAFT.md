# 05 Ideal Interfaces vNext Review & Delta — FG-TIDA

> **Working delta only — not a new interface specification.**  
> The frozen reference remains [**05 — FG-TIDA Ideal Cross-Theme Interface Contracts v0.4**](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) ([part 2](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part02.md), [part 3](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part03.md)).  
> This file accumulates post-freeze interface addenda and review notes. It may remain partial while review is active. Nothing here changes the frozen 05 unless a later version is explicitly promoted.

| | |
|---|---|
| **ID** | 05-vNext Review & Delta |
| **Version · date** | v0.1-draft · opened 24 September 2026 |
| **Status** | Cumulative interface delta / review; incomplete by design; no frozen-contract change |
| **Frozen source** | 05 v0.4 Ideal Cross-Theme Interface Contracts |
| **Upstream control** | [00 Requirements frozen baseline](../../baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) + [Requirements vNext Review & Delta](../../baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) |
| **Downstream relation** | Future 05A current-state delta/review should consume only addenda that are also supportable from public FG-TIDA source evidence |

---

## 1. Delta rule

This file records only what has changed, become clearer or requires reconsideration since the frozen 05 v0.4 interface baseline.

It does **not** need to restate the full 05 contracts. Each addendum should identify:

1. the frozen 05 section or relationship affected;
2. the new public/corpus evidence or architectural clarification;
3. the tentative interface consequence;
4. what remains unresolved; and
5. whether the item is suitable for a later 05 version, only for 05A/current-state mapping, or only for test/conformance.

A new concept is **not** automatically a new interface field. The upstream Requirements delta remains controlling: if the new material is only an architecture, implementation, scenario or test realization of an existing requirement, this interface delta should preserve that distinction rather than manufacture a new universal contract.

---

## 2. Addendum A — Theme #13: Ecosystem Awareness and the incident/signal lifecycle as peer mechanisms

### Frozen 05 area affected
Theme #13 ↔ EA contract and the overall contract anatomy.

### Post-freeze clarification

The current public Theme #13 discussion now supports a stronger architectural reading than a simple one-way “#13 produces, EA consumes” relationship.

Ward Duchamps has publicly stated that:

- **Ecosystem Awareness belongs within Theme #13** because the Theme already assumes independently governed participants and no central orchestrator;
- the systemic-capacity / handoff interface may be foundational for ecosystem-level reasoning;
- defense/containment is the first concrete use, not the whole scope of the envelope; and
- **the determinacy envelope and the signal lifecycle should be defined independently**, so that each can be tested alone and can interoperate through a specified interface.

Nelson Trasatti subsequently confirmed from the UC #4 / testbed side that:

- the incident lifecycle remains a **complete operational mechanism**, not merely a transport layer for EA;
- EA remains independently testable;
- the interaction can be exercised through bounded targeted-refinement loops; and
- the existing four-field determinacy envelope can be consumed as a versioned #13 profile through an adapter without the testbed owning the broader abstraction.

Relevant public anchors:

- Ward — signal lifecycle and federated testbed direction: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5508513343
- Ward — EA placement, foundational interface and independent envelope/lifecycle: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256
- Iván — explicit peer-mechanism / bidirectional interface proposal: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5624367911
- Nelson — testbed-side compatibility and independent-testability confirmation: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397
- Iván — compact interface table preserving the same boundary: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5640186655

### Tentative 05-vNext consequence

For the next ideal-interface version, the #13 relation should be modelled as **two independently testable peer mechanisms inside the Theme #13-derived architecture**, rather than as a parent/subordinate relation:

| Peer mechanism | Primary responsibility |
|---|---|
| **Incident / Signal Lifecycle** | Signal birth and semantics, distribution, corroboration/amendment, operational affected-scope/blast-radius refinement, response coordination, locally authorized containment workflow and resolution. |
| **Ecosystem Awareness** | Decision-scoped systemic qualification of available states, residual/inherited indeterminacy, source/dependency composition, capacity/horizon sufficiency and targeted requalification. |

The interface remains bidirectional:

**Lifecycle → EA:** bounded incident/evidence state, provenance/source relationship, freshness, affected scope/blast radius, response window/reach and unresolved qualifiers.

**EA → Lifecycle:** decision-scoped systemic qualification, residual/UNKNOWN conditions, material capacity/window constraints and targeted refinement/requalification requests.

### Boundary to preserve

- incident resolution ≠ ecosystem requalification;
- operational blast radius ≠ epistemic dependency/inherited-indeterminacy graph;
- signal confidence/assurance ≠ system-level determinacy;
- available containment reach ≠ authority to contain;
- neither signalling nor EA creates action authority.

### Still open

The broader use of **EHD as the general abstraction beyond the concrete #13 determinacy-envelope profile** remains a candidate architecture question. The peer-mechanism relationship is better supported than the final ownership/name/scope of the reusable EHD abstraction.

---

## 3. Addendum B — Theme #16: bounded semantic mapping now has an agreed working sequence

### Frozen 05 area affected
Theme #16 ↔ EA contract, human-capacity handoff, decision/execution/revalidation route and conformance/test relationship.

### Post-freeze clarification

The public Theme #16 discussion has converged on a bounded sequence using Arpita Sarker's UC #6 as the semantic reference.

The current sequence is:

**UC #6 semantic facts / authority-applicability outcome**  
→ **current v0.2 matrices annotate the bounded Theme #16 interfaces**  
→ **UC #4 derives the executable mapping / fixtures / traces**  
→ **originating case and matrix semantic owners review the interpretation**  
→ **only then may the mapping be frozen**

Public anchors:

- Nelson — proposed UC-6 → v0.2 matrices → UC-4 mapping: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803023066
- Arpita — accepts UC #6 as stable semantic reference and review role: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803653565
- Olena — accepts the mapping without adding matrix fields or changing case facts: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5804125734
- Lei — Theme #16 lead approval: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5809248877

### Tentative 05-vNext consequence

The next ideal interface should preserve these separate objects:

1. authority determination / current applicability received from the authority layer;
2. available intervention options;
3. human decision/result;
4. assurance/evidentiary qualification of the received human-review event where applicable;
5. human/institutional capacity qualification;
6. residual/inherited indeterminacy;
7. attempted execution versus externally confirmed outcome where proportionate/available;
8. re-entry/revalidation condition.

The mapping must not infer that human approval expands the upstream grant or that decision receipt proves execution.

### Boundary to preserve

Theme #16 remains semantic owner of human-oversight/intervention lifecycle semantics. EA may qualify systemic implications and consume capacity/decision/outcome state; UC #4 may make the agreed mapping executable; neither EA nor the testbed redefines the Theme #16 matrix.

---

## 4. Addendum C — Requirements-delta constraints on interface evolution

The current Requirements vNext review does **not** justify S15, T5, H7 or a new canonical KPI family. Therefore 05-vNext should avoid creating interface fields merely because later architecture introduced new names.

Two clarification candidates are especially relevant to future interface wording:

### CAND-R1 — effective-role drift

The interface model may need to preserve a material distinction between:

`Role_bound` and `Role_effective`

without treating observed behaviour or newly acquired capability as proof of legitimate authority, representation or membership.

Tentative interface implication: where role drift is material to the receiving decision, a future profile may need enough source-owned state to distinguish bound role/authority from observed effective function/state. This is a **candidate qualifier/profile issue**, not yet a new universal EHD kernel field.

### CAND-R2 — opportunity / admissibility / authority / execution

The interface architecture should preserve the fact that:

`opportunity ≠ admissibility ≠ authority ≠ execution`

Tentative interface implication: a high-value or technically reachable candidate transition may be preserved/routed without being represented as permitted or authorized. A request for re-contracting/requalification and an authority-owner response remain distinct from final execution state.

Again, this does not currently justify a new universal handoff family or mandatory field.

---

## 5. Addendum D — new failure/test pressure from 00G, 00H and DBC v0.2

### 00G — Collective False-Context Convergence

Interface pressure:

- preserve source dependence so correlated repetition is not counted as independent corroboration;
- preserve mission/objective and applicable authority/profile boundaries against external narrative takeover;
- make effective-role drift observable without legitimizing it;
- keep claimed scope/authority separate from established scope/authority;
- support targeted requalification rather than indiscriminate graph expansion.

Current disposition: pressure on existing EHD/profile, dependency and qualification semantics; no new universal interface family established.

### 00H — Batch Opportunity Beyond Authority

Interface pressure:

- preserve a materially beneficial finding even when current authority is insufficient;
- prevent per-action compliance from laundering an aggregate unauthorized campaign;
- carry a bounded request/re-contract/requalification path without treating the request as authority;
- keep `RepositionIntent`, `AuthorityResponse`, new qualification and execution as distinct events/states;
- preserve expiry/no-response without converting silence to permission.

Current disposition: strong test of existing authority, handoff, scope, lineage and action/outcome interfaces; no new universal EHD kernel field established.

### Decision Boundary Challenge v0.2

DBC deliberately separates:

- producer-native verdict;
- Type 0/1/2 determination condition/failure;
- P1/P2/P3 operating posture;
- DBC procedural disposition;
- authority-owner response; and
- actual execution/outcome.

Current disposition: **test/conformance namespace only**. 05-vNext should make these boundaries expressible where material, but must not convert DBC vocabulary into a mandatory FG-TIDA runtime contract.

---

## 6. Addendum E — semantic/qualification window versus response window

Oleksii Voshchak's v0.2 Operational Risk / Response Window / Epistemic Opportunity matrix makes two temporal dimensions more explicit:

1. **semantic / qualification validity window** — how long the relevant evidence, authority, delegation, policy, configuration and assumptions remain applicable; and
2. **operational response window** — how long remains to materially affect the outcome.

It also distinguishes:

- more can still be known within current capacity; from
- more knowledge would still be useful for the current decision.

Tentative 05-vNext consequence:

- do not collapse freshness/validity and response-horizon semantics into one field;
- allow an interface/profile to preserve each when material to the receiving decision;
- preserve epistemic-processing outcomes (continue / stop / redirect / request corroboration) separately from authorized intervention decisions.

Public anchor: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5783505043

---

## 7. Relationship to 05A current-state bridge

This delta describes changes to the **ideal** FG-TIDA interface projection.

It does **not** automatically update 05A.

A future 05A delta/review should examine each addendum against the latest public FG-TIDA evidence and classify it using the 05A vocabulary:

- Current source state;
- Candidate cross-Theme field;
- Test-only evidence; or
- Not established.

The ideal 05 may therefore move ahead conceptually while 05A remains narrower. That difference is intentional and must remain visible.

---

## 8. Current delta determination

No complete 05 rewrite is required at this stage.

The current addenda indicate that a future ideal-interface version should, at minimum:

1. replace any residual one-way/subordinate reading of #13 with an explicit **peer-mechanism, bidirectional** EA ↔ incident-lifecycle architecture;
2. update the Theme #16 route to the now-approved bounded UC-6 → v0.2 matrices → UC-4 mapping sequence;
3. preserve the Requirements-delta distinctions around effective-role drift and opportunity/admissibility/authority/execution without prematurely creating new universal fields;
4. incorporate the temporal separation between qualification validity and response opportunity when material;
5. use 00G/00H/DBC as falsification/conformance pressure rather than as automatic sources of new contracts; and
6. keep EHD generalization, exact mandatory qualifiers and future document ownership explicitly reviewable until the relevant semantic-owner/public-process support is sufficient.

This delta remains open and cumulative. New post-freeze interface changes should be appended here rather than inserted into frozen 05 v0.4.
