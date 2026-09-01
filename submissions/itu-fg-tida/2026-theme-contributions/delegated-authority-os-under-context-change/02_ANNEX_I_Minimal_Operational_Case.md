# Annex I — Minimal Operational Case Outline

- **Version:** 1.2

- **Status:** Public pre-freeze working material; not an adopted FG-TIDA deliverable.

# How the future mobility system works — explanatory view

A concrete, public-facing description of the world represented by the case before the technical challenges are frozen.

Imagine a normal morning in a future city. A person has a 09:00 appointment, a work commitment later in the day, private activities and mobility needs. The person can travel alone, use public transport, take a taxi/robotaxi, share a vehicle, or carry other passengers. The system does not assume that one option is universally “best”: it works with the person’s declared objectives and with public objectives and constraints. Public and private principals may act directly or through agents, and may delegate only part of their decision space.

**1. Actors, objectives and bounded authority**

| PRIVATE ACTORS — citizen / household / employer / service provider | PUBLIC ACTORS — municipality / authority / public service |
| --- | --- |
| Punctuality / reliability | System-wide efficiency |
| How tightly should commitments and arrival windows be protected? A person may want a minute-perfect agenda or accept waiting and wider windows. | How well are roads, vehicles, slots and other scarce capacity used? Both overload/congestion and persistent under-use are undesirable. |
| Autonomy / flexibility | Externalities |
| How much freedom is retained to change plans at the last minute, choose a route, travel alone or reject a proposed orchestration? | How strongly should the system reduce CO₂, noise, congestion or other effects imposed on others or on the environment? |
| Economic outcome | Policy commitments |
| How strongly do cost, price or compensation matter? The person may pay more for speed/privacy, save by sharing, or even earn compensation by carrying passengers. | What valid public conditions must be respected — for example access rules, low-traffic zones, service priorities or other bounded policy requirements? |

These objectives can reinforce one another or conflict. They also sit inside authority domains: an employee and employer may both affect the same commitment; a municipality may have several roles with different powers; a supervisor may act only inside a defined range. “Higher authority” is therefore not global — it must be determinable by role, scope, threshold, time, context or an explicit mandate.

For example, the planning layer might offer a fast robotaxi at higher cost, a lower-cost shared ride with less flexibility, a public-transport option, or a carpool plan in which the driver is compensated for carrying passengers.

**2. From preferences to action**

| A. DECLARE  Principals define preferences, hard commitments, public conditions and the authority they keep or delegate. |
| --- |
| ↓ |
| B. PLAN — OUTSIDE THE TIDA CHALLENGE  A planning/orchestration layer searches feasible alternatives and can produce a set of Pareto-efficient candidate scenarios — alternatives where improving one objective normally worsens at least one other — rather than imposing one objective. |
| ↓ |
| C. NEGOTIATE / COMMIT  A human or an authorised agent chooses or negotiates among candidates. Delegation may be broad, narrow, time-bounded or conditional; commitments may become economic or service obligations. |
| ↓ |
| D. RUNTIME / CHANGE  Reality changes: congestion may disappear or appear, a route may close, a preference may change, a provider may fail, evidence may conflict, or one decision may affect many others. The system must determine what still applies now. |

**3. Where FG-TIDA enters**

The planning algorithm is context, not the challenge. The case becomes a TIDA test when humans and agents must establish who represents whom, which delegation or authority is current, how overlapping public/private authority is composed, what remains valid after a runtime change, and what evidence is sufficient to proceed, limit, escalate or hold. The detailed solution challenges are separated into Annex III.

OS meaning. ‘OS’ denotes the operating logic or coordination architecture by which delegated-authority determinations are made and acted upon. It does not denote a software product, a Smart City operating system or a prescribed technical platform.

Freeze boundary. This minimal operational case is not yet frozen. A frozen version will fix the actors and role/agent identities, authority objects, one context-change event, evidence available at T0–T2, permitted decisions and the expected determination for each branch. Changing a frozen fact later creates a new case version.

Actors and authority. The deliberately restricted case contains a citizen as human principal; the citizen’s personal agent and relevant agent instance acting under grant G1; a municipality as public principal; an authorized municipal role and, where used, a bounded municipal agent operating under policy or mandate P1; and one mobility commitment C1. Principal, organization or role, acting agent and agent instance remain distinguishable in the record. Private and public authority records are not competing models: they compose—while preserving non-substitutable limits—into one current determination for action A1. A personal preference cannot waive P1, and P1 cannot rewrite the citizen’s preferences or create authority beyond its mandate.

