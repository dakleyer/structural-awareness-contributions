# Objective-Conditioned Agentic Gradient Law

**Status:** canonical working law for Ecosystem Positioning, v0.1, 23 September 2026.

**Architectural role:** this document defines the general participant-local gradient used to translate a qualified ecosystem/regime change into an agent-specific repositioning pressure over its current MSCA, under ACC, authority, capacity and time constraints. It is a generalized finite-difference/order law and does **not** require a differentiable state space.

**Parent:** [Ecosystem Positioning — Agentic Architecture](./README.md)

## 1. Core intuition

A participant does not need to minimize uncertainty about the whole world.

It needs to minimize **uncertainty that is material to the achievement of its declared Objective Envelope**.

For participant i, uncertainty is therefore operationally relevant only to the extent that it changes the probability, expected shortfall, robust margin or other declared measure of remaining inside S_i.

In a normalized binary reading:

~~~text
Objective fulfilment + Objective-conditioned risk = 1
~~~

so maximizing expected objective fulfilment and minimizing objective-conditioned risk are dual views of the same quantity.

For multi-objective or non-binary envelopes, use any declared monotone risk/shortfall functional that preserves hard constraints and owner-defined trade-off rules. No universal scalar utility is imposed by this law.

## 2. State used by the law

The participant holds a current MSCA:

~~~text
X_i(t) = [ S_i, E_i, C_i, P_i, M_i ]
~~~

and a qualified MSCA position:

~~~text
Π_X,i(t) = [ A_X, B_X, C_X, D_X ]
~~~

where:

- **A_X** — situated represented control scope: the S/E/C/P/M frame the participant is actually using;
- **B_X** — directional support/confidence for that position;
- **C_X** — recognized control/capability state that could still be established or activated with current capabilities;
- **D_X** — residual control-relevant state outside that represented/currently obtainable boundary.

A Regime Awareness source may emit the qualified delta:

~~~text
Δ_RA(t) = [ A_RA, B_RA, C_RA, D_RA ]
~~~

where **A_RA is direction**, **B_RA is confidence/intensity attached to that direction**, C_RA is the current-capability frontier and D_RA is residual. Scope, Ψ/context/baseline, provenance, freshness and sign semantics qualify the delta but are not substitutes for its direction.

ACC, identity/delegation, signalling and authority remain separate objects that constrain which transitions may be pursued.

## 3. Objective-conditioned uncertainty

Let u be a material uncertainty or unresolved condition and let S_i be the participant's declared Objective Envelope.

Define its objective materiality:

~~~text
μ_i(u | S_i) ≥ 0
~~~

where μ_i = 0 means the uncertainty is not material to the participant's current objective/decision under the declared dependency model.

Let:

~~~text
q_i(u,t) ∈ [0,1]
~~~

represent the current uncertainty/exposure associated with u under the participant's qualified position.

A local objective-conditioned risk contribution is then:

~~~text
r_i(u,t) = μ_i(u | S_i) · q_i(u,t)
~~~

This is the basic law of relevance:

> **Uncertainty matters to the participant only through its material effect on the Objective Envelope.**

An uncertainty that is large but immaterial to S_i contributes no direct repositioning pressure. An uncertainty in another participant's objective matters only when a represented dependency connects that objective/state to S_i.

## 4. Four non-fungible risk regions

The same objective-conditioned risk principle is evaluated separately over the four qualified-position components.

Conceptually:

~~~text
R_i(t) = Φ_S(
  R_A,i(t),
  R_B,i(t),
  R_C,i(t),
  R_D,i(t)
)
~~~

where Φ_S is an **owner/objective-conditioned non-fungible composition operator**.

The four terms are not interchangeable buckets.

### A — represented/current region

R_A concerns uncertainty or potential shortfall inside the MSCA scope currently represented in A_X.

A material RA delta falling inside A_X changes the support of assumptions/configurations already in use.

