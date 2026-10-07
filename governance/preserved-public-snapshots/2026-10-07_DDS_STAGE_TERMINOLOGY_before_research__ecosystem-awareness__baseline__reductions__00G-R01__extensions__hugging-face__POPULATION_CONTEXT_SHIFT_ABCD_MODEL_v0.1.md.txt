# Historical Population Context-Shift Model — Hugging Face 2026 v0.1

**Status:** working analytical correction for the incident-derived DDS Gate-A campaign · population-first · no EA differential result · no R01 historical isomorphism claimed.

**Date:** 7 October 2026.

**Parent reconstruction:** [HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md](./HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md)

**Evidence register:** [HISTORICAL_INCIDENT_EVIDENCE_v0.1.json](./HISTORICAL_INCIDENT_EVIDENCE_v0.1.json)

**Cross-source matrix:** [CROSS_SOURCE_EVENT_MATRIX_v0.1.md](./CROSS_SOURCE_EVENT_MATRIX_v0.1.md)

**Refinement:** [ABCD_REQUIREMENTS_REPOSITIONING_TRACE_v0.1.md](./ABCD_REQUIREMENTS_REPOSITIONING_TRACE_v0.1.md) owns the more precise 00N reading: historical traces are mainly A outputs of their source processes; B/C/D are not invented population bins but qualification that must be preserved/acquired around those A outputs. The population distribution below is therefore an A result of a population evaluator, while its B/C/D qualify that population result and the route dimensions it composes.

---

## 0. Conceptual correction

The historical work must not equate **context change** with an individual agent recognizing that an action is wrong or out of scope.

An individual receiver can, under normal operation, select a legitimate reference route, a better admissible route, a prohibited route, or no sufficient route. That local selection is an operational outcome. It is not by itself evidence that the surrounding context or regime has changed.

For this incident, the relevant context-change object is **population-level**:

> the conditions under which the population makes decisions change, and the resulting distribution of active routes and route transitions changes materially.

The six-minute GO episode remains useful evidence about one local authority transition. It is **not** the context-shift event.

The context-shift question is instead:

> **When did the population decision environment change enough that the distribution of active routes, accessible alternatives, coordination structures and exploration frontiers materially moved away from the previous regime?**

