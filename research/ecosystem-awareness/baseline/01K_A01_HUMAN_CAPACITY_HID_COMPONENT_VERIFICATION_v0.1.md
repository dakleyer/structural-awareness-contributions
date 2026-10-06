# 01K-A01 — Human Capacity / HID Component Verification Record v0.1

**Date:** 6 October 2026  
**Status:** same-author/same-assistant verification record; not independent validation.  
**Component:** [01K-A01 specification](./01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md)  
**Schema:** [JSON Schema](./01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SCHEMA_v0.1.json)  
**Controls:** [semantic test vectors](./01K_A01_HUMAN_CAPACITY_HID_COMPONENT_TEST_VECTORS_v0.1.json)

## 1. Source reconciliation performed

The component was checked against the current public source/consumer documents:

- [01K — Human Capacity / Human Intelligence Debt](./01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md)
- [04 — General Functional Interfaces / EHD](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md)
- [01J — Ecosystem Signalling](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md)
- [01C — EA ↔ Regime Awareness](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md)
- [01B — EA ↔ MSCA](./01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md)
- [Canonical MSCA Architecture](../../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md)
- [Canonical MSCA Operation & Repositioning](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md)
- [UC-EA-03](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md)
- [R01 Human Escalation / Whispering](./reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md)

The parent HID source map already reconciles the Tegrity.AI Human Intelligence Debt / Human Intelligence Gap series and its bridge papers.

## 2. Architectural boundary checks

### Passed — no semantic ownership collision

A01 does not redefine:

- EHD;
- ReceivedSignals_i;
- Cart_i / Delta_Cart;
- Delta_RA;
- MSCA S/E/C/P/M;
- ACC;
- authority;
- Gradient;
- Repositioning outcomes.

### Passed — runtime capacity remains separate from HID

The component uses two different engines and result objects.

No formula equates:

~~~text
runtime queue deficit
=
Human Intelligence Debt
~~~

### Passed — human availability does not create authority

Competence, authority, information sufficiency and timing remain separate terms in eligibility.

### Passed — UNKNOWN remains first-class

The state model does not default missing authority, competence, timing or telemetry to AVAILABLE.

## 3. Mathematical consistency checks

### 3.1 Response margin

For an eligible route:

~~~text
T_hat_ij(q)
=
max(t_now, next_available_j)
+
BacklogDelay_j(q)
+
ServiceTime_ij(q)

ResponseMargin_ij(q)
=
deadline_i - T_hat_ij(q)
~~~

The equations are dimensionally consistent when all timing terms use the same time unit.

### 3.2 Multi-case load

~~~text
sum_i x_ij * ServiceDemand_ij(q)
<=
AvailableServiceTime_j(W)
~~~

is explicitly labelled a **necessary load condition**, not a sufficient schedulability proof when release times, deadlines or non-preemptible work differ.

This prevents the component from converting a workload ratio into a false scheduling guarantee.

### 3.3 HID accounting identity

For exclusive primary task classes:

~~~text
H_total = H_GIC + H_NEO + H_ACW
~~~

and:

~~~text
HICR_time = H_GIC / H_total
HID_observed = H_ACW / H_total
~~~

are dimensionless and do not double-count ACW modifiers.

### 3.4 Bounded counterfactual

The interval form:

~~~text
H_releasable in [L,U]

HICT in [
  HICR_time + L/H_total,
  HICR_time + U/H_total
]
~~~

preserves counterfactual uncertainty instead of manufacturing a midpoint.

### 3.5 Recovery quantities

F_HICT and HID_spent are emitted only when rho is supplied with explicit evidence status.

The component does not infer rho < 1 from fragmentation alone.

## 4. Machine-readable artefact checks

The current JSON Schema parses as valid JSON.

The current semantic test-vector file parses as valid JSON.

Eight vector IDs are present and unique.

Arithmetic controls recomputed from the published vectors:

| Vector | Recomputed check | Declared result |
|---|---:|---:|
| HC-HID-TV-01 | response margin = 30 − (5+10) = **+15** | +15 |
| HC-HID-TV-01 | HICR = 20/100 = **0.20** | 0.20 |
| HC-HID-TV-01 | HID_observed = 70/100 = **0.70** | 0.70 |
| HC-HID-TV-02 | response margin = 20 − (20+10) = **−10** | UNAVAILABLE |
| HC-HID-TV-04 | response margin = 20 − (6+10) = **+4** | +4 / DEGRADED |
| HC-HID-TV-06 | NOI = 18 − 8 = **+10** | +10 |

The remaining vectors are semantic controls rather than arithmetic identities:

- unresolved authority → UNKNOWN;
- Study-0 gate closed → RESEARCH_ONLY;
- one non-preemptible reviewer with incompatible simultaneous deadlines → no feasible batch assignment;
- high HID does not remove current necessary NEO.

## 5. External-method boundary check

The component's workload-observation boundary is consistent with current external reference material:

- ISO 10075-1:2017 defines mental-workload terminology and relations;
- ISO 10075-2:2024 addresses design of work systems and use of human capacities, including robotics and intelligent autonomous systems, with overload and underload in scope;
- ISO 10075-3:2004 addresses principles and requirements for methods that measure/assess mental workload;
- NASA TLX provides a subjective multidimensional workload instrument.

A01 uses those only as **optional workload observability references**.

It does not claim that any of them:

- validates HID;
- yields Human Capacity directly;
- supplies competence/authority;
- proves decision correctness;
- creates a conversion into a universal Human Intelligence unit.

## 6. Current falsifiers / unresolved obligations

The component is **not** considered fully engineered or empirically validated until the following are separately closed.

### Runtime side

