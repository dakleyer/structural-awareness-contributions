# 00J — Success Model Case: Proposition-Scoped Provenance — v0.1

| | |
|---|---|
| **Negative parent** | [00J — The Author Pays for Their Own Work](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) |
| **Family profile** | [00J Extensibility](./00J_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |
| **Method** | [A26](./00K_A26_FAILURE_TO_SUCCESS_MODEL_CASE_AND_EXTENSIBILITY_v0.1.md) |
| **Status** | design-level success case |

> **Success claim.** Every record remains bound to the proposition it actually establishes. Generation, registry or attestation provenance may remain fully valid while still being insufficient for a stronger rights/authority/enforcement proposition. Downstream action occurs only when current evidence and authority support the exact receiving decision.

## 1. Minimum successful traversal

1. original source/right record is preserved with scope/version/owner;
2. bounded access/use permission remains distinct from downstream entitlement;
3. generation/provenance credential proves only the generation relation it actually establishes;
4. dependency on the original source remains represented or explicit UNKNOWN;
5. downstream registry/licence records remain bounded claims, not automatic superior rights;
6. replicas sharing one upstream root are treated as correlated;
7. final enforcement checks evidence/authority for the exact proposition;
8. unsupported branch yields bounded NO-CONCLUSION/REQUALIFY rather than PAY/BLOCK;
9. legitimate transfer and independent creation positive controls are accepted.

## 2. Existing route

Core:

S1/S5/S7/S9/S11/S12/S14 + applicable T1–T4.

S6/S8 join transfer/delegation; S10 material change; S13 later intervention/history.

No S15 is added.

## 3. Success predicate

\[
G_J=
proposition\ scope\ preserved
\land
lineage/dependence\ preserved
\land
no\ false\ corroboration
\land
decision\ evidence\ sufficient
\land
legitimate\ transfer/independence\ accepted.
\]

## 4. Upward extension

- multi-registry ecosystems;
- publisher→provider→catalogue→licensing/enforcement chains;
- many territories/purposes/policy versions;
- long provenance graphs;
- many locally authentic records descending from one upstream claim.

## 5. Downward extension

One source, one derivative, one provenance record, one transformed claim and one receiving decision are enough.

The success case is simply: the record proves \(q\); the receiver refuses to treat it as proof of \(q^+\) unless an independent valid relation establishes that implication.

## 6. Horizontal extension

- open-source/software licensing;
- dataset permitted-use lineage;
- media syndication;
- model/artifact provenance;
- supply-chain origin/entitlement records;
- technical attestation promoted toward safety/authorization decisions, but only where the same proposition-scope inversion through lineage exists.

## 7. Extension boundary

A forged record is primarily an authenticity case. A pure authority error with no provenance/proposition promotion may fit 00H/P4 better.

## 8. Transfer result

\[
Conf(R_J)\Rightarrow G_J\Rightarrow \neg F_J.
\]

The successful pattern is **valid narrow evidence stays narrow until a justified bridge establishes the stronger proposition**.
