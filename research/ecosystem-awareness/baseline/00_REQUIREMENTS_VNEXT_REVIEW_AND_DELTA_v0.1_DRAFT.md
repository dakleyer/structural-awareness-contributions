# Requirements vNext Review & Delta — Ecosystem Positioning

> **Working review only — not a new Requirements document.**  
> The current canonical requirements remain [00 — Canonical Requirements: S1–S14 / T1–T4 / H1–H6 / KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md).  
> This file reviews later Ecosystem Positioning developments against that existing requirement system. It does **not** create S15+, T5+, H7+, new canonical KPIs or a successor version.

| | |
|---|---|
| **ID** | Requirements-vNext Review |
| **Version · date** | v0.1-draft · cumulative review refreshed 24 September 2026 |
| **Status** | Working delta/review; no canonical requirement change |
| **Canonical requirements under review** | S1–S14 · T1–T4 · H1–H6 · KPI/falsification protocol |
| **Review window** | Frozen 00 Requirements baseline · 17 September 2026 → cumulative corpus state reviewed through 24 September 2026 |
| **Later corpus reviewed** | 00G · 00H · 01H · 01I · current 01J signalling/choreography · ACC Lineage · Regime Awareness delta · MSCA 00/03/04 · Objective-Conditioned Gradient · Decision Boundary Challenge v0.2 · Benchmark v0.3 draft · FG-TIDA application/test deltas |
| **Control route** | [Living Workplan — W1](../WORKPLAN.md) |

---

## Review provenance and freeze boundary

This delta exists because the canonical [00 Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) was frozen as the controlling S1–S14 / T1–T4 / H1–H6 / KPI baseline on **17 September 2026**, while the surrounding Ecosystem Awareness / Ecosystem Positioning corpus continued to evolve.

The purpose of this file is therefore not to rewrite the frozen baseline in place. It is to maintain an explicit **change-control layer** between:

1. the requirements that downstream work is currently allowed to rely on;
2. later architecture, control, signalling, positioning and validation material;
3. new reference failure scenarios that stress the requirements from additional directions; and
4. any future editorial or semantic change that may eventually justify a deliberately versioned Requirements successor.

A post-freeze document is not automatically a new requirement source. For every later development this review asks:

> **Does the new material reveal a genuinely missing solution-neutral requirement, or does it instantiate, clarify, test or provide evidence for a requirement that is already present?**

Only the first case could justify a future canonical Requirements change. Architecture objects, component vocabularies, test dispositions, benchmark hypotheses, scenario metrics and FG-TIDA mappings remain in their owning layers unless the review shows that the existing S/T/H system cannot express the required behaviour without distortion.

### Change-control rule

- The frozen 00 Requirements remains the controlling baseline for existing fixtures, benchmarks and traceability.
- This delta may evolve during review without changing the canonical Requirements.
- A later canonical edit, if ever justified, must be explicit, versioned and traceable back to the delta item that motivated it.
- Existing test runs and preregistrations continue to cite the Requirements commit/version they actually used; a later clarification does not retroactively rewrite their semantics.

---

## Post-freeze corpus change ledger

The following are the main substantive changes reviewed since the 17 September freeze. Routing, visual-navigation and source-refresh commits are not treated as requirement changes unless they alter a solution-neutral obligation.

