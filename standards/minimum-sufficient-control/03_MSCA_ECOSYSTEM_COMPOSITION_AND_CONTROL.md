# MSCA Ecosystem Composition & Control — Multi-Resolution Composition of Objective-Bound Architectures

**Status:** canonical public working specification, v0.1, 23 September 2026.

**Architectural role:** this document defines how multiple MSCA instances are represented together as an ecosystem composition, how their semantic and material relationships are maintained at different levels of resolution, and how that composition becomes structural input to Ecosystem Awareness and Regime Awareness. It does not define participant repositioning or a global ecosystem controller.

**Parent architecture:** [Minimum Sufficient Control Architecture — Canonical Architecture](./00_CANONICAL_MSCA_ARCHITECTURE.md)

**Participant role:** [MSCA Architectural Role](./02_MSCA_ARCHITECTURAL_ROLE.md)

## 1. Purpose

A single MSCA represents one objective-bound process/control architecture.

A real ecosystem normally contains many MSCAs: mobility, taxi, bus, food production, logistics, cloud/service, regulatory, institutional and other objective-bound processes.

The ecosystem problem is therefore not only whether one MSCA is sufficient. It is also:

> **Which other MSCAs exist around it, how are they semantically related, which materially affect it, how much detail is worth representing, and how does change in that composed ecosystem alter the assumptions of the focal MSCA?**

This document defines that composition layer.

## 2. Constituent MSCA versus composite MSCA

The canonical rule remains:

> **One constituent MSCA instance is bound to one Objective Envelope.**

Let:

~~~text
X_k = [S_k, E_k, C_k, P_k, M_k]
~~~

represent constituent MSCA k.

An ecosystem may contain:

~~~text
E_MSCA = { X_1, X_2, ... X_n, ... }
~~~

without assuming that n is known, finite or exhaustively enumerable.

Two forms of composition must remain distinct.

### 2.1 Ecosystem composition of peer MSCAs

Several MSCAs may coexist, interact, compete or depend on each other while retaining separate Objective Envelopes.

Example:

~~~text
X_bus   = bus-service MSCA
X_taxi  = taxi-service MSCA
X_food  = healthy-food production MSCA
~~~

They may inhabit one wider ecosystem without becoming one Objective Envelope.

### 2.2 Nested / higher-order composite MSCA

A higher-order MSCA may contain or reference constituent MSCAs only when a legitimate higher-level Objective Envelope exists.

For example, a legitimate multimodal-mobility owner could declare a higher-level envelope that explicitly trades off bus, taxi, accessibility, emissions and service-level outcomes.

Then:

~~~text
X_mobility
  ├─ X_bus
  ├─ X_taxi
  └─ other constituent MSCAs
~~~

is a valid nested composition because S_mobility supplies the higher-order objective/control boundary.

Composition alone does not create that higher-order envelope.

## 3. The ecosystem composition object

For focal participant or focal MSCA i, define a bounded local ecosystem composition map:

~~~text
ECM_i(t) = [ V_i(t), D_i(t), R_i(t), Q_i(t) ]
~~~

where:

- **V_i — semantic representation map:** what neighbouring/known MSCAs are represented as concepts, summaries or richer semantic profiles;
- **D_i — dependency map:** material relations among those MSCAs and between them and the focal MSCA;
- **R_i — resolution map:** how much structural detail is currently represented for each MSCA/relationship;
- **Q_i — qualification map:** provenance, freshness, confidence/intensity, capability frontier and residual/UNKNOWN attached to the composition.

ECM_i is participant-local and incomplete by design.

It is not an ecosystem master model.

## 4. Semantic representation and dependency are different layers

The composition architecture separates semantic proximity from material dependency.

Semantic proximity asks how similar or related two MSCAs appear by objective, process, outputs, resources, domain or other represented meaning.

Material dependency asks whether a change in one MSCA can materially change assumptions, resources, outputs, constraints, authority, timing or control sufficiency in another.

