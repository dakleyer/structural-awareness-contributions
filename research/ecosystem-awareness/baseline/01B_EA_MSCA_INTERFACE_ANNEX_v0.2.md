# Annex 01B — Ecosystem Awareness / Minimum Sufficient Control Architecture interface

**Status:** public working interface annex, v0.2, 23 September 2026. Additive companion to the Ecosystem Awareness (EA) corpus; not one of the six controlled/frozen v0.4 release-baseline documents. This is a proposed cross-programme integration surface, not a deployed interface, completed joint validation, ITU-T deliverable, FG-AI4SSC/FG-TIDA adoption, production certification or substitute for the future Canonical MSCA Architecture.

**Supersedes for current reading:** [v0.1](./01B_EA_MSCA_INTERFACE_ANNEX_v0.1.md), which remains preserved for provenance.

## 1. Purpose and current source boundary

EA and Minimum Sufficient Control Architecture (MSCA) answer different questions.

- **EA** qualifies what a participant can responsibly rely on for a declared decision, scope and time in a changing ecosystem, including A/B/C/D epistemic position, source dependence, residual/UNKNOWN, finite determination capacity and targeted requalification.
- **MSCA** represents and assesses which authorized control configuration is sufficient to keep owner-declared outcomes within an acceptable Objective Envelope under stated operating assumptions, and which supported alternative has the lowest justified burden among the alternatives actually assessed.
- **ACC / participation governance** may constrain whether participation, roles or signalling behaviour are admissible.
- **Identity / delegated authority / policy / attestation** establish who/what is acting and which mandate, capability or permit is valid.
- **Ecosystem Signalling / EHD** carries bounded qualified state and compatibility metadata across independently governed participants.
- **Execution / defence / actuation** remains with the function that already holds legitimate authority.

No layer substitutes for another. EA does not create authority or control sufficiency. MSCA does not create epistemic truth, identity, authority, participation legitimacy or a Semantic Window. A successful signal transport or compatibility mapping does not by itself establish evidence sufficiency.

The current MSCA corpus entry point is [Minimum Sufficient Control / MSCA](../../../standards/minimum-sufficient-control/README.md). It now distinguishes the stable working S/E/C/P/M semantics from three still-pending canonical documents: Canonical MSCA Architecture, Canonical MSCA Operation and MSCA Control Positioning. Until those documents exist, this annex uses the current common MSCA semantics without treating the urban/smart-city working paper as the generic canonical specification.

The **MSCA representation/schema instance** and an **MSCA sufficiency determination** are distinct objects. For discovery/interchange, S/E/C/P/M may be represented with qualified values, UNKNOWN or UNPOPULATED fields; an entirely unpopulated instance is a valid representation with status UNASSESSED, not a supported minimum. SUPPORTED, FAILED and UNRESOLVED remain assessment outcomes that require the applicable objective/assumptions, evidence and authority for the declared scope.

The public FG-AI4SSC input [FGAI4SSC-I-097](../../../submissions/itu-fg-ai4ssc/FGAI4SSC-I-097/README.md) introduced Minimum Sufficient Control as an architectural property of AI-enabled urban systems. Its receipt/posting is not adoption. The [MSCA working paper on Tegrity.AI](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/) develops a concrete, **illustrative urban/smart-city implementation mapping** in §5.1 and staged assessment in §5.2. [Ecosystem Awareness II](./ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md) develops the multi-optima research lineage. [01H](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) later made sparse/empty participant-local MSCA representation explicit; [01I](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) added the neighbouring participation/admissibility layer; and [01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) added bounded signalling, compatibility profiles and ACC-defined signalling modules.

**Source-defined versus proposed.** The present common S/E/C/P/M semantics are reconstructed from the submitted/working MSCA line and subsequent public reconciliation. The §3 source-profile handoffs below come from the urban/smart-city working paper and remain illustrative. The EA↔MSCA payloads, signalling/ACC boundaries and interface sequence in §§4–7 are this annex's candidate integration interpretation. They are not fields in FGAI4SSC-I-097, not an implemented API, not mandatory MIM semantics and not a completed standards result.

## 2. Architectural objects and ownership

