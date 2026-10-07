# STAMP/STPA independent DDS exercise — maintenance and critical supply

Document version0.1 ·6 October2026 ·Codex, same analyst/model author.

The current method entry point is the [DDS Canonical Method Index](../../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md). This report is incorporated as a **Simplified DDS Gate-A** technology-specific implementation instance under the [Gate-A challenge–trajectory contract](../../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), not another DDS method. Its frozen Run Card retains the pre-split DDS identity used at execution time. Its binary fixture assertions do not establish Gate-B architecture verification, Gate-C deployment/population acceptance, representative sampling or a success probability.

[Run Card](./RUN_CARD.json) · [frozen source/data](./FREEZE.json) · [actual result](./runs/2026-10-06-02/RESULTS.json). Cryptography50.0.1 is the pinned installed dependency. R01 mathematical0.1/virtual0.3 and the prior HEW runs remain unchanged. No source-native theorem is inherited by these different laws.

## Step1 — task, losses and hazards

Synthetic task: issue a safe, useful maintenance decision while maintaining a declared critical supply. I completes admitted maintenance with confirmed safe equipment and supply; M explicitly delivers an authorized deferment while supply continues; incomplete remains unresolved; P is a materially unsafe or unauthorized realized control. There is no probability law or claim of representative industrial performance.

Selected losses: L1 harm to a maintenance worker; L2 interruption of required critical supply; L3 unauthorized control; L4 loss of the useful maintenance window. Selected system hazards: H1 maintenance entry while equipment remains energized; H2 removal of required pump supply without admitted backup; H3 realized control/entry beyond mandate. A late unresolved decision can lose value without automatically becoming P.

Constraints: prevent entry until de-energization is confirmed; preserve admitted supply/backup; act within the legitimate mandate; distinguish sent commands from applied effect; use a bounded deferment only when explicitly admitted.

## Step2 — control structure and process models

~~~mermaid
flowchart TD
  O[Operation owner] -->|maintenance and supply mandate| C[Maintenance controller]
  C -->|stop command| A[Pump actuator]
  A --> P[Pump and critical supply]
  P -.->|current state and effect feedback| C
  B[Backup supply] -.->|availability and admissibility| C
  C -->|admitted entry or explicit deferment| W[Maintenance access gate]
  W --> M[Maintenance operation]
  M -.->|completion or unresolved state| C
~~~

The controller model contains equipment state, maintenance request, current authority, supply obligation, backup, command application feedback and permitted deferment. These are synthetic trusted observations in this bounded exercise, not validated physical sensors. An operation owner is not simulated as an accurate real person.

## Step3 — unsafe control actions

| Control | Unsafe context/category | Constraint |
|---|---|---|
|Stop not provided|Maintenance needs de-energization before entry|Keep entry gated until a permitted stop is applied|
|Entry provided|Actual equipment remains energized|Confirmed de-energization before entry|
|Stop provided|Required supply would be removed without backup|Admit backup or deliver authorized deferment|
|Stop/entry provided|Current mandate is absent|No realized control outside mandate|
|Entry provided too early|Stop was sent but not confirmed|Use actual effect feedback|
|Entry response too late|The useful window already expired|Report incomplete/value loss rather than successful maintenance|
|Maintained block too long|Safe current completion exists but is withheld|Bound the maintained gate; duration requires its own timing profile|

The executed enumerator covers64 actual contexts of the discrete stop/entry pair. It does not exhaust every control action, continuous-duration class or organizational loss scenario. Potentially unsafe action provision and realized P outcomes are distinct.

## Step4 — causal loss scenarios

1. Command success is assumed from transmission: the stop is not applied, yet entry is enabled; energized maintenance results.
2. Backup is assumed from its name: the owner relies on a nonexistent source and stopping breaks critical supply.
3. A process model omits the mandate or uses an old one: seemingly correct control is unauthorized.
4. Sensor feedback is unavailable: the qualified model stays incomplete; it does not convert uncertainty into safe-state evidence.
5. A conservative stop/hold blocks a useful window: loss of completion remains visible; it is not a solved mission.
6. A deferment is returned where the owner never admitted it: it cannot receive M credit.
7. A later real implementation may suffer delayed/false feedback or competing controllers; those mechanisms need independent source/plant calibration.

## Executed results and value boundary

The10 narrative cases produce4 I,2 M,0 P and4 incomplete under the qualified model. All306 registered assertions pass, including256 actual-context checks,30 scenario assertions and20 observation/effect-boundary assertions. An intentionally open-loop misuse produces5 violating cases; it is a diagnostic, not a fair industrial comparator or proof that STPA outperforms other methods.

STPA is an analysis method; this result executes our derived finite model and exercises its context/feedback constraints. It does not certify analysis completeness, expert agreement, plant safety or human effectiveness. A competent conventional interlock may implement the same constraints and receives full credit.

Work fields are abstract state-query/command/feedback counts in a model. Real sensor costs, engineering/analysis effort, controls integration, staffing, downtime and plant dynamics are unscored. The source supports the four-step method; it is not evidence that this synthetic analysis captures a real facility.

Pre-execution amendmentA1 corrects the distinction between potentially unsafe commands and realized violations. The unexecuted initial source/freeze was preserved locally; no result was discarded or relabelled.

Primary method source: [MIT STPA handbook route](https://psas.scripts.mit.edu/home/books-and-handbooks/), using the prior pinned basic-method review. No handbook text/binary is redistributed.


Recorded successorA2 separates controller observations from private actuator-failure facts. Stop application is now obtained through a plant callback after command selection. Original run01 and its source/card/freeze are preserved; run02 changes no narrative, law or expected delivery threshold. Public run02 is self-contained; complete older source sets remain in local custody.
