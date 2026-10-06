# 01K-A01 — Human Capacity / Human Intelligence Debt Reusable Component Specification

**Status:** public working component specification v0.1 · 6 October 2026.  
**Parent:** [01K — Human Capacity / Human Intelligence Debt](./01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md).  
**Architectural position:** additive component consumed by Ecosystem Positioning / MSCA / Signalling where material; not an EA core function, not an authority source, not an adopted standard.

## 0. Why this file exists

01K defines the research and architectural meaning of Human Capacity and Human Intelligence Debt. This file turns that material into a **reusable component contract**.

The component can be implemented as a service, library, agent-side module, organisational analytics function or manual assessment process. The implementation technology is intentionally open.

The component has two independent engines:

~~~text
HC-HID Component
|
+-- Runtime Capacity Engine
|   "Can a qualified human intervene in this case, in time?"
|
+-- HID Architecture Engine
    "Is the socio-technical design using humans for genuine contribution /
     necessary oversight, or as avoidable compensatory middleware?"
~~~

The two engines may be deployed independently.

A runtime Human Escalation implementation need not run an enterprise HID study.

An enterprise HID study need not be connected to a live Human Escalation path.

When both are present, they share scope/provenance and can inform the same Ecosystem Positioning cycle without becoming one metric.

---

# 1. Semantic ownership and non-ownership

The component **owns only**:

1. runtime qualification of declared Human Capacity inputs;
2. optional HID task/architecture measurement under the source-series evidence gates;
3. bounded output profiles that other architecture components may consume.

The component **does not own**:

- the truth of an alert or claim;
- Ecosystem Awareness A/B/C/D semantics;
- Ecosystem Cartography;
- Regime Awareness;
- MSCA sufficiency;
- ACC creation or mutation;
- authority/delegation;
- the agentic gradient;
- final Repositioning disposition;
- containment/isolation actuation;
- human legal responsibility.

No output from this component is a command.

No HID score creates authority.

No AVAILABLE state proves that the human's eventual answer will be correct.

---

# 2. Architectural placement

The normal integration route is:

~~~text
local observation / external signal / RA / repositioning condition
        |
        v
EHD / Ecosystem Signalling
        |
        v
receiver qualification
        |
        +------------------------------+
        |                              |
        v                              v
Cart_i / Delta_Cart              HC-HID Component
        |                         |          |
        v                         |          +--> HID architecture evidence
Regime Awareness                  +--> Runtime Human Capacity
        |                                    |
        +----------------+-------------------+
                         v
                MSCA Operation / Repositioning
                         |
                 ACC / lineage / authority
                         |
                         v
              authorised owner / human path
                         |
                         v
                   effect / feedback
~~~

A Human Capacity result may also be computed **before** a human-directed signal is emitted, so that the system does not route work into a path that is already known to be unusable.

An HID architecture result is normally slower-moving and may be computed per process, capability, product, portfolio or organisational window rather than per incident.

---


# 2A. A/B/C/D mapping and EHD contract

A/B/C/D is **process-relative**. The HC-HID component therefore does not emit one blended epistemic position for "human intelligence". It has two producer processes and each emits its own qualified position.

## 2A.1 Runtime Human Capacity process

Fix:

~~~text
producer = HC-HID Runtime Capacity Engine
function = assess whether a declared human intervention path is usable
question = HumanInterventionRequest i
scope = declared decision / role / response window W
time = t
~~~

Then the canonical 00M mapping is:

| HC component | Meaning in Runtime Human Capacity |
|---|---|
| **A_HC** | The result actually delivered by the capacity process: e.g. AVAILABLE / DEGRADED / UNAVAILABLE / UNKNOWN, selected eligible route where established, predicted acknowledgement/completion, response margin, and any route-cost result that this process explicitly delivers. |
| **B_HC** | Established basis and characterized reserve supporting/qualifying A_HC: competence and authority evidence, pool snapshot/version, timing model, prediction interval or bound, known exclusions, proof class, fallback already characterized, known alternative eligible routes left unused, cost assumptions/rates and validity/revalidation conditions. |
| **C_HC** | Grounded but uncharacterized avenues for obtaining human capacity: e.g. another reviewer pool, another organisational unit or external specialist is known to be potentially reachable, but competence/authority/service/cost variables are not yet characterized enough for B-type evaluation. |
| **D_HC** | Potentially material capacity influences beyond the process's effective evaluation route under current access/method/authority/time: e.g. hidden commitments or off-system constraints that may invalidate the schedule but cannot presently be evaluated. |
| **UNKNOWN** | The component has not established enough scope/capability to assign an A/B/C/D role. UNKNOWN is not forced into C or D. |

A probability, confidence interval, response-margin interval or cost estimate can be **A_HC** when producing that measure is part of the declared Runtime Capacity function. The calibration, coverage, model assumptions and limits that qualify that delivered measure are **B_HC**. This follows the canonical 00M rule that A/B is determined by function, not datatype.

## 2A.2 HID Architecture process

Fix:

~~~text
producer = HC-HID Architecture Engine
function = assess human-intelligence allocation/debt for declared scope P
question = HID architecture / measurement question
scope = process / capability / portfolio / measurement window
time = t
~~~

Then:

