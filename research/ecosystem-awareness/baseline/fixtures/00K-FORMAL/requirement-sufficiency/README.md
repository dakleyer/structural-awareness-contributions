# 00K-FORMAL/requirement-sufficiency — audited clause projections

> **Guard scope after audit:** shortcut rejection is clause-local. A target can be split across clauses that individually pass the guard, so guard success does not establish non-circularity or source fidelity of the whole bundle. Such decomposition is not itself proof of circularity either. P1/P2/P4 remain finite-projection implications; P3/P5/P6 and semantic fidelity remain open. [A14](./../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md).

Executable companion to [00K-A23](../../../00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md), **under semantic revision** after the [clause circularity audit](./CLAUSE_AUDIT.md). This package is outside the 379 symbolic ablation count.

The original all-six sufficiency claim is withdrawn. Nine individual clause/target equivalences passed the former 65,536-state exhaustive suite trivially. Rebuilt source projections retain implications for **P1/P2/P4** and countermodels for **P3/P5/P6**. These are partial Boolean translations; neither passing implications nor countermodels establish full real-world canonical conformance.

The model has 33 Boolean fields. The audit exhaustively enumerates exact support projections and validates syntactically that omitted fields cannot affect the result. The [certificate](./clause_audit_certificate.json) records every projection size, full-cube multiplicity, 22 clause-distinguishing comparisons and three replayable counterexamples. A guard rejects both exact clause/target equivalence and a clause that alone entails the target, including a copied target padded with another condition. Source fidelity still requires human review.

Run from this directory:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python audit_requirement_sufficiency.py --output replay.json
cmp clause_audit_certificate.json replay.json
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
~~~

Expected: **11 tests pass**, while the certificate says P3/P5/P6 are **not entailed**. Tests preserve that finding and reject reordered/padded/hidden-call regressions. A green CI is successful audit reproduction, not an all-six proof.

## Applied semantic follow-up

[Semantic bridge review](./SEMANTIC_BRIDGE_REVIEW.md) adds action/proposition and corroboration diagnostics plus a bounded P5 actuation-interlock experiment. The current suite has **20 tests: 11 existing + nine new**. The old certificate remains unchanged; all-six sufficiency remains unestablished. [New certificate](./semantic_bridge_certificate.json).
