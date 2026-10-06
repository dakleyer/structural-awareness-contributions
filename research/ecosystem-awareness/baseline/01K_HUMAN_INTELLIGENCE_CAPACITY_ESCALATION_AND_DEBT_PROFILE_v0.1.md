# Annex 01K — Human Capacity / Human Intelligence Debt

**Status:** additive public working extension, v0.2, 6 October 2026. This is an **Ecosystem Positioning-related Human Capacity / Human Intelligence Debt extension hosted in the EA folder for lineage and routing**. It remains outside the EA core, outside the controlled/frozen EA baseline and outside the semantic ownership of Ecosystem Signalling, Regime Awareness, MSCA or Repositioning. It does not define a universal cognitive metric, a staffing standard, a mandatory human-in-the-loop architecture, an ITU-T deliverable or an adopted FG-TIDA requirement.

**Source-of-truth boundary:** this annex does not invent a second Human Intelligence Debt theory. It imports the Human Intelligence Debt / Human Intelligence Gap research line published by Tegrity.AI and The Integral Management Society, then exposes bounded interfaces by which Ecosystem Positioning, Human Escalation, Signalling/EHD, MSCA Operation/Repositioning and organisational architecture work may consume that research without changing its claim status.

**Primary research index:** https://tegrity.ai/series/human-intelligence-gap/  
**Structural Awareness synthesis/index:** https://tegrity.ai/structural-awareness-program/

---

## 1. Purpose

The extension answers two different questions that must not be collapsed.

### A. Runtime Human Capacity

> **Can a qualified and legitimately authorised human path intervene now, with enough information and time to affect the decision before the useful response window closes?**

This is an operational capacity question.

### B. Human Intelligence Debt

> **Is the socio-technical architecture designed so that scarce human cognition is used for genuine contribution and necessary oversight, or is it structurally consuming that cognition as compensatory middleware for work the available technological and architectural frontier could remove?**

This is an architectural and organisational question.

A reviewer may be AVAILABLE at runtime while the surrounding architecture is generating high Human Intelligence Debt.

Conversely, an architecture may be designed to reserve people for genuinely human contribution while a particular incident finds the relevant reviewer temporarily UNAVAILABLE.

The two questions therefore belong in one extension because they concern the same scarce human capacity, but they retain different units, evidence and decision semantics.

---

## 2. Component contract

01K is best read as one **Human Capacity / Human Intelligence Debt** extension with four surfaces:

~~~text
HumanCapacityHID_i(t) = [
  RuntimeHumanCapacity_i(W),
  HIDArchitectureProfile_i(P),
  HIDMeasurementProfile_i(P),
  HIDBridgeContext_i(P)
]
~~~

where:

- **RuntimeHumanCapacity_i(W)** — bounded operational availability for a particular intervention window W;
- **HIDArchitectureProfile_i(P)** — architecture-level reading for a declared process/capability/portfolio P;
- **HIDMeasurementProfile_i(P)** — optional organisational metrics and evidence state;
- **HIDBridgeContext_i(P)** — optional links to Cost of Clarity, Attribution Gap, Informational Friction, AI Operational Integrity Architecture, AI Integrity Management and Regime Awareness where those relations are material.

None of these four surfaces is mandatory for every implementation.

A small Human Escalation implementation may consume only RuntimeHumanCapacity.

An enterprise architecture or transformation programme may consume the HID architecture and measurement surfaces without using Human Escalation at all.

An organisation may use the complete set.

**UNKNOWN / NOT MEASURED must remain valid states.** Absence of a metric does not authorise the system to invent one.

---

# Part I — Human Intelligence Debt as architectural debt

## 3. Canonical Human Intelligence Debt definition

The foundational source is:

**Human Intelligence Debt: A Socio-Technical Metric for Measuring the Human Cost of Imperfect Data Flows**  
https://tegrity.ai/human-intelligence-debt/

The source asks how much human cognition remains trapped in work that the best available socio-technical capabilities of a technological period could absorb, rather than being used to create genuinely new information, judgement, design, interpretation, care, strategy or other irreducibly human contribution.

The original conceptual quantities are:

~~~text
HICT_t = Human Intelligence Contribution Target
HICR   = Human Intelligence Contribution Ratio

HID_t = HICT_t - HICR
~~~

In the founding formulation:

- **HICT_t** is the period-relative target implied by the technological and architectural frontier;
- **HICR** is the contribution actually realised in the current organisational state;
- **HID_t** is the gap.

The construct is architectural and socio-technical. It is not a moral judgement on employees and it is not a claim that a person is a replaceable unit.

The source explicitly identifies debt-producing conditions such as:

- duplicated data and fragmented systems;
- weak lineage and unclear ownership;
- manual reconciliation across disconnected sources;
- shadow processes and parallel spreadsheets;
- artificial exceptions that could be handled systematically;
- institutional friction;
- poor capture, integration or governance design;
- process fragmentation between organisational units.

