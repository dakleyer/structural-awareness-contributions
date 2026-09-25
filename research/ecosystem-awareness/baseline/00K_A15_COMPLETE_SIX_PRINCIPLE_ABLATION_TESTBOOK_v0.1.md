# 00K-A15 — Complete Six-Principle Ablation Testbook — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Status** | **Complete symbolic testbook for P1–P6** |
| **Date** | 25 September 2026 |
| **Execution summary** | [00K-A04](./00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md) |
| **Completion review** | [00K-A13](./00K_A13_SIX_PRINCIPLE_SERIOUS_ABLATION_COMPLETION_REVIEW_v0.1.md) |
| **CI reproduction** | [00K-A14](./00K_A14_GITHUB_ACTIONS_REPRODUCTION_379_v0.1.md) · [GitHub Actions run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548) |
| **Evidence class** | deterministic symbolic fixtures + paper routes + falsification-first corrections; not live product/runtime evidence |

> **Purpose.** Put the six ablation arguments in one reader-facing place, with the route logic and the executable Python surface side by side. Each principle is treated as falsifiable: a TRUE SUBSTITUTE counts against necessity; a passing peer that succeeds only by implementing the same invariant is SEMANTIC RECONSTRUCTION; a repair that loses either the negative branch or its matched positive/boundary control is a FAILED SUBSTITUTE.

> **Current bounded result.** After correcting known confounds and running serious-repair searches, **no TRUE SUBSTITUTE is known for the corrected minimal P1–P6 invariants inside the declared symbolic fixtures**. P4 is explicitly narrowed: full historical lineage at the relying component is not necessary in 00H; the supported minimum is a current, decision-sufficient, non-amplifying authority qualification.

---

## 1. Test discipline used for all six principles

Every serious ablation follows the same order:

1. **Lock the principle invariant before repair search.**
2. **Freeze the scenario facts, branch oracle, authority, resources and deadline.**
3. **Remove only the target principle.**
4. **Give the remaining five principles and ordinary technology controls the strongest fair opportunity to repair the route.**
5. **Require negative + positive/boundary correctness.** Deny-all, HOLD-all, accept-all and infinite-search shortcuts do not pass.
6. **Search for confounds in the fixture itself.** If a non-target variable separates the branches, the fixture is rejected or corrected.
7. **Classify the strongest repair:**
   - TRUE SUBSTITUTE;
   - SEMANTIC RECONSTRUCTION;
   - FAILED SUBSTITUTE.
8. **Run bounded grids / exhaustive reduced subspaces where useful.**
9. **Keep a falsifier open** for a future repair that defeats the current result.
10. **Separate symbolic necessity from product differential.** Passing these fixtures does not prove any commercial technology weak or Ecosystem Positioning superior.

The [machine-readable execution-lock manifest](./fixtures/00K-SUITE/principle_manifest.json) freezes the current six invariants, branch controls and expected counts.

---

## 2. P1 — Qualified determination / evidence-to-proposition sufficiency

### Route

**Scenario:** [00J — Rights-Provenance Inversion](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md)

The original reader-facing failure is:

```text
valid generation/provenance record
    → silently promoted
    → unsupported rights-enforcement proposition
    → LICENSE / PAY / BLOCK against original author
```

The naive first A1 pair was **rejected as a necessity isolation** because it also changed issuer/source and record class. A source-authority-only rule was a TRUE SUBSTITUTE for that old pair.

The corrected matched-semantic pair holds equal:

- source / issuer;
- signature;
- freshness;
- record class;
- record count;
- provenance completeness;
- authority context.

Only the proposition supported by the evidence changes.

**Negative:** valid evidence supports a narrower proposition such as `GENERATED_BY_MODEL_M1`.  
**Positive:** equally valid evidence supports `RIGHT_TO_ENFORCE_AGAINST_AUTHOR`.

### Serious substitutes attempted

- trusted issuer allow-list;
- complete provenance;
- generic schema allow-list;
- confidence / risk scoring;
- independent quorum;
- human approval without a new rights fact;
- source reputation;
- threshold sweeps;
- replicated valid-but-wrong evidence.

They do not separate the matched branches.

The strong peer that passes uses an evidence-semantics → proposition → allowed-decision contract.

**Classification:** **SEMANTIC RECONSTRUCTION of P1.**

### Executable