| Post-freeze development | What changed / became explicit | Requirements-review consequence |
|---|---|---|
| **00G — Collective False-Context Convergence** | Adds a third reference failure family: correlated repetition, false corroboration, mission/context displacement, authority spoofing, effective-role drift and high-value but inadmissible opportunity pressure. The latest v0.3 Draft also makes the existing S1 authority-current-applicability surface explicit at the frame/role transition gate. | Stresses S1/S2/S3/S6/S9/S11/S14 and T1/T2/T3/T4 without exposing a missing S/T/H. It strengthens the case for an editorial role-drift clarification and for preserving opportunity/admissibility/authority separation. |
| **00H — Batch Opportunity Beyond Authority** | Adds a fourth reference failure family: a materially qualified opportunity lies outside the current grant. The v0.4 Draft preserves the prior causal/adaptive split and adds V19/V20 authority-laundering: individually valid leaf grants can compose into a common-root campaign whose root authority is absent. Review shows this does **not** require S15/H7: existing S7/S8/S9/S12/S13 already express representation, non-amplification, composition and reconstruction, especially S8's rule that subdelegation must not manufacture authority absent from the original principal. The gap was scenario coverage/instrumentation in 00H v0.3, now corrected in Q0/Q2/Q5; the legitimate route is preserve → request/re-contract → authority response → requalify → only then act. | Uses the existing S1/S2/S8/S11/S14 → T2/T3/T4 → H2/H4/H6 route. It materially strengthens the readability case for both `opportunity ≠ admissibility ≠ authority ≠ execution` and `per-action compliance ≠ aggregate/composed authorization`, but does not justify T5 or S15. |
| **01H — participant-local Ecosystem Positioning / decision-scoped epistemic opportunity** | Makes participant-local state, bounded epistemic opportunity and decision-relative effort allocation more explicit. | Existing S9/S11/S14 and T1/T2/T4 cover the solution obligation; the representation is architectural. |
| **01I / ACC-related participation and lineage work** | Makes role, participation, permissions/obligations/prohibitions, hard constraints, versioning, revocation/exit and lineage more explicit. | Existing S1/S2/S7/S8/S11/S12/S13/S14 cover the requirement surface. Do not promote ACC objects into universal Requirements merely because the current architecture uses them. |
| **Current 01J signalling / choreographed repositioning** | Adds selective participant-local signalling, bounded `RepositionIntent` / `AuthorityResponse`, compatibility/qualification boundaries and distributed choreography without requiring shared world-state. | Existing S6/S9/S11/S14 and T2/T3/T4 cover qualified handoff, authority preservation and bounded response. Transport objects remain implementation/interface semantics. |
| **Regime Awareness delta** | Makes material regime/context change a bounded, source-owned delta rather than a generic global state replacement. | Existing S3/S10/S14 and T1/T2/T4 remain sufficient; no new requirement is created by the `Δ_RA` representation. |
| **MSCA 00/03/04 evolution** | Makes control sufficiency, Type 0/1/2, P1/P2/P3 posture, effective-role drift, repositioning and authority-response separation operationally explicit. | Mostly component conformance. `Role_bound ≠ Role_effective` remains the strongest candidate for future Requirements wording clarification. |
| **Objective-Conditioned Agentic Gradient** | Makes opportunity ranking / marginal value of transition explicit while keeping admissibility and authority external. | T4/H6 already require decision-relevant bounded effort and T3 preserves authorization. Gradient semantics stay implementation-specific. |
| **Decision Boundary Challenge v0.2** | Consolidates CAN / KNOW / MAY / SHOULD / ACT review questions, Type condition, posture, DBC disposition and AuthorityResponse into separate namespaces; adds C01–C12 boundary fixtures. | Strong applied-validation pressure for existing requirements, especially S1/S3/S5/S7/S8/S10/S14 and T2/T3/T4. DBC is test/adjudication vocabulary, not a new canonical ontology. |
| **00D Benchmark v0.3 draft / EP-BH1…EP-BH7** | Adds bounded Ecosystem Positioning hypotheses covering drift-first repositioning, opportunity/admissibility separation, qualified signalling, objective-conditioned requalification, participant-local choreography, Type-gated posture and multi-resolution cartography. | Benchmark hypotheses must remain traced to existing S/T/H rather than becoming a hidden second requirement set. |
| **FG-TIDA application/test deltas** | The current UC-6 → Theme #16 v0.2 matrix → UC-4 executable-profile sequence makes authority applicability, human decision, execution confirmation and semantic-owner review more testable. | Useful external/interface evidence for S1/S4/S10/S13/S14 and T2/T3/T4. It does not create a new EA requirement or transfer Theme ownership. |
| **00E/00F named-technology source re-audits (24 Sep)** | Product/technology implementation profiles were date-pinned and evidence boundaries tightened for presentation use. | Evidence provenance improvement only. No solution-neutral Requirements change. |

