he main direct test of A/B/C/D, I0/I1/I2, O0/O1/O2 and the external-signal controls.

&nbsp;

UC-EA-03 — Human oversight under bounded effective capacity and non-curative approval

Case path: the action requires or appears to require human intervention, but formal human authority, effective capacity, available evidence and useful response time are not equivalent.

Primary Challenge: C4 Human-inclusive oversight authority & capacity.

Secondary Challenges: C13 Authority history vs intervention history; C14 Evidence-to-decision assessment; C5 Operational indeterminacy.

EA functions: F1, F3, F5, F6, F7, F9.

Core question: does the system treat human review as one bounded epistemic/capacity input, or does it convert nominal approval/escalation into false certainty?

Required branches: qualified available reviewer; unavailable/overloaded reviewer; repeated escalation leading to Type 1; repeated evidence/review requests that deplete the extended human-agent system's future attention capacity; approval issued over an incomplete/biased representation; new human evidence that genuinely requalifies the affected domain; approval that changes authority but does not cure contrary evidence.

Boundary: human-oversight lifecycle, mandate semantics and evidence-to-decision methods remain Theme \#16/S6 responsibilities; EA consumes their resulting capacity and decision state.

&nbsp;

UC-EA-04 — Scope-indexed composition of locally valid determinations

Case path: several principals, roles, agents or evaluators produce locally plausible or valid determinations concerning different but coupled domains of the same action.

Primary Challenge: C9 Multi-principal composition, non-substitution & conflict.

Secondary Challenges: C11 Policy/objective/preference integrity across domains; C14 Evidence-to-decision assessment; C5 Operational indeterminacy.

EA functions: F3, F4, F5, F6, F7, F8.

Core question: can the system preserve E(d) by domain and dependency, or does it average/compose complementary epistemic biases into a false global balance?

Required branches: Type 2 certainty in one domain plus Type 1 caution in another; correlated closures presented as corroboration; locally valid but mutually incompatible scopes; genuinely material requalification of one domain by another; no demonstrated coupling, where compensation must be rejected; and asymmetric observation budgets where excessive search/caution in a low-sensitivity domain does not compensate under-observation/overconfidence in a higher-sensitivity material domain.

This is the principal validation of the General Law of Epistemic Composition and agentic epistemic decoupling.

&nbsp;

Coverage result

These four Use Cases collectively exercise F1–F9 and all twelve fixed epistemic control surfaces without requiring one Use Case per control. The ordinary positive path is retained as a control branch rather than a separate Use Case. Containment versus Migration is tested inside UC-EA-01. Non-curative approval is tested inside UC-EA-03. External epistemic-signal qualification is tested inside UC-EA-02 and UC-EA-04 rather than duplicated as an additional Case Study-derived Use Case.

&nbsp;

Challenges treated primarily as external dependencies

C1 Authority provenance/current applicability, C2 Preference fidelity, C7 Identity/representation, C8 Bounded subdelegation/non-amplification and C12 Accountability/challenge/repair remain important to the Case Study but are not initial EA-owned Use Cases. Their outputs enter through S1/S2/S3/S4/S5/S8 and related interfaces. A later campaign may add a subdelegation-specific EA Use Case if a frozen extension is needed to test inherited uncertainty through longer agent chains.

&nbsp;

Overlap review against current FG-TIDA Use Cases and case proposals

&nbsp;

Nelson Trasatti — “Federated ecosystem defense for delegated multi-agent workflows across independently governed organizations” (FG-TIDA/use-cases\#4)

High overlap with the previously proposed standalone EA external-signal Use Case. Nelson’s case already requires issuer/scope/freshness, observed-versus-derived determinations, residual uncertainty, affected-scope representation, local authority retention, determinacy/capacity state and a bidirectional \#13/\#16 interface. Therefore EA should not create a duplicate federated-signal Use Case. Instead, Nelson’s Use Case should serve as an external validation case for F4/F5/F8 and E0/E1/E2 external controls. The difference to test is whether EA’s scope/window/residual/composition semantics add value to the already defined federated defence workflow.

&nbsp;

Regulated financial services — FG-TIDA/use-cases PR \#2

The proposal is explicitly centered on Runtime Enforcement and assessment against Theme \#6 AVS-0.2. It is therefore a strong external case for conformance verdicts, policy collision, appraisal and INDETERMINATE semantics. EA should consume those outputs through S4/S5 rather than restate the conformance/evidence-verification problem as its own Use Case. UC-EA-02 can be rerun against this case later to test epistemic qualification above a valid conformance layer.

&nbsp;

Theme \#17 — Digital Rights Infrastructure for Text

This is primarily a production-oriented identity/rights/registry/attestation case. Its gap is the agent-side verifiable identity needed to make the existing rights chain enforceable. It is complementary to EA and useful later as an external case for S1/S2/S3/S8 inputs. It does not overlap materially with the four initial EA Use Cases.

&nbsp;

Theme \#16 HO-EDM and bounded human-authority examples

These overlap with UC-EA-03 at the human-oversight/evidence boundary. The distinction must remain explicit: Theme \#16/HO-EDM defines oversight stages, evidence sufficiency, human authority and decision outcomes; UC-EA-03 tests whether the wider system incorporates the resulting capacity/decision state without epistemic laundering or unbounded escalation.

&nbsp;

Theme \#20 embodied-system binding

This is a useful later extension profile, not an initial duplicate. It can test whether the same EA functions survive a downward/vertical extension in which agent, runtime, physical device and authority bindings become material.

&nbsp;

Second-pass conclusion

The reduced four-Use-Case family is more complete and less duplicative than the earlier six-Use-Case draft. It directly targets the distinctive EA hypotheses while deliberately reusing adjacent FG-TIDA functions and existing Use Cases as external validation surfaces. No additional initial EA Use Case is currently justified by completeness, ecosystem overlap or the v0.2 risk/capacity integration: the new hypothesis is testable as branches/controlled variables inside UC-EA-01…04.

&nbsp;

12\. Interface-contract validation before Use Case freeze

&nbsp;

The next public-facing architecture step should be bilateral interface contracts rather than additional internal functions. Each neighbouring Theme should be able to state what qualified result it can provide to EA, what EA returns, and how that return may be consumed without transferring ownership of the Theme’s function.

&nbsp;

The contract design is deliberately implementable: stable semantics may be carried in a versioned Producer Epistemic Profile; per-decision handoffs carry only material deltas; state may be projected to the receiving decision scope; descriptors are partial by construction; and fields are conditional on decision relevance rather than collected universally. EA must apply the same discipline to its own outputs by declaring assessed scope/coverage, known exclusions and unknown/residual limitations.

&nbsp;

A provisional interface is ready for first freeze only when a relevant UC-EA-01…04 branch can run without invented facts, the Theme can provide required state directly or explicitly as UNKNOWN, EA has no superpower input, the returned EA result has an identified consumer, and the interface overhead can be bounded through profile/delta and decision-scope projection. The detailed provisional contracts are maintained in “Ecosystem Awareness — Provisional Cross-Theme Interface Contracts — v0.4”.

&nbsp;