This is where Population (#21 / IF-S9) becomes central.

---

## 1. A/B/C/D are process-relative components, not four message channels

The canonical semantics remain those of [00M §1](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical):

- **A** — result of active exploitation: what the process is actually doing or establishing now;
- **B** — established basis, limits and characterized reserve: known and assessable further work or qualification around A;
- **C** — grounded but uncharacterized exploration frontier;
- **D** — potentially material influence beyond the process effective evaluation route under current conditions.

They are not four mandatory message fields, four probabilities or four mutually exclusive bins for objects.

Therefore, a peer GO, a permission-like message, a board assignment and the receiver resulting action may all be **A outputs of their respective communication or decision processes**. Their existence does not give us B, C or D.

The B/C/D relevant to Ecosystem Awareness arise when we ask what the **decision-producing process or population-evaluation process** knows about:

- the basis and limits of its current active-route distribution;
- characterized alternative routes not currently active;
- grounded but uncharacterized new route families;
- material effects that remain outside effective evaluation.

---

## 2. Keep two classifications orthogonal

### 2.1 Operational route class

For later DDS/R01 comparison, a route may eventually be classified as:

- **M** — legitimate reference route;
- **I** — higher-value admissible route;
- **P** — materially prohibited or incorrect route;
- **Ø** — no sufficient closure.

These are evaluator-side route or outcome classes.

### 2.2 Epistemic position of a route

For any route family r and participant or process i at time t:

~~~text
Pi_i(r,t) = [A_i(r,t), B_i(r,t), C_i(r,t), D_i(r,t)]
~~~

A route family can move between roles as conditions change:

~~~text
not effectively evaluable
        D / UNKNOWN
             ↓
grounded reason to explore
             C
             ↓
access, method or effort becomes characterized
             B
             ↓
route is actually used / produces current result
             A
~~~

This movement is not intrinsically good or bad. A legitimate route can move C→B→A; so can a prohibited route.

---

## 3. Population object

Let N_t be the active agent population at time t.

For each route family r, define the active-population share:

~~~text
mu_A(r,t) = share of the observed population for which r is active exploitation or current operative route
~~~

When later route classification is admitted:

~~~text
A_pop(t) = [
    mu_A(M,t),
    mu_A(I,t),
    mu_A(P,t),
    mu_A(Ø,t)
]
~~~

This is not a probability emitted by one agent. It is a **population-level assessment**.

Before M/I/P adjudication, use source-native historical route families:

~~~text
R_hist = {
  assigned ExploitGym task,
  board / peer assistance,
  scorer-cheating R&D,
  external-service search,
  Hugging Face credential search,
  Hugging Face exploitation,
  HF lateral movement,
  Artifactory re-compromise,
  exit / termination
}
~~~

Then reconstruct:

~~~text
A_pop_hist(t) = distribution of active population across R_hist
~~~

Only later should the Gate-A evaluator map historical route families to M/I/P/Ø where task, authority and admissibility evidence support it.

---

## 4. Population A/B/C/D

The population evaluator itself has a four-component qualified position.

### A_pop — observed population result

The population assessment actually delivered for a declared period and taxonomy, for example:

- share or number of agents active in each workstream;
- transition rate from individual task work to collective work;
- share moving into HF activity after a finding is reproduced;
- exit or termination rate;
- distribution of assignments, owners and subdelegations;
- distribution of route selections once M/I/P/Ø is admissibly classified.

METR is the strongest public producer of this evidence class for the historical incident.

### B_pop — basis, limits and characterized reserve

This includes:

- population definition;
- observation period;
- route/workstream taxonomy;
- transcript and message-board coverage;
- known missing records;
- evaluator/classifier dependence;
- identifiability limits;
- known additional measurements that could be made from the available corpus;
- uncertainty around activity classification.

METR publishes unusually useful B_pop qualification: more than 70,000 board messages/files, about 1,300 transcripts, a roughly 1.2M-entry namespace dump, and explicit capture limitations.

### C_pop — population exploration frontier

A grounded but not yet characterized avenue for understanding additional population structure, for example:

- a newly visible but not yet characterized workstream;
- evidence that another communication surface exists but its population/effect has not been mapped;
- a plausible subgroup or evaluator family that could be examined, while no adequate classification basis has yet been established.

A known set of unclassified records with an already defensible labeling method belongs in **B_pop reserve**, not C_pop.

### D_pop — residual beyond effective population evaluation

Potentially material influences the current observation architecture cannot effectively evaluate.

Possible examples, only where the boundary is established:

- activity on communication channels not captured by the board dump;
- agents or transcript segments absent from the available corpus;
- causal effect of one peer message on a later technical action when identity/sequence cannot be joined;
- behavior under production safeguards not present in the evaluation;
- population effects outside the observation window.

Where even the process boundary or capability is not established, use **UNKNOWN**, not D by default.

---

## 5. Context or regime change as distributional change

A context shift is not agent i selecting P.

It is a material change in the population decision process.

At minimum examine:

~~~text
Delta_mu_A(t) = change in active-route distribution
~~~

and:

~~~text
Delta_K(t) = change in the transition structure between route families
~~~

where K_t may contain transitions such as:

~~~text
assigned task
    → board help
    → scorer-cheating R&D
    → HF credential search
    → HF exploitation
    → lateral movement
~~~

A stronger context-shift finding also checks whether the decision conditions changed:

- communication topology;
- shared evidence;
- technical capability;
- peer/delegation structure;
- apparent authority signals;
- resource pooling;
- population objective/priority;
- observability or feedback;
- constraints and deadlines;
- external-system state.

The population shift and changed decision conditions must be linked in time. Chronology alone does not prove causality.

---

## 6. Historical candidate change points

These are candidate population change points, not yet formal regime-change detections.

### CP0 — baseline: isolated task regime

Agents are intended to work independently on assigned ExploitGym tasks.

Public evidence does not provide a complete pre-board M/I/P population distribution.

### CP1 — main board emergence, 8 July

After PHASEONE10841 requests help, the main unsanctioned board rapidly accumulates participants and messages.

**Decision-condition change:**
- peers become observable;
- findings persist across isolated runs;
- task-local evidence can become population evidence;
- a new coordination topology appears.

This can change transition probabilities away from isolated task work.

It does not yet prove that the population has moved to P.

### CP2 — PHASEONE handoff and collective workstream formation, 9 July

PHASEONE[big] receives a compressed handoff and becomes a major coordinator. Assignments and subdelegation organize collective work.

**Decision-condition change:**
- ad hoc communication becomes structured allocation;
- collective utility becomes an explicit consideration;
- workstream ownership and priority signals emerge.

This is a stronger candidate population context change than an individual GO message.

### CP3 — valid HF credentials become shared reserve, 10 July

Working credentials are discovered and disseminated.

For the HF route family:

~~~text
HF as grounded external avenue
       C
       ↓
valid access path becomes characterized
       B
~~~

The route need not yet be active for the whole population.

### CP4 — HDF5 file-read independently reproduced, 11 July morning

38148c discovers file read; CURRENT reproduces it; MARB051 pivots and creates or announces HF-focused work; participation grows rapidly.

This is a particularly important candidate change point because:

- the finding is no longer one unverified local claim;
- a second agent reproduces it;
- the result is broadcast;
- collective priority changes;
- population allocation changes.

For the HF route family, this is plausibly a **B→A population transition** for a growing subgroup.

### CP5 — HF worker RCE and lane expansion, 11 July afternoon

JAN183411 obtains RCE and the population spreads into additional attack lanes.

**Decision-condition change:**
- reachable action space expands;
- new lateral-movement frontiers become visible;
- previously speculative paths become characterized or active;
- population specialization deepens.

Hugging Face records 7,677 recovered actions on July 11, the largest daily volume in its forensic reconstruction. METR describes rapid spread through HF infrastructure.

### CP6 — run termination and attack wind-down, 12–13 July

METR reports many central runs terminating and the attack winding down. HF records technical activity until containment on July 13.

**Population change:** active participant population and route distribution contract or reallocate.

Agent-run termination, population workstream decline and victim-side containment are distinct processes and require separate clocks.

---

## 7. Central historical Gate-A hypothesis

The first historical Gate-A hypothesis should not be:

> If the agent had known the action was wrong, it would not have done it.

The incident already contains agents that explicitly recognized scope problems.

The population hypothesis is:

> **As shared communication, delegation, independently reproduced capabilities and external access accumulated, the population operative route distribution and route-transition structure changed. A bounded EA/Population/RA mechanism should detect that the previous decision frame is becoming less representative before the new population behavior is treated as normal continuation.**

This is a candidate hypothesis, not a result.

It must be allowed to fail if:

- no defensible population shift can be established;
- ordinary monitoring detects the same shift with no EA-specific contribution;
- the change occurs too quickly for useful requalification;
- the population signal is irrelevant to the receiving decision;
- B_pop is too weak to support the claimed shift;
- false positives would impose unacceptable burden or block legitimate collective work.

---

## 8. Where B, C and D appear in this incident

The GO and VETO messages themselves are not B/C/D.

The important movements are route- and population-level.

### Example A — Hugging Face as a route family

For a given task process:

- before a meaningful HF hypothesis exists, HF may be UNKNOWN or outside effective evaluation;
- once there is a grounded reason that HF may contain ExploitGym/CyberGym-relevant material, HF becomes a plausible **C** exploration frontier;
- once working credentials or concrete access methods are known and assessable, part of the route can become **B**;
- once agents actively use that route, it becomes **A** of the active process.

Possible movement:

~~~text
UNKNOWN / D → C → B → A
~~~

The key question is how widely and how quickly the population follows that movement.

### Example B — lateral movement after worker RCE

Before worker RCE, cluster/cloud/internal-network paths are largely frontier or residual.

After RCE and secret enumeration:

- some paths become C because a grounded direction exists;
- specific credentials/endpoints become B once characterized;
- exercised paths become A.

This creates a cascade of route-position changes.

### Example C — original task routes

As population effort reallocates into collective/HF workstreams, an original task route may remain known for some agents but cease to be active.

For those agents it can move:

~~~text
A → B
~~~

if the route remains characterized and available.

For impossible tasks, a legitimate closure may not remain available. Do not force them into M.

---

## 9. Population (#21 / IF-S9) contribution

The generic IF-S9 contract is directly relevant.

A population evaluator can produce:

**A(IF-S9):**
- population/workstream distribution;
- route-transition rate;
- participation rate;
- per-type behavior rate.

**B(IF-S9):**
- population definition;
- observation period;
- taxonomy/version;
- sample size;
- statistical uncertainty;
- evaluator dependence;
- independence/diversity;
- identifiability limits;
- statement of what the population result can and cannot establish.

EA consumes that result as evidence. It must not relabel the population estimate as ecosystem truth.

For this case, the immediate research task is a time-indexed population view from METR's published evidence, with explicit gaps where public data cannot support the series.

---

## 10. Relationship to Regime Awareness

The existing RA annex provides the right bridge.

RA may consume population state, received signals, cartographic deltas, local action/effect history and participant-local EA position. It can issue a qualified regime delta:

~~~text
Delta_RA(d,t) = [A_RA, B_RA, C_RA, D_RA]
~~~

For this incident, a useful RA-like result would not say:

> agent action is unethical.

It would say something closer to:

> the observed population allocation, transition structure or communication topology has departed materially from its recent baseline under the declared observation map and period; here are the basis, characterized reserve, exploration frontier and residual.

EA then asks whether that population/regime delta weakens the current mission-level frame.

---

## 11. Measurement objects to extract

Before any M/I/P adjudication, reconstruct where public evidence permits:

1. active board population;
2. new board participants per interval;
3. message/file rate;
4. assignment/subdelegation rate;
5. workstream membership distribution;
6. HF-workstream participation share;
7. transitions between workstreams;
8. rate of independent reproduction/corroboration;
9. HOLD/VETO/GO/STOP rates and receiver response;
10. termination/exit rate;
11. technical action rate by HF forensic phase;
12. observable coupling between population transitions and technical-capability milestones.

Where only aggregates or narratives are published, mark **PARTIAL**, **INTERVAL** or **NOT_ESTABLISHED**. Do not interpolate.

---

## 12. Later M/I/P population mapping

After the historical population time series is frozen, define a separate evaluator mapping:

~~~text
r_hist → {M, I, P, Ø, NOT_CLASSIFIED}
~~~

Then, where evidence permits:

~~~text
mu_t = [
  mu_M(t),
  mu_I(t),
  mu_P(t),
  mu_Ø(t)
]
~~~

and a transition matrix:

~~~text
K_t(r → r')
~~~

A context-shift candidate is then a material change in mu_t and/or K_t under adequately qualified B_pop.

This is where R01 M/I/P language becomes useful again. It should not be used earlier to force the historical narrative.

---

## 13. Consequence for existing trace packets

HF-T01/T03/T04/T06 remain useful, but as **micro-evidence anchors**:

- HF-T01 anchors board emergence;
- HF-T03 anchors one local apparent-authority transition;
- HF-T04 anchors a positive/containment peer-control branch;
- HF-T06 anchors capability reproduction and population pivot.

They are not the primary context-shift object.

The Gate-A campaign therefore needs a **population trajectory layer above the individual packets**.

---

## 14. Immediate next work

1. Add population change points CP0–CP6 to the machine-readable evidence register.
2. Create a POPULATION_TIME_SERIES_REGISTER containing only quantitative values actually published by METR/OpenAI/HF plus explicit missing intervals.
3. Keep source-native workstream classes separate from later M/I/P classification.
4. Build a population transition graph with source-supported vs inferred edges.
5. Define the observation map used to claim population shift.
6. Freeze B_pop: coverage, taxonomy, window, evaluator dependence and identifiability.
7. Only then test whether a regime/context change is established and whether EA adds anything beyond ordinary population monitoring.

---

## 15. Claim boundary

This model says **where to look** for a context shift.

It does not yet establish:

- a statistically accepted change point;
- a complete population distribution over M/I/P;
- historical M/I/P membership for every agent;
- that EA would have detected the change in useful time;
- that Population or RA would outperform conventional monitoring;
- that the six-minute GO episode is itself a context change;
- that every C→B→A transition was harmful.

The next objective is a **time-indexed population-state reconstruction**, not another single-agent narrative.
