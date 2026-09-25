# 00K-A13 — Six-Principle Serious Ablation Completion Review — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Status** | **Serious symbolic hardening completed for P1–P6** |
| **Date** | 25 September 2026 |
| **Evidence class** | deterministic symbolic fixtures + falsification-first methodological corrections; not live product/field evidence |

> **Current result.** All six operational principle families now have both a documented ablation route and executable Python harnesses hardened beyond first-pass/naive substitutes. The core surface is **346 symbolic tests**. Supplemental falsification/isolation/cross-scenario packages add **33**, for a registered campaign of **379 tests**. The count is regression coverage, not 379 independent scientific experiments.

---

## 1. Completion matrix

| Principle | Primary scenario / isolation | Current core | Serious-repair result | Methodological correction / refinement | Current bounded disposition |
|---|---|---:|---|---|---|
| **P1** | 00J matched-semantic rights-provenance isolation | **42** | trusted issuer, provenance, schema, confidence, quorum, human approval and reputation do not separate matched branches; evidence→proposition→decision policy does | original issuer/source-varying pair admits a **TRUE SUBSTITUTE** and is rejected as necessity isolation | **bounded semantic necessity supported after corrected isolation** |
| **P2** | 00E matched-prefix late-resolution family | **58** | TTL, circuit breaker, parallelism, scheduler and probe alternatives pass only when they introduce a viable finite stopping/fallback rule | no separate confound found in hardened matched-prefix family | **bounded semantic necessity supported** |
| **P3** | 00F matched-conflict corridor isolation | **49** | authority/confidence/freshness priority, majority, human/default and risk heuristics false-close; non-permission/unanimity/intersection peers pass | original HOLD-marked base branch admits a literal-HOLD shortcut and is rejected as necessity isolation by itself | **bounded semantic necessity supported after corrected isolation** |
| **P4** | 00H matched U/G/I/NM authority composition | **76** | RBAC, volume, amount, risk, allow-list and non-owner approval fail; lineage, scoped capability, legitimate maker-checker and owner-side PDP pass | **full historical receiver-side lineage is not necessary**; opaque scoped PDP permit passes without exposing delegation history | **minimal authority-qualification/non-amplification invariant supported; P4 wording refined** |
| **P5** | 00I exhaustive material-basis mutation grid | **47** | all 16 field subsets enumerated; TTL/serialization/idempotency/human reapproval fail; full hash/vector/event/epoch peers pass | generation-only compare exposed as partial | **bounded semantic necessity supported** |
| **P6** | 00G matched-authority + transitive-dependency isolation; 00F corroboration | **74** | identity/org/direct-source/confidence/time/content/human/reputation alternatives fail hidden common-root branch; dependency graph/effective-root peers pass | original F/G pair admits authority-only TRUE SUBSTITUTE; direct immediate-source count exposed as partial | **bounded semantic necessity supported after corrected isolation** |

---

## 2. What “complete” means here

For each P1–P6 the corpus now contains:

1. **reader-facing ablation route** tied to an existing 00E–00J failure mechanism;
2. **frozen negative and positive/boundary controls**;
3. **explicit invariant lock before repair search**;
4. **multiple serious alternatives**, including conventional/non-EA mechanisms;
5. **TRUE SUBSTITUTE / SEMANTIC RECONSTRUCTION / FAILED SUBSTITUTE** classification;
6. **Python implementation** of the reduced fixture;
7. **parameter sweeps / bounded grids / exhaustive reduced subspaces** where useful;
8. **falsifier statement** saying what would overturn the current result; and
9. **claim boundary** separating symbolic fixture evidence from live technology evidence.

That is the completed symbolic-ablation layer. It is not the end of empirical validation.

---

## 3. Important negative results retained

The programme did not simply return six desired passes.

### P1

The original A1 pair changed both semantic proposition and issuer/source/record class. A source-authority-only rule was therefore a genuine TRUE SUBSTITUTE for that pair.