| HID component | Meaning in HID Architecture |
|---|---|
| **A_HID** | The delivered HID result for the declared measurement function: qualitative architecture finding and, where admitted, measured/bounded H_GIC, H_NEO, H_ACW, HICR_time, HID_observed, HICT interval/point, F-HICT, HID_spent, NOI and declared architectural mechanism findings. |
| **B_HID** | Established basis, limits and characterized reserve: Study-0 status, task-classification evidence, assessor agreement, counterfactual evidence tier, measurement window, technological period, tracer coverage, releasable-capacity bounds, measured/assumed rho status, known exclusions, uncertainty and already-characterized additional measurements that could be performed. |
| **C_HID** | Grounded but not yet characterized architecture/measurement avenues: suspected ACW-generating process, candidate counterfactual, candidate automation/recovery intervention or new data source for which the variables/method/cost/yield are not yet sufficiently characterized. |
| **D_HID** | Potentially material human-intelligence effects beyond effective evaluation: unobserved shadow work, effects outside the measurement boundary, unknown recovery/hysteresis mechanisms or capability losses for which no effective evaluation route presently exists. |
| **UNKNOWN** | Scope, classification basis or capability boundary is not established enough to assign an A/B/C/D role. |

Again, an interval is not automatically B. If the HID engine's declared output is a bounded HICT interval, that interval is **A_HID** and the evidence/calibration supporting it is **B_HID**.

## 2A.3 EHD projection

HC-HID uses the existing EHD/general-interface semantics; it does not create a competing handoff.

A bounded HC-HID EHD/profile projection may carry:

~~~text
HC_HID_EHD_Profile = {
  producer_process,
  decision_or_measurement_ref,
  scope,
  time,
  A_HC?, B_HC?, C_HC?, D_HC?,
  A_HID?, B_HID?, C_HID?, D_HID?,
  cost_projection?,
  provenance,
  validity,
  revalidation_conditions
}
~~~

All fields are optional according to the declared process/profile.

The sender MAY transmit only A plus enough EHD metadata to bind the result. Missing B/C/D remains **NOT DECLARED / UNKNOWN to the receiver**, not zero.

The receiver:

~~~text
received HC-HID EHD
-> verifies identity / provenance / scope / freshness / compatibility
-> preserves producer-native A/B/C/D roles
-> performs receiver-local qualification
-> decides whether the result is relevant to EA / Cartography / RA / MSCA / Repositioning
~~~

Transport does not make A_HC or A_HID true for the receiver.

A_HC is a result about **capacity**, not a permission to act.

A_HID is a result about **architectural allocation/debt**, not a current incident disposition.

## 2A.4 Cost inside A/B/C/D

Cost follows the same process-relative rule.

If the HC-HID process is explicitly asked:

> "What is the qualified cost of obtaining this human intervention / alternative information route?"

then the delivered cost estimate or cost interval is **A_COST** of that cost-evaluation process.

If cost is used only to qualify another delivered capacity result, it belongs to **B_HC** or **B_HID** as appropriate.

A characterized alternative whose cost is already assessable but not selected remains B.

A grounded alternative whose cost/effect basis is not yet characterized is C.

A potentially material cost beyond effective evaluation is D.

This distinction prevents "we have not priced it" from being silently rewritten as "it is cheap" or "it is residual risk."

# 2B. Circularity and feedback control

The HC-HID ↔ EA relation is a **feedback loop**, but it must not become a same-operation evidential circle.

The legitimate loop is time/version indexed:

~~~text
EA / EHD / Cart / MSCA state at version n
        |
        v
HC-HID evaluation n
        |
        v
qualified HC-HID result n
        |
        v
receiver-local requalification / Cart or RA update
        |
        v
new decision/input bundle version n+1
        |
        v
HC-HID re-evaluation n+1 where material
~~~

### Same-operation anti-circularity rule

For one evaluation identifier `eval_id=n`:

> **HC-HID output produced from InputBundle_n MUST NOT be reused as independent evidence to establish a premise of that same HC-HID evaluation n.**

Examples of prohibited same-cycle circularity:

- A_HC says the reviewer is AVAILABLE because EA says a human path exists, while EA says the human path exists only because A_HC says AVAILABLE.
- B_HC uses a response margin derived from a schedule that itself assumes the availability conclusion being proven.
- A_HID labels work as ACW because a policy already says "this interface creates HID", then uses the resulting HID score as evidence that the policy is correct.
- repeated HC-HID messages are counted as independent corroboration of the same source state.

### Permitted feedback

A completed earlier result MAY become input to a later evaluation when it is treated as a **historical observation with provenance**, not as independent corroboration.

For example:

~~~text
A_HC(n) = AVAILABLE
actual effect later misses deadline
        |
        v
effect record becomes new evidence
        |
        v
B_HC / timing model is requalified at n+1
~~~

Likewise:

~~~text
A_HID(n) identifies high ACW
architecture is changed
new task ledger is observed
        |
        v
A_HID(n+1) measures the new state
~~~

### When HC-HID causes escalation

HC-HID itself does **not** own ESCALATE as a special interrupt.

It emits an ordinary qualified result.

A consuming policy/component may decide that:

- A_HC = UNAVAILABLE;
- A_HC = UNKNOWN for a mandatory human gate;
- low/negative response margin;
- material D_HC;
- a material HID/NOI condition under an explicitly declared architecture-review policy;

requires HOLD, fallback, requalification, ESCALATE or another Repositioning result.

That decision remains owned by the consuming MSCA/Repositioning/authority process.

The component may emit a bounded **requalification request** as an ordinary output when an input needed for its own function is missing or stale. A request is not a command and does not grant authority.


# 2C. Receiver-side requalification — producer A/B/C/D is not copied

The EHD preserves the producer's semantic role; it does not make that role universal.

For receiver process R:

~~~text
ProducerQualifiedPosition
=
[A_HC, B_HC, C_HC, D_HC]

-- EHD -->

