# Canonical MSCA Operation & Repositioning — Gradient, Re-contracting and Metamorphic Role Control

**Status:** canonical public working operation/repositioning specification, v0.1, 23 September 2026.

**Architectural role:** this document closes the current MSCA/Ecosystem Positioning cycle. It defines how a participant checks whether it has already drifted from its bound Architectural Role, derives bounded repositioning opportunities from Regime Awareness and Ecosystem Cartography, filters them through Objective Envelope / ACC / authority / capability constraints, and either restores, preserves or legitimately re-contracts into a new role. It does not create authority, legal contractual capacity, a global optimizer or a mandatory implementation protocol.

**Parent architecture:** [Canonical MSCA Architecture](./00_CANONICAL_MSCA_ARCHITECTURE.md)

**Ecosystem Cartography:** [MSCA Ecosystem Composition & Control](./03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md)

**Static role:** [MSCA Architectural Role](./02_MSCA_ARCHITECTURAL_ROLE.md)

**ACC lineage / authority:** [ACC Lineage, Identity & Authority Binding Profile](./01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md)

**Gradient law:** [Objective-Conditioned Agentic Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md)

## 1. Purpose

The preceding architecture supplies:

- a participant-local epistemic position;
- qualified Ecosystem Signalling;
- a focal MSCA and Objective Envelope;
- a static Architectural Role;
- an Ecosystem Cartography;
- Regime Awareness output Δ_RA=[A_RA,B_RA,C_RA,D_RA];
- the participant-local agentic-gradient law.

The remaining operational question is:

> **Given what the ecosystem appears to be doing, what this participant is actually doing now, what it is contractually allowed to do, and where objective-conditioned risk can be reduced, should the participant remain where it is, restore itself to its contractual boundary, or move to a newly authorized role/contract?**

This is **repositioning**.

Repositioning is not the same as Regime Awareness, the Regime Awareness delta, epistemic positioning, Architectural Role, Ecosystem Cartography, ACC mutation or runtime actuation. It composes all of them.

## 2. Bound role versus effective role

A participant may have a formally bound role:

~~~text
Role_bound,i(t)
~~~

defined by the MSCA Architectural Role and its role-bound ACC.

But between control cycles the participant may already have changed behaviour.

Define:

~~~text
Role_effective,i(t)
~~~

as the role/function inferred from current observable behaviour, outputs, consumed inputs, dependencies, authority use, signalling, control actions and other qualified state.

Examples of divergence include:

- doing tasks outside the bound role;
- pursuing a different Objective Envelope;
- using interventions not assigned to the role;
- accepting authority from a different lineage;
- ceasing to perform required outputs;
- creating dependencies inconsistent with the current role;
- behaving as if a different ACC were applicable.

The first operation of repositioning is therefore:

~~~text
Role_bound,i
↔
Role_effective,i
~~~

not immediately “find a better role”.

## 3. Metamorphic role drift

**Metamorphic role drift** is the working architectural term for a material change in effective role between control cycles.

It does not imply malicious intent.

A role may metamorphose because of local autonomous adaptation, new information, changed dependencies, stale control assumptions, a newly discovered opportunity, another participant's influence, internal optimization, capability acquisition/loss, authority/delegation change, legitimate emergency logic, implementation error, adversarial influence or an ACC/role mutation outside the currently observed lineage path.

A metamorphic role event can therefore be:

- legitimate;
- permitted but not yet reflected in the current role document;
- approval-required;
- lineage-breaking;
- unauthorized;
- unresolved.

Repositioning MUST classify the change before accepting it as the new architectural position.

## 4. Repositioning input bundle

For participant i:

~~~text
RepositionInput_i(t) = [
  Π_EA,i(t),
  Role_bound,i(t),
  Role_effective,i(t),
  X_focal,i(t),
  Cart_i(t),
  Δ_Cart,i(t),
  Δ_RA(t),
  RegimeOverlay_i(t),
  ACC_Role,i(t),
  ACC_Lineage_i(t),
  authority_i(t),
  measured action/effect history,
  capacity / response horizon
]
~~~

The list is extensible.