Therefore:

> **semantic similarity ≠ dependency**

Taxi and bus MSCAs may be semantically close because both are mobility services. A food-production MSCA may be semantically distant from bus routing. Nevertheless, a food process can become materially coupled to logistics if transport disruption affects ingredient availability. Conversely, two semantically similar mobility MSCAs may have little direct dependency.

The composition map keeps both dimensions explicit.

## 5. Multi-resolution semantic representation

Complete representation of the ecosystem is neither required nor generally possible.

The composition architecture therefore uses resolution proportional to materiality, proximity and decision value.

A remote MSCA may be represented only as a semantic concept. A nearby or materially coupled MSCA is represented progressively more precisely.

### Level R0 — semantic anchor

Minimum representation:

~~~text
X_j ≈ concept / label / semantic vector
~~~

Examples: taxi, food production, cloud identity, energy supply.

This level supports discovery, clustering and broad similarity without pretending to know internal structure.

The semantic anchor may be implemented through an embedding/vector, symbolic taxonomy, ontology term or another representation. No specific vector technology is canonical.

### Level R1 — Objective-Envelope semantic signature

A more relevant MSCA SHOULD expose at least a compact semantic signature:

~~~text
Σ_j = [
  objective / Objective-Envelope summary,
  process / function,
  principal outputs or effects,
  material relation to focal MSCA
]
~~~

Implementations may use richer dimensions.

This is the point at which a remote concept becomes a minimally interpretable neighbouring process.

### Level R2 — dependency-qualified MSCA summary

When interaction becomes material, represent:

- S summary / hard constraints / important trade-offs;
- relevant E assumptions;
- important inputs/outputs;
- material resources;
- upstream/downstream dependencies;
- relevant C/P/M capabilities;
- ACC/authority/signalling references where material;
- freshness/provenance;
- known UNKNOWN/residual.

At this level the participant can reason about how change in X_j may propagate into X_i.

### Level R3 — structural/process model

For a close, strongly coupled MSCA, represent explicit process topology:

- roles;
- inputs/outputs;
- dependencies;
- control points;
- buffers;
- thresholds/triggers;
- resource/capacity states;
- intervention pathways;
- feedback loops;
- role/ACC bindings;
- versioned process stages.

The implementation may use BPMN, Lean/value-stream structures, state machines, process graphs or another deterministic/semi-deterministic model.

The canonical requirement is the semantics, not the notation.

### Level R4 — deterministic local operational model

Inside the participant's own process/role boundary, the model may become operationally deterministic to the extent the implementation supports it:

- exact workflow;
- executable protocol;
- machine state;
- queue/buffer;
- trigger;
- timing;
- control logic;
- authorization check;
- measurable output/effect.

This is where high-level semantic composition meets concrete operations.

## 6. Resolution-gradient principle

Resolution is intentionally non-uniform.

For focal MSCA i:

~~~text
resolution(X_j relative to X_i)
↑
as material dependency / decision relevance / interaction intensity ↑
~~~

and may decrease when a relationship becomes immaterial, stale or too costly to maintain.

This is not a geometric-distance rule.

“Near” means decision-relevant / materially coupled, not physically close.

The composition system therefore behaves like a semantic map with variable zoom:

~~~text
remote ecosystem
= sparse semantic anchors

nearby cluster
= richer Objective-Envelope signatures

material dependency neighbourhood
= explicit dependency-qualified MSCA summaries

own process / controlled sub-process
= detailed deterministic process/control representation
~~~

## 7. Semantic composition matrix

For a bounded represented set of MSCAs, the participant may maintain a semantic matrix:

~~~text
V_i =
rows: represented MSCAs
columns: semantic dimensions/features
~~~

The matrix can be dense, sparse, symbolic or vector-embedded.

A minimal row may contain only a concept.

A richer row may contain:

~~~text
[
  S_summary,
  process_class,
  output/effect_class,
  domain,
  resources,
  ACC/governance class,
  relevant capabilities,
  other qualified descriptors
]
~~~

The exact feature space is implementation-specific.

The architecture requires only that richer resolution can be added without changing the identity of the represented MSCA or fabricating missing semantics.

## 8. Dependency matrix / graph

Material dependency is represented separately:

~~~text
D_i[j,k] = qualified dependency from X_j to X_k
~~~

A dependency may concern:

- input/output;
- resource/capacity;
- shared infrastructure;
- constraint/regulation;
- information/evidence;
- authority/governance;
- signalling;
- timing;
- market/competitive pressure;
- safety/externality;
- other domain-specific coupling.

A dependency record SHOULD preserve source MSCA, receiving MSCA, direction, type, materiality, sign where meaningful, freshness, provenance, confidence/intensity, validity conditions, known capability frontier and residual/UNKNOWN.

A missing edge means not represented / not established, not proof that no dependency exists.

## 9. The dependency channel

The principal bridge from ecosystem composition into a focal MSCA is its dependency channel.

For focal X_i:

~~~text
D_i* = {
  dependencies that can materially alter
  S_i, E_i, C_i, P_i or M_i
}
~~~

The participant does not need a complete model of every external MSCA.

It needs enough representation to determine:

1. which external process may matter;
2. through which dependency;
3. which part of X_i may be affected;
4. what is known about the external change;
5. what remains unresolved.

This is the structural surface on which Ecosystem Awareness and Regime Awareness can operate.

## 10. Composition control

“Control” in this document does not mean centralized command over all MSCAs.

It means maintaining the participant's bounded composition representation so that material relationships remain sufficiently qualified.

Composition control includes:

- discovering/referencing an MSCA;
- assigning/updating semantic representation;
- clustering/de-clustering;
- increasing/decreasing resolution;
- creating/updating dependency links;
- preserving provenance/freshness;
- expiring stale relations;
- marking UNKNOWN/residual;
- requesting richer representation where decision value justifies it;
- maintaining consistency between high-level semantic summaries and detailed local models.

Composition control does not grant authority over another MSCA.

### 10.1 Composition update input contract

ECM_i may be updated from several qualified input classes. The list is extensible; no implementation is limited to these sources.

Core inputs include:

- **local epistemic movement:** a material change in the participant's [qualified epistemic position](../../research/ecosystem-awareness/baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md), including action/effect observations;
- **qualified external signalling:** ReceivedSignals_i from [Ecosystem Signalling 01J](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md);
- **focal MSCA/role state:** changes in Objective Envelope, Architectural Role, C/P/M capability, ACC binding, authority or local dependency state;
- **direct observations / telemetry / owner updates:** qualified observations not necessarily originating from another agent;
- **freshness/expiry:** a previously represented dependency, signal, authority or semantic summary becoming stale or expired;
- **Regime Awareness feedback:** a qualified regime overlay, invalidation or targeted requalification request returned by RA.

Each input retains source, scope, freshness, confidence/intensity, compatibility residual and other material qualifiers.

### 10.2 Update triggers

The map is not required to run on a fixed millisecond cadence.

A participant MAY update ECM_i through any combination of:

- **event trigger** — a material local event, action/effect, authority or dependency change;
- **signal trigger** — one qualified signal or a composed set of signals crosses a declared materiality/confidence threshold;
- **insufficiency trigger** — current evidence becomes stale, contradictory, too weak or insufficient for a represented dependency;
- **epistemic-position trigger** — Π_EA,i changes materially in A/B/C/D;
- **regime-feedback trigger** — RA identifies a dependency/context region requiring requalification or increased resolution;
- **periodic trigger** — scheduled refresh appropriate to the participant's domain;
- **owner/policy trigger** — explicit revalidation requested by a legitimate owner or control policy.

