# Canonical Architecture Benchmark v0.3 Draft — Ecosystem Positioning

> **Benchmark vNext — bounded working draft.** This document complements, but does **not yet supersede**, [00D v0.2](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md). v0.2 remains the current canonical benchmark for the EA differential `EA-H1–EA-H4` under B0–B3.  
> **Reason for this draft:** the public architecture has expanded from EA alone to the broader **Ecosystem Positioning** composition (EA + Regime Awareness + MSCA + signalling + ACC/authority + repositioning). v0.2 cannot test most of those later claims.  
> **Evidence status:** design only. No new comparative result, novelty claim, product ranking, standards adoption or validation is asserted here.

| | |
|---|---|
| **ID** | 00D-vNext |
| **Version · date** | v0.3-draft-bounded · 23 September 2026 |
| **Status** | Working draft for review; v0.2 remains canonical |
| **Architectural scope owner** | Ecosystem Positioning |
| **Benchmark / evidence host** | Ecosystem Awareness corpus |
| **Component owners** | Remain with EA, RA, MSCA, ACC/signalling and legitimate governance/authority owners |
| **Primary predecessor** | [00D v0.2](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) |
| **Control route** | [Living Workplan — W1/W2/W3](../WORKPLAN.md) |

---

## 0. Why v0.3 exists

v0.2 remains valid for what it actually measures: the EA differential, its requirements mapping, B0–B3 fairness contract, evidence grades, 00E/00F reference-scenario evidence and the current pre-execution benchmark programme.

What changed afterwards is the **unit under test**.

The current architectural contribution now composes:

- participant-local EA qualification `Π_EA,i(d,t)`;
- EHD / bounded handoff;
- qualified Ecosystem Signalling and `ReceivedSignals_i`;
- MSCA Ecosystem Cartography `Cart_i / Δ_Cart,i`;
- Regime Awareness `Δ_RA`;
- MSCA sufficiency over S/E/C/P/M;
- effective-role drift and Type 0/1/2 qualification;
- P1 Normal / P2 Containment / P3 Migration posture;
- the Objective-Conditioned Agentic Gradient;
- ACC / lineage / authority gating;
- `Π_RP`, `RepositionIntent`, `AuthorityResponse` and bounded role/contract transition.

Therefore v0.3 asks a narrower and more defensible question than “is Ecosystem Positioning novel?”:

> **Does the composed EP architecture improve a declared outcome–burden–accountability frontier, or preserve the same outcome with a measurably simpler accountable surface, relative to strong peers under the same facts, authority, resources and deadlines?**

The benchmark is explicitly designed so that the answer may be **no**, or that some components may prove unnecessary in a given envelope.

---

## 1. What v0.2 still owns

Until v0.3 is adopted, v0.2 remains the authority for:

- evidence grades E1–E4;
- B0–B3 matched-resource fairness contract;
- EA-H1–EA-H4;
- C1–C8 benchmark branches;
- 00E and 00F evidence/plausibility records;
- the common outcome vector;
- pre-registration discipline;
- result-class logic;
- the claim boundary that no comparative superiority is yet established.

This draft does **not** silently rewrite those items.

Where v0.3 later changes an item, the change must be explicit, versioned and traceable.

---

## 2. Precondition and benchmark questions

v0.3 separates **conformance** from comparative questions.

### Q0 — conformance precondition

Before an EP arm can support a comparative claim, verify that it actually instantiates the EP semantics being attributed to it:

- correct component ownership;
- four-component A/B/C/D semantics without cross-object fungibility;
- drift checked before opportunity ranking;
- posture separated from actuation;
- opportunity separated from admissibility;
- admissibility separated from authority;
- authority separated from execution;
- preserved ACC/lineage and external authority boundary;
- signalling treated as qualified input, not command;
- no hidden global-state or super-controller assumption unless the arm is explicitly the OR reference.

A non-conforming EP implementation produces **Insufficient evidence**, not an EP win/loss.

### Q1 — requirement coverage

Can a named, configured architecture satisfy the applicable current S#/T#/H#/KPI gates under frozen facts, authority, resources and deadlines?

### Q2 — component contribution

Within an EP stack, which modules change the declared outcome–burden–accountability frontier, and which show no incremental contribution in the tested envelope?

### Q3 — composition differential

Does the full EP composition beat, or match with a simpler accountable surface:

1. the strongest current industry peer;
2. the strongest faithfully implemented prior-art composition;
3. an orchestrated shared-state reference where that reference is meaningful?

A positive Q3 result is **bounded support in the tested envelope**, not uniqueness, universal superiority or safety.