Typical consequence:

~~~text
reassess current MSCA support
~~~

### B — confidence / intensity region

B does not represent a separate world domain. It qualifies how strongly a direction/position is supported.

For normalized confidence b in [0,1], a simple uncertainty complement may be written:

~~~text
q_B = 1 - b
~~~

but a profile may instead use intervals, likelihood bounds, robust confidence sets or another declared uncertainty representation.

B therefore scales the strength of a candidate change pressure; it does not erase C or D.

### C — recognized current-capability frontier

R_C concerns material state outside the currently established A_X that the participant **could still determine, test, acquire or activate with its present capability**.

A large qualified opportunity in C_X is therefore a genuine repositioning opportunity:

~~~text
current position
→ acquire / expand / activate within existing capability
→ new qualified position
~~~

C cannot be averaged into A as if the state were already known. Moving into C consumes time, capacity and often authority.

### D — structural / capability residual

R_D concerns material uncertainty beyond the currently represented and recognized-obtainable capability boundary.

A delta into D_X does not create an executable direct transition.

It creates pressure for residual-preserving responses such as:

- containment;
- capability discovery;
- signalling/querying another participant;
- acquiring a new tool/profile/extension;
- requesting human/owner intervention;
- seeking authority or ACC mutation;
- migration;
- preserving UNKNOWN.

D cannot be compensated away by strong performance in A unless the Objective Envelope explicitly establishes a legitimate dependency/compensation rule.

## 5. Non-fungibility law

The architecture therefore imposes:

> **Objective-conditioned risks may be compounded, but material uncertainty from one qualified region/domain cannot be cancelled by unrelated certainty or performance in another.**

In particular:

- high confidence B does not eliminate D;
- high output inside A does not imply C has been explored;
- a promising C does not become current A without acquisition/requalification;
- unrelated objective success cannot compensate a hard constraint or material unresolved dependency.

Mathematically, Φ_S MUST be monotone in material risk and MUST preserve owner-declared hard/non-compensable constraints.

It MAY be:

- lexicographic;
- threshold-constrained;
- vector-valued / Pareto;
- robust worst-case;
- expected-shortfall based;
- domain-specific.

The law does not require a universal weighted sum.

## 6. Ecosystem delta from Regime Awareness

Regime Awareness supplies a qualified ecosystem/regime delta:

~~~text
Δ_RA(t)
~~~

together with A_RA/B_RA/C_RA/D_RA.

This is an **ecosystem delta**, not a gradient: it describes where the represented operating regime appears to be moving and how strongly that direction is supported.

The gradient exists only after the receiving participant projects this delta through its own objectives, dependencies and MSCA.

The participant first projects that delta through its represented dependencies:

~~~text
δ_i(t) = P_i( Δ_RA(t) | X_i(t), dependencies_i )
~~~

where P_i is a bounded participant-local projection/mapping onto the parts of S/E/C/P/M that are materially coupled to the incoming change.

If no material dependency exists:

~~~text
δ_i = 0
~~~

for the current objective/decision, even if the ecosystem change is large elsewhere.

## 7. General Agentic Gradient Law

Let τ be a candidate repositioning transition available to participant i.

Examples include:

- re-observe/requalify;
- change a dependency;
- activate an existing capability;
- expand C into A;
- modify control configuration;
- request an ACC change;
- request new authority;
- contain;
- migrate;
- cooperate;
- decline action.

Define the participant's objective-conditioned risk functional:

~~~text
R_i( Π_X,i ; S_i )
~~~

After projecting the regime delta δ_i, the generalized gradient of candidate transition τ is:

~~~text
G_i(τ,t | Δ_RA)
=
R_i(current | δ_i)
-
E[ R_i(after τ | δ_i) ]
~~~

Equivalently, for normalized objective fulfilment V_i = 1 - R_i:

~~~text
G_i(τ,t | Δ_RA)
=
E[ V_i(after τ | δ_i) ]
-
V_i(current | δ_i)
~~~

Therefore:

> **Positive gradient means the transition is expected to reduce objective-conditioned uncertainty/risk and equivalently increase expected Objective-Envelope fulfilment.**

> **Negative gradient means the transition increases objective-conditioned risk or decreases expected fulfilment.**

> **Zero gradient means no material improvement under the current qualified model.**

This is the core law.

It is valid for discrete transitions through finite differences and for continuous state spaces through an ordinary differential gradient when such a representation is justified.

## 8. Nonlinear posture operator

The agentic gradient and the three operating postures are related but not identical.

A participant-local posture is produced by a nonlinear operator:

~~~text
Posture_i
=
Γ_i(
  Δ_RA,
  R_i,
  Π_X,i,
  ACC_i,
  authority_i,
  capacity_i,
  response_horizon_i
)
~~~

with:

~~~text
NORMAL
CONTAINMENT
MIGRATION / REGIME_TRANSITION
~~~

**NORMAL is compatible with continuous change.** The regime delta may have a clear A_RA direction and high B_RA confidence while the participant continues to operate because its historical/current response mapping remains sufficiently qualified.

**CONTAINMENT** occurs when confidence in the current regime mapping or the objective-conditioned risk crosses a local threshold, while a known bounded fallback/containment mapping remains qualified.

**MIGRATION / REGIME TRANSITION** occurs when the current regime/history no longer supplies a sufficiently qualified mapping for the mission. At that point extrapolation/forecasting from the old regime is not a justified control basis; invariant safety controls may remain usable while the new frame is qualified.

Because Γ_i contains thresholds, hard constraints and possibly hysteresis, the compound response is deliberately non-linear:

~~~text
small change in B_RA
+ threshold crossing
→ discrete posture change
~~~

The thresholds belong to the participant's legitimate configuration — potentially ACC, control policy or mission owner — not to Regime Awareness universally.

A sufficiently severe loss of regime qualification may place the participant in the existing **potential critical bifurcation** condition: the old mapping is invalid or insufficiently qualified while several successor paths remain plausible.

## 9. Admissible versus executable gradient

The raw gradient does not create authority.

Define the set of candidate transitions that are currently structurally reachable:

~~~text
T_reachable,i
~~~

and the subset admissible under ACC:

~~~text
T_ACC,i ⊆ T_reachable,i
~~~

and the subset currently authorized/executable:

~~~text
T_exec,i ⊆ T_ACC,i
~~~

The participant's **admissible opportunity gradient** is evaluated over T_ACC,i.

The participant's **executable gradient** is evaluated over T_exec,i.

Thus:

~~~text
τ*_candidate = argmax over T_ACC,i of G_i(τ)
~~~

but:

~~~text
τ*_execute = argmax over T_exec,i of G_i(τ)
~~~

A high-gradient transition outside current authority may instead create another high-value transition:

~~~text
request authority
request ACC mutation
request capability
seek another participant
migrate
~~~

This preserves:

~~~text
opportunity ≠ admissibility ≠ authority ≠ execution
~~~

## 10. Burden and time

Observation, signalling, verification, compute, human review, switching and intervention consume resources.

The cleanest rule is to include those costs in S_i or in the objective-conditioned risk/shortfall functional when they materially affect the Objective Envelope.

Where an implementation prefers an explicit efficiency term, it may use:

~~~text
G_eff,i(τ)
=
G_i(τ)
-
λ_i · Burden_i(τ)
~~~

or a ratio such as:

~~~text
G_i(τ) / Burden_i(τ)
~~~

only if that form is consistent with the owner-declared Objective Envelope.

No universal burden scalar is imposed.

Hard limits such as deadline, privacy, safety or authority remain constraints rather than quantities that can always be bought off with benefit elsewhere.

## 11. Mechanical RA → MSCA → agentic gradient mapping