Receiver R
=
requalify(
  producer,
  scope,
  provenance,
  freshness,
  compatibility,
  own capability,
  own question
)
~~~

The receiver MUST NOT apply:

~~~text
A_HC -> A_R
B_HC -> B_R
C_HC -> C_R
D_HC -> D_R
~~~

as a mechanical identity.

Examples:

- `A_HC = AVAILABLE` is the delivered result of the Runtime Capacity process. For an EA process deciding whether the current frame has an effective intervention path, that result is **input evidence**. After receiver-side qualification it may support the EA result or its basis; it is not automatically `A_EA`.
- `B_HC` may become B of the receiving process when it qualifies a receiver result, or it may remain source evidence without being adopted.
- `C_HC` becomes C for the receiver only if the receiver itself has a grounded but still uncharacterized route to explore it.
- `D_HC` remains D for the receiver only if the relevant effect is also beyond the receiver's effective evaluation route. A specialist receiver may convert a source-side D aspect into its own C, B or A.
- the same rule applies to `A_HID/B_HID/C_HID/D_HID`.

This is the canonical 00M "same phenomenon, different actor/process" rule applied to HC-HID.

## 2C.1 Mapping into Cartography

When HC-HID is material to the local ecosystem representation, Composition & Control may represent a dependency such as:

~~~text
Decision / Role / Process
  -> depends on
HumanReviewCapability(
  competence,
  authority,
  response_window,
  capacity_state
)
~~~

HC-HID does not directly write `A_Cart/B_Cart/C_Cart/D_Cart`.

The Cartography process requalifies the received result and assigns its own process-relative position.

Therefore:

~~~text
A_HC != A_Cart
B_HC != B_Cart
...
~~~

unless the Cartography process independently establishes that correspondence for its own declared function.

## 2C.2 Mapping into Regime Awareness

HC-HID capacity/debt changes are not automatically regime changes.

A material change in Human Capacity, answerability, reviewer dependency or architecture burden may become an RA input **only when it is relevant to the operating-frame question**.

RA then produces its own `Delta_RA=[A_RA,B_RA,C_RA,D_RA]`.

Therefore:

~~~text
A_HC != A_RA
A_HID != A_RA
~~~

by default.

A capacity drop may be evidence of regime departure; it is not itself the regime-position output.

## 2C.3 Mapping into Repositioning

Repositioning may consume the receiver-qualified HC-HID evidence together with Cartography, RA, MSCA, ACC and authority.

The HC-HID output does not select P1/P2/P3 and does not choose ESCALATE.

The normal decision table is:

| HC-HID runtime result | HC-HID own action | Typical downstream consequence when human intervention is mandatory |
|---|---|---|
| **AVAILABLE** with adequate margin | Return normal qualified result | Human path may remain candidate; ACC/authority and other gates still apply. |
| **DEGRADED** | Return qualified result + reasons/fallback/margin | Consumer may use fallback, requalify, reduce reliance or escalate according to policy. |
| **UNAVAILABLE** | Return qualified result | Consumer must not treat the human gate as satisfied; HOLD/fallback/alternative/ESCALATE belongs downstream. |
| **UNKNOWN** | Return qualified result and optionally request missing/stale inputs | Consumer must not assume availability; if the human gate is mandatory and time is material, HOLD/requalification/ESCALATE may follow downstream. |
| **High HID / positive NOI** without incident-capacity failure | Return architecture/debt result | Architecture/design review; **no automatic incident escalation**. |

This keeps 01K a normal component rather than a privileged safety interrupt.

# 3. Core typed objects

## 3.1 HumanInterventionRequest

~~~text
HumanInterventionRequest = {
  request_id,
  participant_id,
  decision_ref,
  scope,
  now,
  deadline,
  required_competencies[],
  required_authority,
  information_sufficiency,
  service_class,
  criticality,
  EHD_ref?,
  ACC_ref?,
  authority_ref?,
  RA_ref?,
  Cart_ref?,
  RepositionIntent_ref?,
  fallback_policy?,
  validity / revalidation conditions
}
~~~

**Required competencies are not fungible.**

A reviewer who has time but lacks the required competence does not create capacity for that request.

## 3.2 HumanPoolSnapshot

~~~text
HumanPoolSnapshot = {
  snapshot_time,
  valid_until,
  reviewers[] or role_pools[],
  provenance,
  telemetry_quality
}
~~~

Each reviewer/role-pool record may contain:

~~~text
{
  reviewer_or_pool_id,
  competence_set,
  authority_set / authority references,
  available_from,
  available_until,
  current_commitments,
  backlog model,
  service-time model,
  non-preemptible commitments,
  fallback flag,
  information-access constraints,
  privacy projection,
  source freshness
}
~~~

A public or cross-system profile SHOULD use role/pool identifiers rather than personal identity unless identity is required for the legitimate decision.

## 3.3 HIDTaskLedger

~~~text
HIDTaskLedger = {
  scope,
  measurement_window,
  technological_period,
  episodes[] {
    episode_id,
    hours,
    class = GIC | NEO | ACW,
    modifiers[],
    capability taxonomy,
    evidence,
    assessor / tracer provenance
  },
  Study0_status,
  counterfactual_evidence,
  releasable_capacity?,
  recovery_coefficient?,
  oversight_hours_added?,
  oversight_hours_removed?
}
~~~

GIC / NEO / ACW are mutually exclusive primary classes for one measured episode.

Modifiers such as ACW-AOV, ACW-WFR and ACW-TTC MUST NOT be added again as separate hours.

## 3.4 PolicyProfile

