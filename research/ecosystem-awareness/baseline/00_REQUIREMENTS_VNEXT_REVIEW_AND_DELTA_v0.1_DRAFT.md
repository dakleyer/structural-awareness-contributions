# Requirements vNext Review & Delta — Ecosystem Positioning

> **Working review only — not a new Requirements document.**  
> The current canonical requirements remain [00 — Canonical Requirements: S1–S14 / T1–T4 / H1–H6 / KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md).  
> This file reviews later Ecosystem Positioning developments against that existing requirement system. It does **not** create S15+, T5+, H7+, new canonical KPIs or a successor version.

| | |
|---|---|
| **ID** | Requirements-vNext Review |
| **Version · date** | v0.1-draft · 23 September 2026 |
| **Status** | Working delta/review; no canonical requirement change |
| **Canonical requirements under review** | S1–S14 · T1–T4 · H1–H6 · KPI/falsification protocol |
| **Later corpus reviewed** | 00G · 01H · 01I · 01J · ACC Lineage · MSCA 00/03/04 · Gradient Law · Benchmark v0.3 draft |
| **Control route** | [Living Workplan — W1](../WORKPLAN.md) |

---

## 0. Executive determination

The review does **not currently justify a new S15, T5, H7 or new canonical KPI family**.

Most later Ecosystem Positioning semantics fall into one of three categories:

1. **Already covered by the current solution-neutral requirements**, sometimes through more than one S/T/H route;
2. **Architecture/conformance choices** that instantiate those requirements but should not be promoted into universal requirements merely because EP uses them;
3. **Benchmark-specific measures** useful to test the later architecture without becoming new canonical requirements.

The strongest candidate for future clarification is **effective-role drift** (`Role_bound` versus `Role_effective`). Even there, the present review finds substantial existing coverage through S7, S10, S12, S13 and S14. If the canonical requirements are later broadened explicitly from the EA challenge to an EP-wide requirement specification, the preferred first action is a **clarification of those existing routes**, not creation of S15.

A second possible clarification is the explicit four-way separation:

`opportunity ≠ admissibility ≠ authority ≠ execution`.

The current requirements already distribute this boundary across S1/S2/S8/S11/S14 and T2/T3/T4. A future editorial clarification may make that separation easier to see, but no new sufficiency condition is presently required.

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

The review found two areas worth considering in a future Requirements edition.

### CAND-R1 — effective-role drift within S7 / S10 / S12 / S13

Current S7 requires the candidate to distinguish principal, organization/role, acting human/agent, instance/substitute and current representation relationship.

Later MSCA 04 makes an additional distinction operational:

`Role_bound ↔ Role_effective`.

A future wording change could clarify that a sufficiently-good representation/attribution route must be able to identify a **material observed function/behaviour mismatch with the bound role** without treating observed behaviour as proof of legitimate authority or membership.

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

That would improve readability but would **not** create T5 or a new challenge.

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
- outcome gap to orchestrated reference.

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
4. Role_effective/Role_bound and opportunity/admissibility/authority/execution remain explicit clarification candidates for a future editorial/versioned pass;
5. any future change is versioned and preserves the requirement commit used by existing fixtures/pre-registrations.

This closes the **analysis stage of W1** without creating Requirements vNext.

The next W1 action, if desired, is an editorial proposal containing only the two clarification candidates above. It should remain a proposal until explicitly approved.
