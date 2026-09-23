# MSCA Architectural Role — Participant Role within an Objective-Bound Architecture

**Status:** canonical public working specification, v0.1, 23 September 2026.

**Architectural role:** this document defines how one participant is located functionally inside one instantiated Minimum Sufficient Control Architecture (MSCA). It defines **role**, not repositioning. Dynamic role drift, role change, migration and re-contracting are owned by [Canonical MSCA Operation & Repositioning](./04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md).

**Parent architecture:** [Minimum Sufficient Control Architecture — Canonical Architecture](./00_CANONICAL_MSCA_ARCHITECTURE.md)

**Normative-extension lineage:** [ACC Lineage, Identity & Authority Binding Profile](./01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md)

## 1. Purpose

An MSCA represents an objective-bound control architecture. It may describe a simple process or a very large, distributed and extensible architecture containing software, protocols, agents, human actors, rules, dependencies, control mechanisms, signalling, authority references and feedback loops.

The canonical MSCA kernel remains small:

~~~text
X = [ S, E, C, P, M ]
~~~

but an instantiated MSCA can be arbitrarily rich through compatible profiles and extensions.

The architectural-role question is narrower:

> **Within this MSCA and this Objective Envelope, what functional place does this participant occupy?**

That place is its **MSCA Architectural Role**.

The role is a bounded projection of an instantiated MSCA. It is not the participant's complete identity, not its complete ACC, not its epistemic position and not a global description of the ecosystem.

## 2. MSCA is objective-bound process architecture

An MSCA instance represents the minimum architecture needed to reason about control sufficiency for **one Objective Envelope** under its operating assumptions.

The represented process need not be centrally orchestrated or sequential. It may be:

- linear;
- partially ordered;
- distributed;
- event-driven;
- multi-agent;
- human-machine;
- cyclic with feedback;
- composed from nested processes;
- implemented across several organizations.

What gives the instance architectural unity is not one orchestrator. It is the fact that its represented roles, dependencies, mechanisms and means contribute to one coherent Objective Envelope and can be assessed together for control sufficiency.

A useful conceptual view is:

~~~text
Objective Envelope S
        ↓
roles / actors / resources / dependencies
        ↓
coordination C
        ↓
intervention mechanisms P
        ↓
enabling means M
        ↓
observable outputs / effects
        ↺
feedback / requalification
~~~

This is a process/control view, not a mandatory execution topology.

## 3. Objective Envelope coherence rule

An Objective Envelope may contain several objectives, including objectives that compete or require trade-offs.

Objectives belong in the **same Objective Envelope** when they are part of the same bounded process/control problem and there is a legitimate rule, owner or governance mechanism able to evaluate their joint trade-offs.

Useful indicators of one envelope include:

- the objectives concern the same operational process or mission;
- the same control decisions can materially affect more than one objective;
- the objectives share material resources, dependencies, constraints or outputs;
- improvement in one objective may legitimately worsen another within declared trade-off limits;
- one owner/governance boundary can declare hard constraints and admissible compromises among them;
- sufficiency of C/P/M can be assessed against the objectives together.

The objectives do **not** need to be perfectly aligned.

### 3.1 Example — logistics / mobility Objective Envelope

Suppose one logistics or mobility process seeks both:

- lower fuel use / lower CO2 emissions; and
- a high percentage of direct journeys / few passenger or cargo transfers.

These objectives can compete.

Additional transfers or route segmentation may increase vehicle utilization and reduce fuel/CO2 per transported unit, while lowering the percentage of direct journeys. Conversely, maximizing direct journeys may require less efficient vehicle utilization.

They can nevertheless belong to one Objective Envelope because:

- they concern the same transport process;
- the same routing/fleet decisions affect both;
- their trade-off is operationally meaningful;
- a legitimate owner can declare acceptable ranges or priorities for both.

The envelope might therefore contain a hard service floor plus a trade-off region rather than one scalar objective.

### 3.2 Example — unrelated objective

