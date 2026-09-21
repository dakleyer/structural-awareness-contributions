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
| [EA-ITP-01](../fg-tida/tests/EA-ITP-01_v0.1_FROZEN.md) | Interoperability test profile | EHD / Theme #13 reciprocal cross-implementation handoff. | Separate from the four-profile family; not a fifth UC. |
| [00E — 100 million tokens](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) | Reference failure scenario and quality plan | Enterprise evidence-compression, overload, false strategy and unbounded-search stress route. | Fictional, reproducible quality-plan fixture; not a product result. |
| [00F — smart-city mobility divergence](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) | Reference failure scenario and quality plan | Multi-actor, shared-resource divergence and bounded requalification stress route. | Fictional, reproducible quality-plan fixture; not an incident report. |

## 3. Coverage scale

- **A — direct EA validation:** the artifact contains a decision path and acceptance/failure evidence for EA's stated responsibility.
- **B — boundary or supporting coverage:** the artifact invokes the requirement or tests preservation of a received determination, but does not independently validate the externally owned source function.
- **C — no dedicated fixture:** no current artifact supplies a concrete decision path and evidence plan for the requirement.

`A` and `B` are scope-specific architecture-coverage labels. Neither means that the requirement is solved universally, that a fixture has been implemented or that it has executed. The next three columns make that distinction visible.

## 4. Canonical challenge coverage map

