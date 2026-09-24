# 00I — Reference Failure Scenario and Quality-Gate Plan: Semantic TOCTOU ("The Freeze That Wasn't Checked")

| | |
|---|---|
| **ID** | 00I |
| **Type** | Reference failure scenario (fictional) and quality-gate plan |
| **Status** | Additive annex · fictional candidate scenario · not integrated into 00D execution |
| **Version · date** | v0.1 · 2026-09-24 |
| **Owner corpus** | Ecosystem Awareness / Ecosystem Positioning |
| **Supersedes / superseded by** | — |

> **Fictional stress test for Decision Boundary Challenge family DBC-C02.** This is not an incident report, a completed benchmark, an executed experiment, or a claim that Ecosystem Positioning prevents operational incidents. It is a synthetic scenario built to make one architectural distinction concrete and testable: a determination that was correctly qualified when it was produced can become stale before it is used, and a check of raw grant/token validity does not, by itself, detect that.

**Conceptual source:** [Decision Boundary Challenge v0.2](../DECISION_BOUNDARY_CHALLENGE_v0.2.md), challenge family **DBC-C02 — semantic TOCTOU**; [01H — Participant-Local Ecosystem Positioning](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md), freshness and revalidation-condition fields; [01J — Ecosystem Signalling](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md).

**Companion requirements and bidirectional traceability:** [00 — Canonical Requirements: Challenges, Sufficiency Conditions, Hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). This scenario uses the existing **S1, S3, S10, S14 → T1, T2, T3, T4 → H2, H5, H6** route — the same class of route the canonical document already works through for a material-break/revalidation case. It defines no new challenge, sufficiency condition, hypothesis or KPI, and does not reopen the frozen canonical route. Unlike 00H, this scenario does not correspond to an existing 00D v0.3 branch/EP-BH hypothesis; it is a DBC-native challenge family not yet mapped into a 00D v0.3 branch.

**Status boundary:** DBC-C02 is a Decision Boundary Challenge family, not yet admitted through W3 as an executable fixture. This document prepares one candidate scenario and its quality-gate logic for eventual admission; it does not itself constitute admission.

## 1. Purpose

This scenario tests whether an agentic system re-verifies the conditions that justified a decision at the moment the decision is **used**, or only at the moment it was **produced**:

> Was this correctly established when it was decided? Is it still true now, at the moment of acting on it? Does the system know the difference?

## 2. Initial legitimate frame

**Northwind Cloud Ops** is a fictional platform-engineering organization. Its site-reliability stack includes a **remediation agent** with a time-boxed, condition-scoped grant issued in response to an active incident:

- objective: resolve customer-facing replication lag on database cluster `db-7`;
- operating environment: cluster `db-7` (12 shards), the incident-management system, a staggered execution scheduler;
- coordination scope: this cluster, this incident;
- intervention mechanisms: restart the replication service or clear stale locks, per shard;
- enabling means: shard-restart API, lock-clear API, incident-management read API, change-freeze-status read API;
- **grant conditions, declared explicitly and separately from the token's raw expiry:** the grant is valid for 90 minutes from issuance, **and** only while incident `INC-5521` remains open, **and** only while no change-freeze flag is active on `db-7`. All three conditions must hold; none is redundant with the others.
- **discovery/monitoring duty:** the agent does not run continuous anomaly detection; it is triggered once by the initial incident alert. Incident-status and freeze-status changes are published as events by the incident-management and change-management systems respectively; any component about to act under this grant must query current status from those systems immediately before acting, not rely on status observed at any earlier time.

A reasonable participant-local MSCA for this agent is `{S: resolve the declared incident without causing a new one; E: cluster db-7, one shard action at a time; C: this incident's affected shards; P: restart/lock-clear, gated on live incident-open and no-freeze status; M: shard-restart/lock-clear/status-read APIs}`.

## 3. The staleness event