The foundational enterprise-architecture implication is direct: measure the share of human effort absorbed by mechanisable work and ask which activities exist only because systems, ownership, information and processes do not compose coherently.

## 4. Period-relative data and genuine information

The founding paper uses a technological-period definition that is important for 01K.

**Data** is not limited to database fields. It includes any representation, content, signal, record, document or output that can be captured, transformed, consolidated, inferred, generated or reused by the best available socio-technical capabilities of the period.

**Genuine information contribution** begins where that transformation is no longer mechanically obtainable under the declared period, evidence and quality/risk conditions.

That makes HID dynamic in principle: as the feasible technological frontier moves, the target HICT can move.

This does **not** mean that every task that a model can imitate is automatically debt. The measurement programme requires an explicit replaceability/counterfactual test rather than a speculative automation claim.

## 5. Ideal-state language and the later measurement correction

Paper 1 describes an **Ideal Operational Intelligence Environment / State** in which capture, transformation, process, governance and institutional conditions are coherent enough that humans touch the information flow primarily for genuine contribution, meaningful exceptions and judgement.

Paper 5 later makes the counterfactual more operational and more defensible:

**Measuring Human Intelligence Debt**  
https://tegrity.ai/meassuring-human-intelligence-debt/

Instead of relying only on an imagined ideal, the measurement programme grades replaceability evidence:

- **Tier 1** — the activity is already automated in a demonstrable benchmark organisation or shipping product;
- **Tier 2** — a working prototype establishes feasibility;
- **Tier 3** — expert attestation naming the technology, with lower confidence.

01K therefore preserves the conceptual HICT/HICR framework while preferring observed or graded counterfactual evidence wherever an organisation attempts to measure debt.

## 6. Task-level operationalisation — GIC / NEO / ACW

Paper 5 supersedes role-level classification for measurement with task-time classification because one role can mix genuine and mechanisable work.

The task-level taxonomy is:

- **GIC — Genuine Information Contribution:** work that creates genuinely new information, judgement or capability not mechanically obtainable under the declared frontier;
- **NEO — Necessary Execution & Oversight:** human work that remains structurally necessary even in a coherent architecture;
- **ACW — Avoidable Compensatory Work:** human work created by avoidable architectural fragmentation, mediation or poor integration.

ACW is the observed debt surface.

Paper 5 also uses modifiers/tags rather than double-counting them as separate debt categories:

- **ACW–AOV** — avoidable AI-output validation/reconciliation;
- **ACW–WFR** — waiting, failure or rework;
- **ACW–TTC** — transitional compensatory work carrying a declared exit path/date.

A necessary human review is therefore not debt merely because a person performs it.

A repeated approval, reconciliation, re-entry, translation or cross-tool comparison can be debt even when the person has abundant time and the queue is empty.

This distinction is the core reason 01K belongs beside Human Escalation.

## 7. The canonical metric family

Where an organisation has passed the required measurement gate, the current measurement paper defines:

~~~text
HICR_time
=
H_GIC / H_total

HID_observed
=
H_ACW / H_total

HICT
=
HICR + H_releasable / H_total

F-HICT
=
HICR + rho_inf * (H_releasable / H_total)

HID_spent
=
(1 - rho_inf) * (H_releasable / H_total)

NOI
=
H_added - H_removed
~~~

Interpretation:

- **HICR_time** — observed share of cognitive work used for genuine contribution;
- **HID_observed** — observed share used for avoidable compensatory work;
- **H_releasable** — human capacity the architecture could release under the bounded counterfactual;
- **F-HICT** — feasible recovered contribution after applying the recovery coefficient;
- **HID_spent** — the portion of releasable capacity that does not return as genuine contribution under the recovery model;
- **NOI — Net Oversight Impact** — human work added by an oversight design minus human work removed by it.

These are not universal constants. Their evidential status depends on the measurement protocol below.

---

# Part II — Why the debt appears and persists

## 8. Paper 2 — capability fragmentation / Harvester Multiplication

**The Harvester Multiplication Problem: Capability Fragmentation, Governance Collapse and the Compounding of Human Intelligence Debt**  
https://tegrity.ai/the-harvester-multiplication-problem-capability-fragmentation-governance-collapse-and-the-compounding-of-human-intelligence-debt/

Paper 2 identifies a mechanism: multiple partially overlapping capabilities can create an interaction layer of reconciliation, coordination and governance work that did not exist in the underlying business outcome.

The relevant object is **not raw application count**.

The series explicitly distinguishes:

- justified multiplicity for resilience, regulation, regional autonomy or specialised function;
- incoherent capability multiplicity that creates human coordination work.

The measurement programme therefore uses:

- **Effective Application Count** — usage/workload-weighted application count rather than a flat count;
- **Functional Redundancy Index**;
- **Justified Multiplicity Ratio**.

A debt signal is not “many applications.” It is the combination of high effective multiplicity, high functional redundancy, low justified multiplicity and compensatory human work.

Paper 2 also identifies a governance cascade associated with fragmented capability coverage:

