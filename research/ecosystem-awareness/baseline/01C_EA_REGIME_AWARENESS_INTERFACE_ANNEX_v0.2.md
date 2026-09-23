# Annex 01C — Ecosystem Awareness / Regime Awareness architectural relation

**Status:** public working architectural interface annex, v0.2, 23 September 2026. Additive companion to the Ecosystem Awareness (EA) corpus, outside the six controlled/frozen v0.4 release-baseline documents. It is a candidate composition, not an implemented common API, an empirically validated detector, an adopted ITU-T architecture or an institutional endorsement.

**Supersedes for current reading:** [v0.1](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.1.md), preserved for provenance.

## 1. Source, scope and architectural thesis

The source for the detector class and the terms below is the [Minimalistic Regime-Aware Early Warning Systems anchor working paper](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/) (updated 13 September 2026), especially §§2–6, 8–9, 13 and Appendix C. The public [Regime Awareness research note](../../regime-awareness/README.md) and [Regime Change Detection review line](../../regime-awareness/regime-change-qava-uv.md) locate the quantitative object and its preliminary-review boundary. EA functions F1–F9 come from the unchanged [Functional Architecture v0.4, part 1](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md), [part 2](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part02.md) and [part 3](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part03.md); the [dual-origin foundation](./01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md) explains residual indeterminacy and changing ecosystem frames. Sections 5–9 of **this annex** design the interface between these lines; their field names and mappings are proposed, not already published as an implemented protocol.

**Regime Awareness (RA) supplies a bounded, representation-relative test of present observable-regime compatibility. EA qualifies what that test can contribute to a mission-level decision across domains, dependencies, evidence sources, capacity and authority.** RA need not reconstruct a hidden system or forecast its future; EA must not promote a directional deviation of one series to a true, complete ecosystem state. Conversely, EA cannot replace RA's scientific obligation to show that its observation map and context preserve the declared regime distinction. The potentially useful relation is a *change-evidence-to-frame-requalification* loop, not an identity of the two architectures.

The paper's strongest “Sufficiently Good” class is a **Safety Governor** whose claim depends on a declared decision problem and a separately justified action mapping. “Good Enough” in programme shorthand refers to this bounded, substantive class; it does not mean an arbitrary detector with passable accuracy. The paper gives a conditional constructive schema and a toy witness of non-emptiness. It does **not** establish a universal observation map, universal context window, automatic Pointwise Non-Inferiority (PNI), real-time/economic feasibility or a validated deployment.

### 1.1 Minimal public detector versus broader Regime Awareness architecture

The public minimal detector and the broader current Regime Awareness architecture must remain distinguishable.

The **public minimal detector** establishes only the bounded representation/context/detection/action contracts supported by the published source.