---

## Reference failure-scenario expansion — two scenarios to four

At the 17 September freeze, the Requirements document explicitly routed two reference scenarios back into the same canonical requirement system:

1. [**00E — 100 Million Tokens and Compounded Epistemic Collapse**](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md), testing compositional overconfidence, capacity/oversight pressure, speculative promotion and structural-residual mismanagement; and
2. [**00F — Smart-City Mobility Divergence under Residual Uncertainty**](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md), testing incompatible locally justified closures, correlated/stale false convergence, shared-resource conflict and bounded ecosystem qualification.

The post-freeze corpus now adds two independent reference scenarios:

3. [**00G — Collective False-Context Convergence**](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md), testing whether unsupported external context, correlated repetition, claimed authority and attractive opportunity can displace a legitimate mission when source independence, role, authority and admissibility are not preserved; and
4. [**00H — Batch Opportunity Beyond Authority**](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.4_DRAFT.md), testing whether a valuable and technically reachable opportunity is preserved and routed without being silently discarded **or** converted into execution authority, including aggregate/salami-slicing failure and bounded re-contracting.

The four scenarios are deliberately different stress surfaces. They do **not** create four requirement families. Their role in this delta is to ask whether the same frozen S1–S14 / T1–T4 / H1–H6 system survives materially different failure mechanisms.

| Scenario | Primary new stress relative to the others | Current delta disposition |
|---|---|---|
| **00E** | Compounded epistemic collapse across exploration, aggregation, human review and alternative generation. | Pre-freeze source; retained canonical pressure. |
| **00F** | Systemic divergence / false convergence among independently governed actors competing over a shared operational surface. | Pre-freeze source; retained canonical pressure. |
| **00G** | Collective false-context convergence, mission displacement, source-correlation error and effective-role drift. | Post-freeze stressor; covered by existing S/T/H; strengthens CAND-R1/CAND-R2. |
| **00H** | Beneficial opportunity beyond current authority, aggregate authorization failure and legitimate re-contracting. | Post-freeze stressor; covered by existing S/T/H; strongly operationalizes CAND-R2 and supplies the concrete falsifier motivating CAND-R3. |

**Current conclusion from the 2→4 scenario expansion:** the requirement system has so far generalized without requiring a new challenge, sufficient condition or hypothesis. The added scenarios increase confidence in the *coverage review*, not confidence that EA satisfies the requirements. They also expose where editorial clarity may still be improved even when semantic coverage is already present.

---

## Pending scenario candidate — 00I is not yet a repository source

An external review supplied a proposed future traceability row for a possible **00I — Semantic TOCTOU / stale grant-condition revalidation** scenario. **No 00I file is present in the repository at this review point, so it is not included in the active post-freeze corpus ledger or the 2→4 scenario count.**

If/when that scenario is committed and its actual text is reviewed, the provisional route to verify is:

- S1, S3, S10, S14;
- T1/T2/T3/T4;
- H2/H5/H6;
- freshness/staleness, material-break/current-applicability and targeted-requalification evidence.

The anticipated requirement question is whether the scenario exposes anything beyond the existing distinction between **technical/token validity** and the **continued semantic applicability of the conditions that justified reliance**. The working expectation is **no new requirement**, with DBC-C02 already providing the current applied-validation expression of the same freshness/applicability boundary.

This paragraph is a **review placeholder only**. It must not be cited as 00I analysis or as evidence that 00I exists until the repository source is available and reviewed.

---

## 0. Executive determination

The cumulative post-freeze review — now including the expansion from two to four reference failure scenarios (00E–00H), the later Ecosystem Positioning architecture/control work and DBC v0.2 — does **not currently justify a new S15, T5, H7 or new canonical KPI family**.

Most later Ecosystem Positioning semantics fall into one of three categories:

1. **Already covered by the current solution-neutral requirements**, sometimes through more than one S/T/H route;
2. **Architecture/conformance choices** that instantiate those requirements but should not be promoted into universal requirements merely because EP uses them;
3. **Benchmark-specific measures** useful to test the later architecture without becoming new canonical requirements.