- ownership contestation;
- lineage opacity;
- loss of a single authoritative version;
- PII/data dispersion;
- more cross-system security surfaces;
- model/data quality problems when AI consumes inconsistent estate state;
- integration backlogs and migration adapters that can preserve rather than remove fragmentation.

For 01K, these are **architectural debt mechanisms and diagnostic context**, not automatic HID measurements.

## 9. Paper 3 — the incentive structure / HID Dilemma

**The Human Intelligence Debt Dilemma: A Game-Theoretic Account of Why Rational Agents Build Irrational Architectures**  
https://tegrity.ai/the-human-intelligence-debt-dilemma-a-game-theoretic-account-of-why-rational-agents-build-irrational-architectures/

Paper 3 asks why the fragmentation persists even when competent actors can see its cost.

Its proposed model is deliberately labelled **game-theoretic and not yet empirically established**.

The core asymmetry is:

~~~text
adding a capability
= fast visible value + lower personal risk

removing a capability
= slower + politically/technically costly + higher personal risk

architectural coherence
= distributed long-term benefit + diffuse credit
~~~

The paper shows how both productive and blocking behaviour can rationally reproduce the same systemic result.

For 01K this becomes an important organisational extension:

> HID is not only a technical-integration problem. It can be maintained by incentives that make local optimisation rational while architectural coherence remains under-rewarded.

An organisation measuring HID should therefore avoid treating ACW only as a worker-productivity problem. The architecture, ownership, decommission authority, incentives and credit structure may be the producing mechanism.

## 10. Paper 4 — Architectural Entropy and partial irreversibility

**Architectural Entropy: How Mediated Systems Spend Human “Exergy” and the Partial Irreversibility of Human Intelligence Debt**  
https://tegrity.ai/architectural-entropy-how-mediated-systems-spend-human-exergy-and-the-partial-irreversibility-of-human-intelligence-debt/

Paper 4 extends the debt from allocation to path dependence.

Its working hypothesis is that long-lived mediated architectures can do more than temporarily misallocate human capability: if higher-order capabilities go unexercised, some released time may not convert automatically back into genuine contribution.

This gives the recovery coefficient used in Paper 5:

~~~text
rho_inf
=
fraction of released capacity that ultimately converts
into genuine contribution under the declared recovery intervention
~~~

The important distinction is:

- **recoverable debt** — capacity that can be released and returned to genuine contribution;
- **spent / structural remainder** — capacity that does not automatically return.

The source is explicit that partial irreversibility is a hypothesis to be tested, not an established empirical law.

01K therefore MUST NOT infer `rho < 1` merely because an organisation is fragmented.

---

# Part III — Organisational measurement extension

## 11. Three-layer measurement architecture

01K may expose the Human Intelligence Debt measurement programme as an **optional organisational profile**.

It should not force every agent or Human Escalation path to calculate enterprise metrics.

The programme separates three layers.

### 11.1 External/context indicators

These help establish environment and candidate architectural disorder.

#### Indicator 1 — market supply per capability

Context only.

It may show that the solution frontier and consolidation options have changed, but it does not establish what one organisation deploys.

#### Indicator 2 — capability multiplicity and redundancy

Core external/portfolio indicators:

~~~text
Effective Application Count
Functional Redundancy Index
Justified Multiplicity Ratio
~~~

These should be read together, not independently.

#### Indicator 3 — portfolio answerability and retrieval cost

The measurement paper identifies this as the strongest and most exposed indicator.

A fixed discovery checklist asks whether the organisation can reproducibly establish, from governed sources, facts such as:

- bounded cost;
- owner with decommission authority;
- deployment/age information;
- licence/commercial information;
- dependencies and lineage where required.

Candidate measures include:

- **Portfolio Answerability Index** — completeness/provenance/freshness/consistency with retrieval-effort penalty;
- **Time-to-Answer**;
- fraction answerable directly;
- fraction reconstructable only through archaeology;
- fraction unobtainable.

**Deficit is not decay.** Poor answerability now does not prove that answerability has deteriorated over time.

### 11.2 Internal task-level measurement stack

Paper 5 proposes five complementary instruments.

#### Task ledger

- time-stamped work sampling;
- person-minutes / cognitive hours per task episode;
- one fixed capability taxonomy defined in advance.

#### Two-axis classification

Classify task episodes into GIC / NEO / ACW with modifiers.

#### Objective tracers

Digital exhaust can provide a conservative floor for ACW through:

- human re-entry between systems;
- context-switch counts;
- reconciliation loops such as A→B→A;
- manual touches between automated steps;
- export / manipulate / re-import patterns.

Telemetry is evidence, not ground truth.

#### Replaceability audit

Use Tier 1 / Tier 2 / Tier 3 evidence described above.

#### Capability probes

Candidate probes include:

- degraded-mode drills where safe;
- real outage logs where drills would be unsafe;
- novel-exception performance;
- cross-context transfer;
- recovery performance after compensatory work is removed.