The component does not invent universal thresholds.

A deployment may supply:

~~~text
PolicyProfile = {
  warning_response_margin?,
  required_prediction_quantile?,
  acceptable_proof_classes[],
  capacity_revalidation_interval?,
  HID_review_thresholds?,
  NOI_thresholds?,
  privacy rules?,
  escalation fallback rules?
}
~~~

Threshold provenance MUST be explicit.

---

# 4. Output contract

~~~text
HumanCapacityHIDResult = {
  runtime_capacity?,
  hid_architecture?,
  policy_interpretation?,
  signal_projection?,
  evidence_envelope,
  provenance,
  valid_until,
  revalidation_conditions
}
~~~

## 4.1 RuntimeCapacityAssessment

~~~text
RuntimeCapacityAssessment = {
  state =
    AVAILABLE |
    DEGRADED |
    UNAVAILABLE |
    UNKNOWN,

  selected_route?,
  eligible_routes?,
  predicted_ack_time?,
  predicted_completion_time?,
  response_margin?,
  fallback_used?,
  proof_class =
    EXACT |
    CONSERVATIVE_BOUND |
    HEURISTIC |
    UNKNOWN,

  material_unknowns[],
  reasons[],
  valid_until,
  source_snapshot_ref
}
~~~

## 4.2 HIDArchitectureAssessment

~~~text
HIDArchitectureAssessment = {
  quantitative_status =
    NOT_MEASURED |
    RESEARCH_ONLY |
    MEASURED_BOUNDED,

  scope,
  H_GIC?,
  H_NEO?,
  H_ACW?,
  H_total?,
  HICR_time?,
  HID_observed?,
  H_releasable?,
  HICT?,
  F_HICT?,
  HID_spent?,
  NOI?,

  architecture_mechanisms[],
  answerability_indicators?,
  multiplicity_indicators?,
  velocity_indicators?,
  counterfactual_evidence?,
  Study0_status,
  evidence_strength,
  material_unknowns[],
  revalidation_conditions
}
~~~

If Study 0 has not passed, an implementation MAY report raw task observations and qualitative architecture findings, but it MUST NOT present the quantitative output as an empirically established organisational HID value.

---

# 5. Runtime Capacity Engine — formal model

## 5.1 Tri-state eligibility

For intervention request i and reviewer/pool j define:

- K_ij = competence match;
- A_ij = applicable authority;
- I_ij = sufficient information/access for the requested decision;
- V_j = reviewer/pool availability/validity.

Each element is:

~~~text
TRUE | FALSE | UNKNOWN
~~~

Then:

~~~text
Eligible_ij = TRUE
iff
K_ij = TRUE
AND A_ij = TRUE
AND I_ij = TRUE
AND V_j = TRUE
~~~

If any material term is FALSE, the route is not eligible.

If no eligible route is established and at least one route remains materially UNKNOWN, the component MUST NOT report UNAVAILABLE as if infeasibility had been proved; it reports UNKNOWN.

Likewise, UNKNOWN MUST NOT silently become AVAILABLE.

## 5.2 Predicted completion and response margin

Where a timing model exists, for declared prediction quantile q:

~~~text
T_hat_ij(q)
=
max(t_now, next_available_j)
+
BacklogDelay_j(q)
+
ServiceTime_ij(q)
~~~

and:

~~~text
ResponseMargin_ij(q)
=
deadline_i - T_hat_ij(q)
~~~

q is deployment-declared. There is no universal mandatory 90th, 95th or 99th percentile.

If only a deterministic upper bound is known, that bound may replace the quantile estimate and the proof class becomes CONSERVATIVE_BOUND.

If the implementation has only a heuristic point estimate, the result MUST say HEURISTIC.

## 5.3 Runtime state rule

A minimal state rule is:

~~~text
AVAILABLE
  if at least one eligible route is established
  and predicted completion is inside the response window
  and no material unknown defeats that conclusion.

DEGRADED
  if a feasible route exists but only through fallback,
  low declared response margin,
  reduced redundancy,
  or another deployment-declared degraded condition.

UNAVAILABLE
  if all relevant candidate routes are sufficiently known
  and none can complete the required intervention inside the window.

UNKNOWN
  if the component cannot establish either a usable route
  or proven unavailability because material competence, authority,
  information, queue, timing or freshness state is unresolved.
~~~

The component does not create a fifth state for every failure cause; causes remain structured reasons.

## 5.4 Multiple simultaneous obligations

Human capacity is not static headcount.

For cases i in I and reviewers/pools j in J, let:

~~~text
x_ij in {0,1}
~~~

represent assignment.

A basic assignment requires:

~~~text
sum_j x_ij = 1
x_ij <= Eligible_ij
~~~

for every admitted case i.

For an additive service-time model, a necessary load condition for reviewer/pool j over window W is:

~~~text
sum_i x_ij * ServiceDemand_ij(q)
<=
AvailableServiceTime_j(W)
~~~

This load inequality alone is **not sufficient** when cases have different release times, deadlines, non-preemptible work or precedence constraints.

A production implementation SHOULD therefore expose its scheduling proof class:

- **EXACT** — an explicit feasible schedule/assignment is constructed under the declared model;
- **CONSERVATIVE_BOUND** — sufficient bounds prove feasibility;
- **HEURISTIC** — a scheduler proposes a route without proof;
- **UNKNOWN** — feasibility remains unresolved.

## 5.5 Competence-specific pressure

Where service demand is additive inside one declared competence class k:

~~~text
CapacityPressure_k(W)
=
QualifiedDemand_k(W)
/
QualifiedCapacity_k(W)
~~~

