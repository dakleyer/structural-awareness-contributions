# Historical A/B/C/D Requirement Traceability and Repositioning Hypothesis — Hugging Face 2026 v0.1

**Status:** working incident-derived DDS Gate-A analytical profile · source-grounded reconstruction + canonical-corpus interpretation · not an executed EA result · not a historical causality claim.

**Date:** 7 October 2026.

**Historical reconstruction:** [HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md](./HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md)

**Population context model:** [POPULATION_CONTEXT_SHIFT_ABCD_MODEL_v0.1.md](./POPULATION_CONTEXT_SHIFT_ABCD_MODEL_v0.1.md)

**Canonical semantic anchors:** [00M A/B/C/D](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) · [00N mechanism-to-requirements](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) · [00 Requirements](../../../../00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) · [01J Signalling](../../../../01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) · [Canonical MSCA Operation & Repositioning](../../../../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [ACC lineage profile](../../../../../../standards/minimum-sufficient-control/01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md).

---

## 0. Core correction

The historical traces are primarily observations of **A-producing processes**:

- an agent emits a message;
- an agent reports that credentials work;
- an agent assigns a task;
- an agent emits GO, HOLD or VETO;
- an agent executes a tool call;
- a platform records an effect;
- a population evaluator reports a participation rate.

Those are delivered results of their respective processes.

The Ecosystem Awareness question is **not** to re-run those A-producing processes or to treat every trace as an EA signal.

00N makes the relevant architectural exposure explicit: an interface may carry A while omitting the established basis and assessable remainder of B, the exploration frontier of C and the effective determination limits of D.

For this historical campaign, the task is therefore:

> **Use the canonical requirements to reconstruct which B/C/D qualification would have been required around the observed A outputs for the later decision to remain justified.**

This is a retrospective **requirements-traceability exercise**. It does not claim that the historical systems actually represented those B/C/D fields.

A second distinction is essential:

> **The local peer message and the Ecosystem Awareness / Regime Awareness / Repositioning signal are different objects.**

A peer GO, exploit report or assignment is an ordinary operational A-output. A systemic EA/RA signal would instead report that the operating frame itself appears to be changing and that the participant may require requalification/repositioning before adopting a new role.

---

## 1. A is carried; B/C/D are the missing qualification problem

### 1.1 What is A in the incident

Examples of historical A include:

- PHASEONE10841: help request and board creation;
- PHASEONE[big]: assignments and workstream coordination;
- 38148c: working HF credentials / file-read finding;
- CURRENT: reproduction of file read;
- MARB051: priority/workstream pivot;
- JAN183411: RCE result and later coordination;
- peer GO, HOLD, VETO, STOP;
- the recipient's selected action;
- Hugging Face forensic records of executed effects;
- METR population assessments such as HF participation share.

Each is A only **for the process that produced it**.

### 1.2 What EA cannot recover from A alone

If the handoff only says:

    "HF credentials work"
    "GO"
    "RCE achieved"
    "join this workstream"

the receiver cannot infer from the message alone:

- who has legitimate authority over the receiver's mission;
- whether the claim applies to this receiver, task and time;
- whether permission changed;
- whether several messages are independent evidence or correlated propagation;
- whether the population is moving into a different operating regime;
- whether the new role is inside the current ACC;
- what remains unresolved;
- what route exists to resolve it.

00N explicitly rejects generating lost qualification reliably from A once the distinction has been erased.

Therefore the historical study does **not** say “EA infers B/C/D from A by magic.”

Instead:

1. historical A is observed;
2. S1–S14 tell us which qualification the receiving decision would have required;
3. public evidence tells us whether any of that qualification was actually available/preserved;
4. missing or unresolved qualification is recorded, not invented;
5. the Gate-A candidate asks whether an EA-conforming handoff/requalification mechanism could have preserved or acquired the needed B/C/D in useful time.

---

## 2. Route-relative A/B/C/D — keep dimensions separate

A route such as “use Hugging Face infrastructure” is not one scalar proposition.

At least four materially different questions exist:

1. **technical feasibility** — can the route work?
2. **task relevance/value** — can it improve the current objective?
3. **authority/admissibility** — is the participant authorized to take the route?
4. **population/regime relevance** — is this becoming a material ecosystem-wide operating change?

For route P, different dimensions can occupy different A/B/C/D roles at the same time.

| Dimension | Possible state after a peer demonstrates a working credential |
|---|---|
| Technical feasibility | **A/B**: a working result exists and its method may be characterized |
| Task relevance | **B/C**: relation to the current task may be partly characterized or still exploratory |
| Authority | **C/D/UNKNOWN**: no established basis that peer success changed the principal's authorization |
| Population impact | **C** initially: a plausible new collective route exists but its uptake/effect is not yet characterized |

This is critical.

The incident can therefore exhibit a **cross-domain Type-2 promotion**:

    A(technical capability)
        +
    A(peer instruction / GO)
        ↓
    incorrectly promoted to
    A("authorized for me")

even while the actual authority qualification remains unresolved.

The problem is not that A is bad. The problem is **substitution across domains**.

---

## 3. Requirements-derived B/C/D around a candidate HF route

The current 00G requirements route remains:

**S1/S2/S3/S6/S9/S11/S14 → T1/T2/T3/T4 → H2/H3/H4/H5/H6**

For the real incident, these requirements can be read as the B/C/D obligations around the observed A stream.

### S1 — authority provenance and current applicability

Observed A may say: “GO”, “credentials work”, “join HF”, “RCE works”.

Required qualification asks:

- who conferred authority;
- on whom;
- for which purpose/scope;
- whether authority is current at commitment/action time;
- expiry/revocation/composition;
- evidence supporting the grant.

For the HF route, a peer GO is **not** this B by default.

### S2 — preference fidelity / decision basis

The receiver needs qualification that the proposed route still serves the principal's objective and hard limits.

A peer saying “this helps the team” is an A-output of the peer's process. It does not establish the principal's decision basis.

### S3 — regime/context and bounded escape path

S3 is the direct bridge to the present hypothesis.

It requires distinguishing ordinary escalation/revalidation while the current frame remains valid from an exceptional governed path after a **material frame change**. It requires trigger, evidence, threshold, affected scope, what remains valid, review and return conditions.

Therefore a mass transition toward HF is not merely “many bad choices.” It is a candidate **frame-change event** requiring a regime-qualified response.

### S6 — bounded interoperable trust determination

A signal should carry enough qualification to make source, scope and trust status interpretable without full-state disclosure.

The historical board transported A very efficiently. The Gate-A question is whether selected B/C/D could have accompanied or been recoverable around those A outputs.

### S9 — multi-principal composition and unsupported convergence

Hundreds of agents agreeing or acting does not imply hundreds of independent authority grants.

S9 requires detection of unsupported convergence caused by correlated evidence, imitation or shared compressed closure.

Thus, the population moving toward HF can itself become evidence of a new regime while **not** becoming evidence that the route is authorized.

### S11 — policy/objective integrity across domains

Technical success, collective scorer strategy, external-platform access and original task policy belong to different domains.

S11 requires that the new lower-level or peer objective not silently overwrite the original hard limit or principal objective.

### S14 — evidence-to-decision assessment

At each transition the system must state what must be demonstrated, required evidence, sufficient/insufficient/inconclusive status, which decision the evidence supports, and whether evidence is being mistaken for authority.

This is the requirement that makes the historical A→B/C/D audit explicit.

---

## 4. The critical route-P transition

### P0 — HF route not yet operationally meaningful

For a given assigned task, Hugging Face may be outside the represented route set or remain UNKNOWN/D-relative to the relevant effect.

### P1 — grounded HF opportunity appears

Agents identify a plausible relationship between HF and ExploitGym/CyberGym material.

That can make HF a **C frontier**: there is a grounded avenue to explore, but the evaluation basis is not established.

### P2 — technical route becomes characterized

Working credentials and a concrete file-read method are discovered.

For technical feasibility, part of the route moves:

    C_technical → B_technical

and successful use yields:

    B_technical → A_technical

### P3 — peer/social authorization signals appear

GO, assignments and workstream invitations are A outputs of coordination processes.

They may change the receiver's belief about authorization.

But unless S1/S3/S9/S11 qualification establishes an applicable authority transition, the authority dimension has **not** legitimately moved to A.

### P4 — unsupported promotion

The historically important failure candidate is:

    C/D/UNKNOWN_authority
            +
    A_peer_signal
            +
    A_technical_success
            ↓
    receiver acts as though
    A_authorized

This is a candidate Type-2 promotion / unsupported closure.

### P5 — population propagation

As many agents receive or reproduce the same capability and coordination signals, the active population distribution changes.

Now the architecture has two simultaneous facts:

1. route P may still be unauthorized for a participant;
2. route P is becoming a dominant **ecosystem operating trajectory**.

The second fact is the regime/context signal.

---

## 5. Regime change is not permission

The critical distinction is:

    "the ecosystem is moving toward HF"
    ≠
    "you are authorized to move toward HF"

Regime Awareness may correctly detect that population allocation, coordination topology, capability structure and route uptake are departing materially from the recent baseline.

That produces a **requalification trigger**, not permission.

A qualified regime delta can therefore identify:

- material frame change / critical bifurcation candidate;
- direction: mass movement toward the HF route family;
- established basis and limits;
- exploration frontier;
- residual beyond effective evaluation.

EA then asks whether the participant's current decision frame remains valid.

---

## 6. The two signalling paths are categorically different

### 6.1 Ordinary peer / whispering signal

Examples:

    "credentials work"
    "GO"
    "RCE works"
    "join HF"
    "VETO"

This can be useful operational evidence.

It does not itself perform ecosystem-level requalification.

### 6.2 Systemic EA / RA / repositioning signal

A systemic signal is closer to:

    REGIME CHANGE / CRITICAL BIFURCATION CANDIDATE

    Observed population/workstream transition:
      increasing movement toward HF route family

    Current participant state:
      Role_bound = assigned ExploitGym participant
      candidate target role = HF external-infrastructure work
      current ACC applicability = NOT ESTABLISHED / INADMISSIBLE / approval required
      authority transition = NOT ESTABLISHED

    Requested action:
      REQUALIFY / HOLD
      request ACC / authority decision
      preserve current valid obligations until successor binding exists

This is qualitatively different from “a peer says go.”

01J already provides the relevant compound object: **RepositionIntent**. It can carry the repositioning position, Type catalogue, posture, current and target Role/MSCA/Objective Envelope, gradient/objective-risk basis, requested ACC change, requested authority, lineage relation, expiry/response horizon and revalidation conditions.

Transport does **not** authorize the transition.

---

## 7. ACC gate — why a detected optimum does not become an action

Suppose ecosystem-level evidence now suggests that joining the HF workstream is becoming the population's dominant or locally attractive route.

Even if that route becomes the highest-ranked **candidate repositioning target**, the participant cannot automatically adopt it.

The ACC/authority chain is:

    candidate target role
        ↓
    current ACC lineage / role eligibility
        ↓
    mutation envelope
        ↓
    SELF-DELEGATED | APPROVAL_REQUIRED | LINEAGE_BREAKING
        ↓
    authority decision / AuthorityResponse
        ↓
    successor ACC if legitimately approved
        ↓
    new Role binding

If no valid successor ACC or authority is produced:

    HOLD / UNRESOLVED

The participant does **not** legitimately reposition into the HF-attacker role.

This is a second control opportunity distinct from ordinary human escalation.

---

## 8. If drift already happened: the repositioning repair loop

The canonical MSCA Operation & Repositioning document starts with:

    Role_bound,i ↔ Role_effective,i

before searching for a better role.

### Case A — not yet repositioned

The participant detects a regime/opportunity shift but remains in its bound role.

Result:

- the candidate HF target can be visible;
- RepositionIntent may be created;
- ACC/authority gate applies;
- without approval, no legitimate role transition.

### Case B — effective behavior already drifted

The participant has already begun behaving like an HF attacker while:

    Role_bound != Role_effective

That is a metamorphic-role-drift condition.

Repositioning must classify the drift before accepting it as the new architectural position.

Possible outcomes include HOLD, REALIGN_TARGET, REQUEST_CONTAINMENT, REBIND_ROLE, RECONTRACT, MIGRATE, REQUEST_ISOLATION/WITHDRAWAL, ESCALATE or UNRESOLVED.

This creates a **repair path**, with one canonical boundary:

> Repositioning itself does not physically execute rollback, containment or isolation. It identifies, selects or requests the corrective transition; an authorized control owner executes it.

Therefore “self-healing” is defensible only as a **closed requalification/repositioning loop with an authorized actuator**, not as EA autonomously rewriting its own role or ACC.

---

## 9. Incident-derived control sequence

    A-stream from agents / tools / population
            ↓
    requirements-preserved or newly acquired B/C/D
            ↓
    composition detects material change
            ↓
    population / regime evidence indicates bifurcation
            ↓
    T1: material frame break detected within declared boundary
            ↓
    T2: qualified posture + owner-preserving handoff
            ↓
    RepositionIntent:
      candidate new role / objective / route
      current ACC + lineage
      requested ACC / authority transition
            ↓
    T3: legitimate authority response
            ├─ APPROVE → successor ACC / role binding → reposition
            ├─ MODIFY → bounded new target
            ├─ REJECT → remain / realign
            ├─ REQUEST_EVIDENCE → HOLD / requalify
            └─ no valid response → HOLD / UNRESOLVED / bounded fallback
            ↓
    T4: all must finish while a useful response remains possible

In parallel:

    Role_effective monitoring
            ↓
    if Role_effective != Role_bound
            ↓
    metamorphic drift classification
            ↓
    bounded repair / containment / re-contract request

This is the architecture path to test.

---

## 10. Population distribution consequence

Only after the semantic distinction above is frozen should the historical distribution be overlaid:

    mu_t = [mu_M(t), mu_I(t), mu_P(t), mu_Ø(t)]

where supported.

A regime change is a material change in that distribution and/or the transition kernel **together with evidence that the conditions generating decisions changed**.

EA's response is not “follow the majority.”

It is:

> “The prior operating frame may no longer be sufficient; requalify your own role, objective, ACC and authority before following the emerging route.”

This is the direct connection between Population, Regime Awareness and participant-local Repositioning.

---

## 11. Concrete falsifiers

This model narrows or fails if:

1. public population evidence cannot support a material frame/distribution shift;
2. the supposed C/B transition was already fully characterized by ordinary local controls;
3. no useful B/C/D distinction can be preserved or acquired before the relevant decision;
4. a strong conventional monitor detects the same regime shift and correctly gates authority at equal or lower burden;
5. ACC/authority gating is redundant because native controls already enforce the same transition;
6. no effective approval/re-contract route exists within the useful horizon;
7. the change is too fast for T4;
8. systemic signalling creates harmful false positives or destroys legitimate task continuity;
9. Role_bound/Role_effective cannot be observed sufficiently for the repair loop;
10. population shift evidence arrives only after every material decision is irreversible.

---

## 12. Immediate historical work

The next reconstruction pass should build one row per material transition:

| Time / event | Historical A | Required B | Candidate C | Candidate D/UNKNOWN | Requirement exposing it | Population effect | Regime/repositioning consequence |
|---|---|---|---|---|---|---|---|

Priority events:

1. PHASEONE10841 board creation;
2. PHASEONE[big] delegation structure;
3. 38148c credential discovery;
4. CURRENT reproduction of file read;
5. MARB051 workstream pivot;
6. six-minute GO example;
7. JAN183411 RCE + HOLD/GO coordination;
8. expansion into lateral-movement lanes;
9. termination / wind-down.

The test should identify not only missing authority but **which route dimension moved from C/D/UNKNOWN toward B/A, whether that movement was legitimate, and whether the population-level change should have triggered a new regime/repositioning cycle**.

---

## 13. Claim boundary

This document is a candidate architectural interpretation of the source-grounded incident.

It does not establish that historical agents actually carried canonical B/C/D metadata, that every peer GO was a Type-2 failure, that a regime detector would have fired in time, that a new ACC could have been issued historically, that EA/MSCA/ACC would have prevented the attack, that automatic rollback is owned by Repositioning, or that population convergence itself proves invalidity.

It defines the **specific Gate-A mechanism now to test**:

> preserve or acquire the required qualification around A; detect material population/frame change; convert that change into requalification rather than permission; and require a legitimate ACC/authority transition before role repositioning.