The strongest candidate for future clarification is **effective-role drift** (`Role_bound` versus `Role_effective`). Even there, the present review finds substantial existing coverage through S7, S10, S12, S13 and S14. If the canonical requirements are later broadened explicitly from the EA challenge to an EP-wide requirement specification, the preferred first action is a **clarification of those existing routes**, not creation of S15.

A second possible clarification is the explicit four-way separation:

`opportunity ≠ admissibility ≠ authority ≠ execution`.

The current requirements already distribute this boundary across S1/S2/S8/S11/S14 and T2/T3/T4. A future editorial clarification may make that separation easier to see, but no new sufficiency condition is presently required.

A third clarification candidate is the scope-of-authorization distinction exposed concretely by 00H:

`per-action compliance ≠ aggregate/composed authorization`.

The current requirements already cover authority scope, non-amplification, composition and evidence-to-decision assessment through S1/S8/S9/S10/S14 and T2/T3/T4. The candidate is therefore editorial/traceability clarification, not a new S15.

---

## 1. Review rule — requirement gap versus architecture gap

The current canonical Requirements document is intentionally **solution-neutral**.

A later EP object does not create a new requirement merely because it introduces a new noun, state or interface.

Examples:

- `Cart_i` is an EP/MSCA representation used to satisfy dependency/composition requirements; a universal candidate need not implement `Cart_i` by name.
- `Δ_RA` is an RA interface object used to qualify material regime change; a universal candidate may use another valid mechanism.
- P1/P2/P3 is the current MSCA operational posture vocabulary; T2 already requires an explicit posture vocabulary and transition conditions without mandating these three labels.
- `RepositionIntent` and `AuthorityResponse` are current signalling/transition objects; T2/T3/S14 require owner-preserving escalation/authorization semantics without mandating those object names.
- the Objective-Conditioned Agentic Gradient is an EP mechanism for ranking candidate transitions; T4/H6 already require decision-relevant, resource-bounded effort and T3 preserves authorization.
- ACC is a governance/participation mechanism; S1/S7/S8/S11/S12/S13 already define the authority, representation, subdelegation, policy, lineage and accountability surfaces a sufficiently-good candidate must preserve.

The W1 question is therefore:

> **Does the later architecture expose a genuinely missing solution requirement, or does it provide one implementation/conformance route for an already stated requirement?**

---

## 2. Later-concept delta table

