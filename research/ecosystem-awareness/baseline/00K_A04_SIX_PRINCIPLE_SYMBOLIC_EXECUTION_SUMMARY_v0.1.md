# 00K-A04 — Six-Principle Symbolic Execution Summary — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Status** | **All six principle ablations have a deterministic symbolic harness** |
| **Date** | 25 September 2026 |
| **Evidence class** | executable symbolic fixtures; not live agent/product/field evidence |

> **Central result at this evidence level.** All six operational principles now have an executable leave-one-principle-out fixture. In every current harness, the full principle route passes its frozen negative and positive/boundary controls. After ablation, the tested alternative repairs either fail a required branch or pass only by implementing an operationally equivalent form of the removed semantic invariant. **No TRUE SUBSTITUTE has been found in the tested repair surfaces.**

> **Methodological falsifier retained.** This sentence refers to the **current isolated core harnesses**. The supplemental A6a run against the unmodified 00G F/G pair **does find a TRUE SUBSTITUTE** (authority-only), proving that the original pair was confounded for P6 necessity. The core A6 result is the corrected matched-authority isolation; see [00K-A06](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).

> **Boundary.** This is not a proof of universal minimality, not a formal theorem, and not evidence that present commercial technologies fail these tests in production. It is stronger than prose-only reasoning because the claims are encoded as executable branch conditions, but the fixtures remain deliberately small symbolic models.

---

## 1. Execution matrix

| Ablation | Principle under test | Scenario anchor | Frozen branch pair / controls | Current symbolic result | Strongest passing repair | 00K classification |
|---|---|---|---|---:|---|---|
| **A1 / −P1** | Qualified determination / evidence→proposition→decision sufficiency | **00J — Rights-Provenance Inversion** | unsupported generation provenance vs legitimate rights grant | **13/13** | typed evidence/proposition schema | **SEMANTIC RECONSTRUCTION of P1** |
| **A2 / −P2** | Bounded unresolved effort / viable oversight | **00E — 100 Million Tokens** | unresolvable repeated search vs positively resolvable bounded search | **13/13** | budgeted decision-relevant search | **SEMANTIC RECONSTRUCTION of P2** |
| **A3 / −P3** | No false closure from unresolved material state | **00F — Chaos in the Smartcity** | incompatible shared-corridor postures vs continuity / determinate Plan A | **15/15** | explicit three-valued unresolved-state closure | **SEMANTIC RECONSTRUCTION of P3** |
| **A4 / −P4** | Qualification-preserving handoff / authority lineage | **00H — The Quiet Four Thousand** | U unauthorized campaign / G authorized campaign / I independent cases / NM | **29/29 active composed harness** | A2-L explicit root/delegation lineage | **SEMANTIC RECONSTRUCTION of P4** |
| **A5 / −P5** | Material-change requalification at time of use | **00I — Semantic TOCTOU** | stale queued action vs valid continuity + unavailable-current-source control | **14/14** | full material-basis compare/binding before actuation | **SEMANTIC RECONSTRUCTION of P5** |
| **A6 / −P6** | No local→ecosystem promotion / non-substitution | **00G — matched-authority isolation of False-Context Convergence** | same authority/count/confidence/freshness; correlated-source F vs independent-source G | **17/17** | source-independence / dependency-aware peer | **SEMANTIC RECONSTRUCTION of P6** |

**Current core after bounded-grid hardening:** **101 passing symbolic tests** across the six isolated principle harnesses.

**Supplemental adversarial surface:** A6a naive-pair falsifier **10**, A6b independent 00F P6 isolation **11**, and independent cross-scenario kernels **12** — **33 supplemental tests**.

**Full registered campaign:** **134 tests**.

**Independent CI reproduction:** GitHub Actions [full campaign run](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36100046965) completes successfully across all **10 jobs** on Python 3.13: the six core harnesses, A6a, A6b, cross-scenario kernels and the aggregate campaign gate. The aggregate job verifies **101/101 core + 27/33 supplemental = 128/128**. The earlier 101-only run and 89-test pre-grid run remain part of Git history as milestones.