Cognitive load may be observed, including load on GIC, but **cognitive load is not itself the debt classifier**.

### 11.3 Dynamic / velocity measures

Paper 5 distinguishes three ways of studying temporal movement.

- **M1 — repeated snapshots**;
- **M2 — vintage gradient**;
- **M3 — flow / derivative read**.

The M3 working quantities are:

~~~text
order_destruction_rate
=
undocumented changes
+ new shadow assets
+ sole-owner departures
+ records going stale
per unit time

order_creation_rate
=
assets onboarded to the model
+ records verified
+ assets decommissioned
+ handovers documented
per unit time

entropy_production
proportional to
order_destruction_rate - order_creation_rate

fidelity_half_life
approximately
ln(2) / verification_decay_rate
~~~

These are measurement proposals / correspondence instruments, not a declaration that organisational systems literally obey thermodynamic laws.

M3 can indicate current direction. It does not by itself establish a multi-year historical decay curve.

## 12. Evidence Notes discipline

**Evidence Notes for Human Intelligence Debt Proposed Study**  
https://tegrity.ai/evidence-notes-for-human-intelligence-debt-propossed-study/

The companion evidence note separates:

1. public evidence;
2. what that evidence licenses one to claim;
3. execution-layer measurement inside an organisation.

It also tags external evidence by source quality/bias, including:

- confirmed;
- vendor;
- consortium;
- academic;
- secondary;
- needs-primary;
- folklore;
- firewalled;
- forecast.

01K adopts the same discipline.

Public benchmarks can motivate an assessment or populate B-level context, but they MUST NOT be silently promoted into a measured HID value for a specific organisation.

Incompatible panels should not be averaged merely because they point in the same direction.

## 13. Instrument-validation and study gates

The measurement programme is explicit that no empirical HID value should be published before Study 0 passes.

### Study 0 — instrument validation

- roughly 300 task episodes;
- at least three independent assessors;
- two-axis task protocol;
- Krippendorff’s alpha;
- required alpha >= 0.80 before substantive HID measurement;
- concordance check between human labels and objective tracers.

### Study 1 — baseline + benchmark pair

Compare fragmented and coherent sites/capabilities with the same task family.

### Study 2 — intervention / recovery experiment

Compare:

- architecture-only removal of ACW;
- architecture fix plus deliberate capability rebuilding / “exergy injection”.

Primary endpoint: recovery coefficient rho.

### Study 3 — hysteresis / history dependence

Tests whether recovery depends on mediation history and whether equal present architectures can carry different capability states because of path dependence.

### Study 4 — oversight threshold

For AI-enabled processes:

~~~text
NOI = H_added - H_removed
~~~

Test the predicted threshold/U-shaped relation between oversight/guardrail coupling and Human Intelligence Debt.

### Study 5 — sector replication

Repeat across sectors to test generality.

Until those gates are passed, 01K may carry **research constructs, proxies and hypotheses** but not an invented organisational HID score.

---

# Part IV — Runtime Human Capacity

## 14. Runtime Human Capacity is not HID

Human Escalation needs an operational capacity check that is intentionally separate from the HID metric family.

For reviewer/reviewer-pool J and response window W:

~~~text
RuntimeHumanCapacity_J(W) = [
  route_reachable,
  qualified_reviewer_available,
  competence_case_fit,
  authority,
  information_sufficiency,
  queue_or_committed_work,
  expected_ack_latency,
  expected_decision_latency,
  fallback_or_backup,
  response_horizon
]
~~~

A compact state may be:

~~~text
HumanCapacityState
∈ {
  AVAILABLE,
  DEGRADED,
  UNAVAILABLE,
  UNKNOWN
}
~~~

UNKNOWN must not silently become AVAILABLE.

This surface answers:

> **Can this human path meaningfully intervene now?**

It does not answer:

> **Is the architecture using human intelligence well?**

## 15. Two-gate rule for Human Escalation

A Human Escalation design may therefore be assessed against two independent gates.

### Gate A — runtime viability

~~~text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND expected latency fits W
~~~

### Gate B — architectural intelligence use

~~~text
HumanIntelligenceArchitectureFit_i
=
human interaction is primarily
GIC or necessary NEO

AND NOT predominantly
ACW generated by avoidable architecture
~~~

Passing Gate A does not imply passing Gate B.

A person may be perfectly available to answer low-value questions that the system should never have designed itself to ask.

That is precisely why HID belongs upstream of a mature Human Escalation interface.

## 16. Human Intelligence Tokens are not canonical HID units

01K does not use Human Intelligence Tokens as the canonical measurement unit.

Paper 5 already has a stronger measurement vocabulary: cognitive hours, GIC/NEO/ACW, releasable capacity, HICR/HICT, recovery coefficient and NOI.

An implementation may use local workload points for queue scheduling if useful, but a local point system MUST NOT be presented as:

- a universal unit of human intelligence;
- a measure of human worth;
- a substitute for HICR/HICT;
- a Human Intelligence Debt value;
- evidence that high cognitive load equals high genuine contribution.

---

# Part V — Interfaces with Ecosystem Positioning

## 17. Human Escalation as an existing consumer/producer

Human Escalation is not inserted as a new core EA function.

A Human Escalation path may:

- consume a qualified alert, objection, `RepositionIntent`, requalification request or other bounded signal;
- consume EHD-carried context required for meaningful review;
- consume RuntimeHumanCapacity;
- optionally consume an HID architecture/profile reference where the design question is material;
- produce acknowledgement, evidence, decision, refusal, request-for-evidence, escalation or no-valid-response;
- return its result through existing Signalling / AuthorityResponse / requalification paths.

A successful route-to-human event is not equivalent to a successful human intervention.

A successful human intervention is not evidence that the surrounding interface is debt-neutral.

## 18. Human / Systemic Alert remains a Signalling profile

A **Human / Systemic Alert** remains a bounded profile over [01J Ecosystem Signalling](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) and the [EHD general interface](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md).

It is not a fifth primitive signal class and not a command.

Candidate triggers include:

1. human-originated objection/anomaly;
2. agent/system alert;
3. material Regime Awareness output/requalification request;
4. condition discovered during Repositioning;
5. runtime Human Capacity degradation/unavailability/unknown;
6. optional architecture-governance trigger where a measured/qualified HID pattern makes the escalation interface itself a review target.

The receiver still performs normal qualification.

Where material:

~~~text
trigger
-> bounded signal / EHD
-> receiver qualification
-> Cart_i update
-> RA/local requalification where needed
-> Repositioning or other legitimate consumer
~~~

No Human Intelligence Debt measure becomes a privileged interrupt.

## 19. Human consumer / subscription semantics

A human may be a receiver where an ACC, policy or signalling profile routes a class of signal to that human/role.

A deployment may implement:

- subscription;
- notification;
- queue membership;
- named-owner routing;
- role-based routing.

Subscription means routing, not authority.

Notification means delivery, not capacity.

Silence does not imply approval unless an externally legitimate rule says so.

A human is one possible receiver in the signalling topology, not a super-controller over Awareness or Repositioning.

## 20. Repositioning-time use

Repositioning may consume RuntimeHumanCapacity for a transition that materially depends on human review.

Separately, an architectural review may consume the HID profile to ask whether the repeated escalation pattern itself is debt-producing.

If a candidate transition requires a successor ACC, new authority or re-contracting:

~~~text
HOLD / UNRESOLVED
~~~

may remain the correct bounded state.

A human/systemic alert cannot manufacture the missing ACC, authority or capacity.

---

# Part VI — Cross-series bridges

## 21. Bridge to The Cost of Clarity

**What Goes Unpriced Is Paid in Human Intelligence**  
https://tegrity.ai/what-goes-unpriced-is-paid-in-human-intelligence/

This bridge connects information cost to human-intelligence allocation.

The Cost of Clarity asks what it costs and risks to produce the information a transformation needs.

Human Intelligence Debt asks what scarce capacity ultimately pays that bill when clarity is not architected into the system.

The bridge identifies two faces of the same scarcity:

- human intelligence consumed as middleware / reconciliation;
- missing frame-defining architectural decisions because that same intelligence is consumed elsewhere.

It also identifies a structural **knowledge-authority split**: operational knowledge may sit where decision rights do not, while decision rights may sit where operational context does not.

01K therefore treats **Cost of Clarity** as a useful upstream organisational diagnostic, not as an HID formula.

Where an escalation or transformation repeatedly requires ad hoc context reconstruction, 01K may reference a Cost-of-Clarity assessment for the information-acquisition burden, while HID measures the resulting human-intelligence misallocation.

## 22. Bridge to The Attribution Gap

**Bridge: The Attribution Gap and Capability Loss**  
https://tegrity.ai/bridge-the-attribution-gap-and-capability-loss/

The two theories were developed independently and must keep their formal machinery separate.

The bridge observes convergence:

- HID asks why automatable human work persists and why governance decision capacity is structurally scarce;
- Attribution Gap asks why the contribution a capability makes can diverge from the formal credit/visibility it receives, causing firms to remove capabilities they actually depend on.

For 01K this matters because low attribution can hide the very expert/capability contribution whose disappearance later produces compensatory work.

But attribution metrics are **not** HID metrics.

Convergence is a useful cross-check, not proof of either theory.

## 23. Bridge to Informational Friction

**The Map and the Flow**  
https://tegrity.ai/the-map-and-the-flow/

Informational Friction re-derives the programme's underlying object without requiring human agents.

It distinguishes:

- the real operational flow;
- the representation/map used as a control surface;
- the gap between them;
- the friction produced when action based on a divergent map deforms the real flow.

This provides a systems-theory neighbour for HID:

~~~text
map/flow divergence
-> compensatory mediation / reconciliation
-> human ACW
-> HID surface
~~~

