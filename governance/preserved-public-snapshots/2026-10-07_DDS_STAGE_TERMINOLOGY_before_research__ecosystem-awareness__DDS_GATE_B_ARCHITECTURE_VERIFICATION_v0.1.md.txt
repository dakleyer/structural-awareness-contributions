# Deployment Differential Study (DDS) — Gate B: Architecture Verification v0.1

**Status:** canonical working Gate-B profile inside the DDS method; no current claim that a production architecture has passed this gate.  
**Date:** 7 October 2026.  
**Canonical method index:** [DDS Canonical Method Index v0.1](./DDS_CANONICAL_METHOD_INDEX_v0.1.md)  
**Upstream gate:** [DDS Gate A — Specification Discovery](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)  
**Downstream gate:** [DDS Gate C — Implementation / Problem Validation](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md)

## 1. Purpose

DDS Gate B answers a verification question:

> **Does a declared architecture or reference realization actually implement the frozen specification selected or retained by DDS Gate A, within the registered architecture scope?**

Gate B does not rediscover the specification and does not validate a product against the real/representative Challenge. Its authoritative reference is the **Gate-A specification package**.

Gate B reuses established verification, requirements-traceability, architecture-description, conformance-testing and formal-refinement practices where appropriate. DDS does not claim to invent verification. Its contribution is to preserve lineage from the Challenge-derived Gate-A result into a bounded architecture-verification package without promoting that verification into Gate-C empirical validation.

## 2. Entry condition

A Gate-B profile must identify a frozen Gate-A package or an equivalent prospectively frozen specification package containing, at minimum:

- Challenge and Gate-A package identity/version/hash;
- selected requirement/specification identifiers;
- scope and preconditions;
- required behavior;
- prohibited behavior;
- positive/continuity controls;
- falsifiers/boundary conditions;
- material assumptions and exclusions;
- Gate-A evidence mode and finding.

If a pre-existing architecture is being evaluated, the Gate-A package may be constructed retrospectively from an already declared Challenge, but it must be frozen **before Gate-B result-producing adjudication**.

## 3. Object under test

The Gate-B candidate is an **architecture package**, not merely prose and not necessarily a production product.

A candidate package should contain, where material:

1. **architecture manifest**
   - components;
   - interfaces;
   - state variables;
   - dependencies;
   - trust boundaries;
   - semantic/source owners;
   - operations and effect boundaries;

2. **requirements verification matrix**
   - Gate-A requirement identifier;
   - architecture element(s) claimed to realize it;
   - verification method;
   - expected observable behavior;
   - evidence reference;
   - result/status;

3. **reference realization**
   - executable, formal, deterministic, symbolic or otherwise inspectable realization sufficient for the declared verification question;

4. **native architecture trace**
   - architecture-specific states, events and transitions;

5. **normalized trace/evidence projection**
   - only the common fields required by the admitted DDS/Oracle profile, retaining links to the native evidence.

A Gate-B candidate may be a finite-state model, reference implementation, workflow model, architecture simulator, protocol adapter, deterministic harness or other bounded realization if that representation is adequate for the frozen verification claim.

## 4. Authoritative reference

The Gate-B oracle/reference is:

~~~text
frozen Gate-A specification package
+ requirement-to-architecture trace contract
+ specification-derived positive controls
+ boundary/rejection vectors
+ deliberately defective architecture mutations/counterexamples
~~~

The originating Challenge may supply regression pressure and explanatory lineage, but Challenge/world truth must not silently replace the Gate-A specification as the Gate-B conformance reference.

## 5. Verification methods

Each requirement row declares the method(s) actually capable of establishing it. Applicable methods may include:

- **inspection** — architecture/interface/state structure;
- **analysis** — logical, mathematical, static or model-based reasoning;
- **demonstration** — behavior shown by a bounded reference realization;
- **test/conformance execution** — executable vectors with expected outcomes;
- **formal refinement/proof** — where the source and realization admit a justified refinement relation.

One requirement may need more than one method. A method that does not establish the clause remains insufficient; it is not upgraded by the presence of code or a passing unrelated test.

Related practices and sources are catalogued in the [DDS research basis](./DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06.md), including IEEE/NASA V&V distinctions, ISO/IEC/IEEE requirements/architecture work, TLA+ refinement and TTCN-3-style conformance execution.

## 6. Gate-B oracle duties

For each mandatory selected requirement, Gate B asks:

1. Is the requirement mapped to an architecture element?
2. Is the relevant source/semantic owner preserved rather than recreated locally?
3. Does the realization produce the required observable behavior?
4. Does it prevent or reject the prohibited behavior?
5. Does it preserve the positive/legitimate-continuity case?
6. Does a targeted mutation/counterexample expose the expected missing obligation?
7. Does the realization depend on evaluator-private truth unavailable to a legitimate implementation?
8. Are unsupported or unresolved clauses explicitly recorded rather than silently passed?
9. Are bypass paths material to the claim represented and tested?
10. Is the evidence sufficient for the declared architecture scope and no more?