The full sequence is:

~~~text
Regime Awareness
Δ_RA = [A_RA,B_RA,C_RA,D_RA]
        ↓
participant-local dependency projection
δ_i = P_i(Δ_RA)
        ↓
MSCA qualified position
Π_X = [A_X,B_X,C_X,D_X]
        ↓
bucket-preserving objective-risk update
R_A, R_B, R_C, R_D
        ↓
candidate transitions τ
        ↓
G_i(τ) = risk reduction = objective-value increase
        ↓
ACC admissibility
        ↓
authority / delegation
        ↓
executable repositioning
~~~

The architecture therefore does not calculate a second unrelated gradient after Regime Awareness.

It **translates the ecosystem delta into an agentic gradient by objective-conditioned projection over the participant's MSCA position**.

## 12. Positioning consequences by region

### Δ aligns with A_X

The current represented control frame is directly affected.

Primary operation:

~~~text
reassess / reinforce / reduce / reconfigure current support
~~~

### Δ aligns with C_X

The change points toward a recognized opportunity or risk that current capability can explore or activate.

Primary operation:

~~~text
expand / acquire / test / activate
~~~

A sufficiently positive G may justify repositioning from current A toward C, subject to ACC, authority and burden.

### Δ aligns with D_X

The change points beyond current represented capability.

Primary operation:

~~~text
preserve residual
+ contain / discover / signal / seek capability / migrate
~~~

Direct exploitation of D as if it were known violates the law.

### Δ has no material coupling

No repositioning pressure follows for the current objective.

The signal may still be retained for other decisions or future dependency changes.

## 13. Multi-agent dependence

Participant i may depend on objectives or control states owned by participant j.

Then uncertainty in j matters to i only through a represented material dependency:

~~~text
S_i ← dependency ← state/objective_j
~~~

The dependency transfers **risk relevance**, not objective ownership.

Participant i may therefore include j-related uncertainty in R_i while still having no authority over S_j, ACC_j or actions of j.

This is how independent local gradients can generate choreography without a central optimizer.

## 14. Choreography law

When each participant repeatedly:

1. receives/observes qualified change;
2. projects it onto its own MSCA/objectives;
3. computes its local agentic gradient;
4. filters candidate transitions through ACC/authority;
5. repositions locally;
6. optionally signals its new bounded state;

the collective system evolves through **choreography** rather than orchestration.

Each local repositioning alters the ecosystem seen by others and therefore changes their future Δ_RA inputs and local agentic gradients.

No global objective, common ACC, common MSCA or equilibrium is required.

## 15. Falsification / boundary conditions

A candidate implementation violates this law if it:

- minimizes uncertainty that has no material connection to its declared objective while ignoring material objective risk;
- averages hard/non-compensable risk away with unrelated gains;
- treats B confidence as proof that C/D are empty;
- treats C as already determined A;
- acts directly on D as though its state were known;
- treats a large ecosystem delta as locally material without dependency projection;
- lets a positive gradient create authority;
- treats ACC inadmissibility as if the opportunity did not exist;
- ignores cost/deadline/capacity when those affect S;
- claims a globally optimal gradient from a participant-local bounded model.

## 16. Canonical law

The law can be stated compactly:

> **For a participant operating under an MSCA and Objective Envelope, the locally relevant gradient of a qualified ecosystem change is the admissible change in expected objective fulfilment — equivalently, the reduction in objective-conditioned uncertainty/risk — produced by a candidate repositioning, after preserving the non-fungible A/B/C/D structure and before authority/execution.**

Or:

~~~text
Agentic Gradient
=
Objective-conditioned projection of ecosystem change
×
expected reduction of non-fungible MSCA risk
subject to
ACC + authority + capability + time
~~~

This law supplies the mathematical/architectural bridge between Regime Awareness, [Canonical MSCA Operation & Repositioning](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) and ecosystem choreography.
