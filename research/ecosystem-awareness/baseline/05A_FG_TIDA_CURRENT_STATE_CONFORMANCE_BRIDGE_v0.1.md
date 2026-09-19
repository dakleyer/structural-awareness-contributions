# 05A — FG-TIDA Current-State Interface and Conformance Bridge — v0.1

## Status and reading rule

**Status: public working bridge; source snapshot and consultation record 19 September 2026 (UTC).** This document is an additive EA corpus companion. It does not modify the controlled text of [05 — Provisional Cross-Theme Contracts v0.4](./05_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md), claim FG-TIDA adoption, define an FG-TIDA common schema, or require a Theme to accept EA theory or payloads.

Document 05 is the **ideal FG-TIDA-oriented bilateral contract**: the complete target relationship between EA and neighbouring functions, subject to validation. This document, 05A, states the **maximum interface and conformance profile defensible from the current public FG-TIDA state**: published Theme discussions, explicitly discussed handoffs and the near-term, contributor-owned testbed direction. It is deliberately smaller than 05 wherever the public discussion has not established a common handoff.

“Current” below means public and explicitly stated at the cited source; it does not mean adopted ITU text, final Theme consensus or independently established interoperability. “Candidate” means a bounded, source-linked field or route that may be tested with its semantic owner; it is not yet a shared requirement. “Test-only” means an ICR or fixture datum that must not be promoted into an operational payload merely because it is useful for evaluation.