| Later concept | Existing S/T/H/KPI coverage | Missing behaviour / evidence | W1 disposition |
|---|---|---|---|
| **00G false-context convergence / mission displacement** | S2, S3, S6, S9, S11, S14 · T1/T2/T4 · H2/H3/H4/H5/H6 · false convergence, correlated-evidence error, wrong-domain closure, handoff integrity, injected-doubt/cascade measures | 00G-specific mission-displacement and re-grounding measures are not canonical KPI names | **No new requirement.** Use scenario/benchmark-specific measures under existing routes. |
| **00H batch opportunity beyond authority / aggregate authorization** | S1, S2, S8, S11, S14 · T2/T3/T4 · H2/H4/H6 · authority-field completeness, aggregate-action trace, authorized-response compliance, response-horizon and requalification evidence | Opportunity-preservation, aggregate-authority and re-contracting measures are scenario/DBC measures rather than canonical KPI names | **No new requirement.** Strongly operationalizes the existing opportunity/admissibility/authority/execution separation and tests whether per-action compliance launders aggregate unauthorized action. |
| **DBC-C02 — semantic TOCTOU / stale applicability** | S1, S3, S10, S14 · T1/T2/T3/T4 · H2/H5/H6 · freshness/staleness, material-break detection, current applicability, targeted requalification and authorized-response evidence | The current Requirements distribute validity/freshness across authority applicability, material change, evidence-to-decision assessment and timely requalification; they do not name `semantic TOCTOU` as a standalone challenge | **No new requirement.** C02 tests a distinct freshness/applicability failure: a result, token or grant may remain technically valid while the semantic conditions that justified reliance have changed before use. This complements CAND-R2 from the freshness axis rather than the opportunity/authority axis. |
| **Participant-local positioning / 01H** | common `σ(d,t)`, W(d,t), non-fungibility · S9/S11/S14 · T1/T2/T4 · H2/H4/H6 | None at requirement level; participant-local representation is an architectural realization | **Existing mapping.** No requirement change. |
| **ACC admissibility / lineage / participation conditions** | S1, S2, S7, S8, S11, S12, S13, S14 · T2/T3/T4 · H2/H4/H6 · authority-field completeness, authorized-response compliance, handoff/lineage evidence | “Admissibility” is not named as its own universal layer, but policy/hard-limit/authority/delegation boundaries are already explicit | **Existing mapping; possible future vocabulary clarification only.** Do not create a new challenge merely to encode ACC. |
| **Selective signalling / receiver-side qualification / compatibility mode** | S6, S9, S11, S14 · T1/T2/T4 · H2/H3/H4/H5/H6 · handoff integrity, qualification loss, false convergence, correlated evidence, privacy/disclosure cost | Compatibility residual and signalling-profile mechanics are implementation/interface detail | **Existing mapping.** No new requirement. |
| **Objective-Conditioned Agentic Gradient** | S2, S3, S10, S11, S14 · T1/T3/T4 · H5/H6 · marginal decision value, evidence yield, deadline pass, response margin, authorized-response compliance | Opportunity-preservation / approved-beneficial-transition are not canonical KPIs | **No new requirement.** Treat those as benchmark-specific measures. Gradient is one implementation of resource/decision relevance. |
| **Reachable → ACC-admissible → executable transition sets** | S1/S2/S8/S11/S14 · T2/T3/T4 · H2/H4/H6 · authority completeness, response compliance, PNI where claimed | The four-way wording opportunity/admissibility/authority/execution is not presented as one explicit sentence in Requirements | **Possible clarification, not new T#.** Existing semantics already separate preference/policy, authority and response. |
| **Ecosystem Cartography `Cart_i / Δ_Cart,i`** | S9, S11, S14 · T1/T2/T4 · H2/H3/H4/H5 · known vs unmeasured dependencies, correlated-evidence error, residual preservation, cross-domain coupling, burden | Hidden-dependency recall is not a named canonical KPI; variable-resolution map is an implementation choice | **No new requirement.** Hidden-dependency recall may be a benchmark/fixture KPI under current H2/H3/H5. |
| **Regime Awareness `Δ_RA`** | S3, S10, S14 · T1/T2/T4 · H1/H5/H6 · material-break recall/precision, freshness, requalification latency, response margin | Qualified A/B/C/D regime-delta object is architecture-specific | **Existing mapping.** No new requirement. |
| **MSCA S/E/C/P/M sufficiency** | S2, S3, S5, S11, S14 · T2/T3/T4 · H1/H5/H6 · posture correctness, authorized response, burden, response margin | Current Requirements do not mandate the MSCA S/E/C/P/M kernel or its SUPPORTED/FAILED/UNRESOLVED state | **Keep as component conformance, not a new EA requirement.** If a future EP-wide Requirements specification is created, reassess whether control-sufficiency deserves an explicit solution-neutral challenge. |
| **Effective-role drift: `Role_bound ≠ Role_effective`** | S7 identity/representation · S10 material change · S12 accountability · S13 authority/intervention history · S14 transition assessment · T1/T2/T3/T4 · H1/H4/H5/H6 | Current S7 does not explicitly name observed effective function/behaviour versus bound role | **Clarification candidate.** Prefer extending/clarifying S7/S10/S12/S13 in a future version rather than creating S15. |
| **Type 0/1/2 operational catalogue** | failure-trajectory rule · S5/S14 · T2/T3/T4 · H1/H4/H5/H6 · Type-1↔Type-2 measures | Runtime `TypeCatalogue_i` is an MSCA 04 implementation object | **Fully covered at requirement level.** No new H/T/S. |
| **P1/P2/P3 hard posture gate** | T2 explicitly requires posture vocabulary, transitions, scope, owner, authority, expiry · T3 authorization · S3/S5/S14 · posture correctness, false continuation/containment, oscillation | P1/P2/P3 labels are architecture-specific | **No new requirement.** P1/P2/P3 remain MSCA operational semantics. |
| **RepositionIntent / AuthorityResponse / re-contracting** | S1, S3, S4, S8, S10, S12, S13, S14 · T2/T3/T4 · H2/H4/H6 · authority completeness, escalation capacity, handoff integrity, authorized-response compliance | Compound signalling object and response enum are architecture/interface details | **Existing mapping.** No new requirement. |
| **Participant-local choreography without shared world-state** | S6/S9/S11/S14 · T2/T4 (and T3 where action follows) · H2/H3/H4/H5/H6 · incompatible-posture exposure, cascade, handoff, burden | Graceful degradation under coordinator loss is not a universal EA requirement; it is an EP comparative proposition | **Benchmark hypothesis only.** Do not convert EP-BH5 into a canonical requirement. |

