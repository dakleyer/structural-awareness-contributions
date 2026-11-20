# Source-preserving evidence entry point for #57

Use [unit_safe_evidence.py](unit_safe_evidence.py) for the architectural review of #57 and audit #58. It depends on the shared measured-outcome contract in the #66 unit-safe implementation; the PR is stacked on that implementation so reviewers can inspect each change separately.

## What this strengthens

EA's contribution includes **task-relevant information and qualified possibilities**, not only an executed physical transition. The corrected report keeps the original conditional Q signals visible, including Q_REVIEW_ONLY when no transfer occurs. In AG01, Q+meta still produces **11.5 from baseline 10 with the same total physical resource budget**; its information price is reported independently, and the instrument's conditional information signal is retained. These are source-generated Stage-A results, preserved exactly.

Every one of the **30×6 original outcomes and the exact 160-cell parameter grid** is replayed. Reports preserve source plans/statuses, physical outputs, itemized instrument prices, conditional information signals, post-hoc claim support, and the complete physical resource ledger. The physical overhead remains inside the conserved resource budget and is never charged again as an information price. The report also exposes equal-output price comparisons wherever the source actually supplies them.

No information acquisition price is subtracted from mission output. Output gain and price are independent observations. A supplied conventional Q is an **information-equivalence control**; its label does not establish that EA's discovery/qualification/requalification work is unnecessary or that ordinary monitoring solves open ecosystem awareness.

## Minimal source crosswalk

[Author notes S1-P0205, P0208, P0220 and P0280](../../model/01_NOTAS_COMPLETAS.md#s1-p0205) own open, nonfungible K. [The shared crosswalk and source review](../intrinsic-abcd-economics-v0.1/UNIT_SAFE_EVIDENCE.md) distinguish R, C, E and V, toy coefficients, epistemic A/B/C/D and instrument measurements. The original author's examples, original engines, frozen reference JSON and controlled 00M/00N remain intact.

Capabilities, consent, authority, protocol availability and the material epistemic witness are reported in **separate typed controls**. True/False/None means PASS/FAIL/UNKNOWN for a control; strings and numeric stand-ins fail validation. A favorable measurement does not change these controls or authorize a transition. This is how the information result remains visible without confusing Awareness with an executor.

```sh
python -B unit_safe_evidence.py
python -B -m unittest test_unit_safe_evidence -v
```

## Reviewer checks and unresolved author choices

- Compare every measured value and source status with unchanged `agentic_reduction.run_case`; compare sweep IDs and physical gain signs with unchanged `sensitivity.run_sweep`.
- Reconcile donor resources + recipient resources + coordination resources with the original budget. Confirm there is no second monetary charge for overhead.
- Check false Q, blocked consent, missing capability and failed protocol cases remain visible. Unknown control evidence must never become PASS.
- Check Q_REVIEW_ONLY retains its conditional information signal even where physical output does not increase. Do not substitute a physical mission metric for all of EA's possible utility.
- Retain #76's tested R/C separation; do not export a scalar Nash-game result into open K.
- **Requires author criterion:** replacing native scalar planning thresholds, assigning physical outputs/prices/overhead to canonical economic dimensions, choosing among K tradeoffs or accepting a conversion. These are deliberately left as decisions, not invented in a reporting fix.

The report strengthens the reproducible evidence; it does not rewrite EA's hypotheses, define new economic dimensions or change audit adjudication. The original scalar source reports remain historical conditional diagnostics. The corrected evidence report is the entry point proposed for review.

