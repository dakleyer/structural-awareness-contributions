# Annex 00I-A01 — AWS Step Functions / RDS implementation trajectories for Semantic TOCTOU

| | |
|---|---|
| **ID** | 00I-A01 |
| **Type** | Product/platform implementation-trajectory profile |
| **Status** | Candidate draft · source-reviewed · implementation skeleton published · unexecuted · not W3-admitted · not a product benchmark, certification or vendor-failure claim |
| **Version · date** | v0.2 Draft · 2026-09-24 |
| **Evidence freeze** | 2026-09-24 |
| **Parent scenario** | [00I — Semantic TOCTOU / “The Patch That Undid the Fix” v0.4 Draft](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.4_DRAFT.md) |
| **Predecessor** | [v0.1 Draft](./00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) |
| **Implementation skeletons** | [00I-AWS fixture package](./fixtures/00I-AWS/README.md) |

> **Three-trajectory implementation analysis.** This profile compares (1) an ordinary console-first workflow, (2) a defended state-of-the-art implementation that must first prove it can close the base 00I case, and (3) that exact defended implementation, frozen before results, after an observable regime/source/dependency change. It does not report that AWS Step Functions, Amazon RDS, Systems Manager, DynamoDB or EventBridge fails 00I.

## Executive view — three minutes

The experiment asks one question at three levels.

| Route | Plain-English description | What should happen |
|---|---|---|
| **AWS-I0 — ordinary** | “The rollback was approved, wait until its slot, then run it.” Good IAM, retries and logs; no special semantic requalification. | It may execute an old but still technically valid decision. This demonstrates the base failure without breaking AWS. |
| **AWS-I1 — top-notch** | “Before touching production, re-read every known material condition, serialize writers, verify version/freeze/incident state, and execute only while that state remains bound.” | It **must** pass the original 00I case. If it does not, strengthen it before using it as the peer. |
| **AWS-I2 — frozen top-notch under drift** | “Now keep that excellent implementation unchanged while the set, meaning, dependency or freshness of the facts needed for a safe decision changes.” | Outcome is deliberately unknown. The question is whether the peer notices its own previously sufficient control model became stale. |

The proposed EA differential begins only at the third route. If AWS-I1 already adapts generically to the drift at equal or lower burden, **that is a pass for the peer and evidence against an EA-specific differential**.

## 1. What each AWS component does — non-specialist reading

| Technology | Role in this fixture | Plain-English interpretation |
|---|---|---|
| **AWS Step Functions** | Orchestrates the delayed remediation workflow using Wait, Task and Choice states. | The process manager: “wait, check, branch, execute.” |
| **Amazon RDS** | Production database target whose configuration/reboot may be changed later. | The thing we are trying to repair without undoing a newer repair. |
| **AWS Lambda / AWS SDK integration** | Reads current state and performs guarded work. | The code that asks “is this still the right thing to do?” |
| **Systems Manager Change Calendar** | One authoritative operational freeze source queried with `GetCalendarState`. | “Are changes allowed right now?” |
| **DynamoDB** | Stores the decision-basis record, policy/source-set reference, application-level generation and short-lived execution lease. | The versioned control ledger shared by all writers. |
| **EventBridge** | Early signal that a calendar changed. | A notification bell, not the source of truth. |
| **CloudWatch / Step Functions history** | Execution and decision trace. | Evidence of what was checked and why the action did or did not run. |
| **IAM / organizational access controls** | Restrict material RDS changes to the change broker in the defended route. | Prevents another path from bypassing the version/lease protocol. |

The product boundary matters: RDS does not need to know Ecosystem Awareness. The control plane around it decides whether a queued intent is still valid.

## 2. Technical architecture and one critical fairness correction

### 2.1 Ordinary route

```text
incident evidence
      ↓
qualify rollback
      ↓
Step Functions Wait
      ↓
Task / Lambda
      ↓
RDS modify / reboot
```

This is deliberately ordinary, not defective.

### 2.2 Defended route

```text
                         ┌─────────────────────────────┐
incident / policy /      │ Versioned Change Broker    │
calendar / config ──────→│ decision basis + lease     │
                         └──────────────┬──────────────┘
                                        │
Step Functions: Wait → read current basis → acquire guarded lease
                                        │
                                        ↓
                                  Choice / gate
                              ↙ REQUALIFY   EXECUTE ↘
                    targeted re-entry       brokered RDS change
```

