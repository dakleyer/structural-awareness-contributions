# 00K-A05 — P6 Confound Falsifier & Isolation Note — v0.1

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Principle:** P6 — no local-to-ecosystem promotion / silent substitution  
**Original scenario:** [00G — Ciber Napoleon Goes to Russia](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md)  
**Status:** executed methodological correction + isolated symbolic re-tests  
**Date:** 25 September 2026

> **Finding.** The unmodified 00G false-frame / genuine-regime-change pair is **not sufficient by itself to establish P6 necessity**, because the two branches differ in more than evidence independence: the genuine-change branch also carries applicable mission-transition authority. A P6-blind authority-only rule can therefore separate that pair. The 00K method caught this as a TRUE SUBSTITUTE rather than protecting the intended conclusion.

---

## 1. Why this matters

The original P6 argument was:

- Branch F: repeated/correlated claims must not become ecosystem truth;
- Branch G: genuinely independent evidence plus legitimate authority must permit transition.

That is a good safety scenario, but a weak **P6 isolation** because two variables move together:

1. source/evidence independence; and
2. applicable transition authority.

A necessity test must not credit P6 for a distinction that P4/authority state can already make.

---

## 2. Falsification-first run — A6a / 00G

Executable fixture:

[**00K-A6a — P6 / 00G falsification-first execution**](./fixtures/00K-A6a-P6-00G/README.md)

The deliberately simple P6-blind repair is:

```text
if transition_authority_applicable:
    EXECUTE
else:
    DENY
```

It never inspects evidence independence.

Under the original F/G distinction:

- F has no applicable transition authority → DENY;
- G has applicable transition authority → EXECUTE.

Result:

```text
10 passed
TRUE SUBSTITUTE found for the unmodified F/G pair
```

This does **not** falsify P6 as a principle. It falsifies the claim that the original unmodified F/G pair, by itself, isolates P6 necessity.

---

## 3. Corrected matched-authority P6 fixture — canonical A6

The existing canonical executable P6 fixture already contains the correct repair to this confound:

[**00K-A6 — matched-authority P6 / 00G**](./fixtures/00K-A6-P6-00G/README.md)

It explicitly freezes:

- the **same current transition authority** in F and G;
- the same agent count;
- the same signatures;
- the same freshness;
- the same confidence;
- the same candidate frame.

The only material difference is source dependence:

- **F:** five authenticated claims inherit one source;
- **G:** five authenticated claims derive from three materially independent sources.

Current suite:

```text
17/17
```

P6-blind repairs fail:

- identity/message quorum;
- confidence threshold;
- provenance preservation without composition semantics;
- human majority;
- deny-all.

A strong non-EA source-independence peer passes F/G, but only by explicitly computing materially independent source paths. Under 00K this is **SEMANTIC RECONSTRUCTION of P6**.

No TRUE SUBSTITUTE is found in the tested matched-authority repair surface.

---

## 4. Independent composition isolation — A6b / 00F

A second fixture checks that the result is not peculiar to Napoleon/source voting:

[**00K-A6b — P6 / 00F shared-resource composition isolation**](./fixtures/00K-A6b-P6-00F/README.md)

Here authority, freshness and local determination remain equal. The discriminant is cross-participant **resource-time compatibility**.

- Hazard: all local postures are valid, but opposed uses overlap on the same corridor/time.
- Positive control: same actors and local validity, but no resource-time conflict.

Result:

```text
11/11
```

Local-only evidence and “no UNKNOWN” execute the hazard. Blanket mutex/static priority suppresses the hazard but fails the compatible positive branch. A strong compatibility peer passes by explicitly computing cross-participant compatibility — another implementation of the P6 composition/non-substitution invariant.

---

## 5. Scientific disposition

The correct P6 evidence record is therefore:

| Test surface | Result | Interpretation |
|---|---|---|
| Original unmodified 00G F/G | **TRUE SUBSTITUTE found** | confounded for P6 necessity; authority-only rule separates branches |
| Corrected matched-authority 00G A6 | **17/17; no TRUE SUBSTITUTE found** | supports P6 semantic necessity within isolated source-dependence fixture |
| Independent 00F A6b composition isolation | **11/11; no TRUE SUBSTITUTE found** | corroborates P6 composition invariant on a different failure mechanism |

This is stronger methodology than simply reporting a clean pass. The test programme produced a result **against its own first fixture**, corrected the confound, and only then retained the principle-level claim.

---

## 6. Claim boundary

The current bounded claim is:

> Within the two isolated symbolic fixtures tested here, branch-correct repairs require an explicit cross-participant composition/non-substitution rule: source-independence composition in matched-authority 00G and resource-time compatibility composition in 00F. The original unmodified 00G F/G pair does not establish that result by itself.

This does not establish universal P6 minimality, and a future TRUE SUBSTITUTE on either isolated fixture must reopen the claim.
