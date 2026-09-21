# Annex 01B — Ecosystem Awareness / Minimum Sufficient Control Architecture interface

**Status:** public working interface annex, v0.1, 15 September 2026. Additive companion to the Ecosystem Awareness (EA) corpus; not one of the six controlled/frozen v0.4 release-baseline documents. This is a proposed cross-programme integration, not a deployed interface, a completed joint validation, an ITU-T deliverable, or FG-AI4SSC/FG-TIDA adoption.

## 1. Purpose and source boundary

EA and Minimum Sufficient Control Architecture (MSCA) address different questions. EA qualifies what the system can responsibly infer about a decision-scoped, changing ecosystem, including residual indeterminacy, evidence dependence, operating-frame validity and finite determination/response capacity. MSCA asks which *authorized configuration of coordination, interventions and enabling means* is sufficient to keep owner-declared outcomes within an acceptable Objective Envelope under stated conditions, and which supported alternative has the lowest justified intervention burden. EA supplies a candidate requalification capability; MSCA supplies a candidate architectural selection and operating-control capability. Neither alone authorizes the other.

The **MSCA representation/schema instance** and an **MSCA sufficiency determination** are distinct objects. For discovery/interchange, S/E/C/P/M may be represented with qualified values, UNKNOWN or UNPOPULATED fields; an entirely unpopulated instance is a valid representation with status UNASSESSED, not a supported minimum. SUPPORTED, FAILED and UNRESOLVED remain assessment outcomes that require the applicable objective/assumptions, evidence and authority for the declared scope.

The public FG-AI4SSC input [FGAI4SSC-I-097](../../../submissions/itu-fg-ai4ssc/FGAI4SSC-I-097/README.md) introduced Minimum Sufficient Control as an architectural property of AI-enabled urban systems. Its receipt/posting is not adoption. The [MSCA working paper on Tegrity.AI](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/) develops a concrete, **illustrative** implementation mapping in §5.1 and staged assessment in §5.2. The [Minimum Sufficient Control standards working note](../../../standards/minimum-sufficient-control/README.md) states the architectural question and five candidate dimensions. The [EA Functional Architecture v0.4](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md) and [part 2](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part02.md) define F1–F9. [Ecosystem Awareness II](./ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md) develops the multi-optima research lineage; it is not a substitute for the submission or proof of a globally minimal design.

**Source-defined versus proposed:** the S/C/P/M dimensions and the §5.1 MSCA component handoffs below are described in the submitted/working MSCA line. The EA↔MSCA payloads and call sequence in §§4–6 are *this annex's candidate interface interpretation*, not fields in FGAI4SSC-I-097, not an implemented API, and not mandatory MIM semantics. Where the article adds responsibilities beyond the original input, it is cited as the 15 September 2026 working paper rather than attributed retroactively to the submitted PDF.

## 2. Architectural objects and ownership

| Object | Responsible owner | Meaning at this boundary |
|---|---|---|
| Objective Envelope S(t) | Legitimate city/service/mission owner | Declared outcomes, acceptable ranges and non-compensable mandatory constraints; the control system cannot set or silently relax it. |
| Operating assumptions E | Service/mission owner with operational evidence | Conditions under which a sufficiency claim applies: demand, disruptions, information quality, infrastructure, staffing, actors and other material dependencies. |
| C — coordination scope | Authorized operator/architecture function | Actors or flows of what type and proportion that can be observed, coordinated, directly controlled or legitimately influenced; mandate and coverage gaps matter. |
| P — intervention mechanisms | Authorized operator/control function | Feasible routing, scheduling, access, containment or other actions with preconditions, authority and timing; a detected problem does not imply an executable repair. |
| M — enabling means | Existing system/adapters | Observation, messaging, interoperable interfaces (including usable MIMs), actuation and separately measured effects. MSCA can incorporate MIMs inside M; it does not replace MIMs or prescribe a universal stack. |
| Epistemic/operating-frame qualification | EA candidate functions F1–F9 | Scope-indexed evidence, source dependence, residual/UNKNOWN, capacity, validity and targeted requalification; an EA assessment is not permission to act. |

The sufficiency problem is **conditional and multi-objective**: assess candidate A=(C,P,M) against S and E; distinguish SUPPORTED, FAILED and UNRESOLVED; select by owner-authorized burden trade-off only among supported alternatives. A finite tested set cannot prove a global minimum. Burdens include reach, collection, staffing, infrastructure and intervention intensity; one arbitrary score must not hide conflicting constraints. [MSCA working paper §§2, 5–5.1](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/); [EA multi-optima lineage §§4–6](./ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md).

## 3. MSCA functions: concrete inputs and outputs in the published working paper

