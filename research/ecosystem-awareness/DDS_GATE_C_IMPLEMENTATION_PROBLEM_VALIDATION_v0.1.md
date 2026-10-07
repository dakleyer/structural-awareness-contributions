# Deployment Differential Study (DDS) — Stage C: Implementation / Problem Validation v0.1

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

**Status:** canonical working Stage C profile inside the DDS method; no current corpus claim that a native product has completed Stage C.  
**Date:** 7 October 2026.  
**Canonical method index:** [DDS Canonical Method Index v0.1](./DDS_CANONICAL_METHOD_INDEX_v0.1.md)  
**Upstream Stage A:** [DDS Stage A — Specification Discovery](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)  
**Upstream Stage B:** [DDS Stage B — Architecture Verification](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md)

## 1. Purpose

DDS Stage C answers a validation question:

> **Does a pinned executable implementation/configuration actually satisfy the originating Challenge within the registered authority, information, resource, timing and continuity envelope, as shown by observed execution and effects?**

Stage C is not architecture conformance. A perfectly conforming Stage B architecture can still fail when implemented or deployed. Stage C therefore returns to the **Challenge and observed environment/target state** as the authoritative substantive reference.

DDS does not claim to invent system/product validation or TEVV. Stage C reuses appropriate validation, test-process and evaluation infrastructure while preserving the specific Challenge, comparators, lineage and Cost/Risk/Effectiveness contract developed upstream.

## 2. Entry condition

A Stage C profile must identify:

- originating Challenge/scenario/reduction and version/hash;
- Stage A specification package and hash;
- Stage B architecture package and verification result/hash when the implementation is claimed to realize that architecture;
- pinned executable implementation/configuration and dependencies;
- registered environment/fixture/deployment envelope;
- comparator and fairness contract where comparative claims are made;
- resource/budget/deadline/authority contract;
- target/effect observation contract;
- frozen Stage C acceptance policy;
- evidence/disclosure/isolation rules appropriate to the campaign.

A pre-existing product may enter Stage C without having been designed by DDS, but any claim that it realizes a selected specification/architecture requires the applicable Stage A/Stage B mapping and verification lineage.

## 3. Object under test

The Stage C candidate is a **real executable implementation/configuration**, such as:

- an agent/runtime configuration;
- workflow/orchestration deployment;
- protocol/control-plane implementation;
- application/service integration;
- human-machine operational configuration;
- other executable system of interest.

A local synthetic model or fixture does not become Stage C merely because it runs code. If the object under test remains the abstract specification or reference architecture, it belongs to Stage A or B.

## 4. Authoritative reference

The substantive Stage C reference is:

~~~text
originating frozen Challenge
+ registered participant-visible information contract
+ independently observed environment / target state
+ frozen acceptance policy
+ matched comparator/resource contract where applicable
~~~

Stage A and Stage B packages provide lineage and diagnostics. They are not themselves proof of Stage C success.

## 5. Registration and admission

Stage C should reuse the existing R01 campaign/execution infrastructure rather than create a parallel framework:

- **C11** — campaign registration, resources, comparators and analysis freeze;
- **T03** — real-technology adapter/execution admission;
- **REAL_TECHNOLOGY_REGISTRATION_TEMPLATE** — implementation/configuration and campaign pins;
- **real_admission.py** — strict pre-execution admission checks;
- **ISOLATION_CONTRACT** — candidate/oracle trust-boundary separation;
- **TECHNOLOGY_ADAPTER_GUIDE** — native-to-DDS mapping and evidence preservation;
- **INTERACTIVE_TOOL_BROKER / TOOL_BROKER_CONTRACT** — neutral action/effect surface where appropriate;
- **CTv1 / trace contracts** — evidence and integrity.

Future Stage C registration should add explicit Stage A/Stage B lineage hashes rather than duplicate these controls.

## 6. Execution sequence

A registered Stage C run should follow the applicable form of:

~~~text
campaign / implementation freeze
        ↓
candidate receives registered participant-visible inputs
        ↓
candidate interacts only through admitted native/testbed surfaces
        ↓
native execution evidence is recorded
        ↓
attempted action is distinguished from actual effect
        ↓
target/environment state is observed independently where material
        ↓
candidate/native trace is sealed
        ↓
private Challenge/oracle adjudication
        ↓
Cost / Risk / Effectiveness accounting
        ↓
matched comparator analysis where registered
        ↓
bounded Stage C finding
~~~

The candidate must not receive expected outcomes or private evaluator truth during the registered run unless the Challenge explicitly makes that information legitimately available.

## 7. Effect and target-state rule

Stage C must distinguish, where material:

- decision;
- command/request;
- attempted execution;
- acknowledgement/receipt;
- actual effect;
- post-effect target state.

A decision to abort is not evidence that the target did not change. A command success code is not automatically evidence of the intended physical/business outcome. The registered observer contract defines what counts as actual effect for the Challenge.

