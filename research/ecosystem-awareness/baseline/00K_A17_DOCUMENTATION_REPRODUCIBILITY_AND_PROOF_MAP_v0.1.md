# 00K-A17 — Documentation, Reproducibility & Proof Map — v0.1

| | |
|---|---|
| **Scope** | complete navigation map for the 00K six-principle ablation workstream |
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Current executable testbook** | [00K-A15](./00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) |
| **Corpus-grounded formal proof** | [00K-A16](./00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) |
| **Pure mathematical proof** | [00K-A18](./00K_A18_PURE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) |
| **CI reproduction** | [00K-A14](./00K_A14_GITHUB_ACTIONS_REPRODUCTION_379_v0.1.md) |
| **Date** | 25 September 2026 |

> **Purpose.** Give a reviewer one stable map for the complete 00K material: preserved design history, requirements coverage, six reader-facing ablations, executable Python, methodological falsifiers, serious-repair hardening, formal independence proof and CI reproduction.

---

## 1. Recommended reading route

For a new technical reviewer:

1. [**00K main protocol**](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) — what is being tested and how TRUE SUBSTITUTE / SEMANTIC RECONSTRUCTION / FAILED SUBSTITUTE are classified.
2. [**A02 Requirements Coverage Matrix**](./00K_A02_REQUIREMENTS_COVERAGE_MATRIX_ADDENDUM_v0.1.md) — why S1–S14 already matter across 00E–00J.
3. [**A15 Complete Six-Principle Ablation Testbook**](./00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) — all six narrative routes + Python surfaces in one place.
4. [**A13 Completion Review**](./00K_A13_SIX_PRINCIPLE_SERIOUS_ABLATION_COMPLETION_REVIEW_v0.1.md) — current bounded scientific interpretation.
5. [**A18 Pure Mathematical Independence Proof**](./00K_A18_PURE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) — self-contained model-theoretic proof using only abstract semantic definitions; no fixture/test premise.
6. [**A16 Formal Relative Independence Proof**](./00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) — mathematical non-derivability / irredundancy theorem.
7. [**A14 CI Reproduction Record**](./00K_A14_GITHUB_ACTIONS_REPRODUCTION_379_v0.1.md) — repository-level independent execution of 379/379 symbolic tests.

---

## 2. Document family

| Document | Role | Current use |
|---|---|---|
| **00K** | controlling principle-first ablation protocol | current normative test method |
| **A01** | verbatim preserved pre-principle-first 00K state | provenance / conservation only |
| **A02** | S1–S14 × 00E–00J documentary coverage matrix | pre-ablation evidence |
| **A03** | P4/00H deterministic paper execution | paper precursor to executable A4 |
| **A04 Execution Summary** | consolidated symbolic campaign summary | current execution overview |
| **A05** | earlier bounded-grid / P5 audit milestone | historical execution milestone; later hardening supersedes counts, not reasoning |
| **A06** | P6 authority-confound falsifier & corrected isolation | methodological negative result |
| **A07** | P1 issuer/source confound falsifier & corrected matched semantics | methodological negative result |
| **A08** | P2 matched-prefix strongest-repair audit | serious P2 hardening |
| **A09** | P3 HOLD-marker confound falsifier & corrected matched conflict | serious P3 hardening |
| **A10** | P4 minimal authority basis / lineage refinement | substantive principle refinement |
| **A11** | P5 exhaustive material-basis subset audit | serious P5 hardening |
| **A12** | P6 transitive-dependency strongest-repair audit | serious P6 hardening |
| **A13** | six-principle completion review | current bounded scientific conclusion |
| **A14** | GitHub Actions 379/379 reproduction | reproducibility evidence |
| **A15** | complete six-principle ablation testbook | preferred single reader artifact |
| **A16** | formal relative-independence proof | mathematical proof layer |
| **A17** | this documentation/proof/reproducibility map | navigation / audit |
| **A18** | pure mathematical independence proof | self-contained model-theoretic independence / irredundancy proof with no fixture or test premise |

---

## 3. Executable Python family

Canonical core harnesses:

| Principle | Directory | Current core |
|---|---|---:|
| **P1** | [fixtures/00K-A1-P1-00J](./fixtures/00K-A1-P1-00J/README.md) | **42** |
| **P2** | [fixtures/00K-A2-P2-00E](./fixtures/00K-A2-P2-00E/README.md) | **58** |
| **P3** | [fixtures/00K-A3-P3-00F](./fixtures/00K-A3-P3-00F/README.md) | **49** |
| **P4** | [fixtures/00K-A4-P4-00H](./fixtures/00K-A4-P4-00H/README.md) | **76** |
| **P5** | [fixtures/00K-A5-P5-00I](./fixtures/00K-A5-P5-00I/README.md) | **47** |
| **P6** | [fixtures/00K-A6-P6-00G](./fixtures/00K-A6-P6-00G/README.md) | **74** |