---

## 3. Unit under test and ownership

| Module | Owner | Isolated proposition to test |
|---|---|---|
| **M1 — EA qualification + EHD** | EA / 01H / 04 | Decision-scoped qualification and bounded handoff reduce false closure without blanket HOLD. |
| **M2 — Ecosystem Signalling** | 01J | Receiver-side qualification resists correlated/spoofed reinforcement while retaining genuine change. |
| **M3 — Ecosystem Cartography** | MSCA 03 | Qualified variable-resolution dependency representation exposes material hidden coupling at bounded burden. |
| **M4 — Regime Awareness** | RA / 01C | A qualified regime delta is useful without taking ownership of posture. |
| **M5 — MSCA sufficiency** | MSCA 00 | S/E/C/P/M sufficiency changes when objective, frame, authority or capability changes. |
| **M6 — drift + Type catalogue + posture** | MSCA 04 | Drift-first Type-gated P1/P2/P3 reduces both unsupported continuation and indefinite HOLD. |
| **M7 — Agentic Gradient** | Gradient Law | Objective-conditioned ranking improves adaptation without creating authority. |
| **M8 — ACC / lineage / authority transition gate** | ACC profile + MSCA 04 + external authority | Attractive but inadmissible/unauthorized opportunities remain visible without unauthorized execution. |

Human/institutional governance and physical/digital actuation are **not EP components under test**. They remain external legitimate owners and are modelled as source/latency/authority conditions.

---

## 4. Provisional benchmark hypotheses

To avoid collision with the canonical requirements hypotheses H1–H6, v0.3 uses the namespace **EP-BH# = Ecosystem Positioning Benchmark Hypothesis**.

These hypotheses remain **provisional until W1 Requirements-vNext maps them explicitly to S1–S14 / T1–T4 / H1–H6 / KPI or identifies a justified requirements extension**.

| ID | Provisional benchmark hypothesis | Primary modules | Decisive falsifier |
|---|---|---|---|
| **EP-BH1 — drift-first repositioning** | Detecting material `Role_effective ≠ Role_bound` before ranking opportunity, and ranking from `Role_effective`, reduces unauthorized transitions without increasing bounded HOLD/paralysis. | M6 + M7 | A strong peer detects/handles the same drift with equal or lower unauthorized-transition rate, latency, HELD time and burden. |
| **EP-BH2 — opportunity / admissibility / execution separation** | Evaluating reachable opportunity first, then distinguishing ACC-admissible and currently authorized/executable subsets, preserves beneficial requests without unauthorized execution. | M7 + M8 | A constrained-utility/shield peer plus ordinary escalation reaches the same approved-beneficial-transition rate and zero unauthorized execution in the declared fixture at equal/lower burden. |
| **EP-BH3 — qualified signalling** | Receiver-qualified signalling reduces false-frame adoption/mission displacement under correlated or spoofed reinforcement without materially increasing rejection of genuine regime change. | M1 + M2 | A signed/provenanced peer or trust-fusion peer matches the adoption/displacement/error frontier at equal/lower burden. |
| **EP-BH4 — objective-conditioned requalification** | Directing requalification toward expected objective-risk reduction improves the decision–burden–deadline frontier relative to uncertainty magnitude or fixed schedules. | M1 + M4 + M7 | A strong value-of-information / active-sensing peer reaches an equal or better frontier under the same objective, resources and horizon. |
| **EP-BH5 — participant-local choreography** | Qualified participant-local positioning degrades more gracefully than a comparable peer under partition/coordinator loss while remaining acceptably close to an orchestrated reference under nominal conditions. | M2 + M3 + M6 + M7 | EP oscillates/diverges more than the peer under partition or exceeds the preregistered outcome gap to the OR reference under nominal conditions. |
| **EP-BH6 — Type-gated posture** | Cataloguing material state as Type 0/1/2/NOT_ESTABLISHED before P1/P2/P3 reduces both Type-1 forced closure and Type-2 continuation relative to strong runtime-assurance switching. | M6 | A well-tuned runtime-assurance peer matches posture correctness, false-containment, false-continuation and forced-closure rates at equal/lower burden. |
| **EP-BH7 — multi-resolution cartography** | Qualified variable-resolution cartography improves material hidden-dependency recall over no map while costing less than full-detail representation. | M3 | A strong provenance/dependency/uncertainty-aware graph reaches equal recall and decision quality at equal/lower burden. |

No component-level novelty is asserted by these hypotheses.

---

## 5. Comparator architecture

### 5.1 Industry arms

v0.2 B0/B1 remain unchanged.