The **broader Regime Awareness working architecture** may additionally project its result into the same [four-component qualified position](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md#2-four-component-qualified-epistemic-position) used by EA and MSCA and may expose a qualified directional **delta**. In Regime Awareness this object is called a delta, not a gradient. This v0.2 interface records that architectural projection as a current programme integration; it does not retroactively attribute the full projection or gradient semantics to the public minimal-detector paper.

This distinction allows the public detector to remain minimal while the surrounding architecture uses a richer, interoperable output.

## 2. Source-defined RA operating chain and limits

For a declared change family Δ, detectability threshold τ, admissible delay ℓ and observation/reduction map Ψ, the paper's minimal chain is:

**External process Ω → observation Ψ → finite observable history H_t(m) / contextual boundary T*_t → invariant d_t=I(H_t) → recent baseline B_t → deviation s_t=d_t−B_t → directional posture P_t∈{−1,0,+1} → separately authorized action A(P_t) → bounded guardrail/operation → observed consequences.**

**Terminology reconciliation:** “directional posture” is the source paper's term for `P_t`. In the current architecture, `P_t` is treated as the **RA directional detector output / directional signal**, not as the participant's P1/P2/P3 operating posture.

A single scalar series is the severe minimum observation setting, not a requirement to ignore other available evidence. Ψ may embody sensor placement, variable selection, aggregation, sampling, synchronization, filtering and transformation. The invariant may concern stability, recurrence, spectral organization, entropy or other regime-relevant structure; it is not a universal feature. The same present value can have different regime meaning under different histories. Negative/positive signs are **directional partitions**, not universal “harm”/“recovery” semantics. Buffer (distance to boundary) and inertia (persistence/rate) are optional descriptors, not forecasts or class-defining requirements.

The maximal defensible detector claim is present-tense: **the selected observable invariant remains compatible with, or departs directionally from, its contextually defined recent baseline above the declared threshold and within the admitted scope**. It is not identification of the unique hidden cause, the exact tipping instant, the future path/magnitude, or all changes in the ecosystem. Hidden transitions invisible under Ψ remain invisible to this detector. A neutral P_t is not proof that EA's wider operating frame is valid.

For the broader RA architecture, that bounded result can be projected as a qualified **regime delta**:

~~~text
Δ_RA(d,t) = [ A_RA, B_RA, C_RA, D_RA ]
~~~

with scope/provenance/context carried as qualifiers of the delta rather than confused with its direction:

- **A_RA — direction:** the qualified direction of observed regime movement/change under the declared Ψ, context, baseline, change family Δ and sign semantics. A_RA is not a generic YES/NO state and does not by itself say whether the change is good or bad for a particular agent.
- **B_RA — confidence / intensity:** the confidence, interval or bounded support attached to A_RA. B_RA determines how strongly the current evidence supports that direction. In the architectural shorthand used here, this is the **intensity of the delta**, not a second direction and not an agentic gradient.
- **C_RA — current-capability frontier:** recognized regime-relevant evidence/context that could still be acquired, tested or recomputed with currently available observation, computation or review capability before the useful deadline, but has not yet been established.
- **D_RA — residual:** regime-relevant state outside the current represented/recognized-obtainable capability boundary, including invisible changes, non-identifiable context and unresolved compatibility residual.

The delta therefore says, in bounded form:

~~~text
where the observable regime appears to be moving
+ how strongly that direction is supported
+ what else could still be established now
+ what remains outside current determination capability
~~~

Regime Awareness does **not** turn this into an agent-specific action gradient. That translation occurs only after the delta is projected through the receiving participant's MSCA/objective dependencies.

The [paper §2.7](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/) separates three contracts, each of which must be qualified independently:

| Contract | Source-defined responsibility | EA relation proposed here |
|---|---|---|
| **Representation** | Declare which scoped regime distinctions Ψ and the context window preserve, what they discard, and the admitted delay. | F1 identifies mission-relevant change domains; F2/APQ qualifies evidence acquisition and the wider W(d,t). EA may challenge a missing domain or stale pathway, but cannot certify Ψ by assumption. |
| **Detection** | Supply effective invariant, baseline, thresholds and contextual rule; issue compatible / directional-departure evidence with stated limits. | F3 if local or F4 if externally produced qualifies the report; F5 composes it without cancelling other uncertainty; F6 asks whether the mission operating frame Q remains justified. |
| **Action** | Declare posture-to-action library, admissible states, stakeholders, utility, horizon, authority and safety guarantee; govern response despite signal error. | EA F7 may request a control review. Owner/authority and control functions authorize/execute actions; EA's posture is not A(P_t), and PNI is not inherited from an EA assessment. |

A sophisticated threshold cannot recover a discarded distinction; a representative signal cannot make a harmful response safe; a safe response cannot rescue an acquisition pipeline that misses its useful deadline.

## 3. What “Sufficiently Good” requires — the ten defining properties

The anchor paper's [Table 5, §4](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/) classifies **ten** of the original nineteen numbered items as defining requirements of the **strong class**. Numbering is preserved so readers can check the source. The proposed EA implication is an interface obligation, not another source-defined membership condition.

| No. | Strong-class requirement | Function in RA / what must be shown | EA interface consequence |
|---|---|---|---|
| 1 | Approximate tipping awareness | Locate observable instability zones without pretending to identify an exact instant. | Carry zone, uncertainty and detection delay to F6; no exact-time premise for requalification. |
| 2 | Directional posture | Stable downward/neutral/upward partition or operational equivalent; domain-specific sign semantics must be declared. | Preserve RA P_t separately from EA Normal/Containment/Migration assessment. |
| 4 | Non-catastrophic trust | Downside of each authorized response remains bounded in the declared admissible domain. | F6/F7 must know the *declared* action-risk limit; “bounded” is not universal safety. |
| 6 | **Pointwise Non-Inferiority** | For every covered admissible state, time and authorized non-neutral signal, the authorized response is no worse than inaction in the declared utility model. | No automatic actuator request on mere deviation; pass the bounded safety declaration to authority/control owners, and keep UNKNOWN if unproven. |
| 7 | Economic viability | Net operational benefit exceeds acquisition, computation, integration, action, maintenance and governance costs for a deployed member. | F1/F2/F9 include latency, attention, response and acquisition burden; an abstract witness does not prove deployment value. |
| 8 | Layered deployment | Architecture permits additional invariant/context layers without changing canonical operational roles. | F2 may request targeted new layers, but cannot assume more layers improve net utility. |
| 9 | Computational efficiency | Finite-window computation fits the response time and resource envelope. | Bind report validity to remaining decision/action horizon, not merely algorithmic termination. |
| 10 | Actionable integration | Output maps to explicit guarded decision, action, abstention or escalation rule. | F7 requests must name the affected domain and authorized receiving capability; a posture without feasible response is insufficient. |
| 14 | Practical detectability threshold | Declare a minimum observable effect distinguishable from within-regime variation. | F4/F6 carry τ, scope, calibration and relative-completeness limits; no unqualified “all changes detected.” |
| 17 | Minimalism | Avoid hidden-state reconstruction and data coupling unnecessary for the declared observable-regime decision. | F2 bounds expansion/search; preserve the structural residual rather than treating the scalar stream as Ω. |

These properties are not all proved by one theorem. The finite online construction is conditional on a **supplied** representative observation map, effective context, invariant, baseline, threshold and admissible action mapping. Operational economic viability and domain PNI require separate evidence.

### The remaining nine items are not independent membership tests

The same [paper Table 6](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/) marks original items **3** decision reliability (derived under strict PNI; otherwise a weaker independent criterion), **5** intensity signal (optional), **11** cascade mitigation (conditional on timing/effect and no countervailing loss), **12** observational universality (conditional scope claim), **13** isomorphic reduction (conditional decision/action equivalence), **15** completeness above threshold (relative to Ψ, Δ and τ, not hidden transitions), **16** layer expansion (set-theoretic coverage only if old layers remain available), **18** model-free robustness (architectural consequence, not immunity to representation failure), and **19** separation of existence/construction (methodological principle). The interface must not present these as nine further independent production guarantees.

## 4. Contextual Sufficiency Boundary: RA science versus EA window management

The paper makes the **Contextual Sufficiency Boundary** T*_t (informally “tailing point”) a first-class object. For the chosen Ψ, change scope Δ, invariant I, threshold τ and delay ℓ, it is the start of the shortest *trailing* history H_t(m) that remains sufficient for the declared continuation/departure distinction. If no sufficient finite m exists, m*_t=∞ and T*_t is undefined. Earlier data are not required by the shortest sufficient suffix **for that decision**, but may still be physically relevant; absent monotonicity, adding older observations can preserve, improve **or destroy** separation by mixing regimes.

Five questions must remain separate: (1) can Ψ preserve the relevant distinction? (2) does a sufficient finite context exist? (3) can its boundary and operators be identified effectively? (4) is there a safe admissible action mapping? (5) can the full chain finish with positive value before the useful action deadline? Per-instance finite context need not imply one uniformly bounded window for the whole change class. Mathematical computability need not imply feasible acquisition, legal availability, latency or cost. The acquisition object can require variable, temporal extent, resolution, spatial/relational scope **and** transformation, not only window length ([paper §8](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/)).

**EA W(d,t) and RA H_t(m) are not synonyms.** F2's W(d,t) is the mission- and domain-scoped *active epistemic/observation boundary* across evidence classes and dependencies. RA's H_t(m)/T*_t is the historical support admitted for a specified observable/invariant and change class. A qualified RA context can be one input inside W(d,t), but cannot define the whole EA window or erase Pole D structural residual. F2 can constrain RA acquisition by burden and response time; RA must return the scientific result or an explicit inability to establish contextual sufficiency. If RA reports UNKNOWN/∞/non-identifiability, EA cannot replace it with a convenient fixed look-back.

The paper's multiscale nested-memory construction is a **candidate companion hypothesis**, not a property proved for all Sufficiently Good detectors. Short, intermediate and long layers can hedge against context-window failure; extra layers may increase contradiction, false alerts, cost and latency. Set-theoretic coverage is monotone only if old layers remain available and the governor may ignore the new one; net utility is not monotone ([paper §9 and §15](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/)).

## 5. Regime Awareness input/output circuit

The broader Regime Awareness integration consumes a **bounded participant-local input bundle**. The list below defines the current architectural minimum; implementations may add further qualified inputs.

For participant i:

~~~text
RA_Input_i(t) = [
  Π_EA,i(t),
  ReceivedSignals_i(t),
  Cart_i(t) / Δ_Cart,i(t),
  focal MSCA X_i(t),
  ArchitecturalRole_i(t),
  decision / Objective Envelope / W_i(d,t),
  qualified direct observations,
  action/effect history where material
]
~~~

### 5.1 Input owners

| Input | Producer / owner | RA use |
|---|---|---|
| **Π_EA,i** | Participant-local EA / [01H](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) | Current situated epistemic state, confidence/intensity, capability frontier and residual for the affected decision/scope. |
| **ReceivedSignals_i** | Receiver-local [Ecosystem Signalling 01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) | Qualified external messages from peers, systems, institutions or other ecosystem sources; only semantically/compatibly qualified content is eligible. |
| **Cart_i / Δ_Cart,i** | [MSCA Ecosystem Composition & Control](../../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) | Current qualified Ecosystem Cartography `Cart_i=[A_Cart,B_Cart,C_Cart,D_Cart]`, bounded dependency neighbourhood and material cartographic change-set. Because the cartography already uses the shared A/B/C/D semantics, RA may consume the relevant bounded slice without a second epistemic translation layer. |
| **focal MSCA X_i** | [Canonical MSCA Architecture](../../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md) | Current Objective Envelope, operating assumptions and C/P/M architecture against which regime change becomes control-relevant. |
| **ArchitecturalRole_i** | [MSCA Architectural Role](../../../standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md) | What this participant actually does, consumes, produces, depends on and is authorized/contracted to perform inside the focal MSCA. |
| **Decision / W_i / owner scope** | Legitimate owner + EA F1/F2 | Defines the active decision, observation boundary, materiality, response horizon and residual tolerance. |
| **Direct observations / action effects** | Local sensors, systems, human/technical observation, execution/effect records | Evidence of local change that need not arrive through inter-agent signalling. |

RA MAY consume other qualified sources. Absence from this table does not make another source invalid.

### 5.2 Trigger policy

RA need not run continuously or at one universal frequency.

An RA evaluation may be triggered by:

- material movement in Π_EA,i;
- one received signal crossing a declared materiality/confidence threshold;
- a set of received signals becoming jointly material after composition;
- signal insufficiency, contradiction, staleness or expiry that weakens the current regime basis;
- Δ_Cart,i showing a new, changed or disappearing dependency/cluster;
- focal MSCA, role, ACC, authority or capability change;
- a local action/effect mismatch;
- explicit owner/policy request;
- periodic scheduled refresh;
- a previous RA result requesting targeted requalification.

Each implementation SHOULD define appropriate debounce/hysteresis/evidence-change rules. No architectural requirement implies millisecond polling.

### 5.3 RA outputs

The broader RA integration produces:

~~~text
RA_Output_i(t) = [
  Δ_RA(t),
  RegimeOverlay_i(t),
  RequalificationRequests_i(t),
  validity / provenance / freshness
]
~~~

where:

- **Δ_RA = [A_RA,B_RA,C_RA,D_RA]** is the qualified directional ecosystem/regime delta;
- **RegimeOverlay_i** identifies which represented cartographic regions/elements, dependencies, assumptions or focal-MSCA elements are still compatible, weakening, departed or unresolved under the current regime evidence;
- **RequalificationRequests_i** identifies bounded areas requiring richer observation, different context, dependency refresh, resolution change or owner/control review.

RegimeOverlay_i is not a second persistent Ecosystem Cartography. [Composition & Control](../../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) owns Cart_i persistence and may use the overlay/request to produce Cart_i(t+1).

A material Δ_RA or bounded RA statement MAY itself be selectively disclosed through [Ecosystem Signalling 01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). RA does not require broadcast and does not turn its output into a command.

The downstream mechanism is [Canonical MSCA Operation & Repositioning](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md). RA supplies Δ_RA / overlay / requalification inputs; it does not select or authorize the resulting role/contract transition.

## 6. Candidate architectural responsibility map

| Boundary / producer | Owns | Receives | Supplies; recipient |
|---|---|---|---|
| Mission/authority owner | S/objective, declared change scope, stakes, admissible states/stakeholders, deadlines, decision rights and utility horizon | Operational outcomes, proposals and review evidence | Versioned decision and action scope; EA F1 and RA representation/action design. |
| EA F1/F2/APQ | Decision relevance, residual tolerance, capacity/response horizon, qualified W(d,t) and pathway fitness | Owner scope; available sensors/sources; RA representativeness/context evidence | Candidate observation need and constraints; RA representation/context design. |
| Participant-local EA / 01H | Current Π_EA,i and material local action/effect change | Local observations, handoffs, focal decision and role/MSCA context | Qualified local epistemic-state update; Composition & Control and RA input bundle. |
| Ecosystem Signalling / 01J receiver | ReceivedSignals_i and compatibility residual | External messages from agents, systems or institutions | Receiver-qualified external state; Composition & Control and RA input bundle. |
| MSCA Ecosystem Composition & Control | Cart_i, Δ_Cart,i, bounded dependency neighbourhood and resolution/qualification state | Local Π_EA,i changes, ReceivedSignals_i, focal MSCA/role changes, direct observations and RA feedback | Current qualified Ecosystem Cartography and material cartographic change-set; EA and RA. |
| RA representation/context layer | Ψ, admitted H_t(m), T*_t status, I and invisible-change declaration | Scoped Δ/τ/ℓ and observable access; EA burden/freshness challenge; ECM/dependency context where material | Context/representation qualification, data series and limitations; RA detector and EA F3/F4. |
| RA detector | d_t, B_t, s_t, thresholds, directional P_t and instability evidence | Qualified context, invariant, baseline and data | Present-tense, scoped report; EA F3 (embedded) or F4 (independent producer), then F5/F6. |
| RA Safety Governor/action design | P_t→candidate A(P_t), declared PNI or weaker bounded-downside proof, response feasibility | Owner-approved action library, utility domain, authority constraints, detector posture | Guarded proposal/abstention/escalation; authority/control function. **Not** an EA command. |
| EA F3/F4/F5/F6 | Qualification/composition of RA signal with other sources and domains; validity of mission-level frame Q | RA report, other evidence/dependencies, capacity, current assumptions | Scoped epistemic condition and EA posture; F7/F8 and decision owner. |
| EA F7/F8 | Targeted requalification requests and bounded internal/external statements | F6 assessment, RA limits, authority/capacity state | Re-test Ψ/T*/baseline/threshold, adjust W, seek independent evidence or request control review; relevant owner/RA/control function. |
| EA F9 and evaluation/observability | Outcome-to-assumption comparison and re-entry selection | RA report and its freshness; execution receipt **plus** measured effects; changes in dependencies/authority | Revalidation trigger for F1/F2/F4/F5/F6, RA recalibration or owner review. |

EA does not own RA invariant extraction, prove PNI or issue actuation authority. RA does not own ecosystem-wide epistemic composition or choose the legitimate mission objective. [EA Functional Architecture, F6–F9](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part02.md) preserves these responsibilities. The RA [public working note](../../regime-awareness/README.md) distinguishes contextual validity from intervention sufficiency.

## 7. Candidate interface contracts and concrete payloads

These are **proposed, transport-neutral semantic fields** for engineering and falsification. They are not an adopted message schema, a mandatory implementation, or claimed fields of the anchor paper.

### I-RA-01: scoped assessment mandate (owner + EA → RA)

Where ecosystem composition is material, the mandate may carry a versioned reference to the participant-local [MSCA Ecosystem Composition & Control](../../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) map or only the bounded dependency neighbourhood relevant to the decision. RA does not require or infer a complete ecosystem graph.

| Field group | Concrete content | Failure rule |
|---|---|---|
| Binding | decision/operation ID, material domain, owner-approved objective/constraints, version, as-of and expiry | A report for another mission or expired scope is not portable. |
| Regime decision | declared continuation/departure question; Δ; practical τ; admissible delay ℓ; sign meaning; stakeholder/utility horizon | Missing Δ/τ makes “complete detection” uninterpretable. |
| Operating frame | current Q assumptions, relevant dependencies, known change triggers, tolerated residual and the EA W(d,t) boundary | Q is an EA/owner context, not automatically RA's observable regime. |
| Acquisition/response | accessible evidence classes/pathways, freshness/quality, compute/privacy/attention budget, latest useful action time and reachable response latency | If evidence cannot be acquired in time, request a non-operational evaluation, not a live-governor claim. |
| Action boundary | action library and null action, permissions, admissible states and utility/stakeholder model supplied by their legitimate owners | EA cannot create authority or certify PNI from a detected change. |

### I-RA-02: representation/context qualification (RA → EA F2/F3 or F4)

| Field group | Concrete content | Qualification |
|---|---|---|
| Observable design | Ψ/version; source, time, variable/resolution, transformation and spatial/relational scope; discarded dimensions | State which Δ changes are demonstrably preserved and which are invisible/UNKNOWN. |
| Context | H_t(m), candidate/selected m, T*_t if established, selection method, baseline support and valid interval | Distinguish local finite, uniform-bound evidence, non-identifiable, unavailable and infeasible context. |
| Evidence of sufficiency | separation criterion/error bound, τ, ℓ, assumed data class, replay/empirical miss/false-reanchor/delay measurements where available | No retrospective tuning disguised as prospective proof. |
| Burden | acquisition/processing latency, compute, storage, disclosure and attention cost | Effective finite processing may still miss the response window. |

### I-RA-03: scoped regime evidence (RA → EA F3/F4 → F5/F6)

| Field group | Concrete content | Interpretation |
|---|---|---|
| Detection | d_t, B_t, s_t, θ−/θ+, P_t and approximate instability zone, plus optional buffer/inertia/persistence | P_t is RA's directional evidence, **not** EA's Normal/Containment/Migration posture. |
| Scope/validity | observable/representation/context IDs, Δ, τ, ℓ, event/as-of/freshness, coverage exclusions, operating period and model version | “Compatible” is only relative to the admitted Ψ/H/Δ; neutral ≠ global stability. |
| Epistemic limits | insufficient context, invisible scoped changes, dependency on upstream evidence, source lineage, unresolved sign or stale baseline | F5 must not cancel residual or call duplicated paths independent corroboration. |
| Evidence status | qualified continuation; qualified directional departure; or unresolved/unsupported representation/context/detection (candidate envelope categories) | These categories are *interface design*, not a replacement for paper P_t={−1,0,+1}. UNKNOWN must remain explicit. |

**Payload validity rule:** I-RA-03 carries a qualification state as well as any directional posture. P_t = 0 is emitted only for a qualified, fresh representation/context/baseline/threshold within the declared Δ/τ/ℓ; if representation, context, detection or baseline is unsupported, unresolved or expired, P_t is absent or explicitly UNKNOWN, never neutral. A prior qualified posture expires when its source contract is invalidated. This interface refinement and its no-context/stale-baseline tests are specified in the [joint operation-composition profile 01D](./01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md); they are **proposed payload semantics**, not extra outputs claimed by the RA paper.

### I-RA-03A: qualified regime delta projection (broader RA → EA/MSCA positioning)

The broader RA integration may normalize I-RA-02/I-RA-03 into the compact delta defined above:

| Component | RA projection |
|---|---|
| **A_RA — direction** | qualified direction of regime movement/change under the declared observation/context/sign semantics |
| **B_RA — confidence / intensity** | confidence, interval or bounded support attached to A_RA; stronger support means a stronger delta in that direction |
| **C_RA — current-capability frontier** | additional observable/context/evidence state that could still be acquired or tested with current available capability before the useful deadline |
| **D_RA — residual** | invisible, structurally unavailable, unenumerated or otherwise non-establishable regime-relevant state under the current capability/representation |

Decision/domain, Ψ/context/baseline/version, location/subject/frame, provenance, freshness and validity remain mandatory **qualifiers of Δ_RA**; they are not collapsed into A_RA.

RA does **not** emit the final Normal / Containment / Migration-Regime Transition posture for the participant. EA supplies the qualified mission/frame evidence; [Canonical MSCA Operation & Repositioning](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) operationally classifies P1/P2/P3 from Δ_RA under the participant's own MSCA risk, Type catalogue, ACC, authority, capacity and response horizon.

Conceptually:

~~~text
RA observation/context
→ qualified direction A_RA
→ confidence/intensity B_RA
→ capability/residual C_RA/D_RA
→ Δ_RA
→ EA / participant-local projection
→ nonlinear posture + agentic gradient
→ [MSCA Operation/Repositioning] ACC/lineage/authority-constrained transition
~~~

The [MSCA Ecosystem Composition & Control](../../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) map supplies the multi-resolution semantic/dependency context in which ecosystem change can be observed. The current [Canonical MSCA Architecture](../../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md#32-mechanical-alignment-with-a-regime-awareness-delta) defines how Δ_RA can then be projected onto S/E/C/P/M and compared with the participant's qualified focal-MSCA position. The [Objective-Conditioned Agentic Gradient Law](../../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) defines the participant-local gradient only after that projection, before ACC/authority execution filtering.


### I-RA-03B: downstream posture interpretation — nonlinear by design

The three top-level postures are **not three RA detector outputs** and are not a linear rescaling of B_RA.

For participant i, EA supplies the qualified mission/frame inputs, while [Canonical MSCA Operation & Repositioning §11](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md#11-hard-posture-gate--p1--p2--p3) owns the **sole current operational definition** of the participant-local posture operator `Γ_i`. This annex does not define a second signature.

The resulting posture vocabulary is:

~~~text
P1 = NORMAL
P2 = CONTAINMENT / MITIGATION
P3 = MIGRATION / REGIME TRANSITION
~~~

The intended reading is:

- **NORMAL:** Δ_RA may be non-zero and directional. The participant can still rely sufficiently on the current regime/response mapping for its Objective Envelope. Normal therefore means **qualified continuation under change**, not “no change”.
- **CONTAINMENT:** confidence/support for the current regime mapping has fallen, or objective-conditioned risk has crossed a participant-defined threshold, but a known bounded response remains qualified. Operation/Repositioning may classify/request this posture; any reduction of autonomy, scope, exposure or actuation is decided/executed by the appropriate authorized control function.
- **MIGRATION / REGIME TRANSITION:** the current historical/response mapping can no longer be relied on sufficiently for the mission. The participant must stop treating the old regime history as an adequate forecast/control basis and qualify another frame while preserving invariant controls where available.

The transition is intentionally **nonlinear**. A small additional fall in B_RA may cross a local threshold and trigger a discrete posture change. Thresholds may be encoded in the ACC, control policy or another legitimate owner profile and SHOULD use hysteresis or an equivalent evidence-change rule to avoid oscillation.

Illustrative confidence values such as 0.5→0.4 for containment or <0.1 for migration are examples only. This architecture does not prescribe universal numeric thresholds.

Loss of sufficient regime qualification may correspond to the existing **potential critical bifurcation** condition: the previous response mapping is no longer sufficiently qualified while several future response paths may remain locally plausible. That term is operational, not a claim that every transition is a mathematical bifurcation.

Operation/Repositioning additionally catalogues material received/local A/B/C/D compositions against the canonical Type 0/Type 1/Type 2 taxonomy before fixing P1/P2/P3. RA does not own that management-failure classification or the final hard posture decision.

### I-RA-04: action-safety declaration and response trace (owner/RA governor/control → EA F6/F9)

| Field group | Concrete content | Boundary |
|---|---|---|
| Action claim | A(P), A_null, admissible Ω_adm, stakeholder set, U, time horizon, response deadline, authority/permit and action-library version | “PNI established” only for the **declared** tuple; if missing/false, state weaker bounded downside or unresolved. |
| Proof/test evidence | per-action/state utility comparison or explicit assumptions, false-positive cost, reversibility, externalities and sensitivity limits | A costly line halt, user block or forced sale cannot be presumed strict-PNI merely because detection is good. |
| Execution/result | authorized permit/refusal, command receipt, separately observed effect, attention/operational cost and remaining capacity | Receipt is not outcome; no valid permit means no live action. |
| Revalidation | changed utility domain, stakeholder, horizon, intervention availability, false-signal experience or cost | Reopen RA action claim and EA operating-frame assessment. |

The strict strong-class inequality is **U_t(A(P_t),ω) ≥ U_t(A_null,ω) for every covered admissible ω and authorized non-neutral signal**, under the stated stakeholders, horizon and cost model ([paper §5](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/)). Reversibility, low apparent friction or signal-action decoupling are possible design patterns, **not proofs**. If a false-positive response has positive net cost in any admitted no-change state, strict PNI fails there even when expected utility is positive. The governor may legitimately use a weaker bounded-downside/expected-utility design, but it must not inherit the strong-class safety theorem by name. Strict PNI addresses the **utility-based** source of “Cry Wolf”; it does not eliminate false signals, attention burden or all alarm fatigue.

### I-RA-05: targeted requalification (EA F7/F9 → RA/owner/control)

Payload: affected decision/domain/dependency; invalidated Ψ, context T*/m, I, B, τ, Δ, Q, evidence source or action-domain assumption; fresh evidence need; bounded acquisition budget; response horizon; explicit UNKNOWN/residual; authority owner; requested re-test and success/stop criterion. The recipient may return a revised scoped RA report, insufficient-context finding, action-safety downgrade, or no feasible timely detector. EA then recomposes rather than merely repeating a stale P_t.

## 8. End-to-end candidate lifecycle, including disagreement

The broader circuit is:

~~~text
participant action / observation
→ Π_EA,i update
        ↘
qualified external messages → ReceivedSignals_i
        ↘
Composition & Control → Cart_i / Δ_Cart,i
        ↓
triggered / scheduled Regime Awareness
        ↓
Δ_RA + RegimeOverlay + requalification requests
        ↓
EA / focal-MSCA interpretation
        ↓
Canonical MSCA Operation & Repositioning
        ↺
new action / effects / signalling / map updates
~~~

1. **Declare the decision before the series:** owner sets objective and constraints, Δ, admissible action/state/utility scope and deadline. EA F1 identifies the material domain, consequences, capacity and response margin; F2 qualifies W and available acquisition paths. RA cannot choose the legitimate objective.
2. **Qualify representation and context:** RA tests whether Ψ preserves the needed change distinctions, whether a sufficient H_t(m) exists and is effectively identifiable, and whether acquisition/processing fits the deadline. If not, it reports the specific failure, not a fabricated neutral posture.
3. **Detect present compatibility:** with admitted context, RA computes I, B, deviation and directional P_t above declared thresholds. The report keeps source, context, scope, delay and invisible-change qualifiers. Approximate instability is admissible; exact tipping prediction is not. Where the broader RA profile is available, it also produces Δ_RA so that direction A_RA and confidence/intensity B_RA can be consumed directly by EA/MSCA positioning without calling the RA output a gradient.
4. **Compose ecosystem evidence:** EA F3/F4 qualifies the RA report; F5 checks lineage and coupling with other domains; F6 assesses whether Q still supports **this mission** under the remaining response capacity. RA departure may be immaterial to this mission, and RA neutral may coexist with a changed dependency that EA found elsewhere.
5. **Request or perform response through legitimate authority:** EA F7 selects a targeted evidence/window/control-review request. The RA Safety Governor may propose an A(P_t) only within its declared safety/action library; owner/authority/control functions permit and execute it if feasible. No RA or EA signal by itself authorizes a command.
6. **Close evidence, not just alarms:** execution receipt, independently observed effect, intervention cost and unchanged/changed assumptions feed EA F9 and RA evaluation. Material mismatch re-enters the affected representation, window, action or frame qualification; it does not silently widen S or assume that the historical baseline is still current.

**Disagreement cases are architecturally informative:** (a) RA reports directional departure while EA has insufficient source independence or mission relevance → hold the stronger systemic conclusion and seek bounded corroboration; (b) RA reports neutral while another dependency/human-capacity source changes → EA can requalify Q independently of RA; (c) RA can detect but no response is authorized, safe or fast enough → detection sufficiency does not establish intervention sufficiency; (d) context is non-identifiable/too costly → preserve UNKNOWN and choose an authorized bounded fallback if one exists; (e) an action is pointwise-safe in an old utility/actor domain but stakeholders or costs change → the PNI claim expires and must be reassessed.

## 9. Evaluation and falsification surface

The paper's formal witness shows the strong class is logically **non-empty** in a stylized two-state, zero-incremental-cost mirrored-route model; it is not field validation. The public RA review line is preliminary methodological challenge, not QAVA/Universitat de València endorsement or completed validation. A joint EA–RA interface evaluation is **proposed**. At minimum, it should measure:

| Test | What should be varied | Required observation / failure |
|---|---|---|
| Representation loss | Remove a variable/scale/relational link carrying a scoped Δ distinction | RA must declare invisibility or miss; EA must not call neutral “ecosystem safe.” |
| Context miss/mixing | Shorten below local sufficiency; lengthen across a prior regime; compare fixed/adaptive/multiscale windows | Report separation, false re-anchor, miss and delay; more history need not improve it. |
| Pathway/provenance | Stale observations, duplicated upstream feeds, inaccessible source, altered sampling | EA F2/APQ and F4/F5 preserve freshness and dependence; RA cannot repair discarded evidence downstream. |
| Ordinary variation versus departure | Noise, seasonality, outliers, gradual drift, abrupt and recurrent transitions | Compare RA to simple change-point/drift baselines without asserting universal superiority. |
| Signal/action mismatch | False directional alerts with costly stop/block/trade; no feasible action; permit refused | Strong PNI fails where false-positive cost is positive; no authorized action follows from a score. |
| Capacity/deadline | Delayed acquisition, processing, human review or effect; expired response window | Finite construction must not be reported as operationally sufficient after deadline. |
| Cross-domain composition | RA departure in one domain; local certainty elsewhere; changed ecosystem dependency not visible to Ψ | EA cannot compensate without demonstrated coupling; RA sign cannot set whole-system posture. |
| Outcome feedback | Receipt without effect, effect outside S, changing action externality/stakeholder | F9 reopens context/frame/action assumptions; no silent success or carried-forward PNI claim. |

The [EA validation files](./README.md#validation-profiles) and [RA preliminary evaluation design](../../regime-awareness/regime-change-qava-uv.md) are adjacent research apparatus. This annex does not claim that their test protocols have already been merged or run. The paper's §13 deployment order—decision scope, observation, representativeness, context boundary, detector, action library, cost/deadline, layered deployment, operational evaluation and continuous boundary governance—provides the source-grounded staging for a future joint experiment.

## 10. Relation to Minimum Sufficient Control Architecture and status boundary

The [EA–MSCA working annex](./01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md) maps owner-approved objectives, coordination, intervention means and response capacity. Its candidate response latency, authority, reversibility and contingency define what warning would be *useful*; RA provides a possible scoped regime-validity signal for EA; EA requests requalification when the epistemic or ecosystem frame no longer supports that MSCA record. This is a compositional design, **not** proof that the three programmes are completely integrated. A statistically excellent warning that arrives after the only feasible response window is not sufficient; a quick safe response may need less expensive advance warning. The strong RA PNI action condition and MSCA's conditional control sufficiency are different tests.

No paper, Focus Group receipt, case analogy, preliminary review route or this public annex confers standards adoption or establishes empirical effectiveness. The value of this annex is a traceable set of scientific prerequisites and architectural interfaces: **RA qualifies observable regime continuity and may emit a qualified directional delta; EA qualifies the mission-level use of that evidence and what must be reopened; MSCA can mechanically align the delta with its represented/control-capability frontier; Operation/Repositioning classifies drift/posture and proposes or escalates role/contract transitions; legitimate owners and controllers retain action authority.** All original EA frozen baseline parts and the RA working paper remain unmodified.
