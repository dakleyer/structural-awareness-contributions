# 00J — Case-Study Extensibility Profile — v0.1

| | |
|---|---|
| **Family** | Provenance-Scope Inversion into Unsupported Downstream Decision |
| **Minimum instantiation** | [00J — The Author Pays for Their Own Work](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) |
| **Extensibility method** | [A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) · [A26 success conversion](./00K_A26_FAILURE_TO_SUCCESS_MODEL_CASE_AND_EXTENSIBILITY_v0.1.md) |
| **Success Model Case** | [Proposition-Scoped Provenance](./00J_SUCCESS_MODEL_CASE_PROPOSITION_SCOPED_PROVENANCE_v0.1.md) |
| **Status** | first-pass structural family profile |

> **Family claim.** Copyright/payment is one vivid enforcement consequence. The structural case is that a valid record proving proposition \(q\) is promoted through broken lineage, correlation or authority substitution into a stronger proposition \(q^+\) that the record does not establish, and \(q^+\) controls a downstream decision.

## 1. Kernel

\[
K_J=
\langle
valid\ narrow\ record,\;
source/lineage\ relation,\;
downstream\ transformation,\;
stronger\ proposition,\;
receiving\ enforcement/decision
\rangle.
\]

Failure:

\[
F_J=
valid(record,q)
\land
use(record,q^+)
\land
q\not\Rightarrow q^+
\land
decision(q^+).
\]

Replication/correlation and absent authority can harden the case but are not required for the minimum semantic inversion.

Primary witness: **P1**; **P4/P6** join authority/composition branches.

## 2. Inherited requirement route

Core surfaces:

**S1/S5/S7/S9/S11/S12/S14**, with T1–T4 as applicable.

Additional:

- S6/S8 for access/delegation transfer;
- S10 for material change;
- S13 for later intervention/history.

The family retains positive controls for legitimate transfer and independent creation; universal blocking is not a valid pass.

## 3. Upward / vertical extensibility

**Strong extensions:**

- many content/rights registries and marketplaces;
- multi-stage publisher → model/provider → catalogue → licensing/enforcement chains;
- replicated metadata across several organizations;
- multiple rights principals, territories, purposes and policy versions;
- long provenance graphs where many authentic records derive from one upstream claim.

The graph may grow while each record remains locally valid.

## 4. Downward extensibility

The family can shrink to:

1. one source object \(W\);
2. one derived object \(D\);
3. one valid generation/provenance record;
4. one downstream claim;
5. one decision that treats the record as proof of a stronger proposition.

A single transformation and one bad proposition jump is enough.

No large registry or multi-agent system is necessary.

## 5. Horizontal extensibility

### Strong rights/provenance extensions

- software/open-source licence lineage;
- dataset licensing / permitted-use lineage;
- media/content syndication;
- model/artifact provenance where a technical generation record is confused with ownership or permitted downstream use;
- supply-chain documentation where a record valid for origin/version is promoted into an unsupported entitlement or enforcement claim.

### Broader candidate neighbour

A similar pattern can appear when:

- an attestation proves “component X passed test Y”;
- a receiver promotes that into “system Z is safe/authorized for action A”.

This is structurally close, but admission as 00J requires the same **proposition-scope inversion through lineage**. If the issue is purely current authority with no provenance/proposition promotion, 00H/P4 may be the cleaner family.

## 6. Boundary

Out of family:

- a forged record whose problem is authenticity rather than proposition scope;
- a simple copyright disagreement with no machine-readable evidence promotion;
- a valid broader right that actually entails the final decision;
- a false claim created directly with no relevant provenance/lineage transformation.

## 7. Conformance transfer

For every admitted extension:

\[
F_J\Rightarrow
(\neg P1\lor\neg P4\lor\neg P6)
\]

depending on whether the decisive defect is proposition fit, absent authority or correlated/non-substituting composition.

A23 supplies sufficiency of the relevant S/T route for those P invariants.

Therefore an in-family requirements-conforming implementation cannot reach the same unsupported provenance-to-enforcement inversion, while still being required to pass legitimate-transfer and independent-work controls.


## Success-case route

The failure-family profile above is paired with the positive [**Proposition-Scoped Provenance**](./00J_SUCCESS_MODEL_CASE_PROPOSITION_SCOPED_PROVENANCE_v0.1.md) Success Model Case. The success case keeps the same kernel and inherited S/T route, defines the positive bounded disposition, and applies the same upward/downward/horizontal admission boundary without introducing new canonical requirements.
