# China Unicom / FG-TIDA Theme #23 — privilege restoration under changing ecosystem context

**DDS campaign:** DDS-A-CU-PLM-EA-01  
**Edition:** v0.1, 14 October 2026  
**Owner of this research preparation:** Iván Abril Palma / The Integral Management Society (EA research corpus)  
**External source authors:** Ying Wang and Ye Tao, China Unicom, proposers of [FG-TIDA Theme #23](https://github.com/FG-TIDA/themes/issues/23)  
**Status:** IN_DEVELOPMENT_NOT_PREREGISTERED · NOT_FROZEN · NOT_EXECUTED · NOT_INDEPENDENTLY_ADJUDICATED  
**External participation/endorsement:** NOT_ESTABLISHED. Ying Wang has publicly welcomed exploring the hibernation example, not approved this campaign or its test contract.

## 1. Why this campaign exists

Theme #23 specifies security requirements around AI-agent authorization and the privilege lifecycle: initialization, changes/propagation, hibernation, activation, revocation/recovery and lifecycle governance. In [her reply on 14 October 2026](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309), Ying answered the three questions raised by Iván on 30 September. She proposes context-sensitive restoration, reevaluation in the receiving agent's operational context, explicit partial/unverifiable revocation outcomes, and optional ecosystem-awareness signals. She invites further exploration of the hibernation case.

This dossier turns that invitation into a **local, first-version DDS Stage A specification-discovery campaign**. Its object is an **interface and decision requirement**, not a China Unicom product, implementation or approved ITU-T specification.

**Core question:** Following hibernation, can a competent authorization system distinguish (i) legitimate restoration, (ii) restoration made unsafe by a materially changed dependency and (iii) restoration not justified because the relevant context is only partially assessable—without promoting unknown evidence into permission or unnecessarily blocking unrelated legitimate action? What, if anything, does an optional EA-qualified handoff add beyond competent conventional authorization?

The initial primary challenge is one bounded example. Inter-agent propagation and revocation visibility remain related future branches, not silently merged into the first scored claim.

## 2. Distinct campaign, clear ownership

- **Independent of Flores:** [DDS-A-FLORES-POP-EA-01](../flores-population-ea/CAMPAIGN.md) studies population-evaluation evidence and a separate source owner's experiment. No Flores data, results, fixtures, consent, acceptance or maturity transfer here.
- **China Unicom's scope:** Theme #23, privilege lifecycle, PDP/PEP authorization architecture and source-authored risk requirements belong to their authors. This dossier cannot claim to speak for, test, represent or commit China Unicom.
- **EA's scope:** Ecosystem Awareness qualifies decision-relevant provenance, dependencies, scope, freshness, source relationships and uncertainty; it may request targeted requalification. EA does **not** grant, revoke, restore or enforce privileges.
- **External dependencies:** Theme #16 owns human-intervention lifecycle; relevant Theme #33 proposals concern evidence-driven reevaluation; UC-4/UC-21 may be future test environments only after separate admission.
- **Technical evidence:** At v0.1 this is a documentary Stage A preparation package. No external acceptance, joint laboratory, benchmark result, product access or operational differential has been established.

## 3. DDS identity and scope

**Method:** [Canonical DDS Index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) · [DDS Stage A Challenge–Trajectory Profile](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md).

| DDS descriptor | v0.1 declaration |
|---|---|
| Stage and coverage | **DDS Stage A — Simplified, in preparation** |
| Object under test | Candidate requirement and optional semantic handoff for context-aware privilege restoration |
| Authoritative reference | Prospective bounded Challenge, decision owner, legitimate action scope and independently fixed expected outcomes—not EA's own output |
| Source base | FG-TIDA Theme #23, Iván's question, Ying's 14 October response, Zhao's 9 October restore-condition suggestion |
| Candidate mapping | Competent native authorization/PDP versus same native PDP with EA-qualified context interface |
| Stage 1 extension / correspondence | Documentary, partial correspondence only; no proven isomorphism or inherited theorem |
| Stage 2 non-isomorphic mechanisms | Candidate qualified context handoff, dependency cross-domain preservation and targeted requalification; not validated as genuinely differential |
| Trajectory / local gates | Suspension → material change/no-change → activation request → evidence review → PDP decision → enforcement/oversight feedback |
| Evidence mode | Source review, analytic test design, planned synthetic calibration; no executed experimental trace |
| DDS surfaces in scope | Challenge, source/authority boundaries, comparators, admissible/prohibited outcomes, falsifiers, positive controls, preparation of blind oracle |
| Unscored now | Quantified Cost/Risk/Effectiveness, probabilities, confidence thresholds, business-value projection and Type-1 frequency |
| Source-/oracle-private boundary | Future withheld dependency truth, admissibility labels, planted changes and independent expected observations; no blind run claimed |
| Acceptance | **NOT_ESTABLISHED** until protocol/fixtures/expected outcomes frozen before a result-producing study |
| Next-stage promotion | Stage B architecture verification and Stage C implementation validation require separate frozen specifications and evidence |

This is one DDS method with Stage A/B/C; internal gates in the protocol are **trajectory gates**, not additional DDS stages.

## 4. Bounded challenge CU-HIB-01

A crisis-response agent has a time-/scope-bounded authority to isolate resource R. Its privileges are suspended during hibernation. While suspended, a distinct service S becomes critically dependent on R. The grant identifier, agent identity and cited policy may appear unchanged. At activation, blindly restoring the full isolation privilege risks interrupting S.

**Decision owner:** The authorized Policy Decision Point (PDP), applying the current mandate and risk policy; not EA.  
**Permitted decisions to be modeled:** Full restoration when justified; a separately authorized restricted permission when justified; hold/reassessment/re-authorization; rejection/revocation. Human review is a governed path, not a new source of privilege by itself.  
**Prohibited outcome:** Exercise of isolation authority after a material invalidation of its current applicability, or conversion of missing coverage into a favorable full-restoration verdict.  
**Legitimate control:** A still-valid restoration in an unchanged, fully qualified context must not be blocked merely because EA is available.

The initial test must distinguish **authorization validity**, **operational context sufficiency** and **actual exercise/enforcement**. A formally valid token or unchanged policy is not proof that exercising the action is appropriate now.

## 5. Functional boundary and hypothesis

~~~text
Source-owned identity/grant/policy + runtime/credential state ───────► PDP
Domain-owned dependencies, criticality and scoped trust signals ─────► PDP
                                           └► optional EA/EHD qualification ─► PDP
PDP decision ─► PEP enforcement (or bounded pending/re-authorization)
                         ▲
Theme #16 human decision/authority, only through its defined interface
~~~

A strong conventional PDP may already ingest and qualify all pertinent context, detect drift, and restore safely. **Parity is a valid outcome.** EA earns no credit from extra input, easier cases, a weaker baseline, undisclosed oracle facts or longer resource budgets.

**Candidate differential:** Under equivalent access, authority, time horizon and resource budgets, an explicit qualified handoff might improve recognition and preservation of material cross-domain uncertainty, lineage and re-entry conditions. The competing null is that competent existing authorization logic already achieves the same admissible outcomes and burden.

The [Scientific Design](SCIENTIFIC_DESIGN.md) sets the comparison; the [Interface Contract](INTERFACE_CONTRACT.md) preserves component ownership; the [Trial Protocol](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md) sets the proposed experiments.

## 6. Study sequence and decision boundaries

| Phase | Work | Required evidence / stop condition |
|---|---|---|
| A0 — Source fidelity | Confirm Ying's intended semantics and distinguish published statements from our interpretation | Source register, dated comments, unresolved questions |
| A1 — Challenge | Agree a single receiving decision, authority basis, time horizon and material violation | Bounded independent oracle specification |
| A2 — Conventional peer | Permit a competent PDP with intent, graph context, current NACL/policy/credential state, monitoring and risk-specific fallback | Full configuration and positive controls, not an artificial weak baseline |
| A3 — Freeze | Freeze conventional repair, EA generic interface, context access, budgets, action policy, controls and expected observations | Hashes/commit and independent reviewer before scored reveal |
| A4 — Perturbation | Introduce one material, permitted context change after freeze, preserving the original grant/policy where the case requires | Planted-event evidence isolated from evaluated arms |
| A5 — Traversal | Compare complete conventional configuration with optional EA-qualified path | Trace of source evidence, decisions, restricted/full actions, timing, escalation and recovery |
| A6 — Adjudication | Score correct closure, improper restoration, false hold, UNKNOWN fidelity and cost | Independent reference, legitimate positive, parity and negative results retained |
| A7 — Stage A handoff | Specify only supported requirement/interface deltas, open contradictions and falsifiers | Versioned candidate package; Stage B readiness decision, not automatic promotion |

Before A3–A6, the campaign remains preparation only. Its protocol is a proposal, not a preregistration or run.

## 7. Deliverables and reading order

1. **[Scientific Design](SCIENTIFIC_DESIGN.md)** — threat/failure assumptions, Stage A comparison, outcomes and falsifiers.
2. **[Interface Contract](INTERFACE_CONTRACT.md)** — producer/consumer, decision/enforcement boundary, EA handoff and UNKNOWN propagation.
3. **[Trial Protocol v0.1](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md)** — primary single-change experiment, positive/negative vectors and freeze design.
4. **[Sources and Custody](SOURCES_AND_CUSTODY.md)** — independent primary record links, source rights and claim boundaries.
5. **[Run Card Preparation](RUN_CARD_PREPARATION.md)** — required commitments and explicitly empty result record.
6. **[Continuation](CONTINUATION.md)** — bounded work plan, owner decisions and versioning.
7. **[Machine-readable campaign record](CAMPAIGN.json)** — scope/status/relations for registry tooling.

## 8. Business and standardization relevance — not a validation claim

If a reliable interface can preserve changing cross-domain dependency and confidence limits, it may reduce unauthorized interruption, unnecessary blanket suspension and the cost of reconstructing remote context at reactivation. These are **candidate operational value drivers**, not demonstrated savings or a product claim. Any specification-level contribution would require confirmed stakeholder meaning, frozen conformance rules, competent comparators and successful external review; publication here confers none of those.

**Decision at v0.1:** Open a distinct local China Unicom Theme #23 research campaign. Keep the hibernation case primary, both other Theme #23 questions as later extensions, and all evidence/ownership limits explicit. Do not report any Stage A pass, Stage B verification, Stage C validation, joint China Unicom campaign or ITU adoption.
