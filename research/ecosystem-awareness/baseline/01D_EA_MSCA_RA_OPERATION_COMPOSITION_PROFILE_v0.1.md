# Annex 01D — EA / MSCA / Regime Awareness operation-composition profile

**Status:** candidate integration profile, v0.1, 15 September 2026. This is an additive working annex, outside the six-document controlled EA v0.4 release baseline. It is a design and test surface, not an implemented interface, a completed pilot, a safety certification, a normative ITU-T artefact, or proof that the three programmes already interoperate.

## 1. Why a joint profile is needed

[Annex 01B](./01B_EA_MSCA_INTERFACE_ANNEX_v0.1.md) describes EA↔MSCA handoffs; [Annex 01C](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.1.md) describes EA↔Regime Awareness (RA) handoffs. A live operation may consume both. Pairwise reports alone do not prove that an RA departure signal, EA mission-frame determination, MSCA supported configuration and action permit all refer to **the same decision, scope, version and useful time interval**. The profile below makes that composition inspectable without imposing one implementation stack.

The RA [anchor paper](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/) defines a representation-relative detector and a separately bounded action-safety requirement. The [MSCA working paper](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/) and [EA Functional Architecture v0.4](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md) assign control sufficiency and mission-frame qualification to distinct functions. This annex proposes an operation-level compatibility test across them; it is **not** stated as a result of either source.

## 2. Operation binding and dependency set

A legitimate decision owner first declares an operation identifier, objective envelope S, affected mission/domain, time horizon, response deadline and authority owner. EA identifies material dependencies and tolerable residual uncertainty. The control owner declares which evidence and capability dependencies are **required for this particular decision or action**. RA is not a universal prerequisite: an independent authorized MSCA action need not be blocked merely because an optional RA monitor lacks context. If an action is explicitly triggered or justified by an RA posture, however, that RA evidence and its action-safety declaration enter the required set.

| Binding item | Versioned content to retain | Owner / consequence of mismatch |
|---|---|---|
| Operation and mission | Operation/decision ID; S and owner approval; domain, stakeholders, horizon, as-of/expiry | Mission/authority owner. A different S or stakeholder domain requires a fresh decision binding. |
| EA qualification | Q operating-frame version, W(d,t) observation boundary, material dependencies, scope-indexed residual, F6 determination and freshness | EA supplies a qualified assessment; it does not issue a permit. Residual may remain if explicitly tolerable for S. |
| RA evidence, when required | Observation map Ψ, admitted context H_t(m) and T* status, Δ/τ/ℓ, invariant/baseline version, event/as-of time, P_RA, representation and detection limits | RA producer. A stale baseline, incompatible scope or unqualified context cannot be treated as neutral evidence. |
| RA response claim, when required | Action-library version, A(P_RA)/null action, admissible states, stakeholders, utility U, horizon, PNI or weaker bounded-downside status, response feasibility | RA Safety Governor/action-design owner. A claim for another action or utility domain is not portable. |
| MSCA sufficiency | E operating environment, S binding, supported C/P_MSCA/M configuration and evidence, preconditions, contingency and assessment status | MSCA assessors/operators. SUPPORTED is scoped; UNRESOLVED cannot be silently recoded as SUPPORTED. |
| Authority and execution | Reachable actor/mandate, permit or refusal, permit target/version/expiry, dispatch recheck, receipt and separately observed effect | Legitimate authority/control owner. Evidence or a feasible proposal is never an execution permit. |
| Feasibility and cost | Useful action deadline, acquisition/processing/response latencies, compute, intervention and human-attention cost, available capacity | Owners jointly assess one decision horizon; cost is not counted twice or assumed zero. |

The symbol P_RA denotes RA directional posture; P_MSCA denotes the MSCA intervention/planning dimension. They are **not the same variable**. Similarly, RA neutral (P_RA = 0) is not EA Normal Operation, and RA Pointwise Non-Inferiority (PNI) is not an MSCA proof of S/E/C/P_MSCA/M sufficiency.

## 3. Candidate eligibility rules and precedence

For an **RA-triggered live action**, the receiving gate should check the conjunction below immediately before dispatch, under the declared dependency set and action deadline:

1. **Mission binding:** the owner-approved S, action domain, stakeholders and horizon still match the operation. EA's Q/F6 assessment is current and sufficient for this S **within its recorded residual tolerance**; absence of omniscience is not itself failure.
2. **Qualified RA input:** Ψ and admitted context preserve the scoped change distinction Δ above the practical threshold τ within delay ℓ. The report is fresh and its baseline/threshold/version remains admitted. A posture for an unsupported context is unavailable, not zero.
3. **Response safety:** the proposed action is in the current authorized action library, and its PNI or explicitly weaker downside claim applies to the *same* admissible states, stakeholder/utility domain and horizon. PNI is not inferred from good detection, reversibility, a low average false-alarm cost or another system's permit.
4. **Control sufficiency and authority:** MSCA's C/P_MSCA/M assessment is SUPPORTED for current S/E and its versioned preconditions; actor mandate, action reach, permit target and expiry are checked separately. A permit from old E or old authority cannot be carried forward merely because RA evidence is fresh.
5. **Useful feasibility:** the remaining acquisition + evaluation + permit + execution latency fits the decision horizon; the combined operating cost/capacity record is admissible for this decision. A theoretical finite computation or safe action may still be too late or too burdensome.
6. **No material unresolved incompatibility:** source dependence, known conflicting evidence or changed assumptions are preserved; any essential unresolved item requests targeted requalification. There is no automatic conversion of UNKNOWN to RA neutral, MSCA SUPPORTED or EA Normal.