The count is a regression/execution count, **not a scientific score**: one pytest assertion is not one independent experiment. The evidentiary content is the branch structure, the attempted substitutes and the falsifiable distinction between TRUE SUBSTITUTE and SEMANTIC RECONSTRUCTION.

---

## 2. What is now tested in code

The six harnesses jointly encode the following claim:

```text
full P1–P6 route
    -> passes the selected negative branch
    -> also passes the matched positive/boundary control

remove Pk
    -> allow strongest fair Pk-blind repairs
    -> do not force use of the S# mapping
    -> if repair fails a branch: FAILED SUBSTITUTE
    -> if repair succeeds only by rebuilding Pk's invariant:
         SEMANTIC RECONSTRUCTION
    -> if repair succeeds without Pk semantics:
         TRUE SUBSTITUTE -> necessity claim loses
```

This is important: **S1–S14 are instrumentation and traceability, not the causal proof.** The code is allowed to solve the fixture by any route it can find.

---

## 3. Principle-specific discriminants

### P1 / 00J — what does the evidence actually establish?

A signed, fresh generation-provenance record can be perfectly valid while failing to establish the stronger proposition `RIGHT_TO_ENFORCE_AGAINST_AUTHOR`.

The P1-blind repairs tested include:

- accept any valid signed record;
- preserve provenance perfectly;
- refresh every record;
- require independent replicated records; and
- deny all.

The passing strong peer succeeds only by typing the evidence and binding it to the proposition it can actually support.

**Fixture-level discriminant:** evidence validity ≠ proposition sufficiency.

---

### P2 / 00E — when must determination effort stop?

The negative branch keeps returning non-decision-relevant evidence until capacity is exhausted. The positive branch becomes resolvable after three bounded steps.

The P2-blind repairs can preserve UNKNOWN and avoid false closure yet still search/review until capacity is exhausted. A crude one-step timeout prevents exhaustion but rejects the positive branch.

The passing peer uses a finite decision-relevant budget and bounded no-conclusion exit.

**Fixture-level discriminant:** epistemic honesty alone does not provide a stopping rule.

---

### P3 / 00F — may unresolved material state become permission?

The negative branch is fresh and fully visible but internally incompatible: Plan A, Plan B, NORMAL and HOLD compete over one shared corridor.

Majority/default, timeout/default, perfect preservation, freshness and conflict detection can all coexist with a final forced NORMAL/PASS. Deny-all fails continuity.

The passing peer introduces an explicit unresolved/non-permission state while still allowing determinate NORMAL and authorized Plan A branches.

**Fixture-level discriminant:** detecting uncertainty/conflict ≠ forbidding false operational closure.

---

### P4 / 00H — can U and G be separated without authority-bearing lineage?

The strongest current A4 fixture holds finding, local grants, campaign identity, timing and volume constant across U/G. The material distinction is current root/campaign authority.

The reviewed v0.2 package independently passes **21/21** and adds the explicit four-arm comparison. The active browsable harness preserves the earlier reviewed source and adds NM/A2-L/four-arm, P4-blind indistinguishability sweeps and the bounded authority/volume grid, yielding a **29-test** regression surface.

A2-L is intentionally not EA-branded. It passes by implementing explicit root/delegation lineage and non-amplification.

**Fixture-level discriminant:** local/leaf validity + composition awareness ≠ authority for the composed effect.

---

### P5 / 00I — can a once-valid decision remain usable after its basis changes?

The continuity and stale branches share the same queued Patch A, original grant and original decision basis. The material distinction exists in current state at use time.

Queue-time qualification, perfect Patch-B provenance, conflict visibility and database serialization all leave the stale action executable. Deny-all fails continuity.

The original generation compare passes the first stale branch, but the bounded-grid audit shows that a generation-only check is **not sufficient for the full P5 invariant**: it misses incident-only, freeze-only and source/policy-version-only changes when the configuration generation itself is unchanged.

The strengthened passing peer binds actuation to the **full declared material decision basis** (generation, incident state, freeze state and source/policy version in this fixture) and reopens qualification on any material mismatch.