**Disposition:** old pair rejected; corrected matched-semantic isolation required.

### P3

The original base conflict contained an explicit `HOLD` posture. A literal HOLD-veto rule could pass that base branch without implementing general unresolved-state semantics.

**Disposition:** base branch insufficient alone; corrected no-HOLD matched conflict required.

### P4

A full root→leaf history at the relying component turned out to be stronger than 00H actually requires. A legitimate owner-side scoped PDP/capability can pass without exposing historical lineage.

**Disposition:** P4 narrowed to the minimal decision-sufficient current authority qualification / non-amplification invariant. Full lineage remains one implementation, not the demonstrated universal requirement.

### P6

The original 00G false/genuine pair changed both evidence independence and transition authority. Authority-only was therefore a TRUE SUBSTITUTE for the naive pair.

**Disposition:** original pair rejected as P6 isolation; authority-matched + transitive-dependency fixture used instead.

These negative results are part of the evidence because they show the method can reject the programme's own first formulation.

---

## 4. Current code surface

Core harnesses:

- [P1 / 00J](./fixtures/00K-A1-P1-00J/README.md) — **42**
- [P2 / 00E](./fixtures/00K-A2-P2-00E/README.md) — **58**
- [P3 / 00F](./fixtures/00K-A3-P3-00F/README.md) — **49**
- [P4 / 00H](./fixtures/00K-A4-P4-00H/README.md) — **76**
- [P5 / 00I](./fixtures/00K-A5-P5-00I/README.md) — **47**
- [P6 / 00G](./fixtures/00K-A6-P6-00G/README.md) — **74**

**Core = 346.**

Supplemental:

- P6 original-pair falsifier — **10**
- P6 independent 00F isolation — **11**
- independent cross-scenario kernels — **12**

**Supplemental = 33.**

**Registered campaign = 379.**\n\nFor the consolidated reader-facing route that puts the six narrative ablations and executable Python surfaces side by side, use [**00K-A15 — Complete Six-Principle Ablation Testbook**](./00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md).

The [00K suite router](./fixtures/00K-SUITE/README.md), execution-lock manifest and GitHub Actions workflow use the current counts. [GitHub Actions run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548) independently reproduces **346/346 core + 33/33 supplemental = 379/379** across all 10 jobs; see [00K-A14](./00K_A14_GITHUB_ACTIONS_REPRODUCTION_379_v0.1.md).

---

## 5. What the six-principle result now supports

At the present symbolic evidence level, the defensible statement is:

> **Across the declared corrected 00E–00J-derived symbolic fixtures, each of the six operational principle families has survived a leave-one-out strongest-repair search after known confounds were controlled. Where a competing architecture passes, it either implements an operationally equivalent form of the principle or, in P4's case, reveals that the principle should be stated at a more minimal authority-qualification level than full lineage preservation. No TRUE SUBSTITUTE has been found for the corrected minimal P1–P6 invariants in the current serious-repair surfaces.**

This does **not** establish:

- universal minimality;
- a mathematical proof that no future substitute exists;
- live failure of any named product;
- empirical superiority of Ecosystem Positioning;
- that every implementation must expose the same fields/interfaces; or
- that the six principles are the only possible abstraction of the same safety properties.

---

## 6. Next evidence level

The next meaningful increment is no longer another naive unit test. It is to move selected hardened fixtures into stronger execution environments while preserving the same falsification rules:

1. **completed:** independently reproduce the current **379-test** campaign in repository CI — 379/379 on run 36108965548;
2. execute the same branch oracles with more realistic stateful agent/workflow substrates;
3. maintain matched resources, authority and evidence access;
4. allow strong conventional peers to add any native controls they can justify;
5. record a TRUE SUBSTITUTE as evidence against the corresponding principle rather than absorbing it retrospectively; and
6. keep symbolic necessity, live technology differential and architecture-specific implementation claims as separate evidence layers.

The symbolic layer is now sufficiently complete to serve as the preregistered test contract for that next stage.
