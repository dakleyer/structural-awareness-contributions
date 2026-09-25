# A23 reconstruction execution record

**Review start:** 25 September 2026 Europe/Madrid; local execution recorded 26 September Europe/Madrid (25 September UTC). **Parent:** `aff0c3787d0b8ee5915a2fcde8ea0be5cecbbd9e`. This record concerns the audited clause reduction, outside the 379 ablation tests. See [audit](./CLAUSE_AUDIT.md) for scope and [certificate](./clause_audit_certificate.json) for the full witnesses.

Commands from this directory:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python audit_requirement_sufficiency.py --output replay.json
cmp clause_audit_certificate.json replay.json
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
~~~

Python 3.12.14: all three commands exit 0; **11 tests pass**, including regression detection for reordered targets, padded targets and hidden calls. The certificate reports P1/P2/P4 implication and P3/P5/P6 countermodels. No test counts a countermodel as a successful sufficiency result. Document integrity and the six-family registry also pass locally.

| Artifact | SHA-256 |
|---|---|
| [`requirement_sufficiency_model.py](./requirement_sufficiency_model.py) | `b1e32ab6b7868eb51beee62a9ff844fa9ea47c46132ffd17b6f93b7770fd12e5` |
| [`audit_requirement_sufficiency.py](./audit_requirement_sufficiency.py) | `c076a95dbe53400403a0c75a0159a7721f70ab06738bc48cbfef5d0c55d061c5` |
| [`test_requirement_sufficiency.py](./test_requirement_sufficiency.py) | `4280554082cdd062919eb39a58b32b148012af4cf087adcd387214bb17994789` |
| [`clause_audit_certificate.json](./clause_audit_certificate.json) | `d4df2ab543b3e349b4af6205420d5e7ebd70cbdf97ce7481351415251c380699` |

Canonical S/T source SHA-256: `36c5ed27590e7deb68aab9968410a9d0894b411bee3ecc238cdead1dc0eebc73`. The canonical source, P1–P6 formulas, original six scenario files and A1–A6 fixture code are unchanged. Fresh pytest runs are not claimed locally (pytest unavailable); use the linked CI run in [A12](../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md) for the published revision.


## Published revision and CI

Code and certificate were published in [`bf99a53cb34257ea8c3a80983eb5778d82f2bcb0`](https://github.com/dakleyer/structural-awareness-contributions/commit/bf99a53cb34257ea8c3a80983eb5778d82f2bcb0). [00K run 36195668166](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36195668166) succeeded on the PR integration checkout for this head, with all ten jobs successful. The full campaign job ran the requirement-conformance step (11 audit tests) and the distinct 346 core + 33 supplemental symbolic regression campaign (379 checks); A3, A4 and A6 also passed their individual jobs.

[Documentation integrity](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36195668174), [00L replay](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36195668158), and [Stage-0 replay](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36195668223) also succeeded for that head. These runs do not establish semantic fidelity, universal reachability or full canonical conformance. In particular, passing tests preserve the P3/P5/P6 countermodels rather than claiming their sufficiency. PR #1 remains unmerged.
