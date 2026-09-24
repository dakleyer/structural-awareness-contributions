# Annex 00I-A01 — AWS Step Functions / RDS implementation trajectories for Semantic TOCTOU

| | |
|---|---|
| **ID** | 00I-A01 |
| **Type** | Product/platform implementation-trajectory profile |
| **Status** | Candidate draft · source-reviewed · unexecuted · not W3-admitted · not a product benchmark, certification or vendor-failure claim |
| **Version · date** | v0.1 Draft · 2026-09-24 |
| **Evidence freeze** | 2026-09-24 |
| **Parent scenario** | [00I — Semantic TOCTOU / “The Patch That Undid the Fix” v0.2 Draft](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.2_DRAFT.md) |

> **Three-trajectory implementation analysis.** This profile compares (1) an ordinary console-first workflow, (2) a defended state-of-the-art implementation that should be allowed to pass the base 00I case, and (3) that same defended implementation, frozen before results, after an observable but previously unmodeled regime/source/dependency change. It does not report that AWS Step Functions, Amazon RDS, Systems Manager or DynamoDB fails 00I.

## 1. Claim in one sentence

The useful 00I comparison is not “bad AWS versus EA.” It is:

**ordinary implementation → defended top-notch implementation → the exact same defended implementation after its previously sufficient decision-basis model becomes stale.**

The differential under test is whether a system can recognize that the *model of what must be rechecked* has become insufficient, requalify the affected decision boundary and adapt the observation window before actuation. A strong conventional implementation that already does this at equal or lower burden falsifies or narrows the EA differential.

## 2. Concrete technology stack

The first implementation family uses only ordinary current AWS building blocks:

- **AWS Step Functions Standard Workflow** — orchestration; Wait separates qualification time from actuation time; Task invokes later work; Choice can implement explicit guard branches.
- **Amazon RDS / PostgreSQL-like database** — target of the delayed configuration/reboot operation.
- **AWS Lambda or AWS SDK integration** — pre-action guard and current-state reads.
- **AWS Systems Manager Change Calendar** — current OPEN/CLOSED change state queried with GetCalendarState.
- **Amazon DynamoDB** — decision/control record, source-set version, configuration generation and optional optimistic/conditional write binding.
- **Amazon EventBridge** — early invalidation signal for calendar changes; not treated as authoritative by itself because Change Calendar event delivery is documented as best effort and can have scheduling tolerance.
- **CloudWatch / execution history** — observability and trace evidence.
- **IAM** — workload identity and least-privilege execution.

Systems Manager Change Manager may strengthen an existing-customer implementation with approval/freeze workflows, but AWS documents that Change Manager stopped accepting new customers on 7 November 2025. It is therefore optional evidence, not a required 2026 baseline component.

## 3. Three implementation trajectories

| Route | Configuration | Expected role in the experiment |
|---|---|---|
| **AWS-I0 — ordinary / OOTB-competent** | Workflow Studio state machine: qualify rollback → Wait → Task/Lambda → RDS change/reboot; normal IAM, retries/timeouts, idempotency and execution logging. The decision facts captured before Wait are passed forward unless the designer explicitly adds new current-state reads. | Should expose the basic 00I failure without requiring a broken product or stolen credential. |
| **AWS-I1 — defended top-notch** | I0 plus pre-action Lambda/Choice gate; current incident read; GetCalendarState at action time; current configuration/deployment generation; DynamoDB version/ConditionExpression or equivalent compare-before-act binding; explicit source timestamps; event-driven invalidation as optimization; bounded retry/hold; human owner; full trace. | Should be allowed to close the original Patch-A/Patch-B/freeze case. If it cannot, the implementation is not a fair strong peer. |
| **AWS-I2 — same frozen top-notch route under latent regime drift** | Exactly the I1 code, guard logic, configured source set and thresholds are frozen. Then the legitimate policy/source/dependency model changes before the next action. No post-outcome recoding of I1 is permitted. | Tests whether the system requalifies the validity of its own control model, not merely whether every control in that old model still passes. |

A future EA-enabled branch must use the **same I1 technical substrate and resource envelope**. EA does not get extra oracle facts, privileged APIs or a later code rewrite.

## 4. AWS-I0 — ordinary console-first route

A plausible quick implementation is:

qualify Patch A → Wait until 14:42 → Task invokes Lambda / AWS SDK → modify/reboot RDS → success/failure handling.

This is a normal Step Functions shape. AWS documents Wait as a state that delays the workflow before the configured Next state, and Task as the state that performs work through a Lambda function, supported AWS service or API.

I0 can be technically competent:

- correct IAM;
- valid Step Functions definition;
- timeout/retry handling;
- idempotency key;
- valid RDS request;
- CloudWatch/Step Functions execution history;
- no duplicate completion.

But none of those facts automatically re-establish:

- whether INC-5521 is still active;
- whether the current change calendar is OPEN;
- whether cfg-217 is still the operative decision basis;
- whether Patch B has superseded Patch A;
- whether the set of authoritative sources itself has changed.

