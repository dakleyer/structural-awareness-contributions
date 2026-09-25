# 00F — Case-Study Extensibility Profile — v0.1

| | |
|---|---|
| **Family** | Systemic Divergence under Heterogeneous Local Windows and Shared Capacity |
| **Minimum instantiation** | [00F — The City That Stopped Safely](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) |
| **Extensibility method** | [A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) |
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

For an admitted extension:

\[
F_F\Rightarrow
(\neg P6\lor\neg P1\lor\neg P3\lor\neg P5)
\]

with P2 joining HOLD/search branches.

A23 makes the applicable 00F S/T route sufficient for those P invariants.

Hence a requirements-conforming in-family extension cannot exhibit the same local-correct/system-incompatible failure predicate, although it may fail for unrelated reasons.