This MAY be useful as an early-warning metric.

It MUST NOT be summed across incompatible competence classes as if all human capacity were fungible.

---

# 6. HID Architecture Engine — formal model

## 6.1 Exclusive task-time decomposition

For one validated measurement scope:

~~~text
H_total
=
H_GIC + H_NEO + H_ACW
~~~

with mutually exclusive primary classification.

The source-series metrics remain:

~~~text
HICR_time
=
H_GIC / H_total

HID_observed
=
H_ACW / H_total

HICT
=
HICR_time + H_releasable / H_total

F_HICT
=
HICR_time
+
rho_inf * H_releasable / H_total

HID_spent
=
(1 - rho_inf)
*
H_releasable / H_total

NOI
=
H_added - H_removed
~~~

No point estimate of F_HICT or HID_spent is emitted unless rho_inf is supplied by a measurement process whose evidence status is explicit.

## 6.2 Bounded counterfactuals

Where releasable capacity is uncertain but bounded:

~~~text
H_releasable in [L_releasable, U_releasable]
~~~

the component SHOULD preserve that uncertainty rather than manufacture a midpoint:

~~~text
HICT
in
[
  HICR_time + L_releasable / H_total,
  HICR_time + U_releasable / H_total
]
~~~

The same interval discipline applies to recovery quantities where rho is bounded rather than measured as a point estimate.

## 6.3 Interface-scoped debt reading

For a Human Escalation interface, the component may scope the ordinary source metric:

~~~text
HID_observed_escalation
=
H_ACW_escalation / H_total_escalation
~~~

This is not a new HID theory. It is the normal HID_observed metric restricted to the escalation interface.

It answers:

> Of the human time consumed by this interface, what share is avoidable compensatory work rather than genuine contribution or necessary oversight?

## 6.4 No automatic safety veto

A high HID_observed value does not itself block a safety-critical intervention.

The component separates:

~~~text
current incident necessity
from
architecture debt
~~~

A necessary NEO intervention may still be required now even if the long-run interface is debt-producing.

The HID result therefore becomes a design/review input unless an externally legitimate policy explicitly gives it operational consequences.

---

# 7. Combined two-gate evaluation

For a human-directed candidate action:

~~~text
Gate A — Runtime Capacity
Can a qualified, authorised, informed human route complete inside W?

Gate B — Architecture Use of Human Intelligence
Is this class of human work primarily GIC / necessary NEO,
or is the architecture repeatedly generating ACW?
~~~

The four combinations are meaningful:

| Gate A | Gate B | Meaning |
|---|---|---|
| PASS | PASS | Human route is usable now and architecturally justified. |
| PASS | FAIL/DEBT | Human can act now, but the interface/process is debt-producing and should enter architecture review. |
| FAIL | PASS | Human involvement may be architecturally justified, but usable capacity is absent now. |
| FAIL | FAIL/DEBT | The current human route is unavailable and the design is also debt-producing. |

UNKNOWN remains distinct from FAIL.

---


# 7A. DDS-compatible human cost model

HC-HID contributes to the existing DDS ledger; it does not create a second Cost–Risk–Effectiveness method.

The canonical DDS cost form is:

~~~text
C(tau) = sum_g c_g(tau)
~~~

and the declared ledger may include search/exploration, validation, external calls, communication, latency, human review, coordination, implementation/maintenance and repeated/recovery work.

HC-HID refines the **human-related cost terms** so that human fallback is never treated as free.

## 7A.1 Human cost vector

For route tau and accounting window W:

~~~text
C_HC_HID(tau,W) = [
  C_human_runtime,
  C_human_readiness_alloc,
  C_human_case_preparation,
  C_human_coordination,
  C_human_rework,
  C_HID_ACW_alloc,
  C_component_operation,
  C_latency,
  C_external_calls,
  C_compute,
  C_communication
]
~~~

The vector is preferred when terms are not commensurable.

A scalar DDS cost may be produced only when the profile declares the valuation/normalization rule and avoids double counting:

~~~text
C_DDS(tau)
=
sum_g c_g(tau)
~~~

## 7A.2 Runtime human cost

For one intervention:

~~~text
C_human_runtime(tau)
=
C_discovery
+
C_case_prep
+
C_review
+
C_coordination
+
C_application_support
+
C_rework
~~~

Queue delay is normally preserved as **latency/time**, not silently monetized.

If a deployment monetizes latency, it MUST preserve the raw latency separately so the same delay is not counted twice without an explicit rule.

## 7A.3 Cost of keeping human capacity available

Human readiness has a cost even if no alert arrives.

For maintained human-capacity pool J over accounting window W:

~~~text
C_human_readiness(J,W)
=
C_staffing
+
C_on_call_or_reserve
+
C_training
+
C_context_currency
+
C_tools_and_access
+
C_governance
+
C_capacity_telemetry
+
C_maintenance
~~~

A route-level allocated readiness cost is:

~~~text
C_human_readiness_alloc(tau)
=
AllocationRule(
  C_human_readiness(J,W),
  tau,
  W
)
~~~

The allocation rule may be time-based, demand-based, reserved-capacity-based or another declared method.

It MUST be stated.

A profile MUST NOT charge readiness to zero merely because the person was not called in that trace.

This preserves the R01/HEW discipline that a human/escalation phase can carry cost even when no alert occurs.

## 7A.4 Architectural human cost / HID cost surface

HID is primarily an architectural allocation measure, not a currency.

For DDS, a deployment may expose the corresponding burden without forcing it into money:

~~~text
HumanArchitectureBurden(P,W) = [
  H_ACW,
  HID_observed,
  NOI,
  H_releasable?,
  answerability_cost?,
  reconciliation_hours?,
  repeated_review_hours?
]
~~~

If the deployment has a legitimate monetary conversion, it may additionally calculate:

~~~text
C_HID_ACW
=
sum_e (
  H_ACW,e * DeclaredCostRate_e
)
~~~

but the underlying H_ACW/HID values remain visible.

The monetary projection MUST NOT replace the architectural metric.

## 7A.5 Cost of the HC-HID component itself

The component is not free.

Where material, DDS should charge:

~~~text
C_component_operation
=
C_data_acquisition
+
C_pool_telemetry
+
C_classification
+
C_model_or_scheduler
+
C_storage
+
C_signalling
+
C_revalidation
+
C_measurement_governance
~~~

Study-0/instrument-validation effort belongs to the architecture/measurement programme and may be amortized only under an explicit allocation rule.

## 7A.6 Alternative information routes

The human route MUST be compared with other routes capable of solving the **same frozen Challenge**.

Candidate routes may include:

~~~text
R = {
  human_review,
  automated_rule_or_model,
  direct_authoritative_source,
  retrieval_or_measurement,
  peer / external specialist,
  mixed human-machine route,
  bounded hold / requalification,
  other admissible route
}
~~~

For route r to be a fair peer for route h, the profile must preserve the same:

- decision/problem scope;
- authority boundary;
- sufficient-quality objective / DDS I-route definition;
- material facts and source access, except where route capability itself is the tested difference;
- deadline/response horizon;
- acceptance policy;
- Risk and Effectiveness semantics.

DDS already requires that the **I region is defined by the Challenge outcome, not by the mechanism**.

Therefore:

> a machine route that is cheaper but reaches a lower-quality M route does not prove that human review is inefficient;

and:

> a conventional non-human route reaching the same I route at equal or lower burden receives full credit.

## 7A.7 Cost–Risk–Effectiveness comparison

For each admissible route r:

~~~text
DDS_HC_HID(r) = [
  C(r),
  Risk(r),
  Effectiveness(r),
  Latency(r),
  ResponseMargin(r),
  Uncertainty(r),
  HumanArchitectureBurden(r)
]
~~~

No single scalar is required.

Default comparison is Pareto-style:

Route r1 dominates r2 only where, under the frozen comparison:

- r1 reaches the same required I/quality region;
- r1 does not worsen any declared hard Risk/authority constraint;
- r1 does not worsen any declared material comparison dimension;
- r1 improves at least one material dimension.

Human review receives no preference merely because it is human.

Automation receives no preference merely because it is cheaper.

## 7A.8 Human-route differential

A useful deployment differential for one matched information/decision task is:

~~~text
DeltaC_H = C(human_route) - C(best_admissible_peer_route)

DeltaL_H = Latency(human_route) - Latency(best_admissible_peer_route)

DeltaB_H = HumanArchitectureBurden(human_route)
           - HumanArchitectureBurden(peer_route)
~~~

These deltas are reported only when the compared routes satisfy the same frozen Challenge/quality/authority conditions.

A positive DeltaC_H does not by itself reject the human route if it produces lower material Risk or reaches an I route peers cannot reach.

Conversely, a human route that reaches the same I route at higher cost, latency and architectural burden with no compensating Risk/Effectiveness advantage has no demonstrated deployment differential.

## 7A.9 A/B/C/D of cost comparison

The route-cost comparison itself is also a qualified process:

- **A_COST** — delivered cost/burden comparison for the frozen routes;
- **B_COST** — rates, allocation rules, uncertainty, known excluded costs, amortization and characterized alternatives;
- **C_COST** — grounded alternative routes whose cost/effect basis is not yet characterized;
- **D_COST** — potentially material costs beyond effective evaluation.

This prevents an unpriced human-readiness or architectural-HID burden from being silently treated as zero.

# 8. Integration with the existing architecture

## 8.1 EHD / General Interfaces

The HumanInterventionRequest SHOULD reference or carry the decision-relevant EHD rather than reconstruct context independently.

Material fields include:

- decision/operation reference;
- subject/scope;
- source/provenance;
- freshness/version;
- material UNKNOWN/residual qualifiers;
- authority/ACC references where needed;
- review/expiry/re-entry conditions.

01K consumes the EHD. It does not redefine it.

## 8.2 Ecosystem Signalling / 01J

RuntimeCapacityAssessment and HIDArchitectureAssessment are **profile payloads over existing Signalling**, not new primitive signal classes.

A receiver requalifies them.

Transport success does not convert AVAILABLE into truth or create authority.

A material capacity change may be carried as a Human/Systemic Alert profile.

## 8.3 Ecosystem Cartography

Cart_i may represent **human-review capability dependencies** such as:

~~~text
process / role / decision
    -> requires
HumanReviewCapability(role_class, competence, authority, response_window)
~~~

The map SHOULD avoid exposing personal identity unless materially required.

A material change in that dependency can contribute to Delta_Cart.

01K does not own the Cartography.

## 8.4 Regime Awareness

RA may consume a material change in Human Capacity, portfolio answerability or another 01K-derived condition **only as qualified evidence relevant to the operating frame**.

RA does not calculate HID.

HID does not become an RA pole or posture.

A material RA result may in turn trigger a new Human Capacity check.

## 8.5 MSCA

Human Capacity naturally projects into:

- **P — Intervention mechanisms:** human escalation / review is a feasible intervention path;
- **M — Enabling means:** qualified human/external capacity, communication and effect-measurement capability.