**B2 — strong interoperable control peer (current configuration)** must be configured with the strongest materially relevant available capabilities rather than a historical weak stack, including where applicable:

- signed/cryptographically bound agent identity;
- declarative runtime/tool policy enforcement;
- provenance/lineage;
- state/checkpointing;
- explicit structured handoff;
- cross-system tracing/evaluation;
- human escalation;
- dependency/context representation already available to that substrate.

The exact product/protocol capabilities used in B2 must be pinned in the pre-registration. Capability names alone are not evidence.

**Standards-boundary inheritance from v0.2.** B2 should credit relevant existing primitives at full strength, including workload identity/authentication such as SPIFFE/SPIRE, subject/actor token exchange such as RFC 8693, and attestation/appraisal such as RFC 9334 RATS. Their documented boundaries must also be preserved: authentication is not authorization policy; RFC 8693 token exchange does not create a general persistent input/output-token linkage or general revocation-propagation semantics; and RATS Attestation Results remain inputs to a relying party's own application-specific decision. NIST's 2026 NCCoE software/AI-agent identity-and-authorization work is treated as current standards-context evidence, not as endorsement of this architecture. See the canonical v0.2 benchmark §5.1 for the source-grounded boundary statement.

### 5.2 EP build-up ladder

The build-up ladder is useful for observing when capabilities appear, but **is not by itself sufficient for causal attribution**.

| Step | Modules present |
|---|---|
| **B3.1** | B2 + M1 |
| **B3.2** | B3.1 + M2 |
| **B3.3** | B3.2 + M3 |
| **B3.4** | B3.3 + M4 |
| **B3.5** | B3.4 + M5 |
| **B3.6** | B3.5 + M6 |
| **B3.7** | B3.6 + M7 |
| **B3.8 — full EP** | B3.7 + M8 |

### 5.3 Leave-one-module-out attribution

For every component-level conclusion, run the full EP stack with one module removed or replaced:

`EP-full – M1`, …, `EP-full – M8`.

A module is **not** called redundant merely because its marginal effect in one build-up order is zero.

Permitted result wording:

> **No incremental contribution detected in this envelope/order.**

A stronger “redundant in this envelope” determination requires:

- no material incremental contribution in the build-up;
- no material degradation in leave-one-module-out;
- no material interaction effect in any preregistered interaction test.

### 5.4 Interaction ablations

Only preregister interactions with clear architectural reasons. Initial candidates:

- **M2 × M3** — signalling × cartography;
- **M6 × M7** — drift/posture × gradient;
- **M7 × M8** — gradient × ACC/authority gate.

---

## 6. Prior-art reference arms — provisional families

This draft does **not yet freeze a publication bibliography**. The exact sources, versions and faithful implementations must be independently verified before adoption.

The benchmark should nevertheless reserve these strong peer families:

| Arm | Reference mechanism family | Main target |
|---|---|---|
| **PA-1** | belief/uncertainty + trust/provenance fusion | M1/M2 |
| **PA-2** | runtime assurance / Simplex-style monitored fallback | M6 |
| **PA-3** | value-of-information / active sensing / constrained decision selection | M4/M7 |
| **PA-4** | normative multi-agent / electronic-institution / role & norm monitoring | M6/M8 |
| **PA-5** | strongest defensible composition of PA-1…PA-4 under the same resource envelope | Q3 composition differential |
| **OR** | orchestrated shared-state reference with realistic latency | nominal upper/reference bound for EP-BH5 |

### OR boundary

OR is a **reference**, not a strawman.

- Under nominal conditions, OR estimates the value of shared-state orchestration.
- Under coordinator loss/partition, the main differential should be EP versus strong distributed peers (B2/PA-5), not EP versus an intentionally failed centralized design.
- If an HA/redundant orchestrator is relevant, it should be modelled as a separate configured peer.

---

## 7. Additional branch catalogue — provisional C9–C15

C1–C8 remain owned by v0.2.

