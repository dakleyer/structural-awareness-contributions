# 00K — Independent Cross-Scenario Kernel Reimplementation

**Status:** additive symbolic robustness test  
**Purpose:** reduce scenario-tailoring and shared-code confirmation bias.

This package intentionally imports **none** of the six A1–A6 harness modules. It reimplements three compact semantic kernels independently and applies each to two materially different scenario families.

| Principle kernel | Scenario 1 | Scenario 2 |
|---|---|---|
| **P4 — non-amplifying qualification/authority lineage** | 00H campaign authority | 00J rights/provenance lineage |
| **P5 — material-basis currentness before use** | 00I semantic TOCTOU | 00H authority/membership change before action |
| **P6 — independent support, not participant count** | 00G false/genuine frame | 00F correlated/independent mobility evidence |

The point is not that three short functions prove the principles universally. The point is that the same invariant can be re-expressed independently and still discriminate the expected positive/negative branches in another scenario family.

Run:

```bash
python -m pytest -q
```

Expected: **6/6**.

This package is supplemental to the 101-test core ablation regression surface; its tests are reported separately so cross-scenario reuse is not confused with additional independent principle proofs.