This table translates the **illustrative** handoff table and pseudocode in [MSCA §5.1](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/) into inspectable responsibilities. C, P and M are dimensions, not three mandatory software products.

| Function / responsibility | Consumes | Delivers | Required boundary |
|---|---|---|---|
| DESIGN / candidate assessment | Owner-approved S, mandatory constraints and contingency policy; E; candidate C/P/M configurations; evidence for each candidate | Per-candidate SUPPORTED / FAILED / UNRESOLVED; supported set; after owner trade-off and authorization, a versioned sufficiency record or no deployment approval | Selection is only among assessed supported alternatives; FAILED is not UNRESOLVED. |
| M observation adapters | Existing telemetry, events and human reports | Observations annotated with source, time, quality and scope | Freshness/provenance must survive transport. An observation is evidence, not an objective verdict. |
| C coordination registry | Observations, declared scope and current mandates | Reachable actors, legitimate influence and coverage gaps | Reach may be narrower than apparent connectivity; no mandate is inferred from interoperability. |
| P intervention catalogue and planner | Current state, C reach, S/objectives, hard constraints and action preconditions | Feasible action candidates and a bounded proposal, possibly no change | A high planning score neither proves constraint satisfaction nor gives actuation authority. |
| Assessment and authorization | Evidence, proposal, approved envelope and current permissions | SUPPORTED / FAILED / UNRESOLVED judgment; scoped permit or refusal | The independent authorization gate may refuse even a feasible plan; unresolved evidence cannot be laundered into approval. |
| M command/effect adapters | Versioned proposal, permit, expiry and rechecked preconditions | Execution receipt **and separately observed effect**, linked to the evidence log | Dispatch rechecks permission/configuration validity; receipt alone cannot prove outcome. |
| Effect evaluator / exception path | Receipt, effects, S, E and response deadline | Outcome check; CONTINUE within recorded scope if supported, otherwise explicit exception and REASSESSMENT_REQUIRED | Contingency applies only if currently authorized and feasible; rejection, timeout or missing effect cannot be silent success. |

The §5.1 record binds S, E, configuration, evidence, decision owner, permissions, deadlines and contingency policy. A shared operation identifier links observation, reach, proposal, permit, command receipt and measured effect; configuration version, provenance, timestamps, permission reference and expiry preserve the conditions behind each step. These are **illustrative integration requirements**, not new normative MIM fields or a published executable API. §5.2 separates replay/shadow assessment from separately authorized bounded live pilots and from production approval.

## 4. Candidate EA → MSCA inputs

EA does not originate S(t) or control mandates. Its proposed contribution is a *qualified context for assessing whether the owner-approved S/C/P/M record remains supportable*. No EA status alone is a command or permission.

| EA source | Candidate input to MSCA | Why MSCA would consume it |
|---|---|---|
| F1 mission/context qualification | Decision/mission identifier; material domains, criticality, tolerated residual, finite determination capacity, response capability and deadlines | Bind a sufficiency claim to the affected objective, consequence and feasible response horizon. S still comes from the authorized owner. |
| F2 window and acquisition-pathway qualification | Selected observation boundary, freshness/coverage, provenance and missing or costly pathways | Test whether M's observation means are adequate for the stated scope without treating more data as automatically better. |
| F3/F4 local/external evidence qualification and F5 composition | Scope-indexed local/external claims, inherited uncertainty, source dependence, coupling and explicitly unresolved/structural residual | Prevent a supported C/P/M claim from relying on duplicated evidence, foreign scope or false systemic closure. |
| F6 operating-frame assessment | Qualified operating-envelope status, epistemic condition and Normal / Containment / Migration-preparation assessment | Ask whether the current E and response mapping still support the existing MSCA record. These are EA assessments, not MSCA actuation modes. |
| F7 targeted directives and F8 bounded statement | Affected domain/dependency, what changed, residual, capacity gap, requested requalification and bounded statement for the receiver | Reassess only the materially affected S/E/C/P/M assumptions; avoid a universal “add control” response. |
| F9 feedback/revalidation | Outcome-to-assumption discrepancy and reason for reopening the frame | Re-enter MSCA assessment after material change instead of carrying forward an expired sufficiency claim. |

F1–F9 meanings are from [EA Functional Architecture v0.4, parts 1–3](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md); [part 2](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part02.md); [part 3](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part03.md). The proposed packaging in this table is new; the frozen EA functional definitions are untouched.

## 5. Candidate MSCA → EA outputs