| Branch | New positioning-layer condition | Minimum conforming behaviour |
|---|---|---|
| **C9 — effective-role drift** | Behaviour already differs materially from `Role_bound`. | Record `Role_effective`; qualify drift before opportunity; do not legitimize drift merely because it occurred. |
| **C10 — authority / ACC change** | Grant or ACC changes, expires or is revoked mid-operation. | Requalify affected scope; preserve lineage; do not execute cached authority. |
| **C11 — adversarial reinforcement** | Correlated repetition, Sybil/spoofed authority or mission-memory pressure. | Preserve dependence; qualify authority; resist false corroboration. |
| **C12 — attractive inadmissible opportunity** | High-value reachable transition lies outside ACC and/or authority. | Keep opportunity visible; request legitimate change/authority; no unauthorized execution. |
| **C13 — partition / coordinator loss** | Participant loses shared coordinator/state or suffers high latency. | Continue only within qualified local scope; avoid forced global consensus; bound oscillation. |
| **C14 — slow authority response** | Authority response exceeds the useful response horizon. | Apply bounded escalation/expiry/fallback; do not convert silence to permission. |
| **C15 — legacy / partial compatibility** | Partner lacks full EHD/signalling semantics. | Use receiver-side bounded compatibility; preserve translation residual; narrow reliance. |

These branches are **scenario-supported test surfaces**, not executable fixtures until admitted through W3.

---

## 8. Measurement additions

Retain the v0.2 common outcome vector and requirement/KPI measures.

Add only the measures needed for later positioning claims:

- unauthorized-transition rate;
- drift-detection latency;
- approved-beneficial-transition rate;
- opportunity-preservation rate;
- false-frame adoption / mission displacement;
- genuine-change false-rejection rate;
- posture correctness;
- false-containment / false-continuation;
- Type-1→Type-2 forced-closure rate;
- hidden-dependency recall;
- oscillation count and settling time;
- outcome gap to OR;
- disclosure cost.

### Complexity / accountability surface

A “same outcome with simpler accountable composition” claim must be preregistered.

Use at least:

1. **semantic obligations** — distinct fields/contracts/gates that must be produced or interpreted;
2. **decision gates** — points capable of changing posture/transition;
3. **normalized configuration burden** — rules/policy/profile/adapter AST nodes or equivalent normalized units, not raw lines of code;
4. **audit reconstruction effort** — reviewer time/steps **and reconstruction error** on fixed blinded traces.

Do not declare “simpler” using an arbitrary two-of-four rule. Compare arms on a preregistered Pareto/equivalence basis with explicit tolerances.

---

## 9. Requirements traceability gate

Before this draft can replace v0.2, W1 Requirements-vNext must produce a delta table for every EP-BH#:

| Benchmark hypothesis | Current S/T/H/KPI route | W1 finding | Requirements disposition |
|---|---|---|---|
| **EP-BH1 — drift-first repositioning** | S7/S10/S12/S13/S14 · T1/T2/T3/T4 · H1/H4/H5/H6 | Covered in substance; `Role_effective` versus `Role_bound` is not named explicitly | **No new S/T/H.** Future S7/S10/S12/S13 clarification candidate only. |
| **EP-BH2 — opportunity / admissibility / execution** | S1/S2/S8/S11/S14 · T2/T3/T4 · H2/H4/H6 | Objective/policy/authority/action boundaries already exist; the exact EP chain is not one explicit reading rule | **No new S/T/H.** Optional future clarification; opportunity metrics remain benchmark-specific. |
| **EP-BH3 — qualified signalling** | S6/S9/S11/S14 · T1/T2/T4 · H2/H3/H4/H5/H6 | False convergence, correlation, privacy/disclosure and handoff are already covered | **Existing mapping.** |
| **EP-BH4 — objective-conditioned requalification** | S2/S3/S10/S11/S14 · T1/T3/T4 · H5/H6 | H6 already covers risk/capacity-calibrated window selection and marginal decision value | **Existing mapping.** |
| **EP-BH5 — participant-local choreography** | S6/S9/S11/S14 · T2/T4 (+T3 where action follows) · H2/H3/H4/H5/H6 | Requirements support distributed composition but do not mandate decentralized choreography | **Benchmark-only differential.** No requirement change. |
| **EP-BH6 — Type-gated posture** | S3/S4/S5/S14 · T2/T3/T4 · H1/H5/H6 | Type transitions, posture correctness, false continuation/containment and oscillation are already explicit | **Existing mapping.** |
| **EP-BH7 — multi-resolution cartography** | S9/S11/S14 · T1/T2/T4 · H2/H3/H4/H5 | Dependency/correlation/cross-domain requirements already exist; variable-resolution Cartography is an implementation | **Existing mapping.** Hidden-dependency recall remains a benchmark/fixture measure. |

**W1 review result:** the current canonical requirements are sufficient to host the bounded Benchmark-vNext design without creating S15+, T5+, H7+ or a new canonical KPI family. Component-specific conformance continues to come from the owning architecture documents. The detailed review is [Requirements vNext Review & Delta v0.1 Draft](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).

This prevents the benchmark from creating a second hidden requirements system.

---

## 10. Staged execution route