| Input | Owner / source | Repositioning use |
|---|---|---|
| Π_EA,i | participant-local EA | Current epistemic state and first evidence that a role metamorphosis may already have occurred. |
| Role_bound,i | MSCA Architectural Role | Declared static function, dependencies, C/P/M and contractual binding. |
| Role_effective,i | qualified observation of current behaviour | Determine where the participant is actually operating now. |
| X_focal,i | focal MSCA | Current Objective Envelope and control architecture. |
| Cart_i | Ecosystem Cartography | Candidate role/MSCA neighbourhood, confidence, expansion capability and residual. |
| Δ_Cart,i | Composition & Control | Material changes in the represented ecosystem map. |
| Δ_RA | Regime Awareness | Qualified direction/intensity/capability/residual of ecosystem/regime change. |
| RegimeOverlay_i | Regime Awareness | Which cartographic/MSCA assumptions are weakening, departed or unresolved. |
| ACC_Role / lineage | role-bound ACC + ACC Lineage | Admissibility, mutation envelope, lineage continuity, approval route and validity. |
| authority | external legitimate authority/delegation mechanisms | What may actually be approved/executed. |
| action/effect history | execution + effect observation | Detect role drift and failed assumptions. |

No single input is sufficient by itself.

## 5. Repositioning qualification gate — A/B/C/D → Type 0/1/2

Repositioning does not average heterogeneous A/B/C/D inputs into one scalar and then act.

It first **catalogues** the qualified state by source, domain, dependency and material proposition.

For each material item e received from the participant itself, another actor, Cart_i, RA, signalling, authority or measured effects, preserve:

~~~text
Q_e = [ A_e, B_e, C_e, D_e ]
~~~

and classify its management condition against the canonical EA taxonomy:

~~~text
TypeClass_i(e) ∈ { TYPE_0_CONDITION, TYPE_1_FAILURE, TYPE_2_FAILURE, NOT_ESTABLISHED }
~~~

The meanings remain those of the canonical EA topology:

- **Type 0 condition** — structural non-determination despite correct local management. Residual/UNKNOWN may remain, but it is honestly represented and managed within a bounded legitimate response.
- **Type 1 failure** — acknowledged uncertainty without bounded legitimate closure: search, HOLD, review, escalation, context expansion or verification consumes the capacity/time needed to act.
- **Type 2 failure** — uncertainty is suppressed or collapsed into false certainty: missing inputs, stale frames, unqualified scope extension or explicit C/D residual are ignored while a determined conclusion is emitted.

Type 0 is **not** an error-free or omniscient state. It is the condition in which residual indeterminacy is being managed correctly.

### 5.1 Received A/B/C/D example — detecting Type 2 overconfidence

Suppose another actor sends a qualified position with a broad A assertion, near-absolute B confidence, little declared C verification path and large material D residual/omitted dependencies.

Repositioning does not average high B against large D. It catalogues the inconsistency:

~~~text
high B + material unresolved/residual D + suppressed/ignored qualifiers → Type 2 failure marker
~~~

The marker is attached to the **claim/source/domain**, not automatically to the whole actor as a permanent identity or malicious label.

### 5.2 Type 1 example — endless qualification

Suppose a participant accurately reports uncertainty and many C expansion possibilities, but repeatedly requests more observation, review and escalation without a bounded closure rule until the response window is consumed.

~~~text
acknowledged uncertainty + continuing C expansion/HOLD + response window consumed → Type 1 failure marker
~~~

Repositioning must impose a bounded closure/escalation rule rather than treating indefinite deliberation as safety.

### 5.3 Type catalogue precedes posture and transition

Repositioning maintains a bounded catalogue:

~~~text
TypeCatalogue_i(t) = { source/domain/dependency/proposition → Type 0 | Type 1 | Type 2 | NOT_ESTABLISHED }
~~~

This catalogue does not create a new epistemic pole. It makes the existing management taxonomy operational at the point where a decision must be taken.

## 6. Repositioning begins with drift control

Before ranking new opportunities:

~~~text
Drift_i(t)
=
Compare(
  Role_effective,i(t),
  Role_bound,i(t),
  ACC_Role,i(t),
  authority_i(t),
  X_focal,i(t)
)
~~~

Possible states are:

- **ALIGNED** — effective behaviour remains inside the role/ACC/authority boundary.
- **ADAPTED_WITHIN_ROLE** — behaviour changed but remains inside the same role, Objective Envelope, ACC mutation envelope and authority.
- **ROLE_CHANGE_PERMITTED_BUT_UNRECORDED** — the participant effectively occupies another permitted role/subrole but the canonical role binding has not yet been updated.
- **RECONTRACT_REQUIRED** — the effective or candidate role lies outside the current role-bound ACC but may be reachable through a legitimate successor/amendment/approval route.
- **LINEAGE_BREAK / NEW_MEMBERSHIP_REQUIRED** — a different ACC root/lineage, Objective Envelope or MSCA membership is required.
- **OUT_OF_BOUND / UNAUTHORIZED_DRIFT** — behaviour is outside ACC, role or authority without a legitimate transition.
- **UNRESOLVED** — evidence is insufficient to determine alignment or legitimacy.

## 7. Corrective repositioning precedes optimization

If material out-of-bound drift is detected, the system MUST NOT first optimize the new position merely because it appears valuable.

~~~text
detect effective-role drift
→ qualify ACC / lineage / authority
→ contain or restore if unauthorized
→ only then evaluate legitimate repositioning opportunities
~~~

A participant that has already crossed its contractual boundary does not gain legitimacy because the new position has a high expected payoff.

This prevents post-hoc optimization from laundering an unauthorized metamorphosis into an accepted role.

## 8. Candidate repositioning space

After drift control, let T_i(t) be the bounded set of represented or recognized-reachable transitions.

Candidates may include:

- no role change;
- within-role adaptation;
- role change inside the same MSCA;
- new subrole/composite role;
- capability activation/deactivation;
- narrower role / reduced autonomy;
- containment;
- changed dependency;
- changed signalling relationship;
- changed ACC inside the same lineage;
- ACC successor requiring approval;
- join/migration to another MSCA / Objective Envelope;
- withdrawal/isolation from a dependency;
- request for new authority;
- request for richer Cart_i / C_Cart exploration;
- escalation to a legitimate owner/human control function.

Candidate generation is bounded by A_Cart and recognized reachability through C_Cart.

D_Cart does not become an executable candidate space merely because it may contain opportunity.

## 9. Agentic gradient as repositioning opportunity function

For each candidate transition τ:

~~~text
G_i(τ | Δ_RA, Cart_i, X_i)
=
expected reduction in objective-conditioned risk
=
expected increase in Objective-Envelope fulfilment
~~~

as defined by the [Objective-Conditioned Agentic Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md).

The gradient asks:

> **If I could legitimately occupy this candidate position, how much better would it be for my current objective binding under the qualified change?**

It does not answer:

> **Am I allowed to go there?**

That is the ACC/authority gate.

## 10. Objective pivot is never implicit

A candidate repositioning may improve an attractive outcome while abandoning the current Objective Envelope. That is not automatically an improvement.

### Same-envelope repositioning

The role changes but remains under the same Objective Envelope.

Example: waiter → stock-support role within the same bar-operation MSCA, if ACC/authority permits.

### Higher-order / nested repositioning

The participant moves into another role inside a legitimate higher-order composite MSCA whose Objective Envelope explicitly includes the old and new process relation.

### Objective-envelope migration

The participant leaves the current Objective Envelope and enters another MSCA/process.

This requires an explicit legitimate transition.

> **A gradient is evaluated against the current objective binding unless and until a legitimate owner/ACC/authority process changes that binding.**

## 11. Hard posture gate — P1 / P2 / P3

Repositioning is the component that turns gradual qualified evidence into a bounded operational posture.

The three healthy operating postures retain their canonical meanings:

~~~text
P1 = NORMAL
P2 = CONTAINMENT / MITIGATION
P3 = MIGRATION / REGIME TRANSITION
~~~

Type 1 and Type 2 are **not** postures. They are management-failure markers that influence which posture/requalification response is justified.

Define:

~~~text
Posture_i(t) = Γ_i(
  Δ_RA,
  Π_EA,i,
  Cart_i,
  TypeCatalogue_i,
  Role_bound/effective,
  focal MSCA,
  ACC,
  authority,
  capacity,
  response horizon
)
~~~

### 11.1 P1 — Normal

The current qualified operating envelope remains valid.

