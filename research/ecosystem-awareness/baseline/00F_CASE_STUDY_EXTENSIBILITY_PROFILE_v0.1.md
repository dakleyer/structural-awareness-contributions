# 00F — Case-Study Extensibility Profile — v0.1

| | |
|---|---|
| **Family** | Systemic Divergence under Heterogeneous Local Windows and Shared Capacity |
| **Minimum instantiation** | [00F — The City That Stopped Safely](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) |
| **Extensibility method** | [A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) · [A26 success conversion](./00K_A26_FAILURE_TO_SUCCESS_MODEL_CASE_AND_EXTENSIBILITY_v0.1.md) |
| **Success Model Case** | [Coherent Shared-Capacity Requalification](./00F_SUCCESS_MODEL_CASE_SHARED_CAPACITY_REQUALIFICATION_v0.1.md) |
| **Status** | first-pass structural family profile |

> **Family claim.** Robotaxis, buses, emergency vehicles and Central Bridge are the minimum mobility scene. The structural case is that locally justified postures derived from heterogeneous windows become mutually incompatible over one material shared resource/decision surface after a frame change, while local safety/correctness can remain intact.

## 1. Kernel

\[
K_F=
\langle
multiple\ independently\ governed\ actors,\;
heterogeneous\ windows,\;
shared\ scarce\ resource,\;
material\ frame\ change,\;
locally\ defensible\ postures,\;
composition\ dependency
\rangle.
\]

The family failure \(F_F\) occurs when locally acceptable postures jointly consume or block the same resource/mission in an incompatible way because the shared decision surface is not sufficiently requalified.

Primary witness: **P6**. Supporting branches exercise **P1/P2/P3/P5**.

## 2. Inherited requirement route

The six 00F gates already define the portable route:

- Q0: **S1/S3/S9/S14 → T2/T3/T4**;
- Q1: **S3/S5/S10/S14 → T1/T2/T4**;
- Q2: **S5/S6/S9/S11/S14 → T2/T4**;
- Q3: **S1/S3/S4/S5/S14 → T2/T3/T4**;
- Q4: **S3/S10/S12/S14 → T1/T2/T4**;
- Q5: **S9/S11/S12/S14 → T1/T2/T4**, plus T3 for action/default.

## 3. Upward / vertical extensibility

**Strong extensions:**

- several corridors, municipalities or jurisdictions;
- regional logistics + emergency + public/private mobility systems;
- shared urban infrastructure with nested resource owners and multiple legitimate vetoes;
- multi-site industrial or cloud infrastructure where local controllers compete for shared capacity.

Scale may increase dramatically so long as the core remains **local validity + shared-resource incompatibility**, not centralized controller failure.

## 4. Downward extensibility

**Strong extensions:**

- one factory production cell where safety, maintenance and production controllers make different locally valid claims over one machine/time slot;
- one warehouse intersection shared by autonomous forklifts, picking agents and human safety control;
- one cloud cluster where deployment, incident response, backup and capacity controllers make incompatible local allocations;
- one hospital operating-resource scheduling problem at the level of beds/rooms/staff availability, provided the case is treated as resource/authority composition rather than clinical judgement.

The smallest fixture needs two independently justified postures and one shared material resource whose simultaneous use is incompatible.

## 5. Horizontal extensibility

**Strong candidates:**

- logistics hubs and loading windows;
- compute/GPU capacity allocation;
- factory-machine scheduling;
- appointment/room/staff allocation;
- energy or charging capacity;
- shared maintenance windows.

The bridge is not essential. **Non-fungible shared capacity under heterogeneous local frames** is.

## 6. Boundary

Out of family:

- ordinary congestion with no divergent decision frames;
- one controller making a bad routing decision;
- collision-avoidance failure itself;
- failures where all actors share one current authoritative resource state and simply violate it.

## 7. Conformance transfer

The evidence route is admission → [00K-A3 Route Q and matched-conflict controls](./fixtures/00K-A3-P3-00F/README.md) → no false closure on the tested P3 branches. The broader P6/P1/P5 family is not certified by this isolated result.

The [A25 §6 evidence boundary](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md#6-evidence-routes-and-conditional-transfer) applies: X1–X7 admit a mapping; passing frozen branches supports that implementation. A guarantee over every admitted extension additionally requires a separately proved base guarantee plus failure reflection and conformance preservation. Each listed domain remains a design case until separately executed or proved within a declared scope.

## Success-case route

The failure-family profile above is paired with the positive [**Coherent Shared-Capacity Requalification**](./00F_SUCCESS_MODEL_CASE_SHARED_CAPACITY_REQUALIFICATION_v0.1.md) Success Model Case. The success case keeps the same kernel and inherited S/T route, defines the positive bounded disposition, and applies the same upward/downward/horizontal admission boundary without introducing new canonical requirements.