| Object | Responsible owner | Meaning at this boundary |
|---|---|---|
| **S — Objective Envelope S(t)** | Legitimate mission/service/institutional owner | Declared outcomes, acceptable ranges and non-compensable constraints. MSCA and EA may represent or qualify S but cannot self-author or silently relax it. |
| **E — operating assumptions / environment** | Mission/service owner plus qualified operational evidence | Conditions under which a sufficiency claim applies: demand, disruptions, information quality, infrastructure, staffing, dependencies, actors, applicable regime and other material conditions. |
| **C — coordination scope** | Authorized operator / architecture function | Actors or flows that can be observed, coordinated, directly controlled or legitimately influenced, including mandate/reach and coverage gaps. Connectivity alone does not create reach or authority. |
| **P — intervention mechanisms** | Authorized operator / control function | Feasible routing, scheduling, access, containment, migration/reconfiguration or other interventions with preconditions, latency, reversibility and authority requirements. |
| **M — enabling means** | Existing systems / adapters / capability owners | Observation, communication, interoperability, computation/processing where relevant, actuation and separate effect-measurement capabilities. MSCA may incorporate existing mechanisms; it does not prescribe one universal stack. |
| **MSCA representation state** | Participant-local MSCA representation | Versioned S/E/C/P/M values that may be qualified, partial, UNKNOWN or UNPOPULATED. Representation does not imply sufficiency. |
| **MSCA assessment state** | MSCA assessment function under legitimate owner criteria | UNASSESSED / SUPPORTED / FAILED / UNRESOLVED for the declared configuration, scope, evidence and time. |
| **Epistemic qualification** | EA F1–F9 and participant-local EA mechanisms | Decision/scope-indexed evidence, source dependence, residual/UNKNOWN, finite capacity, validity and targeted requalification. |
| **Participation / admissibility** | ACC / legitimate governance owner | Membership, roles, obligations/prohibitions, non-compensable participation constraints and, where applicable, signalling obligations. |
| **Identity / authority / permit** | Legitimate identity/delegation/policy/authorization mechanisms | Establishes actor binding, mandate, scope, validity and explicit permit/refusal. Neither EA nor an MSCA sufficiency verdict creates these. |
| **Signal compatibility / normalization** | Ecosystem Signalling receiver-side qualification | Determines whether a native, legacy or specialised signal can be mapped into bounded qualified state and preserves compatibility/capability residuals. |
| **Semantic Window W(d,t)** | EA F2 | Decision-scoped active observation/interpretation boundary. MSCA may change available means/capacity that justify requalification, but does not own W(d,t). |

The sufficiency problem is **conditional and multi-objective**. For a candidate configuration x=(C,P,M), MSCA assesses x against the applicable S and E and distinguishes SUPPORTED, FAILED and UNRESOLVED. Selection or preference among supported alternatives may consider burden, reach, latency, human capacity, infrastructure, privacy, intervention intensity, switching cost and other owner-authorized trade-offs. A finite tested set cannot prove a global minimum, and one scalar burden score must not silently erase non-compensable constraints.

The symbol **x** is deliberately used for a candidate control configuration. It must not be called **A**, because A is already the canonical EA epistemic position for sufficiently determined state.

## 3. Source-profile mapping from the published urban/smart-city working paper

This section preserves the useful concrete mapping from the current MSCA working paper while making its status explicit: it is an **illustrative source profile**, not the generic canonical MSCA topology. C, P and M are dimensions, not three mandatory software products.

| Source-profile responsibility | Consumes | Delivers | Required boundary |
|---|---|---|---|
| DESIGN / candidate assessment | Owner-approved S, mandatory constraints and contingency policy; E; candidate C/P/M configurations; evidence for each candidate | Per-candidate SUPPORTED / FAILED / UNRESOLVED; supported set; after owner trade-off and separate authorization, a versioned sufficiency record or no deployment approval | Selection is only among assessed supported alternatives; FAILED is not UNRESOLVED. |
| M observation adapters | Existing telemetry, events and human reports | Observations annotated with source, time, quality and scope | Freshness/provenance must survive transport. An observation is evidence, not an objective verdict. |
| C coordination registry | Observations, declared scope and current mandates | Reachable actors, legitimate influence and coverage gaps | Reach may be narrower than apparent connectivity; no mandate is inferred from interoperability. |
| P intervention catalogue and planner | Current state, C reach, S/objectives, hard constraints and action preconditions | Feasible action candidates and a bounded proposal, possibly no change | A high planning score neither proves constraint satisfaction nor gives actuation authority. |
| MSCA assessment | Candidate configuration, evidence, applicable S/E and declared assessment criteria | SUPPORTED / FAILED / UNRESOLVED | Sufficiency assessment is distinct from authorization. |
| Authorization gate | Qualified proposal, current permissions/mandates, expiry and applicable governance | Scoped permit / refusal / other owner-defined authorization state | An independent authorization function may refuse a SUPPORTED proposal; UNRESOLVED is never laundered into permission. |
| M command/effect adapters | Versioned proposal, permit, expiry and rechecked preconditions | Execution receipt **and separately observed effect**, linked to the evidence log | Dispatch rechecks permission/configuration validity; receipt alone cannot prove outcome. |
| Effect evaluator / exception path | Receipt, effects, S, E and response deadline | Outcome check; CONTINUE within recorded scope if supported, otherwise explicit exception and REASSESSMENT_REQUIRED | Contingency applies only if currently authorized and feasible; rejection, timeout or missing effect cannot be silent success. |