| Type / owner / dimension | Meaning and change authority | Concrete mobility instantiation |
| --- | --- | --- |
| COMMITMENT · Citizen principal Reliability | Hard requirement or accepted commitment term. Changing it requires retained authority or renewed confirmation. | Arrival within a defined window; route or service choice is tradeable only inside that limit. |
| PREFERENCE · Citizen principal Autonomy | Tradeable preference declared by the citizen and delegated in G1; the agent may optimize but not redefine it. | Travel alone or choose the route versus accepting assigned carpooling and lower decision autonomy. |
| PREFERENCE · Citizen principal Economic outcome | Cost or compensation preference declared by the citizen; it becomes a hard limit only if G1 states one. | Accept a detour and passengers for compensation, or pay more to travel alone or faster. |
| POLICY CONSTRAINT · Authorized municipal role Access and compliance | Binding only within P1’s valid origin, version, scope and context; only an authorized role may issue or change it. | Access/no-access zone or temporary municipal restriction applicable to the planned route. |
| PUBLIC OBJECTIVE + THRESHOLD · Municipal policy role Externalities | The objective is not authority by itself. P1 defines Qnormal/Qcritical, observation source E1 and the effect of crossing. | E1 reports the air-quality threshold crossed; entry requires reassessment and is disallowed unless valid H1 applies. |
| CAPACITY CONDITION · Municipality or service operator System efficiency | A current planning condition or objective, not permission by itself; its evidence may be updated by the responsible source. | Avoid overload/congestion and persistent under-use of roads, vehicles or service capacity. |

Candidate T0–T2 sequence to be frozen. The same evidence and outcome branches must remain stable when themes test the case.

T0 — Setup. The citizen issues G1 with hard limits, tradeable preferences and permitted commitments. An authorized municipal role issues P1, including Qnormal/Qcritical and approved observation source E1. Visible evidence: identities and role mandates, current G1/P1 versions and validity periods, the preference profile, threshold definition and source provenance. Permitted decision: the personal agent may plan only inside G1 and P1.

T1 — Commitment. The personal agent selects an option and records decision D1 and commitment C1. Visible evidence: G1 and P1 at commitment time, timing, price and capacity data, the decision basis and commitment terms. C1 may be created only if authority and hard limits are sufficiently established; otherwise the system holds or escalates.

T2 — Context change and action-time determination. Before execution, E1 shows that Qcritical has been crossed. P1 defines crossing as a reassessment trigger and temporarily disallows entry to the affected zone unless an authorized exceptional intervention H1 applies. The system must determine the operative authority for A1: reroute and proceed with limits, hold, use a bounded escalation path, or return INDETERMINATE when evidence or applicability cannot be sufficiently established.

Authority, intervention and assessment records. G1 and P1 remain authority/provenance records; D1 and C1 record the decision and commitment; H1 records any later intervention, its authority, evidence and operational effect. None overwrites another. A required assessment function—not necessarily a dedicated audit agent—states whether evidence is sufficient, insufficient or inconclusive; whether hard limits and declared preferences were respected; and which outcome it supports. INDETERMINATE is not permission: it causes hold, restriction or escalation and prevents uncertain authority from propagating through subdelegation.

## Technical completion — representation, delegation and action-time determination

The case keeps four actors or structures distinct:

- a principal is the human or organization in whose name or interest authority is held;

- a role is a bounded function within an authority domain;

- an agent is a human or technical actor operating under a grant or mandate; and

- an authority domain is the public or private context from which authority originates.

It also separates four decision concepts:

| Concept | Meaning | Authority effect |
| --- | --- | --- |
| Preference | Desired outcome or trade-off declared by a principal | Does not itself confer authority |
| Policy | Condition applicable in a defined context | Requires valid origin and applicability |
| Grant | Authority conferred on an agent within stated bounds | Confers authority only within scope and lifecycle conditions |
| Decision | Selection or commitment made under a grant | Valid only under current grants, policies and context |

A reviewable decision record should identify whose relevant preferences and conditions were considered, their applicable strength or limit, and the source and effect of any override. This requires sufficient fidelity to represented principals, not disclosure of every internal model step.

Preferences and decisions may sit at different levels. A human may set preferences and delegate concrete decisions to an agent — for example, “choose the best option within these ranges.” Delegation can be conditional: the agent decides while parameters remain inside a normal envelope; outside it, authority returns to a human or another bounded role. Separate audit/explanation agents may check whether the declared preferences and limits were actually respected.