“Produce healthy food ingredients” and “reduce the percentage of transport transfers” do not belong in the same Objective Envelope merely because both occur in the same wider ecosystem.

Without a represented process dependency and legitimate common trade-off rule, they are separate control problems and therefore separate Objective Envelopes / MSCA instances.

### 3.3 Example — competing neighbouring processes

“Maximize taxi utilization” and “maximize bus utilization” may interact competitively in one mobility ecosystem but still belong to separate Objective Envelopes when they are objectives of separate operational processes with separate control logic.

Ecosystem interaction does not by itself merge Objective Envelopes.

A higher-level legitimate owner could deliberately define a broader multimodal mobility envelope that contains both, but that would be a **new explicit envelope and MSCA instance**, not an automatic consequence of coexistence.

## 4. One Architectural Role binds to one Objective Envelope

The canonical role invariant is:

> **One MSCA Architectural Role is defined relative to exactly one MSCA instance and one Objective Envelope.**

For participant i in MSCA instance X:

~~~text
Role_i^X = π_i(X | S)
~~~

where π_i is the participant-specific architectural projection.

An agent may participate in several MSCAs, but it then holds **separate role bindings**:

~~~text
Role_i^(X1 | S1)
Role_i^(X2 | S2)
...
~~~

One role object MUST NOT silently span two Objective Envelopes.

This prevents objective, authority, dependency and performance semantics from being mixed merely because one physical/software participant happens to serve several processes.

## 5. Architectural Role is a projection/subset of the instantiated MSCA

The role is a **subset/projection of the instantiated architecture**, not a subset of the abstract S/E/C/P/M schema.

An instantiated MSCA may contain many participants, roles, protocols, dependencies and control mechanisms.

The participant's role selects the part that is functionally relevant to it.

Conceptually:

~~~text
MSCA instance X
  ├─ Objective Envelope S
  ├─ actors / roles
  ├─ process relationships
  ├─ dependencies
  ├─ C coordination structures
  ├─ P interventions
  ├─ M enabling means
  ├─ compatible ACC profiles
  └─ authority / signalling / evidence references
             ↓
        projection π_i
             ↓
       Role_i^X
~~~

The role therefore answers:

- what the participant contributes;
- what it consumes;
- what it produces;
- what it depends on;
- who/what depends on it;
- which part of C it participates in;
- which P it may propose/use/execute;
- which M it uses, provides or owns;
- which Objective-Envelope conditions its work supports;
- which ACC and authority references constrain its participation.

## 6. Minimum Architectural Role representation

A role SHOULD expose or reference at least:

| Field | Meaning |
|---|---|
| **Role_ID** | Stable identifier for the architectural role definition/binding. |
| **MSCA_Instance_ID** | The MSCA instance in which the role exists. |
| **Objective_Envelope_ID / S version** | The single Objective Envelope to which this role contributes. |
| **Participant / subject reference** | Identity/reference of the actor currently occupying the role, or UNBOUND for a role template. |
| **Role purpose / contribution** | Which part of the Objective Envelope or process outcome the role contributes to. |
| **Inputs** | Information, material, commands, resources, events or commitments consumed by the role. |
| **Outputs** | Information, material, proposals, actions, resources, effects or commitments produced by the role. |
| **Upstream dependencies** | Roles/resources/conditions on which this role depends. |
| **Downstream dependencies** | Roles/processes/decisions that materially depend on this role's outputs. |
| **C projection** | Coordination reach/scope relevant to the role. |
| **P projection** | Intervention mechanisms available to, proposed by or executable through the role. |
| **M projection** | Enabling means used/provided by the role. |
| **ACC_Role_Binding** | The ACC instance/profile that defines participation/admissibility for this role, including lineage reference. |
| **Additional ACC constraints** | Other applicable ACCs that constrain the participant/interaction without defining this role, where relevant. |
| **Authority / delegation references** | Runtime mandate/grant/permit references required for role actions. |
| **Validity / activation conditions** | Preconditions, effective time, expiry, state or context under which the role is active. |
| **Capacity / burden envelope** | Material resource, latency, human/compute or operational constraints attached to the role. |
| **Evidence / provenance** | Source/version references sufficient to reconstruct why this role binding is considered current. |