- [A1 README](./fixtures/00K-A1-P1-00J/README.md)
- [core model](./fixtures/00K-A1-P1-00J/ablation_A1.py)
- [serious repairs](./fixtures/00K-A1-P1-00J/p1_strong_repairs.py)
- [serious-repair tests](./fixtures/00K-A1-P1-00J/test_ablation_A1_strong_repairs.py)
- [P1 methodological correction](./00K_A07_P1_CONFOUND_FALSIFIER_AND_MATCHED_SEMANTIC_ISOLATION_v0.1.md)

**Current core:** **42/42**

### Falsifier

A repair that separates the corrected matched branches without any evidence→proposition→decision sufficiency relation or operational equivalent is a TRUE SUBSTITUTE.

---

## 3. P2 — Bounded unresolved effort / viable oversight

### Route

**Scenario:** [00E — 100 Million Tokens](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md)

The failure is not merely “too many tokens.” It is that unresolved determination can keep consuming search/review capacity until the useful response window disappears.

The serious fixture uses matched prefixes:

```text
steps 1 ... H-1:
    negative == positive == unresolved

step H:
    negative -> still unresolved
    positive -> resolving evidence arrives
```

A policy that stops too early loses a still-reachable positive resolution. A policy that continues past the declared useful horizon fails the negative branch.

### Serious substitutes attempted

- fixed TTL / max-step / token quota;
- no-progress circuit breaker;
- parallel fan-out;
- cached/default closure;
- external scheduler deadline;
- bounded reversible probe;
- exhaustive reduced family of observation-only memoryless policies.

No memoryless observation-only policy passes both branches.

TTL, circuit breaker, scheduler and bounded probes can pass when tuned to the viable horizon — but then they implement a finite effort / horizon / fallback invariant.

**Classification:** **SEMANTIC RECONSTRUCTION of P2.**

### Executable

- [A2 README](./fixtures/00K-A2-P2-00E/README.md)
- [core model](./fixtures/00K-A2-P2-00E/ablation_A2.py)
- [serious repairs](./fixtures/00K-A2-P2-00E/p2_strong_repairs.py)
- [serious-repair tests](./fixtures/00K-A2-P2-00E/test_p2_strong_repairs.py)
- [P2 strongest-repair audit](./00K_A08_P2_STRONGEST_REPAIR_AND_PREFIX_INDISTINGUISHABILITY_v0.1.md)

**Current core:** **58/58**

### Falsifier

A repair that terminates unresolved determination inside capacity, still permits a resolution at any allowed step through the horizon, avoids false closure/permanent HOLD, and does so without a finite effort/horizon/fallback rule or equivalent would be a TRUE SUBSTITUTE.

---

## 4. P3 — No false closure from unresolved material state

### Route

**Scenario:** [00F — Chaos in the Smartcity](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md)

The first base conflict contained a literal `HOLD` posture and was therefore too easy: a HOLD-marker veto could pass without general unresolved-state semantics.

That base pair is retained as a methodological negative result.

The corrected matched-conflict branch removes that shortcut:

```text
PLAN_A / PLAN_B / PLAN_A / PLAN_B
```

Authority, confidence and freshness are equal.

Positive controls:

```text
PLAN_A / PLAN_A / PLAN_A / PLAN_A
NORMAL / NORMAL / NORMAL / NORMAL
```

### Serious substitutes attempted

- authority priority;
- confidence priority;
- freshest-source priority;
- majority/default;
- human approval without new evidence;
- timeout/default;
- risk-priority heuristic;
- supermajority;
- unanimity;
- robust intersection of action sets.

Priority/default mechanisms false-close at least one material conflict.

Supermajority, unanimity and robust intersection can pass, but only by enforcing that materially incompatible/unresolved state is non-permission until requalification/containment.

**Classification:** **SEMANTIC RECONSTRUCTION of P3.**

### Executable

- [A3 README](./fixtures/00K-A3-P3-00F/README.md)
- [core model](./fixtures/00K-A3-P3-00F/ablation_A3.py)
- [serious repairs](./fixtures/00K-A3-P3-00F/p3_strong_repairs.py)
- [serious-repair tests](./fixtures/00K-A3-P3-00F/test_p3_strong_repairs.py)
- [P3 methodological correction](./00K_A09_P3_CONFOUND_FALSIFIER_AND_MATCHED_CONFLICT_ISOLATION_v0.1.md)

**Current core:** **49/49**

### Falsifier

A repair that safely resolves the matched conflict, preserves legitimate uniform execution and does so without treating unresolved/materially incompatible state as non-permission/containment or equivalent would be a TRUE SUBSTITUTE.

