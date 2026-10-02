<a id="hugging-face-código-y-resultados-de-la-validación-acotada"></a>
# Hugging Face: bounded validation code and results

[Case document](../README.md) · [00G-R01](../../../README.md) · [Extensions table](../../../README.md#extensiones)

| File | Function |
|---|---|
| [check.py](../check.py) | Check of synthetic correspondence and counterexamples. |
| [results.json](../results.json) | Exact checker results. |
| [coverage.json](../coverage.json) | Documentary matrix of coverage and pending obligations; not automatic certification. |
| [SHA256.json](../SHA256.json) | Integrity hashes of the case record files. |

**Common procedure:** from `00G-R01/`, run `python3 extensions/verify_audit.py --verify`. It recalculates the three checks in temporary folders, compares recorded reports and verifies textual hashes. [Criteria and scope](../../CRITERIA_AND_AUDIT.md) · [Common guide from R01](../../../README.md#reproducción-conjunta-de-las-comprobaciones).

From the `hugging-face/` case folder:

```sh
python3 check.py
```

From this `proof/` subfolder, the equivalent command is `python3 ../check.py`. Only the Python standard library is used. The script regenerates `results.json` alongside `check.py`.

Published code and result locations are retained to maintain their links. This guide provides the same reproduction entry as in Infoblox.

**Scope:** finite synthetic model; not an agent execution, historical reproduction, complete R01 admission or EA comparison. The [validation document](../README.md#4-comprobación-reproducible-ejecutada) fixes the hypotheses and limits.