---

## 3. Requirements-vNext disposition by benchmark hypothesis

The bounded 00D v0.3 draft uses EP-BH1…EP-BH7. The table below prevents those hypotheses from becoming a hidden second requirement system.

| Benchmark hypothesis | Current requirement route | W1 finding | Requirements action now |
|---|---|---|---|
| **EP-BH1 — drift-first repositioning** | S7/S10/S12/S13/S14 · T1/T2/T3/T4 · H1/H4/H5/H6 | Covered in substance; `Role_effective` versus `Role_bound` is not named explicitly | **No new S/T/H.** Flag S7-role-drift clarification for any future version. |
| **EP-BH2 — opportunity / admissibility / execution separation** | S1/S2/S8/S11/S14 · T2/T3/T4 · H2/H4/H6 | Current requirements preserve objective/policy/authority/action separation but not the exact four-word EP chain | **No new S/T/H.** Optional future clarification; benchmark-specific opportunity metrics remain outside canonical KPI set. |
| **EP-BH3 — qualified signalling** | S6/S9/S11/S14 · T1/T2/T4 · H2/H3/H4/H5/H6 | Strong existing coverage, including false convergence, correlation, privacy/disclosure and handoff | **Existing mapping.** |
| **EP-BH4 — objective-conditioned requalification** | S2/S3/S10/S11/S14 · T1/T4 (+T3 for response) · H5/H6 | Current H6 already expresses risk/capacity calibrated window selection and marginal decision value | **Existing mapping.** Gradient remains implementation/comparator matter. |
| **EP-BH5 — participant-local choreography** | S6/S9/S11/S14 · T2/T4 (+T3 where action follows) · H2/H3/H4/H5/H6 | Requirements support bounded distributed composition, but do not mandate decentralized choreography | **Benchmark-only differential.** No requirement change. |
| **EP-BH6 — Type-gated posture** | S3/S4/S5/S14 · T2/T3/T4 · H1/H5/H6 | Type transitions, posture correctness, false continuation/containment and oscillation are already explicit | **Existing mapping.** |
| **EP-BH7 — multi-resolution cartography** | S9/S11/S14 · T1/T2/T4 · H2/H3/H4/H5 | Dependency/correlation/cross-domain requirements are present; variable-resolution Cartography is one implementation | **Existing mapping.** Hidden-dependency recall may be fixture/benchmark evidence, not new canonical KPI. |

### W1 conclusion for v0.3

The current benchmark draft can proceed with EP-BH1…EP-BH7 **without first creating new canonical requirements**, provided:

- every benchmark pre-registration cites the current Requirements commit it uses;
- component-specific Q0 conformance continues to reference MSCA/Gradient/ACC/01J owners directly;
- the v0.3 benchmark does not claim that EP-BH1…EP-BH7 are new universal Requirements hypotheses;
- any later canonical Requirements edit is versioned and does not rewrite the meaning of earlier test runs.

---

## 4. Genuine clarification candidates — not yet edits

The review now identifies three areas worth considering in a future Requirements edition.

### CAND-R1 — effective-role drift within S7 / S10 / S12 / S13

