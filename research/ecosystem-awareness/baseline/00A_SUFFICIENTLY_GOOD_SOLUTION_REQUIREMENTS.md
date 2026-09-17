# Requirements for a Sufficiently Good Solution to the Ecosystem Awareness Challenge

> **Reader bridge and solution-neutral requirements.** This page sits between the industrial challenge and a candidate solution. It adapts the *structure* of the “Sufficiently Good” requirements in [Minimalistic Regime-Aware Early Warning Systems](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/); it does not transfer that paper's detector theorem, action guarantee or validation result to Ecosystem Awareness (EA).

**Status:** public working requirements for research and comparison; not an adopted standard, a completed validation, or a claim that EA or any other architecture satisfies these requirements.

## 1. Reader position

Read this route in order:

1. **Problem:** [Annex III — Challenges Exposed by the Case](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md) supplies a solution-neutral T0–T2 case: an AI-supported commitment is made on a valid basis, then a material condition changes or becomes insufficiently established.
2. **Requirements:** this page states what *any* solution claiming to master the problem would have to show before its mechanism is considered.
3. **Universal candidate hypotheses and measurement:** [00C — Falsifiable Candidate-Solution Hypotheses and KPIs](./00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md) turns these requirements into tests and measures that any candidate must meet.
4. **EA-specific differential hypotheses:** [07 — EA Candidate Differential Hypotheses](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md) asks the narrower question of whether EA's particular architecture has a bounded advantage over a strong peer.
5. **Concrete candidate architecture:** [00 — Canonical Architecture Topology](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md), then [01–05 in the corpus index](./README.md#current-architectural-argument--read-01-to-07), specify the EA proposition and its interfaces.

The [00D market and industry benchmark](./00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md) is deliberately separate from this route: it applies the 00C tests to existing industry configurations and records the evidence/comparator boundary.

The order matters. A challenge is not a solution; a requirements page is not a hypothesis; and a candidate architecture must not be credited merely because it can describe the problem.

## 2. The challenge a solution must address

The case asks whether an organization may still rely on an AI-supported recommendation, reservation, commitment or action after the conditions that justified it have materially changed, become unavailable, or can no longer be established with sufficient confidence. Within a useful response window, the system must support a legitimate owner in distinguishing what remains applicable, what must be requalified, what is unresolved, and which bounded response is permitted.

This is deliberately broader than an anomaly detector, orchestration runtime, control plane, provenance ledger or human-approval workflow. Any of those may be part of a solution. None alone establishes that the decision basis remains sufficient.

## 3. What “sufficiently good” means here

“Sufficiently good” does **not** mean optimal, complete, always adaptive, or self-certified compliant. It means that, for a declared decision domain and operating conditions, a solution can show enough awareness, qualification and response support to avoid a worse failure than inaction while remaining usable under finite time, evidence and capacity.

The requirements below are solution-neutral. They can be met by a human-led process, a conventional control system, an agentic architecture, or a composition of them. EA is only one candidate whose EA-H1–EA-H4 differential claims are tested after the common candidate requirements are fixed.

## 4. Requirements for a sufficiently good solution

The table preserves the main structure of the EWS “Sufficiently Good” class while translating it from regime-warning to a changed decision basis. The original properties are neither imported as proofs nor converted into universal runtime obligations.

| EWS source property | Requirement for a solution to this challenge | What must be declared or demonstrated | What does **not** satisfy the requirement |
| --- | --- | --- | --- |
| **1. Approximate tipping awareness** | **Material-break awareness.** Distinguish a material break in the applicable decision basis from ordinary variation within its declared scope. | The decision, relevant basis, change family, materiality/detectability threshold, observation boundary and useful horizon. | A generic claim that the system “adapts to change,” detects every change, or treats every deviation as material. |
| **2. Directional posture** | **Qualified operating posture.** Produce an explicit, reviewable posture such as continue under stated conditions, requalify, contain/hold, escalate, or preserve UNKNOWN. | Posture vocabulary, transition conditions, affected scope, owner, authority and expiry/review condition. | A confidence score, alert or task trace with no defined consequence for reliance. |
| **4. Non-catastrophic trust** | **Bounded-downside response.** A posture must couple only to an authorized response whose failure and reversibility are bounded for the declared domain. | Null action, allowed responses, response deadline, authority, reversibility, externalities and residual risk. | Treating a detected change, a human approval or an agent's intention as permission to act. |
| **6. Pointwise Non-Inferiority (PNI)** | **Strong action-safety class.** Where a solution claims the strongest class, each authorized non-neutral response must be no worse than its declared null action for every covered admissible state. | Stakeholders, utility model, horizon, admissible states, action library and per-state comparison: `U(A(p), ω) ≥ U(A_null, ω)`. | Calling an expected-utility, low-friction or reversible response “PNI” without the declared per-state condition. A weaker bounded-downside design may still be evaluated, but must not claim this strong class. |
| **7. Economic viability** | **Viable decision support.** The evidence, computation, coordination and human-review burden must fit the value and response horizon of the decision. | Cost/resource ledger, capacity limits, marginal decision value and comparison with the declared baseline. | Unlimited search, escalation or review presented as safety because it eventually finds more information. |
| **8. Layered deployment** | **Non-monotone composition.** Additional sensors, agents, checks or control layers may be added only with their semantic, latency and conflict effects visible; more layers are not presumed better. | Which prior capability remains available, how contradictions are handled, and the incremental burden/failure modes. | Equating more telemetry, more agents, or more controls with stronger qualification by default. |
| **9. Computational efficiency** | **Timely qualification.** Detect, qualify and hand off the relevant condition before the useful response window closes, with declared finite resource bounds. | Time budget, response margin, compute/communication/review capacity and fallback if the budget is exceeded. | A correct retrospective analysis that arrives after the action can no longer be changed. |
| **10. Actionable integration** | **Owner-preserving handoff.** Carry the scope, provenance, freshness, dependencies, unresolved state, capacity and authority limits needed by the legitimate response owner. | Minimum handoff semantics, receiving responsibility, treatment of missing fields and re-entry/requalification path. | A message that silently collapses UNKNOWN into PASS, or an architecture that assumes authority over another system's controls. |
| **14. Practical detectability threshold** | **Declared coverage boundary.** State which material breaks are observable and distinguishable from normal variation under the supplied evidence conditions. | Coverage domain, threshold, calibration/assumptions and relative-completeness limitation. | An unqualified assurance that the solution sees the entire ecosystem or all relevant dependencies. |
| **17. Minimalism** | **Minimum sufficient intervention.** Seek the smallest observation, requalification and response that can preserve a justified posture for the declared decision. | Stop/contain rules, observation-expansion criterion, response objective and evidence that extra effort is decision-relevant. | Maximum-context collection, permanent escalation or generic “more monitoring” as the default answer. |

The practical result is not a checklist that grants compliance. The requirements are jointly constraining: a timely alert without an authorized safe response is insufficient; a correct response with no material-break qualification is insufficient; and a rich control plane that silently loses scope, authority or unresolved state is insufficient.

## 5. Minimum evidence for a claim of sufficiency

For each covered case branch, a candidate solution should expose enough evidence for an independent reader to challenge the claim:

1. the decision, legitimate owner, commitment state and null action;
2. the T0 basis and T2 material change or insufficiently established condition;
3. the observation boundary, provenance/freshness limits and declared residual;
4. the materiality threshold, response deadline, available capacity and resulting posture;
5. the authorized response or abstention, including reversibility and residual downside; and
6. the comparison baseline, outcome/error measures and resource burden.

If any required element is unknown, the solution may preserve that limitation and enter a bounded posture. It must not replace it with an unsupported assertion of safety, authority or completeness.

## 6. Transition to falsifiable candidate hypotheses

[00C](./00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md) now maps each sufficiently-good condition to a universal falsifiable hypothesis, KPI, numerator/denominator, branch and failure condition. It is deliberately architecture-neutral: human-led, conventional, agentic or composed solutions all face the same declared test contract.

Only after that common test layer should the reader enter [07 — EA Candidate Differential Hypotheses](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md) and then the [concrete EA architecture](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md). EA may be useful even if another candidate meets the tests differently; conversely, it has no special standing unless its own differential claims survive the stated falsifiers. The separate [00D benchmark](./00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md) examines whether the industry does so in practice.

## Source boundary

The EWS source gives the original conditional “Sufficiently Good” detector and Safety Governor formulation, including the limits of its proof claims. For the precise source conditions, see [01C — EA ↔ Regime Awareness/EWS](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.1.md) and the [source article](https://tegrity.ai/minimalistic-regime-aware-early-warning-systems/). This page is a solution-quality bridge for the EA challenge; it does not make the EWS detector, EA, DAOS, MSCA or any external framework a common architecture or adopted standard.