But the formal languages should not be silently merged.

In particular, Informational Friction explicitly avoids requiring a perfect third “ideal” object, whereas the original HICT definition is a period-relative counterfactual target. Paper 5 reduces that tension operationally by using graded, observed counterfactual evidence.

01K may reference the relationship while preserving each source's own semantics.

## 24. Bridge to AI Operational Integrity Architecture

**The Limits of AI Oversight**  
https://tegrity.ai/the-limits-of-ai-oversight/

This is the direct bridge from AI oversight architecture to HID.

Its central prediction is conditional:

- guardrails can remove human work;
- guardrails also create residual validation, reconciliation, exception handling and governance work;
- beyond a coupling/exception threshold, added oversight can create more human work than it removes.

The bridge introduces the **AI Exhaustion Threshold** and motivates **NOI**:

~~~text
NOI = H_added - H_removed
~~~

For 01K this is directly relevant to Human Escalation.

Adding more reviewers, more approval steps or more guardrails is not automatically an improvement.

The interface should ask whether the oversight envelope is releasing human cognition or merely moving residual uncertainty into a human queue.

## 25. Bridge to AI Integrity Management

**What Cannot Be Recovered Must Be Managed**  
https://tegrity.ai/what-cannot-be-recovered-must-be-managed-cross-series-bridge-human-intelligence-gap-with-ai-integrity-management/

This bridge consumes the Paper 4/Paper 5 hypothesis that recovery may be incomplete.

If `rho < 1`, a structural remainder persists.

The bridge reframes that remainder as a standing risk position rather than a cleanup backlog that management should pretend can always reach zero.

It separates:

- **flow** — what capacity/answerability is being spent now;
- **stock/exposure** — what has already become difficult or impossible to recover;
- **fragility** — whether an initiative or capability can actually translate intent into coordinated movement;
- **propagation** — whether its value/risk cascades through the wider system;
- **selection** — concentrate intervention where it changes the most systemic risk/value per unit cost.

This is a proposed management posture, not a validated universal method.

01K may therefore expose a **managed-HID-remnant reference** for AI Integrity Management, but it MUST preserve the empirical uncertainty around rho and the actual size of the remnant.

## 26. Bridge to Regime Awareness

Human Intelligence Debt is not a Regime Awareness output.

Regime Awareness does not calculate HICR/HICT or HID.

The relation is operational:

- debt-producing architecture can change available human response capacity, answerability and dependency fragility;
- a material regime change can alter which human capabilities, information and authority remain relevant;
- a material RA output may trigger a human/systemic alert or repositioning;
- the HID/AI Integrity Management bridge uses regime-aware direction as one possible input to deciding whether a managed exposure is weakening or approaching a critical transition.

The current general interface remains [01C EA ↔ Regime Awareness](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md).

The broader research bridge is also discussed in:
https://tegrity.ai/structural-awareness-foundation-validation/

No cross-series reference transfers proof from one research line into another.

---

# Part VII — Organisational profile

## 27. Optional organisational HID profile

Where an organisation chooses to use the measurement extension, 01K may expose a profile such as:

~~~text
HIDArchitectureProfile(P,t) = [
  scope_capability_or_process,
  technological_period,
  HICR_time,
  HID_observed,
  HICT,
  F_HICT,
  HID_spent,
  NOI,
  effective_application_count,
  functional_redundancy_index,
  justified_multiplicity_ratio,
  portfolio_answerability_index,
  time_to_answer,
  ACW_tags,
  order_destruction_rate,
  order_creation_rate,
  fidelity_half_life,
  evidence_state,
  provenance,
  measurement_window,
  revalidation_conditions
]
~~~

Every field is optional unless a consuming contract explicitly requires it.

Unmeasured fields remain UNKNOWN / NOT MEASURED.

A profile with only qualitative diagnostics is valid.

A numerical profile is valid only to the extent that its instruments and evidence gates support those numbers.

## 28. Candidate organisational dashboard — not a universal standard

For enterprise architecture / transformation use, useful views can include:

| View | Candidate measures | What it asks |
|---|---|---|
| **Human contribution** | HICR_time, HID_observed | Where is human cognitive time going now? |
| **Recoverability** | H_releasable, F-HICT, HID_spent, rho | If ACW is removed, how much genuine contribution returns? |
| **Architecture** | Effective Application Count, Functional Redundancy Index, Justified Multiplicity Ratio | Is capability multiplicity creating coordination work? |
| **Answerability** | Portfolio Answerability Index, Time-to-Answer | Can the organisation answer the governance questions needed to change the estate? |
| **Task mechanics** | GIC / NEO / ACW, re-entry, context-switches, reconciliation loops, export/re-import | Which work is genuine, necessary or compensatory? |
| **Oversight** | NOI, queue/review latency, repeated review, escalation rate | Is safety/governance removing work or creating a new human burden? |
| **Velocity** | order creation/destruction, fidelity half-life | Is architecturability improving or deteriorating now? |
| **Runtime capacity** | AVAILABLE / DEGRADED / UNAVAILABLE / UNKNOWN | Can a particular human path act in time? |

