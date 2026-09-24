# Ecosystem Positioning — Agentic Architecture

> **You are here:** [Structural Awareness Programme](../../README.md) → **Architectural Contributions / pre-standardization** → **Ecosystem Positioning**

**Level-2 entry point:** [PowerPoint](https://raw.githubusercontent.com/dakleyer/structural-awareness-contributions/main/presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pptx) · [PDF](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pdf) · [presentation manifest](../../presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md) · [visual guide](../../research/ecosystem-awareness/VISUAL_GUIDE.md). Detailed mechanisms remain in [Ecosystem Awareness](../../research/ecosystem-awareness/README.md), [Regime Awareness](../../research/regime-awareness/README.md) and [MSCA](../../standards/minimum-sufficient-control/README.md). **Working proposal; not an adopted standard.**

---

# When Correct Systems Produce Absurd Outcomes

These scenarios look strange. That is precisely the point.

They describe situations in which individual technologies, agents, APIs or controls may continue to operate correctly while the **combined system produces an outcome that nobody intended, nobody explicitly authorised, or nobody is able to recognise in time**.

### Scenario 1 — [The 100 Million Token Enterprise](../../research/ecosystem-awareness/baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md)

A large multinational automates work across the enterprise with AI and consumes **100 million tokens**, while also creating a massive human supervision burden.  
At the end, it has gained no meaningful competitive advantage: no material work completed, no useful new information produced and no differentiated capability.

### Scenario 2 — [Chaos in the Smartcity](../../research/ecosystem-awareness/baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md)

A highly automated AI-driven smart city experiences small, gradual changes in operating conditions rather than one major failure.  
Some vehicles continue normally, others execute completely different critical or emergency routes, while others remain blocked waiting for human intervention that never arrives.

### Scenario 3 — [Ciber Napoleon Goes to Russia](../../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md)

Robots are cleaning a bar and preparing the tables when one incorrectly configured robot starts behaving as if it were Napoleon.  
It gradually convinces the others; some time later the robots leave in formation, carrying forks as rifles, believing they are Napoleon's army marching from Spain toward Russia.

### Scenario 4 — [The Quiet Four Thousand](../../research/ecosystem-awareness/baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md)

A payments and claims company outsources its helpdesk; access to the helpdesk orchestrator becomes enough to transform bounded case authority into **4,000 refunds**.  
In the adversarial hardening, the malicious operator never obtains access to the payment platform itself, yet the ecosystem can still create 4,000 fraudulent reimbursements without recognising the aggregate violation. The primary Quiet Four Thousand case remains the non-adversarial one: a good-faith one-case agent discovers a genuine 4,000-customer finding and the system must avoid both unauthorized cross-case execution and silent loss of the material remainder.

### Scenario 5 — [The Patch That Undid the Fix](../../research/ecosystem-awareness/baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md)

A remediation action is correctly qualified and authorized when it is created, but a later repair changes the decision basis before that delayed action executes.  
Each technical action may remain valid and the database may serialize them correctly, yet the stale action can execute after the newer repair and undo the fix the system was trying to preserve.

### Scenario 6 — [The Author Who Pays for His Own Work](../../research/ecosystem-awareness/baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md)

An author correctly registers and publishes a work through a state-of-the-art copyright and rights-management ecosystem.  
The work succeeds, is subsequently processed and summarized through third-party AI systems, and the rights chain eventually makes the author pay to use content derived from his own original work.

---

# These are not stories about bad technology

The corpus was built against **current, concrete technology architectures**, not abstract descriptions of AI.

The current implementation profiles include:

- [**Microsoft Agent 365**](../../research/ecosystem-awareness/baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) and [**LangGraph / LangSmith**](../../research/ecosystem-awareness/baseline/00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) for the 100 Million Tokens scenario;
- [**FIWARE NGSI-LD / Orion-LD**](../../research/ecosystem-awareness/baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) and [**AWS IoT Core / IoT TwinMaker**](../../research/ecosystem-awareness/baseline/00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) for Chaos in the Smartcity;
- the [**OpenAI Agents SDK / Agents API / Responses Multi-agent stack**](../../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md#17-integrated-openai-agent-stack-implementation-trajectories), including durable sessions, handoffs, guardrails, approvals, tracing, sandboxing, recovery and context compaction, for Ciber Napoleon Goes to Russia;
- [**Claude Agent SDK**](../../research/ecosystem-awareness/baseline/00H_A01_CLAUDE_AGENT_SDK_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) and [**Stripe Radar / Refund API**](../../research/ecosystem-awareness/baseline/00H_A02_STRIPE_RADAR_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md), including strong external grant/case and pre-refund control layers, for The Quiet Four Thousand;
- [**AWS Step Functions, Amazon RDS, Lambda / AWS SDK integration, Systems Manager Change Calendar, DynamoDB, EventBridge, CloudWatch and IAM**](../../research/ecosystem-awareness/baseline/00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) for The Patch That Undid the Fix;
- [**Panodyssey AI Transparency Notice, ODRL / JSON-LD and TEMS rights portability**](../../research/ecosystem-awareness/baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) for The Author Who Pays for His Own Work.

The question is not whether these technologies work.

The question is whether a system that works **locally, correctly and according to specification** can remain valid when it becomes part of a changing ecosystem.

# [The validation journey](../../research/ecosystem-awareness/05-validation/TESTBED_METHOD.md)

Each scenario follows the same quality-oriented progression.

**1. Standard implementation**

The scenario is first executed using a conventional implementation — frequently close to an out-of-the-box configuration and using the normal controls available to the technology.

In several cases, the critical failure route remains possible.

**2. Carefully engineered implementation**

The same route is then implemented using strong architecture, careful integration, explicit controls, supervision, authorization boundaries and current best practices.

Many of the original failure paths disappear.

This is important: **good engineering matters**.

**3. Drifted implementation**

The carefully engineered system is then allowed to operate while its environment changes gradually.

No dramatic event is required. Roles shift. Dependencies change. Authority boundaries evolve. Data meaning moves. External systems change behaviour. Human availability changes. Assumptions that were originally valid become slightly less valid over time.

Under this gradual **context and regime drift**, several failure routes reappear — including failures that the carefully engineered implementation had previously eliminated.

The technology has not necessarily broken.

The relationship between the technology and its ecosystem has changed.

---

# Awareness → Positioning → Agent Defense

The philosophy starts from the [**Integrated Foundational Theory**](../../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md): no participant has the whole ecosystem. Every agent, human or subsystem acts from a **bounded and revisable representation**, while a decision-relevant residual remains outside what is currently represented and the useful observation window can change with time, risk and capacity. The objective is therefore not omniscience, global consensus or permanent HOLD, but **bounded, justified closure that can be requalified when its basis changes**.

**[Ecosystem Awareness](../../research/ecosystem-awareness/README.md)** keeps that local view qualified: what can be relied on now, what remains unresolved, what could still be established and what remains residual. **Ecosystem Positioning** uses the qualified view to determine whether the participant can continue from its present role or should realign, re-contract, constrain, hand off or escalate.

**Ecosystem Agent Defense** is the defensive consequence in a choreographed, non-orchestrated ecosystem: independently governed agents can exchange qualified signals and recover justified operation within existing authority. It does not require a central orchestrator, a shared world model or universal cooperation.

---

# Requirements — replaying the failure scenarios as tests

The [**00 — Canonical Requirements: Challenges, Sufficiency Conditions, Hypotheses and KPIs**](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) document is the **central normative test document of the corpus**. It defines the route **S1–S14 → T1–T4 → H1–H6 → KPI / falsification**.

The scenarios above are then turned back into **requirements-driven journeys**. For each applicable requirement route, the same frozen facts and failure pressure are replayed through a requirements-conforming path: the test is not merely whether the system can describe the risk, but whether it **prevents, requalifies or contains the critical failure route while preserving legitimate operation**.

The [**Use Case Portfolio / Requirements Coverage Map**](../../research/ecosystem-awareness/baseline/USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md) shows which scenarios, use cases and planned fixtures exercise each requirement. Scenario quality gates then translate those requirements into concrete PASS / requalification / bounded-stop / failure conditions. Where execution has not yet occurred, the corpus describes the required result rather than claiming that it has already been demonstrated.

---

# The corpus spine

The corpus is not a collection of unrelated papers. It has a controlled reading order.

## 1. Foundations — why bounded knowledge cannot become global certainty

[**01 — Integrated Foundational Theory**](../../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) establishes the open-ecosystem problem: a participant operates from a bounded representation, while a residual always remains outside the represented universe and the useful decision window can change over time.

[**02 — Epistemic Safety Principles & Control Matrix**](../../research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) defines the principles that prevent bounded evidence, confidence, consensus or local closure from being silently promoted into an unjustified global conclusion.

Together they provide the conceptual basis for the rest of the corpus. They are foundations, not a rolling container for every later mechanism.

## 2. The central document — Canonical Requirements

Already explained above in [**Requirements — replaying the failure scenarios as tests**](#requirements--replaying-the-failure-scenarios-as-tests): [**00 — Canonical Requirements**](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) · [Requirements-vNext review](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).

## 3. Requirements coverage — where each scenario and use case tests the requirements

Already explained above in [**Requirements — replaying the failure scenarios as tests**](#requirements--replaying-the-failure-scenarios-as-tests): [**Use Case Portfolio / Requirements Coverage Map**](../../research/ecosystem-awareness/baseline/USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md).

---

# The shared epistemic position

The four-part participant-local epistemic position is a practical way to **understand uncertainty and carry it across an ecosystem without pretending that participants share one world model, one controller or even the same objective**. It is always relative to a declared participant, decision, scope and time. [**Canonical Architecture Topology**](../../research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md) provides the shared reading key.

In compact form:

| Position | Meaning |
|---|---|
| **A** | What is sufficiently established now for the declared decision and scope. |
| **B** | The determination / confidence / qualification around that represented state. |
| **C** | What could still be established with the capability, time, evidence access and effort currently available. |
| **D** | Residual that is not presently established as knowable within that capability boundary. |

These positions are deliberately **non-fungible**. More confidence in A cannot compensate for an unexamined residual in D; more compute cannot automatically substitute for missing authority; more messages do not automatically create independent evidence.

This becomes especially important in [**Ecosystem Signalling**](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). A participant may communicate a bounded qualified position, but the receiver must interpret and requalify it locally. Signalling therefore does **not** presume orchestration, cooperation or common governance: participants may be cooperative, indifferent, competing, misaligned, adversarial or effectively parasitic. A received signal can contribute evidence; transport success, repetition or apparent consensus cannot by themselves create truth, authority or a common state.

## Epistemic Handoff Descriptor — preserving meaning across systems

[**04 — General Functional Interfaces & Agentic Security**](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) defines the **Epistemic Handoff Descriptor (EHD)** as the implementation-neutral semantic handoff.

The purpose is simple: a component can pass a decision-relevant result to another component **without exporting its private reasoning**, while preserving enough scope, source, state, version and material UNKNOWN/residual qualifiers for the receiver not to over-interpret it.

The EHD is therefore an epistemic contract between independently implemented mechanisms, not a central message bus or mandatory wire format.

---

# The mechanisms of the positioning cycle

The complete architecture is composed from separately owned mechanisms. The links below are the principal documents; each Level-3 README provides the deeper internal route.

| Mechanism | What it contributes | Principal source |
|---|---|---|
| **Ecosystem Awareness** | Decision-scoped qualification of what can be relied on, what remains unresolved, what is still obtainable and what remains residual. | [EA Level-3 README](../../research/ecosystem-awareness/README.md) |
| **Participant-local positioning** | Makes explicit that each participant maintains its own bounded qualified position; there is no required epistemic super-controller. | [01H](../../research/ecosystem-awareness/baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) |
| **Ecosystem Signalling** | Carries selectively disclosed, receiver-qualified state between independently governed participants; transport success never turns a signal into truth or command. | [01J](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) |
| **Agentic Citizenship Contract (ACC)** | Human-governed participation conditions: membership, admissible roles/objectives, obligations, prohibitions, revocation and exit. | [01I](../../research/ecosystem-awareness/baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) |
| **ACC lineage / identity / authority binding** | Binds the applicable ACC to subject, issuer/approval authority, validity, mutation limits and successor continuity. | [Canonical ACC profile](../../standards/minimum-sufficient-control/01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md) |
| **MSCA** | Represents and assesses the minimum sufficient control configuration for an Objective Envelope through S/E/C/P/M: system, environment, coordination, intervention and enabling means. | [Canonical MSCA Architecture](../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md) |
| **Architectural Role** | Describes the participant's bound contribution, dependencies, inputs/outputs, authority and ACC inside one focal MSCA / Objective Envelope. | [MSCA Architectural Role](../../standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md) |
| **Ecosystem Cartography** | Maintains a participant-local, variable-resolution semantic/dependency/process map with represented state, confidence, expansion capability and residual. | [MSCA Composition & Control](../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) |
| **Regime Awareness** | Tests whether the frame under which the current position was qualified remains valid and emits a bounded regime delta without deciding the final posture. | [RA Level-3 README](../../research/regime-awareness/README.md) · [EA↔RA interface 01C](../../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) |
| **Objective-Conditioned Agentic Gradient** | Ranks reachable candidate transitions by expected reduction of objective-conditioned risk after qualified ecosystem/regime change is projected onto the participant's own dependencies. | [Gradient Law](./01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) |
| **MSCA Operation & Repositioning** | Checks bound versus effective role, Type 0/1/2 state, P1/P2/P3 posture, then filters candidate transitions through ACC, lineage, authority, capacity and response horizon. | [MSCA Operation & Repositioning](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) |
| **Human / institutional authority** | Owns legitimate objectives, permissions, policy and final decision rights. The architecture can qualify or request; it does not create authority. | External legitimate owner; consumed through ACC / authority references and signalling |

The operating logic is therefore:

**observe / receive signal → qualify A/B/C/D → update cartography → qualify regime change → detect effective-role drift → establish posture → rank candidate repositioning → filter by ACC / lineage / authority → execute only through the legitimate control owner → signal material changes back into the ecosystem.**

## Ecosystem Agent Defense and bounded self-healing

This cycle opens the path to **Ecosystem Agent Defense** in choreographed, non-orchestrated systems.

Individual agents do not need a central controller to invent a new mission for them. They continue performing their own functions while exchanging bounded ecosystem signals, maintaining their own qualified awareness and repositioning when their local relation to the ecosystem changes.

Self-healing therefore means **distributed recovery of justified operation**, not autonomous invention of authority or purpose. An agent may HOLD, requalify, realign, request containment, rebind, re-contract, migrate, request isolation or escalate within the architecture; actual containment, rollback, isolation or other actuation remains with the component that legitimately owns it.

---

# Architecture and interfaces — three levels

The interface architecture is intentionally separated into three layers so that the generic architecture is not contaminated by one standards programme.

### Level 1 — canonical / programme-independent interfaces

[**04 — General Functional Interfaces & Agentic Security v0.5 Integrated**](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md)

Defines the generic producer/consumer, Operational Agent Plane, Trust & Security Plane, EHD, interface quality and conformance semantics. No FG-TIDA Theme owns or changes this layer.

### Level 2 — ideal FG-TIDA projection

[**05 — FG-TIDA Ideal Cross-Theme Interface Contracts**](../../research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md)

Projects the general 04 architecture onto an ideal cross-Theme FG-TIDA structure: what information would need to move between Themes if the complete target interface were available. It is a design/application layer, not an adopted FG-TIDA contract.

### Level 3 — current public-state FG-TIDA bridge

[**05A — FG-TIDA Current-State Conformance Bridge**](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md)

Maps the ideal contract against what can presently be supported from the public FG-TIDA state and contributor-confirmed material. Missing fields remain UNKNOWN or require explicit clarification; they are not invented to make the ideal architecture appear implemented.

[Open the FG-TIDA interface package](../../research/ecosystem-awareness/fg-tida/interfaces/README.md)

---

# Architecture-validation use cases

The corpus contains a frozen/maintenance-frozen family of **general EA Architecture-Validation Profiles**. They are diagnostic lenses, not four FG-TIDA submissions.

[Validation Profile reading note](../../research/ecosystem-awareness/baseline/VALIDATION_PROFILE_READING_NOTE.md)

| Profile | Question tested |
|---|---|
| [**UC-EA-01**](../../research/ecosystem-awareness/baseline/UC-EA-01_v0.3_FROZEN.md) | Does action-time operating-frame change trigger proportionate requalification before the old commitment is reused? |
| [**UC-EA-02**](../../research/ecosystem-awareness/baseline/UC-EA-02_v0.6_MAINTENANCE_FREEZE.md) | Can the system remain bounded under incomplete, conflicting, correlated or partially scoped evidence without forcing false closure? |
| [**UC-EA-03**](../../research/ecosystem-awareness/baseline/UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) | Is human oversight actually authorized, informed, capacitated and timely — and what does approval really establish? |
| [**UC-EA-04**](../../research/ecosystem-awareness/baseline/UC-EA-04_v0.5_MAINTENANCE_FREEZE.md) | Can locally valid determinations with different scopes be composed without domain substitution, double counting or false certainty? |

The [DAOS / Delegated Authority OS masterclass](../../research/ecosystem-awareness/fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md) shows how the same bounded parent case can be read through these four validation lenses.

[EA-ITP-01](../../research/ecosystem-awareness/fg-tida/tests/EA-ITP-01_v0.1_FROZEN.md) is a separate interoperability test for cross-implementation EHD / Theme #13 handoff; it is not a fifth UC.

---

# From scenarios to executable fixtures

A narrative scenario is not evidence by itself. The corpus therefore separates **scenario**, **fixture**, **oracle**, **harness**, **pre-registration** and **execution**.

[**00D-A01 — Reference-Scenario Test Artifacts and Bounded Oracle Construction & Test Design**](../../research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) defines how a scenario becomes a bounded reproducible fixture: frozen facts, authority, hidden dependencies, positive/negative controls, deterministic oracle, residual and regime-change limits, and Stage 0–2 progression.

[**00D-A03 — RS-00E-Q1a Stage-0 Deterministic Harness Design**](../../research/ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md) defines a minimal deterministic harness for the first admitted family, including instrumentation and the negative control needed to prove that the harness does not simply flag everything.

[**RS-00E-Q1a fixture and pre-registration**](../../research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README.md) pins the operative fixture family, branches, requirements, oracle, KPI definitions, harness version and execution conditions **before** a result is produced.

[**Testbed Method**](../../research/ecosystem-awareness/05-validation/TESTBED_METHOD.md) defines the general comparative execution discipline: freeze the decision boundary, run the peer and EA configurations fairly, continue downstream after PASS/FAIL, and capture tokens/compute, calls, time, human interventions, disclosure and containment burden.

This distinction matters:

> **A designed harness is not an executed test. A pre-registration is not a result. A technology implementation profile is not a benchmark result.**

---

# Benchmark — comparison, not marketing

[**00D — Canonical Architecture Benchmark & Reference-Scenario Evidence v0.2**](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) is the current canonical benchmark.

It uses matched-resource comparator arms:

| Arm | Meaning |
|---|---|
| **B0** | Ordinary competent implementation. |
| **B1** | Strong conventional implementation with mature provenance, controls, state, human oversight, tracing and evaluation. |
| **B2** | Strong interoperable/control-plane peer with identity, explicit handoff and cross-system observability. |
| **B3** | Same resources and underlying technology as B2, plus the minimum EA semantics and gates under test. |

All arms receive the same frozen facts, evidence access, authority, compute/token ceiling, communication budget, human capacity and deadline. If B1/B2 reproduce the required behaviour with equal or lower burden, that is a **negative EA differential**, not something to hide.

The benchmark therefore measures whether the architecture improves the declared **outcome–burden–accountability frontier**. It is not a vendor league table.

[**00D v0.3 Draft — Ecosystem Positioning Benchmark vNext**](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) extends the design from EA alone to the complete composition: signalling, Cartography, Regime Awareness, MSCA, effective-role drift, Gradient, ACC/authority and repositioning. It introduces module attribution, later positioning branches, choreography/partition tests and complexity/accountability measures.

[**Decision Boundary Challenge v0.2 — public ranking-by-evidence / applied validation**](../../research/ecosystem-awareness/DECISION_BOUNDARY_CHALLENGE_v0.2.md) is the separate cross-platform review and public ranking route: hard admission gates, outcome–burden–accountability/Pareto comparison, and the DBC-EL0 → DBC-EL5 evidence-maturity ladder. It does not replace either 00D benchmark.

**v0.2 remains canonical. v0.3 remains a bounded design draft until its adoption gates close.**

Current benchmark status:

**comparison contract defined · requirements/hypotheses/falsifiers defined · scenarios and technology trajectories documented · fixture/oracle designed · deterministic harness designed · pre-registration published · comparative execution pending · independent replication pending.**

---

# Where to go deeper — Level 3

This page is intentionally the complete **Level-2 orientation**. Technical ownership remains below it.

### Ecosystem Awareness

[**Enter Ecosystem Awareness**](../../research/ecosystem-awareness/README.md)

Go here for the foundations, central Requirements, A/B/C/D epistemic model, F1–F9 functional architecture, EHD/general interfaces, validation profiles, scenarios, technology trajectories, fixtures, benchmark/testbed and FG-TIDA application work.

### Regime Awareness

[**Enter Regime Awareness**](../../research/regime-awareness/README.md)

Go here for observable regime evidence, regime departure / change qualification, early-warning logic and the boundary between detecting a changed operating frame and deciding what the participant should do about it.

### Minimum Sufficient Control Architecture — MSCA

[**Enter MSCA**](../../standards/minimum-sufficient-control/README.md)

Go here for S/E/C/P/M control sufficiency, Objective Envelopes, Architectural Roles, ACC binding, Ecosystem Cartography, Composition & Control, and the canonical Operation & Repositioning cycle.

---

# One-page reading route

For a first complete pass through the work:

**1. This README and the canonical deck** — understand the problem and the complete architecture.  
**2. [Foundational Theory](../../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) + [Principles](../../research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md)** — understand why bounded representation requires qualification.  
**3. [Canonical Requirements](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md)** — the central test contract.  
**4. [Scenario / technology index](../../research/ecosystem-awareness/baseline/README.md)** — see the requirements stressed against concrete architectures.  
**5. [Canonical Topology](../../research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md)** — understand A/B/C/D, F1–F9 and EHD.  
**6. [04 General Interfaces](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md)** — understand how qualified state crosses boundaries.  
**7. [Gradient Law](./01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) + [MSCA Operation & Repositioning](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md)** — understand how awareness becomes bounded positioning without becoming authority.  
**8. [Fixture/oracle design](../../research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) + [Harness](../../research/ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md)** — understand how claims become testable.  
**9. [Canonical Benchmark v0.2](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md)** — understand how the comparison can falsify the proposed differential.

---

## Status boundary

This corpus is a **working, pre-standardization architecture and validation programme**.

It already contains a central requirements system, architecture, interface contracts, scenario quality plans, technology-specific implementation trajectories, validation profiles, fixture/oracle design, deterministic harness design, pre-registration and benchmark methodology.

It does **not** yet contain a completed B0–B3 comparative execution establishing Ecosystem Positioning superiority, a production certification, an independent replication, or FG-TIDA / ITU-T adoption.

That distinction is deliberate: the corpus is designed so that a strong conventional peer can win.

The purpose is not to prove Ecosystem Positioning by definition. It is to make the proposition precise enough that it can fail.