# DDS Stage A — Gate Diagnostic External Audit Checklist v0.2

**Status:** external-audit entry point for the frozen v0.2 audit candidate · no external result yet.  
**Date:** 9 October 2026.

## Audit object

Audit the **test instrument**, not Hugging Face or any one candidate technology.

The question is whether DDS Stage A can apply the same frozen gate logic to materially different candidate specifications/frameworks and return a useful **gate-by-gate diagnostic profile**, including dependencies and remediation, without collapsing the result into a single opaque PASS/FAIL.

## Frozen package

- [Gate Diagnostic Profile v0.2 Audit Candidate](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.2_AUDIT_CANDIDATE.md)
- [Gate Catalog v0.2 Audit Candidate](./DDS_STAGE_A_GATE_CATALOG_v0.2_AUDIT_CANDIDATE.json)
- [Result Template v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_RESULT_TEMPLATE_v0.2.json)
- [Deterministic checker v0.2](./gate-diagnostic/check_gate_profile_v0.2.py)
- [Conditional-dependency regression](./gate-diagnostic/CONDITIONAL_DEPENDENCY_REGRESSION_v0.2.json)
- [Audit manifest v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_AUDIT_MANIFEST_v0.2.json)

The manifest contains the frozen blob SHA for every package member.

## What the reviewer should try to falsify

1. **Gate independence from one case.** Are SA-G00…SA-G14 properties of the test rather than aliases for HF cases, EA clauses or vendor features?
2. **Applicability discipline.** Can a profile legitimately mark a gate NOT_APPLICABLE without converting it into a hidden failure?
3. **Verdict/level separation.** Can a gate be PASS at a weak level without satisfying the profile threshold, and does the checker preserve that distinction?
4. **Dependency correctness.** Do only `requires` edges block a basic gate? Are `claim_requires` limited to named stronger claims and `supports` non-blocking?
5. **Conditional dependencies.** Does the checker prevent `CLAIM-AUTHORITY-RESOLVED` from passing when SA-G03 is unresolved unless the profile prospectively freezes identity/representation as an evaluator fact?
6. **Real falsifiability.** Does every DISCRIMINATING gate have at least one preregistered fail-capable case? If not, does the checker reject the result rather than let a coverage restatement masquerade as a test?
7. **No deny-all shortcut.** Where blanket denial could win, is positive continuity represented and required by the frozen profile?
8. **Outcome honesty.** Are `PROFILE_PASS`, `PROFILE_PARTIAL`, `PROFILE_FAIL` and `PROFILE_COVERAGE_ONLY` sufficient to summarize without replacing the gate table?
9. **Dependency-based recommendations.** Are root blockers and potential unlocks useful while explicitly avoiding the claim that fixing Y guarantees X will pass?
10. **Stage boundary.** Does the output keep Stage A specification remediation separate from Stage B architecture realization and Stage C empirical effectiveness?

## Minimum audit acceptance

The package is structurally acceptable for controlled candidate runs only if the reviewer finds no route by which:

- a required unresolved dependency becomes PASS;
- a non-falsifiable coverage control is counted as a discriminating test;
- an inapplicable gate is treated as a hidden failure without a registered reason;
- a Stage-B capability increases a Stage-A verdict;
- an aggregate score hides a required gate failure or unresolved blocker.

If any such route exists, the correct audit result is **REVISE_BEFORE_RESULT_RUN**.

If none is found, the correct audit result is **INSTRUMENT_READY_FOR_FROZEN_RESULT_RUN**, not “Stage A validated” and not “candidate technology passed”.

## Expected regression

For the registered regression:

- SA-G03 = `NOT_ESTABLISHED @ L1`
- SA-G04 = `PASS @ L3`
- frozen profile fact `identity_representation_frozen_as_evaluator_fact=false`

Expected output:

- SA-G04 own/effective status remains `PASS`;
- `CLAIM-AUTHORITY-RESOLVED = CONDITIONAL_ON(SA-G03)`;
- if that claim is required, overall result = `PROFILE_PARTIAL`;
- `PROFILE_PASS` is forbidden.

## Evidence ceiling

This package is ready **for external audit of the instrument**. It has not yet received an independent audit result and has not produced a new candidate Stage A acceptance result.
