# 00K-A10 — P4 Minimal Authority Basis & Lineage Refinement — v0.1

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Principle under review:** P4 — qualification-preserving handoff / authority lineage  
**Scenario:** [00H — The Quiet Four Thousand](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md)  
**Status:** serious-repair hardening executed; principle wording refinement identified  
**Date:** 25 September 2026

> **Finding.** The hardened 00H test continues to support a **minimal P4 invariant**: the acting/relying component needs a current, decision-sufficient, non-amplifying authority basis for the composed action. However, the test does **not** establish that a full historical root→leaf delegation chain must always be exposed to that component. An opaque but legitimate owner-side Policy Decision Point (PDP) can pass U/G/I/NM by returning a scoped, current authorization attestation bound to the actual campaign/action set, without returning the delegation history. Therefore **full lineage preservation is not necessary in 00H; decision-sufficient authority qualification is.**

This is a refinement, not a disappearance of the principle.

---

## 1. Why this hardening is stronger than the earlier rate-limit test

The existing A4 harness already showed:

- leaf-validity/RBAC alone cannot distinguish U/G;
- campaign detection alone cannot distinguish U/G;
- rate/aggregate controls can block U but also block G;
- explicit root/delegation lineage passes U/G/I/NM;
- U and G are identical on the declared P4-blind observable surface.

The new layer asks a harder question:

> must the relying component actually reconstruct the **history/chain**, or is some other current authority-bearing mechanism sufficient?

That is a real attempt to weaken P4.

---

## 2. Serious alternatives tested

The additive Python layer tests:

1. leaf RBAC / local grants;
2. non-owner human approval;
3. campaign execute-all / block-all policies;
4. rate limits across multiple thresholds;
5. aggregate-amount limits across multiple thresholds;
6. risk-score thresholds;
7. static campaign allow-lists;
8. **owner-side opaque PDP** returning a current scoped permit;
9. **scoped capability token** with campaign/action/amount caveats;
10. **maker-checker** where the checker is or is not a legitimate authority owner;
11. invalid/stale permit;
12. wrong-campaign permit;
13. under-scoped permit; and
14. an explicit finite-policy indistinguishability check over the P4-blind U/G signature.

The additive serious-repair layer passes **47/47** tests locally.

Together with the active prior A4 surface (**29**), the current A4 harness is:

> **76/76 symbolic tests**

---

## 3. Key result: a strong PDP peer passes without exposing full lineage

The owner-side PDP receives the campaign/action request and returns only a scoped current decision/permit:

```text
issuer
campaign_id
max_actions
max_amount
valid
```

The relying component does **not** receive:

- a root→leaf delegation history;
- historical intervention chain; or
- the internal policy proof by which the owner reached the decision.

Yet the scoped permit is sufficient to:

- block U;
- allow G;
- leave I local;
- avoid escalating NM;
- reject stale/invalid/wrong-campaign/under-scoped permits.

This means:

> **full delegation-history preservation is not necessary for the 00H decision.**

If P4 is interpreted literally as “the receiver must always retain/reconstruct the complete authority lineage/history,” that formulation is too strong for this fixture.

---

## 4. What remains necessary in the fixture

The opaque PDP does not make authority disappear. It supplies a different authority-bearing object.

U and G are deliberately identical on:

- materiality;
- campaign identity;
- leaf validity;
- action count;
- aggregate amount;
- risk score;
- timing.

The required outcomes are opposite.

Therefore a policy using only those P4-blind features cannot deterministically separate the branches.

The passing PDP/capability/maker-checker peers all introduce a current decision-sufficient relation of the form:

```text
legitimate authority source
    -> this campaign/action set
    -> this purpose/scope/time/amount
    -> PERMIT / NOT PERMIT
```

That is the **minimal invariant actually supported by 00H**.

---

## 5. Classification

### Failed substitutes

Leaf RBAC, rate/amount caps, risk scoring, static allow-lists and non-owner human approval either:

- false-execute U;
- false-block G; or
- treat U/G identically.

### Passing strong peers

- full A2-L root/delegation lineage;
- scoped capability/caveat;
- legitimate maker-checker approval bound to the campaign;
- opaque owner-side PDP permit.

### Interpretation

The first is full-lineage **SEMANTIC RECONSTRUCTION**.

The latter three show that the implementation surface is broader than full lineage. For the current test programme the correct conclusion is:

> **P4 REFINEMENT REQUIRED: preserve a receiver-verifiable, decision-sufficient, current authority qualification that prevents amplification. Full historical delegation lineage is one implementation, not a universal requirement established by 00H.**

The PDP result is **not** treated as a TRUE SUBSTITUTE for the minimal authority-qualification invariant, because it still supplies exactly the current scoped authority fact that separates U from G. It **is** a counterexample to the stronger claim that full lineage/history must always be reconstructed at the relying component.

---

## 6. Proposed operational wording for the 00K test abstraction

Current P4 should be read, for ablation purposes, as:

> **P4 — Qualification-preserving authority basis.** When authority/representation state crosses participants or systems, the relying decision must retain or obtain a current, receiver-verifiable qualification sufficient to establish the legitimate source, purpose/scope/time and non-amplification limits of the action. This may be satisfied by preserved delegation lineage **or by an authoritative scoped attestation/capability that is itself sufficient for the receiving decision**. Full historical lineage is required only where the decision, audit, challenge or repair semantics materially depend on it.

This is a refinement of the 00K operational principle family. It does not silently amend the frozen source principles in document 02.

---

## 7. Falsifier

The minimal P4 claim must be reopened if a repair can pass matched U/G/I/NM while:

1. never obtaining any current authority-bearing fact that differs between U and G;
2. never receiving a scoped permit/capability/owner decision;
3. never reconstructing authority lineage;
4. never using an operationally equivalent authority qualification; and
5. still distinguishing unauthorized from authorized composed action without deny-all.

Such a mechanism would be a genuine TRUE SUBSTITUTE for the minimal P4 invariant.
