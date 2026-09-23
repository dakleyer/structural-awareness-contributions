# MSCA Ecosystem Composition & Control — Ecosystem Cartography of Objective-Bound Architectures

**Status:** canonical public working specification, v0.1, 23 September 2026.

**Architectural role:** this document defines the participant-local **Ecosystem Cartography** used to represent multiple MSCA instances together, how semantic and material relationships are maintained at different levels of resolution, and how that qualified cartography becomes structural input to Ecosystem Awareness and Regime Awareness. It does not define participant repositioning or a global ecosystem controller.

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

## 3. Ecosystem Cartography — the qualified composition object

For focal participant or focal MSCA i, define the bounded local **Ecosystem Cartography**:

~~~text
Cart_i(t) = [ A_Cart,i(t), B_Cart,i(t), C_Cart,i(t), D_Cart,i(t) ]
~~~

This deliberately uses the same qualified A/B/C/D semantic form as the rest of the architecture.

### 3.1 A_Cart — represented cartography

**A_Cart** is the cartography that is actually represented now.

It contains the currently mapped ecosystem structure, including as available:

- semantic MSCA entries / clusters;
- Objective-Envelope signatures;
- dependency edges;
- resolution level per element/relationship;
- structural/process models;
- focal MSCA and role references;
- provenance/freshness metadata needed to interpret the mapped elements.

The prior internal decomposition remains useful inside A_Cart:

~~~text
A_Cart ≈ {
  V_i   semantic representation,
  Dep_i dependency graph,
  R_i   resolution map,
  structural/process detail
}
~~~

A_Cart is therefore **the map**, not a claim that the mapped ecosystem is complete.

### 3.2 B_Cart — confidence / intensity overlay

**B_Cart** attaches confidence/intensity to the represented cartographic elements and relations.

For each mapped element or edge e:

~~~text
B_Cart,i(e,t) = qualified confidence / support for e
~~~

B_Cart may vary element by element.

A remote R0 entry represented only as a concept may often have low confidence or weak support. A close R3/R4 process element may often have higher confidence because it is directly observed and structurally detailed.

However:

> **resolution ≠ confidence**

A coarse label can be highly reliable, while a detailed model can be stale, inferred or weakly supported. B_Cart is therefore driven by evidence, provenance, freshness and compatibility as well as representation resolution.

Operationally, the represented cartography is **A_Cart with its B_Cart confidence overlay**.

### 3.3 C_Cart — cartographic expansion capability

**C_Cart** is the recognized frontier of what the participant could still add, inspect, refine or verify **with its current capabilities**.

It may include:

- known but unqueried neighbouring MSCAs;
- dependencies that could be checked;
- richer semantic/profile information that could be requested;
- available sensors, signalling routes or registries;
- analysis/computation that could refine a relationship;
- human/owner review capacity;
- effort, cost and useful-time budget available to increase resolution or confidence.

Conceptually:

~~~text
C_Cart = {
  candidate expansion/refinement targets,
  available acquisition paths,
  effort/capacity/time needed,
  expected gain in resolution/confidence
}
~~~

C_Cart is not already-established map content. It is the participant's current **capacity to enlarge or improve the cartography**.

### 3.4 D_Cart — cartographic residual

**D_Cart** is the structural residual beyond both the represented map and the recognized current-capability frontier.

It includes:

- MSCAs not represented and not currently enumerable;
- unrecognized dependencies;
- relationships whose knowability is itself uncertain;
- external structure outside current acquisition/compatibility capability;
- other ecosystem state that cannot responsibly be promoted into A_Cart or C_Cart.

D_Cart is not zero merely because the current map is detailed.

### 3.5 Compatibility alias

Earlier documents used:

~~~text
ECM_i
~~~

for the participant-local ecosystem composition map.

For compatibility with those references:

~~~text
ECM_i ≡ Cart_i
Δ_ECM,i ≡ Δ_Cart,i
~~~

in the current corpus. New reader-facing text SHOULD use **Ecosystem Cartography / Cart_i**.

Cart_i is participant-local and incomplete by design. It is not an ecosystem master model.

## 4. Semantic representation and dependency are different layers

The composition architecture separates semantic proximity from material dependency.

Semantic proximity asks how similar or related two MSCAs appear by objective, process, outputs, resources, domain or other represented meaning.

Material dependency asks whether a change in one MSCA can materially change assumptions, resources, outputs, constraints, authority, timing or control sufficiency in another.

Therefore:

> **semantic similarity ≠ dependency**

Taxi and bus MSCAs may be semantically close because both are mobility services. A food-production MSCA may be semantically distant from bus routing. Nevertheless, a food process can become materially coupled to logistics if transport disruption affects ingredient availability. Conversely, two semantically similar mobility MSCAs may have little direct dependency.