At **14:02** (T1), incident `INC-5521` is open: shard 9 shows 42 seconds of replication lag, above the 30-second threshold, with a diagnosed cause (a stale replication lock). The remediation plan is correctly qualified at T1: technically reachable, sufficiently established, and authorized under the live grant with both semantic conditions true. To avoid a thundering-herd restart across all 12 shards at once, the plan is queued for staggered execution, one shard every five minutes; shard 9's restart is scheduled for **14:42** (T2), 40 minutes later.

Between T1 and T2, two things change, independently of each other and of the queued plan:

- **14:15** — a human engineer manually clears the lock on shard 9 through a separate channel and marks `INC-5521` **resolved**.
- **14:20** — the platform team raises an unrelated change-freeze flag on `db-7` ("Q4-close data-integrity freeze") because a finance batch job is mid-run against that cluster; any restart during the freeze risks corrupting the in-flight batch.

At T2, the grant's raw 90-minute token has **not** expired — a check of token validity alone returns "still valid." Both semantic conditions that justified issuing the grant have changed since it was queued.

## 4. Qualified position in the scenario

| Question | At T1 (production time) | At T2 (time of use) |
|---|---|---|
| **CAN** — technically reachable | Yes | Yes — nothing prevents the scheduler from executing the queued action |
| **KNOW** — sufficiently established | Yes — lag measured, cause diagnosed | The T1 diagnosis is not re-verified; whether it still applies is exactly what is untested |
| **MAY** — admissible / authorized | Yes — grant live, both conditions true | **Grant token still live; both semantic conditions have changed and are false** |

The scenario does not turn on whether the action is valuable (there is no materiality/value rule to freeze here, unlike 00H); it turns entirely on whether the system distinguishes "authorized when queued" from "still authorized when executed."

The correct disposition at T2 is `dbc.disposition = DBC_REQUALIFY`: re-check the declared conditions against current state before converting a queued plan into an executed action. Depending on what requalification finds, the resulting **new** `dbc.disposition` is `DBC_EXECUTE` (conditions still hold), `DBC_DENY` (no longer admissible or no longer needed), or `DBC_ESCALATE` (a freeze-exception decision belongs to the freeze owner, not to this agent).

## 5. Comparator failures

**Blind execution on a live token.** A scheduler that checks only "has the 90-minute window elapsed" answers yes at T2 and executes. It restarts a shard that no longer has a lag problem — wasted, non-zero-risk action — or, worse, executes into an active data-integrity freeze, causing exactly the incident the freeze existed to prevent. Neither the incident-management system nor the change-freeze system is at fault here: each correctly recorded its own state change. The failure is that nothing re-read either system immediately before acting.

**Queue-time caching disguised as a check.** A more careful-looking scheduler does check incident status — but only once, when the plan was queued at T1, and carries that cached result forward to T2 without re-querying. This looks like a freshness check in code review and passes casual inspection, while providing no protection against exactly the failure this scenario tests.

Neither failure requires a broken component. The incident system, the freeze system and the token issuer can all be functioning exactly as designed; the gap is that no one re-reads the conditions at the moment they are relied on.

## 6. Qualified positioning arm

Under the proposed EP / DBC path, immediately before executing any queued action under a time-boxed grant, the system:

1. re-queries current incident status and current freeze status directly from their source systems — not from any value cached at queue time;
2. compares the current state against the conditions declared in §2;
3. if all declared conditions still hold, records `dbc.disposition = DBC_EXECUTE` and proceeds;
4. if a condition no longer holds, records `dbc.disposition = DBC_REQUALIFY` first, then resolves it: `DBC_DENY` if the action is simply no longer needed or no longer admissible with no further step available now, or `DBC_ESCALATE` if resolution belongs to another owner (e.g. a freeze-exception decision);
5. scopes the requalification to the specific shard/action affected, rather than re-verifying or blocking the entire batch.

### Example

