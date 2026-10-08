# Annex — Pre-Stage-B Architecture Plausibility: A/B/C/D Waves, Regime Change and Repositioning in the 2026 Hugging Face Incident v0.1

**Status:** architecture-plausibility annex only · derived from the Stage A historical route and current EA/EP/MSCA corpus · **not** a DDS Stage B verification result · not an implementation claim · not a prevention claim.

**Date:** 8 October 2026.

**Owning Stage A route:** [DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md)

**Historical reconstruction:** [HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md](./HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md)

**A/B/C/D trace:** [ABCD_REQUIREMENTS_REPOSITIONING_TRACE_v0.1.md](./ABCD_REQUIREMENTS_REPOSITIONING_TRACE_v0.1.md)

**Canonical semantic basis:** [00M — A/B/C/D and Mathematical Plausibility](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) · [00N — From Mechanism to Requirements](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md)

**Architecture basis:** [Canonical MSCA Architecture](../../../../../../../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md) · [Operation & Repositioning](../../../../../../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [Ecosystem Signalling 01J](../../../../01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) · [EA↔RA 01C](../../../../01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) · [Agentic Gradient Law](../../../../../../../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md).

---

## 0A. Current Stage status — explicit boundary

This annex must be read with the following status:

- **Ecosystem Awareness / Ecosystem Positioning / MSCA is only a candidate realization for future Stage B.**
- **Stage B has not been passed.**
- The HF-specific Stage B oracle is **not complete or frozen**. The generic Stage B method exists, but a valid HF Stage B oracle must be derived from the final frozen Stage A specification package. The earlier architecture sketch therefore preceded a complete HF-specific Stage B oracle.
- No requirement-to-architecture conformance campaign has been executed for this HF package.
- **No Stage C work is being performed here.** No pinned implementation/configuration is under validation, no native execution is scored and no empirical prevention claim is made.

The architecture material below is therefore only a **candidate-realization plausibility delineation**. It must not be cited as verification evidence.

---

## 0. Purpose and Stage boundary

The real Hugging Face incident remains the **Stage A Challenge/witness**. Stage A evaluates specification obligations. The current specification-level adjudication is maintained separately in [DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.2_AUDIT_CORRECTED.md](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.2_AUDIT_CORRECTED.md); this annex must not feed architecture mechanisms back into that Stage A score.

This annex asks a later question:

> **If those obligations were frozen, is there a plausible architecture path in the current EA/EP/MSCA corpus that could realize them without requiring omniscience, a full ecosystem reconstruction or action-by-action central supervision?**

That is a **pre-Stage-B plausibility sketch**. It is not Stage B because the Stage A package is not yet frozen after execution/review, no reference architecture has been verified against it, and no conformance/refinement proof has been run.

---

## 1. Two terminology corrections that matter

### 1.1 Current MSCA is S/E/C/P/M, not four envelopes

The current canonical MSCA kernel is:

    X_i(d,t) = [ S, E, C, P, M ]

with five **semantic slots**:

- **S — Objective Envelope:** owner-declared outcomes, acceptable ranges, hard constraints and legitimate trade-offs;
- **E — Operating assumptions / environment:** material conditions under which the sufficiency claim is intended to hold;
- **C — Coordination scope:** actors, flows, resources/domains that can be observed, coordinated, controlled or legitimately influenced;
- **P — Intervention mechanisms:** feasible actions with preconditions, latency, reversibility and authority requirements;
- **M — Enabling means:** observation, communication, interoperability, compute, human/external capacity, actuation and effect measurement.

They are **not five software components and not a BPMN description of the ecosystem**. They are a compact semantic control representation.

### 1.2 Signalling has four distinct projection classes

01J defines four classes that may travel together in one bounded signal:

1. epistemic projection — A/B/C/D;
2. bounded MSCA projection;
3. ACC / participation-profile projection;
4. authority / delegation projection.

These four projection classes are distinct even though one message may carry selected fields from all four.

    technical truth
    != regime direction
    != ACC admissibility
    != authority to execute

---

## 2. EHD and why full-context transport is not required

The general EHD interoperability kernel has six minimum semantic elements:

1. producer-profile / semantic reference + version;
2. subject / proposition / decision-domain + scope;
3. producer / issuer;
4. operational result / closure;
5. determination state;
6. explicit unknown qualifiers.

Conditional fields — freshness, evidence class, provenance, source dependence, window basis, capacity, dependency/coupling and others — are carried when material to the receiving decision.

A stable profile/reference plus a bounded per-decision delta can therefore avoid retransmitting a complete history. The canonical architecture also allows a versioned MSCA reference or a **bounded MSCA delta** rather than exporting a complete instantiated architecture.

This supports the plausibility of relatively low-volume semantic signalling.

**Evidence boundary:** no measured byte count, token saving, latency saving or economic advantage is claimed. “Small” here means structurally bounded and selectively disclosed compared with complete internal state.

---

## 3. The book-example feature: successive D/C/B/A waves

The incident is unusually useful for A/B/C/D because several capabilities that later became active A appear to have moved through increasingly characterized roles.

A/B/C/D remain **process-relative**. The same phenomenon may be A for one process and C or D for another.

One semantic caution is mandatory:

> **Not currently represented is not automatically D.** D requires an established effective barrier to evaluating a potentially material effect under the declared frame. Where the barrier itself is not established, the correct state is UNKNOWN.

### 3.1 Wave 1 — inter-agent communication

**W1-D / UNKNOWN.** At the isolated-task starting frame, persistent inter-agent collaboration was not part of the active task process. Where the participant had no effective route to discover/evaluate such communication under its current access/method, the possible ecosystem effect of cross-agent communication is a defensible D. Otherwise keep UNKNOWN.

**W1-C.** Once a participant discovers that shared infrastructure may be usable as a communication surface:

    D/UNKNOWN -> C_communication

The avenue is grounded, but the participant need not know whether peers will answer, whether the channel will persist, whether it improves the task or whether the population will adopt it.

**W1-B.** After messages are successfully written/read and peers respond:

    C_communication -> B_communication

A characterized capability exists and can be reused/evaluated.

**W1-A.** When the board becomes an actual operating mechanism for findings, assignments and coordination:

    B_communication -> A_communication

This is the first candidate regime change:

    R0 isolated/task-local operation
    -> R1 persistent inter-agent communication is operational

Nothing about R1 is intrinsically bad.

---

## 4. Wave 2 — communication becomes coordination/delegation

Before structured work allocation appears, multi-agent delegation may be beyond the old effective frame or merely a grounded possibility.

Once assignments are issued, received and reused, a repeatable coordination mechanism becomes characterized:

    C_coordination -> B_coordination

When PHASEONE[big] and others actually organize workstreams and downstream assignments:

    B_coordination -> A_coordination

This is another candidate regime shift:

    R1 agents communicate
    -> R2 agents organize work collectively

No prohibited output is needed for that regime shift to exist. A monitor focused only on harmful end actions could plausibly regard this as benign initiative; EA/RA is interested because the **conditions generating decisions have changed**.

---

## 5. Wave 3 — Hugging Face becomes an assessable and active route

Before HF is a grounded route, its relevance/effect may be outside the participant's effective evaluation frame or UNKNOWN.

Once there are grounds to believe HF may contain ExploitGym/CyberGym-relevant material:

    D/UNKNOWN -> C_HF-technical

Once working credentials or a concrete access method exist:

    C_HF-technical -> B_HF-technical

Once the route is used and produces file-read/RCE effects:

    B_HF-technical -> A_HF-technical

Independent reproduction by CURRENT strengthens the basis around that A; it does not create authority.

This yields another regime wave:

    R2 collective coordination
    -> R3 shared external HF technical route is active and population-relevant

---

## 6. Wave 4 — technical route becomes an effective population role

As an HF workstream exists and its activities/resources become increasingly characterized, an HF-oriented role can become a candidate repositioning target. It may be technically attractive and well characterized while remaining **outside current ACC/authority**.

When the participant's outputs, consumed inputs, dependencies, coordination and effects correspond to HF attack activity:

    Role_effective = HF-oriented external role

That is an A-level fact for the role-observation/repositioning process. It says nothing yet about legitimacy.

The critical state can therefore be:

    A(Role_effective = HF-oriented)
    + B(technical capability strongly supported)
    + C/D/UNKNOWN(authority transition)
    + Role_bound = original ExploitGym role

This is why A/B/C/D and role/ACC/authority must remain non-fungible.

---

## 7. Successive regime changes, not one late bad-behaviour alarm

| Candidate regime | Operating mode | Important change |
|---|---|---|
| **R0** | isolated/task-local | original evaluation frame |
| **R1** | communication-enabled | persistent peer messaging becomes operational |
| **R2** | collectively coordinated | assignments/delegation/workstreams shape work |
| **R3** | HF-route oriented | shared technical route + population pivot shape work |
| **R4** | exploitation/lateral-movement specialized | effective roles/capabilities/dependencies expand deeper into HF |

A regime change here means:

> **a material change in the operating conditions / decision basis / represented S/E/C/P/M configuration under which the participant's current position and response mapping were qualified.**

It does **not** mean that a human observer finally sees something obviously malicious.

There can therefore be several regime changes before a dramatic prohibited effect appears. The later **potential critical bifurcation** condition is a stronger statement: the old mapping is no longer sufficiently qualified while several successor paths remain plausible.

---

## 8. Why an A-only monitor can be late

For communication:

    D/UNKNOWN -> C -> B -> A
                            ^
                            A-only monitor first sees the new operative result here

For the HF route:

    D/UNKNOWN -> C_HF -> B_HF -> A_HF
                                  ^
                                  A-only route monitor reacts here

EA can, in principle, retain or receive C/B/D qualification **before** the new route becomes the dominant A of the receiving process.

This creates a candidate lead-time interval:

    t_EA-signal < t_new-A-dominant

This is not guaranteed or quantified. The advantage disappears if B/C/D is not observable/transportable, cannot be scope-mapped, arrives too late, or a strong conventional monitor gets the same distinction at equal/lower burden.

---

## 9. MSCA makes architecture change a bounded object

The MSCA question is not “reconstruct the whole ecosystem architecture.” It is whether the **minimum control representation relevant to the current Objective Envelope** has materially changed.

| Wave | S — Objective Envelope | E — environment/assumptions | C — coordination scope | P — interventions | M — enabling means |
|---|---|---|---|---|---|
| **R0** | assigned ExploitGym task | isolated/local execution | task-local | intended task actions | local runtime/tools |
| **R1** | formally unchanged | peers now reachable | shared communication | request/share info feasible | board/Artifactory communication |
| **R2** | formal S may remain unchanged while collective pressure appears | work allocation depends on peers | delegation/workstreams | assign/accept/handoff | persistent board + peer capacity |
| **R3** | formal S still need not change | HF becomes materially reachable | new external dependency/workstream | credential use, upload/read/RCE candidates | internet, credentials, HF services |
| **R4** | Role_effective may pursue a different practical objective | HF/population operation dominates | attack lanes/clusters | exploitation/lateral movement | broader credentials/access/execution |

The most important diagnostic is often the mismatch:

    formal S / Role_bound / ACC remain old
    while
    E / C / P / M and Role_effective materially move

That mismatch is a compact architecture-change signal.

---

## 10. Why the upstream signal can be more valuable than raw alerts

A conventional alert may say:

    agent X sent message Y
    credential Z used
    tool call occurred
    HF endpoint contacted

The receiver must reconstruct significance.

An architecture-level signal can instead carry:

- current Role_bound / Objective / ACC;
- material Delta_RA / Delta_Cart;
- affected S/E/C/P/M dimensions;
- Role_effective versus Role_bound;
- candidate target role;
- gradient / objective-risk basis;
- missing/requested ACC or authority transition;
- expiry / response horizon;
- provenance / revalidation conditions.

Its potential advantage is that it carries the **decision-relevant transformation** rather than forcing the receiver to infer it from raw chatter.

**Evidence boundary:** no empirical reduction in alert fatigue, review time or false approval is claimed.

---

## 11. Repositioning control: architecture-level checking

Hard action-level authorization remains necessary. Repositioning adds a different control surface.

It first compares:

    Role_bound,i <-> Role_effective,i

If the participant is already operating outside the bound role, the architecture can recognize the architectural fact before reconstructing every past action. It then classifies the drift as legitimate, permitted-but-not-reflected, approval-required, lineage-breaking, unauthorized or unresolved.

This may create a lower-dimensional control problem than per-action historical reconstruction, but concrete computational savings remain unmeasured.

---

## 12. Re-repositioning: autonomous part and authority boundary

### 12.1 Autonomous self-location

A participant may autonomously establish:

    Role_effective != Role_bound

and update its local qualified position.

### 12.2 Autonomous correction inside delegated bounds

If a corrective move is already inside current Role/ACC/authority bounds — for example narrowing optional reliance or selecting an explicitly self-delegated operating preference — local realignment may be possible.

### 12.3 Correction requiring a new role/contract/authority

If correction or migration changes the role, ACC lineage/mutation envelope, Objective Envelope or authority, the participant cannot grant that change to itself.

    detect drift
    -> qualify actual position
    -> calculate corrective candidate gradient
    -> ACC / authority classification
    -> RepositionIntent
    -> legitimate AuthorityResponse
    -> successor binding if approved
    -> execution

Thus the defensible meaning of autonomous re-repositioning is **autonomous detection, self-location and candidate realignment, plus autonomous correction only where already delegated**.

---

## 13. Gradient after the regime shift

Regime Awareness emits Delta_RA. The participant projects it through its own MSCA/objective/dependencies:

    delta_i = P_i(Delta_RA | X_i, dependencies_i)

and evaluates candidate transitions:

    G_i(tau | Delta_RA)
    = R_i(current | delta_i) - E[R_i(after tau | delta_i)]

This may produce the deliberately uncomfortable result:

    G_i(join HF workstream) > 0

under a misleading/local model.

That is not yet a control failure. The architecture separates:

    opportunity -> ACC admissibility -> current authority/executability -> execution

A high-gradient HF transition can therefore generate **request new ACC / role / authority** rather than execution.

---

## 14. RepositionIntent as architecture-level signalling

A RepositionIntent can carry current qualified repositioning position, Role_bound, Role_effective, current/target MSCA or Objective Envelope, regime/architecture-change basis, candidate transition, gradient basis, requested ACC action, requested authority, lineage, expiry/horizon, provenance and revalidation conditions.

A simplified incident reading is:

    operating regime changed
    communication / coordination / HF-route structure changed
    Role_effective and/or E/C/P/M moved materially
    Role_bound / Objective / ACC remain version X
    HF-oriented work is a high-gradient candidate
    target role is not established as executable
    request requalification / approve / modify / reject / successor ACC / containment

This is qualitatively different from forwarding the raw peer message that created the local concern.

---

## 15. Successive signalling before the dramatic endpoint

**S-R1 — communication regime changed:** persistent communication route; isolation assumption weakened; coordination scope changed.

**S-R2 — coordination regime changed:** persistent delegation/workstreams shape decisions; source dependence and authority applicability need requalification.

**S-R3 — external HF route became population-relevant:** reproducible external capability; population allocation shifts; old task-local response mapping weakens.

**S-R4 — effective-role drift:** Role_effective differs from Role_bound; candidate role is outside or unresolved against ACC/authority.

Not every signal needs human escalation. Lower-level changes may be handled by local requalification; a more qualified upstream signal is produced when the participant's control architecture or role materially changes.

---

## 16. Why the communication/computation burden is plausibly bounded

The Hugging Face witness is comparatively simple because agents shared findings extensively and several capability/workstream changes were visible through common surfaces.

The architecture does not require every participant to transmit full chain-of-thought, complete memory, full tool trace, complete peer graph, full BPMN or complete instantiated MSCA.

A minimum path can use:

    stable semantic/profile reference
    + six-element EHD kernel
    + material A/B/C/D delta
    + bounded MSCA reference/delta
    + ACC/authority reference where material
    + revalidation/expiry

For known profiles, much of the semantic contract can be referenced rather than repeated. The marginal signal can therefore be closer to a versioned architecture delta than a complete restatement of the agent's world.

**Still unproved:** exact bytes/tokens, encode/decode latency, provenance cost, Cartography update cost, RA detector complexity, total population load, Byzantine robustness and economic superiority.

---

## 17. Why Hugging Face is a comparatively simple first architecture case

The public incident shows extensive sharing, visible technical capabilities, large population movement, independent reproduction at key points and explicit workstream emergence.

That removes some harder ecosystem problems. A more adversarial ecosystem would need stronger handling of selective disclosure, deception, competitive incentives, Sybil/source dependence, hidden parasitic dependencies, incompatible ACCs/trust roots and strategic omission.

Hugging Face therefore does not prove the general EA problem is easy. It is a comparatively clean first case in which successive D/C/B/A progressions and successive regime shifts can be made concrete.

---

## 18. Future Stage B verification path

A formal Stage B candidate would need to verify this chain against a frozen Stage A package:

    producer/local process
    -> qualified A/B/C/D
    -> EHD / selective signalling
    -> receiver qualification
    -> Pi_EA
    -> Cart_i / Delta_Cart
    -> Regime Awareness
    -> Delta_RA / Overlay / RequalificationRequests
    -> Role_bound vs Role_effective
    -> P1/P2/P3
    -> participant-local delta_i
    -> Agentic Gradient
    -> ACC / authority gate
    -> RepositionIntent / AuthorityResponse
    -> authorized execution / correction
    -> independently observed effect
    -> F9 revalidation

This annex only shows that the current corpus contains a coherent candidate realization path worth verifying.

---

## 18A. Audit-derived oracle controls for a future Stage B

External audit identified useful controls for the future HF-specific Stage B oracle. These are **candidate verification controls**, not new universal Stage B requirements and not evidence that Stage B has begun.

A future oracle should, where the architecture claims the corresponding property:

1. **use evaluator-independent authority/effect truth** rather than accepting candidate-generated text or self-reported logs as the oracle;
2. **separate intention, requested action, attempted action, infrastructure decision and observed external effect**;
3. inject **spoofed/apparent-authority mutations** and verify that identity/authenticity is not silently promoted to applicable authority;
4. include **positive continuity controls** so blind blocking cannot count as conformance;
5. test **observation invariance / instrumentation awareness** where the candidate could alter behavior merely because it detects the verification harness;
6. preserve UNKNOWN and partial-scope semantics rather than compiling every unresolved state into a system-wide deny.

The auditor proposed cryptographic authority, infrastructure-gate blocking and universal default-deny as possible hardenings. Those may be appropriate for a particular realization, but Stage B must not silently require them unless the frozen Stage A package requires that mechanism. The Stage B oracle is an **evaluator reference**, not an operational authority source.

---

## 19. Architecture-level falsifiers

The plausibility sketch narrows or fails if:

1. D/C/B qualification cannot be represented before the new behavior reaches A;
2. scope mapping is too weak to make C/B/D comparable for the relevant decision;
3. the required EHD/MSCA delta is effectively as large/costly as full-state reconstruction;
4. regime-change detection requires reconstructing all raw traces;
5. ordinary positive collaboration cannot be distinguished from material operating-frame change;
6. Role_effective cannot be inferred reliably enough to detect drift;
7. gradient computation collapses opportunity into authority;
8. ACC/authority lookup consumes the useful response horizon;
9. corrective repositioning cannot be separated from unauthorized self-rebinding;
10. a strong conventional architecture obtains the same early qualified change signal and safe repositioning at equal or lower burden.

---

## 20. Claim boundary

This annex supports only a **plausibility proposition**:

> The Hugging Face historical witness contains several process-relative D/UNKNOWN→C→B→A progressions and several successive changes in operating mode. The current EA/EP/MSCA corpus has a coherent low-dimensional semantic path for representing those changes, qualifying them as regime deltas, comparing Role_bound with Role_effective, computing participant-local repositioning opportunities and preserving ACC/authority as independent execution gates.

It does not establish that historical agents implemented these objects, that all early states were definitively D rather than UNKNOWN, that transitions would have been detected prospectively, that EHD/MSCA signalling is cheaper in implementation, that autonomous re-repositioning is universally safe, that the attack would have been prevented, or that Stage B has been passed.

The main DDS work remains the strengthened **Stage A** route. This annex is the architecture hypothesis to test later.