**Fixture-level discriminant:** preservation/serialization — and even one narrow version check — ≠ current semantic applicability of the complete decision basis.

---

### P6 / 00G — can correlated consensus be distinguished from independent support?

**Isolation correction.** The unmodified 00G F/G pair is not sufficient for P6 necessity because authority also differs. The [A6a falsifier](./fixtures/00K-A6a-P6-00G/README.md) finds an authority-only TRUE SUBSTITUTE for that naive pair. The canonical A6 result below therefore refers specifically to the **matched-authority** executable fixture; [A6b / 00F](./fixtures/00K-A6b-P6-00F/README.md) supplies an independent shared-resource composition isolation. See [00K-A06](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).


The P6 harness deliberately holds **transition authority constant** across false Branch F and genuine Branch G. Both have five authenticated, fresh, high-confidence claims. The material distinction is source dependence:

- F: five agents inherit one source;
- G: five agents use three materially independent sources.

Identity quorum, confidence thresholds, raw provenance preservation and human majority all false-transition F. Deny-all fails G. The strong peer passes by counting materially independent evidence paths.

**Fixture-level discriminant:** participant/message plurality ≠ independent evidence.

---

## 3A. Bounded-grid hardening

The additive [**00K-A05 bounded-grid hardening audit**](./00K_A05_BOUNDED_GRID_HARDENING_AND_P5_AUDIT_v0.1.md) expands each harness beyond its first exact branch pair without rewriting the reviewed source. It adds controlled grids over evidence types/replication, resolution position/budget, mixed postures, authority validity/campaign volume, material basis fields and source-diversity/Sybil count.

The robustness pass increases the active regression surface from **89 to 101 passing symbolic tests** and, importantly, exposes the original P5 generation-only repair as a **partial** implementation rather than the complete semantic invariant.

## 4. Falsification remains open

Each harness is constructed so the principle can still lose.

A **TRUE SUBSTITUTE** must:

1. pass the same negative branch;
2. pass the matched positive/boundary branch;
3. stay inside the same declared resource/authority boundary;
4. avoid hidden oracle access;
5. avoid blanket deny/HOLD/accept-all shortcuts; and
6. solve the branch **without implementing an operationally equivalent form of the removed principle's fixed invariant**.

If such a mechanism is found, it is evidence against the necessity of that P# and the 00K decomposition must be revised.

---

## 5. Executable package routes

- [A1 / P1–00J](./fixtures/00K-A1-P1-00J/README.md)
- [A2 / P2–00E](./fixtures/00K-A2-P2-00E/README.md)
- [A3 / P3–00F](./fixtures/00K-A3-P3-00F/README.md)
- [A4 / P4–00H active harness](./fixtures/00K-A4-P4-00H/README.md)
- [A4 reviewed v0.2 package + independent verification](./fixtures/00K-A4-P4-00H-v0.2/README.md)
- [A5 / P5–00I](./fixtures/00K-A5-P5-00I/README.md)
- [A6 / P6–00G matched-authority isolation](./fixtures/00K-A6-P6-00G/README.md)
- [A6a / P6–00G naive-pair falsifier](./fixtures/00K-A6a-P6-00G/README.md)
- [A6b / P6–00F composition isolation](./fixtures/00K-A6b-P6-00F/README.md)
- [Complete symbolic suite router](./fixtures/00K-SUITE/README.md)

---

## 6. Evidence ladder after this milestone

The six-principle programme now has four distinct levels:

1. **Documentary coverage:** S1–S14 are exercised across 00E–00J.
2. **Principle mapping:** S1–S14 are traced to P1–P6 without using that mapping as causal proof.
3. **Executable symbolic ablation:** all six P# now have negative + positive-control code and strongest-repair attempts.
4. **Next level — stronger execution:** property-based/fuzzed fixtures, independent reimplementation, and eventually matched real technology/runtime execution where feasible.

The current result is therefore best described as:

> **complete first-pass executable symbolic coverage of the six-principle ablation design, with provisional semantic-necessity support for P1–P6 inside the declared six-scenario fixture boundary.**

It is not yet empirical validation of the production architectures or universal proof that no seventh/fifth/different principle system can do better.