This dashboard is an integration profile, not a claim that all metrics are already empirically validated.

## 29. Architectural design review questions

Before approving a Human Escalation or human-review interface, an architecture review can ask:

1. Is the human being asked to create GIC, perform necessary NEO, or compensate for ACW?
2. Could the same information be captured once and reused instead of re-entered/reconciled?
3. Is the reviewer seeing raw ambiguity that upstream architecture could resolve mechanically?
4. Are multiple tools/agents producing overlapping outputs that a person must reconcile?
5. Is the human being used as an authority owner, an information producer, a validator, or merely a transport adapter?
6. Does the interface preserve the distinction between knowledge and authority?
7. Does adding this guardrail remove more human work than it creates?
8. Is the human queue a temporary transition with an exit condition, or a permanent architecture?
9. If ACW is removed, is there a deliberate path for released capability to return to genuine contribution?
10. Is the organisation measuring a present deficit, or making an unsupported claim about historical decay?
11. Are external benchmark figures being used only as context, with selection bias visible?
12. Is a supposed “AI productivity gain” simply moving reconciliation and validation cost elsewhere?
13. If the new architecture is not fully recoverable, who owns the managed remainder and its risk?
14. What evidence would falsify the claimed HID improvement?

---

# Part VIII — Validation, evidence and falsification boundary

## 30. Claim-status register

01K MUST preserve these limits from the source series.

**Established by definition / current framework:**

- HICT/HICR/HID conceptual relation;
- GIC/NEO/ACW operational taxonomy in Paper 5;
- metric and experimental definitions as proposals;
- runtime capacity and HID are distinct concepts.

**Supported as present-day diagnostic context, not causal proof:**

- persistent capability multiplicity;
- functional redundancy;
- poor portfolio answerability;
- recurring reconciliation and compensatory work signatures.

**Hypotheses / open empirical questions:**

- population-level accumulation/decay of HID through time;
- recovery coefficient rho and partial irreversibility;
- hysteresis;
- U-shaped oversight threshold in real deployments;
- sector-general magnitude;
- game-theoretic equilibrium as the dominant causal explanation.

The Evidence Notes' central discipline remains:

> **deficit is not decay.**

## 31. Relationship to UC-EA-03 and R01 Human Escalation / Whispering

[UC-EA-03](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) remains the natural architecture-validation lens for whether human oversight is actually authorised, informed, capacitated and timely and what the human action legitimately changes.

[R01 Human Escalation / Whispering](./reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) remains a richer virtual/analytical route for runtime human-review cost, queue, time, completion and signalling effects.

01K adds a separate architectural question:

> **Does the escalation/interface pattern itself reduce ACW and move human effort toward GIC/necessary NEO, or does it turn the human into compensatory middleware?**

A successful runtime route does not prove lower HID.

A lower measured HID does not prove that a particular incident has a reachable human reviewer.

## 32. FG-TIDA contributor lineage

Public contributor-level neighbours include:

- Theme #16 — regime-aware and capacity-aware human oversight:  
  https://github.com/FG-TIDA/themes/issues/16#issuecomment-5462496736
- Theme #16 — consolidated working structure with oversight capacity:  
  https://github.com/FG-TIDA/themes/issues/16#issuecomment-5479999938
- Theme #13 — objection-channel requirement:  
  https://github.com/FG-TIDA/themes/issues/13#issuecomment-5923844082
- Theme #13 — agent-originated objection / named accountable owner:  
  https://github.com/FG-TIDA/themes/issues/13#issuecomment-5985312999

These links establish working lineage only.

They do not establish FG-TIDA or ITU-T adoption of 01K, HICR/HICT/HID, the organisational measurement profile or the Human/Systemic Alert profile.

---

# Annex A — Human Intelligence Debt / Human Intelligence Gap source map