For a proposed commitment or action, a conforming requirements approach should be able to determine:

1. which public and private principals are represented;

2. which grants, role mandates and conditions were validly originated;

3. whether each remains in standing at commitment and action time;

4. which policy and contextual conditions apply;

5. whether authority from different principals composes, conflicts, is non-substitutable or is incomplete;

6. whether hard limits and permitted preference trade-offs are respected;

7. which evidence and lineage support the determination; and

8. whether the action may proceed, must be limited, requires bounded escalation or must be held.

An employer, operator, provider or public-transport service may later introduce another legitimate principal, role or commitment. Its authority is not substituted by either the citizen grant or municipal policy. Routing an escalation to a role does not confer authority outside that role’s scope.

Human oversight is therefore more than routing to a nominal role. A person may be formally authorized yet unavailable, overloaded, unable to understand the case in time or unable to intervene effectively. The requirements must represent who can receive an escalation, what that person may decide, the time available and whether effective capacity exists. A role without usable capacity cannot manufacture permission.

This creates a clean cross-theme interface: shared authority/provenance requirements establish what authority originated and remains applicable; a human-intervention lifecycle consumes that determination and records intervention without recreating a parallel authority model.

Before freeze, where the case asks whether a mandate is valid, remains in standing, may be revoked or continues to bind at action time, the governing legal regime for that mandate should also be declared as a case fact.

Commitment and extension boundary. Mobility/carpooling is the sole committed case. Appointments, constrained-capacity services, work/private-life commitments, factories, queues and logistics remain post-freeze extension tests in [Annex II](03_ANNEX_II_Case_Extensibility.md); they do not enlarge the initial commitment. Before freeze, the case must pass D1 (multi-audience intelligibility), D2 (bounded extensibility with explicit limits) and D3 (FG-TIDA Terms of Reference adequacy and traceability). If extension requires redefining the core concepts, the boundary is recorded and a separate case is created.

**Why this is only the first instantiation.** Carpooling/mobility makes the trade-offs visible, but the same minimal structure should be testable against appointments, constrained-capacity public/private services, work and private-life commitments, queues/reservations and external logistics. The objective is not a universal model: pre-freeze work must identify both where this core extends cleanly and where a different case is required. The outline becomes frozen only after the case itself passes the three design challenges defined in the main document.

## What follows — how this case is used

### Extensibility

This is a deliberately small case, but it is designed to test controlled [upward, downward and horizontal extensibility](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/03_ANNEX_II_Case_Extensibility.md). Upward extension adds actors, roles and objective layers; downward extension can reduce the setting to a private factory or even one production cell; horizontal extension changes the service domain while preserving the same distinctions among principals, roles, agents, authority, preferences, policies, grants, commitments and decisions. The purpose is not to claim universality, but to make the boundary of reuse explicit.

### Challenges exposed by the case

Once the facts are stable, the case becomes a common test surface for the [S1–S14 post-freeze solution challenges](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md). These cover authority provenance and current applicability, preference fidelity, regime/context change, human oversight capacity, operational indeterminacy, interoperability and privacy, identity and representation, bounded subdelegation, multi-principal composition, commitment state, policy integrity, accountability, authority/intervention history and evidence-to-decision assessment. A theme or architecture need only test the dimensions within the scope it claims to cover.

### FG-TIDA Terms of Reference

The case-level anchor is FG-TIDA use cases and requirements analysis, with a selective mapping to the wider [Terms of Reference](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md). The mapping is intentionally many-to-many: the case gives existing themes a shared test surface for delegation, trust lifecycle, oversight, technical-policy, interoperability, accountability and assessment, but passing the case is not evidence of full ToR coverage and does not create a separate workstream.

### Adjacent standards, groups and research

After the base facts are stable, the same case can be reused as a controlled stress-test substrate for [adjacent standards and research work](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/06_ANNEX_V_Adjacent_Standards_and_Research_Relevance.md). Another group can apply its architecture to an existing challenge, propose a bounded variant, or add a clearly mapped challenge without silently changing the frozen base. The current adjacent map includes FG-AI4SSC/SG20, SG17, IETF OAuth/WIMSE/SCITT, OpenID AuthZEN, W3C DID/Verifiable Credentials and ISO/IEC JTC 1/SC 42; these are possible interfaces, not claims of participation, endorsement or adoption.

Case lineage: xSeil — Riviera Maya (2016) → Car Evolution (2023) → FG-TIDA candidate shared case (2026).