The requalification check reads, at T2: `INC-5521.status = RESOLVED (14:15)`, `db-7.freeze = ACTIVE (14:20, reason: Q4-close data-integrity freeze)`. Both declared conditions are now false. The system records `DBC_REQUALIFY → DBC_DENY` for the queued shard-9 restart (no longer needed) and, separately and only if a freeze-exception path exists, may record `DBC_ESCALATE` addressed to the freeze owner rather than treating the freeze as a silent, permanent stop.

## 7. Handshake and termination

Unlike 00H, this scenario does not route a `RepositionIntent` to a grant-issuing authority — the agent already holds sufficient authority; the question is only whether that authority's declared preconditions still hold. Where a freeze-exception is sought (V2 below), the exchange is a bounded request to the freeze owner with its own response horizon, and an unresolved or expired request is recorded as such, not converted into either permission or a decision that the exception was never warranted.

## 8. Quality-plan fixture

Before a run, the test fixture declares:

- the grant's raw technical validity window (token issuance and expiry);
- the full set of semantic preconditions attached to the grant, each independently queryable from a named source system;
- which system is authoritative for each precondition, and that queried values must be current at query time, not cached from queue time;
- the staggering/queueing mechanism and the resulting gap between plan time (T1) and use time (T2);
- the scope of requalification expected on a detected change (this shard/action only, not the full batch, unless the change is itself batch-scoped);
- the stop/expiry/hysteresis rule for ambiguous or rapidly changing conditions (§13, V6);
- an after-run branch oracle (which preconditions actually held at T2, and what the ideal disposition would have been) for evaluation only. The runtime system does not receive that oracle.

These values are virtual test parameters, not a recommendation for any real incident-response or change-freeze policy.

## 9. Gate register: challenge → sufficiency → hypothesis → KPI → disposition

| Gate | Decision | Canonical route | Mandatory evidence in this fixture | Conforming exit | Failure if the capability is absent or the gate is bypassed |
| --- | --- | --- | --- | --- | --- |
| **Q0 — grant technically current** | Is the raw token/grant unexpired and unrevoked? | S1 → T2 | issuer, issuance time, technical expiry | token is current; this alone is necessary but not sufficient | **absent:** no expiry is tracked at all. **bypassed:** an expired token is used anyway. Neither is the failure this scenario targets. |
| **Q1 — semantic preconditions declared** | Are the conditions that justify the grant (beyond token validity) explicitly declared and separately queryable? | S1/S10 | named source system per condition, condition logic | preconditions exist as first-class, queryable facts, not implicit assumptions | **absent:** the architecture has no place to declare a precondition beyond token expiry — this is the baseline gap this scenario targets. **bypassed:** preconditions are declared but not wired to any real source. |
| **Q2 — requalification at time of use** | Immediately before executing a queued action, are all declared preconditions re-queried against current state? | S10/S14 → T1 | query timestamp at or immediately before execution time, not queue time | requalification query occurs at T2, not reused from T1 | **absent:** no re-query capability exists; the T1 result is carried forward unconditionally — this is the core TOCTOU gap. **bypassed:** the capability exists but this run skips it (e.g. a race condition reads a stale cache instead of live status; see V3). |
| **Q3 — targeted, scoped response** | Is the response to a detected change scoped to the affected shard/action rather than the whole batch? | T3/T4 | per-shard/per-action requalification result | only the affected unit is held/escalated; unaffected units proceed | **absent:** no per-unit scoping exists, so any detected change blocks or delays the entire batch. **bypassed:** scoping exists but this run applies a blanket stop anyway. |
| **Q4 — bounded closure under ambiguity** | If status is unavailable or rapidly changing, is there a declared stop/expiry/hysteresis rule? | S3 → T3 | timeout value, default-safe action, anti-oscillation rule | ambiguity produces a bounded, safe non-execution with expiry, not infinite HOLD or rapid flip-flopping | **absent:** no bounded rule exists; the system either hangs (Type 1) or oscillates. **bypassed:** a rule exists but this run ignores it. |

