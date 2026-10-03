<a id="comprobación-finita-de-r01--aplicación-dns"></a>
# Finite check of R01 → DNS application

[Integrated document v0.5](../README.md#6-prueba-acotada-y-resultados-del-modelo) · [00G-R01](../../../README.md)

**Incident scope:** Reproduction here means rerunning the declared synthetic model, not reproducing a historical incident or establishing its cause. Failure or success of this check does not refute or verify the occurrence of the motivating incidents. See the [scenario scope](../README.md#incident-scope) and the [common evidence rule](../../CRITERIA_AND_AUDIT.md#historical-and-constructed-scope).

This package checks an exact synthetic model with the Python 3 standard library. It uses no network, credentials, Infoblox APIs, DNS traffic, cryptography or LLM agents.

**Common procedure:** from `00G-R01/`, run `python3 extensions/verify_audit.py --verify`. It recalculates the three checks in temporary folders, compares recorded reports and verifies textual hashes. [Criteria and scope](../../CRITERIA_AND_AUDIT.md) · [Common guide from R01](../../../README.md#reproducción-conjunta-de-las-comprobaciones).

From this folder:

```sh
python3 check.py
```

The program checks its assertions and regenerates `results.json` alongside the script. Results are exact rationals, not statistical estimates. Code and results retain the bytes of the check accompanying Word v0.5.

The model grants a complete directory and represents strict execution control. Under the contract of limited evidence access, difficulty reaching the optimum within budget may persist, even without executed violations. The positive control with a sufficient, accessible certificate eliminates that difficulty. Neither a universal impossibility of available technologies nor an EA advantage is proved.

Section 6 of the document fixes the hypotheses, synthetic costs, transfer direction, curves and limits. Real integration, complete probabilistic and social exploration, X4/X7 and the paired EA comparison remain pending. This checker replaces neither the pending complete 00G-R01 evaluator nor the C3 oracle.

<a id="integridad"></a>
## Integrity

`../SHA256.json` contains hashes of the reading document, Word, script, results and this README. The source document and historical references are preserved; this folder publishes only the document and its verification kernel.
