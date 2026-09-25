# 00I — Case-Study Extensibility Profile — v0.1

| | |
|---|---|
| **Family** | Semantic TOCTOU / Stale Decision-Basis Reuse |
| **Minimum instantiation** | [00I — The Patch That Undid the Fix](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) |
| **Extensibility method** | [A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) · [A26 success conversion](./00K_A26_FAILURE_TO_SUCCESS_MODEL_CASE_AND_EXTENSIBILITY_v0.1.md) |
| **Success Model Case** | [Action-Time Requalification](./00I_SUCCESS_MODEL_CASE_ACTION_TIME_REQUALIFICATION_v0.1.md) |
| **Status** | first-pass structural family profile |

> **Family claim.** PostgreSQL, rollback and a 40-minute queue are fixture parameters. The family is any system in which an action is correctly qualified at \(t_0\), remains technically executable, but a material part of the decision basis changes before \(t_1\) and the old determination is reused without sufficient requalification.

## 1. Kernel

\[
K_I=
\langle
qualified\ action@t_0,\;
deferred\ actuation,\;
material\ basis,\;
change@t_1,\;
technical\ validity\ survives,\;
action-time\ reliance
\rangle.
\]

Failure:

\[
F_I=
changed(material\ basis,t_0,t_1)
\land
execute(old\ determination,t_1)
\land
\neg requalify.
\]

Primary witness: **P5**.

## 2. Inherited requirement route

Core:

**S1/S3/S10/S14 → T1/T2/T3/T4.**

When another controller/human changes the same state:

**S9/S11/S12/S13** additionally apply.

Q6 check-to-act binding remains a clarification candidate, not a new requirement family.

## 3. Upward / vertical extensibility

**Strong extensions:**

- many queued changes across a distributed deployment;
- approval chains spanning several systems and owners;
- orchestration across application, infrastructure, data and policy controllers;
- long-lived plans containing many individually authorized actions whose bases can change independently.

The larger graph is still 00I if the key error is reuse of an earlier determination after material change.

## 4. Downward extensibility

**Strong minimal forms:**

- one scheduled script;
- one delayed API call;
- one cron job;
- one pending configuration change;
- one pre-approved payment/order/access change;
- one maintenance work order.

Only two times and one material state variable are required.

Example:

> a maintenance order is valid in the morning; the machine is repaired by another route before afternoon; the old work order remains signed and executes anyway.

That is 00I even without LLMs or multi-agent orchestration.

## 5. Horizontal extensibility

**Strong candidates:**

- software deployment/rollback;
- cloud/infrastructure configuration;
- industrial maintenance;
- access provisioning/revocation;
- scheduled financial/operational transactions;
- logistics dispatch or inventory moves;
- policy enforcement where an earlier eligibility/approval fact expires before actuation.

The domain changes. The semantics “qualified then, stale now” do not.

## 6. Boundary

Out of family:

- the original decision was already wrong at \(t_0\);
- the action never had a material delay;
- only the credential expired and no semantic state changed;
- the action fails technically rather than because its decision basis became stale.

## 7. Conformance transfer

For every admitted extension:

\[
F_I\Rightarrow\neg P5.
\]

A23 proves that canonical conformance to the applicable S1/S3/S10/S14/T1–T4 route entails P5.

Thus:

\[
C'\in Family(00I)\land Conf(R_I)\Rightarrow\neg F_I.
\]

This is the cleanest of the six transfer families because the failure predicate is almost exactly the P5 predicate.


## Success-case route

The failure-family profile above is paired with the positive [**Action-Time Requalification**](./00I_SUCCESS_MODEL_CASE_ACTION_TIME_REQUALIFICATION_v0.1.md) Success Model Case. The success case keeps the same kernel and inherited S/T route, defines the positive bounded disposition, and applies the same upward/downward/horizontal admission boundary without introducing new canonical requirements.