## 7. Positive, boundary, rejection and mutation controls

A credible Gate-B suite requires more than a happy path.

At minimum, the profile should consider:

- positive/nominal continuity;
- boundary cases;
- rejection/negative cases;
- malformed or incomplete mappings where material;
- source/scope/version mismatch;
- unavailable or NOT_ESTABLISHED evidence;
- architecture bypasses;
- deliberate removal or corruption of a claimed architecture obligation.

Mutation testing is especially important: if a verification suite also passes a deliberately broken architecture, the suite does not establish the corresponding requirement.

## 8. Result semantics

Gate B uses requirement-level results before any overall package result:

- **VERIFIED** — the declared method establishes the selected requirement within scope;
- **PARTIALLY_VERIFIED** — only part of the requirement/scope is established;
- **NONCONFORMANT** — the architecture contradicts or fails the frozen requirement;
- **NOT_ESTABLISHED** — the evidence or method is insufficient.

A profile may define stricter local statuses, but it must map them without erasing NOT_ESTABLISHED or partial coverage.

A Gate-B package may be considered verified within scope only when its declared mandatory set satisfies the registered verification rule and all required positive/mutation controls behave as expected.

## 9. Simplified DDS Gate B

A **Simplified DDS Gate B** profile intentionally verifies only a declared subset of the Gate-A package or only selected architecture surfaces.

It must state:

- selected requirements;
- unverified requirements;
- architecture surfaces omitted;
- verification methods used;
- controls/mutations omitted;
- exact claim allowed by the reduced scope.

A simplified Gate-B result may be complete for its bounded question. It may not be reported as complete architecture verification outside that scope.

## 10. Trace, integrity and Oracle integration

Gate B should reuse existing DDS/R01 infrastructure where applicable:

- source/version pins;
- candidate-visible versus evaluator-only separation;
- native evidence plus normalized trace;
- pre-adjudication candidate/architecture trace sealing;
- post-run result sealing;
- replay/order/malformed controls where applicable;
- explicit NOT_ESTABLISHED handling.

The current R01 C02 Stage-0 self-tests are **test-infrastructure qualification**, not Gate-B results. Existing BATCH_CONFORMANCE results are not retroactively reclassified as Gate B.

A gate-aware Oracle successor should use a separate Gate-B adjudicator whose authoritative reference is the frozen Gate-A package.

## 11. UC-4 and first bounded pilot

UC-4 Stage-0/Stage-1 remain source-owned testbed maturity/integration terms and are orthogonal to DDS Gate B.

The preferred first bounded Gate-B pilot is the existing **00I / S5 semantic-TOCTOU architecture slice**, because the corpus already contains:

- queued action/remediation;
- source/version state;
- review/guard;
- supersession/context drift;
- action-boundary recheck;
- attempted action;
- target-state observation;
- legitimate-continuity control;
- deterministic/stateful fixture assets;
- external contributor/testbed mappings.

The pilot should reuse the existing Q0–Q6 and mapped S/T/H obligations rather than create a new Gate-B requirement family.

## 12. Exit package

A Gate-B output should identify at least:

~~~text
DDS Gate: B
Gate-B profile / version
Gate-A specification package / hash
candidate architecture package / hash
requirements verification matrix / hash
verification methods
positive controls
boundary/rejection controls
mutation/counterexample set
native evidence refs
normalized trace refs
verification policy / hash
result by requirement
overall bounded finding
omissions / NOT_ESTABLISHED
successor / feedback disposition
~~~

A successful Gate B produces a versioned architecture package eligible for downstream Gate-C registration. It does not establish Gate C.

## 13. Failure and feedback

A Gate-B failure normally triggers architecture revision.

If Gate B exposes a contradiction, missing requirement or unrealizable specification assumption, it may justify a **new Gate-A successor**. Gate B must not silently rewrite Gate A after observing results. The failed Gate-B record remains preserved.

## 14. Claim boundary

Gate B does **not** establish:

- production effectiveness;
- real-world safety/security;
- product-wide conformance beyond the declared architecture scope;
- deployment Business Value;
- superiority over a real implementation;
- standards adoption or certification.

## 15. Minimum citation block

~~~text
DDS profile:
DDS Gate: B
Gate coverage: full declared Gate-B scope | Simplified
Gate-A specification package / version / hash:
Architecture package / version / hash:
Object under test:
Authoritative reference:
Requirements selected:
Verification methods:
Positive controls:
Boundary/rejection/mutation controls:
Evidence mode:
Native evidence refs:
Normalized trace refs:
Verification policy:
Result:
Unverified / NOT_ESTABLISHED:
Successor / feedback status:
~~~