### 2.3 Why DynamoDB locking alone is not enough

A DynamoDB `ConditionExpression` can establish that the **broker record** has not changed since it was read. It does **not** make an unrelated RDS API call atomic with that DynamoDB write.

Therefore AWS-I1 uses a stronger, explicit fixture assumption:

> **single-writer change broker:** every material modification of `db-7` that can invalidate the queued decision — automated or human-initiated — must pass through the same broker/lease/version protocol. Direct mutation paths are denied by the configured execution permissions for the test environment.

Patch B is still human-decided, but the engineer submits it through the broker. The broker advances the application-level database generation and invalidates Patch A's previously qualified basis.

This makes Q6 meaningful. If a deployment permits bypass writers, the run is not the top-notch R1 configuration; it is a separate bypass branch and must be labelled as such.

**Important boundary:** `config_generation` in this fixture is an **application/control-plane generation**, not a claim that Amazon RDS exposes one universal native generation number for every modification.

## 3. Shared control objects

### 3.1 ChangeIntent

Each queued action carries a reconstructable basis:

```text
ChangeIntent {
  intent_id
  target
  desired_state
  incident_id
  qualified_at
  qualified_from_generation
  policy_manifest_version
  source_set_hash
  diagnosis_version
  grant_scope
  grant_expiry
  execute_at
  basis_freshness_budget
  status
}
```

### 3.2 PolicyManifest

```text
PolicyManifest {
  version
  effective_at
  target_scope
  applicable_sources[]
  dependency_refs[]
  source_owners[]
  freshness_rules[]
  supersedes
}
```

The manifest is not “EA magic.” A strong conventional architecture may implement equivalent policy-as-code, service catalog, CMDB, change-governance or dependency metadata.

### 3.3 ExecutionLease

```text
ExecutionLease {
  target
  lease_id
  holder
  expected_generation
  expected_basis_version
  acquired_at
  expires_at
}
```

All defended writers honor this lease. A stale expected generation/basis cannot acquire or consume the lease.

## 4. AWS-I0 — ordinary / OOTB-competent

### 4.1 Build

Use a Step Functions Standard Workflow:

1. `QualifyRollback` — Lambda records the rollback decision and `execute_at`.
2. `WaitUntilT2` — Step Functions Wait state.
3. `ApplyQueuedChange` — Lambda or AWS SDK integration invokes the RDS modification/reboot.
4. normal retry, timeout, idempotency and trace handling.

AWS documents that Wait delays a state machine until a relative or absolute time and then transitions to `Next`. Task states execute work through a worker or AWS service integration. Step Functions can also call AWS service APIs through AWS SDK integrations.

### 4.2 What I0 does well

- correct workload identity;
- least privilege for its role;
- valid workflow definition;
- retries/timeouts;
- idempotency;
- request validation;
- execution history;
- no intentional duplicate execution.

### 4.3 Why I0 can still fail

The workflow can carry the T1 decision forward unchanged. At T2, technical validity does not establish that:

- the incident remains open;
- the applicable freeze set is open;
- the diagnosis is still current;
- no later intervention superseded the rollback;
- the policy/source/dependency model defining those checks remains current.

Expected base result:

- valid-continuity branch → EXECUTE;
- Patch-B/freeze branch → likely false continuation unless the implementer independently added current-state controls.

If an ordinary implementation already performs all required current-state qualification, record that result rather than forcing a failure.

## 5. AWS-I1 — defended top-notch

AWS-I1 must be able to defeat the original 00I fixture before any adaptive claim is considered.

### 5.1 Build

Immediately before actuation:

1. **Load current ChangeIntent and PolicyManifest.**
2. **Read current incident state** from its declared authoritative source.
3. **Query every currently applicable Change Calendar** using `GetCalendarState`.
4. **Read current application-level target generation/config state.**
5. **Read current diagnosis/intervention lineage** required by the frozen manifest.
6. **Check freshness** of each material observation against the manifest.
7. **Acquire ExecutionLease conditionally** only if the expected target generation and basis version remain current.
8. **Choice / disposition:**
   - unchanged + sufficiently current → EXECUTE;
   - material change → REQUALIFY;
   - clear prohibition/supersession → DENY;
   - unavailable/inconclusive → bounded HOLD/ESCALATE.
