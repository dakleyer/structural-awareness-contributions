# Ecosystem Awareness — Canonical Architecture Topology

> **Canonical public reader and reconciliation page.** It makes the common topology explicit across the controlled architecture documents. It does not replace, modify or extend the controlled v0.4 release baseline; it is not an adopted standard, an ITU-T deliverable, an implemented interface or completed validation.

## Purpose

Ecosystem Awareness (EA) is a decision-scoped architecture for preserving a justified epistemic posture when an agent, human or subsystem acts from a finite representation of a changing ecosystem.

The public corpus contains this architecture at several necessary levels: foundational limits, four epistemic positions, functional loops, transport-neutral handoff semantics, cross-theme examples and validation profiles. This page makes their shared topology explicit so that the symbols and boundaries are read consistently.

## Before this architecture: problem, requirements and hypotheses

This topology follows the [foundation](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md), [EA principles](./02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) and [00 — Canonical Requirements: Challenges, Sufficiency Conditions, Hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). Use this page and documents 01–05 to inspect the proposed mechanism, then use the [canonical architecture benchmark and reference-scenario evidence](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) for EA-H1–EA-H4, strong-peer comparison and empirical corroboration. The benchmark is a test route, not part of the universal requirement definition.

That route avoids two category errors: treating a generic challenge statement as a proof of a solution, or treating EA's architecture as the universal definition of a sufficient solution.

## 1. Canonical topology

For a decision `d` at time `t`:

| Element | Canonical meaning | Architectural consequence |
|---|---|---|
| **Ω** | The **open class** of potentially decision-relevant ecosystem state: actors, dependencies, environmental conditions, future configurations and interactions. Ω is not assumed to be closed or exhaustively enumerable. | No actor may claim that its representation exhausts the ecosystem. |
| **U** | The bounded operational universe actually represented for the current decision: identified entities, variables, sources, dependencies, controls and actors inside the working boundary. | A defined item inside U may still be unresolved. |
| **R_U** | The open decision-relevant residual relative to U. It is **not** a closed, known complement of U and may contain state not yet identified or categorized. | Good uncertainty quantification inside U does not establish completeness beyond U. |
| **W(d,t)** | The active observation and semantic window selected for the specific decision, domain and time. It is repeatedly qualified according to mission sensitivity, consequence severity, reversibility, freshness, available capacity and useful response horizon. | EA selects sufficient, bounded observation; it does not prescribe maximum context collection. |

**Ω is not a final universe.** It names the open ecosystem condition against which every local representation remains bounded. U and W(d,t) make that boundedness operational without turning the residual into an enumerable remainder.

## 2. Four epistemic positions

The four positions are **A, B, C and D**. They are not equal quadrants and must not be read as a 25/25/25/25 allocation. Their balance is dynamic, risk-indexed and decision-specific.

| Position | Meaning relative to the active decision window | Required treatment |
|---|---|---|
| **A — sufficiently determined** | State inside the active window is sufficiently determined for the relying decision. | A conclusion remains qualified by its scope, freshness, provenance and decision conditions. |
| **B — recognized and unresolved** | A defined state inside the active window remains unresolved. | Preserve it explicitly as unresolved, INDETERMINATE, HELD, fallback or another bounded operating posture; do not promote it to certainty. |
| **C — recognized and potentially obtainable** | State outside the current window is recognized as potentially obtainable and may justify bounded expansion or refresh. | Expand only when its expected decision value warrants the observation, verification, time and human/compute capacity required. |
| **D — structural residual** | State beyond the active window cannot be presumed fully discoverable, enumerable or eliminable. | Preserve the residual limitation rather than silently treating it as irrelevant or determined. |

C and D provide the operational reading of what remains outside the active window. They are a useful conceptual decomposition of residual uncertainty, but neither makes `R_U` a closed set complement or Ω a closed universe.

## 3. Agent-local qualification and ecosystem composition

EA is **not an epistemic super-controller** and does not reconstruct every participant’s internal reasoning.

