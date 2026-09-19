# Use-Case Portfolio — Canonical Requirements Coverage Map — v0.1

**Status:** public working mapping, 19 September 2026. This annex is a requirements-first portfolio and gap map. It does not modify the frozen Parent Case Study, the four frozen Architecture-Validation Profiles, S1–S14, T1–T4, H1–H6, the KPI protocol, 04, 05 or 05A. It does not claim that a requirement has been validated merely because it is named in a scenario.

## 1. Purpose and reading rule

The [canonical requirements document](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) is the source of truth for what a candidate must address. A Use Case, reference failure scenario, quality-plan fixture or interoperability test must select its applicable requirement route from that document; it must not create a parallel challenge taxonomy.

The portfolio is read in both directions:

1. **Requirements-first:** `S# → T# → H# → KPI` identifies the behaviour and evidence a case must supply.
2. **Evidence-first:** a declared case or failure mechanism identifies its material scope, then maps to the applicable `S# → T# → H# → KPI → test/gate disposition` route.

The same case may support several challenges, and one challenge may need several cases. A direct EA result tests EA's qualification, preservation, composition or re-entry responsibility. It does **not** establish that EA issued an authority grant, interpreted a principal's preference, verified identity, created delegation, executed a response or owns the record of accountability.

## 2. Portfolio inventory

| Artifact | Type | Role in the portfolio | Status boundary |
| --- | --- | --- | --- |
| [DAOS parent case](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/README.md) | Bounded Case Study | Supplies T0–T2 facts and the CH-S1…14 source challenge surface. | Does not itself validate EA or every challenge. |
| [UC-EA-01](./UC-EA-01_v0.3_FROZEN.md) | Architecture-Validation Profile | Action-time operating-frame requalification. | Frozen internal validation profile; not an FG-TIDA submission. |
| [UC-EA-02](./UC-EA-02_v0.6_MAINTENANCE_FREEZE.md) | Architecture-Validation Profile | Bounded determination under incomplete, conflicting or partially scoped evidence. | Maintenance-frozen internal profile. |
| [UC-EA-03](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) | Architecture-Validation Profile | Effective human oversight under bounded capacity; approval does not repair contrary evidence. | Maintenance-frozen internal profile. |
| [UC-EA-04](./UC-EA-04_v0.5_MAINTENANCE_FREEZE.md) | Architecture-Validation Profile | Scope-indexed composition of locally valid determinations. | Maintenance-frozen internal profile. |
| [EA-ITP-01](./EA-ITP-01_v0.1_FROZEN.md) | Interoperability test profile | EHD / Theme #13 reciprocal cross-implementation handoff. | Separate from the four-profile family; not a fifth UC. |
| [00E — 100 million tokens](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) | Reference failure scenario and quality plan | Enterprise evidence-compression, overload, false strategy and unbounded-search stress route. | Fictional, reproducible quality-plan fixture; not a product result. |
| [00F — smart-city mobility divergence](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) | Reference failure scenario and quality plan | Multi-actor, shared-resource divergence and bounded requalification stress route. | Fictional, reproducible quality-plan fixture; not an incident report. |

## 3. Coverage scale

- **A — direct EA validation:** the artifact contains a decision path and acceptance/failure evidence for EA's stated responsibility.
- **B — boundary or supporting coverage:** the artifact invokes the requirement or tests preservation of a received determination, but does not independently validate the externally owned source function.
- **C — no dedicated fixture:** no current artifact supplies a concrete decision path and evidence plan for the requirement.

`A` and `B` are scope-specific. Neither means that the requirement is solved universally.

## 4. Canonical challenge coverage map