The working-paper record binds S, E, configuration, evidence, decision owner, permissions, deadlines and contingency policy. A shared operation identifier may link observation, reach, proposal, permit, command receipt and measured effect; configuration version, provenance, timestamps, permission reference and expiry preserve the conditions behind each step. These remain **illustrative integration requirements**, not mandatory generic MSCA fields or a published executable API.

The xSeil/urban source profile is useful evidence of implementation thinking but does not establish causal regional benefit, generic MSCA minimality, comparative superiority, universal domain validity or production certification.

## 4. Candidate EA → MSCA qualified inputs

EA does not originate S(t), participation legitimacy, identity or control mandates. Its proposed contribution is a **qualified decision frame** for assessing whether an MSCA representation or sufficiency claim can be relied upon for the current decision.

| EA source / qualified state | Candidate input to MSCA | Why MSCA would consume it |
|---|---|---|
| F1 mission/context qualification | Decision/mission identifier; material domains; criticality; tolerated residual; response capability; human/compute capacity; useful-response deadline | Bind a sufficiency claim to the affected objective, consequence, capacity and decision horizon. S still comes from the legitimate owner. |
| F2 Semantic Window / acquisition-pathway qualification | W(d,t), freshness/coverage, provenance, missing/costly pathways, expected acquisition value | Test whether current M observation/signalling means are adequate without treating more data as automatically better. |
| F3/F4 local/external evidence qualification + F5 composition | Scope-indexed claims, A/B/C/D qualification where material, inherited uncertainty, source dependence, coupling, compatibility residual and unresolved/structural residual | Prevent an MSCA assessment from relying on duplicated evidence, foreign scope, unqualified translation or false systemic closure. |
| F6 operating-frame assessment | Qualified current frame and EA healthy posture: Normal / Containment / Migration-Regime Transition, with recorded residual | Ask whether current E and the assumptions supporting the control configuration still hold. These are EA epistemic-management postures, not MSCA actuation modes or permits. |
| F7 targeted requalification + F8 bounded statement | Affected domain/dependency, what changed, capacity gap, residual, requested requalification, receiver-specific bounded statement | Reassess only materially affected S/E/C/P/M assumptions; avoid a universal “add control” response. |
| F9 feedback/revalidation | Outcome-to-assumption discrepancy, pathway learning and reason for reopening the frame | Re-enter MSCA assessment after material change instead of carrying forward an expired sufficiency claim. |
| Qualified Ecosystem Signalling input | Native or compatibility-mapped external signal that survived receiver-side semantic/epistemic qualification, including provenance, freshness and residual | Allow MSCA to use external evidence or capability information without confusing transport success with qualified evidence. |

### 4.1 Signal admissibility for MSCA evidence

MSCA may receive observations or capability information through native EA signalling, legacy telemetry, bounded compatibility mappings or ACC-defined specialised signalling modules. The path may be:

external signal → compatibility mapping → receiver-local epistemic qualification → bounded normalized state → MSCA

Only the part that survives this path is eligible as decision-relevant MSCA evidence. Opaque or unsupported payloads may trigger discovery/requalification but MUST NOT be treated as normalized control evidence merely because transport succeeded.

If a compatibility profile or reasoning-assisted mapping introduces uncertainty, the receiver retains the compatibility/capability residual. A deterministic mapping may justify high confidence in the decoding semantics it actually guarantees while still preserving physical measurement error, capability limits and structural residual outside the verified profile.

This boundary follows [01J Ecosystem Signalling](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). It does not turn MSCA into the owner of signalling semantics.

## 5. Candidate MSCA → EA qualified outputs

EA must be able to consume **partial, unresolved and negative MSCA state**, not only a SUPPORTED configuration.