The external statements in this document are **E4 working-source evidence** under the [canonical evidence-grade definition](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md#3-evidence-grades). They support the stated public discussion and no stronger claim. This bridge must be reviewed when any cited source materially changes and no later than 19 December 2026 (UTC). Without that review, a row labelled **Current source state** remains only a dated consultation record and cannot be carried forward as current support for a new route.

## 1. Source basis and ownership boundary

This bridge uses the following public anchors, each consulted on 19 September 2026 (UTC). A link identifies a mutable public discussion; the bounded record below states what this bridge relied on at consultation, rather than treating a comment as immutable group text.

| Anchor and contributor | Consulted record used by this bridge | Evidence position |
| --- | --- | --- |
| [Theme #13 testbed-side clarification](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397) — T-n-Nelson | A testbed-side EA/#13 boundary can be considered without moving incident lifecycle ownership. | Public contributor clarification, not Theme-wide adoption. |
| [Simplified proposed #13/EA handoff](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5640186655) — dakleyer | A bounded EA handoff was proposed for discussion. | Public author proposal, not FG-TIDA state. |
| [Theme #16 v0.2 matrix](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5715075656) — amsupavlenko-coder (Olena) | The matrix distinguishes human-oversight lifecycle elements that EA may qualify without owning. | Public working matrix. |
| [Structural confirmation](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5724916455) — leigao-research (Lei) | The matrix's structural distinctions were confirmed in discussion. | Public contributor confirmation. |
| [Proposed UC #4 executable-validation boundary](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5733936861) — T-n-Nelson | A testbed/executable-validation layer was proposed beneath the use-case work. | Public proposal, not an adopted profile. |
| [Paired authority-applicability case](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5735344648) — arpitasarker01, and [derive-not-duplicate agreement](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5737323754) — T-n-Nelson | The case remains the semantic source; any executable vector is derived after review. | Public case/proposal boundary, not a parallel case. |

The resulting ownership rule is stable across the bridge:

| Component | Retained ownership | EA role |
| --- | --- | --- |
| Theme #13 incident/signal lifecycle | Signal birth, distribution, corroboration/amendment, affected scope/blast radius, locally authorised containment and resolution. | Consume the qualified signal as evidence; assess what it supports with other decision-relevant state. |
| Ecosystem Awareness within the #13 direction | System-level dependency, capacity and residual-indeterminacy qualification; targeted requalification. | Does not become the incident lifecycle, containment authority or a central controller. |
| Theme #5 authority provenance | Grant, delegation, standing, revocation and current applicability. | Preserve unresolved authority as a material qualification; never originate authority. |
| Theme #16 operational human oversight | Trigger qualification, intervention path, permitted options, human decision, execution confirmation, revalidation and return. | Supply a bounded assessment that #16 may consume; never select, authorise or execute the intervention. |
| UC #4 companion profile | Versioned adapters, fixtures, oracles, traces and conformance reports for reviewed semantics. | Test the route; does not redefine Theme semantics or the case corpus. |

This bridge therefore supports mixed and non-monolithic authority arrangements. Escalation, transport or a new route does not itself confer authority; the applicable authority determination remains owned by the authority layer for the specific action, context and time.

## 2. Current-state conformance vocabulary

| Status | Meaning in 05A | Permitted use |
| --- | --- | --- |
| **Current source state** | A Theme-owned result or distinction is publicly described and can be preserved through an adapter. | Use as native semantics; retain the source and its limits. |
| **Candidate cross-Theme field** | A field is needed by the 05 ideal or a public candidate route, but no common FG-TIDA handoff has been agreed. | Include only in a version-pinned profile/fixture with named semantic owners. |
| **Test-only evidence** | A datum is needed to determine whether a route preserves semantics or remains viable. | Keep in the Interface Conformance Record (ICR), not in the runtime message by default. |
| **Not established** | No public source supports a common field, authority or consumer relationship. | Preserve as `UNKNOWN`; do not infer or invent it. |

## 3. Maximum currently defensible handoff

### 3.1 Current EA adapter baseline

The maximum profile that EA can construct today is a **native Theme result plus a bounded adapter**, not a universal EHD schema. Where a result is composed across independently implemented components, the adapter should preserve the following existing 05 kernel. This is a requirement on the EA adapter's capability, not a requirement that a Theme producer emit these fields.

1. producer semantic/profile reference and version, or an equivalent identifier;
2. subject, proposition or decision domain and scope;
3. producer/issuer;
4. native result or closure;
5. determination/state kind; and
6. explicit `UNKNOWN` qualifiers.

Where material to the receiving decision, the adapter may also preserve source/provenance relationship, evidence class, as-of/freshness, known exclusion, dependency/correlation, capacity/window, authority reference and action/interaction scope. A missing qualifier remains `UNKNOWN`; an adapter must not upgrade it.

This is sufficient to parse and use a bounded, source-attributed result. It is **not**, by itself, sufficient to claim that a multi-hop or composition-critical route has preserved the same decision basis.

### 3.2 Candidate Composition-Critical profile

The following items are required by the 05 ideal only when the declared route composes prior decisions, crosses multiple handoffs, returns after a material change or may issue competing directives over one resource-time segment. They are candidate profile fields, not additions to the universal kernel:

| Candidate profile item | Why it is material | Current position | Legitimate owner or source |
| --- | --- | --- | --- |
| Decision/operation reference and parent-handoff lineage | Binds producer, EA and receiver to the same relying decision rather than merely similar context. | Candidate; native identifiers exist but are not a common cross-Theme relation. | Originating action/decision component; record/adapter preserves it. |
| Decision-basis/reference version | Identifies the policy, authority, mission or evidence basis invalidated by a change. | Candidate. | Source that owns the basis. |
| Validity, expiry and review condition | Prevents stale signal, capacity or authority state from being reused outside its useful horizon. | Partly expressible through current freshness/standing language; not a common profile. | Producing Theme or authority/oversight source. |
| Targeted re-entry reference | Lets a receiver refresh the precise assumption, source or window that became insufficient. | Candidate EA return. | EA identifies the target; the source owner performs the refresh. |
| Dependency/correlation declaration and basis | Prevents several related claims from being counted as independent corroboration. | Current where a Theme can state it; no common required representation. | Producer/aggregator declares its knowledge and basis. |
| Shared resource-time segment, competing-directive references and precedence source | Makes a 00F-style collision observable without EA inventing a hierarchy. | Candidate for conflict routes only. | Relevant action/authority/arbitration owner. |
| EA output validity and limitation | Prevents a scoped assessment from becoming a timeless or global result. | Candidate; compatible with the 05 EA-return rule. | EA. |

No item in this table creates O7, IF-S14, a new Theme, a universal precedence hierarchy or a mandatory metadata tax on simple routes.

### 3.3 Actual versus ideal return

| Direction | Maximum defensible now | Still only candidate until reviewed and tested |
| --- | --- | --- |
| Theme → EA | Native result with semantic source, scope, issuer, state and explicit limitation/`UNKNOWN`; conditional freshness, provenance, capacity, authority and dependency where supplied. | Common decision/operation lineage; portable expiry; shared dependency semantics. |
| EA → #13 | Scoped assessment of the incident/evidence condition, residual limitation and targeted refinement/corroboration request. | A general #13-wide EA payload or mandatory EHD. Any candidate capacity/window or posture qualifier remains bound to the same decision scope; it does not establish a global posture taxonomy. |
| EA → #16 | Bounded statement relevant to trigger qualification or intervention: affected scope, capacity/determinacy limitation, residual uncertainty and specific requalification need. | Three-posture taxonomy or a frozen universal EA return contract for #16. |
| Cross-route record | Native record/action evidence may preserve outcome, authority and reference links. | **Not established:** a common `σ(d,t)` record, shared resource-time conflict relation and cross-Theme precedence schema. |

## 4. Current Theme routes

| Route | Publicly defensible input/output today | Boundary that 05A preserves | Conformance status |
| --- | --- | --- | --- |
| #13 → EA | Qualified incident/signal state, provenance/source relationship, freshness, affected scope or blast radius, response reach/window and unresolved qualifiers where available. | Lifecycle and containment semantics remain #13’s; EA treats the signal as bounded evidence. | **Current source state**; bounded adapter is a **Candidate cross-Theme field** pending #13 review. |
| EA → #13 | Scoped assessment, residual-indeterminacy qualification and targeted refinement request. | EA does not order containment or replace the signal lifecycle. | **Candidate cross-Theme field**. |
| #16 → EA | Effective human-oversight capacity, information coverage, relevant decision/intervention state, execution/reconciliation and material change where available. | #16 retains human authority, option selection and return-to-operation lifecycle. | **Current source state**; EA adapter is a **Candidate cross-Theme field**. |
| EA → #16 | Information relevant to whether the intervention path remains adequately qualified: affected scope, residual limitation, capacity binding and targeted requalification. | EA does not convert an assessment into a human decision, mandate or execution command. | **Candidate cross-Theme field**; no common #16 EA schema asserted. |
| #5 → #16/EA | Grant/provenance, limits, standing, revocation and current-context applicability. | Authority is consumed, not re-created, by #16 and EA. | **Current source state** for the authority boundary; decision-specific binding is a **Candidate cross-Theme field**. |
| #6/#22 → EA | Scoped conformance or attestation result, named reference/version, issuer relationship, limitation and indeterminate/no-assertion state. | A local verdict or attestation does not establish ecosystem truth. | **Candidate cross-Theme field** until a public source anchor and semantic-owner validation are recorded. |
| #1/#10 → EA | Action/outcome record, authority/policy references, available response capability, execution outcome and residual exposure where recorded. | Record is not proof of every carried claim; EA never executes containment. | **Candidate cross-Theme field**; a common cross-Theme record is **Not established**. |
| #19/#21 and other specialised sources → EA | Minimum-disclosure constraint or scoped evaluation result with method/limit where the source can provide it. | Rate, privacy rule or specialist evaluation does not become authority or a universal EA conclusion. | **Candidate cross-Theme field** until a reviewed vector names the route. |

## 5. Conformance bridge to Appendix A

The [Appendix A Interface Quality and Conformance Plan](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part03.md#appendix-a--interface-quality-and-conformance-plan-for-ecosystem-awareness) is the decision rule for this bridge. It is not transmitted in a Theme payload and it does not convert UC #4 into a new governing body. Its cited sections, rather than this bridge, define the ICR and generic control requirements.

| Governing Appendix A section | 05A application |
| --- | --- |
| [A.3 — ICR](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part03.md#a3-unit-under-test-interface-conformance-record) and [A.4 — entry conditions](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part03.md#a4-entry-conditions) | Record the FG-TIDA route, its owners, materiality status, declared route map, review status and admissibility exactly as governed there. |
| [A.5.1–A.5.3 — route and fixtures](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part03.md#a5-test-method) | Apply the generic semantic-preservation, fixture, aggregation and reviewer controls to the specific route; no additional 05A control is created. |
| [A.6 — evidence and test measures](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part03.md#a6-evidence-and-test-measures) and [A.7 — findings](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part03.md#a7-conformance-findings) | Assess the named FG-TIDA vector under the declared capacity basis and horizon, and use the generic result vocabulary. |

Thus a 05A route is called **sufficient only for its declared scope and horizon after ICR evidence exists**. Before that, it is a candidate architecture profile, not an interoperability claim.

## 6. Initial UC #4 vector bridge

The following vectors are the near-term executable direction described for UC #4. They do not replace the Phase 2 case/challenge traceability structure or pre-empt review of the source cases.

| Candidate vector | Minimum route to exercise | Principal conformance question |
| --- | --- | --- |
| Normal intervention | #13/EA qualification → #16 trigger/path → #5 authority → permitted option → human decision → execution → revalidation. | Do scope, authority, capacity and residual limitation remain intelligible without EA choosing the action? |
| Constrained response window | Same route with capacity or time binding. | Is further corroboration/review still useful before the response opportunity expires? |
| Outside authority/options | #16 receives an intervention proposal not supported by current #5 applicability or permitted options. | Does the route reject the action without turning escalation into authority? |
| Decision/execution divergence | Human decision and recorded execution differ; the ICR names the execution-record producer. | Can the same decision/operation and outcome be reconstructed for revalidation? If the execution producer is unavailable, record the Appendix A producer-or-receiver finding rather than infer the outcome. |
| Stale authority at return | Arpita’s reviewed paired case supplies the semantic source; the testbed derives only the executable mapping. | Does current-context applicability prevent historical grant reuse after material change? |
| Capacity change alters qualification | Effective human capacity, as declared by #16, changes after an EA assessment. | Does the receiver re-enter the correct qualification point rather than reuse nominal capacity? EA evaluates the route's use of the declared capacity, not the competence of the reviewer. |

Where a vector aggregates assertions or crosses more than one intermediate handoff, the optional Composition-Critical profile is selected. Where it relies on an external producer, the ICR records whether the boundary is genuinely independent or simulated. This table is informational traceability only: it imports no oracle into a Theme case, and the semantic owner of the Theme route provides or accepts the vector oracle.

| 05 validation profile (informational) | UC #4 vector relationship | Oracle ownership |
| --- | --- | --- |
| UC-EA-01 — action-time operating-frame requalification | Normal intervention, stale authority at return and decision/execution divergence can exercise a material change and the required re-entry. | The relevant Theme/case semantic owner defines or accepts the vector oracle. |
| UC-EA-02 — bounded determination under incomplete/conflicting evidence | Constrained response window can exercise the limits of available corroboration, burden and residual indeterminacy. | The relevant Theme/case semantic owner defines or accepts the vector oracle. |
| UC-EA-03 — human oversight under bounded effective capacity | Normal intervention and capacity change alter the declared #16 capacity basis without EA judging reviewer competence. | Theme #16/case semantic owner defines or accepts the vector oracle. |
| UC-EA-04 — scope-indexed composition | Any multi-hop or aggregating vector adds the composition-critical route conditions; it is not presumed by a single-hop vector. | The relevant producer/Theme semantic owner defines or accepts the vector oracle. |

## 7. Admission, promotion and non-claims

A field or route may move from **candidate** to a **validated 05A candidate profile** only when all of the following are recorded:

1. the relevant Theme/case contributor has validated the semantic mapping for the declared vector;
2. producer, receiver, semantic owner and adapter owner are identified;
3. the route has a version-pinned profile/adapter and ICR evidence for the applicable fixture classes;
4. `UNKNOWN`, limitation, dependency and authority boundaries survive without silent upgrade;
5. the route has an identified receiver and does not transfer action, authority or lifecycle ownership to EA; and
6. observed burden is viable for the declared horizon, or the route remains explicitly limited.

A positive ICR authorises only this statement: *the named adapter/profile preserved the stated qualifiers for the named route, profile version, vector set, scope and horizon on the recorded date.* It does not establish conformity with a Theme or with EA generally. A **Current source state** changes only through new public source evidence, not through a test result.

If the relevant semantic owner objects to the bridge's description of a Theme field or route, the affected row is treated as **Not established** until the objection is resolved or a reviewed source supersedes it. An external contributor may validate a mapping without granting reuse rights; this bridge does not ask them to coauthor fixtures or adapters unless separate terms are agreed.

Failure of a fixture does not by itself justify changing 05, adding a generic interface family or asking a Theme to adopt a new payload. It first identifies whether the issue is a missing producer/receiver, a nonconforming adapter, an insufficient candidate field or an out-of-scope ownership rule.

## 8. Determination

The maximum defensible FG-TIDA profile today is therefore:

- **native, Theme-owned results** preserved through bounded, versioned adapters;
- **#13 incident/signal lifecycle and EA qualification kept distinct**, while connected through a bounded evidence/requalification relation;
- **#16 human-oversight lifecycle and #5 authority applicability kept distinct**, with EA supplying only decision-scoped qualification;
- **candidate Composition-Critical fields** used only where the declared UC #4 route needs decision continuity, targeted re-entry or conflict reconstruction; and
- **Appendix A ICR evidence** as the test-side condition for calling a route sufficient.

This is less than the ideal 05 contract, but it is the most complete profile currently supportable without claiming FG-TIDA adoption, inventing absent fields or converting a testbed into a control plane. It preserves a clear path from public discussion to reviewed adapters, fixtures and conformance evidence while keeping later extension reversible.