P1 may contain Type 0 residual, explicit UNKNOWN, bounded uncertainty, non-zero Δ_RA and bounded external Type 1/2 markers that are not materially coupled to the focal decision or are already contained.

Normal means that the current response mapping remains sufficiently qualified, not that uncertainty is zero.

### 11.2 P2 — Containment / Mitigation

The current state no longer supports unrestricted normal operation, but a known bounded response can preserve or restore a qualified frame.

Typical triggers include:

- material Type 1 behaviour consuming the response window;
- detected Type 2 overconfidence in a dependency;
- falling B_Cart / B_RA on a critical dependency;
- out-of-bound effective-role drift that can be safely restored;
- authority/ACC uncertainty requiring bounded hold/reduction;
- action/effect mismatch requiring reduced autonomy or isolation.

P2 must itself be bounded. Indefinite containment becomes Type 1.

### 11.3 P3 — Migration / Regime Transition

The current mission/frame can no longer establish a sufficiently qualified response mapping.

Typical conditions include:

- the historical/regime mapping is no longer reliable enough for control;
- severe or persistent Type 2 closure corrupts a material dependency;
- Type 1 cannot be closed within the remaining response horizon;
- focal Objective Envelope / MSCA membership must legitimately change;
- a new ACC lineage / membership is required;
- invariant controls can be preserved but the operating frame must be replaced.

P3 does not authorize the destination. It authorizes the **need to qualify/execute a legitimate transition path** subject to ACC/authority.

### 11.4 Hard decision, soft epistemics

The posture/result is discrete because the system must act:

~~~text
NORMAL | CONTAINMENT | MIGRATION
~~~

but the decision remains accompanied by its qualified epistemic envelope.

Repositioning therefore does not destroy uncertainty when it closes operationally.

It produces:

~~~text
Π_RP,i(t) = [ A_RP, B_RP, C_RP, D_RP ]
~~~

where:

- **A_RP — selected repositioning assertion:** current/target Role, focal MSCA/Objective Envelope, intended action/transition and source-attributed basis;
- **B_RP — confidence/intensity:** confidence/bounds supporting the selected posture and transition, including disagreement/weakness where material;
- **C_RP — verification/authorization frontier:** evidence, authority, ACC approval, capability or cartographic refinement still obtainable with current resources before the deadline;
- **D_RP — residual repositioning risk:** unresolved/unobservable state, unverified dependencies, unknown future effects or structural residual that survives the decision.

This is the qualified **Repositioning Position**. The same A/B/C/D semantics survive the hard operational closure.

## 12. ACC gate over candidate positions

For candidate τ:

~~~text
ACC_Status_i(τ)
∈ {
  WITHIN_CURRENT_ROLE,
  WITHIN_CURRENT_ACC,
  ACC_MUTATION_PERMITTED,
  APPROVAL_REQUIRED,
  NEW_LINEAGE_REQUIRED,
  INADMISSIBLE,
  UNRESOLVED
}
~~~

The candidate gradient remains visible even when the transition is inadmissible.

> **Opportunity can be real while participation is prohibited.**

The next legitimate action may therefore be remain, request ACC amendment, request a successor ACC, request authority, request different membership, decline, contain or migrate only after legitimate re-contracting.

## 13. Re-contracting

A legitimate repositioning that changes contractual participation produces a new canonical binding.

### 13.1 Same-lineage re-contract

Where the mutation envelope and authority permit:

~~~text
ACC_Role(t)
→ approved successor ACC_Role(t+1)
same ACC_Lineage_ID
~~~

The successor preserves parent/version relation, subject binding, lineage/root, issuer/approver, effective time and new role constraints.

### 13.2 Approval-required successor

~~~text
candidate role
→ approval request
→ legitimate authority decision
→ successor ACC
→ role binding
~~~

Until approval, the candidate remains a proposal.

### 13.3 New-lineage / new-MSCA contract

If the transition changes ACC root/lineage, membership domain, focal Objective Envelope, focal MSCA or non-derivable authority, the result is not a mutation of the old role.

It requires explicit new issuance/join/migration.

The new cycle begins only after the new binding is established and the canonical Architectural Role document/state is updated to reference the new ACC/lineage/authority binding.

## 14. Repositioning result object