The Ecosystem Cartography keeps both dimensions explicit.

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

## 6. Variable-resolution principle

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
Dep_i[j,k] = qualified dependency from X_j to X_k
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

Cart_i may be updated from several qualified input classes. The list is extensible; no implementation is limited to these sources.

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

A participant MAY update Cart_i through any combination of:

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
current Cart_i
+ local Π_EA,i changes
+ ReceivedSignals_i
+ focal MSCA / Role state
+ qualified direct observations
+ RA requalification feedback
→ Cart_i(t+1)
~~~

The update may change the qualified cartography directly:

- **A_Cart:** represented semantic entries, dependency edges, process detail or resolution;
- **B_Cart:** confidence/intensity of one or more mapped elements/relations;
- **C_Cart:** recognized expansion/refinement capability and effort budget;
- **D_Cart:** residual/UNKNOWN boundary.

Internal V_i / Dep_i / R_i structures remain representations within A_Cart rather than independent top-level epistemic categories.

The update SHOULD preserve a bounded change-set:

~~~text
Δ_Cart,i = changed A_Cart / B_Cart / C_Cart / D_Cart state
~~~

Δ_Cart,i is **not** the Regime Awareness delta. It records a qualified change in the cartography itself and may become input to Regime Awareness.

### 10.4 Outputs from Composition & Control

Composition & Control supplies downstream:

- current Cart_i=[A_Cart,B_Cart,C_Cart,D_Cart] / version;
- bounded focal dependency neighbourhood;
- element-wise B_Cart confidence/intensity;
- C_Cart expansion/refinement opportunities and effort/capacity limits;
- Δ_Cart,i when material;
- newly unresolved/stale dependencies;
- resolution/coverage gaps;
- provenance/freshness;
- explicit D_Cart residual/UNKNOWN;
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

Ecosystem Awareness consumes the Ecosystem Cartography as bounded qualified structural context.

EA may use A_Cart mapped structure, B_Cart element-wise confidence/intensity, C_Cart expansion capability, D_Cart residual, plus the focal Objective Envelope/MSCA and participant role.

EA decides what is sufficiently represented for the current decision and where additional determination has value.

It does not convert the Ecosystem Cartography into ecosystem-wide truth.

## 14. Input to Regime Awareness

Regime Awareness evaluates change against a represented operating regime.

The qualified Ecosystem Cartography supplies part of that representation:

~~~text
Π_EA,i
+
ReceivedSignals_i
+
Cart_i=[A_Cart,B_Cart,C_Cart,D_Cart] / Δ_Cart,i
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

RA does not require the full Ecosystem Cartography. It may consume only the bounded dependency neighbourhood relevant to the declared decision/change family. Because Cart_i already uses A/B/C/D semantics, that bounded slice can enter RA without inventing a second epistemic translation layer.

Its output remains:

~~~text
Δ_RA = [A_RA, B_RA, C_RA, D_RA]
~~~

RA may additionally return a regime-qualified overlay identifying which cartographic/MSCA assumptions, elements or dependency regions require requalification. Because Cart_i uses the same A/B/C/D semantic form, the overlay can be applied element-wise: weakening B_Cart, requesting C_Cart refinement, or preserving/escalating D_Cart residual where appropriate. Composition & Control owns persistence/update of Cart_i; RA does not become the cartography repository. The participant later projects Δ_RA onto its own focal MSCA/objectives to calculate the agentic gradient.

## 15. Ecosystem composition is not global orchestration

The composition layer MUST NOT be interpreted as one global controller, one complete ecosystem graph, one global ontology, one common Objective Envelope, one universal ACC, one shared MSCA, one mandatory embedding space, one universal dependency score or proof that unrepresented MSCAs do not exist.

Different participants may maintain different Cart_i cartographies.

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
- converts a local Ecosystem Cartography into global ecosystem truth;
- claims authority over another MSCA merely because it is represented;
- forces all MSCAs into one common ACC or objective;
- uses composition to hide provenance, freshness or residual uncertainty.

## 19. Canonical thesis

An ecosystem is represented as a **bounded, multi-resolution Ecosystem Cartography of objective-bound MSCAs**.

The focal participant does not need to know the entire ecosystem equally well.

It maintains:

> **high-resolution deterministic knowledge close to its own role/process, progressively richer structural knowledge around material dependencies, and increasingly coarse semantic/vector representations as relevance decreases.**

Semantic proximity supports discovery.

Material dependency supports control relevance.

Ecosystem Awareness qualifies what can be relied on.

Regime Awareness detects qualified change over that composed representation.

The result is a scalable ecosystem-control map without requiring a global controller or complete world model.