Implementations SHOULD define hysteresis, debounce, evidence-change or equivalent anti-churn rules where repeated small signals could otherwise cause oscillatory map updates.

A signal may therefore matter in two opposite ways:

- enough qualified evidence arrives to justify adding/refining a relation; or
- the evidence supporting an existing relation becomes insufficient, requiring downgrade, UNKNOWN, expiry or wider observation.

### 10.3 Composition update operation

A triggered composition update may:

~~~text
current ECM_i
+ local Π_EA,i changes
+ ReceivedSignals_i
+ focal MSCA / Role state
+ qualified direct observations
+ RA requalification feedback
→ ECM_i(t+1)
~~~

The update may change:

- semantic entries V_i;
- dependency edges D_i;
- representation resolution R_i;
- qualification/provenance state Q_i.

The update SHOULD preserve a bounded change-set:

~~~text
Δ_ECM,i = changed semantic/dependency/resolution/qualification state
~~~

Δ_ECM,i is **not** the Regime Awareness delta. It is a structural map change-set that may become input to Regime Awareness.

### 10.4 Outputs from Composition & Control

Composition & Control supplies downstream:

- current ECM_i/version;
- bounded focal dependency neighbourhood;
- Δ_ECM,i when material;
- newly unresolved/stale dependencies;
- resolution/coverage gaps;
- provenance/freshness;
- explicit residual/UNKNOWN;
- requested richer observations where appropriate.

These outputs feed Ecosystem Awareness qualification and the [Regime Awareness interface 01C](../../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md).

## 11. Focal MSCA and participant interest surface

The participant normally reasons from:

1. its focal MSCA — the process in whose Objective Envelope its current Architectural Role exists;
2. its Architectural Role — the specific sub-process/function it occupies;
3. its dependency neighbourhood — external MSCAs and relations that may materially affect the focal MSCA or role;
4. progressively coarser semantic representations beyond that neighbourhood.

Thus the participant's strongest representational resolution is normally:

~~~text
own role
> own MSCA
> material dependency cluster
> related ecosystem clusters
> distant semantic concepts
~~~

This ordering denotes expected representational resolution, not epistemic certainty.

## 12. Worked composition examples

### 12.1 Logistics / mobility MSCA

The logistics/mobility MSCA may contain an Objective Envelope balancing lower fuel/CO2 burden, a high percentage of direct journeys/fewer transfers, and other hard service constraints.

Inside that MSCA, route planning may be represented at R3/R4 because the participant operates there directly.

### 12.2 Taxi MSCA

A taxi-service MSCA may have a separate Objective Envelope such as utilization, service availability, revenue/cost or other legitimate taxi-process objectives.

To the logistics/bus participant, taxi may initially be represented only as:

~~~text
R0: taxi
~~~

If competition for passenger demand becomes material, the representation may expand to objective summary, service/output class, demand relationship, resource/market dependency and freshness/confidence.

If detailed multimodal coordination becomes operationally necessary, the representation may move toward R3.

This does not merge the taxi and bus Objective Envelopes.

### 12.3 Healthy-food / nutrient MSCA

A food-production MSCA may be semantically remote from a mobility MSCA.

At first it may remain only a semantic concept:

~~~text
R0: healthy-food / nutrient production
~~~

If a logistics dependency emerges — for example transport availability becomes material to ingredient supply — the food MSCA may enter the focal dependency neighbourhood.

Only the dependency-relevant portion needs richer representation.

The architecture therefore expands knowledge along material dependency, not by attempting to model the whole world uniformly.

## 13. Input to Ecosystem Awareness

Ecosystem Awareness consumes the composition map as bounded structural context.

EA may use the focal Objective Envelope/MSCA, participant role, semantic neighbours, dependency edges, source/freshness state, resolution level, known capability frontier and residual/UNKNOWN.

EA decides what is sufficiently represented for the current decision and where additional determination has value.