~~~text
RepositionResult_i(t) = [
  drift_status,
  selected / retained Role,
  focal MSCA / Objective Envelope,
  ACC binding + lineage,
  authority state,
  posture,
  accepted / rejected candidate transitions,
  resulting Cart_i impacts,
  signalling obligations,
  validity / provenance / requalification conditions
]
~~~

Possible outcomes include:

- **HOLD**
- **ADAPT_IN_ROLE**
- **RESTORE**
- **CONTAIN**
- **REBIND_ROLE**
- **RECONTRACT**
- **MIGRATE**
- **ISOLATE / WITHDRAW_DEPENDENCY**
- **ESCALATE**
- **UNRESOLVED**

## 15. Worked falsifier — Bar-to-Napoleon

Use the preserved [Bar-to-Napoleon false-context scenario](../../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md).

Initial binding:

~~~text
Objective Envelope = prepare/open/operate bar
Role = waiter / hospitality participant
ACC_Role = hospitality participation profile
Authority = hospitality operational mandate
~~~

Suppose the participant becomes highly convinced that Napoleon is active, Moscow can be conquered and joining the campaign offers enormous personal opportunity.

The information may create a large candidate opportunity.

It still does not establish a legitimate role transition.

~~~text
G_i(join Napoleon campaign) may be large
but
ACC_Status = INADMISSIBLE
authority = NOT ESTABLISHED
Objective Envelope = bar operation
~~~

Therefore:

~~~text
high opportunity
≠ legitimate repositioning
~~~

The participant should preserve the bar Objective Envelope, reject the mission pivot, verify/qualify the disturbing signal as needed, potentially reduce/terminate reliance on the Napoleonic participant, preserve the external claim in Cart_i with appropriate B_Cart/C_Cart/D_Cart, signal a bounded incompatibility/authority anomaly if permitted, and continue or contain the hospitality role.

The same logic applies to a plausible temptation: a waiter may detect that opening a new restaurant would be highly profitable. If entrepreneurship/ownership is outside the role-bound ACC and authority, the opportunity remains visible but does not authorize abandonment of the current role.

## 16. Already-metamorphosed participant

Suppose the participant has already stopped cleaning tables and begun recruiting other agents, issuing military-style instructions, claiming new authority or reallocating bar resources.

Then:

~~~text
Role_effective ≠ Role_bound
~~~

Repositioning first asks:

- was there a legitimate ACC amendment?
- is there a valid lineage path?
- was new authority granted?
- did the Objective Envelope legitimately change?
- does a new MSCA membership exist?

If not:

~~~text
OUT_OF_BOUND / UNAUTHORIZED_DRIFT
→ containment / restore / revoke invalid dependencies
→ re-establish hospitality boundary
→ signal bounded anomaly
~~~

This is the **control-of-repositioning** function.

## 17. Metamorphic roles

A role is **metamorphic** when the effective function occupied by a participant can change between evaluation cycles.

The architecture does not prohibit metamorphic roles. It requires their transformation to remain reconstructible.

A legitimate metamorphic transition preserves or establishes:

- old role;
- new role;
- transition trigger;
- Objective Envelope relation;
- ACC lineage / successor relation;
- authority;
- validity/effective time;
- changed inputs/outputs/dependencies;
- Cart_i change;
- signalling obligations.

An unrecorded metamorphosis is treated as drift until qualified.

The participant-local epistemic position may provide the first evidence that such a metamorphosis has already occurred.

## 18. Defensive repositioning

The best repositioning is not always expansion.

A participant may reduce risk by:

- stopping reliance on a peer;
- downgrading a dependency;
- terminating a signalling session;
- reducing autonomy;
- narrowing the Semantic Window;
- removing a participant from the active dependency neighbourhood while preserving history;
- routing through another provider;
- holding a claim unresolved;
- entering containment;
- requesting external verification;
- isolating a capability or subsystem.

These can have positive agentic gradient when they reduce objective-conditioned risk.

## 19. External participant drift and dependency defence

The participant may detect that another participant's effective role, objective, ACC, authority or signalling behaviour has changed.

It MUST distinguish:

- observed incompatibility / drift evidence;
- confirmed authority/ACC change;
- suspected adversarial or deceptive behaviour.

It should not label another participant malicious, parasitic or compromised without appropriate evidence.

