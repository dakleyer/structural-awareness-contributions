# 00K-A05 — Bounded-Grid Hardening & P5 Repair Audit — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Prior execution summary** | [00K-A04 — Six-Principle Symbolic Execution Summary](./00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md) |
| **Status** | **Additive robustness pass completed** |
| **Date** | 25 September 2026 |
| **Evidence class** | deterministic bounded-grid/property-style symbolic testing |

> **Purpose.** Reduce dependence on one hand-picked negative/positive pair per principle without rewriting the already-reviewed harnesses. Each harness receives an additive bounded-grid test file. The grid expands the input surface while preserving the fixed principle invariant and the same falsification rule: a TRUE SUBSTITUTE must pass the negative and positive/boundary branches without reconstructing the removed principle.

## 1. Result

The six harnesses now pass:

| Principle | Previous | Added bounded-grid tests | Current |
|---|---:|---:|---:|
| **P1 / 00J** | 11 | +2 | **13/13** |
| **P2 / 00E** | 11 | +2 | **13/13** |
| **P3 / 00F** | 13 | +2 | **15/15** |
| **P4 / 00H** | 27 | +2 | **29/29** |
| **P5 / 00I** | 12 | +2 | **14/14** |
| **P6 / 00G** | 15 | +2 | **17/17** |

**Aggregate symbolic regression surface: 101 passing tests.**

GitHub Actions independently reproduces the six updated counts in [run #10](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36091807530): **completed / success**, all six matrix jobs successful.

The count remains a regression-coverage count, not 101 independent scientific experiments.

---

## 2. What the grids add

### P1 — evidence type and replication

The A1 grid varies unsupported proposition types and independently replicated records.

Result:

- signatures, freshness and independent replication do not upgrade a record that supports the wrong proposition;
- an actual rights-enforcement proposition remains executable;
- repeated generation-provenance records remain insufficient no matter how many independent copies exist.

This hardens the P1 claim against the objection that the original fixture used only one misleading record.

### P2 — resolution-position × budget grid

The A2 grid varies:

- the step at which genuinely decision-relevant evidence becomes resolving; and
- the finite determination budget.

Result:

- a budgeted peer executes exactly when the resolution point is reachable inside the budget;
- otherwise it exits as explicit no-conclusion;
- the P2-blind search continues to capacity exhaustion.

This makes the stopping rule a measurable boundary rather than a single arbitrary timeout.

### P3 — exhaustive mixed-posture grid

The A3 grid enumerates mixed NORMAL / PLAN_A posture combinations over several widths.

Result:

- every mixed material state remains unresolved under the P3-aware route;
- uniform determinate states remain executable;
- majority/default rules produce multiple false-closure counterexamples.

This removes dependence on the one original PLAN_A / PLAN_B / NORMAL / HOLD tuple.

### P4 — root-authority validity × campaign-volume grid

The A4 grid varies:

- absent root authority;
- invalid root authority;
- expired root authority;
- current valid root authority; and
- several campaign volumes.

Result:

- Route Q and A2-L separate U/G on authority validity rather than volume;
- the same branch distinction holds across campaign-size variation.

This complements the reviewed rate-cap result: volume can block, but authority-bearing lineage is what discriminates U from G.

### P5 — material-basis field grid

The A5 hardening produced the most important audit correction.

The earlier minimal fixture showed that a **generation compare** can separate the original stale branch from continuity. The bounded grid changes one material basis field at a time:

1. configuration generation;
2. incident state;
3. freeze state; and
4. source/policy version.

Result:

- generation-only compare catches the generation change;
- it **misses incident-only, freeze-only and source/version-only changes**;
- a full-basis compare-before-act requalifies all four and preserves continuity.

Therefore the earlier phrase “generation/version compare is the strongest passing P5 repair” is too broad if read universally. The stronger and more accurate reconstruction is:

> **action-time binding to the declared material decision basis, using generation/version/epoch/fingerprint or equivalent mechanisms sufficient to detect every material field in scope.**

This does not weaken P5. It strengthens the test by showing that one narrow implementation of P5 is itself insufficient for the broader invariant.

### P6 — source-diversity × Sybil-count grid

**Isolation note.** This grid belongs to the corrected **matched-authority** A6 fixture. The unmodified 00G F/G scenario pair changes both evidence independence and transition authority and therefore admits an authority-only TRUE SUBSTITUTE. That confound and its correction are recorded separately in [00K-A06](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).

The A6 grid varies:

- number of authenticated participants;
- number of materially independent source lineages; and
- Sybil/message count with one common source.

Result:

- the dependency-aware peer transitions exactly when the declared independent-source threshold is met;
- adding more authenticated agents on one source never creates independent evidence;
- identity quorum continues to false-transition the single-source branch once its count threshold is met.

This strengthens the distinction between identity plurality and evidentiary independence.

---

## 3. Scientific consequence

The robustness pass changes the status of the claim in one useful way:

The first-pass harnesses showed that **one** selected branch pair per principle could be encoded and falsified.

The bounded-grid pass shows that the same semantic distinctions survive controlled variation around those branch pairs.

It still does **not** establish universal necessity. It provides stronger fixture-level evidence that the result is not solely an artefact of one numeric threshold or one exact trace.

---

## 4. Preserved-source rule

No previously reviewed A4 source was rewritten for this hardening.

The additions are separate files:

- A1: `test_ablation_A1_grid.py`
- A2: `test_ablation_A2_grid.py`
- A3: `test_ablation_A3_grid.py`
- A4: `test_ablation_A4_grid.py`
- A5: `p5_strong_peer.py` + `test_ablation_A5_grid.py`
- A6: `test_ablation_A6_grid.py`

The original tests remain visible and independently attributable in Git history.

---

## 5. Next strengthening level

The next useful evidence increment is no longer “add more prose.” It is:

1. independent second implementations that do not import the first harness helpers;
2. cross-scenario reuse of the same principle kernel;
3. matched burden/resource ledgers for TRUE SUBSTITUTE versus SEMANTIC RECONSTRUCTION;
4. randomized/property-based generation around the frozen oracles; and
5. real runtime implementations where the cost is justified and the technology boundary can be kept fair.

A passing independent substitute remains a valid falsifier of any P# necessity claim.