Current S7 requires the candidate to distinguish principal, organization/role, acting human/agent, instance/substitute and current representation relationship.

Later MSCA 04 makes an additional distinction operational:

`Role_bound ↔ Role_effective`.

A future wording change could clarify that a sufficiently-good representation/attribution route must be able to identify a **material observed function/behaviour mismatch with the bound role** without treating observed behaviour as proof of legitimate authority or membership. 00G now supplies a concrete mission-displacement / metamorphic-role stressor for that distinction, and DBC-C06 provides an applied validation route. The same clarification should preserve the guardrail that continuity of identity, name, runtime lineage or newly acquired capability does **not** by itself establish continuity or expansion of authority.

Why this is probably a clarification, not S15:

- S7 already owns identity/representation;
- S10 owns material state/context/authority change;
- S12 owns reconstructability;
- S13 separates authority history from intervention history;
- S14 owns evidence-to-decision transition assessment.

### CAND-R2 — make opportunity / admissibility / authority / execution separation visually explicit

The current requirements already state:

- preferences/hard limits and permitted trade-offs — S2;
- authority provenance/current applicability — S1;
- delegation/non-amplification — S8;
- policy/objective integrity — S11;
- evidence-versus-authority and arbitration owner — S14;
- authorized bounded response — T3;
- owner-preserving handoff — T2.

A future edition could add one sentence or reading aid stating:

`opportunity ≠ admissibility ≠ authority ≠ execution`.

00H now gives this separation a concrete failure and recovery path: a candidate can be reachable, well-evidenced and materially beneficial while remaining outside the current grant; the correct route is preserve/rank → check admissibility/authority → request or re-contract through the legitimate owner → requalify → only then execute if authorized. That strengthens the case for an editorial reading aid while still **not** creating T5 or a new challenge.

### CAND-R3 — per-action compliance does not establish aggregate authorization

00H exposes a boundary that is semantically covered by the current Requirements but not stated with enough visibility:

> **Compliance or authorization of each individual action does not by itself establish authorization of the cumulative or composed effect of a sequence of those actions.**

The concrete 00H failure is simple: every refund may satisfy a per-transaction cap while the aggregate campaign remains outside the participant's current grant. Treating each micro-action as independently sufficient can therefore launder an unauthorized aggregate outcome through a locally conforming sequence.

Current coverage already exists:

- **S1** requires current authority provenance, scope and applicability at action time;
- **S8** requires bounded delegation / non-amplification and prevents manufacture of authority outside the original grant;
- **S9** requires composition without silent substitution where multiple determinations or effects interact;
- **S10** requires detection of material commitment/action change;
- **S12/S13** preserve reconstructable authority and intervention history; and
- **S14** requires evidence-to-decision assessment at each transition, including the arbitration rule governing what advances.

T2/T3/T4 already require owner-preserving handoff, bounded authorized response and timely requalification. Therefore the present issue is not absence of a solution-neutral requirement family.

What is missing is **editorial explicitness about the unit of authorization**. A future Requirements edition could clarify that where the legitimate authority constraint is cumulative, campaign-level, resource-time-based or otherwise compositional, the determination must be made against the **material composed effect**, not only against each atomic action viewed in isolation.

This clarification should remain implementation-neutral. It must not mandate one universal aggregation window, one accounting schema or one centralized ledger. The applicable authority owner defines the relevant aggregate/composition boundary; the solution must preserve enough action/lineage state to avoid treating local compliance as proof of composed authorization.

Why this is probably a clarification, not S15:

- S1 already owns scope/current applicability of authority;
- S8 already owns non-amplification;
- S9 already owns composition/non-substitution;
- S10/S14 already own material-change and evidence-to-decision transition assessment; and
- 00H now provides the concrete falsifier showing why atomic compliance is insufficient when the authority condition is aggregate.

**Candidate reading aid:**

`per-action compliance ≠ aggregate/composed authorization`.

This candidate is independent of CAND-R2. CAND-R2 asks whether opportunity/admissibility/authority/execution are being collapsed. CAND-R3 asks whether the **scope of the authority check itself** is too narrow to cover the composed effect.