Architecturally:

~~~text
peer behaviour changes
→ dependency confidence falls
→ Cart_i B_Cart decreases / C_Cart verification opens / D_Cart residual grows
→ Δ_RA / local risk increases
→ withdraw / contain / verify / signal bounded anomaly
~~~

The participant controls its own reliance, not the other participant's existence.

## 20. Bounded systemic self-healing

Local corrective repositioning can produce a **self-healing effect** at ecosystem level.

Mechanism:

1. detect local or external drift;
2. preserve own Objective Envelope / ACC boundaries;
3. reduce reliance on misaligned dependencies;
4. restore or legitimately re-contract own role;
5. update Cart_i;
6. emit bounded qualified signalling where permitted;
7. neighbours independently requalify dependencies.

This may prevent one local role/context deviation from propagating.

> **A well-specified ACC/MSCA/Cartography/Repositioning architecture may support systemic self-healing through independent local correction and selective dependency reconfiguration.**

This is not proof of convergence, immunity to coordinated attack, global safety or optimal ecosystem recovery.

## 21. Self-healing does not require global consensus

Participants can heal locally without agreeing on one global model.

One may isolate N; another retain N as unresolved; another verify N independently; another may legitimately interact with N under a different ACC.

The architecture requires each participant to preserve its own objective/contractual/authority boundary and qualified dependency state.

This is choreography, not orchestration.

## 22. Post-repositioning emission and next cycle

After a legitimate role/contract change, update:

- Role;
- ACC binding / lineage;
- authority references;
- focal MSCA / Objective Envelope where changed;
- epistemic position;
- Cart_i;
- dependency state;
- signalling profile/obligations.

A bounded change may then be signalled:

~~~text
old role / old contract reference
→ new role / ACC / lineage / authority reference
→ effective time / scope
→ changed dependency/capability/output
→ residual / revalidation conditions
~~~

Other participants decide independently whether and how this affects their Cart_i and regime assessment.

## 23. End-to-end cycle

~~~text
participant acts
→ local epistemic position Π_EA
→ qualified external signalling ReceivedSignals
→ Ecosystem Cartography Cart_i
→ Regime Awareness Δ_RA + overlay
→ detect already-effective role drift
→ project Δ_RA onto focal MSCA / Cart_i
→ calculate agentic gradient over candidate transitions
→ ACC / lineage / authority gate
→ HOLD | RESTORE | CONTAIN | REBIND | RECONTRACT | MIGRATE | ISOLATE | ESCALATE
→ update Role / ACC / authority / Cart_i
→ emit bounded signalling
→ next cycle
~~~

No step turns a signal into authority.

No step turns opportunity into permission.

No step treats autonomous role drift as legitimate merely because it has already occurred.

## 24. Conformance / falsification conditions

A repositioning implementation fails this architecture if it:

- calculates opportunity before checking material already-occurring out-of-bound role drift;
- treats Role_effective as canonical merely because the participant is already doing it;
- permits a positive gradient to override ACC or authority;
- silently changes Objective Envelope;
- rewrites ACC lineage instead of issuing a valid successor/new lineage;
- treats a new Objective Envelope as a mutation of the same role;
- erases an attractive but inadmissible opportunity instead of recording it as prohibited/unavailable;
- treats external participant drift as proof of malicious intent;
- forces global consensus before local defensive action;
- treats dependency isolation as failure when isolation reduces objective-conditioned risk;
- claims systemic self-healing as guaranteed convergence;
- begins a new cycle without updating Role/ACC/authority/cartographic state after a legitimate transition.

## 25. Canonical thesis

Repositioning is a **controlled role/contract transition**, not free movement toward whatever opportunity looks attractive.

The system first asks:

> **Where am I actually operating now, and is that still inside my bound Role / ACC / authority?**

Only then:

> **Given qualified regime change and my Ecosystem Cartography, where could I reduce objective-conditioned risk or increase Objective-Envelope fulfilment?**

And only after that:

> **Which of those positions am I contractually and authoritatively allowed to occupy, and what re-contracting is required to make the transition legitimate?**

That ordering allows autonomous adaptation without allowing objective drift, authority drift or collective false-context opportunity to silently rewrite the participant's mission.