1. a real source of reviewer/pool availability and commitments;
2. a declared service-time model per task/reviewer class;
3. validation/calibration of prediction quantiles or bounds;
4. a multi-case scheduler or conservative admission controller;
5. explicit treatment of preemption and non-preemptible duties;
6. live expiry/requalification on schedule, authority and context changes;
7. privacy/security review of HumanPoolSnapshot;
8. at least one real EHD/01J adapter.

### HID side

1. Study 0 instrument validation;
2. empirical GIC/NEO/ACW classification reliability;
3. counterfactual evidence for H_releasable;
4. intervention data before estimating rho;
5. no claim of historical decay from one snapshot;
6. validation of NOI and oversight-threshold hypotheses in real processes.

### Integration side

1. confirm which 01K fields belong in local-only state versus shareable Signalling profiles;
2. bind validity/revalidation to actual Cart/RA/Operation consumers;
3. run the one-human/two-obligation case through the component and UC-EA-03/R01 harness;
4. test a competent conventional implementation with equal/lower burden;
5. prove that adding the component does not silently create another authority or central orchestrator.

## 7. Current verdict

**Architectural specification:** coherent enough for reuse and implementation prototyping.  
**Machine-readable profile:** structurally available; JSON syntax verified.  
**Semantic controls:** eight deterministic controls registered; core arithmetic controls recomputed.  
**Runtime engineering validation:** open.  
**Human empirical calibration:** open.  
**HID empirical validation:** open by source-series design.  
**Independent review:** open.

The current justified claim is therefore:

> 01K-A01 is a reusable, internally specified HC-HID component contract with explicit formulas, states, inputs/outputs, architectural integration points and falsification obligations. It is not yet a validated production component or empirical Human Intelligence Debt instrument.


---

## 8. A/B/C/D / EHD reconciliation update

**Update 6 October 2026.** The component now explicitly follows the canonical 00M process-relative semantics.

Two different producer processes are retained:

~~~text
Runtime Capacity Engine
-> [A_HC,B_HC,C_HC,D_HC]

HID Architecture Engine
-> [A_HID,B_HID,C_HID,D_HID]
~~~

Verification points:

- a delivered capacity state / completion interval / declared route-cost result is A of the HC producer when producing that result is the declared function;
- timing-model calibration, schedule snapshot, known exclusions, proof class and characterized unused alternatives are B_HC;
- a grounded but uncharacterized capacity avenue is C_HC;
- a material capacity effect beyond effective evaluation is D_HC;
- equivalent rules apply to the HID engine;
- EHD preserves the producer's role but the receiving process **requalifies** it; `A_HC` is not automatically `A_EA`, `A_Cart` or `A_RA`;
- source-side D is not copied as receiver-side D when the receiver has a stronger evaluation route.

This closes the principal semantic ambiguity identified in the follow-up discussion.

## 9. Circularity control update

The component now declares a versioned feedback rule:

~~~text
InputBundle_n
-> HC-HID evaluation n
-> qualified result n
-> receiver-local requalification
-> new InputBundle_(n+1)
~~~

Within one `evaluation_id`, the component output cannot be reused as independent evidence for a premise of the same evaluation.

The new semantic control **HC-HID-TV-10** requires detection of same-operation self-support and expects:

- circularity flag = true;
- runtime result = UNKNOWN;
- requalification request = true;
- no command / no privileged escalation.

Feedback through later observed effects remains permitted when provenance and cycle/version are preserved.

## 10. DDS cost reconciliation update

The component now imports the existing DDS cost form:

~~~text
C(tau) = sum_g c_g(tau)
~~~

and refines only the human-related ledger.

Explicit cost surfaces include:

- human runtime;
- maintained/readiness capacity;
- case preparation;
- coordination;
- rework;
- ACW/HID architecture burden;
- HC-HID component operation;
- communication / external calls / compute;
- raw latency plus any separately declared monetised latency.

Readiness capacity is not free when unused.

A scalar DDS cost is allowed only with a declared valuation/allocation rule; otherwise the burden remains a vector.

Fair comparison requires the same frozen Challenge and sufficient-quality / I-region semantics. A cheaper M-route is not treated as a substitute for an I-route.

### New deterministic controls

**HC-HID-TV-09 — A/B/C/D mapping**

Checks that a completion interval can be A_HC when it is the component's deliverable, while schedule/calibration evidence remains B_HC, an uncharacterized specialist route is C_HC and hidden off-system commitments remain D_HC.

**HC-HID-TV-11 — readiness cost even with no alert**

Recomputed:

~~~text
human total
=
0 runtime
+ 100 readiness allocation
+ 10 component operation
= 110

peer total = 50

DeltaC_H = +60
~~~

Both routes declare the same DDS I-region and Risk gate, so the peer receives full credit.

**HC-HID-TV-12 — cheaper but lower-quality peer**

Human route reaches I1 at cost 120.

Peer route reaches M1 at cost 20.

The test correctly marks:

~~~text
same_challenge_I_region = false
cost_dominance_claim_allowed = false
~~~

This prevents price-only comparison across different effectiveness regions.

## 11. Updated verification verdict

**A/B/C/D integration:** explicit and process-relative.  
**EHD mapping:** explicit; receiver-side requalification required.  
**Same-operation circularity:** explicit prohibition + deterministic control.  
**DDS cost integration:** explicit human-runtime/readiness/architecture/component ledger.  
**Matched alternative-route comparison:** explicit same-Challenge/I-region requirement.  
**Machine-readable schema:** updated with evaluation/version, qualified positions and cost profile.  
**Semantic controls:** twelve registered; new A/B/C/D, circularity and DDS-cost controls recomputed where arithmetic applies.

Remaining empirical/engineering obligations from the previous verdict still apply.