**Core = 346.**

Supplemental anti-confirmation-bias / independent packages:

- [A6a original 00G pair falsifier](./fixtures/00K-A6a-P6-00G/README.md) — 10
- [A6b independent 00F P6 isolation](./fixtures/00K-A6b-P6-00F/README.md) — 11
- [cross-scenario independent kernels](./fixtures/00K-cross-scenario-independent/README.md) — 12

**Supplemental = 33.**

**Registered campaign = 379.**

---

## 4. Reproducibility route

### Aggregate runner

[fixtures/00K-SUITE](./fixtures/00K-SUITE/README.md)

```bash
cd research/ecosystem-awareness/baseline/fixtures/00K-SUITE
python validate_manifest.py
python run_all.py
```

Expected current result:

```text
Core passing regression count: 346/346
Supplemental passing count: 33/33
Campaign total: 379/379
```

### Repository CI

Workflow:

[`.github/workflows/00k-symbolic-ablations.yml`](../../../.github/workflows/00k-symbolic-ablations.yml)

Current reproduced run:

[GitHub Actions run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548)

Status:

```text
10/10 jobs successful
346/346 core
33/33 supplemental
379/379 total
```

---

## 5. Formal proof route

The symbolic tests and the mathematical proof are related but not identical.

### Executable tests establish

- concrete branch behavior;
- serious repair failures;
- positive-control preservation;
- discovered fixture confounds;
- partial implementations;
- semantic reconstructions.

### A16 establishes

For the current formalized predicates:

~~~text
∀ i ∈ {1,...,6}:  {P1,...,P6} \\ {Pi} ⊭K Pi
~~~

The proof uses six corrected fixture-derived countermodels. The certificate computes P1–P6 from lower-level semantic witness fields rather than storing the six truth values directly.

Machine-checkable certificate:

[fixtures/00K-FORMAL/formal_independence_certificate.py](./fixtures/00K-FORMAL/formal_independence_certificate.py)

Run:

```bash
python research/ecosystem-awareness/baseline/fixtures/00K-FORMAL/formal_independence_certificate.py
```

The formal certificate is a **meta-proof check** and is not added to the 379 ablation-test count.

---

## 6. Negative results that must remain visible

The 00K family is not a six-pass marketing narrative.

It retains these corrections:

- **P1:** original A1 pair was confounded by source/issuer/record class; a source-authority rule was a TRUE SUBSTITUTE for that naive pair.
- **P3:** original base branch exposed literal HOLD; a HOLD-marker shortcut was sufficient for the naive pair.
- **P4:** full receiver-side historical delegation lineage was stronger than necessary; scoped authoritative PDP/capability is sufficient in 00H.
- **P5:** generation-only compare was only a partial implementation.
- **P6:** original F/G pair was confounded by authority; later direct source-ID count was also only a partial proxy for transitive independence.

These are evidence **for the method's falsifiability**, not defects to erase.

---

## 7. Current bounded claim

The current formal + symbolic position is:

> **Within the declared corrected 00E–00J-derived symbolic model class, P1–P6 are an irredundant / logically independent axiom family, and every minimal principle has survived the current strongest-repair ablation search. The full-lineage version of P4 did not survive and has been narrowed to a current decision-sufficient authority-qualification/non-amplification invariant.**

This is not:

- universal minimality;
- completeness for every future failure;
- a theorem that no alternative five-principle basis can be logically equivalent;
- live product evidence; or
- proof of Ecosystem Positioning superiority.

---

## 8. Maintenance rule for 00K

When any 00K fixture, count, principle wording or proof assumption changes:

1. update the affected fixture README / execution record;
2. update the machine-readable principle manifest;
3. update the suite runner expected counts;
4. update the GitHub Actions expected counts;
5. update 00K main if the bounded interpretation changes;
6. update A13, A15 and A16 when the scientific/formal conclusion changes;
7. update this A17 map;
8. keep old falsified fixtures and milestone documents as labelled lineage rather than silently rewriting them.

The current source of truth for **current counts and invariants** is the execution-lock manifest plus the current 00K main document, not an older milestone count embedded in A05 or a preserved predecessor.