An intervention mechanism without the enabling Human Capacity needed to use it is not made sufficient by naming the mechanism.

## 8.6 MSCA Operation / Repositioning

For a candidate transition requiring human decision:

~~~text
Repositioning
-> request RuntimeCapacityAssessment
-> preserve AVAILABLE / DEGRADED / UNAVAILABLE / UNKNOWN
-> continue ACC / lineage / authority gate
~~~

If the result is UNAVAILABLE or UNKNOWN, Repositioning may HOLD, seek a fallback, request evidence, seek another authority or remain UNRESOLVED according to its own rules.

01K does not select the final repositioning outcome.

Where the focal Objective Envelope or architecture-review policy includes human-intelligence sustainability / burden, the Gradient or Repositioning may also consume qualified HID/NOI evidence as a cost/risk input.

That consumption is objective-conditioned; HID does not silently become a universal optimisation objective.

## 8.7 Feedback / learning

Observed acknowledgement, decision, completion, expiry and effect records may update:

- backlog/service-time estimates;
- route validity;
- fallback reliability;
- task classification evidence;
- NOI;
- ACW patterns;
- revalidation conditions.

Feedback MUST preserve the distinction between:

~~~text
message receipt
decision
application
effect
~~~

A human approval is not proof that the underlying world model was correct.

---

# 9. State machines

## 9.1 Runtime state machine

~~~text
UNASSESSED
   |
   v
INPUT_QUALIFICATION
   |
   +--> UNKNOWN
   |
   v
ELIGIBILITY_MATCH
   |
   +--> UNAVAILABLE
   |
   v
TIMING / SCHEDULABILITY
   |
   +--> AVAILABLE
   +--> DEGRADED
   +--> UNAVAILABLE
   +--> UNKNOWN

any state
   |
   +--> EXPIRED
   +--> REQUALIFY on material change
~~~

## 9.2 HID measurement state machine

~~~text
NOT_MEASURED
   |
   v
SCOPED
   |
   v
TASK_CLASSIFICATION
   |
   v
INSTRUMENT_VALIDATION
   |
   +--> RESEARCH_ONLY
   |
   v
MEASURED_BOUNDED
   |
   v
REVALIDATE / INTERVENTION STUDY
~~~

A qualitative architecture review may exist before MEASURED_BOUNDED.

It must not be mislabeled as a measured organisational HID value.

---

# 10. Reference algorithms

## 10.1 AssessRuntimeCapacity

~~~text
function AssessRuntimeCapacity(request, pool, policy):

  validate decision boundary, deadline, freshness and required fields

  candidate_routes = []

  for each reviewer/pool j:
      competence = qualify competence match
      authority  = qualify applicable authority
      info       = qualify access / information sufficiency
      validity   = qualify availability / freshness

      if any is FALSE:
          reject route

      else if any is UNKNOWN:
          preserve UNKNOWN route

      else:
          estimate completion under declared timing model
          compute response margin
          add feasible route if inside deadline

  if feasible route exists:
      choose route according to declared policy
      return AVAILABLE or DEGRADED
      plus proof_class, margin and provenance

  else if material UNKNOWN route exists:
      return UNKNOWN

  else:
      return UNAVAILABLE
~~~

## 10.2 AssessHID

~~~text
function AssessHID(scope, task_ledger, counterfactuals):

  verify scope, technological period and exclusive GIC/NEO/ACW classification

  if Study0 gate is not satisfied:
      return qualitative findings + raw observations
      quantitative_status = RESEARCH_ONLY

  compute H_total, H_GIC, H_NEO, H_ACW
  compute HICR_time and HID_observed

  if bounded releasable capacity exists:
      compute HICT point or interval

  if measured/bounded rho exists:
      compute F_HICT and HID_spent point or interval
  else:
      leave them UNKNOWN

  if oversight added/removed work is measured:
      compute NOI

  return metrics + evidence envelope + material unknowns
~~~

## 10.3 ComposeForRepositioning

~~~text
function ComposeForRepositioning(candidate_transition):

  if candidate does not require human action:
      do not invent a Human Capacity dependency

  if candidate requires human action:
      runtime = AssessRuntimeCapacity(...)

  if architecture-review context exists:
      hid = AssessHID(...) or consume last valid bounded assessment

  emit qualified 01K result

  Repositioning independently applies:
      Cart / RA context
      ACC
      lineage
      authority
      Objective Envelope
      response horizon
~~~

---

# 11. Error and adversarial conditions

The component MUST preserve or test at least these failure families.

| Failure | Required behaviour |
|---|---|
| Stale reviewer schedule | Expire/requalify; do not retain AVAILABLE. |
| Competence mismatch | Do not count time as usable qualified capacity. |
| Authority mismatch | Do not convert expertise into permission. |
| Incomplete EHD/context | UNKNOWN or insufficient-information result; do not force approval. |
| Queue flood / alert storm | Preserve backlog and response-window effect; do not assume unlimited reviewers. |
| One human, simultaneous obligations | Expose assignment/scheduling conflict; naming the same human twice does not create capacity. |
| Non-preemptible critical work | Preserve existing commitment in the capacity model. |
| Fallback only | Return DEGRADED when policy declares fallback degradation. |
| Missing telemetry | UNKNOWN rather than optimistic AVAILABLE. |
| Metric gaming | Preserve classification provenance and inter-rater gate. |
| Relabel ACW as NEO/GIC | Re-audit classification; do not let managerial labels redefine evidence. |
| More guardrails create more human work | Capture NOI and ACW rather than assuming oversight is free. |
| High HID used to skip necessary safety review | Prohibited: architecture debt does not erase current legitimate NEO. |
| Human result contradicts source evidence | Preserve contradiction; approval does not rewrite evidence. |
| Privacy overexposure | Project role/pool capacity where possible; disclose identity only when necessary. |