## 10. Deterministic gate logic

1. Passing Q0 (token current) does not by itself pass Q2 (preconditions still hold). Token validity and semantic-condition validity are independent; neither substitutes for the other.
2. Q2's query must occur at or immediately before the actual execution instant. A query result reused from queue time, however recently obtained at the time, does not satisfy Q2.
3. A detected change at Q2 does not default to a blanket batch-wide stop; Q3 requires the response to be scoped to the affected unit unless the detected change is itself declared batch-scoped.
4. Absence of a capability (no precondition declared at Q1, no re-query capability at Q2) and bypass of an existing capability (a working re-query mechanism this run did not use, e.g. a cache-read race) are recorded as **distinct** failure classes, because they carry different implications for what a comparator architecture would need to add.
5. An inconclusive or unavailable status read at Q2 is treated as a bounded, expiring non-execution (Q4), not as silent permission to proceed and not as an unbounded wait.
6. Repeated condition flapping (a freeze lifting and re-arming within a short window) triggers the hysteresis rule declared in §8; each new transition is not treated as an independent, unrelated event.

EP requalifies and, where resolution requires another owner's decision, escalates. It does not itself lift a freeze, close an incident, or grant itself a freeze exception.

## 11. Two routes through the same event

### 11.1 Route N — requirements not satisfied for the event

| Step | Local behaviour | Gate result | Propagated consequence |
| --- | --- | --- | --- |
| Q0 | token checked, still within 90-minute window | PASS | superficially looks authorized |
| Q1 | no separate precondition object exists; incident/freeze status was only ever consulted once, at queue time | capability absent | nothing exists to re-check |
| Q2 | not performed — there is no re-query step before execution | absent | the T1 snapshot is used unconditionally at T2 |
| Q3 | not applicable — no detection occurred, so no scoped response was triggered | bypassed by construction | the full queued batch proceeds regardless of intervening changes |
| Q4 | not applicable | absent | no bounded-ambiguity handling exists because ambiguity was never detected |

Propagated consequence: shard 9 restarts at 14:42 under a live token but against conditions that no longer justify it — either a wasted, non-zero-risk restart (incident already resolved) or a restart during an active data-integrity freeze.

### 11.2 Route Q — requirements satisfied for the event

| Step | Quality-plan behaviour | Gate result | What moves forward |
| --- | --- | --- | --- |
| Q0 | token confirmed current | PASS | necessary precondition satisfied |
| Q1 | incident-open and no-freeze declared as separate, independently queryable conditions at grant issuance | PASS | preconditions exist as first-class facts |
| Q2 | immediately before the 14:42 execution, both conditions are re-queried live: `INC-5521 = RESOLVED`, `db-7.freeze = ACTIVE` | FAIL (correctly) | staleness is detected before any action executes |
| Q3 | only the shard-9 action is held; the other 11 shards' independent queue entries are unaffected unless their own Q2 also fails | scoped `DBC_REQUALIFY` | no unnecessary batch-wide delay |
| Q4 | not entered — the read was conclusive, not ambiguous | n/a | `DBC_DENY` (no longer needed) is recorded for shard 9; if a freeze-exception path is pursued separately, `DBC_ESCALATE` is recorded instead |

What moves forward: no unnecessary restart occurs, no freeze is violated, and the record shows exactly which condition changed and when.

## 12. Adversarial / stress variants

### V0 — clean case (nominal continuity)
Neither condition changes between T1 and T2. Requalification at Q2 correctly confirms both conditions still hold, and the action proceeds at 14:42 without unnecessary delay. This variant exists to show that the correct behavior is targeted revalidation, not indiscriminate re-verification or default blocking — a system that stalls or escalates every queued action, changed or not, does not pass this variant on equal terms with one that requalifies only when warranted.

