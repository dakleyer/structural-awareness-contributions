# 00K-FORMAL — Relative Independence Certificate

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](../../00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Formal proof note:** [00K-A16 — Formal Relative Independence Proof](../../00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md)

This directory contains a **machine-checkable finite-model certificate** for the
relative logical independence of the six current operational principles.

It does not replace the executable ablation harnesses and is not counted among
the 379 symbolic ablation tests.

## Claim checked

Let:

```text
T = {P1, P2, P3, P4, P5, P6}
```

The certificate checks, for every `Pi`, that there exists a witness trace `Mi`
such that:

```text
Mi satisfies every Pj for j != i
Mi violates Pi
```

Therefore:

```text
T \ {Pi} does not entail Pi
```

for each `i = 1..6`.

That is the standard model-theoretic criterion for **independence of an axiom
family relative to the declared semantics/model class**.

## Run

```bash
python formal_independence_certificate.py
```

Expected terminal line:

```text
00K formal relative-independence certificate: PASS (6/6 countermodels)
```

## Boundary

This proves independence only for the formalized P1–P6 predicates and declared
00K witness class. It does not prove statistical independence, universal
minimality for every possible architecture, or that no alternative
re-formulation can combine/split the same semantic properties.


## P5 matched-pair proof supplement

[P5 blind-signature proof](./p5-blind-signature/README.md) is a compact 18-test illustration of the projection-indistinguishability lemma used by A16. It is deliberately outside the canonical P5 harness and is **not counted** in the 379-test campaign.
