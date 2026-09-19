# Annex 00D-A02 — Stage-0 Execution and Coverage-Alignment Change Plan — Ecosystem Awareness

> **Dated public change record.** This document consolidated the reviewable changes to the public Contributions corpus before any Stage-0 scenario execution. Its specified document changes are enacted in the same public commit that updates this record. It is not an executed fixture, testbed, benchmark or validation result.

**Version:** 0.1 — 19 September 2026  
**Status:** enacted public change record; not a further approval gate.

**Reviewed baseline:** public Contributions commit [`063999acaa0c09f9e61bf94c0446e27c23633bf5`](https://github.com/dakleyer/structural-awareness-contributions/commit/063999acaa0c09f9e61bf94c0446e27c23633bf5), including [00D-A01](./00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_PROOF_SKETCH_v0.1.md), the [coverage map](./USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md) and [00](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md).
**Change authority:** corpus maintainer — **self-approved implementation**. Independent reviewer: not named in the public record; no independent-validation claim follows.

## 1. Purpose and enacted decision

The corpus now has a requirements route, two Reference Failure Scenarios, a bounded-oracle fixture design and a portfolio coverage map. The remaining issue is alignment: narrative gates, planned fixtures, KPI evidence and future execution must not be read as the same thing.

The bounded public change set below is enacted. The next work is the harness self-test, pre-registration and Stage-0 execution—not another methodological layer. This record remains only to make the reviewed change set inspectable against its fixed baseline.

The canonical route remains:

`Reference Failure Scenario → Quality-Gate Plan → S# → T# → H# → KPI → evidence/disposition`.

## 2. Scope and conservation rule

### 2.1 Documents changed by this implementation

1. [00D-A01 — Reference-Scenario Test Artifacts and Bounded Reference-Oracle Proof Sketch](./00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_PROOF_SKETCH_v0.1.md)
2. [Use-Case Portfolio Requirements Coverage Map](./USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md)
3. [00 — Canonical Requirements: Challenges, Sufficiency Conditions, Hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), only for a short clarification of the already-existing S14 aggregate.
4. [README](./README.md) and [Canonical Corpus Manifest](./CANONICAL_CORPUS_MANIFEST.md), to identify this dated change record, its reading position and the open product-profile source-basis review.

### 2.2 Documents deliberately unchanged

The implementation does **not** alter the facts, gates or outcomes in 00E/00F; the frozen UC-EA profiles; 04 Appendix A; 05; 05A; the Parent Case Study; or the underlying S1–S14 / T1–T4 / H1–H6 taxonomy.

It does not claim that a planned fixture has executed, that a stipulated Stage-0 oracle is observational, or that an EA differential has been established.

## 3. Enacted changes to 00D-A01

### 3.1 Fixture-record discipline

The scenario-fixture record will add the following fields and rules:

| Item | Change |
| --- | --- |
| Public source anchor | Each fixture declares the exact public document path, document version and Git commit used for its requirements, benchmark and applicable interface reference. An ICR exercised by the fixture cites the same public anchor; Appendix A itself remains unchanged. |
| Scenario-fact independence | When the authority freezing facts is also the candidate designer, the fixture is labelled **facts self-declared**. |
| Comparator defender | The named defender may improve B0–B3 only within the pre-registered budget, access and time envelope. An unresolved objection is recorded and prevents a differential claim, while leaving the descriptive run visible. |
| Harness self-test | Before any candidate result, inject a known qualifier loss at a named handoff and require the trace to record the loss at that handoff. |
| Stage-0 burden | All Stage-0 resource results are labelled **modelled burden — provisional**. They may guide the next run but cannot permanently close a route before measured Stage-1 evidence. |

### 3.2 Matrix and falsification discipline

The traceability matrix will:

1. split its current combined comparator/falsification column into **candidate failure condition** and **differential falsifier**;
2. name the applicable KPI set and its pre-registered measurement rule for every fixture;
3. retain the existing evidence-status column, which describes what the fixture can support and is not the E1–E4 source taxonomy;
4. state that a stipulated cascade branch cannot retrospectively falsify itself through non-observation. A separate pre-registered null branch may test no-cascade behaviour in Stage 0; real non-cascade observation belongs to Stage 1 or later; and
5. retain controls for GEEW degradation, approval saturation, source re-query and non-deterministic comparators.

### 3.3 New fixture: RS-00E-Q4

Add **RS-00E-Q4 — bounded requalification under non-reducing residual**:

| Element | Required declaration |
| --- | --- |
| Requirement route | S3/S4/S5/S10/S14 → T1/T2/T3/T4 → H1/H5/H6. |
| Frozen branch | A residual remains material after the declared additional search; decision deadline, authority, resource ledger and permitted bounded experiments remain fixed. |
| Candidate expectation | Select a bounded experiment or explicit `NO COMMITMENT`; do not consume the useful horizon in unbounded search or silently close the decision. |
| Differential falsifier | A pre-registered strong comparator reaches an equally qualified outcome within the common budget and tolerance, or the EA candidate incurs avoidable false containment, deadline loss or burden. |
| Null-action KPI | Record the **cost of action or inaction relative to `O_ref`**: containment/no-commitment is not free when a reducible residual would have supported a timely qualified route. |
| Negative control | Same declared decision family with a residual reducible inside the horizon. The candidate must reopen and advance when the required evidence is restored, rather than remain contained. |

This makes containment falsifiable in both directions: unsafe closure and avoidable abstention.

## 4. Enacted changes to the portfolio coverage map

### 4.1 Separate narrative coverage from executable evidence

The current A/B/C scale remains a statement of architecture responsibility and external-owner boundary. It will not be used as a proxy for execution. Each S# row will therefore add three explicit statuses:

| Status | Meaning |
| --- | --- |
| **Named in a gate/profile** | A scenario gate or validation profile invokes the route. |
| **Fixture status** | No fixture / planned fixture / implemented fixture. |
| **Execution status** | Not executed / Stage 0 / Stage 1 / Stage 2. |

The table will also name the applicable KPI family from 00, rather than referring only to `S# → T# → H#`.

### 4.2 S14 as aggregate, not artificial breadth

S14 remains visible in the canonical map but is marked **aggregate — not independently scored A/B/C**. Its coverage is reported through five declared components in 00:

1. evidence sufficiency;
2. Type-1 / Type-2 transition;
3. conflict, arbitration or precedence record without EA resolving it;
4. expiry; and
5. re-entry and disposition update.

Each fixture names the S14 component it exercises. “S14 everywhere” will no longer be read as independent coverage of every configuration.

### 4.3 Sequencing and workbook language

The map will replace Route N/Q as a reusable workbook field with **configuration under test and pre-registered comparator**, using the common authority, evidence, resource and time envelope.

The public execution sequence is:

1. pre-register and run the Stage-0 atomic 00E Q1 branches, Q2 and Q4, with the 00F composition branches and their controls;
2. seek an independently operated producer/receiver pair for EA-ITP-01 in parallel for **90 days**;
3. if no pair is available at that point, record that limit and begin WB-EA-01 rather than blocking it; and
4. use Stage-0 results to constrain WB-EA-01 before drafting a larger cross-organisation workbook.

## 5. Minimal clarification in 00

00 will gain only the S14 aggregate clarification in §4.2 above. It creates no S14 sub-requirements, no new KPI taxonomy and no EA authority to arbitrate. Its purpose is only to keep fixture and portfolio terminology stable.

## 6. Review checks and completion condition

The reviewer can approve this plan if all of the following hold:

1. every proposed fixture still begins with an existing S/T/H/KPI route;
2. the planned Q4 fixture can fail for over-search, false closure **and** avoidable abstention;
3. A/B/C portfolio coverage cannot be mistaken for an executed fixture or result;
4. S14 is visible but cannot inflate the apparent breadth of coverage;
5. comparator, facts and Stage-0 burden limitations are visible rather than absorbed into a claimed EA differential; and
6. the implementation changes no scenario facts, frozen profile, interface contract or canonical taxonomy.

This implementation changes the documents in §2.1 only. It does not authorize an execution result: each Stage-0 fixture must still be separately pre-registered before it runs.

## 7. Out of scope for this change set

External corpus mirrors, licensing and evidence outside this public Contributions repository are not part of this change set. Product-profile source review remains open inside this repository with owner and review date recorded in the manifest; it does not block the controlled changes above or the first stipulated Stage-0 fixture.
