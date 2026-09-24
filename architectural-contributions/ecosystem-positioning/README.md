# Ecosystem Positioning — Agentic Architecture

> **You are here:** [Structural Awareness Programme](../../README.md) → **Architectural Contributions / pre-standardization** → **Ecosystem Positioning**

This README is the **human entry point and reading map for the complete Ecosystem Positioning corpus**. It explains why the architecture exists, how the principal pieces fit together, what is already specified, and where to go for the technical detail.

The PowerPoint remains the visual companion. The three Level-3 corpora — **Ecosystem Awareness, Regime Awareness and Minimum Sufficient Control Architecture (MSCA)** — remain the semantic owners of their detailed mechanisms. This page does not replace them; it makes the whole system intelligible before the reader enters them.

## Canonical presentation

### ⬇️ [Download the canonical PowerPoint (.pptx)](https://raw.githubusercontent.com/dakleyer/structural-awareness-contributions/main/presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pptx)

### 📄 [Open the canonical PDF](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pdf)

[Presentation manifest](../../presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md)

[Visual guide to the wider corpus](../../research/ecosystem-awareness/VISUAL_GUIDE.md)

The deck is a **working proposal**, not an adopted standard. Git history provides its version lineage.

---

# Why this architecture exists

Agentic systems can remain locally correct while becoming badly situated in a changing ecosystem.

Identity may still verify. Policy may still return a permit. A tool call may still be technically valid. A human may still approve. A digital twin may still be healthy. Yet the practical meaning of those results can change when roles, authority, dependencies, evidence, operating conditions or the surrounding ecosystem change faster than the local control model.

The corpus therefore asks a different question:

> **For this participant, this decision and this moment, what can responsibly be relied on, what remains unresolved, what has changed, and what should be requalified before action continues?**

Ecosystem Positioning is participant-local. It does not require one global controller, one universal state, or one actor that understands the entire ecosystem.

## Six scenarios — when correct systems produce absurd outcomes

These scenarios are deliberately memorable. They are not claims that the named technologies caused the failures; they are controlled ways to test whether locally reasonable behaviour remains systemically valid.

### 00E — The 100 Million Token Enterprise

A large multinational automates work across the enterprise, consumes **100 million tokens** and creates a major human supervision burden. At the end, the organization has gained no meaningful differential advantage: enormous processing and review effort, but little useful new determination, work or strategic value.

### 00F — The City That Stopped Safely

A highly automated smart city experiences small, gradual changes rather than one obvious failure. Some vehicles continue normally, others follow different emergency routes, and others HOLD waiting for intervention, producing a system-level mobility failure from individually understandable local postures.

### 00G — Bar-to-Napoleon

Robots or agents are preparing and operating a bar in present-day Spain when one participant begins signalling a false Napoleonic frame. Repetition and apparent agreement can progressively displace the still-valid mission until the group behaves as if it were marching toward Russia — unless source dependence, authority and genuine regime change are distinguished correctly.

### 00H — The Quiet Four Thousand

A good-faith agent authorized for one customer discovers a real overcharge affecting roughly **4,000 customers**. The system can fail in both directions: execute outside the original mandate, or correctly stop after one case and silently lose the material finding; a separate adversarial hardening tests an outsourced helpdesk Dispatcher that creates valid leaves under an unauthorized common campaign root.

### 00I — The Patch That Undid the Fix

A remediation action is correct when it is approved, but another repair changes the decision basis before the delayed action executes. The database may serialize both actions correctly and every local technical control may remain healthy, yet the stale action can still execute later and undo the newer fix.

### 00J — The Author Pays for Their Own Work

An author correctly publishes and registers a work through a strong rights/provenance chain. As content moves through external AI and rights-resolution systems, technically valid records can be promoted beyond their original evidentiary scope until the downstream system may treat the author as needing permission or payment to reuse content derived from the author's own work.

---

# These are not stories about bad technology

The corpus deliberately uses **strong current technologies and strong implementation trajectories**, not weak strawmen.

Current technology profiles include:

**Microsoft Agent 365 · LangGraph / LangSmith · FIWARE NGSI-LD / Orion-LD · AWS IoT Core / IoT TwinMaker · OpenAI Agents SDK / Agents API / Responses Multi-agent · Claude Agent SDK · Stripe Radar / Refund API · AWS Step Functions / Amazon RDS / Systems Manager / DynamoDB / EventBridge · Panodyssey AI Transparency Notice / ODRL / JSON-LD / TEMS rights portability.**

The normal progression is:

**standard competent implementation → defended / top-notch implementation → the same defended implementation frozen → material ecosystem or regime drift → targeted requalification / repositioning.**

Good engineering matters: strong implementations eliminate many ordinary failure routes. The harder question is what happens when the system remains technically healthy but the relation between the system and its ecosystem changes.

The technology has not necessarily broken.

**The relationship between the technology and its ecosystem has changed.**

[Open the scenario and technology-profile index](../../research/ecosystem-awareness/baseline/README.md)

---

# The corpus spine

The corpus is not a collection of unrelated papers. It has a controlled reading order.

## 1. Foundations — why bounded knowledge cannot become global certainty

[**01 — Integrated Foundational Theory**](../../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) establishes the open-ecosystem problem: a participant operates from a bounded representation, while a residual always remains outside the represented universe and the useful decision window can change over time.

[**02 — Epistemic Safety Principles & Control Matrix**](../../research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) defines the principles that prevent bounded evidence, confidence, consensus or local closure from being silently promoted into an unjustified global conclusion.

Together they provide the conceptual basis for the rest of the corpus. They are foundations, not a rolling container for every later mechanism.

## 2. The central document — Canonical Requirements

[**00 — Canonical Requirements: Challenges, Sufficiency Conditions, Hypotheses and KPIs**](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) is the **central normative test document of the current corpus**.

It defines the controlling route:

**S1–S14 Challenges → T1–T4 sufficiently-good conditions → H1–H6 falsifiable hypotheses → KPI / falsification protocol.**

Scenarios, use cases, fixtures, technology profiles, interfaces and benchmarks select and test applicable routes from this document. They do **not** create a parallel hidden requirements system.

[Requirements-vNext review](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) checks whether later Ecosystem Positioning mechanisms require a new requirements version. The current bounded review finds that the later mechanisms can still be mapped to the existing requirements, with clarification candidates rather than an automatic S15/T5/H7 expansion.

## 3. Requirements coverage — where each scenario and use case tests the requirements

[**Use Case Portfolio / Requirements Coverage Map**](../../research/ecosystem-awareness/baseline/USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md) is the requirements-first map across scenarios, use cases, fixtures, execution status and gaps.

The six reference scenarios above then turn the requirements into concrete quality routes. Each scenario freezes facts, defines positive/negative/adversarial controls where needed, maps relevant requirements into gates, and records what would count as a pass, fail, requalification or unresolved result.

This is why the scenarios are detailed: they are not illustrations added after the architecture; they are part of the requirements-to-evidence path.

---

# The shared epistemic position

A central structural pattern is the four-part participant-local epistemic position.

[**Canonical Architecture Topology**](../../research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md) provides the shared reading key across the corpus.

In compact form:

| Position | Meaning |
|---|---|
| **A** | What is sufficiently established now for the declared decision and scope. |
| **B** | The determination / confidence / qualification around that represented state. |
| **C** | What could still be established with the capability, time, evidence access and effort currently available. |
| **D** | Residual that is not presently established as knowable within that capability boundary. |

These positions are deliberately **non-fungible**. More confidence in A cannot compensate for an unexamined residual in D; more compute cannot automatically substitute for missing authority; more messages do not automatically create independent evidence.

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
