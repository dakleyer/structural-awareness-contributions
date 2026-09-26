# A23 semantic bridge review

26 September 2026. Applied step F02 of [the change plan](../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A15_PLAN_CAMBIOS_Y_EFECTO_EN_LA_TESIS_v0.1.md). Author review against the canonical source; not independent peer review.

## What passing traversals establishes

A successful traversal establishes the expected disposition for its declared facts, implementation and oracle. A negative control establishes that the test detects its injected failure. Neither quantifies over every conforming implementation or every admissible trace. A23 asks a different question: whether faithfully satisfying a declared requirement route entails its principle. A22 asks about distinct diagnostic signatures and their encoding; independence or diagnostic minimality is not sufficiency.

The previous A23 green test result includes assertions that three counterexamples remain counterexamples. Green means that this finding reproduced. It does not mean that all six implications hold. The 379 traversal regressions, 77 correction checks, 11 original A23 audit checks and nine new semantic checks must retain separate counts.

## Source adjudication and bounded diagnostics

| Candidate | Source and model comparison | Result and remaining obligation |
|---|---|---|
| P3 | Canonical §1.1 binds evidence to one subject/proposition/decision; S5 forbids uncertainty becoming permission, and T3 permits a qualified authorized response. A20 §4 ties conflict to action a. The flat A23 fields do not identify the proposition required by the executing action. | `stop` with an established stopping basis can be permitted while `continue` on unresolved route safety cannot. If the uncertainty is material to stopping itself, or stopping lacks authority, the partial policy rejects it. A different-action example is not a coherent lift of an action-scoped `unresolved_material=True`; it demonstrates the missing scope correspondence. No universal R3 implication follows. |
| P5 | S10 requires recognition of the needed disposition; S14 requires an assessment at each transition; T2 expressly rejects a trace with no reliance consequence. The flat R5 records detection and disposition but has no state transition that binds the action to the current basis. | Implemented a separate candidate revision interlock. Recording cannot refresh qualification; qualification before a second change cannot authorize later execution. This is an explicit operational refinement under fixed assumptions, not evidence that the original route already enforced it everywhere. General canonical reachability remains open. |
| P6 | S9 targets unsupported convergence and silent substitution. A20 §4 tests pairs counted as independent. Flat A23 P6 instead demands independence for every active composition. | Shared-root records with no claim of independent corroboration do not violate the dependency part of A20 P6. Counting those same records as independent does. This resolves a specific over-strong target interpretation; compatibility and other S9 obligations are not certified by this check. The historical P6 formula remains intact. |

The source distinctions support model-translation/refinement findings, not a new canonical S15/T5/H7. The old three counterexamples still reproduce unchanged. P1/P2/P4 remain exact implications for their listed finite projections; full source fidelity is not established by decomposing a target across clauses. The prose source arguments in A23 must be read with that limit.

## Executed P5 transition check

The [runner](./semantic_bridge_review.py) represents qualification, observable material change, recorded disposition and attempted action for one decision. Qualification stores the current basis revision; actuation requires that revision still to match. A separate history oracle checks that the last qualification occurred after the last change, without reading the runner's revision variables.

All **5,460 event words of lengths one through six** over those four event types were enumerated. The interlock admits execution in **1,836 traces** and produces **zero stale-execution traces**. Removing the interlock produces **3,212 traces with stale or unqualified execution**. These are bounded model counts, not independent trials, real incident rates or general proof. Repeated changes and recording without requalification are included. A permanently blocking implementation would fail the positive controls.

Scope assumptions: changes are observed and declared material; one decision and one serialized event stream; fixed valid authority; qualification is treated as successful when its event occurs. Concurrent actuation, missed changes, expiry, distributed observation, adequacy of the qualification evidence and response costs are outside this diagnostic. The runner is not integrated into a production EA architecture. It demonstrates what the missing operational obligation does and that the mutation is detected.

## Reproduction and status

~~~bash
PYTHONDONTWRITEBYTECODE=1 python semantic_bridge_review.py --output replay-semantic.json
cmp semantic_bridge_certificate.json replay-semantic.json
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
~~~

Local result: **20 tests pass = 11 unchanged clause-audit tests + nine new semantic diagnostics**. [Certificate and example traces](./semantic_bridge_certificate.json). Existing CI discovers the additional test file automatically; local execution is not a claim of completed CI.

F02 has advanced to executable, scoped adjudication. It has not closed full canonical sufficiency. Remaining work includes a common typed refinement for all clauses, reachability under the full canonical obligations, representation of every applicable S/T dimension and independent semantic review. F01 remains open: no B1–B11 lifting certificate has been added to A22. A favorable count must not be obtained by deleting counterexamples or changing the frozen canon.