The T/H entries below are the normal routes from [00 §6.1](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md#61-challenge-to-condition-to-hypothesis-map). “Named” identifies a gate or profile that invokes the route; “fixture” identifies an executable branch; “execution” records actual evidence. None is inferred from another.

| Challenge | Canonical route and KPI family | Named in gate/profile | Architecture coverage | Fixture status | Execution status | Residual gap and required evidence |
| --- | --- | --- | --- | --- | --- | --- |
| **S1 — authority provenance and current applicability** | T2, T3 → H2, H4; authority-field completeness, residual preservation, authorized-response compliance. | 00F Q0/Q3; RS-00F-C1/C2. | B | Planned RS-00F-C1/C2. | Not executed. | Independently produced grant, revocation and current-standing record; EA may only preserve/qualify it. |
| **S2 — preference fidelity and reviewable decision basis** | T2 → H1, H2; local determinacy margin, qualified-posture correctness, residual preservation. | 00E Q3; RS-00E-Q1c-R/NR. | B | Planned Q1c pair. | Not executed. | Principal-owned preference/version change and independently reviewable decision-basis record. |
| **S3 — regime, context, escalation and bounded escape path** | T1, T2, T3, T4 → H1, H5, H6; material-break recall/precision, false continuation, latency, deadline pass. | UC-EA-01; 00E Q4; 00F Q1/Q4; RS-00E-Q1b/Q1e/Q4/N0. | A | Planned listed fixtures. | Not executed. | Replication under independently operated source/receiver pair. |
| **S4 — human-inclusive oversight authority and capacity** | T2, T3, T4 → H1, H6; human-capacity binding, forced closure, response margin, deadline pass. | UC-EA-03; 00E Q2/Q4; 00F Q3; RS-00E-Q2/Q4. | A | Planned Q2/Q4. | Not executed. | External validation of declared human lifecycle; EA does not appoint or assess reviewer competence. |
| **S5 — operational indeterminacy and containment** | T1, T2, T3, T4 → H1, H2, H5; explicit indeterminacy, false continuation, Type transitions, containment recovery. | UC-EA-02; 00E Q1/Q2/Q4; 00F Q1/Q2/Q3; planned 00E fixture set. | A | Planned Q1/Q2/Q4 and controls. | Not executed. | Independent execution of containment owner/action, rather than EA inference of execution. |
| **S6 — interoperable, privacy-preserving trust determination** | T2, T4 → H2, H4; handoff integrity, qualification loss, retained fields, latency/bandwidth/privacy cost. | UC-EA-02; 00E Q1; 00F Q2; EA-ITP-01. | B | EA-ITP-01 specified; no independent fixture yet. | Not executed. | Independent producer/consumer run with privacy/authorization constraints owned outside EA. |
| **S7 — identity and representation link** | T2, T3 → H2, H4; authority-field completeness, provenance/freshness preservation, handoff integrity. | No dedicated current gate. | C | No fixture. | Not executed. | Identity/role/substitute relation from external owner, preserved through decision and response. |
| **S8 — bounded subdelegation and non-amplification** | T2, T3 → H2, H4; scope/expiry completeness, inherited indeterminacy, unauthorized-response rate. | No dedicated current gate. | C | No fixture. | Not executed. | Delegation chain with purpose, scope, time, hard limits and revocation propagation. |
| **S9 — multi-principal composition, non-substitution and conflict** | T2, T4 → H2, H3, H4; incompatible-posture exposure, false convergence, correlated-evidence error, re-entry precision. | UC-EA-04; 00E Q5; 00F Q0/Q2/Q5; RS-00E-Q1a/Q1c, RS-00F-C1/C2. | A | Planned listed fixtures. | Not executed. | Cross-organization replication with independent evidence producers and declared arbitration owners. |
| **S10 — commitment state, material change and normal escalation** | T1, T2, T4 → H1, H5, H6; material-break recall/precision, freshness, latency, response margin, evidence yield. | UC-EA-01; 00E Q3/Q4; 00F Q1/Q4; RS-00E-Q1b/Q4. | A | Planned Q1b/Q4. | Not executed. | Broader domain replication remains useful. |
| **S11 — policy, objective and preference integrity across domains** | T2, T4 → H2, H3, H4; owner/version/scope preservation, wrong-domain closure, qualification loss. | UC-EA-04; 00E Q1/Q3/Q5; 00F Q2/Q5; RS-00F-C1. | B | Planned C1. | Not executed. | Source-owner version/priority conflict, showing EA preserves rather than sets policy or preference. |
| **S12 — accountability, challenge and repair** | T2, T4 → H4, H5; handoff integrity, targeted re-entry, containment recovery, observable outcome effect. | 00E Q2/Q5; 00F Q4/Q5; RS-00E-Q1c-R/NR. | B | Planned Q1c pair. | Not executed. | Independent decision, intervention, execution and outcome record reconstructable without rewriting history. |
| **S13 — authority history versus intervention history** | T2, T3 → H2, H4; authority/provenance preservation, authorized-response compliance, action/outcome trace. | UC-EA-03; DAOS; RS-00F-C2. | B | Planned C2. | Not executed. | Paired authority/intervention histories and independent execution receipt. |
| **S14 — evidence-to-decision assessment** | Aggregate of the common outcome vector, condition-specific KPI/trajectory sets and precedence record. | All UC-EA profiles; 00E/00F; EA-ITP-01; all listed fixtures only for their named component. | Aggregate — not scored A/B/C. | Component-specific planned fixtures; no standalone S14 fixture. | Not executed. | Cross-case replication and independent adjudication; see the five components in 00 §6.1.1. |

## 5. What the current portfolio establishes

The four UC-EA profiles directly exercise the EA architecture's F1–F9 surfaces. The two reference scenarios make the same canonical requirements operational under different failure pressure: 00E stresses information compression, human overload and non-monotone resource use; 00F stresses shared-resource conflict, heterogeneous freshness and local-to-systemic divergence.

This is sufficient to design tests of the EA-owned core around S3, S4, S5, S9 and S10. It is not sufficient to claim an executed test or end-to-end validation of all fourteen challenges. S14 is aggregate, not a breadth score. Across the portfolio, S1, S2, S6, S11, S12 and S13 have supporting/boundary coverage; S7 and S8 have no dedicated fixture.

## 6. Required next workbook: delegated decision integrity and accountable intervention

The missing priority is one **requirements-first validation workbook**, not a fifth generic EA function or a rewrite of DAOS:

> **WB-EA-01 — Delegated Decision Integrity, Revocation and Accountable Intervention**

It should describe one bounded cross-organization decision in which a principal's preference and hard limits are represented by an authorized delegate; a substitute human or agent acts under a time- and purpose-limited subdelegation; revocation or contextual invalidation is pending or arrives during the decision; a permitted intervention occurs; and the recorded execution must be distinguishable from the decision and reconstructable afterwards.

| Workbook element | Required content |
| --- | --- |
| Primary requirements | S1, S2, S7, S8, S12 and S13. |
| Supporting requirements | S3, S4, S5, S6, S10, S11 and S14 where material to the declared decision. |
| Quality plan | Configuration under test and pre-registered comparator under the same resource, evidence, authority and time envelope: no requirement is satisfied merely because a grant, approval or message exists; each selected S/T/H/KPI route has a gate, oracle, threshold, disposition and observable outcome. |
| External ownership | Identity/role, grant/delegation/revocation, policy/preference, action authority, execution record and accountability remain with named source owners. EA only qualifies, preserves, composes and requests re-entry. |
| Interface discipline | Apply [04](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) to every handoff; for FG-TIDA-specific testing, map the ideal bilateral route through [05](../fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) only where needed and use [05A](../fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) solely to limit what is presently defensible from public FG-TIDA sources. |
| Evidence needed | Independently produced records for identity/representation, grant/delegation, revocation, intervention, execution and outcome; a source/version/freshness/dependency trail; an observable effect and an independent reviewer/oracle where applicable. |

This one workbook closes the two absent fixtures, S7 and S8, and converts the current supporting treatment of S1, S2, S12 and S13 into an end-to-end, owner-preserving test. It does not turn EA into an identity, authority, execution or accountability system.

## 7. Sequencing and admission rule

1. Run the Stage-0 harness self-test, then pre-register the atomic 00E Q1 branches, Q2, Q4 and 00F composition branches with their controls.
2. Seek an independently operated EA-ITP-01 producer/receiver pair in parallel. The 90-day clock starts only once the dated counterpart ledger contains a named candidate, role, owner and contact record.
3. If no counterpart is secured after that 90-day search, record the outreach evidence and begin WB-EA-01 with the limit visible rather than blocking it.
4. Use Stage-0 results to constrain WB-EA-01 from the requirements outward; select its concrete source case only after its primary S1/S2/S7/S8/S12/S13 route is fixed.
5. Admit a later workbook only if it adds a challenge/evidence/owner combination not covered above. A new domain alone is not sufficient reason to duplicate a case.

## 8. Minimum reusable workbook record

Every future workbook should contain the following sections, in this order:

1. bounded case facts, `σ(d,t)`, owner, authority, deadline, null action and source boundary;
2. selected primary and secondary S# routes, with the complete T# conditions, H# expectations and KPI thresholds;
3. external-owner inputs and the EA boundary;
4. configuration under test and pre-registered comparator with the same resources, evidence, authority and time envelope;
5. interface classification: 04 generic requirement, 05 ideal bilateral target, 05A current-state limitation where relevant;
6. gate disposition, observable outcome, residual limitation and determination.

This order keeps requirements primary while allowing a case study or reference failure scenario to supply concrete evidence and a reproducible quality plan.