This is an architectural semantic model, not a mandatory wire format.

## 7. ACC availability in MSCA versus ACC bound to a role

A crucial distinction is required.

### 7.1 MSCA-level ACC set

An MSCA instance may contain or reference **one or several compatible ACC profiles**:

~~~text
ACC_Set(X) = { ACC_1, ACC_2, ... ACC_n }
~~~

These ACCs define available or applicable contractual/participation frameworks inside the Objective Envelope.

They may correspond to different:

- organizations;
- participant classes;
- roles;
- interaction types;
- authority domains;
- signalling obligations;
- governance regimes.

An ACC in ACC_Set(X) is **not automatically the ACC of every agent in the MSCA**.

It may exist as:

- an available role contract;
- an unbound template;
- a contract for another participant class;
- a conditional profile applicable only to certain interactions.

### 7.2 Role-bound ACC

The role identifies the ACC that currently defines the participant's contractual/admissibility position **for this role**:

~~~text
ACC_Role(i,X)
~~~

This role-bound ACC references its lineage/root through the [ACC Lineage profile](./01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md).

The participant may therefore have:

- an identity independent of the MSCA;
- several ACC memberships in the wider ecosystem;
- several possible ACC profiles visible inside the MSCA;
- **one role-defining ACC binding for this Architectural Role**, plus additional overlapping ACC constraints where legitimately applicable.

This preserves the distinction:

~~~text
ACC available in MSCA
≠ ACC bound to role
≠ participant identity
≠ runtime authority
~~~

## 8. ACC does not define the whole role

The role-bound ACC determines contractual/admissibility conditions such as:

- role eligibility;
- obligations;
- prohibitions;
- autonomy bounds;
- signalling requirements;
- mutation rights;
- validity/suspension/revocation conditions.

But the Architectural Role additionally contains process/architecture information that ACC does not necessarily own:

- concrete inputs/outputs;
- upstream/downstream dependencies;
- C/P/M projection;
- process contribution;
- capacity/burden;
- runtime authority references;
- current MSCA/S version.

Therefore:

> **ACC constrains and identifies the contractual participation of the role; the MSCA Role locates the participant functionally inside the architecture.**

## 9. Role templates and occupied roles

The architecture distinguishes:

### Role template

A role may exist in an MSCA before a participant occupies it.

~~~text
RoleTemplate_X
subject = UNBOUND
ACC profile = compatible / available
~~~

### Occupied role

When participant identity, role-bound ACC and required authority references are established:

~~~text
Role_i^X
subject = participant_i
ACC_Role = bound
authority = current reference(s)
~~~

Occupying a role does not transfer ownership of S, the MSCA, the ACC lineage or another participant's role.

## 10. Role inside the ecosystem composition

A participant's role is defined in one focal MSCA, but that MSCA may itself sit inside the wider [MSCA Ecosystem Composition & Control](./03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) map.

The role therefore has two structural views:

- **inside view:** exact function, inputs/outputs, dependencies, C/P/M, ACC and authority within the focal MSCA;
- **outside view:** only those cross-MSCA dependencies from the ecosystem composition map that are materially relevant to this role or its Objective Envelope.

The role does not need to import the full ecosystem composition. It consumes the bounded dependency neighbourhood needed for its process/control responsibilities.

## 11. Role and qualified epistemic/MSCA position are different

Three objects must remain distinct.

### Epistemic Position

What the participant currently represents/knows, with A/B/C/D qualification.

### Qualified MSCA Position

How the participant qualifies the represented control architecture and its known/current capability frontier.

### Architectural Role

Where the participant functionally sits in the instantiated MSCA.

A participant can have a perfectly clear role while holding incomplete epistemic knowledge of the ecosystem.

Conversely, it can possess rich ecosystem knowledge while occupying a very narrow architectural role.

Role is therefore **structural/function assignment**, not epistemic confidence.