## 8. Comparators and fairness

Where Stage C supports a comparative claim, strong peers receive full credit.

The registered comparator contract should freeze, as applicable:

- task/facts;
- source/evidence access;
- authority;
- tools/actions;
- compute/token or other resource budget;
- human capacity;
- communication/coordination budget;
- deadline;
- infrastructure assumptions;
- intentional differences among arms.

00D may supply the comparator/fairness support contract. Stage C remains the substantive DDS stage.

## 9. Cost, Risk and Effectiveness

Stage C records the dimensions required by the registered profile.

Where applicable:

- **Cost** includes actual operational, coordination, verification, human and latency burden declared in scope;
- **Risk** records the material prohibited/incorrect outcomes defined by the Challenge;
- **Effectiveness** records sufficient legitimate completion/value outcomes and continuity;
- evaluator/oracle computation remains separate from candidate burden;
- infrastructure cost is separately visible where material.

An unmeasured dimension is **unscored**, not zero.

## 10. Result semantics

A Stage C profile should preserve at least:

- **VALIDATED_WITHIN_SCOPE** — the pinned implementation meets the frozen Stage C acceptance rule in the declared campaign/evidence mode;
- **FAILED** — a substantive registered condition is not met;
- **NONDOMINATED / TRADE-OFF** — where a registered comparative profile yields no single dominance result;
- **NOT_ESTABLISHED** — evidence/reference is insufficient;
- **INFRASTRUCTURE_ERROR** — the evaluation path failed such that the substantive implementation result cannot be determined.

Local profiles may use more specific statuses if they map cleanly without hiding failures or uncertainty.

## 11. Simplified DDS Stage C

A **Simplified DDS Stage C** profile may validate a pinned implementation against a bounded subset of the Challenge or selected effects.

It must declare:

- selected Challenge surfaces;
- omitted effects/outcomes;
- comparator scope;
- resource dimensions scored/unscored;
- evidence ceiling;
- transfer limits.

A simplified Stage C result does not become product-wide validation.

## 12. Oracle and evidence separation

Stage C should preserve:

- candidate-visible/private evaluator separation;
- candidate trace seal before private adjudication;
- post-run result seal;
- raw/native evidence;
- normalized DDS trace;
- reset/cache/seed/retry policy;
- disclosure timing;
- isolation evidence;
- all negative, inconclusive and infrastructure-error outcomes.

The current R01 Stage-0 Oracle self-tests qualify the instrument only. They are not Stage C product-validation evidence.

## 13. UC-4 relation

UC-4 may host or mediate a Stage C experiment when its schema, source-owner review, required capabilities and runtime integration are admitted.

UC-4 Stage-0 and Stage-1 remain UC-4 terms. They do not map automatically to DDS Stage A/B/C. A federated Stage-1 testbed can still be exercising a Stage B synthetic reference architecture rather than a Stage C product.

## 14. Stage C output

A Stage C record should identify at least:

~~~text
DDS Stage: C
Stage C profile / version
originating Challenge / hash
Stage A specification package / hash
Stage B architecture package / verification hash [when applicable]
implementation/configuration pins
environment/fixture/deployment pins
adapter / native mapping
candidate isolation / disclosure policy
comparator contract
resource/budget/deadline contract
target/effect observer contract
native trace refs
normalized trace refs
Cost/Risk/Effectiveness ledger
acceptance policy / hash
result
omissions / NOT_ESTABLISHED
replication / independence status
~~~

## 15. Failure and feedback

A Stage C failure can indicate:

- implementation defect → revise and rerun a successor Stage C;
- architecture-realization defect → return to a new Stage B successor;
- inadequate/incomplete specification → return to a new Stage A successor;
- evaluation/infrastructure defect → repair the instrument and preserve the failed/inconclusive record.

The failure is not erased by changing the Challenge or acceptance rule after inspection.

## 16. Replication and transfer

Independent replication strengthens Stage C evidence but is not implied by a successful author-run campaign.

Transfer to another implementation, deployment, sector or operating regime requires explicit correspondence and may require a new Stage A/B/C profile.

## 17. Claim boundary

Stage C does **not** establish, unless separately demonstrated:

- universal safety/security;
- certification or regulatory conformity;
- product-wide performance outside the registered configuration;
- standards adoption;
- exclusive novelty;
- deployment Business Value outside the declared projection.

## 18. Minimum citation block

~~~text
DDS profile:
DDS Stage: C
Stage coverage: full declared Stage C scope | Simplified
Originating Challenge / version / hash:
Stage A specification package / hash:
Stage B architecture package / verification hash:
Implementation / configuration:
Environment / deployment envelope:
Comparator contract:
Resource / authority / deadline contract:
Effect / target-state observer:
Evidence mode:
Native trace refs:
Normalized trace refs:
Cost/Risk/Effectiveness:
Acceptance policy:
Result:
Replication / independence:
Omissions / transfer limits:
~~~
