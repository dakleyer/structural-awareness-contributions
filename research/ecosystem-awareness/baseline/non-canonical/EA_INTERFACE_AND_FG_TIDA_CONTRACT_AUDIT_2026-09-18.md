# EA interface and FG-TIDA contract audit — 18 September 2026

> **Status: non-canonical audit.** This is a source-pinned review, not a change to the EA interface taxonomy, a claim of FG-TIDA adoption, or a request for a Theme to adopt EA. “Current” means public, published and explicitly confirmed to the extent stated below; it does **not** mean an adopted common schema. “Ideal” is the target contract needed to test EA against the canonical EA requirements.

## 1. Scope and source snapshot

This audit uses:

- the EA corpus at `structural-awareness-contributions` commit `b81d3c8` locally, compared with GitHub `origin/main` at `6a8fd5f`;
- the canonical EA requirements, challenges, T1–T4 and H1–H6/KPI protocol;
- the EA functional interfaces v0.4 and the existing *Provisional Cross-Theme Interface Contracts v0.4*;
- FG-TIDA Themes GitHub `main` at `2b77cb8`, and the public issue discussions and attachments consulted on 18 September 2026 UTC.

Primary public sources include [Theme #13’s testbed-side clarification](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397), [the simplified proposed #13/EA handoff](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5640186655), [Theme #16’s v0.2 matrix](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5715075656), [Lei’s confirmation of that matrix’s two structural repairs](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5724916455), and [Nelson’s proposed testbed/conformance-profile next step](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5733936861).

## 2. Publication and surgical-change audit

### 2.1 Publication state

| Check | Result |
| --- | --- |
| Local EA commit | `b81d3c8 Clarify EA interface namespaces and evidence status` |
| GitHub `origin/main` after `fetch --prune` | `6a8fd5f Refine hybrid failure trajectories and quality arbitration` |
| Relationship | local `main` is **ahead by one commit** |
| Push result | **Not published.** GitHub rejected the push because this environment has no GitHub authentication (`could not read Username`). |
| Working tree | clean |

Accordingly, the surgical change exists locally and is auditably committed, but it must not be described as present in GitHub until an authenticated maintainer pushes `b81d3c8` to `main`.

### 2.2 Integrity of the change

The commit changes only the three fragments of **04 — General Functional Interfaces & Agentic Security v0.4**:

| File | Added | Removed | Nature of change |
| --- | ---: | ---: | --- |
| `04_...part01.md` | 17 | 17 | Namespace clarification and labels |
| `04_...part02.md` | 11 | 11 | Heading labels only (`S#` → `IF-S#`) |
| `04_...part03.md` | 34 | 32 | Reference labels and an evidence-status/date note |

`git diff --check` passes. Inspection of the complete diff confirms:

1. No O1–O6, F1–F9, interface family, payload field, producer/consumer ownership rule or minimum-profile item was deleted.
2. `S1–S13` in 04 are now unambiguously `IF-S1–IF-S13`; `CH-S#` remains the DAOS-challenge namespace; and canonical requirements are explicitly `REQ-S1–REQ-S14`.
3. No `IF-S14` was created.
4. Section 10 now dates its external-alignment snapshot and limits its claims to E4 market/standard evidence. It does not claim adoption, universal interoperability, completeness or EA effectiveness.

This meets the requested narrow correction. It does **not** implement the substantive candidate gaps below.

## 3. Independent EA input/output completeness audit

### Finding

The v0.4 taxonomy gives every canonical requirement an intelligible input/output route, but it is **not yet a fully testable end-to-end contract against T1–T4 and the KPI protocol**. The main issue is traceability and composition semantics, not absence of another generic producer family.

| Requirement surface | Current functional route | Independent assessment | Minimum unresolved contract need |
| --- | --- | --- | --- |
| `REQ-S1`, `S7`, `S8`, `S13` — authority, identity, delegation, history | O1; IF-S1, IF-S2, IF-S8; F3/F5/F8/F9 | Largely covered when the source supplies grant, standing, scope, provenance and history. EA correctly does not originate them. | A consistently available action/decision/operation binding and versioned lineage across handoffs. Annex 01D supplies this for EA/MSCA/RA, but 04 does not make it a generic composition condition. |
| `REQ-S2` — preference fidelity | O1/F1 and decision context | Correct ownership boundary, but only as strong as the mission-side preference handoff. | A decision-basis reference/version and coverage/expiry where preference is material. |
| `REQ-S3`, `S5`, `S10` — change, indeterminacy, commitment | O1, O3–O5; IF-S4, IF-S5, IF-S7, IF-S12; F1–F9 | Strong generic coverage of freshness, scope, UNKNOWN, response capability and revalidation. | A machine-testable re-entry pointer to the invalidated assumption/window and an explicit preservation path for uncertainty across a prior handoff. |
| `REQ-S4` — effective human capacity | IF-S6, IF-S12; F1/F6/F9 | Covered: authority, information scope, capacity, response window and outcome have a natural home. | Binding to the exact receiving decision/operation, so a nominal capacity state is not reused beyond its scope. |
| `REQ-S6` — bounded private interoperability | O6 and IF-S10, with profile/delta discipline | Covered conceptually. Explicit UNKNOWN and minimum disclosure are sound. | Test instrumentation for disclosure/latency cost; this is not a universal message field. |
| `REQ-S9`, `S11` — composition, conflict and policy integrity | F5/F6; IF-S2, IF-S4, IF-S8, IF-S11, IF-S13 | Partial. Existing IF-S4 carries intent collision and criticality; scope/dependency and source-independence are available. | A shared-resource/time conflict relation, competing-directive references and applicable precedence/authority reference. This is exposed by 00F; it cannot be inferred from two local verdicts. |
| `REQ-S12` — accountability and repair | IF-S8; O3/O5; F8/F9 | Covered as a record/revalidation path, without making a record proof of substantive truth. | A link from the preserved record to the decision/operation and re-entry target. |
| `REQ-S14` — evidence-to-decision assessment | F1–F9 and O1–O6 | Partial by design: it is an assessment layer, not another producer. The current architecture can host it. | A traceability/test harness that binds scope, owner, required evidence, arbitration/precedence, expiry, re-entry and outcome to the same run. |

### KPI consequence

The KPI protocol does not require every numerator and denominator to travel as an interface field. Many measures are test-harness observables: decision count, oracle branch, latency, burden and downstream error. It **does** require the handoff to retain the material qualifiers that make those measures interpretable: `scope`, `provenance/freshness`, `dependency`, `unresolved state`, `capacity`, `authority`, `expiry`, and a re-entry path.

The current generic interfaces cover most of those conditionally. The cross-boundary weaknesses are: (a) operation/decision identity and lineage, (b) recoverable targeted re-entry, and (c) shared resource-time conflict/precedence. Therefore the right next artifact is a traceability and test-profile matrix, not a speculative O7 or IF-S14.

## 4. FG-TIDA: current published/confirmed interface state

There is currently **no adopted, common FG-TIDA → EA wire contract or general EHD schema**. The published material is a set of Theme-owned handoffs, with different degrees of maturity. In particular, the #13/EA mapping is compatible with Use Case #4 from the testbed perspective, while its wider characterization remains pending Theme #13 confirmation; the #16 matrix is a bounded discussion draft, not a universal interface standard.

| Theme/component | Current published/confirmed inputs and outputs relevant to EA | Status of that statement | What is deliberately not asserted |
| --- | --- | --- | --- |
| **#5 Authority provenance** | Grant/principal, purpose/scope, limits, standing/applicability, revision/revocation and current-context applicability are the authority-layer facts that #16 consumes. | Public Theme discussion; authority boundary is explicit in the #16 matrix. | A finalized cross-Theme schema or that EA decides authority. |
| **#6 Intent/policy runtime conformance** | Verdict; named/versioned policy/reference; evaluated scope/context; material conflict/criticality where applicable; issuer relationship; confidence/threshold semantics; explicit indeterminate versus evidence absence. | Comparatively stable local vocabulary and used as an upstream #16 row. | That #6 provides systemic composition, inherited uncertainty or general EA posture. |
| **#10 Governance/enforcement** | Escalation condition/signal, enforcement state, affected scope, authority/policy context; execution confirmation enters the #16 sequence. | Bounded #16 v0.2 row. | A final independent #10→EA schema or that EA executes enforcement. |
| **#13 Ecosystem-level agent defense** | Incident lifecycle: signal semantics/birth, distribution, corroboration/amendment, operational blast-radius refinement, response coordination, locally authorized containment and resolution. Proposed/testbed-compatible EA handoff: qualified incident state, provenance/source relationship, freshness, affected scope, blast radius/dependency, response window/reach, unresolved qualifiers; EA may return a scoped assessment and targeted refinement request. | Testbed-compatible and explicitly bounded; broader architecture pending #13 confirmation. | Theme-wide adoption of a general EHD, a peer-mechanism decision, or a requirement that other Themes translate into #13 state. |
| **#16 Operational human oversight** | Matrix v0.2 sequence: trigger qualification → intervention path → applicable #5 authority → capacity → permitted options → required evidence → residual indeterminacy → selected intervention → execution confirmation → revalidation → return condition. The #13 row consumes affected scope, capacity/determinacy, confidence/freshness where available and local oversight evidence. | Discussion draft; two structural distinctions explicitly accepted for the draft. | An EA payload or three-posture taxonomy frozen as a #16 requirement. |
| **#19 Privacy/minimum disclosure** | Authorized minimum view: recipient/purpose, permitted/forbidden attributes, retention/linkability constraints and selective-disclosure capability. | Cross-cutting boundary discussed as a profile, not a parallel lifecycle. | A finalized EA-specific payload. |
| **#21 Population-level evaluation** | Defined population, period, taxonomy/policy version, evaluator/evaluator-family characteristic, rate, what it can establish and residual indeterminacy; #16 preserves sampling versus structural indeterminacy. | Bounded #16 v0.2 row and public interface shape. | That a population rate establishes a local decision, authority or action. |
| **#22 Remote attestation for agentic AI** | Attestation needs a claim bound to relevant interaction/action, policy identity/version and declared issuer relationship; no assertion is distinct from #6’s action-side indeterminate. | Public cross-theme discussion; no EA-specific handoff stabilized. | A finalized #22→EA contract or that attestation establishes behavioral/system truth. |

## 5. Actual versus ideal EA contract

### 5.1 Actual, interoperable only by bounded adapters today

The current workable contract is an **adapter discipline**, not a single common envelope:

1. Preserve each Theme’s native result and source semantics.
2. Bind it to an applicable scope and relevant time/context.
3. Preserve its issuer/source relationship and any material limitation or indeterminacy.
4. Do not convert the result into a new authority, human decision, execution confirmation or system-wide conclusion.
5. Let the receiving Theme retain the decision/action it owns.

This supports the #16 matrix’s current operational cycle. It does not yet guarantee testable composition across independently implemented EA, #13, #16 and the other producers.

### 5.2 Ideal EA contract for the canonical requirements

The ideal contract is deliberately split into a **producer handoff** and an **EA return**. It remains an architectural target until validated and accepted by the owning Themes.

| Direction | Ideal minimum, conditional on decision materiality | Current gap versus ideal |
| --- | --- | --- |
| **Producer → EA** | Profile/schema reference and version; subject–proposition–receiving-decision scope; operation/decision ID and handoff lineage; native result/state; issuer and relationship; evidence/provenance basis; as-of/freshness/expiry; known exclusions and explicit UNKNOWN; dependency/correlation; authority/reference and current applicability; capacity/response window; action/interaction binding where ephemeral. | The local pieces exist in different Themes, but operation/decision lineage, expiry and shared dependency semantics are not consistently carried or cross-Theme agreed. #13’s EHD relation is not general adoption. |
| **EA → producer/consumer** | Decision-scoped assessment; assessed scope/coverage; residual and inherited indeterminacy; dependency/correlation or conflict warning; evidence/authority/capacity limitation; posture as a non-executing qualification; a targeted re-entry request with the invalidated assumption/window/reference; EA result’s own freshness/expiry and limitation. | #13 testbed proposal covers much of this, but only as a proposed bounded interaction. #16 currently consumes a much smaller EA row and has not frozen an EA return contract. |
| **Composition/control record** | Same `σ(d,t)` across producer, EA and consumer; shared resource-time segment when directives collide; applicable precedence/authority reference; selected action versus execution outcome; revalidation trigger and outcome; traceable oracle/KPI links. | #16 v0.2 gives the lifecycle distinction, but no common cross-Theme record/schema yet. The 00F conflict and 00E composition cases require this to be testable. |
| **Test instrumentation** | Per KPI: named producer, receiver, numerator/denominator source, oracle, run/branch, time and cost ledger; tests for loss, stale reuse, false correlation, conflict, forced closure and targeted re-entry. | This is mostly absent by design from an operational wire contract. It belongs in the proposed UC #4 conformance profile. |

### 5.3 Concrete gap statement

The gap is **not** “FG-TIDA lacks all EA inputs and outputs.” The gap is narrower and actionable:

- Current Themes already expose much of the state EA would consume, under their own semantics.
- The current public #16 matrix provides a bounded operational destination for selected upstream results.
- What is missing is an agreed cross-Theme adapter/test contract that preserves identity of the same decision, uncertainty and dependency semantics, authority/precedence, time/expiry and targeted re-entry across that route.

Nelson’s proposed UC #4 conformance profile is the appropriate location to test exactly this gap, while leaving the #16 matrix and each Theme’s semantics under their own contributors’ control.

## 6. Recommended next decision

Do **not** modify 04 or the provisional 05 contracts on the strength of this audit alone. First create a version-pinned UC #4 testbed/conformance profile with an **actual / candidate / rejected** status for each field and named semantic owners. The first vectors should include:

1. normal #13 → #16 intervention;
2. constrained response window;
3. intervention outside current authority/options;
4. human decision differing from executed action;
5. stale/no-longer-applicable authority at return to operation; and
6. changing human capacity that changes the ecosystem qualification.

For the EA corpus, add the ideal-only fields to that profile as candidate requirements: `operation/decision ID + lineage`, `targeted re-entry reference`, `shared resource-time conflict + precedence`, and `EA output validity/expiry`. Promote any of them into 04 only if a frozen vector shows that the existing generic interfaces cannot express the needed fact without inventing it.