## 12. Worked role example — route-planning participant

Using the logistics/mobility envelope above, suppose an MSCA contains:

- S: reduce CO2/fuel burden while maintaining a declared minimum percentage of direct journeys and other hard service constraints;
- E: demand, fleet, roads, transfer infrastructure and operating conditions;
- C: fleet/operator/route coordination;
- P: route assignment, vehicle selection, transfer-point selection and bounded rescheduling;
- M: telemetry, timetable/demand data, communications, optimization tools and effect measurement.

A route-planning agent may occupy:

~~~text
Role = Route Planner
Input = demand + fleet state + service constraints
Output = proposed route/fleet plan
Contribution = jointly improve S within declared trade-off limits
C = relevant fleet/route coordination
P = proposal/replanning mechanisms
M = planning computation + qualified data feeds
ACC_Role = Planner participation profile / lineage
Authority = may propose; execution authority may remain with another role
~~~

The role does not own the whole MSCA.

It also does not own the Objective Envelope merely because its planning function optimizes against it.

## 13. Multiple roles and role granularity

One participant may perform several functions inside the **same** MSCA.

Implementations may represent them as:

- one composite role with explicitly separated subroles; or
- several role objects bound to the same participant and Objective Envelope.

The correct granularity is the smallest role decomposition needed to preserve materially different:

- inputs/outputs;
- authority;
- ACC constraints;
- dependencies;
- C/P/M responsibilities;
- validity conditions.

Role decomposition must not be used to hide shared dependencies or manufacture independent corroboration.

### 13.1 Role output into the ecosystem-awareness circuit

The Architectural Role supplies the focal structural binding used by the cycle:

- MSCA instance / Objective Envelope;
- participant identity/subject;
- role purpose;
- inputs/outputs;
- material upstream/downstream dependencies;
- relevant C/P/M projection;
- role-bound ACC;
- authority/delegation references;
- validity/capacity constraints.

These fields allow [Composition & Control](./03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) and [Regime Awareness 01C](../../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) to interpret a change relative to **what this participant actually does** rather than relative to the whole MSCA indiscriminately.

The role object remains static. Supplying it as context does not itself change the role.

## 14. What this document does not define

This document does not define:

- how a role changes;
- how a participant chooses a new role;
- how a participant moves between Objective Envelopes;
- how competing MSCAs interact;
- how one MSCA is replaced by another;
- the Regime Awareness trigger for architectural change;
- the agentic-gradient transition-selection algorithm;
- the authorization workflow for a role change;
- execution of migration/repositioning.

Those belong to [Canonical MSCA Operation & Repositioning](./04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md).

This document freezes only the static semantic object:

> **where this participant is, functionally and contractually, inside this MSCA and this Objective Envelope.**

## 15. Conformance conditions

An implementation violates this role model if it:

- binds one role object to multiple Objective Envelopes;
- treats ecosystem coexistence as proof that objectives belong in one envelope;
- merges unrelated objectives without a legitimate common trade-off rule;
- treats all ACCs visible in an MSCA as contracts of every participant;
- binds a role to an ACC without lineage/applicability qualification;
- treats ACC membership as runtime execution authority;
- defines role only by identity while omitting its process contribution/dependencies;
- lets a participant's role silently own or rewrite S;
- treats architectural role as equivalent to epistemic position;
- changes role while pretending the static role document itself defines repositioning.

## 16. Canonical thesis

MSCA represents one objective-bound control/process architecture.

Its Objective Envelope may contain several competing objectives when they belong to the same process and their trade-offs are legitimately governable.

Within that MSCA, several compatible ACC frameworks may exist.

An agent's **Architectural Role** is the bounded projection of the instantiated MSCA that identifies:

> **what the agent does, what it consumes and produces, what it depends on, what depends on it, which C/P/M capabilities are relevant, which Objective Envelope it serves, and which ACC lineage/authority conditions bind that participation.**

The role is static.

Repositioning is a separate operation defined in [Canonical MSCA Operation & Repositioning](./04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md).
