# FG-TIDA — Ecosystem Awareness
## Public Footprint and Provenance — 2026-09-08

**Status:** public-footprint and provenance record. This document records public contributor-level discussion and related controlled internal provenance. It is **not** an ITU-T deliverable, Recommendation, adoption statement or endorsement.

### Public anchors

- FG-TIDA Theme #13: https://github.com/FG-TIDA/themes/issues/13
- Current Ecosystem Awareness conceptual / functional milestone: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5585387513
- Placement / foundational-interface acknowledgement by Ward Duchamps: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256

### Claim boundary

Ecosystem Awareness is being developed as contributor-level research and a candidate pre-standardization architecture. Public discussion inside FG-TIDA provides provenance and technical interaction; it does not establish FG-TIDA or ITU-T adoption.

## 1. Purpose

This record preserves the public development trace of Ecosystem Awareness and its relationship to the FG-TIDA Theme #13 discussion, neighbouring Themes and the controlled internal architecture corpus. Its purpose is provenance, not institutional attribution beyond the public evidence.

The relevant distinction is:

- **public discussion / contributor trace** — issues, comments, replies, commits and public artifacts that can be independently inspected;
- **controlled internal corpus** — the architecture, validation profiles, contracts, benchmarks and derivation records maintained by Tegrity.AI / The Integral Management Society;
- **formal FG-TIDA / ITU-T outputs** — only what the applicable ITU-T process actually designates as such.

No movement from the first or second category into the third is implied by this document.

## 2. Ecosystem Awareness problem framing

The public line starts from a structural problem: in agentic systems, locally justified decisions can coexist with system-level indeterminacy because agents, people and independently governed subsystems operate with bounded representations, finite capacity and different scopes.

The candidate architecture asks how a system can preserve a justified epistemic posture when:

- the relevant ecosystem cannot be completely known;
- local confidence remains conditional on a bounded observation/context window;
- additional determination has cost and may consume compute, latency, privacy and human attention;
- dependencies and operating regimes can change on operational timescales; and
- a downstream consumer may otherwise mistake local closure for system-level certainty.

The public differential is therefore not uncertainty quantification, observability, orchestration or human oversight by themselves. It is the preservation and composition of scoped epistemic state, residual indeterminacy, dependency and capacity semantics across boundaries.

## 3. Theme #13 placement

Theme #13 is the closest public FG-TIDA surface because it deals with ecosystem-level signals, independently governed participants, correlation / affected scope, containment and related interoperable information flows.

Ward Duchamps' public comment supported the view that Ecosystem Awareness belongs in Theme #13 rather than being separated merely to create a new home for it. The same comment described the lightweight systemic-capacity / handoff layer as a potential foundational architectural building block and supported keeping the determinacy-envelope work independently testable from the Theme #13 signal lifecycle.

This is an important provenance point, but the wording must remain bounded: it is public contributor discussion by a Theme participant, not formal adoption of Tegrity.AI technology by FG-TIDA or ITU-T.

## 4. Systemic-capacity / epistemic handoff

The current public architecture direction is a lightweight handoff that allows independently governed producers and consumers to communicate enough system-level state without requiring a shared internal reasoning model or a central orchestrator.

The public Theme #13 line has explored a compact determinacy/capacity envelope including concepts such as:

- operational closure/result;
- determinacy margin or decision/scope qualifier;
- capacity binding;
- inherited indeterminacy.

The controlled corpus generalizes this through the Epistemic Handoff Descriptor (EHD), but the public Theme #13 four-field envelope remains a specialized public-facing profile rather than the entire internal architecture.

The handoff is intended to preserve minimum semantics required by a relying component while allowing internal algorithms, uncertainty models, private memory and reasoning details to remain local.

## 5. Neighbouring Theme interfaces

Ecosystem Awareness is intentionally transversal. It consumes qualified outputs from neighbouring functions and returns scoped systemic state; it does not take ownership of their local mechanisms.