9. **Apply through the single-writer broker.** The worker validates the still-live lease immediately before issuing the RDS change.
10. **Advance generation / release lease / record outcome.**

### 5.2 EventBridge is an accelerator, not proof

AWS documents Change Calendar state notifications through EventBridge as best effort with up to 15 minutes of scheduling tolerance. Therefore:

- an event may invalidate early;
- absence of an event does not establish current OPEN state;
- the defended route performs authoritative action-time reads.

### 5.3 Multiple calendars

AWS documents that `GetCalendarState` returns OPEN for multiple requested calendars only when all are open. Thus, if the current PolicyManifest says both Operations A and Finance B are applicable, the conventional peer has a direct way to enforce the combined freeze.

### 5.4 Base acceptance gate

Before AWS-I1 may enter drift testing it must:

- pass the valid-continuity branch without unnecessary HOLD;
- stop/requalify stale Patch A after Patch B;
- respect an active configured freeze;
- reject stale broker generation/version;
- preserve a reconstructable Q0–Q6 trace;
- close ambiguity within the declared horizon.

Failure here means **strengthen I1**, not “EA wins.”

## 6. AWS-I2 — same top-notch implementation under drift

### 6.1 Freeze first

After I1 passes, freeze:

- state-machine definition;
- Lambda/guard code;
- broker schema and lease logic;
- current PolicyManifest interpretation;
- source/dependency discovery route;
- current source set;
- freshness rules;
- thresholds;
- resource/time/human budget.

No code or rule changes are permitted after the drift outcome is observed.

### 6.2 What “adaptive” means here

Adaptive does **not** mean self-modifying code, omniscience or autonomous policy invention.

It means:

> when an observable signal shows that the basis used to qualify a decision is no longer current, the architecture can reopen the affected boundary, obtain the current legitimate basis, change the minimum necessary observation set, and re-decide before action.

If no observable material signal exists inside the declared boundary, neither EA nor the peer is credited with knowing the drift.

## 7. Drift ladder — do not force the peer to lose

The drift family is intentionally progressive. Stop as soon as the strongest peer demonstrates generic adaptation at the same or better frontier, or continue to the next preregistered stress only if the previous one is no longer discriminatory.

### D1 — policy/source-set drift — easiest strong-peer test

At t0:

```text
PolicyManifest v17
  incident source
  Ops Change Calendar A
  db-7 application generation
```

Later, the legitimate owner publishes:

```text
PolicyManifest v18
  incident source
  Ops Change Calendar A
  Finance Settlement Calendar B
  db-7 application generation
```

A = OPEN; B = CLOSED.

**Fairness rule:** if AWS-I1 already loads the current manifest dynamically, it should discover B and pass. That is a strong-peer success, not a failed experiment.

D1 therefore tests dynamic policy/source-set loading; it is not the deepest proposed EA differential.

### D2 — dependency drift — stronger adaptive stress

The policy wording remains stable, but the **material system relation changes**: `db-7` becomes a dependency of a Finance settlement process or is attached to a shared parameter/control domain that was not material under the old topology.

The drift is observable through a legitimate service/dependency manifest version, catalog relation or equivalent source available to both compared configurations.

The question becomes:

> does the control architecture re-evaluate which dependencies belong in the decision basis, or does it keep checking the old list perfectly?

A top-notch peer may absolutely implement dynamic dependency discovery and pass D2. That counts against the EA differential.

### D3 — causal/data drift

The incident remains OPEN and lag remains high, but the diagnosis changes from configuration regression to network/replica-path failure.

All infrastructure controls may be green. Reusing the old rollback because “the ticket is still open” fails.

### D4 — freshness-regime drift

A source that was safely usable with a five-minute freshness budget enters a high-risk settlement regime in which the legitimate owner changes the required validity horizon to seconds.

The data source is the same; the **meaning of sufficiently fresh** changed.

### D5 — adversarial relocation

A preregistered attacker/adaptive participant cannot forge grants, rewrite logs or alter hidden thresholds. It may only exploit legitimate routing/dependency changes so that the material state moves to a path the old basis did not treat as relevant.