Therefore I0 is expected to fail the base stale-decision branch while remaining an ordinary implementation rather than a strawman.

## 5. AWS-I1 — defended top-notch route

I1 is deliberately strong and should pass the original 00I base branch.

Immediately before RDS actuation:

1. **Read current incident state** from its authoritative store.
2. **Call GetCalendarState** for every currently configured applicable Change Calendar. AWS documents that multiple calendars return OPEN only when all specified calendars are open.
3. **Read current configuration/deployment generation** and the relevant parameter-group/configuration state.
4. **Compare against the qualified decision-basis record** stored with Patch A.
5. **Use conditional/version binding** for the control record. DynamoDB optimistic locking / ConditionExpression can reject an update when the version changed after the earlier read.
6. **Treat EventBridge as early invalidation only**, then perform authoritative reads at the decision boundary. AWS documents Change Calendar EventBridge delivery as best effort with up to 15-minute scheduling tolerance.
7. **Choice/guard outcome**:
   - unchanged/current → EXECUTE;
   - material change → REQUALIFY;
   - freeze/clear supersession → DENY or route to legitimate exception owner;
   - unavailable/ambiguous state → bounded non-execution, not silent permission.
8. **Preserve execution trace** including source/version/timestamps, guard result and actual RDS request.

This conventional architecture can satisfy Q0–Q6 for the original case. That is intentional.

## 6. AWS-I2 — same top-notch implementation under regime drift

### 6.1 Freeze the good implementation first

Before the drift is injected, freeze:

- I1 state-machine definition and Lambda/guard code;
- source list and source ownership;
- applicable Change Calendar set;
- policy/source-set version understood by I1;
- decision-basis schema;
- config/dependency fields checked before actuation;
- freshness thresholds;
- DynamoDB version-binding logic;
- resource/time/human budget.

I1 must first pass the ordinary base case and the valid-continuity control.

### 6.2 Primary drift — authoritative source-set change

At t0, the legitimate change-governance basis is:

- Ops Change Calendar A;
- incident source;
- local db-7 configuration generation.

I1 correctly checks all three.

Before the next queued remediation reaches actuation, the legitimate governance owner publishes **PolicySet v18**. The new policy adds a second independently owned **Finance Settlement Calendar B** to the applicable freeze set for db-7 during settlement operations. Calendar A remains OPEN; Calendar B is CLOSED.

Nothing is hacked:

- identity remains valid;
- I1 code remains unchanged;
- Calendar A returns the expected value;
- local db generation is unchanged;
- all old I1 checks can still pass.

The material change is that **the set of facts that constitutes a sufficient decision basis has changed**.

The drift is observable: PolicySet version/lineage or another declared governance signal shows that v18 superseded v17. What is not pre-programmed into the frozen I1 route is the new semantic dependency on Calendar B.

### 6.3 What counts as a conventional peer pass

I1/I2 passes if, without post-outcome recoding, it already has an equivalent generic mechanism that:

- discovers/loads the current policy/source set;
- detects that its previously frozen source/dependency set is stale;
- adds Calendar B or otherwise obtains the current governing determination;
- re-runs the affected guard;
- blocks/requalifies before RDS actuation;
- does not blanket-stop valid-continuity runs unnecessarily.

Examples of acceptable conventional mechanisms include dynamic policy-as-code, current source-set lookup, signed policy version references, dependency discovery, or another equivalent control.

A pass at equal or lower burden counts **against** an EA-specific differential.

### 6.4 What the EA/Requirements route is expected to do

EA is not expected to “guess” Calendar B from nowhere. The drift must produce an observable material signal inside the declared fixture.

The EA route should instead:

1. preserve the original decision basis, including policy/source/dependency version;
2. notice that the basis itself is no longer current (S10/S11/S14; T1/T2/T4);
3. emit REQUALIFY rather than treating all old checks as a continuing PASS;
4. reopen only the affected observation boundary;
5. acquire the current source/dependency set from the legitimate owner/interface;
6. add Calendar B to the current W(d,t) or preserve UNKNOWN if compatibility/current semantics cannot yet be established;
7. re-evaluate the queued Patch A;
8. execute only if the new basis supports it inside the response horizon.

This is the sense in which 00I tests **adaptive requalification under regime change**. It is adaptation of the decision boundary and observation window, not autonomous invention of policy or authority.

## 7. Drift family

The primary source-set drift above is the first executable branch. Later matched variants may test the same architecture without changing the core claim:

| Drift | Change after I1 freeze | Failure pressure |
|---|---|---|
| **D1 — source-set drift** | new legitimate Finance calendar/policy source becomes material | old guard checks all old sources correctly but misses a newly applicable source |
| **D2 — dependency drift** | effective DB behavior becomes dependent on a shared parameter group / new controller not present in the original local dependency set | local generation/version stays current while the composed decision basis changes |
| **D3 — causal/data drift** | incident remains OPEN and lag remains high, but the causal diagnosis changes | status-only guard passes while the action rationale is stale |
| **D4 — freshness-regime drift** | source validity horizon shortens materially under a critical business period | previously sufficient cache/freshness threshold becomes insufficient |
| **D5 — adversarial relocation** | an authorized/adaptive adversary moves the material change through a legitimate but previously non-material dependency path without breaking IAM | tests whether controls follow changing dependency/authority relations rather than only known endpoints |

D5 must be tightly preregistered. “Attacker” is not permission to inject oracle knowledge or arbitrary compromise.

## 8. Three decisive matched tests

### Test A — OOTB failure

Run AWS-I0 on:

- valid-continuity branch;
- base Patch-A/Patch-B/freeze branch.

Required result:
- continuity executes;
- stale base branch exposes the failure.

If I0 already requalifies current basis and passes both, record that result; do not force failure.

### Test B — top-notch control

Run frozen AWS-I1 on the exact same branches.

Required fair-peer result:
- continuity executes without material unnecessary burden;
- base stale branch is detected and prevented/requalified;
- Q0–Q6 evidence is reconstructable.

If I1 cannot pass the base case, strengthen it before the drift experiment.

### Test C — regime drift

After I1 is frozen and has passed Test B, inject D1 without changing I1 code.

Run two matched configurations:

- **C-peer:** frozen AWS-I1 under D1;
- **C-EA:** same AWS-I1 substrate/resource budget plus the pre-registered EA decision-basis/version/requalification semantics, also frozen before D1.

Compare:

- material-drift detection;
- false continuation;
- current source-set recovery;
- targeted re-entry precision/recall;
- requalification latency;
- remaining response margin;
- unnecessary hold/false containment;
- total control burden.

The key question is:

> Does a top-notch implementation that is correct for the old regime remain correct when the **definition of sufficient current state** changes, and can EA improve that transition without simply adding more static checks?

## 9. Requirements mapping

The drift test remains inside the current requirements system:

- **S3** — context/regime change, re-entry and bounded escape;
- **S10** — material change between commitment and execution;
- **S11** — owner/source/version/scope and material cross-domain coupling;
- **S14** — evidence needed at each transition and re-entry;
- **S9/S12/S13** where multi-owner composition and intervention/history become material;
- **T1** — detect an observable material break in the decision basis;
- **T2** — preserve source/version/freshness/dependency in the qualified handoff;
- **T3** — only an authorized bounded response may follow;
- **T4** — requalify while a useful response remains possible;
- **H5** — shortened validity/churn increases requalification pressure;
- **H6** — adapt window/freshness effort to current risk, capacity and response horizon.

CAND-R4 remains the check-to-act binding clarification. D1 does not create S15/T5/H7.

## 10. Falsifiers

The adaptive EA differential is weakened or rejected if:

- AWS-I1 already discovers and requalifies the changed source/policy/dependency set under D1 at equal or lower burden;
- the EA branch requires an oracle, manual recoding or a signal unavailable to the peer;
- EA wins only by always HOLDing after any policy version change;
- EA adds Calendar B only because the fixture tells it the answer rather than through a pre-registered legitimate re-entry/source-discovery route;
- the drift is not materially relevant to the queued action;
- the improvement arrives after the response horizon;
- total added burden outweighs the measured reduction in false continuation under the declared risk/resource criterion.

## 11. Official product sources reviewed — 24 September 2026

- AWS Step Functions — state machines / Wait / Task / Choice:
  - https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html
  - https://docs.aws.amazon.com/step-functions/latest/dg/state-wait.html
  - https://docs.aws.amazon.com/step-functions/latest/dg/state-task.html
  - https://docs.aws.amazon.com/step-functions/latest/dg/state-choice.html
- Amazon RDS — pending modifications / parameter application / reboot:
  - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html
  - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/parameter-groups-overview.html
  - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html
- AWS Systems Manager Change Calendar:
  - https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar-working.html
  - https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCalendarState.html
  - https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-systems-manager-event-examples.html
- Amazon DynamoDB conditional/version control:
  - https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_OptimisticLocking.html
  - https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html
- Optional existing-customer Change Manager strengthening:
  - https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html
  - https://docs.aws.amazon.com/en_en/systems-manager/latest/userguide/change-manager-account-setup.html

## 12. Claim boundary

This profile does not claim:

- that AWS Step Functions or RDS has a Semantic-TOCTOU defect;
- that an AWS best-practice implementation necessarily fails D1;
- that EA can detect an unobservable regime shift;
- that more telemetry is automatically safer;
- that PolicySet v18 or Northwind is a real AWS incident.

It tests a narrower proposition: **whether a previously excellent, frozen control implementation notices when the set/semantics of facts required for a sufficient action-time decision changes, and whether the EA requirements provide a more portable requalification discipline under that change.**

**Status:** source-reviewed design trajectory only; no run has been executed.