It does not convert the composition map into ecosystem-wide truth.

## 14. Input to Regime Awareness

Regime Awareness evaluates change against a represented operating regime.

The ecosystem composition map supplies part of that representation:

~~~text
Π_EA,i
+
ReceivedSignals_i
+
ECM_i / Δ_ECM,i
+
focal MSCA + Architectural Role
+
EA-qualified window/context
+
other qualified observations
→ Regime Awareness
→ Δ_RA + regime-qualified overlay / requalification requests
~~~

RA may observe:

- changed semantic cluster structure;
- new/disappearing dependencies;
- changed strength/direction of dependencies;
- changes inside a materially represented neighbouring MSCA;
- degradation of freshness/coverage;
- movement of a dependency from represented/current into capability frontier or residual;
- divergence among related MSCAs.

RA does not require the full ecosystem map. It may consume only the bounded dependency neighbourhood relevant to the declared decision/change family.

Its output remains:

~~~text
Δ_RA = [A_RA, B_RA, C_RA, D_RA]
~~~

RA may additionally return a regime-qualified overlay identifying which ECM/MSCA assumptions or dependency regions require requalification. Composition & Control owns persistence/update of ECM_i; RA does not become the map repository. The participant later projects Δ_RA onto its own focal MSCA/objectives to calculate the agentic gradient.

## 15. Ecosystem composition is not global orchestration

The composition layer MUST NOT be interpreted as one global controller, one complete ecosystem graph, one global ontology, one common Objective Envelope, one universal ACC, one shared MSCA, one mandatory embedding space, one universal dependency score or proof that unrepresented MSCAs do not exist.

Different participants may maintain different ECM_i maps.

Their maps may overlap, disagree or have different resolution.

That is expected.

## 16. Composite MSCA and competing ecosystems

Several MSCAs can compete for users, resources, authority, infrastructure, time, information, market share, environmental budget or other scarce capacity.

Competition does not invalidate MSCA.

It is represented through cross-MSCA dependency/coupling relations.

Only when a legitimate higher-order owner explicitly defines a common Objective Envelope should those processes become constituents of a higher-order composite MSCA.

Otherwise they remain peer MSCAs in the ecosystem composition.

## 17. What this document does not define

This document does not define how a participant changes Architectural Role, how an MSCA changes its Objective Envelope, how the agent chooses a new MSCA, the full repositioning lifecycle, global convergence, a universal semantic-embedding algorithm, a universal clustering algorithm, a global dependency-discovery service, a mandatory BPMN/Lean notation or central control over peer MSCAs.

Those belong to future operation/repositioning or implementation-specific profiles.

## 18. Conformance / falsification conditions

The composition model fails its architectural purpose if an implementation:

- merges several Objective Envelopes merely because their MSCAs are semantically similar;
- treats semantic similarity as proof of dependency;
- treats absence of a dependency edge as proof of no dependency;
- requires full-detail representation of every known MSCA;
- prevents resolution from increasing around newly material dependencies;
- flattens an R3/R4 deterministic process back into an ambiguous semantic label at the point of control;
- converts a local composition map into global ecosystem truth;
- claims authority over another MSCA merely because it is represented;
- forces all MSCAs into one common ACC or objective;
- uses composition to hide provenance, freshness or residual uncertainty.

## 19. Canonical thesis

An ecosystem is represented as a **bounded, multi-resolution composition of objective-bound MSCAs**.

The focal participant does not need to know the entire ecosystem equally well.

It maintains:

> **high-resolution deterministic knowledge close to its own role/process, progressively richer structural knowledge around material dependencies, and increasingly coarse semantic/vector representations as relevance decreases.**

Semantic proximity supports discovery.

Material dependency supports control relevance.

Ecosystem Awareness qualifies what can be relied on.

Regime Awareness detects qualified change over that composed representation.

The result is a scalable ecosystem-control map without requiring a global controller or complete world model.