| MSCA output | EA consumer | Qualification EA must retain |
|---|---|---|
| Versioned **partial or complete S/E/C/P/M representation**, including UNKNOWN / UNPOPULATED fields | F1/F2/F5/F6/F8 | Representation is not sufficiency. Missing fields remain missing; EA must not infer a supported minimum from schema presence. |
| UNASSESSED representation | F1/F6/F8 | Means no sufficiency determination has been established for the declared scope; it is not FAILED and not SUPPORTED. |
| SUPPORTED / FAILED / UNRESOLVED assessment for candidate x | F6/F7/F8 | Assessment is scoped to S/E/evidence/version/time. UNRESOLVED is neither proof of insufficiency nor permission. |
| Supported-set / alternative-configuration information and burden data | F1/F2/F6/F7 | EA may use response capacity, switching burden and useful-response margin to requalify where additional determination still has value; no global optimum is implied. |
| Reachable actors, coordination/mandate coverage and coverage gaps | F1/F5/F6 | Distinguish technical connectivity, legitimate influence and explicit authority. |
| Available P/M capabilities, latency, effectiveness, reversibility, contingency and resource capacity | F1/F2/F6/F7 | Recalculate proportionate observation/warning need and response horizon; no response capability may be invented to justify a detector. |
| Known control/capability gap or no supported configuration | F6/F7 | Preserve the gap explicitly and request bounded requalification/escalation where material; do not silently relax S. |
| Observation/proposal/receipt/effect records linked to an operation | F4/F5/F9 | Preserve provenance, freshness, scope and dependency lineage. Receipt is not measured effect. |
| Change-triggered reassessment request / invalidated prior support | F6/F7/F9 | Requalify dependent assumptions rather than globally invalidating unrelated state. |

### 5.1 Authorization is not an MSCA assessment output

A scoped **permit/refusal** may be associated with the same operation, but it belongs to the legitimate authorization mechanism, not to the semantic meaning of SUPPORTED / FAILED / UNRESOLVED.

The interface therefore keeps at least these objects distinct:

MSCA assessment ≠ authority/permit state ≠ EA epistemic qualification ≠ execution result.

A SUPPORTED configuration may still be refused. A valid permit may expire or become inapplicable after E, authority or other preconditions change. A fresh permit cannot convert an epistemically unsupported or stale input into qualified evidence.

## 6. ACC, signalling, authority and extensibility boundary

### 6.1 ACC / participation profile

An applicable [Agentic Citizenship Contract / participation profile](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) may define membership, role eligibility, obligations/prohibitions, non-compensable constraints and required signalling behaviour.

At the EA↔MSCA boundary:

- ACC may constrain which candidate transitions or roles are admissible;
- an ACC-defined signalling profile may determine what a participant must communicate and to whom;
- identity/delegation/policy mechanisms still establish actual authority;
- MSCA may consume these qualified constraints/references but does not author the ACC or grant itself membership/authority;
- a technically feasible or MSCA-SUPPORTED action may remain inadmissible or unauthorized.

### 6.2 Ecosystem Signalling

[Ecosystem Signalling 01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) provides the generic bounded signalling and compatibility layer. It may normalize richer ACC-specific signalling modules or simpler legacy/telemetry signals into receiver-local qualified state.

A full MSCA export is not universally required. A signal may carry or reference only the material S/E/C/P/M delta, capability, burden, assessment state or limitation needed by the receiver. Omitted components remain UNKNOWN / NOT DECLARED unless a verified compatibility/profile mapping legitimately supplies receiver-local qualification.

### 6.3 Extensibility

The future Canonical MSCA Architecture is expected to define generic upward, downward and horizontal extensibility. This interface already preserves the necessary boundary:

- **downward:** a participant may expose a sparse/legacy MSCA representation and remain interoperable;
- **upward:** richer domain profiles may refine S/E/C/P/M without redefining their canonical meanings;
- **horizontal:** different domains may map their own controls/resources into S/E/C/P/M while retaining the same semantic ownership.

This annex does not itself declare a domain profile canonical. The urban/smart-city paper and DAOS remain source/example material, not definitions of generic MSCA.

### 6.4 Future Control Positioning

The MSCA corpus reserves **MSCA Control Positioning** as a pending canonical specification. Until that document exists, this annex may exchange current/alternative configuration, support state, burden, capability gaps and transition-relevant data, but it MUST NOT invent a normative control-position object or gradient semantics on behalf of MSCA.