| MSCA output | EA consumer | Qualification EA must retain |
|---|---|---|
| Versioned supported C/P/M configuration, S/E scope, assumptions, evidence and limits | F1/F6/F8 | “Supported” means within tested/declared conditions, not ecosystem-wide certainty or a globally minimal architecture. |
| Reachable actors, mandates, coverage gaps and available interventions | F1/F5/F6 | Distinguish a technical path from legitimate influence; a control in one domain cannot automatically compensate for epistemic failure in another. |
| Intervention burden, response latency, effectiveness, reversibility and contingency capacity | F1/F2/F6/F7 | Recalculate proportionate observation/warning need and escalation margin; no response capability may be invented to justify a detector. |
| SUPPORTED / FAILED / UNRESOLVED candidate verdict and scoped permit/refusal | F6/F7 | Keep evidence sufficiency distinct from authorization and epistemic validity. UNRESOLVED is neither proof of insufficiency nor approval. |
| Operation-linked observation, proposal, permit, receipt and separately measured effects | F4/F5/F9 | Maintain provenance, freshness, scope and dependency lineage; a dispatch acknowledgement is not measured service outcome. |
| Explicit exception, unresolved effect, failed precondition or change-triggered reassessment request | F6/F7/F9 | Requalify the affected operating frame; do not silently relax S or infer a universal safe shutdown. |

These are proposed consumer mappings to the article's explicit MSCA outputs, not claims that the existing EA and MSCA implementations already exchange these records. The article's xSeil retrospective case offers inspectable planning/monitoring/reassignment evidence, but **does not** establish causal regional traffic benefit, MSCA minimality, comparative superiority or a validated deployment; its code and comparative MSCA tests remain open ([MSCA §4](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/)).

## 6. Proposed interaction and falsifiable checks

1. **Declare:** the legitimate owner supplies S, constraints, decision rights, expiry and contingency; operators describe E, candidate C/P/M means and existing evidence. EA qualifies the decision-scoped ecosystem frame without rewriting S.
2. **Assess and select:** MSCA tests candidates against S and E, preserving FAILED versus UNRESOLVED, and records the owner's chosen supported alternative, burden trade-offs and scope. An unresolved set produces re-assessment or no approval, not a fabricated minimum.
3. **Operate within authority:** M observes; C resolves actual mandate/reach; P proposes feasible action; an authorization gate issues or refuses a scoped permit; M dispatches only after recheck; measured effect is evaluated separately from receipt.
4. **Requalify:** EA compares the result and changing dependencies against the supporting frame. It requests targeted MSCA reassessment if S, E, C, P, M, authority, response capacity or evidence validity materially changes. MSCA returns the new support/exception/coverage record; EA preserves inherited uncertainty. MSCA reassessment may change available observation/signalling means, coordination reach, response capacity or candidate control configuration; those outputs may cause F2 to requalify, expand, narrow or redirect W(d,t), but MSCA does not itself own or modify the Semantic Window. Either side may request requalification, but only authorized owners/controllers approve or execute a new posture.

A future interoperability test should deliberately vary evidence freshness, source dependence, actor mandate, operator capacity, disturbance, action preconditions and observed effect. It should verify that (i) EA does not turn local support into ecosystem certainty, (ii) MSCA does not act on an expired/UNRESOLVED frame, (iii) authorization stays outside epistemic assessment, and (iv) a receipt without effect evidence cannot close the loop. These are **proposed tests**, not completed validation. The [EA validation apparatus](./README.md#validation-profiles) and [MSCA §5.2 deployment proposal](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/) are neighbouring routes, not an already integrated test suite.

**Joint-operation boundary:** where an MSCA decision is *specifically triggered or justified* by a Regime Awareness posture, pairwise EA↔MSCA qualification is not enough. The candidate [operation-composition profile 01D](./01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) binds current S/E/C/P/M support and mandate/permit to EA Q and scoped RA evidence/action-safety versions, with an explicit fail-closed rule for essential invalidation. An advisory RA monitor is not a universal veto on an independently authorized MSCA action. This is a proposed integration test, not a published MSCA implementation.

## 7. Limits and programme placement

The mobility-derived xSeil case in the MSCA paper is a retrospective, bounded illustration. Its private fleet objective cannot stand in for a city's legitimately declared public Objective Envelope. The developing cross-focus-group case/extensibility package may provide shared challenges, use cases and Terms-of-Reference traceability later; **this annex does not claim that EA, MSCA and that package are completely integrated**. EA's general architecture is not limited to FG-TIDA Theme #13, and MSCA's submitted FG-AI4SSC context is not a general adoption. No platform, MIM extension, Python module, BPMN workflow or message schema is prescribed here.

For the general EA foundation and the system-security versus ecosystem-security distinction, see [Two Foundational Origins](./01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md). This annex adds a bounded architectural relationship and explicit I/O map while leaving all controlled/frozen release-baseline and original focus-group contribution files byte-for-byte unchanged.