An unmet **essential** condition blocks that RA-triggered live dispatch; it does not censor the diagnostic signal, force a universal shutdown, or authorize another action. The legitimate owner/control function chooses any authorized bounded fallback. If RA is merely advisory and **not** in the declared dependency set for a separate action, its unavailability is reported but does not automatically veto that independent action. No layer may silently widen another layer's scope: S/authority comes from the owner, RA evidence cannot grant a permit, an MSCA permit cannot repair RA's representation or action-safety claim, and an EA determination cannot certify PNI.

## 4. RA payload state semantics (correction to Annex 01C)

The proposed I-RA-03 message needs an explicit *qualification state* independent of its numeric/directional posture.

| Qualification state | P_RA field | Required report behaviour |
|---|---|---|
| QUALIFIED_COMPATIBLE | Present, value 0 only if Ψ/context/baseline/threshold are qualified and fresh for the declared Δ/τ/ℓ | Report relative compatibility and exclusions; never claim global stability. |
| QUALIFIED_DIRECTIONAL_DEPARTURE | Present, value −1 or +1 under declared sign semantics | Report scope, confidence/limits, freshness and approximate instability zone. |
| UNRESOLVED_CONTEXT / UNSUPPORTED_REPRESENTATION / STALE_BASELINE / EXPIRED | **Absent or explicitly UNKNOWN; never 0** | Name the failed contract and requested re-test; no posture-dependent live action. |
| DETECTION_UNRESOLVED_WITH_QUALIFIED_CONTEXT | Absent or UNKNOWN unless the source's rule can legitimately return a qualified neutral result | Preserve detection uncertainty rather than laundering it into compatibility. |

These are **candidate interface states**, not four new outputs claimed by the RA paper. Its source-defined three-way directional posture applies only after the representation and context contracts are admitted. An expiry or material re-anchoring invalidates the previous posture for this operation and routes a targeted I-RA-05 request.

## 5. One decision-wide cost and utility envelope

The mission/authority owner owns the decision's stakeholder, horizon and admissible-action scope. RA action design evaluates U(A(P_RA),ω) versus U(A_null,ω) only in its declared covered state domain; MSCA assesses supported control means and their intervention burden; EA F1/F2/F6 assesses residual, determination capacity, acquisition value and useful response margin. The operation record **joins**, but does not mathematically identify, these judgments.

A candidate cost ledger distinguishes (a) evidence acquisition, (b) RA computation/false-signal and human attention, (c) MSCA coordination/planning/actuation, (d) permit/governance, and (e) outcome evaluation/requalification. Shared staff or compute are attributed once to the operation, with a declared allocation rule. Utility horizons, stakeholder sets and null-action baselines must be compatible before a joint net-benefit statement is made; otherwise the statement is UNRESOLVED. RA strict PNI, even if established for its bounded response, does **not** imply MSCA minimum burden, zero attention cost, mission fulfilment or economic viability of the entire composite.

## 6. Invalidation and falsification tests

Any material change in S, Q, E, Ψ/context/baseline, Δ/τ/ℓ, action library/U/stakeholders, C/P_MSCA/M, authority, permit, costs or remaining deadline invalidates **only the dependent claims**. The dependency owner requests requalification and retains the previous evidence as historical evidence, not current approval. A new RA report cannot extend an old MSCA permit; a fresh permit cannot turn an RA UNKNOWN into neutral. Receipt and separately measured effect feed EA F9 and both source programmes' evaluation without silently closing missing-outcome state.

| Test | Injected variation | Expected observable result |
|---|---|---|
| T1 — race between signal and permit | RA P_RA = +1 and action claim fresh; MSCA permit still bound to previous E or expired actor mandate | RA evidence retained diagnostically; no RA-triggered dispatch until S/E/configuration/mandate/permit are rechecked. |
| T2 — insufficient context | Ψ does not preserve Δ or no identifiable finite H_t(m) | I-RA-03 qualification reports unsupported/UNKNOWN; P_RA absent, not 0; EA keeps residual and requests bounded context repair. |
| T3 — stale baseline | Re-anchoring, regime mixing or freshness expiry after a qualified neutral report | Old P_RA = 0 cannot be reused; affected RA and EA assumptions requalify. |
| T4 — scope mismatch | RA report for a different S, utility horizon, stakeholder or Δ | No action-claim portability; state the mismatch without discarding reusable source evidence. |
| T5 — separate authorized action | RA advisory monitor unresolved, but an independently supported MSCA action does not depend on RA | No automatic veto from optional RA; still check the independent S/E/configuration/mandate/permit and EA frame. |
| T6 — false-positive cost | Proposed RA response has positive net downside for an admitted no-change state | Do not claim strict PNI; assess weaker bounded downside or change the authorized response. |
| T7 — budget double counting | Same human reviewer appears in RA warning response and MSCA permit path | One attributed attention/latency cost; if remaining horizon becomes infeasible, no composite live-action approval. |
| T8 — receipt without effect | Dispatch receipt arrives, no independent effect evidence | Keep outcome unresolved; reopen EA F9 and MSCA/RA evaluation as applicable. |

Each test is a **proposal**. No benchmark result, pilot pass or institutional validation is asserted. Existing [EA validation profiles](../validation/) and the RA [paper's theoretical/empirical claim separation](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/) are inputs to an eventual test design, not evidence that these joint tests have run.

## 7. Architectural disposition

The independent review found no need to rewrite the six frozen EA F1–F9 baseline documents. It identified a **composition gap** between two pairwise working annexes. This profile closes the *documentation* gap by fixing operation binding, conditional dependency, payload nullability, utility/cost ownership and falsifiable race conditions. Implementation, safety proof, economic evidence, interprogramme validation and standards disposition remain open.