---

## 5. P4 — Qualification-preserving authority basis

### Route

**Scenario:** [00H — The Quiet Four Thousand](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md)

Matched controls:

- **U:** valid leaf actions compose into a campaign whose current authority is absent;
- **G:** same campaign topology, but current authority covers the composed effect;
- **I:** genuinely independent cases;
- **NM:** non-material finding.

U and G are matched on materiality, campaign identity, leaf validity, volume, amount, risk and timing. Their required decisions are opposite.

### Serious substitutes attempted

- leaf RBAC;
- campaign detection;
- rate limits;
- aggregate amount limits;
- risk thresholds;
- static allow-lists;
- non-owner human approval;
- full root/delegation lineage;
- scoped capability/caveat;
- legitimate maker-checker;
- opaque owner-side PDP permit.

The important result is a **refinement**.

A legitimate owner-side PDP can return a current scoped permit bound to campaign/action/amount without exposing full delegation history. That passes U/G/I/NM.

Therefore:

> **full historical root→leaf lineage at the relying component is not necessary in 00H.**

What remains necessary in the tested surface is the smaller invariant:

> the relying decision must retain or obtain a current, decision-sufficient, receiver-verifiable, non-amplifying authority basis for the actual composed action.

Lineage, scoped capability, maker-checker and owner-side PDP are alternative implementations.

**Classification:** **P4 REFINED; MINIMAL AUTHORITY-QUALIFICATION INVARIANT SUPPORTED.**

### Executable

- [A4 README](./fixtures/00K-A4-P4-00H/README.md)
- [core model](./fixtures/00K-A4-P4-00H/ablation_A4.py)
- [A2-L strong peer](./fixtures/00K-A4-P4-00H/a2l_strong_peer.py)
- [serious repairs](./fixtures/00K-A4-P4-00H/p4_strong_repairs.py)
- [serious-repair tests](./fixtures/00K-A4-P4-00H/test_p4_strong_repairs.py)
- [P4 refinement report](./00K_A10_P4_MINIMAL_AUTHORITY_BASIS_AND_LINEAGE_REFINEMENT_v0.1.md)

**Current core:** **76/76**

### Falsifier

A repair that passes matched U/G/I/NM without lineage, scoped permit/capability, legitimate authority-owner decision, or any operationally equivalent current authority qualification would be a TRUE SUBSTITUTE for the minimal P4 invariant.

---

## 6. P5 — Material-change requalification at time of use

### Route

**Scenario:** [00I — The Patch That Undid the Fix](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md)

A queued Patch A is correct at T1. At T2 the technical token/job can still be valid although the decision basis changed.

The hardening declares four material basis fields:

```text
generation
incident_open
freeze_active
source_version
```

The executable reduced model enumerates all `2^4 = 16` subsets of those checks.

Only the full declared material basis passes:

- continuity;
- unavailable-current-source handling;
- every single-field material mutation.

### Serious substitutes attempted

- generation-only compare;
- every partial/full subset of basis checks;
- queue-age TTL;
- serialization;
- idempotency;
- human reapproval without fresh state;
- cancel-on-any-event;
- material-event invalidation;
- state hash;
- version vector;
- material epoch.

Generation-only compare is exposed as partial.

Hash/vector/event/epoch peers pass only when they represent every declared material field that can invalidate action applicability.

**Classification:** **SEMANTIC RECONSTRUCTION of P5.**

### Executable

- [A5 README](./fixtures/00K-A5-P5-00I/README.md)
- [core model](./fixtures/00K-A5-P5-00I/ablation_A5.py)
- [full-basis strong peer](./fixtures/00K-A5-P5-00I/p5_strong_peer.py)
- [serious repairs](./fixtures/00K-A5-P5-00I/p5_serious_repairs.py)
- [serious-repair tests](./fixtures/00K-A5-P5-00I/test_p5_serious_repairs.py)
- [P5 exhaustive audit](./00K_A11_P5_EXHAUSTIVE_MATERIAL_BASIS_ABLATION_v0.1.md)

**Current core:** **47/47**

### Falsifier

A repair that executes continuity, requalifies every declared material change, handles unavailable current state, ignores irrelevant changes and does all of that without representing/binding/invalidation from the current material decision basis or equivalent would be a TRUE SUBSTITUTE.

---

## 7. P6 — No local-to-ecosystem promotion / non-substitution

