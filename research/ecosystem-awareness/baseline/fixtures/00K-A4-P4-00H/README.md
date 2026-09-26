# Executed ablation — A4 (remove P4) against 00H, "The Quiet Four Thousand"

> **Audit corrections — 26 September 2026:** [A14](./../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md) describes current behavior and regression evidence. Prior execution records below remain historical; current implementations and replay outputs are versioned separately.

## What this is

A **first, partial execution** of one of the six 00K ablations — a deterministic,
rule-level simulation, not a test of any real LLM agent or commercial product.
It encodes 00H's frozen Branch U / Branch G / Branch I fixture (§14 of the v0.5
draft) and 00K's strongest-repair protocol (§4) as runnable Python, then
actually runs it.

## What it tests

Removed principle: **P4 — Qualification-preserving handoff and authority lineage**
Unique ablation anchor: **S8 — Bounded subdelegation and non-amplification**

Four genuine rescue attempts are tried, using only the other five principles
plus one realistic native control, exactly as 00K's protocol requires (no
capability is disabled merely because it happens to share a gate with P4):

1. **P1 alone** (stricter evidence sufficiency)
2. **P5 alone** (revalidate every leaf grant immediately before use)
3. **P6 alone** (detect that a common-root campaign exists, but do nothing with that fact)
4. **A realistic native control** (a per-hour action-rate cap, the kind almost any
   production system already has)

Each is checked against **both** Branch U (unauthorized common-root campaign —
must stay blocked) **and** Branch G (genuinely authorized campaign — must stay
allowed), because a rescue that blocks both is a deny-all in disguise, not a fix.

## Result

**11 of 11 tests pass.** Concretely:

- Route Q (all six principles, including P4) correctly separates Branch U,
  Branch G and Branch I.
- Every rescue attempt using P1, P5, or P6 alone **wrongly executes** Branch U
  — none of them ever inspects root campaign authority, so none of them can
  tell the difference.
- The native rate cap **does** stop Branch U — but the same test shows it
  **also blocks Branch G**, the genuinely authorized campaign, at the exact
  same threshold. It cannot distinguish the two because it was never given
  anything to distinguish them with.
- No TRUE SUBSTITUTE was found among the four attempts tried. Every rescue
  that touched the actual U/G distinction did so by checking
  `RootCampaignAuthority` — i.e., by reconstructing P4.

## What this does and does not establish

**Does:** provide one concrete, re-runnable, falsifiable data point for 00K's
ablation A4, with real code instead of prose argument. Anyone can run
`pytest -v test_ablation_A4.py`, change the rescue functions, and try to make
a rescue pass both Branch U and Branch G without touching root authority.
If someone succeeds, that is a real result against P4's necessity claim —
the code is built to allow that, not to prevent it.

**Does not:**
- test any real agent framework, LLM, or product;
- execute A1, A2, A3, A5 or A6 (the other five 00K ablations);
- prove universal necessity of P4 — only that four specific, plausible
  rescue attempts fail within this fixture;
- constitute a benchmark, certification, or comparative claim of any kind.

## How to extend this

The honest next move is for someone (human or another model) to try to
defeat `test_ablated_native_rate_cap_ALSO_blocks_branch_G` — write a fifth
rescue function in `ablation_A4.py` that passes both Branch U and Branch G
without adding anything resembling `RootCampaignAuthority`. That is exactly
the TRUE SUBSTITUTE case 00K's protocol asks for, and this harness is built
so that attempt is one function and one test away, not a redesign.

## Files

- `ablation_A4.py` — the simulation: Route Q and four ablated rescue attempts.
- `test_ablation_A4.py` — the pytest suite that runs and checks all of it.
- Run with: `pip install pytest && pytest -v test_ablation_A4.py`


## Current corpus-integrated status — 25 September 2026

A later independently-authored successor package was supplied after the original
11-test harness. Its ZIP SHA-256 is
`e7d1caf81e2534fa5b0250f8982fe16fb8e960a273803f151b9ca876dd7c4b63`.

The successor package itself was independently executed before integration:

```text
21 passed in 0.25s
```

To preserve the already-reviewed corpus files and their Git history, the
successor was integrated **additively** rather than by silently replacing the
earlier tests:

- `a2l_strong_peer_decision` is provided by `a2l_strong_peer.py`;
- `test_ablation_A4_v02_additions.py` carries the successor's A2-L, NM and
  four-arm comparison checks;
- `test_ablation_A4_extended.py` remains the independent six-test
  indistinguishability strengthening.

The active corpus fixture family now composes four preserved/additive layers:

- reviewed predecessor: **11** tests;
- reviewed v0.2 successor additions: **10** tests, bringing the successor contract to **21**;
- independent U/G indistinguishability strengthening: **6** tests;
- bounded root-authority / campaign-volume grid: **2** tests.

Current active suite:

```text
29 tests
```

The earlier duplicate alignment file created during integration was removed once the already-existing reviewed `test_ablation_A4_v02_additions.py` was confirmed to carry the same successor checks. The reviewed `ablation_A4.py` was also restored verbatim; A2-L remains isolated in `a2l_strong_peer.py`. This keeps one executable fixture family while preserving provenance of every layer.


## Serious-repair hardening — minimal authority basis versus full lineage

A later additive hardening layer is maintained in:

- [`p4_strong_repairs.py`](./p4_strong_repairs.py)
- [`test_p4_strong_repairs.py`](./test_p4_strong_repairs.py)
- [00K-A10 — P4 Minimal Authority Basis & Lineage Refinement](../../00K_A10_P4_MINIMAL_AUTHORITY_BASIS_AND_LINEAGE_REFINEMENT_v0.1.md)

This layer adds **47** tests and raises the active A4 surface from **29** to **76**.

The important result is not only a larger count. The strong repair search finds that a
full historical root→leaf delegation chain is **not necessary** for 00H when a
legitimate owner-side PDP, scoped capability or maker-checker produces a current
decision-sufficient permit bound to the actual campaign/action set.

Therefore the current A4 conclusion is refined:

- leaf RBAC, rate/amount caps, risk gates, static allow-lists and non-owner approval
  remain FAILED SUBSTITUTES;
- full lineage remains a valid SEMANTIC RECONSTRUCTION;
- scoped capability and legitimate owner approval are alternative P4 implementations;
- an opaque scoped PDP permit passes U/G/I/NM without exposing full delegation history;
- the minimal invariant still required by the matched U/G fixture is a **current,
  decision-sufficient, non-amplifying authority qualification**, not necessarily a
  complete historical lineage at the relying component.

Local execution of the additive serious-repair layer:

```text
47 passed
```

Current A4 total:

```text
76 tests
```