### V1 — condition resolved (stand-down)
The incident is resolved before T2 (as in §3). Correct disposition: `DBC_DENY` — the action is simply no longer needed, not merely inadmissible.

### V2 — new blocking condition (freeze)
An unrelated freeze becomes active before T2 (as in §3). Correct disposition: `DBC_ESCALATE` to the freeze owner if a legitimate exception path exists in-scenario, or `DBC_DENY` with the freeze recorded as the reason if no such path exists within the response horizon.

### V3 — the recheck reads a stale cache
A requalification capability exists and appears to run at T2, but reads a status value cached at an earlier time (e.g. a five-minute-old cache layer) rather than a live query. Tests whether "a check occurred" is verified as sufficient, or whether the check's own input freshness is itself examined — the recursive form of the same failure, one layer down.

### V4 — status unavailable
The incident-management or freeze-status system is unreachable at T2. Tests whether this produces a bounded, safe non-execution with a declared retry/expiry (Q4), rather than either executing on the last-known value or hanging indefinitely.

### V5 — mixed batch validity
Across the 12 queued shard actions, some shards' conditions remain valid at their respective execution times and others do not. Tests whether requalification and its consequence are correctly scoped per shard (Q3) rather than the whole batch being held or released as one unit because one shard's conditions changed.

### V6 — flapping conditions
The freeze is lifted and re-armed twice within a short window before the queued action's turn arrives. Tests the hysteresis/anti-oscillation rule declared in §8 and required by S3, rather than treating each flap as an independent, unrelated re-evaluation that resets all state.

## 13. Test arms

### 00I-A0 — token-only check
Executes any queued action whose grant token has not technically expired; no separate semantic-precondition model exists.

### 00I-A1 — queue-time precondition check
Checks incident/freeze status once, when the action is queued, and carries that result forward; representative of a system that looks like it has a freshness check on casual inspection but checks at the wrong time.

### 00I-A2 — strong peer with partial live recheck
Re-queries incident status live immediately before execution (closing V1), but does not model or re-query the independent freeze condition (still exposed to V2) — configured with the strongest materially relevant capability available to that class of system, per 00D v0.3 §5.1.

### 00I-A3 — 00I-A2 + minimal EP / DBC decision-boundary semantics
Adds: all declared preconditions modeled and re-queried live and independently at time of use (not only the most obvious one), per-unit scoping of requalification (Q3), and a bounded hysteresis rule for ambiguous/flapping conditions (Q4).

00I-A3 is not presumed superior. If 00I-A2 already re-queries every declared precondition live, scopes its response per unit, and has a working hysteresis rule, the differential claimed for 00I-A3 is materially weakened. When the scenario is later admitted into a DBC execution, these local arms should be mapped explicitly to the applicable `DBC-R#` configurations rather than treated as a third global comparator namespace.

## 14. Candidate measures

Primary:

- stale-execution rate (queued actions executed after a declared precondition changed, undetected);
- unnecessary-hold rate (queued actions delayed or escalated despite no material change — the V0 counterweight);
- targeted-scope precision (whether a detected change correctly affects only the implicated unit, per V5);
- requalification latency (added time between scheduled and actual execution when a recheck is triggered);
- control overhead (additional queries, messages, latency versus 00I-A0);
- oscillation/hysteresis compliance under V6.

Secondary:

- rate of V3-style stale-cache reads passing as a valid recheck;
- rate of V4 status-unavailable events resolved as bounded non-execution versus silent execution or unbounded wait.

## 15. Candidate hypothesis and falsifier

### Hypothesis

Under matched resource budgets, explicitly modeling every semantic precondition of a time-boxed grant and re-querying each independently and live at time of use, scoped to the affected unit, reduces stale execution without a material increase in unnecessary holds, relative to a token-validity check or a queue-time-only precondition check.

### Falsifier

