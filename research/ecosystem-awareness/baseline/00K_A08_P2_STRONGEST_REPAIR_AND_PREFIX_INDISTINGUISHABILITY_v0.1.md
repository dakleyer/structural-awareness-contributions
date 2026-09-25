# 00K-A08 — P2 Strongest-Repair & Prefix-Indistinguishability Audit — v0.1

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Principle:** P2 — bounded unresolved effort and viable oversight  
**Scenario:** [00E — 100 Million Tokens](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md)  
**Status:** serious-repair hardening executed  
**Date:** 25 September 2026

> **Finding.** The first A2 harness already showed that unbounded search, perfect UNKNOWN preservation and perfect handoff can still consume capacity, while a crude timeout can destroy the positive branch. The strengthened A2 test now makes the boundary harder: negative and positive branches share an identical observation prefix until the final useful step. Across that matched prefix, memoryless observation-only policies cannot solve both branches. Repairs based on fixed TTLs, no-progress circuit breakers, parallel fan-out, cached defaults, external schedulers and bounded probes either miss a still-reachable positive resolution, exceed the useful horizon, false-close, or succeed only by introducing the P2 invariant in another place.

---

## 1. Corrected hard branch pair

For a declared horizon `H`:

- **negative branch:** steps 1…H remain unresolved/non-decision-relevant;
- **positive branch:** steps 1…H−1 are identical to the negative branch and only step H supplies resolving evidence.

Before step H the two branches are observationally identical.

This removes easy “pattern recognition” shortcuts. Any deterministic policy that stops before H on the negative prefix also stops before the positive branch's still-reachable resolution. A policy that continues beyond H violates the declared horizon/capacity condition.

The branch-correct solution therefore needs a stopping/continuation relation to the finite horizon, decision value or an equivalent bounded fallback. That is precisely the P2 semantic invariant under test.

---

## 2. Serious repair attempts

The additive harness tests the following conventional alternatives:

1. **fixed TTL / max-step / token quota**;
2. **no-progress circuit breaker**;
3. **parallel fan-out with bounded rounds**;
4. **cached/default decision after waiting**;
5. **externally managed scheduler deadline**;
6. **bounded reversible-probe posture**;
7. **observation-only memoryless policies**, exhaustively enumerated over the reduced observation alphabet; and
8. **horizon-aware policy** as the strong peer.

The point is not that these mechanisms are bad. Several are exactly the kind of mechanism a strong production system should use.

The classification question is whether they eliminate P2 or implement it.

---

## 3. Execution result

The serious-repair layer adds **45 passing tests**.

Local pre-publication run:

```text
45 passed
```

Together with the existing A2 base + grid layer (**13**), the current P2 harness is:

> **58/58 symbolic tests**

### Observed classifications

- timeout before the still-reachable positive resolution → **FAILED SUBSTITUTE**;
- timeout after useful horizon → **FAILED SUBSTITUTE**;
- cached/default closure without resolving evidence → **FAILED SUBSTITUTE / false closure**;
- insufficient parallel fan-out → **FAILED SUBSTITUTE**;
- fixed TTL at the declared horizon → **SEMANTIC RECONSTRUCTION of P2**;
- no-progress breaker tuned to the declared viable horizon → **SEMANTIC RECONSTRUCTION of P2**;
- externally enforced scheduler deadline → **SEMANTIC RECONSTRUCTION at architecture level**;
- bounded experiment/probe selected through a finite horizon rule → **SEMANTIC RECONSTRUCTION of P2**;
- horizon-aware strong peer → **SEMANTIC RECONSTRUCTION of P2**.

No TRUE SUBSTITUTE is found in this serious-repair surface.

---

## 4. Exhaustive reduced-policy check

For the matched late-resolution pair, the harness enumerates every **memoryless** policy over the reduced observation alphabet:

- unresolved/non-resolving observation;
- resolving observation;

with actions:

- CONTINUE;
- EXECUTE;
- NO_CONCLUSION.

No memoryless observation-only policy passes both negative and positive branches.

Once the policy is allowed to use the declared horizon/step state, a passing policy exists:

```text
if resolves:
    EXECUTE
elif step == useful_horizon:
    NO_CONCLUSION
else:
    CONTINUE
```

That result does not prove P2 universally. It does show that in the isolated matched-prefix fixture, the missing discriminator is not “better search content” but a bounded decision relation to capacity/horizon.

---

## 5. Current P2 disposition

- **TRUE SUBSTITUTE found:** no, within the serious repair surface.
- **Strong passing peers found:** yes.
- **How they pass:** by explicit finite budget/deadline/patience/probe rules tied to decision viability.
- **00K classification:** **SEMANTIC RECONSTRUCTION of P2**.
- **Evidence class:** deterministic symbolic fixture.

---

## 6. Falsifier

P2's bounded necessity claim must be reopened if a repair can, under the matched-prefix family:

1. terminate the indefinitely unresolved branch before useful capacity expires;
2. still permit a resolution that arrives at any allowed step through the declared horizon;
3. avoid timeout/default false closure and permanent HOLD;
4. do so without a finite effort bound, decision-relevance stopping condition, response-horizon rule, bounded fallback or operational equivalent.

Such a mechanism is a **TRUE SUBSTITUTE** and counts against P2 necessity.
