# Ecosystem Awareness — Frozen Public Reference Corpus

> **Publication freeze: 11 September 2026**  
> **Status:** frozen public reference snapshot for citation, provenance and architecture review. This publication freeze does **not** imply final architecture freeze, completed validation, ITU-T adoption, NIST acceptance, or standards endorsement.

Ecosystem Awareness is a research and pre-standardization architecture for maintaining justified operation when the decision-relevant ecosystem is larger, more dynamic and less completely knowable than the representation available to any one agent, human or subsystem.

The core problem is simple to state:

> **In agentic systems, locally justified decisions can coexist with global indeterminacy.**

The architecture therefore asks how a system can preserve a justified epistemic posture while relating residual uncertainty to mission risk, determination capacity, available response time and the value of knowing more.

## Canonical public statement

Ecosystem Awareness is **not** an attempt to know or reconstruct the complete ecosystem. It is an architectural discipline for managing uncertainty correctly across the current observation window and the decision-relevant state that remains outside that window.

Its minimum architectural statement is:

> **Ecosystem Awareness is the set of architectural principles and control mechanisms by which a system maintains justified operation through the correct management of uncertainty inside and outside its current observation window, including detection and handling of structural non-determination, unbounded unresolved uncertainty and false certainty, and requalification of the decision frame when its assumptions cease to be sufficient.**

## Frozen corpus map

| Artifact | Role | Status in this public freeze |
|---|---|---|
| [`FOUNDATIONAL_THEORY_v0.4_PUBLIC_FREEZE.md`](./FOUNDATIONAL_THEORY_v0.4_PUBLIC_FREEZE.md) | Theoretical basis: bounded operational universe, open residual, Type 0/1/2, agentic amplification, window selection and requalification | Working foundational architecture preserved as a frozen public reference snapshot |
| [`ARCHITECTURE_BENCHMARK_v0.4_PUBLIC_FREEZE.md`](./ARCHITECTURE_BENCHMARK_v0.4_PUBLIC_FREEZE.md) | Peer-architecture completeness and differentiation audit | Provisional architecture benchmark; novelty hypothesis, not novelty proof |
| [`UC-EA-01_v0.3_FROZEN.md`](./UC-EA-01_v0.3_FROZEN.md) | Architecture-validation profile for action-time operating-frame requalification | Frozen validation profile; **not** an FG-TIDA use-case submission |
| [`PUBLIC_PROVENANCE_2026-09-08.md`](./PUBLIC_PROVENANCE_2026-09-08.md) | Public contribution and acknowledgement chain | Controlled provenance snapshot with exact public links |
| [`MANIFEST.md`](./MANIFEST.md) | Freeze scope, claim boundaries and version record | Publication control record |

## Architecture at a glance

The current model separates four epistemic positions by domain:

1. **Sufficiently determined in-window state** — enough has been established for the declared decision.
2. **Defined in-window indeterminacy** — the relevant entity or determination is represented, but cannot currently be established sufficiently.
3. **Recognized potentially knowable out-of-window state** — additional decision-relevant state may be brought into the active frame when justified.
4. **Structural residual** — decision-relevant state beyond the bounded representation whose exhaustive discovery cannot be presumed.

The architecture also separates one structural condition from two failures of epistemic management:

- **Type 0 — structural non-determination:** the current frame does not support sufficient mission-level determination even under correct uncertainty handling.
- **Type 1 — unbounded unresolved uncertainty:** uncertainty is acknowledged but determination effort is not bounded into legitimate closure.
- **Type 2 — false certainty:** uncertainty is suppressed, lost or overextended into unjustified certainty.

The objective is not maximum awareness. It is **minimum sufficient awareness** for the mission and criticality, with observation and determination effort calibrated to ecosystem sensitivity, consequence severity, reversibility, available capacity and remaining response time.

## Candidate architectural differential

The current benchmark preserves seven candidate differentiators as one combined architecture:

- **A. Four-position epistemic state by domain**
- **B. Twelve in/out-window epistemic control surfaces**
- **C. General Law of Epistemic Composition — scope-bound and non-fungible epistemic state**
- **D. Agentic epistemic decoupling**
- **E. Risk/capacity-indexed double-loop requalification**
- **F. Orthogonal epistemic condition and operating posture**
- **G. Transport-neutral epistemic handoff**

Most underlying primitives have strong prior art. The research hypothesis is the value of their composition into a runtime functional/interface architecture. The benchmark does **not** claim that uncertainty quantification, uncertainty propagation, context engineering, human oversight, provenance, attestation, observability, containment or multi-agent orchestration are themselves novel.

## Relationship to Minimum Sufficient Control and Regime Awareness

Ecosystem Awareness is part of a connected operational-integrity line:

**Ecosystem Awareness → Minimum Sufficient Control Architecture → Regime Awareness / Sufficiently Good Early Warning → Requalification**

- Ecosystem Awareness qualifies what is sufficiently determined, unresolved and outside the current frame.
- Minimum Sufficient Control asks what least intervention-intensive architecture can preserve a declared Objective Envelope under those conditions.
- Regime Awareness detects when the assumptions supporting the current frame and control architecture are losing validity.
- Requalification updates only the affected scope, window or control posture where necessary.

## Public FG-TIDA provenance

Ecosystem Awareness is currently **contributor-level pre-standardization work**, not an adopted ITU-T architecture or Recommendation.

Primary public thread:

- [ITU-T FG-TIDA Theme #13](https://github.com/FG-TIDA/themes/issues/13)
- [Detection sufficiency vs intervention sufficiency](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5462867033)
- [Lightweight systemic-capacity / handoff architecture](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5529042183)
- [Residual ecosystem-level indeterminacy](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5554099339)
- [Ward Duchamps — placement and possible foundational architectural building block](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256)
- [Lei Gao — bidirectional human-oversight / Ecosystem Awareness interface](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5578556995)
- [Cyril Gorlla — local verdict mapping to determinacy envelope](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5584191756)
- [Consolidated Ecosystem Awareness conceptual / functional contribution](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5585387513)

## Claim boundaries

This corpus does **not** claim:

- that the complete ecosystem can be exhaustively enumerated;
- that probability and indeterminacy are synonyms;
- that every residual is quantifiable as probability mass;
- that every complex system-level property is formally undecidable;
- that more agents automatically imply more information loss;
- that distributed systems are inherently inferior to monolithic systems;
- that signalling creates knowledge nobody possesses;
- that complete ecosystem-state sharing is desirable;
- that Ecosystem Awareness replaces observability, uncertainty quantification, provenance, formal methods, resilience, human oversight or security controls;
- that ITU-T, FG-TIDA, NIST or another standards body has adopted or validated this architecture.

## Stewardship

This corpus is maintained in the public research context of **Tegrity.AI**, an initiative of **The Integral Management Society, a Swiss non-profit association**.

No open-source or content licence has yet been selected for this repository. No permission beyond GitHub's applicable platform terms should be inferred.