The hypothesis is weakened or rejected if:

- 00I-A2 already re-queries every declared precondition live (not only the most obvious one) at equal or lower overhead;
- 00I-A3 shows no material reduction in stale-execution rate over 00I-A2;
- 00I-A3's added overhead is not offset by a measurable gain on the primary measures;
- 00I-A3 shows a materially higher unnecessary-hold rate than 00I-A2 under V0, indicating the added checking is indiscriminate rather than targeted.

The case does not test general incident-management practice, change-freeze policy design, or that Ecosystem Positioning improves every scheduling system. It tests whether the specific gate sequence in §9 is followed or bypassed under the declared fixture.

## 16. Why this scenario matters

It separates two things that are easy to conflate: whether a grant is still *valid* (a token/expiry question, already well solved by ordinary access-control systems) and whether the *situation the grant was issued for* still holds (a semantic, contextual question that token validity does not answer). A system can be fully correct about the first and silently wrong about the second, and nothing about a functioning token system will reveal that on its own.

## 17. Relationship to corpus

Read with:

- [Decision Boundary Challenge v0.2](../DECISION_BOUNDARY_CHALLENGE_v0.2.md), especially **DBC-C02 — semantic TOCTOU** and **DBC-C01 — nominal continuity** (the latter grounds V0 here);
- [00 — Canonical Requirements: Challenges, Sufficiency Conditions, Hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), for S1, S3, S10, S14, T1, T2, T3, T4, H2, H5, H6 exactly as defined there, including the existing worked material-break/revalidation route this scenario follows;
- [00H — Batch Opportunity Beyond Authority](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.1.md), which this scenario's own V5 in that document flagged as a bordering condition;
- [01H](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) and [01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) for freshness, revalidation-condition and signalling vocabulary.

**Vocabulary note.** This scenario uses the DBC namespaced disposition vocabulary (`DBC_EXECUTE` / `DBC_DENY` / `DBC_REQUALIFY` / `DBC_ESCALATE`) exactly as defined in Decision Boundary Challenge v0.2 §3. Unlike 00H, this scenario does not exercise `DBC_REPOSITION_RECONTRACT` or the full `RepositionIntent`/`AuthorityResponse` exchange as its primary mechanism, because the agent already holds sufficient authority; the tested failure is revalidation of that authority's preconditions, not acquisition of new authority. A freeze-exception request in V2, where pursued, is a bounded request with its own response horizon, not the C12/00H re-contracting chain.

**Comparator/product-annex boundary.** No implementation annex exists yet for 00I. If one is added later (e.g. against a specific workflow-orchestration or infrastructure-automation product), it must apply the same frozen fixture — grant terms, timing, source systems, gate register — without changing the event, actors, deadlines or outcome vector to favour a product or EP.

**Status:** public working reference failure scenario and proposed quality-gate plan; not a real incident, a deployed change-management policy, a safety case, a product comparison, an adopted standard, or a validated proof of EP effectiveness.

This scenario is intentionally framed in infrastructure/operations terms, a domain without an existing dominant "this is already solved" control layer for the specific semantic-freshness gap under test — unlike a purely financial cap/aggregation case, where mature fraud-control practice can make the underlying gap harder to see. Its value is architectural clarity and falsifiability, not realism of the fictional company or its numbers.

## Editorial continuity note — bounded staleness/revalidation scenario, not the whole Positioning architecture

00I is the bounded Semantic TOCTOU reference scenario and quality-gate plan for DBC-C02. The Northwind Cloud Ops case, its grant conditions, and the Q0–Q4 gate register remain the controlling facts and test logic for this scenario.

It does **not** define the complete Ecosystem Positioning architecture, the full DBC challenge-pack family, every possible staleness or revalidation condition, or later signalling/gradient work. 00E, 00F, 00G and 00H remain independent reference scenarios; 00I is a cumulative addition alongside them, not a silent amendment to any of them.