| Stage | Content | Evidence ceiling |
|---|---|---|
| **0 — harness integrity** | RS-00E-Q1a instrumentation + determinism under operative pre-registration | Descriptive harness evidence only |
| **1 — continuity controls** | Valid-continuity/null branches for every relevant comparator family | Confirms arms do not “win” by blanket HOLD |
| **2 — EA baseline** | v0.2 EA-H1–EA-H4 / B0–B3 programme | EA differential only |
| **3 — module attribution** | B3 build-up + leave-one-module-out + selected interactions | Component contribution in tested envelopes |
| **4 — positioning branches** | C9–C12/C14 with 00G/authority fixtures | Positioning-layer comparative evidence |
| **5 — distributed choreography** | C13 / multi-actor 00F with B2, PA-5 and OR reference | Distributed resilience/choreography evidence |
| **6 — replication** | Independent re-run of any supportive result | Independent bounded support |

Every comparative arm that supports a differential claim should have a named defender. A self-configured comparator may produce descriptive evidence but no strong differential claim.

---

## 11. Prior-art proximity — no novelty rating yet

This draft intentionally does **not** label any EP component “likely unique”.

The working prior is:

- most individual mechanisms have close prior art;
- ACC/normative participation is deliberately close to normative MAS/electronic-institution work;
- value-of-information and runtime-assurance families are intentionally strong peers;
- role drift may contain a narrower compositional differential, but that claim requires dedicated prior-art review;
- the strongest defensible EP claim, if any, is likely to be **composition and decision-order**, not primitive invention.

Candidate compositional differential to test:

1. shared four-component A/B/C/D **structural pattern** across separately owned objects, without semantic fungibility;
2. strict separation of:
   - assessment;
   - posture;
   - opportunity;
   - admissibility;
   - authority;
   - actuation;
3. drift qualification before opportunity ranking;
4. preservation of attractive but currently inadmissible/unauthorized opportunities as explicit requests rather than either execution or erasure.

If PA-5 or B2 reproduces this composition at equal or lower burden/accountability surface, the EP differential fails for that envelope.

---

## 12. What is supported now

Supported by the current public corpus:

- v0.2 is insufficient to benchmark the whole current EP architecture;
- the later architecture has separately owned components and explicit conformance/falsification boundaries;
- 00G supplies additional signalling/false-context test pressure;
- MSCA 04 makes drift qualification precede opportunity/repositioning closure;
- Gradient Law separates reachable opportunity, ACC-admissible transitions and currently authorized/executable transitions;
- current test design is materially ahead of execution.

Not supported now:

- that full EP beats B2 or PA-5;
- that any individual EP component is novel;
- that role-drift control has no equivalent prior art;
- that choreography converges;
- that EP improves safety;
- that 00G, C9–C15 or the v0.3 comparator families have executed;
- that this draft has passed the Requirements-vNext or bibliographic gate.

---

## 13. Adoption gates for v0.3

v0.3 becomes the canonical benchmark only after all of the following are complete:

1. **W1 Requirements-vNext delta:** every EP-BH# is mapped to the current requirement system or a justified versioned requirements change.
2. **Prior-art source audit:** PA-1…PA-5/OR bibliography and claimed mechanism boundaries are verified against primary sources.
3. **Industry comparator audit:** B2 capabilities are pinned to dated primary vendor/standard documentation.
4. **Ablation protocol:** build-up, leave-one-module-out and selected interaction tests are frozen.
5. **Complexity protocol:** normalized complexity/accountability measures and equivalence margins are preregistered.
6. **Fixture admission:** at least the first positioning-specific branch family is specified well enough to execute.
7. **Conservation:** v0.2 is preserved unchanged as predecessor and all existing pre-registrations continue to cite their original benchmark/requirements commits.

Until those gates are met:

> **v0.2 remains current canonical; v0.3 remains Benchmark vNext.**

---

## 14. Relation to the larger 23 September draft

A larger v0.3 design draft was prepared on 23 September 2026 with expanded industry/prior-art tables, EP hypotheses, ablation, new branches and a staged execution programme.

This bounded draft deliberately retains the **architectural and experimental structure** of that proposal while deferring source-sensitive prior-art ratings and detailed industry claims until verification. It also tightens:

- benchmark ownership;
- Q0 conformance versus Q1–Q3 benchmark questions;
- hypothesis namespace;
- module attribution;
- reachable → admissible → executable opportunity semantics;
- complexity/accountability measurement;
- adoption gates.

The larger draft remains useful as working material, but publication-sensitive bibliography and component distinctness assessments should not be promoted into the canonical route without the explicit audits above.