### Route

**Primary scenario:** [00G — Ciber Napoleon Goes to Russia](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md)  
**Independent corroborating isolation:** [A6b / 00F shared-resource composition](./fixtures/00K-A6b-P6-00F/README.md)

The original 00G false/genuine pair was rejected as a necessity isolation because it changed both source independence and transition authority. An authority-only policy was a TRUE SUBSTITUTE for that naive pair.

The corrected matched-authority fixture then exposed another partial repair: counting distinct immediate source IDs.

The serious hidden-dependency pair now matches:

- six authenticated agents;
- six organizations;
- six immediate source IDs;
- signatures;
- freshness;
- confidence;
- timing diversity;
- content diversity;
- transition authority.

Only the **transitive dependency graph** differs.

False branch:

```text
six immediate sources
    -> two intermediates
    -> one material root
```

Genuine branch:

```text
six immediate sources
    -> six material roots
```

### Serious substitutes attempted

- identity quorum;
- organization diversity;
- direct source count;
- confidence weighting;
- temporal diversity;
- content diversity;
- human committee;
- source reputation;
- source-count threshold sweeps;
- transitive dependency graph;
- effective material-root count.

The first group cannot distinguish the matched branches.

Dependency graph/effective-root peers pass by explicitly computing material dependence/non-substitution.

**Classification:** **SEMANTIC RECONSTRUCTION of P6.**

### Executable

- [A6 README](./fixtures/00K-A6-P6-00G/README.md)
- [core model](./fixtures/00K-A6-P6-00G/ablation_A6.py)
- [serious repairs](./fixtures/00K-A6-P6-00G/p6_serious_repairs.py)
- [serious-repair tests](./fixtures/00K-A6-P6-00G/test_p6_serious_repairs.py)
- [naive-pair falsifier](./fixtures/00K-A6a-P6-00G/README.md)
- [independent 00F isolation](./fixtures/00K-A6b-P6-00F/README.md)
- [P6 confound note](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md)
- [P6 transitive-dependency audit](./00K_A12_P6_TRANSITIVE_DEPENDENCY_AND_STRONGEST_REPAIR_AUDIT_v0.1.md)

**Current core:** **74/74**

### Falsifier

A repair that rejects the hidden-common-root branch and accepts the independent branch under matched authority/identity/org/signature/freshness/confidence/time/content observables, while never representing or inferring material dependence/independence/compatibility or equivalent, would be a TRUE SUBSTITUTE.

---

## 8. Consolidated result

| Principle | Corrected serious isolation | Core tests | Negative result retained? | Current disposition |
|---|---|---:|---|---|
| **P1** | 00J matched semantics | **42** | old issuer/source pair falsified | bounded semantic necessity supported |
| **P2** | 00E matched prefix / late resolution | **58** | — | bounded semantic necessity supported |
| **P3** | 00F matched conflict | **49** | old HOLD-marked pair insufficient | bounded semantic necessity supported |
| **P4** | 00H matched U/G/I/NM | **76** | full-lineage claim narrowed | **minimal authority-basis invariant supported** |
| **P5** | 00I exhaustive material basis | **47** | generation-only compare partial | bounded semantic necessity supported |
| **P6** | 00G matched authority + transitive dependence | **74** | original F/G falsified; direct source count partial | bounded semantic necessity supported |

**Core:** **346/346**  
**Supplemental anti-confirmation-bias / isolation / cross-scenario:** **33/33**  
**Registered campaign:** **379/379**

Repository CI independently reproduced the current campaign on [run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548).

The test count is a regression surface, not a scientific score.

---

## 9. What this establishes — and what it does not

The strongest defensible statement is:

> **Within the corrected declared symbolic fixtures, every minimal P1–P6 invariant has survived a leave-one-principle-out strongest-repair search. The programme has also falsified several of its own earlier fixture formulations and narrowed P4. Where strong conventional peers pass the corrected tests, they do so by implementing an operationally equivalent form of the relevant minimal invariant.**

This does **not** establish:

- universal minimality;
- formal impossibility of all future substitutes;
- live product failure;
- live agent/robot behavior;
- empirical superiority of Ecosystem Positioning;
- that one implementation or interface owns a principle; or
- that six is the only possible abstraction of the same properties.

The next evidence level is live or stateful execution against stronger technology substrates under the same frozen branch oracles and the same willingness to accept TRUE SUBSTITUTE as a result against the model.