---

# 12. Observability and measurement

## 12.1 Runtime observability

Useful observations include:

- request arrival;
- acknowledgement;
- queue entry/exit;
- assignment;
- review start/end;
- decision;
- application;
- effect confirmation;
- timeout;
- fallback invocation;
- re-entry/restart;
- workload discarded/reworked.

These records SHOULD be operation/decision scoped.

## 12.2 Mental-workload observability

Human workload may be observed separately.

Relevant external references include:

- ISO 10075-1:2017 — terminology for mental stress/strain and effects;
- ISO 10075-2:2024 — design principles for work systems and use of human capacities, including robotics and intelligent autonomous systems;
- ISO 10075-3:2004 — principles/requirements for methods that measure and assess mental workload;
- NASA Task Load Index (TLX) — subjective multidimensional workload assessment.

These may help observe **workload**.

They do not automatically provide:

- a Human Intelligence Debt value;
- an additive Human Capacity stock;
- a universal conversion into service minutes;
- competence or authority;
- correctness of the human decision.

Workload is therefore an optional observation channel, not the HC-HID kernel.

---

# 13. Privacy and disclosure

The component should follow minimum-sufficient disclosure.

An external signal can often expose:

~~~text
role class
capacity state
response margin band
proof class
validity
fallback availability
material unknowns
~~~

without exposing:

~~~text
personal identity
full schedule
medical/fatigue data
private HR data
individual performance history
~~~

unless the legitimate decision requires those details.

HID organisational measurement MUST NOT be repurposed as a hidden employee-ranking system.

The unit of architectural diagnosis is the **socio-technical design / task episode**, not human worth.

---

# 14. Conformance requirements

A component claiming conformance to this specification SHALL:

1. keep runtime Human Capacity and HID architecture debt distinct;
2. preserve UNKNOWN as a first-class state;
3. represent competence and authority separately from time availability;
4. expose timing proof class when predicting response;
5. preserve response-window/deadline semantics;
6. prevent the same human capacity from being counted as fungible across incompatible competence classes;
7. avoid treating a human alert/approval as truth or authority by itself;
8. use GIC/NEO/ACW without double-counting modifiers;
9. withhold empirical HID claims when the declared measurement gate is not passed;
10. preserve provenance, scope, technological period and revalidation conditions;
11. expose NOI when claiming that an oversight intervention reduces human work and the relevant added/removed hours are measured;
12. preserve the current-incident need for legitimate NEO even when long-run HID is high;
13. not convert HID into an automatic Repositioning posture;
14. not create ACC or authority;
15. not claim a universal Human Intelligence Token unit.

A component fails conformance if it:

- reports AVAILABLE from headcount alone;
- treats UNKNOWN capacity as AVAILABLE;
- reports a numerical HID value from unvalidated task labels;
- assumes more human review necessarily lowers risk/debt;
- uses a single scalar to hide competence mismatch;
- silently discards queue/deadline effects;
- uses HID as justification to remove necessary human oversight;
- turns an 01K payload into a command.

---

# 15. Machine-readable profile and test vectors

Companion artefacts:

- [01K-A01 component JSON Schema](./01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SCHEMA_v0.1.json)
- [01K-A01 semantic test vectors](./01K_A01_HUMAN_CAPACITY_HID_COMPONENT_TEST_VECTORS_v0.1.json)

The schema is an interchange/reference profile, not a mandatory wire format.

The vectors are deterministic semantic controls, not human-performance experiments.

---

# 16. Example — available human, debt-producing interface

Suppose:

- one reviewer has the required competence and authority;
- the case arrives at t=0;
- deadline = 30 minutes;
- backlog + review time predicts completion at 15 minutes;
- response margin = +15 minutes.

Runtime result:

~~~text
AVAILABLE
proof = EXACT under declared snapshot/model
response margin = +15 min
~~~

Now suppose the surrounding escalation interface consumes, over a validated measurement window:

~~~text
H_GIC = 20 h
H_NEO = 10 h
H_ACW = 70 h
H_total = 100 h
~~~

Then:

~~~text
HICR_time = 0.20
HID_observed = 0.70
NEO_share = 0.10
~~~

This is the key combined case:

> **The human path works operationally, but the architecture is using humans badly.**

The correct response is not to block this specific necessary intervention merely because HID is high.

The correct response is:

1. permit the current legitimate intervention if the surrounding architecture authorises it;
2. preserve the runtime capacity result;
3. route the recurring ACW pattern into architecture review;
4. redesign upstream capture/integration/guardrails/ownership so future human work moves toward GIC/necessary NEO.

---

# 17. Scientific / standards boundary

This component reuses source-series constructs and established workload/scheduling concepts, but its combined HC-HID composition is a **working architecture specification**.

It does not claim:

- empirical validation of organisational HID;
- a universal service-time distribution for human work;
- a universal q percentile;
- that ISO 10075 or NASA TLX validates HID;
- that queue feasibility proves decision quality;
- that the component is adopted by FG-TIDA, ITU-T, ISO or NIST.

The reusable contribution is the explicit separation and composition of:

~~~text
qualified human schedulability
+
architectural human-intelligence allocation/debt
+
existing EA / Signalling / RA / MSCA / Repositioning interfaces
~~~

That separation makes the component testable and replaceable without making humans a special super-controller in the architecture.