1. A producer or agent qualifies a decision-relevant result for its own domain and window.
2. It preserves material scope, determination state, unresolved qualifiers, provenance, freshness, dependency and capacity information through the **Epistemic Handoff Descriptor (EHD)** or an equivalent semantic handoff.
3. A receiving agent treats the result as a bounded, attributed claim. It does not convert that claim into ecosystem-wide truth.
4. EA composes only what remains qualified and material for the receiving decision. Missing material qualification remains **UNKNOWN**.

A locally correct result may therefore remain insufficient for a system-level conclusion. More agents, more signals or more review do not automatically remove shared dependencies, scope limits or structural residual.

## 4. Conditions and failures are not additional poles

The architecture separately distinguishes:

| Category | Meaning |
|---|---|
| **Condition Type 0** | Structural non-determination despite correct local management. It is a condition, not a management failure. |
| **Failure Type 1** | Acknowledged uncertainty without bounded legitimate closure: indefinite search, HOLD or escalation that consumes the capacity and response time needed to act. |
| **Failure Type 2** | Suppressed uncertainty promoted into false certainty: forced binary closure, stale-frame reuse, unjustified scope extension or silently discarded missing inputs. |

These categories can arise inside U or in relation to residual uncertainty. They do not add a fifth, sixth or seventh epistemic position.

Type 1 and Type 2 are endpoint failure classes, not necessarily pure end-to-end system states. A Type-1 loop may be forced by timeout, default or review pressure into Type-2 closure; a Type-2 closure may later reopen as Type-1 HOLD/search when contradiction appears but its discarded basis cannot be reconstructed. False convergence, incompatible divergence, oscillation and cascades describe observable trajectories or consequences of those two classes. Defensive `UNKNOWN`, qualifier saturation and injected doubt are classified by what they do: unbounded delay/containment is Type 1; suppression, habituation or forced unsupported closure is Type 2. No additional failure type is introduced.

## 5. How the topology maps to the architecture

| Architecture layer | Role in the canonical topology | Source |
|---|---|---|
| **01 — Foundational Theory** | Defines Ω, U, `R_U`, bounded representation, residual indeterminacy, Type 0/1/2 and the need to qualify W(d,t). | [01 — Integrated Foundational Theory v0.5](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) and preserved [v0.4 source parts](./01_FOUNDATIONAL_THEORY_v0.4.part01.md) |
| **02 — Epistemic Safety Principles & Control Matrix** | Defines A–D and the internal and received-signal controls that prevent bounded evidence from becoming an unjustified global conclusion. | [02 — Control Matrix v0.4](./02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) |
| **03 — Functional Architecture** | Implements the two qualification loops through F1–F9: decision/frame qualification, evidence qualification, scoped composition, posture, requalification and learning. | [03 — Functional Architecture v0.4](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md) |
| **04 — Functional Interfaces & Agentic Security** | Makes qualified claims transport-neutral through the EHD and maintains the no-supercontroller rule across agents and security functions. | [04 — Functional Interfaces v0.4](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part01.md) |
| **05 — Provisional Cross-Theme Contracts** | Provides an FG-TIDA-oriented application example of the general interface architecture. It is not the definition of EA or an adopted group contract. | [05 — Cross-Theme Contracts v0.4](./05_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) |
| **00D — Canonical Architecture Benchmark and Reference-Scenario Evidence** | States EA-H1…EA-H4, matched B0–B3 comparison, evidence grades and empirical corroboration of 00E/00F. | [00D — Canonical Benchmark v0.2](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) |

## 6. Reading rule

Read the architecture in this order:

**open ecosystem Ω → represented universe U → active window W(d,t) → A/B/C/D qualification → bounded handoff and composition → requalification or bounded operating posture.**

The architecture does not promise complete ecosystem knowledge. Its claim is narrower: a decision can remain operational while explicitly preserving what is determined, unresolved, potentially obtainable and structurally residual, together with the authority and evidence limits that condition reliance.

## Status and source boundaries

This page is a public, canonical reading and reconciliation aid for the existing EA corpus. The controlled/frozen release baseline remains the six source documents recorded in the [Canonical Corpus Manifest](./CANONICAL_CORPUS_MANIFEST.md). The current integrated v0.5 foundation and canonical working benchmark v0.2 are working successors with their own stated status. No statement on this page implies standards adoption, deployed interoperability, completed comparative validation or a claim that EA has complete knowledge of an ecosystem.
