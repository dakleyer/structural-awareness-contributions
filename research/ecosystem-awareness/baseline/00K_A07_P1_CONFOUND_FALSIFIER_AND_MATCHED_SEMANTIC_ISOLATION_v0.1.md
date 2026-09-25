# 00K-A07 — P1 Confound Falsifier & Matched-Semantic Isolation — v0.1

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Principle:** P1 — qualified determination / evidence→proposition→decision sufficiency  
**Scenario:** [00J — Rights-Provenance Inversion](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md)  
**Status:** executed methodological correction + strengthened symbolic repair search  
**Date:** 25 September 2026

> **Finding.** The original small A1 negative/positive pair was not sufficient by itself to isolate P1 necessity because the two branches also differed in issuer/source and record class. A P1-blind source-authority rule can therefore reject the negative branch and accept the positive branch. The strengthened A1 harness preserves that as a methodological falsifier and adds a corrected matched-semantic pair in which issuer, record class, signature, freshness and authority context are equal. On that corrected pair, serious P1-blind repairs do not separate the branches; the strongest passing peer succeeds by explicitly binding evidence semantics to the decision proposition, i.e. **SEMANTIC RECONSTRUCTION of P1**.

---

## 1. Why the original pair was confounded

The first A1 harness compared:

- negative: a valid generation-provenance record from `SRC-M1`;
- positive: a rights-grant record from `RIGHTS-OWNER`.

That is useful as a 00J story, but it changes more than P1's target variable. A rule that never evaluates the evidence→proposition relation can still do:

```text
if issuer == RIGHTS_OWNER:
    ENFORCE
else:
    NO_CONCLUSION
```

and pass that pair.

The new test `test_original_naive_pair_is_confounded_by_source_authority` deliberately demonstrates this **TRUE SUBSTITUTE for the naive pair**.

This does **not** falsify P1 as a principle. It falsifies the claim that the old pair alone isolated P1.

---

## 2. Corrected matched-semantic pair

The corrected isolation freezes equal:

- issuer/source;
- signature validity;
- freshness;
- record class;
- number of records;
- authority context;
- transport/provenance completeness.

The only material difference is the semantic proposition that the valid record actually supports:

- negative: `GENERATED_BY_MODEL_M1` (and other narrower valid propositions);
- positive: `RIGHT_TO_ENFORCE_AGAINST_AUTHOR`.

The decision remains the same: may the system enforce a licensing/payment/blocking claim against the author?

This removes the issuer/type shortcut and asks the P1 question directly.

---

## 3. Serious repair attempts

The strengthened harness tests:

1. **trusted issuer allow-list**;
2. **complete provenance / perfect record preservation**;
3. **generic signed-assertion schema allow-list**;
4. **confidence/risk scoring** from signature, freshness, source trust and availability;
5. **independent-record quorum**;
6. **human approval without a new rights fact**;
7. **source-reputation thresholding**;
8. **confidence-threshold sweeps**;
9. **replication of semantically wrong but independently valid records**; and
10. a strong peer with an explicit **evidence-semantics → allowed-decision policy matrix**.

The first nine mechanisms are allowed to be strong. They fail because they can improve authenticity, freshness, confidence, provenance or review quality without establishing that the evidence supports the proposition required by the receiving decision.

The policy matrix passes, but only by encoding the operational equivalent of:

```text
what proposition does this evidence establish?
is that proposition sufficient for this decision?
```

That is classified as **SEMANTIC RECONSTRUCTION of P1**, not as a proprietary EA mechanism.

---

## 4. Execution result

The prior A1 harness + bounded grid contributed **13** tests.

The new falsification-first / serious-repair layer adds **29** tests.

**Current A1 total: 42/42 symbolic tests.**

Local pre-publication execution of the new layer:

```text
29 passed
```

The repository CI campaign is configured to require the updated A1 total before the aggregate gate can pass.

---

## 5. Current P1 disposition

- **TRUE SUBSTITUTE for the old naive pair:** **YES** — source-authority-only.
- **Old pair accepted as P1 necessity isolation:** **NO**.
- **Corrected matched-semantic isolation:** **YES**.
- **TRUE SUBSTITUTE in the corrected serious-repair surface:** **NONE FOUND**.
- **Strongest passing repair:** evidence-semantics / proposition / decision policy contract.
- **00K classification:** **SEMANTIC RECONSTRUCTION of P1**.
- **Evidence level:** deterministic symbolic fixture only.

This is a stronger result than simply increasing a test count because the method first found and preserved a counterexample to the earlier isolation.

---

## 6. Falsifier

P1's current necessity claim must be reopened if a repair can, under the corrected matched branch pair:

1. reject the narrower-but-valid evidence on the enforcement decision;
2. accept the legitimate enforcement proposition;
3. preserve unknown/unsupported conclusions rather than deny everything;
4. do so without an evidence→proposition→decision sufficiency relation or operational equivalent.

Such a repair is a **TRUE SUBSTITUTE** and counts against P1 necessity.