### Theme #6 — local verdict / conformance

Theme #6 can provide a scoped local verdict or conformance state. Ecosystem Awareness can consume that state while preserving its issuer, scope, evidence and indeterminate semantics. A valid local verdict must not automatically be projected into a system-level determination beyond the domain it actually covers.

### Theme #16 — human oversight

Theme #16 owns the human-oversight and intervention lifecycle. Ecosystem Awareness may consume effective human-capacity, authority, intervention and decision state, but human approval does not automatically cure missing evidence or transform unresolved external state into certainty.

### Theme #5 / authority provenance

Authority provenance and standing remain upstream inputs. Ecosystem Awareness does not originate grants, delegations or legal standing. It can preserve the fact that authority state is unresolved when that uncertainty remains material to the relying decision.

### Population/evaluation layers

Population-level assessment, evaluator diversity, sampling uncertainty and structural residual can enter as qualified evidence. More samples may reduce sampling uncertainty while leaving structural non-identifiability or scope limitations intact.

## 6. Why a separate architecture layer is being explored

A conventional architecture can have strong identity, policy enforcement, attestation, provenance, HITL and observability while still fail at system-level epistemic composition.

Examples include:

- several locally valid outputs whose scopes are not composable;
- repeated evidence that is actually derived from one upstream source;
- a human reviewer who is authorised but unavailable within the useful response window;
- a stale operating frame reused after material context change;
- confidence in one domain compensating for unresolved state in a different material domain;
- an upstream UNKNOWN disappearing during a handoff and being interpreted downstream as no residual issue.

The candidate EA layer therefore asks whether the system can state what is determined, what remains unresolved, what could still be determined at justified cost, and what remains structurally residual — and preserve those distinctions across boundaries.

## 7. Internal architecture relationship

The controlled corpus currently expresses the architecture through:

- Foundational Theory of Bounded Uncertainty;
- Epistemic Safety Principles & Control Matrix;
- Functional Architecture F1–F9;
- Operational interfaces O1–O6;
- Trust/security interfaces S1–S13;
- Epistemic Handoff Descriptor semantics;
- Provisional Cross-Theme Interface Contracts;
- Architecture Benchmark & Novelty Audit;
- a four-profile validation family plus the EHD / Theme #13 interoperability test.

Those documents provide the deeper test and falsification apparatus. They should not be represented as adopted FG-TIDA architecture simply because selected concepts have been discussed publicly.

## 8. Current public-status boundary

The safest public description is:

> Ecosystem Awareness is a candidate pre-standardization architecture being developed publicly through contributor work in ITU-T FG-TIDA, with current discussion centred on Theme #13 and interfaces to neighbouring local-verdict, human-oversight, authority and evaluation work.

The following claims are not supported and must not be made:

- "ITU-T adopted Ecosystem Awareness";
- "FG-TIDA adopted Tegrity.AI technology";
- "Ecosystem Awareness is an ITU standard";
- "The validation profiles are official FG-TIDA use cases";
- "The public comments prove architectural novelty or superiority".

## 9. Public milestone chronology

The public footprint should be read chronologically rather than as if the latest comment retroactively made all earlier material formal.

Early comments introduced the conceptual problem, bounded ecosystem reasoning and a minimum interoperable handoff direction. Later discussion clarified placement inside Theme #13 and the distinction between the systemic-capacity assessment and the incident-signal lifecycle. Subsequent work connected the architecture to neighbouring functions and matured the controlled internal corpus.

The latest public conceptual/functional contribution is the current public milestone; older comments remain provenance and historical context.

## 10. Provenance principle

Public provenance is useful precisely because it permits later reviewers to distinguish:

- what existed at a particular date;
- which ideas were public versus still internal;
- what neighbouring contributors responded to;
- which terminology changed during refinement;
- and what remains only a candidate research architecture.

The Git history and public issue/comment history should therefore be preserved rather than rewritten to simulate a cleaner origin story.