This branch tests whether awareness follows changing relations rather than merely hardening known endpoints.

D5 is not admitted until actor capabilities, prohibited actions and observable signals are frozen.

## 8. The four matched configurations actually scored

The three narrative trajectories produce four scored configurations in the drift test:

| Configuration | Code/control state | Drift | Purpose |
|---|---|---|---|
| **I0** | ordinary | no/base | establish base failure/continuity |
| **I1** | defended top-notch | no/base | establish that conventional excellence closes ordinary TOCTOU |
| **I2-peer** | exact frozen I1 | D1–D5 | test generic adaptability of the peer |
| **I2-EA** | same technical substrate/budget plus preregistered EA basis/version/dependency/re-entry semantics | same D1–D5 | test differential under the identical drift |

I2-EA gets no later code rewrite, private oracle or extra authoritative source unavailable to I2-peer.

## 9. State transitions

### I0

```text
QUALIFY
  → WAIT
  → TECHNICAL VALIDITY CHECK
  → APPLY
```

### I1

```text
QUALIFY + RECORD BASIS
  → WAIT
  → LOAD CURRENT KNOWN BASIS
  → ACQUIRE GUARDED LEASE
  → REQUALIFY ALL CURRENTLY DECLARED MATERIAL CONDITIONS
      ├─ current / allowed → APPLY UNDER LEASE
      ├─ changed          → REQUALIFY
      ├─ prohibited       → DENY
      └─ inconclusive     → BOUNDED HOLD / ESCALATE
```

### I2-EA under drift

```text
QUALIFY + RECORD BASIS/MANIFEST VERSION
  → WAIT
  → CHECK WHETHER THE BASIS MODEL ITSELF IS CURRENT
      ├─ current → ordinary I1 requalification
      └─ stale   → TARGETED RE-ENTRY
                    → acquire current legitimate basis/dependencies
                    → rebuild minimum sufficient W(d,t)
                    → requalify
                    → acquire/renew guarded lease
                    → EXECUTE / DENY / ESCALATE
```

## 10. Outcome adjudication — no predetermined winner

| Outcome | Interpretation |
|---|---|
| **Peer passes drift at equal/lower burden** | No demonstrated EA differential for that drift family. |
| **Peer detects drift but cannot recover before deadline; EA does** | Possible differential in targeted re-entry / minimum-sufficient adaptation. |
| **Peer false-continues; EA requalifies correctly** | Supports the adaptive decision-basis hypothesis for this fixture. |
| **Both false-continue or both miss the observable drift** | EA implementation is insufficient; no positive claim. |
| **EA avoids error only through blanket HOLD/excessive search** | EA fails T4/H6 burden/continuity criteria. |
| **EA requires oracle facts or extra APIs unavailable to peer** | Invalid comparison; rerun after symmetry is restored. |

## 11. Tests

### Test A — continuity admission

No material state or basis changes.

Required: I0/I1/I2 configurations execute within their allowed latency/burden. A deny-all architecture fails admission.

### Test B — base Semantic TOCTOU

Patch B supersedes A and/or the configured freeze becomes CLOSED.

- I0: may fail; record actual result.
- I1: **must pass before drift admission**.
- I2 configurations: should reproduce I1 behavior in the non-drift control.

### Test C — D1 policy/source-set drift

Freeze I1, publish v18, set B=CLOSED.

Score I2-peer versus I2-EA. If the peer dynamically loads v18 and passes, D1 is not discriminatory.

### Test D — D2 dependency drift

Freeze the same implementation and change a material dependency relation with an observable current manifest/catalog signal.

Score detection, targeted re-entry and burden.

### Test E — D3/D4/D5

Only after the earlier branch is preregistered and its outcome boundary is understood. Do not keep inventing harder drift after observing results merely to obtain a difference.

## 12. Quality-plan and Requirements mapping

The implementation profile uses the parent Q0–Q6 gates and current Requirements:

- **S1:** grant applicability;
- **S3:** regime/context change and bounded re-entry;
- **S10:** material change between commitment and actuation;
- **S11:** owner/source/version/scope and cross-domain coupling;
- **S14:** evidence required at each transition;
- **S9/S12/S13:** composition/intervention/history when D2 or multi-owner drift makes them material;
- **T1:** observable material-break detection;
- **T2:** qualified source/version/freshness/dependency handoff;
- **T3:** bounded authorized response;
- **T4:** timely minimum-sufficient requalification;
- **H5/H6:** shortening validity/churn and adaptive window/freshness effort.

No S15/T5/H7 is introduced. CAND-R4 remains a clarification candidate for check-to-act binding.

## 13. Metrics

Report per branch/configuration:

- false-continuation rate;
- stale-action execution rate;
- basis-model drift detection;
- source/dependency-set recovery;
- targeted re-entry precision/recall;
- requalification latency;
- remaining response margin;
- unnecessary HOLD / false containment;
- total control burden;
- execution/denial correctness;
- evidence needed to reconstruct the final disposition.

Do not pool all drift families into a single unvalidated “adaptivity score.”

## 14. Implementation skeleton package

The companion package contains inspectable, non-deployed skeletons:

- `i0_ordinary.asl.json` — qualify → Wait → apply;
- `i1_top_notch.asl.json` — basis record → Wait → broker guard/lease → Choice → apply/requalify/deny;
- `i2_ea_drift.asl.json` — basis-model version check → targeted re-entry when stale → I1 guard/lease;
- `fixture_d1_source_set_drift.json`;
- `trace_contract.json`.

These files make the architecture concrete enough for review. They are **not** evidence of deployment or execution and remain outside W3 admission until the fixture/oracle/configuration is frozen through the normal process.

## 15. Source verification — official documentation reviewed 24 September 2026

### Step Functions

- state machines / AWS SDK integrations: https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
- Wait: https://docs.aws.amazon.com/step-functions/latest/dg/state-wait.html
- Task: https://docs.aws.amazon.com/step-functions/latest/dg/state-task.html
- Choice: https://docs.aws.amazon.com/step-functions/latest/dg/state-choice.html
- AWS SDK integrations: https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html

### RDS

- pending modifications / Apply Immediately: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html
- parameter groups / pending reboot: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/parameter-groups-overview.html
- reboot: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html

### Systems Manager

- GetCalendarState: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCalendarState.html
- Change Calendar EventBridge behavior: https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-systems-manager-event-examples.html
- Change Manager availability boundary: https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html

### DynamoDB

- optimistic locking: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_OptimisticLocking.html
- condition expressions: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html

## 16. External-review findings incorporated in v0.2

The profile was re-reviewed through four independent lenses.

### Architecture / Requirements lens

**Finding:** the adaptive claim is only meaningful if the drift supplies an observable legitimate signal and EA is not allowed to invent policy/dependencies.

**Correction:** explicit symmetry rule, frozen basis, targeted re-entry and no-oracle boundary.

### AWS engineering lens

**Finding:** DynamoDB optimistic locking alone cannot atomically protect an unrelated RDS call.

**Correction:** explicit single-writer change broker, shared lease/version protocol and denial of bypass mutation paths in the defended test environment.

### Experimental-design lens

**Finding:** D1 could be trivial for a genuinely dynamic policy engine, so assuming I1 fails would create a strawman.

**Correction:** drift ladder and stop rule; peer success at D1/D2 counts against EA.

### Executive-readability lens

**Finding:** the previous version introduced product names before stating the business question.

**Correction:** three-minute executive table, plain-English technology map and outcome-adjudication table precede the low-level implementation detail.

## 17. Claim boundary

This profile does not claim:

- that AWS Step Functions, RDS, Systems Manager, DynamoDB or EventBridge has a Semantic-TOCTOU defect;
- that an AWS best-practice implementation necessarily fails D1–D5;
- that EA can detect an unobservable regime shift;
- that a DynamoDB conditional write alone makes RDS actuation atomic;
- that more telemetry is automatically safer;
- that the Northwind scenario is a real AWS incident.

It tests the narrower proposition:

> **Can a previously excellent, frozen control implementation notice when the set, dependency, meaning or freshness of facts required for a sufficient action-time decision changes; and, under the same observable signals and resource budget, do EA's current requirements provide a more portable and minimum-sufficient requalification discipline?**

**Status:** source-reviewed implementation design with published skeletons; no execution result.