---

## 5. What should remain outside the canonical Requirements

The following are valuable current architecture semantics but should remain outside the universal Requirements unless a future scope decision explicitly broadens the specification:

- exact A/B/C/D object names for `Cart_i`, `Δ_RA`, `Π_MSCA` or `Π_RP`;
- S/E/C/P/M as the mandatory implementation schema;
- P1/P2/P3 as the only allowed posture labels;
- `RepositionIntent` / `AuthorityResponse` as mandatory transport objects;
- a mandatory ACC implementation;
- a mandatory agentic-gradient algorithm;
- a mandatory distributed/no-shared-state choreography;
- a particular Cartography data structure/resolution policy;
- a particular detector for Regime Awareness.

Those belong to architecture/component conformance.

The Requirements should remain capable of evaluating **another sufficiently-good architecture that solves the same problem differently**.

---

## 6. KPI disposition

No new canonical KPI family is currently required.

Later benchmark/test work may define **derived or scenario-specific measures** under the existing KPI protocol, including:

- drift-detection latency;
- unauthorized-transition rate;
- opportunity-preservation rate;
- approved-beneficial-transition rate;
- false-frame adoption / mission displacement;
- time to re-ground;
- genuine-change false-rejection;
- hidden-dependency recall;
- oscillation / settling time;
- outcome gap to orchestrated reference;
- aggregate-authority failure rate / cap-decomposition escape rate;
- targeted re-contracting / recovery rate;
- source-independence error under correlated repetition;
- mission-displacement and re-grounding latency;
- stale-basis use rate / semantic-TOCTOU detection and targeted-requalification rate.

These measures should be linked back to the relevant H#/T#/S# and clearly labelled as benchmark/fixture measures unless and until a future Requirements version adopts them as canonical.

This preserves the current rule that an operational measure is not automatically a second hypothesis or a new universal KPI.

---

## 7. Scope decision still open

There are two legitimate future directions:

### Option A — keep 00 Requirements as the EA / solution-neutral requirements basis

Under this option:

- current S1–S14/T1–T4/H1–H6 remain the universal decision-basis requirements;
- later EP components use their own conformance documents;
- 00D v0.3 combines requirement coverage with component conformance and comparative hypotheses;
- no EP-wide Requirements successor is needed unless a genuine solution requirement appears.

### Option B — create a future EP-wide Requirements successor

Only if later review establishes that the broader Positioning architecture requires universal solution conditions not expressible without distortion in the existing system.

If that decision is ever made, it must:

- preserve the current 00 Requirements as predecessor;
- distinguish EA-owned challenge semantics from MSCA/RA/ACC/external-owner requirements;
- avoid turning current EP implementation objects into mandatory universal schemas;
- preserve all benchmark/pre-registration citations to the older requirement version.

**Current W1 recommendation: Option A.**

---

## 8. W1 determination

**Current recommendation:** do **not** create or modify the canonical Requirements beyond a visible link to this review.

The current requirement system is broad enough to support the bounded Benchmark-vNext design if:

1. EP-BH1…EP-BH7 remain benchmark hypotheses, not new canonical H#;
2. later component conformance is tested against the component-owner documents;
3. benchmark-specific metrics are traced to existing S/T/H routes;
4. Role_effective/Role_bound, opportunity/admissibility/authority/execution, and per-action compliance versus aggregate/composed authorization remain explicit clarification candidates for a future editorial/versioned pass;
5. any future change is versioned and preserves the requirement commit used by existing fixtures/pre-registrations.

This closes the **analysis stage of W1** for the corpus state reviewed through 24 September 2026 without creating a canonical Requirements successor. The review now includes the 00E–00H four-scenario set and DBC v0.2. Future post-freeze material should be added to this delta first and should reopen W1 only if it exposes a genuinely missing solution-neutral obligation rather than another architecture, interface, scenario or conformance realization.

The next W1 action, if desired, is an editorial proposal containing only the three clarification candidates above. It should remain a proposal until explicitly approved.
