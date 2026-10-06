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