EA's Decision-Scoped Epistemic Opportunity remains an epistemic/value-of-information ordering; it is not automatically identical to a future MSCA control-transition ordering.

## 7. Candidate interface interaction sequence and falsifiable checks

This section defines only the **cross-boundary interaction sequence**. It is not the Canonical MSCA Operation specification.

1. **Bind the decision.** A legitimate owner supplies or references S, decision scope, applicable constraints, authority owner, horizon and expiry. The participant may already hold a partial S/E/C/P/M representation.
2. **Qualify the frame.** EA qualifies evidence, W(d,t), provenance/source dependence, A/B/C/D state, residual, compatibility limitations, capacity and useful response margin without rewriting S or authority.
3. **Assess MSCA state.** MSCA may return UNASSESSED, SUPPORTED, FAILED or UNRESOLVED for candidate configurations under the current S/E frame, together with partial/complete representation, evidence limits, capabilities, burden and gaps.
4. **Keep authorization separate.** If an action is proposed, the legitimate authorization mechanism independently verifies identity/mandate/permit conditions. MSCA support does not issue permission.
5. **Execute outside the interface.** An authorized execution/control function acts, if permitted. Receipt and separately measured effect remain distinct.
6. **Requalify dependencies.** A material change in S, E, C, P, M, EA frame, ACC applicability, authority, signalling compatibility, evidence freshness/capacity or measured effect invalidates only dependent claims and requests targeted requalification.

A future interoperability test should deliberately vary:

- evidence freshness and source dependence;
- partial versus complete S/E/C/P/M representation;
- UNASSESSED / SUPPORTED / FAILED / UNRESOLVED states;
- compatibility-profile quality and residual;
- actor mandate / ACC admissibility / permit expiry;
- operator and human capacity;
- disturbance and action preconditions;
- response latency / burden;
- receipt versus independently measured effect.

It should verify at minimum that:

1. EA does not convert local support into ecosystem-wide certainty.
2. MSCA does not convert UNKNOWN/UNPOPULATED or UNRESOLVED state into SUPPORTED.
3. Signal transport or compatibility success is not treated as evidence sufficiency.
4. ACC admissibility, authority/permit and MSCA sufficiency remain distinct.
5. A stale or materially invalidated S/E/configuration is not carried forward as current support.
6. A receipt without measured effect cannot close the loop.
7. Sparse/legacy participants can interoperate without requiring a complete MSCA export.
8. A richer domain-specific profile cannot silently redefine S/E/C/P/M.

These are **proposed tests**, not completed validation.

### 7.1 Joint-operation boundary with Regime Awareness

Where an MSCA decision is specifically triggered or justified by a Regime Awareness posture, pairwise EA↔MSCA qualification is not enough. The candidate [operation-composition profile 01D](./01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) binds current S/E/C/P/M support and mandate/permit to EA qualification and scoped RA evidence/action-safety versions, with an explicit fail-closed rule for essential invalidation.

An advisory RA monitor is not a universal veto on an independently authorized MSCA action. A fresh RA signal cannot extend an expired permit; a fresh permit cannot repair an unsupported RA representation or stale EA/MSCA frame.

## 8. Limits, provenance and programme placement

The mobility-derived xSeil/urban case in the MSCA working paper is a retrospective, bounded source profile. Its private fleet objective cannot stand in for a city's legitimately declared public Objective Envelope, and the urban framing cannot stand in for generic MSCA.

The [DAOS case](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/README.md) supplies a separate extensible authority/commitment fixture. Its upward/downward/horizontal extension logic may inform later MSCA profile design, but its semantics are not silently imported into MSCA core.

EA's general architecture is not limited to FG-TIDA Theme #13. MSCA's submitted FG-AI4SSC context is not a general adoption. 01I/01J are additive working extensions and do not establish an adopted interprogramme protocol.

No platform, MIM extension, Python module, BPMN workflow, signalling transport, adapter registry, SLM compatibility component or message schema is prescribed by this annex. Implementations may realize the semantics differently if the ownership boundaries, qualification states, lineage and falsifiers remain inspectable.

For the general EA foundation and the system-security versus ecosystem-security distinction, see [Two Foundational Origins](./01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md). For participant-local sparse MSCA representation, see [01H](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md). For current MSCA corpus status and pending canonical documents, see the [MSCA corpus entry](../../../standards/minimum-sufficient-control/README.md).

This annex updates the **current interface reading** while preserving the v0.1 file, controlled/frozen EA baseline documents and original focus-group submission artefacts unchanged.