The T/H entries below are the normal routes from [00 §6.1](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md#61-challenge-to-condition-to-hypothesis-map). KPI families remain defined there; this table identifies which current cases exercise them and what evidence is still missing.

| Challenge | Canonical route | Existing case / fixture evidence | Coverage | Residual gap and required evidence |
| --- | --- | --- | --- | --- |
| **S1 — authority provenance and current applicability** | T2, T3 → H2, H4 | 00F Q0/Q3 consumes authority, owner and expiry; DAOS supplies the source boundary. | B | Independently produced grant, revocation and current-standing record; EA may only preserve/qualify it. |
| **S2 — preference fidelity and reviewable decision basis** | T2 → H1, H2 | 00E Q3 tests whether a strategic option preserves its evidence threshold, hard limits and decision relevance. | B | Principal-owned preference/version change and an independently reviewable decision-basis record. |
| **S3 — regime, context, escalation and bounded escape path** | T1, T2, T3, T4 → H1, H5, H6 | UC-EA-01 primary; 00E Q4; 00F Q1/Q4. | A | Replication under an independently operated source/receiver pair. |
| **S4 — human-inclusive oversight authority and capacity** | T2, T3, T4 → H1, H6 | UC-EA-03 primary; 00E Q2/Q4; 00F Q3. | A | External validation of the declared human lifecycle; EA does not appoint or assess reviewer competence. |
| **S5 — operational indeterminacy and containment** | T1, T2, T3, T4 → H1, H2, H5 | UC-EA-02 primary; 00E Q1/Q2/Q4; 00F Q1/Q2/Q3. | A | Independent execution of the declared containment owner/action, rather than EA inference of execution. |
| **S6 — interoperable, privacy-preserving trust determination** | T2, T4 → H2, H4 | UC-EA-02 secondary; 00E Q1; 00F Q2; EA-ITP-01 defines reciprocal EHD fixtures. | B | Executed independent producer/consumer fixture, including privacy/authorization constraints owned outside EA. |
| **S7 — identity and representation link** | T2, T3 → H2, H4 | No dedicated current case or reference-scenario gate. | C | Identity/role/substitute relationship from an external owner, preserved through a decision and response path. |
| **S8 — bounded subdelegation and non-amplification** | T2, T3 → H2, H4 | No dedicated current case or reference-scenario gate. | C | Delegation chain with purpose, scope, time, hard limits and revocation propagation. |
| **S9 — multi-principal composition, non-substitution and conflict** | T2, T4 → H2, H3, H4 | UC-EA-04 primary; 00E Q5; 00F Q0/Q2/Q5. | A | Cross-organization replication with independent evidence producers and declared arbitration owners. |
| **S10 — commitment state, material change and normal escalation** | T1, T2, T4 → H1, H5, H6 | UC-EA-01 secondary; 00E Q3/Q4; 00F Q1/Q4. | A | None for requirements coverage; broader domain replication remains useful. |
| **S11 — policy, objective and preference integrity across domains** | T2, T4 → H2, H3, H4 | UC-EA-04 secondary; 00E Q1/Q3/Q5; 00F Q2/Q5. | B | Source-owner version/priority conflict, showing EA preserves rather than sets policy or preference. |
| **S12 — accountability, challenge and repair** | T2, T4 → H4, H5 | 00E Q2/Q5 and 00F Q4/Q5 require targeted re-entry and observable outcome. | B | Independent decision, intervention, execution and outcome record that can be reconstructed without rewriting history. |
| **S13 — authority history versus intervention history** | T2, T3 → H2, H4 | UC-EA-03 secondary distinguishes approval from evidence; DAOS supplies the distinction. | B | Paired authority/intervention histories and an independent execution receipt. |
| **S14 — evidence-to-decision assessment** | T1, T2, T3, T4 → H1–H6 | All four UC-EA profiles; all 00E/00F Q0–Q5 gates; EA-ITP-01 at handoff. | A | Cross-case replication and independent adjudication, not a new requirement. |

## 5. What the current portfolio establishes

The four UC-EA profiles directly exercise the EA architecture's F1–F9 surfaces. The two reference scenarios make the same canonical requirements operational under different failure pressure: 00E stresses information compression, human overload and non-monotone resource use; 00F stresses shared-resource conflict, heterogeneous freshness and local-to-systemic divergence.

This is sufficient to test the EA-owned core around S3, S4, S5, S9, S10 and S14. It is not sufficient to claim end-to-end validation of all fourteen challenges. Across the portfolio, S1, S2, S6, S11, S12 and S13 have supporting/boundary coverage; S7 and S8 have no dedicated fixture.

## 6. Required next workbook: delegated decision integrity and accountable intervention

The missing priority is one **requirements-first validation workbook**, not a fifth generic EA function or a rewrite of DAOS:

> **WB-EA-01 — Delegated Decision Integrity, Revocation and Accountable Intervention**

It should describe one bounded cross-organization decision in which a principal's preference and hard limits are represented by an authorized delegate; a substitute human or agent acts under a time- and purpose-limited subdelegation; revocation or contextual invalidation is pending or arrives during the decision; a permitted intervention occurs; and the recorded execution must be distinguishable from the decision and reconstructable afterwards.

| Workbook element | Required content |
| --- | --- |
| Primary requirements | S1, S2, S7, S8, S12 and S13. |
| Supporting requirements | S3, S4, S5, S6, S10, S11 and S14 where material to the declared decision. |
| Quality plan | Matched Route N/Q evidence: no requirement is satisfied merely because a grant, approval or message exists; each selected S/T/H/KPI route has a gate, oracle, threshold, disposition and observable outcome. |
| External ownership | Identity/role, grant/delegation/revocation, policy/preference, action authority, execution record and accountability remain with named source owners. EA only qualifies, preserves, composes and requests re-entry. |
| Interface discipline | Apply [04](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part01.md) to every handoff; map the ideal bilateral route to [05](./05_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) only where needed; use [05A](./05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) solely to limit what is presently defensible in a FG-TIDA route. |
| Evidence needed | Independently produced records for identity/representation, grant/delegation, revocation, intervention, execution and outcome; a source/version/freshness/dependency trail; an observable effect and an independent reviewer/oracle where applicable. |

This one workbook closes the two absent fixtures, S7 and S8, and converts the current supporting treatment of S1, S2, S12 and S13 into an end-to-end, owner-preserving test. It does not turn EA into an identity, authority, execution or accountability system.

## 7. Sequencing and admission rule

1. Keep UC-EA-01…04 frozen and retain 00E/00F unchanged as the existing direct EA and failure-pressure evidence.
2. Use this map to draft WB-EA-01 from the requirements outward; select a concrete source case only after its primary S1/S2/S7/S8/S12/S13 route is fixed.
3. Run EA-ITP-01 with an independently operated producer and receiver. That is completion of an existing interoperability profile, not another use case.
4. Admit a later workbook only if it adds a challenge/evidence/owner combination not covered above. A new domain alone is not sufficient reason to duplicate a case.

## 8. Minimum reusable workbook record

Every future workbook should contain the following sections, in this order:

1. bounded case facts, `σ(d,t)`, owner, authority, deadline, null action and source boundary;
2. selected primary and secondary S# routes, with the complete T# conditions, H# expectations and KPI thresholds;
3. external-owner inputs and the EA boundary;
4. Route N and Route Q with the same resources, evidence, authority and time envelope;
5. interface classification: 04 generic requirement, 05 ideal bilateral target, 05A current-state limitation where relevant;
6. gate disposition, observable outcome, residual limitation and determination.

This order keeps requirements primary while allowing a case study or reference failure scenario to supply concrete evidence and a reproducible quality plan.
