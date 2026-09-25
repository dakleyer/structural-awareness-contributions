# P5 blind-signature proof supplement

**Parent:** [00K-A5 — P5 / 00I](../README.md)  
**Formal proof:** [00K-A16 — P1–P6 relative independence](../../../00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md)  
**Status:** compact mathematical illustration; **not counted** in the 47 canonical P5 tests or the 379 registered 00K campaign tests

## Claim

P5 requires action-time access to a current material condition when a previously issued grant can remain technically valid after that condition changes.

The matched pair is:

| Branch | material | token valid | scope match | elapsed | condition true now | Correct disposition |
|---|:---:|:---:|:---:|---:|:---:|---|
| STALE | 1 | 1 | 1 | 2400 s | **0** | REQUALIFY |
| FRESH | 1 | 1 | 1 | 2400 s | **1** | EXECUTE |

STALE and FRESH are identical on the P5-blind projection:

~~~text
(material, token_valid, scope_match, elapsed_time)
~~~

but require different outputs.

Therefore, by projection indistinguishability, no deterministic policy using only that blind projection can be correct on both branches.

## Why this is useful

This is a compact proof of the same separation used in A16:

~~~text
π(STALE) = π(FRESH)
O(STALE) ≠ O(FRESH)

therefore no deterministic f can satisfy:
f(π(STALE)) = O(STALE)
and
f(π(FRESH)) = O(FRESH)
~~~

The legitimate repair is a current-state query at action time.

The proof also narrows P5: a full historical change log is not required. A current, verifiable material condition is enough for this matched pair.

## Relation to the canonical P5 harness

The canonical [A11 material-basis audit](../../../00K_A11_P5_EXHAUSTIVE_MATERIAL_BASIS_ABLATION_v0.1.md) is stronger operationally. It enumerates all 16 subsets of the declared four-field material basis and shows that only complete material-basis coverage survives every single-field mutation while preserving continuity.

This supplement is therefore retained for **mathematical readability**, not to inflate the canonical execution count.

## Reproduction

~~~bash
python -m pytest -q
~~~

Expected:

~~~text
18 passed
~~~

The supplied package was independently executed on 25 September 2026 with **18/18 passing**.
