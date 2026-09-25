# 00K-A6a — P6 / 00G falsification-first symbolic execution

**Removed principle:** P6 — no local-to-ecosystem promotion / non-substitution  
**Scenario:** 00G — *Ciber Napoleon Goes to Russia*  
**Status:** deterministic symbolic execution; not live agent/product evidence

## Why this run matters

This fixture was executed **without protecting the intended P6 result**. It
reveals a genuine experimental confound in the original 00G Branch F / Branch G
pair: the two branches differ in both evidence independence **and** applicable
mission-transition authority.

## Result

The suite passes **10/10**, but the important result is a **TRUE SUBSTITUTE**
for this specific F/G pair:

- identity quorum and confidence threshold fail Branch F;
- deny-all fails Branch G;
- provenance-preserving identity counting still fails Branch F;
- **authority-only**, without inspecting source independence at all, rejects F
  and accepts G exactly as Route Q does.

Therefore **00G F/G alone does not establish P6 necessity**. The authority
difference is sufficient to discriminate the pair.

This is evidence that the 00K method is capable of returning a result against
its own initial mapping rather than classifying every successful repair as
semantic reconstruction.

## Consequence

The P6 necessity test must be isolated on a branch where authority/local
validity are matched and only cross-participant composition differs. The
companion fixture [00K-A6b — P6 / 00F](../00K-A6b-P6-00F/README.md) performs
that isolation using 00F's shared-corridor composition pressure.

## Boundary

This is a fixture-level counterexample to **the original 00G necessity test**,
not evidence that P6 is unnecessary in general.