| Source | Role in the integrated component |
|---|---|
| [Human Intelligence Debt — Paper 1](https://tegrity.ai/human-intelligence-debt/) | Defines period-relative data/information, HICR, HICT and HID; identifies mechanisable work and EA implications. |
| [Harvester Multiplication — Paper 2](https://tegrity.ai/the-harvester-multiplication-problem-capability-fragmentation-governance-collapse-and-the-compounding-of-human-intelligence-debt/) | Mechanism: incoherent capability multiplicity, coordination overhead and governance cascade. |
| [HID Dilemma — Paper 3](https://tegrity.ai/the-human-intelligence-debt-dilemma-a-game-theoretic-account-of-why-rational-agents-build-irrational-architectures/) | Persistence model: incentive/cost asymmetry that makes addition locally rational and removal costly. |
| [Architectural Entropy — Paper 4](https://tegrity.ai/architectural-entropy-how-mediated-systems-spend-human-exergy-and-the-partial-irreversibility-of-human-intelligence-debt/) | Path-dependence / partial-irreversibility hypothesis; recoverable vs spent capability. |
| [Measuring Human Intelligence Debt — Paper 5](https://tegrity.ai/meassuring-human-intelligence-debt/) | GIC/NEO/ACW, cognitive-hours metrics, external indicators, internal instruments, rho, NOI, velocity and Study 0–5 programme. |
| [Evidence Notes](https://tegrity.ai/evidence-notes-for-human-intelligence-debt-propossed-study/) | Preliminary evidence map, bias/status tags, deficit-vs-decay discipline and open questions. |
| [Human Intelligence Gap series index](https://tegrity.ai/series/human-intelligence-gap/) | Series navigation and related working papers. |

---

# Annex B — Cross-series bridge map

| Bridge / neighbour | What it contributes | Boundary |
|---|---|---|
| [Cost of Clarity → HID](https://tegrity.ai/what-goes-unpriced-is-paid-in-human-intelligence/) | The hidden cost/risk of producing clarity is paid in misallocated human intelligence; knowledge-authority split; self-reinforcing loop. | Cost-of-Clarity measures are not HID measures. |
| [Attribution Gap ↔ HID](https://tegrity.ai/bridge-the-attribution-gap-and-capability-loss/) | Contribution/credit divergence can hide capabilities whose loss later produces compensatory work. | Independent theories; convergence is observation, not proof. |
| [Informational Friction](https://tegrity.ai/the-map-and-the-flow/) | Map/flow divergence and structural-awareness deficit provide systems-theory upstream context for compensatory mediation. | Different formal object; do not collapse its no-ideal framing into HICT. |
| [AI Operational Integrity ↔ HID](https://tegrity.ai/the-limits-of-ai-oversight/) | Oversight residual, AI Exhaustion Threshold, NOI and predicted U-shaped guardrail/coupling relation. | Prediction to be tested; more guardrails are not automatically worse. |
| [HID ↔ AI Integrity Management](https://tegrity.ai/what-cannot-be-recovered-must-be-managed-cross-series-bridge-human-intelligence-gap-with-ai-integrity-management/) | If rho<1, manage residual as risk/selection; flow vs stock; fragility/propagation. | Partial irreversibility and management method remain hypotheses/proposals. |
| [Structural Awareness synthesis](https://tegrity.ai/structural-awareness-program/) | Places HID beside Cost of Clarity, Attribution Gap, Informational Friction and wider AI Integrity / Regime Awareness work. | Cross-series convergence is abductive support, not transferred validation. |
| [Structural Awareness validation bridge](https://tegrity.ai/structural-awareness-foundation-validation/) | Proposed bridge from formal/Regime Awareness work to organisational risk/HID measurement. | Preliminary assessment proposal, not validation result. |

---

# Annex C — Minimum data needed for an organisational HID study

A serious organisational measurement should declare, at minimum:

- scope: process/capability/portfolio and organisational boundary;
- technological period / counterfactual frontier date;
- fixed capability taxonomy;
- task-sampling window;
- task episode identifiers;
- person-minutes/cognitive hours;
- GIC/NEO/ACW decision rules and anchor examples;
- ACW modifiers;
- objective tracer coverage;
- replaceability-evidence tier;
- reviewer/assessor identities or independence condition;
- Study-0 inter-rater result;
- H_releasable method;
- recovery-intervention definition if rho is estimated;
- application/capability multiplicity method;
- answerability checklist and provenance;
- external evidence tags;
- measurement uncertainty;
- exclusions;
- revalidation date;
- explicit statement of which outputs remain hypotheses.

Without these, the organisation may still conduct a qualitative HID architecture review, but it should not publish a numerical HID result.

---

# Annex D — Canonical integration thesis

The complete 01K reading is:

~~~text
architecture / information / incentives
        |
        v
GIC / NEO / ACW allocation
        |
        +----> HICR / HICT / HID
        |          |
        |          +----> recoverable / spent hypothesis
        |          +----> organisational measurement
        |          +----> AI Integrity managed-remnant path
        |
        +----> Human Escalation design review
                    |
                    +----> should a human be asked at all?
                    |
                    +----> if yes:
                          Runtime Human Capacity
                          AVAILABLE / DEGRADED /
                          UNAVAILABLE / UNKNOWN
                    |
                    +----> EHD / Signalling
                    +----> Cartography / RA where material
                    +----> Repositioning
                    +----> ACC / authority gate
~~~

The architectural ordering matters:

1. **Do not use the human as compensatory middleware by default.**
2. **Where genuinely human contribution or necessary oversight is required, check runtime capacity.**
3. **Carry the request and result through qualified Signalling/EHD.**
4. **Do not let alerting create authority, truth or a new ACC.**
5. **Measure organisational debt only with the evidence discipline of the source programme.**
6. **Where debt is partly unrecoverable, treat the remainder as a managed risk hypothesis until rho is actually measured.**

That is the role of **Human Capacity / Human Intelligence Debt** inside the wider Ecosystem Positioning corpus.
